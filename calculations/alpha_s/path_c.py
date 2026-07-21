import numpy as np

# ============================================================
# PATH C: CP2 Volume Modulus Stabilization Scale
# ============================================================

print("="*70)
print("PATH C: CP2 Volume Modulus Stabilization Scale")
print("="*70)

print("""
Question: Is the CP2 volume modulus stabilized at M_KK or at a LOWER scale?

If CP2 volume modulus is stabilized at the electroweak scale (~TeV) 
rather than the KK scale (~10^16 GeV), then the geometric prediction 
for alpha_s would be at M_Z, not M_KK. This fundamentally changes 
the numerical comparison.

Let me analyze this step by step.
""")

# ============================================================
# Part 1: What determines the CP2 volume?
# ============================================================
print("-"*50)
print("Part 1: CP2 Volume in SCVC Framework")
print("-"*50)

print("""
In the SCVC framework, the internal space is (at least) CP2 x S2.
The CP2 factor has isometry SU(3), giving the QCD gauge group.
The S2 factor has isometry SO(3) ~ SU(2), giving the weak gauge group.

The volume moduli are 4D scalar fields:
- Vol(CP2) ~ phi_CP2 (determines 1/g^2_3 ~ I_CP2/kappa^2_4)
- Vol(S2) ~ phi_S2   (determines 1/g^2_2 ~ I_S2/kappa^2_4)

If the moduli are NOT stabilized at the same scale, the gauge 
couplings would be evaluated at DIFFERENT renormalization scales:
- g3 at mu = 1/R_CP2 (inverse CP2 size)
- g2 at mu = 1/R_S2  (inverse S2 size)

If R_CP2 >> R_S2 (CP2 much larger than S2, stabilized at lower energy):
- g3 is evaluated at a LOWER scale
- alpha_s would be LARGER at that scale
- This could explain the discrepancy!

Conversely, if R_CP2 << R_S2:
- alpha_s would be evaluated at higher scale, making it SMALLER
- This goes in the right direction!
""")

# ============================================================
# Part 2: Quantitative analysis
# ============================================================
print("-"*50)
print("Part 2: Quantitative Analysis")
print("-"*50)

# The SCVC prediction gives alpha_s at the compactification scale.
# If CP2 is stabilized at a different scale mu_CP2:
# alpha_s(mu_CP2) = 1/30 (geometric prediction)
# We need to run this to M_Z to compare with experiment.
# 
# Running: 1/alpha_s(M_Z) = 1/alpha_s(mu_CP2) + b0/(2*pi)*ln(M_Z/mu_CP2)
#
# We know alpha_s(M_Z) = 0.1181, so 1/alpha_s(M_Z) = 8.47
# 
# If alpha_s(mu_CP2) = 1/30 = 0.0333, 1/alpha_s(mu_CP2) = 30
# Then: 8.47 = 30 + b0/(2*pi)*ln(M_Z/mu_CP2)
# ln(M_Z/mu_CP2) = (8.47 - 30) * 2*pi / b0
#                = -21.53 * 2*pi / 7
#                = -19.3
# mu_CP2 = M_Z * exp(19.3) = 91 * 2.4e8 = 2.2e10 GeV
#
# So the CP2 scale would need to be ~2e10 GeV to match alpha_s(M_Z)!
# That's intermediate between EW and GUT scales.

b0 = 7.0
M_Z = 91.0
inv_alpha_MZ = 1/0.1181
inv_alpha_geom = 30.0  # from SCVC: alpha_s = 1/30

ln_ratio = (inv_alpha_MZ - inv_alpha_geom) * 2*np.pi / b0
mu_CP2 = M_Z * np.exp(-ln_ratio)  # M_Z/mu_CP2 = exp(ln_ratio), so mu_CP2 = M_Z/exp(ln_ratio)
print(f"\nIf alpha_s(mu_CP2) = 1/30 and alpha_s(M_Z) = 0.1181:")
print(f"  ln(M_Z/mu_CP2) = {ln_ratio:.2f}")
print(f"  mu_CP2 = {mu_CP2:.2e} GeV")

# But wait, that gives mu_CP2 ~ 2e10 GeV, which means alpha_s is 
# evaluated at a HIGHER scale than M_Z, making it SMALLER:
# alpha_s(2e10) < alpha_s(M_Z)
# But 1/30 = 0.033 << 0.118, so this means alpha_s at the high scale 
# is MUCH weaker than at M_Z, which is the WRONG direction (QCD is 
# asymptotically free, so alpha_s DECREASES with energy).

# Let me check: with b0=7, alpha_s DECREASES as mu INCREASES.
# alpha_s(high) < alpha_s(low)
# 1/30 = 0.033 at mu_CP2=2e10, and alpha_s(M_Z) = 0.118
# This is consistent with QCD running! alpha_s is smaller at higher energy.

# But the problem is: the geometric prediction alpha_s = 1/30 is 
# TOO SMALL compared to what SM running would give at M_KK ~ 10^16.

# Let me check: SM running from M_Z to M_KK:
# 1/alpha_s(M_KK) = 1/alpha_s(M_Z) + b0/(2*pi)*ln(M_KK/M_Z)
M_KK = 1e16
inv_at_KK_SM = inv_alpha_MZ + b0/(2*np.pi) * np.log(M_KK/M_Z)
print(f"\nSM running from M_Z to M_KK={M_KK:.0e} GeV:")
print(f"  1/alpha_s(M_KK) = {inv_at_KK_SM:.2f}")
print(f"  alpha_s(M_KK)   = {1/inv_at_KK_SM:.4f}")

# The SCVC predicts alpha_s(M_KK) = 1/30 = 0.0333
# SM extrapolation gives alpha_s(M_KK) = 1/49 = 0.0204
# So SCVC predicts alpha_s(M_KK) is LARGER than SM extrapolation.
# 
# Alternative interpretation: what if the geometric prediction 
# gives alpha_s at the scale mu_CP2, and mu_CP2 != M_KK?

# If mu_CP2 < M_KK (CP2 stabilized lower):
# alpha_s(mu_CP2) = 1/30 (geometric)
# Run DOWN to M_Z: alpha_s gets LARGER (wrong, we need it to match 0.118)
# 
# If mu_CP2 > M_KK (CP2 stabilized higher):
# alpha_s(mu_CP2) = 1/30 (geometric)
# Run DOWN to M_Z: alpha_s gets larger still
#
# Actually wait. The geometric prediction gives alpha_s at whatever 
# scale the CP2 modulus is stabilized. If that scale is NOT M_KK but 
# some other scale, we need to run from THAT scale to M_Z.
#
# Let me think about this differently. The SCVC prediction is:
# alpha_s = (some geometric quantity involving CP2)
# This is the VALUE of alpha_s at the compactification scale.
# 
# If the compactification scale for CP2 is mu_s, then:
# alpha_s(mu_s) = 1/30 (SCVC prediction)
# 
# We measure alpha_s(M_Z) = 0.118. The SM running gives:
# 1/alpha_s(M_Z) = 1/alpha_s(mu_s) + b0/(2*pi)*ln(mu_s/M_Z)
# (running from mu_s down to M_Z, alpha_s increases)
# 8.47 = 30 + 7/(2*pi)*ln(mu_s/91)
# ln(mu_s/91) = (8.47-30)*2*pi/7 = -19.3
# mu_s = 91*exp(-19.3) = 3.7e-7 GeV
# That 's a ridiculously low scale, below the QCD scale!

# This means alpha_s = 1/30 CANNOT be at any scale above M_Z and 
# still match alpha_s(M_Z) via SM running. alpha_s = 1/30 means 
# the coupling is WEAKER than at M_Z (1/30 < 1/8.47), so it must 
# be at a HIGHER scale. But we showed above that mu_CP2 ~ 2e10 GeV 
# gives the right running. Let me recalculate.

print("\n--- Recalculation ---")
# 1/alpha_s(mu) = 1/alpha_s(M_Z) - b0/(2*pi)*ln(mu/M_Z)  (running UP)
# At mu = mu_CP2: 1/alpha_s = 30
# 30 = 8.47 - 7/(2*pi)*ln(mu_CP2/91)
# ln(mu_CP2/91) = (8.47-30)*2*pi/7 = -19.3
# mu_CP2 = 91*exp(-19.3) = 3.7e-7 GeV = 3.7e-16 GeV? That can't be right.
# 
# Let me be very careful with signs.
# 
# QCD: alpha_s DECREASES as energy INCREASES (asymptotic freedom)
# So alpha_s(high energy) < alpha_s(low energy)
# 1/alpha_s(high energy) > 1/alpha_s(low energy)
# 
# At M_Z = 91 GeV: alpha_s = 0.118, 1/alpha_s = 8.47
# At higher energy: alpha_s < 0.118, 1/alpha_s > 8.47
# 
# SCVC prediction: alpha_s = 1/30 = 0.033, 1/alpha_s = 30
# Since 30 > 8.47, this must be at a HIGHER energy than M_Z.
# 
# The running from mu_0 to mu (mu > mu_0):
# 1/alpha_s(mu) = 1/alpha_s(mu_0) + b0/(2*pi)*ln(mu/mu_0)
# 
# If mu_0 = M_Z: 1/alpha_s(mu) = 8.47 + 7/(2*pi)*ln(mu/91)
# Set 1/alpha_s(mu) = 30:
# ln(mu/91) = (30-8.47)*2*pi/7 = 21.53*6.283/7 = 19.3
# mu = 91*exp(19.3) = 91*2.4e8 = 2.2e10 GeV
# 
# So at mu = 2.2e10 GeV, SM running gives alpha_s = 1/30.
# This matches the SCVC prediction exactly at this scale!
# But M_KK is typically 10^16 GeV >> 2e10 GeV.
# 
# So if the SCVC prediction is for mu = 2e10 GeV (not M_KK),
# then alpha_s(M_Z) would match SM + running!
# 
# The question becomes: can CP2 be stabilized at 2e10 GeV 
# while the overall KK scale is 10^16 GeV?

mu_match = M_Z * np.exp((30 - inv_alpha_MZ) * 2 * np.pi / b0)
print(f"  Scale where SM running gives alpha_s = 1/30: {mu_match:.2e} GeV")
print(f"  This is where SCVC prediction would match SM running PERFECTLY.")
print(f"  But M_KK ~ 10^16 GeV, which is 5e5 times larger.")
print(f"  At M_KK, SM gives alpha_s = {1/(inv_alpha_MZ + b0/(2*np.pi)*np.log(M_KK/M_Z)):.4f}")

# ============================================================
# Part 3: Can the modulus be stabilized at a lower scale?
# ============================================================
print("\n" + "-"*50)
print("Part 3: Modulus Stabilization Mechanism")
print("-"*50)

print("""
In KK compactifications, modulus stabilization requires:
1. A potential for the modulus (from fluxes, Casimir energy, etc.)
2. The minimum of this potential determines the stabilized value

The CP2 volume modulus corresponds to the overall scale of CP2.
In the SCVC framework with CP2 x S2 internal space:
- The total internal volume sets M_Pl via M_Pl^2 = Vol(K) * M_D^{D-2}
- Individual moduli set the gauge couplings

If the CP2 modulus is stabilized by different physics than the 
overall volume modulus, they can have different stabilization scales.

For example:
- Overall volume: stabilized by fluxes/Casimir at M_KK ~ 10^16 GeV
- CP2 shape modulus: stabilized by gauge instantons at a lower scale

The CP2 sigma model has instantons (since pi_4(CP2) = Z).
These generate a potential for the CP2 modulus:
  V(phi) ~ Lambda^4 * exp(-S_inst)
  
The instanton action depends on the CP2 volume:
  S_inst ~ 8*pi^2/g^2_4d ~ 2*pi/alpha_s
  
If the instantons are QCD instantons, Lambda ~ Lambda_QCD ~ 200 MeV.
This gives stabilization near the QCD scale, not at M_KK!

But more likely, the relevant instantons are from the higher-dimensional 
theory, with action:
  S_inst ~ Vol(CP2) * (something)
  
If set by the UV completion, Lambda ~ M_KK, and the modulus is 
stabilized at M_KK.

Key question: what is the origin of the potential that stabilizes 
the CP2 modulus separately from the overall volume?
""")

# ============================================================
# Part 4: Alternative - CP2 = internal space at EW scale
# ============================================================
print("-"*50)
print("Part 4: Alternative Scenario")
print("-"*50)

print("""
Scenario: CP2 is NOT part of the small compact dimensions.
Instead, CP2 might be a "large" extra dimension stabilized at 
a lower scale, or even related to the electroweak scale.

If the CP2 radius R_CP2 ~ 1/TeV (large extra dimensions scenario):
- M_KK_CP2 ~ TeV
- alpha_s is evaluated at TeV scale
- Running from TeV to M_Z is a small effect
- alpha_s(TeV) ≈ alpha_s(M_Z) ≈ 0.118
- But SCVC predicts alpha_s = 1/30 = 0.033 at the CP2 scale
- 0.033 vs 0.118 is off by factor 3.6

So even if CP2 is at TeV, the prediction is wrong by factor ~3.6.

What if CP2 is at 2e10 GeV as computed above?
- alpha_s(2e10) = 1/30 from SCVC matches SM running
- But WHY would CP2 be stabilized at exactly this scale?
- The scale 2e10 GeV has no obvious physical significance.

Unless the stabilization mechanism naturally gives this scale:
  mu_stab ~ M_Pl * exp(-c/alpha_GUT)
  = 10^18 * exp(-c/alpha)
  
With c ~ 4*pi (instanton action):
  mu ~ 10^18 * exp(-4*pi/0.04) ~ 10^18 * exp(-314) ~ 0 (too small)
  
With c ~ 1:
  mu ~ 10^18 * exp(-1/0.04) ~ 10^18 * 1.4e-11 ~ 1.4e7 GeV (too low)
  
With c ~ 0.5:
  mu ~ 10^18 * exp(-12.5) ~ 3.7e12 GeV (too high)
  
So 2e10 GeV could in principle come from a non-perturbative effect 
with the right coefficient. But this is speculative at best.
""")

# ============================================================
# Part 5: Combined analysis
# ============================================================
print("\n" + "="*70)
print("PATH C: CONCLUSIONS")
print("="*70)

print(f"""
If alpha_s(geometric) = 1/30 is evaluated at scale mu_s:
- For mu_s = M_KK ~ 10^16: alpha_s(M_Z) blows up (Landau pole at ~10^5)
- For mu_s = {mu_match:.2e} GeV: alpha_s(M_Z) = 0.118 PERFECTLY
- For mu_s = M_Z: alpha_s(M_Z) = 1/30 = 0.033, WRONG by factor 3.6

The "sweet spot" scale {mu_match:.2e} GeV is:
- 5e5 times smaller than typical GUT-scale M_KK
- Much larger than EW scale
- Has no obvious physical motivation
- Unless there is a separate stabilization mechanism for CP2

Path C assessment: The CP2 volume modulus would need to be stabilized 
at ~2e10 GeV for the geometric alpha_s prediction (1/30) to match SM 
running to M_Z. This scale has no natural explanation in the standard 
KK framework, making this path UNLIKELY without additional physics.

However, if there IS a mechanism that stabilizes CP2 at this specific 
scale (e.g., from gaugino condensation or instanton effects), the 
alpha_s problem would be completely resolved without any geometric 
correction factor.
""")

# Check: what if Path A correction factor (0.617) is applied to 
# alpha_s(M_KK), AND CP2 is stabilized at M_KK?
print("-"*50)
print("Combined Path A + Standard M_KK:")
print("-"*50)

alpha_KK_corrected = (1/30) * (np.pi**2 / 16)
inv_alpha_KK_corrected = 1/alpha_KK_corrected
inv_alpha_Z_from_corrected = inv_alpha_KK_corrected + b0/(2*np.pi) * np.log(M_Z/M_KK)
print(f"  alpha_s(M_KK) corrected = {alpha_KK_corrected:.6f}")
print(f"  1/alpha_s(M_KK) = {inv_alpha_KK_corrected:.2f}")
if inv_alpha_Z_from_corrected > 0:
    print(f"  1/alpha_s(M_Z) = {inv_alpha_Z_from_corrected:.2f}")
    print(f"  alpha_s(M_Z) = {1/inv_alpha_Z_from_corrected:.4f}")
    print(f"  Observed = 0.1181, Diff = {abs(1/inv_alpha_Z_from_corrected-0.1181)/0.1181*100:.1f}%")
else:
    print(f"  STILL Landau pole before M_Z!")

# What about Path A correction AND Path C scale?
print("\nCombined Path A + Path C (mu_CP2 = 2e10):")
alpha_s_at_mu = (1/30) * (np.pi**2 / 16)
inv_alpha_at_mu = 1/alpha_s_at_mu
inv_alpha_Z_combined = inv_alpha_at_mu + b0/(2*np.pi) * np.log(M_Z/mu_match)
print(f"  alpha_s({mu_match:.2e}) = {alpha_s_at_mu:.6f}")
print(f"  1/alpha_s(M_Z) = {inv_alpha_Z_combined:.2f}")
print(f"  alpha_s(M_Z) = {1/inv_alpha_Z_combined:.4f}")

print("\nDone.")
