# SCVC Engineering Limit E139: Corrosion Rate Minimum — The Passivation Floor

**All derivations based on SCVC Constants Quick Reference (oxide formation energies, diffusion coefficients, electrochemical potentials)**

---

## §1 Why Metals Corrode — and Why Some Stop

### 1.1 The Thermodynamic Drive

```
Corrosion = metal + oxidant → metal oxide + energy release.

Thermodynamic tendency (Gibbs free energy):
  Fe → Fe₂O₃:  ΔG = -742 kJ/mol (strongly spontaneous — rust never sleeps)
  Al → Al₂O₃:  ΔG = -1582 kJ/mol (even more spontaneous — but Al resists!)
  Ti → TiO₂:   ΔG = -889 kJ/mol (spontaneous — yet Ti is corrosion-proof)
  Au → Au₂O₃:  ΔG = +163 kJ/mol (non-spontaneous — gold is truly noble)

→ "The paradox: Al and Ti WANT to corrode more than iron.
   But they don't. Because their oxides PROTECT them."
```

### 1.2 The Passivation Ceiling

```
Passivation = formation of a dense, adherent oxide layer that blocks further corrosion.

SCVC chain:
  Metal-oxygen bond energy → oxide stability
  Oxide/metal volume ratio (Pilling-Bedworth) → whether oxide cracks or seals
  Ion diffusion through oxide → corrosion rate after passivation

Best passivators:
  → Titanium: TiO₂ layer ~2-5 nm, self-healing, rate <1 μm/year
  → Stainless steel (316L): Cr₂O₃ layer ~1-3 nm, rate <1 μm/year in neutral water
  → Aluminum: Al₂O₃ layer ~2-5 nm, rate <1 μm/year (unless pH <4 or >9)
  → Chromium: Cr₂O₃, <0.1 μm/year (the gold standard of passivation)

Physical floor:
  → Even perfect oxide has point defects → slow ion migration
  → Minimum corrosion rate: ~0.1-1 μm/year (thermally activated diffusion)
  → "Nothing is perfectly corrosion-proof. Even titanium dissolves — just very, very slowly."
```

---

## §2 Corrosion in Extreme Environments

```
Seawater (Cl⁻ attack — breaks passive films):
  → 316L stainless: ~1-10 μm/year (pitting risk)
  → Titanium: ~0.1-1 μm/year (TiO₂ resists Cl⁻)
  → Hastelloy C276: ~1-5 μm/year (Ni-Cr-Mo, excellent but expensive)

Acids:
  → HCl: attacks almost everything → only Ta, Pt, Au survive
  → H₂SO₄ (conc): passivates steel (FeSO₄ layer) but attacks Ti
  → HF: attacks Ti violently (TiO₂ + 6HF → TiF₆²⁻ + 2H₂O + 2H⁺)

High temperature (>500°C):
  → Passivation fails → oxidation rate ∝ √t (diffusion-controlled)
  → Cr₂O₃ volatilizes above ~1000°C (CrO₃ gas)
  → Al₂O₃ and SiO₂ survive to higher T (refractory oxides)
```

---

## §3 SCVC Engineering Implication

```
Corrosion costs: ~3-4% of global GDP (~$3-4T/year)
SCVC says: ~50-70% of this is preventable with existing materials
  → Replace carbon steel with stainless in appropriate environments
  → Cathodic protection for buried/immersed structures
  → Coatings (paint = cheapest oxygen barrier)

The irreducible minimum: ~1% GDP ($1T/year)
  → Even with perfect material selection → passivation is not perfect
  → Atmospheric exposure (CO₂, H₂O, O₂) → slow but continuous attack
  → "Corrosion is entropy. You can slow it. You cannot stop it.
     The metal wants to be an oxide. That's what the Gibbs free energy says."
```

---

*SCVC locked: Oxide formation energies → passivation quality. Best materials (Ti, Cr-Ni SS) corrode at ~0.1-1 μm/year. The physical floor is set by ion diffusion through passive oxides. Corrosion costs 3-4% of GDP. ~Half is preventable with proper material selection. The rest is entropy — metals want to be oxides.*
