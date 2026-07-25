# E2-E30: SCVC Engineering Application Prompts

## E2: Superconductor Tc Search Prompt
Task: Use SCVC constants (α, m_e, θ_D formula, λ scale) to search periodic table for room-temperature superconductor candidates. Method: Allen-Dynes Tc formula with SCVC-derived θ_D and λ constraints. Output: ranked candidate list with Tc predictions.

## E3: Battery Materials Prompt
Task: Derive electrochemical voltage upper limit from SCVC ionization energies. Li-metal anode theoretical limit ~3.04V from Li ionization energy. Maximum practical cell voltage ~6-8V limited by electrolyte HOMO/LUMO gap.

## E4: Thermoelectric Materials Prompt
Task: Calculate ZT upper limit from minimum thermal conductivity (κ_min from Debye model with SCVC θ_D). ZT_max ~4-5 theoretically, currently achieved ~2.6 (SnSe).

## E5: Ferromagnetic Materials Prompt
Task: Derive Curie temperature upper limit from exchange coupling J (SCVC: vortex ring Ampère overlap). T_C_max ~2300K. Current best: Co at 1388K (60% of limit).

## E6: Catalytic Materials Prompt
Task: Calculate TOF upper limit from transition state theory. TOF_max ~10⁹ s⁻¹ at 300K. SCVC: activation barriers ∝ α² (bond energies). Sabatier optimum ~10⁶ s⁻¹.

## E7: Optical Materials Prompt
Task: Derive refractive index ceiling. n_max ∝ α^(-1/2) ≈ 11.7 theoretically. Practical: PbTe n≈5.5. Gap from band gap requirements for material stability.

## E8: Corrosion Resistance Prompt
Task: Calculate maximum corrosion rate from electrochemical kinetics. Rate_max ~mm/s for unstable metals. Real rates limited by passivation layer formation.

## E9: Hydrogen Storage Prompt
Task: Derive optimal H₂ adsorption energy (-15 to -30 kJ/mol) from SCVC intermolecular forces. DOE target: 5.5 wt%, requires light-element alloys with tuned binding.

## E10: Drug Design Prompt
Task: Calculate maximum drug-target binding affinity from non-covalent interaction sum. K_d_min ~fM range (biotin-streptavidin). SCVC: binding energy ∝ (H-bond count × α² energy scale).

## E11-E20: Medical Engineering
- E11: Drug design upper limit
- E12: Pharmacokinetics — absorption/distribution ceilings
- E13: Drug delivery — nanoparticle size/penetration limits
- E14: Antibiotic design — resistance evolution time constraints
- E15: Vaccine design — epitope immunogenicity from MHC binding
- E16: Gene therapy — vector capacity and nuclear entry limits
- E17: Cell therapy — CAR-T expansion time constraints (E168 DNA polymerase)
- E18: Tissue engineering — scaffold degradation/regeneration rate matching
- E19: Medical imaging — spatial resolution limits (MRI~100μm, CT~200μm)
- E20: Radiation therapy — normal tissue tolerance vs tumor kill ratio

## E21-E30: Energy and Environment
- E21: Solar cell efficiency — Shockley-Queisser limit from α (band gap ~1.34 eV optimal from solar spectrum × semiconductor physics)
- E22: Nuclear fusion — Lawson criterion from Coulomb barrier (α-dependent)
- E23: Nuclear fission — maximum energy density from binding energy curve
- E24: Geothermal — Earth heat flux ~0.087 W/m²
- E25: Wind power — Betz limit (59.3%, fluid dynamics)
- E26: Hydro power — maximum head × flow from topography
- E27: Enzyme catalysis — k_cat/K_M diffusion limit ~10⁸-10⁹ M⁻¹s⁻¹
- E28: Photosynthesis — maximum quantum efficiency from chlorophyll excitation
- E29: Carbon capture — minimum energy from CO₂ concentration gradient
- E30: Water desalination — minimum energy ~1 kWh/m³ (thermodynamic limit)
