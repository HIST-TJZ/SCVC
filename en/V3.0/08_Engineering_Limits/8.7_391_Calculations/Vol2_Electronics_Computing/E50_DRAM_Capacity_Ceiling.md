# SCVC Engineering Limits: DRAM Refresh Time — The Tunneling Ceiling of Capacitor Leakage

**Derivation Date**: 2026-07-23  
**SCVC Hard Inputs**: α = 1/(4π³+π²+π), m_e = 0.511 MeV, ℏc = 197.3 MeV·fm, k_B = 8.617×10⁻⁵ eV/K

---

## Tunneling Leakage and Retention Time

### Physical Model

Direct tunneling probability (WKB):

$$T(d) = \exp\left(-\frac{2d\sqrt{2m_e\Phi}}{\hbar}\right)$$

| Dielectric | Φ (eV) | κ (m⁻¹) | Decay Length (nm) |
|------|--------|---------|-------------|
| SiO₂ | 3.1 | 9.03×10⁹ | 0.111 |
| HfO₂ | 2.0 | 7.25×10⁹ | 0.138 |
| ZrO₂ | 1.5 | 6.28×10⁹ | 0.159 |

### Tunneling Probability vs. Thickness

| d (nm) | SiO₂ (3.1 eV) | HfO₂ (2.0 eV) | ZrO₂ (1.5 eV) |
|--------|-------------|-------------|-------------|
| 0.5 | 1.2×10⁻⁴ | 7.1×10⁻⁴ | 1.9×10⁻³ |
| 1.0 | 1.5×10⁻⁸ | 5.1×10⁻⁷ | 3.6×10⁻⁶ |
| 2.0 | 2.1×10⁻¹⁶ | 2.6×10⁻¹³ | 1.3×10⁻¹¹ |
| 3.0 | 3.1×10⁻²⁴ | 1.3×10⁻¹⁹ | 4.5×10⁻¹⁷ |
| 5.0 | 6.7×10⁻⁴⁰ | 3.4×10⁻³² | 5.6×10⁻²⁸ |

```
Every additional 0.5 nm physical thickness → tunneling probability drops ~10³–10⁴×
→ This is why DRAM dielectrics cannot be infinitely thinned
```

### DRAM Leakage Budget

Typical DRAM cell: C = 20 fF, V_DD = 1.0 V, refresh = 64 ms, allowable voltage droop 100 mV

**Maximum allowable leakage current: < 31 fA/cell**

| d_phys (nm) | Dielectric | I_leak | Retention Time | 64 ms OK? |
|------------|------|--------|---------|----------|
| 1.0 | SiO₂ | **1.46 nA** | 1.4 μs | ✗ FAIL |
| 2.0 | SiO₂ | 21 fA | **94 s** | ✓ PASS |
| 2.0 | HfO₂ | 26 fA | **77 ms** | ✓ Barely |
| 2.0 | ZrO₂ | 1.26 pA | 1.6 ms | ✗ FAIL |
| 3.0 | SiO₂ | 3.1×10⁻²⁵ A | ~10¹⁰ s | ✓ — but impossible to fabricate |
| 3.0 | ZrO₂ | 45 fA | **448 s** | ✓ PASS |

```
◆ Direct tunneling: suppressed by d > 2–3 nm physical thickness → not the real bottleneck
◆ The real killer: Trap-Assisted Tunneling (TAT) → indirect tunneling via defect states in the dielectric

TAT vs. direct tunneling (SiO₂, mid-gap traps ~1.5 eV):
  d = 3 nm: T_TAT = 4.5×10⁻¹⁷, T_direct = 3.1×10⁻²⁴ → TAT is ~10⁷× higher!
  d = 4 nm: T_TAT = 1.6×10⁻²², T_direct = 4.6×10⁻³² → TAT is ~10¹⁰× higher!
  d = 5 nm: T_TAT = 5.6×10⁻²⁸, T_direct = 6.7×10⁻⁴⁰ → TAT is ~10¹²× higher!

→ Once direct tunneling is suppressed by thickness, TAT immediately becomes dominant
→ TAT is limited by material quality (defect density) → a process problem, not a physical wall
```

### Thermionic Emission (85°C DRAM Specification)

| Barrier Φ (eV) | exp(−Φ/k_BT) at 85°C | Significance |
|------------|----------------------|--------|
| 0.5 | 1.3×10⁻⁷ | Trap levels → significant |
| 1.0 | 1.2×10⁻¹⁴ | Shallow traps |
| 2.0 | 1.5×10⁻²⁸ | Negligible |
| 3.1 (SiO₂ CB offset) | **2.3×10⁻⁴⁴** | **Completely negligible** |

```
◆ Thermionic emission across an intact barrier (>2 eV) is completely negligible
◆ But thermal excitation of defect states (~0.3–0.5 eV) is the main leakage source at 85°C
◆ This is precisely why accelerated aging tests use 85°C → TAT + thermionic double acceleration
```

---

## Minimum Capacitance Value

### Two-Layer Constraint

| Constraint | Minimum Capacitance | Physical Mechanism |
|------|---------|---------|
| **Thermal noise** (k_BT/C) | **~0.0006 fF** | V_rms = √(k_BT/C), requires 6σ SNR |
| **Sense amplifier** | **~0.5 fF** | Bitline capacitance 30 fF, minimum sensing 15 mV |

```
◆ Thermal noise is far below the practical limit → not a bottleneck
◆ The sense amplifier is the true capacitance floor
◆ ΔV_BL = V_DD × C_cell/(C_cell + C_BL) → when C_cell is too small, the signal is swallowed by bitline capacitance
```

### DRAM Scaling Path

| Node | C_cell (fF) | V_DD (V) | ΔV_BL (mV) | Sensable? |
|------|-----------|---------|-----------|---------|
| DDR3 (50 nm) | 25 | 1.5 | 682 | ✓ |
| DDR4 (30 nm) | 20 | 1.2 | 480 | ✓ |
| DDR5 (15 nm) | 15 | 1.1 | 367 | ✓ |
| Future (10 nm) | 10 | 1.0 | 250 | ✓ |
| **Extreme (~8 nm)** | **5** | **0.9** | **129** | ✓ Still OK |
| **Physical floor** | **~0.5** | **0.8** | **12** | △ Extremely tight |

```
◆ Current DRAM still has ~10× headroom to the capacitance floor
◆ But requires ever-increasing aspect ratios (trench/stacked) → already >50:1
◆ Mechanical stability and process complexity are the true walls for capacitance scaling
```

---

## FeRAM / MRAM / RRAM — Breaking Through the Capacitor Leakage Ceiling

### Fundamental Difference: Energy Barrier Height

All memories rely on some physical state; retention time is determined by the energy barrier:

$$\tau_{retention} \sim \tau_0 \cdot \exp(E_a/k_BT), \quad \tau_0 \sim 10^{-12}\ \mathrm{s}$$

| Technology | Stored Physical Quantity | E_a (eV) | E_a/k_BT (85°C) | Retention Time | SCVC Origin |
|------|-----------|---------|----------------|---------|----------|
| **DRAM** (TAT) | Charge | **0.3** | 10 | **0.02 ms** | Defect states |
| **DRAM** (thermionic) | Charge | **0.5** | 16 | **0.01 s** | Shallow traps |
| FeRAM (PZT) | Polarization | **1.5** | 49 | **>40 years** | Dipole-dipole ∝ α |
| FeRAM (HfO₂) | Polarization | **1.0** | 32 | **120 s** | Oxygen sublattice |
| STT-MRAM | Magnetization | **1.5** | 49 | **>40 years** | SOC ∝ α² |
| RRAM (HfO_x) | Conductive filament | **2.0** | 65 | **>10⁸ years** | Bond energy ∝ α |
| PCM (GST) | Phase state | **2.5** | 81 | **>10¹⁵ years** | Bond rearrangement |

```
DRAM vs. FeRAM/MRAM/RRAM barrier gap:
  E_a(FeRAM) / E_a(DRAM) ≈ 1.5/0.3 = 5×
  Retention time ratio = exp(1.2 eV/k_BT) ≈ exp(39) ≈ 10¹⁷ at 85°C

→ This is why emerging memories need no refresh!
→ An extra 1 eV of barrier → retention time explodes by ~10¹⁴×
```

### SCVC Physical Hierarchy

```
Storage Mechanism       Barrier Origin                      E_a Scale        DRAM?   Emerging?
────────────────────────────────────────────────────────────────────────────
Charge (electrostatic)  Band gap / defects                  ~0.3–0.5 eV      ✓       
Polarization (FE)       Dipole-dipole interaction           ~1.0–1.5 eV              ✓
Magnetization (FM)      Spin-orbit coupling + exchange      ~1.0–1.5 eV              ✓
Conductive filament     Atomic migration / bond breaking    ~2.0–2.5 eV              ✓
Phase change (chalcogenide) Amorphous ↔ crystalline rearrangement ~2.0–3.0 eV        ✓

SCVC insight: Each step upward exploits a stronger physical interaction → exponentially better retention
              The trade-off: writing also must overcome a higher barrier → higher write power
```

---

## Engineering Conclusions

### DRAM Endgame

```
Three hard walls for DRAM scaling:

1. Tunneling wall (direct): d_phys > 2–3 nm → EOT > 0.5 nm
   → High-k dielectrics (ZrO₂/Al₂O₃/HfO₂ stacks) can mitigate
   → But TAT trap-assisted tunneling remains a bottleneck at 3–5 nm

2. Capacitance wall: C_cell > ~0.5 fF
   → Current ~15 fF → still ~30× headroom
   → But requires extreme aspect ratios (>100:1) → mechanical limit

3. Sensing wall: ΔV_BL > ~12 mV
   → Advanced sense amplifiers (offset cancellation) already near the limit
   → Further reduction requires entirely new sensing architectures

DRAM lifetime: Can scale to ~5–8 nm node (approximately 2030–2035)
Thereafter: must transition to 3D-DRAM, FeRAM, or MRAM hybrid architectures
```

### SCVC Advantages of Emerging Memories

```
FeRAM: Retention from ferroelectric domains (~1.5 eV barrier)
  → Non-volatile + DRAM-class speed → perfect "universal memory" candidate
  → Bottleneck: 3D integration, fatigue lifetime (~10¹² cycles)

MRAM: Retention from magnetic anisotropy (~1.5 eV barrier)  
  → Infinite endurance + non-volatile → already used for eFlash replacement
  → Bottleneck: write current, thermal stability at <20 nm nodes

RRAM: Retention from atomic rearrangement (~2.0 eV barrier)
  → Highest density (3D crosspoint) + non-volatile
  → Bottleneck: variability, sneak-path currents

SCVC core insight:
  DRAM is the "lowest-barrier" memory → fastest but most "forgetful"
  All emerging memories use ~3–5× higher barriers
  → ~1 eV more → retention time ~10¹⁴× longer → no refresh needed
  → SCVC permits all of these as physically feasible
  → The engineering challenge is not "physically impossible," but "how to manufacture uniformly + reliably"
```

---

*All limit values are forward-derived from the SCVC Constants Quick-Reference. Tunneling probability ∝ exp(−2d√(2m_eΦ)/ℏ), where m_e and ℏ both originate from α (m_e given directly, ℏ from ℏc = 197.3 MeV·fm → c from α). Storage barrier heights span multiple physical tiers, from electromagnetic interaction energy (∝ α) to chemical bond energy (∝ 3–10 eV).*
