# SCVC Engineering Limits: Carbon Capture — Energy Lower Bound for Direct Air Capture (DAC)

**Based on**: `_SCVC_Engineering_Constants_Quick_Reference.md` (all π-polynomial derivations, zero free parameters)
**Calculation Date**: 2026-07-23

---

## §1. Thermodynamic Minimum Work

### 1.1 The Nature of De-Mixing

Same logic as E10 (Seawater Desalination): carbon capture is **de-mixing** — enriching CO₂ from dilute air into a pure stream. The minimum work is determined by $k_B T$ and the CO₂ partial pressure:

$$W_\text{min} = RT \ln\frac{1}{x_\text{CO₂}} \quad\text{(dilute-solution limit, per mol CO₂)}$$

### 1.2 SCVC Calculation

| Parameter | Value | SCVC Origin |
|------|-----|----------|
| $k_B T$ (298 K) | 0.0257 eV | Fundamental constant |
| Atmospheric CO₂ concentration | **420 ppm** = $4.2 \times 10^{-4}$ | Measured (2024) |
| CO₂ partial pressure | **~42 Pa** | $x_\text{CO₂} \cdot P_\text{atm}$ |

$$W_\text{min}^\text{DAC} = 8.314 \times 298 \times \ln\!\left(\frac{1}{4.2\times10^{-4}}\right) = 19.3\ \text{kJ/mol} = 0.20\ \text{eV/molecule}$$

$$W_\text{min}^\text{DAC} = \boxed{122\ \text{kWh/ton CO₂}}$$

### 1.3 Minimum Work at Various CO₂ Concentrations

| Scenario | CO₂ Concentration | $W_\text{min}$ (kWh/ton) | Relative to DAC |
|------|---------|------------------------|---------|
| **Atmosphere (DAC)** | **420 ppm** | **122** | 1× |
| Indoor air | 1,000 ppm | 108 | 0.88× |
| Natural gas flue gas | 5% | 47 | 0.38× |
| Coal flue gas | 10–13% | **32–36** | **0.26–0.30×** |
| Cement kiln flue gas | 20–30% | 20–24 | 0.17–0.20× |
| Pure CO₂ stream | 100% | 0 | — |

> **SCVC core insight**: DAC requires ~3.4× more minimum work than point-source capture. This ratio is locked by the **concentration ratio (10%/420 ppm ≈ 240×)** — it is physics, not an engineering choice.

### 1.4 Energy Context

- 122 kWh/ton CO₂ ≈ 440 MJ/ton CO₂ ≈ 0.44 GJ/ton
- Burning 1 ton of coal releases ~2.5 tons CO₂ and ~8,000 kWh of thermal energy
- Capturing those 2.5 tons CO₂ at minimum energy: $2.5 \times 122 = 305$ kWh → only **~4%** of the combustion energy
- **Carbon capture is not energetically impossible — it merely requires 3.4× more work than point-source capture**

---

## §2. Additional Energy Consumption of Absorption/Adsorption Methods

### 2.1 Amine Process (MEA): The Cost of Thermal Regeneration

The most mature current DAC/point-source capture technology. Chemical absorption + thermal regeneration:

$$\text{CO₂} + 2\text{RNH₂} \rightleftharpoons \text{RNHCOO}^- + \text{RNH₃}^+ \quad (\Delta H \approx 80\ \text{kJ/mol})$$

| Energy Term | Value (kJ/mol CO₂) | Fraction |
|--------|----------------|------|
| Reaction enthalpy (CO₂–amine bond breaking) | 80 | 17% |
| Solvent sensible heat (40→120°C)ᵃ | 250–350 | 55% |
| Water vaporization (stripping steam) | 70–120 | 28% |
| **Total (thermal)** | **400–550** | 100% |
| Equivalent work (Carnot 24%) | **~100–130 kWh/ton** | — |

> ᵃ Net sensible heat after heat recovery. Modern plants can recover ~50% of sensible heat via lean/rich solvent heat exchange.

| Technology Level | Heat Consumption (GJ/ton) | Equivalent Work (kWh/ton) | vs $W_\text{min}$ |
|----------|-------------|-----------------|-------------------|
| Current MEA | 3.5–4.0 | **220–270** | 1.8–2.2× |
| Advanced amine (target) | 2.0–2.5 | **120–170** | 1.0–1.4× |
| **SCVC floor** | **0.44** | **122** | **1.0×** |

**Remaining headroom**: Current best plants are only ~1.8× from the SCVC floor. Sensible heat (not reaction enthalpy) is the largest energy term → **R&D focus is not "stronger binding" but "lower-heat-capacity solvents."**

### 2.2 Solid Sorbents (TSA/VSA)

Metal-organic frameworks (MOFs), zeolites, etc. CO₂ binding energy ~0.3–0.5 eV (physisorption):

| Parameter | MOF/ZIF | Amine-Functionalized Solid |
|------|---------|------------|
| CO₂ binding energy | 0.3–0.5 eV | 0.6–1.0 eV |
| Sorbent heat capacity | ~700–900 J/kg/K | ~1000–1500 |
| CO₂ working capacity | 1–3 mol/kg | 0.5–1.5 |
| Regeneration temperature | 60–100°C | 80–120°C |
| Equivalent work | **~200–500 kWh/ton** | **~150–400 kWh/ton** |

> Core advantage of solid sorbents: no water vaporization heat loss. Disadvantage: the sorbent's own sensible heat must still be overcome, and thermal conductivity is low (cycle time ~minutes).

---

## §3. Membrane Separation

### 3.1 SCVC Constraints on Molecular Size

| Molecule | Kinetic Diameter (Å) | Characteristics |
|------|---------------|------|
| CO₂ | **3.30** | Linear, quadrupole moment → high solubility in polar polymers |
| O₂ | 3.46 | Paramagnetic |
| N₂ | **3.64** | Primary obstacle |
| H₂O | 2.65 | Typically permeates preferentially (competition) |

The CO₂/N₂ size difference is only 10% → **pure size-sieving selectivity is insufficient**. Membrane separation must rely on **solubility selectivity** (CO₂ quadrupole moment interacting with polar polymer groups).

### 3.2 Robeson Upper Bound

CO₂/N₂ separation exhibits a permeability-selectivity trade-off:
- Typical polymers: $\alpha(\text{CO₂/N₂}) = 10$–$50$, $P_\text{CO₂} = 10$–$100$ Barrer
- Robeson upper bound: $\alpha_\text{max} \approx 30$–$60$

From 420 ppm → 90% purity requires ~2,140× concentration. A single-stage membrane with $\alpha = 30$ can only concentrate ~30× → requires **~3–4 stage cascade**.

### 3.3 Membrane Energy Consumption

| Energy Term | Value (kWh/ton) | Remarks |
|--------|-------------|------|
| Fan (air delivery, ~200 Pa) | **~50–80** | Must process ~$1.3 \times 10^6$ m³/ton CO₂ |
| Interstage compression (3–4 stages) | ~200–400 | Recompression per stage |
| Vacuum pump (permeate side) | ~50–100 | Maintaining driving force |
| **Total** | **~300–600** | |

> **SCVC fan-energy hard constraint**: $W_\text{fan} \propto \Delta P \times V_\text{air}$. Since $V_\text{air} \propto 1/x_\text{CO₂}$, DAC membrane processes inevitably face an enormous air-handling energy demand — this is **another form of the concentration-ratio cost**.

---

## §4. Electrochemical Methods — pH-Swing and Redox Capture

### 4.1 pH-Swing Electrodialysis

Uses electrochemical pH modulation to shift the CO₂/HCO₃⁻ equilibrium:

$$\text{CO₂} + \text{H₂O} \rightleftharpoons \text{H₂CO₃} \rightleftharpoons \text{HCO₃⁻} + \text{H⁺}$$

| Step | Principle | Energy |
|------|-----------|--------|
| ① Air contact (pH > 10) | CO₂ → CO₃²⁻ | 0 (spontaneous) |
| ② Acidification (pH < 4) | CO₃²⁻ → CO₂↑ | ~0.2–0.3 eV/CO₂ |
| ③ Electrochemical pH recovery | H⁺/OH⁻ generation | ~0.1–0.2 eV (IR drop + overpotential) |

Theoretical total: ~0.3–0.5 eV/CO₂ → **~180–300 kWh/ton** (1.5–2.5× $W_\text{min}$)

This is currently the **technology route closest to the SCVC floor** — theoretically needing only 1.5× $W_\text{min}$.

### 4.2 SCVC Electrochemical Constraints

- **Electrochemical window**: <6–8 V (water stability) → far above any CO₂ capture voltage needed → **window is not the limitation**
- **CO₂ binding energy**: must be $\geq 0.2$ eV to effectively capture 420 ppm → $K_d \leq 4.2\times10^{-4}$ (relative to standard state)
- **Selectivity**: O₂ reduction ($E⁰ \approx 0.8$ V vs RHE) is the main competing reaction → requires carefully designed catalyst/support

---

## §5. Engineering Conclusions

### 5.1 Energy Consumption Ladder

```
                    kWh/ton CO₂ (equivalent electrical work)
                    ────────────────────────
W_min(DAC) = 122   ▓▓▓▓ Absolute thermodynamic floor

W_min(flue gas 10%) = 36 ▓▓ Point-source floor (must be 3.4× lower than DAC)

pH-swing (ideal) ~180  ▓▓▓▓▓▓ Closest to SCVC floor (1.5×)
Advanced amine (target) ~150  ▓▓▓▓▓ (1.2×, but includes Carnot)
Amine (current)  ~250  ▓▓▓▓▓▓▓▓▓ (2.0×)
Membrane (multi-stage)  ~400  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ (3.3×)
Electrochemical (+0.3 V) ~600 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ (5×)
```

### 5.2 Cost Floor

| Electricity Price | Pure Energy Cost (W_min) | Actual (2× W_min) | Actual (4× W_min) |
|------|-------------------|-----------------|-----------------|
| $0.02/kWh | **$2.4/ton** | $4.9/ton | $9.8/ton |
| $0.05/kWh | **$6.1/ton** | $12.2/ton | $24.4/ton |
| $0.10/kWh | **$12.2/ton** | $24.4/ton | $48.8/ton |

> **Physical meaning of the $100/ton target**: $100/(122 kWh/ton × $0.05/kWh) ≈ 16× the energy floor. $100/ton includes capital depreciation (~$30–50), sorbent replacement (~$10–20), O&M (~$20–30) + energy (~$20–40) → **$100/ton is an engineering target, far above the physical floor. The SCVC-allowed minimum cost is ~$2–5/ton (energy only).**

### 5.3 DAC vs. Point Source — An Eternal Gap

| Factor | DAC | Point Source | SCVC Judgment |
|------|-----|------|-----------|
| $W_\text{min}$ | 122 kWh/ton | 36 kWh/ton | **Concentration ratio sets ~3.4× gap** |
| Fan energy | ~50–80 kWh/ton | ~0 (existing pressure head) | Additional DAC penalty |
| Equipment size | Large (~$10^6$ m³ air/ton) | Small (~$10^4$ m³ flue gas/ton) | **~100× scale difference** |

**SCVC's fundamental judgment**: DAC will forever be 3–5× the energy consumption of point-source capture in physical terms. **DAC cannot replace point-source capture** — it is the "last resort" for distributed emissions (transportation, agriculture).

### 5.4 Technology Routes Closest to the SCVC Limit

| Rank | Technology | Gap to $W_\text{min}$ | Key Advantage |
|------|------|-----------------|---------|
| 1 | **pH-swing electrodialysis** | ~1.5× | Direct electricity use, no Carnot, no sensible heat |
| 2 | Advanced amine (heat-integrated) | ~1.2× (equivalent work) | High maturity, but requires heat source |
| 3 | Electrochemical redox | ~2× (ideal) / 5× (actual) | High flexibility |
| 4 | Solid sorbent (MOF) | ~2–4× | No water vaporization loss |
| 5 | Multi-stage membrane | ~3–5× | Simple, but fan energy is a hard constraint |

### 5.5 The Ultimate Answers

| Question | SCVC Answer |
|------|----------|
| **DAC minimum energy** | **122 kWh/ton CO₂** ($k_B T \ln(1/x)$) |
| **Point-source minimum energy** | **36 kWh/ton** (10% CO₂) → forever 1/3.4 of DAC |
| **Is $100/ton physically feasible?** | **Yes** — physical floor ~$2–5/ton (energy only) |
| **Where is the $100/ton gap?** | Energy ~20–40 + capital ~30–50 + O&M ~20–30 |
| **Optimal technology route?** | **pH-swing electrodialysis** (~1.5× $W_\text{min}$, no thermal loss) |
| **Can DAC replace point-source capture?** | **No** — the ~3.4× gap locked by concentration ratio cannot be eliminated |
| **Energy to reduce atmosphere from 420→350 ppm?** | ~400 EJ (~10 years of global energy consumption) — scale-infeasible |

---

## Appendix: Key Formula Derivations

### A.1 Minimum Work of De-Mixing
From ideal-gas mixing free energy:

$$\Delta G_\text{mix} = RT \sum_i x_i \ln x_i$$

For extracting pure CO₂ from the atmosphere ($x_\text{CO₂} = 4.2\times10^{-4}$):

$$W_\text{min} = -\frac{\Delta G_\text{sep}}{n_\text{CO₂}} \approx RT \ln\frac{1}{x_\text{CO₂}} \quad (\text{dilute solution})$$

$$= 8.314 \times 298 \times 7.776 = 19.3\ \text{kJ/mol} = \boxed{122\ \text{kWh/ton}}$$

### A.2 Fan Energy
$$W_\text{fan} = \frac{\Delta P \cdot V_\text{air}}{\eta}$$

Air to be processed per ton of CO₂:
$$n_\text{air} = \frac{1000\ \text{kg}}{0.044\ \text{kg/mol}} \cdot \frac{1}{4.2\times10^{-4}} = 5.4 \times 10^7\ \text{mol}$$
$$V_\text{air} \approx 1.3 \times 10^6\ \text{m}^3$$

### A.3 Carnot Conversion (Heat → Work)
$$W_\text{eq} = Q_\text{thermal} \cdot \left(1 - \frac{T_c}{T_h}\right)$$

Amine regeneration: $T_h \approx 393$ K, $T_c \approx 298$ K → $\eta_\text{Carnot} \approx 0.24$.

### A.4 CO₂ Binding Energy → Electrochemical Voltage
$$V_\text{min} = \frac{\Delta E_\text{bind}}{n e}$$

$\Delta E_\text{bind} = 0.4$ eV, $n = 2$ → $V_\text{min} \approx 0.20$ V.

---

*All physical limits are based on the SCVC Engineering Constants Quick-Reference Table. $k_B T \ln(1/x_\text{CO₂})$ is the absolute lower bound driven by chemical potential difference; any DAC method claiming lower energy consumption is equivalent to claiming a perpetual-motion machine of the second kind.*
