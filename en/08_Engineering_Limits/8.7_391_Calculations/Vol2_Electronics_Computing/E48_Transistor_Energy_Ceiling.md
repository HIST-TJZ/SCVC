====================================================================
SCVC Engineering Limit E48: Transistor Switching Energy — Gate Capacitance Charge/Discharge Floor, Tighter Than Landauer
====================================================================

**All derivations based on SCVC Constants Quick-Reference (zero free parameters, α = 1/(4π³+π²+π)).**

--------------------------------------------------------------------
§1. Switching Energy Floor — The SCVC Floor of E = ½CV²
--------------------------------------------------------------------

【Landauer Is Not the Physical Floor; CV² Is】

  Landauer limit (kT ln2): 2.9×10⁻²¹ J = 18 meV — quantum lower bound for information erasure.
  But a transistor ≠ bit erasure; a transistor = charging/discharging a physical capacitance:
    E_sw = ½ C_g V_DD²

  C_g and V_DD locked by SCVC:
    C_g = ε₀ε_r × WL / t_ox → ε₀ derived from α; t_ox_min ≈ 3 Å (one atomic layer, SCVC bond length)
    V_DD ≥ SS × log₁₀(I_on/I_off) → SS ≥ 60 mV/dec (Boltzmann)

【SCVC Descent of Gate Capacitance】

  Process Node        t_ox (nm)   WL (nm²)    ε_r    C_g (F)      
  ─────────────────────────────────────────────────────
  7nm FinFET          1.2          7×7        3.9    1.4×10⁻¹⁸
  3nm GAA             0.8          3×3        3.9    3.9×10⁻¹⁹
  Extreme CMOS        0.5          1×1        25     4.4×10⁻¹⁹
  Atomic-scale FET    0.3          0.5×0.5    10     7.4×10⁻²⁰
  SCVC floor (single atom) 0.3     0.3×0.3     5     1.3×10⁻²⁰

  ▸ Shrinking dimensions encounters the C_g paradox: WL↓ → C_g↓, but t_ox can no longer shrink (tunneling)
  ▸ ε_r can be increased (HfO₂ → 25; possibly ferroelectric/superlattice → 100+), but interface state density sets a limit
  ▸ **SCVC practical C_g floor: ~10⁻²⁰–10⁻¹⁹ F**

【SCVC Floor for V_DD】

  SS_thermionic = (kT/q)·ln10 = 60 mV/dec (300K, insurmountable)
  I_on/I_off = 10⁶ → V_min = 60 mV × 6 = 360 mV
  Noise margin ~100 mV → V_DD_min ≈ 450 mV

  TFET (tunneling FET): SS can break 60; SCVC sets limit ~30 mV/dec (e-ph coupling broadening)
    → V_DD_TFET_min ≈ 30×6 + 100 ≈ 280 mV
  
  NCFET (negative capacitance): transient SS < 60 is achievable, but steady-state ≥ 60 (Second Law of Thermodynamics)
    → Practical gain is reducing effective V_DD, not breaking SS

  **SCVC V_DD floor: ~200–300 mV** (below this: thermal noise drowns signal + tunneling leakage)

【Switching Energy Hierarchy】

  Tier                       E_sw (J)         E_sw (eV)    vs. kT
  ──────────────────────────────────────────────────────────
  Current 5nm (0.7V)         2.5×10⁻¹⁷       156          ~6000
  Near-term 2nm (0.5V)       6.3×10⁻¹⁸        39          ~1500
  Extreme CMOS (0.2V)        2.0×10⁻¹⁹        1.2          ~48
  SCVC floor (0.1V)          1.0×10⁻²⁰        0.06         ~2.4
  Landauer (kT ln2)          2.9×10⁻²¹        0.018        ~0.7
  SCVC vacuum (E15)          2.8×10⁻²⁴        1.8×10⁻⁵     ~7×10⁻⁴

  ▸ CMOS switching energy vs. Landauer ~10⁴× → not close; a distant physical ideal
  ▸ SCVC practical floor (~48 kT) is ~70× higher than Landauer (~0.7 kT)
  ▸ This ~70× gap arises from "must use macroscopic voltage to control macroscopic capacitance" — ineliminable
  ▸ **Reversible computing can bypass this wall (see §5)**

--------------------------------------------------------------------
§2. Subthreshold Swing — Can 60 mV/dec Be Broken?
--------------------------------------------------------------------

【Comparison of Three Routes】

  Route          Physical Mechanism        SS Floor (SCVC)   Current Demo     Verdict
  ────────────────────────────────────────────────────────────────
  MOSFET         Thermionic injection      60 mV/dec          60–70           Ceiling reached
  TFET           Band-to-band tunneling    ~30 mV/dec          30–50           Breakable
  NCFET          Ferroelectric voltage amp 60 (steady-state)  Transient <60   Steady-state unbreakable

【SCVC Constraints on TFET】

  Tunneling outperforms thermionic injection → does not obey Boltzmann → SS < 60 is possible ✓

  But how narrow can the tunneling window be?
    Ideal: step-function DOS at conduction-valence band → SS → 0
    Reality: electron-phonon coupling (SCVC λ = 0.5–3) broadens band edges
    ΔE_min (broadening) ≈ λ × kT ≈ 13–77 meV
    SS_TFET_min ≈ ΔE_min/ln10 ≈ 6–33 mV/dec

  ▸ **SCVC TFET SS floor: ~30 mV/dec** (e-ph coupling sets the limit)
  ▸ ~2× improvement over MOSFET, but cannot be eliminated
  ▸ Primary bottleneck: TFET I_on is far lower than MOSFET (tunneling probability ≪ 1)

【NCFET: A V_DD-Reduction Trick, Not a Breakthrough in SS】

  Ferroelectric negative capacitance amplifies gate voltage → equivalent V_DD reduction → total energy reduction
  But: ferroelectric switching itself consumes energy → a trade-off exists
  SCVC: ferroelectric coercive field is determined by the polarization-switching barrier derived from SCVC bond energies
  → NCFET net energy improvement ~20–40%, not revolutionary

--------------------------------------------------------------------
§3. Interconnects — The Quantum Floor of RC Delay
--------------------------------------------------------------------

【SCVC Origin of RC Delay】

  Signal propagation delay in a wire:
    τ_RC = R_wire × C_wire
    R_wire = ρ × L / (W × H) → ρ is set by e-ph scattering (SCVC: λ ∼ 2–3)
    C_wire = ε₀ε_r × L × W / d → ε₀ from α

  Even with the best conductors (Cu, Ag), ρ at room temperature is locked by phonon scattering:
    ρ_Cu ≈ 1.7×10⁻⁸ Ω·m → SCVC floor ~1.0×10⁻⁸ Ω·m (single-crystal, defect-free)

【SCVC Interconnect Scaling】

  Wire Width (nm)   H (nm)   d_to_ground (nm)   τ_RC per 1 μm (ps)
  ────────────────────────────────────────────────────────────
  50                 100      200                 0.22
  20                  40       80                 1.4
  10                  20       40                 8.8
   5                  10       20                70
   2                   4        8                ~1,100

  Comparison with transistor delay (current: ~1 ps):

  Wire Length   τ_RC (10nm-wide)    Assessment
  ──────────────────────────────────────────────────
  10 μm         88 ps               Close to transistor ✓
  100 μm        220 ps              Much slower than transistor ✗
  1 mm          22 ns               Severe bottleneck ✗✗

  ▸ **Global interconnects >100 μm: RC delay overwhelms transistor delay → hard wall on chip speed**
  ▸ This is why chips use multi-layer metal + repeaters → but repeaters also consume energy
  ▸ 3D stacking / Through-Silicon Vias (TSV) shrink longest interconnects from mm → μm → alleviates RC bottleneck
  ▸ Optical interconnects can eliminate RC but introduce E/O conversion energy (~pJ/bit) → only justified for >mm distances

--------------------------------------------------------------------
§4. CMOS vs. Brain Energy Consumption
--------------------------------------------------------------------

【"The Brain Is More Efficient Than CMOS" — A Layered Comparison】

  Layer                         Brain            CMOS (5nm)      Ratio
  ──────────────────────────────────────────────────────
  Per switch/synaptic event    2×10⁻¹⁵ J         1×10⁻¹⁶ J       Brain ×20
  Per MAC operation            2×10⁻¹⁵ J         1×10⁻¹² J       Brain ×500
  MAC per Joule                5×10¹⁴            1×10¹²           Brain ×500
  System power (inference)     20 W (whole brain) ~200 W (GPU)    Comparable

  ▸ **Raw switching: CMOS is 5× more efficient** — but this is not a fair comparison
  ▸ **Equivalent computation (MAC): the brain is 500× more efficient** — this is the correct comparison
  ▸ Brain efficiency comes from: analog + sparse + 3D + event-driven, not superior underlying physics

【SCVC Analysis of Brain Efficiency】

  Five efficiency advantages, each with an SCVC root:
  1. Analog computing → one synapse = one MAC, rather than 10⁴ digital switches
  2. Sparse activity → only 1–10% of neurons active simultaneously → idle portions ≈ zero power (CMOS has leakage)
  3. 3D integration → cortex ~2 mm thick, shortest possible interconnect lengths (SCVC: cortical thickness determined by cellular metabolism)
  4. Subthreshold operation → 100 mV action potential; CMOS requires >200 mV
  5. Event-driven → no clock → no clock-tree power (~30% of chip power)

  ▸ SCVC digital CMOS floor ~10⁻²⁰ J/switch → ~10³× gap to current
  ▸ Neuromorphic chips (analog + sparse + event) already approaching ~10⁻¹⁷ J/MAC → ~100× to brain
  ▸ **Reaching brain efficiency does not require surpassing SCVC, only mimicking the brain''s architecture!**

--------------------------------------------------------------------
§5. Engineering Conclusions
--------------------------------------------------------------------

【The "End of Moore''s Law" for CMOS Energy Consumption】

  Tier                   E_sw (J)         Distance to Landauer    Time Forecast
  ──────────────────────────────────────────────────────────
  Current 5nm            2.5×10⁻¹⁷       ~10⁴×                  Now
  Near-term 2nm          6×10⁻¹⁸        ~2×10³×                2025–2027
  Extreme CMOS (~2035)   2×10⁻¹⁹        ~70×                   2030–2040
  SCVC floor             1×10⁻²⁰        ~3.5×                  Physical wall
  Landauer               2.9×10⁻²¹       1×                     Quantum floor

  ▸ CMOS shrinks ~30% per generation (~2 years) in energy → ~6–8 generations to SCVC floor → hit ~2035–2040
  ▸ After hitting SCVC floor: cannot further reduce E_sw → can only improve energy efficiency through architecture (parallelism, near-threshold, 3D)

【SCVC Verdict on Various "Breakthrough" Technologies】

  Technology        Claim                            SCVC Verdict
  ──────────────────────────────────────────────────────────
  TFET              SS < 60 mV/dec                   Permitted (floor ~30), but I_on low
  NCFET             Ultra-low V_DD                   Permitted (reduces V_DD, not SS)
  Spintronics       Zero standby power               Permitted (non-volatile), switching energy higher
  Optical interconnects Zero RC delay                Permitted, but E/O conversion cost >pJ/bit
  Reversible computing Approach Landauer             Permitted, but requires adiabatic switching → speed penalty
  Quantum computing  Exponential speedup             Only for specific problems, not a universal replacement
  Neuromorphic       Brain-level efficiency          Permitted, analog + sparse → optimal path

【Brain Efficiency Is an Achievable Goal — But Requires an Architectural Revolution】

  SCVC does not forbid silicon chips from reaching brain-level energy efficiency (10⁻¹⁵ J/MAC).
  But what is needed is not better transistors, rather:
    ▸ Analog in-memory computing (eliminate the von Neumann bottleneck)
    ▸ Sparse + event-driven (compute only what needs computing)
    ▸ 3D integration (shrink longest interconnects from mm → μm)
    ▸ Near-threshold / subthreshold operation (V_DD → 100–200 mV)

  ▸ **"The 3rd dimension of Moore''s Law" is not continuing to shrink transistors — it is reinventing the computing architecture**

====================================================================
* The SCVC floor for transistor switching energy is ~10⁻²⁰ J (~2.4 kT) — jointly set by C_min and V_min.
* Landauer (0.7 kT) is the lower bound for information erasure; CMOS switching (>48 kT) is far above it → reversible computing can bridge the gap.
* Interconnect RC delay is the real bottleneck on chip speed → 3D integration is the only physical path.
* CMOS raw switching is more energy-efficient than the brain, but the brain wins 500× at the "per MAC" level → architectural innovation > device innovation.
====================================================================
