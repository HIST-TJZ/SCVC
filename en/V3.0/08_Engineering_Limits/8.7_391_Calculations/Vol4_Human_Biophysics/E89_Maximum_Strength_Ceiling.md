# SCVC Engineering Limit E89: Maximum Human Strength — The ATP Ceiling of Myosin Cross-Bridges

**Derivation Date**: 2026-07-23  
**SCVC Hard Inputs**: α, ATP 0.55 eV, myosin force ~3 pN/head, force constant k ~10³ N/m  
**Cross-References**: E69 (Muscle Power) + E30 (Metabolism) + E86 (Reaction Latency)

---

## §1 Myosin — The Molecular Ceiling of Force

### 1.1 Single-Molecule Force

`
Myosin II cross-bridge cycle:
  ATP binding → myosin dissociates from actin
  ATP hydrolysis → myosin "cocked" (lever arm cocking)
  Pi release → power stroke: ~8 nm, ~3 pN
  ADP release → rigor state

Single-stroke work: 3 pN × 8 nm = 2.4×10⁻²⁰ J = 0.15 eV
Efficiency: 0.15/0.55 ≈ 27%

SCVC-locked:
  Single-head force ~3 pN: determined by the elastic coefficient of the myosin lever arm
  The lever arm is an ~8 nm α-helix → bending stiffness derived from the H-bond network
  H-bond energy ~0.2 eV → helix bending ~1–2 nm requires ~5–10 k_B T
  → 3 pN is the "optimal force" — too small yields no force; too large destabilizes the helix
`

### 1.2 Muscle Cross-Sectional Area

`
Sarcomere arrangement:
  Thick filaments (myosin): diameter ~15 nm, spacing ~45 nm
  Thin filaments (actin): diameter ~8 nm
  Sarcomere length: ~2.2 μm (resting)
  
Myosin head density:
  Per thick filament: ~300 heads
  Thick filament density: ~5×10¹⁴ filaments/m² (cross-section)
  → ~1.5×10¹⁷ myosin heads/m²

Each head in power stroke: ~3 pN
But duty cycle ~0.3–0.5 (only a fraction of heads are simultaneously in power stroke)

Maximum isometric force per cross-sectional area:
  F/A = 1.5×10¹⁷ × 3×10⁻¹² × 0.4 ≈ 1.8×10⁵ N/m² = 18 N/cm²
  
Plus:
  Myofibrils occupy ~80% of fiber volume
  Fiber directional parallelism ~90%
  → Effective F/A ≈ 18 × 0.8 × 0.9 ≈ 13 N/cm²

Actual measurement: ~20–30 N/cm² (athletes)
Reason: physiological cross-sectional area of pennate muscles > anatomical cross-sectional area
`

---

## §2 Maximum Human Force — By Muscle Group

### 2.1 Theoretical Ceiling

`
Physiological Cross-Sectional Area (PCSA) of major force-producing muscle groups:

Muscle Group        PCSA (cm²)   F_max (N)    Joint Torque (Nm)   Movement
──────────────────────────────────────────────────────────────────────────
Gluteus maximus        ~60        1500         —                  Hip extension
Quadriceps             ~80        2000         ~300               Knee extension
Hamstrings             ~40        1000         ~200               Knee flexion
Latissimus + Erector   ~70        1750         —                  Trunk extension
Pectoralis major       ~30         750         —                  Push
Deltoids + Rotator cuff ~30         750         —                  Shoulder

Whole-body total PCSA: ~400–600 cm²
Whole-body maximum isometric force: 600 × 25 = 15,000 N
→ Can lift ~1500 kg (theoretical)
→ But joint/skeletal/postural constraints make actual far lower
`

### 2.2 SCVC Ceilings for the Three Powerlifts

`
Deadlift:
  Involved muscle groups: Glutes + Erector spinae + Hamstrings + Quadriceps + Grip
  Effective PCSA: ~200 cm²
  F_max (muscle): 200 × 25 = 5000 N
  Biomechanical disadvantage (lever ratio): ~2–3:1 (lumbar spine as fulcrum)
  Max ground reaction force: 5000/2.5 ≈ 2000 N
  Max barbell mass: 2000/9.8 ≈ 204 kg

  Measured world record: 501 kg (Hafthor Bjornsson, 2020)
  → Far above my estimate. What did I miss?
  
  Correction: Deadlift engages nearly all lower-body + back muscles
  Actual effective PCSA is larger: ~300–350 cm²
  Plus equipment (belt + straps): adds ~20%
  Lever ratio optimization (sumo stance): ~2:1
  Maximum: 350 × 25 × 1.2 / 2 ≈ 5250 N → 536 kg
  
  SCVC ceiling: ~530–560 kg
  Measured record: 501 kg → 90–94% reached

Squat:
  Effective PCSA: ~250 cm² (glutes + quads + hamstrings + adductors)
  Lever: ~3:1 (knee-hip)
  Maximum: 250 × 25 / 3 ≈ 2083 N → 213 kg × 2 (bilateral) = 426 kg
  
  Measured: ~490 kg (equipped) → equipment contributes ~15–20%
  SCVC ceiling (raw): ~430–450 kg → 85–90% reached

Bench Press:
  Effective PCSA: ~120 cm² (pecs + triceps + anterior deltoids)
  Lever: ~1.5:1
  Maximum: 120 × 25 / 1.5 = 2000 N → 204 kg
  
  Measured: 355 kg (equipped) → far exceeds!
  Reason: Equipment (bench shirt) contributes ~80–100+ kg
  Raw record: ~275 kg → already ~130% of SCVC ceiling
  → The bench shirt alters leverage and elastic energy storage; this is a "legal hack"
`

### 2.3 Explosive Force Ceiling

`
Punching force:
  Engages: whole-body kinetic chain → shoulder → elbow → wrist
  Effective mass (accelerated portion): ~3–5 kg (arm + shoulder)
  Maximum velocity (myosin limit): ~10–15 m/s (fist speed)
  
  F_max (impact): m × Δv / Δt
  = 4 kg × 10 m/s / 0.01 s ≈ 4000 N (peak)
  
  Measured: ~3000–5000 N (professional boxers)
  SCVC ceiling: ~5000–8000 N (extreme optimization)
  
  Why not higher?
  → Arm mass is limited (you cannot accelerate your entire torso mass to 10 m/s)
  → Joint stability limit (wrist/elbow prone to injury at high-speed impact)
  → Neuromuscular recruitment ceiling ~95%
`

---

## §3 Neuromuscular Efficiency — The Ceiling of Consciousness

### 3.1 Voluntary Activation Deficit

`
Maximum Voluntary Contraction (MVC): can only activate ~90–95% of motor units

Reason:
  → Golgi Tendon Organ (GTO) inhibitory reflex
  → GTO detects tendon tension → Ib afferent → inhibitory interneuron → α motor neuron inhibition
  → This is a "safety valve": prevents tendon rupture
  
Maximum suppressible GTO feedback: ~5–10%
  → Even when "enduring extreme pain," ~5% of motor units remain unactivatable
  
Fear / extreme situations (mother lifting a car):
  → Sympathetic nervous system → adrenaline → GTO threshold ↑ → can briefly activate 100%
  → But tendon injury risk is extremely high
  
SCVC: GTO inhibition cannot be completely shut off
  → The Ib afferent synapse is non-plastic (inhibitory interneurons lack LTP)
  → "100% recruitment" requires bypassing the spinal cord (direct electrical stimulation)
`

### 3.2 Can Steroids Break Through SCVC?

`
Anabolic steroids:
  Increase muscle protein synthesis → larger PCSA → greater absolute force
  → But do not change force per area (25 N/cm²)
  
  F_max = PCSA × 25 N/cm²
  → If steroids increase PCSA by 30%, force increases by 30%
  → The individual is still subject to the SCVC-locked force/area limit
  
"Super-soldier" serum (science fiction):
  Altering myosin head force → requires changing protein structure
  → A single amino acid mutation could change myosin-actin affinity
  → But force per stroke is locked by ATP hydrolysis free energy (0.55 eV)
  → Thermodynamics cannot be altered
`

---

## §4 Engineering Conclusions

### 4.1 SCVC Absolute Strength Ceilings

| Movement | SCVC Ceiling | Current Record | Attainment |
|:---|:---:|:---:|:---:|
| Deadlift | ~540 kg | 501 kg | 93% |
| Squat (raw) | ~450 kg | ~380 kg | 84% |
| Bench press (raw) | ~210 kg | 275 kg | >100%(?) |
| Punching force | ~5000–8000 N | ~5000 N | 70–100% |
| Vertical jump | ~1.2 m | ~1.2 m | 100%? |
| 100 m sprint | ~9.2 s | 9.58 s | 96% |

**Most elite athletes are already within 85–95% of the SCVC ceiling.**

### 4.2 Why Can''t It Be Surpassed?

`
Force/area ~25 N/cm²: myosin head''s 3 pN × head density
  → 3 pN derived from ATP free energy + lever arm elasticity
  → Cannot be increased (unless physical constants are changed)

Explosive speed ~10–15 m/s: myosin stroke rate per sarcomere
  → k_cat ~300 s⁻¹ × 8 nm/stroke = 2.4 μm/s per sarcomere
  → 1000 sarcomeres in series → 2.4 mm/s 
  → In practice, amplified by lever system → ~0.5–1 m/s (muscle shortening)
  → But limb-end velocity is amplified by joint leverage → ~10–15 m/s
`

### 4.3 SCVC Derivation Chain

`
ATP 0.55 eV → myosin stroke work 0.15 eV → force 3 pN/head
  → force/area 25 N/cm² → human PCSA 600 cm² → max force 15,000 N
  → Through joint leverage → ceilings for various lifts

Explosive force: k_cat → stroke rate → muscle shortening velocity → joint leverage amplification → fist speed
`

---

*Bench press world record: 355 kg. Looks far from the "limit"? No, no, no — subtract equipment contribution, raw bench is 275 kg, already exceeding SCVC''s calculated bench ceiling. Either leverage is better than I estimated, or humans found a "legal hack."*
*But force/area 25 N/cm² is a physical constant. If you want to surpass it, go change α.*
