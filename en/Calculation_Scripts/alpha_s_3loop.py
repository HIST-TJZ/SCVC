#!/usr/bin/env python3
"""脚本1：alpha_s_3loop.py — QCD耦合常数3-loop RG跑动验证

从SCVC文档读取的公式和参数：
  α_s⁻¹(M_KK) = 16π (GKM局部化, M_KK文档)
  M_KK = 1.076×10¹⁸ GeV (N9终章锁定值)
  3-loop QCD β函数 (MSbar方案)
  RK4积分，夸克阈值处连续匹配

验证：α_s(M_Z) 是否匹配 PDG 2024 值 0.1181±0.0011
"""

import math

# ============================================================
# 物理参数 (全部来自SCVC文档)
# ============================================================
M_KK = 1.076e18          # GeV, N9终章锁定值
M_Z  = 91.1876           # GeV, PDG Z玻色子质量

# 夸克质量阈值 (GeV) — SCVC文档
M_T = 173.0              # top pole mass
M_B = 4.49               # bottom (MSbar at m_b)
M_C = 1.262              # charm (MSbar at m_c)

# α_s在M_KK处的初始值 (GKM局部化: α_s⁻¹ = 16π)
alpha_s_inv_KK = 16.0 * math.pi
alpha_s_KK = 1.0 / alpha_s_inv_KK

# PDG 2024 参考值
ALPHA_S_PDG = 0.1181
ALPHA_S_PDG_ERR = 0.0011

# ============================================================
# 3-loop QCD β函数系数 (MSbar)
# ============================================================
def beta_coeffs(nf):
    """返回 (β₀, β₁, β₂) 用于 dα_s/d ln μ = -β₀α_s²/(2π) - β₁α_s³/(8π²) - β₂α_s⁴/(32π³)"""
    beta0 = 11.0 - 2.0/3.0 * nf
    beta1 = 102.0 - 38.0/3.0 * nf
    beta2 = 2857.0/2.0 - 5033.0/18.0 * nf + 325.0/54.0 * nf**2
    return beta0, beta1, beta2


def dalpha_dlnmu(alpha_s, beta_coeffs):
    """3-loop beta function: d(α_s)/d(ln μ)"""
    b0, b1, b2 = beta_coeffs
    # dα_s/d ln μ = -(β₀/(2π))α_s² - (β₁/(8π²))α_s³ - (β₂/(32π³))α_s⁴
    t2 = alpha_s**2
    t3 = alpha_s**3
    t4 = alpha_s**4
    return -(b0 * t2) / (2*math.pi) - (b1 * t3) / (8*math.pi**2) - (b2 * t4) / (32*math.pi**3)


def nf_from_mu(mu):
    """根据能标返回活跃夸克味数 (连续匹配)"""
    if mu >= M_T:
        return 6
    elif mu >= M_B:
        return 5
    elif mu >= M_C:
        return 4
    else:
        return 3


# ============================================================
# RK4 积分 (自适应步长)
# ============================================================
def rk4_step(alpha_s, lnmu, dlnmu, beta_coeffs):
    """单步RK4: 从 lnmu 积分到 lnmu + dlnmu"""
    def f(a):
        return dalpha_dlnmu(a, beta_coeffs)

    k1 = f(alpha_s)
    k2 = f(alpha_s + 0.5*dlnmu * k1)
    k3 = f(alpha_s + 0.5*dlnmu * k2)
    k4 = f(alpha_s + dlnmu * k3)

    alpha_s_new = alpha_s + (dlnmu/6.0) * (k1 + 2*k2 + 2*k3 + k4)
    return alpha_s_new


def run_rg(alpha_s_start, lnmu_start, lnmu_end, n_steps=2000):
    """从高能标向下积分到低能标，自适应步长"""
    if lnmu_start >= lnmu_end:
        return alpha_s_start # 方向错误

    alpha_s = alpha_s_start
    lnmu = lnmu_start
    total_dlnmu = lnmu_end - lnmu_start
    dlnmu = total_dlnmu / n_steps

    for i in range(n_steps):
        nf = nf_from_mu(math.exp(lnmu))
        b = beta_coeffs(nf)
        alpha_s = rk4_step(alpha_s, lnmu, dlnmu, b)
        lnmu += dlnmu

    return alpha_s


def run_rg_verbose(alpha_s_start, lnmu_start, lnmu_end, n_steps=2000):
    """带详细输出的RG跑动"""
    alpha_s = alpha_s_start
    lnmu = lnmu_start
    total_dlnmu = lnmu_end - lnmu_start
    dlnmu = total_dlnmu / n_steps

    thresholds_hit = []

    for i in range(n_steps):
        mu = math.exp(lnmu + i * dlnmu)
        nf_before = nf_from_mu(mu)
        nf_after = nf_from_mu(mu + math.exp(lnmu + i * dlnmu) * dlnmu)

        if nf_before != nf_after:
            # 记录阈值穿越
            thresh_mu = {6: M_T, 5: M_B, 4: M_C}.get(nf_before, math.exp(lnmu))
            thresholds_hit.append((thresh_mu, nf_before, nf_after, alpha_s))

        nf = nf_before
        b = beta_coeffs(nf)
        alpha_s = rk4_step(alpha_s, lnmu + i * dlnmu, dlnmu, b)

    return alpha_s, thresholds_hit


# ============================================================
# 主计算
# ============================================================
print("=" * 65)
print("脚本1: QCD耦合常数3-loop RG跑动验证")
print("=" * 65)
print(f"\n输入: α_s⁻¹(M_KK={M_KK:.4e} GeV) = 16π = {16*math.pi:.6f}")
print(f"      α_s(M_KK) = {alpha_s_KK:.10f}")
print()

# RG跑动: ln(M_KK) → ln(M_Z)
lnmu_KK = math.log(M_KK)
lnmu_Z  = math.log(M_Z)

alpha_s_MZ, thresholds = run_rg_verbose(alpha_s_KK, lnmu_KK, lnmu_Z, n_steps=5000)

print(f"输出: α_s(M_Z={M_Z} GeV) = {alpha_s_MZ:.6f}")
print()

# 阈值穿越细节
print("夸克阈值穿越:")
for thresh_mu, nf_before, nf_after, a_s in thresholds:
    print(f"  μ ≈ {thresh_mu:.2f} GeV: nf {nf_before}→{nf_after}, α_s = {a_s:.6f}")
print()

# 对比
deviation = (alpha_s_MZ - ALPHA_S_PDG) / ALPHA_S_PDG * 100
sigma   = abs(alpha_s_MZ - ALPHA_S_PDG) / ALPHA_S_PDG_ERR
print(f"PDG 2024: α_s(M_Z) = {ALPHA_S_PDG} ± {ALPHA_S_PDG_ERR}")
print(f"SCVC预言: α_s(M_Z) = {alpha_s_MZ:.5f}")
print(f"偏差: {deviation:+.2f}% ({sigma:.2f}σ)")
print()

# 也输出备用匹配方案 (O(α_s²)阈值修正)
# 在MSbar中，非零nf扇区的decoupling修正从α_s²阶开始：
# α_s^(nf-1)(m_q) = α_s^(nf)(m_q) * [1 + c2*(α_s^(nf)/π)² + ...]
# c2 = -7*C_A*T_F/72 = -7*3*0.5/72 ≈ -0.1458

def run_with_oas2_matching(alpha_s_start, lnmu_start, lnmu_end, n_steps=5000):
    """带O(α_s²)阈值匹配的RG跑动"""
    alpha_s = alpha_s_start
    lnmu = lnmu_start
    total_dlnmu = lnmu_end - lnmu_start
    dlnmu = total_dlnmu / n_steps

    # O(α_s²) matching corrections at thresholds
    c2 = -7.0 * 3.0 * 0.5 / 72.0  # = -7*C_A*T_F/72

    for i in range(n_steps):
        lnmu_i = lnmu_start + i * dlnmu
        mu = math.exp(lnmu_i)
        nf = nf_from_mu(mu)
        mu_next = math.exp(lnmu_i + dlnmu)
        nf_next = nf_from_mu(mu_next)

        b = beta_coeffs(nf)
        alpha_s = rk4_step(alpha_s, lnmu_i, dlnmu, b)

        # 如果跨过阈值，应用O(α_s²)匹配
        if nf != nf_next and nf > nf_next:
            # 重夸克decoupling: α_s^(nf-1) = α_s^(nf) * [1 + c2*(α_s^(nf)/π)²]
            correction = 1.0 + c2 * (alpha_s / math.pi)**2
            alpha_s = alpha_s * correction

    return alpha_s


alpha_s_MZ_oas2 = run_with_oas2_matching(alpha_s_KK, lnmu_KK, lnmu_Z, n_steps=5000)
print(f"O(α_s²)匹配: α_s(M_Z) = {alpha_s_MZ_oas2:.5f}")
dev2 = (alpha_s_MZ_oas2 - ALPHA_S_PDG) / ALPHA_S_PDG * 100
sigma2 = abs(alpha_s_MZ_oas2 - ALPHA_S_PDG) / ALPHA_S_PDG_ERR
print(f"偏差: {dev2:+.2f}% ({sigma2:.2f}σ)")
print()

# 也测试SCVC文档中提到的0.11846对应M_KK (文档中M_KK取1.08e18时结果)
print("--- 敏感性测试 ---")
for test_M_KK in [0.83e18, 1.08e18, 1.45e18]:
    a_s_test = 1.0/(16*math.pi)
    a_s_res, _ = run_rg_verbose(a_s_test, math.log(test_M_KK), lnmu_Z, n_steps=5000)
    print(f"  M_KK={test_M_KK:.2e}: α_s(M_Z)={a_s_res:.5f}")
print()

print("=== 审计结论 ===")
print(f"3-loop RG + 连续匹配: α_s(M_Z) = {alpha_s_MZ:.5f} ({deviation:+.2f}%)")
print(f"3-loop RG + O(α_s²)匹配: α_s(M_Z) = {alpha_s_MZ_oas2:.5f} ({dev2:+.2f}%)")
