# Plasma Fusion Conditions: Debye Length SCVC Derivation

**Date**: 2026-07-26 | **Status**: 🟢 Debye length from α geometry

---

## Core Formula

```
λ_D = √(ε₀ k_B T / (n_e e²)) = √(k_B T / (4π n_e α ℏc))
```

SCVC input: e² = 4παℏc, α = 1/(4π³+π²+π).

## Lawson Criterion (SCVC Form)

```
n_e τ_E T > 3k_B T² / (⟨σv⟩ E_α)
```

SCVC contribution: the fusion cross-section ⟨σv⟩ depends on α (Coulomb barrier penetration factor).
→ Lawson criterion ∝ α⁻² → if α were different, fusion conditions would be different.

## Honesty: SCVC provides the Coulomb scale via α. Lawson criterion detailed physics needs plasma kinetic theory.
