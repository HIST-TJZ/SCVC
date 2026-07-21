# g1 = SCVC g1 analysis
# What exact geometric formulas give g1 in SCVC?
import numpy as np

print("="*70)
print("DETAILED g1 ANALYSIS: S^1 KK REDUCTION")
print("="*70)

# The SCVC framework has alpha = 4(ell_Pl / R1)^2 and g1 = sqrt(4*pi*alpha)
# = sqrt(4*pi) * 2 * ell_Pl / R1

# In KK theory:
# S^1 radius R1, circumference = 2*pi*R1 (but with Z2: pi*R1)
# Planck length from 7D: ell_Pl^2 = G_N (4D Newton constant)

# 7D Einstein-Hilbert: S = 1/(2*kappa_7^2) integral d^7x sqrt(-g7) R7
# Compactify on M_vac = (S^2 x S^1)/Z2
# Volume: Vol(S^2) = 4*pi*R2^2, Vol(S^1/Z2) = pi*R1
# Total Vol = 4*pi^2 * R2^2 * R1

# 4D Planck: 1/kappa_4^2 = Vol / kappa_7^2

# For the S^1 U(1) coupling:
# 1/g^2 = (1/kappa_7^2) * integral_S1 sqrt(gamma) gamma^{psipsi} K_psi K_psi
# K = d/dpsi, K_psi = g_{psi psi} K^psi = R1^2
# sqrt(gamma) = R1, gamma^{psipsi} = 1/R1^2
# integrand = R1 * (1/R1^2) * R1^4 = R1^3
# integral = pi*R1^3 (Z2 quotient: psi in [0, pi))

# Actually wait, with Z2: the integration range is [0, pi) not [0, 2pi)
# So integral = R1^3 * pi

# Without Z2: integral = 2*pi*R1^3

# 1/g^2 = (pi*R1^3) / kappa_7^2

# Express kappa_7^2 in terms of kappa_4^2:
# 1/kappa_7^2 = Vol / kappa_4^2 = (4*pi^2*R2^2*R1) / kappa_4^2

# So: 1/g^2 = (pi*R1^3) * (4*pi^2*R2^2*R1) / kappa_4^2
# = 4*pi^3 * R1^4 * R2^2 / kappa_4^2

# g^2 = kappa_4^2 / (4*pi^3 * R1^4 * R2^2)

# SCVC says: g1 = 2*sqrt(pi)*ell_Pl/R1 (or similar)
# They have: alpha = 4*(ell_Pl/R1)^2, g1^2 = 4*pi*alpha = 16*pi*(ell_Pl/R1)^2
# So g1 = 4*sqrt(pi)*ell_Pl/R1

# Let's see if this matches the KK formula.
# g1^2 = 16*pi*(ell_Pl/R1)^2
# 1/g1^2 = R1^2 / (16*pi*ell_Pl^2)

# From KK with Z2: 1/g^2 = 4*pi^3*R1^4*R2^2 / kappa_4^2
# Since kappa_4^2 = 8*pi*G_N = 8*pi*ell_Pl^2:
# 1/g^2 = 4*pi^3*R1^4*R2^2 / (8*pi*ell_Pl^2) = (pi^2/2) * R1^4*R2^2 / ell_Pl^2

# Comparing with SCVC: 1/g1^2 = R1^2 / (16*pi*ell_Pl^2)
# These have different R1 scaling! (R1^4 vs R1^2)

# This means SCVC is NOT using the naive KK formula. They have additional 
# assumptions about the relationship between R1, R2, and ell_Pl.

# The SCVC formula g1 = sqrt(4*pi*alpha) with alpha = 4*(ell_Pl/R1)^2
# is a specific model prediction, not a generic KK result.

# For the normalization dictionary, what matters is the ratio:
# N1 = g1(SM, M_KK) / g1(SCVC) = 0.598 / 0.303 = 1.975

# Let's check if there's a relationship involving M_KK and the compactification scales.
print()
print("The SCVC g1 = 0.303 comes from: alpha = 4*(ell_Pl/R1)^2")
print("This is a MODEL-SPECIFIC prediction, not generic KK.")
print()
print("Key question: does R1 relate to M_KK in a standard way?")
print("M_KK ~ 1/R1 typically for KK theories.")
print()
print("If M_KK = 5.2e17 GeV and 1/R1 ~ M_KK:")
print(f"  R1 ~ 1/M_KK ~ {1/5.2e17:.3e} GeV^-1")
print()

# The factor of ~2
print("="*70)
print("ORIGIN OF FACTOR 2 FOR g1")
print("="*70)
print()
print("Several geometric sources can contribute a factor of 2:")
print()
print("1. Z2 QUOTIENT on S^1:")
print("   - S^1 circumference: 2*pi*R vs S^1/Z2: pi*R")
print("   - 1/g^2 proportional to circumference")
print("   - g with Z2 / g without Z2 = sqrt(2) = 1.414")
print("   - This alone does NOT give factor 2")
print()
print("2. GUT NORMALIZATION:")
print("   - sqrt(5/3) = 1.291 reflects U(1)_Y embedding in SU(5)")
print("   - Not natural for SCVC (no SU(5) GUT)")
print()
print("3. COMBINED: Z2 x GUT:")
print("   - sqrt(2) * sqrt(5/3) = 1.414 * 1.291 = 1.826")
print("   - Factor needed: 1.975. Ratio 1.975/1.826 = 1.082 (8% off)")
print()
print("4. CANONICAL U(1) NORMALIZATION:")
print("   - SM U(1)_Y kinetic term: -1/4 B_{munu} B^{munu}")
print("   - KK U(1) kinetic term may differ by factor 2 in canonical normalization")
print("   - This would give exactly factor 2")
print()
print("5. BEST INTERPRETATION:")
print("   The factor of 2 most likely comes from the difference between")
print("   the KK geometric normalization of the U(1) gauge field and the")
print("   SM canonical normalization convention. The KK reduction naturally")
print("   gives g_KK^2 = 2*g_SM^2 (i.e., 1/g_KK^2 = 1/(2*g_SM^2)), so")
print("   g_SM = sqrt(2)*g_KK... no wait.")
print()
print("   Actually: the simplest interpretation is that the KK reduction")
print("   formula for 1/g^2 has an overall factor that differs by 4 between")
print("   the SCVC convention and the SM canonical convention:")
print("   1/g_SM^2 = (1/4) * 1/g_SCVC^2")
print("   g_SM = 2 * g_SCVC")
print()
print("   This factor 4 in 1/g^2 (factor 2 in g) is a canonical normalization")
print("   difference, analogous to how the non-abelian case gives factor 4")
print("   from the Dynkin index ratio T_adj/T_fund = 4 for SU(2).")
print()
print("   For abelian U(1), there is no Dynkin index, but the canonical")
print("   normalization of the kinetic term -1/(4g^2) F^2 has an analogous")
print("   ambiguity: is g defined so that D_mu = d_mu - i g A_mu (so the")
print("   covariant derivative has coupling g) or so that the charge-1 field")
print("   has D_mu = d_mu - i A_mu (so g=1 and the 'charge' absorbs g)?")
print()
print("   IN THE SM: D_mu = d_mu - i g' Y B_mu with Y being the hypercharge")
print("   operator. g' is the coupling constant. The KK reduction gives")
print("   D_mu = d_mu - i n A_mu where n is the KK integer charge.")
print()
print("   If the KK charge n=1 state is identified with the Y=1/2 lepton")
print("   doublet (or Y=1/6 quark), then: g' = g_KK / (2*Y_min)")
print("   For Y_min = 1/6: g' = 3*g_KK (factor 3, not 2)")
print("   For Y_min = 1/2: g' = g_KK (factor 1)")
print()
print("   This charge identification does NOT naturally give factor 2 either.")

# Bottom line
print()
print("="*70)
print("CONCLUSION ON g1 FACTOR 2")
print("="*70)
print()
print("The factor of ~2 is empirically clear (N1 = 1.975, 1.28% from 2)")
print("but the geometric derivation is LESS CLEAN than for g2's factor 1/2.")
print()
print("Plausible origin: SM canonical normalization convention for U(1)")
print("differs from KK geometric normalization by factor 2, analogous to")
print("the adjoint/fundamental distinction in non-abelian groups but for")
print("the abelian case. This is a 'convention' factor, not a derived one.")
print()
print("Confidence: 75% (empirically well-motivated, derivation incomplete)")

