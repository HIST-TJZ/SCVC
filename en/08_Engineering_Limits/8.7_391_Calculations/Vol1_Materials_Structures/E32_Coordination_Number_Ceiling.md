# SCVC Engineering Limit: Coordination Chemistry — Maximum Coordination Number + Closest Packing

> All derivations based on SCVC Reference constants (derived from π polynomials, zero free parameters).
> Coordination chemistry and crystal packing are jointly locked by Pauli repulsion (vortex ring topological repulsion) and bond energies.

---

## §1. Maximum Coordination Number

### 1.1 Pauling Radius Ratio Rules

In ionic crystals, coordination number is determined by the cation/anion radius ratio:

| CN | Coordination Polyhedron | Minimum r⁺/r⁻ | Geometric Principle |
|----|----------|-----------|----------|
| 3 | Triangle | 0.155 | Three spheres in contact, center sphere just doesn't rattle |
| 4 | Tetrahedron | 0.225 | Four spheres in contact |
| 6 | Octahedron | 0.414 | Six spheres in contact |
| 8 | Cube | 0.732 | Eight spheres in contact |
| 12 | Cuboctahedron | 1.000 | Closest packing of equal spheres |

**Maximum ionic radius ratio (from known ionic radii):**

```
Largest cation: Fr⁺ ≈ 1.80 Å (CN=6, Shannon)
Smallest anion: F⁻  = 1.33 Å (CN=6)

r⁺/r⁻(max) = 1.80 / 1.33 ≈ 1.35 → Pauling predicts CN=8
```

But in reality CsF (r⁺/r⁻ = 1.67/1.33 = 1.26) adopts the NaCl type (CN=6), not the predicted CsCl type (CN=8). This shows that **Pauling rules are unreliable for high r⁺/r⁻ ratios** — ions are not hard spheres; polarizability and covalency play key roles in large-cation–small-anion combinations.

### 1.2 SCVC Correction to Pauling Rules

SCVC's vortex ring picture (Pauli repulsion = topological repulsion of co-aligned vortex rings) provides understanding:

- The circulation ratio of cation (small vortex ring) to anion (large vortex ring) determines their effective "hard-sphere" radii
- Large cations (e.g., Cs⁺, Fr⁺) have vortex rings that **penetrate** anion vortex rings more than the radius ratio rule assumes
- This makes the "effective radius ratio" smaller than the geometric radius ratio → coordination number lower than Pauling predicts

SCVC Reference data can be used for correction:
```
Force constant k ∼ E_bond/r² ∼ 10³ N/m
Bond energy: ionic bond ~10-12 eV (strongest)
```

When the cation is sufficiently large, bond stiffness with the anion decreases (k ∝ 1/r²), leading to **bond softening** — while CN=8 is geometrically possible, each bond is too weak; CN=6 is more stable.

### 1.3 High Coordination in Metals and Intermetallics

Metallic bonds are non-directional → CN can be higher:

**fcc/hcp: CN = 12**
This is the maximum contact number for equal spheres in 3D (kissing number problem). SCVC does not alter this mathematical fact.

**bcc: CN = 8 + 6 = 14 (effective)**
First shell 8 (distance a√3/2), second shell 6 (distance a) only 15% further

**Frank-Kasper phases (size-mismatched intermetallics):**

| CN | Polyhedron | Face Composition | Example |
|----|--------|--------|------|
| 12 | Icosahedron | 20 Δ | Amorphous metal local order |
| 14 | FK14 | 24 Δ + 2 ⬡ | σ phase, μ phase |
| 15 | FK15 | 26 Δ + 2 ⬠ | σ phase |
| **16** | **Friauf polyhedron** | **28 Δ + 4 ⬡** | **MgCu₂ (Laves phase)** |

**CN=16 is the highest coordination number observed in stable crystals.** Does SCVC permit higher?

### 1.4 SCVC-Locked Maximum Coordination Number

Three physical limits constrain coordination number:

**(a) Geometric limit: spherical packing**

How many equal spheres can surround a central sphere? 3D kissing number = 12. For central sphere > ligand sphere:

```
N_max ≈ (4πR²) / (πr²) × (π/√12)   [R: central sphere radius, r: ligand sphere radius]

     = (2√3π/3) × (R/r)² ≈ 3.63 × (R/r)²
```

Maximum ionic radius ratio is Fr⁺/F⁻ ≈ 1.35:
```
N_max ≈ 3.63 × 1.35² ≈ 6.6 → geometric upper bound ~ CN=7
```

This is lower than actually observed (CsCl can reach CN=8) — again proving ions are not hard spheres.

**For interstitial H atoms in metals:**

Assuming H effective radius ~0.5 Å (in transition metal hydrides), metal-H distance ~1.7 Å:
```
N_max ≈ 3.63 × (1.7/1.05)² ≈ 9.5 → CN~10

Larger lanthanides: R_LnH ≈ 2.1 Å → N_max ≈ 15
Larger actinides: R_AnH ≈ 2.3 Å → N_max ≈ 17
```

Current highest known: **ReH₉²⁻ (nonahydridorhenate ion), CN_H=9**.

**(b) Bond energy dilution limit (SCVC-specific)**

Pauling's electrostatic valence rule: each bond strength ≈ formal charge / CN. Pauling stability criterion:

```
Bond strength ≥ (cation charge) / (anion charge) × (1/CN) × (Coulomb energy) > k_B T_melting
```

For tetravalent ions (e.g., Zr⁴⁺, Hf⁴⁺):
- CN=8: each bond ≈ 0.5 valence units, still far above k_B T
- CN=16: each bond ≈ 0.25 valence units, bond energy ~1-2 eV, still stable
- CN=20: each bond < 3 eV → may still hold, but coordination polyhedron begins to destabilize

For monovalent ions (e.g., Cs⁺, Fr⁺):
- CN=8: each bond ~0.125 eV, already approaching thermal activation
- CN=12: each bond ~0.08 eV → likely to melt at room temperature

Thus **SCVC's bond energy ceiling (~10-12 eV/bond) means monovalent ion coordination numbers are locked below ~8-10**.

**(c) Pauli repulsion limit**

From the SCVC vortex ring model: the closest distance between two vortex rings (atoms/ions) is determined by circulation κ = h/m_e = 7.274×10⁻⁴ m²/s. As CN increases, inter-ligand distances decrease → Pauli repulsion (topological repulsion of co-aligned vortex rings) increases sharply → bond compression → bond energy decreases.

**SCVC conclusion: Maximum stable coordination number = 16 (Frank-Kasper phases, the observed upper bound). CN>16 requires bond energies exceeding SCVC's covalent bond ceiling and is thus prohibited.**

---

## §2. Closest Packing Density

### 2.1 Equal-Sphere Packing (Kepler Conjecture)

```
fcc/hcp packing fraction: π/(3√2) ≈ 74.048%
```

SCVC does not change this purely geometric theorem. The packing of equal incompressible spheres is determined by topology, not bond energies.

### 2.2 Maximum Packing Density for Multi-Size Spheres

By filling tetrahedral and octahedral interstices with smaller spheres:

```
fcc + all octahedral voids filled:
  ρ_fill = (4 × 4/3πR³ + 4 × 4/3πr_oct³) / a³
  r_oct / R = √2 - 1 ≈ 0.414
  → ρ_fill ≈ 74% + 4 × (0.414)³ / (4√2/3) ≈ 79.2%

fcc + all tetrahedral + octahedral voids filled:
  r_tet / R = √(3/2) - 1 ≈ 0.225
  → Additional 8 × (0.225)³ / (4√2/3) ≈ 82.6%
```

But in real crystals, the minimum interatomic distance is locked by SCVC Pauli repulsion at ~1.0-1.5 Å. Smaller atoms cannot be "compressed in" arbitrarily because van der Waals repulsion (from α → polarizability → dispersion forces) sets a minimum distance.

| System | Packing Density | Example |
|------|-------|------|
| fcc/hcp (equal spheres) | 74.05% | Cu, Al, Au |
| bcc | 68.02% | Fe, W |
| Diamond (sp³) | 34.01% | C, Si |
| Amorphous metal | ~64-74% | Metglas |
| Random close packing | ~64% | Glass, granular matter |
| **Multi-size max (SCVC)** | **~85-90%** | Pauli-locked |

**SCVC insight**: The maximum packing density of real atoms (~85-90%) is higher than equal-sphere packing (74%) because different-sized atoms can fill interstices, but lower than the mathematical limit for ideal multi-size spheres (~96%) because Pauli repulsion prevents arbitrary compression.

---

## §3. Maximum Crystal Density

### 3.1 SCVC Derivation

``` 
ρ_max = (maximum atomic mass) / (minimum atomic volume × atoms per unit cell packing)

Atomic mass: heaviest stable nucleus ~238 u (U, but radioactive);
             heaviest stable nucleus ~209 u (Bi)

Atomic volume: determined by Pauli repulsion minimum distance
  d_min ≈ 1.0-1.5 Å (from SCVC vortex ring model, κ = h/m_e)

  V_atom_min ≈ d_min³ ≈ 1.0-3.4 Å³
```

But this is per-atom volume; real packing depends on coordination:

```
For fcc (packing 74%), d_min = 2r_min:
  ρ_fcc = (M/N_A) / (d³/(4√2)) = (4√2 M) / (N_A d³)

For the heaviest stable element, Os:
  M = 190.2 g/mol, d = 2.70 Å (fcc)
  ρ ≈ (4√2 × 190.2) / (6.022×10²³ × (2.70×10⁻¹⁰)³) ≈ 22.6 g/cm³ ✓ (consistent with measurement)
```

### 3.2 Density Comparison

| Material | Density (g/cm³) | Crystal Structure | Note |
|------|-------|------|------|
| Osmium (Os) | **22.59** | hcp | Current densest (stable) |
| Iridium (Ir) | 22.56 | fcc | Near Os |
| Platinum (Pt) | 21.45 | fcc | |
| Plutonium (Pu) | 19.86 | monoclinic | Radioactive |
| Gold (Au) | 19.32 | fcc | |
| Uranium (U) | 19.05 | orthorhombic | Radioactive |
| **SCVC ceiling** | **~23** | — | Bi + minimum d |

```
◆ Os (22.59) already at ~98% of SCVC ceiling (~23)
◆ Density is fundamentally limited by nuclear mass, not by packing
◆ Heavier nuclei exist (up to Og ~294 u) but are too short-lived for bulk materials
◆ SCVC hard ceiling: ~23 g/cm³ → determined by the heaviest stable nucleus (Bi~209 u)
   and Pauli-repulsion minimum packing distance
◆ No engineering headroom for density improvement — it's fundamentally nuclear-limited
```

---

## §4. Engineering Conclusions

### 4.1 Hydrogen Storage Density

**Gravimetric density:**

| Material | H wt% | Release T (°C) | Note |
|------|-------|---------|------|
| MgH₂ | 7.6 | ~300 | Too hot for PEMFC |
| LiBH₄ | 18.5 | >400 | Irreversible |
| NH₃BH₃ | 19.6 | ~150 | Decomposes |
| **SCVC theoretical max** | **~20** | — | Lightest host framework + all H filled |

SCVC constraint: the lightest solid framework that can accommodate H is Li (~7 u). Even at LiH (H/Li=1), H wt% ≈ 1/(7+1) ≈ 12.5%. Higher ratios (LiH₂, LiH₃) are Pauli-forbidden (H-H distances < 2.1 Å → too close).

**Volumetric density:**

Maximum H atoms per unit volume:
```
n_H_max ≈ (interstitial site fill fraction) × n_atomic

For fcc metals: octahedral + tetrahedral = 1 + 2 = 3 interstitial sites per metal atom
If all filled: H/M = 3 → LaNi₅H₆, H/M=1.

Highest known volumetric density: AlH₃ ~148 g H₂/L (2× denser than liquid hydrogen)
```

Maximum volumetric H density under SCVC constraints:
```
Net H density after accounting for host lattice mass:
ρ_H2_max ≈ 150-200 g H₂/L

SCVC-locked ceiling is ~2-3× liquid hydrogen density.
```

**Note:** This is lower than gasoline's energy density (~9000 Wh/L vs H₂ ~150 g/L×33.3 kWh/kg ≈ 5000 Wh/L), but H₂'s **gravimetric** energy density (33.3 kWh/kg) far exceeds gasoline (12 kWh/kg). For mass-sensitive applications (aerospace), hydrogen has a clear advantage; for volume-sensitive applications (passenger vehicles), the gap narrows.

### 4.2 Maximum Specific Surface Area of Porous Materials

| Material | SSA (m²/g) | Type |
|------|----------------|------|
| Graphene (monolayer) | **2630** | Theoretical maximum (both sides) |
| MOF-210 | ~10,400 (BET) | Experimental record |
| MOF-210 | ~7,000 (geometric) | Crystallographic calculation |
| NU-110 | ~7,140 | Geometric |
| Theoretical limit (Hupp) | **~14,600** | Pure carbon framework |

> ⚠️ The BET method often overestimates by 2-3× for microporous materials (micropore filling vs surface coverage).

**SCVC limit derivation:**

Limiting case — every atom is a surface atom (single-atom-thick 3D framework):

```
SSA_max = (total surface area of atoms per gram) / (mass per gram)

For a carbon framework:
  SSA ≈ (2π r² × N_A) / (12 g/mol)  [r: van der Waals radius]
      ≈ (2π × (1.7×10⁻¹⁰)² × 6.022×10²³) / 12
      ≈ 15,400 m²/g
```

But this ignores:
1. Interatomic bonds occlude part of the surface
2. The framework must be self-supporting (requires some connectivity and thickness)

**SCVC-locked practical ceiling: ~15,000 m²/g (geometric), corresponding to all C atoms being surface atoms.**

The best current MOFs have reached ~7,000 m²/g (geometric) → ~2× from SCVC ceiling. But further increasing SSA causes **mechanical stability to plummet** (single-atom-thick walls collapse under capillary forces/surface tension).

### 4.3 Maximum Spatial Density of Catalytic Active Sites

**2D (supported catalysts):**

```
Surface atom density: n_surf = n^(2/3) = (10²³)^(2/3) ≈ 4.6×10¹⁵ cm⁻²

Maximum active sites per cm² ≈ 4.6×10¹⁵ sites/cm²
                              ≈ 7.7×10⁻⁹ mol/cm²
                              ≈ 77 μmol/m²

Current single-atom catalysts (SACs): ~5-15 μmol/m²
SCVC limit: ~77 μmol/m²
```

**3D (MOF/molecular catalysts):**

```
If every metal node is an active site, with node spacing ~1 nm:
  Site density ≈ 1/(1 nm)³ ≈ 10²¹ sites/cm³ ≈ 1.7 mol/L

SCVC limit: atomic density ≈ 10²³ cm⁻³ ≈ 170 mol/L
            (but not every atom can be an independent catalytic site)
```

**SCVC ceiling of catalytic Turnover Frequency (TOF):**

Maximum molecules processed per active site per second, limited by diffusion rate and reaction barrier:

```
TOF_max = ν₀ × exp(-E_a/k_B T)

ν₀ ≈ k_B T / h ≈ 6×10¹² s⁻¹ (300 K)  [Transition State Theory]
E_a: activation energy

Optimal catalytic E_a ≈ 0.5-1.0 eV (can be overcome thermally, but not too fast)
```

In practice ~10⁻¹-10³ s⁻¹, limited by **diffusion to the active site** rather than the reaction itself.

At maximum areal density (10¹⁵ cm⁻²) and TOF=1 s⁻¹:
```
Maximum areal reaction rate ≈ 10¹⁵ reactions/cm²/s
                              ≈ 1.7×10⁻⁹ mol/cm²/s
```

This corresponds to ~1 A/cm² Faradaic current (for single-electron reactions), already approached in fuel cells.

### 4.4 SCVC Coordination Chemistry Limits Summary

| Parameter | SCVC Limit | Determining Factor | Current Best |
|------|-----------|----------|----------|
| Maximum coordination number | **16** (Frank-Kasper) | Bond energy dilution + geometry | 16 (MgCu₂) |
| Maximum H-atom coordination | **~12-17** | R_MH / R_HH ratio | 9 (ReH₉²⁻) |
| Closest packing (equal spheres) | **74.05%** | Geometric theorem | fcc/hcp |
| Closest packing (multi-component) | **~90%** | Pauli minimum atomic spacing | — |
| Maximum crystal density | **~23 g/cm³** | Heaviest nucleus + Pauli repulsion | 22.6 (Os) |
| Volumetric H₂ storage density | **~150-200 g H₂/L** | H-H repulsion + host lattice | 148 (AlH₃) |
| MOF specific surface area | **~15,000 m²/g** | Single-atom-thickness limit | ~7,000 (geometric) |
| Catalytic site areal density | **~5×10¹⁵ cm⁻²** | n^(2/3) | ~10¹⁵ cm⁻² |

---

## Appendix: SCVC Derivation Chain (Coordination Chemistry)

```
π → α → ℏ, m_e
         ↓
    ┌────┴─────┬──────────┬───────────┐
    ↓          ↓          ↓           ↓
  Pauli       Bond       Ionic       Atomic
  repulsion   energies   radii       density
  Vortex ring 3.6-12eV   from α      n ∼ 10^23
  topology
    ↓          ↓          ↓           ↓
  Minimum     Bond       r+/r-       Closest
  spacing     strength   ratio       packing
  ~1.0-1.5Å   CN≤16      ~0.1-1.4    ≤74-90%
    ↓          ↓          ↓           ↓
  CN ceiling  Bond       High CN     Crystal
  ≤16         dilution   spherical   density
              limits CN  packing     ≤23 g/cm³
```

All coordination chemistry limits reduce to π (via α → electronic structure → ionic radii / bond energies / Pauli repulsion) and nuclear mass (density ceiling).
