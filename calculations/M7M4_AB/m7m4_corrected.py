"""
CORRECTED ANALYSIS: Flux and R^2 sign convention fix.
Key: F_R = -dV/dR. Negative dV/dR means REPULSIVE force (expansion).
"""
import numpy as np

print("=" * 70)
print("CORRECTED FORCE ANALYSIS: dV/dR vs F_R = -dV/dR")
print("=" * 70)

# Potential terms (V/M7^4):
# V_EH   = -4pi^2 * y                    dV_EH/dx=0,       dV_EH/dy=-4pi^2
# V_R2   = +16pi^2*cR2 * y/x^2           dV_R2/dx < 0,     dV_R2/dy > 0
# V_flux = +c_flux / (x^4*y)             dV_flux/dx < 0,   dV_flux/dy < 0  
# V_Cas  = -c_cas * g(x/y) / y^4        dV_Cas/dx > 0,    dV_Cas/dy > 0?

# Forces: F_x = -dV/dx, F_y = -dV/dy
# 
# F_x_R2  = -dV_R2/dx  = +32pi^2*cR2*y/x^3 > 0  → pushes x LARGER (repels)
# F_x_flux= -dV_flux/dx = +4*c_flux/(x^5*y) > 0  → pushes x LARGER (repels)  
# F_x_Cas = -dV_Cas/dx  = -c_cas*|g'|/y^5 < 0    → pushes x SMALLER (attracts)
#
# F_y_EH  = -dV_EH/dy   = +4pi^2 > 0             → pushes y LARGER (repels!)
# F_y_R2  = -dV_R2/dy   = -16pi^2*cR2/x^2 < 0    → pushes y SMALLER (attracts)
# F_y_flux= -dV_flux/dy = +c_flux/(x^4*y^2) > 0  → pushes y LARGER (repels)

# ===========================================================================
# Key insight: F_y_EH > 0 → EH term tries to EXPAND S^1, not collapse it!
# Both F_x_R2 and F_x_flux try to EXPAND S^2.
# Casimir provides the ONLY inward force on S^2.
# ===========================================================================

print("""
FORCE ANALYSIS (corrected for F = -dV/dr):
=============================================

S^2 direction (x = R*M7):
  F_x(EH)    = 0                          [EH doesn't depend on R directly]
  F_x(R^2)   = +32pi^2*cR2*y/x^3  > 0   [EXPANSION ← repulsive]
  F_x(flux)  = +4*c_flux/(x^5*y)  > 0   [EXPANSION ← repulsive]
  F_x(Cas)   = -c_cas*|g'|/y^5    < 0   [CONTRACTION ← attractive]
  
  → R^2 and flux try to expand S^2, Casimir tries to contract it.
  → Force balance IS possible: R^2+flux outward = Casimir inward

S^1 direction (y = R1*M7):
  F_y(EH)    = +4pi^2 = +39.5     > 0   [EXPANSION ← repulsive!]
  F_y(R^2)   = -16pi^2*cR2/x^2   < 0   [CONTRACTION ← attractive]
  F_y(flux)  = +c_flux/(x^4*y^2) > 0   [EXPANSION ← repulsive]
  F_y(Cas)   = +c_cas*(4g+g'*x/y)/y^5 [MIXED sign]
  
  → R^2 provides the ONLY inward force on S^1!
  → Balance: EH + flux outward = R^2 + Casimir inward

THE FUNDAMENTAL CHALLENGE (restated correctly):
=================================================
Both equilibrium conditions ∂V/∂x=0 and ∂V/∂y=0 must hold
SIMULTANEOUSLY. The magnitudes:

  |F_x(R^2+flux)| ~ O(10-100)   (large expansion force on S^2)
  |F_x(Cas)|      ~ O(0.001)    (tiny contraction force on S^2)
  → IMBALANCE: ~1000-100000x!

  |F_y(EH)|       = 39.5        (constant expansion force on S^1)
  |F_y(R^2)|      ~ O(10-100)   (contraction force, can be tuned)
  → y-equation CAN be balanced by tuning cR2/x^2

  But the x-equation CANNOT be balanced because:
  - R^2 and flux EXPAND S^2 (force ~O(10-100))
  - Casimir is the ONLY thing trying to CONTRACT S^2 (force ~O(0.001))
  - Mismatch: factor ~10^4-10^5

  THEREFORE: No stable minimum exists with physically reasonable
  Casimir coefficients.
""")

# Numerical verification
x0 = 0.442
y0 = 1.414
cR2 = 0.05
c_flux = 0.01
c_cas = 0.001

print(f"\nNumerical verification at x={x0}, y={y0}:")
print(f"  cR2={cR2}, c_flux={c_flux}, c_cas={c_cas}")

def V(x,y):
    Vt = -4*np.pi**2*y
    Vr = 16*np.pi**2*cR2*y/x**2
    Vf = c_flux/(x**4*y)
    z = x/y
    g = 2.0/(1+z**4)
    Vc = -c_cas*g/y**4
    return Vt+Vr+Vf+Vc

eps = 1e-6
dVdx = (V(x0+eps,y0)-V(x0-eps,y0))/(2*eps)
dVdy = (V(x0,y0+eps)-V(x0,y0-eps))/(2*eps)

print(f"  dV/dx = {dVdx:.3f}  (F_x = -dV/dx = {-dVdx:.3f}, {'EXPANSION' if -dVdx>0 else 'CONTRACTION'})")
print(f"  dV/dy = {dVdy:.3f}  (F_y = -dV/dy = {-dVdy:.3f}, {'EXPANSION' if -dVdy>0 else 'CONTRACTION'})")

# Individual contributions
def gradient_terms(x,y):
    dV_EH_dy = -4*np.pi**2
    
    dV_R2_dx = -32*np.pi**2*cR2*y/x**3
    dV_R2_dy = 16*np.pi**2*cR2/x**2
    
    dV_flux_dx = -4*c_flux/(x**5*y)
    dV_flux_dy = -c_flux/(x**4*y**2)
    
    z = x/y
    g = 2.0/(1+z**4)
    gp = -8*z**3/(1+z**4)**2
    dV_Cas_dx = -c_cas * gp / y**5  # dg/d(z)*dz/dx * 1/y^4
    dV_Cas_dy = -c_cas * (gp*(-x/y**2) / y**4 + g*(-4)/y**5)
    
    return {
        'EH_y': (-dV_EH_dy, 'expansion of S1'),
        'R2_x': (-dV_R2_dx, 'expansion of S2'),
        'R2_y': (-dV_R2_dy, 'contraction of S1'),
        'flux_x': (-dV_flux_dx, 'expansion of S2'),
        'flux_y': (-dV_flux_dy, 'expansion of S1'),
        'Cas_x': (-dV_Cas_dx, 'contraction of S2'),
        'Cas_y': (-dV_Cas_dy, 'mixed on S1'),
    }

terms = gradient_terms(x0, y0)
print("\nForce contributions (F = -dV/dr, positive = expansion):")
for name, (val, desc) in terms.items():
    print(f"  F_{name} = {val:+.4e}  [{desc}]")

F_S2_expand = terms['R2_x'][0] + terms['flux_x'][0]
F_S2_contract = terms['Cas_x'][0]
F_S1_expand = terms['EH_y'][0] + terms['flux_y'][0] + terms['Cas_y'][0]
F_S1_contract = terms['R2_y'][0]

print(f"\n  Net S2 force: expand={F_S2_expand:.1e}, contract={F_S2_contract:.1e}")
print(f"  Ratio S2 expand/contract = {abs(F_S2_expand/F_S2_contract):.0f}")
print(f"  Net S1 force: expand={F_S1_expand:.1f}, contract={F_S1_contract:.1f}")

print("""

FINAL CORRECTED CONCLUSION:
============================

The geometry CAN in principle support force balance:
- S^2: R^2+flux push outward (like radiation pressure), Casimir pulls inward
- S^1: EH pushes outward (S^2 curvature creates tension), R^2 pulls inward

But the force from R^2/flux on S^2 is ~10^5 times larger than the 
Casimir counter-force. To balance, we would need c_cas ~ O(10^3),
which is ~10^6 times the natural value per degree of freedom (~0.001).

This is NOT fine-tuning we can hand-wave away. It's a fundamental
mismatch of scales: curvature energies ~ O(M7^4) vs Casimir energies 
~ O(M7^4/1000). The Casimir effect on a positively curved compact
space simply cannot compete with the geometric tension.

WHAT WOULD ACTUALLY BE NEEDED:
  A mechanism that generates repulsion on S^2 at the SAME scale 
  as the curvature energy, i.e., O(M7^4), not O(M7^4/1000).
  
  Candidates that are NOT Casimir-scale:
  - Higher-spin fields with large Casimir (if SUSY broken badly)
  - Non-perturbative effects at Planck scale (wormholes? topology change?)
  - Strongly coupled conformal sector on M_vac
  - A completely different internal geometry
  
  None of these are calculable with current methods.
""")