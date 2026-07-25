#[compute]
#version 450

// ============================================================
// VFM Biot-Savart Compute Shader — SCVC v2.0
// ============================================================
// Replaces O(N²) CPU GDScript Biot-Savart loop with GPU parallelism.
//
// Each workgroup item computes the Biot-Savart induced velocity
// at ONE ring segment, from ALL other segments + ALL point vortices.
//
// Physics reference:
//   v(r) = (kappa/4π) * ∮ (ds × r̂) / r²          [Biot-Savart]
//   Desingularized: core_a cuts off 1/r divergence
//   c.f. Schwarz 1985, Tsubota 2000 (quantum turbulence)

layout(local_size_x = 64, local_size_y = 1, local_size_z = 1) in;

// ---- Input Buffers (readonly) ----

// Buffer 0: All ring segment world positions (flattened, vec3 per segment)
layout(set = 0, binding = 0, std430) readonly buffer SegPositions {
    float seg_positions[];  // length = total_segments * 3
};

// Buffer 1: Ring index per segment: seg_ring_map[i] = which ring segment i belongs to
layout(set = 0, binding = 1, std430) readonly buffer SegRingMap {
    uint seg_ring_map[];  // length = total_segments
};

// Buffer 2: Ring metadata: [seg_start, seg_count] per ring (uvec2 packed)
layout(set = 0, binding = 2, std430) readonly buffer RingOffsets {
    uint ring_offsets[];  // length = total_rings * 2, pairs of [start, count]
};

// Buffer 3: Ring radii
layout(set = 0, binding = 3, std430) readonly buffer RingRadii {
    float ring_radii[];  // length = total_rings
};

// Buffer 4: Point vortex positions (vec3 per vortex)
layout(set = 0, binding = 4, std430) readonly buffer VortexPositions {
    float vortex_positions[];  // length = total_vortices * 3
};

// ---- Output Buffer (readwrite) ----

// Buffer 5: Computed Biot-Savart velocities (vec3 per segment)
layout(set = 0, binding = 5, std430) buffer BSVelocities {
    float bs_velocities[];  // length = total_segments * 3
};

// ---- Uniforms (push constants) ----

layout(push_constant, std430) uniform Params {
    uint total_segments;
    uint total_rings;
    uint total_vortices;
    float kappa;
    float core_a;
    float self_core_factor;
} pc;

// ---- Helper: read vec3 from float buffer at index ----
vec3 read_vec3(int idx) {
    int base = idx * 3;
    return vec3(
        seg_positions[base],
        seg_positions[base + 1],
        seg_positions[base + 2]
    );
}

vec3 read_vortex_pos(int idx) {
    int base = idx * 3;
    return vec3(
        vortex_positions[base],
        vortex_positions[base + 1],
        vortex_positions[base + 2]
    );
}

void write_velocity(int idx, vec3 v) {
    int base = idx * 3;
    bs_velocities[base]     = v.x;
    bs_velocities[base + 1] = v.y;
    bs_velocities[base + 2] = v.z;
}

// ---- Core: Biot-Savart desingularized kernel ----
// v = (kappa/4π) * (rA × rB) * (|rA|+|rB|) / [ |rA||rB|*(|rA||rB|+rA·rB) + a² ]
vec3 biot_savart_kernel(vec3 eval_point, vec3 seg_start, vec3 seg_end, float gamma, float a) {
    vec3 rA = eval_point - seg_start;
    vec3 rB = eval_point - seg_end;
    float rA_len = length(rA);
    float rB_len = length(rB);

    if (rA_len < 1e-4 || rB_len < 1e-4) {
        return vec3(0.0);
    }

    vec3 rA_cross_rB = cross(rA, rB);
    float denom = rA_len * rB_len * (rA_len * rB_len + dot(rA, rB)) + a * a;

    if (denom < 1e-4) {
        return vec3(0.0);
    }

    float prefactor = gamma / (4.0 * 3.14159265359);
    float numerator = rA_len + rB_len;

    vec3 result = rA_cross_rB * (prefactor * numerator / denom);

    // Guard against numerical explosion
    if (length(result) > 1e6 || isnan(result.x) || isnan(result.y) || isnan(result.z)) {
        return vec3(0.0);
    }
    return result;
}

// ---- Main kernel ----
void main() {
    uint seg_idx = gl_GlobalInvocationID.x;
    if (seg_idx >= pc.total_segments) {
        return;
    }

    vec3 eval_point = read_vec3(int(seg_idx));
    uint ring_idx = seg_ring_map[seg_idx];

    // Ring range
    uint ring_base = ring_idx * 2u;
    uint seg_start = ring_offsets[ring_base];
    uint seg_count = ring_offsets[ring_base + 1u];
    float my_radius = ring_radii[ring_idx];

    // Self-induction radius
    float self_a = pc.core_a + my_radius * pc.self_core_factor;

    vec3 v_total = vec3(0.0);

    // ---- SELF-INDUCTION: same ring ----
    for (uint j = seg_start; j < seg_start + seg_count; j++) {
        if (j == seg_idx) continue;
        uint j_next = (j == seg_start + seg_count - 1u) ? seg_start : (j + 1u);
        vec3 s_start = read_vec3(int(j));
        vec3 s_end   = read_vec3(int(j_next));
        v_total += biot_savart_kernel(eval_point, s_start, s_end, pc.kappa, self_a);
    }

    // ---- CROSS-INDUCTION: all OTHER rings' segments ----
    // Loop over ALL segments; skip segments in my own ring
    for (uint k = 0u; k < pc.total_segments; k++) {
        // Fast skip: same ring
        if (seg_ring_map[k] == ring_idx) continue;

        uint k_next;
        // Find k's ring
        uint rk = seg_ring_map[k];
        uint rk_base = rk * 2u;
        uint rk_end = ring_offsets[rk_base] + ring_offsets[rk_base + 1u];

        if (k + 1u < rk_end) {
            k_next = k + 1u;
        } else {
            k_next = ring_offsets[rk_base]; // wrap to ring start
        }

        vec3 s_start = read_vec3(int(k));
        vec3 s_end   = read_vec3(int(k_next));
        v_total += biot_savart_kernel(eval_point, s_start, s_end, pc.kappa, pc.core_a);
    }

    // ---- POINT VORTEX INDUCTION ----
    for (uint vi = 0u; vi < pc.total_vortices; vi++) {
        vec3 vp = read_vortex_pos(int(vi));
        vec3 r_vec = eval_point - vp;
        float r = length(r_vec);
        if (r < 0.01) continue;
        vec3 r_hat = r_vec / r;
        // v_point = kappa / (2π * (r + core_a)) * UP × r_hat
        float factor = pc.kappa / (6.28318530718 * (r + pc.core_a));
        vec3 v_point = cross(vec3(0.0, 1.0, 0.0), r_hat) * factor;
        v_total += v_point;
    }

    write_velocity(int(seg_idx), v_total);
}
