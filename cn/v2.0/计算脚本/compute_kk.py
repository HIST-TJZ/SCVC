import numpy as np
from math import log, pi, sqrt
import json

# ============================================================
# PHYSICAL CONSTANTS & INPUT PARAMETERS
# ============================================================

alpha_s_MZ_exp = 0.1181
alpha_s_MZ_err = 0.0011
sin2thetaW_MZ_exp = 0.2312
sin2thetaW_MZ_err = 0.0003
M_Z = 91.1876
M_KK = 5.0e17
N1, N2, N3 = 2, 0.5, 1
g1_KK = 0.303
g2_KK = 1.055
alpha1_KK = g1_KK**2 / (4*pi)
alpha2_KK = g2_KK**2 / (4*pi)
alphaS_KK_predicted = 1.0 / (16.0 * pi)
alpha3_KK = alphaS_KK_predicted

# SM beta function coefficients
b1_SM = 41.0/10.0
b2_SM = -19.0/6.0
b3_SM = -7.0

# ============================================================
# CP² GEOMETRY
# ============================================================

def C2_SU3(p, q):
    return (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0

# R3 from first KK mode: m_KK = sqrt(C2(1,0))/R3
R3 = sqrt(C2_SU3(1, 0)) / M_KK
V_CP2 = (pi**2 / 2.0) * R3**4  # Volume

# ============================================================
# PART A: SCALAR KK SPECTRUM
# ============================================================

scalar_modes = []
max_level = 12
for n in range(max_level + 1):
    for p in range(n + 1):
        q = n - p
        lam = C2_SU3(p, q)
        mass = sqrt(lam) / R3
        deg = (1+p)*(1+q)*(2+p+q)//2
        scalar_modes.append({
            'p': p, 'q': q, 'lambda_R3sq': round(lam, 4),
            'mass_GeV': mass, 'degeneracy': deg
        })

scalar_modes.sort(key=lambda x: x['mass_GeV'])

# ============================================================
# PART B: VECTOR (1-FORM) SPECTRUM
# ============================================================

def vector_coexact_eigenvalue(p, q):
    return (C2_SU3(p, q) + 3) / R3**2

# ============================================================
# PART C: SPINOR SPECTRUM (spin^c Dirac)
# ============================================================

def spinor_eigenvalue_sq(p, q):
    return (C2_SU3(p, q) + 3) / R3**2

# ============================================================
# WEYL MODE COUNTING
# ============================================================

def count_scalar_modes_below(mass_cutoff):
    count = 0
    deg_sum = 0
    for m in scalar_modes:
        if m['mass_GeV'] < mass_cutoff:
            count += 1
            deg_sum += m['degeneracy']
    return count, deg_sum

def weyl_scalar_estimate(mu):
    return (mu / M_KK)**4 / 36.0

# ============================================================
# PART D: BETA FUNCTIONS
# ============================================================

C2_SU3_val = 3.0
C2_SU2_val = 2.0

# Per-level gauge contributions
delta_b_gauge_SU3_vec = -11.0/3.0 * C2_SU3_val  # vector part
delta_b_gauge_SU3_sca = 3 * (1.0/3.0) * C2_SU3_val  # 3 scalar components
delta_b_gauge_SU3_total = delta_b_gauge_SU3_vec + delta_b_gauge_SU3_sca

delta_b_gauge_SU2_vec = -11.0/3.0 * C2_SU2_val
delta_b_gauge_SU2_sca = 3 * (1.0/3.0) * C2_SU2_val

# Power-law coefficients b_tilde
# b_tilde = per-mode-contribution * density_factor
# density = Weyl coefficient in N(mu) ~ density * (mu/M_KK)^4

scalar_density = 1.0/36.0
coexact_1form_density = 3.0/36.0  # co-exact 1-forms
spinor_density = 4.0/36.0  # Dirac spinor on 4-manifold

b_tilde_3_gauge_vec = delta_b_gauge_SU3_vec * scalar_density
b_tilde_3_gauge_sca = delta_b_gauge_SU3_sca * coexact_1form_density
b_tilde_3_gauge = b_tilde_3_gauge_vec + b_tilde_3_gauge_sca

b_tilde_2_gauge_vec = delta_b_gauge_SU2_vec * scalar_density
b_tilde_2_gauge_sca = delta_b_gauge_SU2_sca * coexact_1form_density
b_tilde_2_gauge = b_tilde_2_gauge_vec + b_tilde_2_gauge_sca

# Fermion contributions (vector-like KK partners)
N_Dirac_quarks = 6  # u,d,c,s,t,b
b_tilde_3_fermion = (4.0/3.0) * (1.0/2.0) * N_Dirac_quarks * spinor_density

N_weyl_doublets = 6  # Q_L(3) + L_L(3)
b_tilde_2_fermion = (4.0/3.0) * (1.0/2.0) * N_weyl_doublets * spinor_density

# U(1): sum Y^2 over all Weyl fermions
sum_Y2 = 18*(1/36) + 9*(4/9) + 9*(1/9) + 6*(1/4) + 3*1  # = 10
b_tilde_1_fermion = (4.0/3.0) * sum_Y2 * spinor_density
b_tilde_1_fermion_GUT = b_tilde_1_fermion * (3.0/5.0)

# Higgs KK contribution
b_tilde_2_Higgs = (1.0/3.0) * (1.0/2.0) * scalar_density
b_tilde_1_Higgs = (1.0/3.0) * (1.0/4.0) * scalar_density * (3.0/5.0)

# Totals
b_tilde_3 = b_tilde_3_gauge + b_tilde_3_fermion
b_tilde_2 = b_tilde_2_gauge + b_tilde_2_fermion + b_tilde_2_Higgs
b_tilde_1 = 0 + b_tilde_1_fermion_GUT + b_tilde_1_Higgs  # U(1) gauge = 0

# ============================================================
# PART E: RG RUNNING
# ============================================================

ln_ratio = log(M_KK / M_Z)

# Inverse couplings at M_KK
a1_KK_inv = 1.0 / alpha1_KK
a2_KK_inv = 1.0 / alpha2_KK
a3_KK_inv = 1.0 / alpha3_KK

# Run DOWN to M_Z (SM beta functions, No KK modes below M_KK)
a1_MZ_inv = a1_KK_inv + (b1_SM/(2*pi)) * ln_ratio
a2_MZ_inv = a2_KK_inv + (b2_SM/(2*pi)) * ln_ratio
a3_MZ_inv = a3_KK_inv + (b3_SM/(2*pi)) * ln_ratio

alpha1_MZ = 1.0 / a1_MZ_inv
alpha2_MZ = 1.0 / a2_MZ_inv
alpha3_MZ = 1.0 / a3_MZ_inv

# sin^2 theta_W
alphaY_MZ = (3.0/5.0) * alpha1_MZ
aEM_MZ_inv = 1.0/alpha2_MZ + 1.0/alphaY_MZ
sin2W_pred = (1.0/aEM_MZ_inv) / alpha2_MZ
sin2W_MSbar = alphaY_MZ / (alphaY_MZ + alpha2_MZ)

# ============================================================
# DEVIATIONS
# ============================================================

dev_alphaS = alpha3_MZ - alpha_s_MZ_exp
dev_sin2W = sin2W_pred - sin2thetaW_MZ_exp
dev_pct_alphaS = abs(dev_alphaS) / alpha_s_MZ_exp * 100
dev_pct_sin2W = abs(dev_sin2W) / sin2thetaW_MZ_exp * 100

flag_alphaS = "GREEN" if dev_pct_alphaS < 2 else ("YELLOW" if dev_pct_alphaS < 5 else "RED")
flag_sin2W = "GREEN" if dev_pct_sin2W < 2 else ("YELLOW" if dev_pct_sin2W < 5 else "RED")

# ============================================================
# PARAMETRIC SCAN
# ============================================================

# Vary g2_KK
g2_scan = []
for dg2 in [-0.10, -0.05, 0.0, 0.05, 0.10]:
    g2_v = g2_KK + dg2
    a2_v = g2_v**2 / (4*pi)
    a2_inv_v = 1.0/a2_v
    a2_MZ_inv_v = a2_inv_v + (b2_SM/(2*pi)) * ln_ratio
    a2_MZ_v = 1.0/a2_MZ_inv_v
    aEM_inv_v = 1.0/a2_MZ_v + 1.0/alphaY_MZ
    s2W_v = (1.0/aEM_inv_v) / a2_MZ_v
    g2_scan.append({'g2': g2_v, 'alpha2_MZ': a2_MZ_v, 'sin2W': s2W_v})

# Vary M_KK
MKK_scan = []
for factor in [0.5, 0.8, 1.0, 1.2, 1.5, 2.0]:
    MKK_v = M_KK * factor
    ln_v = log(MKK_v / M_Z)
    a3_inv_v = a3_KK_inv + (b3_SM/(2*pi)) * ln_v
    a3_v = 1.0/a3_inv_v
    a2_inv_v = a2_KK_inv + (b2_SM/(2*pi)) * ln_v
    a2_v = 1.0/a2_inv_v
    a1_inv_v = a1_KK_inv + (b1_SM/(2*pi)) * ln_v
    a1_v = 1.0/a1_inv_v
    aY_v = (3.0/5.0) * a1_v
    aEM_inv_v = 1.0/a2_v + 1.0/aY_v
    s2W_v = (1.0/aEM_inv_v) / a2_v
    MKK_scan.append({
        'M_KK': MKK_v, 'ln_ratio': ln_v,
        'alpha3_MZ': a3_v, 'sin2W': s2W_v
    })

# ============================================================
# OUTPUT RESULTS
# ============================================================

results = {
    'framework': {
        'M_KK_GeV': M_KK,
        'M_Z_GeV': M_Z,
        'ln_MKK_MZ': round(ln_ratio, 2),
        'R3_GeV_inv': round(1.0/R3, 2),
        'R3_cm': round(R3 * 1.973e-14 * 1e13, 4),
        'V_CP2_R3_units': round(V_CP2 / R3**4, 4),
        'N1_N2_N3': [N1, N2, N3],
        'g1_KK': g1_KK,
        'g2_KK': g2_KK,
        'alpha1_KK': round(alpha1_KK, 6),
        'alpha2_KK': round(alpha2_KK, 6),
        'alpha3_KK_predicted': round(alpha3_KK, 6)
    },
    'scalar_spectrum': [
        {k: (round(v, 4) if isinstance(v, float) else v) for k, v in m.items()}
        for m in scalar_modes[:30]
    ],
    'mode_counting': {},
    'beta_functions': {
        'b_SM': [b1_SM, b2_SM, b3_SM],
        'b_tilde_KK': [round(b_tilde_1, 4), round(b_tilde_2, 4), round(b_tilde_3, 4)],
        'per_level_gauge_SU3': [round(delta_b_gauge_SU3_vec, 4), round(delta_b_gauge_SU3_sca, 4)],
        'per_level_gauge_SU2': [round(delta_b_gauge_SU2_vec, 4), round(delta_b_gauge_SU2_sca, 4)]
    },
    'RG_running': {
        'a1_MZ': round(alpha1_MZ, 6),
        'a2_MZ': round(alpha2_MZ, 6),
        'a3_MZ': round(alpha3_MZ, 6),
        'sin2W_pred': round(sin2W_pred, 6),
        'sin2W_MSbar': round(sin2W_MSbar, 6)
    },
    'comparison': {
        'alphaS_MZ_pred': round(alpha3_MZ, 6),
        'alphaS_MZ_exp': alpha_s_MZ_exp,
        'alphaS_MZ_err': alpha_s_MZ_err,
        'deviation_alphaS': round(dev_alphaS, 6),
        'deviation_pct_alphaS': round(dev_pct_alphaS, 2),
        'flag_alphaS': flag_alphaS,
        'sin2W_MZ_pred': round(sin2W_pred, 6),
        'sin2W_MZ_exp': sin2thetaW_MZ_exp,
        'sin2W_MZ_err': sin2thetaW_MZ_err,
        'deviation_sin2W': round(dev_sin2W, 6),
        'deviation_pct_sin2W': round(dev_pct_sin2W, 2),
        'flag_sin2W': flag_sin2W
    },
    'parametric_scan': {
        'g2_scan': g2_scan,
        'MKK_scan': MKK_scan
    }
}

# Mode counting at various cutoffs
for mc in [1, 2, 3, 5, 10]:
    cutoff = mc * M_KK
    cnt, deg_sum = count_scalar_modes_below(cutoff)
    weyl = weyl_scalar_estimate(cutoff)
    results['mode_counting'][f'{mc}x_MKK'] = {
        'levels': cnt, 'degeneracy_sum': deg_sum, 'weyl_estimate': round(weyl, 1)
    }

# Write JSON for later use
with open(r'C:\Users\20606\Documents\Codex\2026-07-21\p1-alphas-sin2thetaw-kk-md\work\results.json', 'w') as f:
    json.dump(results, f, indent=2, default=str)

print(json.dumps(results, indent=2, default=str))
print("\n=== COMPUTATION COMPLETE ===")

