# Vortex Core Energy: GP Equation → E_CORE = 2.1322

**Confidence**: 95% (GP equation numerical solution)
**Source**: SCVC_See_I/E_CORE_DERIVATION.md
**Nature**: Dynamical derivation (non-geometric GKM/DH)

---

## Core Conclusion

$$\boxed{E_{\text{CORE}} = 2.1322 \quad \text{(GP natural units)}}$$

This is the self-energy of a single n=1 vortex in BEC — forward numerical solution from the Gross-Pitaevskii equation.

## Derivation

### GP Equation

SCVC vacuum = F=1 spinor BEC. The vortex radial order parameter f(r) satisfies the dimensionless GP equation:

$$f'' + \frac{f''}{r} - \frac{f}{r^2} + f - f^3 = 0$$

Boundary conditions:
- f(0) = 0 (vortex core: order parameter vanishes)
- f(∞) = 1 (far from core: recovers ground state)

### Shooting Method Solution

Only free parameter c₁ = f''(0). Determined by shooting:

c₁ = 0.5831869855
ξ_eff = 1.3176 (f(ξ) ≈ 0.632, healing length)

### Vortex Energy Functional

GP free energy (per unit length) for n=1 vortex ψ(r,θ) = f(r)·e^(iθ):

$$E_{\text{vortex}} = 2\pi \int_0^\infty r\,dr \left[ \frac{1}{2}(f'')^2 + \frac{f^2}{2r^2} + \frac{1}{4}(1-f^2)^2 \right]$$

| Term | Physical Meaning | Fraction |
|:---|:---|:--:|
| ½(f′)² | Gradient energy of order parameter across core | 25.2% |
| f²/(2r²) | Kinetic energy of superfluid circulation ~1/r | 35.9% |
| ¼(1−f²)² | Potential cost of deviating from ground state |ψ|=1 | 38.9% |

### Core vs Tail Separation

Centrifugal term at large r: f²/(2r²) → 1/(2r²), integral → π·log(R_max/R_min) — logarithmic divergence.

**This is the classical log divergence of 2D vortices, representing long-range vortex-vortex interaction.** The pairwise term G·(wᵢ·wⱼ)·log(1+r²/ξ²) in simulations already captures this. Hence E_CORE takes only the r<ξ core region.

## Numerical Verification

Independently reproducible. Run SCVC_See_I/python_backend/run_all.py to generate vortex_profile.json, then verify:

Numerical result: E_CORE = 2.1322
Gradient term: 0.5364 (25.2%)
Centrifugal term: 0.7664 (35.9%)
Potential term: 0.8294 (38.9%)

Three terms comparable magnitude — consistent with well-defined vortex core.

## Physical Meaning

E_CORE is the "existence cost" of a particle in SCVC — every vortex (= every particle) has this fundamental self-energy. Multiplied by mass factor mf² and gauge coupling |w|², it gives the self-energy scale for different particles.

**In GP natural units:**
- Electron core energy ≈ 1.07 (mf=1.0, |w|²=0.50)
- u quark core energy ≈ 49.1 (mf=4.24, |w|²=1.28)
- d quark core energy ≈ 227.5 (mf=9.13, |w|²=1.28)

**u/d core energy ratio = 4.63:1** — directly from SCVC π-polynomial mass factor ratio (mf_d/mf_u)² = (9.13/4.24)² ≈ 4.63.

## Honest Assessment

| Claim | Status |
|:---|:--:|
| GP equation is standard vortex description | ✅ Standard condensed matter physics |
| c₁=0.5832 is unique GP solution | ✅ Numerical shooting verified |
| E_CORE=2.1322 | ✅ Independently reproducible |
| Core vs tail separation (r<ξ) | ✅ Physically well-motivated |
| E_CORE connects to particle mass? | 🟡 Scaling correct, absolute units TBD |

E_CORE does not directly equal nuclear force or binding energy. It is single-particle self-energy. But correct derivation of E_CORE ensures each particle''s "baseline energy" in simulation is physical — not hand-tuned.
