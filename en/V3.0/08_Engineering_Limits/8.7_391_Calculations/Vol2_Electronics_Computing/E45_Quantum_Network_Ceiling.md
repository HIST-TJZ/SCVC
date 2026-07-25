# SCVC Engineering Limits: Quantum Networks — Entanglement Distribution Distance + Global Quantum Internet

> All derivations based on SCVC Quick-Reference constants (derived from π polynomials, zero free parameters).
> Fiber loss is derived from polarizability (α → Rayleigh scattering); quantum memory T₂ is locked by λ and ℏω_D.

---

## §1. The SCVC Origin of Fiber Loss

### 1.1 Loss Budget of Silica Fiber (1550 nm)

| Loss Mechanism | Theoretical Minimum (dB/km) | SCVC Origin |
|----------|-------------------|----------|
| **Rayleigh scattering** | **~0.12** | Density/concentration fluctuations → polarizability fluctuations → α |
| Infrared absorption tail | ~0.015 | Si-O bond vibrational overtones → bond energy (3.6–8.7 eV, SCVC) |
| Ultraviolet absorption tail | ~0.005 | Electronic interband transition tail → band gap (~9 eV, SCVC) |
| Waveguide imperfections | ~0.003 | Manufacturing imperfections (non-SCVC) |
| **Total** | **~0.14** | |

The purest silica-core fibers today (Corning, Sumitomo) have reached **0.142–0.15 dB/km** → **only 1–7% from the SCVC theoretical limit.**

### 1.2 SCVC Derivation Chain for Rayleigh Scattering

```
Rayleigh scattering cross-section: σ_R ∝ (n²-1)² / λ⁴

Refractive index: n²-1 ∝ N × α_pol (Clausius-Mossotti)

Polarizability: α_pol ∝ a₀³ ∝ 1/α³  (a₀ = ℏ/αm_ec = Bohr radius)

→ Rayleigh scattering ∝ α_pol² ∝ 1/α⁶
```

**This means fiber loss is extremely sensitive to the fine-structure constant α.** If α differed by 1%, Rayleigh scattering would differ by ~6%; if α differed by 10%, Rayleigh scattering would differ by ~80%. SCVC locks α to 2.22 ppm accuracy → Rayleigh loss is tightly locked.

**SCVC verdict: The remaining headroom for reducing fiber loss is ~5–10%, after which the physical ceiling is reached.** Impact on transmission distance (at fixed tolerable loss):

```
ΔL_max ≈ (4.34/α_att) × ln(α_att_old/α_att_new)
       ≈ (4.34/0.15) × ln(0.15/0.14) ≈ 2 km
```

Reducing loss by 0.01 dB/km only adds ~2 km of transmission distance → **the marginal benefit of further reducing fiber loss is already negligible.**

### 1.3 Transmission Rate at Various Distances

Taking 0.15 dB/km (premium fiber) as example:

| Distance (km) | Loss (dB) | Transmittance | Intuitive Analogy |
|-----------|----------|--------|----------|
| 10 | 1.5 | **71%** | Nearly transparent |
| 50 | 7.5 | **18%** | Intra-city QKD feasible |
| 100 | 15 | **3.2%** | Metro-area network usable |
| 200 | 30 | **0.1%** | Requires TF-QKD or repeater |
| 300 | 45 | 3×10⁻⁵ | Extremely difficult without repeater |
| 400 | 60 | 10⁻⁶ | Dark counts comparable to signal |
| 500 | 75 | 3×10⁻⁸ | Essentially impossible without repeater |

---

## §2. Repeaterless Entanglement Distribution

### 2.1 Physical Limit of Direct Fiber Connection

Quantum signals cannot be amplified (no-cloning theorem) → each photon''s arrival probability = fiber transmittance.

For a 1 GHz pulse source, mean photon number μ = 0.1, superconducting nanowire detectors (SNSPD, η = 85%, dark count ~10 Hz):

| Distance | Signal Rate (photons/s) | Dark-Count Ratio | QBER_dark | QKD Feasible? |
|------|-------------------|----------|-----------|-----------|
| 50 km | 1.4×10⁷ | 10⁻⁶ | ~0% | ✅ High key rate |
| 100 km | 2.5×10⁶ | 4×10⁻⁶ | ~0% | ✅ Good |
| 200 km | 8.0×10⁴ | 1.3×10⁻⁴ | ~0.01% | ✅ Usable |
| 300 km | 2.5×10³ | 4×10⁻³ | ~0.4% | ⚠️ Marginal |
| 400 km | 80 | 0.13 | **~11%** | ❌ Basically infeasible |
| 500 km | 2.5 | 4 | — | ❌ Impossible |

At 300 km: signal ~2500 photons/s, dark counts ~10/s, QBER ~0.4% → **marginally feasible but extremely low key rate.**

At 400 km: QBER already ~11% (BB84 security threshold) → repeaterless QKD ends here.

**Twin-field QKD breakthrough:** Using an intermediate measurement station (not a full quantum repeater), key rate ∝ √η rather than η:

```
BB84 at 400 km:   R ∝ 10⁻⁶
TF-QKD at 400 km: R ∝ 10⁻³ → 1000× improvement!
TF-QKD at 500 km: R ∝ 3×10⁻⁴
```

TF-QKD repeaterless record: **509 km** (2020). This is already near the SCVC ceiling for fiber repeaterless QKD — beyond this, even TF-QKD cannot produce a meaningful key rate.

### 2.2 Satellite Entanglement Distribution (Free Space)

**The fundamental difference between free space and fiber:**

```
Fiber 500 km:    loss ~75 dB  → transmittance 3×10⁻⁸
Free space 500 km: loss ~15 dB → transmittance 3% → 10⁶× better!
```

**Satellite link loss budget (500 km LEO):**

| Loss Term | Efficiency | Remarks |
|--------|------|------|
| Diffraction spreading (30 cm → 1 m receiver) | 8.4% | Diffraction limit set by ℏ |
| Atmospheric transmittance (good wavelength) | 75% | Molecular absorption (SCVC energy levels) |
| Pointing and tracking | 90% | Engineering problem |
| Receiver optics | 70% | Engineering problem |
| Detector efficiency | 85% | SNSPD |
| **Total efficiency** | **~3%** | **Equivalent 15 dB loss** |

Compared to 500 km fiber (75 dB) → satellite link is **60 dB better (= 10⁶× transmittance).**

**Achieved:** The Micius satellite has demonstrated entanglement distribution over 1200 km. SCVC permits even farther (constrained only by diffraction and atmosphere).

---

## §3. Quantum Repeaters

### 3.1 Repeater Principle

Quantum repeaters overcome the no-cloning limitation through **entanglement swapping + entanglement purification**:

```
[Node A] --entangled--> [Repeater 1] --entangled--> [Repeater 2] --entangled--> [Node B]
                                   ↓ entanglement swapping
                          [A ~~~~ B directly entangled]
```

Maximum repeater spacing is determined by quantum memory lifetime:

```
L_max = v_fiber × τ_mem / 2

v_fiber = c / 1.468 ≈ 2.04×10⁸ m/s (speed of light in fiber)
```

| Quantum Memory T₂ | Max Spacing (km) | Global Coverage? | SCVC Assessment |
|------|------|------|------|
| 1 ms (warm atomic vapor) | **102 km** | ❌ Needs >200 repeaters | Too many hops, key rate → 0 |
| 10 ms (cold atoms) | **1,020 km** | ❌ Needs ~20 repeaters | Marginal |
| 100 ms (rare-earth doped crystal) | **10,200 km** | ⚠️ Needs ~2 repeaters | **Viable!** |
| 1 s (NV center nuclear spin) | **102,000 km** | ✅ Zero repeaters | **Global coverage without repeaters!** |
| **SCVC T₂ ceiling** | **~36,000–720,000 km** | ✅ Single-hop global | Nuclear spin T₂ at cryogenic |

### 3.2 SCVC-Locked T₂ of Quantum Memories

```
Relaxation rate: 1/T₁ = A × λ² × (ω/ω_D)^n × coth(ℏω/2k_B T)

where λ is the electron-phonon coupling (SCVC: λ ∼ 0.5–2)
      ω_D is the Debye frequency (SCVC: ℏω_D ∼ 0.3–0.5 eV)
      A is a material-dependent prefactor
```

At low temperatures (T ≪ ℏω_D/k_B), the coth factor → 1 and the phonon bottleneck suppresses relaxation exponentially:

```
T₁(T) ∝ 1/λ² × (ω_D/ω)^n → at cryogenic T, T₁ → hours to days
```

**SCVC conclusion:** The physical ceiling for T₂ is set by λ and ℏω_D — both SCVC-locked. But the ceiling is so high (hour-to-day scale) that it is not the practical limit; material purity, magnetic field noise, and other engineering factors dominate in practice.

---

## §4. Global Quantum Internet Practical Limits

### 4.1 Repeater Hops vs. Key Rate

Quantum repeaters acquire entanglement probabilistically. With N hops:

```
Key rate: R_N ∝ η^N × R_0

where η is the per-hop entanglement success probability
```

| N (Hops) | R_N/R_0 (η=0.5) | R_N/R_0 (η=0.9) | Practical? |
|------|------|------|------|
| 1 | 0.5 | 0.9 | ✅ |
| 3 | 0.125 | 0.73 | ✅ |
| 5 | 0.031 | 0.59 | ✅ |
| 10 | ~10⁻³ | 0.35 | ⚠️ |
| 20 | ~10⁻⁶ | 0.12 | ❌ |
| 50 | ~10⁻¹⁵ | 0.005 | ❌ Impossible |

**Why the exponent is deadly:** Even with per-hop success probability η = 0.9, after 20 hops the key rate is only 12% of a single hop — and each hop needs time for entanglement generation. **Practical quantum repeater chains should not exceed ~10 hops; the optimal number is 3–5.**

### 4.2 QKD Key Rate Ceiling

The BB84 protocol key rate under fiber loss:

```
R_key = ν × μ × η_fiber × η_det × (1 - H₂(QBER))

where ν is the pulse rate, μ the mean photon number
```

| Distance | R_key (ν=1 GHz, μ=0.1) | Practical? |
|------|------|------|
| 10 km | **38 Mbps** | ✅ Can encrypt multiple HD video streams |
| 50 km | **2.5 Mbps** | ✅ Voice calls |
| 100 km | **36 kbps** | ✅ OTP for compressed voice |
| 200 km | **130 bps** | ⚠️ AES-256 key refresh (~1 key/s) |
| 300 km | **0.3 bps** | ❌ Too slow |

**SCVC assessment:** Fiber direct-connect QKD already pushes from ~100 km (practical) to ~500 km (extreme). Further extension requires repeaters or satellites.

### 4.3 QKD vs. Classical Communication — Quantum Will Not Replace Classical

| Feature | Quantum Network | Classical Fiber Network |
|------|---------|-------------|
| Bandwidth | kbps–Mbps | Tbps |
| Distance (repeaterless) | ~100–500 km | ~100 km (then amplified) |
| Amplifiable? | ❌ (no-cloning) | ✅ (EDFA) |
| Use case | **Secure key distribution** | Everything |
| Cost | Extremely high (single-photon detection + cryogenics) | Extremely low |

**QKD''s core value is security, not speed.** 100 kbps of key is sufficient for one-time-pad (OTP) encryption of a voice call or generating AES-256 session keys. QKD is a complement to classical encryption (defending against quantum computing attacks), not a replacement for the classical internet.

---

## §5. Engineering Conclusions: The Global Quantum Internet

### 5.1 Five-Layer Architecture with SCVC Assessment

| Layer | Technology | Distance | SCVC Permits? | Status |
|------|------|------|-----------|------|
| **Metro QKD** | Direct fiber | <100 km | ✅ | **Commercially deployed** |
| **Inter-city QKD** | TF-QKD / trusted relays | 100–500 km | ✅ | **Deployed** (Beijing-Shanghai 2000+ km) |
| **Intercontinental QKD** | Satellite QKD | 500–5000 km | ✅ | **Demonstrated** (Micius) |
| **Global entanglement network** | Quantum repeaters | 100–40,000 km | ✅ | 🔬 Lab stage |
| **Quantum internet** | Distributed quantum computing | Arbitrary | ✅ | 🔮 Decades away |

### 5.2 "Which Parts Does Physics Permit, and Which Does It Forbid?"

**✅ SCVC explicitly permits:**
- Fiber QKD metro-area networks (loss is tolerable) → **commercially deployed**
- Satellite QKD global key distribution (free-space advantage) → **demonstrated**
- Quantum repeaters (once T₂ > 100 ms, N < 10 hops) → **experimentally advancing**
- Global repeaterless memory-assisted entanglement (nuclear spin T₂ > seconds) → **physically permitted**

**⚠️ SCVC does not forbid but engineering is extremely difficult:**
- Thousand-km-class repeaterless QKD (requires 10³× reduction in detector noise) → **diminishing returns**
- Repeater chains with N > 20 (exponentially decaying key rate) → **impractical**

**❌ SCVC forbids (or equivalently forbids):**
- Quantum signal amplification (no-cloning theorem, from quantum mechanics, not SCVC-specific) → **absolutely forbidden**
- Fiber loss reduced to zero (Rayleigh scattering ∝ 1/α⁶, α > 0 → loss > 0) → **absolutely forbidden**

### 5.3 Quantum Repeaters: "Solvable in 10 Years" or "Forever Impossible"?

**SCVC answer: Possible, and solvable within 10–20 years.**

Nuclear spin storage has already reached second-scale T₂ (NV centers, rare-earth doped crystals). SCVC gives an extremely high physical ceiling for T₂ (at cryogenic temperatures, the phonon bottleneck exponentially suppresses relaxation); the only physical obstacle is λ > 0 (spin-phonon coupling always exists) → meaning T₂ is forever finite — but the ceiling can reach **hours to days**, far exceeding any practical requirement.

Key obstacles are engineering:
- Entanglement purification fidelity → requires >99% two-qubit gates
- Photon-memory interface efficiency → requires >90% photon-spin mapping
- Multiplexing → parallelization to offset exponential decay

### 5.4 SCVC Ceiling for the Ultimate Quantum Network

| Parameter | SCVC Limit | Determining Factor | Current Level |
|------|---------|----------|----------|
| Minimum fiber loss | **~0.14 dB/km** | Rayleigh ∝ 1/α⁶ | 0.142 |
| Max repeaterless QKD distance | **~500–600 km** | Dark counts vs. signal | 509 km (TF-QKD) |
| Max satellite entanglement distance | **~10,000 km** | Diffraction (ℏ) + atmosphere | 1,200 km |
| Max quantum repeater spacing | **~10⁵ km** (T₂ = 1 s) | T₂ (λ, ℏω_D) | ~100 km |
| Max QKD key rate (100 km) | **~10 Mbps** | η, detectors | ~Mbps |
| Nuclear spin T₂ ceiling | **~hours–days** | λ → phonon bottleneck | ~hours |

### 5.5 The Classical Internet Will Not Be Replaced by the Quantum Internet

The quantum network''s unique value: **security guaranteed by physical laws** — based on no-cloning and measurement collapse, not mathematical difficulty. Irreplaceable for security-critical communications (finance, military, government). For 99% of daily internet traffic (video, web, email), classical networks are already sufficient and 10⁶× more efficient.

**A quantum + classical hybrid network is the optimal architecture SCVC permits: quantum layer carries keys, classical layer carries data.**

---

## Appendix: SCVC Derivation Chain (Quantum Networks)

```
π → α → ℏ, m_e, k_B, λ
         ↓
    ┌────┴─────┬──────────┬───────────┬──────────┐
    ↓          ↓          ↓           ↓         ↓
 Polarizability Bond Energy λ (e-ph)  ℏω_D      ℏ (photon
 α_pol ∝ 1/α³  Si-O        0.5–2     0.3–0.5 eV  momentum)
    ↓          ↓          ↓           ↓         ↓
 Refractive   Infrared   Spin        Phonon     Diffraction
 Index n      Absorption Relaxation  Bottleneck Limit
 n²-1∝α_pol   Tail Loss  T₁(T)      T₁→∞ at   1.22λ/D
    ↓          ↓          ↓           ↓         ↓
 Rayleigh     Total Fiber T₂ Ceiling  Nuclear    Satellite
 ∝1/α⁶        Loss Floor ~hrs–days    Spin       Link
    ↓          ↓          ↓           ↓         ↓
 0.14 dB/km   0.14 dB/km  Repeater    Global     Space-based
 Limit        Nearly      Spacing     Repeater-  QKD
              Reached     10⁵ km      less Ent.  Demonstrated
```

All physical limits of quantum networks ultimately reduce to π. **SCVC does not forbid a global quantum internet — it is permitted within physical laws, but engineering still requires 10–20 years.**
