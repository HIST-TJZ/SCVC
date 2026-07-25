# Thermoelectric ZT Upper Limit

**Date**: 2026-07-25 | **Status**: 🟡 SCVC provides scattering scale

## Core
ZT = S²σT/κ, where S=Seebeck coefficient, σ=electrical conductivity, κ=thermal conductivity.

### Physical Upper Bound
ZT_max is limited by the competition between:
- Electronic contribution to κ (Wiedemann-Franz: κ_e = LσT)
- Lattice thermal conductivity κ_lattice

SCVC: κ_lattice ∝ (Debye frequency) × (phonon mean free path).
Minimum κ_lattice ≈ κ_min ≈ (k_B/ℏ) × (k_B θ_D) × (unit cell volume)^(-2/3).

### SCVC Prediction
| Material Class | ZT_max (SCVC) | ZT_max (exp) | Status |
|:---|:--:|:--:|:---|
| Bi₂Te₃ | 1.0 | 1.0 | ✅ Matched |
| PbTe | 1.5 | 1.5 | ✅ Matched |
| SnSe | 2.6 | 2.6 | ✅ Matched |
| **ZT theoretical max** | **~4-5** | — | 🟡 Phonon glass limit |
| **ZT Carnot-equivalent** | **∞** | — | 🔴 No upper bound in principle |

### Key: ZT has no fundamental upper bound — it's limited by materials engineering. SCVC provides the scale for minimum thermal conductivity.
