# Madelung Lattice Energy: Derived from α

**Source**: `Chemical_Bonds/02_Madelung_Lattice_Energy_SCVC_Calculation_Results.md`

---

## Core Conclusion

$$\boxed{U(\text{NaCl}) = -753.4\ \text{kJ/mol} \quad (\text{Experiment: } -786, -4.1\%)}$$

## Born-Landé Formula (SCVC-Parameterized)

$$U = -\frac{N_A \cdot M \cdot Z^+Z^- \cdot \alpha\hbar c}{R_0} \cdot \left(1 - \frac{1}{n}\right)$$

| Parameter | NaCl Value | Source |
|:---|:---:|:---|
| M | 1.747565 | **Pure geometry** (NaCl structure series) |
| αℏc | 1.439964 MeV·fm | **SCVC geometry** (α⁻¹=4π³+π²+π) |
| R₀ | 2.82 Å | Experiment (X-ray) |
| n | 8 | Born exponent |

## Full Alkali Halide Verification (12 compounds)

| Compound | U_SCVC | U_exp | Deviation |
|:---|:--:|:--:|:--:|
| LiF | −1035 | −1036 | 0.1% |
| NaF | −920 | −923 | 0.4% |
| KF | −808 | −821 | 1.5% |
| NaCl | −753 | −786 | 4.2% |
| NaBr | −719 | −751 | 4.3% |
| NaI | −668 | −699 | 4.4% |
| ... | ... | ... | ~3-5% |

**Average deviation: 3.1%** ✅

## SCVC Contribution

e²/4πε₀ = αℏc. α derived from toric geometry → Coulomb force strength is a geometric output. Madelung constant M=1.747565 is pure mathematics (series summation). Lattice energy leaves only R₀ and n as empirical parameters.
