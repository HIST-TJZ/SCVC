extends Control

func _draw() -> void:
	var main = get_node("/root/Main")
	if main and main.has_method("_on_unrolled_draw"):
		main._on_unrolled_draw()
