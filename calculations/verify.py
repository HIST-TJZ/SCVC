"""
KK gauge coupling calculation from M_vac = (S^2 x S^1)/Z_2
Verification of all integrals using sympy.
"""
import sympy as sp

R1, R2, GN = sp.symbols("R1 R2 GN", positive=True)
theta, phi, psi = sp.symbols("theta phi psi", real=True)

# === Volumes ===
Vol_S2 = 4*sp.pi*R2**2
Vol_S1 = 2*sp.pi*R1
Vol_Mvac = sp.Rational(1,2) * Vol_S2 * Vol_S1  # 4*pi^2 * R2^2 * R1
G7 = Vol_Mvac * GN  # G_7 = 4*pi^2 * GN * R1 * R2^2

print("="*60)
print("M_vac = (S^2 x S^1)/Z_2  KK Gauge Coupling")
print("="*60)

# === U(1) from S^1 ===
# Killing vector K = partial_psi, K^psi=1, gamma_psipsi=R1^2
# G_U1 = R1^2 (constant over M_vac)
# integral: R1^2 * Vol(M_vac) = 4*pi^2 * R1^3 * R2^2
int_U1 = R1**2 * Vol_Mvac

g2_U1_inv = sp.simplify(int_U1 / (16*sp.pi*G7))
g2_U1 = sp.simplify(1/g2_U1_inv)
alpha_U1 = sp.simplify(g2_U1/(4*sp.pi))

print(f"\n--- U(1) gauge coupling (from S^1) ---")
print(f"integral = {int_U1}")
print(f"1/g^2     = {g2_U1_inv}")
print(f"g^2       = {g2_U1}")
print(f"alpha     = {alpha_U1}")

# === SO(3) from S^2 ===
# K^3 = d_phi,  gamma_phiphi = R2^2 sin^2(theta)
# G_33 = R2^2 sin^2(theta)
# sqrt(gamma_S2) = R2^2 sin(theta)
integrand_K3 = R2**4 * sp.sin(theta)**3
int_K3_S2 = sp.integrate(sp.integrate(integrand_K3, (phi, 0, 2*sp.pi)), (theta, 0, sp.pi))
# By SO(3) symmetry: int G_ab = int_K3_S2 * delta_ab
# Full M_vac: (1/2) * Vol_S1 * int_K3_S2 = (1/2)*2*pi*R1 * int_K3_S2
int_SO3 = sp.Rational(1,2) * Vol_S1 * int_K3_S2

g2_SO3_inv = sp.simplify(int_SO3 / (16*sp.pi*G7))
g2_SO3 = sp.simplify(1/g2_SO3_inv)
alpha_SO3 = sp.simplify(g2_SO3/(4*sp.pi))

print(f"\n--- SO(3) gauge coupling (from S^2) ---")
print(f"int_S2 K3.K3 = {sp.simplify(int_K3_S2)}")
print(f"int_Mvac      = {sp.simplify(int_SO3)}")
print(f"1/g^2         = {g2_SO3_inv}")
print(f"g^2           = {g2_SO3}")
print(f"alpha         = {alpha_SO3}")

# === Numerical ===
lPl = 1.616e-35
print(f"\n--- Numerical (l_Pl = {lPl:.3e} m) ---")
print(f"alpha_U1  = 4 * (l_Pl/R1)^2")
print(f"alpha_SO3 = 6 * (l_Pl/R2)^2")

for name, coeff in [("U(1)", 4), ("SO(3)", 6)]:
    R_for_fine = (coeff * 137)**0.5
    print(f"  For alpha_{name} = 1/137: R = sqrt({coeff}*137) * l_Pl = {R_for_fine:.1f} * l_Pl = {R_for_fine*lPl:.3e} m")

print("\nDone. All integrals verified.")
