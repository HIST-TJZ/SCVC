filepath = r"C:\Users\20606\Desktop\SCVC-github\SCVC_See_I\scripts\vortex_physics.gd"
with open(filepath, "rb") as f:
    text = f.read().decode("utf-8")

idx = text.find("vfm_enabled and ring.target_orbit_radius <= 0.0:")
start = text.rfind("\n", 0, idx-50)
start = text.rfind("\n", 0, start-1)
end = text.find("physics_update(delta, merged)", idx)
end = text.find("\n", end) + 1

old_block = text[start:end]
new_block = old_block

# Replacements
new_block = new_block.replace("_compute_vfm_forces", "_compute_vfm_velocities")
new_block = new_block.replace("Biot-Savart -> Magnus forces (flavor-blind)", "Biot-Savart velocities (advect with flow)")
new_block = new_block.replace("Merge: F_total = F_BS + F_gauge+Pauli", "Merge: v_VFM + F_gauge*dt/m")
new_block = new_block.replace("var merged: Array = []", "var merged_vels: Array = []")
new_block = new_block.replace("var f_total: Vector3 = Vector3.ZERO", "var v_total: Vector3 = Vector3.ZERO")
new_block = new_block.replace("f_total += vfm_forces[i]", "v_total += vfm_vels[i]")
new_block = new_block.replace("f_total += gauge_forces[i]", "v_total += gauge_forces[i] * delta / max(ring.mass_factor, 0.01)")
new_block = new_block.replace("merged.append(f_total)", "merged_vels.append(v_total)")
new_block = new_block.replace('ring.set_meta("_ext_forces", merged)', 'ring.set_meta("_vfm_velocities", merged_vels)')
new_block = new_block.replace("ring.physics_update(delta, merged)", "ring.physics_update_vfm(delta)")
new_block = new_block.replace("vfm_forces", "vfm_vels")
new_block = new_block.replace("V1 Three-Channel VFM: Channel A (BS) + Channel B (gauge) + Channel C (Pauli)", "V1 Three-Channel VFM: BS velocities + gauge/Pauli forces")

text = text[:start] + new_block + text[end:]
text = text.replace("\r\r\n", "\r\n")

with open(filepath, "wb") as f:
    f.write(text.encode("utf-8"))
print("DONE")
