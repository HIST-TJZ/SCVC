# vortex_ring.gd -- SCVC 1D Vortex Ring
# Leptons (no color charge) are represented as closed vortex rings.
# The ring is a topological defect in the CP^2 BEC: N segments connected
# by springs, with quantized circulation kappa.
#
# Physics:
#   Magnus force: F_M = RHO_S * circulation * (v x n)  [RHO_S = 2*pi^2/3]
#   Ring self-energy: E = RHO_S*R/(4*pi)*[log(8R/xi)-2-1/3] + E_CORE*mf*|w|^2
#   SCALE SEPARATION: ring radius R ~ 0.1 sim (intrinsic, ~1 fm)
#                    orbital radius ~ 4000 sim (Bohr, NOT simulated to scale)
#   EM interaction with other particles via ring-quark / ring-ring forces
#
# Topological consequences (automatic, no postulates):
#   Circulation kappa = h/m_e  ->  discrete Bohr orbits (Magnus+Coulomb balance)
#   Ring circulation direction ->  spin +/- 1/2
#   Ring tilt                 ->  l quantum number
#   Two rings same orientation ->  topological repulsion (Pauli exclusion)

class_name VortexRing
extends Node3D

static var batch_render: bool = true  # GPU instancing for ring segments/springs

# SCVC winding (same 4D structure as point vortex, but w_c1=w_c2=0 for leptons)
var w_c1: float = 0.0
var w_c2: float = 0.0
var w_w:  float = 0.0
var w_y:  float = 0.0
var mass_factor: float = 1.0

# Ring geometry
var radius: float = 0.15  # R_eq = XI*e/8 = 0.085; 0.15 for visibility
var normal: Vector3 = Vector3.UP
var num_segments: int = 12
var circulation: float = 1.0

# Dynamics
var center_velocity: Vector3 = Vector3.ZERO
var angular_velocity: float = 0.0
var force_accum: Vector3 = Vector3.ZERO
var target_orbit_radius: float = 0.0  # SCVC-locked orbital radius (constrained mode)
var reference_radius: float = 0.0  # Fixed reference radius for free-ring tension (prevents expansion chasing)
var nucleus_position: Vector3 = Vector3.ZERO
var _rotation_phase: float = 0.0  # current rotation angle for constrained orbit
var is_dragging: bool = false

# Internal
var _segment_nodes: Array = []
var _spring_nodes: Array = []
var _segment_velocities: Array = []
var _active: bool = false

# Physics constants (matching vortex_physics.gd)
const G_EM: float = 2.00
const XI: float = 0.25
const RHO_S_EFFECTIVE: float = 6.5797   # = 2*pi^2/3 (GP vortex geometry, same as G_sim factor)
# SCVC derived constants (R2: Magnus-Bohr two-radius picture)
# R_ring(intrinsic) = XI*e/8 = 0.085 sim (~1.1 fm) ->ring self-size, GP energy minimum
# R_orbit(Bohr)     = n^2 * 4016 sim (~n^2 * 0.529 A) ->orbital radius, Magnus+Coulomb
# SCALE SEPARATION: R_orbit/R_ring ~ 47,000 ->orbital dynamics too slow for real-time sim
# In simulation: compressed orbital scale (R_orbit ~ 5-15 sim) for visual demonstration
const A0_SIM: float = 4016.1               # Bohr radius in sim units

# SCVC Slater shielding constants (from 09_Slater常数_几何推导结果.md)
# sigma_same = F0(nl,nl) / (2*<1/r>), pure Coulomb geometry
const SLATER_SAME_N1: float = 0.3125   # 1s-1s shielding = 5/16
const SLATER_SAME_N2: float = 0.3477   # n=2 shell weighted average
const SLATER_SAME_N3: float = 0.3561   # n=3 shell weighted average
const SLATER_INNER: float = 0.85       # inner-shell electron shielding
const F_MAGNUS_PER_V: float = 78.96        # N*RHO_S = Magnus force per unit velocity (N=12)
const H_SIM: float = 2.603                 # Planck constant in sim units
const HBAR_SIM: float = 0.414              # Reduced Planck constant
const SIM_LENGTH_M: float = 1.32e-14       # 1 sim unit in meters
const SIM_TIME_S: float = 3.32e-21         # 1 sim time unit in seconds
const ALPHA_CURV: float = 0.0071            # Vortex curvature coefficient (R4: electron-anchored)
const SPRING_K: float = 80.0
const DAMPING: float = 0.999  # near-conservative: ring orbit survives ~1000 frames (~17s) before significant decay

func _ready():
	pass  # Built on activate

func activate(pos: Vector3, _wc1: float, _wc2: float, _ww: float, _wy: float, _mf: float = 1.0):
	w_c1 = _wc1; w_c2 = _wc2; w_w = _ww; w_y = _wy
	mass_factor = _mf
	position = pos
	center_velocity = Vector3.ZERO
	active = true
	_build_ring()

func deactivate():
	_clear_ring()
	_active = false
	visible = false

func _build_ring():
	_clear_ring()
	_segment_nodes.clear()
	_spring_nodes.clear()
	_segment_velocities.clear()

	for i in range(num_segments):
		var angle = float(i) / num_segments * TAU
		var local_pos = _segment_local_pos(angle)

		# Segment sphere
		var seg = MeshInstance3D.new()
		seg.name = "Seg%d" % i
		var sm = SphereMesh.new()
		sm.radius = 0.08; sm.height = 0.16
		sm.radial_segments = 8; sm.rings = 4
		seg.mesh = sm
		var mat = StandardMaterial3D.new()
		var col = display_color()
		mat.albedo_color = col
		mat.emission_enabled = true
		mat.emission = col * 1.5
		mat.emission_energy_multiplier = 2.0
		mat.roughness = 0.3
		seg.material_override = mat
		seg.position = local_pos
		add_child(seg)
		_segment_nodes.append(seg)
		_segment_velocities.append(Vector3.ZERO)

	# Spring cylinders between segments
	for i in range(num_segments):
		var j = (i + 1) % num_segments
		var sp = MeshInstance3D.new()
		sp.name = "RingSpring%d" % i
		var cm = CylinderMesh.new()
		cm.top_radius = 0.03; cm.bottom_radius = 0.03; cm.height = 1.0
		sp.mesh = cm
		var smat = StandardMaterial3D.new()
		smat.albedo_color = Color(0.3, 0.5, 0.9, 0.7)
		smat.emission_enabled = true
		smat.emission = Color(0.2, 0.4, 0.8)
		smat.emission_energy_multiplier = 1.0
		smat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
		smat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
		sp.material_override = smat
		sp.position = (_segment_local_pos(float(i)/num_segments*TAU) + _segment_local_pos(float(j)/num_segments*TAU)) * 0.5
		add_child(sp)
		_spring_nodes.append(sp)

	# Normal indicator (small arrow)
	var arrow = MeshInstance3D.new()
	arrow.name = "NormalIndicator"
	var cm2 = CylinderMesh.new()
	cm2.top_radius = 0.04; cm2.bottom_radius = 0.02; cm2.height = 0.5
	arrow.mesh = cm2
	arrow.position = normal * (radius + 0.3)
	var amat = StandardMaterial3D.new()
	amat.albedo_color = Color(1.0, 0.3, 0.3)
	amat.emission_enabled = true
	amat.emission = Color(0.8, 0.2, 0.2)
	add_child(arrow)
	_arrow_node = arrow

	_update_springs()

var _arrow_node: MeshInstance3D = null

func _segment_local_pos(angle: float) -> Vector3:
	# Position on ring in local coordinates
	var right = _get_right()
	var fwd = right.cross(normal).normalized()
	return (right * cos(angle) + fwd * sin(angle)) * radius

func _get_right() -> Vector3:
	if abs(normal.dot(Vector3.UP)) > 0.999:
		return Vector3.RIGHT
	return normal.cross(Vector3.UP).normalized()

func _clear_ring():
	for n in _segment_nodes:
		if is_instance_valid(n): n.queue_free()
	for s in _spring_nodes:
		if is_instance_valid(s): s.queue_free()
	if _arrow_node and is_instance_valid(_arrow_node):
		_arrow_node.queue_free()
		_arrow_node = null
	_segment_nodes.clear()
	_spring_nodes.clear()

# Safe look_at that avoids colinear up-vector error
func _safe_look_at(node: Node3D, target: Vector3, up: Vector3 = Vector3.UP):
	var to_target := target - node.global_position
	if to_target.length_squared() < 0.000001:
		return
	var dir := to_target.normalized()
	if abs(dir.dot(up)) > 0.999:
		# Direction nearly parallel to up -> use alternative up
		var alt_up = Vector3.RIGHT if abs(up.dot(Vector3.RIGHT)) < 0.9 else Vector3.FORWARD
		node.look_at(target, alt_up)
	else:
		node.look_at(target, up)

func _update_springs():
	for i in range(num_segments):
		var j = (i + 1) % num_segments
		if i >= _spring_nodes.size(): break
		var sp = _spring_nodes[i]
		if not is_instance_valid(sp): continue
		var a = _segment_nodes[i]; var b = _segment_nodes[j]
		if not is_instance_valid(a) or not is_instance_valid(b): continue
		var mid = (a.position + b.position) * 0.5
		var dist = a.position.distance_to(b.position)
		sp.position = mid
		if dist > 0.01:
			_safe_look_at(sp, b.global_position, Vector3.UP)
			sp.scale = Vector3(1, dist, 1)

	if _arrow_node and is_instance_valid(_arrow_node):
		_arrow_node.position = normal * (radius + 0.3)
		_safe_look_at(_arrow_node, global_position + normal * 2.0, Vector3.UP)

## SCVC HONESTY: The orbit is a CONSTRAINT from topological quantization
## (kappa = h/m_e), not from classical force balance. Classical dynamics
## cannot spontaneously yield quantum stability at orbital scale.
##
## Constrained mode (target_orbit_radius > 0): ring center = nucleus,
## segments rotate at omega = hbar/(m_e * r^2). No radial dynamics.
##
## Free mode: original force-based dynamics for non-orbital rings.
func physics_update(delta: float, external_forces_per_segment: Array):
	if not _active: return

	# ===== BRANCH 1: CONSTRAINED ORBIT (target_orbit_radius > 0) =====
	if target_orbit_radius > 0.0:
		_physics_constrained(delta)
		return

	# ===== BRANCH 2: FREE DYNAMICS (non-orbital, e.g. e+e- pair) =====
	# Apply forces to each segment
	for i in range(num_segments):
		if i >= _segment_nodes.size(): break
		var seg = _segment_nodes[i]
		if not is_instance_valid(seg): continue

		var force = Vector3.ZERO

		# External force (from point vortices, other rings)
		if i < external_forces_per_segment.size():
			force += external_forces_per_segment[i]

		# Spring forces from neighbors
		var prev_i = (i - 1 + num_segments) % num_segments
		var next_i = (i + 1) % num_segments
		var prev_seg = _segment_nodes[prev_i]
		var next_seg = _segment_nodes[next_i]
		if is_instance_valid(prev_seg):
			var to_prev = prev_seg.position - seg.position
			var rest_len = 2.0 * radius * sin(PI / num_segments)
			var stretch = to_prev.length() - rest_len
			force += to_prev.normalized() * SPRING_K * stretch
		if is_instance_valid(next_seg):
			var to_next = next_seg.position - seg.position
			var rest_len = 2.0 * radius * sin(PI / num_segments)
			var stretch = to_next.length() - rest_len
			force += to_next.normalized() * SPRING_K * stretch

		# Ring tension: pull toward ideal circle at FIXED reference radius
		# Uses reference_radius to avoid expansion chasing (VFM self-induction expands rings)
		var angle = float(i) / num_segments * TAU
		var saved_radius = radius
		radius = max(reference_radius, 0.1)  # use fixed ref, not dynamic
		var ideal_pos = _segment_local_pos(angle)
		radius = saved_radius  # restore for display
		var radial_offset = seg.position - ideal_pos
		force -= radial_offset * 15.0  # radial restoration toward ref_radius

		# Magnus force DISABLED: VFM B-S already handles this.
		# Segment-velocity Magnus causes double-counting -> runaway oscillation.
		# var v_seg = _segment_velocities[i] if i < _segment_velocities.size() else Vector3.ZERO
		# var magnus = RHO_S_EFFECTIVE * circulation * v_seg.cross(normal)
		# force += magnus

		# Update velocity
		var mf_inertia = mass_factor
		_segment_velocities[i] += force * delta / max(mf_inertia, 0.01)
		_segment_velocities[i] *= DAMPING

		# Update position
		seg.position += _segment_velocities[i] * delta
		if is_nan(seg.position.x) or is_nan(seg.position.y) or is_nan(seg.position.z): seg.position = Vector3.ZERO

	# Recalculate ring center
	var new_center = Vector3.ZERO
	for seg in _segment_nodes:
		if is_instance_valid(seg): new_center += seg.position
	new_center /= float(num_segments)
	# Recenter: displacement drives ring movement, NOT abs position reset
	for seg in _segment_nodes:
		if is_instance_valid(seg):
			seg.position -= new_center
	position += new_center
	center_velocity = new_center / max(delta, 0.0001)

	# Recalculate radius
	var avg_r = 0.0
	for seg in _segment_nodes:
		if is_instance_valid(seg):
			avg_r += seg.position.length()
	radius = avg_r / float(num_segments)

	_update_springs()


## CONSTRAINED ORBIT: ring center HARD-LOCKED to nucleus.
## Rotation from topological quantization kappa = h/m_e.
## No radial dynamics. No external forces. No Magnus balance needed.
## Spring forces maintain ring shape only.
func _physics_constrained(delta: float):
	# 1. HARD CONSTRAINT: ring center orbits nucleus at fixed radius
	#    SCVC: the ring center IS at the Bohr orbital radius.
	#    Radii come from alpha = 1/137.036, not from classical force balance.
	#    omega = hbar / (m_e * r^2) from topological quantization kappa = h/m_e.
	var omega_orbit: float = HBAR_SIM / max(mass_factor * target_orbit_radius * target_orbit_radius, 0.001)
	_rotation_phase += omega_orbit * delta
	_rotation_phase = fmod(_rotation_phase, TAU)

	# Ring center at orbital distance from nucleus, rotating at omega
	var orbit_dir: Vector3 = Vector3(cos(_rotation_phase), 0, sin(_rotation_phase))
	position = nucleus_position + orbit_dir * target_orbit_radius

	# 2. Position each segment on the ring at its angle
	for i in range(num_segments):
		if i >= _segment_nodes.size():
			break
		var seg = _segment_nodes[i]
		if not is_instance_valid(seg):
			continue

		# Segment angle: fixed offset around ring + same orbital phase
		var seg_angle: float = float(i) / num_segments * TAU + _rotation_phase
		var target_pos: Vector3 = _segment_local_pos(seg_angle)
		# Hard-set to ideal position: no convergence -> no oscillation
		seg.position = target_pos

		# Store tangential velocity for reference
		if i < _segment_velocities.size():
			var tangent: Vector3 = normal.cross(target_pos.normalized())
			_segment_velocities[i] = tangent * omega_orbit * target_orbit_radius

	# 3. Update springs (visual only)
	_update_springs()

	# radius: stays at what setup_bohr_orbit set (visual ring size, NOT physical R_eq)
	center_velocity = Vector3.ZERO




## VFM update: apply Biot-Savart velocities directly.
## In VFM at T=0: ds/dt = v_superfluid. Segments advect with the flow.
## Velocities pre-computed, merged with gauge/Pauli contributions.
## Spring forces + ring tension maintain shape.
func physics_update_vfm(delta: float):
	if not _active:
		return

	var vfm_vels = get_meta("_vfm_velocities", null)
	if vfm_vels == null or vfm_vels.size() < num_segments:
		return

	for i in range(num_segments):
		if i >= _segment_nodes.size():
			break
		var seg = _segment_nodes[i]
		if not is_instance_valid(seg):
			continue

		var velocity: Vector3 = vfm_vels[i]

		# Spring forces from neighbors
		var prev_i: int = (i - 1 + num_segments) % num_segments
		var next_i: int = (i + 1) % num_segments
		var prev_seg = _segment_nodes[prev_i]
		var next_seg = _segment_nodes[next_i]
		var spring_force: Vector3 = Vector3.ZERO
		if is_instance_valid(prev_seg):
			var to_prev: Vector3 = prev_seg.position - seg.position
			var rest_len: float = 2.0 * radius * sin(PI / num_segments)
			var stretch: float = to_prev.length() - rest_len
			spring_force += to_prev.normalized() * SPRING_K * stretch
		if is_instance_valid(next_seg):
			var to_next: Vector3 = next_seg.position - seg.position
			var rest_len: float = 2.0 * radius * sin(PI / num_segments)
			var stretch: float = to_next.length() - rest_len
			spring_force += to_next.normalized() * SPRING_K * stretch

		# Ring tension: pull toward ideal circle
		var angle: float = float(i) / num_segments * TAU
		var ideal_pos: Vector3 = _segment_local_pos(angle)
		var radial_offset: Vector3 = seg.position - ideal_pos
		spring_force -= radial_offset * 15.0

		# Convert spring/tension forces to velocity contribution
		var mf_inertia: float = max(mass_factor, 0.01)
		velocity += spring_force * delta / mf_inertia

		if i < _segment_velocities.size():
			_segment_velocities[i] = velocity

		seg.position += velocity * delta
		if is_nan(seg.position.x) or is_nan(seg.position.y) or is_nan(seg.position.z): seg.position = Vector3.ZERO

	# Recalculate ring center
	var new_center: Vector3 = Vector3.ZERO
	for seg in _segment_nodes:
		if is_instance_valid(seg):
			new_center += seg.position
	new_center /= float(num_segments)
	for seg in _segment_nodes:
		if is_instance_valid(seg):
			seg.position -= new_center
	position += new_center
	center_velocity = new_center / max(delta, 0.0001)

	# Recalculate radius
	var avg_r: float = 0.0
	for seg in _segment_nodes:
		if is_instance_valid(seg):
			avg_r += seg.position.length()
	radius = avg_r / float(num_segments)

	_update_springs()

func display_color() -> Color:
	var cmag = sqrt(w_c1*w_c1 + w_c2*w_c2)
	if cmag < 0.08:
		# Lepton colors (tinted by spin: UP=brighter, DOWN=darker)
		var spin: float = 1.0 if angular_velocity >= 0 else 0.55
		if w_w < -0.1 and w_y < -0.1:
			# electron: purple (spin UP) / dark purple (spin DOWN)
			return Color(0.55 * spin, 0.2 * spin, 0.85 * spin)
		if w_w > 0.1 and w_y > 0.1:
			# positron: gold
			return Color(1.0, 0.7, 0.1) * spin
		if w_w > 0.1 and w_y < -0.3:
			return Color(0.85, 0.9, 1.0)      # neutrino: ice white
		if w_w < -0.1 and w_y > 0.3:
			return Color(1.0, 0.7, 0.75)      # anti-neutrino: pale rose
		return Color(0.35, 0.1, 0.6)
	return Color(0.5, 0.5, 0.55)

func charge() -> float:
	return w_w + w_y


# Place ring at a Bohr-like orbit (compressed scale for demo)
# n: principal quantum number (1,2,3...)
# nucleus_pos: position of the atomic nucleus
# For correct Magnus-Coulomb balance, ring normal must be parallel to orbital angular momentum
func setup_bohr_orbit(n: int, nucleus_pos: Vector3, Z: int = 1, scale_compression: float = 400.0, angle_deg: float = 0.0, zeff: float = -1.0):
	# True Bohr radius: n^2 * A0_SIM (~4016 sim for n=1)
	# Compressed for visual demo: divide by scale_compression
	var r_orbit = float(n * n) * A0_SIM / (max(zeff if zeff > 0.0 else float(Z), 0.1) * scale_compression)
	r_orbit = clamp(r_orbit, 2.0, 60.0)

	# Ring normal parallel to orbital angular momentum
	normal = Vector3.UP

	# Initialize rotation phase from angle offset (radians)
	_rotation_phase = angle_deg * PI / 180.0

	# Initial ring center position at orbital distance
	position = nucleus_pos + Vector3(cos(_rotation_phase), 0, sin(_rotation_phase)) * r_orbit

	# SCVC HONESTY: In constrained mode, the orbit is a TOPOLOGICAL CONSTRAINT.
	# kappa = h/m_e -> omega = hbar/(m_e * r^2). The ring center is hard-locked
	# to this orbit by _physics_constrained(). No Magnus-Coulomb balance needed.
	# center_velocity is unused in constrained mode (center = hard-set each frame).

	# VISUALIZATION: use visible ring radius (NOT physical R_eq = 0.085 sim)
	# Enlarged for visual clarity at orbital scale
	radius = clamp(r_orbit * 0.08, 0.4, 3.0)

	# Reposition segments to new visual radius
	for i in range(num_segments):
		if i < _segment_nodes.size() and is_instance_valid(_segment_nodes[i]):
			var angle = float(i) / num_segments * TAU
			_segment_nodes[i].position = _segment_local_pos(angle)

	target_orbit_radius = r_orbit
	nucleus_position = nucleus_pos
	reference_radius = radius  # store initial visual radius
	return r_orbit

# R3 Pauli exclusion: three-region potential (I2 SCVC: normal-aware spin)
# Barrier = E_CORE = 2.132 sim = 1.02 MeV (derived from GP winding argument)
# Same-spin (w_dot > 0): REPULSION  |  Opposite-spin (w_dot <= 0): NO REPULSION
func pauli_potential(other_ring, distance: float) -> float:
	var w_dot = w_w * other_ring.w_w + w_y * other_ring.w_y
	# Opposite spin: velocity fields cancel -> no repulsion (Pauli allowed!)
	if w_dot <= 0.0:
		return 0.0
	var R = max(radius, other_ring.radius)
	var dc = 2.0 * R
	if distance < dc:
		# Region I: core overlap -> constant E_CORE barrier
		return 2.1322 * (w_dot / 0.5)
	elif distance < dc + XI:
		# Region II: near-field exponential decay, lambda = R*sqrt(2)
		var lam = R * sqrt(2.0)
		return 2.1322 * exp(-(distance - dc) / lam) * (w_dot / 0.5)
	else:
		# Region III: Ampere dipole-dipole, 1/d^3
		return RHO_S_EFFECTIVE * pow(R, 4) / pow(distance, 3) * (w_dot / 0.5)

func core_energy() -> float:
	# R4 COMPLETE CLOSURE: E_curv + E_ring = 0 at R=R_eq -> point-particle limit
	# E_total = E_CORE*mf*|w|^2 + E_curv + E_ring + E_spin
	var w2 = w_c1*w_c1 + w_c2*w_c2 + w_w*w_w + w_y*w_y
	# 1) Core energy (mf LINEAR rule, B1-verified)
	var e_core = 2.1322 * mass_factor * w2
	# 2) Curvature correction (per-ring FIXED, NOT proportional to mf!)
	var xi_over_r = XI / max(radius, 0.001)
	var e_curv = 2.1322 * ALPHA_CURV * xi_over_r
	# 3) Ring geometric energy (standard superfluid)
	var log_arg = max(8.0 * radius / XI, 1.01)
	var e_ring = RHO_S_EFFECTIVE * radius / (4.0 * PI) * (log(log_arg) - 2.0)
	# 4) F=1 spinor coupling (quarks only: w_c1^2+w_c2^2 ~ 1)
	var wc2 = w_c1*w_c1 + w_c2*w_c2
	var e_spin = RHO_S_EFFECTIVE * wc2 / (radius / XI + 1.0)
	return max(e_core + e_curv + e_ring + e_spin, 0.5)

func get_segment_world_pos(i: int) -> Vector3:
	if i < _segment_nodes.size() and is_instance_valid(_segment_nodes[i]):
		return to_global(_segment_nodes[i].position)  # FIXED: was local, now world
	# Fallback
	var angle = float(i) / num_segments * TAU
	return position + _segment_local_pos(angle)

func get_segment_nodes() -> Array:
	return _segment_nodes

func get_spring_nodes() -> Array:
	return _spring_nodes

func get_spin_direction() -> int:
	# +1 = counterclockwise (spin up), -1 = clockwise (spin down)
	return 1 if angular_velocity >= 0 else -1

# Properties
var active: bool:
	get: return _active
	set(v): _active = v

func _exit_tree():
	_clear_ring()
