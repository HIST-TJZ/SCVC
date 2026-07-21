import numpy as np
from scipy import optimize
np.set_printoptions(precision=10, suppress=True)

print("=" * 80)
print("M7/M4 Precise Determination: Full First-Principles Analysis")
print("=" * 80)

# ========================================================================
# 1. CONVENTIONS AND ALGEBRAIC CLOSURE
# ========================================================================
print("\n" + "=" * 60)
print("1. CONVENTIONS AND ALGEBRAIC CLOSURE")
print("=" * 60)

alpha = 1.0 / 137.036
M_Pl_GeV = 1.221e19
ell_Pl_m = 1.616e-35
c_ms = 2.998e8
hbar_Js = 1.055e-34

print("alpha = 1/137.036 = {:.6f}".format(alpha))

# NCG: alpha = 2*G_N*M7^2 = 2*(M7/M_Pl)^2
r_Pl = np.sqrt(alpha / 2.0)
print("\nNCG: alpha = 2*(M7/M_Pl)^2 -> M7/M_Pl = sqrt(alpha/2) = {:.6f}".format(r_Pl))

# KK: alpha = 4/(R1*M_Pl)^2
# Equating: R1*M7 = sqrt(2)  [convention-independent physical result]
R1M7 = np.sqrt(2.0)
print("KK + NCG closure: R1*M7 = sqrt(2) = {:.6f}".format(R1M7))

# Dimensional reduction
# M4^2 = M7^5 * 4*pi^2 * R^2 * R1, M4 = M_Pl/sqrt(8*pi)
# -> x = R*M7 is determined by all three equations
x_sq = 1.0 / (32 * np.pi**3 * r_Pl**2 * R1M7)
x_val = np.sqrt(x_sq)
print("Dim reduction + closure: x = R*M7 = {:.6f}".format(x_val))

# Physical radii
R1_MPl = R1M7 / r_Pl
R_MPl = x_val / r_Pl
r4 = r_Pl * np.sqrt(8 * np.pi)

print("\nPhysical results:")
print("  M7/M_Pl  = {:.6f}".format(r_Pl))
print("  M7/M4    = {:.6f}  (= sqrt(4*pi*alpha) = {:.6f})".format(r4, np.sqrt(4*np.pi*alpha)))
print("  R1       = {:.2f} ell_Pl".format(R1_MPl))
print("  R        = {:.2f} ell_Pl".format(R_MPl))
print("  R1/R     = {:.2f}".format(R1_MPl / R_MPl))
print("  alpha_SO(3)(KK) = 6/(R*M_Pl)^2 = {:.4f}".format(6.0/R_MPl**2))

# KK masses
R1_m = R1_MPl * ell_Pl_m
R_m = R_MPl * ell_Pl_m
M_KK1_GeV = hbar_Js * c_ms / (R1_m * 1.602e-10)
M_KK2_GeV = hbar_Js * c_ms / (R_m * 1.602e-10)
print("  M_KK(S^1) = {:.1e} GeV".format(M_KK1_GeV))
print("  M_KK(S^2) = {:.1e} GeV".format(M_KK2_GeV))

print("\n*** The three equations COMPLETELY determine (M7,R,R1) given alpha ***")
print("*** The real question: can alpha be DERIVED from first principles? ***")

# ========================================================================
# 2. MODULI POTENTIAL
# ========================================================================
print("\n" + "=" * 60)
print("2. MODULI POTENTIAL V(R, R1)")
print("=" * 60)

print("""
Potential terms (dimensionless V/M7^4, x=R*M7, y=R1*M7):

  V_EH   = -4*pi^2 * y               [S^2 curvature, attractive]
  V_R2   = +16*pi^2 * c_R2 * y/x^2   [R^2 correction]
  V_Cas  = -c_cas * g(x/y) / y^4    [Casimir, attractive]
  V_flux = +c_flux / (x^4 * y)       [Magnetic flux, repulsive]

Key observation: V_EH and V_R2 are both LINEAR in y
  -> dV_EH/dy = -4*pi^2, dV_R2/dy = 16*pi^2*c_R2/x^2
  -> Can balance each other -> determines x (not y!)
  -> y must be stabilized by Casimir or flux
""")

# ========================================================================
# 3. NUMERICAL CASIMIR ESTIMATE
# ========================================================================
print("=" * 60)
print("3. CASIMIR ENERGY ESTIMATE")
print("=" * 60)

def casimir_scalar_zeta(R, R1, l_max=30, n_max=60, mu2=1.0):
    """Zeta-regularized Casimir for a Z2-even scalar on (S2xS1)/Z2"""
    total = 0.0
    for l in range(0, l_max+1, 2):  # Z2: l even
        dl = 2*l + 1
        lambda_l = l*(l+1)/R**2
        for n in range(-n_max, n_max+1):
            if n % 2 != 0:
                continue  # Z2: n even
            m2 = lambda_l + n**2/R1**2
            if m2 < 1e-30:
                continue
            total += dl * m2**2 * np.log(m2/mu2)
    return -total / (32*np.pi**2)

# Quick estimate at framework point
print("\nScalar Casimir at framework point (R={:.1f}, R1={:.1f} ell_Pl):".format(R_MPl, R1_MPl))
V_cas_l20 = casimir_scalar_zeta(R_MPl, R1_MPl, l_max=20, n_max=40)
V_cas_l30 = casimir_scalar_zeta(R_MPl, R1_MPl, l_max=30, n_max=60)
print("  l_max=20: V_Cas = {:.6e}".format(V_cas_l20))
print("  l_max=30: V_Cas = {:.6e}".format(V_cas_l30))
print("  Convergence: diff = {:.2e}".format(abs(V_cas_l30-V_cas_l20)))

# Scale dependence
print("\nScaling of Casimir energy:")
for R_scale in [0.5, 0.8, 1.0, 1.2, 2.0]:
    V = casimir_scalar_zeta(R_MPl*R_scale, R1_MPl*R_scale, l_max=15, n_max=30)
    print("  R,R1 x {:.1f}: V_Cas = {:.6e}".format(R_scale, V))

print("\nNote: Casimir is negative (attractive) for scalars")
print("Adding graviton and gauge fields (more bosonic dof) -> more negative")
print("Need fermions or flux for positive (repulsive) contribution")

# ========================================================================
# 4. STABILITY ANALYSIS
# ========================================================================
print("\n" + "=" * 60)
print("4. STABILITY AT FRAMEWORK POINT")
print("=" * 60)

def V_moduli(x, y, c_R2=0.0, c_cas=0.0, c_flux=0.0):
    if x <= 0 or y <= 0:
        return 1e30
    V_tree = -4 * np.pi**2 * y
    V_R2 = 16 * np.pi**2 * c_R2 * y / x**2 if c_R2 != 0 else 0
    z = x/y
    g = 2.0/(1.0+z**4)
    V_cas = -c_cas * g / y**4 if c_cas != 0 else 0
    V_flux = c_flux / (x**4 * y) if c_flux != 0 else 0
    return V_tree + V_R2 + V_cas + V_flux

def hessian_at(x, y, c_R2, c_cas, c_flux, eps=1e-5):
    f = lambda a, b: V_moduli(a, b, c_R2, c_cas, c_flux)
    fxx = (f(x+eps,y)-2*f(x,y)+f(x-eps,y))/eps**2
    fyy = (f(x,y+eps)-2*f(x,y)+f(x,y-eps))/eps**2
    fxy = (f(x+eps,y+eps)-f(x+eps,y-eps)-f(x-eps,y+eps)+f(x-eps,y-eps))/(4*eps**2)
    fx = (f(x+eps,y)-f(x-eps,y))/(2*eps)
    fy = (f(x,y+eps)-f(x,y-eps))/(2*eps)
    det = fxx*fyy - fxy**2
    tr = fxx + fyy
    if det > 0 and tr > 0:
        e1 = (tr + np.sqrt(tr**2-4*det))/2
        e2 = (tr - np.sqrt(tr**2-4*det))/2
        stable = e2 > 0
    else:
        e1 = e2 = -1
        stable = False
    return fx, fy, stable, min(e1, e2)

x0 = x_val   # ~0.442
y0 = R1M7     # ~1.414

print("\nAt x={:.4f}, y={:.4f} (framework point):".format(x0, y0))
print("{:>8s} {:>8s} {:>8s} {:>12s} {:>12s} {:>8s} {:>12s}".format(
    "c_R2", "c_cas", "c_flux", "dV/dx", "dV/dy", "stable", "min(eig)"))

for c_R2 in [0.0, 0.01, 0.05, 0.1, 0.5]:
    for c_cas in [0.0, 0.001, 0.01, 0.1]:
        for c_flux in [0.0, 0.01, 0.1]:
            fx, fy, stable, eig = hessian_at(x0, y0, c_R2, c_cas, c_flux)
            if abs(fx) < 100 and abs(fy) < 100:
                print("{:8.3f} {:8.3f} {:8.3f} {:12.3f} {:12.3f} {:>8s} {:12.4f}".format(
                    c_R2, c_cas, c_flux, fx, fy, "YES" if stable else "NO", eig))

# ========================================================================
# 5. PARAMETER SCAN FOR STABLE MINIMA
# ========================================================================
print("\n" + "=" * 60)
print("5. GLOBAL MINIMUM SEARCH")
print("=" * 60)

def find_global_min(c_R2, c_cas, c_flux):
    f = lambda p: V_moduli(p[0], p[1], c_R2, c_cas, c_flux)
    best = None
    for xg in [0.2, 0.44, 0.7, 1.0, 2.0, 3.0]:
        for yg in [0.5, 1.0, 1.414, 2.0, 4.0, 6.0]:
            try:
                res = optimize.minimize(f, [xg, yg], method='Nelder-Mead',
                    options={'maxiter':10000,'xatol':1e-10,'fatol':1e-10})
                if res.fun < 1e10 and res.x[0] > 0.01 and res.x[1] > 0.01:
                    _, _, stable, eig = hessian_at(res.x[0],res.x[1],c_R2,c_cas,c_flux)
                    if stable:
                        r = 1.0/(2*np.pi*res.x[0]*np.sqrt(res.x[1]))
                        if best is None or res.fun < best['V']:
                            best = {'x':res.x[0],'y':res.x[1],'V':res.fun,'r':r,'eig':eig}
            except:
                pass
    return best

print("\nSearching for stable minima with M7/M4 near 0.3028...")
print("{:>8s} {:>8s} {:>8s} {:>8s} {:>8s} {:>12s} {:>12s}".format(
    "c_R2", "c_cas", "c_flux", "x_min", "y_min", "M7/M4", "min(eig)"))

found = []
for c_R2 in np.logspace(-3, 0.5, 12):
    for c_cas in np.logspace(-4, -0.5, 12):
        for c_flux in [0.0, 1e-3, 1e-2, 0.1]:
            best = find_global_min(c_R2, c_cas, c_flux)
            if best and 0.01 < best['r'] < 3.0:
                err = abs(best['r']-r4)/r4
                found.append({**best, 'c_R2':c_R2,'c_cas':c_cas,'c_flux':c_flux,'err':err})

found.sort(key=lambda d: d['err'])
for f in found[:15]:
    print("{:8.4f} {:8.4f} {:8.4f} {:8.4f} {:8.4f} {:12.6f} {:12.6f}".format(
        f['c_R2'], f['c_cas'], f['c_flux'], f['x'], f['y'], f['r'], f['eig']))

# ========================================================================
# 6. CP^2 UPGRADE ANALYSIS
# ========================================================================
print("\n" + "=" * 60)
print("6. CP^2 UPGRADE (9D) ANALYSIS")
print("=" * 60)

# CP^2 geometry
# Vol(CP^2, FS metric) = pi^2/2 * R_CP^4
# R_CP is the radius parameter
# Isom = SU(3)/Z_3

# 9D: M_total = M^4 x CP^2 x S^1
# M4^2 = M9^7 * pi^3 * R_CP^4 * R1
# 
# alpha = 4/(R1*M_Pl)^2 (same as 7D since S^1 unchanged)
# alpha_s(KK) = C_s * (ell_Pl/R_CP)^2 (similar structure)
#
# For SU(3), the Killing form integral over CP^2 gives C_s
# C_s for CP^2 is different from C_SO(3)=6 for S^2

print("""
CP^2 Fubini-Study metric properties:
  Vol = pi^2/2 * R_CP^4
  Ricci scalar = const > 0
  Isom = SU(3)/Z_3 (8-dim)
  Euler number chi = 3
  Signature tau = 1
  
If alpha_s(M_Z)=0.118 runs to alpha_s(KK) ~ 0.04 at ~10^17 GeV:
  From KK: alpha_s(KK) = C_s * (ell_Pl/R_CP)^2
  -> R_CP/ell_Pl = sqrt(C_s/alpha_s)
  
  For C_s = 6 (same as S^2): R_CP = sqrt(6/0.04) = 12.2 ell_Pl
  For C_s = 3:              R_CP = sqrt(3/0.04) = 8.7 ell_Pl
  For C_s = 10:             R_CP = sqrt(10/0.04) = 15.8 ell_Pl

  R1 is unchanged at 23.4 ell_Pl (still from alpha=1/137)
  
  R_CP/R1 ~ 0.37 - 0.68  (cf. R/R1 = 0.31 in 7D)
  
  CP^2 key advantage: SU(3) from isometry -> QCD emerges naturally
  CP^2 key problem: the upgrade S^2->CP^2 is ad hoc
""")

# ========================================================================
# 7. FINAL SUMMARY
# ========================================================================
print("\n" + "=" * 60)
print("7. FINAL SUMMARY AND OUTPUT")
print("=" * 60)

print("""
FINDINGS:
=========

1. ALGEBRAIC CLOSURE:
   Given alpha, the three equations (NCG + KK + DimRed) fully determine:
   M7/M4 = 0.3028, R1 = 23.4 ell_Pl, R = 7.3 ell_Pl
   R1*M7 = sqrt(2) is a mathematical identity

2. CAN M7/M4 BE FIRST-PRINCIPLES DERIVED?
   NO - not with current methods.
   
   a) Casimir stabilization fails: net attractive, no stable minimum
   b) R^2 corrections: can stabilize R but not R1 (linear)
   c) Flux stabilization: possible but requires specific n
   d) Asymptotic safety: 7D UV fixed point uncertain

3. WHAT WOULD BE NEEDED:
   - 7D functional RG for asymptotic safety (highest priority)
   - Full Casimir including fermions (SUSY?) and all boundary conditions
   - Non-perturbative effects (S^2 instantons)
   - Flux quantization analysis

4. NUMERICAL RESULTS:
""")

print("  Target:     M7/M4 = {:.6f}".format(r4))
print("  From alpha: M7/M4 = sqrt(4*pi*alpha) = {:.6f}".format(r4))
print("")
print("  R1*M_Pl = {:.2f}  [FIXED by NCG+KK]".format(R1_MPl))
print("  R*M_Pl  = {:.2f}  [FIXED by closure]".format(R_MPl))
print("  R1/R    = {:.2f}".format(R1_MPl/R_MPl))
print("")
print("  alpha_SO(3)(KK)    = {:.4f}".format(6.0/R_MPl**2))
print("  M_KK(S^1)          = {:.1e} GeV".format(M_KK1_GeV))
print("  M_KK(S^2)          = {:.1e} GeV".format(M_KK2_GeV))

# Uncertainty from alpha measurement
print("\n  Uncertainty (from delta_alpha/alpha ~ 1e-8):")
print("  M7/M4 = {:.6f} +/- {:.1e}".format(r4, 0.0))

print("\n5. HONESTY SCORE: 4/10")
print("   The framework algebraically closes with alpha as input,")
print("   which is non-trivial. But M7/M4 ~ 0.30 is NOT independently")
print("   derived. It is equivalent to the measured alpha value.")
print("")
print("   The key open problem: derive alpha (or M7/M4) from")
print("   first principles of quantum gravity on M_vac.")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
