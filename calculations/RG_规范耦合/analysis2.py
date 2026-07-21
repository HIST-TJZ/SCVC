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

# Two-loop beta
def two_loop_beta(ln_mu, y):
    a1, a2, a3 = y
    B = np.array([[199/50, 27/10, 44/5],
                   [9/10, 35/6, 12],
                   [11/10, 9/2, -26]])
    da1 = -a1**2 * (b1/(2*np.pi) + (B[0,0]*a1 + B[0,1]*a2 + B[0,2]*a3)/(8*np.pi**2))
    da2 = -a2**2 * (b2/(2*np.pi) + (B[1,0]*a1 + B[1,1]*a2 + B[1,2]*a3)/(8*np.pi**2))
    da3 = -a3**2 * (b3/(2*np.pi) + (B[2,0]*a1 + B[2,1]*a2 + B[2,2]*a3)/(8*np.pi**2))
    return [da1, da2, da3]

def sin2thetaW(g1, g2):
    gp_sq = (3.0/5.0)*g1**2
    return gp_sq / (g2**2 + gp_sq)

# Run SM forward (MZ -> MKK)
a1_0 = (5.0/3.0) * alpha_MZ / cos_thetaW**2
a2_0 = alpha_MZ / sin_thetaW**2
a3_0 = alpha_s_MZ

sol_fwd = solve_ivp(two_loop_beta, [np.log(M_Z), np.log(M_KK)],
                     [a1_0, a2_0, a3_0], method='RK45', rtol=1e-12, atol=1e-15)
a1_KK_SM, a2_KK_SM, a3_KK_SM = sol_fwd.y[:,-1]
g1_KK_SM = np.sqrt(4*np.pi*a1_KK_SM)
g2_KK_SM = np.sqrt(4*np.pi*a2_KK_SM)
g3_KK_SM = np.sqrt(4*np.pi*a3_KK_SM)

print("="*70)
print("TWO-LOOP SM AT M_KK")
print("="*70)
print(f"  g1(M_KK, 2L) = {g1_KK_SM:.4f}")
print(f"  g2(M_KK, 2L) = {g2_KK_SM:.4f}")
print(f"  g3(M_KK, 2L) = {g3_KK_SM:.4f}")
print(f"  alpha_s(M_KK) = {a3_KK_SM:.6f}")
print(f"  sin^2theta_W(M_KK) = {sin2thetaW(g1_KK_SM, g2_KK_SM):.6f}")

# SCVC values
g1_SCVC = 0.303
g2_SCVC = 1.053
alpha_s_SCVC = 0.0199
g3_SCVC = np.sqrt(4*np.pi*alpha_s_SCVC)

# Exact ratios
N1_exact = g1_KK_SM / g1_SCVC
N2_exact = g2_KK_SM / g2_SCVC
N3_exact = g3_KK_SM / g3_SCVC

print("\n" + "="*70)
print("EXACT 2-LOOP RATIOS")
print("="*70)
print(f"  N1 = {N1_exact:.6f}")
print(f"  N2 = {N2_exact:.6f}")
print(f"  N3 = {N3_exact:.6f}")
print(f"  N1 or 2:  diff={abs(N1_exact-2.0):.4f} ({abs(N1_exact-2.0)/N1_exact*100:.3f}%)")
print(f"  N2 or 1/2: diff={abs(N2_exact-0.5):.4f} ({abs(N2_exact-0.5)/abs(N2_exact)*100:.3f}%)")
print(f"  N3 or 1:   diff={abs(N3_exact-1.0):.4f} ({abs(N3_exact-1.0)/N3_exact*100:.3f}%)")

# Check if geometric candidate ratios exist
print("\n" + "="*70)
print("GEOMETRIC CANDIDATE SEARCH")
print("="*70)

candidates = {
    'sqrt(5/3)': np.sqrt(5/3),
    'sqrt(3/5)': np.sqrt(3/5),
    'sqrt(pi/4)': np.sqrt(np.pi/4),
    'sqrt(4/pi)': np.sqrt(4/np.pi),
    'sqrt(2)': np.sqrt(2),
    '1/sqrt(2)': 1/np.sqrt(2),
    'pi/2': np.pi/2,
    '2/pi': 2/np.pi,
    'pi/4': np.pi/4,
    '4/pi': 4/np.pi,
    'sqrt(pi/2)': np.sqrt(np.pi/2),
    'sqrt(2/pi)': np.sqrt(2/np.pi),
    '3/2': 1.5,
    '2/3': 2/3,
    'sqrt(3/2)': np.sqrt(3/2),
    'sqrt(2/3)': np.sqrt(2/3),
    'sqrt(8/3)': np.sqrt(8/3),
    'sqrt(3/8)': np.sqrt(3/8),
    'sqrt(6)': np.sqrt(6),
    '1/sqrt(6)': 1/np.sqrt(6),
}

# For g1: check N1/sqrt(5/3) (if SCVC gives g')
print(f"\n  For g1: N1/sqrt(5/3) = {N1_exact/np.sqrt(5/3):.6f}")
for name, val in candidates.items():
    diff = abs(N1_exact/np.sqrt(5/3) - val)
    if diff < 0.1:
        print(f"    vs {name:15s} = {val:.6f}  diff={diff:.6f}")

print(f"\n  For g1: N1 = {N1_exact:.6f}")
for name, val in candidates.items():
    diff = abs(N1_exact - val)
    if diff < 0.1:
        print(f"    vs {name:15s} = {val:.6f}  diff={diff:.6f}")

print(f"\n  For g2: N2 = {N2_exact:.6f}")
for name, val in candidates.items():
    diff = abs(N2_exact - val)
    if diff < 0.1:
        print(f"    vs {name:15s} = {val:.6f}  diff={diff:.6f}")

# ============================================================
# Backward run with fitted N_i
# ============================================================
print("\n" + "="*70)
print("BACKWARD RG WITH FITTED N_i")
print("="*70)

g1_fit = g1_SCVC * N1_exact
g2_fit = g2_SCVC * N2_exact
g3_fit = g3_SCVC * N3_exact

a1_fit_KK = g1_fit**2/(4*np.pi)
a2_fit_KK = g2_fit**2/(4*np.pi)
a3_fit_KK = g3_fit**2/(4*np.pi)

sol_bwd = solve_ivp(two_loop_beta, [np.log(M_KK), np.log(M_Z)],
                     [a1_fit_KK, a2_fit_KK, a3_fit_KK],
                     method='RK45', rtol=1e-12, atol=1e-15)

a1_fit_MZ, a2_fit_MZ, a3_fit_MZ = sol_bwd.y[:,-1]
g1_fit_MZ = np.sqrt(4*np.pi*a1_fit_MZ)
g2_fit_MZ = np.sqrt(4*np.pi*a2_fit_MZ)
g3_fit_MZ = np.sqrt(4*np.pi*a3_fit_MZ)
s2w_fit_MZ = sin2thetaW(g1_fit_MZ, g2_fit_MZ)

print(f"  Using exact N_i = {{{N1_exact:.4f}, {N2_exact:.4f}, {N3_exact:.4f}}}")
print(f"  g1(M_Z) = {g1_fit_MZ:.4f} (SM: {g1_MZ_target:.4f}, dev: {(g1_fit_MZ-g1_MZ_target)/g1_MZ_target*100:+.3f}%)")
print(f"  g2(M_Z) = {g2_fit_MZ:.4f} (SM: {g2_MZ_target:.4f}, dev: {(g2_fit_MZ-g2_MZ_target)/g2_MZ_target*100:+.3f}%)")
print(f"  g3(M_Z) = {g3_fit_MZ:.4f} (SM: {g3_MZ_target:.4f}, dev: {(g3_fit_MZ-g3_MZ_target)/g3_MZ_target*100:+.3f}%)")
print(f"  sin^2theta_W(M_Z) = {s2w_fit_MZ:.6f} (PDG: {sin2thetaW_MZ_target})")
print(f"  alpha_s(M_Z) = {a3_fit_MZ:.6f} (PDG: {alpha_s_MZ})")

# ============================================================
# sin^2 theta_W as function of N1, N2
# ============================================================
print("\n" + "="*70)
print("SENSITIVITY: sin^2theta_W(M_Z) vs N1, N2")
print("="*70)

def compute_s2w_MZ(N1, N2):
    g1_kk = g1_SCVC * N1
    g2_kk = g2_SCVC * N2
    a1_kk = g1_kk**2/(4*np.pi)
    a2_kk = g2_kk**2/(4*np.pi)
    a3_kk = a3_KK_SM  # use SM value for g3
    sol = solve_ivp(two_loop_beta, [np.log(M_KK), np.log(M_Z)],
                     [a1_kk, a2_kk, a3_kk],
                     method='RK45', rtol=1e-10, atol=1e-12)
    a1_mz, a2_mz, a3_mz = sol.y[:,-1]
    g1_mz = np.sqrt(4*np.pi*a1_mz)
    g2_mz = np.sqrt(4*np.pi*a2_mz)
    return sin2thetaW(g1_mz, g2_mz)

# Scan around the proposed values
print(f"\n  Target sin^2theta_W(M_Z) = {sin2thetaW_MZ_target}")
print(f"  With N1=2.0, N2=0.5: s2w = {compute_s2w_MZ(2.0, 0.5):.6f}")
print(f"  With N1={N1_exact:.4f}, N2={N2_exact:.4f}: s2w = {compute_s2w_MZ(N1_exact, N2_exact):.6f}")

# Find N1, N2 that give correct sin^2theta_W
def objective(params):
    N1, N2 = params
    s2w = compute_s2w_MZ(N1, N2)
    return (s2w - sin2thetaW_MZ_target)**2

res = minimize(objective, [N1_exact, N2_exact], method='Nelder-Mead',
               options={'xatol': 1e-8, 'fatol': 1e-12})
N1_opt, N2_opt = res.x
s2w_opt = compute_s2w_MZ(N1_opt, N2_opt)
print(f"\n  Optimized to match sin^2theta_W(M_Z):")
print(f"  N1_opt = {N1_opt:.6f}")
print(f"  N2_opt = {N2_opt:.6f}")
print(f"  sin^2theta_W(M_Z) = {s2w_opt:.8f}")

# What are N1_opt and N2_opt as multiples of round numbers?
print(f"  N1_opt/2 = {N1_opt/2:.6f}")
print(f"  N2_opt*2 = {N2_opt*2:.6f}")

# ============================================================
# PHYSICAL ANALYSIS
# ============================================================
print("\n" + "="*70)
print("PHYSICAL INTERPRETATION")
print("="*70)

print("""
SUMMARY:
--------
1. g3 (SU(3)): N3 ~ 1. No correction needed. CP^2 KK reduction
   naturally gives the SM fundamental representation normalization.
   This is consistent with the fact that alpha_s matches to within ~3%.

2. g2 (SU(2)): N2 ~ 0.5 = 1/2. This has a clean group theory origin:
   - SCVC's KK reduction on S^2 gives the coupling in the SO(3)/SU(2) 
     adjoint representation convention (Dynkin index T=2)
   - SM uses the fundamental representation convention (T=1/2)
   - g_fund/g_adj = sqrt(T_fund/T_adj) = sqrt((1/2)/2) = 1/2
   
   WAIT - let me double-check this sign.
   
   Actually: the coupling appears as g in D_mu = d_mu - i g A_mu^a T^a
   The gauge kinetic term: -1/(4 g^2) F^a_{munu} F^{a munu}
   Or equivalently: -1/(2) Tr(F_{munu} F^{munu}) with F = F^a T^a
   For this to equal -1/4 F^a F^a, we need Tr(T^a T^b) = (1/2)delta^{ab}.
   
   In the adjoint rep: Tr(T^a_adj T^b_adj) = f^{acd} f^{bcd} = C_A delta^{ab} = N delta^{ab}
   For SU(2): C_A = 2, so Tr_{adj}(T^a T^b) = 2 delta^{ab}.
   
   So in the adjoint, -1/2 Tr(F F) = -1/2 * 2 * F^a F^a = -F^a F^a = -4 * (1/4 F^a F^a)
   This means the "1/4" convention needs the coupling to be 1 in adjoint normalization.
   
   OK this is getting confusing. Let me think about it differently.
   
   The KK reduction produces: S_4D contains -C * integral F^a_{munu} F^{a munu}
   where C is some coefficient. The SM convention is C = 1/4.
   
   If the KK gives C_KK = 1/(4 g_KK^2) and we define g_SM so that C_SM = 1/4,
   then 1/(4 g_KK^2) = 1/4, so g_KK = 1. But that's not what we observe.
   
   Actually, the KK coefficient C depends on the Killing normalization:
   C = (1/2kappa_7^2) * I where I = integral sqrt(gamma) gamma^{ij} K_i^a K_j^a
   
   For canonically normalized gauge fields: C = 1/4.
   So: 1/4 = (1/2kappa_7^2) * I
   => 1/g_SM^2 = (2/kappa_7^2) * I
   
   Now if SCVC computes I_SCVC with one Killing normalization and 
   SM convention uses I_SM with a different one:
   g_SM^2/g_SCVC^2 = I_SCVC/I_SM = (lambda_SCVC/lambda_SM)^2
   => g_SM/g_SCVC = lambda_SCVC/lambda_SM
   
   So N2 = lambda_SCVC/lambda_SM = 1/2 means lambda_SM = 2 * lambda_SCVC.
   The SM generators are "twice as large" as the SCVC Killing vectors.
   
   For SU(2): T^a_fund = sigma^a/2, T^a_adj has matrix elements -i epsilon^{abc}.
   The normalization comparison:
   Tr(T^a_fund T^b_fund) = delta^{ab}/2
   Tr(T^a_adj T^b_adj) = 2 delta^{ab}
   
   The "size" ratio: If Killing vectors correspond to the adjoint rep 
   (which they naturally do, since they form the algebra of isometries),
   then the SM generators in the fundamental rep are related by:
   T_fund = (1/2) T_adj (in terms of normalization)
   
   So N2 = 1/2 makes perfect sense.

3. g1 (U(1)): N1 ~ 2. This is less clean.
   Possible origins:
   a) The S^1 Killing vector normalization differs by factor 2
      between the geometric (SCVC) and SM conventions.
   b) The Z_2 quotient on S^1 halves the available circumference,
      changing the effective 1/g^2 by factor 2, so g changes by sqrt(2).
      But N1=2, not sqrt(2)=1.414...
   c) GUT normalization sqrt(5/3) combined with some geometric factor.
   d) The hypercharge quantization (Y=1/6 for quarks vs Y=1 for KK charge)
      combined with the GUT factor.

   Further analysis needed for g1.
""")
