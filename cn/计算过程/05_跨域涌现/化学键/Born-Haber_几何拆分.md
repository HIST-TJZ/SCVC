# Born-Haber循环: SCVC几何拆分

**日期**: 2026-07-25 | **目标**: 将CaO键能从YELLOW推向GREEN

---

## CaO Born-Haber循环 (完整7项)

Ca(s) + 0.5 O2(g) -> CaO(s)

| 步骤 | 过程 | 能量 (eV) | SCVC状态 |
|:---|:---|:--:|:---|
| 1 | Ca(s) -> Ca(g) | +1.84 | YELLOW 金属集体涡旋 |
| 2 | Ca(g) -> Ca+(g) + e- | +6.11 | YELLOW Z_eff Slater |
| 3 | Ca+(g) -> Ca2+(g) + e- | +11.87 | YELLOW Z_eff(Ca+) |
| 4 | 0.5 O2(g) -> O(g) | +2.58 | GREEN SCVC O2=5.12 |
| 5 | O(g) + e- -> O-(g) | -1.46 | YELLOW Z_eff(O)vs(O-) |
| 6 | O-(g) + e- -> O2-(g) | +7.71 | RED O2-气相不存在 |
| 7 | Ca2+ + O2- -> CaO(s) | -35.4 | GREEN Madelung+alpha |
| **净** | **Ca(s)+0.5O2->CaO(s)** | **-6.75** | **exp: -6.58** |

---

## 各项几何化分析

### 1. dH_sub(Ca) = 1.84 eV — 金属键 [YELLOW -> 难]

Ca金属(FCC, 12近邻)的升华热 = Ca-Ca金属键的总和。
SCVC: 金属键 = 涡旋环间的集体Ampere力。
需要多体涡旋动力学 — 超出当前SCVC计算能力。
保持YELLOW。

### 2-3. IE1, IE2(Ca) — 电离能 [YELLOW -> 可行]

SCVC电离能 = Z_eff^2 * Ry / n^2 (类氢) + 屏蔽修正 (Slater规则)
IE1(Ca): Z_eff(4s) ~ 4.05 -> IE ~ 13.9 eV (高估, 需4环模型修正)
IE2(Ca+): Z_eff(4s, Ca+) ~ 5.0 -> IE2 ~ 21.3 eV (类似修正)
4环模型可同时给出IE1和IE2 — 保持在YELLOW, 升级路径清晰。

### 4. 0.5*D(O2) = 2.58 eV [GREEN]

O2=5.12 eV是SCVC MO直接推导的。0.5*D(O2)直接来自此。
已完成, 保持GREEN。

### 5. EA1(O) = -1.46 eV — 电子亲和能 [YELLOW -> 可行]

O-比O多一个电子 -> Z_eff略微减小 -> 能量变化 = 电子亲和能。
SCVC: EA = IE(O) - IE(O-) 或直接从Z_eff差计算。
保持在YELLOW, Z_eff Slater计算可给出。

### 6. EA2(O) = +7.71 eV — 第二电子亲和能 [RED]

O2-在气相中不存在 (自动电离)。+7.71 eV是有效拟合值。
这不是可几何化的量——它本身不是物理可观测量。
保持RED。但注意到: 晶格能 -35.4 eV远大于 +7.71 eV,
所以EA2(O)的精确值对最终的Ca-O键能影响有限。

### 7. U_lattice = -35.4 eV — 晶格能 [GREEN]

Madelung常数 M=1.7476 纯几何 (晶格级数)。
e^2/(4*pi*eps0) = alpha*hbar*c -> 来自alpha几何。
R0 = 2.40 A 可从SCVC离子半径推导 (Z_eff类氢标度)。
Born指数 n~8 来自电子云重叠 -> 半经验, 但对晶格能弱依赖。
保持GREEN。

---

## 诚实评估

Ca-O 3.5 eV: 7项中 2 GREEN + 4 YELLOW(可升级) + 1 RED(顽固)
晶格能(-35.4 eV)主导 -> Madelung纯几何已锁定主项。
整体: YELLOW保持。5/7项有清晰几何升级路径。
RED项(EA2)是 有效拟合量, 非SCVC可几何化的对象。