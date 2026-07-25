# E171: Immune Evasion — The Impossible Triangle

## Core
Cancer immune evasion faces a fundamental trilemma constrained by MHC-I physics.

### MHC-I Biology
- 6 MHC-I alleles (3 HLA-A, 3 HLA-B, 3 HLA-C — one from each parent)
- Each presents a different peptide repertoire
- T cells recognize specific peptide-MHC combinations
- NK cells attack cells with LOW total MHC-I

### The Impossible Triangle
Cancer cells simultaneously need:
1. **Low specific pMHC** → evade T cells (selective MHC allele loss)
2. **High total MHC-I** → suppress NK cells
3. **Continuous growth** → accumulate more mutations and immune evasion capability

→ (1)+(2) require fine-tuning specific MHC alleles → extremely narrow fault tolerance
→ (3) requires time (E169: mutation accumulation ~years)
→ Under dual immune pressure (T+NK), the "pick two" window can be compressed to disappearance!

### Two-Layer Evasion Structure
```
Layer 1 (MHC loss): T cells cannot see tumor → checkpoint inhibitors INEFFECTIVE
Layer 2 (Checkpoint upregulation): PD-L1 expression → checkpoint inhibitors EFFECTIVE

Patient tumors may have some cells in Layer 1, some in Layer 2
→ Checkpoint inhibitor alone: Layer 2 killed, Layer 1 survives → RELAPSE!
```

### Triple Combination — Window Closure
```
Strategy A: Restore MHC-I expression
  Epigenetic drugs (HDAC inhibitors, DNMT inhibitors)
  IFN-γ pathway activation → MHC-I upregulation
  
Strategy B: Enhance NK killing
  NK cell engagers (bispecific antibodies)
  Block NK inhibitory receptors (anti-KIR, anti-NKG2A)
  
Strategy C: Checkpoint inhibitors (anti-PD-1/PD-L1 + anti-CTLA-4)

A + B + C simultaneously:
  High MHC-I cancer cells → killed by T cells (A+C)
  Low MHC-I cancer cells → killed by NK cells (B)
  PD-L1+ → checkpoint blocked (C)
  → NOWHERE TO HIDE! WINDOW FULLY CLOSED!
```

### SCVC Physical Judgment
The MHC-I-mediated immune evasion window objectively exists (selective allele loss), but its width is finite — not because the immune system is perfect, but because T+NK dual surveillance + mutation time constraints force cancer through "trial-and-error-selection" rather than "one-shot escape."

**If we apply pressure on all three axes simultaneously → window closes → cancer has nowhere to escape.**
