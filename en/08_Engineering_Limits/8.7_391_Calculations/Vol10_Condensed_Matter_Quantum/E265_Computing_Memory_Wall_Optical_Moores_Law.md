# Computing Trilogy: Memory Wall · Optical Computing · End of Moore's Law → SCVC Physical Floor

**Status**: 🟡→🟢 75%

---

# 1. Memory Wall: DRAM/SRAM Physical Latency Floor

## 1.1 Latency = RC + Speed of Light

\[
\tau = \tau_{RC} + \tau_{\text{light}}
\]

### RC Delay
RC = (ρL/A)(ε₀A/d) = ρε₀L/d.
- ρ(Cu) = 1.68×10⁻⁸ Ω·m. SCVC: ρ ∝ 1/τ_eph → phonon scattering rate ∝ T/θ_D → θ_D ∝ α.
- ε₀ = 1/(μ₀c²) = 8.854×10⁻¹². c input, μ₀ defined → ε₀ related to α via ε₀ = e²/(αħc).
- d_min ≈ 0.5 nm (SiO₂ monolayer breakdown).
- L = 1 μm (on-chip) → τ_RC ≈ 1.68×10⁻⁸ × 8.85×10⁻¹² × 10⁻⁶ / 5×10⁻¹⁰ ≈ **3×10⁻¹⁶ s = 0.3 fs**.

→ RC is not the bottleneck. ✅

### Speed-of-Light Delay
τ_light = L/v_signal ≈ L/(c/√ε_r). SiO₂ (ε_r ≈ 3.9) → v ≈ c/2.

| Distance | Delay | Location |
|----------|-------|----------|
| 1 mm (on-chip) | 7 ps | — |
| 1 cm (chip edge) | 70 ps | 🔴 Already impacts CPU cycle |
| 20 cm (motherboard) | 1.4 ns | 🔴 Essence of memory wall |
| 1 m (rack) | 7 ns | 🔴 Data-center scale |

**SCVC verdict**: Memory wall is fundamentally the speed-of-light wall — 1 cm = 70 ps already approaches CPU cycle time (0.2 ns). Speed of light c is external input, ε_r ∝ polarizability ∝ α. **The only way around the light-speed wall: bring memory onto the chip (3D stacking + near-memory compute).**

## 1.2 DRAM Basic Latency Breakdown

| Component | Latency | Physical Limit |
|-----------|---------|---------------|
| Wordline RC | ~10 ns | Long wire (L ~ mm) → light-speed dominates |
| Bitline sensing | ~5 ns | ΔV_min ~ 100 mV → C_bl ~ 30 fF → τ ~ C·V/I |
| Column select + output | ~15 ns | Bus light-speed |
| **Total CAS** | **~40-50 ns** | — |

**SCVC physical floor**: Shortest wordline = L_min ≈ cell pitch × 1 column ≈ 50 nm × 1 → RC ≈ 0.01 ps. Sense amplifier → C_bl_min ≈ 1 fF → τ ≈ C·ΔV/I_on ≈ 10⁻¹⁵ × 0.1 / 10⁻⁴ ≈ 1 ps. **DRAM physical floor ~10-100 ps → 500-5000× faster than current ~50 ns.**

Why the huge gap? → Capacity vs. speed tradeoff: larger DRAM array → longer wordline → larger RC. Engineering choice, not physical wall.

## 1.3 SRAM Latency Floor

6T SRAM: cross-coupled inverters. Latency = gate charging time:
τ_read = C_bitline · ΔV / I_read. C ≈ 1 fF/μm × 10 μm = 10 fF. I ≈ 100 μA/μm × 0.1 μm = 10 μA. ΔV ≈ 100 mV.

→ τ ≈ 10×10⁻¹⁵ × 0.1 / 10⁻⁵ = 10⁻¹⁰ s = **0.1 ns**.

Current SRAM ~0.5-2 ns → 5-20× above floor. SCVC floor from: I_read ∝ carrier mobility ∝ 1/scattering rate ∝ 1/(phonon ∝ θ_D ∝ α).

---

# 2. Optical Computing & Neuromorphic: Minimum Energy

## 2.1 Optical Computing: Shot Noise Floor

Minimum photon communication energy from shot noise. BER = 10⁻¹⁵ → required SNR:
P(0|1) = ½erfc(√(SNR/2)) → SNR ≈ (√2·erfc⁻¹(2×10⁻¹⁵))² ≈ 110 → ~21 dB.

For coherent light (Poisson statistics) → need N_γ = SNR ≈ 110 photons/bit.

1550 nm photon → ħω = 0.8 eV. → E_min ≈ 110 × 0.8 ≈ **88 eV ≈ 1.4×10⁻¹⁷ J/bit**.

~5000× larger than Landauer (k_BT ln2 ≈ 3×10⁻²¹ J). → Photon transmission energy far exceeds computation energy. Optical computing's advantage is not per-bit energy — it's zero Joule heating (long distance).

## 2.2 Nonlinear Optical Switch → α

All-optical switch: Kerr effect n = n₀ + n₂I. Switching energy ∝ 1/n₂. n₂ ∝ χ⁽³⁾ ∝ electronic anharmonic response ∝ binding energy⁻³ ∝ (α²Ry)⁻³.

Current microring resonators ~fJ/bit. Theoretical floor (Purcell-enhanced + optimal cavity) → ~aJ/bit. SCVC gives n₂ scaling but exact value needs material DFT.

## 2.3 Neuromorphic: Capacitive Charging Floor

Artificial synapse minimum energy = membrane capacitance charging energy:
E_min = ½CV² ≈ ½ × (1 fF) × (0.1 V)² ≈ **5×10⁻¹⁸ J = 5 aJ**.

C_min ∝ ε₀(A_min/d) → A_min ≈ (10 nm)² → C ≈ 10⁻¹⁸ F = 1 aF → E ≈ ½×10⁻¹⁸×0.01 ≈ 5×10⁻²¹ J = 0.005 aJ.

Current memristors ~1-10 pJ → 10⁵-10⁶× above floor. Enormous headroom.

**SCVC**: C ∝ ε₀ ∝ 1/α. V_min ∝ thermal noise √(k_BT/C) → ∝ √(1/α). → E_min α-dependence ≈ α^(−3/2).

## 2.4 Brain vs. GPU Efficiency

| | Brain | GPU (H100) | Reason |
|---|---|---|---|
| Power | 20 W | 700 W | — |
| Equivalent ops/s | ~10¹⁶ | ~2×10¹⁵ (FP8) | — |
| J/op | ~2×10⁻¹⁸ | ~3.5×10⁻¹³ | ×175 |
| Advantage source: | | | |
| Asynchronous | ✅ | ❌ | Continuous clock waste |
| Sparse | ~1% active | ~100% | 100× |
| Analog | Continuous | 8-bit discrete | ~10× |

**SCVC**: 175× difference = 100×(sparse) × ~10×(analog) × compensation factor. Where is the ceiling? Asynchronous + sparse + analog → approaches Landauer or capacitive floor → still 10³-10⁴× above brain.

---

# 3. Transistor Density: End of Moore's Law

## 3.1 Tunneling Limit

Gate L_g → source-drain direct tunneling. Transmission:
\[
T \approx \exp\left(-\frac{2L\sqrt{2m^*E_g}}{\hbar}\right)
\]

Si: m* ≈ 0.26 m_e, E_g ≈ 1.12 eV.

T = 10⁻⁶ (per electron → 100 nA/μm leakage → unacceptable):
→ L_min = (ħ/2√(2m*E_g)) × ln(1/10⁻⁶) ≈ (1.05×10⁻³⁴/(2√(2×0.26×9.1×10⁻³¹×1.12×1.6×10⁻¹⁹))) × 13.8 ≈ **2.5 nm**.

TSMC 3nm → already hit. 2nm → in development. Physical limit ~**1-2 nm**.

## 3.2 SCVC Trace

E_g ← covalent bond energy ← orbital level gap ← Z_eff²·Ry ← α². m* ← band curvature ← bond stiffness ← bond energy ← α.
→ L_min ∝ 1/√(m*E_g) ∝ 1/√(α×α²) = **α^(−3/2)**.

If α were 1% larger → L_min ~1.5% smaller → ~3% more transistors.

## 3.3 Density Ceiling

ρ_max ≈ 1/(4L_min)². L_min = 2 nm → 4 nm pitch → ρ ≈ **6×10¹⁰/cm²**.
Current (TSMC 3nm) ~2×10⁸ → still ~300×. But heat dissipation 🟡 is the tighter wall.

## 3.4 Moore's Law SCVC Verdict

| Wall | Arrival Time | Type |
|------|-------------|------|
| Tunneling (1-2 nm) | ~2028-2032 | 🟢 Physical hard wall |
| Heat (Dennard scaling failure) | ~2005 already | 🟡 Power wall |
| Speed of light (interconnect) | ~2015 already | 🟢 Light-speed wall |

Moore's Law died from three walls converging simultaneously. SCVC provides α-trace for each wall.

---

# 4. Three-in-One Quick Reference

| Ceiling | Value | α Role | Distance to Wall |
|---------|-------|--------|-----------------|
| Memory light-speed latency | 70 ps/cm | ε_r ∝ polarizability ∝ α | Already hit |
| DRAM physical floor | ~10-100 ps | ρ, ε₀ → α | 500-5000× |
| Photon communication E_min | ~88 eV/bit | Shot noise ∝ ħω | Physical wall |
| Neuromorphic E_min | ~5 aJ | C ∝ ε₀ ∝ 1/α | 10⁵-10⁶× |
| Transistor L_min | ~1-2 nm | ∝ α^(−3/2) | ~1.5× |
| Density ρ_max | ~6×10¹⁰/cm² | ← L_min | ~300× |

---

*SCVC: Memory wall = light-speed wall (unbreakable). Optical computing's advantage is zero Joule heating over long distances. Neuromorphic computing has 10⁵-10⁶× headroom to the physical floor. Transistors can squeeze ~1.5× more before hitting the tunneling wall. Moore's Law died from three-wall convergence — each wall bears α's signature.*