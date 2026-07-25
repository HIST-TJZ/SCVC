# bec_vacuum.gd -- Visualize BEC vacuum density + superfluid flow
# Attach to a plane MeshInstance3D. Generates texture each frame.
extends MeshInstance3D

@export var resolution: int = 64
@export var plane_size: float = 16.0
@export var update_every: int = 12  # frames between texture updates

var _image: Image
var _texture: ImageTexture
var _frame: int = 0
var _physics_ref: Node = null
var _visible_flag: bool = false

func _ready():
	set_process_input(true)
	_image = Image.create(resolution, resolution, false, Image.FORMAT_RGBA8)
	_texture = ImageTexture.create_from_image(_image)
	var mat = StandardMaterial3D.new()
	mat.albedo_texture = _texture
	mat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	mat.flags_unshaded = true
	material_override = mat

func _input(event):
	if event is InputEventKey and event.pressed and event.keycode == KEY_H:
		_visible_flag = not _visible_flag
		visible = _visible_flag

func _process(_delta):
	if not _visible_flag: return
	_frame += 1
	if _frame % update_every != 0: return
	if not _physics_ref:
		var root = get_tree().current_scene
		var pc = root.get_node_or_null("PhysicsContainer")
		if pc:
			for c in pc.get_children():
				if c.has_method("total_energy"):
					_physics_ref = c
					break
	if not _physics_ref: return
	
	var vortices = _physics_ref.vortices
	var n = 0
	for v in vortices:
		if is_instance_valid(v) and v.visible: n += 1
	if n == 0: return
	
	var half = plane_size / 2.0
	var scale = float(resolution) / plane_size
	
	for y in range(resolution):
		for x in range(resolution):
			var wx = float(x) / scale - half
			var wz = float(y) / scale - half
			var world_pos = global_position + Vector3(wx, 0, wz)
			
			# Compute density: ρ = Π (1 - exp(-d²/2ξ²))  → simpler: sum of gaussian dips
			var density = 1.0
			var flow_x = 0.0
			var flow_z = 0.0
			var xi = 0.4  # healing length scale
			
			var vcount = 0
			for v in vortices:
				if not is_instance_valid(v) or not v.visible: continue
				vcount += 1
				var dx = world_pos.x - v.global_position.x
				var dz = world_pos.z - v.global_position.z
				var dist2 = dx*dx + dz*dz
				var dist = sqrt(dist2)
				if dist < 0.01: dist = 0.01
				
				# Density dip from vortex core
				var dip = exp(-dist2 / (2.0 * xi * xi))
				density *= (1.0 - 0.7 * dip)
				
				# Superfluid velocity: circulation around vortex
				# v_s ∝ (k × r) / r² → in 2D: tangential direction
				var circ = 0.15 / dist  # 1/r decay
				flow_x += -dz / dist * circ
				flow_z += dx / dist * circ
			
			density = clamp(density, 0.0, 1.0)
			
			# Color: density → brightness. Flow → hue shift
			var r = 0.05 + density * 0.15  # dark blue base
			var g = 0.05 + density * 0.3
			var b = 0.2 + density * 0.7
			# Flow modulates slightly
			var flow_mag = sqrt(flow_x*flow_x + flow_z*flow_z) * 0.3
			r += flow_mag * 0.2
			g += flow_mag * 0.1
			
			_image.set_pixel(x, y, Color(r, g, b, density * 0.7))
	
	_texture.update(_image)