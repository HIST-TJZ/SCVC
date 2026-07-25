# SCVC v2.0 Calculation Scripts

This directory contains Python scripts for verifying key numerical results of SCVC theory.

## Independent Verification Scripts (v5 Audit, 2026-07-23)

Written from scratch by independent AI, referencing no existing code, reading only SCVC document formulas.

| Script | Verification Item | Result | Deviation |
|:---|:---|:--:|:--:|
| `alpha_s_3loop.py` | α_s(M_Z) 3-loop RG | 0.11845 | +0.30% |
| `dh_sum_verify.py` | α⁻¹ DH summation | 137.036304 | 2.22 ppm |
| `casimir_mvac.py` | C_cas + K | 0.2449 / 0.4775 | Algebraically exact |
| `mpl_fixedpoints.py` | M_Pl 6 fixed points | 2.433×10¹⁸ GeV | −0.10% |
| `lambda4_seesaw.py` | Λ₄ dual path | 2.41/2.24×10⁻³ eV | +0.43%/−6.5% |

Audit report: `../10_Audit_Verification/Independent_Verification_Report_5_Scripts.md`

## Early Calculation Scripts

| Script | Function | Corresponding Document |
|:---|:---|:---|
| `compute_kk.py` | Four-coupling RG running → M_KK lock | `Gauge/M_KK_Precise_Lock.md` |
| `rg_step1/2/3.py` | RG running stepwise implementation | Same as above |
| `33_C_total_verification_script.py` | C_total=1 verification | `Postulate/C_total_Three_Path_Closure.md` |
| `_compute_strengthened.py` | Nuclear physics calculations | `Nuclear_Physics/Liquid_Drop_Model_Five_Coefficients.md` |
| `vortex_profile_cp2.py` | Vortex CP² profile | `Gauge/K1_KK_Reduction_Triple_Closure.md` |
| `reverse_rho_s_verify.py` | BEC density verification | `Postulate/P8_Higgs_Vortex_Cooper_Pair.md` |
| `fix_merge.py` | Data merge fix | — |

## Runtime Instructions

All scripts are Python 3, dependencies limited to numpy/scipy.
Runs on ordinary laptop, total runtime <5 minutes.
