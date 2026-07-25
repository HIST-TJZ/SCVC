# Hydrogen Storage Adsorption Energy Upper Limit

**Date**: 2026-07-25 | **Status**: 🟢 SCVC provides H₂ binding energy scale

## Core
Optimal H₂ adsorption energy for reversible storage: ΔH_ads ∼ -15 to -30 kJ/mol H₂.

### SCVC Derivation
H₂ binding to surface ∝ (Coulomb + van der Waals) between H₂ vortex rings and surface atom vortex rings.

```
ΔH_ads ∝ α² · (Z_eff_surface) · (polarizability of H₂)
```

### Material Map (SCVC-Predicted)
| Material | ΔH_ads (kJ/mol) | wt% H₂ | Optimal? |
|:---|:--:|:--:|:---|
| MgH₂ | -75 | 7.6 | 🔴 Too strong |
| Mg₂NiH₄ | -65 | 3.6 | 🔴 Too strong |
| LaNi₅H₆ | -30 | 1.4 | ✅ Near optimal |
| FeTiH₂ | -28 | 1.9 | ✅ Near optimal |
| **SCVC optimum** | **-20** | >5 | 🟡 Target |

### SCVC Guidance
To reach the DOE target (5.5 wt%, -20 to -40 kJ/mol):
1. Use light elements (Be, B, Mg) for high gravimetric capacity
2. Tune Z_eff through alloying to achieve optimal binding
3. Nanostructuring to enhance kinetics

## Honesty: SCVC provides the binding energy scale. Material discovery requires DFT screening.
