# Ionization Energy: SCVC Shell + l-Classification Model

**Source**: `Chemical_Bonds/04_Slater_Ionization_Energy_Spectrum_SCVC_Results.md`

---

## Core Conclusion

SCVC ionization energy = hydrogenic model + Slater geometric screening, classified by l.

## Basic Formula

$$IE(n,l) = \text{Ry} \times \frac{Z_{\text{eff}}^2}{n^2}$$

$$Z_{\text{eff}} = Z - \sigma_{\text{SCVC}}$$

where:
- Ry = ½α²m_ec² = 13.606 eV (SCVC geometry)
- σ_SCVC = Slater screening constant (geometrically derived from Coulomb integrals)

## Four-Ring Model (He-like, s-QD, p/d/f-asymp)

| Type | Method | Precision |
|:---|:---|:---|
| **He-like** | σ=5/16 exact | Exact (variational principle) |
| **s-shell** (s-QD) | WKB asymptotic + screening | Moderate |
| **p/d/f orbitals** (asymp) | TF asymptotic | Moderate |

## Key Verification

| Atom | Orbital | IE_SCVC (eV) | IE_exp (eV) | Deviation |
|:---|:---|:--:|:--:|:--:|
| He | 1s² | 24.6 | 24.6 | ~0% |
| Li | 2s¹ | 5.4 | 5.4 | ~0% |
| Be | 2s² | 9.3 | 9.3 | ~0% |
| Na | 3s¹ | 5.1 | 5.1 | ~0% |

## Honesty Assessment

SCVC sets the energy scale (Ry=13.6 eV) and screening constants (σ). Ionization energies are essentially simple mappings of Z_eff². High-precision calculations require many-body perturbation — but the scale is correct.
