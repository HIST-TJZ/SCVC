# SCVC Engineering Limit E155: Glacier Maximum Velocity

> Deriving the physical upper bound on glacier flow velocity from SCVC constants (α → H-bond energy → ice creep activation energy).
> Core: the exponential temperature dependence of Glen's flow law is determined by the SCVC-locked H-bond rearrangement activation energy.

---

## §1. Ice Creep — SCVC Origins of Glen's Flow Law

### 1.1 Plastic Deformation of Ice

Ice crystals deform via dislocation creep. Glen's flow law:

```
ε̇ = A × τ^n

A = A₀ × exp(-E_a / k_B T)    exponential temperature dependence!

n = 3 (stress exponent for ice)
E_a ≈ 0.65 eV = 63 kJ/mol (creep activation energy)
```

**SCVC Connection: Microscopic Origin of E_a**

Dislocation motion in ice requires breaking and rearranging the hydrogen bond network. Each H-bond ∼0.1–0.3 eV:

```
Dislocation glide requires simultaneous breaking of ∼3–5 H-bonds
→ E_a ∼ 3×0.2 eV = 0.6 eV ✓
→ Matches observed 0.62–0.67 eV with high accuracy

H-bond energy derived from α:
  H₂O molecular polarizability ∝ 1/α³
  Dipole-dipole interaction energy ∝ α_pol²
  → H-bond strength ultimately determined by the fine-structure constant α
```

### 1.2 The Astonishing Consequence of Temperature Sensitivity

Exponential variation of A(T) with temperature:

```
A(0°C)  / A(-10°C)  ≈ 3×10¹² ×
A(0°C)  / A(-20°C)  ≈ 9×10¹² ×
A(0°C)  / A(-50°C)  ≈ 10²⁷ ×
```

**This means: virtually all glacier deformation is concentrated in the bottom ∼10–50 meters** (basal temperature near 0°C, surface possibly -20 to -30°C). Basal ice is 10¹³ times softer than surface ice — this is the single most central fact of glacier physics.

### 1.3 How Much Velocity Can Internal Deformation Contribute?

Surface velocity (pure creep):

```
u_surface = (2A/(n+1)) × τ_b^n × h

τ_b: basal shear stress, h: ice thickness
```

| Glacier Type | τ (bar) | Ice Thickness (m) | Creep Velocity | Notes |
|----------|---------|---------|----------|------|
| Cold small valley glacier | 1.0 | 200 | **0.02 m/day** | Nearly motionless |
| Large valley glacier | 1.5 | 800 | **0.3 m/day** | Slow |
| Thick ice stream | 2.0 | 1500 | **1.2 m/day** | Visible flow |
| Extreme outlet glacier | 5.0 | 3000 | **39 m/day = 14 km/yr** | Creep limit |
| SCVC theoretical max | 10.0 | 4000 | **415 m/day = 152 km/yr** | Pure creep only! |

**Key insight: Pure creep can reach up to ∼14 km/yr.** Jakobshavn's 17 km/yr is within the theoretical reach of pure creep — but in reality, >90% of Jakobshavn's velocity comes from basal sliding (because its stress is only ∼2 bar, ice thickness ∼800m → pure creep contributes only ∼0.5 km/yr).

---

## §2. Basal Sliding — The True Velocity Engine

### 2.1 Sliding Mechanism

Glaciers slide over their beds, lubricated by high-pressure meltwater. Sliding velocity depends on effective pressure N:

```
N = p_ice - p_water (ice overburden pressure - water pressure)

N → 0: ice nearly "floating" on its bed → friction →0 → extremely fast sliding
N large: ice firmly coupled to bedrock → slow sliding (limited by bedrock roughness)
```

### 2.2 Velocity Regimes

| Regime | N State | Velocity (m/day) | Mechanism |
|------|-------|-------------|------|
| Cold bed | N ≈ p_ice | **0.01–0.1** | Almost no sliding (frozen to bedrock) |
| Normal sliding | N > 0.5 p_ice | **0.1–1** | Ice creeps around bedrock obstacles + regelation slip |
| Enhanced sliding | 0.1 < N < 0.5 p_ice | **1–20** | High water pressure → partial decoupling |
| Near-flotation | N → 0 | **20–100** | Ice-bedrock separation → dramatic velocity increase |
| **Surge** | N → 0 + positive feedback | **100–500** | Self-reinforcing: fast → frictional heat → more water → faster |
| Physical fracture limit | ε̇ > 0.01/day | **500–1000** | Ice fractures → iceberg calving → velocity cannot increase further |

### 2.3 SCVC Limit on Surges

Glacier surges are self-reinforcing cycles: rapid flow → frictional heating → meltwater → lubrication → faster flow. Surges terminate by:
1. Upstream ice reservoir exhaustion (insufficient mass supply)
2. Subglacial hydrological reorganization (channel formation → drainage → N increases → friction restored)

**SCVC-locked surge velocity ceiling:**

```
Ceiling 1 — Mass supply: upstream ice must "feed" the surge front fast enough
  Constrained by: ice creep rate (from E_a → Glen's law → ≤~150 km/yr theoretical)

Ceiling 2 — Fracture limit: strain rate exceeds ~0.01/day → crevasse formation → iceberg calving
  Fracture toughness K_IC determined by H-bond rupture energy (each H-bond ~0.2 eV → multiple bonds rupture cooperatively)

Ceiling 3 — Available driving stress: τ_b ≤ ρgh sinα
  Maximum slope α_max ≈ 10–15° (steeper → ice avalanches rather than flows)
  → τ_max ≈ 2.5 bar → constrains achievable τ_b
```

**Actual surge records:**
- Variegated Glacier, Alaska: from 0.1 m/day → 50 m/day (500× acceleration)
- Most extreme surges: ∼100 m/day (36 km/yr)

**SCVC surge ceiling: ∼100–200 m/day (∼36–73 km/yr)** — constrained by the fracture limit and mass supply, not by the pure creep rate.

---

## §3. Where Jakobshavn's 17 km/yr Sits in SCVC Space

```
SCVC creep limit ──────────── 14 km/yr (pure deformation, τ=5 bar, h=3000m)
     ↑ only slightly above
Jakobshavn 2012 ──────── 17 km/yr (90% basal sliding)
     ↑ 
SCVC surge ceiling ─────────── 36–73 km/yr (100–200 m/day)
     ↑ 
SCVC theoretical creep max ────── 152 km/yr (τ=10 bar, but unattainable in reality)
     ↑ 
Inertial limit √(gh) ──── 3×10⁶ km/yr (never approached)
```

**Jakobshavn's position in SCVC space:**

- Pure creep contribution: ∼0.5 km/yr (τ~2 bar, h~800m)
- Sliding contribution: ∼16.5 km/yr (N greatly reduced → near-flotation)
- **SCVC permits: ✅** — 17 km/yr far below SCVC surge ceiling (~70 km/yr)
- **Acceleration headroom: approximately 3–4×** — but constrained by fracture limit and fjord geometry

### Why Can Jakobshavn Go So Fast?

Three factors converge (none prohibited by SCVC):

1. **Warm ocean water intrusion**: deep fjord warm water (~3–4°C) melts the ice shelf base → loss of buttressing → acceleration
2. **Retrograde bed slope**: bedrock deepens inland → ice body becomes progressively thicker → flux ↑ (marine ice sheet instability)
3. **High meltwater pressure**: surface meltwater reaches the bed via moulins → N→0

---

## §4. Thwaites "Doomsday Glacier" — Theoretical Fastest Collapse Time

### 4.1 Current State

```
Thwaites Glacier (West Antarctica):
  Current velocity: ~2 km/yr (at grounding line)
  Width: ~120 km
  Ice thickness (grounding line): 800–1200 m
  Ice volume: ~65 cm global sea-level equivalent
  Bed: retrograde (deepens inland) → Marine Ice Sheet Instability
```

### 4.2 Collapse Scenarios

| Scenario | Velocity (km/yr) | Collapse Time (yr) | Sea-Level Rise Rate (mm/yr) |
|------|-------------|-------------|---------------------|
| Current trend | 2 | **~250** | 2.6 |
| Accelerated | 5 | **~100** | 6.5 |
| Rapid collapse | 10 | **~50** | 13 |
| Jakobshavn-class | 20 | **~25** | 26 |
| SCVC surge ceiling | 50 | **~10** | 65 |

### 4.3 SCVC-Locked Fastest Collapse Rate

Marine Ice Cliff Instability (MICI) is currently the most extreme collapse mechanism:

```
Ice cliff taller than ∼100 m → ice fracture toughness insufficient to support it → sustained calving

Calving front retreat rate ≈ ice flow velocity

For Thwaites (500 km to ice divide):
  Fastest credible rate: 10–20 km/yr → 25–50 years for complete collapse

SCVC constraints:
  1. Ice cliff limit height determined by H-bond fracture toughness → ∼80–110 m (matches observations)
  2. Retreat rate cannot exceed the rate at which "ice can be delivered to the calving front"
      → locked by ice creep + sliding combination → ≤50 km/yr (most extreme)
```

### 4.4 SCVC's Final Verdict

```
Thwaites fastest collapse: ∼25–50 years (10–20 km/yr)
SCVC does not permit faster (because ice delivery is constrained by creep rate → from E_a)
Much slower (>200 years) is the more likely median scenario

But SCVC permits: once MICI is triggered, collapse can be "self-sustaining + accelerating"
(retrograde bed → thicker ice → greater flux → faster retreat → positive feedback)

Key uncertainty is not SCVC physics, but:
  1. Bed topography (how far inland does the retrograde slope extend?)
  2. Ocean warming rate (determines ice shelf melt speed)
  3. Ice stream interactions (adjacent glacier collapse → loss of lateral buttressing → acceleration)
```

---

## §5. SCVC Summary: Glacier Velocity Ladder

| Mechanism | Typical Velocity | Record | SCVC Ceiling | Determining Factor |
|------|---------|------|----------|----------|
| Pure creep (cold bed) | ~0.01 m/day | — | — | H-bond activation energy E_a |
| Pure creep (warm bed) | ~1 m/day | ~40 m/day | **~400 m/day** | τ³ × exp(-E_a/kT) |
| Normal sliding | ~1 m/day | — | — | Bed roughness + N |
| Enhanced sliding | ~10 m/day | ~46 m/day | **~100 m/day** | N → 0 |
| Surge | ~50 m/day | ~100 m/day | **~200 m/day** | Fracture + mass supply |
| Inertial limit | — | — | 3×10⁶ km/yr | √(gh) — never approached |

**Core SCVC Insights:**

1. **Activation energy 0.65 eV locks everything** — the exponential temperature dependence of ice creep comes from H-bond rearrangement, and H-bond energy is derived from α. This gives glacier physics a **hard temperature sensitivity**: basal ice (0°C) is ∼10¹³ times softer than surface ice (-20°C).

2. **Creep sets a "supply ceiling" for sliding** — even if the bed were completely frictionless (N=0), a glacier cannot accelerate without bound, because upstream ice must "feed" the fast-flowing zone at a finite creep rate.

3. **Jakobshavn's 17 km/yr is within SCVC's permitted range (∼1/4 of ceiling)** — headroom for further acceleration exists, but is constrained by the fracture limit and fjord geometry.

4. **Thwaites' "doomsday" scenario (25–50 year collapse) is SCVC-permitted** — but not much faster than this. Once triggered, the MICI mechanism can be self-sustaining, but the ice delivery rate (from E_a) sets a physical hard floor.
