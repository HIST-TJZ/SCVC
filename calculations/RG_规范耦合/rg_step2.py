# Step 2: Comparison and normalization analysis
import numpy as np
import json

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
g3_MZ = np.sqrt(4 * np.pi * alpha_s_MZ)
g1_MZ = np.sqrt(5.0/3.0) * g_prime_MZ

b1 = 41.0/10.0
b2 = -19.0/6.0
b3 = -7.0
log_factor = np.log(M_KK / M_Z)

alpha1_inv_MZ = 4*np.pi / g1_MZ**2
alpha2_inv_MZ = 4*np.pi / g2_MZ**2
alpha3_inv_MZ = 1.0 / alpha_s_MZ

alpha1_inv_KK = alpha1_inv_MZ - b1/(2*np.pi) * log_factor
alpha2_inv_KK = alpha2_inv_MZ - b2/(2*np.pi) * log_factor
alpha3_inv_KK = alpha3_inv_MZ - b3/(2*np.pi) * log_factor

g1_KK = np.sqrt(4*np.pi / alpha1_inv_KK)
g2_KK = np.sqrt(4*np.pi / alpha2_inv_KK)
g3_KK = np.sqrt(4*np.pi / alpha3_inv_KK)
alpha_s_KK = 1.0 / alpha3_inv_KK

# SCVC values
g1_SCVC = 0.303
g2_SCVC = 1.053
alpha_s_SCVC = 0.0199
g3_SCVC = np.sqrt(4*np.pi * alpha_s_SCVC)

# Ratios
N1 = g1_KK / g1_SCVC
N2 = g2_KK / g2_SCVC
N3 = g3_KK / g3_SCVC

print(\"=\"*70)
print(\"SCVC vs SM COMPARISON AT M_KK\")
print(\"=\"*70)
print(f\"{'Coupling':<12} {'SCVC':>10} {'SM(M_KK)':>12} {'Ratio N_i':>12}\")
print(f\"{'-'*48}\")
print(f\"{'g1':<12} {g1_SCVC:>10.4f} {g1_KK:>12.4f} {N1:>12.4f}\")
print(f\"{'g2':<12} {g2_SCVC:>10.4f} {g2_KK:>12.4f} {N2:>12.4f}\")
print(f\"{'g3':<12} {g3_SCVC:>10.4f} {g3_KK:>12.4f} {N3:>12.4f}\")

print(\"\\n\" + \"=\"*70)
print(\"GEOMETRIC/GROUP THEORY CANDIDATES\")
print(\"=\"*70)

# g1 analysis
print(\"\\n--- g1 (U(1) from S^1) ---\")
g_prime_KK = g1_KK / np.sqrt(5.0/3.0)
print(f\"  N1 = {N1:.6f}\")
print(f\"  Is N1 ~ 2?  Diff: {abs(N1-2.0):.4f} ({abs(N1-2.0)/N1*100:.2f}%)\")
print(f\"  sqrt(5/3) = {np.sqrt(5/3):.4f}\")
print(f\"  N1/sqrt(5/3) = {N1/np.sqrt(5/3):.4f}\")
print(f\"  If SCVC g1 is g': g1(GUT,SCVC)={np.sqrt(5/3)*g1_SCVC:.4f}, ratio={g1_KK/(np.sqrt(5/3)*g1_SCVC):.4f}\")

# g2 analysis
print(\"\\n--- g2 (SU(2) from S^2) ---\")
print(f\"  N2 = {N2:.6f}\")
print(f\"  Is N2 ~ 1/2?  Diff: {abs(N2-0.5):.4f} ({abs(N2-0.5)/abs(N2)*100:.2f}%)\")

# Dynkin index ratio
T_adj_SU2 = 2.0
T_fund_SU2 = 0.5
g_ratio_SU2 = np.sqrt(T_fund_SU2 / T_adj_SU2)
print(f\"  Dynkin: sqrt(T_fund/T_adj) = sqrt({T_fund_SU2}/{T_adj_SU2}) = {g_ratio_SU2:.4f}\")
print(f\"  N2 matches Dynkin ratio? match = {abs(N2-g_ratio_SU2)/abs(N2)*100:.2f}% deviation\")

# Check sqrt(pi/4) factor
print(f\"  sqrt(pi/4) = {np.sqrt(np.pi/4):.6f}\")
print(f\"  g2_SCVC * sqrt(pi/4) = {g2_SCVC * np.sqrt(np.pi/4):.4f}\")
print(f\"  g2_raw (before sqrt(pi/4)) = {g2_SCVC / np.sqrt(np.pi/4):.6f}\")

# g3 analysis
print(\"\\n--- g3 (SU(3) from CP^2) ---\")
print(f\"  N3 = {N3:.6f}\")
print(f\"  Is N3 ~ 1?  Diff: {abs(N3-1.0):.4f} ({abs(N3-1.0)/N3*100:.2f}%)\")

T_adj_SU3 = 3.0
T_fund_SU3 = 0.5
g_ratio_SU3 = np.sqrt(T_fund_SU3 / T_adj_SU3)
print(f\"  Dynkin: sqrt(T_fund/T_adj) = sqrt({T_fund_SU3}/{T_adj_SU3}) = {g_ratio_SU3:.4f}\")
print(f\"  N3 does NOT match Dynkin ratio ({g_ratio_SU3:.4f})\")

# sin^2 theta_W
print(\"\\n\" + \"=\"*70)
print(\"sin^2 theta_W ANALYSIS\")
print(\"=\"*70)

def sin2thetaW(g1, g2, gut=True):
    if gut:
        gp_sq = (3.0/5.0) * g1**2
    else:
        gp_sq = g1**2
    return gp_sq / (g2**2 + gp_sq)

s2w_MZ = sin2thetaW(g1_MZ, g2_MZ, True)
s2w_KK_SM = sin2thetaW(g1_KK, g2_KK, True)
s2w_KK_SCVC_raw = sin2thetaW(g1_SCVC, g2_SCVC, False)
s2w_KK_SCVC_GUT = sin2thetaW(g1_SCVC, g2_SCVC, True)

print(f\"  sin^2 theta_W(M_Z) from g1,g2:  {s2w_MZ:.6f}  (PDG: {sin2thetaW_MZ})\")
print(f\"  sin^2 theta_W(M_KK, SM):       {s2w_KK_SM:.6f}\")
print(f\"  sin^2 theta_W(M_KK, SCVC raw): {s2w_KK_SCVC_raw:.6f} (if g1=g')\")
print(f\"  sin^2 theta_W(M_KK, SCVC GUT): {s2w_KK_SCVC_GUT:.6f} (if g1=GUT)\")

# Propose normalized values
print(\"\\n\" + \"=\"*70)
print(\"PROPOSED NORMALIZATION DICTIONARY\")
print(\"=\"*70)

N1_prop = 2.0
N2_prop = 0.5
N3_prop = 1.0

g1_norm = g1_SCVC * N1_prop
g2_norm = g2_SCVC * N2_prop
g3_norm = g3_SCVC * N3_prop

print(f\"\\n  N1 = {N1_prop}  (geometric: S^1 Killing normalization)\")
print(f\"  N2 = {N2_prop}  (group theory: T_fund/T_adj for SU(2))\"  )
print(f\"  N3 = {N3_prop}  (CP^2 KK naturally gives fundamental norm)\")

print(f\"\\n  Normalized couplings:\")
print(f\"  g1: {g1_SCVC:.4f} x {N1_prop} = {g1_norm:.4f}  (SM: {g1_KK:.4f}, dev: {(g1_norm-g1_KK)/g1_KK*100:+.2f}%)\")
print(f\"  g2: {g2_SCVC:.4f} x {N2_prop} = {g2_norm:.4f}  (SM: {g2_KK:.4f}, dev: {(g2_norm-g2_KK)/g2_KK*100:+.2f}%)\")
print(f\"  g3: {g3_SCVC:.4f} x {N3_prop} = {g3_norm:.4f}  (SM: {g3_KK:.4f}, dev: {(g3_norm-g3_KK)/g3_KK*100:+.2f}%)\")

s2w_norm = sin2thetaW(g1_norm, g2_norm, True)
print(f\"\\n  sin^2 theta_W(M_KK, normalized): {s2w_norm:.6f}\")
print(f\"  sin^2 theta_W(M_KK, SM):         {s2w_KK_SM:.6f}\")

# RG run sin^2 theta_W back to M_Z
print(\"\\n\" + \"=\"*70)
print(\"RG RUNNING sin^2 theta_W: M_KK -> M_Z\")
print(\"=\"*70)

# sin^2 theta_W RG evolution at one loop:
# sin^2 theta_W(mu) = [3/5 - (8/5)alpha(mu)/alpha_s(mu) * (1 - ...)] ... 
# Actually, simpler to evolve g1 and g2 separately and compute sin^2 at M_Z

g1_KK_norm = g1_norm
g2_KK_norm = g2_norm

a1_KK_norm = g1_KK_norm**2 / (4*np.pi)
a2_KK_norm = g2_KK_norm**2 / (4*np.pi)

a1_MZ_norm_inv = 1.0/a1_KK_norm + b1/(2*np.pi) * log_factor
a2_MZ_norm_inv = 1.0/a2_KK_norm + b2/(2*np.pi) * log_factor

g1_MZ_norm = np.sqrt(4*np.pi / a1_MZ_norm_inv)
g2_MZ_norm = np.sqrt(4*np.pi / a2_MZ_norm_inv)

s2w_MZ_norm = sin2thetaW(g1_MZ_norm, g2_MZ_norm, True)
print(f\"  g1(M_Z, normalized RG): {g1_MZ_norm:.4f} (SM: {g1_MZ:.4f})\")
print(f\"  g2(M_Z, normalized RG): {g2_MZ_norm:.4f} (SM: {g2_MZ:.4f})\")
print(f\"  sin^2 theta_W(M_Z, normalized): {s2w_MZ_norm:.6f}\")
print(f\"  sin^2 theta_W(M_Z, PDG):        {sin2thetaW_MZ}\")
print(f\"  Deviation: {(s2w_MZ_norm-sin2thetaW_MZ)/sin2thetaW_MZ*100:+.2f}%\")

