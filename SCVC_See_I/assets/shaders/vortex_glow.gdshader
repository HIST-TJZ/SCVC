shader_type spatial;
render_mode blend_mix, depth_draw_opaque, cull_disabled;

// Vortex tube glow shader
// Samples a radial profile to show vortex core brightness

uniform sampler2D profile_tex : source_color, filter_linear_mipmap;
uniform float tube_radius : hint_range(0.0, 5.0) = 0.15;
uniform vec3 core_color : source_color = vec3(1.0, 0.6, 0.15);
uniform vec3 glow_color : source_color = vec3(1.0, 0.2, 0.05);
uniform float intensity : hint_range(0.0, 5.0) = 1.5;

void fragment() {
    // UV.x goes along tube, UV.y wraps around
    // Compute radial distance from cylinder axis
    // For CylinderMesh, UV.y * 2 - 1 gives position on cross-section
    float radial_pos = abs(UV.y - 0.5) * 2.0; // 0 at surface, 1 at center

    // Sample vortex profile: f(r) ~ 0 at core, ~1 at infinity
    // Invert: brightness where f is small (vortex core region)
    float profile = texture(profile_tex, vec2(radial_pos, 0.0)).r;

    // Vortex core is bright where |psi| is small
    float core_factor = 1.0 - profile;
    
    // Exponential glow falloff from core
    float glow = exp(-radial_pos * 4.0) * core_factor;
    
    // Edge enhancement for vortex boundary
    float edge = profile * (1.0 - profile) * 4.0;
    
    vec3 col = mix(glow_color, core_color, glow) + core_color * edge * 0.5;
    float alpha = (glow * 0.8 + edge * 0.6) * intensity;
    
    ALBEDO = col;
    ALPHA = clamp(alpha, 0.0, 0.95);
}
