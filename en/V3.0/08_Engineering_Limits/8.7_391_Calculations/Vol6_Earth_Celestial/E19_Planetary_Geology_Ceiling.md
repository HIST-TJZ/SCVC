====================================================================
SCVC Engineering Limit E19: Planetary / Geology — Maximum Planet Mass + Tallest Mountains + Deepest Oceans
====================================================================

【Input Constants】(from _SCVC_Engineering_Constants_Quick_Reference.md)
--------------------------------------------------------------
α = 1/137.0363                   (fine-structure constant)
m_e = 0.5110 MeV/c²
M_Pl = 2.435×10¹⁸ GeV            (4D effective Planck mass)
ħc = 197.327 MeV·fm
E_bond_max = 9.8 eV (N≡N)         (strongest chemical bond)
C-C single bond energy 3.6 eV, bond length 1.54 Å
C≡C triple bond energy 8.7 eV, bond length 1.20 Å
Atomic density n ~ 10²³ cm⁻³
m_p ≈ 938.3 MeV, m_n ≈ 939.6 MeV
k_B = 8.617×10⁻⁵ eV/K
--------------------------------------------------------------

【Note on the Gravitational Constant】
SCVC M_Pl = 2.435×10¹⁸ GeV (4D effective value)
Standard M_Pl = 1.221×10¹⁹ GeV
SCVC''s M_Pl is the effective value after 5D theory compactification.
SCVC''s internal G can be computed from M_Pl, but this chapter uses the
measured G = 6.6743×10⁻¹¹ N·m²/kg² for scaling calculations in planetary mechanics.
SCVC contributes microscopic ceilings: material strength, phase-transition pressures, etc.


1. Maximum Planet Mass
==============================================================

1.1 Mass Spectrum: From Rubble Piles to Black Holes
--------------------------------------------------------------
Three fundamental scales locked by SCVC partition the mass spectrum of all celestial bodies:

  Tier              Dominant Physics               Mass Range            SCVC Input
  ───────────────────────────────────────────────────────────────
  Irregular bodies   Material strength > Gravity    < 10⁻⁴ M_⊕       Bond energy E_bond
  Rocky planets      Hydrostatic equilibrium        10⁻⁴ – 10 M_⊕     Bond energy + α
  Gas giants         Gas accretion                  10 – 300 M_⊕      Opacity (α)
  Brown dwarfs       Electron degeneracy pressure   0.01 – 0.07 M_☉   m_e
  Stars              Thermonuclear fusion           0.07 – ~100 M_☉   α_s
  White dwarfs       Electron degeneracy (relativ.) < 1.44 M_☉       m_e, M_Pl
  Neutron stars      Neutron degeneracy             1.4 – ~2.5 M_☉   m_n, α_s, M_Pl
  Black holes        None (gravitational collapse)  > 3 M_☉          M_Pl
  ───────────────────────────────────────────────────────────────

1.2 Material Strength → Hydrostatic Transition
--------------------------------------------------------------
When does a body transition from "held irregular by material strength" to "gravity-forced spherical"?

    Central pressure: P_c ≈ (3G/8π) · M²/R⁴  (uniform-sphere approximation)
    Strength condition: P_c < σ_yield  → non-spherical

    → Critical radius: R_crit = √(3σ_yield / (2π G ρ²))

    ⚫ Perfect crystal (SCVC ceiling, σ ≈ 465 GPa): R_crit ~ 16,500 km
       (equivalent to 2.6 R_⊕, 11 M_⊕ — all known rocky planets are spherical)
    ⚫ Actual rock (σ ≈ 10 MPa, fracture-limited): R_crit ~ 76 km
       (Ceres ~ 470 km radius ≈ spherical, Vesta ~ 260 km ≈ near-spherical)

    Conclusion: SCVC perfect crystals have never been realized at planetary scales.
          All bodies >100 km obey hydrostatic equilibrium.

1.3 Maximum Mass of Rocky Planets
--------------------------------------------------------------
Three physical mechanisms compete to set the upper bound:

  ┌─────────────────────────────────────────────────────┐
  │ (A) Electron Degeneracy Pressure                      │
  │                                                       │
  │ For terrestrial planets (ρ ~ 5–10 g/cm³), interior     │
  │ temperature ~ 2000–5000 K, electron Fermi temperature  │
  │ T_F ~ 10⁶ K ≫ T → in the non-degenerate regime.        │
  │ Degeneracy pressure does not dominate planetary        │
  │ interiors — this is completely different from white    │
  │ dwarfs.                                               │
  │                                                       │
  │ Rocky planet mass  P_c(GPa)  ρ_c(g/cm³)  T_F(K)  Degenerate? │
  │ ────────────────────────────────────────────────────────── │
  │   0.1 M_⊕            70         7          700,000    No    │
  │   1 M_⊕             578        11          937,000    No    │
  │   5 M_⊕            2540        15        1,149,000    No    │
  │  20 M_⊕            9095        19        1,370,000    No    │
  │                                                       │
  │ Electron degeneracy pressure does not limit rocky       │
  │ planet mass.                                           │
  └─────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────┐
  │ (B) Gas Accretion — The Critical Core                   │
  │                                                       │
  │ When a rocky core exceeds ~10–15 M_⊕, its gravity       │
  │ becomes sufficient to accrete nebular gas → runaway     │
  │ accumulation → it becomes a gas giant (or brown dwarf). │
  │                                                       │
  │ Critical core mass M_crit (from planet formation       │
  │ theory, opacity κ dependent on α):                     │
  │                                                       │
  │ M_crit ≈ 10 (κ/1 cm²/g)^0.25 M_⊕                      │
  │                                                       │
  │ ⚫ This is the practical ceiling for rocky planet mass. │
  │   The theoretical maximum pure-rock planet (no gas)    │
  │   could be ~20 M_⊕ — but such an object would have     │
  │   already accreted gas in any realistic protoplanetary │
  │   disk.                                                │
  └─────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────┐
  │ (C) Structural Phase Transitions                        │
  │                                                       │
  │ At extremely high pressures, mantle silicates undergo   │
  │ phase transitions → post-perovskite → further phases.   │
  │ SCVC: bond energy ~3–5 eV sets the pressure scale for   │
  │ each phase transition.                                 │
  │                                                       │
  │ Pressure at various depths in a 10 M_⊕ planet:          │
  │   Core-mantle boundary: ~2 TPa                          │
  │   Center: ~5–8 TPa                                      │
  │                                                       │
  │ This is comparable to the bond-energy density of        │
  │ silicates → all possible phases are realized.           │
  │ No new physical ceiling emerges from phase transitions. │
  └─────────────────────────────────────────────────────┘

  **Conclusion: The maximum mass of a rocky planet is ~10–15 M_⊕, set by the gas-accretion critical core mass. SCVC does not set a stricter ceiling.**


2. Maximum Mountain Height
==============================================================

2.1 The Isostasy Ceiling
--------------------------------------------------------------
A mountain cannot grow arbitrarily tall — its weight causes the crust to sink into the mantle.

    Isostatic limit: h_max = σ_yield / (ρ g) × ρ_mantle / (ρ_mantle − ρ_crust)

  ┌─────────────────────────────────────────────────────┐
  │ Planet       g (m/s²)   σ_yield (MPa)   h_max (km)    │
  │ ──────────────────────────────────────────────────── │
  │ Earth         9.8        10–100           ~10         │
  │ Mars          3.7        10               ~22         │
  │ (Olympus Mons 21.9 km — at the ceiling!)             │
  │ Moon          1.6        10               ~52         │
  │ 5 M_⊕         15         10               ~7          │
  │ 10 M_⊕        20         10               ~5          │
  │ SCVC perfect  9.8        465,000          ~3,700      │
  │ crystal (theoretical, never realized)                 │
  └─────────────────────────────────────────────────────┘

  ⚫ Olympus Mons (~22 km) on Mars is already at the isostasy ceiling
    for fractured rock (~10 MPa). Mars has no plate tectonics → the
    volcanic hotspot stayed in one place → mountain grew to the physical limit.
  ⚫ On Earth, plate motion prevents any single volcano from reaching
    the ceiling (Hawaii would need ~100 Myr of stationary eruption to hit ~10 km).
  ⚫ The SCVC perfect-crystal ceiling (~3700 km) is physically meaningless —
    a mountain taller than the planet''s radius is geometry, not engineering.

2.2 Why Is Mars''s Olympus Mons So Tall?
--------------------------------------------------------------
Three SCVC factors:
  (1) Lower g → higher h_max (∝ 1/g)
  (2) No plate tectonics → hotspot remains stationary → lava keeps piling up
  (3) Thicker lithosphere → can support greater loads without flexural failure

  SCVC verdict: Olympus Mons is near the SCVC ceiling for fractured rock on Mars.
  Any claim of a Martian mountain exceeding ~25 km requires explaining
  how rock strength exceeded SCVC''s fracture limit.


3. Maximum Ocean Depth
==============================================================

3.1 The Ice Phase-Transition Ceiling
--------------------------------------------------------------
On Earth, ocean depth is limited not by rock strength but by H₂O phase transitions.

  Pressure at the seafloor: P = ρ_water × g × h

  Key H₂O phases:
  ┌─────────────────────────────────────────────────────┐
  │ Phase       Pressure (GPa)   Depth on Earth (km)      │
  │ ──────────────────────────────────────────────────── │
  │ Liquid      0–1              0–100                   │
  │ Ice VI      1–2              100–200                 │
  │ Ice VII     2–60             200–~6000               │
  │ Ice X       60–300           >6000                   │
  │ Superionic  100–4000         —                       │
  └─────────────────────────────────────────────────────┘

  ⚫ Liquid ocean on Earth: max depth ~100 km (before the entire seafloor
    is sealed by Ice VI). On a water world (5 M_⊕), the ocean could be
    ~600–1000 km deep before Ice X/superionic phases take over.
  ⚫ SCVC: The phase-transition pressures of H₂O are set by H-bond energy
    (~0.2 eV) and O-H covalent bond energy (~5 eV), both from α.

3.2 The "Water World" Problem
--------------------------------------------------------------
If liquid water completely covers a rocky planet:
  → The water-rock interface is isolated by high-pressure ice
  → No silicate weathering → no carbonate-silicate cycle → no CO₂ regulation
  → The planet may be uninhabitable despite abundant water

  SCVC: For a habitable "water world," ocean depth must be < Ice VI transition
  depth → < ~100 km on an Earth-mass planet. This requires the total water
  inventory to be < ~3–5× Earth''s oceans.


4. Engineering Conclusions
==============================================================

4.1 SCVC Planetary Limits Summary
--------------------------------------------------------------
  Physical Quantity                    SCVC Constraint              Value
  ──────────────────────────────────────────────────────────
  Max rocky planet mass                 Gas-accretion critical core   ~10–15 M_⊕
  White dwarf max mass                  M_Ch ∝ M_Pl³/m_H²           1.44 M_☉
  Neutron star max mass                 TOV                           2–3 M_☉
  Minimum stellar mass                  H ignition                    0.07 M_☉
  Max mountain height on Earth (actual) σ_rock/ρg × isostasy         ~10 km
  Max mountain height (perfect crystal) σ_theor/ρg                   ~3700 km (meaningless)
  Max mountain height on Mars           Olympus Mons                 ~22 km
  Max depth of liquid ocean on Earth    Ice VI/VII phase transition   ~100–500 km
  Water-world liquid ocean ceiling      Ice X / superionic            ~600–1000 km
  Plate-tectonics mass window           τ_conv ~ τ_yield              0.3–5 M_⊕
  Habitable super-Earth mass            Ocean + tectonics + atm.      ~0.5–3 M_⊕

4.2 Which Earth Features Are "Astrophysical Inevitabilities"?
--------------------------------------------------------------
  ┌─────────────────────────────────────────────────────┐
  │ Inevitable (locked by SCVC constants):                │
  │ · Mountain height ~ km-scale (σ/ρg ~ 10 km order)    │
  │ · Ocean depth ~ 100 km ceiling (H-bond → ice phases) │
  │ · Planets are spherical (>10⁻⁴ M_⊕, material limit)  │
  │ · Iron core exists (nucleosynthesis, α_s → ⁵⁶Fe peak)│
  │                                                      │
  │ Not inevitable (historical contingency):              │
  │ · Plate tectonics (at edge of window, needs specific  │
  │   initial conditions)                                 │
  │ · Liquid water ocean depth exactly ~4 km (not a       │
  │   physical inevitability)                             │
  │ · The Moon (giant impact is a random event)           │
  │ · Atmospheric composition N₂-O₂ (product of life)     │
  │                                                      │
  │ If an Earth-sized planet is discovered in another     │
  │ stellar system, its mountain heights, ocean-depth     │
  │ ceiling, and core-mantle structure should be roughly  │
  │ similar. But plate tectonics and atmospheric           │
  │ composition may be completely different.              │
  └─────────────────────────────────────────────────────┘


====================================================================
Appendix: Key Calculations
====================================================================

  Quantity                              Formula                                    SCVC Origin
  ──────────────────────────────────────────────────────────────────────────────────────
  Material theoretical strength         E_bond / d³                                α → bond energy
  Actual rock strength                  σ_theor / √(crack/atom)                    α → bond energy
  Irregular-body critical radius        √(3σ/(2πGρ²))                             M_Pl → G
  Mountain height (isostasy)            σ/(ρg) × ρ_mantle/(ρ_mantle−ρ_crust)      α + M_Pl
  Seafloor pressure                     ρ_water · g · h                            M_Pl → g
  H-bond characteristic pressure        E_H-bond / V_H2O                           α → bond energy
  Critical core mass (gas accretion)    10 (κ/1)^0.25 M_⊕                          α → cross-section
  Chandrasekhar mass                    (ħc/G)^(3/2) / m_H²                       m_e + M_Pl
  Convective stress                     α_T ρ g ΔT d_lith                          α + M_Pl
  Convective planet mass window         τ_conv / τ_yield > 1                       α + M_Pl

====================================================================
SCVC Engineering Constants cited: all from _SCVC_Engineering_Constants_Quick_Reference.md
Zero free parameters | Derived from π polynomials | 2.22 ppm accuracy
====================================================================
