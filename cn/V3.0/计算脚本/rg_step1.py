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

print(\"=\"*70)
print(\"SM COUPLINGS AT M_Z\")
print(\"=\"*70)
print(f\"  alpha^-1(M_Z)   = {alpha_inv_MZ}\")
print(f\"  sin^2 theta_W   = {sin2thetaW_MZ}\")
print(f\"  alpha_s(M_Z)    = {alpha_s_MZ}\")
print(f\"  e(M_Z)          = {e_MZ:.6f}\")
print(f\"  g' (U(1)_Y)     = {g_prime_MZ:.6f}\")
print(f\"  g1 (GUT norm)   = {g1_MZ:.6f}\")
print(f\"  g2 (SU(2)_L)    = {g2_MZ:.6f}\")
print(f\"  g3 (SU(3)_c)    = {g3_MZ:.6f}\")

b1 = 41.0/10.0
b2 = -19.0/6.0
b3 = -7.0

log_factor = np.log(M_KK / M_Z)
print(f\"\\nln(M_KK/M_Z) = {log_factor:.4f}\")

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

print(\"\\n\" + \"=\"*70)
print(\"ONE-LOOP RG RUNNING TO M_KK\")
print(\"=\"*70)
print(f\"  g1(M_KK) = {g1_KK:.4f}\")
print(f\"  g2(M_KK) = {g2_KK:.4f}\")
print(f\"  g3(M_KK) = {g3_KK:.4f}\")
print(f\"  alpha_s(M_KK) = {alpha_s_KK:.6f}\")
