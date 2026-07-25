====================================================================
SCVC Engineering Limits E162: Artificial Photosynthesis Efficiency Ceiling
====================================================================

**All derivations based on SCVC Constants Quick-Reference Table. References E3 photovoltaic limits and E5 catalytic overpotentials.**
Core difference: artificial photosynthesis = PV + chemical synthesis → voltage penalty → efficiency below pure PV.

--------------------------------------------------------------------
§1. Sunlight → Hydrogen (STH) — Efficiency Ceiling
--------------------------------------------------------------------

【Voltage Requirement for Water Splitting — Triple Stack】

  V_rev (H₂O → H₂ + ½O₂)           = 1.23 V  (thermodynamic minimum)
  η_OER (oxygen evolution, E5 floor) = 0.37 V  (*OOH–*OH scaling relation)
  η_HER (hydrogen evolution, Pt is optimal) = 0.05 V
  η_ohm (membrane resistance + contact + bubbles) = 0.10 V
  ─────────────────────────────────────────
  Required photovoltage V_needed      = 1.75 V

  ▸ This is 2.5× higher than pure PV (V ≈ 0.7 V for Si) → this is the "synthesis tax"

【Single-Junction STH】

  The light absorber must simultaneously supply sufficient current and voltage:
    Voltage requirement: V_mpp > 1.75 V → band gap E_g > ~2.1 eV
    Current requirement: high E_g → low fraction of solar photons absorbed

  Band gap E_g    V_mpp (typical)   Usable Photon Fraction   STH (max)
  ─────────────────────────────────────────────────────────────
  1.1 eV          0.7 V             75%                       0% (V insufficient)
  1.4 eV          1.0 V             55%                       0%
  1.7 eV          1.2 V             38%                       0%
  2.0 eV          1.4 V             25%                       0%
  2.2 eV          1.6 V             17%                       0%
  2.5 eV          1.9 V             11%                       ~9%
  3.0 eV          2.3 V              6%                       ~10%

  ▸ **Single-absorber STH ceiling: ~10–12%** (extremely narrow band-gap–voltage window)
  ▸ Current best single absorbers: ~5–8% (BiVO₄, Cu₂O, Ta₃N₅)

【Tandem Absorbers — Breaking the Single-Junction Ceiling】

  Dual absorber: top cell (E_g ≈ 1.7 eV) + bottom cell (E_g ≈ 1.1 eV)
    Current matching: ~15–18 mA/cm² (limited by high-band-gap top cell)
    Voltage sum: V_top ≈ 1.2 V + V_bottom ≈ 0.7 V = 1.9 V > 1.75 V ✓

    STH_max = J_matched × V_needed × FF / P_sun
            = 16 × 1.75 × 0.85 / 100 ≈ 24%

  Triple absorber: E_g ≈ 1.9/1.4/0.9 eV → STH ≈ 28–32%

  ▸ **Dual-junction tandem STH ceiling: ~24–28%**
  ▸ **Triple-junction tandem STH ceiling: ~28–32%**
  ▸ Current lab-best dual-junction: ~15–19% (III-V semiconductors)

【PV + Electrolyzer (Decoupled) — Bypassing Voltage Matching】

  PV module (η ≈ 25%) × PEM electrolyzer (η ≈ 75%) = 18.8%
  → Lower than integrated but already demonstrated → the most practical current route
  → SCVC ceiling: η_PV (30%) × η_electrolysis (82%) ≈ 24.6%

--------------------------------------------------------------------
§2. Sunlight → Carbon-Based Fuels (CO₂ Reduction) — Heavier "Synthesis Tax"
--------------------------------------------------------------------

【Methanol: CO₂ + 3H₂O → CH₃OH + 1.5O₂ (6 electrons)】

  V_rev = ΔG/(6F) = 702 kJ/mol ÷ (6×96485) = 1.21 V
  η_CO₂RR (C–C coupling + multi-step protonation) = 0.30–0.50 V
  η_OER (E5 floor)                                 = 0.37 V
  η_ohm                                             = 0.15 V
  ─────────────────────────────────────────────────────────
  V_needed ≈ 2.0–2.2 V

  Dual-junction tandem: STH ≈ 15–20% (more stringent voltage requirement)
  Triple-junction tandem: STH ≈ 18–24%
  Decoupled PV + electrolysis: η_PV (25%) × η (65%) ≈ 16%

【Methane: CO₂ + 2H₂O → CH₄ + 2O₂ (8 electrons)】

  V_rev = 891/(8F) = 1.15 V
  V_needed ≈ 2.1–2.3 V
  Dual-junction tandem STH ≈ 13–18%

【Efficiency Penalty Sources for Carbon-Based Fuels】

  Reaction           e⁻ count    V_rev    V_needed    STH_tandem    vs. H₂
  ────────────────────────────────────────────────────────────────────────────
  H₂                 2            1.23 V    1.75 V       24–28%      Baseline
  CO (syngas)        2            1.33 V    1.90 V       20–24%      −15%
  CH₃OH              6            1.21 V    2.10 V       15–20%      −30%
  CH₄                8            1.15 V    2.20 V       13–18%      −35%
  C₂H₄               12           1.10 V    2.30 V       10–15%      −45%

  ▸ Each additional C–C bond and C–H bond requires more overpotential
  ▸ **SCVC ceiling for carbon-based fuels is 30–50% lower than H₂**
  ▸ "Liquid solar fuels" are physically penalized → this is an SCVC-locked trade-off

--------------------------------------------------------------------
§3. Comparison with Natural Photosynthesis — Why a 10× Difference?
--------------------------------------------------------------------

【Efficiency Chain of Natural Photosynthesis (C3 Plants)】

  Loss Layer                                    Remaining Efficiency
  ─────────────────────────────────────────────────────────────────
  Solar spectrum (PAR 45%)                       45%
  Photon energy excess (2.25 eV → 1.82 eV usable) 36% (×0.81)
  Quantum requirement (8 photons/CO₂)            12.4% (×0.34)
  Photorespiration (C3, ~30% carbon loss)         8.7% (×0.70)
  Mitochondrial respiration (~25%)                6.5% (×0.75)
  **C3 theoretical maximum: ~4.6%** | **C4 theoretical maximum: ~6.0%**

  Measured:
    Typical crop annual mean: 0.5–1.5%
    Sugarcane/Miscanthus (peak): 3–4%
    Microalgae (photobioreactor): 5–7%

【SCVC Comparison: Natural vs. Artificial】

  Technology Route                  Efficiency Ceiling    Current Best      Improvement Headroom
  ──────────────────────────────────────────────────────────────────────────────────────────
  Natural C3 land plants            ~5%                   1–2%              2–3×
  Natural C4 plants                 ~6%                   3–4%              1.5×
  Microalgae (engineered)           ~10%                  5–7%              1.5×
  Artificial STH single absorber    ~12%                  5–8%              1.5–2×
  Artificial STH dual-junction      ~28%                  15–19%            1.5×
  Artificial CH₃OH dual-junction    ~20%                  5–10%             2–3×
  PV + electrolyzer (decoupled)     ~25%                  20–22%            1.2×

  ▸ **Artificial photosynthesis is 4–6× higher than natural plants (ceiling vs. ceiling)**
  ▸ Current artificial levels (~5–10%) already exceed natural measured (~1–3%)
  ▸ But still 2–4× headroom to the SCVC ceiling → positive!

【Why Didn't Evolution Select for High Efficiency? — SCVC Perspective】

  The "inefficiency" of natural photosynthesis is not an SCVC physical limit, but an evolutionary optimum:

  1. RuBisCO (carbon-fixing enzyme): turnover number ~3/s → the slowest enzyme in nature
     Reason: CO₂ vs. O₂ discrimination (from SCVC H-bond energy difference ~0.2 eV)
     Must sacrifice speed for selectivity → this is a physical trade-off, but evolution could do better

  2. Chlorophyll over-absorption: absorbs the full visible spectrum but only uses ~1.8 eV (PSII) + 1.1 eV (PSI)
     Reason: evolved in low-light environments (underwater/forest understory) → broad absorption = survival advantage
     Wasted as heat under high light → this is "historical baggage," not a physical wall

  3. Photorespiration (30% carbon loss): RuBisCO mistakenly fixes O₂
     Reason: O₂/H₂O are photosynthetic products → cannot be fully excluded from the chloroplast
     C4 plants solved this through spatial separation → proves evolution can improve

  4. Self-repair / self-replication: protein half-life ~hours to days → continuous consumption of photosynthate
     Artificial catalyst advantage: no self-repair needed (but requires replacement)

  ▸ **Nature's "inefficiency" is fixable — SCVC does not prohibit a 10× efficiency improvement**
  ▸ **The greatest advantage of artificial photosynthesis: evolution's historical baggage can be discarded**

--------------------------------------------------------------------
§4. Engineering Conclusions
--------------------------------------------------------------------

【"Sunlight → Fuel" Efficiency Tiers】

  Efficiency     Technology Route                      SCVC Verdict
  ─────────────────────────────────────────────────────────────────────
  <5%            Natural photosynthesis (plants/algae) Already achieved ✓
  5–10%          Current artificial PS (lab)            Already achieved ✓
  10–15%         Single-absorber STH ceiling            Approaching
  15–20%         Dual-junction CO₂ reduction / PV+electrolysis  Achievable in 2–3 years
  20–25%         Dual-junction STH / triple CO₂ reduction  5–10 year goal
  25–32%         Triple-junction STH ceiling            SCVC hard wall
  >32%           STH exceeding SCVC/SQ                  **Prohibited ✗**

【SCVC Scoring of Key Technology Routes】

  Route                          Ceiling    Complexity    SCVC Bottleneck
  ─────────────────────────────────────────────────────────────────────
  PV + alkaline electrolysis     24%        Low           Electrolysis efficiency
  PV + PEM electrolysis          25%        Low           Iridium scarcity (E5)
  Integrated photoelectrode (1-j) 12%       High          V insufficient
  Integrated photoelectrode (2-j) 28%       Very high     Current matching + corrosion
  Powder photocatalyst (1-step)  10%        Very low      H₂/O₂ back-reaction
  Photoelectrochemical + CO₂ reduction 20%  Extremely high CO₂ selectivity low

  ▸ Decoupled PV + electrolysis is currently optimal (demonstrated ~20%, near ceiling)
  ▸ Integrated is theoretically more efficient but engineering complexity explodes
  ▸ Powder photocatalysis is the "holy grail" (simplest) but efficiency ceiling is only ~10%

【"30% Efficient Artificial Photosynthesis" — SCVC Verdict】

  STH = 30% → requires triple-junction tandem + perfect overpotential → physics allows but engineering extreme
  STH = 20% → dual-junction tandem suffices → achievable target
  ▸ Already progressed from 1% to 5–10% — using ~25–50% of the SCVC quota
  ▸ "Reaching 20% efficiency within 15 years" — SCVC says this is a reasonable engineering goal

====================================================================
* STH ceiling: single-junction ~12%, dual-junction ~28%, triple-junction ~32% → set by spectral matching + synthesis tax.
* The "synthesis tax" (OER overpotential 0.37 V + membrane resistance 0.15 V) makes STH ~30% lower than the PV ceiling.
* Natural photosynthesis (~1–2%) is only 3× from the SCVC wall (~5–6%); artificial (~5–10%) is still 3× from its wall (~20–30%).
* CO₂ → fuel is 30–50% lower than H₂ → the physical cost of liquid solar fuels is locked behind SCVC's overpotential wall.
====================================================================
