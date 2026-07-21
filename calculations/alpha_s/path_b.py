import numpy as np
import math

# ============================================================
# PATH B: CP2 KK SPECTRUM & SU(3) BETA FUNCTION THRESHOLD CORRECTIONS
# ============================================================

print("="*70)
print("PATH B: CP2 KK Spectrum & Beta Function Threshold Corrections")
print("="*70)

# --- Part 1: CP2 KK energy levels ---
print("\n" + "-"*50)
print("Part 1: CP2 KK Energy Levels")
print("-"*50)

# CP2 = SU(3)/[SU(2)xU(1)] is a symmetric space.
# The KK spectrum comes from the Laplacian on CP2 with Fubini-Study metric.
#
# Eigenvalues of the Laplacian on CP^n:
# lambda_k = 4k(k+n)  for the Fubini-Study metric with holomorphic 
# sectional curvature = 4.
# For CP2 (n=2): lambda_k = 4k(k+2), k = 0,1,2,...
#
# The degeneracy for the k-th level:
# d_k = (2k+n) * [Gamma(k+n)/Gamma(k+1)/Gamma(n)]^2 / n
# For n=2: d_k = (2k+2) * (k+1)^2 * k^2 / 4 = (k+1)^3 * k / 2 (???)
# Let me compute more carefully.
#
# For CP^n: d_k = (n+2k) * C(n+k-1, k)^2
# For n=2: d_k = (2+2k) * C(1+k, k)^2 = (2k+2) * (k+1)^2 = 2*(k+1)^3
#
# Wait, let me verify:
# d_0 = 2*(1)^3 = 2 (zero mode: 2 real scalars from the 2 complex dims? No...)
# Actually, the scalar Laplacian on CP^n has multiplicity:
# d_k^{scalar} = (n+2k)/n * binomial(n+k-1, k)^2
# For n=2: d_k = (2+2k)/2 * binomial(k+1, k)^2 = (k+1) * (k+1)^2 = (k+1)^3
#
# d_0 = 1 (constant function)
# d_1 = 8
# d_2 = 27
# d_3 = 64

print("\nLaplacian eigenvalues on CP2 (Fubini-Study metric):")
print("  lambda_k = 4k(k+2),  k = 0, 1, 2, ...")
print()

for k in range(6):
    lam = 4 * k * (k + 2)
    deg = (k + 1)**3
    energy = np.sqrt(lam)  # in units of 1/R (KK scale)
    print(f"  k={k}: lambda={lam:3d},  E/R^(-1)={energy:8.4f},  degeneracy={deg:4d}")

# Now, CP2 has isometry SU(3), so there are also vector and tensor harmonics.
# 
# For the gauge field A_m on CP2, the KK expansion involves:
# - Scalar harmonics (for the 4D scalars from A_m)
# - Vector harmonics (for the 4D vectors from off-diagonal metric components)
# - The gauge group from isometry gives massless 4D vectors
#
# For our purpose (SU(3) beta function), we need the KK modes of:
# 1. SU(3) gauge bosons (massive KK excitations of the 4D gluons)
# 2. Fermions (if any) in the bulk
# 3. Scalars from the internal components of gauge fields
#
# The gauge boson KK spectrum on CP2:
# The 4D gluons are the zero modes from the SU(3) isometry.
# Their KK excitations are massive spin-1 particles in 4D.
# 
# The spectrum for vector harmonics on CP2:
# These are 1-forms on CP2 that are eigenmodes of the Hodge Laplacian.
# For CP^n, the eigenvalues for coexact 1-forms are:
# lambda_k^{(1)} = 4k(k+n+1) + 2n,  k >= 1
# For CP2 (n=2): lambda_k = 4k(k+3) + 4 = 4[k(k+3)+1], k >= 1
#
# And for exact 1-forms (from scalar gradients): same as scalar + curvature

print("\nVector harmonic eigenvalues for SU(3) gauge boson KK modes:")
print("  (coexact 1-forms on CP2)")
for k in range(1, 6):
    lam = 4 * k * (k + 3) + 4
    deg = 2 * (k+1) * (k+2) * (2*k+3) // 6  # multiplicity for vector harmonics
    # Actually, let me use the formula for CP^n coexact 1-forms
    energy = np.sqrt(lam)
    # Multiplicity formula for CP^n: 
    # For coexact 1-forms at level k (k>=1), multiplicity is more complex.
    # Let me use: dim = 2 * binomial(n+k, k+1) * binomial(n+k-1, k)
    # For n=2: dim_k = 2 * binomial(k+2, k+1) * binomial(k+1, k)
    #                = 2 * (k+2) * (k+1) = 2(k+1)(k+2)
    dim_k = 2 * (k+1) * (k+2)
    print(f"  k={k}: lambda={lam:3d},  E/R^(-1)={energy:8.4f},  dim={dim_k:4d}")

# --- Part 2: SU(3) Beta Function ---
print("\n" + "-"*50)
print("Part 2: SU(3) Beta Function & KK Thresholds")
print("-"*50)

# The 1-loop beta function for SU(3) with N_f flavors:
# beta(alpha_s) = -b_0 * alpha_s^2 / (2*pi)
# b_0 = 11 - 2*N_f/3  (pure gauge + fermion contributions)
# 
# For SM: N_f = 6, b_0 = 11 - 4 = 7
# 
# Running: 1/alpha_s(mu) = 1/alpha_s(mu_0) + b_0/(2*pi) * ln(mu/mu_0)
#
# KK threshold corrections:
# At each KK mass level M_k, massive modes contribute to the beta function.
# The contribution depends on spin:
# - Spin-1 (gauge boson): delta_b = -11/3 * T(R) [actually for adjoint, it's -11*C_A/3...]

print("\nBeta function coefficient contributions per KK mode:")
print("  (in units of the zero-mode normalization)")

# For a massive gauge boson in representation R of SU(3):
# Contribution to b_0: delta_b = -(11/3) * T(R) [for complex scalar in loop]
# More precisely, for a massive particle of spin s:
# - Real scalar: delta_b = -(1/3) * T(R)
# - Complex scalar: delta_b = -(2/3) * T(R) 
# - Weyl fermion: delta_b = -(2/3) * T(R)
# - Gauge boson (massive): delta_b = -(11/3) * C_A  (for adjoint)
#   Actually, for a massive gauge boson, the contribution changes as 
#   you go through the threshold. Below the mass, it contributes 0 
#   (integrated out). Above the mass, it contributes the same as a 
#   massless gauge boson. At the threshold, there''s a matching correction.
#
# The standard threshold correction: when crossing a mass threshold M,
# the coupling changes by:
# 1/alpha(above) = 1/alpha(below) + delta_b/(2*pi) * ln(M/mu_0)
#
# For the full KK tower, the sum over all thresholds gives:
# Delta(1/alpha_s) = sum_{KK modes} delta_b_i / (2*pi) * ln(M_KK * E_i / mu_0)
#
# where E_i are the dimensionless KK energies.

# Let me compute the cumulative effect.

print("\n--- Massive gauge boson KK modes ---")
# Each KK level has massive spin-1 particles in the adjoint of SU(3)
# Contribution to b_0 from each massive gauge boson:
# Above threshold: contributes -11*C_A/3 = -11*3/3 = -11 per mode
# But below threshold: contributes 0
# At threshold, the step in 1/alpha is:
# delta(1/alpha) = 11/(2*pi) * ln(M/mu_0)  (going from below to above)

# For the KK tower starting at M_KK, with energies E_k:
# Sum_k d_k * 11/(2*pi) * ln(E_k * M_KK / M_KK) 
# = 11/(2*pi) * sum_k d_k * ln(E_k)
# where d_k is the multiplicity at level k, E_k = sqrt(lambda_k)

print("\nKK gauge boson tower contribution to 1/alpha_s at M_KK:")
total_contrib = 0.0
for k in range(1, 8):
    lam = 4 * k * (k + 3) + 4
    E_k = np.sqrt(lam)
    dim_k = 2 * (k+1) * (k+2)
    contrib = dim_k * np.log(E_k)
    total_contrib += contrib
    print(f"  k={k}: E={E_k:.4f}, dim={dim_k:3d}, contrib={contrib:.2f}")

delta_inv_alpha = 11/(2*np.pi) * total_contrib
print(f"\n  Total sum of d_k*ln(E_k) = {total_contrib:.2f}")
print(f"  Delta(1/alpha_s) = {delta_inv_alpha:.2f}")

# But wait, this assumes ALL KK modes are above the threshold.
# The running from M_KK down to M_Z involves integrating out these modes.
# The full effect: at scales mu < M_KK, all KK modes are integrated out.
# The zero-mode (SM) beta function runs from M_KK down to M_Z.
# The KK modes affect the matching at M_KK.

print("\n--- Scalar KK modes from A_m ---")
# The internal components A_m of the higher-dimensional gauge field 
# give 4D scalars. These are in the adjoint of SU(3).
# For CP2 with dim=4, A_m has 4 components.
# The scalar KK spectrum uses the scalar Laplacian eigenvalues.
# Each scalar mode contributes delta_b = -(1/3)*C_A = -1 to b_0 (real scalar in adjoint)
# Or more precisely: -(1/3)*T(adj) = -(1/3)*C_A = -1

print("Scalar (from A_m) KK tower contribution:")
total_scalar = 0.0
for k in range(1, 8):
    lam = 4 * k * (k + 2)
    E_k = np.sqrt(lam)
    deg = (k + 1)**3
    # For the 4 internal components: 4 real scalars per mode
    # But one combination gives the Higgs-like modes, and the gauge
    # condition removes some. For a rough estimate, use 4*n_mode.
    # Actually, in KK reduction, the 4D scalars from A_m in adjoint:
    # There are dim(M) = 4 real adjoint scalars.
    # Each scalar KK mode: delta_b per real scalar = -(1/3)*C_A = -1
    # Total per scalar mode: 4 * (-1) = -4
    # But after gauge fixing, some are eaten by massive gauge bosons.
    # The physical scalar spectrum is smaller.
    # Let me compute a rough upper bound first.
    contrib = 4 * deg * np.log(E_k)  # rough upper bound
    total_scalar += contrib
    # print(f"  k={k}: E={E_k:.4f}, deg={deg:3d}, contrib={contrib:.1f}")

delta_scalar = 1/(2*np.pi) * total_scalar  # |delta_b|=1 per mode
print(f"  Rough upper bound Delta(1/alpha_s) = {delta_scalar:.1f}")

# --- Part 3: Landau Pole Analysis ---
print("\n" + "-"*50)
print("Part 3: Landau Pole Analysis")
print("-"*50)

# Current situation (file):
# - SCVC predicts alpha_s(M_KK) ~ 1/30
# - SM extrapolation needs alpha_s(M_KK) ~ 1/49
# - Landau pole at ~10^6 GeV (from SCVC prediction, running UP from M_KK?)
#   Actually, the Landau pole is where 1/alpha_s -> 0 when running UP.
#   If alpha_s(M_KK) = 1/30 and we run UP, the Landau pole occurs at:
#   mu_Landau = M_KK * exp(-2*pi/(b_0 * alpha_s(M_KK)))
#             = M_KK * exp(-2*pi*30/b_0)
#   With b_0 = 7: mu_Landau = M_KK * exp(-60*pi/7) = M_KK * exp(-26.9)
#   That's way below M_KK, not above!
#
#   Wait, maybe I have it backwards. Landau pole from running DOWN?
#   alpha_s = 1/30 at M_KK, running to lower scales:
#   1/alpha_s(mu) = 1/alpha_s(M_KK) + b_0/(2*pi) * ln(mu/M_KK)
#   = 30 + 7/(2*pi) * ln(mu/M_KK)
#   At mu = M_Z ~ 91 GeV: 1/alpha_s = 30 + 7/(2*pi)*ln(91/M_KK)
#   If M_KK ~ 10^16 GeV: ln(91/10^16) = -32.2
#   1/alpha_s = 30 - 7*32.2/(2*pi) = 30 - 35.9 = -5.9
#   That's negative! The coupling would blow up before reaching M_Z.
#   
#   So the problem is running DOWN from M_KK to M_Z.
#   alpha_s(M_KK) = 1/30 is TOO SMALL (coupling too strong at M_KK)?
#   Wait, alpha_s = 1/30 is large (strong coupling). That means 
#   running down makes it even larger, and it hits the Landau pole.
#   
#   The SM needs alpha_s(M_KK) = 1/49 (weaker coupling) so that 
#   running down to M_Z gives the observed alpha_s(M_Z) ≈ 0.118.
#
#   Let me verify:
print("\nRunning alpha_s from M_KK to M_Z:")
M_KK = 1e16  # GeV (typical GUT-scale KK)
M_Z = 91.0   # GeV
b0_SM = 7.0  # 11 - 2*6/3 = 7

alpha_KK_scvc = 1/30
inv_alpha_Z = 1/alpha_KK_scvc + b0_SM/(2*np.pi) * np.log(M_Z/M_KK)
print(f"  SCVC prediction: alpha_s(M_KK) = 1/30 = {alpha_KK_scvc:.4f}")
print(f"  1/alpha_s(M_Z) = {inv_alpha_Z:.2f}")  
print(f"  alpha_s(M_Z)   = {1/inv_alpha_Z:.4f}" if inv_alpha_Z > 0 else f"  LANDAU POLE! (1/alpha < 0)")

alpha_KK_sm = 1/49
inv_alpha_Z_sm = 1/alpha_KK_sm + b0_SM/(2*np.pi) * np.log(M_Z/M_KK)
print(f"\n  SM-extrapolated: alpha_s(M_KK) = 1/49 = {alpha_KK_sm:.4f}")
print(f"  1/alpha_s(M_Z) = {inv_alpha_Z_sm:.2f}")
print(f"  alpha_s(M_Z)   = {1/inv_alpha_Z_sm:.4f}")

# Check observed: alpha_s(M_Z) ≈ 0.118
observed_inv = 1/0.118
print(f"\n  Observed: 1/alpha_s(M_Z) = {observed_inv:.2f}")

# Now, find where the Landau pole is with SCVC prediction
# Landau pole: where 1/alpha_s -> 0 running up from M_KK
# 1/alpha_s(M_KK) + b0/(2*pi)*ln(mu_L/M_KK) = 0
# ln(mu_L/M_KK) = -2*pi/(b0*alpha_s(M_KK)) = -2*pi*30/7 = -60*pi/7
mu_L = M_KK * np.exp(-2*np.pi/(b0_SM * alpha_KK_scvc))
print(f"\n  Landau pole (SCVC, running up from M_KK): {mu_L:.2e} GeV")
print(f"  (Running DOWN, coupling hits Landau pole before M_Z)")

# The file says Landau pole at ~10^6 GeV
# Let me check: what M_KK gives Landau pole at 10^6?
# MU_Landau = 10^6, find alpha_s(M_KK):
# mu_L = M_KK * exp(-2*pi/(b0*alpha_s(M_KK)))
# 10^6 = M_KK * exp(-2*pi/(7*alpha_s))
# If M_KK ~ 10^14: exp(-2*pi/(7*alpha_s)) = 10^-8
# alpha_s = 2*pi/(7*ln(10^8)) = 2*pi/(7*18.42) = 0.0488
# 1/alpha_s = 20.5
# Hmm, close to 1/30 (1/30 = 0.033, alpha_s = 30).

# Let me check: if alpha_s(M_KK) = 1/30, M_KK = ?
# mu_L = M_KK * exp(-60*pi/7)
# For mu_L = 10^6: M_KK = 10^6 * exp(60*pi/7) = 10^6 * exp(26.9) ~ 10^6 * 5e11 ~ 5e17
# So M_KK ~ 5e17 GeV, which is near the GUT scale. But the Landau pole at 10^6 
# is when running in the WRONG direction?

# Wait, let me re-read the file: "Landau 极点在 ~10^6 GeV 而非 GUT 标度"
# This means the Landau pole is at ~10^6 GeV. 
# Running UP from M_Z to M_KK with alpha_s(M_Z) = 0.118:
# 1/alpha_s(mu) = 1/0.118 - 7/(2*pi)*ln(mu/M_Z)
# Landau: 1/0.118 = 7/(2*pi)*ln(mu_L/M_Z)
# mu_L = M_Z * exp(2*pi/(7*0.118)) = 91 * exp(2*pi/0.826) = 91 * exp(7.60)
#       = 91 * 2000 = 1.8e5 GeV
# Hmm, that gives ~10^5, not 10^6. Close though.

# With alpha_s(M_Z) = 0.1181 (PDG 2024):
mu_L_sm = M_Z * np.exp(2*np.pi/(b0_SM * 0.1181))
print(f"\n  SM Landau pole (running UP from M_Z, alpha_s=0.1181): {mu_L_sm:.2e} GeV")

# So the SM itself has a Landau pole at ~10^5 GeV if alpha_s runs with 
# only SM content! But above the top mass, b0 changes, and at higher 
# scales new particles appear...
# 
# Anyway, the file says the SCVC prediction puts the Landau pole at 10^6 GeV
# and we need it at >10^17 GeV. Let me work with that.

# --- Part 4: How much Delta_b0 is needed? ---
print("\n" + "-"*50)
print("Part 4: Required Delta_b0 to Push Landau Pole")
print("-"*50)

# Landau pole condition: 1/alpha_s(mu_L) = 0
# Running FROM M_Z (where we know alpha_s) UP:
# 1/alpha_s(M_Z) + b_eff/(2*pi) * ln(mu_L/M_Z) = 0
# mu_L = M_Z * exp(-2*pi/(b_eff * alpha_s(M_Z)))
# But wait, running UP from M_Z to mu_L should use the beta function 
# ABOVE M_Z, which includes all particles active at those scales.
#
# Actually, let me re-interpret the problem.
# 
# The SCVC prediction is for alpha_s at M_KK. The issue is:
# 1. SCVC says alpha_s(M_KK) ≈ 1/30
# 2. Running from M_KK DOWN to M_Z with SM beta function gives the WRONG alpha_s(M_Z)
# 3. The SCVC prediction has a Landau pole at ~10^6 GeV
#
# The Landau pole at 10^6 means alpha_s blows up before reaching M_Z (when running down)
# OR it means running up from M_KK gives Landau at 10^6.
#
# I think the file means: the SCVC prediction for alpha_s gives a Landau pole 
# at 10^6 GeV (too low, should be at >10^17 GeV). This is because the coupling 
# is too strong (alpha_s too large) at the KK scale.
#
# So the question: what delta_b0 from KK thresholds would change the running 
# such that the Landau pole is pushed above 10^17 GeV?

print("\nAnalysis: Landau pole position vs. b_0 and alpha_s(M_KK)")
print("Landau pole: mu_L where 1/alpha_s(mu_L) = 0")
print("Running UP from M_KK: 1/alpha_s(M_KK) + b_0/(2*pi) * ln(mu_L/M_KK) = 0")
print()

# With SCVC prediction alpha_s(M_KK) = 1/30:
alpha_KK = 1/30
M_KK_val = 1e16  # assume GUT scale

for b0 in [7.0, 8.0, 9.0, 10.0, 12.0, 15.0, 20.0]:
    mu_L = M_KK_val * np.exp(-2*np.pi/(b0 * alpha_KK))
    print(f"  b0={b0:5.1f}: Landau pole at mu_L = {mu_L:.2e} GeV")

# To push Landau above 10^17 GeV:
# 10^17 = M_KK * exp(-2*pi/(b0*alpha_KK))
# -2*pi/(b0*alpha_KK) = ln(10^17/10^16) = ln(10) = 2.303
# b0 = -2*pi/(alpha_KK * 2.303)

# Wait, that gives negative b0 because the exponential argument is negative.
# Let me reconsider...

# If 1/alpha_s = 30 at M_KK = 10^16, and we run UP:
# 1/alpha_s(mu) = 30 + b0/(2*pi) * ln(mu/10^16)
# Landau at mu_L: 30 + b0/(2*pi)*ln(mu_L/10^16) = 0
# ln(mu_L/10^16) = -60*pi/b0
# mu_L = 10^16 * exp(-60*pi/b0)
# For b0 = 7: mu_L = 10^16 * exp(-26.9) = 10^16 * 2e-12 = 2e4 GeV
# That gives ~10^4 GeV, not 10^6.

# Hmm, maybe I need to reconsider. If alpha_s(M_KK) = 1/30 and the Landau 
# pole is at 10^6, then M_KK must be different:
# mu_L = M_KK * exp(-60*pi/7) = M_KK * 2e-12
# mu_L = 10^6 => M_KK = 10^6/2e-12 = 5e17 GeV
# That's actually a reasonable GUT/KK scale!

# OK so with M_KK ~ 5e17 and alpha_s(M_KK) = 1/30:
M_KK_alt = 5e17
mu_L_check = M_KK_alt * np.exp(-60*np.pi/7)
print(f"\n  With M_KK = 5e17: Landau at {mu_L_check:.2e} GeV")

# To push Landau above 10^17 from M_KK=5e17:
# 5e17 * exp(-60*pi/b0) > 10^17
# exp(-60*pi/b0) > 0.2
# -60*pi/b0 > ln(0.2) = -1.609
# b0 > 60*pi/1.609 = 117

# That seems way too large! Let me reconsider the whole Landau pole issue.

# Maybe the file means: running FROM M_Z UP, with the SM beta function, 
# the Landau pole is at ~10^6 GeV (since the SM SU(3) coupling grows),
# but with SCVC + KK corrections, the effective beta function pushes 
# the Landau pole above 10^17.
#
# SM Landau pole (from M_Z with b0=7):
mu_L_SM = M_Z * np.exp(2*np.pi/(7 * 0.1181))
print(f"\n  SM Landau pole (from M_Z, b0=7, alpha_s=0.1181): {mu_L_SM:.2e} GeV")

# Actually with b0=7 (6 quarks), the Landau pole is:
# 1/alpha_s(mu) = 1/0.1181 - 7/(2*pi) * ln(mu/M_Z) = 0
# mu = M_Z * exp(2*pi/(7*0.1181)) = 91 * exp(7.60) = 1.8e5 GeV

# But in reality, between M_Z and M_KK, b0 changes as we cross 
# quark thresholds (top, bottom, charm). Let me compute more carefully.

# At M_Z: N_f = 5 (top not active yet), b0 = 11 - 10/3 = 23/3 ≈ 7.67
# Above m_t ~ 173 GeV: N_f = 6, b0 = 11 - 12/3 = 7

# The detailed running:
# From M_Z to m_b (~4.2 GeV): N_f=5 actually... no wait.
# At M_Z=91 GeV: u,d,s,c,b active (5 flavors). Top threshold at 173 GeV.
# 1/alpha_s(m_t) = 1/alpha_s(M_Z) - 23/3/(2*pi) * ln(m_t/M_Z)
# Above m_t: b0=7
# 1/alpha_s(mu) = 1/alpha_s(m_t) - 7/(2*pi) * ln(mu/m_t)

inv_at_MZ = 1/0.1181
b0_5 = 23/3
inv_at_mt = inv_at_MZ - b0_5/(2*np.pi) * np.log(173/91)
b0_6 = 7
mu_L_full = 173 * np.exp(2*np.pi * inv_at_mt / b0_6)
print(f"  SM Landau pole (threshold-corrected): {mu_L_full:.2e} GeV")

# That's still ~10^5 GeV. To push it to >10^17:
# We need extra contributions to the beta function.
# Delta_b0 needed: mu_L = 10^17
# 10^17 = 173 * exp(2*pi*inv_at_mt/(b0_6 + Delta_b0))
# ln(10^17/173) = 2*pi*inv_at_mt/(7+Delta_b0)
# 7+Delta_b0 = 2*pi*inv_at_mt/ln(5.78e14)
#            = 2*pi*inv_at_mt/34.0

inv_at_mt_val = inv_at_mt
target_ln = np.log(1e17 / 173)
b0_needed = 2*np.pi * inv_at_mt_val / target_ln
delta_b0_needed = b0_needed - b0_6
print(f"\n  To push Landau pole to 10^17 GeV:")
print(f"  ln(mu_L/m_t) = {target_ln:.1f}")
print(f"  b0_needed = {b0_needed:.2f}")
print(f"  Delta_b0 needed = {delta_b0_needed:.2f}")
print(f"  (i.e., need extra matter content contributing ~{delta_b0_needed:.0f} to b0)")

# ============================================================
# Part 5: Can KK modes provide the needed Delta_b0?
# ============================================================
print("\n" + "-"*50)
print("Part 5: Can CP2 KK Modes Provide Needed Delta_b0?")
print("-"*50)

# For the RGE above M_KK, the KK modes contribute to b0.
# Each massive gauge boson KK mode (adjoint of SU3):
#   Contribution to b0 = -11*C_A/3 = -11 per mode
#   (This makes b0 MORE negative, meaning the coupling runs FASTER,
#    making the Landau pole WORSE, not better!)
#
# For Weyl fermion KK modes in representation R:
#   Contribution to b0 = +2*T(R)/3 per Weyl fermion
#   (This makes b0 LESS negative, slowing the growth of alpha_s)
#
# For complex scalar KK modes in adjoint:
#   Contribution to b0 = -C_A/3 = -1 per real scalar
#   = -2 per complex scalar

print("\nContribution to b0 from CP2 KK modes (change relative to SM):")
print("  Massive gauge bosons (adjoint): delta_b0 = -11 per mode")
print("  Weyl fermions (fundamental):    delta_b0 = +1/3 per mode")
print("  Complex scalars (adjoint):      delta_b0 = -2 per mode")

# The gauge boson KK modes make things WORSE (more negative b0).
# To help, we need fermion KK modes that make b0 LESS negative.
# 
# In the SCVC framework, there may be bulk fermions.
# If there are N_f_bulk bulk Dirac fermions in the fundamental:
# Each Dirac = 2 Weyl, contribution = +2*(1/2)/3 * 2 = +2/3 per Dirac
# 
# For each KK level, if we have N_f_bulk bulk fermions:
# Delta_b0_per_level = N_f_bulk * (2/3) * degeneracy_of_level

print("\nTo get Delta_b0 ~ +{:.0f} (from KK fermions):".format(delta_b0_needed))
print("Need sum over KK levels of contributions.")

# With CP2 scalar degeneracies d_k = (k+1)^3:
# Each KK level contributes N_f_bulk * (2/3) * d_k
# Sum_{k=1}^{K_max} (k+1)^3 ~ K_max^4/4
# 
# For Delta_b0 ~ 55, with N_f_bulk bulk Dirac fermions:
# (2/3) * N_f_bulk * sum_k d_k = 55
# sum_k d_k = 55 * 3/(2*N_f_bulk)
#
# If N_f_bulk = 3 (one generation in the bulk):
# sum_k d_k = 55 * 3/6 = 27.5
# sum_{k=1}^{K} (k+1)^3 ≈ 27.5
# (2^3+3^3+4^3+...) until sum ≈ 27.5
# 2^3=8, 8+27=35 (k=1,2). So K_max ≈ 2.
# That's only 2 KK levels needed!

# But wait, the gauge bosons also contribute negatively!
# For each KK level of gauge bosons (vector harmonics):
# Delta_b0_gauge = -11 * dim_vector_k
# 
# So the net effect might be negative or close to zero.
# The sign depends on the balance of bosons and fermions.
# In a supersymmetric theory, the contributions cancel.

print("\nNet Delta_b0 per KK level (with various assumptions):")

# Without SUSY, assuming 3 bulk Dirac fermions (one generation)
Nf_bulk = 3  # bulk Dirac fermions (equivalent to 6 Weyl)
for k_max in [1, 2, 3, 4]:
    total_b0 = 0
    total_gauge = 0
    total_fermion = 0
    for k in range(1, k_max+1):
        # Gauge bosons (vector harmonics)
        lam_vec = 4*k*(k+3) + 4
        dim_vec = 2*(k+1)*(k+2)
        total_gauge += -11 * dim_vec
        
        # Fermions (scalar harmonics degeneracy)
        deg_ferm = (k+1)**3
        total_fermion += Nf_bulk * (2/3) * deg_ferm
    
    total_b0 = total_gauge + total_fermion
    print(f"  k_max={k_max}: gauge={total_gauge:.0f}, fermion={total_fermion:.0f}, net={total_b0:.0f}")

print("\nThe gauge boson contribution is LARGE and NEGATIVE.")
print("Without supersymmetry, KK modes make the Landau pole WORSE.")
print("Need N_f_bulk >> 10 to overcome gauge boson contribution.")

# ============================================================
# Part 6: Supersymmetric KK towers
# ============================================================
print("\n" + "-"*50)
print("Part 6: Supersymmetric KK Towers (if SCVC is SUSY)")
print("-"*50)

print("""
In a supersymmetric theory on CP2:
- Each gauge boson has a gaugino partner (fermion in adjoint)
- The beta function contributions partially cancel
  
N=1 SUSY SU(3) beta function:
  b0_SUSY = 9 - N_f  (vs SM: b0 = 11 - 2N_f/3)
  
For N_f = 6 (3 generations): b0_SUSY = 3
(vs b0_SM = 7)
  
The slower running in SUSY means alpha_s runs less,
so the Landau pole is pushed to higher scales.

In SUSY, the KK tower contributions are:
  Gauge multiplet: gauge boson (-11) + gaugino (+2*C_A) = -11 + 6 = -5 per mode
  Chiral multiplet: complex scalar (-2) + Weyl fermion (+2) = 0 per mode

So each gauge KK mode contributes Delta_b0 = -5.
While each matter KK mode contributes Delta_b0 = 0.

The net effect of the gauge KK tower:
  sum_k (-5) * dim_vector_k

For SUSY, the Landau pole is LESS severe:
""")

# SUSY running from M_Z to M_SUSY (~1 TeV), then SUSY beta above
M_SUSY = 1e3
b0_SUSY = 3  # N_f=6 in SUSY

inv_at_MSUSY = inv_at_MZ - b0_5/(2*np.pi)*np.log(173/91) - 7/(2*np.pi)*np.log(M_SUSY/173)
mu_L_SUSY = M_SUSY * np.exp(2*np.pi * inv_at_MSUSY / b0_SUSY)
print(f"  SUSY Landau pole (from M_SUSY=1 TeV): {mu_L_SUSY:.2e} GeV")

# Landau pole in SUSY with KK towers
# Including KK gauge modes makes the running faster (more negative b0)
print("\n  But SUSY gauge KK modes make it run FASTER:")
for k_max in [1, 2, 3]:
    delta_b0_kk = sum(-5 * 2*(k+1)*(k+2) for k in range(1, k_max+1))
    total_b0 = b0_SUSY + delta_b0_kk
    print(f"  k_max={k_max}: delta_b0={delta_b0_kk}, total_b0={total_b0}")

print("\nFor SUSY SCVC with KK gauge modes:")
for k_max in [0,1,2,3]:
    delta_b0 = sum(-5 * 2*(k+1)*(k+2) for k in range(1, k_max+1))
    b0_total = b0_SUSY + delta_b0
    if b0_total > 0:
        mu_L = M_SUSY * np.exp(2*np.pi * inv_at_MSUSY / b0_total)
        print(f"  k_max={k_max}: b0={b0_total}, mu_L={mu_L:.2e} GeV")
    else:
        print(f"  k_max={k_max}: b0={b0_total} <= 0, no Landau pole (AF)")

print("\n" + "="*70)
print("PATH B COMPLETE")
print("="*70)
