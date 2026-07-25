====================================================================
SCVC Engineering Limit E46: Detonation / Explosion — Maximum Detonation Velocity + Maximum Explosive Yield
====================================================================

【Input Constants】(from _SCVC Engineering Constants Reference.md)
--------------------------------------------------------------
N≡N triple bond energy = 9.8 eV            (strongest chemical bond — king of detonation products)
C-C single 3.6 eV, C=C 6.3 eV, C≡C 8.7 eV
Strongest ionic bond ~10-12 eV
Atomic density n ~ 10²³ cm⁻³
Force constant k ~ 10³ N/m
α = 1/137.0363
m_e = 0.5110 MeV/c²
α_s = 1/(16π)
Strongest nuclear binding energy/nucleon ~8.8 MeV (⁵⁶Fe)
D-T fusion 17.6 MeV/reaction
²³⁵U fission ~200 MeV/nucleus
M_Pl = 2.435×10¹⁸ GeV
--------------------------------------------------------------


1. Detonation Velocity Ceiling — Chapman-Jouguet Theory
==============================================================

1.1 CJ Detonation Velocity
--------------------------------------------------------------
    D = √(2(γ²−1)Q) × f(ρ₀)    (ideal gas simplification)
    P_CJ = ρ₀ D² / (γ+1)         (CJ pressure)

    where Q = heat of explosion (J/kg), γ = product adiabatic index (~1.2-1.3),
    ρ₀ = initial charge density.

    More precise Kamlet-Jacobs semi-empirical formula (CHNO explosives):
    D = A · N^(1/2) · M^(1/4) · Q^(1/4) · (1 + B ρ₀)

    ⚫ Core: D ∝ √(Q × ρ₀). Energy density and charge density jointly determine detonation velocity.

1.2 Detonation Velocity Ceiling of Current Chemical Explosives
--------------------------------------------------------------
    Explosive      Q (kJ/g)    ρ₀ (g/cm³)    D (km/s)    P_CJ (GPa)
    ──────────────────────────────────────────────────────────────
    TNT            4.2          1.65          6.9          21
    RDX            5.6          1.82          8.7          34
    HMX            5.7          1.91          9.1          39
    CL-20 (HNIW)   6.3          2.04          9.5          43
    ONC (octanitrocubane) 7.0   2.0           9.8          48
    ──────────────────────────────────────────────────────────────

    ⚫ Traditional CHNO explosive ceiling ≈ 10 km/s, Q ≈ 7 kJ/g.
       Root cause: limited bond energy differences among C, H, N, O → net heat release ceiling is here.

1.3 Nitrogen Clusters — Breaking the CHNO Ceiling
--------------------------------------------------------------
    If reactants contain only N atoms and products are entirely N₂:

    · Polymeric nitrogen (cg-N, cubic gauche structure):
      All N-N single bonds (~1.7 eV/bond) → ½ N≡N (4.9 eV/N)
      Q ≈ 22 kJ/g  (≈ 4× HMX!)
      ρ₀ ≈ 3.0 g/cm³ (high-pressure phase)
      D ≈ 15-16 km/s (conservative estimate)
      P_CJ ≈ 200-300 GPa  → exceeds any material strength!

    · Octaazacubane N₈ (never synthesized):
      12 N-N single bonds → 4 N≡N
      Q ≈ 16-20 kJ/g, ρ₀ ≈ 2.0
      D ≈ 14-15 km/s (theoretical prediction)

    · Pentazolate salts N₅⁺N₅⁻ (partially synthesized):
      2 aromatic N₅ rings → 5 N≡N
      Q ≈ 18-23 kJ/g, ρ₀ ≈ 2.2
      D ≈ 15-17 km/s (theoretical)

    ⚫ Chemical explosive theoretical detonation velocity ceiling ≈ 16-18 km/s.
       Roughly 1.7-2.0× HMX. A meaningful improvement, but not revolutionary.

1.4 Metallic Hydrogen — If Metastable
--------------------------------------------------------------
    Metallic hydrogen (high-pressure metallic phase) → H₂ molecular gas:
    Energy release ~0.5-2 eV/H (highly uncertain)
    Q ≈ 50-200 kJ/g (if metastable)
    D ≈ 30-60 km/s (if metastable!)
    P_CJ ≈ 1,000+ GPa

    ⚫ But this rests on the enormous assumption that "metallic hydrogen is metastable at ambient pressure."
       Most theories predict it is not metastable.
    ⚫ SCVC: Pauli repulsion + zero-point motion prevent metallic hydrogen metastability.
       Hydrogen atoms are too light (κ = h/m_e circulation constraint → large zero-point kinetic energy → lattice unstable).


2. Maximum Energy Density
==============================================================

2.1 Map of Chemical Bond Energies
--------------------------------------------------------------
    Fundamental principle of explosives: break weak bonds + form strong bonds → net exothermic.

    Reactant "instability" sources:
    · Strained rings (cubane, nitrogen clusters)
    · Oxidizer + fuel in the same molecule (nitro compounds)
    · High-energy bond angle distortion (cage structures)

    Products always pursue:
    · N≡N (9.8 eV) — champion product bond
    · C≡O (11.2 eV) — extremely strong, but CO itself is a fuel
    · H-O-H (4.8 eV/OH) — stable light product
    · CO₂ (2×8.3 eV) — deep oxidation product

2.2 Energy Density Spectrum
--------------------------------------------------------------
    Explosive Type              Q (kJ/g)     Relative to HMX    Status
    ─────────────────────────────────────────────────────────
    TNT                          4.2           0.74×           Traditional
    HMX                          5.7           1.00×           Current military standard
    CL-20                        6.3           1.11×           Highest deployed
    ONC                          7.0           1.23×           Laboratory
    cg-N (polymeric nitrogen)    ~22            ~3.9×           Theoretical/high-P
    N₅⁺N₅⁻                       ~20            ~3.5×           Theoretical
    Free atomic N → N₂           **34**          **6.0×**        **Absolute SCVC ceiling**
    ─────────────────────────────────────────────────────────
    Metallic H (if metastable)   ~50-200        ~9-35×          Highly speculative
    ─────────────────────────────────────────────────────────
    **Nuclear fission**          **~8×10⁴**     **~1.4×10⁴×**   **Different physics**
    **D-T fusion**               **~3.4×10⁵**   **~6×10⁴×**    **Different physics**

    ⚫ The SCVC absolute ceiling is 34 kJ/g — all N atoms are free atoms,
       then recombine to N₂. This is "the maximum energy chemical bonds can release per unit mass."
    ⚫ Nuclear energy is ~10⁴-10⁵× higher because it releases nuclear binding energy (MeV-level)
       rather than chemical bond energy (eV-level). This gap is SCVC-locked forever.


3. Maximum Explosive Yield — From Chemistry to Nucleus
==============================================================

3.1 Why Is the Chemical-Nuclear Gap So Enormous?
--------------------------------------------------------------
    Chemical energy scale:  Ry = α²m_e c²/2 = 13.6 eV
    Nuclear energy scale:   ~8.8 MeV/nucleon

    Ratio = 8.8×10⁶ / 13.6 ≈ 6.5×10⁵

    ┌──────────────────────────────────────────────────────────┐
    │ This ratio is fundamentally:                              │
    │                                                          │
    │   E_nuc / E_chem ≈ (α_s / α) × (m_p / m_e) ≈ 6×10⁵       │
    │                                                          │
    │ α = 1/137   (electromagnetic, sets chemical bond energy)  │
    │ α_s = 1/(16π) ≈ 0.02 (strong interaction, sets nuclear    │
    │        binding energy)                                   │
    │                                                          │
    │ Nuclear forces are ~10³× stronger AND nucleon mass is     │
    │ ~10³× heavier than electrons → combined ~10⁶× gap.      │
    │                                                          │
    │ This is not an engineering problem. It is the universe's  │
    │ fundamental design. Chemistry can never approach nuclear. │
    └──────────────────────────────────────────────────────────┘

3.2 Nuclear Weapon Yield
--------------------------------------------------------------
    Fission weapon yield:
    Y_max (pure fission) ≈ 500 kt TNT (practical)
                        ≈ 1 Mt TNT (absolute, critical mass & efficiency limits)

    Fusion-boosted / thermonuclear:
    Y_max (practical) ≈ 50-100 Mt (Tsar Bomba, limited by delivery)
    Y_max (SCVC)      → No physical ceiling (can chain arbitrarily large devices)

    ⚫ SCVC: Nuclear weapon yield has no physical ceiling —
       fusion fuel mass can be added without limit.
       But delivery constrains practical yield to ~50-100 Mt.

3.3 "Can an Explosion Destroy the Earth?"
--------------------------------------------------------------
    Gravitational binding energy of Earth:
    U_grav ≈ (3/5) × G M² / R ≈ 2.2×10³² J ≈ 5×10¹⁶ Mt

    Tsar Bomba (50 Mt): U_grav / 50 Mt ≈ 10¹⁵
    → Need 10¹⁵ Tsar Bombas to destroy Earth

    Total global nuclear arsenal (peak, ~1985):
    ~15,000 Mt → U_grav / 15,000 Mt ≈ 3×10¹²
    → Still 3×10¹²× insufficient

    ⚫ SCVC verdict: Earth cannot be destroyed by any feasible
       nuclear arsenal. Binding energy is too enormous.


4. Engineering Conclusions
==============================================================

4.1 "Strongest Conventional Explosive" — SCVC Verdict
--------------------------------------------------------------
    ⚫ CL-20 (deployed, ~6.3 kJ/g) → already ~18% of SCVC ceiling
    ⚫ ONC (laboratory, ~7.0 kJ/g) → ~21%
    ⚫ cg-N (theoretical, ~22 kJ/g) → ~65% — the true engineering ceiling
    ⚫ Free atomic N (34 kJ/g) → 100% of SCVC ceiling — permanently unreachable

    SCVC prediction: If cg-N can be stabilized at ambient conditions,
    it would be ~4× HMX in energy density — a "super-HMX." But the N₂
    molecule has already won: at 34 kJ/g, chemistry is completely drained.

4.2 Explosive Welding and Forming
--------------------------------------------------------------
    ┌─────────────────────────────────────────────────────┐
    │ Explosive welding requires: P_CJ must exceed the    │
    │ dynamic yield strength of the metals to be joined.  │
    │                                                        │
    │ Metal yield strength: 0.3-1.5 GPa (static)             │
    │                      ~1-5 GPa (dynamic/shock)          │
    │                                                        │
    │ HMX P_CJ ≈ 40-70 GPa → far exceeds all metal yields ✓  │
    │                                                        │
    │ Existing explosives are already sufficient to weld      │
    │ any metal combination. Stronger explosives (N₈)        │
    │ would not improve welding — they would shatter         │
    │ the plates due to excessive pressure.                  │
    │                                                        │
    │ Explosive forming: similarly, HMX-class is sufficient. │
    │ Limit pressure ≈ ultimate strength of the formed       │
    │ material. Diamond (SCVC σ_theor ≈ 50-100 GPa) could     │
    │ theoretically be shock-formed by HMX (70 GPa) —         │
    │ but it's too brittle as powder.                        │
    │                                                        │
    │ cg-N (P_CJ ≈ 200-300 GPa) would exceed the strength     │
    │ of any material → cannot be used for forming            │
    │ (would obliterate everything).                          │
    │ → Use limited to: scenarios needing extreme pressure   │
    │    but not "forming."                                  │
    └─────────────────────────────────────────────────────┘

4.3 SCVC Detonation Limits Summary Table
--------------------------------------------------------------
  Physical Quantity                   SCVC Ceiling          Current Extreme      Headroom
  ──────────────────────────────────────────────────────────────────────
  Explosive energy density (practical) ~25 kJ/g             5.7 (HMX)           ~4×
  Explosive energy density (absolute)  34 kJ/g              —                   ~6×
  Detonation velocity (practical)      ~16-18 km/s          9.5 (CL-20)         ~1.8×
  Detonation velocity (metal H, if metastable) ~30-60 km/s  —                   Uncertain
  CJ pressure                          ~300 GPa (cg-N)      43 GPa (CL-20)      ~7×
  Chemical↔Nuclear energy gap          ~10⁷×                 —                   Permanent

  ⚫ Core insights:
    · Chemical explosives have explored ~60% of the theoretical ceiling (5.7/34).
      All-nitrogen explosives can push this to ~60-70% (20-25/34).
      But 34 kJ/g cannot be broken — N₂ bond energy is the ultimate hard wall.
    · The 10⁷× chemical-nuclear gap is one of SCVC's deepest engineering conclusions:
      not an engineering problem, but the universe's fundamental design.
    · Detonation pressure can exceed any material's strength → explosions can "destroy everything."
      Chemical bond energies are sufficient to produce pressures exceeding Pauli repulsion.


====================================================================
Appendix: Key Calculations
====================================================================

  Quantity                           Formula                                     SCVC Value
  ───────────────────────────────────────────────────────────────────────────────────
  N≡N bond energy                    SCVC constant                               9.8 eV
  Polymeric nitrogen Q              (E_N≡N/2 − E_N-N) / m_N                     22 kJ/g
  N₈ cubane Q                       (4E_N≡N − 12E_N-N) / 8m_N                   16-20 kJ/g
  Free N atom Q                     E_N≡N / 2m_N                                34 kJ/g
  CJ detonation velocity (scaling)  D ∝ √(Q × ρ₀)                               ~15-18 km/s
  CJ pressure                        P_CJ = ρ₀ D² / (γ+1)                        200-300 GPa
  Chemical energy scale              Ry = α² m_e c² / 2                          13.6 eV
  Nuclear energy scale               Strongest nuclear binding energy/nucleon    8.8 MeV
  Energy gap                         E_nuc / E_chem                              ~6.5×10⁵

====================================================================
SCVC Engineering Constants reference: all from _SCVC Engineering Constants Reference.md
Zero free parameters | Derived from π polynomials | 2.22 ppm precision
====================================================================
