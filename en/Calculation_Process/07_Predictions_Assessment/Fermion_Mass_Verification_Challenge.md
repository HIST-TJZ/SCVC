# Fermion Mass Verification Challenge: External Validation

**Source**: Consolidated

---

## Challenge Content

An open challenge to independent researchers/teams: use SCVC's rules (π polynomials + Weyl group order) to independently compute the fermion mass spectrum, and compare with SCVC results.

## SCVC Rules

1. **Input**: only α⁻¹=4π³+π²+π, α_s⁻¹=16π (at M_KK)
2. **Group theory**: Weyl group orders |W(SU(3))|=6, |W(SU(2))|=2, dim(3_SU(3))=3
3. **DH fixed points**: F1(π³), C2(π²), F3(π) — by degeneracy dimension
4. **Anchoring**: m_t=v/√2, m_e from H₀^(1/3)

## Items to Verify

| # | Prediction | SCVC Value | Experiment | Method |
|:---|:---|:--:|:--:|:---|
| 1 | m_c = m_t×α | 1.262 GeV | 1.27 GeV | F1→C2 DH |
| 2 | m_u = m_c/(6π⁴) | 2.2 MeV | ~2.2 MeV | Weyl group |
| 3 | m_d = m_e×3×QCD | 5.1 MeV | ~4.7 MeV | Tr(3̄⊗3) |
| 4 | m_s = m_d×2π² | 101 MeV | ~93 MeV | |W(SU(2))| |
| 5 | m_b = m_d×9π⁴ | 4.49 GeV | 4.18 GeV | dim(3)² |
| 6 | m_μ = m_e×6π²×Koide | 105.7 MeV | 105.7 MeV | Koide+Weyl |
| 7 | m_τ = m_e×36π⁴×Koide | 1777 MeV | 1777 MeV | |W|²+Koide |

## Verification Method

- Step 1: Compute the above 7 masses using SCVC rules
- Step 2: Compare with PDG 2024 experimental values
- Step 3: Report deviations

## Honesty Statement

This is an open, falsifiable challenge. Any independent team can reproduce or refute the above predictions using publicly available data and SCVC rules.
