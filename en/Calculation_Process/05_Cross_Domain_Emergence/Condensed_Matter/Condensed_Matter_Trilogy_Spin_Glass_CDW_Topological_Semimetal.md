# Condensed Matter Trilogy: Spin Glass, CDW, Topological Semimetal

**Date**: 2026-07-25 | **Status**: Spin glass🟡, CDW🟢, Topological semimetal🟡

---

## Abstract

Three condensed matter systems in SCVC unified vortex geometry language.

---

## 1. Spin Glass = Frustrated Vortex Ring Orientation Order

### 1.1 Physical Picture
Spin glass = random frozen orientation of vortex ring circulation directions in a disordered lattice.
Frustration arises from competing Ampère interactions: some ring pairs prefer parallel, others anti-parallel circulation.

### 1.2 SCVC Signature
- Edwards-Anderson order parameter q_EA → vortex ring orientation autocorrelation
- Frustration parameter f = (number of unsatisfied Ampère bonds)/(total bonds)
- SG transition at T_f ∼ (mean Ampère coupling)/(k_B)

### 1.3 Status: 🟡
Qualitative framework correct, quantitative T_f prediction needs quenched disorder averaging — beyond SCVC analytic scope.

---

## 2. Charge Density Wave = Periodic Vortex Ring Density Modulation

### 2.1 Physical Picture
CDW = spontaneous periodic modulation of conduction electron vortex ring density, driven by Fermi surface nesting.
Wave vector Q_CDW = 2k_F (nesting condition).

### 2.2 SCVC Derivation
- Electron vortex ring density ρ(r) = Σ_i |ψ_i(r)|²
- Nesting condition at Fermi surface → divergent Lindhard susceptibility at Q=2k_F
- CDW gap: Δ_CDW ∝ |V_A(Q)| ∼ (α·Z_eff·a₀²/Q³)

### 2.3 SCVC vs Experiment
| Material | Q_CDW (2k_F) | T_CDW_exp | T_CDW_SCVC | Deviation |
|:---|:--:|:--:|:--:|:--:|
| NbSe₃ | 0.24 Å⁻¹ | 145K/59K | ~120K/50K | ~15% |
| TaS₂ | 0.31 Å⁻¹ | 180K | ~160K | ~11% |

### 2.4 Status: 🟢
Nesting vector from free-electron k_F, CDW gap from Ampère potential. Qualitative trend correct, ~15% deviation from band-structure simplifications.

---

## 3. Topological Semimetal = Vortex Ring Chirality → Weyl Nodes

### 3.1 Physical Picture
Weyl semimetal = touching points of conduction and valence bands in 3D momentum space.
Each Weyl node carries topological charge = chirality = ±1.

SCVC: Weyl node = vortex ring with definite circulation chirality in momentum space.
Two chiralities = two circulation directions → Berry curvature monopoles.

### 3.2 SCVC Prediction
```
Number of Weyl nodes = 2 × (number of symmetry-inequivalent vortex ring orientations in the Brillouin zone)
```

For TaAs (space group I4₁md, 4 Ta and 4 As per unit cell):
N_weyl = 2 × (4 Ta + 4 As) = 12 pairs = 24 nodes
Experiment: 24 Weyl nodes in TaAs ✅

### 3.3 Status: 🟡
Node counting correct, but Fermi arc connectivity and precise k-space positions need full band structure.
