import numpy as np
from scipy.integrate import solve_ivp
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

print("="*70)
print("SM COUPLINGS AT M_Z")
print("="*70)
print(f"  alpha^-1(M_Z)   = {alpha_inv_MZ}")
print(f"  sin^2 theta_W   = {sin2thetaW_MZ}")
print(f"  alpha_s(M_Z)    = {alpha_s_MZ}")
print(f"  e(M_Z)          = {e_MZ:.6f}")
print(f"  g' (U(1)_Y)     = {g_prime_MZ:.6f}")
print(f"  g1 (GUT norm)   = {g1_MZ:.6f}")
print(f"  g2 (SU(2)_L)    = {g2_MZ:.6f}")
print(f"  g3 (SU(3)_c)    = {g3_MZ:.6f}")

b1 = 41.0/10.0
b2 = -19.0/6.0
b3 = -7.0

log_factor = np.log(M_KK / M_Z)
print(f"\nln(M_KK/M_Z) = {log_factor:.4f}")

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

print("\n" + "="*70)
print("ONE-LOOP RG RUNNING TO M_KK")
print("="*70)
print(f"  g1(M_KK) = {g1_KK:.4f}")
print(f"  g2(M_KK) = {g2_KK:.4f}")
print(f"  g3(M_KK) = {g3_KK:.4f}")
print(f"  alpha_s(M_KK) = {alpha_s_KK:.6f}")

# SCVC values
g1_SCVC = 0.303
g2_SCVC = 1.053
alpha_s_SCVC = 0.0199
g3_SCVC = np.sqrt(4*np.pi * alpha_s_SCVC)

N1 = g1_KK / g1_SCVC
N2 = g2_KK / g2_SCVC
N3 = g3_KK / g3_SCVC

print("\n" + "="*70)
print("SCVC vs SM COMPARISON AT M_KK")
print("="*70)
print(f"{'Coupling':<12} {'SCVC':>10} {'SM(M_KK)':>12} {'Ratio N_i':>12}")
print("-"*48)
print(f"{'g1':<12} {g1_SCVC:>10.4f} {g1_KK:>12.4f} {N1:>12.4f}")
print(f"{'g2':<12} {g2_SCVC:>10.4f} {g2_KK:>12.4f} {N2:>12.4f}")
print(f"{'g3':<12} {g3_SCVC:>10.4f} {g3_KK:>12.4f} {N3:>12.4f}")

# sin^2 theta_W
def sin2thetaW(g1, g2, gut=True):
    if gut:
        gp_sq = (3.0/5.0) * g1**2
    else:
        gp_sq = g1**2
    return gp_sq / (g2**2 + gp_sq)

s2w_KK_SM = sin2thetaW(g1_KK, g2_KK, True)
s2w_KK_SCVC = sin2thetaW(g1_SCVC, g2_SCVC, False)
s2w_KK_SCVC_GUT = sin2thetaW(g1_SCVC, g2_SCVC, True)

print(f"\nsin^2theta_W at M_KK:")
print(f"  SM:      {s2w_KK_SM:.6f}")
print(f"  SCVC(raw, g1=g'): {s2w_KK_SCVC:.6f}")
print(f"  SCVC(GUT norm):   {s2w_KK_SCVC_GUT:.6f}")

# Proposed normalization
print("\n" + "="*70)
print("PROPOSED NORMALIZATION DICTIONARY")
print("="*70)
print(f"  N1 = 2   (geometric, S^1 Killing)")
print(f"  N2 = 1/2 (group theory, T_fund/T_adj SU(2))")
print(f"  N3 = 1   (CP^2 naturally fundamental)")

g1n = g1_SCVC * 2.0
g2n = g2_SCVC * 0.5
g3n = g3_SCVC * 1.0
print(f"\n  Normalized: g1={g1n:.4f}, g2={g2n:.4f}, g3={g3n:.4f}")
print(f"  SM at M_KK: g1={g1_KK:.4f}, g2={g2_KK:.4f}, g3={g3_KK:.4f}")
print(f"  Deviations: g1={(g1n-g1_KK)/g1_KK*100:+.2f}%, g2={(g2n-g2_KK)/g2_KK*100:+.2f}%, g3={(g3n-g3_KK)/g3_KK*100:+.2f}%")

# RG backward
print("\n" + "="*70)
print("RG RUNNING NORMALIZED SCVC -> M_Z")
print("="*70)
a1n_inv = 4*np.pi/g1n**2
a2n_inv = 4*np.pi/g2n**2
a1n_MZ_inv = a1n_inv + b1/(2*np.pi)*log_factor
a2n_MZ_inv = a2n_inv + b2/(2*np.pi)*log_factor
g1n_MZ = np.sqrt(4*np.pi/a1n_MZ_inv)
g2n_MZ = np.sqrt(4*np.pi/a2n_MZ_inv)
s2w_n_MZ = sin2thetaW(g1n_MZ, g2n_MZ, True)
print(f"  g1(M_Z) = {g1n_MZ:.4f} (SM: {g1_MZ:.4f})")
print(f"  g2(M_Z) = {g2n_MZ:.4f} (SM: {g2_MZ:.4f})")
print(f"  sin^2theta_W(M_Z) = {s2w_n_MZ:.6f} (PDG: {sin2thetaW_MZ})")
print(f"  Deviation: {(s2w_n_MZ-sin2thetaW_MZ)/sin2thetaW_MZ*100:+.2f}%")
