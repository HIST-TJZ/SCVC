# main.gd -- SCVC Emergent Physics
# Point vortices in SU(3)xSU(2)xU(1) gauge space
# All particles emerge from 4D winding vectors.
extends Node3D

@onready var physics_container: Node3D
@onready var physics: Node
@onready var ui_label: Label3D = $"UI/Label"
@onready var ui_title: Label3D = $"UI/Title"
@onready var status_label: Label = $"CanvasLayer/Control/Label"
@onready var help_label: Label = $"CanvasLayer/Control/Label2"

# FULL 4D winding preset: (wc1, wc2, ww, wy)
var sel_wc1: float = 1.0; var sel_wc2: float = 0.0
var sel_ww: float = 0.5; var sel_wy: float = 0.1667; var sel_mf: float = MF_U
var _place_y: float = 0.0
var _ring_radius: float = 0.15  # R_eq=0.085; visible at 0.15 (scale separation: ring size != orbital size)
var placing_anti: bool = false
var spin_up: bool = true  # spin toggle for lepton rings
var _last_preset_name: String = ""
var lang: int = 0  # 0=EN, 1=CN
var full_sm_mode: bool = false  # toggle for full SM particle spectrum
var _track_com: bool = false  # F toggles: camera follows center-of-mass
var _com_marker: MeshInstance3D = null  # visual marker at COM
var ground_plane: Plane = Plane(Vector3.UP, 0.0)
var _click_screen_pos: Vector2 = Vector2.ZERO
var _click_was_vortex: bool = false

# SM particle presets
const U_R = [1.0, 0.0, 0.5, 0.1667]
const D_R = [1.0, 0.0, -0.5, 0.1667]
const U_G = [-0.5, 0.866, 0.5, 0.1667]
const D_G = [-0.5, 0.866, -0.5, 0.1667]
const U_B = [-0.5, -0.866, 0.5, 0.1667]
const D_B = [-0.5, -0.866, -0.5, 0.1667]
const ELECTRON = [0.0, 0.0, -0.5, -0.5]
const NU_E = [0.0, 0.0, 0.5, -0.5]

# Full SM: all 6 quark flavors x 3 colors (gauge windings, mass from generation)
# Strange (down-type, gen2): same gauge as down
const S_R = [1.0, 0.0, -0.5, 0.1667]
const S_G = [-0.5, 0.866, -0.5, 0.1667]
const S_B = [-0.5, -0.866, -0.5, 0.1667]
# Charm (up-type, gen2): same gauge as up
const C_R = [1.0, 0.0, 0.5, 0.1667]
const C_G = [-0.5, 0.866, 0.5, 0.1667]
const C_B = [-0.5, -0.866, 0.5, 0.1667]
# Bottom (down-type, gen3)
const B_R = [1.0, 0.0, -0.5, 0.1667]
const B_G = [-0.5, 0.866, -0.5, 0.1667]
const B_B = [-0.5, -0.866, -0.5, 0.1667]
# Top (up-type, gen3)
const T_R = [1.0, 0.0, 0.5, 0.1667]
const T_G = [-0.5, 0.866, 0.5, 0.1667]
const T_B = [-0.5, -0.866, 0.5, 0.1667]

# Full SM leptons
const MUON = [0.0, 0.0, -0.5, -0.5]      # same gauge as electron
const TAU = [0.0, 0.0, -0.5, -0.5]        # same gauge as electron
const NU_MU = [0.0, 0.0, 0.5, -0.5]         # same gauge as nu_e
const NU_TAU = [0.0, 0.0, 0.5, -0.5]        # same gauge as nu_e

# SCVC π-polynomial mass factors (electron=1.0)
# m_u/m_e=3??, m_d/m_u=(5/3)^(3/2), m_c/m_u=6π?? etc.
const MF_E = 1.0
const MF_NU = 0.01
const MF_U = 4.2426     # 3*sqrt(2)
const MF_D = 9.1317     # 3*sqrt(2) * (5/3)^(3/2)
const MF_MU = 206.8     # 4*pi^3 * (5/3)
const MF_TAU = 3507.0   # 36*pi^5
const MF_S = 180.2      # 2*pi^2 * m_d/m_e
const MF_C = 2480.0     # 6*pi^5 * 3*sqrt(2)
const MF_B = 8004.0     # 9*pi^5 * m_d/m_e
const MF_T = 339840.0   # 6*pi^5 * DH * 3*sqrt(2)


func _ready():
	await get_tree().process_frame
	await get_tree().process_frame
	if not has_node("PhysicsContainer"):
		var pc = Node3D.new(); pc.name = "PhysicsContainer"; add_child(pc)
	physics_container = $PhysicsContainer
	_setup_physics()
	ui_title.text = "SCVC -- Emergent Standard Model"
	_update_status()
	_update_ui_labels()
	_update_help()
	_build_scene_panel()
	_build_particle_panel()

func _setup_physics():
	physics = load("res://scripts/vortex_physics.gd").new()
	physics.name = "VortexPhysics"
	physics_container.add_child(physics)
	physics.pair_created.connect(_on_pair_created)

	# Ground reference
	var ground = MeshInstance3D.new(); ground.name = "Ground"
	var plane = PlaneMesh.new(); plane.size = Vector2(128, 128)
	ground.mesh = plane; ground.rotation_degrees = Vector3(-90, 0, 0)
	ground.position = Vector3(0, 0, 0)
	var gmat = StandardMaterial3D.new()
	gmat.albedo_color = Color(0.08, 0.08, 0.15, 0.5)
	gmat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	gmat.flags_unshaded = true; ground.material_override = gmat
	physics_container.add_child(ground)

	# BEC vacuum visualization plane
	var bec_plane = MeshInstance3D.new(); bec_plane.name = "BECVacuum"
	var quad2 = PlaneMesh.new(); quad2.size = Vector2(128, 128)
	bec_plane.mesh = quad2
	bec_plane.position = Vector3(0, 0.05, 0)
	var bec_script = load("res://scripts/bec_vacuum.gd")
	bec_plane.set_script(bec_script)
	physics_container.add_child(bec_plane)

	# Initial scene: hydrogen atom
	_load_scene("hydrogen")

func _input(event):
	if event is InputEventKey and event.pressed:
		match event.keycode:
			KEY_SHIFT: placing_anti = event.pressed; _update_status()
			KEY_DELETE: _clear_all_vortices()
			KEY_L: lang = 1 - lang; _update_status(); _update_ui_labels()
			KEY_M: full_sm_mode = not full_sm_mode; update_panel_visibility(); _update_status(); _update_ui_labels()
			KEY_SPACE: _toggle_snapshot()
			KEY_P: _toggle_freeze()
			KEY_K: _toggle_springs()
			KEY_V: _toggle_decay()
			KEY_T: _speed_up()
			KEY_G: _slow_down()
			KEY_F: _toggle_track_com()
			KEY_BRACKETLEFT: _place_y -= 0.5; _update_status()
			KEY_BRACKETRIGHT: _place_y += 0.5; _update_status()
	elif event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT:
		# Don't process if clicking on UI panel
		if _is_mouse_over_ui(): return
		if event.pressed:
			_click_screen_pos = event.position
			_click_was_vortex = _is_vortex_at(event.position)
		else:
			# On release: place only if quick click (not drag) and not on vortex
			if _click_screen_pos.distance_to(event.position) < 5.0 and not _click_was_vortex:
				_try_place_vortex(event.position)


# Check if screen position hits a vortex (avoid placing on top of existing)
func _is_vortex_at(screen_pos: Vector2) -> bool:
	var cam = $Camera3D
	var from = cam.project_ray_origin(screen_pos)
	var to = from + cam.project_ray_normal(screen_pos) * 100.0
	var space_state = get_world_3d().direct_space_state
	var query = PhysicsRayQueryParameters3D.create(from, to)
	query.collide_with_areas = true
	query.collide_with_bodies = false
	var result = space_state.intersect_ray(query)
	return not result.is_empty()


# Check if mouse is over UI panel (prevent click-through)
func _is_mouse_over_ui() -> bool:
	if not _panel or not _panel.visible: return false
	var mouse_pos = _panel.get_local_mouse_position()
	var panel_rect = Rect2(Vector2.ZERO, _panel.size)
	return panel_rect.has_point(mouse_pos)

func _try_place_vortex(screen_pos: Vector2):
	var cam = $Camera3D
	var from = cam.project_ray_origin(screen_pos)
	var to = from + cam.project_ray_normal(screen_pos) * 100.0
	var intersection = ground_plane.intersects_ray(from, to)
	if not intersection: return
	var pos = Vector3(intersection.x, _place_y, intersection.z)
	for v in physics.vortices:
		if is_instance_valid(v) and v.position.distance_to(pos) < 0.5: return
	var wc1 = sel_wc1; var wc2 = sel_wc2; var ww = sel_ww; var wy = sel_wy
	if placing_anti: wc1 = -wc1; wc2 = -wc2; ww = -ww; wy = -wy
	# Leptons (no color charge) = vortex rings, quarks = point vortices
	var cmag := sqrt(wc1*wc1 + wc2*wc2)
	if cmag < 0.08:
		# Lepton: create vortex ring
		var ring = physics.create_ring(pos, wc1, wc2, ww, wy, sel_mf, _ring_radius)
		if ring:
			ring.normal = Vector3.UP if spin_up else Vector3.DOWN
		if not ring:
			status_label.text = _tr("Cannot create ring", "Cannot create ring")
	else:
		# Quark: create point vortex
		var created = physics.create_vortex(pos, wc1, wc2, ww, wy, Vector3.ZERO, sel_mf)
		if not created:
			status_label.text = _tr("POOL FULL! Max " + str(physics.POOL_SIZE) + " particles.", "Pool full")

func _set_preset(p: Array, pname: String = "", mf: float = MF_U):
	sel_wc1 = p[0]; sel_wc2 = p[1]; sel_ww = p[2]; sel_wy = p[3]; sel_mf = mf
	_last_preset_name = pname
	_update_status()

func preset_name() -> String:
	if _last_preset_name != "":
		var pfx = "anti-" if placing_anti else ""
		return pfx + _last_preset_name
	var wc1=sel_wc1; var wc2=sel_wc2; var ww=sel_ww; var wy=sel_wy
	if placing_anti: wc1=-wc1; wc2=-wc2; ww=-ww; wy=-wy
	var _wc1=wc1; var _wc2=wc2; var _ww=ww; var _wy=wy
	if abs(_wc1-1.0)<0.02 and abs(_wc2)<0.02 and abs(_ww-0.5)<0.02 and abs(_wy-0.1667)<0.02:
		return _tr("u-quark (bright)", "u(bright)")
	if abs(_wc1+0.5)<0.02 and abs(_wc2-0.866)<0.02 and abs(_ww-0.5)<0.02 and abs(_wy-0.1667)<0.02:
		return _tr("u-quark (medium)", "u(medium)")
	if abs(_wc1+0.5)<0.02 and abs(_wc2+0.866)<0.02 and abs(_ww-0.5)<0.02 and abs(_wy-0.1667)<0.02:
		return _tr("u-quark (dark)", "u(dark)")
	if abs(_wc1-1.0)<0.02 and abs(_wc2)<0.02 and abs(_ww+0.5)<0.02 and abs(_wy-0.1667)<0.02:
		return _tr("d-quark (bright)", "d(bright)")
	if abs(_wc1+0.5)<0.02 and abs(_wc2-0.866)<0.02 and abs(_ww+0.5)<0.02 and abs(_wy-0.1667)<0.02:
		return _tr("d-quark (medium)", "d(medium)")
	if abs(_wc1+0.5)<0.02 and abs(_wc2+0.866)<0.02 and abs(_ww+0.5)<0.02 and abs(_wy-0.1667)<0.02:
		return _tr("d-quark (dark)", "d(dark)")
	if abs(_wc1)<0.02 and abs(_wc2)<0.02 and abs(_ww+0.5)<0.02 and abs(_wy+0.5)<0.02:
		return _tr("electron", "electron")
	if abs(_wc1)<0.02 and abs(_wc2)<0.02 and abs(_ww-0.5)<0.02 and abs(_wy+0.5)<0.02:
		return _tr("neutrino", "neutrino")
	return _tr("custom", "custom")

func _on_pair_created(pos: Vector3, wc1: float, wc2: float, ww: float, wy: float):
	var off = Vector3(randf()-0.5, 0, randf()-0.5).normalized() * 0.8
	# Estimate mass factor from windings (fallback, pair creation can't know generation)
	var cmag = sqrt(wc1*wc1 + wc2*wc2)
	var mf: float = MF_E
	var is_lepton = cmag < 0.1
	if is_lepton:
		var q = ww + wy
		mf = MF_NU if abs(q) < 0.05 else MF_E
	else:
		mf = MF_U if ww > 0.0 else MF_D
	if is_lepton:
		physics.create_ring(pos+off, wc1, wc2, ww, wy, mf, 2.0)
		physics.create_ring(pos-off, -wc1, -wc2, -ww, -wy, mf, 2.0)
	else:
		physics.create_vortex(pos+off, wc1, wc2, ww, wy, Vector3.ZERO, mf)
		physics.create_vortex(pos-off, -wc1, -wc2, -ww, -wy, Vector3.ZERO, mf)

func _print_energy(): _update_status()

func _tr(en: String, cn: String) -> String:
	return cn if lang == 1 else en

func _update_status():
	var lines = PackedStringArray()
	if physics and physics.time_scale != 1.0:
		lines.append(_tr("SPEED: " + str(physics.time_scale) + "x", "SPEED: " + str(physics.time_scale) + "x"))
	lines.append(_tr("SELECTED: ", "已选择") + preset_name())
	if spin_up:
		lines.append(_tr("SPIN: UP", "SPIN: UP"))
	else:
		lines.append(_tr("SPIN: DOWN", "SPIN: DOWN"))
	if placing_anti:
		lines.append(_tr("MODE: ANTI-PARTICLE", "模式:反粒子"))
	else:
		lines.append(_tr("MODE: particle", "particle"))
	lines.append(_tr("WINDING: ", "缠绕数") + "(%.1f, %.1f, %.1f, %.1f)" % [sel_wc1, sel_wc2, sel_ww, sel_wy])
	lines.append(_tr("MASS: %.4f m_e", "质量: %.4f m_e") % sel_mf)
	# SCVC predicted physical mass (GeV bridge)
	var _w2 = sel_wc1*sel_wc1 + sel_wc2*sel_wc2 + sel_ww*sel_ww + sel_wy*sel_wy
	var _ec = 2.1322 * sel_mf * _w2
	var _emev = _ec * 0.4793
	if sqrt(sel_wc1*sel_wc1 + sel_wc2*sel_wc2) > 0.1: _emev *= 0.3927
	if _emev > 1000.0:
		lines.append("  ~ %.4f GeV" % (_emev / 1000.0))
	elif _emev > 0.001:
		lines.append("  ~ %.4f MeV" % _emev)
	lines.append(_tr("HEIGHT: %.1f", "高度: %.1f") % _place_y)
	if physics:
		var n = 0
		for v in physics.vortices:
			if is_instance_valid(v) and v.visible: n += 1
		lines.append(_tr("VORTICES: %d / %d", "涡旋数: %d / %d") % [n, physics.POOL_SIZE])
		if full_sm_mode:
			lines.append(_tr("FULL SM MODE [M=toggle]", "全SM模式 [M=切换]"))
		if physics.time_frozen:
			lines.append(_tr("[!] TIME FROZEN [P=toggle]", "[!] Time frozen [P=toggle]"))
		if physics:
			var sv = _tr("ON", "开") if physics.springs_visible else _tr("OFF", "OFF")
			lines.append(_tr("SPRINGS: " + sv + " [K=toggle]", "Springs: " + sv + " [K=toggle]"))
		if physics.decay_mode:
			lines.append(_tr("DECAY: ON [V=toggle]", "衰变: 开 [V=切换]"))
		var ring_count = 0
		for r in physics.rings:
			if is_instance_valid(r) and r.active: ring_count += 1
		if ring_count > 0:
			lines.append(_tr("RINGS: %d  [,/.]=radius %.1f", "Rings: %d  rad=%.1f") % [ring_count, _ring_radius])
		if physics.snapshot_mode:
			lines.append(_tr("SNAPSHOT MODE [Space=off, S=flash]", "Snapshot [Space=off, S=flash]"))
		var e = physics.total_energy()
		lines.append(_tr("ENERGY H = %.2f", "能量 H = %.2f") % e)
		if physics.has_method("total_energy_mev"):
			var _etot = physics.total_energy_mev()
			if _etot > 1000.0:
				lines.append("  = %.4f GeV" % (_etot / 1000.0))
			else:
				lines.append("  = %.2f MeV" % _etot)
	status_label.text = "\n".join(lines)

func _update_ui_labels():
	ui_label.text = _tr("[Panel] select particle  [Click] place  [Drag] move vortex\n[Shift] anti-particle  [Del] clear  [L] CN/EN  [P] freeze  [K] springs  [M] full SM", "[Panel] select  [Click] place  [Drag] move\n[Shift] anti  [Del] clear  [L] lang  [P] freeze")
	_update_help()

func _update_help():
	if not help_label: return
	help_label.text = _tr(
		"[CONTROLS]\n  Panel = select particle    [ / ] = adjust height\n  Left Click (short) = place    Left Drag = move vortex\n  Right Drag = orbit camera    Middle Drag = pan\n  Scroll = zoom    WASD/QE = move camera    HOME = reset\n  Shift = anti-particle    P = freeze    K = toggle springs\n  M = full SM    L = CN/EN    T/G = speed    F = track COM\n  ,/. = ring radius    Del = clear all\n  [LEFT PANEL] = load preset scenes\n\n[HOW TO FORM A PROTON]\n  Proton = u(bright,R)+u(medium,G)+d(dark,B)  (2u+1d, color singlet)\n  Neutron = d(bright,R)+d(medium,G)+u(dark,B) (2d+1u, color singlet)\n  Place 3 quarks within ~1.5 units = auto-bind!\n\n[SCVC LIMITATIONS]\n  Photon: not a vortex; EM force is via effective potential.\n  e+e- annihilation: ring-ring not implemented (needs photon).\n  Bound neutron decay: not yet implemented.\n  Molecules: bond lengths from experiment (yellow), not SCVC.",
		"[操作说明]\n  面板 = 选择粒子    [ / ] = 调整高度\n  左键短按 = 放置    左键拖拽 = 移动涡旋\n  右键拖拽 = 旋转视角    中键拖拽 = 平移\n  滚轮 = 缩放    WASD/QE = 移动相机    HOME = 重置\n  Shift = 反粒子    P = 冻结    K = 切换弹簧显示\n  M = 全SM模式    L = 中/英    T/G = 加速/减速    F = 追踪质心\n  ,/. = 环半径    Del = 清除全部\n  [左侧面板] = 加载预设场景\n\n[如何构成质子]\n  质子 = u(亮,R)+u(中,G)+d(暗,B)  (2u+1d, 色单态)\n  中子 = d(亮,R)+d(中,G)+u(暗,B)  (2d+1u, 色单态)\n  将3个夸克放置在~1.5单位内 = 自动绑定！\n\n[SCVC 已知限制]\n  光子：非涡旋结构；电磁力通过有效势能项实现。\n  e+e-湮灭：环-环湮灭未实现（需要光子机制）。\n  束缚中子衰变：尚未实现。\n  分子：键长取自实验结果（黄色标注），非SCVC推导。"
	)

func _process(_delta: float):
	# COM tracking: camera follows center-of-mass of all vortices
	if _track_com and physics:
		var cam = $Camera3D
		var com := Vector3.ZERO
		var count := 0
		for v in physics.vortices:
			if is_instance_valid(v) and v.visible:
				com += v.position
				count += 1
		if count > 0:
			com /= float(count)
			cam.pivot = com
			# Visual marker
			if not _com_marker:
				_com_marker = MeshInstance3D.new()
				var sphere = SphereMesh.new()
				sphere.radius = 0.3; sphere.height = 0.6
				_com_marker.mesh = sphere
				var mat = StandardMaterial3D.new()
				mat.albedo_color = Color.WHITE; mat.emission = Color.WHITE * 0.5
				_com_marker.material_override = mat
				add_child(_com_marker)
			_com_marker.position = com
			_com_marker.visible = true
	elif _com_marker:
		_com_marker.visible = false

func _toggle_track_com():
	_track_com = not _track_com
	$Camera3D.track_com = _track_com
	if not _track_com:
		$Camera3D.pivot = Vector3.ZERO
		if _com_marker:
			_com_marker.queue_free()
			_com_marker = null
	status_label.text = _tr("TRACK COM: " + ("ON" if _track_com else "OFF"), "TRACK: " + ("ON" if _track_com else "OFF"))
	await get_tree().create_timer(1.5).timeout
	_update_status()

func _toggle_snapshot():
	if physics: physics.toggle_snapshot()
	_update_status()

func _snap_once():
	if physics: physics.snap_visuals()


func _toggle_freeze():
	if physics:
		physics.toggle_freeze()
		_update_status()

func _toggle_decay():
	if physics:
		physics.toggle_decay()
		status_label.text = _tr("DECAY: " + ("ON" if physics.decay_mode else "OFF"), "Decay: " + ("ON" if physics.decay_mode else "OFF"))
		await get_tree().create_timer(1.5).timeout
		_update_status()


func _speed_up():
	if physics:
		physics.time_scale *= 10.0
		if physics.time_scale > 1000.0: physics.time_scale = 1000.0
		status_label.text = _tr("SPEED: " + str(physics.time_scale) + "x", "SPEED: " + str(physics.time_scale) + "x")
		await get_tree().create_timer(1.0).timeout
		_update_status()

func _slow_down():
	if physics:
		physics.time_scale /= 10.0
		if physics.time_scale < 1.0: physics.time_scale = 1.0
		status_label.text = _tr("SPEED: " + str(physics.time_scale) + "x", "SPEED: " + str(physics.time_scale) + "x")
		await get_tree().create_timer(1.0).timeout
		_update_status()

func _clear_all_vortices():
	physics.clear_all()
	_current_scene = ""

# Place Z protons + N neutrons in tight cluster (point-like to electron rings)
func _place_nucleus(pos: Vector3, Z: int, N: int):
	var r_nuc = 0.08  # SCVC: nuclear size ~1 fm = 0.076 sim
	var total = Z + N
	var placed = 0
	# Protons: uud each
	for i in range(Z):
		var off = Vector3(randf()-0.5, 0, randf()-0.5).normalized() * r_nuc * randf()
		var pp = pos + off
		physics.create_vortex(pp + Vector3(0.2,0,0),  1.0, 0.0, 0.5, 0.1667, Vector3.ZERO, MF_U)
		physics.create_vortex(pp + Vector3(-0.1,0,0.17), -0.5, 0.866, 0.5, 0.1667, Vector3.ZERO, MF_U)
		physics.create_vortex(pp + Vector3(-0.1,0,-0.17), -0.5, -0.866, -0.5, 0.1667, Vector3.ZERO, MF_D)
	# Neutrons: ddu each
	for i in range(N):
		var off = Vector3(randf()-0.5, 0, randf()-0.5).normalized() * r_nuc * randf()
		var np = pos + off
		physics.create_vortex(np + Vector3(0.2,0,0),  1.0, 0.0, -0.5, 0.1667, Vector3.ZERO, MF_D)
		physics.create_vortex(np + Vector3(-0.1,0,0.17), -0.5, 0.866, -0.5, 0.1667, Vector3.ZERO, MF_D)
		physics.create_vortex(np + Vector3(-0.1,0,-0.17), -0.5, -0.866, 0.5, 0.1667, Vector3.ZERO, MF_U)

# Place electron ring at compressed Bohr-like orbit
## SCVC Slater Z_eff: uses geometry-derived shielding (09_Slater常数_几何推导结果.md)
## sigma_same(n=1)=0.3125, sigma_same(n=2)=0.3477, sigma_inner=0.85
func _compute_zeff(Z: int, n: int, n_inner: int, n_same: int) -> float:
	var sigma: float = n_inner * 0.85
	if n == 1:
		sigma += n_same * 0.3125
	elif n == 2:
		sigma += n_same * 0.3477
	else:
		sigma += n_same * 0.3561
	return max(Z - sigma, 0.3)

# Generic element builder: auto shell-filling from Z
# Z <= 10: SCVC-locked (verified shell structure)
# Z >= 11: heuristic (Madelung rule, no d/f orbital derivation)
func _scene_element(Z: int):
	_clear_all_vortices()
	if Z < 1 or Z > 118:
		status_label.text = "Z must be 1-118"
		return

	# Approximate neutron count (most common isotope)
	var N: int = Z
	if Z == 1: N = 0     # H-1
	elif Z == 2: N = 2   # He-4
	elif Z == 3: N = 4   # Li-7
	elif Z == 4: N = 5   # Be-9
	elif Z == 5: N = 6   # B-11
	elif Z == 6: N = 6   # C-12
	elif Z == 7: N = 7   # N-14
	elif Z == 8: N = 8   # O-16
	elif Z == 9: N = 10  # F-19
	elif Z == 10: N = 10 # Ne-20
	elif Z <= 20: N = Z
	elif Z <= 30: N = Z + int((Z-20)*0.2)
	else: N = Z + int((Z-20)*0.45)

	_place_nucleus(Vector3.ZERO, Z, N)

	# Shell filling: Madelung rule (n+l, lower n first)
	# (n, l_name, capacity, n_inner_before)
	var shells = [
		[1, "s", 2],   # 1s
		[2, "s", 2],   # 2s
		[2, "p", 6],   # 2p
		[3, "s", 2],   # 3s
		[3, "p", 6],   # 3p
		[4, "s", 2],   # 4s
		[3, "d", 10],  # 3d
		[4, "p", 6],   # 4p
		[5, "s", 2],   # 5s
		[4, "d", 10],  # 4d
		[5, "p", 6],   # 5p
		[6, "s", 2],   # 6s
		[4, "f", 14],  # 4f
		[5, "d", 10],  # 5d
		[6, "p", 6],   # 6p
		[7, "s", 2],   # 7s
		[5, "f", 14],  # 5f
		[6, "d", 10],  # 6d
		[7, "p", 6],   # 7p
	]

	var remaining := Z
	var shell_plan := []  # [{n, n_inner, n_same, count}]
	var n_electrons := {}  # n -> total electrons in that shell

	for sh in shells:
		if remaining <= 0: break
		var n: int = sh[0]
		var cap: int = sh[2]
		var take: int = min(cap, remaining)
		if take > 0:
			# Count electrons in lower-n shells
			var n_inner := 0
			for nn in n_electrons:
				if nn < n:
					n_inner += n_electrons[nn]
			# Count same-n electrons already assigned
			var n_same: int = n_electrons.get(n, 0)
			shell_plan.append({"n": n, "n_inner": n_inner, "n_same": n_same, "count": take})
			n_electrons[n] = n_same + take
			remaining -= take

	# Place electron rings
	var angle_step := 0.0
	for sp in shell_plan:
		var n: int = sp["n"]
		var n_inner: int = sp["n_inner"]
		var n_same: int = sp["n_same"]
		var count: int = sp["count"]
		for i in range(count):
			var angle := (float(i) / count) * 360.0
			var zeff := _compute_zeff(Z, n, n_inner, n_same + i)
			_place_electron_ring(Vector3.ZERO, n, angle, Z, 400.0, zeff)

	# Status label
	var verif := "SCVC-locked" if Z <= 10 else ("heuristic" if Z <= 18 else "HEURISTIC")
	var emoji := "SCVC" if Z <= 10 else ("heuristic" if Z <= 18 else "HEURISTIC")
	_current_scene = "Z=%d (%s)" % [Z, verif]
	status_label.text = "Z=%d: %s" % [Z, emoji]
	_update_status()

func _place_electron_ring(nucleus_pos: Vector3, n_shell: int, angle_offset: float = 0.0, Z_nuc: int = 1, scale_comp: float = 400.0, zeff: float = -1.0):
	var r_orbit = float(n_shell * n_shell) * 4016.0 / scale_comp
	r_orbit = clamp(r_orbit, 3.0, 15.0)
	var angle = angle_offset * PI / 180.0
	var pos = nucleus_pos + Vector3(cos(angle), 0, sin(angle)) * r_orbit
	# Create ring with visual radius (will be overridden by setup_bohr_orbit)
	var ring = physics.create_ring(pos, 0.0, 0.0, -0.5, -0.5, MF_E, 1.0)
	if ring and ring.has_method("setup_bohr_orbit"):
		ring.setup_bohr_orbit(n_shell, nucleus_pos, Z_nuc, scale_comp, angle_offset, zeff)
	return ring

# ========== SCENE PRESETS ==========

func _load_scene(name: String):
	_clear_all_vortices()
	_current_scene = name
	match name:
		"pion0":     _scene_pion0()
		"pion_plus": _scene_pion_plus()
		"hydrogen":  _scene_hydrogen()
		"neutron":   _scene_neutron()
		"delta_pp":  _scene_delta_pp()
		"delta_mm":  _scene_delta_mm()
		"helium4":   _scene_helium4()
		"lithium7":  _scene_lithium7()
		"beryllium9":_scene_beryllium9()
		"boron11":   _scene_boron11()
		"carbon12":  _scene_carbon12()
		"nitrogen14":_scene_nitrogen14()
		"oxygen16":  _scene_oxygen16()
		"fluorine19":_scene_fluorine19()
		"neon20":    _scene_neon20()
		"epair":     _scene_epair()
		"p_collide": _scene_proton_collision()
		"h2":         _scene_h2()
		"h2_plus":    _scene_h2_plus()
		"heh_plus":   _scene_heh_plus()
		"h2_sep":     _scene_h2_separated()
		"h2_vfm":     _scene_h2_vfm()
		"h1":         _scene_h1()
		"deuterium":  _scene_deuterium()
		"tritium":    _scene_tritium()
		"quadium":    _scene_quadium()
		"lih":        _scene_lih()
		"h2o":        _scene_h2o()
		"nh3":        _scene_nh3()
		"ch4":        _scene_ch4()
		"empty":     pass
	_update_status()

## SCVC HONESTY: 🟢 SCVC-locked
## pi0(u+anti-u): quark+antiquark, color singlet, SCVC winding. Binding via confinement.
## Manual: initial positions ~5sim apart. Binding is SCVC-automatic within BIND_DIST=0.50.
# pi0: u(bright) + anti-u(bright) -> meson binding
## [TIME] ~5-10 sec: quarks start ~5sim apart, confinement force F≈r closes gap. Binding is SCVC-automatic.
func _scene_pion0():
	physics.create_vortex(Vector3(-2.5, 0, 0),  1.0, 0.0,  0.5, 0.1667, Vector3(0.8,0,0), MF_U)
	physics.create_vortex(Vector3( 2.5, 0, 0), -1.0, 0.0, -0.5, -0.1667, Vector3(-0.8,0,0), MF_U)

## SCVC HONESTY: 🟢 SCVC-locked
## pi+(u+anti-d): SCVC winding, color singlet. Binding via confinement (SCVC automatic).
## Manual: initial positions for visual clarity.
# pi+: u(bright) + anti-d(bright) -> pi+ meson
## [TIME] ~5-10 sec: same as pi0. Confinement binding via color singlet spring.
func _scene_pion_plus():
	physics.create_vortex(Vector3(-2, 0, 0),  1.0, 0.0,  0.5, 0.1667, Vector3(0.6,0,0), MF_U)
	physics.create_vortex(Vector3( 2, 0, 0), -1.0, 0.0,  0.5, -0.1667, Vector3(-0.6,0,0), MF_D)

## SCVC HONESTY: 🟢 SCVC-locked
## Proton(uud): SCVC color singlet, MF_U=4.2426, windings from SU(3)×SU(2)×U(1)
## Electron ring: MF_E=1.0, w=(-0.5,-0.5), a0=4016sim from SCVC alpha=1/137.036
## Manual: ring placed at compressed a0~10sim. Dynamics would take hours to reach.
## Why: Magnus-Coulomb orbital velocity ~0.00025/frame. No free parameters.
# Hydrogen: proton(uud) + electron ring (Bohr orbit, compressed scale)
## [TIME] ~70 min/orbit (v=0.00025/frame, circumference=63sim). Dynamics correct, just slow.
func _scene_hydrogen():
	_place_nucleus(Vector3.ZERO, 1, 0)   # 1 proton
	_place_electron_ring(Vector3.ZERO, 1, 0, 1, 400.0)

## SCVC HONESTY: 🟢 SCVC-locked
## Neutron(ddu): color singlet, MF_D=9.1317, net charge=0 from SCVC winding
## Quark positions: SCVC baryon scale ~0.06sim (~1fm). Binding via color confinement.
# Neutron: ddu
## [TIME] <1 sec: quarks at SCVC baryon scale (0.06sim << BIND_DIST=0.50), bind immediately.
func _scene_neutron():
	var r = 0.06  # SCVC: baryon ~1 fm = 0.076 sim; 3-quark triangle r=0.044; 0.06 for margin
	physics.create_vortex(Vector3( r*1.0, 0, 0),  1.0, 0.0, -0.5, 0.1667, Vector3.ZERO, MF_D)    # d(bright)
	physics.create_vortex(Vector3(r*-0.5, 0, r*0.866), -0.5, 0.866, -0.5, 0.1667, Vector3.ZERO, MF_D) # d(medium)
	physics.create_vortex(Vector3(r*-0.5, 0, r*-0.866), -0.5, -0.866, 0.5, 0.1667, Vector3.ZERO, MF_U) # u(dark)

## SCVC HONESTY: 🟢 SCVC-locked
## Delta++(uuu): 3 up-quarks, color singlet, SCVC winding. Decay->p+pi+ is SCVC lock.
## Manual: initial positions at SCVC baryon scale. Decay triggers automatically (V key).
# Delta++: uuu resonance -> decays to p + pi+ (enable V for decay)
## [TIME] <1 sec to bind. Decay: ~17s with DEMO prob=0.015, effectively never with real prob=2e-23.
func _scene_delta_pp():
	# uuu in tight triangle (within BIND_DIST=1.2) -> immediate binding
	var r = 0.06  # SCVC: baryon ~1 fm = 0.076 sim; 3-quark triangle r=0.044; 0.06 for margin
	physics.create_vortex(Vector3( r*1.0, 0, 0),  1.0, 0.0, 0.5, 0.1667, Vector3.ZERO, MF_U)
	physics.create_vortex(Vector3(r*-0.5, 0, r*0.866), -0.5, 0.866, 0.5, 0.1667, Vector3.ZERO, MF_U)
	physics.create_vortex(Vector3(r*-0.5, 0, r*-0.866), -0.5, -0.866, 0.5, 0.1667, Vector3.ZERO, MF_U)
	# Auto-enable decay mode for resonance scenes
	if physics and not physics.decay_mode:
		physics.toggle_decay()

## SCVC HONESTY: 🟢 SCVC-locked
## Delta-(ddd): 3 down-quarks, color singlet. Decay->n+pi- is SCVC lock.
## Manual: initial positions at SCVC baryon scale. Decay triggers automatically (V key).
# Delta-: ddd resonance -> decays to n + pi-
## [TIME] <1 sec to bind. Decay: ~17s with DEMO prob=0.015, effectively never with real prob=2e-23.
func _scene_delta_mm():
	# ddd in tight triangle (within BIND_DIST=1.2) -> immediate binding
	var r = 0.06  # SCVC: baryon ~1 fm = 0.076 sim; 3-quark triangle r=0.044; 0.06 for margin
	physics.create_vortex(Vector3( r*1.0, 0, 0),  1.0, 0.0, -0.5, 0.1667, Vector3.ZERO, MF_D)
	physics.create_vortex(Vector3(r*-0.5, 0, r*0.866), -0.5, 0.866, -0.5, 0.1667, Vector3.ZERO, MF_D)
	physics.create_vortex(Vector3(r*-0.5, 0, r*-0.866), -0.5, -0.866, -0.5, 0.1667, Vector3.ZERO, MF_D)
	# Auto-enable decay mode
	if physics and not physics.decay_mode:
		physics.toggle_decay()

## SCVC HONESTY: 🟢 SCVC-locked
## Nucleus: 2p+2n at SCVC baryon scale ~0.08sim. Electron rings at compressed Bohr orbit.
## Pauli singlet: ring1 normal=UP, ring2 normal=DOWN -> SCVC normal-aware Pauli allows.
## Manual: ring placement at orbital distance. Orbital period ~hours, dynamics too slow.
# Helium-4: 2p + 2n + 2e rings (simplified, quarks pre-grouped)
## [TIME] ~70 min/orbit per ring (same v as H). Two rings opposite sides. Pauli singlet. Static if unperturbed.
func _scene_helium4():
	_place_nucleus(Vector3.ZERO, 2, 2)   # 2 protons + 2 neutrons
	_place_electron_ring(Vector3.ZERO, 1, 0, 2, 400.0, _compute_zeff(2,1,0,1))     # e1 Z_eff=2-0.3125=1.6875
	_place_electron_ring(Vector3.ZERO, 1, 180, 2, 400.0, _compute_zeff(2,1,0,1))    # e2 Z_eff=1.6875
## SCVC HONESTY: 🟢 SCVC-locked
## 3p+4n+3e at SCVC scales. Electron shells: 1s2 2s1 (SCVC Bohr+Pauli).
## Manual: ring placement. Orbital dynamics too slow for real-time emergence.
# Lithium-7: 3p + 4n + 3e
## [TIME] ~70 min/orbit/shell. 1s2 2s1: 3 rings. Static at SCVC equilibrium positions.
func _scene_lithium7():
	_place_nucleus(Vector3.ZERO, 3, 4)
	_place_electron_ring(Vector3.ZERO, 1, 0, 3, 400.0, _compute_zeff(3,1,0,1))
	_place_electron_ring(Vector3.ZERO, 1, 180, 3, 400.0, _compute_zeff(3,1,0,1))
	_place_electron_ring(Vector3.ZERO, 2, 0, 3, 400.0, _compute_zeff(3,2,2,0))

## SCVC HONESTY: 🟢 SCVC-locked
## 4p+5n+4e. Electron shells: 1s2 2s2 (from SCVC Bohr+Pauli).
# Beryllium-9: 4p + 5n + 4e
## [TIME] ~70 min/orbit/shell. 1s2 2s2: 4 rings. Static at SCVC equilibrium.
func _scene_beryllium9():
	_place_nucleus(Vector3.ZERO, 4, 5)
	_place_electron_ring(Vector3.ZERO, 1, 0, 4, 400.0, _compute_zeff(4,1,0,1))
	_place_electron_ring(Vector3.ZERO, 1, 180, 4, 400.0, _compute_zeff(4,1,0,1))
	_place_electron_ring(Vector3.ZERO, 2, 0, 4, 400.0, _compute_zeff(4,2,2,1))
	_place_electron_ring(Vector3.ZERO, 2, 180, 4, 400.0, _compute_zeff(4,2,2,1))

## SCVC HONESTY: 🟢 SCVC-locked
## 5p+6n+5e. Electron shells: 1s2 2s2 2p1.
# Boron-11: 5p + 6n + 5e
## [TIME] ~70 min/orbit/shell. 1s2 2s2 2p1: 5 rings. Static at SCVC equilibrium.
func _scene_boron11():
	_place_nucleus(Vector3.ZERO, 5, 6)
	_place_electron_ring(Vector3.ZERO, 1, 0, 5, 400.0, _compute_zeff(5,1,0,1))
	_place_electron_ring(Vector3.ZERO, 1, 180, 5, 400.0, _compute_zeff(5,1,0,1))
	_place_electron_ring(Vector3.ZERO, 2, 0, 5, 400.0, _compute_zeff(5,2,2,2))
	_place_electron_ring(Vector3.ZERO, 2, 120, 5, 400.0)
	_place_electron_ring(Vector3.ZERO, 2, 240, 5, 400.0)

## SCVC HONESTY: 🟢 SCVC-locked
## 6p+6n+6e. Electron shells: 1s2 2s2 2p2.
# Carbon-12: 6p + 6n + 6e
## [TIME] ~70 min/orbit/shell. 1s2 2s2 2p2: 6 rings. Static at SCVC equilibrium.
func _scene_carbon12():
	_place_nucleus(Vector3.ZERO, 6, 6)
	_place_electron_ring(Vector3.ZERO, 1, 0, 6, 400.0, _compute_zeff(6,1,0,1))
	_place_electron_ring(Vector3.ZERO, 1, 180, 6, 400.0, _compute_zeff(6,1,0,1))
	_place_electron_ring(Vector3.ZERO, 2, 0, 6, 400.0, _compute_zeff(6,2,2,3))
	_place_electron_ring(Vector3.ZERO, 2, 90, 6, 400.0, _compute_zeff(6,2,2,3))
	_place_electron_ring(Vector3.ZERO, 2, 180, 6, 400.0, _compute_zeff(6,2,2,3))
	_place_electron_ring(Vector3.ZERO, 2, 270, 6, 400.0, _compute_zeff(6,2,2,3))

## SCVC HONESTY: 🟢 SCVC-locked
## 7p+7n+7e. Electron shells: 1s2 2s2 2p3.
# Nitrogen-14: 7p + 7n + 7e
## [TIME] ~70 min/orbit/shell. 1s2 2s2 2p3: 7 rings. Static at SCVC equilibrium.
func _scene_nitrogen14():
	_place_nucleus(Vector3.ZERO, 7, 7)
	_place_electron_ring(Vector3.ZERO, 1, 0, 7, 400.0, _compute_zeff(7,1,0,1))
	_place_electron_ring(Vector3.ZERO, 1, 180, 7, 400.0, _compute_zeff(7,1,0,1))
	_place_electron_ring(Vector3.ZERO, 2, 0, 7, 400.0, _compute_zeff(7,2,2,4))
	_place_electron_ring(Vector3.ZERO, 2, 72, 7, 400.0)
	_place_electron_ring(Vector3.ZERO, 2, 144, 7, 400.0)
	_place_electron_ring(Vector3.ZERO, 2, 216, 7, 400.0)
	_place_electron_ring(Vector3.ZERO, 2, 288, 7, 400.0)

## SCVC HONESTY: 🟢 SCVC-locked
## 8p+8n+8e. Electron shells: 1s2 2s2 2p4.
# Oxygen-16: 8p + 8n + 8e
## [TIME] ~70 min/orbit/shell. 1s2 2s2 2p4: 8 rings. Static at SCVC equilibrium.
func _scene_oxygen16():
	_place_nucleus(Vector3.ZERO, 8, 8)
	_place_electron_ring(Vector3.ZERO, 1, 0, 8, 400.0, _compute_zeff(8,1,0,1))
	_place_electron_ring(Vector3.ZERO, 1, 180, 8, 400.0, _compute_zeff(8,1,0,1))
	_place_electron_ring(Vector3.ZERO, 2, 0, 8, 400.0, _compute_zeff(8,2,2,5))
	_place_electron_ring(Vector3.ZERO, 2, 60, 8, 400.0)
	_place_electron_ring(Vector3.ZERO, 2, 120, 8, 400.0)
	_place_electron_ring(Vector3.ZERO, 2, 180, 8, 400.0, _compute_zeff(8,2,2,5))
	_place_electron_ring(Vector3.ZERO, 2, 240, 8, 400.0)
	_place_electron_ring(Vector3.ZERO, 2, 300, 8, 400.0)

## SCVC HONESTY: 🟢 SCVC-locked
## 9p+10n+9e. Electron shells: 1s2 2s2 2p5.
# Fluorine-19: 9p + 10n + 9e
## [TIME] ~70 min/orbit/shell. 1s2 2s2 2p5: 9 rings. Static at SCVC equilibrium.
func _scene_fluorine19():
	_place_nucleus(Vector3.ZERO, 9, 10)
	_place_electron_ring(Vector3.ZERO, 1, 0, 9, 400.0, _compute_zeff(9,1,0,1))
	_place_electron_ring(Vector3.ZERO, 1, 180, 9, 400.0, _compute_zeff(9,1,0,1))
	_place_electron_ring(Vector3.ZERO, 2, 0, 9, 400.0, _compute_zeff(9,2,2,6))
	_place_electron_ring(Vector3.ZERO, 2, 51, 9, 400.0)
	_place_electron_ring(Vector3.ZERO, 2, 103, 9, 400.0)
	_place_electron_ring(Vector3.ZERO, 2, 154, 9, 400.0)
	_place_electron_ring(Vector3.ZERO, 2, 206, 9, 400.0)
	_place_electron_ring(Vector3.ZERO, 2, 257, 9, 400.0)
	_place_electron_ring(Vector3.ZERO, 2, 309, 9, 400.0)

## SCVC HONESTY: 🟢 SCVC-locked
## 10p+10n+10e. Electron shells: 1s2 2s2 2p6 (closed shell).
# Neon-20: 10p + 10n + 10e
## [TIME] ~70 min/orbit/shell. 1s2 2s2 2p6: 10 rings. Closed shell. Static at SCVC equilibrium.
func _scene_neon20():
	_place_nucleus(Vector3.ZERO, 10, 10)
	_place_electron_ring(Vector3.ZERO, 1, 0, 10, 400.0, _compute_zeff(10,1,0,1))
	_place_electron_ring(Vector3.ZERO, 1, 180, 10, 400.0, _compute_zeff(10,1,0,1))
	_place_electron_ring(Vector3.ZERO, 2, 0, 10, 400.0, _compute_zeff(10,2,2,7))
	_place_electron_ring(Vector3.ZERO, 2, 45, 10, 400.0, _compute_zeff(10,2,2,7))
	_place_electron_ring(Vector3.ZERO, 2, 90, 10, 400.0, _compute_zeff(10,2,2,7))
	_place_electron_ring(Vector3.ZERO, 2, 135, 10, 400.0, _compute_zeff(10,2,2,7))
	_place_electron_ring(Vector3.ZERO, 2, 180, 10, 400.0, _compute_zeff(10,2,2,7))
	_place_electron_ring(Vector3.ZERO, 2, 225, 10, 400.0, _compute_zeff(10,2,2,7))
	_place_electron_ring(Vector3.ZERO, 2, 270, 10, 400.0, _compute_zeff(10,2,2,7))
	_place_electron_ring(Vector3.ZERO, 2, 315, 10, 400.0, _compute_zeff(10,2,2,7))

## SCVC HONESTY: 🔴 Demo/visual
## Electron + positron rings at arbitrary positions. Visual demonstration only.
## SCVC-locked: ring winding, charge. NOT SCVC: placement, velocity.
# e+ e- pair (electron ring + positron ring)
## [TIME] ~seconds: rings attract and may annihilate. Visual demo only.
func _scene_epair():
	physics.create_ring(Vector3(-3, 0, 0), 0.0, 0.0, -0.5, -0.5, MF_E, 0.15)
	physics.create_ring(Vector3( 3, 0, 0), 0.0, 0.0,  0.5,  0.5, MF_E, 0.15)

# Proton collision: two protons approaching at speed
## SCVC HONESTY: 🔴 Demo/visual
## [TIME] ~2 sec: protons at v=3sim/frame, distance 10sim. Collision in ~1.7 sec. Visual demo.
## Two protons with arbitrary approach velocities. Visual collision demo.
## SCVC-locked: proton quark structure (uud), MF_U=4.2426, color singlet.
## NOT SCVC: initial positions (+-5sim), velocity (3.0sim/frame). Arbitrary demo values.
func _scene_proton_collision():
	var spd = 3.0
	# Proton 1 moving right
	var r = 0.8
	physics.create_vortex(Vector3(-5, 0, 0.5),  1.0, 0.0, 0.5, 0.1667, Vector3(spd,0,0), MF_U)
	physics.create_vortex(Vector3(-5.4, 0, 1.0), -0.5, 0.866, 0.5, 0.1667, Vector3(spd,0,0), MF_U)
	physics.create_vortex(Vector3(-5.4, 0, -0.5), -0.5, -0.866, -0.5, 0.1667, Vector3(spd,0,0), MF_D)
	# Proton 2 moving left
	physics.create_vortex(Vector3( 5, 0, -0.5),  1.0, 0.0, 0.5, 0.1667, Vector3(-spd,0,0), MF_U)
	physics.create_vortex(Vector3( 5.4, 0, -1.0), -0.5, 0.866, 0.5, 0.1667, Vector3(-spd,0,0), MF_U)
	physics.create_vortex(Vector3( 5.4, 0, 0.5), -0.5, -0.866, -0.5, 0.1667, Vector3(-spd,0,0), MF_D)


## SCVC HONESTY: 🟡 Empirical (bond length from QM, not SCVC)
## SCVC-locked: electron winding, Pauli singlet (normal-aware), EM coupling G_EM=2.00.
## NOT SCVC: D_H2=0.741A (QM). SCVC gives eV/A scale but not exact bond length.
## I2: 'SCVC provides scale. Exact numbers need equivalent QM (verified).'
## Manual: ring placement at d/4. Dynamics cannot reach equilibrium in sim time.
# H2 Molecule: 2 protons + 2 shared electron rings (I2 SCVC covalent bond)
# D_H2 = 0.741 A -> sim: 10 * 0.741/0.529 = 14.0 (I2 scaling, from QM bond length)
# Ring normals: UP (default, ring in XZ plane). Bond axis = Y.
# Anti-spin singlet: both e-(-0.5,-0.5) + ring2.normal=DOWN -> Pauli allowed
## [TIME] STATIC: rings at I2 equilibrium (d/4). v=0 quasi-static. No visible evolution expected.
func _scene_h2():
	const D_H2_SIM: float = 14.0
	var d2 = D_H2_SIM / 2.0  # 7.0
	# Protons at +-d2 on Y axis (bond axis)
	_place_nucleus(Vector3(0, -d2, 0), 1, 0)  # proton 1
	_place_nucleus(Vector3(0,  d2, 0), 1, 0)  # proton 2
	# Rings at +-d2/2 (between protons), normals=UP (XZ plane), quasi-static
	var ring1 = physics.create_ring(Vector3(0, -d2/2, 0), 0.0, 0.0, -0.5, -0.5, MF_E, 1.5)
	ring1.center_velocity = Vector3.ZERO
	var ring2 = physics.create_ring(Vector3(0, d2/2, 0), 0.0, 0.0, -0.5, -0.5, MF_E, 1.5)
	ring2.center_velocity = Vector3.ZERO

## SCVC HONESTY: 🟡 Empirical (bond length from QM, not SCVC)
## SCVC-locked: electron winding, EM coupling. NOT SCVC: D_H2=0.741A (QM).
# H2+ Ion: 2 protons + 1 shared electron ring (I2 single-electron bond)
## [TIME] STATIC: ring at midpoint, quasi-static. Dynamics too slow for equilibration.
func _scene_h2_plus():
	const D_H2_SIM: float = 14.0
	var d2 = D_H2_SIM / 2.0
	_place_nucleus(Vector3(0, -d2, 0), 1, 0)
	_place_nucleus(Vector3(0,  d2, 0), 1, 0)
	var ring = physics.create_ring(Vector3.ZERO, 0.0, 0.0, -0.5, -0.5, MF_E, 1.5)
	ring.center_velocity = Vector3.ZERO

## SCVC HONESTY: 🟡 Empirical (bond length from QM, not SCVC)
## SCVC-locked: electron winding, Pauli singlet. NOT SCVC: bond length (QM).
# HeH+: Helium nucleus + proton + 2 electron rings (I2: asymmetric bond)
## [TIME] STATIC: rings at I2 equilibrium positions. Asymmetric bond, quasi-static.
func _scene_heh_plus():
	const D_BOND: float = 14.0
	var d2 = D_BOND / 2.0
	_place_nucleus(Vector3(0, -d2, 0), 2, 2)  # He at -Y (2p+2n)
	_place_nucleus(Vector3(0,  d2, 0), 1, 0)  # H+ at +Y (1p)
	# Rings closer to He (higher Z pulls electrons)
	var offset = -d2 * 0.25  # shift toward He
	var ring1 = physics.create_ring(Vector3(2, offset, 0), 0.0, 0.0, -0.5, -0.5, MF_E, 1.5)
	var ring2 = physics.create_ring(Vector3(-2, offset, 0), 0.0, 0.0, -0.5, -0.5, MF_E, 1.5)
	ring1.center_velocity = Vector3.ZERO
	ring2.center_velocity = Vector3.ZERO

## SCVC HONESTY: 🔴 Demo control
## Two isolated H atoms at arbitrary separation. Purely for comparison with H2 scene.
## No SCVC derivation for the separation distance (30sim = visual choice).
# H2 Separated: two isolated H atoms far apart (I2 control)
## [TIME] STATIC: two isolated H atoms at arbitrary distance. Control scene, no evolution.
func _scene_h2_separated():
	const SEP: float = 30.0  # far enough, no bond
	var s2 = SEP / 2.0
	_place_nucleus(Vector3(0, -s2, 0), 1, 0)
	_place_nucleus(Vector3(0,  s2, 0), 1, 0)
	_place_electron_ring(Vector3(0, -s2, 0), 1, 0, 1, 400.0)
	_place_electron_ring(Vector3(0,  s2, 0), 1, 180, 1, 400.0)

## SCVC HONESTY: demo -- VFM free-ring covalent bond test
## Two H atoms with FREE electron rings (no orbital constraint).
## VFM Biot-Savart drives ring-ring and ring-quark dynamics.
## If covalent bond forms: rings move to bond region, protons settle.
# H2 VFM Test: 2 protons + 2 free electron rings
func _scene_h2_vfm():
	const SEP: float = 30.0
	var s2 = SEP / 2.0
	_place_nucleus(Vector3(0, -s2, 0), 1, 0)
	_place_nucleus(Vector3(0,  s2, 0), 1, 0)
	var r1 = physics.create_ring(Vector3(0, -s2, 0), 0.0, 0.0, -0.5, -0.5, MF_E, 1.5)
	r1.center_velocity = Vector3.ZERO
	var r2 = physics.create_ring(Vector3(0,  s2, 0), 0.0, 0.0, -0.5, -0.5, MF_E, 1.5)
	r2.center_velocity = Vector3.ZERO


## SCVC HONESTY: yellow Empirical (bond length/angle from experiment)
## SCVC-locked: atomic shells (Z_eff from Slater), Pauli, shell radii.
## NOT SCVC: bond length & angle (experimental). Rings placed at parent nuclei.
# LiH: Li(1s2 2s1) + H(1s1), d=1.595A
func _scene_lih():
	var d: float = 1.595 * 18.89  # 30.1 sim
	var d2: float = d / 2.0
	_place_nucleus(Vector3(0, -d2, 0), 3, 4)   # Li: 3p+4n
	_place_nucleus(Vector3(0,  d2, 0), 1, 0)   # H: 1p
	# Li inner 1s2
	_place_electron_ring(Vector3(0, -d2, 0), 1, 0, 3, 400.0, _compute_zeff(3,1,0,1))
	_place_electron_ring(Vector3(0, -d2, 0), 1, 180, 3, 400.0, _compute_zeff(3,1,0,1))
	# Li valence 2s1
	_place_electron_ring(Vector3(0, -d2, 0), 2, 0, 3, 400.0, _compute_zeff(3,2,2,0))
	# H 1s1
	_place_electron_ring(Vector3(0,  d2, 0), 1, 0, 1, 400.0, _compute_zeff(1,1,0,0))

## SCVC HONESTY: yellow Empirical. O-H=0.958A, H-O-H=104.5 deg.
# H2O: O(1s2 2s2 2p4) + 2H
func _scene_h2o():
	var d_OH: float = 0.958 * 18.89  # 18.1 sim
	var half_angle: float = deg_to_rad(104.5 / 2.0)  # 52.25 deg
	var dx: float = d_OH * sin(half_angle)
	var dz: float = d_OH * cos(half_angle)
	# O at origin, H in XZ plane forming V
	_place_nucleus(Vector3.ZERO, 8, 8)   # O: 8p+8n
	_place_nucleus(Vector3( dx, 0, dz), 1, 0)   # H1
	_place_nucleus(Vector3(-dx, 0, dz), 1, 0)   # H2
	# O inner 1s2
	_place_electron_ring(Vector3.ZERO, 1, 0, 8, 400.0, _compute_zeff(8,1,0,1))
	_place_electron_ring(Vector3.ZERO, 1, 180, 8, 400.0, _compute_zeff(8,1,0,1))
	# O valence 2s2+2p4 = 6 electrons at n=2, evenly spaced
	for a in [0, 60, 120, 180, 240, 300]:
		_place_electron_ring(Vector3.ZERO, 2, a, 8, 400.0, _compute_zeff(8,2,2,5))
	# H 1s1 (each)
	_place_electron_ring(Vector3( dx, 0, dz), 1, 0, 1, 400.0, _compute_zeff(1,1,0,0))
	_place_electron_ring(Vector3(-dx, 0, dz), 1, 0, 1, 400.0, _compute_zeff(1,1,0,0))

## SCVC HONESTY: yellow Empirical. N-H=1.012A, H-N-H=107 deg.
# NH3: N(1s2 2s2 2p3) + 3H, trigonal pyramid
func _scene_nh3():
	var d_NH: float = 1.012 * 18.89  # 19.1 sim
	var angle: float = deg_to_rad(107.0)
	# N above H3 plane by h = d*cos(theta) where theta from axis
	# For pyramid, bond angle from vertical: cos(bond_to_vertical) relationship
	# Simple: place H at 120 deg apart in XZ, N above
	var h: float = d_NH * cos(angle / 2.0)  # approx height
	var r: float = d_NH * sin(angle / 2.0)  # approx radius
	# N at (0, h, 0), H in XZ at y=0
	_place_nucleus(Vector3(0, h, 0), 7, 7)   # N: 7p+7n
	for i in range(3):
		var a: float = deg_to_rad(i * 120.0)
		_place_nucleus(Vector3(r*cos(a), 0, r*sin(a)), 1, 0)
	# N inner 1s2
	_place_electron_ring(Vector3(0, h, 0), 1, 0, 7, 400.0, _compute_zeff(7,1,0,1))
	_place_electron_ring(Vector3(0, h, 0), 1, 180, 7, 400.0, _compute_zeff(7,1,0,1))
	# N valence 2s2+2p3 = 5 electrons
	for a in [0, 72, 144, 216, 288]:
		_place_electron_ring(Vector3(0, h, 0), 2, a, 7, 400.0, _compute_zeff(7,2,2,4))
	# H 1s1
	for i in range(3):
		var a: float = deg_to_rad(i * 120.0)
		_place_electron_ring(Vector3(r*cos(a), 0, r*sin(a)), 1, 0, 1, 400.0, _compute_zeff(1,1,0,0))

## SCVC HONESTY: yellow Empirical. C-H=1.087A, tetrahedral 109.5 deg.
# CH4: C(1s2 2s2 2p2) + 4H, tetrahedron
func _scene_ch4():
	var d_CH: float = 1.087 * 18.89  # 20.5 sim
	var s: float = d_CH / sqrt(3.0)  # tetrahedron vertex coordinate
	# C at origin, 4 H at tetrahedral vertices
	_place_nucleus(Vector3.ZERO, 6, 6)   # C: 6p+6n
	_place_nucleus(Vector3( s,  s,  s), 1, 0)
	_place_nucleus(Vector3(-s, -s,  s), 1, 0)
	_place_nucleus(Vector3( s, -s, -s), 1, 0)
	_place_nucleus(Vector3(-s,  s, -s), 1, 0)
	# C inner 1s2
	_place_electron_ring(Vector3.ZERO, 1, 0, 6, 400.0, _compute_zeff(6,1,0,1))
	_place_electron_ring(Vector3.ZERO, 1, 180, 6, 400.0, _compute_zeff(6,1,0,1))
	# C valence 2s2+2p2 = 4 electrons
	for a in [0, 90, 180, 270]:
		_place_electron_ring(Vector3.ZERO, 2, a, 6, 400.0, _compute_zeff(6,2,2,3))
	# H 1s1
	_place_electron_ring(Vector3( s,  s,  s), 1, 0, 1, 400.0, _compute_zeff(1,1,0,0))
	_place_electron_ring(Vector3(-s, -s,  s), 1, 0, 1, 400.0, _compute_zeff(1,1,0,0))
	_place_electron_ring(Vector3( s, -s, -s), 1, 0, 1, 400.0, _compute_zeff(1,1,0,0))
	_place_electron_ring(Vector3(-s,  s, -s), 1, 0, 1, 400.0, _compute_zeff(1,1,0,0))

# ========== HYDROGEN ISOTOPES (SCVC-derived parameters) ==========
# All isotopes: Z=1 -> same electron Bohr orbit (A0_SIM=4016.1, scale=400)
# Nuclear structure uses SCVC quark windings, no free parameters.

## SCVC HONESTY: 🟢 SCVC-locked (same as hydrogen)
## 1p+1e. All parameters from SCVC. Same orbit as all H isotopes (Z=1).
## [TIME] ~70 min/orbit (v=0.00025/frame, 2π×10sim). Dynamics correct, just slow.
# H-1 Protium: 1p + 1e (stable, identical to hydrogen scene)
func _scene_h1():
	_place_nucleus(Vector3.ZERO, 1, 0)
	_place_electron_ring(Vector3.ZERO, 1, 0, 1, 400.0)

## SCVC HONESTY: 🟢 SCVC-locked
## 1p+1n+1e. Neutron(ddu) SCVC color singlet. Z=1 -> same electron orbit as 1H.
## I1 verified: stability pattern correct. Deuteron binding from SCVC vortex ring picture.
# H-2 Deuterium: 1p + 1n + 1e (stable isotope)
## [TIME] ~70 min/orbit. Heavier nucleus (1p+1n) but Z=1 -> same electron orbit.
func _scene_deuterium():
	_place_nucleus(Vector3.ZERO, 1, 1)
	_place_electron_ring(Vector3.ZERO, 1, 0, 1, 400.0)

## SCVC HONESTY: 🟢 SCVC-locked (decay not implemented for bound neutrons)
## 1p+2n+1e. Z=1 -> same electron orbit. I1: beta-unstable (t1/2=12.3yr).
## LIMIT: beta decay requires bound-neutron decay (not yet implemented, free neutron only).
## [TIME] ~70 min/orbit. Beta decay of bound neutrons not yet implemented.
# H-3 Tritium: 1p + 2n + 1e (beta-unstable, t1/2=12.3y)
# NOTE: decay not yet implemented (requires n->p+e+nu weak interaction)
func _scene_tritium():
	_place_nucleus(Vector3.ZERO, 1, 2)
	_place_electron_ring(Vector3.ZERO, 1, 0, 1, 400.0)

## SCVC HONESTY: 🟢 SCVC-locked (decay not implemented)
## 1p+3n+1e. I1: neutron-unstable (t1/2~1e-22s). SCVC predicts non-bound.
## LIMIT: neutron emission not yet implemented.
# H-4 Quadium: 1p + 3n + 1e (neutron-unstable, t1/2~1e-22s)
# NOTE: decay not yet implemented (requires neutron emission channel)
## [TIME] ~70 min/orbit. Neutron emission not yet implemented.
func _scene_quadium():
	_place_nucleus(Vector3.ZERO, 1, 3)
	_place_electron_ring(Vector3.ZERO, 1, 0, 1, 400.0)
# ========== PARTICLE SELECTION PANEL ==========
var _panel: Control = null
var _anti_toggle: CheckButton = null
var _panel_buttons: Dictionary = {}
var _scene_panel: Control = null
var _current_scene: String = ""

func _toggle_springs():
	if physics: physics.springs_visible = not physics.springs_visible
	_update_status()

# ========== SCENE SELECTION PANEL ==========

func _build_scene_panel():
	var canvas = $CanvasLayer
	_scene_panel = Panel.new()
	_scene_panel.name = "ScenePanel"
	_scene_panel.position = Vector2(10, 40)
	_scene_panel.size = Vector2(150, 620)
	var ps = StyleBoxFlat.new()
	ps.bg_color = Color(0.05, 0.05, 0.08, 0.85)
	ps.border_width_left = 1; ps.border_width_right = 1
	ps.border_width_top = 1; ps.border_width_bottom = 1
	ps.border_color = Color(0.3, 0.3, 0.4, 0.8)
	ps.corner_radius_top_left = 8; ps.corner_radius_top_right = 8
	ps.corner_radius_bottom_left = 8; ps.corner_radius_bottom_right = 8
	_scene_panel.add_theme_stylebox_override("panel", ps)
	canvas.add_child(_scene_panel)

	var sv = ScrollContainer.new()
	sv.name = "SceneScroll"
	sv.position = Vector2(5, 5)
	sv.size = Vector2(140, 610)
	sv.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	_scene_panel.add_child(sv)

	var vbox = VBoxContainer.new()
	vbox.name = "SceneList"
	vbox.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	sv.add_child(vbox)

	_add_scene_label(vbox, "=== SCENES ===")
	_add_scene_label(vbox, "🟢=SCVC locked  🟡=QM/exp  🔴=Demo")
	_add_scene_button(vbox, "pi0 Meson", "pion0", "pi0: u+anti-u (🟢SCVC bind)")
	_add_scene_button(vbox, "pi+ Meson", "pion_plus", "pi+: u+anti-d (🟢SCVC bind)")
	_add_scene_button(vbox, "HYDROGEN", "hydrogen", "HYDROGEN (🟢SCVC)")
	_add_scene_button(vbox, "Neutron", "neutron", "Neutron (🟢SCVC)")
	_add_scene_button(vbox, "Delta++", "delta_pp", "Delta++ (🟢SCVC decay)")
	_add_scene_button(vbox, "Delta-", "delta_mm", "Delta- (🟢SCVC decay)")
	_add_scene_button(vbox, "Helium-4", "helium4", "He-4 (🟢SCVC+Pauli)")
	_add_scene_label(vbox, "--- LIGHT ELEMENTS ---")
	_add_scene_button(vbox, "Li-7", "lithium7", "Li-7 (🟢SCVC)")
	_add_scene_button(vbox, "Be-9", "beryllium9", "Be-9 (🟢SCVC)")
	_add_scene_button(vbox, "B-11", "boron11", "B-11 (🟢SCVC)")
	_add_scene_button(vbox, "C-12", "carbon12", "C-12 (🟢SCVC)")
	_add_scene_button(vbox, "N-14", "nitrogen14", "N-14 (🟢SCVC)")
	_add_scene_button(vbox, "O-16", "oxygen16", "O-16 (🟢SCVC)")
	_add_scene_button(vbox, "F-19", "fluorine19", "F-19 (🟢SCVC)")
	_add_scene_button(vbox, "Ne-20", "neon20", "Ne-20 (🟢SCVC)")
	_add_scene_label(vbox, "")
	_add_scene_button(vbox, "e+e- Pair", "epair", "e+e- (🔴demo)")
	_add_scene_button(vbox, "p+p Collide", "p_collide", "p+p (🔴demo)")
	_add_scene_label(vbox, "--- MOLECULES ---")
	_add_scene_button(vbox, "H2 Molecule", "h2", "H2 (🟡QM bond)")
	_add_scene_button(vbox, "H2+ Ion", "h2_plus", "H2+ (🟡QM bond)")
	_add_scene_button(vbox, "HeH+", "heh_plus", "HeH+ (🟡QM bond)")
	_add_scene_button(vbox, "H2 Separated", "h2_sep", "H2 Sep (🔴demo)")
	_add_scene_button(vbox, "H2 VFM Test", "h2_vfm", "H2 VFM (bond test)")
	_add_scene_label(vbox, "--- MOLECULES (exp geom) ---")
	_add_scene_button(vbox, "LiH", "lih", "LiH (yellow exp d=1.595A)")
	_add_scene_button(vbox, "H2O", "h2o", "H2O (yellow exp 104.5deg)")
	_add_scene_button(vbox, "NH3", "nh3", "NH3 (yellow exp 107deg)")
	_add_scene_button(vbox, "CH4", "ch4", "CH4 (yellow exp tetra)")
	_add_scene_label(vbox, "")
	_add_scene_label(vbox, "")
	_add_scene_label(vbox, "--- H ISOTOPES ---")
	_add_scene_button(vbox, "H-1 Protium", "h1", "H-1 (🟢SCVC)")
	_add_scene_button(vbox, "H-2 Deuterium", "deuterium", "H-2 (🟢SCVC)")
	_add_scene_button(vbox, "H-3 Tritium", "tritium", "H-3 (🟢SCVC,no decay)")
	_add_scene_button(vbox, "H-4 Quadium", "quadium", "H-4 (🟢SCVC,no decay)")
	_add_scene_label(vbox, "")
	_add_scene_label(vbox, "--- CUSTOM Z ---")
	var z_row = HBoxContainer.new()
	z_row.name = "ZInputRow"
	z_row.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	var z_input = LineEdit.new()
	z_input.name = "ZInput"
	z_input.placeholder_text = "Z (1-118)"
	z_input.custom_minimum_size = Vector2(60, 24)
	z_input.add_theme_font_size_override("font_size", 11)
	z_row.add_child(z_input)
	var z_btn = Button.new()
	z_btn.name = "ZButton"
	z_btn.text = "Go"
	z_btn.custom_minimum_size = Vector2(35, 24)
	z_btn.add_theme_font_size_override("font_size", 11)
	var zbs = StyleBoxFlat.new()
	zbs.bg_color = Color(0.08, 0.1, 0.18, 0.7)
	zbs.border_width_left = 1; zbs.border_color = Color(0.2, 0.7, 0.4, 0.6)
	zbs.corner_radius_top_left = 4; zbs.corner_radius_top_right = 4
	zbs.corner_radius_bottom_left = 4; zbs.corner_radius_bottom_right = 4
	z_btn.add_theme_stylebox_override("normal", zbs)
	z_btn.pressed.connect(_on_z_generate.bind(z_input))
	z_row.add_child(z_btn)
	vbox.add_child(z_row)
	_add_scene_label(vbox, "(Z<=10: SCVC  Z>=11: heuristic)")
	_add_scene_label(vbox, "")
	_add_scene_button(vbox, "CLEAR ALL", "empty", "empty workspace")

func _add_scene_label(parent: VBoxContainer, text: String):
	var lbl = Label.new()
	lbl.text = text
	lbl.add_theme_color_override("font_color", Color(0.4, 0.6, 0.9))
	lbl.add_theme_font_size_override("font_size", 11)
	lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	parent.add_child(lbl)

func _add_scene_button(parent: VBoxContainer, label: String, scene_id: String, hint: String):
	var btn = Button.new()
	btn.text = label
	btn.tooltip_text = hint
	btn.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	btn.custom_minimum_size = Vector2(0, 24)
	var bs = StyleBoxFlat.new()
	bs.bg_color = Color(0.08, 0.1, 0.18, 0.7)
	bs.border_width_left = 1; bs.border_color = Color(0.2, 0.4, 0.7, 0.6)
	bs.corner_radius_top_left = 4; bs.corner_radius_top_right = 4
	bs.corner_radius_bottom_left = 4; bs.corner_radius_bottom_right = 4
	btn.add_theme_stylebox_override("normal", bs)
	var bsh = StyleBoxFlat.new()
	bsh.bg_color = Color(0.15, 0.2, 0.35, 0.9)
	bsh.border_width_left = 1; bsh.border_color = Color(0.3, 0.6, 1.0, 0.8)
	bsh.corner_radius_top_left = 4; bsh.corner_radius_top_right = 4
	bsh.corner_radius_bottom_left = 4; bsh.corner_radius_bottom_right = 4
	btn.add_theme_stylebox_override("hover", bsh)
	btn.pressed.connect(_on_scene_button.bind(scene_id))
	parent.add_child(btn)

func _on_z_generate(z_input: LineEdit):
	var text: String = z_input.text.strip_edges()
	if text.is_valid_int():
		var Z: int = text.to_int()
		_scene_element(Z)
	else:
		status_label.text = "Enter valid Z (1-118)"

func _on_scene_button(scene_id: String):
	_load_scene(scene_id)

func _build_particle_panel():
	var canvas = $CanvasLayer
	_panel = Panel.new()
	_panel.name = "ParticlePanel"
	_panel.position = Vector2(DisplayServer.window_get_size().x - 170, 40)
	_panel.size = Vector2(155, 600)
	var ps = StyleBoxFlat.new()
	ps.bg_color = Color(0.05, 0.05, 0.08, 0.85)
	ps.border_width_left = 1; ps.border_width_right = 1
	ps.border_width_top = 1; ps.border_width_bottom = 1
	ps.border_color = Color(0.3, 0.3, 0.4, 0.8)
	ps.corner_radius_top_left = 8; ps.corner_radius_top_right = 8
	ps.corner_radius_bottom_left = 8; ps.corner_radius_bottom_right = 8
	_panel.add_theme_stylebox_override("panel", ps)
	canvas.add_child(_panel)

	var scroll = ScrollContainer.new()
	scroll.name = "Scroll"
	scroll.position = Vector2(5, 5)
	scroll.size = Vector2(145, 550)
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	_panel.add_child(scroll)

	var vbox = VBoxContainer.new()
	vbox.name = "ButtonList"
	vbox.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	scroll.add_child(vbox)

	_anti_toggle = CheckButton.new()
	_anti_toggle.text = "ANTI-PARTICLE"
	_anti_toggle.toggled.connect(_on_anti_toggled)
	_add_section_label(vbox, "")
	vbox.add_child(_anti_toggle)

	var spin_toggle = CheckButton.new()
	spin_toggle.name = "SpinToggle"
	spin_toggle.text = "SPIN UP"
	spin_toggle.button_pressed = true
	spin_toggle.toggled.connect(_on_spin_toggled)
	vbox.add_child(spin_toggle)

	_add_section_label(vbox, "── QUARKS ──")
	_add_particle_button(vbox, "u(bright)",   Color(0.95, 0.18, 0.06), U_R, MF_U)
	_add_particle_button(vbox, "u(medium)", Color(0.65, 0.12, 0.07), U_G, MF_U)
	_add_particle_button(vbox, "u(dark)",  Color(0.38, 0.06, 0.04), U_B, MF_U)
	_add_particle_button(vbox, "d(bright)",   Color(0.06, 0.9, 0.16), D_R, MF_D)
	_add_particle_button(vbox, "d(medium)", Color(0.05, 0.58, 0.12), D_G, MF_D)
	_add_particle_button(vbox, "d(dark)",  Color(0.03, 0.36, 0.07), D_B, MF_D)

	_add_section_label(vbox, "── LEPTONS ──")
	_add_particle_button(vbox, "electron", Color(0.55, 0.2, 0.85), ELECTRON, MF_E)
	_add_particle_button(vbox, "neutrino", Color(0.85, 0.9, 1.0), NU_E, MF_NU)

	_add_section_label(vbox, "── FULL SM [M] ──")
	_add_particle_button(vbox, "muon",    Color(0.35, 0.1, 0.6),  MUON, MF_MU)
	_add_particle_button(vbox, "tau",     Color(0.25, 0.05, 0.4), TAU, MF_TAU)
	_add_particle_button(vbox, "nu_mu",   Color(0.7, 0.8, 0.95),  NU_MU, MF_NU)
	_add_particle_button(vbox, "nu_tau",  Color(0.6, 0.7, 0.85),  NU_TAU, MF_NU)
	_add_particle_button(vbox, "strange", Color(0.04, 0.48, 0.1), S_R, MF_S)
	_add_particle_button(vbox, "charm",   Color(0.7, 0.14, 0.07), C_R, MF_C)
	_add_particle_button(vbox, "bottom",  Color(0.03, 0.32, 0.07), B_R, MF_B)
	_add_particle_button(vbox, "top",     Color(0.88, 0.16, 0.05), T_R, MF_T)

	update_panel_visibility()

func _add_section_label(parent: VBoxContainer, text: String):
	var lbl = Label.new()
	lbl.text = text
	lbl.add_theme_color_override("font_color", Color(0.5, 0.5, 0.6))
	lbl.add_theme_font_size_override("font_size", 11)
	lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	parent.add_child(lbl)

func _add_particle_button(parent: VBoxContainer, label: String, color: Color, winding: Array, mf: float):
	var btn = Button.new()
	btn.text = label
	btn.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	btn.custom_minimum_size = Vector2(0, 26)
	var bs = StyleBoxFlat.new()
	bs.bg_color = Color(color.r*0.25, color.g*0.25, color.b*0.25, 0.7)
	bs.border_width_left = 2
	bs.border_color = color
	bs.corner_radius_top_left = 4; bs.corner_radius_top_right = 4
	bs.corner_radius_bottom_left = 4; bs.corner_radius_bottom_right = 4
	btn.add_theme_stylebox_override("normal", bs)
	var bsh = StyleBoxFlat.new()
	bsh.bg_color = Color(color.r*0.5, color.g*0.5, color.b*0.5, 0.9)
	bsh.border_width_left = 2; bsh.border_color = color
	bsh.corner_radius_top_left = 4; bsh.corner_radius_top_right = 4
	bsh.corner_radius_bottom_left = 4; bsh.corner_radius_bottom_right = 4
	btn.add_theme_stylebox_override("hover", bsh)
	btn.toggle_mode = true  # stay highlighted when selected
	btn.button_pressed = false
	parent.add_child(btn); _panel_buttons[label] = btn; btn.pressed.connect(_on_panel_button.bind(winding, label, mf))

func _on_panel_button(winding: Array, label: String, mf: float):
	_set_preset(winding, label, mf)
	# Unpress all other buttons, keep this one pressed
	for key in _panel_buttons:
		var b = _panel_buttons[key]
		if is_instance_valid(b): b.button_pressed = (key == label)

func _on_spin_toggled(pressed: bool):
	spin_up = pressed
	var tb = _panel.get_node_or_null("Scroll/ButtonList/SpinToggle")
	if tb: tb.text = "SPIN UP" if pressed else "SPIN DOWN"
	_update_status()

func _on_anti_toggled(pressed: bool):
	placing_anti = pressed
	_update_status()

func update_panel_visibility():
	if not _panel: return
	var in_sm = false
	var scroll = _panel.get_node_or_null("Scroll/ButtonList")
	if not scroll: return
	for child in scroll.get_children():
		if child is Label and child.text.begins_with("── FULL SM"):
			in_sm = true
			child.visible = full_sm_mode
			continue
		if in_sm and child is Button:
			child.visible = full_sm_mode


func is_dragging_vortex() -> bool:
	if physics:
		for v in physics.vortices:
			if is_instance_valid(v) and v.is_dragging: return true
	return false
