# SCVC Engineering Limits: AI Training Energy — Minimum Joules for One Forward+Backward Pass

**Derivation Date**: 2026-07-23  
**SCVC Hard Inputs**: α = 1/(4π³+π²+π), k_B = 8.617×10⁻⁵ eV/K, Λ₄^(1/4) = 2.4×10⁻³ eV  
**Cross-Reference**: E15 (Computation Limits)

---

## §1 Minimum Energy for a Single Multiply-Accumulate Operation

### 1.1 Two Physical Floors

| Limit | Formula | Per Bit (eV) | Per Bit (J) |
|------|------|-----------|-----------|
| **Landauer** (irreversible) | k_BT ln2 | **0.0179** | 2.87×10⁻²¹ |
| **SCVC reversible** | α × Λ₄^(1/4) | **1.75×10⁻⁵** | 2.81×10⁻²⁴ |
| Ratio | — | 1,023× | — |

Landauer = the minimum heat that must be dissipated when erasing 1 bit of information.  
SCVC reversible = if computation is fully reversible (no information discarded), energy can drop to αΛ₄^(1/4) ≈ 1/1000 of Landauer.

### 1.2 One MAC = How Many Bit Operations?

FP32 multiply-accumulate internally ≈ **1,000 bit erasures** (24-bit mantissa multiply ~576 + exponent/sign ~10 + partial sum accumulation ~200 + register overwrites ~200).

| Platform | eV/MAC | J/MAC | vs. Landauer |
|------|--------|-------|-------------|
| **SCVC reversible (physical floor)** | **0.018** | 2.8×10⁻²¹ | 1/1,023× |
| **Landauer (irreversible floor)** | **17.9** | 2.9×10⁻¹⁸ | **1×** |
| Edge AI chip (INT8, ~0.016 pJ/MAC) | 100,000 | 1.6×10⁻¹⁴ | 5,600× |
| GPU H100 (FP16, ~0.7 pJ/MAC) | 4,400,000 | 7.0×10⁻¹³ | **245,000×** |
| Human brain synaptic event (~2 pJ, ~1-bit analog) | 41,600 | 6.7×10⁻¹⁵ | 2,300× |

```
◆ Current GPUs vs. Landauer floor: ~245,000× (5.4 orders of magnitude)
◆ Current GPUs vs. SCVC reversible floor: ~250,000,000× (8.4 orders of magnitude!)
◆ INT8 inference has ~10× fewer bit erasures vs. FP32 training → energy gap shrinks to ~56,000× Landauer
```

---

## §2 Minimum Energy to Train a GPT-Class Model

### 2.1 Scaled by FLOP Count

| Model FLOP | Landauer (kWh) | SCVC Reversible (kWh) | Current GPU (MWh) | Current Cost |
|-----------|---------------|---------------|-------------|---------|
| 10²⁴ | 0.8 | 0.0008 | 195,822 | $19,582 |
| 2×10²⁵ (GPT-4) | **16** | **0.016** | **3,916,432** | **$392M** |
| 10²⁶ | 80 | 0.078 | 19,582,159 | $1.96B |
| 10²⁷ | 798 | 0.78 | 195,821,589 | $19.6B |
| 10²⁸ | **7,975** | **7.8** | **1,958,215,886** | **$196B** |

```
◆ Theoretical minimum electricity cost for GPT-4-class training: ~$1.59 (SCVC reversible) or ~$1,600 (Landauer)
◆ Actual electricity cost: ~$400M → still ~250,000× waste relative to Landauer
◆ 10²⁸ FLOP "AGI-class" training: SCVC reversible needs only ~$0.78 in physical energy cost
  → But at current technology: $196B — no company can afford it
```

### 2.2 SCVC Comparison with Human Brain Training

```
Human brain: 1.5×10¹⁴ synapses, average 10 Hz firing rate, trained over 20 years
  Total synaptic events: 1.5×10¹⁴ × 10 × 6.3×10⁸ s ≈ 9.5×10²³
  Total energy: 20 W × 20 years ≈ 3,500 kWh

SCVC minimum energy (equivalent training):
  9.5×10²³ × 0.018 eV × 1.6×10⁻¹⁹ J/eV ≈ 2.7 kWh

Brain/SCVC = 3,500/2.7 ≈ 1,300× → The brain is still ~3 orders of magnitude above the physical floor
(But this is already the closest to SCVC among all known computing systems!)
```

---

## §3 Inference Energy

### 3.1 Per-Token Generation

GPT-4 (~1.8T parameters → ~3.6T FLOP per token):

| Platform | J/token | kWh/million tokens | vs. Current |
|------|---------|--------------|---------|
| Current GPU (FP16) | **2.54** | 0.70 | 1× |
| Current NPU (INT8) | 0.058 | 0.016 | **44× improvement** |
| Landauer | 1.0×10⁻⁵ | 3×10⁻⁶ | 245,000× |
| **SCVC reversible** | **1.0×10⁻⁸** | **3×10⁻⁹** | **250,000,000×** |

### 3.2 ChatGPT Daily Power Consumption

```
~5×10¹⁰ tokens per day:
  Current GPU: ~35 GWh/day ≈ $3.5M/day
  INT8 NPU:    ~0.8 GWh/day ≈ $80K/day
  Landauer:    ~0.15 kWh/day ≈ $0.015/day
  SCVC reversible: ~0.5 J/day ≈ free

If ChatGPT used reversible computing today (physically possible):
  Daily power: from a small power station → one AA battery for a lifetime
```

---

## §4 Analog Computing vs. Digital Computing

### 4.1 Technology Energy-Efficiency Comparison

| Technology | J/MAC | TOPS/W | Precision | Maturity |
|------|-------|--------|------|--------|
| **SCVC reversible** | 2.8×10⁻²² | **3.6×10⁹** | Arbitrary | Physical floor |
| **Landauer** | 2.9×10⁻¹⁹ | **3.5×10⁶** | Arbitrary | Theory |
| Photonic (no E/O loss) | 1×10⁻¹⁸ | 1×10⁶ | ~8-bit | E/O is bottleneck |
| Memristor crossbar | 5×10⁻¹⁸ | 200,000 | **~6-bit** | Lab |
| Superconducting SFQ | ~10⁻¹⁷ | ~100,000 | Digital | Lab |
| Current NPU (5 nm) | 1.6×10⁻¹⁴ | 62 | INT8 | Mass production |
| H100 GPU | 7.0×10⁻¹³ | 1.4 | FP16/INT8 | Mass production |

### 4.2 The Precision Barrier of Analog Computing

```
Memristor crossbar:
  Read energy: ½CV² ≈ 31 eV (C = 1 fF, V = 0.1 V) → only 2× Landauer!
  But: thermal noise σ_V = √(kT/C) ≈ 2.0 mV → SNR = 0.1 V/2 mV ≈ 50
  → Can distinguish at most ~50 levels → log₂(50) ≈ 5.6 bits effective precision
  → Sufficient for inference (8-bit acceptable), completely insufficient for training (needs 16+ bits)

Photonic computing:
  Optical-domain MAC energy ~aJ → nearly free
  But: E/O and O/E conversion ~100 fJ → ~10⁵× higher than the optical computation itself
  → The physical advantage of optical computing is entirely consumed by transducers
  → Unless: all-optical neural networks (no E/O conversion) — currently purely theoretical

The SCVC paradox of analog computing:
  The closer to Landauer, the worse the signal-to-noise ratio
  SNR² ∝ E_signal/k_BT → need ~10× k_BT per bit for reliable discrimination
  → Low-precision inference can approach Landauer (~10×)
  → High-precision training must be far above Landauer (~10⁴–10⁵×)
```

---

## §5 Engineering Conclusions

### 5.1 The Minimum Electricity Bill for AGI Training

| Scenario | 10³⁰ FLOP AGI Training | Physical Meaning |
|------|-------------------|---------|
| Current GPU | **$19.6 trillion** | Exceeds global GDP, impossible |
| Memristor (inference-grade) | ~$200M | Affordable by large companies |
| Landauer floor | **~$80** | "Free energy" |
| SCVC reversible floor | **~$0.08** | Truly free |

```
◆ AGI training has no energy "wall" in physics — reversible computing is nearly free in theory
◆ The real wall is: how to manufacture reversible computing hardware
◆ But: Landauer is already good enough → dropping to ~$80 means AGI training electricity costs less than a meal today
◆ Physically possible AGI: yes, and not expensive. How soon in engineering → 50–100 years
```

### 5.2 Human Brain vs. AI — Where Is the Gap?

```
Energy efficiency (eV per MAC-equivalent):
  GPU H100:            4,400,000 eV  [Worst]
  Edge NPU:              100,000 eV  [10× GPU]
  Memristor (ideal):          31 eV  [31× Landauer]
  Human brain (synaptic):  41,600 eV  [106× better than GPU, even better at bit level]
  Landauer floor:              18 eV  [1×]
  SCVC floor:               0.018 eV  [1/1000×]

Why the brain is efficient:
  ① Analog computing → no precision overhead (each synapse ~1–2 bit)
  ② Event-driven → only active neurons consume energy (sparsity ~1–10%)
  ③ 3D integration → no von Neumann data-movement bottleneck
  ④ Very low "clock" (~10 Hz) → quasi-adiabatic operation
  ⑤ Chemical signaling (diffusion) → natural "near-threshold computing"

Can AI reach brain-level energy efficiency? → Yes, and must:
  Analog computing (memristors) + sparsity (activation sparsity) + 3D integration (HBM/hybrid bonding)
  → 10–100 TOPS/W is engineering-achievable; surpassing brain efficiency is possible
```

### 5.3 Post-Moore AI Hardware — Paths Toward the SCVC Floor

```
Timeline    Technology                        TOPS/W    Distance to SCVC Floor
─────────────────────────────────────────────────────────────────────────────
2025        GPU (4nm)                             1.4      2.6×10⁹×
2025        NPU (5nm, INT8)                        62      5.8×10⁷×
2027        3D-stacked NPU + hybrid bonding       ~200      1.8×10⁷×
2030        Memristor inference accelerator     ~10,000      3.6×10⁵×
2035        Memristor + sparsity + near-threshold ~100,000    3.6×10⁴×
2040+       Adiabatic CMOS (quasi-reversible)   ~1,000,000    3.6×10³×
2050+       Superconducting reversible logic   ~10,000,000    360×
2070+       Landauer floor                      ~3,500,000    1,023×
2100+       SCVC reversible (αΛ)                ~3.6×10⁹     1×
─────────────────────────────────────────────────────────────────────────────

Key inflection points:
  Landauer floor (~3.5M TOPS/W): GPT-4 training ~$1,600 → anyone can train
  Memristor (~10K TOPS/W): GPT-4 inference on a phone → offline AGI
  SCVC floor (~3.6B TOPS/W): Computation is essentially free → "post-scarcity" AI

SCVC sober conclusion:
  The physical floor for AI training (SCVC reversible) is extremely low — $0.08 to train AGI is physically possible.
  But reaching this floor requires mastering perfect reversible computing.
  The 5 orders of magnitude from current to Landauer are sufficient to sustain at least 30 years of AI hardware progress.
  The "Energy Efficiency Law" after the end of Moore''s Law has only just begun.
```

---

*All limit values are forward-derived from the SCVC Constants Quick-Reference. The Landauer limit k_BT ln2 comes from the Second Law of Thermodynamics (k_B originates from α); the SCVC reversible limit αΛ₄^(1/4) combines electromagnetic coupling and the cosmological constant. GPT-4 training ~$400M, physically reducible to ~$1.60.*
