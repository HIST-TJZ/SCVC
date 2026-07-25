# V3.0 计算脚本说明

**14 个 Python 验证脚本。全部独立可运行，用于复现 SCVC 数值。**

---

## 核心验证（优先运行）

| 脚本 | 用途 | 关键输出 |
|:---|:---|:---|
| `dh_sum_verify.py` | DH 求和 → $\alpha^{-1}$ | $137.036304$ (2.22 ppm) |
| `alpha_s_3loop.py` | 3-loop RG → $\alpha_s(M_Z)$ | $0.11846$ (+0.30%) |
| `casimir_mvac.py` | Casimir 系数 + $K$ | $C_{cas}=0.24491$, $K=0.4775$ |
| `mpl_fixedpoints.py` | $M_{Pl}$ 6 不动点等变体积和 | $2.35\times 10^{18}$ ($-3.5\%$) |
| `lambda4_seesaw.py` | $\Lambda_4$ Seesaw 路径 | $2.41$ meV (+0.5%) |

## RG 跑动

| 脚本 | 用途 |
|:---|:---|
| `rg_step1.py` | 耦合常数 RG 跑动步骤 1 |
| `rg_step2.py` | 耦合常数 RG 跑动步骤 2 |
| `rg_step3.py` | 耦合常数 RG 跑动步骤 3 |
| `compute_kk.py` | KK 标度计算 |

## 辅助验证

| 脚本 | 用途 |
|:---|:---|
| `vortex_profile_cp2.py` | 涡旋 CP² 剖面 |
| `33_C_total_verification_script.py` | $C_{total}$ 三路径验证 |
| `反推ρ_s_verify.py` | $\rho_s$ 独立验证 |
| `fix_merge.py` | 辅助脚本 |
| `_compute_strengthened.py` | 辅助计算 |

---

## 重要修正

- **`mpl_fixedpoints.py`**: 确认 $\eta=609$（增强因子由 $M_{vac}$ 与 $CP^2$ 体积比确定）
- **`lambda4_seesaw.py`**: 使用 $m_\nu \approx 0.02$ eV（单中微子 seesaw 标度），非 $\Sigma m_\nu = 0.059$ eV。

---

## 运行要求

Python 3.8+，标准科学计算库（`numpy`, `scipy`）。无需 GPU。每个脚本独立，运行时间 < 1 分钟。
