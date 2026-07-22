extends Node

# Global autoload - shared state and data
var vortex_profile: Dictionary = {}
var dh_data: Dictionary = {}
var cp2_data: Dictionary = {}
var moduli_scan: Array = []

var profile_texture: Texture2D = null

func _ready():
	load_all_data()

func load_all_data():
	_load_vortex_profile()
	_load_dh_data()
	_load_cp2_data()
	_load_moduli_scan()
	_create_profile_texture()

func _load_vortex_profile():
	var f = FileAccess.open("res://data/vortex_profile.json", FileAccess.READ)
	if f:
		var json = JSON.parse_string(f.get_as_text())
		if json:
			vortex_profile = json
			#print("[Data] vortex_profile loaded: xi=", json.get("xi_effective", "?"))

func _load_dh_data():
	var f = FileAccess.open("res://data/dh_fixed_points.json", FileAccess.READ)
	if f:
		var json = JSON.parse_string(f.get_as_text())
		if json:
			dh_data = json
			#print("[Data] dh_data loaded: sum=", json["dh_sum"]["value"])

func _load_cp2_data():
	var f = FileAccess.open("res://data/cp2_weights.json", FileAccess.READ)
	if f:
		var json = JSON.parse_string(f.get_as_text())
		if json:
			cp2_data = json
			#print("[Data] cp2_data loaded: K=", json["koide"]["K_experiment"])

func _load_moduli_scan():
	var f = FileAccess.open("res://data/moduli_scan.json", FileAccess.READ)
	if f:
		var json = JSON.parse_string(f.get_as_text())
		if json is Array:
			moduli_scan = json
			#print("[Data] moduli_scan loaded: ", moduli_scan.size(), " points")

func _create_profile_texture():
	if not vortex_profile.has("profile_psi"):
		return
	var psi: Array = vortex_profile["profile_psi"]
	var size = psi.size()
	var img = Image.create(size, 1, false, Image.FORMAT_RF)
	for i in range(size):
		var val = clamp(psi[i], 0.0, 1.0)
		img.set_pixel(i, 0, Color(val, val, val))
	profile_texture = ImageTexture.create_from_image(img)
	#print("[Data] profile_texture created: ", size, "x1")
