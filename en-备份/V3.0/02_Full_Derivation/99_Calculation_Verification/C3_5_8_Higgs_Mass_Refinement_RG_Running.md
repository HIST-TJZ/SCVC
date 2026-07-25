# Higgs Mass Refinement

Date: 2026-07-21

## Summary

| | Original | Refined |
|:---|:---:|:---:|
| m_H range | 144-157 GeV | 140-164 GeV |
| Central (yt=SM 2L) | ~150 GeV | 156 GeV |
| Geometric yt (NDA) | -- | 146 GeV |
| LHC | 125.1 GeV | 125.1 GeV |
| Deviation (central) | +15-26% | +24% |
| Verdict | Green | Yellow (still >10 GeV) |

## Input Parameters

| Parameter | Value | Source |
|:---|:---|:---|
| M_KK | 5.22e+17 GeV | KK scale |
| ln(M_KK/v) | 35.29 | v=246.2 GeV |
| g1(SM, M_KK) | 0.5983 | N1=1.9746 x SCVC |
| g2(SM, M_KK) | 0.5141 | N2=0.4320 x SCVC |
| g3(SM, M_KK) | 0.5047 | N3=1.0092 x SCVC |
| lambda_eff(M_KK) | 2.0 | BPS(1.0)/f_c(0.5) |
| yt(M_KK, SM 2L) | 0.437181 | SM 2-loop RG |
| yt(M_KK, geo NDA) | 0.3635 | g2_SM/sqrt(2) |
| v0(BEC VEV) | 7.03e+17 GeV | sqrt(rho_s/m_c^2) |

## RG Results (running yt, no gauge in beta_lam)

| Scenario | lam(M_KK) | lam(v) | m_H(GeV) | dev |
|:---|:---:|:---:|:---:|:---:|
| Pure lam^2 analytic | 2.00 | 0.1705 | 144 | +14.9% |
| yt=0.30 (running) | 2.00 | 0.1615 | 140 | +11.8% |
| yt=SM 2L (running) | 2.00 | 0.2000 | 156 | +24.5% |
| yt=0.50 (running) | 2.00 | 0.2221 | 164 | +31.2% |
| yt(geo) (running) | 2.00 | 0.1765 | 146 | +16.9% |
| Alt lam=0.71+geo yt | 0.71 | 0.1630 | 141 | +12.4% |

## Key Findings

1. yt(M_KK) = 0.4372 from precise SM 2-loop running
2. Z2 compression f_c=1/2 is exact, giving lambda_eff=2.0
3. KK threshold: dlam_KK=0.0760, ~2-3 GeV effect
4. Running yt RG gives m_H ~ 140-164 GeV (higher than original frozen-yt)
5. Alternative BPS (g2/2) + geometric yt could give m_H ~ 141 GeV

## Verdict: YELLOW - refined but >10 GeV from 125.1 GeV

Residual deviation sources: lambda_eff uncertainty, yt geometric vs SM, 2-loop beta_lam

```
Numerical:
  M_KK=5.22e+17, ln(M_KK/v)=35.2902
  N1=1.9746, N2=0.4320, N3=1.0092
  yt_KK=0.437181, yt_geo=0.3635
  lam(v)=0.2000, mH=156 GeV (central)
  mH range=(140,164) GeV, mH_alt=141 GeV
  dlam_KK=0.0760
```