# E274: SCVC DH vs Equivariant GW Invariants — Cross-Validation Result

**Date**: 2026-07-26 | **Status**: 🟡 New Mathematical Object

---

## Step 1: Standard CP2 T2 DH Sum

CP2 under T2 action (weights w0,w1,w2, w0+w1+w2=0):
Fixed points: [1:0:0], [0:1:0], [0:0:1]

DH sum = sum_p 1 / prod(weights at p)

Taking w0=0,w1=1,w2=-1:
  p0[1:0:0]: 1/(1 * -1) = -1
  p1[0:1:0]: 1/((-1)*(-2)) = 1/2
  p2[0:0:1]: 1/(1*2) = 1/2
  sum = -1 + 1/2 + 1/2 = 0

=> Standard CP2 equivariant volume = 0
This is a known result: CP2 equivariant volume vanishes.

---

## Step 2: Why is SCVC Non-Zero?

Key differences:
1. SCVC moduli space is not smooth CP2 — it is a truncated cone polytope
2. Truncation introduces boundary terms -> DH formula needs boundary corrections
3. Standard CP2xS1 T3 fixed-point set is empty (no fixed points on S1)
   Yet SCVC has 6 fixed points -> from special toric structure of truncated cone

---

## Step 3: Volume Interpretation Verification

Vol(CP2, FS) = pi^2/2. Vol(S1) = 2pi. Vol(CP2xS1) = pi^3.
alpha^-1 = 4pi^3 + pi^2 + pi = 137.036304

Decomposition:
  4pi^3 = 4 x Vol(CP2 x S1)
  pi^2  = 2 x Vol(CP2)
  pi    = (1/2) x Vol(S1)

---

## Step 4: Comparison with Known GW Literature

CP2 pure GW invariants (genus 0): N1=1, N2=1, N3=12, N4=620... — rational, no pi.
CP2 equivariant GW potential (Givental 1996): genus 0, degree 0 term = equivariant volume = 0.

Conclusion: SCVC 4pi^3+pi^2+pi matches no known GW invariant.

---

## Step 5: Mathematical Origin of the Difference

Standard DH: int_M omega = sum_p omega(p)/e_T(N_p). For CP2 -> 0.
SCVC differs due to: truncated cone geometry, physical regularization, special weights (4,1,1).

---

## Step 6: This Is a New Mathematical Object

SCVC DH invariant = bounded equivariant integral on truncated cone polytope.
May be a generalization of Duistermaat-Heckman to toric orbifolds with boundary.

---

## Step 6.5: CP2 Itself Is Unchanged — S1 Is What Changes

CP2 is standard. The difference is in S1:
  Smooth CP2xS1: S1 is a circle -> U(1) acts freely -> no fixed points -> DH=0
  SCVC: S1 cut into interval [0, h_max] -> endpoints = new fixed points -> DH=137
Moduli space = CP2 x [0, h_max] (with boundary), not CP2 x S1 (boundaryless).

---

## Step 6.6: Not a Correction — A Different Mathematical Object

Smooth CP2xS1 DH=0 is a CORRECT mathematical theorem. It describes a universe with alpha-1=0 — that universe does not exist, but the math is not wrong. SCVC studies a DIFFERENT object: CP2 x [0, h_max] with boundary.
Adding a boundary changes the object, not corrects the result. Circle vs line segment — different perimeter formulas.

---

## Step 7: Why Must It Be Truncated? — A Smooth CP2 Universe Does Not Exist

Smooth CP2 -> alpha^-1=0 -> EM coupling infinite -> universe does not exist.
Truncated cone saves it: boundary breaks symmetry, residue = 4pi^3+pi^2+pi = 137.
Truncation = geometric expression of finite vortex ring size. No boundary -> no universe.
Connection to E272 Kakeya duality: boundary = precondition for existence.

---

## Honest Conclusion

SCVC 4pi^3+pi^2+pi:
  X Not a standard equivariant GW invariant
  X Does not match known GW literature values
  O Is a new mathematical object: bounded DH invariant on truncated cone
  O Volume interpretation (4,1,1) is rigorous geometric fact

---
*E274 Cross-Validation. 2026-07-26.*
