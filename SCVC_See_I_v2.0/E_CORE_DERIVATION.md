# SCVC E_CORE Derivation: Vortex Core Energy from GP Functional

## Summary

**E_CORE = 2.1322** (dimensionless, in GP natural units)

This is the self-energy of a single n=1 vortex excitation, integrated
over the vortex core region (r < xi). The long-range logarithmic tail
is excluded because it is already captured by the pairwise
`log(1 + r^2/xi^2)` interaction term in the simulation Hamiltonian.

## Method

### 1. Ginzburg-Pitaevskii (GP) Free Energy

The SCVC vortex profile is obtained by solving the dimensionless GP
ordinary differential equation (ODE) via a shooting method:

```
f'' + f'/r - f/r^2 + f - f^3 = 0
```

with boundary conditions:
- f(0) = 0          (vortex core: order parameter vanishes)
- f(r->inf) = 1     (bulk: order parameter saturates)

The shooting parameter c1 = f'(0) is determined by requiring
f(r) -> 1 as r -> infinity.

**Numerical result (from `run_all.py`):**
- c1 = 0.5831869855
- xi_eff = 1.3176   (healing length: f(xi_eff) ~ 0.632)

### 2. Vortex Energy Functional

For a single n=1 vortex psi(r,theta) = f(r) * exp(i*theta), the
dimensionless GP free energy per unit length is:

```
E_vortex = 2*pi * integral_0^inf  r dr *
           [ 1/2 * (f')^2  +  f^2/(2*r^2)  +  1/4 * (1 - f^2)^2 ]
            \___________/    \____________/    \_______________/
             gradient term    centrifugal term   potential term
```

Each term's physical meaning:
- **Gradient**: energy cost of order parameter variation across core
- **Centrifugal**: kinetic energy from superfluid circulation (~1/r^2)
- **Potential**: energy cost of order parameter deviating from |psi|=1

### 3. Separating Core vs Tail

The centrifugal term at large r behaves as:

```
f(r->inf) -> 1  =>  f^2/(2r^2) -> 1/(2r^2)
Integral: 2*pi * r * 1/(2r^2) * dr = pi * dr/r
=> diverges logarithmically as pi * log(R_max / R_min)
```

This is the well-known **2D vortex logarithmic divergence**.
It represents the long-range interaction between vortices, NOT the
local core energy.

In the simulation, the pairwise term `-G * (w_i.w_j) * log(1 + r^2/xi^2)`
already captures this interaction. Therefore E_CORE should only
include the **short-range core contribution** (r < xi).

### 4. Numerical Integration

Input data: `data/vortex_profile.json` (256 radial points, r_max = 8.0)

| Cutoff | E (core) | Notes |
|--------|----------|-------|
| r < 1.00*xi | **2.1322** | Cleanest definition: everything within one healing length |
| r < 1.50*xi | 3.3773 | Includes some tail contamination |
| r < 2.00*xi | 4.2960 | Significant tail mixing |
| r < 8.00 (all) | 7.7411 | Full energy including log-divergent tail |

**Integrand breakdown at cutoff r < xi:**

| Term | Value | Fraction |
|------|-------|----------|
| Gradient | 0.5364 | 25.2% |
| Centrifugal | 0.7664 | 35.9% |
| Potential | 0.8294 | 38.9% |
| **Total** | **2.1322** | 100% |

### 5. Mapping to Simulation

In the simulation Hamiltonian:
```
H = sum_i  E_CORE * mf_i^2 * |w_i|^2
  - sum_{i<j} G_{ij} * (w_i . w_j) * log(1 + r_{ij}^2 / xi^2)
```

E_CORE is the **dimensionless** vortex core energy. It does NOT
require length/energy scaling (L0*S) because it is already in the
natural units of the GP theory, where the energy scale is set by
the coupling constants G_STRONG and G_EM.

**E_CORE_sim = E_CORE_phys = 2.1322**

(Previous value was 1.5, off by factor 1.42)

### 6. Per-Particle Core Energies

Using E_CORE = 2.13, mass_factors from SCVC pi-polynomials,
and |w|^2 = wc1^2 + wc2^2 + ww^2 + wy^2:

| Particle | mf | |w|^2 | Core Energy |
|----------|-----|------|-------------|
| electron | 1.00 | 0.50 | 1.07 |
| u quark | 4.24 | 1.28 | 49.1 |
| d quark | 9.13 | 1.28 | 227.5 |
| neutrino | 0.01 | 0.50 | ~0 |
| top quark | 339840 | 1.28 | 8.9e11 |

## Verification

To reproduce this result:
```bash
cd python_backend
python run_all.py    # generates data/vortex_profile.json
```

Then run the integration (Python):
```python
import json, numpy as np
with open('data/vortex_profile.json') as f:
    data = json.load(f)
r = np.array(data['profile_r'])
f = np.array(data['profile_psi'])
xi = data['xi_effective']
c1 = data['c1']
dr = r[1] - r[0]
fp = np.zeros_like(f)
fp[1:-1] = (f[2:] - f[:-2]) / (2*dr)
fp[0] = (f[1]-f[0])/dr; fp[-1] = (f[-1]-f[-2])/dr
with np.errstate(divide='ignore', invalid='ignore'):
    f_or = np.where(r > 1e-10, f/r, c1)
integrand = 2*np.pi*r * (0.5*fp**2 + 0.5*f_or**2 + 0.25*(1-f**2)**2)
E_core = np.trapz(integrand[r <= xi], r[r <= xi])
print(f'E_CORE = {E_core:.4f}')
```

Expected output: `E_CORE = 2.1322`
