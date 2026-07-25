# Atmospheric Optics: Blue Sky, Red Sunset + Stellar Mass Window → SCVC Complete Derivation

**Status**: 🟢 85% (Blue sky 🟢; stellar window 🟡)

---

# Part 1: Why the Sky Is Blue

## 1. Rayleigh Scattering → λ⁻⁴

Scattering cross-section (dipole radiation, particle << wavelength):
\[
\sigma_R = \frac{8\pi^3}{3}\frac{(n^2-1)^2}{N^2\lambda^4}
\]

Blue light 450 nm vs. red 700 nm: σ_blue/σ_red = (700/450)⁴ = **5.86**.

## 2. n−1 → Molecular Polarizability → α

(n²−1) ∝ N·α_pol. N₂ polarizability ≈ 1.74×10⁻³⁰ m³ → from N≡N triple bond electron cloud → molecular orbitals → binding energy ∝ α²·Ry.

**Key**: N ∝ 1/molecular volume ∝ 1/a₀³ ∝ α³. α_pol ∝ electron orbital volume ∝ a₀³ ∝ 1/α³. → **α-factors in (n²−1) cancel.** Isomorphic to the rainbow 42° case. ✅

## 3. Why Blue, Not Violet

- Rayleigh σ ∝ λ⁻⁴ → violet (400 nm) > blue (450 nm) → 1.6×
- Solar Planck spectrum: 400 nm ≈ 0.6× intensity at 450 nm
- Human eye V(λ): 400 nm ≈ 0.004× sensitivity at 450 nm
- Combined: blue (470 nm) peak → **pure blue**. ✅

## 4. Red Sunset

Horizon → air mass ~40× zenith. τ_blue ≈ 20 → attenuation e⁻²⁰ ≈ 2×10⁻⁹. τ_red = 20×(450/700)⁴ ≈ 3.5 → 3% still reaches us → red sunset.

## 5. Martian Sky Reversal — Verified

Mars atmosphere thin (6 mbar) → Rayleigh weak. Dust Mie scattering dominates → orange-red by day, **blue sunset**. Photographed by Curiosity ✅.

---

# Part 2: Stellar Mass Window [0.08, 300] M_⊙

## 6. Lower Bound: Hydrogen Ignition

p-p chain requires T_c > 3×10⁶ K (Gamow penetration of Coulomb barrier):
\[
\text{Gamow} \propto \exp\left(-\sqrt{\frac{E_G}{E_{\text{cm}}}}\right)
\]

E_G = 2m_r(πα)² ≈ 247 keV (two protons). T_c = 3×10⁶ K → E_cm ≈ 0.4 keV → Gamow ≈ 1.5×10⁻¹¹.

Solar core power density only 276 W/m³ → needs huge volume → M > 0.08 M_⊙.

**α sensitivity**: α 1% larger → E_G 2% larger → Gamow factor ~25% smaller → M_min larger → fewer stars.

## 7. Upper Bound: Eddington Limit

L_Edd = 4πGMc/κ. κ ∝ α² (Thomson scattering). L ∝ M^3.5. → M_max ∝ 1/α².

R136a1 ~ 265 M_⊙ → already near ceiling.

## 8. Stellar Mass Window = α Fingerprint

```
[0.08, 300] M_⊙ = α-defined hydrogen burning range
  ├─ M_min ← Gamow ∝ exp(−1/α)
  └─ M_max ← κ ∝ α²
```

---

## 9. Honest Assessment

| | Status |
|---|---|
| Rayleigh λ⁻⁴ | 🟢 Classical electromagnetism |
| α-cancellation in n−1 | 🟢 Geometric constant |
| Blue sky (not violet) | 🟢 Spectrum + cone cells |
| M_min ∝ exp(−1/α) | 🟡 Scaling correct |
| M_max ∝ 1/α² | 🟡 Scaling correct |
| IMF slope | 🔴 Turbulent fragmentation |

**Falsifiable**: <0.07 M_⊙ hydrogen-burning star → SCVC dead.

---

## 10. Key Formulas

```
σ_R ∝ 1/λ⁴, σ_blue/σ_red = 5.86
n²−1 ∝ N·α_pol → α³×α⁻³ = constant
M_min ≈ 0.08 M_⊙ (Gamow ∝ exp(−1/α))
M_max ≈ 200-300 M_⊙ (κ ∝ α²)
```