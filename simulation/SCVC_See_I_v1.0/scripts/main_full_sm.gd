# main_full_sm.gd -- extends main.gd, starts in full SM mode
extends "res://scripts/main.gd"

func _ready():
	full_sm_mode = true
	super._ready()
	_update_ui_labels()