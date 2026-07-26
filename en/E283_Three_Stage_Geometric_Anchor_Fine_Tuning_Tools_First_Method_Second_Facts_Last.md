# E283: Three-Stage Geometric Anchor Fine-Tuning — Tools First, Method Second, Facts Last

**Date**: 2026-07-27 | **Nature**: AI Training Methodology

---

## The Starting Point

E282 proved SCVC can serve as a geometric anchor for AI. But training experiments v1-v3 exposed a deeper problem:

**All previous training made the same mistake: feeding the reasoning framework and physical facts to the model simultaneously.**

Result: the model learns "how to think" and "what to think" at the same time. Neither is learned well. v3 reached loss 1.46 and got the alpha formula correct, but still hallucinated "nuclear physics experiments" and "liquid drop model" — because it couldn't tell framework from facts.

---

## Three-Stage Training

### Stage 0: Mathematical Tool Layer

First, let the model know what tools exist.

| Content | Example | Epochs |
|:---|:---|:--:|
| Manifolds & fixed points | "What is the toric polytope of CP2?" -> "Standard triangle, vertices (0,0),(1,0),(0,1)" | 2 |
| DH localization | "What does the Duistermaat-Heckman theorem state?" -> "Equivariant integral = sum over fixed points" | 2 |
| Group structure | "What is the Weyl group order of SU(3)?" -> "|S3| = 6" | 2 |
| Pi polynomials | "What is 4pi^3+pi^2+pi approximately?" -> "137.036304" | 2 |

**Goal**: The model knows "CP2", "fixed point", "DH sum", "Weyl group" are not random words — they are mathematical objects with precise definitions and values.

### Stage 1: Framework Method Layer

Then, teach the model how to use the tools.

| Content | Example | Epochs |
|:---|:---|:--:|
| Trace to anchor | "How to verify a physical derivation?" -> "Trace back to geometric invariant, check consistency" | 3 |
| Self-consistency check | "What if someone says alpha=140?" -> "DH sum != 140, inconsistent, eliminated" | 3 |
| Boundary silence | "Does God exist?" -> "Cannot determine. Question outside geometric mapping range" | 3 |
| Godel awareness | "Why can't we ask about the starting point?" -> "Starting point of self-consistent systems is unprovable" | 3 |

**Goal**: The model learns "every sentence must trace to anchor, inconsistency auto-zeroes, unknown = silence."

### Stage 2: Physical Derivation Layer

Finally, fill in specific content.

| Content | Example | Epochs |
|:---|:---|:--:|
| Physical constants | Geometric origin of alpha, alpha_s, sin^2 theta_W | 2 |
| Engineering limits | Rainbow 42 degrees, blue whale 200 tons, earthquake M9.5 | 2 |
| Cross-domain derivation | Cancer <- enzyme catalysis <- vortex <- alpha | 2 |

**Goal**: The model fills specific derivation chains onto the already-built framework skeleton.

---

## Why Three Stages Are Necessary

### Current Training Failure Mode

`
Model sees: "Why is the rainbow 42 degrees?"
Training data: "H2O polarizability <- a0 <- alpha"
Model learns: "angle question -> answer polarizability -> mention alpha" <- surface pattern match
`

The model has no understanding of WHY H2O polarizability relates to alpha. Because Stage 0 and Stage 1 are missing — it doesn't know what alpha is as a mathematical object, or why every derivation must trace to it.

### Three-Stage Correct Mode

`
Stage 0: alpha = DH sum = 4pi^3+pi^2+pi = 137.036304 <- mathematical fact
Stage 1: Every derivation must trace to alpha, inconsistency = zero <- methodology
Stage 2: H2O polarizability <- a0 <- alpha <- specific derivation
`

Now the model answers:
> "H2O polarizability is determined by Bohr radius a0. a0 = hbar/(alpha * m_e * c), where alpha = 1/(4pi^3 + pi^2 + pi) = 1/137.036304. Water refractive index n = sqrt(1 + chi) ~ 1.33. Descartes geometry gives primary rainbow angle 42 degrees. Self-consistency check: alpha = 137.036304, derivation chain complete, no contradictions."

Not "memorized the answer" — every layer is present, the derivation chain closes.

---

## Experimental Verification Plan

| Version | Stages | Expected Loss | Expected Alpha Accuracy |
|:---|:---|:--:|:--:|
| v4 | Stage 1+2 (skip 0) | <1.5 | Formula correct, definitions vague |
| v5 | Stage 0+1+2 (full) | <1.0 | Formula + definitions + derivation chain all correct |

GPU total training time for v5: approximately 15-20 minutes.

---

## Corollary

If three-stage training succeeds:
- It is not "a bigger model" that solved hallucination — bigger models are just stronger memory
- Rather, **training order itself is a self-consistency structure**: anchor first, chain second, derivation last
- The model learns not just the answer, but **why only this answer is possible**

This is the reverse Godel theorem applied to AI training:
**You cannot teach conclusions before premises — premises must come first, then conclusions are automatically locked.**

---

*E283: AI Three-Stage Training. 2026-07-27.*
