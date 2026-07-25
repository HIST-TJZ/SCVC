# SCVC Engineering Limit E86: Human Reaction Latency Floor — Absolute Physical Delay: Sensory → Cortex → Motor

**Derivation Date**: 2026-07-23  
**SCVC Hard Inputs**: α, k_B, τ_m ≈ 20 ms, axonal v_max ≈ 100 m/s (myelinated) / 1 m/s (unmyelinated), synaptic delay ~1 ms  
**Cross-References**: E28 (Nerve Conduction) + E69 (Muscle Power) + E70 (Vision) + E83 (Decision Rate)

---

## §1 Layer-by-Layer Signal Pathway Decomposition — Visual → Hand Movement Example

### 1.1 Complete Delay Chain

`
Retina:
  Phototransduction (cones):        5 ms    (opsin isomerization + transducin activation)
  Bipolar cell synapse:            2 ms
  Ganglion cell AP generation:     3 ms
  Retinal output delay:         ≈ 10 ms  [SCVC: opsin conformation driven by photoisomerization,
                                          activation energy ~2 eV, determined by retinal''s π-conjugated
                                          system (from α → C=C bond length)]

Optic nerve → LGN → V1:
  Axon length: ~5 cm (retina → LGN)
  Conduction velocity: ~10 m/s (unmyelinated; optic nerve partially myelinated but thin)
  LGN delay: ~2 ms (synaptic transmission)
  LGN → V1: ~2 cm, ~10 m/s
  V1 activation: ~5 ms (requires multi-synaptic integration)
  Visual input delay:           ≈ 17 ms  [SCVC: conduction velocity from E28, τ_m limits synaptic delay]

V1 → MT/V5 → Parietal → Premotor:
  V1 → MT (motion detection): ~5 ms (myelinated, ~5 cm, ~10 m/s ≈ 5 ms)
  MT → Parietal (spatial localization): ~5 ms
  Parietal → Premotor cortex: ~10 ms (long distance, ~10 cm)
  Premotor cortex integration: ~30 ms (attractor convergence, 5–10×τ_m)
  Motor planning delay:           ≈ 50 ms  [SCVC: here we hit E83''s decision wall]

Premotor → M1 → Spinal cord → Muscle:
  M1 activation: ~10 ms
  Corticospinal tract: ~50 cm, v ≈ 80 m/s (myelinated)
  → ~6 ms
  Spinal motor neuron: ~2 ms (monosynaptic)
  Neuromuscular junction: ~1 ms
  Muscle AP → contraction: ~10 ms (excitation-contraction coupling)
  Motor execution delay:        ≈ 30 ms  [SCVC: from E69 myosin ATP cycle]

─────────────────────────────────────────────────
Total delay (visual → hand button press): ≈ 107 ms
`

**SCVC locks each layer: Every layer''s delay is a physical constant. No "training" can lower transducin''s activation energy. No "talent" can accelerate axonal conduction.**

### 1.2 Delay Comparison Across Sensory Modalities

| Modality | Transduction | Conduction | Cortex | Motor | **Total** | Measured |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Visual → hand** | 10 | 17 | 50 | 30 | **107** | ~120–180 |
| **Auditory → hand** | 1 | 8 | 40 | 30 | **79** | ~80–120 |
| **Touch → hand** | 2 | 15 | 30 | 25 | **72** | ~70–100 |
| **Auditory → foot** | 1 | 8 | 40 | 45 | **94** | ~100–140 |

`
Auditory fastest → hair cell transduction ~0.1 ms (MET channels directly mechanically gated)
Tactile second → mechanoreceptors ~2 ms (stretch-activated channels)
Visual slowest → photochemical cascade ~10 ms (second-messenger amplification)
`

---

## §2 SCVC-Locked Layers

### 2.1 Phototransduction — Why Can''t It Be Faster Than ~5 ms?

`
Rhodopsin → photoisomerization: ~200 fs (ultrafast, quantum process)
Transducin (Gt) activation: ~1 ms (diffusion-limited, from k_B T)
PDE activation → cGMP hydrolysis: ~2 ms (enzymatic cascade amplification)
cGMP-gated channel closure: ~1 ms (ligand dissociation)
Membrane hyperpolarization: ~1 ms (membrane capacitance charging, τ_m ≈ 20 ms
  but this is the outer segment, with small C)

SCVC: Transducin diffusion time = r²/(2D) ≈ (1 μm)²/(2×10⁻¹⁰ m²/s) ≈ 5 ms
  Diffusion coefficient D is determined by protein viscosity in aqueous solution
  Water viscosity derived from H-bond energy (0.2 eV, from α) (E27)
  → Phototransduction cannot be faster than ~5 ms, locked by thermal motion of water molecules
`

### 2.2 Synaptic Delay — Why ~1 ms Each?

`
Presynaptic:
  AP arrival → Ca²⁺ channel opening: 0.2 ms (voltage-gated S4 motion, from force constant k ~10³ N/m)
  Ca²⁺ diffusion → vesicle fusion: 0.3 ms (Ca²⁺ sensor protein synaptotagmin)
  Transmitter release: 0.1 ms (vesicle fusion, SNARE complex)

Synaptic cleft:
  Transmitter diffusion: 0.05 ms (cleft ~20 nm, D ~10⁻¹⁰ m²/s)

Postsynaptic:
  Receptor binding + channel opening: 0.2 ms (ligand-gated, conformational change)
  EPSP rise: 0.5 ms (membrane capacitance charging, determined by C_m)

Total delay: ~1–2 ms/synapse [SCVC-locked: incompressible]
`

### 2.3 Cortical Decision — Why at Least ~50 ms?

`
From E83:
  Attractor convergence: 5–10 × τ_m = 100–200 ms (prefrontal complex decision)
  
But sensory→motor pathways use a faster "shortcut":
  Sensory cortex → Parietal (spatial attention) → Premotor → M1
  This is not "thinking" — this is "perception-action mapping"
  Per cortical relay: ~10–20 ms (excitatory synapses + local circuits)
  4–5 relays: ~50–80 ms

SCVC: Even "thought-free" reactions, cortical relaying still requires
  ~5 × τ_m ≈ 100 ms (pure sensory→motor, no cognitive processing)
  
Fastest measured:
  Sprint start (auditory gun): ~100–120 ms (Olympic sprinting)
  F1 start reaction: ~150–200 ms (visual signal → foot press, longer pathway)
  CS aim + fire: ~150–250 ms (visual detection + confirmation + motor)
`

---

## §3 SCVC Floor of Reaction Latency

### 3.1 Absolute Physical Floor (Monosynaptic Reflex)

`
The simplest "reaction": monosynaptic spinal reflex (knee jerk)
  Muscle spindle stretch → 1a afferent fiber (fastest myelinated, ~120 m/s)
  → Monosynaptic → α motor neuron
  → Muscle contraction
  
  Knee-jerk latency: ~20–30 ms [SCVC absolute floor]
  
This is the fastest human "stimulus→response" circuit.
No conscious involvement — purely a monosynaptic reflex arc.
No reaction involving the cortex can be faster than this.
`

### 3.2 SCVC Ceiling by Reaction Type

| Reaction Type | Circuit | SCVC min | Measured min | Gap |
|:---|:---|:---:|:---:|:---|
| **Spinal reflex** | Mono/disynaptic | **20 ms** | 20–30 | ✅ Reached |
| **Auditory simple RT** | Brainstem → cortex → motor | **80 ms** | 80–100 | Near |
| **Tactile simple RT** | Cortex → motor | **70 ms** | 70–100 | Near |
| **Visual simple RT** | Retina → V1 → motor | **100 ms** | 120–150 | ~20% gap |
| **Visual choice RT** | + Prefrontal | **200 ms** | 200–300 | ~30% gap |
| **Visual complex decision** | Widespread cortex | **500 ms** | 500–2000 | Variable |
| **Brake pedal (driving)** | Visual → cognitive → foot | **300 ms** | 350–500 | ~15% gap |

### 3.3 Why Are Humans Always ~20–50 ms Slower Than the SCVC Floor?

`
SCVC floor = sum of physical delays (ideal conditions, zero synaptic failure rate)
Measured = physical delay + synaptic reliability margin

Each synapse''s release probability ~0.2–0.5
→ Multiple attempts or parallel pathways needed for reliable transmission
→ Reliability margin: ~20–40% additional delay

Plus attentional switching cost: ~20–50 ms
→ Measured is 30–80 ms slower than the floor

These 30–80 ms are "biological noise," not the "physical ceiling."
Can be approached through training (e.g., esports athletes), but can never reach zero.
`

---

## §4 Engineering Conclusions

### 4.1 The Most Extreme Human Reactions

`
F1 driver start:    ~150 ms → ~50 ms from SCVC visual floor
CS pro player:      ~150 ms → smart strategy using auditory (gunshot) rather than visual
Table tennis return: ~200 ms → visual + prediction (ball-trajectory anticipation, not pure reaction)
Boxing dodge:        ~150 ms → using brainstem superior colliculus shortcut (bypassing V1!)

Any claimed "<100 ms visual reaction" human achievement:
  → Either anticipation (saw the opponent''s preparatory movement)
  → Or substituted auditory/tactile for visual
  → Or cheated on the measurement apparatus
  → Physically impossible: phototransduction + optic nerve + LGN + V1 > 50 ms
`

### 4.2 Why Is AI Faster Than Humans?

`
AI visual reaction:
  Camera exposure + transmission: ~1 ms
  GPU inference (ResNet etc.): ~1–5 ms
  Decision (policy network): ~1–2 ms
  Output: ~1 ms
  Total latency: ~5–10 ms (~20× faster than humans)

Bottleneck:
  Speed of light (3×10⁸ m/s): camera → chip ~30 cm → 1 ns (negligible)
  Chip clock: ~1 GHz → 1 ns per step
  Humans use chemical signals (ms-scale); AI uses electrical signals (ns-scale)
  Gap ~10⁶×
`

### 4.3 SCVC Derivation Chain

`
α → C-C bond length → lipid bilayer → C_m → τ_m → cortical delay ~50–100 ms
α → H-bond energy → water viscosity → protein diffusion → transduction delay ~5–10 ms
α → force constant → channel gating → synaptic delay ~1 ms
ATP → myosin → excitation-contraction coupling ~10 ms

Sum: ~80–110 ms (auditory → hand)
     ~100–130 ms (visual → hand)
`

---

*Your reaction speed is not "insufficient training" — it is because the diffusion speed of transducin protein in water is locked by the thermal motion of water molecules.*  
*And water''s hydrogen bond energy is derived from α.*
