# -*- coding: utf-8 -*-
"""SCVC涡旋剖面计算脚本 — 复现用
运行: python vortex_profile_cp2.py
"""

import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import root_scalar

# ===== 常数 =====
hbar = 1.054571817e-34
c = 2.99792458e8
GN = 6.67430e-11
H0 = 2.1928e-18
alpha_fs = 1/137.035999084
me_exp = 9.1093837e-31
l_Pl = np.sqrt(hbar*GN/c**3)
m_Pl = np.sqrt(hbar*c/GN)

# ===== 涡旋几何 =====
r_e = alpha_fs * hbar / (me_exp * c)
a_vortex = r_e * (np.pi/2)**(1/3)
ln_factor = abs(np.log(r_e/a_vortex))

# ===== 超流密度 =====
m_c = m_Pl
kappa = 2*np.pi*hbar/m_c
S_vortex = 2*me_exp*c**2/(r_e*ln_factor)
rho_s = S_vortex/kappa**2

# ===== GL参数 =====
a_s = l_Pl
xi = np.sqrt(m_c/(8*np.pi*a_s*rho_s))
print(f"ξ = {xi:.4e} m, a = {a_vortex:.4e} m, ξ/a = {xi/a_vortex:.4f}")

# ===== GP涡旋剖面 =====
def gp_ode(r, y):
    f, fp = y
    fpp = -fp/r + f/r**2 + f**3 - f
    return [fp, fpp]

def shoot(c1):
    r0 = 1e-6
    c3 = -c1/8
    f0 = c1*r0 + c3*r0**3
    fp0 = c1 + 3*c3*r0**2
    sol = solve_ivp(gp_ode, [r0, 20], [f0, fp0], max_step=0.1, rtol=1e-8)
    return sol.y[0,-1] - 1.0

c1 = root_scalar(shoot, bracket=[0.5, 2.0], method='brentq').root
print(f"c₁ = {c1:.8f}")

# ===== CP²积分 =====
sigma = a_vortex/r_e
print(f"σ = a/r_e = {sigma:.6f}")

def integrand_Phi(r, sig):
    return np.exp(-r**2/(2*sig**2))/(1+r**2)**6 * 2*np.pi**2 * r**3

I_phi, _ = quad(lambda r: integrand_Phi(r, sigma), 0, np.inf)
print(f"∫Φ dvol = {I_phi:.6e}")

# 费米子波函数归一化
I_psi, _ = quad(lambda r: 1/(1+r**2)**6 * 2*np.pi**2 * r**3, 0, np.inf)
print(f"∫|ψ₀|² dvol = {I_psi:.6f} (理论 π²/20 = {np.pi**2/20:.6f})")

print("\n完成。")
