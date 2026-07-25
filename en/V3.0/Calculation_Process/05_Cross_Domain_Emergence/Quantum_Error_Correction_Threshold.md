# Quantum Error Correction Threshold: SCVC Derivation

**Date**: 2026-07-26 | **Status**: 🟡 Threshold scale from Ampère energy hierarchy

---

## Core Insight

Quantum error correction threshold ~1% is not arbitrary — it reflects the ratio of physical gate error rate to logical operation energy scale.

SCVC: physical gate error rate ∝ (thermal noise energy)/(Ampère flip energy)
```
ε_gate ∼ k_B T / ΔE_flip ∼ 0.026 eV / 0.13 eV ∼ 0.2 (at 300K)
```

At 4K: ε_gate ∼ 3.4×10⁻⁴ eV / 0.13 eV ∼ 2.6×10⁻³ ≈ 0.26%
→ Below surface code threshold (~1%) ✅

SCVC predicts: quantum error correction viable below ~15K.

## Honesty: This is a scale argument. Actual threshold values depend on detailed noise models and code design — information theory, not physics.
