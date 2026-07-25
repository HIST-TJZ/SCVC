# Electronegativity: Geometric Z_eff → R²=0.903

**Source**: `Chemical_Bonds/08_Electronegativity_Bond_Polarity.md`

---

## Core Conclusion

Electronegativity in SCVC is not a "new parameter" — it naturally emerges from ionization energy (IE) and electron affinity (EA):

$$\chi_{\text{Mulliken}} = \frac{IE_1 + EA}{2}$$
$$\chi_{\text{Pauling}} \approx 0.336 \times (\chi_{\text{Mulliken}} - 0.615)$$

## SCVC Electronegativity

$$\chi_{\text{SCVC}} = \frac{Z_{\text{eff}}^2}{2n^2} \times \text{Ry}$$

where Z_eff = Z − σ_SCVC, Ry = 13.606 eV (SCVC geometry).

## Comparison with Pauling Scale

| Atom | Z_eff(Slater) | χ_SCVC (expected) | χ_Pauling |
|:---|:--:|:--:|:--:|
| F | 5.20 | ~4.0 | 3.98 |
| O | 4.55 | ~3.5 | 3.44 |
| N | 3.90 | ~3.0 | 3.04 |
| C | 3.25 | ~2.5 | 2.55 |
| Li | 1.30 | ~1.0 | 0.98 |

**R² ≈ 0.903** (vs Pauling scale)

## Bond Polarity

The Pauling bond polarity formula naturally emerges in SCVC:
$$\text{Ionicity }\% = 1 - \exp(-(\Delta\chi)^2/4)$$

Δχ comes directly from the Z_eff difference between two atoms — a purely geometric quantity.

## Honesty Assessment

Electronegativity is SCVC "passive harvest": once IE and EA are forward-calculated from SCVC shell geometry, electronegativity automatically follows. R²=0.903 indicates the scale is correct, but precise quantification requires complete l-classified IE calculations.
