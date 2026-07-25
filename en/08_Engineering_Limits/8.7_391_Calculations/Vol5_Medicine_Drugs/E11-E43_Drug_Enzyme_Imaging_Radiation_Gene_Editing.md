# E11: Drug Design Upper Limit

**SCVC**: Drug-target binding affinity maximum ~fM range (biotin-streptavidin).
Limitation: drugs must be small enough for oral bioavailability (<500 Da per Lipinski Rule of 5) yet specific enough for single-target binding.
SCVC: binding energy ∝ (H-bond count × 2-5 kcal/mol) + (hydrophobic contact area × 25 cal/mol/Å²) → maximum ~15-20 kcal/mol for drug-sized molecules.

# E27: Enzyme Catalytic Rate Upper Limit

**SCVC**: k_cat/K_M ≤ diffusion limit ~10⁸-10⁹ M⁻¹s⁻¹.
Physical ceiling: every enzyme-substrate encounter leads to reaction. Real enzymes: 10³-10⁷ M⁻¹s⁻¹.
Catalytic perfection gap: ~10²-10⁶-fold → room for enzyme engineering.
SCVC: transition state stabilization energy ∝ α² → ceiling set by electrostatic complementarity maximum.

# E34: Medical Imaging Upper Limit

**SCVC spatial resolution**: 
- MRI: ~100 μm (limited by proton density and gradient strength, ∝ α for nuclear magnetic moment)
- CT: ~200 μm (radiation dose limit)
- PET: ~5 mm (positron range limit, ∝ α for annihilation physics)
- Ultrasound: ~200 μm (wavelength λ=c/f, at safe frequencies)
Physical ceiling: ~10 μm for non-invasive in vivo imaging without radiation damage.

# E35: Radiation Therapy Upper Limit

**SCVC**: Maximum tumor dose limited by normal tissue tolerance.
Therapeutic ratio = (tumor cell kill)/(normal tissue damage).
SCVC: DNA double-strand break repair ∝ (H-bond energy per base pair) ∝ α².
Fractionation exploits differential repair rates between tumor and normal tissue.
Physical ceiling: ~80 Gy total dose for most sites (normal tissue fibrosis threshold).

# E43: Gene Editing Upper Limit

**SCVC**: CRISPR-Cas9 efficiency ceiling:
- On-target rate: ~10-50% (limited by chromatin accessibility)
- Off-target rate: ~0.1-1% (limited by PAM site uniqueness in genome)
SCVC: Cas9-sgRNA-DNA binding ∝ (RNA-DNA base pairing energy) ∝ H-bond network ∝ α².
Physical ceiling: no genome-wide unique target sites beyond ~20 bp guide length.
