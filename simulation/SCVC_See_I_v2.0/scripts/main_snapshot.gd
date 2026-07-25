# main_snapshot.gd -- extends main.gd, starts in snapshot mode
extends "res://scripts/main.gd"

func _ready():
	super._ready()
	if physics:
		physics.snapshot_mode = true
		for v in physics.vortices:
			if is_instance_valid(v): v.visible = false
	_update_status()