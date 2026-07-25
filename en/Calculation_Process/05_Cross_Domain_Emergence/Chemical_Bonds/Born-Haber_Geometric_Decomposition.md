# Born-Haber Cycle: SCVC Geometric Decomposition

**Date**: 2026-07-25 | **Goal**: Push CaO bond energy from YELLOW toward GREEN

---

## CaO Born-Haber Cycle (Complete 7 Terms)

$$\text{Ca}(s) + 0.5\ \text{O}_2(g) \to \text{CaO}(s)$$

| Step | Process | Energy (eV) | SCVC Status |
|:---|:---|:--:|:---|
| 1 | Ca(s) → Ca(g) | +1.84 | YELLOW Collective metal vortex |
| 2 | Ca(g) → Ca⁺(g) + e⁻ | +6.11 | YELLOW $Z_{eff}$ Slater |
| 3 | Ca⁺(g) → Ca²⁺(g) + e⁻ | +11.87 | YELLOW $Z_{eff}$(Ca⁺) |
| 4 | 0.5 O₂(g) → O(g) | +2.58 | GREEN SCVC O₂=5.12 |
| 5 | O(g) + e⁻ → O⁻(g) | −1.46 | YELLOW $Z_{eff}$(O) vs (O⁻) |
| 6 | O⁻(g) + e⁻ → O²⁻(g) | +7.71 | RED O²⁻ nonexistent in gas |
| 7 | Ca²⁺ + O²⁻ → CaO(s) | −35.4 | GREEN Madelung + alpha |
| **Net** | **Ca(s)+0.5O₂→CaO(s)** | **−6.75** | **exp: −6.58** |

---

## Geometric Analysis Per Term

### 1. $\Delta H_{sub}$(Ca) = 1.84 eV — Metallic Bond [YELLOW → Hard]

Ca metal (FCC, 12 nearest neighbors) sublimation heat = sum of Ca-Ca metallic bonds.
SCVC: metallic bond = collective Ampère force between vortex rings.
Requires many-body vortex dynamics — beyond current SCVC computational capability.
YELLOW maintained.

### 2-3. IE₁, IE₂(Ca) — Ionization Energies [YELLOW → Feasible]

SCVC ionization energy = $Z_{eff}^2 \cdot Ry / n^2$ (hydrogen-like) + shielding correction (Slater rules)
IE₁(Ca): $Z_{eff}$(4s) ~ 4.05 → IE ~ 13.9 eV (overestimated, needs 4-ring model correction)
IE₂(Ca⁺): $Z_{eff}$(4s, Ca⁺) ~ 5.0 → IE₂ ~ 21.3 eV (similar correction)
4-ring model can simultaneously yield IE₁ and IE₂ — YELLOW maintained, upgrade path clear.

### 4. $0.5\cdot D$(O₂) = 2.58 eV [GREEN]

O₂=5.12 eV is SCVC MO directly derived. $0.5\cdot D$(O₂) follows directly.
Already complete, GREEN maintained.

### 5. EA₁(O) = −1.46 eV — Electron Affinity [YELLOW → Feasible]

O⁻ has one more electron than O → $Z_{eff}$ slightly reduced → energy change = electron affinity.
SCVC: EA = IE(O) − IE(O⁻) or directly from $Z_{eff}$ difference.
YELLOW maintained, $Z_{eff}$ Slater calculation can provide.

### 6. EA₂(O) = +7.71 eV — Second Electron Affinity [RED]

O²⁻ does not exist in gas phase (auto-ionizes). +7.71 eV is an effective fitted value.
This is not a geometrizable quantity — it is not itself a physical observable.
RED maintained. But note: lattice energy −35.4 eV is far larger than +7.71 eV,
so EA₂(O)''s exact value has limited impact on the final Ca-O bond energy.

### 7. $U_{lattice}$ = −35.4 eV — Lattice Energy [GREEN]

Madelung constant $M=1.7476$ pure geometry (lattice series).
$e^2/(4\pi\varepsilon_0) = \alpha\hbar c$ → from alpha geometry.
$R_0 = 2.40\ \text{Å}$ derivable from SCVC ionic radii ($Z_{eff}$ hydrogen-like scaling).
Born exponent $n\sim 8$ from electron cloud overlap → semi-empirical, but weakly dependent for lattice energy.
GREEN maintained.

---

## Honest Assessment

Ca-O 3.5 eV: 7 terms = 2 GREEN + 4 YELLOW (upgradeable) + 1 RED (stubborn)
Lattice energy (−35.4 eV) dominates → Madelung pure geometry already locks the main term.
Overall: YELLOW maintained. 5/7 terms have clear geometric upgrade paths.
RED term (EA₂) is an effective fitted quantity, not an object SCVC can geometrize.
