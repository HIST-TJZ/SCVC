extends Node3D
# ============================================================
# Physics Parameters
# ============================================================
const R := 2.0
const H := 1.0
var c_sim := 20.0

var v := 1.0
var omega := 2.0 * PI
# ============================================================
# Simulation State
# ============================================================
var sim_time := 0.0
var running := true
var emit_timer := 0.0
var cylinder_launched := false
var t_launch := 0.0
var initial_offset := 2.0
var emit_interval := 0.03
var trajectory_records := []

var active_photons: Array = []
# Language state
var is_chinese := false
var show_misses := false
var periods_locked := true
var use_extrapolation := true
# Translation dictionary
const T := {
	"Pause": { "en": "Pause", "zh": "暂停" },
	"Play": { "en": "Play", "zh": "播放" },
	"Launch": { "en": "Launch", "zh": "发射" },
	"Reset": { "en": "Reset", "zh": "重置" },
	"UnrolledView": { "en": "Unrolled View", "zh": "展开视图" },
	"3DView": { "en": "3D View", "zh": "3D 视图" },
	"BackTo3D": { "en": "Back to 3D", "zh": "返回 3D" },
	"LangToggle": { "en": "中", "zh": "EN" },
	"SpeedLabel": { "en": "Speed v:", "zh": "速度 v:" },
	"OmegaLabel": { "en": "Angular w:", "zh": "角速度 w:" },
	"DebugTime": { "en": "Time:", "zh": "时间:" },
	"DebugCylZ": { "en": "Cyl Bottom Z:", "zh": "圆柱底部 Z:" },
	"DebugAngle": { "en": "Laser Angle:", "zh": "激光角度:" },
	"DebugInside": { "en": "Inside Cylinder:", "zh": "圆柱内:" },
	"DebugPending": { "en": "Pending:", "zh": "待发射:" },
	"DebugPoints": { "en": "Points:", "zh": "轨迹点:" },
	"DebugYes": { "en": "YES", "zh": "是" },
	"DebugNo": { "en": "NO", "zh": "否" },
	"GapLabel": { "en": "Dx = wR^2/c_sim = %.6f m  (%.1f px)", "zh": "Dx = wR^2/c_sim = %.6f \u7c73  (%.1f \u50cf\u7d20)" },
	"TitleUnrolled": { "en": "Unrolled Cylinder Wall  (x = R*theta  |  y = z_hit  |  dots = photon hits)", "zh": "展开圆柱侧面  (x = R*theta  |  y = z_hit  |  圆点 = 光子命中)" },
	"DensityLabel": { "en": "Photons:", "zh": "光子密度:" },
	"MissToggle": { "en": "Show Misses", "zh": "显示未命中" },
	"MissToggleOn": { "en": "Show All", "zh": "显示全部" },
	"CLabel": { "en": "c_sim:", "zh": "模拟光速c:" },
	"OffsetLabel": { "en": "Start Dist:", "zh": "初始距离:" },
	"CMeasured": { "en": "c_meas = %.6f  vs  c_sim = %.6f m/s", "zh": "实测 c = %.6f  对比  设定 c = %.6f m/s" },
	"LockOn": { "en": "Lock T:ON", "zh": "周期锁定:开" },
	"LockOff": { "en": "Lock T:OFF", "zh": "周期锁定:关" },
	"MethodDisc": { "en": "Method: Disc", "zh": "方法: 离散" },
	"MethodExtr": { "en": "Method: Extr", "zh": "方法: 外推" },
}
# ============================================================
# Node References
# ============================================================
@onready var cylinder_rig: Node3D = $CylinderRig
@onready var cylinder_body: CSGCylinder3D = $CylinderRig/CylinderBody
@onready var laser_indicator: MeshInstance3D = $CylinderRig/LaserIndicator
@onready var laser_plane_vis: Node3D = $CylinderRig/LaserPlaneVis
@onready var laser_ring: MeshInstance3D = $CylinderRig/LaserPlaneVis/LaserRing
@onready var laser_dir: MeshInstance3D = $CylinderRig/LaserPlaneVis/LaserDir
@onready var trajectory_container: Node3D = $TrajectoryContainer
# UI nodes
@onready var debug_label: Label = $UI/DebugLabel
@onready var play_pause_btn: Button = $UI/ControlPanel/VBox/BtnRow/PlayPauseBtn
@onready var reset_btn: Button = $UI/ControlPanel/VBox/BtnRow/ResetBtn
@onready var view_toggle_btn: Button = $UI/ControlPanel/VBox/BtnRow/ViewToggleBtn
@onready var lang_toggle_btn: Button = $UI/ControlPanel/VBox/BtnRow/LangToggleBtn
@onready var miss_toggle_btn: Button = $UI/ControlPanel/VBox/BtnRow/MissToggleBtn
@onready var lock_btn: Button = $UI/ControlPanel/VBox/BtnRow/LockBtn
@onready var method_btn: Button = $UI/ControlPanel/VBox/BtnRow/MethodBtn
@onready var speed_slider: HSlider = $UI/ControlPanel/VBox/SpeedRow/SpeedSlider
@onready var speed_value_label: Label = $UI/ControlPanel/VBox/SpeedRow/SpeedValue
@onready var speed_label: Label = $UI/ControlPanel/VBox/SpeedRow/SpeedLabel
@onready var omega_slider: HSlider = $UI/ControlPanel/VBox/OmegaRow/OmegaSlider
@onready var omega_value_label: Label = $UI/ControlPanel/VBox/OmegaRow/OmegaValue
@onready var density_slider: HSlider = $UI/ControlPanel/VBox/DensityRow/DensitySlider
@onready var density_value_label: Label = $UI/ControlPanel/VBox/DensityRow/DensityValue
@onready var c_slider: HSlider = $UI/ControlPanel/VBox/CRow/CSlider
@onready var c_value_label: Label = $UI/ControlPanel/VBox/CRow/CValue
@onready var offset_slider: HSlider = $UI/ControlPanel/VBox/OffsetRow/OffsetSlider
@onready var offset_value_label: Label = $UI/ControlPanel/VBox/OffsetRow/OffsetValue
@onready var offset_label: Label = $UI/ControlPanel/VBox/OffsetRow/OffsetLabel
@onready var c_label: Label = $UI/ControlPanel/VBox/CRow/CLabel
@onready var density_label: Label = $UI/ControlPanel/VBox/DensityRow/DensityLabel
@onready var omega_label: Label = $UI/ControlPanel/VBox/OmegaRow/OmegaLabel
@onready var unrolled_view: Control = $UI/UnrolledView
@onready var unrolled_draw: Control = $UI/UnrolledView/UnrolledDraw
@onready var unrolled_back_btn: Button = $UI/UnrolledView/BackBtn
@onready var gap_label: Label = $UI/UnrolledView/GapLabel
@onready var title_label: Label = $UI/UnrolledView/TitleLabel
var marker_mesh: SphereMesh
var photon_mesh: SphereMesh
var photon_material: StandardMaterial3D
var photon_container: Node3D
# ============================================================
# Translation helper
# ============================================================
func _tr(key: String) -> String:
	var lang := "zh" if is_chinese else "en"
	return T[key][lang]
func _update_all_text() -> void:
	lang_toggle_btn.text = _tr("LangToggle")
	speed_label.text = _tr("SpeedLabel")
	omega_label.text = _tr("OmegaLabel")
	density_label.text = _tr("DensityLabel")
	c_label.text = _tr("CLabel")
	offset_label.text = _tr("OffsetLabel")


	title_label.text = _tr("TitleUnrolled")
	unrolled_back_btn.text = _tr("BackTo3D")
	reset_btn.text = _tr("Reset")
	miss_toggle_btn.text = _tr("MissToggleOn") if show_misses else _tr("MissToggle")
	lock_btn.text = _tr("LockOn") if periods_locked else _tr("LockOff")
	method_btn.text = _tr("MethodExtr") if use_extrapolation else _tr("MethodDisc")
	play_pause_btn.text = _tr("Pause") if cylinder_launched else _tr("Launch")
	view_toggle_btn.text = _tr("3DView") if unrolled_view.visible else _tr("UnrolledView")
	if unrolled_view.visible:
		unrolled_draw.queue_redraw()
# ============================================================
# Lifecycle
# ============================================================
func _ready() -> void:
	photon_container = Node3D.new()
	add_child(photon_container)
	_setup_materials()
	_setup_cylinder()
	_setup_laser_visuals()
	_setup_ui_signals()
	speed_slider.set_value_no_signal(v)
	omega_slider.set_value_no_signal(omega)
	_update_ui_labels()
	unrolled_view.visible = false
	_update_all_text()
func _setup_materials() -> void:
	marker_mesh = SphereMesh.new()
	marker_mesh.radius = 0.04
	marker_mesh.height = 0.08


	# Photon traveling mesh
	photon_mesh = SphereMesh.new()
	photon_mesh.radius = 0.03
	photon_mesh.height = 0.06
	photon_material = StandardMaterial3D.new()
	photon_material.albedo_color = Color(1.0, 0.9, 0.2)
	photon_material.emission_enabled = true
	photon_material.emission = Color(1.0, 0.8, 0.0)
	photon_material.emission_energy_multiplier = 3.0
	photon_material.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED

func _setup_cylinder() -> void:
	var mat := StandardMaterial3D.new()
	mat.albedo_color = Color(0.2, 0.5, 0.8, 0.35)
	mat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	mat.metallic = 0.3
	mat.roughness = 0.6
	mat.cull_mode = BaseMaterial3D.CULL_DISABLED
	cylinder_body.material_override = mat
	cylinder_body.radius = R
	cylinder_body.height = H
func _setup_laser_visuals() -> void:
	var origin_mat := StandardMaterial3D.new()
	origin_mat.albedo_color = Color.RED
	origin_mat.emission_enabled = true
	origin_mat.emission = Color.RED
	origin_mat.emission_energy_multiplier = 3.0
	origin_mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	laser_indicator.material_override = origin_mat
	var ring_mat := StandardMaterial3D.new()
	ring_mat.albedo_color = Color(1.0, 0.3, 0.1, 0.5)
	ring_mat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	ring_mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	ring_mat.cull_mode = BaseMaterial3D.CULL_DISABLED
	laser_ring.material_override = ring_mat
	var dir_mat := StandardMaterial3D.new()
	dir_mat.albedo_color = Color(1.0, 0.2, 0.0)
	dir_mat.emission_enabled = true
	dir_mat.emission = Color(1.0, 0.2, 0.0)
	dir_mat.emission_energy_multiplier = 2.0
	dir_mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	laser_dir.material_override = dir_mat
func _setup_ui_signals() -> void:
	play_pause_btn.pressed.connect(_on_play_pause)
	reset_btn.pressed.connect(_on_reset)
	view_toggle_btn.pressed.connect(_on_view_toggle)
	lang_toggle_btn.pressed.connect(_on_lang_toggle)
	miss_toggle_btn.pressed.connect(_on_miss_toggle)
	lock_btn.pressed.connect(_on_lock_toggle)
	method_btn.pressed.connect(_on_method_toggle)
	unrolled_back_btn.pressed.connect(_on_unrolled_back)
	speed_slider.value_changed.connect(_on_speed_changed)
	omega_slider.value_changed.connect(_on_omega_changed)
	density_slider.value_changed.connect(_on_density_changed)
	c_slider.value_changed.connect(_on_c_changed)
	offset_slider.value_changed.connect(_on_offset_changed)
# ============================================================
# Main Loop
# ============================================================
func _process(delta: float) -> void:


	sim_time += delta
	var z_bottom := -(H + initial_offset) + (v * (sim_time - t_launch) if cylinder_launched else 0.0)
	cylinder_rig.position = Vector3(0, 0, z_bottom)
	var theta := omega * sim_time
	laser_plane_vis.rotation_degrees = Vector3(0, 0, rad_to_deg(theta))
	var laser_inside := (z_bottom <= 0.0) and (0.0 <= z_bottom + H)
	if sim_time < 10.0:
		emit_timer += delta
		while emit_timer >= emit_interval:
			emit_timer -= emit_interval
			var actual_birth := sim_time - emit_timer
			var actual_theta := omega * actual_birth
			_emit_photon(actual_theta, actual_birth)
	_update_photons()
	_update_debug_text(theta, z_bottom, laser_inside)
# ============================================================
# Photon Emission & Arrival
# ============================================================
func _emit_photon(theta: float, birth_time: float) -> void:
	var node := MeshInstance3D.new()
	node.mesh = photon_mesh
	node.material_override = photon_material.duplicate()
	node.position = Vector3.ZERO
	photon_container.add_child(node)
	var dir := Vector3(cos(theta), sin(theta), 0.0)
	active_photons.append({"node": node, "dir": dir, "birth": birth_time, "theta": theta})

func _update_photons() -> void:
	var to_arrive: Array = []
	for p: Dictionary in active_photons:
		var age = sim_time - p.birth
		var dist = c_sim * age
		p.node.position = p.dir * dist
		if dist >= R:
			to_arrive.append(p)
	for p: Dictionary in to_arrive:
		active_photons.erase(p)
		_process_arrival(p)

func _process_arrival(p: Dictionary) -> void:
	p.node.queue_free()
	var theta_emit: float = p.theta
	var t_arrive = p.birth + R / c_sim
	var z_bottom_arrive: float = -(H + initial_offset) + (v * max(0.0, t_arrive - t_launch) if cylinder_launched else 0.0)
	var z_hit_local: float = -z_bottom_arrive
	var world_hit := Vector3(R * cos(theta_emit), R * sin(theta_emit), 0.0)
	if z_hit_local >= 0.0 and z_hit_local <= H:
		var hue := fmod(theta_emit / (2.0 * PI), 1.0)
		var color := Color.from_hsv(hue, 1.0, 1.0)
		trajectory_records.append({"theta": theta_emit, "z_hit": z_hit_local, "color": color, "world_pos": world_hit})
		_spawn_marker(world_hit, color)
		if unrolled_view.visible:
			unrolled_draw.queue_redraw()
	else:
		if show_misses:
			_spawn_miss_marker(world_hit)
func _spawn_marker(world_pos: Vector3, color: Color) -> void:
	var marker := MeshInstance3D.new()
	marker.mesh = marker_mesh
	var mat := StandardMaterial3D.new()
	mat.albedo_color = color
	mat.emission_enabled = true
	mat.emission = color
	mat.emission_energy_multiplier = 2.0
	mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	marker.material_override = mat
	marker.position = world_pos
	trajectory_container.add_child(marker)
# ============================================================
# Debug & UI Labels
# ============================================================
func _update_debug_text(theta: float, z_bottom: float, laser_inside: bool) -> void:
	var theta_deg := fmod(rad_to_deg(theta), 360.0)
	var n := trajectory_records.size()
	var gap: float = omega * R * R / c_sim
	var c_measured: float = 0.0
	if trajectory_records.size() > 0 and cylinder_launched:
		var theta_ref: float = omega * (t_launch + (H + initial_offset) / v)
		if use_extrapolation:
			# ===== ???: ??????????? z=0 =====
			# theta_at_z0 = theta + z_hit * omega/v  (????????? -v/omega)
			# ??????????? theta_at_z0???????
			var sum_c: float = 0.0
			var count_c: int = 0
			for rec in trajectory_records:
				var theta_at_z0: float = rec.theta + rec["z_hit"] * omega / v
				var delta_x: float = R * abs(theta_ref - theta_at_z0)
				if delta_x > 0.00001:
					sum_c += omega * R * R / delta_x
					count_c += 1
			if count_c > 0:
				c_measured = sum_c / float(count_c)
		else:
			# ===== ?????: ???? z=0 ???????? =====
			# ??: ?????? theta, z_hit???? v/omega ????
			# ??: ???????????????????
			var z_best: float = 999.0
			var theta_best: float = 0.0
			for rec in trajectory_records:
				var dz: float = abs(rec["z_hit"])
				if dz < z_best:
					z_best = dz
					theta_best = rec.theta
			var delta_x: float = R * abs(theta_ref - theta_best)
			if delta_x > 0.00001:
				c_measured = omega * R * R / delta_x







	debug_label.text = (
		_tr("DebugTime") + " %.3f s\n" % sim_time +
		_tr("DebugCylZ") + " %.3f\n" % z_bottom +
		_tr("DebugAngle") + " %.1f deg\n" % theta_deg +
		_tr("DebugInside") + " " + (_tr("DebugYes") if laser_inside else _tr("DebugNo")) + "\n" +
		_tr("DebugPending") + " %d  |  " % active_photons.size() +
		_tr("DebugPoints") + " %d\n" % n +
		"v=%.6f  w=%.6f  Gap=%.6f m" % [v, omega, gap] + "\\n" + _tr("CMeasured") % [c_measured, c_sim]
	)
func _update_ui_labels() -> void:
	speed_slider.set_value_no_signal(v)
	omega_slider.set_value_no_signal(omega)
	speed_value_label.text = "%.6f m/s" % v
	omega_value_label.text = "%.6f rad/s" % omega
	density_value_label.text = "%d /s" % int(1.0 / emit_interval)
	c_value_label.text = "%.1f m/s" % c_sim
	offset_value_label.text = "%.2f m" % initial_offset
# ============================================================
# UI Controls
# ============================================================
func _on_play_pause() -> void:
	cylinder_launched = true
	t_launch = sim_time
	play_pause_btn.text = _tr("Pause")
func _on_reset() -> void:
	sim_time = 0.0
	emit_timer = 0.0
	cylinder_launched = false
	t_launch = 0.0
	for ap: Dictionary in active_photons:
		ap.node.queue_free()
	active_photons.clear()
	trajectory_records.clear()

	play_pause_btn.text = _tr("Launch")
	for child in trajectory_container.get_children():
		child.queue_free()
	cylinder_rig.position = Vector3(0, 0, -(H + initial_offset))
	unrolled_draw.queue_redraw()
func _on_view_toggle() -> void:
	unrolled_view.visible = not unrolled_view.visible
	view_toggle_btn.text = _tr("3DView") if unrolled_view.visible else _tr("UnrolledView")
	unrolled_back_btn.visible = unrolled_view.visible
	if unrolled_view.visible:
		unrolled_draw.queue_redraw()
func _on_speed_changed(value: float) -> void:
	v = value
	_update_ui_labels()
	if periods_locked:
		omega = v * 2.0 * PI / H
		omega_slider.set_value_no_signal(omega)
		_update_ui_labels()
func _on_omega_changed(value: float) -> void:
	omega = value
	_update_ui_labels()
	if periods_locked:
		v = H * omega / (2.0 * PI)
		speed_slider.set_value_no_signal(v)
		_update_ui_labels()
func _on_density_changed(value: float) -> void:
	emit_interval = 1.0 / value
	_update_ui_labels()
func _on_lang_toggle() -> void:
	is_chinese = not is_chinese
	_update_all_text()
func _on_unrolled_back() -> void:
	unrolled_view.visible = false
	view_toggle_btn.text = _tr("UnrolledView")
	unrolled_back_btn.visible = false
# ============================================================
# Unrolled View Drawing
# ============================================================
func _on_unrolled_draw() -> void:
	var circumference := 2.0 * PI * R
	var view_w := unrolled_draw.size.x
	var view_h := unrolled_draw.size.y
	var grid_c := Color(1, 1, 1, 0.08)
	for i in range(5):
		var x_px := remap(i * circumference / 4.0, 0.0, circumference, 0.0, view_w)
		unrolled_draw.draw_line(Vector2(x_px, 0), Vector2(x_px, view_h), grid_c)
	for i in range(6):
		var y_px := remap(i * H / 5.0, 0.0, H, view_h, 0.0)
		unrolled_draw.draw_line(Vector2(0, y_px), Vector2(view_w, y_px), grid_c)
	for rec: Dictionary in trajectory_records:
		var theta_mod: float = fmod(rec.theta, 2.0 * PI)
		var sx := remap(R * theta_mod, 0.0, circumference, 0.0, view_w)
		var sy: float = remap(rec["z_hit"], 0.0, H, view_h, 0.0)
		unrolled_draw.draw_circle(Vector2(sx, sy), 3.0, rec.color)
	var gap: float = omega * R * R / c_sim
	var gap_px := remap(gap, 0.0, circumference, 0.0, view_w)
	var yellow := Color(1, 1, 0, 0.7)
	for i in range(6):
		var x_px := remap(i * gap, 0.0, circumference, 0.0, view_w)
		if x_px < view_w:
			unrolled_draw.draw_line(Vector2(x_px, 0), Vector2(x_px, view_h), yellow, 1.0)
	var c_meas_ur: float = 0.0
	if trajectory_records.size() > 0 and cylinder_launched:
		var theta_ref_ur: float = omega * (t_launch + (H + initial_offset) / v)
		if use_extrapolation:
			# ???: ? debug ????
			var sum_c_ur: float = 0.0
			var count_c_ur: int = 0
			for rec2 in trajectory_records:
				var theta_at_z0_ur: float = rec2.theta + rec2["z_hit"] * omega / v
				var delta_x_ur: float = R * abs(theta_ref_ur - theta_at_z0_ur)
				if delta_x_ur > 0.00001:
					sum_c_ur += omega * R * R / delta_x_ur
					count_c_ur += 1
			if count_c_ur > 0:
				c_meas_ur = sum_c_ur / float(count_c_ur)
		else:
			# ?????
			var z_best_ur: float = 999.0
			var theta_best_ur: float = 0.0
			for rec2 in trajectory_records:
				var dz_ur: float = abs(rec2["z_hit"])
				if dz_ur < z_best_ur:
					z_best_ur = dz_ur
					theta_best_ur = rec2.theta
			var delta_x_ur: float = R * abs(theta_ref_ur - theta_best_ur)
			if delta_x_ur > 0.00001:
				c_meas_ur = omega * R * R / delta_x_ur







	gap_label.text = _tr("GapLabel") % [gap, gap_px] + "\\n" + _tr("CMeasured") % [c_meas_ur, c_sim]
	var lbl_c := Color(1, 1, 1, 0.3)
	unrolled_draw.draw_string(ThemeDB.fallback_font, Vector2(5, 14), "2piR = %.2f" % circumference, HORIZONTAL_ALIGNMENT_LEFT, -1, 11, lbl_c)
	unrolled_draw.draw_string(ThemeDB.fallback_font, Vector2(5, view_h - 4), "H = %.2f" % H, HORIZONTAL_ALIGNMENT_LEFT, -1, 11, lbl_c)
# ============================================================
# Missed Photon Marker
# ============================================================
func _spawn_miss_marker(world_pos: Vector3) -> void:
	var marker := MeshInstance3D.new()
	var miss_mesh := SphereMesh.new()
	miss_mesh.radius = 0.025
	miss_mesh.height = 0.05
	marker.mesh = miss_mesh
	var mat := StandardMaterial3D.new()
	mat.albedo_color = Color(0.4, 0.4, 0.4, 0.5)
	mat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	marker.material_override = mat
	marker.position = world_pos
	trajectory_container.add_child(marker)
func _on_miss_toggle() -> void:
	show_misses = not show_misses
	miss_toggle_btn.text = _tr("MissToggleOn") if show_misses else _tr("MissToggle")
func _on_c_changed(value: float) -> void:
	c_sim = value
	_update_ui_labels()
func _on_method_toggle() -> void:
	use_extrapolation = not use_extrapolation
	method_btn.text = _tr("MethodExtr") if use_extrapolation else _tr("MethodDisc")
	unrolled_draw.queue_redraw()

func _on_lock_toggle() -> void:
	periods_locked = not periods_locked
	lock_btn.text = _tr("LockOn") if periods_locked else _tr("LockOff")
	method_btn.text = _tr("MethodExtr") if use_extrapolation else _tr("MethodDisc")
	if periods_locked:
		omega = v * 2.0 * PI / H
		omega_slider.set_value_no_signal(omega)
		_update_ui_labels()
func _on_offset_changed(value: float) -> void:
	initial_offset = value
	_update_ui_labels()
