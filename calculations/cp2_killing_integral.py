"""
CP² Killing矢量归一化积分的显式计算
=====================================
I_CP² = ∫_{CP²} √g g^{ab} K_a^i K_b^j dvol

结论: I^{ab} = (π²/8)·Tr(T^a T^b) = (π²/16)·δ^{ab}
"""
import numpy as np
from numpy import pi

np.random.seed(42)

# SU(3) Gell-Mann generators T^a = λ^a/2, Tr(T^a T^b) = δ_ab/2
def su3_generators():
    l1 = np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex) / 2
    l2 = np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex) / 2
    l3 = np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex) / 2
    l4 = np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex) / 2
    l5 = np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex) / 2
    l6 = np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex) / 2
    l7 = np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex) / 2
    l8 = np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / (2*np.sqrt(3))
    return [l1, l2, l3, l4, l5, l6, l7, l8]

Ts = su3_generators()

Vol_S5 = pi**3
Vol_CP2 = pi**2 / 2

def sample_S5(N):
    """均匀采样 S⁵ ⊂ C³ (Gaussian方法)"""
    z = np.random.randn(N, 3) + 1j * np.random.randn(N, 3)
    return z / np.sqrt(np.sum(np.abs(z)**2, axis=1, keepdims=True))

def killing_norm_sq(Z, T):
    """|K^H_T(Z)|² 在 S⁵ 上, K^H = iTZ - (Z†iTZ)Z"""
    TZ = (T @ Z[..., None])[..., 0]
    K = 1j * TZ
    Z_dot_K = np.sum(np.conj(Z) * K, axis=1)
    K_H = K - Z_dot_K[:, None] * Z
    return np.real(np.sum(np.abs(K_H)**2, axis=1))

def killing_inner(Z, Ta, Tb):
    """g(K^a, K^b) = Re((K^a_H)†·K^b_H)"""
    TaZ, TbZ = (Ta @ Z[..., None])[..., 0], (Tb @ Z[..., None])[..., 0]
    Ka, Kb = 1j * TaZ, 1j * TbZ
    Ka_H = Ka - np.sum(np.conj(Z) * Ka, axis=1)[:, None] * Z
    Kb_H = Kb - np.sum(np.conj(Z) * Kb, axis=1)[:, None] * Z
    return np.real(np.sum(np.conj(Ka_H) * Kb_H, axis=1))

N = 200000
Z = sample_S5(N)

print("=" * 60)
print("CP² Killing积分: I^{ab} = ∫⟨K^a,K^b⟩_FS dvol")
print("=" * 60)
print(f"Vol(S⁵)=π³={Vol_S5:.6f}  Vol(CP²)=π²/2={Vol_CP2:.6f}")
print(f"解析公式: I^{{ab}} = π²/8 · Tr(T^a T^b)")
print(f"对角元:   I^{{aa}} = π²/16 = {pi**2/16:.6f}")
print()

print("对角元 (MC × 解析公式):")
for a in range(8):
    I_mc = Vol_S5 * np.mean(killing_norm_sq(Z, Ts[a])) / (2*pi)
    I_an = pi**2 / 8 * np.real(np.trace(Ts[a] @ Ts[a]))
    print(f"  T{a+1}: {I_mc:.6f} / {I_an:.6f}  (ratio={I_mc/I_an:.6f})")

print("\n非对角元 (应全为0):")
for a, b in [(0,1),(0,2),(1,3),(4,5),(6,7)]:
    I_mc = Vol_S5 * np.mean(killing_inner(Z, Ts[a], Ts[b])) / (2*pi)
    I_an = pi**2 / 8 * np.real(np.trace(Ts[a] @ Ts[b]))
    print(f"  ({a+1},{b+1}): {I_mc:+.8f}  (预期 0)")

# 关键：S⁵积分的各步骤验证
print(f"\nS⁵矩公式验证:")
for a in range(3):
    val = Vol_S5 * np.mean(np.real(np.conj(Z[:, a]) * Z[:, a]))
    print(f"  ∫|Z_{a}|² dΩ = {val:.6f}  (预期 Vol/3 = {Vol_S5/3:.6f})")

print(f"\n核心公式: ∫|K^H_T|² dΩ = (π³/4)·Tr(T²)")
for a in [0, 3, 7]:
    integral = Vol_S5 * np.mean(killing_norm_sq(Z, Ts[a]))
    expected = pi**3 / 4 * np.real(np.trace(Ts[a] @ Ts[a]))
    print(f"  T{a+1}: {integral:.6f} / {expected:.6f}")

print(f"\n=== 结论 ===")
print(f"I^{{ab}} = (π²/8)·Tr(T^a T^b)  — 严格被CP² Fubini-Study度规确定")
print(f"非自由参数，是CP²=SU(3)/U(2)作为对称空间的必然结果")
