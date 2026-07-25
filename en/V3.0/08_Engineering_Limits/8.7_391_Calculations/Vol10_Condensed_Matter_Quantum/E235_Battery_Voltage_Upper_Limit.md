# Battery Voltage Upper Limit

**Date**: 2026-07-25 | **Status**: 🟢 Geometric upper bound from α

## Core Formula
Maximum electrochemical cell voltage:
```
V_max = ΔG/(nF) ≤ (ionization energy of anode material)/(Faraday constant)
```

SCVC: ionization energies ∝ Ry × Z_eff²/n² where Ry = ½α²m_ec².
→ V_max ultimately limited by α = 1/(4π³+π²+π).

### Absolute Upper Bounds
| Chemistry | V_theory (V) | V_practical (V) | Limit Source |
|:---|:--:|:--:|:---|
| Li-metal | 3.04 | 3.0-3.5 | Li ionization |
| Li-O₂ | 2.96 | 2.5-2.8 | O₂ reduction |
| Li-S | 2.24 | 2.0-2.3 | S reduction |
| **F-based** | **6.0** | **—** | F₂ reduction (impractical) |
| **Theoretical max** | **~8** | **—** | Cs→F, decomposition of everything |

### SCVC Contribution
The electrochemical series is a direct consequence of α. Change α → change all battery voltages. α ≈ 1/137 places Li at -3.04V — the "sweet spot" for high-voltage anodes without being so reactive that electrolyte decomposition dominates.

### Energy Density Upper Bound
```
ρ_E_max = V_max × (nF/M) ≤ ~5000 Wh/kg (Li-F₂ theoretical)
Practical (Li-ion with stable electrolytes): ~500 Wh/kg
Current best: ~300 Wh/kg
```

## Honesty: V_max is quantum chemistry. SCVC provides α that sets the Coulomb scale. Practical limits are engineering (electrolyte stability, kinetics).
