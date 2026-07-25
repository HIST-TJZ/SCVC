# E254: Fluid Mechanics Five-Domain Ceilings — SCVC Geometric Locking

**Status**: 🟡 65% (geometric optimization framework naturally fits SCVC; specific values partially locked)

---

## I. Minimum Drag Shape and Strouhal Vortex Shedding

### St ≈ 0.2: Why 0.2?
St = fD/U ≈ 0.21 for 300 < Re < 10⁵. Extremely robust across 3 orders of Re.
Origin: von Kármán vortex street stability — the spacing ratio h/l ≈ 0.281 is the unique linearly stable value. St ≈ 0.2 is a **pure geometric number** from vortex array stability conditions — independent of viscosity, density, or any material parameter.

SCVC: St ≈ 0.2 is the same for all fluids past the same obstacle — **vortex arrangement is a topological constraint, not a material property.** ✅

SCVC locks: Re_crit ≈ 47 (onset of vortex shedding). Re_crit = UD/ν. ν → molecular collisions → bond energy → α. SCVC: any fluid's critical Re for vortex shedding = f(ν), and ν→α.

### Minimum Drag Floor
Laminar skin friction: C_f = 1.328/√Re_L. For L=1m, U=10m/s, water: C_f ≈ 4.2×10⁻⁴. Streamlined C_D_min ≈ 0.0005.

SCVC lock: C_D_min ∝ 1/√Re = √(ν/UL). ν→α. Minimum drag ratio between fluids = √(ν₁/ν₂).

---

## II. Rayleigh-Bénard Convection

### Ra_c = 1708: Geometric Eigenvalue
Lowest eigenvalue of ∇⁴w = Ra·∇²⊥θ under rigid boundaries. **Independent of fluid type** — water, air, mercury, helium all Ra_c=1708. Purely geometric.

SCVC insight: Ra_c has nothing to do with α — it comes from problem geometry (horizontal layer, rigid boundaries). Consistent with SCVC "all physical constants are geometry."

### Ultimate Regime Nu ∝ Ra^β
Nu_max ∼ L/λ_mfp (macro scale / molecular mean free path). For water (λ_mfp~3Å, L~0.1m): Nu_max ~ 3×10⁸. Experiment ~10⁴-10⁵ → still ~10³-10⁴× room.
**SCVC says**: Nu physical ceiling from molecular free path → a₀ → α.

---

## III. River Networks and Fractal Branching

### Horton Laws: Pure Geometric Emergence
Branching ratio R_b ≈ 4, length ratio R_l ≈ 2, area ratio R_a ≈ 4-5. **All natural river networks** — Mississippi, Amazon, backyard streams. Independent of climate, geology, vegetation.

SCVC insight: Horton laws = geometric inevitability of optimal transport networks. Minimizing total energy dissipation (flow friction + basin maintenance) naturally locks branching ratio ~4.

### Murray Law: r³ Sum
r_parent³ = r_child1³ + r_child2³. Why **cube**? Two competing costs: pumping work ∝ r⁻⁴, blood volume cost ∝ r². Minimizing sum → optimum at r³. Pure variational geometry.

---

## IV. Blood Flow — Womersley Number

α_Wo = R√(ω/ν). For human aorta: α_Wo ≈ 15-20 (pulsatile, plug-like profile). For arterioles: α_Wo ≪ 1 (quasi-steady Poiseuille).

SCVC: ν → molecular viscosity → α. Maximum heart rate (for α_Wo approach to steady limit) → ~200 bpm → near human maximum.

---

## V. Ocean Circulation — Thermohaline + Wind-Driven

Sverdrup balance: βV = curl(τ)/(ρ₀). Maximum transport ~150 Sv (Gulf Stream ~30-80 Sv + Antarctic Circumpolar ~130 Sv).
SCVC: β = df/dy (planetary vorticity gradient) — Earth rotation, not SCVC.

AMOC (meridional overturning): ~15-20 Sv. Stability threshold from freshwater forcing (hosing experiments: ~0.1-0.5 Sv freshwater → AMOC collapse).
SCVC lock: density difference Δρ ∝ thermal expansion ∝ α (anharmonicity of bonds).

---

## VI. Viscoelastic Damping

Kramers-Kronig constraint: ∫E"(ω)dω/ω = (π/2)ΔE. ΔE = relaxation strength bounded by total elastic modulus ∝ bond stiffness ∝ α.
**SCVC gives total energy budget ∝ α, but tanδ_max depends on molecular structure → 🔴 beyond pure geometry.**

---

## VII. Forest Fire Maximum Intensity

Byram fireline intensity: I_B = H·w·r.
- H (fuel heat): cellulose combustion ~15-18 MJ/kg → locked by α (bond energies) ✅
- w (fuel load): mature forest ~10-25 kg/m² dry → photosynthesis ceiling (α) ✅  
- r (spread rate): radiation-driven, T_flame ~1000-1500K → combustion chemistry → α

I_B,max ≈ 18×10⁶ × 25 × 10 ≈ **4.5×10⁶ kW/m**.
Observed max: ~3×10⁵ kW/m (Australia Black Saturday 2009). **Still 10× below SCVC ceiling** — Earth forests haven't hit the physical limit yet.

---

## Summary: 7-in-1

| Phenomenon | SCVC Ceiling | Observed Max | Gap | α Chain |
|:---|:---|:---|:--:|:---|
| Repose angle | 25-50° | 30-45° | At limit | Friction ∝ surface energy ∝ α |
| Mountain/landslide | h_max~8km | ~8.8km | At limit | Rock strength ∝ bond ∝ α |
| Solar flare | ~3×10³² erg | ~10³² erg | At limit | Photospheric P ∝ fusion ∝ α² |
| Traffic (human) | ~3600 v/h | ~2400 v/h | 1.5× | Reaction ∝ neural ∝ α |
| Adhesion energy | ~10 J/m² | ~10 J/m² | At limit | C-C bond ∝ orbital ∝ α² |
| Fire (I_B) | ~5×10⁶ kW/m | ~3×10⁵ kW/m | **10×** | Fuel heat ∝ bond ∝ α |
| Power grid (sync) | ~3000km | ~4000km(DC) | Crossed | c locks wave speed |

**Five of seven already hit α ceiling.** Fire has 10× room (no large enough continuous forest + sustained wind). Viscoelastic damping is the only 🔴 (molecular structure beyond geometry).
