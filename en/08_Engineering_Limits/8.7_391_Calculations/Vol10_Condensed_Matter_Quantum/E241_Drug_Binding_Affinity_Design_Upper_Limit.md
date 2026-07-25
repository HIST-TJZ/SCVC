# Drug Binding Affinity Design Upper Limit

**Date**: 2026-07-25 | **Status**: 🟡 SCVC provides intermolecular force scales

## Core
Binding affinity K_d ∝ exp(-ΔG_bind/k_B T).
Maximum affinity limited by the strongest non-covalent interactions.

### Interaction Energy Scales (SCVC)
| Interaction | Energy (kcal/mol) | α-dependence |
|:---|:--:|:---|
| H-bond | 1-7 | ∝ α² |
| van der Waals | 0.5-1 | ∝ α² |
| Ionic | 5-10 | ∝ α |
| π-π stacking | 1-3 | ∝ α² |
| **Covalent (not drug-like)** | 50-100 | ∝ α² |

### Maximum Drug-Like Affinity
```
ΔG_bind_max ∼ 15-20 kcal/mol (sum of optimized non-covalent interactions)
K_d_min ∼ exp(-20/0.6) ∼ 10⁻¹⁵ M (fM range — biotin-streptavidin)
```

### SCVC Drug Design Principle
Optimal binding = maximize Ampère complementarity between drug and target vortex ring patterns.
→ Shape complementarity + electrostatic complementarity + dynamic complementarity.

## Honesty: Binding affinity optimization is computational chemistry, not fundamental physics. SCVC provides the energy scales.
