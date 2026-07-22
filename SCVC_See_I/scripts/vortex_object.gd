# vortex_object.gd -- Point vortex in SU(3)xSU(2)xU(1) gauge space
# Object pool compatible: visuals rebuilt on _on_pool_activate()
extends Node3D

static var batch_render: bool = true  # set by vortex_physics for GPU instancing

signal vortex_moved(v: Node3D)
signal out_of_bounds(v: Node3D)

var w_c1: float = 0.0
var w_c2: float = 0.0
var w_w:  float = 0.0
var w_y:  float = 0.0

var is_dragging: bool = false
var bound_partners: Array = []
var velocity: Vector3 = Vector3.ZERO
var mass_factor: float = 0.0  # SCVC π-polynomial, 0=auto-detect
var force_accum: Vector3 = Vector3.ZERO
var _label_node: Label3D = null

func color_winding() -> Vector2: return Vector2(w_c1, w_c2)
func has_color() -> bool: return color_winding().length() > 0.12
func has_weak() -> bool: return abs(w_w) > 0.12
func has_hyper() -> bool: return abs(w_y) > 0.12
func is_color_singlet() -> bool: return not has_color()

func _ready():
	# Pool objects start hidden, no visuals until activated
	pass

func _on_pool_activate(pos: Vector3, _wc1: float, _wc2: float, _ww: float, _wy: float):
	# Rebuild visuals with current winding data
	_clear_visuals()
	_setup_visuals()
	_update_label()

func _clear_visuals():
	_label_node = null
	for c in get_children():
		if c.name in ["Core", "Glow", "Label", "PickArea"]:
			c.queue_free()

func _setup_visuals():
	var sz = 0.18

	if not batch_render:
		# Core sphere
		var core = MeshInstance3D.new(); core.name = "Core"
		var sm = SphereMesh.new()
		sm.radius = sz; sm.height = sz*2; sm.radial_segments = 12; sm.rings = 6
		core.mesh = sm
		var mat = StandardMaterial3D.new()
		var disp = display_color()
		mat.albedo_color = disp
		mat.emission_enabled = true; mat.emission = disp * 1.2
		mat.emission_energy_multiplier = 2.5; mat.roughness = 0.3
		core.material_override = mat
		add_child(core)

		# Glow shell
		var glow = MeshInstance3D.new(); glow.name = "Glow"
		var gm = SphereMesh.new()
		gm.radius = sz * 1.7; gm.height = sz * 3.4; gm.radial_segments = 8; gm.rings = 4
		glow.mesh = gm
		var gmat = StandardMaterial3D.new()
		gmat.albedo_color = Color(disp.r, disp.g, disp.b, 0.12)
		gmat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
		gmat.emission_enabled = true; gmat.emission = disp * 0.5
		gmat.emission_energy_multiplier = 1.0
		gmat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
		glow.material_override = gmat
		add_child(glow)

	# Label (skip in batch render mode - individual draw calls)
	if not batch_render:
		var label = Label3D.new(); label.name = "Label"
		label.text = emergent_name()
		label.font_size = 10; label.billboard = BaseMaterial3D.BILLBOARD_ENABLED
		label.position = Vector3(0, sz + 0.3, 0)
		label.modulate = Color.WHITE; label.outline_size = 1
		label.outline_modulate = Color.BLACK
		_label_node = label
		add_child(label)

	# Pick area
	var area = Area3D.new(); area.name = "PickArea"
	var cs = CollisionShape3D.new(); var ss = SphereShape3D.new()
	ss.radius = max(sz * 2.0, 0.35); cs.shape = ss; area.add_child(cs)
	area.input_ray_pickable = true; area.input_capture_on_drag = true
	area.mouse_entered.connect(_on_mouse_entered)
	area.mouse_exited.connect(_on_mouse_exited)
	area.input_event.connect(_on_input_event)
	add_child(area)

func _update_label():
	if batch_render: return
	if _label_node and is_instance_valid(_label_node):
		_label_node.text = emergent_name()

func display_color() -> Color:
	var cw = color_winding()
	var cmag = cw.length()
	
	# === LEPTONS (no color) ===
	if cmag < 0.08:
		if abs(w_w) < 0.03 and abs(w_y) < 0.03:
			return Color(0.5, 0.5, 0.55)      # vacuum
		if w_w < -0.1 and w_y < -0.1:
			return Color(0.55, 0.2, 0.85)     # electron: purple
		if w_w > 0.1 and w_y > 0.1:
			return Color(1.0, 0.7, 0.1)       # positron: gold
		if w_w > 0.1 and w_y < -0.3:
			return Color(0.85, 0.9, 1.0)      # neutrino: ice white
		if w_w < -0.1 and w_y > 0.3:
			return Color(1.0, 0.7, 0.75)      # anti-neutrino: pale rose
		if w_w < -0.1:
			return Color(0.35, 0.1, 0.6)      # muon/tau: dark purple
		if w_w > 0.1:
			return Color(0.8, 0.5, 0.1)       # anti-muon/tau: dark gold
		return Color(0.5, 0.5, 0.55)
	
	# === QUARKS: detect type by w_w × w_y product ===
	# w_w*w_y > 0: up-type (particle or anti) ; w_w*w_y < 0: down-type
	# w_w > 0: particle ; w_w < 0: anti-particle
	var prod = w_w * w_y
	var is_up = prod > 0.0
	var is_anti = w_y < 0.0
	
	# Shade from color direction (R/G/B angle in SU(3))
	# For anti-particles, negate cw to restore original particle's angle
	var shade_cw = cw if not is_anti else -cw
	var angle = shade_cw.angle()
	var shade: float
	var cos_a = cos(angle)
	if cos_a > 0.5:
		shade = 0.95   # bright
	elif cos_a < -0.5 and sin(angle) > 0:
		shade = 0.6    # medium
	else:
		shade = 0.3    # dark
	
	if is_up:
		# Up family ->RED (proton quarks all red)
		if is_anti:
			# Anti-up ->CYAN
			return Color(0.05, 0.4 + shade*0.5, 0.4 + shade*0.5)
		else:
			return Color(0.35 + shade*0.65, 0.02 + shade*0.1, 0.02 + shade*0.08)
	else:
		# Down family ->GREEN (neutron quarks all green)
		if is_anti:
			# Anti-down ->MAGENTA
			return Color(0.4 + shade*0.5, 0.05, 0.4 + shade*0.5)
		else:
			return Color(0.02 + shade*0.1, 0.25 + shade*0.65, 0.02 + shade*0.15)

func emergent_name() -> String:
	# Per-quantum winding (1/3 of fermion net). Thresholds ÷3.
	var cmag = color_winding().length()
	if cmag < 0.08:
		if abs(w_w) < 0.03 and abs(w_y) < 0.03: return "vac"
		if w_w < -0.1 and w_y < -0.1: return "e-?"
		if w_w > 0.1 and w_y > 0.1: return "e-?"
		if w_w > 0.1 and w_y < -0.3: return "ν"
		if w_w < -0.1 and w_y > 0.3: return "ν̄"
		if abs(w_w) > 0.25: return "W"
		if abs(w_y) > 0.25: return "B"
		return "??"
	var cw = color_winding()
	var is_anti = w_y < 0.0
	var ref_cw = cw if not is_anti else -cw
	var angles = [ref_cw.angle_to(Vector2(1,0)), ref_cw.angle_to(Vector2(-0.5,0.866)), ref_cw.angle_to(Vector2(-0.5,-0.866))]
	var best = 0; var ba = 10.0
	for i in range(3):
		if angles[i] < ba: ba = angles[i]; best = i
	var prod = w_w * w_y
	var is_up = prod > 0.0
	var base = ["??","??","??"][best]
	var prefix = "a" if is_anti else ""
	if cmag > 0.4: return prefix + "g " + base
	if is_up: return prefix + "u " + base
	return prefix + "d " + base

func _on_mouse_entered():
	if batch_render: return
	for c in get_children():
		if c.name == "Core" and c is MeshInstance3D:
			var m = c.material_override
			if m is StandardMaterial3D: m.emission_energy_multiplier = 5.0

func _on_mouse_exited():
	if is_dragging: return
	if batch_render: return
	for c in get_children():
		if c.name == "Core" and c is MeshInstance3D:
			var m = c.material_override
			if m is StandardMaterial3D: m.emission_energy_multiplier = 2.5
	scale = Vector3.ONE

func _on_input_event(_cam: Node, event: InputEvent, _pos: Vector3, _norm: Vector3, _idx: int):
	if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT:
		if event.pressed:
			is_dragging = true; scale = Vector3(1.3,1.3,1.3)
			get_viewport().set_input_as_handled()
		else:
			is_dragging = false; scale = Vector3.ONE
			get_viewport().set_input_as_handled()

func _process(_delta: float):
	if not is_dragging: return
	var vp = get_viewport()
	if not vp: return
	var cam = vp.get_camera_3d()
	if not cam: return
	var mp = vp.get_mouse_position()
	var from = cam.project_ray_origin(mp)
	var to = from + cam.project_ray_normal(mp) * 100.0
	var hit = Plane(Vector3.UP, 0.0).intersects_ray(from, to)
	if hit:
		position = Vector3(hit.x, position.y, hit.z)
		if abs(position.x) > 800.0 or abs(position.z) > 800.0:
			out_of_bounds.emit(self)
			return

func physics_update(delta: float, total_force: Vector3):
	if is_dragging: velocity = Vector3.ZERO; return
	# Respect global time freeze
	var p = get_parent()
	if p and p.has_method("is_frozen") and p.is_frozen():
		return

	# Relativistic: Lorentz factor γ limits acceleration near c
	var v2: float = velocity.length_squared()
	const C: float = 4.90
	const C2: float = C * C
	var gamma: float = 1.0
	if v2 > 0.001 and v2 < C2 * 0.999:
		gamma = 1.0 / sqrt(1.0 - v2 / C2)
	# Smooth proximity damping: 0.92 at r=0 ->0.995 at r~=.0
	var near_dist: float = 999.0
	if p and p.has_method("nearest_vortex_dist"):
		near_dist = p.nearest_vortex_dist(self)
	var t: float = clamp(near_dist / 2.0, 0.0, 1.0)
	var damp: float = 0.96 + 0.035 * t  # smooth 0.96->.995 (faster response)
	var mf: float = _inertial_mass()
	velocity += total_force * delta / (gamma * mf); velocity *= damp
	position += velocity * delta
	if velocity.length() < 0.005: velocity = Vector3.ZERO
	# Safety cap at 0.999c (asymptotic, should rarely trigger)
	var spd: float = velocity.length()
	if spd > C * 0.999:
		velocity = velocity.normalized() * C * 0.999
	if abs(position.x) > 800.0 or abs(position.z) > 800.0 or position.y < -400.0 or position.y > 600.0:
		out_of_bounds.emit(self)
		return
	vortex_moved.emit(self)


# Inertial mass from winding: lepton~1, quark~2-3 (relative to electron)
# SCVC π-polynomial inertial masses (electron=1.0)
# m_u/m_e=3??, m_d/m_u=(5/3)^(3/2), m_c/m_u=6π?? m_s/m_d=2π², etc.
func _inertial_mass() -> float:
	if mass_factor > 0.0: return mass_factor
	# Fallback: guess from winding (basic mode only)
	var cmag: float = sqrt(w_c1*w_c1 + w_c2*w_c2)
	if cmag < 0.1:
		var q: float = w_w + w_y
		if abs(q) < 0.05: return 0.01  # neutrino
		return 1.0  # electron (muon/tau use mass_factor)
	if w_w > 0.0: return 4.2426  # up quark (charm/top use mass_factor)
	return 9.1317  # down quark (strange/bottom use mass_factor)
func is_bound_to(other: Node) -> bool: return other in bound_partners
func bind_to(other: Node):
	if not is_bound_to(other):
		bound_partners.append(other)
		if not other.is_bound_to(self): other.bound_partners.append(self)
func unbind_from(other: Node):
	bound_partners.erase(other); other.bound_partners.erase(self)
func unbind_all():
	for p in bound_partners.duplicate(): unbind_from(p)

func color_dot(other: Node3D) -> float:
	return w_c1 * other.w_c1 + w_c2 * other.w_c2
func weak_dot(other: Node3D) -> float:
	return w_w * other.w_w
func hyper_dot(other: Node3D) -> float:
	return w_y * other.w_y

func _exit_tree():
	for p in bound_partners.duplicate():
		if is_instance_valid(p): p.bound_partners.erase(self)
	bound_partners.clear()
