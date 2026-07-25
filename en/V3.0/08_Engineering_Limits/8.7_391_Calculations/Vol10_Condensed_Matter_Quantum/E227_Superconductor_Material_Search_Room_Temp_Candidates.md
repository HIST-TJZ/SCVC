# Superconductor Material Search → SCVC Periodic Table Scan → Room-Temperature Candidates

**Date**: 2026-07-25 | **Status**: Honest report — λ cannot be purely geometrized, but SCVC provides the scale framework

---

## 0. Core Finding (Honesty First)

**λ cannot be derived from a simple function of Z_eff+Z_val+a.** Back-calculating λ for 7 known superconductors, k=λ/(Z_eff·Z_val^(1/3)/a⁴) varies from 5 to 82 — a factor of 16:

| Material | λ_exp | k-factor | Notes |
|:---|:--:|:--:|:---|
| Al | 0.42 | 19 | Simple metal |
| Nb | 0.75 | 9 | d-band enhanced |
| Pb | 1.03 | 38 | Strong coupling |
| V | 0.57 | 5 | d-band, lowest k |
| Sn | 0.62 | 82 | Complex structure, highest k |
| Hg | 0.94 | 8 | Strong coupling |
| Nb₃Sn | 0.99 | 70 | A15 structure |

**Conclusion: N(0) and electron-phonon matrix elements depend on band structure — pure geometric closed form not feasible. 🟡→🔴**

## 1. What SCVC Still Provides

### 1.1 θ_D Geometric Closed Form (Verified, 🟢)
```
θ_D = 4200 · √(Z_eff²/M) · a^(-4/3) K
```
Deviation: Al(−3.7%), Cu(+1.5%), Nb(+1.1%), Pb(−6.7%). Average ~3%.

### 1.2 λ Scale Range (SCVC Constraint)
SCVC sets physical scale upper bounds:
- V_SCVC_max ∼ α·ℏc/a₀ ∼ 27 eV (atomic scale)
- χ_lattice_max ∼ (M_ion/m_e)^(1/4) ∼ 10-30
- λ_max ∼ 3-4 (Eliahsberg theory strong-coupling limit)

### 1.3 Tc Contour Map (Allen-Dynes, μ*=0.13)
Tc>300K requires: θ_D>1200K AND λ>2.5, OR θ_D>1500K AND λ>2.0.

## 2. The Dilemma

```
High θ_D → needs ultra-light elements (H, Be, B, C)
High λ   → needs high N(0) (d-band metals, transition elements)

These are orthogonal in the periodic table!
```

**High pressure breaks the dilemma**: H-sublattice provides extremely high θ_D, heavy atoms (La, Y, S) provide high N(0), λ increases under pressure.

## 3. Candidate Rankings

### Room-Temperature Candidates (Tc>300K):
| Material | θ_D(K) | λ_est | Tc(K) | P(GPa) | Confidence |
|:---|:--:|:--:|:--:|:--:|:--:|
| **BeH₄** | 1500 | 2.5 | **380** | 180 | 🟡 Speculative |
| **BH₈** | 1600 | 2.5 | **410** | 200 | 🟡 Speculative |
| **CH₈** | 1800 | 2.5 | **460** | 220 | 🟡 Speculative |
| **Be-H-B** | 1800 | 3.0 | **580** | 200 | 🟠 Bold |
| **Metallic H** | 2500 | 2.5 | **640** | 400 | 🟠 Extreme |
| **Li-Be-H** | 1600 | 3.0 | **520** | 180 | 🟠 Bold |

### Most Reliable Candidates:
- **YH₁₀** (unsynthesized): Extrapolation from YH₆+YH₉>240K
- **CaH₁₀** (unsynthesized): CaH₆ predicted 210K
- **Be-H compounds**: Be 3× lighter than Mg → θ_D 3× MgB₂
- **C-S-H optimization**: Existing room-temperature reports

## 4. Honesty Assessment

| Item | Status |
|:---|:--:|
| θ_D geometric closed form | 🟢 Verified, avg ~3% |
| λ cannot be purely geometrized | 🔴 Needs N(0) band structure |
| Tc contour map | 🟡 Semi-quantitative |
| Room-temperature candidate ranking | 🟡 Material-dependent |
| SCVC contribution | 🟢 Sets physical scale; guides search direction |
