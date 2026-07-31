extends Camera3D

@export var target: Node3D
@export var distance := 8.0
@export var pitch_min := -80.0
@export var pitch_max := 80.0
@export var zoom_min := 2.0
@export var zoom_max := 30.0
@export var orbit_speed := 0.3
@export var zoom_speed := 1.0

var yaw := 45.0   # degrees, horizontal rotation around target
var pitch := -30.0 # degrees, vertical angle

func _ready() -> void:
	if not target:
		target = get_parent()
	_update_transform()

func _input(event: InputEvent) -> void:
	# Right mouse button for orbit
	if event is InputEventMouseMotion and Input.is_mouse_button_pressed(MOUSE_BUTTON_RIGHT):
		yaw -= event.relative.x * orbit_speed
		pitch -= event.relative.y * orbit_speed
		pitch = clamp(pitch, pitch_min, pitch_max)
		_update_transform()
	
	# Scroll wheel for zoom
	if event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_WHEEL_UP:
			distance = max(zoom_min, distance - zoom_speed * 0.5)
			_update_transform()
		elif event.button_index == MOUSE_BUTTON_WHEEL_DOWN:
			distance = min(zoom_max, distance + zoom_speed * 0.5)
			_update_transform()

func _update_transform() -> void:
	if not target:
		return
	var yaw_rad := deg_to_rad(yaw)
	var pitch_rad := deg_to_rad(pitch)
	
	var dir := Vector3(
		cos(pitch_rad) * sin(yaw_rad),
		sin(pitch_rad),
		cos(pitch_rad) * cos(yaw_rad)
	)
	
	position = target.global_position + dir * distance
	look_at(target.global_position, Vector3.UP)
