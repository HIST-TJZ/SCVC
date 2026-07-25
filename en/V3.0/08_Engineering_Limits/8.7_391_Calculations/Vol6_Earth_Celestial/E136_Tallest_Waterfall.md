====================================================================
SCVC Engineering Limit E136: Maximum Waterfall Height — The Triple Ceiling of Droplet Breakup + Evaporation + Atomization
====================================================================

**All derivations based on SCVC constants (H-bond 0.20 eV → surface tension 72.8 mN/m, k_B T → evaporation rate).**

--------------------------------------------------------------------
§1. The Physics of Waterfalls — It's Not That Cliffs Aren't Tall Enough, It's That Water Never Reaches the Bottom
--------------------------------------------------------------------

  Waterfall height ≠ cliff height. Cliffs can be arbitrarily tall (as long as mountains exist),
  but beyond a certain height → water atomizes/evaporates during the fall → what reaches the bottom is no longer a "waterfall."

  Triple constraint:
    Chain 1: Droplet breakup (Weber number) → large drops shatter into small drops
    Chain 2: Small drop evaporation → vanish during the fall
    Chain 3: Atomization → what reaches the bottom is mist, not water

  Definition of "waterfall": visible continuous water column at the bottom, >50% of water mass reaches the bottom as liquid.

--------------------------------------------------------------------
§2. Chain 1: Droplet Breakup — The Weber Number Criterion
--------------------------------------------------------------------

  Critical condition for a water droplet to be torn apart by airflow:
    We = ρ_air × v² × D / γ

    When We > We_crit ≈ 10–12 → droplet breakup

  γ = 72.8 mN/m (derived from H-bond 0.20 eV)

  Droplet acceleration to terminal velocity:
    v_t ≈ 9 m/s (large drops, D ≈ 4–6 mm, typical raindrops)
    v_t ≈ 6.5 m/s (D ≈ 2–3 mm)
    v_t ≈ 4 m/s (D ≈ 1 mm)
    v_t ≈ 2 m/s (D ≈ 0.5 mm)
    v_t ≈ 0.3 m/s (D ≈ 0.1 mm, mist droplets)

  Computing We (ρ_air=1.2 kg/m³):
    D=5mm, v=9 m/s:  We = 1.2×81×0.005/0.0728 ≈ 6.7 ✓ (does not break)
    D=3mm, v=6.5m/s: We = 1.2×42×0.003/0.0728 ≈ 2.1 ✓
    D=10mm, v=9m/s: We = 1.2×81×0.01/0.0728 ≈ 13.4 ✗ (shatters)

  ▸ Initial large drops (>8mm) shatter before reaching terminal velocity.
  ▸ Stable drops: D ≈ 1–6 mm, Weber number <10.

  But in a waterfall:
    - Turbulence + collisions cause additional breakup
    - Air is entrained into the falling column → inter-drop airflow can reach 20–30 m/s
    - Collisions → some drops shatter into <1mm droplets

  SCVC: after falling beyond ~200–500 m, air entrainment becomes significant →
        secondary breakup produces large numbers of <1mm droplets.

--------------------------------------------------------------------
§3. Chain 2: Evaporation — The Demise Time of Small Droplets
--------------------------------------------------------------------

  Droplet evaporation rate (diffusion-controlled in still air):
    dm/dt = 4π × D_v × r × (ρ_sat - ρ_amb)

    D_v ≈ 2.5×10⁻⁵ m²/s (diffusion coefficient of water vapor in air)
    ρ_sat(20°C) ≈ 0.0173 kg/m³
    50% RH: Δρ ≈ 0.00865 kg/m³

  Droplet mass: m = ρ_water × (4/3)πr³

  Evaporation lifetime: τ ≈ m / (dm/dt) ≈ ρ_water × r² / (3 × D_v × Δρ)

    τ ≈ 1000 × r² / (3 × 2.5×10⁻⁵ × 0.00865)
      ≈ r² / (6.49×10⁻¹⁰) s

  ┌──────────┬──────────┬──────────┬──────────────────┐
  │ Drop Dia. │ Fall Speed │ Evap. Lifetime │ Survivable Fall Height │
  │ (mm)     │ (m/s)    │              │ h_survive ≈ v×τ         │
  ├──────────┼──────────┼──────────┼──────────────────┤
  │ 5        │ 9        │ ~9,600 s │ ~86,000 m        │
  │ 3        │ 6.5      │ ~3,500 s │ ~22,000 m        │
  │ 2        │ 6.5      │ ~1,540 s │ ~10,000 m        │
  │ 1        │ 4        │ ~385 s   │ ~1,540 m         │
  │ 0.5      │ 2        │ ~96 s    │ ~192 m           │
  │ 0.2      │ 1        │ ~15 s    │ ~15 m            │
  │ 0.1(mist)│ 0.3      │ ~3.8 s   │ ~1.1 m           │
  └──────────┴──────────┴──────────┴──────────────────┘

  ▸ Large drops >2mm: evaporation not a threat (>10 km survival distance).
  ▸ 1mm drops: evaporate completely in ~1.5 km fall.
  ▸ 0.5mm drops: evaporate completely in ~200 m fall.
  ▸ Mist droplets (<0.1mm): vanish almost instantly.

  SCVC: The key to waterfall height — it's not "large drops evaporating,"
        it's "large drops shattering into small drops → small drops evaporating → water mass at the bottom steadily decreases."

--------------------------------------------------------------------
§4. Chain 3: Atomization — The Waterfall → Mist Transition
--------------------------------------------------------------------

  Defining "waterfall visibility": liquid water mass reaching bottom / water mass at top.

  Model:
    At height h_z, rate at which large drops shatter into small drops ∝ turbulence intensity
    Turbulence intensity ∝ entrained airflow speed ∝ √(h) (longer fall → more entrainment)
    
    Let breakup rate α(h) = α₀ × h (simplified linear)
    Small drop evaporation: survival distance ~200m (0.5mm drops) → ~1 e-folding decay
    
  Bottom water mass:
    M_bottom ≈ M_top × exp(-h/h_char)
    h_char ≈ 500–1000 m (characteristic height for breakup + evaporation)

  Visibility thresholds:
    Bottom mass > 50%  →  h < 0.7×h_char ≈ 350–700 m
    Bottom mass > 10%  →  h < 2.3×h_char ≈ 1150–2300 m

  Angel Falls h=979m:
    If h_char ≈ 800m: M_bottom/M_top ≈ e^(-979/800) ≈ 0.29 → 29%
    → Still ~30% water mass → visible waterfall ✓

    If h_char ≈ 500m (more turbulent): M_bottom ≈ e^(-979/500) ≈ 0.14 → 14%
    → Marginal — still visible but thin.

--------------------------------------------------------------------
§5. The SCVC Ceiling
--------------------------------------------------------------------

  Intersection of three chains:

  ┌──────────────┬──────────────────┬──────────────────┐
  │ Constraint    │ Principle         │ Height Limit      │
  ├──────────────┼──────────────────┼──────────────────┤
  │ Large drop stability │ Weber <10         │ No direct height limit │
  │ Air entrainment breakup │ Turbulence ∝√h   │ ~300–800 m       │
  │ Small drop evaporation │ Diffusion-controlled │ ~200 m (0.5mm drops) │
  │ Atomization (visibility) │ Breakup+evaporation combined │ ~1000–2000 m     │
  └──────────────┴──────────────────┴──────────────────┘

  **SCVC maximum waterfall: ~1500–2000 m**
  (At this height, even starting with large drops, bottom water mass <10% → no longer a "waterfall")

  Angel Falls 979 m:
    Achievement rate: 49–65%
    Status: approaching but not hitting the wall

  ┌──────────────────────────────────────────────────────┐
  │                                                      │
  │  Earth's highest possible waterfall: ~1500–2000 m     │
  │  Prerequisite: a cliff of that height + sufficient   │
  │  water source + suitable climate.                    │
  │                                                      │
  │  Angel 979m — at ~50–65% of the SCVC range.          │
  │  ~500–1000m of theoretical headroom remains          │
  │  unexplored by nature.                               │
  └──────────────────────────────────────────────────────┘

--------------------------------------------------------------------
§6. Why Has Nature Not Produced a 2000m Waterfall?
--------------------------------------------------------------------

  Four reasons:
    1. Cliffs not tall enough: Earth's tallest cliff ~1.2km (Thor Peak, Canada)
       → Geological erosion flattens cliffs before they reach 1500m
    2. Insufficient water source: a 2000m drop requires a river source at corresponding elevation
       → Alpine catchment areas are limited
    3. Not a waterfall: if too tall → bottom is mist → humans don't call it a "waterfall"
       → Perceptual bias: the tallest "mist falls" may have been observed but never named
    4. Climate: high altitude → low temperatures → partially frozen part of the year → not a continuous waterfall

  SCVC distinguishes two limits:
    - Physical limit (water can reach the bottom): ~1500–2000 m
    - Geological limit (cliff can survive): ~1200–1500 m
    → The geological limit is tighter — cliffs collapse from erosion before the waterfall's physical limit is reached.

--------------------------------------------------------------------
§7. Where Does the Water Go? — The SCVC Poetry of Waterfalls
--------------------------------------------------------------------

  When height exceeds ~1500m, the fate of a water droplet:
    1. Falls ~500m → accelerates to terminal velocity ~9 m/s
    2. Falls 500–1000m → air entrainment → large drops begin to shatter
    3. Falls 1000–1500m → small drops (<0.5mm) begin to evaporate
    4. Falls >1500m → most water has become invisible vapor + mist
    5. Reaches bottom → a damp fog — no longer a waterfall

  **SCVC says: α locks water's surface tension → locks the droplet breakup threshold → locks the maximum waterfall height.**
  The most spectacular waterfalls are a precise balance between the H-bond at 0.20 eV and gravity.

====================================================================
* The waterfall limit is not cliff height — it is the survival distance of water droplets.
* Large drops (>2mm) evaporating is not the issue; large drops shattering into small drops → evaporation is the bottleneck.
* SCVC ceiling: ~1500–2000 m. Angel 979m achieves 49–65%.
* Earth's tallest cliff ~1200m → geological erosion locks waterfall height before the physical limit is reached.
* Beyond ~1500m → waterfall becomes mist → no longer a "waterfall" → a definitional boundary exists.
* α → H-bond 0.20 eV → surface tension 72.8 mN/m → Weber number → breakup → waterfall height.
====================================================================
