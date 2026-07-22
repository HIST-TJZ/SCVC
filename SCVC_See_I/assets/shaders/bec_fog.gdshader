shader_type spatial;
render_mode blend_mix, depth_draw_opaque, cull_disabled;

// BEC background volumetric fog
// Represents the condensate density |psi|^2

uniform float fog_density : hint_range(0.0, 1.0) = 0.15;
uniform vec3 fog_color : source_color = vec3(0.05, 0.08, 0.2);
uniform float time_scale : hint_range(0.0, 2.0) = 0.3;

global uniform float global_time;

void fragment() {
    // Subtle quantum fluctuation pattern
    float n = sin(UV.x * 30.0 + global_time * time_scale) * 
              cos(UV.y * 30.0 + global_time * time_scale * 1.3) * 0.5 + 0.5;
    
    float alpha = fog_density * (0.7 + 0.3 * n);
    
    ALBEDO = fog_color;
    ALPHA = alpha;
}
