extends Camera3D

@export var target: Node3D
@export var distance: float = 12.0
@export var min_distance: float = 1.0
@export var max_distance: float = 200.0
@export var orbit_speed: float = 0.004
@export var pan_speed: float = 0.02
@export var zoom_speed: float = 0.8
@export var auto_rotate: bool = true
@export var auto_rotate_speed: float = 0.12

var theta: float = 0.0
var phi: float = PI/5.0
var orbit_active: bool = false
var pan_active: bool = false
var last_mouse: Vector2
var pivot: Vector3 = Vector3.ZERO
var track_com: bool = false  # F toggles: follow center-of-mass

func _ready():
	if not target:
		target = get_parent()
	_update_camera()

func _input(event):
	if event is InputEventMouseButton:
		match event.button_index:
			MOUSE_BUTTON_RIGHT:
				orbit_active = event.pressed
				last_mouse = event.position
				if event.pressed:
					auto_rotate = false
			MOUSE_BUTTON_MIDDLE:
				pan_active = event.pressed
				last_mouse = event.position
			MOUSE_BUTTON_WHEEL_UP:
				distance = max(min_distance, distance - zoom_speed)
				_update_camera()
			MOUSE_BUTTON_WHEEL_DOWN:
				distance = min(max_distance, distance + zoom_speed)
				_update_camera()

	if event is InputEventMouseMotion:
		if orbit_active:
			var delta = event.position - last_mouse
			theta -= delta.x * orbit_speed
			phi = clamp(phi - delta.y * orbit_speed, -PI/2.0 + 0.05, PI/2.0 - 0.05)
			last_mouse = event.position
			_update_camera()
		elif pan_active:
			var delta = event.position - last_mouse
			var right = global_transform.basis.x
			var up = global_transform.basis.y
			pivot -= right * delta.x * pan_speed - up * delta.y * pan_speed
			last_mouse = event.position
			_update_camera()



func _process(_delta):
	# Smooth keyboard movement (checked every frame)
	var move_speed: float = 8.0 * _delta
	var fwd = -global_transform.basis.z
	fwd.y = 0; fwd = fwd.normalized()
	var right = global_transform.basis.x
	right.y = 0; right = right.normalized()

	if Input.is_key_pressed(KEY_W): pivot += fwd * move_speed
	if Input.is_key_pressed(KEY_S): pivot -= fwd * move_speed
	if Input.is_key_pressed(KEY_A): pivot -= right * move_speed
	if Input.is_key_pressed(KEY_D): pivot += right * move_speed
	if Input.is_key_pressed(KEY_Q): pivot.y -= move_speed
	if Input.is_key_pressed(KEY_E): pivot.y += move_speed
	if Input.is_key_pressed(KEY_HOME): _reset_view()

	if auto_rotate and not orbit_active and not pan_active:
		theta += auto_rotate_speed * _delta
	_update_camera()

func _reset_view():
	pivot = Vector3.ZERO
	distance = 12.0

func _update_camera():
	var pos = pivot + Vector3(
		distance * cos(phi) * cos(theta),
		distance * sin(phi),
		distance * cos(phi) * sin(theta)
	)
	global_position = pos
	look_at(pivot, Vector3.UP)
