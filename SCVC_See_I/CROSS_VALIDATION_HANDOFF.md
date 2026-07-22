# SCVC Godot Simulation — Cross-Validation Handoff

## What This Is
Godot 4.6 interactive physics simulation of **SCVC theory** (Standard Model from CP² Vortex Condensate).
Point vortices in SU(3)×SU(2)×U(1) gauge space emerge as Standard Model particles via 4D winding vectors `(wc1, wc2, ww, wy)`.

## Project Location
`C:\Users\20606\Desktop\SCVC-github\SCVC_See_I\`

## File Map
```
scenes/main_scene.tscn          — Main scene (CanvasLayer, Camera3D, WorldEnvironment)
scripts/main.gd                 — Controller: input, UI, panel, presets, placement
scripts/vortex_physics.gd       — Physics engine: forces, binding, pool, springs
scripts/vortex_object.gd        — Individual vortex: winding, drag, display color, label, physics_update
scripts/camera_orbit.gd         — Free 3D camera: right-drag orbit, middle-drag pan, WASD, scroll
```

## SCVC Theory (What You Need to Know)

### Winding Vectors
Every particle is a point vortex with 4D winding `(wc1, wc2, ww, wy)`:
- **(wc1, wc2)**: SU(3) color charge (R=0°, G=120°, B=240°)
- **(ww)**: SU(2) weak isospin I₃
- **(wy)**: U(1) hypercharge Y

Electric charge Q = I₃ + Y = ww + wy.

### Standard Model Winding Values
```
Quarks (up-type, ww=+0.5, wy=+0.1667):
  u(red):   [ 1.0,  0.0,    0.5, 0.1667]   Q = +2/3
  u(green): [-0.5,  0.866,  0.5, 0.1667]   Q = +2/3
  u(blue):  [-0.5, -0.866,  0.5, 0.1667]   Q = +2/3

Quarks (down-type, ww=-0.5, wy=+0.1667):
  d(red):   [ 1.0,  0.0,   -0.5, 0.1667]   Q = -1/3
  d(green): [-0.5,  0.866, -0.5, 0.1667]   Q = -1/3
  d(blue):  [-0.5, -0.866, -0.5, 0.1667]   Q = -1/3

Leptons (no color, wc1=wc2=0):
  electron:  [0, 0, -0.5, -0.5]   Q = -1
  neutrino:  [0, 0,  0.5, -0.5]   Q = 0
```

### Anti-Particles
Negate ALL windings: anti(w) = -w. Detected by `w_y < 0`.

### Proton/Neutron
- Proton = u(亮) + u(中) + d(暗) → total color = 0 (singlet), total Q = +1
- Neutron = d(亮) + d(中) + u(暗) → total color = 0 (singlet), total Q = 0

### SCVC Mass Factors (electron=1.0)
```
MF_E=1.0   MF_NU=0.01   MF_U=4.2426   MF_D=9.1317
MF_MU=206.8   MF_TAU=3507.0   MF_S=180.2   MF_C=2480.0
MF_B=8004.0   MF_T=339840.0
```

## Physics Engine (vortex_physics.gd)

### Forces
- **Color (strong)**: G_STRONG=3.30, log potential, acts on SU(3) winding dot product
- **EM**: G_EM=2.00, log potential, couples to Q = ww+wy
- **Z boson**: Yukawa with r_Z=0.003 (effectively zero range)
- **Confinement**: σ=1.5 linear, only for non-singlet color pairs

### Binding
- Checks 2/3/4-body combinations every 4 frames
- Filters out neutrinos (non-interacting) from binding count
- Up to 400 active particles
- Color singlet: total (wc1,wc2) < 0.15 threshold
- BIND_DIST=1.2, BREAK_DIST=2.2

### Key Constants
- XI=0.25 (interaction range)
- E_CORE=1.5 (core energy)
- POOL_SIZE=400 (object pool)
- C=4.90 (light speed in sim units)
- Damping: 0.96→0.995 smooth based on nearest neighbor

## Conventions
- ALL files: UTF-8 without BOM, LF line endings, TAB indentation
- Color scheme: Up-type=RED family, Down-type=GREEN family
  - SU(3) color direction → brightness (亮/中/暗 = bright/medium/dark)
  - Anti-up → CYAN, Anti-down → MAGENTA
- 3D labels: "u 亮", "d 暗", "e⁻", "e⁺", "ν", "a u 亮" (anti)
- Panel buttons use English: "u(bright)", "d(dark)", etc.

## Controls
| Key | Action |
|-----|--------|
| Shift | Anti-particle toggle |
| P | Time freeze |
| K | Toggle spring lines |
| M | Full SM mode |
| L | Chinese/English |
| Del | Clear all |
| [ / ] | Placement height |
| Space | Snapshot mode |

## What to Cross-Validate
1. Physics correctness: Are forces computed correctly for all particle types?
2. Anti-particle detection: `w_y < 0` for quarks, proper negation logic
3. Binding logic: correct singlet detection, momentum conservation
4. Display colors matching winding values (e⁻=purple, e⁺=gold, u=red, d=green)
5. Mass factors used properly in xi_for_pair and core energy
6. Object pool: no leaks, proper recycling
7. Edge cases: anti-quarks, heavy quarks, pair creation from breaks

## Recent Bug Fixes Applied
- display_color: specific e⁺/e⁻ checks moved before generic fallbacks
- emergent_name: anti-quark uses `w_w*w_y > 0` (not just `w_w > 0`)
- Drag preserves y-position (doesn't reset to 0)
- _xi_for_pair uses object.mass_factor (SCVC π-polynomials)
- _core_energy in total_energy uses object.mass_factor
- UI text: removed dead keyboard shortcuts
- Chinese translations: 亮/中/暗 not 红/绿/蓝
- Spring toggle: K key, visible flag respected
- Panel buttons: add_child was missing, now fixed
- Neutrino filter in binding check