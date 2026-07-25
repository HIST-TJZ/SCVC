# SCVC Engineering Limit E87: Human Pain Ceiling — Physical Upper Bound on Maximum Perceivable Pain Intensity

**Derivation Date**: 2026-07-23  
**SCVC Hard Inputs**: k_B T = 0.0267 eV (310 K), τ_m ≈ 20 ms, C-fiber v ≈ 1 m/s, ATP 0.55 eV  
**Cross-References**: E28 (Nerve Conduction) + E30 (Metabolism) + E86 (Reaction Latency)

---

## §1 The Molecular Ceiling of Nociceptors

### 1.1 TRPV1 Channel — The Thermal Pain Floor

`
TRPV1 (capsaicin receptor): non-selective cation channel
  Activation threshold: >43°C or H⁺ (pH<6) or capsaicin
  Maximum open probability: P_open → 1 (saturated, >~50°C)
  
  Single-channel conductance: ~100 pS
  Driving voltage: ~−80 mV → +20 mV (when cell depolarizes)
  Single-channel current: ~10 pA
  
TRPV1 channels per neuron: ~10³–10⁴
Maximum inward current: ~10–100 nA/neuron
→ Depolarization rate ~10–100 V/s
→ AP frequency saturation: ~50–100 Hz (C-fiber refractory period ~10–20 ms)

SCVC: TRPV1 opening is temperature-driven — activation energy of protein conformational change
  ΔG‡ ≈ 100–150 k_B T (difference between >43°C and 37°C)
  → Channel gating energy barrier is locked by the k_B T scale
`

### 1.2 C-Fibers — The Pain Signal Ceiling

`
C-fibers (unmyelinated):
  Diameter: ~0.5–1.5 μm
  Conduction velocity: ~0.5–2 m/s (unmyelinated)
  Refractory period: ~10–20 ms
  Maximum firing frequency: ~50–100 Hz

Aδ fibers (thinly myelinated):
  Diameter: ~2–5 μm  
  Conduction velocity: ~5–30 m/s
  Refractory period: ~3–5 ms
  Maximum firing frequency: ~200–300 Hz

C-fiber fraction in peripheral nerves: ~70–80% (predominantly nociceptive)
C-fiber count in a single nerve: ~10³–10⁴
`

### 1.3 Spinal Dorsal Horn — First-Level Integration

`
Each dorsal horn neuron receives:
  → ~100–1000 C-fiber afferents
  → Spatial summation → can amplify ~10–100×

Synapses:
  C-fibers release glutamate + Substance P (SP)
  SP diffusion → NK1 receptor activation → slow EPSP (lasting ~10–30 s)
  → Temporal summation → "wind-up" phenomenon (progressive enhancement with repeated stimuli)

SCVC: Substance P diffusion is constrained (MW ~1300 Da)
  Diffusion coefficient D ≈ 5×10⁻¹¹ m²/s (in spinal interstitium)
  Diffusion range ~10 μm → τ_diff ≈ (10 μm)²/(2D) ≈ 1 s
  → SP action timescale ~1–30 s, locked by aqueous diffusion
`

---

## §2 SCVC Pain Intensity Scale

### 2.1 From Firing Frequency to Pain Intensity

`
Pain intensity ∝ firing frequency of spinal dorsal horn neurons

Dorsal horn neurons:
  Baseline: 0–1 Hz (no pain)
  Mild pain: 5–10 Hz
  Moderate pain: 10–30 Hz
  Severe pain: 30–60 Hz
  Extreme pain: 60–100 Hz
  
Saturation mechanisms:
  C-fiber refractory period ~10–20 ms → maximum ~50–100 Hz
  Synaptic vesicle depletion → transmitter release drops under high-frequency stimulation
  GABA/glycine inhibition → negative feedback
  
Maximum sustained dorsal horn neuron firing: ~100–200 Hz
  → At the spinal level, the pain signal is already ceiling-locked by the refractory period
`

### 2.2 Central Sensitization — Gain Cranked to Maximum

`
Central sensitization = NMDA receptor → Ca²⁺ → PKC → TRPV1 phosphorylation → positive feedback

Amplification factor:
  NMDA receptor activation → Ca²⁺ influx → CaMKII → AMPA receptor phosphorylation
  Each phosphorylated AMPAR → single-channel conductance increased ~50–100%
  Total: synaptic efficiency can be enhanced ~2–5×

But:
  Ca²⁺ pumps (SERCA/PMCA) have a maximum rate → Ca²⁺ accumulation
  → Mitochondrial Ca²⁺ overload → permeability transition pore (mPTP) opening
  → Apoptosis → if sensitization is too strong for too long, neurons die
  
SCVC ceiling: Central sensitization amplification factor ≤ ~5–10×
  → Cannot exceed the maximum capacity of Ca²⁺ pumps
  → Ca²⁺ pump energy comes from ATP → derived from α
`

### 2.3 Descending Inhibition — Physical Ceiling of Pain Relief

`
Endogenous opioid system:
  Endorphins/enkephalins → μ/δ/κ receptors → Gi/o proteins
  → K⁺ channel opening → hyperpolarization → inhibition of transmitter release

Receptor abundance:
  μ receptors per neuron: ~10³–10⁴
  Maximum occupancy: 100% (saturation)
  
Descending pathway:
  PAG (periaqueductal gray) → nucleus raphe magnus → spinal dorsal horn
  Releases 5-HT + norepinephrine → inhibits nociceptive transmission

Maximum inhibition efficiency: ~70–80%
  → Cannot reach 100% (must preserve nociceptive survival function)
  → The remaining 20–30% of the pain signal is "ineliminable"
`

---

## §3 SCVC Pain Ceiling

### 3.1 Absolute Upper Bound

`
Physical ceiling = C-fiber max firing × max spatial recruitment ratio × max central amplification factor

C-fiber max firing: 100 Hz
Max spatial recruitment (all C-fibers): ~10⁵–10⁶ fibers (per spinal segment)
All C-fibers in a single segment firing: impossible (refractory randomness → ~30–50% simultaneous)

Dorsal horn max convergence: ~10³ C-fibers → 1 projection neuron
  Convergence ratio × single-fiber frequency = 1000 × 100 Hz × 0.05 (synaptic reliability) = 5000 Hz
  But dorsal horn neuron refractory limit: ~200 Hz maximum

Ceiling: ~200 Hz dorsal horn discharge → via thalamus → cortical perception
  → "10/10 pain" corresponds to ~150–200 Hz
  
Note: This "10/10" is not "the worst pain you can imagine"
  It is "the maximum neural discharge you have experienced in your lifetime"
  Physically, 200 Hz is the ceiling — locked by the refractory period
`

### 3.2 Why Do Different People Have Different Tolerance?

`
Same tissue damage → same C-fiber activation → but:

Sources of individual variation:
  (1) Descending inhibition efficiency: genetically determined receptor density (±30%)
  (2) Central sensitization propensity: NMDA receptor subtype differences (±50%)
  (3) Cognitive appraisal: prefrontal evaluation of pain meaning
  (4) Cultural/learned: pain behavior is socially modulated

These modulate perceived pain by ~2–5×
But cannot change the physical ceiling — C-fiber refractory period is a constant.
`

### 3.3 SCVC Pain Derivation Chain

`
α → lipid bilayer → C_m → τ_m → neuronal refractory period
α → H-bond energy → protein conformation → TRPV1 activation
α → Ca²⁺ pump energy → central sensitization ceiling
ATP → Substance P synthesis → slow pain pathway
`

---

*Your "10/10 pain" is physically limited to ~200 Hz of dorsal horn neuron firing. No torture, no disease, no nerve damage can push it higher — the refractory period of the neuron membrane, locked by τ_m derived from α, simply refuses.*
