# E3: GP Lookup Tables v2.0 — Complete Results

**Date**: 2026-07-24
**Status**: All 12 JSON LUTs computed. 500 sim range, 2000 bins, l=0/1/2.

---

## Scaling Coefficient Analysis

**Question**: Does the simulation need the 1/137 = alpha scaling factor?

**Answer: NO.** The sim uses its own unit system (sim_E, sim_L) and is internally consistent.

| Factor | Needed? | Reason |
|:---|:---|:---|
| 1/137 (alpha) | NO | alpha is SCVC OUTPUT: (4pi^3+pi^2+pi)^(-1) |
| 1/sqrt(1836) | NO for G, YES for xi | Mass rescaling: xi_e = xi * sqrt(1836). G_EM unchanged. |
| G_EM = 2.00 | YES, universal | e and p have same charge -> same coupling |

**Previous ee tables used G_EM/sqrt(1836)=0.0467 -> FIXED to G_EM=2.00.**

---

## Changelog

| Item | v1.0 | v2.0 |
|:---|:---|:---|
| Range | 0.01-200 sim | **0.01-500 sim** |
| Bins | 1000 | **2000** (0.25 sim/bin) |
| Orbitals | l=1 only | **l=0,1,2** (s,p,d) |
| G_EM | ep=2.00, ee=0.0467 | **Unified = 2.00** |
| Pauli ee | same:strong/short, opp:weak/long | **Same range, different amplitude** |

---

## Generated Files

| File | Size | Description |
|:---|:--:|:---|
| lut_ep_l0.json | 122.6 KB | e-p, s-orbital |
| lut_ep_l1.json | 122.6 KB | e-p, p-orbital |
| lut_ep_l2.json | 122.7 KB | e-p, d-orbital |
| lut_ep.json | 122.7 KB | backward compat (=l1) |
| lut_ee_l0.json | 199.3 KB | e-e, s-orbital, spin-dep |
| lut_ee_l1.json | 199.3 KB | e-e, p-orbital, spin-dep |
| lut_ee_l2.json | 199.4 KB | e-e, d-orbital, spin-dep |
| lut_ee.json | 199.3 KB | backward compat (=l1) |
| lut_pp_l0.json | 118.7 KB | p-p, s-orbital |
| lut_pp_l1.json | 118.8 KB | p-p, p-orbital |
| lut_pp_l2.json | 118.7 KB | p-p, d-orbital |
| lut_pp.json | 118.7 KB | backward compat (=l1) |

**Total**: 12 files, 1.72 MB

---

## Key Values

### e-p (l=0/1/2 comparison)

| r (sim) | l=0 | l=1 | l=2 | Physics |
|:--:|:--:|:--:|:--:|:---|
| 0.5 | -0.13 | +0.89 | +2.94 | centrifugal dominates |
| 1.0 | -0.86 | -0.60 | -0.08 | core+Coulomb+centrifugal |
| 5.0 | -11.78 | -11.77 | -11.75 | Coulomb dominates |
| 10.0 | -14.76 | -14.76 | -14.75 | Coulomb |
| 100.0 | -23.97 | -23.97 | -23.97 | far-field VFM |
| 500.0 | -27.65 | -27.65 | -27.65 | asymptotic log |

l-differences significant only for r < xi_e = 10.7 sim (vortex core overlap)

### e-e (spin-dependent, l=0)

| r (sim) | Same-spin | Opp-spin | Delta |
|:--:|:--:|:--:|:--:|
| 0.5 | 1.058 | 0.320 | +0.737 |
| 1.0 | 1.033 | 0.322 | +0.711 |
| 3.0 | 0.841 | 0.358 | +0.483 |
| 10.0 | 1.262 | 1.256 | +0.006 |
| 30.0 | 4.359 | 4.359 | ~0 |

Same-spin >= opp-spin at all r ✓ Pauli vanishes at r > 30 sim

### p-p (N1 OPEP+core, l=0)

| r (sim) | r (fm) | V (MeV) |
|:--:|:--:|:--:|
| 0.5 | 2.65 | 1.6 |
| 1.0 | 5.29 | 2.73 |
| 2.0 | 10.6 | 4.01 |

---

## Centrifugal Coefficient

C_l = l(l+1) * 0.1333 sim_E * sim_L^2

Derived from GP vortex core: C_base = xi_e^2 * E_CORE_e = 114.7 * 0.001161 = 0.133

**Honest note**: Centrifugal coefficient is at nuclear (MeV) scale. Atomic orbital effects (eV scale) require an additional analytic centrifugal term in the sim code. The LUT centrifugal term has physical effect only for r < 5 sim.

---

## Sim Loading Guide

`gdscript
func get_potential(pair: String, l: int, r: float, same_spin: bool = true):
    var lut = load_lut(pair, l)
    if r < lut.r_max:
        return lut.interpolate(r, same_spin)
    else:
        return compute_vfm_log(r)
`

---

## Honest Assessment

**Strengths**:
- All three pair types * three orbitals = 9 combinations
- G_EM=2.00 unified -> physical consistency
- ee spin-dependent Pauli: same-spin >= opp-spin for all r
- Force derivatives pre-computed
- 500 sim covers nuclear to atomic scales

**Limitations**:
- Centrifugal at nuclear scale; atomic orbitals need analytic term
- Spherically symmetric -> bond directionality needs superposition
- Static potential -> no dynamic polarization
- pp hard core capped at r < 0.5 sim

---

*E3 v2.0 completed: 2026-07-24*
*Scaling is not the issue — alpha emerges from the sim, it is not put in by hand.*
