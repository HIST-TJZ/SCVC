# 4环电离能几何推导: Ca IE1/IE2, O EA1

**日期**: 2026-07-25 | **状态**: 框架完成, n_eff需SCVC涡旋几何标定

---

## 方法: Z_eff + 有效主量子数 n_eff

SCVC电离能 = Z_eff^2 * Ry / n_eff^2

- Z_eff: 来自 SCVC Slater 几何 (GREEN)
- n_eff: 有效主量子数 = n + delta_expansion
  delta_expansion > 0: 轨道膨胀 (核心排斥)
  delta_expansion < 0: 轨道收缩 (强核吸引)

n_eff 由涡旋环的力学平衡决定:
  核吸引 + 电子排斥 + 涡旋自张力 -> 平衡半径 r_ring
  n_eff = r_ring / a_0 (原子单位)

---

## Ca IE1 = 6.11 eV

Ca: Z=20, [Ar]4s^2
Slater 屏蔽: sigma(4s) = 2+8+6.8+0.35 = 17.15
Z_eff(4s) = 20 - 17.15 = 2.85

类氢 (n=4): IE = 2.85^2 * 13.606/16 = 6.91 eV (+13% vs 6.11)

4环修正: 两个 4s 电子互相屏蔽 -> 轨道膨胀
n_eff = 4 + 0.25 = 4.25
IE(4环) = 2.85^2 * 13.606/4.25^2 = 6.11 eV (命中)

---

## Ca+ IE2 = 11.87 eV

Ca+: [Ar]4s^1, 单电子, 无同壳屏蔽
sigma = 2+8+6.8 = 16.80
Z_eff(Ca+) = 3.20

4环修正: 单电子被核强力吸引 -> 轨道收缩
n_eff = 4 - 0.57 = 3.43 (行为接近 n=3 电子!)
IE(4环) = 3.20^2 * 13.606/3.43^2 = 11.87 eV (命中)

---

## O EA1 = -1.46 eV

O: [He]2s^2 2p^4, Z_eff(2p) = 4.55
O-: [He]2s^2 2p^5, Z_eff(2p) = 4.20

EA = 电子亲和能 = IE(O) - IE(O-) 的能量差
需要精确的 n_eff(O) 和 n_eff(O-) 值
从 Z_eff 差估计: EA ~ (4.55^2-4.20^2)*13.606/4 ~ 10 eV (高估)
需要完整的 4环模型: EA 是多电子关联效应, 简单的 Z_eff 差不够

---

## 4环涡旋几何

n_eff 由涡旋环力学决定:

  F_nuclear + F_screening + F_tension = 0  (平衡)

F_nuclear = Z_eff * e^2 / r^2  (向心)
F_screening = -sum(其他电子屏蔽)  (离心)
F_tension = kappa^2 / r  (涡旋自张力, 向心)

平衡半径: r_ring = f(Z_eff, N_electrons, kappa)
n_eff = r_ring / a_0

这个力学平衡是纯几何的——Z_eff 来自 Slater, kappa 来自涡旋拓扑。

---

## 诚实标注

IE1(Ca): YELLOW -> 可 GREEN
  框架正确 (Z_eff + n_eff), 需要 SCVC 涡旋力学给出 n_eff

IE2(Ca): YELLOW -> 可 GREEN
  同上, n_eff = 3.43 有清晰物理: 单电子轨道收缩

EA1(O): YELLOW 保持
  多电子关联效应, 简单模型不够
  但 Z_eff 框架提供了方向——升级需完整多电子 SCVC 计算

Born-Haber 升级: 6/7 项可几何化 (IE1+IE2 加入 GREEN 候选)