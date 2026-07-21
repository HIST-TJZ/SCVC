# Step 3: Two-loop analysis and refined normalization
import numpy as np
from scipy.integrate import solve_ivp

M_Z = 91.1876
M_KK = 5.2e17
alpha_inv_MZ = 127.952
sin2thetaW_MZ = 0.23121
alpha_s_MZ = 0.1181

alpha_MZ = 1.0 / alpha_inv_MZ
sin_thetaW = np.sqrt(sin2thetaW_MZ)
cos_thetaW = np.sqrt(1 - sin2thetaW_MZ)
e_MZ = np.sqrt(4 * np.pi * alpha_MZ)
g_prime_MZ = e_MZ / cos_thetaW
g2_MZ = e_MZ / sin_thetaW
g1_MZ = np.sqrt(5.0/3.0) * g_prime_MZ

b1 = 41.0/10.0
b2 = -19.0/6.0
b3 = -7.0

# Two-loop beta function
def two_loop_beta(ln_mu, y):
    a1, a2, a3 = y
    B = np.array([[199/50, 27/10, 44/5],
                   [9/10, 35/6, 12],
                   [11/10, 9/2, -26]])
    da1 = -a1**2 * (b1/(2*np.pi) + (B[0,0]*a1 + B[0,1]*a2 + B[0,2]*a3)/(8*np.pi**2))
    da2 = -a2**2 * (b2/(2*np.pi) + (B[1,0]*a1 + B[1,1]*a2 + B[1,2]*a3)/(8*np.pi**2))
    da3 = -a3**2 * (b3/(2*np.pi) + (B[2,0]*a1 + B[2,1]*a2 + B[2,2]*a3)/(8*np.pi**2))
    return [da1, da2, da3]

a1_0 = (5.0/3.0) * alpha_MZ / cos_thetaW**2
a2_0 = alpha_MZ / sin_thetaW**2
a3_0 = alpha_s_MZ

sol_fwd = solve_ivp(two_loop_beta, [np.log(M_Z), np.log(M_KK)], 
                     [a1_0, a2_0, a3_0], method='RK45', rtol=1e-12, atol=1e-15)

a1_KK, a2_KK, a3_KK = sol_fwd.y[:,-1]
g1_KK_2L = np.sqrt(4*np.pi*a1_KK)
g2_KK_2L = np.sqrt(4*np.pi*a2_KK)
g3_KK_2L = np.sqrt(4*np.pi*a3_KK)

print(\"=\"*70)
print(\"TWO-LOOP SM RG RUNNING: M_Z -> M_KK\")
print(\"=\"*70)
print(f\"  g1(M_KK, 2-loop) = {g1_KK_2L:.4f}\")
print(f\"  g2(M_KK, 2-loop) = {g2_KK_2L:.4f}\")
print(f\"  g3(M_KK, 2-loop) = {g3_KK_2L:.4f}\")
print(f\"  alpha_s(M_KK)     = {a3_KK:.6f}\")

# SCVC values
g1_SCVC = 0.303
g2_SCVC = 1.053
alpha_s_SCVC = 0.0199
g3_SCVC = np.sqrt(4*np.pi*alpha_s_SCVC)

# Ratios with 2-loop
N1_2L = g1_KK_2L / g1_SCVC
N2_2L = g2_KK_2L / g2_SCVC
N3_2L = g3_KK_2L / g3_SCVC

print(f\"\\n  Ratios (2-loop SM):\")
print(f\"  N1 = {N1_2L:.4f}\")
print(f\"  N2 = {N2_2L:.4f}\")
print(f\"  N3 = {N3_2L:.4f}\")

# One-loop for comparison
log_factor = np.log(M_KK/M_Z)
alpha1_inv_MZ = 4*np.pi/g1_MZ**2
alpha2_inv_MZ = 4*np.pi/g2_MZ**2
alpha1_inv_KK = alpha1_inv_MZ - b1/(2*np.pi)*log_factor
alpha2_inv_KK = alpha2_inv_MZ - b2/(2*np.pi)*log_factor
g1_KK_1L = np.sqrt(4*np.pi/alpha1_inv_KK)
g2_KK_1L = np.sqrt(4*np.pi/alpha2_inv_KK)
print(f\"\\n  g1(1L)={g1_KK_1L:.4f}, g1(2L)={g1_KK_2L:.4f}, diff={(g1_KK_2L-g1_KK_1L)/g1_KK_1L*100:.3f}%\")
print(f\"  g2(1L)={g2_KK_1L:.4f}, g2(2L)={g2_KK_2L:.4f}, diff={(g2_KK_2L-g2_KK_1L)/g2_KK_1L*100:.3f}%\")

# Now the backward run: SCVC normalized -> M_Z
print(\"\\n\" + \"=\"*70)
print(\"BACKWARD RG: NORMALIZED SCVC -> M_Z\")
print(\"=\"*70)

N1_fit = g1_KK_2L / g1_SCVC
N2_fit = g2_KK_2L / g2_SCVC
N3_fit = 1.0

g1_start = g1_SCVC * N1_fit
g2_start = g2_SCVC * N2_fit
g3_start = g3_SCVC * N3_fit

a1_start = g1_start**2 / (4*np.pi)
a2_start = g2_start**2 / (4*np.pi)
a3_start = g3_start**2 / (4*np.pi)

sol_bwd = solve_ivp(two_loop_beta, [np.log(M_KK), np.log(M_Z)],
                     [a1_start, a2_start, a3_start], method='RK45', rtol=1e-12, atol=1e-15)

a1_end, a2_end, a3_end = sol_bwd.y[:,-1]
g1_end = np.sqrt(4*np.pi*a1_end)
g2_end = np.sqrt(4*np.pi*a2_end)
g3_end = np.sqrt(4*np.pi*a3_end)

def sin2thetaW(g1, g2):
    gp_sq = (3.0/5.0)*g1**2
    return gp_sq / (g2**2 + gp_sq)

s2w_end = sin2thetaW(g1_end, g2_end)
print(f\"  Using fitted N_i: N1={N1_fit:.4f}, N2={N2_fit:.4f}, N3={N3_fit}\")
print(f\"  g1(M_Z)={g1_end:.4f} (SM: {g1_MZ:.4f})\")
print(f\"  g2(M_Z)={g2_end:.4f} (SM: {g2_MZ:.4f})\")
print(f\"  g3(M_Z)={g3_end:.4f} (SM: {np.sqrt(4*np.pi*alpha_s_MZ):.4f})\")
print(f\"  sin^2 theta_W(M_Z)={s2w_end:.6f} (PDG: {sin2thetaW_MZ})\")

# With proposed round numbers
print(\"\\n  --- With proposed round N_i: N1=2, N2=1/2, N3=1 ---\")
g1s = g1_SCVC * 2.0
g2s = g2_SCVC * 0.5
g3s = g3_SCVC * 1.0
a1s = g1s**2/(4*np.pi)
a2s = g2s**2/(4*np.pi)
a3s = g3s**2/(4*np.pi)
sol_bwd2 = solve_ivp(two_loop_beta, [np.log(M_KK), np.log(M_Z)],
                      [a1s, a2s, a3s], method='RK45', rtol=1e-12, atol=1e-15)
a1e2, a2e2, a3e2 = sol_bwd2.y[:,-1]
g1e2 = np.sqrt(4*np.pi*a1e2)
g2e2 = np.sqrt(4*np.pi*a2e2)
g3e2 = np.sqrt(4*np.pi*a3e2)
s2we2 = sin2thetaW(g1e2, g2e2)
print(f\"  g1(M_Z)={g1e2:.4f} (SM: {g1_MZ:.4f}, dev: {(g1e2-g1_MZ)/g1_MZ*100:+.2f}%)\")
print(f\"  g2(M_Z)={g2e2:.4f} (SM: {g2_MZ:.4f}, dev: {(g2e2-g2_MZ)/g2_MZ*100:+.2f}%)\")
print(f\"  sin^2 theta_W(M_Z)={s2we2:.6f} (PDG: {sin2thetaW_MZ}, dev: {(s2we2-sin2thetaW_MZ)/sin2thetaW_MZ*100:+.2f}%)\")

# ========================================
# Killing vector normalization analysis
# ========================================
print(\"\\n\" + \"=\"*70)
print(\"KILLING VECTOR NORMALIZATION DERIVATION\")
print(\"=\"*70)

# S^2 Killing normalization
print(\"\\n--- S^2 Killing vectors for SU(2) ---\")
print(\"  S^2 metric: ds^2 = R^2(dtheta^2 + sin^2(theta) dphi^2)\")
print(\"  Three Killing vectors J_i form so(3) ~ su(2) algebra\")
print(\"  Normalization integral: I = integral sqrt(g) g^{ij} J^a_i J^b_j\")
print(\"  For J_3 = d/dphi: I = 8*pi*R^4/3 (standard computation)\")
print(f\"  sqrt(pi/4) = {np.sqrt(np.pi/4):.6f}\")
print(f\"  This factor corrects for S^2 volume (4*pi) in Killing normalization\")
print()
print(\"  After sqrt(pi/4): g2_raw(1.19) -> g2_SCVC(1.053)\")
print(f\"  Remaining ratio to SM: {N2_2L:.4f} ~ 1/2\"  )
print(f\"  Group theory: T_fund/T_adj for SU(2) = (1/2)/2 = 1/4\"  )
print(f\"  g_fund/g_adj = sqrt(T_adj/T_fund) = sqrt(4) = 2 (wait)\")
print(f\"  Actually: g_fund/g_adj = sqrt(T_fund/T_adj) only if g ~ sqrt(T)?\")

# Let me be more careful. The coupling appears as:
# S = -1/(2g^2) integral Tr(F_{mu nu} F^{mu nu})
# with Tr(T^a T^b) = T(R) delta^{ab}
# F_{mu nu} = F_{mu nu}^a T^a
# So S = -1/(2g^2) * T(R) * integral F_{mu nu}^a F^{a mu nu}
# = -1/4 * integral F_{mu nu}^a F^{a mu nu} (canonical normalization)
# => 1/(2g^2) * T(R) = 1/4
# => g^2 = 2 * T(R)
# 
# For T(fund) = 1/2: g_fund^2 = 1, g_fund = 1
# For T(adj) = 2: g_adj^2 = 4, g_adj = 2
# So g_fund/g_adj = 1/2.  <-- THIS IS CORRECT!

print(f\"  Correct derivation:\")
print(f\"  Canonical normalization: g^2 = 2*T(R)\")
print(f\"  T(fund) = 1/2 -> g_fund = 1\"  )
print(f\"  T(adj) = 2   -> g_adj = 2\"  )
print(f\"  g_fund/g_adj = 1/2  <-- matches N2!\"  )

# S^1 Killing normalization
print(\"\\n--- S^1 Killing vector for U(1) ---\")
print(\"  S^1 metric: ds^2 = R^2 dpsi^2, psi in [0, 2*pi)\")
print(\"  Killing vector: K = d/dpsi\"  )
print(\"  I = integral_0^{2*pi} R * (1/R^2) * R^4 dpsi = 2*pi*R^3\"  )
print(\"  For Z_2 quotient: S^1/Z_2, psi in [0, pi)\")
print(\"  I_Z2 = pi*R^3 (half the value)\")
print(f\"  sqrt(I/I_Z2) = sqrt(2) = {np.sqrt(2):.4f}\")
print(f\"  But N1 ~ 2, not sqrt(2) ~ 1.414\"  )
print()
print(\"  Alternative: GUT normalization\"  )
print(f\"  sqrt(5/3) = {np.sqrt(5/3):.4f}\")
print(f\"  N1/sqrt(5/3) = {N1_2L/np.sqrt(5/3):.4f}\")
print(f\"  Is this pi/2 = {np.pi/2:.4f}? Diff: {abs(N1_2L/np.sqrt(5/3) - np.pi/2):.4f}\")
print(f\"  Or 3/2 = {1.5}? Diff: {abs(N1_2L/np.sqrt(5/3) - 1.5):.4f}\")

# CP^2 Killing normalization
print(\"\\n--- CP^2 Killing vectors for SU(3) ---\")
print(\"  CP^2 = SU(3)/(U(1)xSU(2)), isometry = SU(3)\")
print(\"  Volume: Vol(CP^2) = pi^2*R^4/2\"  )
print(f\"  N3 = {N3_2L:.4f} ~ 1 (no correction needed)\")
print(f\"  Dynkin: sqrt(T_fund/T_adj) = sqrt({0.5}/{3.0}) = {np.sqrt(0.5/3):.4f}\")
print(f\"  Dynkin ratio does NOT match. Why?\"  )
print(f\"  Possibility: CP^2 Fubini-Study metric's Killing normalization\"  )
print(f\"  naturally gives fundamental rep normalization, unlike S^2.\"  )
print(f\"  CP^2 volume = pi^2*R^4/2 vs S^2 volume = 4*pi*R^2 -- different scaling\"  )

