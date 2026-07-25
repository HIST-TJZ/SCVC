# Corrosion Rate Upper Limit

**Date**: 2026-07-25 | **Status**: 🟡 Electrochemical kinetics from α

## Core
Corrosion rate ∝ exp(-E_a/k_B T) where E_a = activation barrier for metal dissolution.

### SCVC Scale
E_a ∝ (metal-oxygen bond energy) ∝ α².
Maximum corrosion rate when E_a → 0 (thermodynamically unstable metal in given environment).

```
Rate_max ∼ (surface atom density) × (attempt frequency)
         ∼ 10¹⁵ atoms/cm² × 10¹³ s⁻¹ ∼ 10²⁸ atoms/(cm²·s)
         ∼ 1 mm/s (unstable metals like Na in water)
```

### Practical Limits
| Environment | Rate (mm/year) | Mechanism |
|:---|:--:|:---|
| Dry air | <0.001 | Passivation layer |
| Fresh water | 0.01-0.1 | Electrochemical |
| Seawater | 0.1-1 | Cl⁻ pitting |
| Strong acid | 1-100 | Rapid dissolution |
| **SCVC maximum** | **~3×10⁷** | Bare metal, no passivation |

## Honesty: Corrosion is dominated by passivation layer kinetics, not fundamental physics.
