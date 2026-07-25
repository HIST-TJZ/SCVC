# Optical Refractive Index Ceiling

**Date**: 2026-07-25 | **Status**: 🟢 SCVC provides dielectric response scale

## Core
n_max = √(ε_max) where ε = dielectric constant.

### Theoretical Bounds
```
n² = ε ∼ 1 + (plasmon frequency/band gap)²

Maximum n when: band gap → 0 (metallic limit)
```

In practice: n_max ∼ 4-5 (e.g., PbS n≈4.0, PbSe n≈4.7, PbTe n≈5.5).

### SCVC Scale
Plasmon frequency: ω_p ∝ √(n_e e²/m_e) ∝ √(α).
Band gap: E_g ∝ Ry ∝ α².
→ n_max ∝ α^(-1/2) ∝ √137 ≈ 11.7 (theoretical, never achieved because band gap cannot be zero in stable materials).

### Comparison
| Material | n (IR) | % of SCVC limit |
|:---|:--:|:--:|
| PbTe | 5.5 | 47% |
| PbSe | 4.7 | 40% |
| Si | 3.4 | 29% |
| Diamond | 2.4 | 21% |
| **SCVC upper bound** | **~12** | 100% |

## Honesty: Practical n is limited by material stability, not fundamental physics. SCVC sets the dielectric scale.
