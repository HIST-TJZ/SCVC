# Three Condensed Matter Crystals → SCVC Vortex Geometry Unified Derivation

**Date**: 2026-07-25 | **Status**: Wigner🟡, Exciton Insulator🟢, Time Crystal🟡

---

## Abstract

Three "crystals" find a unified language in SCVC vortex geometry: Wigner crystal = vortex ring Coulomb repulsion → spatial ordering, exciton insulator = vortex ring-anti-ring Coulomb attraction → pair condensation, time crystal = non-equilibrium periodic oscillation of vortex ring orientation. SCVC provides scaling laws and energy scales, but precise critical values still require quantum many-body calculations.

---

# Part 1: Wigner Crystal

## 1. Vortex Ring Crystallization

### 1.1 Physical Picture

```
Electron vortex rings + low density + low temperature → Coulomb repulsion dominates
→ vortex rings repel each other into periodic arrangement → Wigner crystal

Competition:
  Kinetic E_K ~ ħ²/(2m_e a²)  → quantum fluctuations → disrupt order
  Coulomb E_C ~ e²/(εa)       → repulsion → establish order

Critical condition: E_C/E_K = Γ_crit
```

### 1.2 SCVC Scale Derivation

```
e²/(4πε₀) = αħc  (SCVC fine structure constant)

E_C = αħc/(εa)
E_K = ħ²/(2m_e a²)

E_C/E_K = 2αm_e c a/(εħ) = 2αa/(ελ_C) = 2a/(εa_B)

where λ_C = ħ/(m_e c) (Compton wavelength), a_B = ħ/(αm_e c) (Bohr radius)

a_crit = (Γ_crit/2) · ε · a_B
r_s_crit = a_crit/a_B = Γ_crit · ε/2
```

### 1.3 Numerical Verification

```
Experiment/QMC:
  2D Wigner crystal: r_s ≈ 35-40
  3D Wigner crystal: r_s ≈ 100 (QMC)

SCVC reverse Γ_crit:
  2D: Γ_crit = 2r_s/ε ≈ 2×37/1 = 74 (vacuum ε=1)
      For GaAs(ε≈13): Γ_crit ≈ 2×37/13 ≈ 5.7
  3D: Γ_crit ≈ 2×100/1 = 200

Conclusion: Γ_crit is not O(1). SCVC provides the scale E_C/E_K ∝ α⁻¹a, but Γ_crit itself requires QMC.
```

### 1.4 What SCVC Can and Cannot Compute

| Quantity | SCVC? | Result |
|:---|:--:|:---|
| E_C/E_K scale ∝ α⁻¹·a/a_B | 🟢 Yes | Exact scaling law |
| Critical density n_c | 🟡 Semi-quantitative | Needs Γ_crit input |
| Ground state energy (3D bcc) | 🟡 Semi-quantitative | Madelung constant × e²/a |
| Melting temperature T_m | 🔴 No | Needs full phonon spectrum |
| Vortex ring orientation long-range order | 🟡 Semi-quantitative | Afv order → experimental test |

### 1.5 2D Wigner Crystal (GaAs/AlGaAs)

```
Experimental platform: GaAs/AlGaAs heterojunction, ε≈13, m*≈0.067m_e

SCVC prediction:
  E_C/E_K = 2a/(εa_B*) where a_B* = εħ²/(m*e²) ≈ 100Å

  With Γ_crit≈74: a_crit ≈ 3700Å, n_c ≈ 2.3×10⁹ cm⁻²

Experiment: n_c ~ 10⁹-10¹⁰ cm⁻²  ✅ Correct order of magnitude

SCVC scaling: n_c ∝ 1/m*² → lighter m* → higher n_c → harder to crystallize ✅
```

### 1.6 Unique SCVC Predictions

```
① Vortex ring circulation direction in Wigner lattice has Afv long-range order
   → Neutron scattering/μSR should detect antiferromagnetic signal (even without real spin)

② Phonon modes: collective oscillation of vortex ring circulation → distinguishable from ordinary phonons

③ Topological phase transition: vortex ring crystal → vortex ring liquid
   → Possible intermediate "hexatic phase" (KTHNY melting theory)

✅ Falsifiable: If Wigner crystal has no Afv order → vortex ring picture incomplete
```

### 1.7 Honest Verdict

| Question | Answer |
|:---|:---|
| Can SCVC derive r_s_crit closed-form? | 🔴 No. Γ_crit needs QMC. SCVC gives scale, not absolute value. |
| What does vortex ring picture add beyond QMC? | 🟡 Afv order prediction + topological phase transition mechanism |
| Falsifiable experimental prediction? | 🟢 Afv long-range order |
| Status | 🟡 Scaling law 🟢, absolute value needs QMC 🔴 |

---

# Part 2: Exciton Insulator

## 2. Exciton = Vortex Ring-Anti-Vortex Ring Pair

### 2.1 Superconductor vs Exciton Insulator SCVC Mirror

```
Superconductor:                   Exciton Insulator:
  e⁻ vortex ring + e⁻ vortex ring   e⁻ vortex ring + h⁺ anti-vortex ring
  → Initial repulsion               → Initial attraction (opposite circulation!)
  → Needs phonon mediator→pairing   → Coulomb direct pairing
  → Cooper pair                     → Exciton

Key symmetry:
  Cooper pair: vortex ring pair (same charge, needs mediator)
  Exciton: vortex ring-anti-ring pair (opposite charge, direct attraction)

→ Exciton insulator = "charge conjugate" version of superconductor
→ SCVC superconductor framework → directly transferable!
```

### 2.2 Exciton Binding Energy SCVC Closed Form

```
3D Exciton (Bulk):
  E_b(3D) = μe⁴/(2ε²ħ²) = μ(αc)²/(2ε²) = Ry* = (μ/m_e)·(1/ε²)·13.6 eV

2D Exciton (Quantum Well):
  E_b(2D) = 4μe⁴/(ε²ħ²) = 4×E_b(3D) = 4Ry*

SCVC input: α → e² = αħc → E_b ∝ α²
→ Exciton binding energy directly determined by fine structure constant ✅
```

### 2.3 Exciton Condensation Temperature

```
Weak-coupling BCS limit (low density, large exciton radius):
  T_c(BCS) ≈ T_F · exp(-1/|g_eff|)

Strong-coupling BEC limit (high density, tightly-bound excitons):
  T_c(BEC) ≈ 3.31 ħ²n_exc^(2/3)/(m_exc k_B)

Crossover: g_eff ∼ 1 at n_exc a_B*³ ∼ 1
```

### 2.4 SCVC Contribution Summary

| Item | Status |
|:---|:--:|
| Exciton binding energy scale ∝ α² | 🟢 Exact |
| T_c(BCS) | 🟡 Semi-quantitative |
| T_c(BEC) | 🟡 Semi-quantitative |
| Exciton insulator ↔ superconductor mirror | 🟢 Geometric symmetry |
| Honest status | 🟢 Scale correct, quantitative needs many-body input |

---

# Part 3: Time Crystal

## 3. Time Crystal = Vortex Ring Orientation Non-Equilibrium Periodic Oscillation

### 3.1 Physical Picture

```
In SCVC: vortex ring has internal degree of freedom = circulation direction (normal vector n̂)

Non-equilibrium drive → n̂ oscillation → periodic in time → time crystal

Two necessary conditions:
  ① Floquet drive: external periodic modulation (e.g. AC magnetic field)
  ② Many-body localization: prevents heating to infinite temperature

SCVC-predicted frequency:
  ω_TC ∝ α · ω_drive (subharmonic response at ω_drive/2)
```

### 3.2 Honest Verdict

SCVC provides geometric language (vortex ring orientation = internal degree of freedom), but time crystal realization requires detailed non-equilibrium many-body dynamics — beyond SCVC pure geometry scope.

**Status: 🟡 Conceptual framework provided, quantitative predictions need Floquet many-body calculations.**
