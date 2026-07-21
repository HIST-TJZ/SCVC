import numpy as np
from scipy.integrate import nquad
from scipy.special import beta as beta_func

# ============================================================
# PATH A: CP2 Killing Normalization Analysis
# ============================================================

def volume_cp2():
    """Vol(CP2) = pi^2/2 with Fubini-Study metric"""
    return np.pi**2 / 2

def volume_s2(R=1.0):
    return 4 * np.pi * R**2

def killing_s2(R=1.0):
    """I_S2 = 8*pi*R^4/3 (per Killing vector)"""
    return 8 * np.pi * R**4 / 3

print("="*70)
print("PATH A: CP2 Killing Normalization — Analytical Computation")
print("="*70)

# --- S2 known data ---
I_S2 = killing_s2()
V_S2 = volume_s2()
print(f"\nS2 = SO(3)/SO(2):")
print(f"  Vol(S2)       = {V_S2:.6f}")
print(f"  I_Killing     = {I_S2:.6f}")
print(f"  I/Vol         = {I_S2/V_S2:.6f}")
print(f"  g2 correction = sqrt(pi/4) = {np.sqrt(np.pi/4):.6f}")
print(f"  sqrt(Vol/16)  = {np.sqrt(V_S2/16):.6f}")

# --- CP2 as S5/U(1) Hopf fibration ---
print(f"\nCP2 = SU(3)/[SU(2)xU(1)] = S^5/U(1):")
print(f"  Vol(S5, R=1)  = pi^3 = {np.pi**3:.6f}")
print(f"  Vol(CP2)      = pi^3/(2pi) = pi^2/2 = {np.pi**2/2:.6f}")

# Killing normalization on S^5 (per SO(6) generator)
# For S^n, a Killing vector rotating in one plane has squared norm sin^2(theta).
# Integral: ∫ sin^2 theta * Vol(S^{n-1}) * sin^{n-1} theta * R^{n+2} dtheta
# = Vol(S^{n-1}) * R^{n+2} * ∫_0^pi sin^{n+1} theta dtheta

# For S^5 (n=5): Vol(S^4) * ∫_0^pi sin^6 theta dtheta
# Vol(S^4) = 2*pi^{5/2} / Gamma(5/2) = 2*pi^{5/2} / (3*sqrt(pi)/4) = 8*pi^2/3
# ∫_0^pi sin^6 theta dtheta = 5*pi/16

vol_S4_exact = 8 * np.pi**2 / 3
int_sin6_exact = 5 * np.pi / 16
I_S5_exact = vol_S4_exact * int_sin6_exact

print(f"\n  Vol(S^4)      = 8*pi^2/3 = {vol_S4_exact:.6f}")
print(f"  integral(sin^6)= 5*pi/16  = {int_sin6_exact:.6f}")
print(f"  I_S5 (1 gen)  = 5*pi^3/6 = {I_S5_exact:.6f}")

# SU(3) Killing vectors on CP2 descend from SO(6) generators on S5
# that commute with the Hopf U(1). 
# Since Hopf U(1) (diag(e^itheta)) is NOT in SU(3) (it's trace=3 not 0),
# the SU(3) Killing vectors are purely horizontal.
# 
# For Riemannian submersion S5 -> CP2 with fiber length 2*pi:
# I_CP2 = I_S5 / (2*pi)

I_CP2_exact = I_S5_exact / (2 * np.pi)
print(f"\n  I_CP2 (1 gen) = I_S5/(2pi) = 5*pi^2/12 = {I_CP2_exact:.6f}")
print(f"  Vol(CP2)      = pi^2/2 = {np.pi**2/2:.6f}")
print(f"  I/Vol(CP2)    = 5/6 = {5/6:.6f}")

V_CP2 = volume_cp2()

# --- Geometric correction factor analysis ---
print(f"\n{'='*70}")
print("GEOMETRIC CORRECTION FACTOR ANALYSIS")
print(f"{'='*70}")

target_factor = 0.61  # need to multiply alpha_s by ~0.61 to fix

# The g2 correction factor is sqrt(pi/4) = sqrt(Vol(S2)/16).
# Let's test if a similar pattern works for CP2.

print(f"\nPattern: factor = sqrt(Vol(M) / C)")
print(f"  S2:  C=16, factor = sqrt(4pi/16) = sqrt(pi/4) = {np.sqrt(np.pi/4):.6f}")
print(f"  CP2: need factor = {target_factor}")

# Test various C candidates
candidates = [
    ("16 (same as S2)", 16),
    ("4*pi", 4*np.pi),
    ("8*pi/3", 8*np.pi/3),
    ("pi^2", np.pi**2),
    ("2*pi", 2*np.pi),
    ("C_A*2*pi (3*2pi)", 6*np.pi),
    ("C_A*4 (3*4)", 12),
    ("C_A*dim(CP2) (3*4)", 12),
    ("dim(SU3)*2 (8*2)", 16),
    ("4*dim(CP2) (4*4)", 16),
    ("2*dim(SU3) (2*8)", 16),
]

for name, C in candidates:
    factor = np.sqrt(V_CP2 / C)
    marker = " *** CLOSE" if abs(factor - target_factor) < 0.05 else ""
    print(f"  C={name:30s} factor = {factor:.6f}{marker}")

# Reverse-engineer C
C_target = V_CP2 / target_factor**2
print(f"\n  Target C = Vol(CP2)/0.61^2 = {C_target:.4f}")

# Check if C_target equals any nice expression
nice_checks = [
    ("2*pi^2/3", 2*np.pi**2/3),
    ("4*pi", 4*np.pi),
    ("3*pi", 3*np.pi),
    ("pi^2/sqrt(2)", np.pi**2/np.sqrt(2)),
    ("8*pi/3", 8*np.pi/3),
    ("(2*pi)^2/3", 4*np.pi**2/3),
    ("5*pi/2", 5*np.pi/2),
    ("dim(SU3)*pi/2", 8*np.pi/2),
]
print()
for name, val in nice_checks:
    diff_pct = abs(val - C_target) / C_target * 100
    marker = " *** GOOD" if diff_pct < 5 else ""
    print(f"  {name:20s} = {val:.4f}  (diff: {diff_pct:.1f}%){marker}")

# ============================================================
# The g2 correction: deeper analysis
# ============================================================
print(f"\n{'='*70}")
print("DEEP ANALYSIS: Where does sqrt(pi/4) come from?")
print(f"{'='*70}")

# The KK ansatz for metric:
# ds^2 = g_mu_nu dx^mu dx^nu + g_mn (dy^m + K^a_m A^a_mu dx^mu)(dy^n + K^b_n A^b_nu dx^nu)
#
# From D-dimensional Einstein-Hilbert:
# S = 1/(2*kappa^2_D) ∫ d^D x sqrt(-G) R
#
# The 4D gauge kinetic term:
# L_gauge = -1/4 * Vol(K)/(2*kappa^2_D) * I * F^a_mu_nu F^{a,mu nu}
#
# where I = (1/Vol(K)) ∫ K^a_m K^b_n g^{mn} sqrt(g_K)
#
# Standard 4D: L = -1/(4g^2_4d) F^a F^a
# So: 1/g^2_4d = Vol(K)/(2*kappa^2_D) * I
#
# Now, the D-dimensional gravitational coupling:
# kappa^2_D = 8*pi*G_D (in natural units)
# M_{Pl,D}^{D-2} = 1/(8*pi*G_D) = 1/kappa^2_D
#
# 4D Planck mass: M_{Pl,4}^2 = M_{Pl,D}^{D-2} * Vol(K)
# So: kappa^2_4 = kappa^2_D / Vol(K)
#
# Therefore:
# 1/g^2_4d = 1/(2*kappa^2_4) * I
#          = M_{Pl}^2 / (16*pi) * I
#
# For different gauge groups from different isometry factors:
# g1, g2, g3 all come from the SAME D-dimensional gravitational coupling 
# but DIFFERENT internal manifold factors (or different components of the 
# same internal manifold).
#
# In SCVC: CP2 x S2 (or similar product manifold)
# The isometry of S2 gives SU(2) ~ SO(3)
# The isometry of CP2 gives SU(3)
#
# Both come from the same D-dimensional kappa^2_D and the same Vol(total).
# But I_S2 and I_CP2 differ.
#
# g^2_2 / g^2_3 = I_CP2 / I_S2

ratio_I = I_CP2_exact / I_S2
print(f"\n  I_CP2 / I_S2 = {ratio_I:.6f}")
print(f"  (This would give g^2_3/g^2_2 = I_CP2/I_S2 = {ratio_I:.6f})")

# But wait, the g2 correction is sqrt(pi/4), meaning:
# g2_corrected = g2_raw * sqrt(pi/4)
# g2_raw is the "uncorrected" geometric prediction
# 
# If g2_raw already uses I_S2, then:
# g2_raw^2 \propto 1/I_S2
# g2_corrected^2 \propto 1/(I_S2 * pi/4) = 1/(I_S2 * Vol(S2)/16)
# 
# This means the geometric I_S2 needs to be multiplied by Vol(S2)/16 
# to match the field theory normalization. Equivalent to:
# I_eff = I_S2 * Vol(S2)/16 = (8*pi/3) * (pi/4) = 2*pi^2/3

I_S2_eff = I_S2 * V_S2 / 16
print(f"\n  I_S2_effective = I_S2 * Vol(S2)/16 = {I_S2_eff:.6f}")
print(f"  (This is the normalization needed to match field theory)")

# So the "correction factor" for any manifold M is:
# factor = sqrt( (I_M * Vol(M)/C_M) / (I_S2 * Vol(S2)/C_S2) )  for relative
# or:   factor = sqrt( Vol(M) / C )  for absolute (where C matches S2 C=16)
#
# If we assume the same C=16 for CP2:
factor_cp2_sameC = np.sqrt(V_CP2 / 16)
print(f"\n  Assuming same C=16:")
print(f"  CP2 correction = sqrt(Vol(CP2)/16) = {factor_cp2_sameC:.6f}")
print(f"  Target = 0.61, ratio = {factor_cp2_sameC/0.61:.4f}")

# ============================================================
# Alternative: factor from I/Vol ratio
# ============================================================
print(f"\n{'='*70}")
print("ALTERNATIVE: Correction from I/Vol and group theory")
print(f"{'='*70}")

# The SU(2) and SU(3) gauge generators in field theory are normalized by:
# Tr(T^a T^b) = (1/2) * delta^{ab}  (fundamental representation)
#
# The geometric Killing vectors satisfy the isometry algebra:
# [K^a, K^b] = f^{abc} K^c
# with structure constants f^{abc} from SU(2) or SU(3).
#
# The normalization of K^a is fixed by the metric on the internal manifold.
# The relationship between the geometric K^a and field theory T^a is:
# K^a = lambda * T^a (as differential operators)
#
# where lambda is the normalization factor.
# 
# For S2: I_S2 = (1/3) * Vol(S2) * R^2 * C_A(SO3) 
# Actually: I_S2/Vol(S2) = 2/3 (with R=1)
# C_A(SO3) = C_A(SU2) = 2
# dim(SO3) = 3
#
# I_S2 = Vol(S2) * (2/3) = Vol(S2) * (C_A/dim) * (dim/(dim+1)?)
# Let me check: C_A/dim = 2/3 ✓ (exactly I_S2/Vol(S2)!)
# 
# For CP2: I_CP2/Vol(CP2) = 5/6
# C_A(SU3)/dim(SU3) = 3/8 = 0.375
# dim(CP2)/dim(SU3) = 4/8 = 0.5
#
# 5/6 = 0.833. This doesn't match C_A/dim = 0.375.
#
# But 5/6 = (dim(CP2)+1)/dim(CP2) = 5/4 = 1.25. No.
# 5/6 = dim(SU3)/C_A(SU3) * something?
# dim/C_A = 8/3 = 2.667. 5/6 = 0.833. Not a simple relationship.
#
# Hmm. Let me try:
# I/Vol = (dim(G) + dim(M)) / (2 * dim(G)) ?
# S2: (3+2)/(2*3) = 5/6. But I_S2/Vol = 2/3 = 4/6. Close but not exact.
#
# Or: I/Vol = (dim(G/H) + 1) / (dim(G/H) + 2)?
# S2: (2+1)/(2+2) = 3/4. No.
# 
# I/Vol = dim(G/H) / (dim(G/H) + 1)?
# S2: 2/3 ✓
# CP2: 4/5 = 0.8. But actual is 5/6 = 0.833. Close but not exact.
#
# So 4/5 vs 5/6. The difference is: 
#   For symmetric spaces of rank 1:
#   S2 (rank 1): I/Vol = dim/(dim+1) holds? dim=2, 2/3 ✓
#   CP2 (rank 1): dim=4, 4/5 = 0.8. But actual = 5/6 = 0.833.
#   
#   Hmm, maybe there's a correction for complex projective spaces.
#
# Let me verify the exact I_CP2 more carefully.
# 
# Our derivation: I_CP2 = I_S5 / (2*pi)
# I_S5 = vol(S4) * ∫ sin^6 theta
# 
# But wait: the Killing vector on S5 that corresponds to an SU(3) generator 
# has a specific normalization. The SU(3) generators are a subset of the 
# SO(6) generators, but they may have different normalizations.
#
# In SO(6), the 15 generators are normalized by the Killing form:
# B(X,Y) = 4 * Tr(XY)  (for the vector representation of SO(6))
#
# SU(3) generators embedded in SO(6) via C^3 ≅ R^6:
# For a generator T^a of SU(3) (3x3 complex), the corresponding SO(6) 
# generator is a 6x6 real matrix.
#
# The embedding SU(3) → SO(6) has a specific index:
# For the fundamental 3 of SU(3), the embedding in 6 of SO(6):
# Tr_{SO(6)}(X Y) = 2 * Tr_{SU(3)}(X Y) (???)
#
# Actually, SU(3) ⊂ SO(6) is the embedding where the 3 of SU(3) and its 
# conjugate 3bar together form the 6 of SO(6).
#
# The Dynkin index of the embedding: l = 1 (for standard embedding)
# meaning Tr_{6}(X^2) = l * Tr_{3}(X^2)
# 
# For the standard embedding (3 ⊕ 3bar = 6 of SO(6)):
# Tr_{6}(X^2) = 2 * Tr_{3}(X^2) (trace in 3 plus trace in 3bar)
#
# But the SO(6) Killing vectors on S5 are normalized by the SO(6) Killing form.
# The SU(3) Killing vectors on CP2 descend from these.
#
# The key question: does the Hopf projection S5 → CP2 preserve the 
# normalization of the horizontal Killing vectors?
#
# For a Riemannian submersion pi: S5 → CP2:
# The horizontal lift of a vector field X on CP2 is a vector field X~ on S5.
# For Killing vectors: the horizontal lift of an SU(3) Killing vector 
# is a horizontal SO(6) Killing vector.
#
# The integral on CP2: ∫_{CP2} |K|^2 vol_{CP2}
# = ∫_{S5} |K_horiz|^2 vol_{S5} / (fiber length)
# = ∫_{S5} |K|^2 vol_{S5} / (2*pi)    (since K = K_horiz for SU(3))
#
# And for K corresponding to an SU(3) generator, |K|^2 on S5 is the 
# squared norm of the SO(6) vector field.
# 
# Now, the SO(6) vector field norm: for a generator X of SO(6),
# the Killing vector on S5 has squared norm = <X·p, X·p> at point p∈S5.
# Averaging over S5: <sin^2 theta> * |X|^2 where |X|^2 is the 
# Killing form norm of the generator X.
#
# For the 15 generators of SO(6), all have the same Killing form norm 
# (by simplicity of SO(6)). But when we embed SU(3) in SO(6), the 
# 8 SU(3) generators map to 8 specific SO(6) generators.
#
# Their norms under the SO(6) Killing form are the same as any other 
# SO(6) generator, since SU(3) is a subgroup and the restriction of 
# the Killing form is proportional to the SU(3) Killing form.
#
# SO(6) Killing form: B_{SO6}(X,Y) = 4 * Tr_{vec}(X Y)
# SU(3) Killing form: B_{SU3}(T^a, T^b) = 6 * Tr_{fund}(T^a T^b) 
#                                        = 6 * (1/2) * delta^{ab} 
#                                        = 3 * delta^{ab} (physics norm)
#
# For the embedding SU(3) → SO(6), the induced Killing form:
# B_{SO6}(X_SU3, Y_SU3) = 4 * Tr_{6}(X_SU3 Y_SU3)
#                        = 4 * 2 * Tr_{3}(X_SU3 Y_SU3) 
#                        = 8 * (1/2) * delta^{ab}
#                        = 4 * delta^{ab}
#
# While B_{SU3}(T^a, T^b) = 3 * delta^{ab} (using the same Tr norm)
#
# So the induced metric differs by factor 4/3:
# B_{SO6} = (4/3) * B_{SU3}
#
# This means on S5, the SU(3) generators have norm proportional to 
# B_{SO6} = 4 * delta^{ab}, not B_{SU3} = 3 * delta^{ab}.

# Let me recompute I_CP2 with this correction.
# The I_S5 we computed uses the SO(6) Killing form normalization.
# When we project to CP2 and identify with SU(3) gauge generators,
# we need to account for the ratio of Killing forms.

killing_form_ratio = 4.0 / 3.0  # B_SO6 / B_SU3 (induced)
I_CP2_corrected = I_CP2_exact / killing_form_ratio

print(f"\n  Killing form ratio B_SO6/B_SU3 = {killing_form_ratio:.4f}")
print(f"  I_CP2 (corrected) = {I_CP2_corrected:.6f}")
print(f"  I_CP2_corrected/Vol(CP2) = {I_CP2_corrected/V_CP2:.6f}")

# ============================================================
# FINAL: compute all candidate factors
# ============================================================
print(f"\n{'='*70}")
print("FINAL: All candidate correction factors for alpha_s")
print(f"{'='*70}")

# 1. sqrt(Vol(CP2)/16) — naive extension of S2 formula
f1 = np.sqrt(V_CP2 / 16)
print(f"\n  1. sqrt(Vol/16)              = {f1:.6f}  (naive S2 extension)")

# 2. sqrt(Vol(CP2)/(4*pi)) — another naive guess
f2 = np.sqrt(V_CP2 / (4*np.pi))
print(f"  2. sqrt(Vol/4pi)             = {f2:.6f}")

# 3. Using I/Vol ratio
# factor_su3/factor_su2 = sqrt((I_CP2/Vol_CP2) / (I_S2/Vol_S2) * something)
# Correction = sqrt(Vol(CP2)/16) * sqrt( (I_CP2/Vol_CP2) / (I_S2/Vol_S2) )
ratio_IV = (I_CP2_exact/V_CP2) / (I_S2/V_S2)
f3 = np.sqrt(V_CP2 / 16) * np.sqrt(ratio_IV)
print(f"  3. sqrt(Vol/16)*sqrt(IVratio)= {f3:.6f}")

# 4. Direct I comparison
f4 = np.sqrt(I_CP2_exact / I_S2) * np.sqrt(np.pi/4)
print(f"  4. sqrt(I_ratio)*sqrt(pi/4)  = {f4:.6f}")

# 5. With Killing form correction
f5 = np.sqrt(I_CP2_corrected / I_S2) * np.sqrt(np.pi/4)
print(f"  5. sqrt(ICorr_ratio)*sqrt(pi/4) = {f5:.6f}")

# 6. sqrt(I_CP2/(C_A*Vol_CP2)) * something
f6 = np.sqrt(I_CP2_exact / (3 * V_CP2))
print(f"  6. sqrt(I/(C_A*Vol))          = {f6:.6f}")

# 7. Direct correction: factor = sqrt(I_CP2/I_S2 * 4/pi)
f7 = np.sqrt((I_CP2_exact / I_S2) * (4/np.pi))
print(f"  7. sqrt(Iratio * 4/pi)        = {f7:.6f}")

# 8. The SCVC matching: factor must be about 0.61
# If factor = sqrt(Vol(CP2)/C), then C = Vol/factor^2
# C = pi^2/2 / (target^2)
# The correct C should have a group-theoretic meaning.

print(f"\n  --- All factors vs target 0.61 ---")
for i, f in enumerate([f1, f2, f3, f4, f5, f6, f7], 1):
    diff_pct = abs(f - target_factor) / target_factor * 100
    print(f"  Factor {i}: {f:.6f}  (diff {diff_pct:+.1f}%)")

# ============================================================
# NUMERICAL VERIFICATION
# ============================================================
print(f"\n{'='*70}")
print("NUMERICAL VERIFICATION OF CP2 VOLUME AND KILLING INTEGRALS")
print(f"{'='*70}")

# Fubini-Study metric on CP2 in inhomogeneous coords (z1, z2)
def fs_metric(z):
    """Fubini-Study metric g_{i*bar{j}} at z=(z1,z2)"""
    r2 = np.abs(z[0])**2 + np.abs(z[1])**2
    denom = (1 + r2)**2
    g = np.zeros((2,2), dtype=complex)
    for i in range(2):
        for j in range(2):
            delta = 1.0 if i==j else 0.0
            g[i,j] = ((1+r2)*delta - np.conj(z[i])*z[j]) / denom
    return g

def metric_4x4_real(z):
    """Convert 2x2 complex Hermitian FS metric to 4x4 real metric.
    z = [x1+iy1, x2+iy2], real coords = [x1,y1,x2,y2]
    ds^2 = 2 Re(g_{i*bar{j}} dz^i d*zbar^j)
    """
    gc = fs_metric(z)
    A, B = np.real(gc), np.imag(gc)
    g = np.zeros((4,4))
    for i in range(2):
        for j in range(2):
            g[2*i, 2*j] += 2*A[i,j]
            g[2*i+1, 2*j+1] += 2*A[i,j]
            g[2*i, 2*j+1] += -2*B[i,j]
            g[2*i+1, 2*j] += 2*B[i,j]
    return g

def sqrt_g(z):
    return np.sqrt(np.linalg.det(metric_4x4_real(z)))

# Gell-Mann matrices
def gell_mann_matrices():
    l1 = np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex)
    l2 = np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex)
    l3 = np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex)
    l4 = np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex)
    l5 = np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex)
    l6 = np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex)
    l7 = np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex)
    l8 = np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / np.sqrt(3)
    return [l1,l2,l3,l4,l5,l6,l7,l8]

def killing_cp2(z, T):
    """Killing vector at z for SU(3) generator T.
    Action on homogeneous coords: Z -> (1 + i*eps*T)Z
    Then project back: z_i = Z_i/Z_0 (i=1,2)
    Returns 4-vector [v_x1, v_y1, v_x2, v_y2]
    """
    Z = np.array([1.0+0j, z[0], z[1]])
    dZ = 1j * (T @ Z)
    dz = np.zeros(2, dtype=complex)
    for i in range(2):
        dz[i] = (dZ[i+1]*Z[0] - Z[i+1]*dZ[0]) / (Z[0]**2)
    return np.array([np.real(dz[0]), np.imag(dz[0]),
                     np.real(dz[1]), np.imag(dz[1])])

def killing_integrand(z_flat, a):
    """Integrand |K^a|^2 sqrt(g) at 4D point"""
    zc = np.array([z_flat[0]+1j*z_flat[1], z_flat[2]+1j*z_flat[3]])
    K = killing_cp2(zc, gell_mann_matrices()[a])
    g_real = metric_4x4_real(zc)
    g_inv = np.linalg.inv(g_real)
    sg = sqrt_g(zc)
    return K @ g_inv @ K * sg

# Quick numerical check of CP2 volume
print("\nNumerical CP2 volume (integrating over box [-L,L]^4)...")
for L in [3.0, 5.0, 8.0]:
    def vol_int(*args):
        z = np.array([args[0]+1j*args[1], args[2]+1j*args[3]])
        return sqrt_g(z)
    v, err = nquad(vol_int, [[-L,L]]*4, opts={'limit':40,'epsabs':1e-3,'epsrel':1e-3})
    print(f"  L={L:.0f}: Vol = {v:.6f}  (analytic = {np.pi**2/2:.6f})  err={err:.2e}")

print("\nDone with Path A analysis.")
