# E36: SCVC Engineering Limits — Wireless Power Transfer (Near-Field Coupling Efficiency × Distance Ceiling)

> **Input**: SCVC Engineering Constants Quick-Reference (α → conductor conductivity, polarizability, magnetic response)
> **Method**: SCVC constants + electromagnetic field theory + Friis transmission formula → physical limits of wireless power transfer
> **Core Proposition**: The efficiency-distance-frequency trilemma of wireless power transfer is set by SCVC-locked conductor losses, radiation losses, and the diffraction limit

---

## §1. Inductive (Near-Field) Coupling

### 1.1 Basic Physics of Coupling Efficiency

The efficiency of wireless power transfer between two coils is determined by the coupling coefficient k and quality factor Q:

```
Efficiency: η = k²Q₁Q₂ / (1 + √(1 + k²Q₁Q₂))²

For identical coils (Q₁=Q₂=Q):
```

| Target Efficiency η | Required k²Q² | Meaning |
|-----------|----------|------|
| 50% | ≥ 8 | Basically usable |
| 75% | ≥ 48 | Good |
| 85% | ≥ 151 | Excellent |
| **90%** | **≥ 360** | Commercial standard |
| 95% | ≥ 1,520 | High-end |
| 99% | ≥ 39,600 | Near-perfect |

### 1.2 Coupling Coefficient k and Distance Decay Law

For two coaxial circular loop coils (radius r, separation d), the coupling coefficient at large distances (d ≫ r) satisfies:

```
k ≈ (π/2) × r³/(d³ × [ln(8r/a)-2])
```

**k decays as d⁻³** — this is the fundamental reason near-field coupling distance is limited. Near-field energy is stored in the magnetic field surrounding the coils; magnetic field strength decays as 1/d³ (dipole field), not the 1/d decay of far-field radiation.

### 1.3 SCVC Constraints on Quality Factor Q

```
Q = ωL/R_total

R_total = R_ohmic + R_rad

R_ohmic ∝ √ω  (skin effect: current confined to surface depth δ = √(2/ωμ₀σ))
R_rad   ∝ ω⁴  (small loop antenna radiation resistance: ∝ (r/λ)⁴)

→ Q_ohmic ∝ √ω  (frequency ↑ → Q ↑)
→ Q_rad   ∝ 1/ω³ (frequency ↑ → Q ↓)
```

**SCVC constraint**: Conductor conductivity σ is determined by free-electron density and scattering rate, with the scattering rate set by α (electron-phonon coupling λ_max ~3). Even in the best conductors (Cu, Ag), σ at room temperature is locked by phonon scattering at ~6×10⁷ S/m.

| Frequency | Wavelength | Q_ohmic (Cu) | Q_rad | Q_total | Dominant Loss |
|------|------|-------------|-------|---------|---------|
| 0.1 MHz | 3 km | 672 | ~10¹¹ | **672** | Ohmic |
| 1 MHz | 300 m | 2,130 | ~10⁹ | **2,130** | Ohmic |
| **10 MHz** | **30 m** | **6,730** | **~9×10⁵** | **~6,680** | **Optimal balance** |
| 100 MHz | 3 m | 21,300 | ~900 | **~860** | **Radiation** |

**Optimal frequency**: ~10 MHz (optimal operating point for r ~ 0.3 m coils). Below this frequency, ohmic losses dominate and Q is low. Above this frequency, radiation losses surge.

### 1.4 Maximum Effective Distance

| Configuration | Coil Radius r | Q | d/r (η=90%) | d/r (η=80%) | d_max (η=80%) |
|------|----------|---|------------|------------|-------------|
| Phone Qi charging | 2 cm | 100 | 1.4 | 1.8 | **3.6 cm** |
| Laptop charging pad | 5 cm | 200 | 1.7 | 2.2 | **11 cm** |
| Room-scale resonance | 30 cm | 2,000 | 3.3 | 4.2 | **1.3 m** |
| Hall-scale resonance | 50 cm | 3,000 | 3.8 | 4.8 | **2.4 m** |
| **SCVC limit (cryogenic Cu)** | **50 cm** | **10,000** | **5.6** | **7.2** | **3.6 m** |

**Key conclusion**: d/r_max ≈ 5–7 is the SCVC physical ceiling for near-field coupling. Even with superconducting coils (Q → ∞), the d⁻³ decay law of the coupling coefficient k means efficiency can never be maintained at distances far exceeding the coil dimensions.

---

## §2. Resonant Magnetic Coupling (MR-WPT)

### 2.1 Principle of Resonance Enhancement

When the transmitter and receiver coils are tuned to the same resonant frequency, reactive power oscillates back and forth between the coils, reducing the reactive current the source must supply. This is equivalent to boosting the system''s effective Q.

```
Essence of resonant coupling: Two LC resonant tanks exchange energy via mutual inductance M
→ Energy exchange rate ∝ k·ω₀
→ Loss rate ∝ ω₀/Q
→ Efficiency depends on kQ (not k²Q)
```

In practice, resonant coupling does not alter the k²Q² efficiency formula, but allows operation at lower k values (because resonance makes impedance matching easier).

### 2.2 SCVC Derivation of Optimal Frequency

The optimal frequency is determined by maximizing Q_total. Considering the competition between ohmic and radiation losses:

```
Q_total = (1/Q_ohmic + 1/Q_rad)⁻¹

Q_ohmic ∝ √ω · σ·a/√(μ₀)   (a = wire radius)
Q_rad   ∝ c³/(ω³·r³)        (r = coil radius)

Setting ∂Q/∂ω = 0:
ω_opt ∝ (c³/(r³ · √(σ·a/√μ₀)))^(2/7)
```

For a copper coil with r = 0.3 m, a = 3 mm: ω_opt ≈ 2π × 12 MHz → **f_opt ≈ 12 MHz**.

### 2.3 Range Extension via Multi-Coil Repeaters

Single-hop coupling has a d/r ceiling of ~5–7, but repeater coils (passive repeaters) can be inserted to form a "magnetic waveguide":

```
TX coil → Repeater 1 → Repeater 2 → ... → RX coil
Per-hop distance: d_hop/r ≈ 2–3 (maintaining high efficiency)
N-hop total distance: d_total/r ≈ N × 2–3

3 repeaters: d_total/r ≈ 9 (r = 0.3 m → 2.7 m coverage)
```

KAIST dipole coil array (Korea, 2014): 6 repeater coils covering ~5 m distance, efficiency ~50%. This is the main engineering route for extending resonant coupling range.

---

## §3. Far-Field (Microwave/Laser) Transmission

### 3.1 Friis Transmission Equation

```
P_r/P_t = G_t · G_r · (λ/(4πd))²

where G_t, G_r are antenna gains, G = 4πA_eff/λ²

Substituting: A_eff = G·λ²/(4π)

→ Key scaling law: A_required = √η × d × λ
(for identical TX and RX antennas, efficiency η = 0.5)
```

### 3.2 Microwave vs. Laser — The Fundamental Trade-off

| Parameter | Microwave (5.8 GHz) | Laser (1 μm, ~300 THz) |
|------|----------|----------|
| Wavelength λ | 5.2 cm | 10⁻⁶ m |
| Antenna size for 1 km beam at 100 km | ~5.2 m | ~0.1 mm (!) |
| Antenna size for 1 km beam at GEO (36,000 km) | ~1.9 km | ~3.6 cm |
| Atmospheric attenuation | <3% (clear sky) | 10–90% (weather-dependent) |
| Conversion efficiency | ~70–85% (rectenna) | ~30–50% (photovoltaic) |
| Eye safety | Non-ionizing, thermal | Retinal burn hazard |
| **SCVC recommendation** | **Short range (<10 km)** | **Long range, space-based** |

### 3.3 Space Solar Power — SCVC Reality Check

Beaming 1 GW from GEO (36,000 km) to the ground:

```
Scaling law: A = √η × d × λ

2.45 GHz: A_tx = A_rx ≈ 3.1 km² (diameter 2.0 km)
5.8 GHz:  A_tx = A_rx ≈ 1.3 km² (diameter 1.3 km)
35 GHz:   A_tx = A_rx ≈ 0.22 km² (diameter 530 m)
```

**Practical constraints**:
- Deploying a km²-scale phased array on GEO — tens of thousands of tons, far exceeding current launch capacity
- Ground rectenna can use lightweight mesh — economically feasible
- Power density safety: 100–200 W/m² (~10–20% of sunlight) → 1 GW reception requires 5–10 km²
- **Atmospheric breakdown (ionization) threshold**: ~1 MW/m² (far above practical power densities, but beam center requires attention)

### 3.4 The Hard SCVC Diffraction Limit

Far-field beam divergence is set by diffraction:

```
θ ≈ λ/D    (half-power beamwidth)

Beam diameter at distance d: w ≈ d·λ/D
```

For a 1 km transmit antenna on GEO, 5.8 GHz:
- θ ≈ 0.052/1000 = 5.2×10⁻⁵ rad ≈ 0.003°
- Ground beam diameter ≈ 3.6×10⁷ × 5.2×10⁻⁵ ≈ **1.9 km**

Not much larger than the antenna itself — this is the power of high-gain antennas. But the diffraction limit means **beam spreading is forever present**; energy can never be focused onto a spot smaller than λ/D times distance. This is a geometric constraint of Maxwell''s equations; α and ℏ within SCVC add no new restrictions here.

---

## §4. Engineering Conclusions

### 4.1 Physical Feasibility of "Room-Scale Wireless Power"

```
Coil radius r = 0.5 m, Q = 2000 (6.78 MHz copper coil, achievable):
  d_max(η=80%) ≈ 2.0 m
  → One coil covers a 4 m × 4 m room if placed at center
  → Or use 4 repeater coils (one per wall) → efficiency ~50–60%

Coil radius r = 1.0 m (embedded in ceiling/floor):
  d_max(η=80%) ≈ 4.0 m
  → Single coil covers an entire large room
  → Cost: 1 m diameter coil + 6.78 MHz RF power amplifier

SCVC assessment: Room-scale wireless power is fully physically feasible.
It is not forbidden by physics — it is constrained by cost and EMF safety standards.
```

### 4.2 EMF Safety: The Real Bottleneck

```
ICNIRP 2020 public exposure limits (6.78 MHz near-field):
  Electric field: E < 83 V/m
  SAR: < 2 W/kg (head/torso)

100 W transmit, antenna gain ~1, 2 m distance:
  E ≈ √(30·P·G)/d ≈ √3000/2 ≈ 27 V/m ✅ OK

1 kW transmit, 2 m distance:
  E ≈ √30000/2 ≈ 87 V/m ⚠️ Exceeds limit!

→ Room-scale wireless power ceiling ≈ 300–500 W
  (without triggering safety limits)
→ Sufficient for lights + small electronics
→ Insufficient for high-power devices like air conditioners/induction cooktops
```

### 4.3 In-Flight Drone Charging

```
Ground coil r = 1.0 m, Q = 2000, 6.78 MHz
Drone coil r = 0.1 m (small)

Asymmetric coupling (TX coil much larger than RX coil):
  k ∝ √(r_tx³ × r_rx³)/d³
  → d_max(η=50%) ≈ 8–15 m (depending on precise alignment)
  
Practical limits:
  Landing-pad charging: d = 0 → η > 90% (already commercial)
  Hover charging: d = 1–3 m → η ≈ 50–70% (requires alignment + stable hover)
  In-flight charging: d > 5 m → η < 30% (efficiency too low)
  
→ Drone "in-air charging networks" require dense TX coil arrays (spacing ~10–20 m)
```

### 4.4 Technology Roadmap

```
Current (2026):
  Qi/PMG: d ~5 mm, η ~80%, 5–15 W → Phones/watches
  MR-WPT: d ~0.5 m, η ~80%, 10–100 W → Laptops/kitchen appliances
  DARPA POWER: d ~1 km, η ~10%, kW-class → Military long-range power beaming

Near-term (2030):
  Room-scale MR-WPT: d ~3 m, η ~60%, 100–300 W → Consumer "wireless room"
  Drone charging networks: landing + hover charging → Logistics/inspection drones

Long-term (2040+):
  Microwave power beaming 1 km+: d ~1–10 km, η ~30–50% → High-altitude platforms/disaster relief
  Space solar power: requires km² antennas → Fusion/fission more practical

SCVC ceiling:
  Near-field d/r_max ≈ 5–7 (Q = 10,000 limit)
  Far-field A = √η·d·λ (diffraction law, unbreakable)
  Safety limits on public-exposure power ceiling (~kW-class at m distances)
  
Infinite-range wireless power transfer — triply forbidden by SCVC''s
diffraction + ohmic loss + human safety constraints.
```

---

## Appendix A: SCVC Constants Used in This Document

| Symbol | Value | Purpose |
|------|-----|------|
| α | 1/137.0363 | Electron-phonon coupling → conductor resistivity ceiling |
| ℏc | 197.327 MeV·fm | Skin-depth quantum limit |
| k_B | 8.617×10⁻⁵ eV/K | Johnson noise → minimum detectable signal |
| n_atom | 10²³ cm⁻³ | Conductor free-electron density ceiling |
| e-ph λ_max | 2–3 | Room-temperature resistivity floor ~1.7×10⁻⁸ Ω·m (Cu) |
| k (force constant) | 10³ N/m | Structural vibration → mechanical deformation impact on Q |

## Appendix B: Key Formula Quick Reference

```
Coupling efficiency:        η = k²Q²/(1+√(1+k²Q²))²
Coupling coefficient (far): k ≈ (π/2)·r³/(d³·[ln(8r/a)-2])
Q-factor (ohmic):           Q_ohmic ∝ √ω · σ
Q-factor (radiation):       Q_rad ∝ c³/(ω³r³)
Optimal frequency:          ω_opt ∝ (c³/(r³√σ))^(2/7)
Friis transmission:         P_r/P_t = G_t·G_r·(λ/4πd)²
Antenna area scaling law:   A = √η × d × λ
Beam divergence:            θ ≈ λ/D
Near-field region:          d_near = λ/(2π)
```

---

*All limit values in this document are forward-derived from SCVC constants combined with classical electromagnetic field theory. The triple physical walls of wireless power transfer — near-field d⁻³ decay, far-field diffraction divergence, and conductor ohmic losses — are all set by SCVC-locked material properties and Maxwell''s equations, non-negotiable.*
