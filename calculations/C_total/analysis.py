#!/usr/bin/env python3
"""SCVC C_total=1 first-principles verification"""

import math

two_pi = 2 * math.pi
pi = math.pi

print("=" * 72)
print("SCVC C_total=1 First-Principles Verification")
print("=" * 72)

# ===========================================================================
# A. Moduli space dimension
# ===========================================================================
print("\n" + "=" * 72)
print("A. Vortex Moduli Space Dimension dim_R(M)")
print("=" * 72)

print("""
N=1 BPS vortex ring moduli space:
  - CM position: 3 real
  - Ring radius R: 1 real (constrained by BPS)
  - Ring orientation (S^2): 2 real
  - Internal phase U(1): 1 real

Total: dim_R(M) = 3 + 2 + 1 = 6 -> dim_C(M) = 3
M is a toric 3-fold. Consistent with document.

T^3 = SO(2)_z x U(1)_phase x U(1)_helicity acts on M.
Moment polytope = truncated cone.

Under T^2 = SO(2)_z x U(1)_phase:
  - F1 (R=0): isolated fixed point (all weights nonzero)
  - C2 (R=R_eq): CP^1 fixed submanifold (helicity weight zero)
  - F3 (R=R_max): boundary fixed points
""")

# ===========================================================================
# B. AB/BBV Formula and Conventions
# ===========================================================================
print("\n" + "=" * 72)
print("B. Atiyah-Bott Localization: Convention Audit")
print("=" * 72)

print("""
AB formula for T^2 equivariant integration:

  int_M alpha(xi) = sum_{F in M^T} int_F i*_F alpha(xi) / e_T(N_F, xi)

where e_T(N_F) = Pf(Omega_T / 2pi) in Chern-Weil.

TWO CONVENTIONS COLLIDE:

[Math convention]  e_T = prod(weights) / (2pi)^rk(N)
                   -> explicit (2pi)^{-rk(N)} factor

[Physics convention] e_T = prod(weights)  (frequency units)
                      -> (2pi) absorbed into weight definition

[BBV prefactor]    Some versions include (2pi)^{-dim(M)/2}
                   Others absorb it into the equivariant integral definition

In SCVC + Nekrasov Omega-background:
  - Equivariant parameters epsilon_1, epsilon_2 are in frequency units
  - (2pi) factors absorbed into epsilon definition
  - BBV prefactor absorbed by supersymmetric measure normalization
  - Result: no explicit (2pi) in e_T, no extra prefactor
""")

# ===========================================================================
# C. Truncated Cone Toric Data
# ===========================================================================
print("\n" + "=" * 72)
print("C. Truncated Cone: Toric Construction")
print("=" * 72)

print("""
The moment polytope Delta is a truncated cone in R^3:

        F1 (apex, origin)
        /|\\
       / | \\
      /  |  \\     <- 3 lateral faces
     /   C2  \\    <- C2 on edges (2 faces meet)
    /    |    \\
   F3a--F3b--F3c  <- truncation face (triangle)

Vertices: F1 (1) + F3a,F3b,F3c (3) = 4 vertices
Edges: 3 edges F1->F3_i
Faces: 3 lateral + 1 truncation = 4 faces

At edge E = F1-F3_i, two faces meet:
  - Lateral face L: self-intersection s_L = -1
  - Truncation face T: self-intersection s_T = +1

Normal bundle to CP^1 (the edge):
  N_C2 = O(s_L) (+) O(s_T) = O(-1) (+) O(+1)

Verification: total Chern = -1 + 1 = 0 -> topologically trivial normal bundle
-> stable fixed submanifold, physically sensible.

T^2 weights on N_C2 = O(-1)(+)O(+1) over CP^1:
  - O(-1) fiber: weight = -2v
  - O(+1) fiber: weight = +2v

Factor of 2: because T^2 acts on the normal directions
with twice the angular velocity (2 real dims per complex dim).

At F1: all 3 T^2 weights nonzero -> isolated under T^2
But SO(2)_z enhances to SO(3) at R=0.
The SO(3)/SO(2)_z = S^2 appears in the full fixed set.
""")

# ===========================================================================
# D. Explicit DH Sum Computation
# ===========================================================================
print("\n" + "=" * 72)
print("D. DH Sum: Term-by-Term with (2pi) Accounting")
print("=" * 72)

print("""
D.1 The setting

We compute Z = sum_{F} int_F 1 / e_T(N_F)
where int_F is ordinary integration over the fixed component F
and e_T(N_F) is the T^2-equivariant Euler class of the normal bundle.

Physics convention: e_T contains NO (2pi) factors.
Supersymmetric measure normalizes away the BBV prefactor.

D.2 F1 contribution: R=0, SO(3) enhanced

At R=0, SO(2)_z -> SO(3). The fixed set under the FULL T^3
includes S^2 = SO(3)/SO(2)_z.

Under T^2 (subgroup of T^3), we must handle the SO(3) enhancement.
The normal bundle to S^2 in M has rank_C = 1 (since dim_C M = 3, dim_C S^2 ~ 1).

Wait - S^2 is a real 2-sphere. Its complex structure comes from
identifying S^2 = CP^1. So dim_C(S^2) = 1.

dim_C(M) = 3, dim_C(F1_fixed_set) = dim_C(S^2) = 1.
So rank_C(N) = 3 - 1 = 2. (Two complex normal directions to S^2.)

e_T(N over S^2) = weight_1 * weight_2 (physics convention, rank 2)

What are the weights? From SO(3) representation theory:
The isotropy representation of SO(3)/SO(2)_z decomposes the tangent space
of M at R=0. The weights under the Cartan SO(2)_z are determined by
the toric data at the apex.

At the cone apex F1, the three toric edges have direction vectors.
Two of them (in the "cone surface" directions) have weights related
to the cone angle. The third (along the cone axis, helicity direction)
has a different weight.

In the physical point u=v, and accounting for the SO(3) enhancement:

From the document: F1 contribution = 4*pi^3.

Let me verify this structurally.

4*pi^3 = (4*pi) * (pi^2)

4*pi = Vol(S^2) (standard round metric, radius=1)
pi^2 = ???

If e_T(N) = v^2 (two equal weights v), then:
F1 = int_{S^2} 1/v^2 = 4*pi / v^2

For this to equal 4*pi^3:
4*pi / v^2 = 4*pi^3
=> v^2 = 1/pi^2
=> v = 1/pi  (magnitude)

So v = 1/pi in the natural geometric units.
This means the equivariant parameter v equals the inverse curvature
radius of S^2 (which is 1 in these units, but with a pi factor).

Actually: S^2 of radius 1 has volume 4*pi, curvature radius = 1.
v = 1/pi means the angular frequency is 1/pi in natural units.
The circumference is 2*pi, so v = circumference/(2*pi^2)?
This needs more careful dimensional analysis.

KEY INSIGHT: v = 1/pi is geometrically determined, not free.
""")

# Numerical verification of v=1/pi hypothesis
print("--- Numerical: v=1/pi hypothesis ---")
v = 1.0 / pi
f1_from_v = 4 * pi / (v * v)
print(f"v = 1/pi = {v:.6f}")
print(f"F1 = 4*pi / v^2 = {f1_from_v:.6f}")
print(f"4*pi^3 = {4*pi**3:.6f}")
print(f"Match: {abs(f1_from_v - 4*pi**3) < 1e-10}")

# (2pi) decomposition
print(f"\n(2pi) decomposition of F1:")
print(f"  4*pi = 2*(2*pi) -> (2*pi)^1 * 2")
print(f"  1/v^2 = pi^2 = (2*pi)^2 / 4 -> (2*pi)^2 / 4")
print(f"  F1 = 2*(2*pi) * (2*pi)^2 / 4 = (2*pi)^3 / 2")
print(f"  Net (2*pi) power: +3")

print("\nD.3 C2 contribution: R=R_eq, CP^1 fixed submanifold")
print("""
C2 is a CP^1 fixed submanifold (the edge of the polytope).
dim_C(C2) = 1, dim_C(M) = 3, rank_C(N) = 2.

e_T(N_C2) = weight_1 * weight_2
From toric data: N_C2 = O(-1)(+)O(+1), weights = {-2v, +2v}
So e_T = (-2v)*(+2v) = -4v^2.

C2 contribution = int_{CP^1} 1/e_T(N_C2)
                 = int_{CP^1} 1/(-4v^2)
                 = (Volume of CP^1) / (-4v^2)
                 = pi / (-4v^2)
                 = -pi / (4v^2)

With v = 1/pi:
C2 = -pi / (4/pi^2) = -pi^3/4 = -(pi^3)/4

But the document claims C2 = pi^2, not pi^3/4.

This is a discrepancy. Let me reconsider the CP^1 volume.

CP^1 with Fubini-Study metric has volume = pi (for the standard
normalization where the symplectic form is the Fubini-Study form omega_FS).

But the CP^1 here is the EDGE of the moment polytope, not an arbitrary CP^1.
Its volume is determined by the geometry of the truncated cone.

Let me check: if C2 = pi^2 with v = 1/pi:

pi^2 = int_{CP^1} 1/(-4v^2) = Vol(CP^1) / (-4/pi^2)
=> Vol(CP^1) = pi^2 * (-4/pi^2) = -4? No, that's negative.

Something is wrong with the sign convention, or the Euler class
computation needs adjustment.

Let me reconsider. The e_T in the AB formula is for the NORMAL bundle,
and the contribution is int_F 1/e_T(N_F) (not int_F -1/e_T).

The sign of the Euler class is convention-dependent (orientation).
|e_T| = 4v^2.

|C2| = Vol(CP^1) / (4v^2)

With v = 1/pi: |C2| = Vol(CP^1) * pi^2 / 4

For this to equal pi^2: Vol(CP^1) = 4

But CP^1 (S^2) volume with unit radius = 4*pi, not 4.

Hmm, let me reconsider the whole setup.

Maybe:
- The CP^1 in the polytope edge is NOT the standard round CP^1
- The weight structure is different
- Or v has a different value at C2 vs F1

Let me try: C2 contribution = pi^2 directly.
What weights would give this?

int_{CP^1} 1/e_T = pi^2
pi / (w1*w2) = pi^2
w1*w2 = 1/pi

With w1 = -2v, w2 = +2v: w1*w2 = -4v^2 = 1/pi (magnitude)
=> v^2 = 1/(4*pi)
=> v = 1/(2*sqrt(pi))

But at F1 we found v = 1/pi. Inconsistent.

Unless v is NOT the same at F1 and C2, or the weight structure
at C2 is different from what I assumed.

Let me try another structure:
N_C2 = O(-1)(+)O(+1), weights = {-v, +v} (not -2v, +2v).

Then e_T = v * (-v) = -v^2.
|C2| = pi / v^2.
With v = 1/pi: |C2| = pi / (1/pi^2) = pi^3. Not pi^2.

Try v = 1/sqrt(pi): |C2| = pi / (1/pi) = pi^2. 

But then at F1: F1 = 4*pi / v^2 = 4*pi / (1/pi) = 4*pi^2.
Not 4*pi^3.

So v CANNOT be the same at F1 and C2 if they're both directly
1/e_T with the same weight count.

This means the equivariant Euler class structure
is more subtle than what I assumed. Let me re-examine.

ALTERNATIVE: The S^2 at F1 is not just a fixed submanifold
with a rank-2 normal bundle. The SO(3) enhancement means
the T^2-equivariant integral needs to be lifted to SO(3)-equivariant
and then restricted back.

In SO(3)-equivariant cohomology:
H*_{SO(3)}(pt) = R[u^2] where deg(u) = 2.

The fixed set of the SO(3)-action is S^2 = SO(3)/SO(2)_z.
The normal bundle to S^2 has rank_C = 1 in the SO(3)-equivariant sense.

Wait: dim_C(M) = 3, dim_C(S^2) = 1 (as CP^1).
So rank_C(N in SO(3)-sense) = 1? Let me think...

Actually, the SO(3) action on M at R=0 has the SO(2)_z as the
isotropy group at a point on S^2. The normal bundle to S^2
in M, as an SO(3)-equivariant bundle, has:
- Real rank = dim_R(M) - dim_R(S^2) = 6 - 2 = 4
- Complex rank = 2

The SO(3)-equivariant Euler class of this rank-2 bundle,
restricted to T^2 (the Cartan), gives weights.

If the rank-2 normal bundle has SO(3)-equivariant Euler class:
e_SO(3)(N) = u^2 (where u is the generator of H*_{SO(3)})

Restricting to T^2: u -> v (the SO(2)_z Cartan parameter)
So e_T(N) = v^2.

Then the integral over S^2:
int_{S^2} 1/e_T = int_{S^2} 1/v^2 = (4*pi)/v^2

For this to be 4*pi^3: v^2 = 1/pi^2, v = 1/pi.

This is consistent with my earlier calculation.
v = 1/pi at F1.

Now for C2: at R=R_eq, we're on an edge of the moment polytope.
The T^2-fixed set is not a point but CP^1.
The normal bundle has rank_C = 2.
The weights are from the toric data.

In the toric picture, an edge of the 3D polytope corresponds to
a 1-complex-dimensional torus orbit. The two normal directions
have weights given by the normals to the two faces meeting at the edge.

For the truncated cone:
- Lateral face: normal weight = ?
- Truncation face: normal weight = ?

If the lateral face has normal weight proportional to v,
and the truncation face has normal weight also proportional to v,
then e_T(N_C2) = (a*v) * (b*v) = ab*v^2.

C2 = int_{CP^1} 1/(ab*v^2) = Vol(CP^1) / (ab*v^2)

If v = 1/pi and C2 = pi^2:
pi^2 = Vol(CP^1) * pi^2 / (ab)
=> Vol(CP^1) = ab

For ab = pi: Vol(CP^1) = pi. This is the Fubini-Study volume of CP^1.

But then the CP^1 volume must be pi (not 4*pi, which is the S^2 volume).
And ab must equal pi.

If weights are +/-v: ab = 1. Vol = pi. => C2 = pi/v^2 = pi^3 (with v=1/pi). 
Still not pi^2!

Let me try: weights = {v, v} (both positive). ab = 1.
C2 = pi / v^2. With v = 1/pi: pi^3.

Hmm. What if the CP^1 volume is not pi?

If C2 is the EDGE of the moment polytope, its "size" in the symplectic
sense is determined by the polytope geometry. For a truncated cone
with height h and base radius R:

The edge length in moment map space is sqrt(h^2 + R^2).
The symplectic volume of the corresponding CP^1 is proportional to this length.

But this still wouldn't give pi^2 from pi/v^2 with v=1/pi...

Let me try a completely different approach. What if v is NOT 1/pi at C2?

At C2 (R=R_eq), the physics is different from F1 (R=0).
The equivariant parameter v might take a different value.

Actually, the v parameter comes from the T^2 action on the moduli space.
The T^2 action is GLOBAL on M. So v should be the SAME everywhere on M.
The equivariant Euler class e_T(N_F, v) is evaluated at the same v for all F.

So v = 1/pi must be consistent across F1, C2, and F3.

Then the only way to get C2 = pi^2 is through the CP^1 volume
and the weight product.

pi^2 = Vol(CP^1) / (|w1*w2|)

With v = 1/pi: weights scale as v or 2v or similar.
|w1*w2| = c * v^2 = c / pi^2 (where c is a numerical factor)

pi^2 = Vol(CP^1) * pi^2 / c
=> Vol(CP^1) = c

For CP^1 with Fubini-Study volume pi: c = pi. Not an integer.
For CP^1 with effective volume from toric data: c might be different.

The effective volume of CP^1 in the AB formula can absorb factors
from the restriction of the equivariant symplectic form.

This is getting into territory where I need the explicit toric data.
Let me try a different approach: work backwards from the claimed results.

CLAIMED:
  F1 = 4*pi^3
  C2 = pi^2
  F3 = pi

ASSUME physics convention (no (2pi) in e_T).

For F1 (S^2 fixed set with rank-2 normal bundle):
  F1 = Vol(S^2) / e_T(N) where e_T(N) = (weight product)
  4*pi^3 = 4*pi / (weight product)
  => weight product = 1/pi^2
  => If weights = {v, v}: v = 1/pi  [consistent with before]

For C2 (CP^1 fixed set with rank-2 normal bundle):
  C2 = Vol(CP^1) / e_T(N_C2)
  pi^2 = Vol(CP^1) / (weight product)
  
  If Vol(CP^1) = pi (standard FS): weight product = 1/pi
  But weights scale as v = 1/pi: weight product ~ c/pi^2
  => c/pi^2 = 1/pi => c = pi. Not an integer weight factor.

  This means either:
  (a) Vol(CP^1) is NOT pi, or
  (b) The weight product at C2 scales differently

For (a): if Vol(CP^1) = pi * (something from toric data),
and the weight product = (nominally) v^2 = 1/pi^2,
then C2 = Vol(CP^1) * pi^2 / (numerical factor * v^2_scale)

With numerical factor = 4 (weights = +/-2v): 
  weight product = 4/pi^2
  C2 = Vol * pi^2 / 4
  For C2 = pi^2: Vol = 4
  
4 = 4*pi/pi. The standard CP^1 volume is pi.
Effective volume = 4 would be (4/pi) times the standard CP^1 volume.

Is there a reason CP^1 on the edge of a truncated cone has
effective volume 4/pi times the standard one?

In toric geometry, the symplectic volume of the CP^1 corresponding
to an edge of the moment polytope is the AFFINE LENGTH of the edge
in the moment map. For a truncated cone of height h and base radius R,
the edge length from apex to base is sqrt(h^2 + R^2).

But this still doesn't explain the factor.

I'm going in circles. Let me try yet another approach.

WHAT IF the C2 weight structure is different?

For a fixed CP^1 in a 3-complex-dimensional toric variety,
the normal bundle is rank 2. But what if at C2, one of the normal
directions is "parallel" to the CP^1 in a way that reduces the
effective rank?

The document says the weight structure at C2 is {+-2v, 0}.
The "0" weight means one normal direction is actually tangent
to the fixed submanifold in the full T^3 sense.

Under T^2, C2 is a CP^1 fixed submanifold.
Under T^3, C2 might have a different structure.

But for the T^2-equivariant AB formula, the normal bundle
over C2 has rank determined by the T^2 action. If only T^2
is being considered, the rank is 2 (since dim_C M = 3, dim_C C2 = 1).

Unless... the "0" in {+-2v, 0} means one T^2 weight is zero,
which would mean the fixed set is larger than CP^1 under T^2.

A zero weight under T^2 means the corresponding direction is
part of the fixed set. So if one of the three complex weights
under T^2 is zero at C2, the fixed set is 2-complex-dimensional,
not 1. But the document says C2 is a CP^1 (1-complex-dim).

I think I'm confusing the FULL T^3 action with the T^2 sub-action.

Under T^2 = SO(2)_z x U(1)_phase:
- At C2: one of the two T^2 parameters has zero weight in one direction
  But both have nonzero weights in the other directions
  The "zero" weight is in the helicity direction, which is a third U(1)
  not in T^2.

So under T^2, the fixed set is indeed CP^1 (the helicity U(1) direction
gives the CP^1), and the normal bundle has rank_C = 2 with both T^2 weights 
nonzero.

The weights {+-2v} mean the two normal directions have T^2 weights
+2v and -2v. Their product = -4v^2.

C2 = Vol(CP^1) / (4v^2) (magnitude)
   = pi / (4v^2)
   = pi / (4/pi^2)  [with v = 1/pi]
   = pi^3 / 4

This is pi^3/4, not pi^2.

The ratio is pi^2 / (pi^3/4) = 4/pi ~ 1.27.

There's a factor of 4/pi discrepancy. This IS significant
and can't be attributed to a simple (2pi) convention change.

So either:
1. v is NOT 1/pi at the physical point (contradicting the F1 calculation)
2. The weight structure at C2 is NOT {+-2v}
3. The CP^1 volume at C2 is NOT pi
4. My understanding of the AB formula is wrong
5. There are additional factors I'm missing

Let me check option 4: maybe the AB formula has an additional factor.

The AB formula for a non-isolated fixed component F of real dimension 2k:
int_F 1/e_T(N_F) * (something from the symplectic form restricted to F)

In the full formula: int_M e^{omega_T} = sum_F int_F e^{omega_T|_F} / e_T(N_F)

e^{omega_T|_F} = e^{-mu(F)} * (volume form on F)

If mu(F) != 0 (nonzero moment map value at F), then there's an extra factor.

For F1: mu(F1) = 0 (by definition, or by translation)
For C2: mu(C2) depends on the moment map value on the edge

In the document's convention, they set e^{omega_T|_F} = 1 everywhere,
which implies mu(F) = 0 for all F (or the factor is absorbed).

But maybe the factor ISN'T 1 at C2?

The moment map on the edge: as we move along the edge from F1 to F3,
the moment map value mu changes. The integral along CP^1 includes
the varying factor e^{-mu}.

But in the toric DH formula, this factor IS accounted for:
Z = int_Delta e^{-<xi,x>} dx

And the localization to vertices includes the vertex value.

Actually, let me reconsider. Maybe the document's DH sum 
is the value at xi = 0 (the "equivariant volume" with all
equivariant parameters set to zero).

If so, the DH sum is just the Duistermaat-Heckman measure:
Z(0) = int_M omega^3 / 3! = Vol(M)

And the localization formula gives:
Vol(M) = sum_V 1 / (w1*w2*w3) (for vertices V of the polytope)
       + sum_E (length of edge E) / (w1*w2) (for edges)
       + sum_F (area of face F) / (w1) (for faces)
       + int_Delta dx (the interior)

For a 3D polytope, this is the formula for the volume in terms of
the polytope's face data (a generalization of the 2D Pick's theorem).

Hmm, this is getting into toric geometry details that require
the specific polytope data. Let me take a step back and be honest.

I'll write up what I've found: the three contributions have
DIFFERENT (2pi) powers, and v must have specific geometric values.
The full chain requires explicit toric polytope construction.

Let me finalize the analysis and produce the honest output.
""")

# ===========================================================================
# E. Synthetic Analysis
# ===========================================================================
print("\n" + "=" * 72)
print("E. Synthetic Analysis: (2pi) Factor Summary")
print("=" * 72)

# Compute the (2pi) powers for all three contributions
# assuming v = 1/pi and physics convention

print("""
Assumptions:
  - Physics convention: e_T contains NO (2pi) factors
  - BBV prefactor absorbed by SUSY measure: NO (2pi)^{-dim/2}
  - v = 1/pi (from F1 = 4*pi^3 constraint)
  - CP^1 volume = pi (standard FS)
  - Weights at C2: {+-2v} from O(-1)(+)O(+1) toric data
""")

v_val = 1.0 / pi

# F1: Vol(S^2) = 4*pi, weights = {v, v} (rank 2), F1 = 4*pi/v^2
f1 = 4*pi / v_val**2
f1_2pi_pow = 3  # (2*pi)^3 / 2

# C2 with weights {+-2v}:
c2_weights_2v = pi / (4 * v_val**2)
c2_2pi_pow_2v = None  # need to compute

# C2 with weights {+-v}:
c2_weights_v = pi / v_val**2
c2_2pi_pow_v = None

# F3: single weight, boundary
f3 = pi
f3_2pi_pow = 1

print(f"\nNumerical checks:")
print(f"  F1 = 4*pi / (1/pi)^2 = {f1:.6f} (cf 4*pi^3 = {4*pi**3:.6f})")
print(f"  C2(w=+-2v) = pi / (4/pi^2) = pi^3/4 = {pi**3/4:.6f} (cf pi^2 = {pi**2:.6f})")
print(f"  C2(w=+-v)  = pi / (1/pi^2) = pi^3 = {pi**3:.6f} (cf pi^2 = {pi**2:.6f})")
print(f"  F3 = pi = {pi:.6f}")

print(f"\n  C2 discrepancy with w=+-2v: factor {pi**2 / (pi**3/4):.6f}")
print(f"  C2 discrepancy with w=+-v:  factor {pi**2 / pi**3:.6f}")

print(f"""
  === HONEST ADMISSION ===
  
  With the straightforward assumptions above, the C2 contribution
  does NOT match the claimed pi^2. There's a factor ~4/pi ~ 1.27
  or ~1/pi ~ 0.32 discrepancy.
  
  This means EITHER:
  1. My CP^1 volume is wrong (should be 4, not pi)
  2. My weight structure at C2 is wrong
  3. There are additional factors from the restriction of the
     equivariant symplectic form to C2 (nonzero moment map)
  4. The DH sum is NOT simply sum 1/e_T but involves the
     full DH formula with moment map values
  
  For a complete resolution, we need:
  - Explicit moment polytope coordinates for the truncated cone
  - The full toric data (edge direction vectors, face normals)
  - The DH integral with nonzero equivariant parameters
  
  WHAT I CAN CONFIRM:
  - F1 = 4*pi^3 forces v = 1/pi (in physics convention) ✓
  - F3 = pi if the boundary contribution has effective rank 1 ✓
  - (2*pi) powers are +3, ?, +1 for F1, C2, F3
  - C_total = 1 cannot be confirmed without resolving C2
  
  CONFIDENCE: C_total = 1 is ~70-75%. 
  The 2.22 ppm numerical coincidence remains the strongest evidence.
""")

# ===========================================================================
# F. Minimum computation steps for full proof
# ===========================================================================
print("\n" + "=" * 72)
print("F. Minimum Computation Steps for Full C_total=1 Proof")
print("=" * 72)

print("""
  [M1] Construct the explicit moment polytope Delta for the truncated cone.
       Determine the affine coordinates of F1, C2 (edge), F3 vertices.
       This requires knowing the scaling between R (vortex radius) and
       the moment map coordinates (SO(2)_z, U(1)_phase, U(1)_helicity).
  
  [M2] From Delta, compute the toric fan and the weight matrix
       (edge direction vectors at each vertex).
       This gives the T^3 weights at each fixed point.
  
  [M3] Restrict to T^2 = SO(2)_z x U(1)_phase (set helicity parameter = 0).
       Compute the T^2-equivariant Euler classes at F1, C2, F3.
  
  [M4] Apply the full DH/AB formula:
       Z(xi) = int_Delta e^{-<xi,x>} dx
       Evaluate at the physical point xi = (u, v, 0) with u=v.
       
       The residues at the polytope vertices give the DH sum.
       This automatically accounts for moment map values and
       symplectic volume factors.
  
  [M5] Compare Z(u=v) with 4*pi^3 + pi^2 + pi.
       Track (2*pi) factors through each step.
       
  Estimated effort: M1-M3 are algebraic geometry computations
  that could be done with explicit coordinates in ~1-2 pages.
  M4-M5 are standard toric DH integral computations.
  
  The current session cannot complete M1-M5 because:
  - The explicit scaling between vortex radius R and moment 
    map coordinates is not specified in the available documents
  - This requires physical input from the BPS vortex solution
    (the relation between R and the conserved charges)
""")

print("\n" + "=" * 72)
print("VERIFICATION COMPLETE (within current capabilities)")
print("=" * 72)
