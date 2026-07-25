====================================================================
SCVC Engineering Limit E55: Cavitation Onset — Not a Design Problem, a Physical Inevitability
====================================================================

**All derivations based on SCVC Constants Reference (zero free parameters, α=1/(4π³+π²+π)).**

--------------------------------------------------------------------
§1. Theoretical Tensile Strength of Water — Derived from SCVC H-Bond Energy
--------------------------------------------------------------------

【H-bond network = water's "tensile skeleton"】

  H-bond energy: 0.20 eV = 3.2×10⁻²⁰ J (SCVC electronegativity → N-H···O and O-H···O bond energy derivation)
  Per H₂O molecule: ~3.5 H-bonds (liquid phase average)
  O-O H-bond distance: 2.75 Å
  Water molecule cross-sectional area: ~9.7 Å²

  Theoretical tensile strength (Orowan formula):
    σ_theory = √(E·γ/a₀)
             = √(2.2 GPa × 0.073 J/m² / 2.75 Å)
             = **~760 MPa**

  Direct SCVC derivation (fracture-surface H-bond force/area):
    Single-bond rupture force = 0.20 eV / 2.75 Å ≈ 0.12 nN
    Areal density = 1 / 9.7 Å² ≈ 1.0×10¹⁹ m⁻²
    σ_SCVC ≈ 0.12 nN × 10¹⁹ m⁻² ≈ **~1200 MPa**

  ▸ **SCVC theoretical tensile strength: ~700-1200 MPa (~7000-12000 atm)**

【Ideal vs Reality: The 100-10,000× Gap from Cavitation Nuclei】

  Water Quality                 Measured Tensile/Cavitation Threshold   From Theory
  ──────────────────────────────────────────────────
  SCVC theoretical pure water   700-1200 MPa                            —
  Laboratory degassed pure water 10-30 MPa                              40-100×
  Tap water                     0.1-1 MPa                               1000×
  Seawater                      0.05-0.5 MPa                            2000-10000×
  Bubble-laden water            ~0.01 MPa                               100,000×

  ▸ **Cavitation nuclei** (dissolved bubbles 10-100 μm, particulates, wall defects) are the root of the gap
  ▸ SCVC H-bond energy gives the strength of "ideal water," but engineering water can never reach it
  ▸ Cavitation is not a "design flaw" — it is a physical inevitability of SCVC thermodynamics + the necessary presence of gas in water

--------------------------------------------------------------------
§2. Propeller Cavitation — Physical Ceiling of Ship Speed
--------------------------------------------------------------------

【Cavitation number σ】

  σ = (p − p_v) / (½ρV²)
  σ < σ_crit → cavitation
  σ_crit ≈ 0.3-1.0 (depends on blade section design)

  Propeller at 5 m immersion depth (seawater, 20°C):
    p_static ≈ 1.52 bar, p_v ≈ 0.023 bar
    Cavitation-free max tip speed: V_tip = √(2×1.50×10⁵/(1025×0.5)) ≈ 24 m/s ≈ 47 knots

  But actual propeller tip speeds:
    Merchant ships: 30-50 m/s → σ = 0.18-0.5 → **partial cavitation inevitable**
    Naval vessels: 40-60 m/s → σ = 0.08-0.28 → **developed cavitation**
    High-speed craft: 60-80 m/s → σ < 0.05 → **supercavitation**

  ▸ **At any useful speed, propeller cavitation is unavoidable**
  ▸ → Engineering is not about "avoiding cavitation" but "designing for controlled cavitation"

【Ship speed ceiling — Not the engine, it's cavitation!】

  Cavitation-limited max ship speed (conventional cavitation-free propeller, J≈0.8-1.2):
    V_ship_max ≈ V_tip_max × J/π ≈ 24 × 0.9/π ≈ **7 m/s ≈ 13 knots**

  Strategies to break through:
    1. Increase blade area → reduce unit loading → σ_crit↓ → V↑ ~20-30%
    2. Increase immersion depth → p↑ → military subs can reach extreme depths → V↑
    3. Supercavitating propellers → intentional cavity formation → drag reduction → V↑ (30-50 knots)
    4. Waterjet propulsion → internal high pressure → delay cavitation → V↑ (40-60 knots)
    5. Surface-piercing propellers → semi-submerged → ventilated to atmosphere → stable cavity → V↑ (60-100 knots)

  ▸ **Surface ship speed ceiling ~50-60 knots (waterjet), jointly locked by cavitation + drag**
  ▸ Faster → must leave the water surface (hydrofoils, hovercraft, ground-effect vehicles)

--------------------------------------------------------------------
§3. Supercavitating Torpedo — Speed Ceiling
--------------------------------------------------------------------

【VA-111 Shkval: 200 knots ≈ 370 km/h — Current Record】

  Supercavitation principle: nose cavitator + gas injection → entire torpedo enveloped in a bubble
  → Water friction replaced by water vapor + gas friction → C_D drops from ~0.5 to ~0.08

  Drag power (D=0.533m, C_D≈0.08):
    200 km/h:   1.6 MW   ← Shkval
    370 km/h:   9.9 MW   ← Current record
    500 km/h:  25  MW    ← Next generation?
    700 km/h:  67  MW    ← Chemical rocket achievable
   1000 km/h: 196  MW    ← Unrealistic (rocket engine ceiling for 0.5m diameter ~50MW)
   1500 km/h: 662  MW    ← Physically excluded

【SCVC-locked ceiling】

  (1) Drag: P ∝ V³ → 8× power per doubling of speed → chemical propulsion ceiling ~500-600 km/h
  (2) Cavity stability: cavity wall = water surface (H-bond network) → Rayleigh-Taylor instability
      → Cavity length ~L_cavity ∝ σ × C_D × D → reaches ~10m at ~500 km/h
      → Wake closure → high-pressure pulses → instability → physical ceiling
  (3) Noise: cavity collapse noise ~180-200 dB → self-guidance systems unusable
      → **Supercavitating torpedoes are effectively "straight-running torpedoes," no terminal guidance possible**

  ▸ Practical ceiling: **~500-600 km/h** (requires >25 MW rocket propulsion)
  ▸ Physical ceiling: ~1000 km/h (cavity stability + power density dual walls)

--------------------------------------------------------------------
§4. Acoustic Cavitation and Sonoluminescence — SCVC Energy Density Ceiling
--------------------------------------------------------------------

【Bubble Collapse: Rayleigh-Plesset + Adiabatic Compression】

  Bubble R₀=100 μm → R_min=0.5 μm:
    Volume compression ratio: 8×10⁶×
    PV work (1 atm): 4.2×10⁻⁷ J
    Post-collapse energy density: **8×10¹¹ J/m³ ≈ 800 GJ/m³**
    Compare: SCVC H-bond energy density: 3.7 GJ/m³

  ▸ Collapse energy density far exceeds water's H-bond energy density → water molecules will inevitably be torn apart!

  Temperature ceiling (SCVC-locked):
    Ideal adiabatic (γ=1.4): T_max ≈ 173,000 K (unrealistic — assumes no chemical reactions)
    
    SCVC's staircase energy absorption barriers:
      ~5,000 K:    H-bonds fully broken (0.20 eV × 3.5 bonds)
      ~10,000 K:   O-H covalent bonds begin rupturing (4.8 eV) → H₂O → H + OH
      ~50,000 K:   Complete atomization (9.6 eV per H₂O) → H, O
      ~100,000 K:  H ionization → H⁺ + e⁻ (13.6 eV, SCVC H 1s orbital energy)
    
    ▸ Measured sonoluminescence temperature: 5,000-20,000 K
    ▸ **SCVC ceiling: ~50,000-100,000 K** (all energy beyond this goes into bond breaking)
    ▸ Sonoluminescence energy ceiling determined by SCVC bond energy absorption spectrum
    ▸ >100,000 K → water ionizes to plasma → all energy absorbed by ionization → T will not rise further

--------------------------------------------------------------------
§5. Engineering Conclusions
--------------------------------------------------------------------

【Cavitation — Physical Inevitability Verdict】

  Phenomenon                  Avoidable?          SCVC Root Cause
  ─────────────────────────────────────────────────
  Propeller cavitation (>10 kts)  No               H-bond energy sets water's tensile ceiling
  Pump cavitation (high RPM)      No               Cavitation nuclei necessarily present
  Valve/orifice cavitation         No               Bernoulli principle + finite p_v
  Ultrasonic cavitation            No (intentional) H-bond network energy absorption
  Water hammer cavitation          No               Transient negative pressure exceeds water strength

  ▸ **Cavitation is not an engineering mistake — in a K_B T > 0 world, dissolved gas in water + weak H-bonds make it a physical inevitability**

【SCVC Ceilings by Domain】

  Application                   Current Level           SCVC Ceiling
  ─────────────────────────────────────────────────────
  Surface ships (waterjet)      40-60 knots             ~60 knots (cavitation+drag joint wall)
  Supercavitating torpedo       200 knots (~370 km/h)   ~300 knots (~560 km/h)
  Sonoluminescence temperature  ~20,000 K               ~50,000-100,000 K
  Pump NPSHr (cavitation margin) 1-5 m                  ~0.1 m (SCVC theoretical minimum)
  "Silent submarine propeller"  Infeasible >10 knots    Physical inevitability

【SCVC Water Bond Energy Quick Reference】

  H-bond energy         0.20 eV       →  Tensile strength ~1000 MPa (theoretical)
  O-H covalent bond     4.8 eV        →  Cavity collapse >5000K begins bond rupture
  H-H bond energy       4.52 eV       →  Sonoluminescence product H₂
  H 1s ionization energy 13.6 eV      →  Cavity collapse >100,000K ionization wall
  Water molecule area   9.7 Å²        →  H-bond areal density → tensile strength
  Water surface tension 0.073 J/m²    →  Bubble surface energy → cavity nucleus stability

====================================================================
* Ideal water can withstand ~1000 MPa negative pressure — directly from SCVC H-bond energy. But in reality cavitation nuclei reduce this 100-10,000×.
* Propeller cavitation is a physical inevitability at any speed >10 knots — not a design problem, but a corollary of "water has finite bond energy + water contains bubbles."
* Supercavitating torpedo ceiling ~500-600 km/h — V³ drag growth + cavity stability doubly locked by water surface physics.
* Sonoluminescence temperature ceiling ~50,000-100,000 K — all energy beyond this is swallowed by the staircase absorption of SCVC bond energies.
====================================================================
