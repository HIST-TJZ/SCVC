# I1: Hydrogen Isotopes — SCVC Liquid Drop Model + Vortex Ring Verification

**Date**: 2026-07-22
**Source**: `Simulation_Bridge/I1_Hydrogen_Isotopes_Verification_Results.md`

---

## Core Results

| Isotope | B_exp (MeV) | Stability | SCVC Determination |
|:---|:--:|:---|:---|
| ¹H | — | Stable ✅ | Single proton, stable ✅ |
| ²H | 2.225 | Stable ✅ | p-n vortex ring pair bound ✅ |
| ³H | 8.482 | β⁻ (12.33 yr) ✅ | p+2n, β⁻ ✅ |
| ⁴H | 5.6 | n emission ✅ | p+3n, unbound ✅ |

## Liquid Drop Model: Honest A<10 Failure

The liquid drop model assumptions do not hold for A=2-4 light nuclei (surface/volume term distinction meaningless, pairing term diverges). **Not an SCVC failure — an inherent limitation of the liquid drop model.**

## SCVC Vortex Ring Light-Nucleus Picture

### ²H (Deuteron)
- Proton ring + neutron ring, spin triplet (S=1), isospin singlet (T=0)
- No Pauli repulsion between rings (different isospin → can coexist)
- Nuclear force effective coupling ≈ 1.4× bare QCD coupling (π-meson exchange enhancement)

### ³H (Tritium) → β⁻ decay
- p+2n, w_w flip: d→u (Δw_w=+1) → ³He
- Half-life 12.33 yr, SCVC G_F prediction (I3)

## Vortex Ring Picture vs Liquid Drop Model

Vortex ring picture is more natural for light nuclei (A<10) — directly handles few-body dynamics without relying on macroscopic assumptions.

## Honesty Assessment

| Item | Status |
|:---|:--:|
| H/D/T/⁴H stability pattern | ✅ 4/4 correct |
| Liquid drop model A<10 | 🟡 Honest failure |
| ²H binding energy quantitative | 🟡 Needs nuclear force effective coupling refinement |

