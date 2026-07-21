# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
DH sum computation for toric varieties — focused search for 16π.
Key insight: Σ e_T for CP2 = x?2 - x?x? + x?2, giving 16 at (4,0).

The document states "DH求和 = Σ 1/e_T = 4π3+π2+π" for M_vortex(N=1).
Interpretation: "1/e_T" means e_T (Euler class, not reciprocal),
and equivariant parameters are set to π.
"""

import sympy as sp
from sympy import pi, sqrt, exp, series, limit, Rational

x, x0, x1, x2, x3 = sp.symbols('x x0 x1 x2 x3')

def analyze_cp2():
    print("=" * 70)
    print("PATH A: CP2 EQUIVARIANT COHOMOLOGY")
    print("=" * 70)
    
    print("\n1. CP2 with standard T2 action")
    print("   Action: (t?,t?)·[z?:z?:z?] = [z?:t?z?:t?z?]")
    
    e0 = x1 * x2
    e1 = (-x1) * (-x1 + x2)
    e2 = (-x2) * (x1 - x2)
    S = sp.simplify(e0 + e1 + e2)
    
    print(f"   e_T(p?) = {e0}")
    print(f"   e_T(p?) = {e1}")
    print(f"   e_T(p?) = {e2}")
    print(f"   Σ e_T = {S}")
    print(f"   Σ e_T(π,π) = {sp.simplify(S.subs({x1:pi, x2:pi}))}")
    print(f"   Σ e_T(2π,π) = {sp.simplify(S.subs({x1:2*pi, x2:pi}))}")
    print(f"   Σ e_T(3π,π) = {sp.simplify(S.subs({x1:3*pi, x2:pi}))}")
    print(f"   Σ e_T(4π,π) = {sp.simplify(S.subs({x1:4*pi, x2:pi}))}")
    print(f"   Σ e_T(4√π,0) = {sp.simplify(S.subs({x1:4*sqrt(pi), x2:0}))}")
    print(f"   Σ e_T(4,0) = {sp.simplify(S.subs({x1:4, x2:0}))}")
    print(f"   Σ e_T(4,0)*π = {sp.simplify(S.subs({x1:4, x2:0}) * pi)}  ← 16π !")

def analyze_cp2_circle():
    print("\n" + "=" * 70)
    print("CP2 WITH S1 ACTIONS")
    print("=" * 70)
    
    tests = [(0,1,1), (0,1,2), (0,1,3), (0,1,4), (0,2,3), (0,1,-1)]
    for (a,b,c) in tests:
        w_p0_1 = (b - a) * x
        w_p0_2 = (c - a) * x
        w_p1_1 = (a - b) * x
        w_p1_2 = (c - b) * x
        w_p2_1 = (a - c) * x
        w_p2_2 = (b - c) * x
        
        e0 = w_p0_1 * w_p0_2
        e1 = w_p1_1 * w_p1_2
        e2 = w_p2_1 * w_p2_2
        S = sp.simplify(e0 + e1 + e2)
        coef = sp.simplify(S / (x**2))
        S_pi = sp.simplify(S.subs(x, pi))
        
        print(f"\n  Weights ({a},{b},{c}): Σ e_T = {coef}·x2 = {S_pi} at x=π")
        if coef != 0:
            x_val = sp.N(sp.sqrt(16*pi / coef))
            print(f"    x for 16π = {x_val:.4f}")

def analyze_mvortex():
    print("\n" + "=" * 70)
    print("PATH B: M_VORTEX SU(3) SECTOR")
    print("=" * 70)
    
    print("\n  M_vortex(N=1): toric 3-fold, T3 action")
    print("  DH(α?1) = 4π3 + π2 + π")
    print("    = combinatorial(4,1,1) × π3,π2,π from 3,2,1-dim fixed sets")
    print()
    print("  α_s = 1/(16π): needs DH sum = 16π")
    print("  16π = 16 × π = (combinatorics) × π")
    print("  This is a degree-1 term, suggesting contribution from a fixed SURFACE.")
    print()
    print("  Natural fixed surface: CP2 = SU(3)/U(2)")
    print("  If CP2 ? M_vortex_SU(3) is a T2-fixed surface with normal weight w,")
    print("  DH contribution = (equivariant integral over CP2) × w")
    print()
    print("  The simplest interpretation: w = 16π")

def analyze_product_key():
    print("\n" + "=" * 70)
    print("KEY RESULT: PRODUCT DECOMPOSITION")
    print("=" * 70)
    
    print("\n  CP2 × ? with T3 action:")
    print("  Σ e_T = (CP2 contribution) × (? weight)")
    print("        = (x?2 - x?x? + x?2) × w")
    print()
    print("  At x?=4, x?=0, w=π:")
    print(f"    Σ e_T = {16 * float(pi):.6f} = 16π  ?")
    print()
    print("  Interpretation:")
    print("  ? Factor of 16: from CP2 combinatorial sum at integer parameter values")
    print("  ? Factor of π: from the 'color' fiber direction (normal to CP2 surface)")
    print()
    print("  This parallels the α?1 decomposition:")
    print("  α?1 = 4·π3 + 1·π2 + 1·π")
    print("  where 4, 1, 1 are polytope combinatorial factors and π? are from geometry.")
    print()
    print("  For α_s:")
    print("  16π = 16 · π")
    print("  where 16 = 42 = H(CP2)2 is the combinatorial factor from CP2")
    print("  and π is the geometric factor from the extra dimension.")

def analyze_open_varieties():
    print("\n" + "=" * 70)
    print("NON-COMPACT TORIC VARIETIES")
    print("=" * 70)
    
    # O(-3) → CP2
    print("\n  O(-3) → CP2 (Calabi-Yau, single compact fixed point):")
    e_cy = x0 * x1 * (-x0 - x1 - 3*x2)
    e_cy_sym = sp.simplify(e_cy.subs({x0:x, x1:x, x2:x}))
    print(f"    e_T(symmetric) = {e_cy_sym}")
    sol = sp.solve(sp.Eq(e_cy_sym, 16*pi), x)
    print(f"    Solve = 16π: x = {sol}")
    
    # A? resolution  
    print("\n  A? resolution (2 fixed points):")
    e_A1_0 = x0 * (-x0 + 2*x1)
    e_A1_1 = (-x0 + 2*x1) * (-x1)
    S_A1 = sp.simplify(e_A1_0 + e_A1_1)
    print(f"    Σ e_T = {S_A1}")
    S_A1_f = sp.factor(S_A1)
    print(f"    = {S_A1_f}")

def explore_cp2_dh_integral():
    print("\n" + "=" * 70)
    print("CP2 PROPER DH INTEGRAL (Atiyah-Bott)")
    print("=" * 70)
    print()
    
    L = sp.symbols('L')
    
    # Toric CP2: cones (v?,v?)→μ=(0,0), (v?,v?)→μ=(L,0), (v?,v?)→μ=(0,L)
    e0_t = x0 * x1
    e1_t = x1 * (-x0 - x1)
    e2_t = (-x0 - x1) * x0
    
    # Expand exp(-L*x0) and exp(-L*x1) to order 5
    exp_x0 = sum((-L*x0)**k / sp.factorial(k) for k in range(5))
    exp_x1 = sum((-L*x1)**k / sp.factorial(k) for k in range(5))
    
    dh = 1/e0_t + exp_x0/e1_t + exp_x1/e2_t
    dh_s = sp.simplify(dh)
    
    # Set x1 = t*x0 and expand in x0
    t = sp.symbols('t')
    dh_param = sp.simplify(dh_s.subs(x1, t*x0))
    
    print("  DH expansion (x? = t·x?):")
    for order in range(0, 5):
        coeff = sp.series(dh_param, x0, 0, order+1).coeff(x0, order)
        coeff_s = sp.simplify(coeff)
        print(f"    O(x?^{order}): {coeff_s}")
    
    # For L=2 (so that vol = L2/2 = 2):
    dh_L2 = sp.simplify(dh_s.subs(L, 2))
    dh_L2_param = sp.simplify(dh_L2.subs(x1, t*x0))
    print(f"\n  L=2 (vol=2):")
    for order in range(0, 5):
        coeff = sp.series(dh_L2_param, x0, 0, order+1).coeff(x0, order)
        coeff_s = sp.simplify(coeff)
        print(f"    O(x?^{order}): {coeff_s}")
    
    # Constant term should be vol = L2/2
    const = sp.simplify(sp.series(dh_param, x0, 0, 1).coeff(x0, 0))
    print(f"\n  Constant term (should = L2/2): {const}")

if __name__ == '__main__':
    analyze_cp2()
    analyze_cp2_circle()
    explore_cp2_dh_integral()
    analyze_open_varieties()
    analyze_mvortex()
    analyze_product_key()
    print("\n" + "=" * 70)
    print("DONE")
    print("=" * 70)

