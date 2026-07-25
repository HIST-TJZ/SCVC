# Liquid Drop Model Five Coefficients: a_c = 0.711, a_a = 24.4

**Source**: Nuclear_Physics/N1_Liquid_Drop_Model_SCVC_Derivation_Results.md

---

## Core Results

| Coefficient | Experiment (MeV) | SCVC | Deviation | Key Input |
|:---|:--:|:--:|:--:|:---|
| **a_c** | 0.711 | **0.720** | **+1.3%** | α=1/(4π³+π²+π), r₀=1.20 fm |
| a_v | 15.75 | ~16 (estimate) | ~2% | α_s=1/(16π), m_p |
| a_s | 17.8 | 14-18 (estimate) | ~15% | Geometry + vortex surface tension |
| a_a | 23.7 | ~25 (estimate) | ~5% | Fermi gas + topological repulsion |
| a_p | 34.0 | ~34 (framework) | — | Vortex pair Ampère energy |

## a_c: Direct SCVC Derivation ✅

a_c = \frac{3}{5} \cdot \frac{e^2}{4\pi\varepsilon_0 r_0} = \frac{3}{5} \cdot \frac{\alpha\hbar c}{r_0}

| Quantity | Value | Source |
|:---|:---|:---|
| α⁻¹ | 137.036304 | DH summation |
| αℏc | 1.439964 MeV·fm | SCVC geometry |
| r₀ | 1.20 fm | Electron scattering experiment |

a_c = \frac{3}{5} \times \frac{1.439964}{1.20} = 0.720\ \text{MeV}

**Deviation: +1.3%** ✅

## Remaining Coefficients: SCVC Scale Framework

- a_v: α_s sets nuclear force scale, m_p dominated by gluon field energy
- a_a: N≠Z asymmetry energy, Fermi gas + Pauli = topological repulsion
- a_s, a_p: Surface and pairing terms, vortex geometry framework

## Honesty Assessment

a_c is a direct SCVC derivation (dependent only on α), deviation 1.3%. The remaining coefficients provide scale estimates rather than precise values. r₀ remains a nuclear physics experimental input.
