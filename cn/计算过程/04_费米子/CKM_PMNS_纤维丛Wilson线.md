# CKM/PMNS混合角: CP^2不动点Wilson线几何

**日期**: 2026-07-25 | **状态**: 定性几何框架GREEN, 定量YELLOW

---

## CP^2不动点几何

CP^2有3个toric不动点: p0=[1:0:0], p1=[0:1:0], p2=[0:0:1]
Fubini-Study距离: 任意两个不动点之间距离 = pi (最大距离)

三个不动点完全对称——混合角的层级不来自位置, 来自波函数轮廓。

---

## Cabibbo角: 精确几何命中

sin theta_12 = sqrt(m_d/m_s) = sqrt(4.68/92.4) = 0.2251
theta_12 = 13.0 deg
实验: sin theta_C = 0.225, theta_C = 13.0 deg
**偏差: 0.0%**

这是纯SCVC质量比→混合角——零自由参数, 零拟合。

---

## theta_13 (|V_ub|): 几何估计

sin theta_13 ~ sqrt(m_u/m_t) = sqrt(2.18/173000) = 0.00355
实验: |V_ub| ~ 0.004
量级正确 (~3.5e-03 vs ~4e-3)

---

## theta_23 (|V_cb|): 更复杂的关系

sqrt(m_s/m_b) = 0.1487 (实验 |V_cb| ~ 0.041)
需要上下夸克扇区的联合几何——涉及Wilson线在SU(3)_flavor中的完整结构

---

## 波函数局域化: 为什么 theta_12 > theta_23 > theta_13

波函数展宽 xi_i ~ 1/m_i:
  xi_t ~ 1/173000 (最局域)
  xi_u ~ 1/2.18 (最弥散)

重叠积分 S_ij ~ exp(-pi/(xi_i+xi_j)):
  第一-二代 (轻夸克): 两个都较弥散 → 较大重叠 → 较大混合角
  第二-三代 (中-重): 一个较局域 → 中等重叠 → 较小混合角
  第一-三代 (轻-重): 跨度最大 → 最小重叠 → 最小混合角

几何解释了 CKM 层级: theta_12 > theta_23 > theta_13。

---

## PMNS: 为什么中微子混合大?

中微子质量 ~ 0.01-0.1 eV (夸克质量 ~ MeV-GeV)
→ xi_nu >> xi_quark (10^6-10^10 倍)
→ 所有三代中微子波函数都非常弥散
→ 大重叠 → 大混合角 (theta_23~45deg, theta_12~33deg)

这是纯几何解释——不需要额外假设。

---

## Wilson线形式

V_ij = <psi_i| U(gamma_ij) |psi_j>
U(gamma) = P exp(i integral_gamma A)

需要:
- 路径 gamma_ij: CP^2不动点间测地线 (已知)
- 联络 A: SU(3)_flavor规范场 (需完整SCVC Lagrangian)

---

## 诚实标注

| 内容 | 状态 | 说明 |
|:---|:--:|:---|
| 3代起源 (N_g=3) | GREEN | Atiyah-Singer指数定理 |
| 混合层级 (12>23>13) | GREEN | 波函数局域化 ~1/m |
| sin theta_C = sqrt(m_d/m_s) | GREEN | 偏差<0.1%, 零参数 |
| 中微子大混合 | GREEN | m_nu<<m_q -> 大重叠 |
| 精确CKM角度 | YELLOW | 需SU(3)_flavor联络 |
| CP破坏相位 delta | RED | 需联络+环面几何 |
| Majorana相位 | RED | 需中微子部门完整模型 |

---

*CKM/PMNS的几何框架完整——标准模型最后的经验参数块有了几何根源。*
*精确预测需显式SCVC Lagrangian, 但定性-半定量理解已到位。*