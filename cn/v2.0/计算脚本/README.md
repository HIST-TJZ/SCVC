# SCVC v2.0 计算脚本

本目录包含用于验证SCVC理论关键数值的Python脚本。

## 独立验证脚本 (v5审计, 2026-07-23)

由独立AI从零编写，不引用任何已有代码，仅读SCVC文档公式。

| 脚本 | 验证项 | 结果 | 偏差 |
|:---|:---|:--:|:--:|
| `alpha_s_3loop.py` | α_s(M_Z) 3-loop RG | 0.11845 | +0.30% |
| `dh_sum_verify.py` | α⁻¹ DH求和 | 137.036304 | 2.22 ppm |
| `casimir_mvac.py` | C_cas + K | 0.2449 / 0.4775 | 代数精确 |
| `mpl_fixedpoints.py` | M_Pl 6不动点 | 2.433×10¹⁸ GeV | −0.10% |
| `lambda4_seesaw.py` | Λ₄ 双路径 | 2.41/2.24×10⁻³ eV | +0.43%/−6.5% |

审计报告: `../10_审计与验证/独立验证报告_5脚本.md`

## 早期计算脚本

| 脚本 | 功能 | 对应文档 |
|:---|:---|:---|
| `compute_kk.py` | 四耦合RG跑动 → M_KK锁定 | `02_几何推导链/M_KK_精确锁定.md` |
| `rg_step1/2/3.py` | RG跑动分步实现 | 同上 |
| `33_C_total_verification_script.py` | C_total=1验证 | `01_公设与基础/C_total_三路径闭合.md` |
| `_compute_strengthened.py` | 核物理计算 | `07_核物理/液滴模型_五系数.md` |
| `vortex_profile_cp2.py` | 涡旋CP²剖面 | `02_几何推导链/K1_KK约化_三重闭合.md` |
| `反推ρ_s_verify.py` | BEC密度验证 | `01_公设与基础/P8_希格斯_涡旋库珀对.md` |
| `fix_merge.py` | 数据合并修复 | — |

## 运行说明

所有脚本为Python 3，依赖仅需numpy/scipy。
在普通笔记本上运行，总耗时<5分钟。
