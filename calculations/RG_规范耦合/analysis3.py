import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

M_Z = 91.1876
M_KK = 5.2e17
alpha_inv_MZ = 127.952
sin2thetaW_MZ_target = 0.23121
alpha_s_MZ = 0.1181

alpha_MZ = 1.0 / alpha_inv_MZ
sin_thetaW = np.sqrt(sin2thetaW_MZ_target)
cos_thetaW = np.sqrt(1 - sin2thetaW_MZ_target)
e_MZ = np.sqrt(4 * np.pi * alpha_MZ)
g_prime_MZ = e_MZ / cos_thetaW
g2_MZ_target = e_MZ / sin_thetaW
g1_MZ_target = np.sqrt(5.0/3.0) * g_prime_MZ
g3_MZ_target = np.sqrt(4 * np.pi * alpha_s_MZ)

b1 = 41.0/10.0
b2 = -19.0/6.0
b3 = -7.0

# Two-loop beta: d(alpha_i)/d(ln mu) = alpha_i^2/(2*pi) * [b_i + sum_j B_ij * alpha_j/(4*pi)]
B = np.array([[199/50, 27/10, 44/5],
               [9/10, 35/6, 12],
               [11/10, 9/2, -26]])

def two_loop_beta(ln_mu, y):
    a1, a2, a3 = y
    factor = 1.0 / (2*np.pi)
    two_loop_factor = 1.0 / (4*np.pi)
    da1 = factor * a1**2 * (b1 + two_loop_factor * (B[0,0]*a1 + B[0,1]*a2 + B[0,2]*a3))
    da2 = factor * a2**2 * (b2 + two_loop_factor * (B[1,0]*a1 + B[1,1]*a2 + B[1,2]*a3))
    da3 = factor * a3**2 * (b3 + two_loop_factor * (B[2,0]*a1 + B[2,1]*a2 + B[2,2]*a3))
    return [da1, da2, da3]

def sin2thetaW(g1, g2):
    gp_sq = (3.0/5.0)*g1**2
    return gp_sq / (g2**2 + gp_sq)

# Run SM forward (MZ -> MKK)
a1_0 = (5.0/3.0) * alpha_MZ / cos_thetaW**2
a2_0 = alpha_MZ / sin_thetaW**2
a3_0 = alpha_s_MZ

print("="*70)
print("FORWARD 2-LOOP RG: M_Z -> M_KK")
print("="*70)
print(f"  Start: a1={a1_0:.6f}, a2={a2_0:.6f}, a3={a3_0:.6f}")

sol_fwd = solve_ivp(two_loop_beta, [np.log(M_Z), np.log(M_KK)],
                     [a1_0, a2_0, a3_0], method='RK45', rtol=1e-12, atol=1e-15)

a1_KK_SM, a2_KK_SM, a3_KK_SM = sol_fwd.y[:,-1]
g1_KK_SM = np.sqrt(4*np.pi*a1_KK_SM)
g2_KK_SM = np.sqrt(4*np.pi*a2_KK_SM)
g3_KK_SM = np.sqrt(4*np.pi*a3_KK_SM)

print(f"  End:   a1={a1_KK_SM:.6f}, a2={a2_KK_SM:.6f}, a3={a3_KK_SM:.6f}")
print(f"  g1(M_KK, 2L) = {g1_KK_SM:.4f}")
print(f"  g2(M_KK, 2L) = {g2_KK_SM:.4f}")
print(f"  g3(M_KK, 2L) = {g3_KK_SM:.4f}")
print(f"  alpha_s(M_KK) = {a3_KK_SM:.6f}")
print(f"  sin^2theta_W(M_KK) = {sin2thetaW(g1_KK_SM, g2_KK_SM):.6f}")

# One-loop comparison
log_factor = np.log(M_KK/M_Z)
a1_1L_inv = 1.0/a1_0 - b1/(2*np.pi)*log_factor
a2_1L_inv = 1.0/a2_0 - b2/(2*np.pi)*log_factor
a3_1L_inv = 1.0/a3_0 - b3/(2*np.pi)*log_factor
a1_KK_1L = 1.0/a1_1L_inv
a2_KK_1L = 1.0/a2_1L_inv
a3_KK_1L = 1.0/a3_1L_inv
print(f"\n  1-loop comparison:")
print(f"  a1_KK: 1L={a1_KK_1L:.6f}, 2L={a1_KK_SM:.6f}, diff={(a1_KK_SM-a1_KK_1L)/a1_KK_1L*100:.3f}%")
print(f"  a2_KK: 1L={a2_KK_1L:.6f}, 2L={a2_KK_SM:.6f}, diff={(a2_KK_SM-a2_KK_1L)/a2_KK_1L*100:.3f}%")
print(f"  a3_KK: 1L={a3_KK_1L:.6f}, 2L={a3_KK_SM:.6f}, diff={(a3_KK_SM-a3_KK_1L)/a3_KK_1L*100:.3f}%")

# SCVC values
g1_SCVC = 0.303
g2_SCVC = 1.053
alpha_s_SCVC = 0.0199
g3_SCVC = np.sqrt(4*np.pi*alpha_s_SCVC)

# Exact ratios (2-loop)
N1_exact = g1_KK_SM / g1_SCVC
N2_exact = g2_KK_SM / g2_SCVC
N3_exact = g3_KK_SM / g3_SCVC

print("\n" + "="*70)
print("EXACT 2-LOOP RATIOS: N_i = g_i(SM, M_KK) / g_i(SCVC)")
print("="*70)
print(f"  N1 = {N1_exact:.6f}")
print(f"  N2 = {N2_exact:.6f}")
print(f"  N3 = {N3_exact:.6f}")
print(f"  N1 vs 2:   diff={abs(N1_exact-2.0):.4f} ({abs(N1_exact-2.0)/N1_exact*100:.3f}%)")
print(f"  N2 vs 1/2: diff={abs(N2_exact-0.5):.4f} ({abs(N2_exact-0.5)/abs(N2_exact)*100:.3f}%)")
print(f"  N3 vs 1:   diff={abs(N3_exact-1.0):.4f} ({abs(N3_exact-1.0)/N3_exact*100:.3f}%)")

# 1-loop ratios
N1_1L = np.sqrt(4*np.pi*a1_KK_1L) / g1_SCVC
N2_1L = np.sqrt(4*np.pi*a2_KK_1L) / g2_SCVC
N3_1L = np.sqrt(4*np.pi*a3_KK_1L) / g3_SCVC
print(f"\n  1-loop ratios: N1={N1_1L:.4f}, N2={N2_1L:.4f}, N3={N3_1L:.4f}")

# ============================================================
# GEOMETRIC CANDIDATE ANALYSIS
# ============================================================
print("\n" + "="*70)
print("GEOMETRIC/GROUP THEORY INTERPRETATION")
print("="*70)

# g2: Dynkin index ratio
T_adj_SU2 = 2.0
T_fund_SU2 = 0.5
ratio_SU2 = np.sqrt(T_fund_SU2 / T_adj_SU2)
print(f"\n  SU(2) Dynkin: sqrt(T_fund/T_adj) = sqrt({T_fund_SU2}/{T_adj_SU2}) = {ratio_SU2:.4f}")
print(f"  N2 (2L) = {N2_exact:.6f}")
print(f"  Match: diff = {abs(N2_exact-ratio_SU2)/abs(N2_exact)*100:.3f}%")

# g3: Dynkin ratio
T_adj_SU3 = 3.0
T_fund_SU3 = 0.5
ratio_SU3 = np.sqrt(T_fund_SU3 / T_adj_SU3)
print(f"\n  SU(3) Dynkin: sqrt(T_fund/T_adj) = sqrt({T_fund_SU3}/{T_adj_SU3}) = {ratio_SU3:.4f}")
print(f"  N3 (2L) = {N3_exact:.6f}")
print(f"  Dynkin does NOT match for SU(3)")

# g1: Various interpretations
print(f"\n  U(1) analysis:")
print(f"  N1 (2L) = {N1_exact:.6f}")
print(f"  sqrt(5/3) = {np.sqrt(5/3):.6f}")
print(f"  N1/sqrt(5/3) = {N1_exact/np.sqrt(5/3):.6f}")
print(f"  vs sqrt(4/pi) = {np.sqrt(4/np.pi):.6f}, diff={abs(N1_exact/np.sqrt(5/3) - np.sqrt(4/np.pi)):.6f}")
print(f"  vs 2/sqrt(3) = {2/np.sqrt(3):.6f}")
print(f"  vs pi/2 = {np.pi/2:.6f}")
print(f"  vs 3/2 = {1.5:.6f}")

# ============================================================
# BACKWARD RG: Normalized SCVC -> M_Z
# ============================================================
print("\n" + "="*70)
print("BACKWARD 2-LOOP RG: NORMALIZED SCVC -> M_Z")
print("="*70)

def run_backward(N1, N2, N3):
    g1_kk = g1_SCVC * N1
    g2_kk = g2_SCVC * N2
    g3_kk = g3_SCVC * N3
    a1_kk = g1_kk**2/(4*np.pi)
    a2_kk = g2_kk**2/(4*np.pi)
    a3_kk = g3_kk**2/(4*np.pi)
    sol = solve_ivp(two_loop_beta, [np.log(M_KK), np.log(M_Z)],
                     [a1_kk, a2_kk, a3_kk],
                     method='RK45', rtol=1e-12, atol=1e-15)
    a1_mz, a2_mz, a3_mz = sol.y[:,-1]
    g1_mz = np.sqrt(4*np.pi*a1_mz)
    g2_mz = np.sqrt(4*np.pi*a2_mz)
    g3_mz = np.sqrt(4*np.pi*a3_mz)
    s2w = sin2thetaW(g1_mz, g2_mz)
    return g1_mz, g2_mz, g3_mz, a3_mz, s2w

# Proposed round numbers
g1r, g2r, g3r, a3r, s2wr = run_backward(2.0, 0.5, 1.0)
print(f"\n  With N_i = {{2, 1/2, 1}}:")
print(f"  g1(M_Z) = {g1r:.4f} (SM: {g1_MZ_target:.4f}, dev: {(g1r-g1_MZ_target)/g1_MZ_target*100:+.2f}%)")
print(f"  g2(M_Z) = {g2r:.4f} (SM: {g2_MZ_target:.4f}, dev: {(g2r-g2_MZ_target)/g2_MZ_target*100:+.2f}%)")
print(f"  g3(M_Z) = {g3r:.4f} (SM: {g3_MZ_target:.4f}, dev: {(g3r-g3_MZ_target)/g3_MZ_target*100:+.2f}%)")
print(f"  alpha_s(M_Z) = {a3r:.6f} (PDG: {alpha_s_MZ})")
print(f"  sin^2theta_W(M_Z) = {s2wr:.6f} (PDG: {sin2thetaW_MZ_target})")

# Exact fitted values
g1e, g2e, g3e, a3e, s2we = run_backward(N1_exact, N2_exact, N3_exact)
print(f"\n  With exact N_i = {{{N1_exact:.4f}, {N2_exact:.4f}, {N3_exact:.4f}}}:")
print(f"  g1(M_Z) = {g1e:.4f} (SM: {g1_MZ_target:.4f}, dev: {(g1e-g1_MZ_target)/g1_MZ_target*100:+.2f}%)")
print(f"  g2(M_Z) = {g2e:.4f} (SM: {g2_MZ_target:.4f}, dev: {(g2e-g2_MZ_target)/g2_MZ_target*100:+.2f}%)")
print(f"  alpha_s(M_Z) = {a3e:.6f} (PDG: {alpha_s_MZ})")
print(f"  sin^2theta_W(M_Z) = {s2we:.6f} (PDG: {sin2thetaW_MZ_target})")

# Optimize N1, N2 for sin^2theta_W
print("\n" + "="*70)
print("OPTIMIZATION: FIND N1,N2 TO MATCH sin^2theta_W(M_Z)")
print("="*70)

def objective_s2w(params):
    N1, N2 = params
    _, _, _, _, s2w = run_backward(N1, N2, N3_exact)
    return (s2w - sin2thetaW_MZ_target)**2

res = minimize(objective_s2w, [N1_exact, N2_exact], method='Nelder-Mead',
               options={'xatol': 1e-8, 'fatol': 1e-12})
N1_opt, N2_opt = res.x
_, _, _, _, s2w_opt = run_backward(N1_opt, N2_opt, N3_exact)
print(f"  Optimal N1 = {N1_opt:.6f}")
print(f"  Optimal N2 = {N2_opt:.6f}")
print(f"  sin^2theta_W(M_Z) = {s2w_opt:.8f}")
print(f"  N1_opt / 2 = {N1_opt/2:.6f}")
print(f"  N2_opt * 2 = {N2_opt*2:.6f}")

# Try geometric interpretation of N1_opt
print(f"\n  Geometric candidates for N1_opt = {N1_opt:.6f}:")
for name, val in [('2', 2.0), ('sqrt(5/3)*sqrt(4/pi)', np.sqrt(5/3)*np.sqrt(4/np.pi)),
                   ('pi/sqrt(3)', np.pi/np.sqrt(3)), ('sqrt(3)', np.sqrt(3)),
                   ('sqrt(pi)', np.sqrt(np.pi))]:
    print(f"    {name:30s} = {val:.6f}  (diff: {abs(N1_opt-val):.6f})")

print(f"\n  Geometric candidates for N2_opt = {N2_opt:.6f}:")
for name, val in [('1/2', 0.5), ('2/pi', 2/np.pi), ('sqrt(pi/4)/2', np.sqrt(np.pi/4)/2),
                   ('sqrt(3/pi)', np.sqrt(3/np.pi)), ('1/sqrt(3)', 1/np.sqrt(3))]:
    print(f"    {name:30s} = {val:.6f}  (diff: {abs(N2_opt-val):.6f})")

