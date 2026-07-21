import numpy as np
from scipy.special import beta as beta_func

# ============================================================
# PATH A: CP2 Killing Normalization — Pure Analytical
# ============================================================

def volume_cp2():
    return np.pi**2 / 2

def volume_s2(R=1.0):
    return 4 * np.pi * R**2

def killing_s2(R=1.0):
    return 8 * np.pi * R**4 / 3

print("="*70)
print("PATH A: CP2 Killing Normalization — Analytical Computation")
print("="*70)

# --- S2 known data ---
I_S2 = killing_s2()
V_S2 = volume_s2()
print(f"\nS2 = SO(3)/SO(2):")
print(f"  Vol(S2)       = 4*pi   = {V_S2:.6f}")
print(f"  I_Killing     = 8*pi/3 = {I_S2:.6f}")
print(f"  I/Vol         = 2/3    = {I_S2/V_S2:.6f}")
print(f"  g2 correction = sqrt(pi/4) = {np.sqrt(np.pi/4):.6f}")
print(f"  Also equals sqrt(Vol(S2)/16) = {np.sqrt(V_S2/16):.6f}")

# --- CP2 as S5/U(1) Hopf fibration ---
print(f"\nCP2 = SU(3)/S[U(2)xU(1)] = S^5/U(1):")
print(f"  Vol(S5, R=1)  = pi^3 = {np.pi**3:.6f}")
print(f"  Vol(CP2)      = pi^3/(2pi) = pi^2/2 = {np.pi**2/2:.6f}")

# Killing normalization on S^5 (per SO(6) generator)
# I_S5 = Vol(S^4) * ∫_0^pi sin^6(theta) dtheta
# Vol(S^4) = 8*pi^2/3
# ∫ sin^6 = 5*pi/16
# => I_S5 = 5*pi^3/6

vol_S4 = 8 * np.pi**2 / 3
int_sin6 = 5 * np.pi / 16
I_S5 = vol_S4 * int_sin6  # = 5*pi^3/6

print(f"\n  Vol(S^4)      = 8*pi^2/3 = {vol_S4:.6f}")
print(f"  ∫ sin^6 dtheta = 5*pi/16  = {int_sin6:.6f}")
print(f"  I_S5 (1 gen)  = 5*pi^3/6 = {I_S5:.6f}")

# CP2 Killing normalization via Riemannian submersion
# SU(3) generators = horizontal w.r.t. Hopf fibration
# I_CP2 = I_S5 / (fiber length) = I_S5 / (2*pi)
I_CP2 = I_S5 / (2 * np.pi)  # = 5*pi^2/12
V_CP2 = volume_cp2()

print(f"\n  I_CP2 (1 gen) = I_S5/(2pi) = 5*pi^2/12 = {I_CP2:.6f}")
print(f"  Vol(CP2)      = pi^2/2 = {V_CP2:.6f}")
print(f"  I/Vol(CP2)    = 5/6 = {5/6:.6f}")
print(f"  (cf. S2: I/Vol = 2/3 = 0.6667)")

# ============================================================
# Killing form analysis for SU(3) ⊂ SO(6)
# ============================================================
print(f"\n{'='*70}")
print("SU(3) ⊂ SO(6) EMBEDDING: KILLING FORM RATIO")
print(f"{'='*70}")

print("""
SO(6) Killing form: B_SO6(X,Y) = 4 * Tr_{vec}(X Y)
  (vec = 6-dim vector representation)

SU(3) Killing form: B_SU3(T^a,T^b) = 6 * Tr_{fund}(T^a T^b)
  = 3 * delta^{ab} (physics: Tr(T^a T^b) = 1/2 delta^{ab})

Embedding SU(3) → SO(6): 3 ⊕ 3bar = 6 of SO(6)
  Tr_{6}(X Y) = Tr_{3}(X Y) + Tr_{3bar}(X Y) = 2 * Tr_{3}(X Y)

  B_SO6|_{SU(3)} = 4 * 2 * Tr_{3}(X Y) = 8 * (1/2)delta^{ab} = 4 * delta^{ab}
  B_SU3 = 3 * delta^{ab}

  Ratio: B_SO6/B_SU3 = 4/3
""")

kf_ratio = 4.0/3.0

# The I_CP2 we computed uses the S5 metric, which is normalized by 
# the SO(6) Killing form. When we identify the Killing vectors with 
# SU(3) gauge generators, we need to adjust the normalization.
# 
# I_CP2_SU3 = I_CP2 / (B_SO6/B_SU3) = I_CP2 * 3/4
I_CP2_SU3 = I_CP2 / kf_ratio
print(f"  I_CP2 (SU3 normalized) = I_CP2 / (4/3) = {I_CP2_SU3:.6f}")
print(f"  I_SU3/Vol = {I_CP2_SU3/V_CP2:.6f}")

# ============================================================
# CORRECTION FACTOR DERIVATION
# ============================================================
print(f"\n{'='*70}")
print("CORRECTION FACTOR: MATCHING TO FIELD THEORY")
print(f"{'='*70}")

# In KK reduction from D-dimensional gravity:
# 1/g^2_4d = Vol(K) / (2*kappa^2_D) * I
# where I = (1/Vol(K)) * ∫ K^a_m K^b_n g^{mn} * sqrt(g)
#
# For 4D: 1/g^2_4d = 1/(2*kappa^2_4) * I
#            = M_Pl^2 / (16*pi) * I
#
# But the standard 4D Yang-Mills normalization is:
# -1/(4g^2) F^a_{mu nu} F^{a,mu nu}
# with F^a = dA^a + g * f^{abc} A^b ∧ A^c
# and the generators normalized by Tr(T^a T^b) = delta^{ab}/2
#
# The geometric Killing vectors K^a generate the isometry algebra:
# [K^a, K^b] = f^{abc} K^c  (same structure constants)
#
# But the normalization of K^a is fixed by the metric on M.
# The field theory normalization of T^a is fixed by Tr(T^a T^b).
#
# The ratio between the two normalizations gives the correction factor.
#
# For S2: I_geom = 8*pi/3, but the field theory needs something else.
# The g2 correction factor is sqrt(pi/4).
# This means: the geometric prediction for g2 must be multiplied by 
# sqrt(pi/4) to match the field theory.
#
# g^2_geom ∝ 1/I
# g^2_corrected = g^2_geom * (correction)^2
#               = g^2_geom * (pi/4)
# g^2_corrected ∝ 1/(I * 4/pi)
#              = 1/((8*pi/3) * (4/pi))
#              = 1/(32/3)
#              = 3/32
#
# So the "effective I" for S2 in field theory normalization:
# I_S2_eff = I_S2 * 4/pi = (8*pi/3) * (4/pi) = 32/3
# 
# Hmm, but this is larger than I_S2 = 8*pi/3 ≈ 8.378.
# The effective normalization is larger, meaning g^2 is smaller.
# This makes sense: the correction factor < 1 reduces the coupling.
#
# But where does 4/pi come from? It equals Vol(S2)/4, since Vol(S2)=4*pi.
# And 4 = 16/4...
# 
# The correction = sqrt(Vol/16) = sqrt(4*pi/16) = sqrt(pi/4)
# 1/correction^2 = 16/Vol = 16/(4*pi) = 4/pi

# So the pattern is:
# I_eff = I_geom * (C / Vol(M))
# where C is a constant that's the same for all manifolds?
# For S2: C=16, I_eff = I_S2 * 16/Vol(S2) = (8pi/3) * 16/(4pi) = 32/3
#
# For CP2: if C=16 also, then
# I_CP2_eff = I_CP2 * 16/Vol(CP2) = (5pi^2/12) * 16/(pi^2/2) = (5pi^2/12) * 32/pi^2 = 40/3

I_CP2_eff_sameC = I_CP2 * 16 / V_CP2
I_S2_eff = I_S2 * 16 / V_S2
print(f"\nPattern: I_eff = I_geom * 16 / Vol(M)")
print(f"  I_S2_eff   = {I_S2_eff:.6f} (= 32/3)")
print(f"  I_CP2_eff  = {I_CP2_eff_sameC:.6f} (= 40/3)")

# Now compute the relative correction:
# g^2_3 / g^2_2 (from geometry) = I_S2 / I_CP2 (inverse of I ratio)
# With corrections: g^2_3 / g^2_2 = I_S2_eff / I_CP2_eff
ratio_eff = I_S2_eff / I_CP2_eff_sameC
print(f"\n  I_S2_eff / I_CP2_eff = {ratio_eff:.6f}")

# But this gives the RATIO between g2 and g3, not the absolute correction.
# For the absolute CP2 correction:
# correction = sqrt(I_CP2_eff_sameC / I_CP2)  ???
# No, correction = sqrt(I_CP2 / I_CP2_eff_sameC)?
# Let me think about this more carefully.
#
# g^2 ∝ 1/I (geometric)
# g^2 ∝ 1/I_eff (field theory)
# correction = g_field / g_geom = sqrt(I_geom / I_eff)
# = sqrt(I / (I * 16/Vol)) = sqrt(Vol/16)

correction_cp2_sameC = np.sqrt(V_CP2 / 16)
print(f"\n  CP2 correction (C=16): sqrt(Vol/16) = {correction_cp2_sameC:.6f}")
print(f"  Target: 0.61")
print(f"  Ratio correction/target = {correction_cp2_sameC/0.61:.4f}")

# That gives 0.555, not 0.61. 9% off.

# ============================================================
# ALTERNATIVE: C is NOT the same for all manifolds
# ============================================================
print(f"\n{'='*70}")
print("ALTERNATIVE DERIVATIONS OF C_CP2")
print(f"{'='*70}")

# If correction = sqrt(Vol(M)/C_M) where C_M depends on M:
# For S2: C_S2 = 16
# For CP2: C_CP2 = Vol(CP2) / (target)^2 = (pi^2/2) / 0.3721

C_CP2_target = V_CP2 / (0.61**2)
print(f"\n  C_CP2_target = {C_CP2_target:.4f}")

# What could C_CP2 be in terms of group theory?
# Candidates:
candidates_theory = {
    "dim(SU3)^2 = 64": 64,
    "4*dim(SU3) = 32": 32,
    "C_A^2 * 2 = 18": 18,
    "(dim*C_A) = 24": 24,
    "dim(SU3)*pi = 8*pi": 8*np.pi,
    "4*pi = 4pi": 4*np.pi,
    "dim(CP2)*dim(SU3) = 32": 32,
    "2*dim(CP2)^2 = 32": 32,
    "(dim(CP2)+2)^2 = 36": 36,
    "dim(G)*dim(M)/2 = 16": 16,
    "C_A*Vol(S2) = 3*4pi = 12pi": 12*np.pi,
    "C_A*2*pi = 6pi": 6*np.pi,
}

print("\n  Testing candidate C values:")
for name, C in candidates_theory.items():
    factor = np.sqrt(V_CP2 / C)
    diff_pct = abs(factor - 0.61) / 0.61 * 100
    marker = " *** GOOD" if diff_pct < 5 else ""
    if diff_pct < 20:  # only show reasonable ones
        print(f"    {name:35s} C={C:8.4f}  factor={factor:.4f}  diff={diff_pct:.1f}%{marker}")

# ============================================================
# KEY INSIGHT: The correction comes from the normalization of
# the kinetic term in the effective 4D action
# ============================================================
print(f"\n{'='*70}")
print("KEY DERIVATION: Normalization of 4D Gauge Kinetic Term")
print(f"{'='*70}")

print("""
Start from D-dimensional Einstein-Yang-Mills on M4 x K:

S = ∫ d^Dx sqrt(-G) [ R/(2kappa^2_D) - 1/(4g^2_D) F_{MN}F^{MN} ]

For KK metric ansatz:
  ds^2 = g_{mu nu} dx^mu dx^nu + g_{mn}(dy^m + A^a_mu K^a_m dx^mu)(dy^n + A^b_nu K^b_n dx^nu)

The gauge fields A^a_mu come from the METRIC (gravitational KK), 
not from a higher-dimensional gauge field.

The 4D effective action:
  S_4d = ∫ d^4x sqrt(-g_4) [ R_4/(2kappa^2_4) - 1/4 * I_{ab} * F^a_{mu nu} F^{b,mu nu} ]

where:
  kappa^2_4 = kappa^2_D / Vol(K)
  I_{ab} = (Vol(K)/kappa^2_D) * ∫ K^a_m K^b_n g^{mn} sqrt(g_K) / Vol(K)
         = (1/kappa^2_4) * (1/Vol(K)) * ∫ K^a_m K^b_n g^{mn} sqrt(g_K)
  Wait, let me be more careful...

Actually, from the Einstein-Hilbert term:
  R(D) gives the 4D gauge kinetic term as:
  L_gauge = -(1/4) * (Vol(K)/kappa^2_D) * (1/Vol(K)) * ∫ K^a K^b g^{mn} sqrt(g) * F^a F^b
          = -(1/4) * (1/kappa^2_4) * I * F^a F^b

where I = (1/Vol(K)) * ∫ K^a_m K^b_n g^{mn} sqrt(g_K) d^n y

So the 4D gauge coupling is:
  1/g^2_{4d} = 1/kappa^2_4 * I = M_Pl^2 / (8*pi) * I

Wait: kappa^2_4 = 8*pi*G_N = 8*pi/M_Pl^2
So: 1/g^2_{4d} = M_Pl^2/(8*pi) * I

This seems too large. Let me check...

Actually, the kinetic term from KK is:
  L_KK = -1/4 * (Vol(K)/kappa^2_D) * (∫ K^a K^b g^{mn} sqrt(g) / Vol(K)) * F^a F^b

And 1/kappa^2_4 = Vol(K)/kappa^2_D

So: L_KK = -1/4 * (1/kappa^2_4) * I * F^a F^b

where I = (1/Vol(K)) * ∫ K^a_m K^a_n g^{mn} sqrt(g)  (for diagonal)

Comparing with standard 4D Yang-Mills:
  L_YM = -1/(4g^2) * F^a F^a

We get: 1/g^2 = I / kappa^2_4 = I * M_Pl^2 / (8*pi)

For S2: I = 8pi/3, M_Pl ~ 10^18 GeV
  => 1/g^2 ~ (8pi/3) * (10^18)^2 / (8pi) = (10^18)^2 / 3
  => g^2 ~ 3 * 10^{-36}

This is the gravitational-strength coupling, not the SM coupling!
So the SCVC must have an additional mechanism to enhance the coupling.

In SCVC, the key point is that the gauge fields come from the CP2 
component of the internal space, and the CP2 metric has curvature ~ 1/R^2_KK
not ~ 1/M_Pl^2. This means the KK scale R_KK is much larger than 1/M_Pl.
The 4D Planck scale is M_Pl^2 = Vol(K) * M^{D-2}_D, and the KK scale is 1/R.
The gauge coupling is g^2 ~ (M_Pl * R)^-2 or similar.

The crucial point for our task: the geometric correction factor does NOT 
involve the overall scale (M_Pl, R_KK, etc.) — it only involves the 
RELATIVE normalization between different gauge groups from different 
components of the internal manifold.

For the ratio g^2_2/g^2_3:
  g^2_2/g^2_3 = I_CP2 / I_S2  (inverse of I ratio)
  
This is independent of the overall scale!
And the geometric correction factor for g2 is already known: sqrt(pi/4).
This correction is applied multiplicatively to g2.

If the same correction pattern applies to g3:
  correction_g3 = correction_g2 * sqrt(I_CP2/I_S2) or something...

Let me compute: if g2_geom and g3_geom are the geometric predictions, and
  g2_corrected = g2_geom * sqrt(pi/4)
  
then the g3 correction relative to g2 is:
  g3/g2 |_corrected = g3_geom/g2_geom * (correction_g3/correction_g2)
                     = sqrt(I_S2/I_CP2) * R
  
where R = correction_g3 / correction_g2.

We know: g3/g2 |_SM at M_KK ~ sqrt(alpha_s/alpha_2) ~ ???
And the SCVC geometric prediction gives a specific ratio.

Actually, let me think about this differently. The file says:
  alpha_s(M_KK) ~ 1/30 (SCVC prediction)
  alpha_s(M_KK) ~ 1/49 (SM extrapolation, needed)
  
So the correction factor is 30/49 ≈ 0.612.
alpha_s_corrected = alpha_s_geom * 0.612

This is a factor on alpha_s directly, or equivalently:
  g3_corrected = g3_geom * sqrt(0.612) = g3_geom * 0.782

Hmm, actually: alpha_s = g3^2/(4*pi)
  alpha_s_corrected/alpha_s_geom = (g3_corrected/g3_geom)^2 = 0.612
  g3_corrected/g3_geom = sqrt(0.612) = 0.782

But the file says "multiply by ~0.61", referring to the correction on alpha_s.
So target correction on alpha_s = 0.61.
Target correction on g3 = sqrt(0.61) = 0.782.

Now, the g2 correction is sqrt(pi/4) ≈ 0.886. This is a correction on g2.
(as stated: "g2: deviation 0.19% after sqrt(pi/4) geometric normalization correction")

So the question: what geometric factor gives ~0.61 for alpha_s?
alpha_s correction = (g3_correction)^2 = Vol(CP2)/C
=> C = Vol(CP2) / 0.61 = (pi^2/2) / 0.61 = 4.9348/0.61 = 8.09

Hmm, that's close to 8 = dim(SU3)? 

Vol(CP2)/dim(SU3) = pi^2/2 / 8 = pi^2/16 = 0.6169
And 0.6169... sqrt of this on g would be sqrt(0.6169) = 0.785.

Wait, I'm confusing myself. Let me be clear:

For g2: correction_factor = sqrt(pi/4). This is applied to g2.
  g2_corrected = g2_geom * sqrt(pi/4)
  
For g3: we need correction_factor such that:
  alpha_s_corrected = alpha_s_geom * 0.61
  => g3_corrected = g3_geom * sqrt(0.61)
  => g3 correction on coupling = sqrt(0.61) ≈ 0.782

For alpha_s correction of 0.61:
  This is alpha_s_correction = Vol(CP2)/C
  => C = Vol(CP2) / 0.61 = pi^2/2 / 0.61 ≈ 8.09

Close to dim(SU3) = 8! But not exactly 8.
pi^2/2 / 8 = pi^2/16 ≈ 0.6169. This is within 1% of 0.61!

Let me check: 0.6169 / 0.61 = 1.011. 1.1% off.
And the g2 correction had 0.19% deviation... 

Actually, the file says g2 deviation is 0.19% AFTER correction.
And g1 deviation is 0.3% WITHOUT correction.

So if the g3 correction is Vol(CP2)/dim(SU3) = pi^2/16 ≈ 0.6169,
that gives alpha_s_corrected/alpha_s_geom = 0.6169.

The SM needs 1/30 → 1/49, factor = 30/49 = 0.6122.
0.6169 vs 0.6122: 0.77% difference.

That's actually quite good! But not as good as 0.19%.

Let me check if there's a better formula...

For S2 with g2:
  correction on g2 = sqrt(Vol(S2)/16) = sqrt(4*pi/16) = sqrt(pi/4)
  
  In terms of alpha_2: correction = pi/4 ≈ 0.785
  But the file doesn't specify the alpha_2 deviation in percentage for the 
  uncorrected case...

Let me try to find a consistent pattern:

For S2: correction on g = sqrt(Vol/16)  => correction on alpha = Vol/16 = 4*pi/16 = pi/4
For CP2: if same C=16: correction on alpha = Vol(CP2)/16 = pi^2/32 = 0.3086

That's way too small (70% reduction vs needed 39%).

If C = dim(G): 
For S2: correction on alpha = Vol(S2)/dim(SO3) = 4*pi/3 ≈ 4.19 > 1 (enhancement, not reduction)
No, that doesn't work for S2.

If C = dim(G)^2 / dim(M):
For S2: C = 9/2 = 4.5. Vol/C = 4*pi/4.5 = 2.79. No.

OK let me try a completely different approach. Let me check if:
alpha_s correction = (I_CP2 / Vol(CP2)) / (I_S2 / Vol(S2)) * (pi/4)

= (5/6) / (2/3) * (pi/4)
= (5/4) * (pi/4)
= 5*pi/16 ≈ 0.981

No, that's way too close to 1.

What about: alpha_s correction = (Vol(CP2)/dim(SU3)) / (Vol(S2)/dim(SO3))?
= (pi^2/2 / 8) / (4*pi / 3)
= (pi^2/16) / (4*pi/3)
= pi^2/16 * 3/(4*pi)
= 3*pi/64 ≈ 0.147

No.

Hmm. Let me try: 
correction = Vol(CP2) / (dim(SU3) * [Vol(S2)/C_S2])
= Vol(CP2) / (8 * [4*pi/16])
= (pi^2/2) / (8 * pi/4)
= (pi^2/2) / (2*pi)
= pi/4 ≈ 0.785

That's the same as the g2 correction! Not what we want.

OK, I think the most promising formula is:
alpha_s correction = Vol(CP2) / dim(SU3) = pi^2/16 = 0.6169

This gives a 1.1% deviation from the target 0.6122. That's pretty good but 
not as perfect as the g2 case (0.19%).

Let me also check if using the Killing-form-corrected I gives a better result.

Let me output all this now and move on.
""")

# ============================================================
# FINAL SUMMARY
# ============================================================
print(f"\n{'='*70}")
print("PATH A: FINAL SUMMARY")
print(f"{'='*70}")

V_CP2 = volume_cp2()
dim_SU3 = 8
dim_SO3 = 3

# Candidate 1: Vol(CP2)/dim(SU3)
c1 = V_CP2 / dim_SU3
print(f"\nCandidate 1: alpha_s correction = Vol(CP2)/dim(SU3) = {c1:.6f}")
print(f"  = pi^2/16 = {c1:.6f}")
print(f"  Target: 30/49 = {30/49:.6f}")
print(f"  Deviation: {abs(c1 - 30/49)/(30/49)*100:.2f}%")

# Candidate 2: Vol(CP2)/16 (same C as S2)
c2 = V_CP2 / 16
print(f"\nCandidate 2: alpha_s correction = Vol(CP2)/16 = {c2:.6f}")
print(f"  = pi^2/32 = {c2:.6f}")
print(f"  Deviation: {abs(c2 - 30/49)/(30/49)*100:.2f}%")

# Candidate 3: Vol(CP2)/C where C = 16 * dim(SU3)/dim(SO3)
C3 = 16 * dim_SU3 / dim_SO3
c3 = V_CP2 / C3
print(f"\nCandidate 3: C = 16*dim(SU3)/dim(SO3) = {C3:.4f}")
print(f"  alpha_s correction = Vol/C = {c3:.6f}")
print(f"  Deviation: {abs(c3 - 30/49)/(30/49)*100:.2f}%")

# Candidate 4: explicit C from geometry
# I_CP2 = 5*pi^2/12, I_S2 = 8*pi/3
# C_S2 = 16 =? (dim(SO3)+1)*4? No, 3*4=12.
# Or C = dim(G) * dim(M)? S2: 3*2=6. No.
# Or C = 2^(dim(M)+2)? S2: 2^4=16. Yes! CP2: 2^6=64 => alpha_s correction = pi^2/128
C4 = 2**(4+2)  # dim(CP2)=4, +2
c4 = V_CP2 / C4
print(f"\nCandidate 4: C = 2^(dim(M)+2) = 2^6 = 64")
print(f"  alpha_s correction = {c4:.6f}")

# Candidate 5: correction from I ratio
# alpha_s_correction = (I_CP2/Vol_CP2) / (I_S2/Vol_S2) * (pi/4)
I_CP2_val = 5 * np.pi**2 / 12
I_S2_val = 8 * np.pi / 3
c5 = (I_CP2_val/V_CP2) / (I_S2_val/V_S2) * (np.pi/4)
print(f"\nCandidate 5: (I_CP2/Vol)/(I_S2/Vol) * (pi/4) = {c5:.6f}")

# Candidate 6: from Killing-form-corrected I
I_CP2_corrected = I_CP2_val / (4/3)  # Killing form correction
c6 = (I_CP2_corrected/V_CP2) / (I_S2_val/V_S2) * (np.pi/4)
print(f"\nCandidate 6: with Killing form correction = {c6:.6f}")

# Candidate 7: Vol(CP2)/(C_A(SU3)*something)
# Need C such that Vol/C = 0.6122
C_need = V_CP2 / (30/49)
print(f"\n  Needed C = Vol(CP2)/target = {C_need:.4f}")
print(f"  dim(SU3) = 8")
print(f"  Vol(CP2)/8 = {V_CP2/8:.6f}")
print(f"  4*pi = {4*np.pi:.4f}")
print(f"  dim(SU3)*pi/4 = {8*np.pi/4:.4f}")

# Most promising:
print(f"\n{'*'*60}")
print(f"MOST PROMISING: alpha_s correction = Vol(CP2)/dim(SU3) = pi^2/16")
print(f"  = {np.pi**2/16:.6f}")
print(f"  Target = {30/49:.6f}")
print(f"  Ratio  = {np.pi**2/16 / (30/49):.6f}")
print(f"  This means: alpha_s(M_KK) = (1/30) * (pi^2/16)")
print(f"             = 1/(30 * 16/pi^2)")
print(f"             = 1/({30*16/np.pi**2:.2f})")
print(f"  vs target of 1/49")
print(f"  Difference: {abs(30*16/np.pi**2 - 49)/49*100:.2f}%")
print(f"{'*'*60}")

print("\nDone.")
