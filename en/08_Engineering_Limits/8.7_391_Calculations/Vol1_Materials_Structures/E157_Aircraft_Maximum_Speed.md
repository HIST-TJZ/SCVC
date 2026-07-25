====================================================================
SCVC Engineering Limit E157: Aircraft Maximum Speed — Five Physical Ceilings for Atmospheric Flight
====================================================================

**All derivations based on SCVC constants (α→speed of sound 343 m/s, metallic bond energy→melting point, N≡N bond energy 9.8 eV, O=O 5.2 eV).**

--------------------------------------------------------------------
§1. Speed of Sound — The Benchmark for All Ceilings
--------------------------------------------------------------------

  The speed of sound is the yardstick for atmospheric flight. Every speed threshold is "some consequence of approaching/exceeding Mach 1."

  SCVC derivation:
    c = √(γRT/M)

    γ = 1 + 2/f, f = 5 (N₂ and O₂: 3 translational + 2 rotational, room temperature)
    → γ = 1.4

    R = 8.314 J/(mol·K), M = 0.029 kg/mol
    T_sl = 288 K → c = √(1.4×8.314×288/0.029) = √115,600 = **340 m/s**

    SCVC: Air's specific heat ratio γ is determined by molecular degrees of freedom f.
    f = 5 because vibrational modes are "frozen" by quantum mechanics —
    vibrational energy level spacing ↔ chemical bond force constant k~10³ N/m ↔ α.
    If α were different, γ would be different, the speed of sound would be different, and all "Mach number ceilings" would shift.

--------------------------------------------------------------------
§2. First Layer: Propeller Limit — Mach ~0.7
--------------------------------------------------------------------

  【Physics】Blade tips approach Mach 1 → local shock waves → shock-induced separation → efficiency collapse.

  Tip speed: v_tip = ωR
  Flight speed: v_flight
  Resultant speed: v_relative = √(v_flight² + v_tip²)

  When v_relative → c (local speed of sound, varies with temperature/pressure):
    → Supersonic zones appear on blade surfaces
    → Shock waves → boundary layer separation → thrust collapse + drag surge

  Fastest known propeller aircraft: Tu-95 Bear, ~Mach 0.7 (~925 km/h)
  Theoretical limit: Mach ~0.75-0.85 (advanced blade design, swept tips)

  SCVC lock:
    A propeller is a rotating wing. An airfoil's critical Mach number is determined by its thickness ratio.
    Thickness ratio ↓ → critical Mach ↑ → but structural strength ↓ →
    Ultimately locked by material stiffness/density ratio → traced to α (bond energy→elastic modulus).

    **Propeller ceiling: Mach ~0.8-0.85 (absolute)**

--------------------------------------------------------------------
§3. Second Layer: Turbine Blade Melting — Mach ~3.5-4.0
--------------------------------------------------------------------

  【Physics】Intake air heats up during compression. Stagnation temperature T₀ = T × (1 + 0.2M²).
  Compressor and combustor further heat it → turbine inlet temperature exceeds blade material limits.

  【Precise SR-71 calculation】
    Cruise altitude 24 km, T_ambient ≈ 220 K
    Intake stagnation: T_inlet = 220 × (1 + 0.2×3.3²) = 220 × 3.178 ≈ **699 K (426°C)**
    Compressor exit: T_comp ≈ 699 × 2.0 ≈ 1400 K
    Combustor exit: T_comb ≈ 1400 + 800 = 2200 K → but dilution cooling → T_turbine ≈ 1200 K

    SR-71's J58 engine uses titanium alloy. Titanium's service ceiling ~550°C (creep limit).
    Intake is already at 426°C. After compressor → far exceeds titanium limit.
    → J58 uses special high-temperature titanium alloy + compressor bleed air cooling.

  【SCVC Absolute Ceiling (Turbine)】
    Best material: Ceramic Matrix Composites CMC (SiC/SiC)
    Operating temperature ceiling: ~1500-1700 K (oxidation + creep limits)

    Optimized cycle (low compression ratio, ramjet-like transition):
      T_turbine_max ≈ 1700 K
      T_inlet_max ≈ T_turbine / (compression heating × combustion heating)
                   ≈ 1700 / (1.5 × 1.5) ≈ 756 K
      
      T_inlet = 220 × (1 + 0.2M²) → M ≈ 3.5

    With extreme cooling technologies (transpiration cooling, heat pipes):
      T_inlet_max ≈ 1000 K → M ≈ **4.0-4.2**

  ┌──────────────────────────────────────────────────────┐
  │  Turbine ceiling: Mach ~3.5-4.0                       │
  │  SR-71 Mach 3.3 → achieves ~83-94%                   │
  │  Beyond this wall → must abandon turbine → ramjet.   │
  └──────────────────────────────────────────────────────┘

--------------------------------------------------------------------
§4. Third Layer: N₂ Dissociation Wall — Mach ~6-9
--------------------------------------------------------------------

  【Physics】Ramjet/scramjet engines have no turbine. But combustor stagnation temperature grows with M².
  When T₀ > ~2500 K: O₂ begins dissociation (O₂→2O, 5.2 eV)
  When T₀ > ~4000 K: N₂ begins dissociation (N₂→2N, 9.8 eV)

  Dissociation = absorbs enormous energy without producing thrust (atoms cannot fully recombine in the nozzle).
  This is the "dissociation wall" — the heat you add gets swallowed by molecules being torn apart.

  SCVC precise calculation:
    N≡N bond energy = 9.8 eV (strongest chemical bond, derived from α_s)
    Dissociation equilibrium: N₂ ⇌ 2N, K_p(T) ∝ exp(-E_diss/k_B T)

    10% dissociation temperature (T_10%):
      O₂: ~3000-3500 K
      N₂: ~5000-6000 K

    Corresponding Mach numbers:
      T₀ = T × (1 + 0.2M²), at altitude 30 km (T ≈ 227 K):
        O₂ 10% dissociation: T₀ ≈ 3500 K → M ≈ 8.5
        N₂ 10% dissociation: T₀ ≈ 5500 K → M ≈ 10.8

    But: as soon as O₂ dissociates, combustion chemistry is disrupted.
    So the practical wall is **O₂ dissociation**: Mach ~6-9.

  ┌──────────────────────────────────────────────────────┐
  │  Dissociation wall: Mach ~6-9                         │
  │  X-15 Mach 6.7 → at the edge of this wall            │
  │  X-43A Mach 9.6 → scramjet, right at O₂ dissociation │
  │  Beyond → must abandon air-breathing → rocket.       │
  └──────────────────────────────────────────────────────┘

--------------------------------------------------------------------
§5. Fourth Layer: Thermal Structure Limit — Mach ~12-18
--------------------------------------------------------------------

  【Physics】Even without engines (gliding reentry), aerodynamic heating alone can destroy the vehicle.
  Heat flux: q̇ ∝ ρ^0.5 × v³ (at hypersonic speeds)

  Material limits:
    Aluminum alloy: ~150-200°C → Mach 2.0-2.5 max
    Titanium alloy: ~550°C → Mach 3.3 (SR-71)
    Stainless steel: ~800-900°C → Mach ~5-6
    C/C composite (no cooling): ~1600-2000°C → Mach ~8-10
    C/C + active cooling: ~2500-3000°C → Mach ~12-15
    UHTC (Ultra-High Temperature Ceramics): ~3000-3500°C → Mach ~15-18

  SCVC: Melting point ∝ bond energy ∝ α.
  The highest melting point on Earth (HfC, ~3900°C) is the absolute thermal structure ceiling.

  ┌──────────────────────────────────────────────────────┐
  │  Thermal structure ceiling: Mach ~12-18               │
  │  Hypersonic glide vehicles Mach ~15-20                │
  │  → Rely on UHTC + ablative heat shields               │
  │  X-15 (Inconel X) Mach 6.7 → structure limit ~60%    │
  └──────────────────────────────────────────────────────┘

--------------------------------------------------------------------
§6. Fifth Layer: Plasma Blackout Wall — Mach ~20-25
--------------------------------------------------------------------

  【Physics】When T exceeds ~4000-5000 K, air molecules completely dissociate + ionize → plasma sheath.
  Plasma reflects/absorbs radio waves → communication blackout + GPS loss.
  More critically: plasma radiation heating exceeds convective heating → thermal protection collapses.

  SCVC ionization calculation:
    First ionization energy: O→O⁺ + e⁻ = 13.6 eV, N→N⁺ + e⁻ = 14.5 eV
    But: NO⁺ formation (ionization energy ~9.3 eV) is easier → plasma appears at lower T.

    Significant ionization (~1%): T₀ ≈ 5000-6000 K
    Corresponding M:
      At altitude 50 km, T ≈ 271 K:
        M ≈ √((6000/271 - 1) / 0.2) ≈ **10.3**

      At altitude 70 km, T ≈ 220 K:
        M ≈ √((6000/220 - 1) / 0.2) ≈ **11.5**

    But for reentry vehicles at lower altitude (denser air):
      Plasma becomes optically thick → radiation dominates
      M ≈ **20-25** is the "communication + thermal" dual wall.

  ┌──────────────────────────────────────────────────────┐
  │  Plasma wall: Mach ~20-25                             │
  │  Intercontinental ballistic missile warheads Mach ~20-23 │
  │  → Operate at this limit; blackout ~1-5 minutes      │
  │  Beyond → air is no longer "air" → it's plasma soup. │
  └──────────────────────────────────────────────────────┘

--------------------------------------------------------------------
§7. Five-Layer Comprehensive Ceiling Diagram
--------------------------------------------------------------------

```
Mach
 25 ┤ ═══════════════ Plasma blackout wall (communication loss + radiation)
    │ ████ ICBM warheads 20-23
 20 ┤
    │ ═══════════════ Hypersonic weapon / glide vehicle zone
    │
 15 ┤ ═══════════════ Thermal structure limit (active cooling, CMC+UHTC)
    │
 12 ┤ ═══════════════ Thermal structure limit (no cooling, C/C)
    │
 10 ┤ ████ X-43A 9.6
    │ ═══════════════ N₂ dissociation wall (ramjet/scramjet failure)
  8 ┤
    │ ████ X-15 6.7
  6 ┤ ═══════════════ O₂ dissociation onset
    │
  4 ┤ ═══════════════ Turbine melting limit
    │ ████ SR-71 3.3
  3 ┤
    │ ████ Concorde 2.04
  2 ┤ ═══════════════ Aluminum alloy thermal limit
    │
  1 ┤ ═══════════════ Propeller limit
    │ ████ Airliner cruise 0.85
  0 ┴──────────────────────────────────────────────────
```

  Each wall is a "lock" — the key is what you're willing to give up:
    Propeller→Turbine: give up simplicity
    Turbine→Ramjet: give up static-start capability
    Ramjet→Rocket: give up air-breathing
    Rocket→Glide: give up propulsion, pure kinetic energy

--------------------------------------------------------------------
§8. The Physics-Economics Intersection for Airliners
--------------------------------------------------------------------

  【Why do airliners stop at Mach 0.85?】

  Not because they physically can't fly faster — because economics forbids it.

  Fuel energy: aviation kerosene ~43 MJ/kg
  From SCVC: C-H bond energy ~4.3 eV/bond, C:H ratio ~1:2
  Combustion release: C-C(3.6eV) + C-H(~4.3eV) → C=O(~8eV) + H-O(~5eV)
  → ΔE ≈ product bond energy - reactant bond energy → ~43 MJ/kg

  Cruise power required: P = D × v = (L/(L/D)) × v

  L/D variation with Mach number:
    Mach 0.5: L/D ≈ 18-20
    Mach 0.8: L/D ≈ 18-20 (optimum, transonic drag not yet surging)
    Mach 0.85: L/D ≈ 17-19 (typical airliner cruise)
    Mach 0.95: L/D ≈ 12-15 (wave drag begins to appear)
    Mach 1.2: L/D ≈ 8-10
    Mach 2.0: L/D ≈ 6-8 (Concorde ~7.5)

  Fuel per passenger-km ∝ v / (L/D):
    Mach 0.85: 0.85/18 ≈ 0.047
    Mach 2.0:  2.0/7.5 ≈ 0.267 → **5.7× the fuel of Mach 0.85**

  Concorde fare ~$12,000 (current) vs economy ~$800 → **15×**.
  Not because "the technology isn't there" — it's because of physics.
  The cost of overcoming wave drag is exponential.

  SCVC verdict:
    **Supersonic airliners can never economically compete with subsonic airliners.**
    This is not a technology problem — wave drag comes from Mach cone geometry,
    Mach cone geometry from the speed of sound, speed of sound from γ, γ from α.
    As long as α is constant, supersonic costs 5-10× more fuel than subsonic.

  Boom Supersonic (Overture, target Mach 1.7):
    Claims L/D ≈ 10 → fuel ratio 1.7/10=0.17 vs 0.85/18=0.047 → **3.6×**
    Even if successful, fares will be 2-3× business class. Niche market, not mass transit.

--------------------------------------------------------------------
§9. SCVC Optimal Altitude-Speed Surface
--------------------------------------------------------------------

  High altitude → low air density → low heat flux → permits higher Mach.
  But high altitude → low lift → needs higher angle of attack / larger wing → increased drag.

  Optimal cruise altitude:
    h_opt ≈ 10-13 km (tropopause, lowest temperature ~216K)
    At this altitude: lowest drag + highest engine efficiency

  Thermal limits at different altitudes (M_max):
    ┌──────────┬──────────┬───────────────┐
    │ Alt (km) │ T_amb(K) │ M_max(Ti,550°C)│
    ├──────────┼──────────┼───────────────┤
    │ 0         │ 288      │ 2.7           │
    │ 10        │ 223      │ 3.2           │
    │ 20        │ 217      │ 3.3           │
    │ 30        │ 227      │ 3.2           │
    │ 40        │ 250      │ 3.0           │
    │ 50        │ 271      │ 2.8           │
    └──────────┴──────────┴───────────────┘

  ▸ Tropopause (~12km) gives SR-71 extra thermal margin.
  ▸ Higher → stratospheric temperature inversion → T rises → thermal limit actually drops.

====================================================================
* Five ceilings: Propeller 0.7 / Turbine 3.5-4 / Dissociation 6-9 / Thermal Structure 12-18 / Plasma 20-25.
* SR-71 Mach 3.3 → 83-94% of turbine ceiling. X-15 Mach 6.7 → onset of dissociation wall.
* Hypersonic weapons Mach 20 → edge of plasma wall.
* Airliner economic ceiling Mach 0.85: not a physical wall, but wave drag × fuel = SCVC economic wall.
* Supersonic airliners always 5-10× more fuel than subsonic → SCVC says this is geometric inevitability.
* Every wall traces back to α: speed of sound (γ←α), melting point (bond energy←α), dissociation (N≡N←α_s).
====================================================================
