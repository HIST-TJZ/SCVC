# Catalytic TOF (Turnover Frequency) Upper Limit

**Date**: 2026-07-25 | **Status**: 🟡 SCVC provides reaction barrier scale

## Core
TOF_max ∝ (attempt frequency) × exp(-E_a/k_B T)

SCVC: E_a (activation energy) ∝ (bond rearrangements) ∝ α-dependent bond energies.
Attempt frequency ∝ k_B T/h ∼ 6×10¹² s⁻¹ at 300K.

### Upper Bound
```
TOF_max ∼ (k_B T/h) × exp(-E_a_min/k_B T)
E_a_min ∼ 0.1-0.3 eV (weakest chemisorption without being physisorption)
→ TOF_max ∼ 10⁶-10⁹ s⁻¹ at 300K
```

### SCVC Contribution
Chemical bond energies ∝ α² → activation barriers ∝ α².
If α were different, all catalytic rates would change.

### Comparison
| Catalyst | Reaction | TOF (s⁻¹) | % of limit |
|:---|:---|:--:|:--:|
| Pt | CO oxidation | 10¹-10³ | <0.1% |
| Nitrogenase | N₂→NH₃ | ~1 | ~10⁻⁷% |
| **Sabatier optimum** | — | ~10⁶ | ~10% |
| **SCVC upper bound** | — | **~10⁹** | 100% |

## Honesty: TOF limits are dominated by catalyst design (active site geometry), not fundamental physics. SCVC provides the bond-energy scale.
