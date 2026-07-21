
"""
(2*pi)????? ? ????
=============================
??DH???KK??????(2*pi)???????????
"""

import math

# ---- ???? ----
two_pi = 2 * math.pi
alpha_inv_exp = 137.035999084  # CODATA 2018

# ---- DH?? ----
dh_f1 = 4 * math.pi**3
dh_c2 = math.pi**2
dh_f3 = math.pi
dh_sum = dh_f1 + dh_c2 + dh_f3

print("=" * 60)
print("(2*pi)???? ? ??????")
print("=" * 60)

# ---- ???? ----
print(f"\nF1 = 4*pi^3 = {dh_f1:.6f}")
print(f"      = (2*pi)^3 * {dh_f1/(2*math.pi)**3:.6f}")
print(f"      = (2*pi)^3 * 1/2  (since 4*pi^3 = (2*pi)^3 * 1/2)")

print(f"\nC2 = pi^2 = {dh_c2:.6f}")
print(f"     = (2*pi)^2 * {dh_c2/(2*math.pi)**2:.6f}")
print(f"     = (2*pi)^2 * 1/4  (since pi^2 = (2*pi)^2 * 1/4)")

print(f"\nF3 = pi = {dh_f3:.6f}")
print(f"     = (2*pi) * {dh_f3/(2*math.pi):.6f}")
print(f"     = (2*pi) * 1/2  (since pi = (2*pi) * 1/2)")

# ---- C_total ?? ----
print(f"\n{'='*60}")
print(f"DH_sum = {dh_sum:.6f}")
print(f"alpha^-1 (exp) = {alpha_inv_exp:.6f}")
ratio = dh_sum / alpha_inv_exp
dev_ppm = (ratio - 1) * 1e6
print(f"ratio DH/alpha^-1 = {ratio:.10f}")
print(f"deviation = {dev_ppm:.2f} ppm")

# ---- ?????: ??k != 1 ----
print(f"\n--- ??? (2*pi) ?????? ---")
for power in [-3, -2, -1, 0, 1, 2, 3]:
    k = (2*math.pi)**power
    pred = dh_sum * k
    dev = abs(pred - alpha_inv_exp) / alpha_inv_exp
    status = "*** MATCH ***" if dev < 1e-4 else f"dev={dev:.2e}"
    print(f"  k = (2*pi)^{power:+d} = {k:.6f}, pred = {pred:.3f}, {status}")

# ---- ??(2*pi)???? ----
print(f"\n--- ????(2*pi)????? ---")

# ??dim(M)=6: BBV?? (2*pi)^{-3}
dim_M = 6
bbv_prefactor = (2*math.pi)**(-dim_M/2)

# F1: rk(N)=3, int_{S^2} -> (2*pi)^2
# ???? (????????)
f1_two_pi = bbv_prefactor * (2*math.pi)**3 * (2*math.pi)**2
f1_two_pi_power = -dim_M/2 + 3 + 2
print(f"  ?dim(M)=6: F1?(2*pi)?? = {f1_two_pi:.6f} = (2*pi)^{f1_two_pi_power}")

# C2: rk(N)=2, int_{CP^1} -> (2*pi)^2
c2_two_pi = bbv_prefactor * (2*math.pi)**2 * (2*math.pi)**2
c2_two_pi_power = -dim_M/2 + 2 + 2
print(f"  ?dim(M)=6: C2?(2*pi)?? = {c2_two_pi:.6f} = (2*pi)^{c2_two_pi_power}")

# F3: rk(N)=1, ?????????
f3_two_pi = bbv_prefactor * (2*math.pi)**1
f3_two_pi_power = -dim_M/2 + 1
print(f"  ?dim(M)=6: F3?(2*pi)?? = {f3_two_pi:.6f} = (2*pi)^{f3_two_pi_power}")

print(f"\n  -> ????(2*pi)??: {f1_two_pi_power}, {c2_two_pi_power}, {f3_two_pi_power}")
print(f"  -> ???! ????BBV??????,")
print(f"     ?????/?????????(2*pi)?")

# ??????: ?????(2*pi)???
# ? e_T ??? (2*pi) -> ?????? (2*pi)^{rk(N)} ???
print(f"\n  --- ?????? (e_T??(2*pi)) ---")
f1_two_pi_alt = bbv_prefactor * (2*math.pi)**2
print(f"  ?dim(M)=6, freq conv: F1?(2*pi) = {f1_two_pi_alt:.6f} = (2*pi)^{int(-dim_M/2+2)}")

c2_two_pi_alt = bbv_prefactor * (2*math.pi)**2
print(f"  ?dim(M)=6, freq conv: C2?(2*pi) = {c2_two_pi_alt:.6f} = (2*pi)^{int(-dim_M/2+2)}")

# ?? dim(M)=4 ? BBV???????????
f1_two_pi_dim4 = (2*math.pi)**(-2) * (2*math.pi)**2
print(f"\n  ?dim(M)=4, freq conv: F1/C2?(2*pi) = {f1_two_pi_dim4:.6f} = 1")

print(f"\n  -> ? dim_R(M)=4 ??????, F1?C2?(2*pi)???1")
print(f"  -> F3?????????????")

print(f"\n{'='*60}")
print(f"??: C_total=1 ?? dim_R(M)=4 (?6) ?")
print(f"      ?????????? (e_T??(2*pi))?")
print(f"      ????????????? + Omega-?????")
