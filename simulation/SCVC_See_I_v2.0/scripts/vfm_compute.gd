# vfm_compute.gd -- SCVC v2.0 GPU Compute Dispatcher
# Manages Vulkan compute shader for Biot-Savart N-body calculation.
extends RefCounted

var _rd = null
var _pipeline_rid = RID()
var _shader_rid = RID()
var _uniform_set = RID()
var _seg_pos_buf = RID()
var _seg_map_buf = RID()
var _ring_off_buf = RID()
var _ring_rad_buf = RID()
var _vor_pos_buf = RID()
var _vel_out_buf = RID()
var _max_seg: int = 0
var _max_ring: int = 0
var _max_vor: int = 0
const SHADER_PATH: String = "res://assets/compute/vfm_bs.glsl"
const VFM_KAPPA: float = 1.0
const VFM_CORE_A: float = 0.125
const VFM_SELF_CORE_F: float = 0.5
const LOCAL_SIZE: int = 64

func initialize() -> bool:
	if _rd: return true
	_rd = RenderingServer.create_local_rendering_device()
	if not _rd: push_error("VFM: No RD"); return false
	var sf: RDShaderFile = load(SHADER_PATH)
	if not sf: push_error("VFM: No shader"); return false
	var spv: RDShaderSPIRV = sf.get_spirv()
	var err: String = spv.get_stage_compile_error(RenderingDevice.SHADER_STAGE_COMPUTE)
	if err != "": push_error("VFM: " + err); return false
	var shader_rid: RID = _rd.shader_create_from_spirv(spv)
	if not shader_rid.is_valid(): push_error("VFM: Shader create fail"); return false
	_pipeline_rid = _rd.compute_pipeline_create(shader_rid)
	if not _pipeline_rid.is_valid(): push_error("VFM: Pipeline fail"); return false
	print_rich("[color=cyan]VFM GPU ready[/color]")
	return true

func shutdown():
	if _rd:
		_free_bufs()
		if _shader_rid.is_valid(): _rd.free_rid(_shader_rid); _shader_rid = RID()
		if _pipeline_rid.is_valid(): _rd.free_rid(_pipeline_rid)
		if _uniform_set.is_valid(): _rd.free_rid(_uniform_set)
		_rd.free()
		_rd = null

func _free_bufs():
	if not _rd: return
	for rid in [_seg_pos_buf,_seg_map_buf,_ring_off_buf,_ring_rad_buf,_vor_pos_buf,_vel_out_buf]:
		if rid.is_valid(): _rd.free_rid(rid)
	_seg_pos_buf = RID(); _seg_map_buf = RID(); _ring_off_buf = RID()
	_ring_rad_buf = RID(); _vor_pos_buf = RID(); _vel_out_buf = RID()
	if _uniform_set.is_valid(): _rd.free_rid(_uniform_set); _uniform_set = RID()

func _ensure_bufs(n_seg: int, n_ring: int, n_vor: int) -> bool:
	var grow: bool = false
	if n_seg > _max_seg: _max_seg = max(n_seg, _max_seg*2); grow = true
	if n_ring > _max_ring: _max_ring = max(n_ring, _max_ring*2); grow = true
	if n_vor > _max_vor: _max_vor = max(n_vor, _max_vor*2); grow = true
	if not grow and _uniform_set.is_valid(): return true
	_free_bufs()
	_seg_pos_buf   = _rd.storage_buffer_create(_max_seg * 3 * 4)
	_seg_map_buf   = _rd.storage_buffer_create(_max_seg * 4)
	_ring_off_buf  = _rd.storage_buffer_create(_max_ring * 2 * 4)
	_ring_rad_buf  = _rd.storage_buffer_create(_max_ring * 4)
	_vor_pos_buf   = _rd.storage_buffer_create(_max_vor * 3 * 4)
	_vel_out_buf   = _rd.storage_buffer_create(_max_seg * 3 * 4)
	var u0 := RDUniform.new(); u0.uniform_type = RenderingDevice.UNIFORM_TYPE_STORAGE_BUFFER; u0.binding = 0; u0.add_id(_seg_pos_buf)
	var u1 := RDUniform.new(); u1.uniform_type = RenderingDevice.UNIFORM_TYPE_STORAGE_BUFFER; u1.binding = 1; u1.add_id(_seg_map_buf)
	var u2 := RDUniform.new(); u2.uniform_type = RenderingDevice.UNIFORM_TYPE_STORAGE_BUFFER; u2.binding = 2; u2.add_id(_ring_off_buf)
	var u3 := RDUniform.new(); u3.uniform_type = RenderingDevice.UNIFORM_TYPE_STORAGE_BUFFER; u3.binding = 3; u3.add_id(_ring_rad_buf)
	var u4 := RDUniform.new(); u4.uniform_type = RenderingDevice.UNIFORM_TYPE_STORAGE_BUFFER; u4.binding = 4; u4.add_id(_vor_pos_buf)
	var u5 := RDUniform.new(); u5.uniform_type = RenderingDevice.UNIFORM_TYPE_STORAGE_BUFFER; u5.binding = 5; u5.add_id(_vel_out_buf)
	_uniform_set = _rd.uniform_set_create([u0,u1,u2,u3,u4,u5], _shader_rid, 0)
	return _uniform_set.is_valid()

func compute_all(seg_pos: PackedFloat32Array, seg_map: PackedInt32Array, ring_off: PackedInt32Array, ring_rad: PackedFloat32Array, vor_pos: PackedFloat32Array, n_seg: int, n_ring: int, n_vor: int) -> PackedFloat32Array:
	if n_seg == 0: return PackedFloat32Array()
	if not initialize(): return PackedFloat32Array()
	if not _ensure_bufs(n_seg, n_ring, n_vor): return PackedFloat32Array()
	_rd.buffer_update(_seg_pos_buf, 0, seg_pos.size()*4, seg_pos.to_byte_array())
	_rd.buffer_update(_seg_map_buf, 0, seg_map.size()*4, seg_map.to_byte_array())
	_rd.buffer_update(_ring_off_buf, 0, ring_off.size()*4, ring_off.to_byte_array())
	_rd.buffer_update(_ring_rad_buf, 0, ring_rad.size()*4, ring_rad.to_byte_array())
	_rd.buffer_update(_vor_pos_buf, 0, vor_pos.size()*4, vor_pos.to_byte_array())
	var push: PackedFloat32Array = PackedFloat32Array([float(n_seg),float(n_ring),float(n_vor),VFM_KAPPA, VFM_CORE_A, VFM_SELF_CORE_F])
	var wg: int = int(ceil(float(n_seg)/float(LOCAL_SIZE)))
	var cl: int = _rd.compute_list_begin()
	_rd.compute_list_bind_compute_pipeline(cl, _pipeline_rid)
	_rd.compute_list_bind_uniform_set(cl, _uniform_set, 0)
	_rd.compute_list_set_push_constant(cl, push.to_byte_array(), push.size()*4)
	_rd.compute_list_dispatch(cl, wg, 1, 1)
	_rd.compute_list_end()
	_rd.submit()
	_rd.sync()
	var out_bytes: PackedByteArray = _rd.buffer_get_data(_vel_out_buf, 0, n_seg*3*4)
	return out_bytes.to_float32_array()

static var _inst = null
static func instance() -> RefCounted:
	if not _inst: _inst = load("res://scripts/vfm_compute.gd").new()
	return _inst
