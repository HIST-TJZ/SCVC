# V3.0 Calculation Scripts Reference

**14 Python verification scripts. All independently runnable, for reproducing SCVC numerical values.**

---

## Core Verification (Run First)

| Script | Purpose | Key Output |
|:---|:---|:---|
| dh_sum_verify.py | DH summation ? $\alpha^{-1}$ | .036304$ (2.22 ppm) |
| lpha_s_3loop.py | 3-loop RG ? $\alpha_s(M_Z)$ | .11846$ (+0.30%) |
| casimir_mvac.py | Casimir coefficient + $ | {cas}=0.24491$, =0.4775$ |
| mpl_fixedpoints.py | {Pl}$ 6-fixed-point equivariant volume sum | .35\times 10^{18}$ ($-3.5\%$) |
| lambda4_seesaw.py | $\Lambda_4$ Seesaw pathway | .41$ meV (+0.5%) |

## RG Running

| Script | Purpose |
|:---|:---|
| 
g_step1.py | Coupling constant RG running step 1 |
| 
g_step2.py | Coupling constant RG running step 2 |
| 
g_step3.py | Coupling constant RG running step 3 |
| compute_kk.py | KK scale calculation |

## Auxiliary Verification

| Script | Purpose |
|:---|:---|
| ortex_profile_cp2.py | Vortex CP? profile |
| 33_C_total_verification_script.py | {total}$ Three-Pathway Verification |
| ???_s_verify.py | $\rho_s$ Independent Verification |
| ix_merge.py | Auxiliary Script |
| _compute_strengthened.py | Auxiliary Computation |

---

## Important Corrections

- **mpl_fixedpoints.py**: Confirms $\eta=609$ (enhancement factor determined by {vac}$ to ^2$ volume ratio)
- **lambda4_seesaw.py**: Uses \nu \approx 0.02$ eV (single neutrino seesaw scale), NOT $\Sigma m_\nu = 0.059$ eV.

---

## Runtime Requirements

Python 3.8+, standard scientific computing libraries (
umpy, scipy). No GPU needed. Each script independent, runtime < 1 minute.
