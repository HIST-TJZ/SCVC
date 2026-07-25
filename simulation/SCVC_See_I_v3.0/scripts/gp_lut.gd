# gp_lut.gd -- SCVC GP Effective Potential Lookup Table
# E2 Phase 2: Pre-computed GP effective potentials for electron-involved pairs.
# Offline GP solves -> JSON tables -> O(1) runtime lookup.
extends RefCounted

var _lut: Dictionary = {}

enum PairType { EP = 0, EE = 1, PP = 2 }

const R_MIN: float = 0.01  # updated: 500 sim range, 2000 bins
const R_MAX: float = 500.0
const N_BINS: int = 2000
const DR: float = (R_MAX - R_MIN) / float(N_BINS)

var _loaded: bool = false

func load_tables() -> bool:
    if _loaded: return true
    var types = {
        PairType.EP: "res://data/lut_ep.json",
        PairType.EE: "res://data/lut_ee.json",
        PairType.PP: "res://data/lut_pp.json",
    }
    for pair_type in types:
        var path_str: String = types[pair_type]
        if not FileAccess.file_exists(path_str):
            print_rich("[color=yellow]GP LUT not found: " + path_str + "[/color]")
            continue
        var file = FileAccess.open(path_str, FileAccess.READ)
        if not file: continue
        var text: String = file.get_as_text()
        file.close()
        var json = JSON.new()
        if json.parse(text) != OK: continue
        _lut[pair_type] = json.get_data()
        print_rich("[color=green]GP LUT loaded: " + path_str + "[/color]")
    _loaded = _lut.size() > 0
    return _loaded

func has_table(pair_type: int) -> bool:
    return _lut.has(pair_type)

func get_potential(r: float, pair_type: int) -> float:
    if not _lut.has(pair_type): return 0.0
    var table = _lut[pair_type]
    if r <= R_MIN: return table["v_values"][0]
    if r >= R_MAX:
        var last: int = table["n_bins"] - 1
        return table["v_values"][last]
    var idx_f: float = (r - R_MIN) / DR
    var idx: int = int(idx_f)
    var frac: float = idx_f - float(idx)
    var v0: float = table["v_values"][idx]
    var next: int = min(idx + 1, table["n_bins"] - 1)
    var v1: float = table["v_values"][next]
    return v0 + (v1 - v0) * frac

func get_force_derivative(r: float, pair_type: int) -> float:
    if not _lut.has(pair_type): return 0.0
    var table = _lut[pair_type]
    if r <= R_MIN: return table["dvdr_values"][0]
    if r >= R_MAX:
        var last: int = table["n_bins"] - 1
        return table["dvdr_values"][last]
    var idx_f: float = (r - R_MIN) / DR
    var idx: int = int(idx_f)
    var frac: float = idx_f - float(idx)
    var d0: float = table["dvdr_values"][idx]
    var next: int = min(idx + 1, table["n_bins"] - 1)
    var d1: float = table["dvdr_values"][next]
    return d0 + (d1 - d0) * frac

func get_pair_type(a_is_lepton: bool, b_is_lepton: bool) -> int:
    if a_is_lepton and b_is_lepton: return PairType.EE
    if not a_is_lepton and not b_is_lepton: return PairType.PP
    return PairType.EP

static var _inst = null
static func instance() -> RefCounted:
    if not _inst: _inst = load("res://scripts/gp_lut.gd").new()
    return _inst
