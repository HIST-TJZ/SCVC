# Biology: Action Potential Minimum Energy SCVC Derivation

**Date**: 2026-07-26 | **Status**: 🟡 Ion channel energetics from α scale

---

## Core Formula

Action potential energy cost per spike:
```
E_AP ≈ N_channels × (ΔV)² × C_membrane
```

SCVC: ion channel gating energy scale ∼ k_B T (thermal) with selectivity determined by:
- Ion hydration energy ∝ α² (Coulomb binding of water to ion)
- Channel pore geometry → vortex ring circulation selects ion size

Na⁺/K⁺ selectivity = exp(-ΔG/k_B T) where ΔG = (hydration energy difference)/(dielectric constant of pore).
SCVC: hydration energies ∝ α² → ion selectivity directly traces to α = 1/(4π³+π²+π).

## Honesty: SCVC provides the underlying Coulomb scale for ion hydration. Detailed channel gating kinetics requires protein structural biology — far beyond SCVC scope.
