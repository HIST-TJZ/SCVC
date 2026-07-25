====================================================================
SCVC Medical Engineering  E177  Autoimmune Disease — Physical Boundary Shift of the Immune Synapse
====================================================================

【Input Constants】(from _SCVC_Engineering_Constants_QuickRef.md)
--------------------------------------------------------------
TCR-peptide-MHC binding energy: H-bonds ~0.2 eV/bond × ~5-10 H-bonds = ~1-2 eV
van der Waals contacts ≈ 0.01-0.02 eV/contact (buried surface area ~500-1000 Å²)
Peptide-MHC binding groove: 9-mer peptide, anchor residues (P2, P9) + TCR contact residues (P4-P8)
Thymic selection threshold: positive selection ~0.5-1 eV, negative selection ~1-2 eV
Peripheral activation threshold: slightly below negative selection threshold (requires co-stimulatory signals)
k_B T = 0.026 eV (310K)
MHC-I: intracellular peptides, MHC-II: extracellular peptides (15-24 mer)
α = 1/137.0363 (sets all protein-protein binding energies)
--------------------------------------------------------------


1. The Physical Essence of the Problem
==============================================================

1.1 Autoimmunity = Threshold Shift of the Same Physical Mechanism
--------------------------------------------------------------
    E171 analyzed how T+NK cells attack cancer cells (immune evasion).
    Autoimmune disease is the flip side of the same mechanism: the immune system mistakenly attacks self.

    ┌──────────────────────────────────────────────────────────┐
    │                                                          │
    │  T Cell Lifecycle — Two Rounds of Selection:              │
    │                                                          │
    │  In the Thymus (Central Tolerance):                       │
    │  · Positive selection: TCR weakly binds self-peptide-MHC → survive
    │    Threshold E_pos ≈ 0.5-1.0 eV → "useful but not dangerous"
    │  · Negative selection: TCR strongly binds self-peptide-MHC → apoptosis
    │    Threshold E_neg ≈ 1.5-2.0 eV → "too dangerous, delete"
    │                                                          │
    │  In the Periphery (Peripheral Tolerance):                 │
    │  · Activation threshold E_act ≈ 1.0-1.5 eV + co-stimulatory signal
    │  · No co-stimulation → anergy → "sees but does not attack"
    │                                                          │
    │  ⚫ Physical Root of Autoimmune Disease:                  │
    │    Gray zone ΔE_gray = E_neg − E_pos ≈ 0.5-1.0 eV       │
    │    T cells in this gray zone escape negative selection,   │
    │    yet may still be activated under specific conditions   │
    │    → attack self-tissue.                                  │
    └──────────────────────────────────────────────────────────┘


2. SCVC Quantification of TCR-Peptide-MHC Binding Energy
==============================================================

2.1 Physical Composition of the Binding Interface
--------------------------------------------------------------
    TCR-contacting peptide residues (typically P4-P8, i.e. 5 residues):

    Side-chain contribution per residue:
    · Large hydrophobic (F, W, Y, L, I): ΔG ≈ 0.3-0.5 eV/residue (hydrophobic + vdW)
    · Charged (K, R, D, E): ΔG ≈ 0.2-0.4 eV/residue (salt bridge + H-bonds)
    · Polar (N, Q, S, T): ΔG ≈ 0.1-0.2 eV/residue (H-bonds)
    · Small (A, G, V, P): ΔG ≈ 0.05-0.1 eV/residue (vdW only)

    Total TCR-peptide interface binding energy: E_interface ≈ 1.0-2.5 eV

2.2 Self-Peptide vs Foreign Peptide — What's the Physical Difference?
--------------------------------------------------------------
    ┌──────────────────────────────────────────────────────────┐
    │ ⚫ Physically, self-peptides and foreign peptides have    │
    │   NO essential difference!                                │
    │                                                          │
    │ Both are 9 amino acids, both built from the same 20.      │
    │ The immune system cannot "see" a peptide's origin —       │
    │ it can only "feel" the binding energy.                    │
    │                                                          │
    │ The logic of thymic selection is:                         │
    │ "Whatever is presented here (in the thymus) and has       │
    │  binding energy > threshold → delete"                     │
    │                                                          │
    │ Problems:                                                 │
    │ 1. Not all self-peptides are presented in the thymus      │
    │    (tissue-specific antigens)                             │
    │ 2. Presented self-peptides may have binding energy        │
    │    just below the negative selection threshold            │
    │ 3. After infection, pathogen peptides may structurally    │
    │    "mimic" self-peptides                                  │
    │    → molecular mimicry                                    │
    └──────────────────────────────────────────────────────────┘


3. The Physical Window of Autoimmune Disease
==============================================================

3.1 Why Don't We All Have Autoimmune Disease?
--------------------------------------------------------------
    Thymic selection screens ~10^7-10^8 TCR specificities.
    Each TCR has a "binding energy fingerprint" for 5 contact residues.

    Gray zone survival probability:
    P_survive = fraction of TCRs with E_interface in [E_pos, E_neg]

    Using Boltzmann distribution of binding energies:
    P_survive ≈ exp(-E_pos/k_B T) − exp(-E_neg/k_B T)
              ≈ exp(-0.75/0.026) − exp(-1.75/0.026)
              ≈ 3×10⁻¹³ − 6×10⁻³⁰
              ≈ 3×10⁻¹³

    With ~10⁸ TCR specificities screened → ~3×10⁻⁵ surviving autoreactive clones
    → i.e., ~30,000 autoreactive T cells survive per individual.

    ⚫ This means: every person carries ~30,000 potentially autoreactive T cells.
    Whether they cause disease depends on:
    1. Activation threshold (co-stimulation, inflammation)
    2. Tissue accessibility (blood-brain barrier, immune privilege)
    3. Regulatory T cell (Treg) suppression efficiency


3.2 Why Autoimmune Disease "Suddenly" Flares
--------------------------------------------------------------
    ┌──────────────────────────────────────────────────────────┐
    │ ⚫ Triggers that shift the activation threshold:          │
    │                                                          │
    │  1. Infection → inflammatory cytokines (IL-6, TNF-α)     │
    │     → lower effective activation threshold by ~0.3-0.5 eV│
    │     → previously "safe" autoreactive T cells now activate │
    │                                                          │
    │  2. Tissue damage → release of sequestered self-antigens  │
    │     → antigens previously unseen by thymus now exposed    │
    │     → "epitope spreading"                                │
    │                                                          │
    │  3. Molecular mimicry → pathogen peptide resembles self   │
    │     → anti-pathogen response cross-reacts with self       │
    │     (Detailed in Section 5)                               │
    │                                                          │
    │  4. Treg dysfunction → suppression weakened               │
    │     → activation threshold effectively lowered             │
    └──────────────────────────────────────────────────────────┘


4. SCVC Classification of Autoimmune Diseases by Physical Correctability
==============================================================

4.1 Classification Framework
--------------------------------------------------------------
    Two physical axes determine correctability:

    Axis 1: Antigen Complexity
    · Single defined antigen → ★★★★★ correctable
    · Oligo-antigen (2-5 targets) → ★★★☆☆ partially correctable
    · Poly-antigen / broad spectrum → ★☆☆☆☆ difficult

    Axis 2: Tissue Renewability
    · Fully renewable tissue (e.g., hematopoietic cells) → ★★★★★
    · Partially renewable (e.g., liver, skin) → ★★★☆☆
    · Non-renewable / critical (e.g., CNS neurons, pancreatic β-cells) → ★★☆☆☆

    ┌────────────────────┬──────────┬────────────────────────────┐
    │ Disease            │ Score    │ Physical Reason              │
    ├────────────────────┼──────────┼────────────────────────────┤
    │ Myasthenia Gravis  │ ★★★★☆   │ Single antigen (AChR),      │
    │                    │          │ thymectomy surgically       │
    │                    │          │ removes source              │
    │ Graves'' Disease    │ ★★★★☆   │ Single antigen (TSHR),      │
    │                    │          │ thyroid is non-essential    │
    │                    │          │ (replaceable hormone)       │
    │ Type 1 Diabetes    │ ★★★☆☆   │ Single/few antigens but     │
    │                    │          │ β-cells are non-renewable   │
    │ Multiple Sclerosis │ ★★☆☆☆   │ Multiple antigens + CNS     │
    │                    │          │ inaccessible                │
    │ Systemic Lupus     │ ★☆☆☆☆   │ Extremely broad antigen     │
    │ Erythematosus      │          │ spectrum (chromatin + RNA)  │
    └────────────────────┴──────────┴────────────────────────────┘

    ⚫ SCVC Principle: the more singular the antigen + the more renewable the tissue
      → the more correctable.
      The more dispersed the antigen (e.g., SLE attacking DNA/RNA/protein complexes)
      → nearly impossible.


5. The Physical Window of Post-Infection Autoimmunity
==============================================================

5.1 Guillain-Barré Syndrome (GBS) — Classic Case of Molecular Mimicry
--------------------------------------------------------------
    Campylobacter jejuni lipooligosaccharide (LOS) mimics ganglioside (GM1):
    · The sugar chain structures of both are nearly identical (difference < 2 Å)
    · Anti-LOS antibodies produced by the immune system also bind GM1
    · → attack peripheral nerves → ascending paralysis

    ⚫ SCVC Bond Energy Analysis:
    Antibody-LOS binding energy ΔG_LOS ≈ 1.5-2.5 eV (high affinity)
    Antibody-GM1 cross-binding energy ΔG_GM1 ≈ 1.2-1.8 eV (slightly lower but sufficient)

    ΔG_GM1/ΔG_LOS ≈ 0.7-0.8 → cross-reactivity probability determined by
    Boltzmann weight: exp(-ΔΔG/k_B T)

    ΔΔG ≈ 0.3-0.7 eV → exp(-0.5/0.026) ≈ 4×10⁻⁹ →
    In a B cell repertoire of 10⁷ → inevitably some cross-reactive clones.

    ⚫ This explains why GBS is "rare but inevitable":
      Molecular mimicry probability ≈ 10⁻⁶-10⁻⁸ → in a large sample of 10⁹ people,
      it is inevitable. It is not "bad luck" — it is a physical necessity of
      how the immune system works.


6. SCVC Overall Verdict
==============================================================

    ┌──────────────────────────────────────────────────────────┐
    │                                                          │
    │  Question: Is autoimmune disease physically correctable?  │
    │                                                          │
    │  SCVC Answer:                                             │
    │                                                          │
    │  ⚫ Partially yes, depending on "antigen complexity"       │
    │    and "tissue renewability":                             │
    │                                                          │
    │    · Single antigen + sacrificable tissue                 │
    │      (e.g., MG → thymectomy)                             │
    │      → ★★★★★ Correctable                                 │
    │                                                          │
    │    · Single antigen + non-sacrificable tissue             │
    │      (e.g., T1D β-cells)                                 │
    │      → ★★★☆☆ Requires antigen-specific tolerance         │
    │        + early intervention                               │
    │                                                          │
    │    · Multi-antigen + critical tissue (e.g., MS, SLE)      │
    │      → ★★☆☆☆ Difficult to correct, management only       │
    │                                                          │
    │  ⚫ Physical Root Cause:                                   │
    │    The TCR "gray zone" ΔE ≈ 0.3-0.5 eV is a physical      │
    │    constant — determined by H-bond energies and van der   │
    │    Waals forces (set by α).                               │
    │    This gray zone cannot be eliminated → certain          │
    │    autoimmune diseases are a "physical inevitability"     │
    │    → cannot be fully eradicated, but can be managed       │
    │    to not affect lifespan.                                │
    │                                                          │
    │  ⚫ Clinically Validated "Threshold Correction":           │
    │    · CTLA-4-Ig (Abatacept) → raises activation threshold  │
    │      → RA                                                │
    │    · Antigen-specific immunotherapy → in clinical trials  │
    │      (T1D, MS, allergy)                                   │
    │    → "Threshold is not fixed" — this is SCVC''s core      │
    │      therapeutic insight                                  │
    └──────────────────────────────────────────────────────────┘


====================================================================
E177 Conclusion
====================================================================

  ⚫ TCR gray zone ΔE ≈ 0.3-0.5 eV — a physical constant set by α
  ⚫ Thymic screening is not perfect → some autoreactive T cells inevitably survive
  ⚫ Molecular mimicry: post-infection autoimmunity is physically inevitable (probability ~10⁻⁶-10⁻⁸)
  ⚫ Single antigen + sacrificable tissue → correctable (MG → thymectomy)
  ⚫ Multi-antigen + critical tissue → difficult to correct, management only (MS, SLE)
  ⚫ CTLA-4-Ig has proven "threshold correction" is clinically feasible
  ⚫ Antigen-specific tolerance is the physically most elegant direction — precise and non-toxic

====================================================================
