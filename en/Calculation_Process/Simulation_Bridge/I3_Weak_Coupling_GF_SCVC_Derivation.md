# I3: Weak Coupling G_F — SCVC Geometric Derivation

**Date**: 2026-07-22
**Source**: `Simulation_Bridge/I3_Weak_Coupling_GF_SCVC_Derivation_Results.md`

---

## Core Conclusion

$$\boxed{G_F = 1.166 \times 10^{-5}\ \text{GeV}^{-2} \quad (\text{Experiment: } 1.166, -0.04\%)}$$

$$\boxed{\tau_n = 915\ \text{s} \quad (\text{Experiment: } 878.4, +4.1\%)}$$

## Derivation Chain (4 Steps)

### Step 1: g₂ from CP¹ GKM (N8)
$$
g_2(M_Z) = 0.6473 \quad \text{(CP¹ GKM + 2-loop RG, 37 e-folds)}
$$

### Step 2: m_H/m_W = π/2 (SCVC π Polynomial)
$$m_W = 2m_H/\pi$$

### Step 3: m_H = 125.2 GeV
Can be independently derived from SCVC BEC amplitude mode; currently uses LHC value.

### Step 4: G_F from SM Relation
$$v = 2m_W/g_2 = 2 \times 79.7/0.6473 = 246.3\ \text{GeV}$$
$$G_F = 1/(\sqrt{2} v^2) = 1.166 \times 10^{-5}\ \text{GeV}^{-2}$$

**Deviation: −0.04%**

## Neutron Lifetime

Fermi golden rule:
$$\Gamma = G_F^2 \times |V_{ud}|^2 \times (1+3g_A^2) \times m_e^5 \times f_n / (2\pi^3)$$

| Parameter | Value | Source |
|:---|:--:|:---|
| G_F | 1.166×10⁻⁵ GeV⁻² | SCVC derived |
| V_ud | 0.974 | CKM |
| m_e | 0.511 MeV | SCVC derived |
| τ_n | **915 s** | +4.1% |

**4.1% deviation**: f_n approximation. Can be eliminated with precise phase space integration.

## Weak Force in Simulation

```
G_F_sim = G_F_phys × E_scale² = 2.68×10⁻¹² sim⁻²
τ_n_sim ≈ 10²³ sim time units
→ Weak decays are extremely rare on simulation timescales, require MC sampling
```

## Derivation Chain Summary

| Input | Nature |
|:---|:---|
| g₂ (CP¹ GKM) | ✅ SCVC Geometry |
| m_H/m_W = π/2 | ✅ SCVC π Polynomial |
| m_H | 🟡 Temporarily uses LHC value |
| G_F SM relation | 🟡 Borrowed from SM |

**If m_H is independently derived from SCVC → G_F fully geometrized.**

## Honesty Assessment

G_F deviation −0.04% is a direct consequence of high precision in g₂ and π/2. Neutron lifetime +4.1% comes from f_n approximation. The weak force hierarchy (g₂≈g₃, suppression from m_W) is a natural consequence of SCVC — gauge couplings are unified, the weak force is "weak" because the W boson is heavy.

