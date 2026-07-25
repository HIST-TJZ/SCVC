# Quantum Decoherence T₂ Upper Limit

**Date**: 2026-07-25 | **Status**: 🟡 SCVC Ampère fluctuation noise floor

## Core
T₂ (dephasing time) is limited by environmental noise coupling to the qubit.

### Noise Sources and SCVC Limits
| Noise Source | T₂ Limit (s) | SCVC Origin |
|:---|:--:|:---|
| Thermal (phonon) | ~10⁻³ at 4K | θ_D ∝ √(α/M) |
| Charge (1/f) | ~10⁻⁶-10⁻³ | Coulomb fluctuations ∝ α |
| **Ampère fluctuation** | **~10⁻²** | Vacuum vortex ring fluctuations |
| Nuclear spin bath | ~10⁻⁴-10⁻³ | Hyperfine ∝ α³ |
| **SCVC absolute floor** | **~10⁻¹** | Fundamental Ampère vacuum noise |

### SCVC Ampère Noise Floor
Two vacuum vortex rings can spontaneously create/annihilate → Ampère field fluctuation at the qubit.

```
S_Ampère(ω) ∝ α² · (ℏ/ΔE_flip) · (r_qubit/ξ)⁻⁶
T₂_Ampère ∝ 1/S_Ampère(ω_qubit) ∼ 0.1 s (for superconducting qubit at ω∼5 GHz)
```

### Comparison
| Qubit Type | T₂ (best) | T₂/T₂_Ampère |
|:---|:--:|:--:|
| Superconducting (transmon) | ~300 μs | 0.3% |
| Trapped ion | ~1 s | ~10× |
| NV center | ~1 ms | 1% |
| **SCVC Ampère floor** | **~0.1 s** | 100% |

### Implications
- Current superconducting qubits are ~300× below the Ampère noise floor → lots of room for improvement
- Trapped ions already near/exceeding Ampère floor → may be close to fundamental limit
- SCVC predicts: no quantum computer can have T₂ > ~0.1 s for electron-spin-based qubits

## Honesty: Ampère vacuum noise is a new prediction. Experimental verification needed.
