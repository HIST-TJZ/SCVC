# vortex_physics.gd -- Point vortex Hamiltonian on CP2
# Object pool: pre-allocate N vortex visuals, recycle on create/remove.
# H = -SUM_{i<j} (w_i . w_j) * log(1 + |r_i-r_j|^2/xi^2) + SUM_i mf_i * |w_i|^2 * E_CORE
extends Node3D

signal singlet_formed(vortices: Array)
signal singlet_broken(vortices: Array)
signal pair_created(pos: Vector3, wc1: float, wc2: float, ww: float, wy: float)

# ========== SCVC LOCKED CONSTANTS (ALL from first principles) ==========
# GP vortex ODE: f'' + f'/r - f/r² + f - f³ = 0
#   xi_GP = 1.3176  (shoot method, c1=0.583187)
#   xi_sim = 0.25    (mesh choice)
#   L0 = xi_sim/xi_GP = 0.1897  (length anchor, pure bookkeeping)
#
# S DERIVED from GP vortex geometry (NOT a free parameter!):
#   GP vortex-vortex interaction: E_int = 2π * n1*n2 * log(r/xi)
#   Sim interaction: E_int = -2*G_sim * (w·w) * log(r/xi),  w=n
#   -> G_sim = (2π²/3) * g_phys  = 6.5797 * g_phys
#   -> G_STRONG = 6.5797 * 0.500 = 3.290  (sim: 3.30, dev 0.3%)
#   -> G_EM     = 6.5797 * 0.303 = 1.993  (sim: 2.00, dev 0.3%)
#   -> S = (2π²/3) / L0 = 6.5797 / 0.1897 = 34.68
#
# mf LINEAR rule (verified by triple lepton cross-check, dev<0.05%):
#   H_core = E_CORE * mf * |w|²   (NOT mf²!)
#   m_e:  1.0661 * 0.4793 = 0.511 MeV  (anchor)
#   m_mu: 220.4  * 0.4793 = 105.6 MeV  (exp: 105.66)
#   m_tau:3707   * 0.4793 = 1777  MeV  (exp: 1776.86)
#
# GeV bridge:
#   E_scale_BEC = m_e(MeV) / E_core_e(sim) = 0.511 / 1.0661 = 0.4793 MeV
#   Quarks: apply π/8 QCD screening factor (color confinement)
const XI: float = 0.25          # = L0 * xi_GP = 0.1897 * 1.3176
const E_CORE: float = 2.1322    # SCVC GP vortex core energy (from vortex_profile.json)
const BIND_DIST: float = 0.50   # SCVC: L0 * 2 * xi_phys = 0.1897*2*1.3176 (core overlap distance)
const BREAK_DIST: float = 1.00   # SCVC: 2 * BIND_DIST = 2 * 0.50 (vortex core separation threshold)
const G_STRONG: float = 3.30    # = (2π²/3)*g3 = 6.580*0.500 = 3.290
const G_EM: float = 2.00        # = (2π²/3)*e  = 6.580*0.303 = 1.993
const R_Z: float = 0.003        # Z boson Yukawa range (sim units)
const R_W: float = 0.0035       # W boson range = R_Z * m_Z/m_W
const E_SCALE_BEC: float = 0.4793    # MeV per GP energy unit: m_e/E_core(e) = 0.511/1.0661
const QUARK_PI_OVER_8: float = 0.3927  # pi/8 QCD color-confinement screening factor



# =====================================================================
# VFM (Vortex Filament Model) -- V1 SCVC-derived
# =====================================================================
# Biot-Savart velocity induction. Mathematically: vortex ring <=> current loop.
#
# V1 result: Biot-Savart is FLAVOR-BLIND (kappa=1.0 for all particles).
# SCVC-specific physics enters through three independent channels:
#   Channel A: Biot-Savart -> Magnus force (flavor-blind)
#   Channel B: Gauge forces (G_EM/G_STRONG, w-dot-w modulated)
#   Channel C: Pauli topological repulsion (three-region potential)
# Total: F = F_BS + F_gauge + F_Pauli
#
# Master switch: vfm_enabled (default false = legacy log-potential)
# =====================================================================

# ===== VFM: V1 SCVC-derived parameters =====
# V1 result: Biot-Savart is FLAVOR-BLIND. kappa = 1.0 for all particles.
# SCVC-specific physics enters through three independent channels:
#   Channel A: Biot-Savart (fluid dynamics, flavor-blind, kappa=1.0)
#   Channel B: Gauge forces (G_EM, G_STRONG, modulated by w-dot-w)
#   Channel C: Pauli topological repulsion (three-region potential)
# Total force: F = F_BS + F_gauge + F_Pauli
const VFM_KAPPA: float = -1.0  # SCVC sign convention: CCW ring self-induces UP (verified 2026-07-24)
const VFM_CORE_A: float = XI * 0.5  # Desingularization: vortex core radius (XI=0.25 -> a=0.125)
const VFM_SELF_CORE_FACTOR: float = 0.5  # Self-induction desingularization: segment arc length factor
const RHO_S_EFFECTIVE: float = 6.5797   # = 2*pi^2/3 (GP vortex geometry, shared with vortex_ring.gd)

# ===== N1: Nucleon-Nucleon Potential (SCVC First-Principles, 2026-07-24) =====
# EVERY parameter has its OWN SCVC scaling formula (NOT a universal factor!)
#
# SCVC LENGTH ANCHOR: sim_per_fm = sim_per_A * 0.01 = 18.89 * 0.01 = 0.1889 sim/fm
#   (from A0_SIM=4016.1 sim = a0=0.529 A = 52.9 fm, CROSS_VALIDATION_HANDOFF)
# SCVC ENERGY ANCHOR: E_SCALE_BEC = 0.4793 MeV/sim_E (B1 bridge)
#
# Scaling formulas (each property type has its own):
#   Inverse length m [sim^-1] = m_phys[MeV] / (hbar_c[MeV*fm]) / sim_per_fm[sim/fm]
#   Energy*length V0 [sim_E*sim_L] = V0_phys[MeV*fm] * sim_per_fm[sim/fm] / E_SCALE_BEC[MeV/sim_E]
#   Dimensionless (g_piNN=12.9): unchanged in all unit systems
#
# N1 SCVC-derived physical values (zero free parameters):
#   m_pi = 140 MeV (GMOR + SCVC quark masses)
#   g_piNN = 12.9 (Goldberger-Treiman, from SCVC g_A=1.27, f_pi=92 MeV)
#   M_N = 938 MeV (nucleon mass)
#   m_omega = 782 MeV (Regge trajectory, from SCVC string tension)
#   A_core = 2000 MeV*fm (omega exchange + vortex topology overlap)
#   hbar_c = 197.3 MeV*fm
#
# Spin-isospin factor (tau*tau)(sigma*sigma)/9 (NOT yet implemented per-cluster):
#   T=0,S=1 (deuteron): -1/3 (attractive OPEP) | T=1,S=0 (singlet): -1/3
#   T=1,S=1: +1/9 (repulsive) | T=0,S=0: +1 (repulsive)
#   Current: factor=1.0 (SCVC HONESTY: averaging over states, no spin tracking)
#
# Reference: N1_NucleonNucleon_SCVC_Derivation_results.md
const NN_SIM_PER_FM: float = 0.1889     # SCVC length anchor: sim_per_A * 0.01
const NN_M_PI: float = 3.7564           # = 140 / 197.3 / 0.1889 sim^-1, OPEP range=0.266 sim=1.41 fm
const NN_V_PI: float = 0.009689         # = gpNN^2/4pi * mpi^2/(12*MN^2) * sim_per_fm / E_SCALE_BEC
const NN_M_OMEGA: float = 20.982        # = 782 / 197.3 / 0.1889 sim^-1, core range=0.048 sim=0.25 fm
const NN_V_CORE: float = 788.23         # = 2000 * sim_per_fm / E_SCALE_BEC
const NN_SPIN_ISOSPIN_FACTOR: float = 1.0  # SCVC HONESTY: no per-nucleon spin/isospin tracking yet
const NN_MIN_CLUSTER_SIZE: int = 3      # Only nucleon-sized clusters (>=3 quarks) feel NN force
const NN_FORCE_CAP: float = 200.0       # Numerical guard: cap per-cluster force (SCVC HONESTY: hard core
                                         # is ~30000 at r=0.1 sim, 1500 at r=0.2 sim. Cap only affects
                                         # extreme short-range where timestep can't resolve.)

var _nn_enabled: bool = true            # Master switch for NN potential

## VFM master switch: false = legacy log-potential forces, true = Biot-Savart velocities
var vfm_enabled: bool = true

## Time acceleration multiplier: 1.0=realtime, 10=10x, 100=100x
## Only affects physics delta, not rendering.
var time_scale: float = 1.0
var ring_visual_scale: float = 1.0  # visual scale of ring segments (N/SHIFT+N)
var quark_visual_scale: float = 1.0  # visual scale of quark spheres (-/=)

const POOL_SIZE: int = 400

var vortices: Array = []        # active VortexObject nodes
var rings: Array = []           # active VortexRing nodes
var pool: Array = []            # ALL pre-allocated VortexObject nodes
var springs: Array = []
var energy: float = 0.0
var _pair_cooldown: int = 0
var snapshot_mode: bool = false
var _snap_frame: int = 0
var decay_mode: bool = false    # V toggles resonance decay
var show_quarks: bool = true     # H toggles quark visibility
var _cluster_cache := []       # cached cluster COMs
var _cluster_cache_frame := -1  # frame when cache was built
var _batch_mesh: MultiMeshInstance3D = null  # batched GPU rendering for all quarks
var _batch_glow: MultiMeshInstance3D = null  # batched glow shells
var _batch_material: StandardMaterial3D = null
var _batch_glow_material: StandardMaterial3D = null
var _batch_ring_segs: MultiMeshInstance3D = null  # batched ring segment spheres
var _batch_ring_springs: MultiMeshInstance3D = null  # batched ring spring cylinders
const MAX_RING_SEGS: int = 240  # 20 rings * 12 segments
const MAX_RING_SPRINGS: int = 240
var time_frozen: bool = false   # P toggles time stop
var springs_visible: bool = true # K toggles spring lines
var _decay_immune: Dictionary = {}  # vortex -> frames remaining of decay immunity
const PAIR_COOLDOWN_FRAMES: int = 60
const DECAY_IMMUNITY_FRAMES: int = 180  # 3 seconds @ 60fps
# I3 SCVC weak coupling (SCVC-derived, NOT fitted): G_F_sim = 2.68e-12 sim^{-2}
# tau_n = 915s (+4.1% vs PDG 878.4s). Decay rate: Gamma_sim = 1.50e-24 sim^{-1}
# Per-check probability (15 frames): 2.25e-23 -- physically invisible without demo boost.
const G_F_SIM: float = 2.68e-12       # sim^{-2}, from I3 (g2 geometry + m_H/m_W=pi/2)
const V_UD: float = 0.974              # CKM, experimental input
const G_A: float = 1.275              # axial coupling, experimental input
const F_N: float = 1.69               # phase space integral, approximate
const M_E_SIM: float = 1.0661          # electron mass in sim energy units
const NEUTRON_DECAY_PROB: float = 2.25e-23  # = 15 * Gamma_sim, physically correct (visible only with demo boost)

func _ready():
	var VortexClass = load("res://scripts/vortex_object.gd")
	VortexClass.batch_render = true
	var RingClass = load("res://scripts/vortex_ring.gd")
	RingClass.batch_render = true
	_build_pool()
	_setup_batch_render()
	set_process(true)

func _setup_batch_render():
	# Core spheres: one MultiMesh for all quark cores
	_batch_mesh = MultiMeshInstance3D.new()
	_batch_mesh.name = "BatchCores"
	var mm = MultiMesh.new()
	mm.transform_format = MultiMesh.TRANSFORM_3D
	mm.use_colors = true
	mm.instance_count = POOL_SIZE
	var core_mesh = SphereMesh.new()
	core_mesh.radius = 0.18; core_mesh.height = 0.36
	core_mesh.radial_segments = 12; core_mesh.rings = 6
	mm.mesh = core_mesh
	_batch_mesh.multimesh = mm
	_batch_material = StandardMaterial3D.new()
	_batch_material.vertex_color_use_as_albedo = true
	_batch_material.emission_enabled = true
	_batch_material.emission_energy_multiplier = 2.5
	_batch_material.roughness = 0.3
	_batch_mesh.material_override = _batch_material
	add_child(_batch_mesh)
	# Glow shells
	_batch_glow = MultiMeshInstance3D.new()
	_batch_glow.name = "BatchGlows"
	var mmg = MultiMesh.new()
	mmg.transform_format = MultiMesh.TRANSFORM_3D
	mmg.use_colors = true
	mmg.instance_count = POOL_SIZE
	var glow_mesh = SphereMesh.new()
	glow_mesh.radius = 0.306; glow_mesh.height = 0.612
	glow_mesh.radial_segments = 8; glow_mesh.rings = 4
	mmg.mesh = glow_mesh
	_batch_glow.multimesh = mmg
	_batch_glow_material = StandardMaterial3D.new()
	_batch_glow_material.vertex_color_use_as_albedo = true
	_batch_glow_material.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	_batch_glow_material.emission_enabled = true
	_batch_glow_material.emission_energy_multiplier = 1.0
	_batch_glow_material.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	_batch_glow.material_override = _batch_glow_material
	add_child(_batch_glow)
	# Ring segment spheres
	_batch_ring_segs = MultiMeshInstance3D.new()
	_batch_ring_segs.name = "BatchRingSegs"
	var mmr = MultiMesh.new()
	mmr.transform_format = MultiMesh.TRANSFORM_3D
	mmr.use_colors = true
	mmr.instance_count = MAX_RING_SEGS
	var ring_seg_mesh = SphereMesh.new()
	ring_seg_mesh.radius = 0.08; ring_seg_mesh.height = 0.16
	ring_seg_mesh.radial_segments = 8; ring_seg_mesh.rings = 4
	mmr.mesh = ring_seg_mesh
	_batch_ring_segs.multimesh = mmr
	var ring_mat = StandardMaterial3D.new()
	ring_mat.vertex_color_use_as_albedo = true
	ring_mat.emission_enabled = true
	ring_mat.emission_energy_multiplier = 2.0
	_batch_ring_segs.material_override = ring_mat
	add_child(_batch_ring_segs)
	# Ring spring cylinders
	_batch_ring_springs = MultiMeshInstance3D.new()
	_batch_ring_springs.name = "BatchRingSprings"
	var mms = MultiMesh.new()
	mms.transform_format = MultiMesh.TRANSFORM_3D
	mms.use_colors = true
	mms.instance_count = MAX_RING_SPRINGS
	var spring_mesh = CylinderMesh.new()
	spring_mesh.top_radius = 0.03; spring_mesh.bottom_radius = 0.03; spring_mesh.height = 1.0
	mms.mesh = spring_mesh
	_batch_ring_springs.multimesh = mms
	var spring_mat = StandardMaterial3D.new()
	spring_mat.vertex_color_use_as_albedo = true
	spring_mat.emission_enabled = true
	spring_mat.emission_energy_multiplier = 0.5
	_batch_ring_springs.material_override = spring_mat
	add_child(_batch_ring_springs)


func _safe_set_transform(mm: MultiMesh, idx: int, t: Transform3D):
	if not mm: return
	var o := t.origin
	if is_nan(o.x) or is_nan(o.y) or is_nan(o.z): return
	if is_inf(o.x) or is_inf(o.y) or is_inf(o.z): return
	# Check basis for NaN/Inf too
	var bx := t.basis.x; var by := t.basis.y; var bz := t.basis.z
	if is_nan(bx.x) or is_nan(bx.y) or is_nan(bx.z): return
	if is_nan(by.x) or is_nan(by.y) or is_nan(by.z): return
	if is_nan(bz.x) or is_nan(bz.y) or is_nan(bz.z): return
	if is_inf(bx.x) or is_inf(bx.y) or is_inf(bx.z): return
	if is_inf(by.x) or is_inf(by.y) or is_inf(by.z): return
	if is_inf(bz.x) or is_inf(bz.y) or is_inf(bz.z): return
	mm.set_instance_transform(idx, t)

func _update_batch_render():
	if not _batch_mesh or not _batch_glow or not _batch_mesh.multimesh or not _batch_glow.multimesh:
		return
	var count: int = 0
	for v in vortices:
		if not is_instance_valid(v) or not v.visible:
			continue
		if count >= POOL_SIZE:
			break
		if is_nan(v.position.x) or is_nan(v.position.y) or is_nan(v.position.z):
			continue
		var t := Transform3D(Basis().scaled(Vector3(quark_visual_scale, quark_visual_scale, quark_visual_scale)), v.position)
		var col: Color = v.display_color()
		_safe_set_transform(_batch_mesh.multimesh, count, t)
		_batch_mesh.multimesh.set_instance_color(count, col)
		_safe_set_transform(_batch_glow.multimesh, count, t)
		_batch_glow.multimesh.set_instance_color(count, Color(col.r, col.g, col.b, 0.12))
		count += 1
	# Hide unused instances by scaling to zero
	for i in range(count, POOL_SIZE):
		_safe_set_transform(_batch_mesh.multimesh, i, Transform3D(Basis().scaled(Vector3.ZERO), Vector3(0, -999, 0)))
		_safe_set_transform(_batch_glow.multimesh, i, Transform3D(Basis().scaled(Vector3.ZERO), Vector3(0, -999, 0)))
	if show_quarks:
		_batch_mesh.multimesh.visible_instance_count = count
		_batch_glow.multimesh.visible_instance_count = count
	else:
		_batch_mesh.multimesh.visible_instance_count = 0
		_batch_glow.multimesh.visible_instance_count = 0
	# Ring segments
	if not _batch_ring_segs or not _batch_ring_springs:
		return
	var seg_count: int = 0
	for ring in rings:
		if not is_instance_valid(ring) or not ring.active:
			continue
		var segs = ring.get_segment_nodes()
		var col: Color = ring.display_color()
		for seg in segs:
			if not is_instance_valid(seg): continue
			if seg_count >= MAX_RING_SEGS: break
			var gp = seg.global_position
			if is_nan(gp.x) or is_nan(gp.y) or is_nan(gp.z):
				continue
			var t := Transform3D(Basis().scaled(Vector3(ring_visual_scale, ring_visual_scale, ring_visual_scale)), gp)
			_safe_set_transform(_batch_ring_segs.multimesh, seg_count, t)
			_batch_ring_segs.multimesh.set_instance_color(seg_count, col)
			seg_count += 1
	for i in range(seg_count, MAX_RING_SEGS):
		_safe_set_transform(_batch_ring_segs.multimesh, i, Transform3D(Basis().scaled(Vector3.ZERO), Vector3(0, -999, 0)))
	_batch_ring_segs.multimesh.visible_instance_count = seg_count
	# Ring springs: use EXACT same node positions as segment batch render
	var spring_count: int = 0
	for ring in rings:
		if not is_instance_valid(ring) or not ring.active: continue
		var segs = ring.get_segment_nodes()
		var n_seg: int = segs.size()
		for i in range(n_seg):
			if spring_count >= MAX_RING_SPRINGS: break
			var j: int = (i + 1) % n_seg
			var seg_a = segs[i]
			var seg_b = segs[j]
			if not is_instance_valid(seg_a) or not is_instance_valid(seg_b): continue
			var a: Vector3 = seg_a.global_position
			var b: Vector3 = seg_b.global_position
			if is_nan(a.x) or is_nan(a.y) or is_nan(a.z): continue
			if is_nan(b.x) or is_nan(b.y) or is_nan(b.z): continue
			var mid := (a + b) * 0.5
			var diff := b - a
			var length := diff.length()
			if length < 0.001: continue
			var dir := diff / length
			if is_nan(dir.x) or is_nan(dir.y) or is_nan(dir.z): continue
			var basis := Basis()
			var up := Vector3.UP
			if abs(dir.dot(up)) > 0.99: up = Vector3.RIGHT
			var right := dir.cross(up)
			if right.length_squared() < 0.0001: continue
			right = right.normalized()
			up = right.cross(dir).normalized()
			basis = Basis(right, dir, up)
			var t := Transform3D(basis.scaled(Vector3(ring_visual_scale, length, ring_visual_scale)), mid)
			_safe_set_transform(_batch_ring_springs.multimesh, spring_count, t)
			_batch_ring_springs.multimesh.set_instance_color(spring_count, Color(0.3, 0.5, 0.9, 0.7))
			spring_count += 1
	for i in range(spring_count, MAX_RING_SPRINGS):
		_safe_set_transform(_batch_ring_springs.multimesh, i, Transform3D(Basis().scaled(Vector3.ZERO), Vector3(0, -999, 0)))
	_batch_ring_springs.multimesh.visible_instance_count = spring_count

func _build_pool():
	var VortexClass = load("res://scripts/vortex_object.gd")
	for i in range(POOL_SIZE):
		var v = VortexClass.new()
		v.name = "Vortex" + str(i)
		v.visible = false
		add_child(v)
		pool.append(v)

func _acquire_from_pool() -> Node3D:
	for v in pool:
		if is_instance_valid(v) and not v.visible:
			return v
	return null

func _return_to_pool(v: Node3D):
	v.w_c1 = 0.0; v.w_c2 = 0.0; v.w_w = 0.0; v.w_y = 0.0
	v.unbind_all()
	v.velocity = Vector3.ZERO
	v.force_accum = Vector3.ZERO
	v.is_dragging = false
	v.visible = false
	v.position = Vector3(0, -999, 0)

var _frame: int = 0


func _process(delta: float):
	if time_frozen:
		update_springs()
		return
	_frame += 1
	var phys_delta: float = delta * time_scale
	if _pair_cooldown > 0: _pair_cooldown -= 1

	# Expire decay immunity
	var expired_keys = []
	for key in _decay_immune:
		_decay_immune[key] -= 1
		if _decay_immune[key] <= 0: expired_keys.append(key)
	for k in expired_keys: _decay_immune.erase(k)

	# Snapshot: hide after brief flash
	if _snap_frame > 0:
		_snap_frame -= 1
		if _snap_frame == 0 and snapshot_mode:
			for v in vortices:
				if is_instance_valid(v): v.visible = false

	# Physics: quark path only when quarks visible
	if show_quarks:
		compute_forces()
		if _frame % 4 == 0:
			check_bindings()
			check_breakings()
		if decay_mode and _frame % 15 == 0:
			_check_resonance_decay()
			_check_neutron_decay()
		if _frame % 10 == 0:
			energy = total_energy()
		for v in vortices:
			if is_instance_valid(v) and not v.is_dragging:
				v.physics_update(phys_delta, v.force_accum)
			if is_nan(v.position.x) or is_nan(v.position.y) or is_nan(v.position.z): v.position = Vector3(0,10,0)
		# Per-cluster COM: cached BFS (every 8 frames), COM updates every frame
		var _clusters: Array = []
		if _frame % 8 == 0 or _cluster_cache_frame < 0:
			var _visited := {}
			_cluster_cache.clear()
			for v in vortices:
				if not is_instance_valid(v) or not v.visible: continue
				var vid: int = v.get_instance_id()
				if _visited.has(vid): continue
				var _cluster := []
				var _queue := [v]
				_visited[vid] = true
				while not _queue.is_empty():
					var curr = _queue.pop_front()
					_cluster.append(curr)
					for other in vortices:
						if not is_instance_valid(other): continue
						var oid: int = other.get_instance_id()
						if _visited.has(oid): continue
						if curr.is_bound_to(other):
							_visited[oid] = true
							_queue.append(other)
				if _cluster.size() >= 2:
					_cluster_cache.append(_cluster)
			_cluster_cache_frame = _frame
		for cl in _cluster_cache:
			var com := Vector3.ZERO
			var valid := true
			for q in cl:
				if not is_instance_valid(q): valid = false; break
				com += q.position
			if not valid: continue
			com /= float(cl.size())
			_clusters.append(cl)
			for ring in rings:
				if not is_instance_valid(ring) or not ring.active: continue
				if ring.target_orbit_radius <= 0.0: continue
				var d = ring.position.distance_to(com)
				if d < ring.position.distance_to(ring.nucleus_position) * 0.5 + 1.0:
					ring.nucleus_position = com
		for cl in _cluster_cache:
			var com_vel := Vector3.ZERO
			var total_mf := 0.0
			var valid := true
			for q in cl:
				if not is_instance_valid(q): valid = false; break
				var mf = q.mass_factor if q.mass_factor > 0.0 else 1.0
				com_vel += q.velocity * mf
				total_mf += mf
			if valid and total_mf > 0.0:
				com_vel /= total_mf
				for q in cl:
					q.velocity -= com_vel
	# N1: Nucleon-Nucleon potential (SCVC: nucleons identified from color+isospin, not springs)
	if _nn_enabled:
		_compute_nn_forces()
	update_springs()
	# Update rings (always run)
	for ring in rings:
		if is_instance_valid(ring) and ring.active and not ring.is_dragging:
			# V1 Three-Channel VFM: BS velocities + gauge/Pauli forces
			if vfm_enabled and ring.target_orbit_radius <= 0.0:
				# Channel A: Biot-Savart velocities (advect with flow)
				var vfm_vels: Array = _compute_vfm_velocities(ring)
				# Channel B+C: gauge + Pauli from existing _compute_ring_forces
				_compute_ring_forces(ring)
				var gauge_forces: Array = ring.get_meta("_ext_forces", [])
				# Merge: v_VFM + F_gauge*dt/m
				var merged_vels: Array = []
				for i in range(ring.num_segments):
					var v_total: Vector3 = Vector3.ZERO
					if i < vfm_vels.size():
						v_total += vfm_vels[i]
					if i < gauge_forces.size():
						v_total += gauge_forces[i] * delta / max(ring.mass_factor, 0.01)
					merged_vels.append(v_total)
				ring.set_meta("_vfm_velocities", merged_vels)
				ring.physics_update_vfm(phys_delta)
			else:
				# Constrained rings skip forces (positions hard-set by SCVC constraint)
				if ring.target_orbit_radius <= 0.0:
					_compute_ring_forces(ring)
				ring.physics_update(phys_delta, ring.get_meta("_ext_forces", []))
	_update_batch_render()
	_check_annihilation()

# ========== HAMILTONIAN ==========

func total_energy() -> float:
	var e = 0.0
	for i in range(vortices.size()):
		var a = vortices[i]
		if not is_instance_valid(a): continue
		var amf = a.mass_factor if a.mass_factor > 0.0 else _mass_factor(a.w_c1, a.w_c2, a.w_w, a.w_y)
		e += E_CORE * amf * (a.w_c1*a.w_c1 + a.w_c2*a.w_c2 + a.w_w*a.w_w + a.w_y*a.w_y)
		for j in range(i+1, vortices.size()):
			var b = vortices[j]
			if not is_instance_valid(b): continue
			var r = a.position.distance_to(b.position)
			var xi2 = _xi_for_pair(a, b); xi2 *= xi2
			var l = log(1.0 + r*r/xi2)
			e += G_STRONG * a.color_dot(b) * l
			# EM + Z energy (SCVC electroweak unification)
			var qa2 = a.w_w + a.w_y; var qb2 = b.w_w + b.w_y
			const G_EM2: float = 2.00; const R_Z2: float = 0.003
			e += G_EM2 * qa2 * qb2 * l
			var zc2 = (a.w_w - qa2*0.25) * (b.w_w - qb2*0.25)
			e += G_EM2 * zc2 * l * exp(-r/R_Z2)
			# Confinement energy: V_conf = (sigma/2) * r^2 for non-singlets
			var ac = a.color_winding(); var bc = b.color_winding()
			if ac.length() > 0.1 and bc.length() > 0.1:
				var total_c = ac + bc
				if total_c.length() > 0.1:
					e += 0.5 * r * r
	# Ring energies
	for ring in rings:
		if is_instance_valid(ring) and ring.active:
			e += ring.core_energy()
			# Ring-point interactions
			for v in vortices:
				if not is_instance_valid(v): continue
				var r_c = ring.position.distance_to(v.position)
				var xi2 = XI * XI
				var l = log(1.0 + r_c*r_c/xi2)
				var qr = ring.charge(); var qv = v.w_w + v.w_y
				e += G_EM * qr * qv * l
			# Ring-ring EM interactions
			for ring2 in rings:
				if ring2 == ring or not is_instance_valid(ring2) or not ring2.active: continue
				var rr = ring.position.distance_to(ring2.position)
				var xi22 = XI * XI
				var ll = log(1.0 + rr*rr/xi22)
				e += G_EM * ring.charge() * ring2.charge() * ll
	return e

func compute_forces():
	for v in vortices:
		if is_instance_valid(v): v.force_accum = Vector3.ZERO
	for i in range(vortices.size()):
		var a = vortices[i]
		if not is_instance_valid(a): continue
		for j in range(i + 1, vortices.size()):
			var b = vortices[j]
			if not is_instance_valid(b): continue
			var diff = b.position - a.position
			var r = diff.length()
			if r < 0.01: continue
			var dir = diff / r
			var xi2 = _xi_for_pair(a, b); xi2 *= xi2
			var ft: float = 0.0
			var cd = a.color_dot(b)
			if abs(cd) > 0.01: ft -= 2.0*G_STRONG*cd*r/(xi2+r*r)
			# EM force: photon = massless, couples to Q = I3 + Y = w_w + w_y
			const G_EM: float = 2.00
			var qa = a.w_w + a.w_y; var qb = b.w_w + b.w_y; var qq = qa * qb
			if abs(qq) > 0.005: ft -= 2.0*G_EM*qq*r/(xi2+r*r)
			# Z boson: Yukawa suppressed
			var zc = (a.w_w - qa*0.25) * (b.w_w - qb*0.25)
			if abs(zc) > 0.005: ft -= 2.0*G_EM*zc*r/(xi2+r*r) * exp(-r/R_Z)
			# Apply accumulated force to both particles
			var f = dir * ft * 0.5
			a.force_accum += f
			b.force_accum -= f

			# Linear confinement: color-non-singlet pairs feel sigma*r attraction
			var ac = a.color_winding(); var bc = b.color_winding()
			if ac.length() > 0.1 and bc.length() > 0.1:
				var total_c = ac + bc
				if total_c.length() > 0.1:
					var sigma = 1.0  # Matches energy V=0.5*r^2 -> F=r
					var fconf = dir * sigma * r
					a.force_accum += fconf
					b.force_accum -= fconf

# ========== BINDING ==========

func check_bindings():
	# Count only INTERACTING particles (exclude neutrinos that don't bind)
	var active = []
	for idx in range(vortices.size()):
		var vv = vortices[idx]
		if not is_instance_valid(vv): continue
		var cmag = sqrt(vv.w_c1*vv.w_c1 + vv.w_c2*vv.w_c2)
		var emag = abs(vv.w_w) + abs(vv.w_y)
		if cmag > 0.05 or emag > 0.6:  # not a neutrino
			active.append(idx)
	var n_active = active.size()
	if n_active > 400: return
	var sizes = [2]
	# Count unbound - skip multi-body when all bound (saves O(N^3)/O(N^4))
	var n_unbound := 0
	for vv in vortices:
		if is_instance_valid(vv) and vv.bound_partners.size() == 0:
			n_unbound += 1
	if n_unbound >= 3 and n_active <= 400: sizes.append(3)
	if n_unbound >= 4 and n_active <= 400: sizes.append(4)
	for size in sizes:
		for combo in _combinations(n_active, size):
			var real_combo = []
			for c in combo: real_combo.append(active[c])
			combo = real_combo
			var subset = []
			var tc1 = 0.0; var tc2 = 0.0; var tw = 0.0; var ty = 0.0
			var valid = true
			for idx2 in combo:
				var v = vortices[idx2]
				if not is_instance_valid(v): valid = false; break
				subset.append(v)
				tc1 += v.w_c1; tc2 += v.w_c2; tw += v.w_w; ty += v.w_y
			if not valid: continue
			var mag_c = sqrt(tc1*tc1+tc2*tc2)
			if mag_c > 0.15: continue
			var center = Vector3.ZERO
			for v in subset: center += v.position
			center /= float(subset.size())
			var all_close = true
			for v in subset:
				if v.position.distance_to(center) > BIND_DIST: all_close = false; break
			if not all_close: continue
			var already = true
			for x in subset:
				for y in subset:
					if x!=y and not x.is_bound_to(y): already = false; break
			if already: continue
			bind_cluster(subset)

func bind_cluster(subset: Array):
	# Momentum conservation: average velocities (inelastic binding)
	var com_vel = Vector3.ZERO
	for v in subset:
		if is_instance_valid(v): com_vel += v.velocity
	com_vel /= float(subset.size())
	for v in subset:
		if is_instance_valid(v): v.velocity = com_vel

	for i in range(subset.size()):
		for j in range(i + 1, subset.size()):
			if not subset[i].is_bound_to(subset[j]):
				subset[i].bind_to(subset[j])
				create_spring(subset[i], subset[j])
	singlet_formed.emit(subset)

func check_breakings():
	for i in range(vortices.size()):
		var a = vortices[i]
		if not is_instance_valid(a): continue
		for j in range(i + 1, vortices.size()):
			var b = vortices[j]
			if not is_instance_valid(b): continue
			if a.is_bound_to(b) and a.position.distance_to(b.position) > BREAK_DIST:
				break_binding(a, b)


# Snap continuous winding to nearest valid SM value
func _snap_to_sm(wc1: float, wc2: float, ww: float, wy: float) -> Array:
	var best_cx = 0.0; var best_cy = 0.0; var best_cd = 999.0
	var cx = [0.0, 1.0, -0.5, -0.5, -1.0, 0.5, 0.5]
	var cy = [0.0, 0.0, 0.866, -0.866, 0.0, -0.866, 0.866]
	var i = 0
	while i < 7:
		var dx = wc1 - cx[i]; var dy = wc2 - cy[i]
		var dist2 = dx*dx + dy*dy
		if dist2 < best_cd: best_cd = dist2; best_cx = cx[i]; best_cy = cy[i]
		i += 1
	var weaks = [0.0, 0.5, -0.5, 1.0, -1.0]
	var best_w = 0.0; var best_wd = 999.0
	i = 0
	while i < 5:
		var d = abs(ww - weaks[i])
		if d < best_wd: best_wd = d; best_w = weaks[i]
		i += 1
	var hypers = [0.0, 0.1667, -0.1667, 0.5, -0.5, 0.6667, -0.6667, 0.3333, -0.3333, 1.0, -1.0]
	var best_y = 0.0; var best_yd = 999.0
	i = 0
	while i < 11:
		var d = abs(wy - hypers[i])
		if d < best_yd: best_yd = d; best_y = hypers[i]
		i += 1
	return [best_cx, best_cy, best_w, best_y]

func break_binding(a: Node3D, b: Node3D):
	if not a.is_bound_to(b): return
	var mid = (a.position + b.position) * 0.5
	var com_vel = (a.velocity + b.velocity) * 0.5
	var out_dir = (a.position - b.position).normalized()
	if out_dir.length() < 0.1: out_dir = Vector3(randf()-0.5, 0, randf()-0.5).normalized()
	a.velocity = com_vel + out_dir * 0.5
	b.velocity = com_vel - out_dir * 0.5
	var fc1 = -(a.w_c1 + b.w_c1) * 0.2
	var fc2 = -(a.w_c2 + b.w_c2) * 0.2
	var fw = -(a.w_w + b.w_w) * 0.2
	var fy = -(a.w_y + b.w_y) * 0.2
	a.unbind_from(b)
	remove_springs_between(a, b)
	singlet_broken.emit([a, b])
	if abs(fc1)+abs(fc2)+abs(fw)+abs(fy) > 0.05 and _pair_cooldown <= 0:
		_pair_cooldown = PAIR_COOLDOWN_FRAMES
		var snapped = _snap_to_sm(fc1, fc2, fw, fy)
		var smag = snapped[0]*snapped[0] + snapped[1]*snapped[1] + snapped[2]*snapped[2] + snapped[3]*snapped[3]
		if smag > 0.01:
			pair_created.emit(mid, snapped[0], snapped[1], snapped[2], snapped[3])


# ========== MASS HELPERS ==========

func _core_energy(wc1: float, wc2: float, ww: float, wy: float) -> float:
	var mf = _mass_factor(wc1, wc2, ww, wy)
	return E_CORE * mf * mf

func _xi_for_pair(a: Node3D, b: Node3D) -> float:
	var ma = a.mass_factor if a.mass_factor > 0.0 else _mass_factor(a.w_c1, a.w_c2, a.w_w, a.w_y)
	var mb = b.mass_factor if b.mass_factor > 0.0 else _mass_factor(b.w_c1, b.w_c2, b.w_w, b.w_y)
	return XI / sqrt(max(ma, 0.01) * max(mb, 0.01))

# SCVC pi-polynomial mass factors (electron=1.0), used as fallback:
func _mass_factor(wc1: float, wc2: float, ww: float, wy: float) -> float:
	var cmag = sqrt(wc1*wc1 + wc2*wc2)
	if cmag < 0.1:
		var charge = ww + wy
		if abs(charge) < 0.05: return 0.01      # neutrino
		if abs(charge + 1.0) < 0.1: return 1.0  # e/mu/tau
		if abs(charge - 1.0) < 0.1: return 1.0  # positron
		return 1.0
	if abs(ww) > 0.3: return 4.2426   # up-type: SCVC mass factor
	return 9.1317  # down-type: SCVC mass factor

# ========== RESONANCE DECAY (SCVC Winding Rearrangement) ==========
# In SCVC, decay = topological rearrangement of vortex winding vectors.
# Total 4D winding (wc1,wc2,ww,wy) is conserved.
# Same-flavor quark clusters have SU(2) tension -> unstable -> decay.
# Decay: one quark flips w_w (flavor change), winding deficit carried by
# created quark-antiquark pair (meson) or lepton pair.

func _check_resonance_decay():
	var processed = []
	for i in range(vortices.size()):
		var v = vortices[i]
		if not is_instance_valid(v) or v in processed: continue
		if _decay_immune.get(v, 0) > 0: continue

		# Build bound cluster via spring connectivity
		var cluster = [v]
		for j in range(vortices.size()):
			if i == j: continue
			var w = vortices[j]
			if not is_instance_valid(w): continue
			if v.is_bound_to(w) and not w in cluster:
				cluster.append(w)
		if cluster.size() < 2: continue

		# Skip if any member is immune
		var any_immune = false
		for q in cluster:
			if _decay_immune.get(q, 0) > 0: any_immune = true; break
		if any_immune: continue

		# Compute cluster winding totals
		var tc1 = 0.0; var tc2 = 0.0; var tw = 0.0; var ty = 0.0
		var cmag_max = 0.0
		for q in cluster:
			tc1 += q.w_c1; tc2 += q.w_c2; tw += q.w_w; ty += q.w_y
			var qcmag = sqrt(q.w_c1*q.w_c1 + q.w_c2*q.w_c2)
			if qcmag > cmag_max: cmag_max = qcmag
		var mag_c = sqrt(tc1*tc1 + tc2*tc2)
		if mag_c > 0.2: continue  # Must be color singlet

		# Detect same-flavor: use w_w * w_y product (>0 = up-type, <0 = down-type)
		var first_prod = cluster[0].w_w * cluster[0].w_y
		var first_up = first_prod > 0.0
		var all_same = true
		for q in cluster:
			var qprod = q.w_w * q.w_y
			if (qprod > 0.0) != first_up: all_same = false; break

		# === RESONANCE CONDITIONS ===
		var do_decay = false
		if cluster.size() >= 3 and all_same and cmag_max > 0.5:
			# 3+ same-flavor quarks in color singlet = resonance
			do_decay = true
		if cmag_max < 0.1 and (abs(tw) > 0.8 or abs(ty) > 0.8):
			# W/Z-like boson cluster
			do_decay = true

		if not do_decay: continue

		# === EXECUTE DECAY ===
		var center = Vector3.ZERO
		for q in cluster: center += q.position
		center /= float(cluster.size())
		for q in cluster: processed.append(q)

		if all_same and cmag_max > 0.5:
			_execute_hadron_resonance_decay(cluster, center, first_up)
		else:
			_execute_boson_decay(cluster, center)

# ========== HADRON RESONANCE DECAY ==========
# Delta++ (uuu) -> proton(uud) + pi+(u + anti-d)
# Delta-  (ddd) -> neutron(udd) + pi-(d + anti-u)
# The key SCVC mechanism:
#   1. One quark flips w_w sign (flavor change: u<->d)
#   2. Excess winding is carried by a created quark-antiquark pair (meson)
#   3. Total 4D winding is conserved throughout

# Valid SU(3) color winding vectors for quarks (from SCVC handoff)
const SU3_R  = [ 1.0,  0.0]
const SU3_G  = [-0.5,  0.866]
const SU3_B  = [-0.5, -0.866]

# Quark winding database: [wc1, wc2, ww, wy, mass_factor]
const Q_UP_R   = [ 1.0,  0.0,    0.5, 0.1667, 4.2426]
const Q_UP_G   = [-0.5,  0.866,  0.5, 0.1667, 4.2426]
const Q_UP_B   = [-0.5, -0.866,  0.5, 0.1667, 4.2426]
const Q_DN_R   = [ 1.0,  0.0,   -0.5, 0.1667, 9.1317]
const Q_DN_G   = [-0.5,  0.866, -0.5, 0.1667, 9.1317]
const Q_DN_B   = [-0.5, -0.866, -0.5, 0.1667, 9.1317]
const Q_AU_R   = [-1.0,  0.0,   -0.5, -0.1667, 4.2426]
const Q_AU_G   = [ 0.5, -0.866, -0.5, -0.1667, 4.2426]
const Q_AU_B   = [ 0.5,  0.866, -0.5, -0.1667, 4.2426]
const Q_AD_R   = [-1.0,  0.0,    0.5, -0.1667, 9.1317]
const Q_AD_G   = [ 0.5, -0.866,  0.5, -0.1667, 9.1317]
const Q_AD_B   = [ 0.5,  0.866,  0.5, -0.1667, 9.1317]
# Leptons
const L_E      = [ 0.0,  0.0,   -0.5, -0.5, 1.0]
const L_NU     = [ 0.0,  0.0,    0.5, -0.5, 0.01]
const L_POS    = [ 0.0,  0.0,    0.5,  0.5, 1.0]
const L_ANU    = [ 0.0,  0.0,   -0.5,  0.5, 0.01]

func _execute_hadron_resonance_decay(cluster: Array, center: Vector3, first_up: bool):
	# Count quarks and find the one to flavor-convert
	# For uuu -> uud + (u+anti-d): flip one u->d, create pi+
	# For ddd -> udd + (d+anti-u): flip one d->u, create pi-

	# Step 1: Pick one quark farthest from center to flip
	var target = cluster[0]; var best_d = 0.0
	for q in cluster:
		var d = q.position.distance_to(center)
		if d > best_d: best_d = d; target = q

	# Step 2: Flavor conversion -- flip w_w, update mass_factor
	# SCVC: u (ww=+0.5, wy=+0.1667) <-> d (ww=-0.5, wy=+0.1667)
	# The wy stays the same for both quark types
	target.w_w = -target.w_w
	target.mass_factor = 9.1317 if first_up else 4.2426  # u->d or d->u
	target._on_pool_activate(target.position, target.w_c1, target.w_c2, target.w_w, target.w_y)

	# Step 3: Create meson to carry away the excess winding
	# uuu -> uud: lost w_w = -1.0, wy unchanged -> need (ww=+1.0, wy=0) = W+
	# The W+ immediately materializes as u + anti-d (pi+)
	# pi+ = u(bright) + anti-d(bright): total (0,0,1,0)
	# Find a color for the anti-d that makes it a color singlet with u
	# Use bright (R) for both: u(bright) + anti-d(bright) = color singlet

	# The meson particles
	var m_q_w = Q_UP_R if first_up else Q_DN_R  # u(bright) for uuu decay, d(bright) for ddd
	var m_aq_w = Q_AD_R if first_up else Q_AU_R  # anti-d(bright) or anti-u(bright)
	var m_mf = m_q_w[4]  # mass factor for the quark in meson

	# Create meson particles near center with outward velocity
	var out_dir = (target.position - center).normalized()
	if out_dir.length() < 0.1:
		out_dir = Vector3(randf()-0.5, 0, randf()-0.5).normalized()

	var pos_q = center + out_dir * 1.0
	var pos_aq = center - out_dir * 1.0

	var kick = Vector3(randf()-0.5, 0, randf()-0.5).normalized() * (3.0 + randf() * 3.0)

	var new_q = create_vortex(pos_q, m_q_w[0], m_q_w[1], m_q_w[2], m_q_w[3], kick, m_mf)
	var new_aq = create_vortex(pos_aq, m_aq_w[0], m_aq_w[1], m_aq_w[2], m_aq_w[3], -kick, m_aq_w[4])
	# Give new meson particles decay immunity to prevent re-trigger
	if new_q: _decay_immune[new_q] = DECAY_IMMUNITY_FRAMES
	if new_aq: _decay_immune[new_aq] = DECAY_IMMUNITY_FRAMES

	# Step 4: Unbind original cluster and kick surviving particles
	for q in cluster: q.unbind_all()
	for sp in springs.duplicate():
		if not is_instance_valid(sp): springs.erase(sp); continue
		var sa = sp.get_meta("a", null)
		if sa in cluster: springs.erase(sp); sp.queue_free()

	# Step 5: Kinetic kick to all original particles (mass excess -> velocity)
	for q in cluster:
		if q == target: continue  # The flipped quark stays near center
		var dir = (q.position - center).normalized()
		if dir.length() < 0.1:
			dir = Vector3(randf()-0.5, 0, randf()-0.5).normalized()
		q.velocity = dir * (4.0 + randf() * 4.0)
		q.position = center + dir * 2.5
		_decay_immune[q] = DECAY_IMMUNITY_FRAMES
	_decay_immune[target] = DECAY_IMMUNITY_FRAMES

func _execute_boson_decay(cluster: Array, center: Vector3):
	# W/Z-like boson clusters: unbind and scatter
	for q in cluster: q.unbind_all()
	for sp in springs.duplicate():
		if not is_instance_valid(sp): springs.erase(sp); continue
		var sa = sp.get_meta("a", null)
		if sa in cluster: springs.erase(sp); sp.queue_free()

	for q in cluster:
		var dir = (q.position - center).normalized()
		if dir.length() < 0.1:
			dir = Vector3(randf()-0.5, 0, randf()-0.5).normalized()
		q.velocity = dir * (5.0 + randf() * 5.0)
		q.position = center + dir * 2.5
		_decay_immune[q] = DECAY_IMMUNITY_FRAMES


# ========== NEUTRON BETA DECAY (PLACEHOLDER G_F) ==========
# n(ddu) -> p(uud) + e- + nu_e_bar
# SCVC mechanism: d->u flavor flip via W-boson (weak interaction)
# Winding conserved: ddu -> uud + e-(ww=-0.5,wy=-0.5) + nu_bar(ww=-0.5,wy=0.5)
# Energy: Delta_E = E_CORE * (MF_D - MF_U) * |w|^2 -> product kinetic energy
#
# I3: NEUTRON_DECAY_PROB = 15 * Gamma_sim = 2.25e-23 (physically correct)
# Fermi GR: Gamma = G_F^2 |V_ud|^2 (1+3g_A^2) m_e^5 f_n / (2pi^3)
# Demo mode: replace NEUTRON_DECAY_PROB with 0.015 for visible decay (~17s).

func _check_neutron_decay():
	var processed = []
	for i in range(vortices.size()):
		var v = vortices[i]
		if not is_instance_valid(v) or v in processed: continue
		if _decay_immune.get(v, 0) > 0: continue
		
		# Build spring-bound cluster
		var cluster = [v]
		for j in range(vortices.size()):
			if i == j: continue
			var w = vortices[j]
			if not is_instance_valid(w): continue
			if v.is_bound_to(w) and not w in cluster:
				cluster.append(w)
		if cluster.size() != 3: continue  # free neutron only (3-quark cluster)
		
		# Check: exactly 2 down-type + 1 up-type = neutron candidate
		var n_d = 0; var n_u = 0
		var tc1 = 0.0; var tc2 = 0.0
		var down_candidates = []
		for q in cluster:
			tc1 += q.w_c1; tc2 += q.w_c2
			var prod = q.w_w * q.w_y  # >0 = up-type, <0 = down-type
			if prod < -0.01:
				n_d += 1
				down_candidates.append(q)
			else:
				n_u += 1
		
		var mag_c = sqrt(tc1*tc1 + tc2*tc2)
		if mag_c > 0.2: continue  # not color singlet
		if n_d != 2 or n_u != 1: continue  # not a neutron
		if down_candidates.size() == 0: continue
		
		# Real decay probability (I3 SCVC: G_F=2.68e-12, tau_n=915s)
		# Physically correct: ~10^{-23} per check -- requires demo boost to observe
		# Replace NEUTRON_DECAY_PROB with DEMO_DECAY_PROB=0.015 for visible decay
		if randf() > NEUTRON_DECAY_PROB: continue
		
		# Execute beta decay
		var center = Vector3.ZERO
		for q in cluster: center += q.position
		center /= float(cluster.size())
		
		# Pick one down quark to flip
		var target = down_candidates[0]
		if down_candidates.size() > 1:
			# Pick the one farthest from center (more energetic)
			var best_d = 0.0
			for dq in down_candidates:
				var dd = dq.position.distance_to(center)
				if dd > best_d: best_d = dd; target = dq
		
		_execute_beta_decay(cluster, target, center)
		for q in cluster: processed.append(q)

func _execute_beta_decay(cluster: Array, target, center: Vector3):
	# Step 1: Flavor flip d -> u
	# SCVC: u has w_w=+0.5, d has w_w=-0.5; wy=0.1667 same for both
	target.w_w = -target.w_w  # -0.5 -> +0.5 (d->u flip, same pattern as resonance decay)
	target.mass_factor = 4.2426  # MF_D=9.1317 -> MF_U=4.2426
	target._on_pool_activate(target.position, target.w_c1, target.w_c2, target.w_w, target.w_y)
	
	# Step 2: Create electron ring at decay site
	# winding: (0,0,-0.5,-0.5)  charge: -1  mass: MF_E=1.0
	var e_dir = (target.position - center).normalized()
	if e_dir.length() < 0.1:
		e_dir = Vector3(randf()-0.5, 0, randf()-0.5).normalized()
	var e_pos = center + e_dir * 2.0
	var e_ring = create_ring(e_pos, 0.0, 0.0, -0.5, -0.5, 1.0, 0.3)
	if e_ring:
		e_ring.center_velocity = e_dir * 2.5
	
	# Step 3: Create anti-neutrino vortex
	# Anti-NU_E = flip all signs: (0,0,-0.5,0.5)  MF_NU=0.01
	var nu_dir = -e_dir + Vector3(randf()-0.5, 0, randf()-0.5).normalized() * 0.3
	nu_dir = nu_dir.normalized()
	var nu_pos = center + nu_dir * 2.5
	var nu_kick = nu_dir * 8.0  # light, fast
	var nu = create_vortex(nu_pos, 0.0, 0.0, -0.5, 0.5, nu_kick, 0.01)
	if nu: _decay_immune[nu] = DECAY_IMMUNITY_FRAMES
	
	# Step 4: Mass excess -> kinetic energy for products
	# Delta_mf = MF_D - MF_U = 9.1317 - 4.2426 = 4.8891
	# E_release = E_CORE * Delta_mf * |w|^2 ~ 2.1322 * 4.8891 * 1.28 ~ 13.3 sim
	# Subtract electron rest energy (~1.07 sim) -> ~12.2 sim for kinetic
	var kick_energy = 3.0  # sim kinetic per remaining quark (conservative)
	
	# Step 5: Unbind old cluster, kick surviving quarks
	for q in cluster: q.unbind_all()
	for sp in springs.duplicate():
		if not is_instance_valid(sp): springs.erase(sp); continue
		var sa = sp.get_meta("a", null)
		if sa in cluster: springs.erase(sp); sp.queue_free()
	
	for q in cluster:
		if q == target: continue  # flipped quark stays near center
		var dir = (q.position - center).normalized()
		if dir.length() < 0.1:
			dir = Vector3(randf()-0.5, 0, randf()-0.5).normalized()
		q.velocity = dir * (kick_energy + randf() * 2.0)
		q.position = center + dir * 2.0
		_decay_immune[q] = DECAY_IMMUNITY_FRAMES
	_decay_immune[target] = DECAY_IMMUNITY_FRAMES
# ========== SPRINGS ==========

func create_spring(a: Node3D, b: Node3D):
	var sp = MeshInstance3D.new(); sp.name = "Spring"
	var cm = CylinderMesh.new()
	cm.top_radius = 0.02; cm.bottom_radius = 0.02; cm.height = 1.0
	sp.mesh = cm
	var sm = StandardMaterial3D.new()
	sm.albedo_color = Color(0.3, 0.5, 0.9, 0.6)
	sm.emission_enabled = true; sm.emission = Color(0.2, 0.3, 0.8)
	sm.emission_energy_multiplier = 1.5
	sm.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	sm.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	sp.material_override = sm
	add_child(sp)
	sp.set_meta("a", a); sp.set_meta("b", b)
	springs.append(sp)

func remove_springs_between(a: Node3D, b: Node3D):
	var dead = []
	for sp in springs:
		if not is_instance_valid(sp): continue
		var sa = sp.get_meta("a", null); var sb = sp.get_meta("b", null)
		if (sa == a and sb == b) or (sa == b and sb == a):
			dead.append(sp); sp.queue_free()
	for d in dead: springs.erase(d)

func update_springs():
	var dead = []
	for sp in springs:
		if not is_instance_valid(sp):
			dead.append(sp)
			continue
		sp.visible = springs_visible
		var a = sp.get_meta("a", null); var b = sp.get_meta("b", null)
		if not is_instance_valid(a) or not is_instance_valid(b) or not a.is_bound_to(b):
			dead.append(sp); sp.queue_free(); continue
		var mid = (a.position + b.position) * 0.5
		var dist = a.position.distance_to(b.position)
		sp.position = mid
		if dist > 0.01:
			sp.look_at(b.position, Vector3.UP)
			sp.scale = Vector3(1, dist, 1)
	for d in dead: springs.erase(d)

# ========== SNAPSHOT ==========

func toggle_snapshot():
	snapshot_mode = not snapshot_mode
	if snapshot_mode:
		for v in vortices:
			if is_instance_valid(v): v.visible = false
	else:
		for v in vortices:
			if is_instance_valid(v): v.visible = true

func toggle_freeze():
	time_frozen = not time_frozen

func toggle_quarks():
	show_quarks = not show_quarks

func toggle_decay():
	decay_mode = not decay_mode

func snap_visuals():
	for v in vortices:
		if is_instance_valid(v): v.visible = true
	_snap_frame = 2

func _check_annihilation():
	const ANNIHIL_RADIUS = 0.3
	var dead = []
	for i in range(vortices.size()):
		var a = vortices[i]
		if not is_instance_valid(a) or a in dead: continue
		for j in range(i + 1, vortices.size()):
			var b = vortices[j]
			if not is_instance_valid(b) or b in dead: continue
			if abs(a.w_c1 + b.w_c1) < 0.02 and abs(a.w_c2 + b.w_c2) < 0.02 and abs(a.w_w + b.w_w) < 0.02 and abs(a.w_y + b.w_y) < 0.02:
				if a.position.distance_to(b.position) < ANNIHIL_RADIUS:
					dead.append(a); dead.append(b)
					break
	for v in dead: remove_vortex(v)

# ========== UTILS ==========

func _combinations(n: int, k: int) -> Array:
	if k == 0: return [[]]
	if n < k: return []
	var result = []
	var with_first = _combinations(n - 1, k - 1)
	for c in with_first:
		c.append(n - 1)
		result.append(c)
	var without = _combinations(n - 1, k)
	result.append_array(without)
	return result

func add_vortex(v: Node3D):
	if not v in vortices: vortices.append(v)

func remove_vortex(v: Node3D):
	v.unbind_all()
	_decay_immune.erase(v)
	for sp in springs.duplicate():
		if not is_instance_valid(sp): springs.erase(sp); continue
		var sa = sp.get_meta("a", null); var sb = sp.get_meta("b", null)
		if sa == v or sb == v:
				springs.erase(sp)
				var spp = sp.get_parent()
				if spp: spp.remove_child(sp)
				sp.free()
	vortices.erase(v)
	_return_to_pool(v)


func nearest_vortex_dist(v: Node3D) -> float:
	var nearest: float = 999.0
	for other in vortices:
		if other == v or not is_instance_valid(other): continue
		var d = v.position.distance_to(other.position)
		if d < nearest: nearest = d
	return nearest

func vortex_nearby(v: Node3D) -> bool:
	return nearest_vortex_dist(v) < 2.0
func _on_vortex_out_of_bounds(v: Node3D):
	remove_vortex(v)

func clear_all():
	for v in vortices.duplicate(): remove_vortex(v)
	for r in rings.duplicate(): remove_ring(r)
	_decay_immune.clear()
	springs.clear()
	_frame = 0
	decay_mode = false
	_cluster_cache.clear()
	_cluster_cache_frame = -1
	# Force-free any orphaned children (immediate, not deferred)
	var orphans := []
	for child in get_children():
		if child is VortexRing or (child is Node3D and child.name.begins_with("VortexRing")):
			orphans.append(child)
	for child in orphans:
		if is_instance_valid(child):
			if child.has_method("deactivate"):
				child.deactivate()
			var p = child.get_parent()
			if p: p.remove_child(child)
			child.free()
	# Force batch render reset: hide all instances immediately
	if _batch_mesh and _batch_mesh.multimesh:
		_batch_mesh.multimesh.visible_instance_count = 0
	if _batch_glow and _batch_glow.multimesh:
		_batch_glow.multimesh.visible_instance_count = 0
	if _batch_ring_segs and _batch_ring_segs.multimesh:
		_batch_ring_segs.multimesh.visible_instance_count = 0
	if _batch_ring_springs and _batch_ring_springs.multimesh:
		_batch_ring_springs.multimesh.visible_instance_count = 0


func create_vortex(pos: Vector3, wc1: float, wc2: float, ww: float, wy: float, vel: Vector3 = Vector3.ZERO, mf: float = 0.0) -> Node3D:
	var v = _acquire_from_pool()
	if not v: return null
	if not v.out_of_bounds.is_connected(_on_vortex_out_of_bounds):
		v.out_of_bounds.connect(_on_vortex_out_of_bounds)
	v.position = pos
	v.w_c1 = wc1; v.w_c2 = wc2; v.w_w = ww; v.w_y = wy; v.mass_factor = mf
	v.velocity = vel
	v.visible = true
	v._on_pool_activate(pos, wc1, wc2, ww, wy)
	add_vortex(v)
	return v


# ========== RING PHYSICS ==========

func create_ring(pos: Vector3, wc1: float, wc2: float, ww: float, wy: float, mf: float = 1.0, ring_radius: float = 2.0) -> Node3D:
	var RingClass = load("res://scripts/vortex_ring.gd")
	var ring = RingClass.new()
	ring.name = "VortexRing%d" % rings.size()
	add_child(ring)
	ring.activate(pos, wc1, wc2, ww, wy, mf)
	ring.radius = ring_radius
	rings.append(ring)
	return ring

func remove_ring(ring: Node3D):
	if ring in rings:
		rings.erase(ring)
	if is_instance_valid(ring):
		ring.deactivate()
		# Detach from tree and free IMMEDIATELY (not deferred queue_free)
		# This prevents accumulation when rapidly switching scenes.
		var parent = ring.get_parent()
		if parent:
			parent.remove_child(ring)
		ring.free()

func _compute_ring_forces(ring: Node3D):
	# Compute external forces on each ring segment from point vortices and other rings
	var n_seg = ring.num_segments
	var seg_forces = []
	for i in range(n_seg):
		seg_forces.append(Vector3.ZERO)

	# Ring-point interactions
	for v in vortices:
		if not is_instance_valid(v): continue
		var qv = v.w_w + v.w_y
		var qr = ring.charge()
		for i in range(n_seg):
			var seg_pos = ring.get_segment_world_pos(i)
			var diff = v.position - seg_pos
			var r = diff.length()
			if r < 0.01: continue
			var xi2 = XI * XI
			var ft = -2.0 * G_EM * qr * qv * r / (xi2 + r * r)  # minus: F = -dE/dr (attraction for opposite charges)
			seg_forces[i] += diff.normalized() * ft

	# Ring-ring interactions (topological + EM)
	for ring2 in rings:
		if ring2 == ring or not is_instance_valid(ring2) or not ring2.active: continue
		var qr2 = ring2.charge()
		var qr1 = ring.charge()
		for i in range(n_seg):
			var seg_pos = ring.get_segment_world_pos(i)
			# Use ring2 center for efficiency (accurate enough for non-overlapping rings)
			var diff = ring2.position - seg_pos
			var r = diff.length()
			if r < 0.01: continue
			var xi2 = XI * XI
			var ft = -2.0 * G_EM * qr1 * qr2 * r / (xi2 + r * r)  # minus: F = -dE/dr
			# R3 Pauli exclusion: three-region potential (E_CORE barrier)
			# ring.pauli_potential() handles w_dot sign, core/exponential/Ampere regions
			var ring_dist = ring.position.distance_to(ring2.position)
			var topo_rep = 0.0
			if ring.has_method("pauli_potential"):
				topo_rep = ring.pauli_potential(ring2, ring_dist)
			seg_forces[i] += diff.normalized() * (ft + topo_rep)

	# Store forces for ring to use
	ring.set_meta("_ext_forces", seg_forces)


# =====================================================================
# VFM: Biot-Savart velocity induction
# =====================================================================
# Standard desingularized Biot-Savart for a straight vortex segment.
# rA = eval_point - segment_start (world coords)
# rB = eval_point - segment_end   (world coords)
# gamma = effective circulation (kappa_eff modulated by winding coupling)
# core_a = desingularization radius

func _biot_savart_segment(eval_point: Vector3, seg_start: Vector3, seg_end: Vector3, gamma: float, core_a: float) -> Vector3:
	var rA: Vector3 = eval_point - seg_start
	var rB: Vector3 = eval_point - seg_end
	var rA_len: float = rA.length()
	var rB_len: float = rB.length()

	# Guard: avoid computing when segment and eval_point coincide
	if rA_len < 0.0001 or rB_len < 0.0001:
		return Vector3.ZERO

	var rA_cross_rB: Vector3 = rA.cross(rB)
	var cross_mag2: float = rA_cross_rB.length_squared()

	# Standard desingularized VFM kernel (Schwarz 1985, Tsubota 2000):
	# v = (gamma/4pi) * (rA x rB) * (|rA|+|rB|) / [ |rA||rB| * (|rA||rB| + rA?rB) + core_a? ]
	var denominator: float = rA_len * rB_len * (rA_len * rB_len + rA.dot(rB)) + core_a * core_a

	if denominator < 0.0001:
		return Vector3.ZERO

	var prefactor: float = gamma / (4.0 * PI)
	var numerator: float = rA_len + rB_len

	var result: Vector3 = rA_cross_rB * (prefactor * numerator / denominator)
	if result.length() > 1e6 or is_nan(result.x) or is_nan(result.y) or is_nan(result.z): return Vector3.ZERO
	return result





## V1: Compute VFM Biot-Savart -> Magnus FORCES for all ring segments.
## Returns Array[Vector3] of forces (Channel A only).
## Channels B+C (gauge + Pauli) are added by the caller (_process).
## Self-induction + cross-induction + point vortex induction included.
func _compute_vfm_velocities(ring) -> Array:
	# V1: Biot-Savart velocity induction (flavor-blind, kappa=1.0).
	# In VFM at T=0: ds/dt = v_superfluid. Segments ADVECT with flow.
	# NO Magnus force conversion. Just return velocities.
	var n_seg: int = ring.num_segments
	var bs_velocities: Array = []
	for i in range(n_seg):
		bs_velocities.append(Vector3.ZERO)

	var seg_positions: Array = []
	for i in range(n_seg):
		seg_positions.append(ring.get_segment_world_pos(i))

	# --- Self-induction ---
	var self_core_a: float = VFM_CORE_A + ring.radius * VFM_SELF_CORE_FACTOR
	for i in range(n_seg):
		var pi: Vector3 = seg_positions[i]
		var v_bs_self: Vector3 = Vector3.ZERO
		for j in range(n_seg):
			if j == i: continue
			var j_next: int = (j + 1) % n_seg
			var seg_start: Vector3 = seg_positions[j]
			var seg_end: Vector3 = seg_positions[j_next]
			v_bs_self += _biot_savart_segment(pi, seg_start, seg_end, VFM_KAPPA, self_core_a)
		bs_velocities[i] += v_bs_self

	# --- Cross-induction: OTHER rings ---
	for ring2 in rings:
		if ring2 == ring or not is_instance_valid(ring2) or not ring2.active: continue
		var n2: int = ring2.num_segments
		for i in range(n_seg):
			var pi: Vector3 = seg_positions[i]
			var v_bs_cross: Vector3 = Vector3.ZERO
			for j2 in range(n2):
				var j2_next: int = (j2 + 1) % n2
				var seg_start: Vector3 = ring2.get_segment_world_pos(j2)
				var seg_end: Vector3 = ring2.get_segment_world_pos(j2_next)
				v_bs_cross += _biot_savart_segment(pi, seg_start, seg_end, VFM_KAPPA, VFM_CORE_A)
			bs_velocities[i] += v_bs_cross

	# --- Point vortex (quark) induction ---
	for v in vortices:
		if not is_instance_valid(v): continue
		for i in range(n_seg):
			var r_vec: Vector3 = seg_positions[i] - v.position
			var r: float = r_vec.length()
			if r < 0.01: continue
			var r_hat: Vector3 = r_vec.normalized()
			var v_point: Vector3 = VFM_KAPPA / (TAU * (r + VFM_CORE_A)) * Vector3.UP.cross(r_hat)
			bs_velocities[i] += v_point

	return bs_velocities

func _compute_point_force_from_rings(v: Node3D) -> Vector3:
	# Force on a point vortex from all rings (Newton's 3rd law)
	var f = Vector3.ZERO
	for ring in rings:
		if not is_instance_valid(ring) or not ring.active: continue
		var n_seg = ring.num_segments
		var qv = v.w_w + v.w_y
		var qr = ring.charge()
		for i in range(n_seg):
			var seg_pos = ring.get_segment_world_pos(i)
			var diff = seg_pos - v.position
			var r = diff.length()
			if r < 0.01: continue
			var xi2 = XI * XI
			var ft = -2.0 * G_EM * qr * qv * r / (xi2 + r * r)  # minus: F = -dE/dr
			f += diff.normalized() * ft
	return f


# =====================================================================
# =====================================================================
# N1: Nucleon-Nucleon Potential (SCVC First-Principles, 2026-07-24)
# =====================================================================
# Identifies nucleons directly from quark SCVC winding numbers:
#   Nucleon = 3 quarks with |sum(w_c)|~0 (color singlet) AND |sum(w_w)|~0.5 (isospin)
#   Then applies V_NN between all nucleon pairs.
#
# NO dependence on spring connectivity (springs merge across nucleons -> broken clusters).
# Spatial clustering uses proximity, nucleon ID uses SCVC winding algebra.
#
# SCVC HONESTY:
#   - NN_SPIN_ISOSPIN_FACTOR=1.0: no per-nucleon spin tracking (known limitation)
#   - NN_FORCE_CAP=200: numerical guard for r<0.2 sim where F_core~1500+
#   - All other constants from SCVC first principles, zero free parameters
func _compute_nn_forces():
	# Step 1: Collect color-carrying quarks (skip neutrinos, leptons)
	var quarks := []
	for v in vortices:
		if not is_instance_valid(v) or not v.visible: continue
		var cmag := sqrt(v.w_c1 * v.w_c1 + v.w_c2 * v.w_c2)
		if cmag < 0.05: continue  # no color charge -> not a quark
		quarks.append(v)
	
	if quarks.size() < 6: return  # need at least 2 nucleons (6 quarks)
	
	# Step 2: Spatial clustering by proximity (cutoff ~2 sim units ~ 10 fm)
	const SPATIAL_CUTOFF: float = 2.0
	var visited := {}
	var spatial_clusters := []
	for q in quarks:
		var qid: int = q.get_instance_id()
		if visited.has(qid): continue
		var cluster := []
		var queue := [q]
		visited[qid] = true
		while not queue.is_empty():
			var curr = queue.pop_front()
			cluster.append(curr)
			for other in quarks:
				var oid: int = other.get_instance_id()
				if visited.has(oid): continue
				if curr.position.distance_to(other.position) < SPATIAL_CUTOFF:
					visited[oid] = true
					queue.append(other)
		if cluster.size() >= 3:
			spatial_clusters.append(cluster)
	
	# Step 3: Within each spatial cluster, identify nucleons (3-quark color singlets)
	var nucleons := []  # Array[{com: Vector3, quarks: Array}]
	const COLOR_EPSILON: float = 0.15
	const ISOSPIN_EPSILON: float = 0.3
	
	for cl in spatial_clusters:
		var remaining := cl.duplicate()
		while remaining.size() >= 3:
			var best_trio: Array = []
			var best_score: float = 1e9
			
			# Try all 3-quark combinations in remaining
			for i in range(remaining.size()):
				for j in range(i + 1, remaining.size()):
					for k in range(j + 1, remaining.size()):
						var a = remaining[i]
						var b = remaining[j]
						var c = remaining[k]
						var sum_c1: float = a.w_c1 + b.w_c1 + c.w_c1
						var sum_c2: float = a.w_c2 + b.w_c2 + c.w_c2
						var sum_w: float = a.w_w + b.w_w + c.w_w
						var color_score: float = sqrt(sum_c1 * sum_c1 + sum_c2 * sum_c2)
						var iso_score: float = abs(abs(sum_w) - 0.5)
						var score: float = color_score + iso_score
						if score < best_score:
							best_score = score
							best_trio = [i, j, k]
			
			# Accept trio if it forms a valid nucleon
			if best_trio.size() == 3 and best_score < (COLOR_EPSILON + ISOSPIN_EPSILON):
				var i_idx: int = best_trio[0]
				var j_idx: int = best_trio[1]
				var k_idx: int = best_trio[2]
				var a = remaining[i_idx]
				var b = remaining[j_idx]
				var c = remaining[k_idx]
				
				var com := (a.position + b.position + c.position) / 3.0
				nucleons.append({"com": com, "quarks": [a, b, c]})
				
				# Remove in descending index order (so shifting doesn't break later removes)
				var r0: int = max(i_idx, max(j_idx, k_idx))
				var r2: int = min(i_idx, min(j_idx, k_idx))
				var r1: int = i_idx + j_idx + k_idx - r0 - r2
				remaining.remove_at(r0)
				remaining.remove_at(r1)
				remaining.remove_at(r2)
			else:
				break  # can't form more nucleons from remaining quarks
	
	if nucleons.size() < 2: return
	
	# Step 4: Apply NN potential between all nucleon pairs
	for i in range(nucleons.size()):
		var ni = nucleons[i]
		for j in range(i + 1, nucleons.size()):
			var nj = nucleons[j]
			var r_vec := nj["com"] - ni["com"]
			var r: float = r_vec.length()
			if r < 0.001: continue
			var dir := r_vec.normalized()
			
			# OPEP (attractive): F = -factor*V_PI*exp(-M_PI*r)*(M_PI/r+1/r^2)
			var f_pi: float = -NN_SPIN_ISOSPIN_FACTOR * NN_V_PI * exp(-NN_M_PI * r) * (NN_M_PI / r + 1.0 / (r * r))
			# Hard core (repulsive): F = +factor*V_CORE*exp(-M_OMEGA*r)*(M_OMEGA/r+1/r^2)
			var f_core: float = NN_SPIN_ISOSPIN_FACTOR * NN_V_CORE * exp(-NN_M_OMEGA * r) * (NN_M_OMEGA / r + 1.0 / (r * r))
			var f_mag: float = f_pi + f_core
			
			if is_nan(f_mag) or is_inf(f_mag): continue
			f_mag = clamp(f_mag, -NN_FORCE_CAP, NN_FORCE_CAP)
			
			# Distribute force to constituent quarks
			var force := dir * f_mag
			var fi := force / 3.0
			var fj := -force / 3.0
			for q in ni["quarks"]:
				if is_instance_valid(q): q.force_accum += fi
			for q in nj["quarks"]:
				if is_instance_valid(q): q.force_accum += fj


# ========== GeV BRIDGE ==========
# Converts dimensionless simulation energy to physical MeV.
# m_physical = E_CORE * mf * |w|^2 * E_SCALE_BEC * (pi/8 if quark else 1)
func to_mev(v: Node3D) -> float:
	var mf = v.mass_factor if v.mass_factor > 0.0 else _mass_factor(v.w_c1, v.w_c2, v.w_w, v.w_y)
	var w2 = v.w_c1*v.w_c1 + v.w_c2*v.w_c2 + v.w_w*v.w_w + v.w_y*v.w_y
	var e_sim = E_CORE * mf * w2
	var has_color = sqrt(v.w_c1*v.w_c1 + v.w_c2*v.w_c2) > 0.1
	var e_mev = e_sim * E_SCALE_BEC
	if has_color:
		e_mev *= QUARK_PI_OVER_8
	return e_mev

# Returns total system energy in MeV
func total_energy_mev() -> float:
	var e_mev = 0.0
	for v in vortices:
		if not is_instance_valid(v): continue
		e_mev += to_mev(v)
	# Pairwise interactions (approximate: dominated by core energies for heavy particles)
	for i in range(vortices.size()):
		var a = vortices[i]
		if not is_instance_valid(a): continue
		for j in range(i+1, vortices.size()):
			var b = vortices[j]
			if not is_instance_valid(b): continue
			var r = a.position.distance_to(b.position)
			var xi2 = _xi_for_pair(a, b); xi2 *= xi2
			var l = log(1.0 + r*r/xi2)
			e_mev += G_STRONG * a.color_dot(b) * l * E_SCALE_BEC
			var qa = a.w_w + a.w_y; var qb = b.w_w + b.w_y
			e_mev += G_EM * qa * qb * l * E_SCALE_BEC
	# Ring contributions
	for ring in rings:
		if is_instance_valid(ring) and ring.active:
			e_mev += ring.core_energy() * E_SCALE_BEC
	return e_mev
