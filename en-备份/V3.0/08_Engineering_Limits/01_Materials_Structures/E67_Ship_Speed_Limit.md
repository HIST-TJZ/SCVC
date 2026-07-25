# SCVCEngineering Limit：Ship速度 — FroudeLimit+CavitationCeiling

**基于**：`_SCVC工程常数速查表.md`（全π多项式Derivation，零自由参数）
**CalculationDate**：2026-07-23

---

## 船速的三个物理Ceiling

船舶速度受到三个独立的Physical Constraint：

| Ceiling | 物理定律 | SCVC 角色 |
|--------|---------|-----------|
| **Froude 墙**（排水船） | 表面重力波Dispersion $c = \sqrt{g\lambda/2\pi}$ | 经典流体力学，SCVC 不修正 |
| **CavitationLimit**（Propeller/水翼） | 水蒸气压 $P_\text{vap}$ ← H 键能 | **SCVC 直接设定**（$E_\text{H-bond}=0.42$ eV） |
| **能量Density**（航程） | Fuel/电池化学能 | SCVC 键能设定Upper Limit |

---

## §1. Froude Limit — 排水船的"波墙"

### 1.1 船体波速

船在航行时产生的船首波的Wavelength $\lambda$ 随船速增加而增长。当 $\lambda = L$（船长）时，船"陷在"自己制造的波谷中：

$$V_\text{hull} = \sqrt{\frac{gL}{2\pi}} \approx 1.25\sqrt{L}\ \text{m/s} \approx 2.43\sqrt{L}\ \text{knots}\ (L\ \text{in meters})$$

| 船长 (m) | 船长 (ft) | $V_\text{hull}$ (kn) | 船舶类型 |
|----------|----------|---------------------|---------|
| 10 | 33 | 7.7 | 巡航帆船 |
| 30 | 98 | 13.3 | 小型护卫舰 |
| 100 | 328 | **24.3** | 驱逐舰 |
| 200 | 656 | 34.3 | 战列舰/大型游轮 |
| 300 | 984 | **42.1** | 航母 (Nimitz级) |
| 337 | 1,106 | 44.6 | 超级油轮 (ULCC) |
| 400 | 1,312 | **48.6** | 最大船舶 (Prelude FLNG) |

### 1.2 Froude 数判据

$$\text{Fr} = \frac{V}{\sqrt{gL}}$$

| Fr | Status | 工程含义 |
|----|------|---------|
| <0.3 | 经济航速 | Power $P \propto V^3$（表皮Friction主导） |
| 0.3–0.4 | 过渡 | Wave-Making Resistance快速增长 |
| **0.40** | **Froude 墙** | 船首波+船尾波相长干涉→Drag陡增 |
| 0.40–0.50 | 越墙区 | $P \propto V^5$–$V^6$ |
| >0.50 | 几乎不可能 | Power需求指数Explosion |

### 1.3 Power尺度律：为什么不是"发动机不够大"

以 300 m 船为例：

| Fr | 速度 (kn) | 相对Power | 物理Status |
|----|----------|---------|---------|
| 0.35 | 32 | **1×** | 经济可行 |
| 0.40 | 37 | ~2× | 接近墙 |
| 0.45 | 41 | **~4–5×** | 每个节代价巨大 |
| 0.50 | 46 | ~10× | 多数发动机跟不上 |
| 0.55 | 51 | ~20× | 核动力才能尝试 |

> **航母**：Nimitz级（337 m）核动力 ~260,000 SHP → 可达 ~35 kn（Fr ≈ 0.32）——刻意保持在墙的安全侧。任何 300 m+ 船舶的实用Upper Limit都在 35–40 kn 附近。

### 1.4 "100节超级油轮"——SCVC判决

400 m 超级油轮达到 100 kn 意味着 Fr ≈ 0.82。Wave-Making Resistance ~$V^6$ 标度意味着需要 **~76 倍于 17 kn 航速的Power**。17 kn 下 100,000 HP → 100 kn 需要 ~$8\times 10^6$ HP ≈ **6 GW** ≈ 6 座大型核反应堆。

$$\boxed{\text{100 kn 超级油轮：被 Froude 波动物理绝对禁止}}$$

---

## §2. 超越 Froude 墙——三条路线

### 2.1 滑行艇：Lift取代浮力

$$L = \frac{1}{2}\rho V^2 A C_L$$

| 船长 (m) | 起滑速度 (kn) | 最大实用速度 (kn) | 限制 |
|----------|-------------|-----------------|------|
| 5（小型赛艇） | ~15 | **80–100** | Stability |
| 10 | ~19 | 60–80 | 波浪冲击 |
| 30（大型游艇） | ~34 | **50–60** | 结构载荷 |
| 50（巡逻艇） | ~44 | 45–55 | 乘员耐受 |

> 滑行艇"绕过"了 Froude 墙，但引入了新限制：**结构冲击载荷**（波浪拍击）和**乘员Acceleration耐受**。SCVC 从 E4（Structural Material）和人体生理设定了这两个限制。

### 2.2 水翼艇：船体出水

水翼将船体完全抬离水面 → Drag降至水翼 + 支柱的 ~30%。

**CavitationCeiling——SCVC直接约束**：

$$V_\text{cav} = \sqrt{\frac{2(P_\text{atm} + \rho g d - P_\text{vap})}{\rho \cdot \sigma}}$$

| 水翼深度 (m) | Cavitation速度 (kn) | 备注 |
|-------------|-------------|------|
| 0.5 | **39** | 浅潜翼，快速Cavitation |
| 1.0 | 40 | — |
| 2.0 | 42 | — |
| 3.0 | 44 | — |
| 5.0 | **47** | 深潜翼 |

$$P_\text{vap}^\text{water} \approx 0.023\ \text{bar}\ (20^\circ\text{C})$$

> **SCVC根源**：$P_\text{vap}$ 由水分子从液态逃逸所需的能量决定——即 **H键能 $E_\text{H-bond} \approx 0.42$ eV**。如果水有更强的H键 → 更低的 $P_\text{vap}$ → 更高的Cavitation速度 → 更快的水翼艇。

**超Cavitation水翼**：故意让空泡完全包覆Airfoil吸力面 → 可突破常规Cavitation限制 → **~60–80 kn**（受限于空泡Stability和Airfoil结构Strength）。

### 2.3 地效翼（WIG）：离开水面

地效飞行器本质上是一架低空飞行的Aircraft：
- 速度：**100–250 kn**（航空领域）
- Lift-to-Drag Ratio提升 ~50–100%（地面效应）
- 限制：浪高 > 飞行Height → 无法运行
- **SCVC**：不再受Hydrodynamics约束 → 进入空气动力学范畴（由 $\alpha$ 和分子间力设定）

### 2.4 Propulsion器Cavitation——Propeller的速度墙

| Propulsion器类型 | Cavitation限制 (kn) | 备注 |
|-----------|-------------|------|
| 常规Propeller | **35–45** | 叶尖低压 → 空泡 → Thrust崩溃 |
| 超CavitationPropeller | 50–70 | 故意在Cavitation区工作 |
| 喷水Propulsion | **50–80+** | 封闭叶轮 → 更高Cavitation阈值 |

> **SCVC 洞察**：Propeller的ThrustUpper Limit由水在负压下的Tensile Strength决定，后者由 H 键能约束。这是Cavitation限制的**分子根源**。

---

## §3. 工程Conclusion

### 3.1 船舶速度Ceiling汇总

```
速度 (kn)
─────────────────────────────────────────────
0    10    20    30    40    50    60    80   100   200   300
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
[ ===== 排水船 (经济航速) ==============|WALL|
  超级油轮(17)  集装箱船(25)
                    航母(35) 驱逐舰(37)
                              |===== 越墙区 =====|
                              双体渡轮(45)
                                    水翼艇(45-55)
                                    滑行艇(50-60)
                                        超Cavitation桨(60-70)
                                        喷水Propulsion(70-80)
                                              | == WIG == |
                                                 (100-250)
                                                       | 世界纪录(318)
                                                         (喷气发动机)
```

### 3.2 各类Limit速一览

| 船型 | 最大速度 | 物理Ceiling | SCVC 角色 |
|------|---------|-----------|-----------|
| 超级油轮 (400m) | **~17 kn** | 经济（非物理） | — |
| 航母 (337m) | **~35 kn** | Froude 墙附近 | — |
| 大型驱逐舰 | **~37 kn** | 在 Froude 墙上 | — |
| 水翼客船 | **~45 kn** | 水翼Cavitation | **H键 → $P_\text{vap}$** |
| 军用高速艇 | **~55 kn** | 结构+人员 | E4 Material + 生理 |
| 超Cavitation水翼 | **~70 kn** | 空泡Stability | H键 + 流体力学 |
| WIG 地效翼 | **~250 kn** | 空气动力学 | $\alpha$（电磁散射） |
| 喷气水上Aircraft | **~318 kn** (纪录) | 气动/结构 | — |

### 3.3 电动 vs 常规Propulsion

| 属性 | 柴油机 | 电动机（电池） | SCVC 比率 |
|------|--------|-------------|-----------|
| 能量Density | **~12 kWh/kg** | ~0.2–0.3 kWh/kg | 柴油 ~50× |
| 最适合 | 远洋航程 | 短途渡轮/港口拖船 | — |
| SCVC根源 | C–C 键能 3.6 eV | Li-ion 电化学 ~3 V | 化学键 vs Electrode电位 |

> **SCVC 定论**：电动船在短程（<50 nm）和低速（<20 kn）中已有竞争力。长程远洋在电池能量Density达到 ~2 kWh/kg 之前无法电动化——距 SCVC 键能Ceiling（~12 kWh/kg）差 ~6×。

### 3.4 终极答案

| 问题 | SCVC答案 |
|------|----------|
| **排水船绝对速度Upper Limit** | **~50 kn**（400m 船，Fr≈0.5，核动力） |
| **100 kn 超级油轮可能吗？** | **不可能** — 需要 6 GW（Froude 物理禁止） |
| **最快实用水面船** | **~70–80 kn**（超Cavitation水翼/喷水Propulsion） |
| **Cavitation的分子根源** | **H 键能 0.42 eV → $P_\text{vap}$** |
| **如果水有更强的 H 键？** | 更晚Cavitation → 更快的水翼艇和Propeller |
| **海面是高速的"错误介质"** | **是** — 超过 80 kn 应飞离水面（WIG/Aircraft） |
| **电动远洋货轮何时可行？** | 电池能量Density需提升 ~50×（接近 SCVC 化学键能Upper Limit） |

---

## 附录：关键公式

### A.1 船体波Dispersion关系
$$\omega^2 = gk \quad\Rightarrow\quad c = \sqrt{\frac{g}{k}} = \sqrt{\frac{g\lambda}{2\pi}}$$

### A.2 Froude 数
$$\text{Fr} = \frac{V}{\sqrt{gL}}$$

### A.3 Cavitation判据
$$\sigma = \frac{P_\infty - P_\text{vap}}{\frac{1}{2}\rho V^2}$$

Cavitation开始于 $\sigma < \sigma_\text{crit} \approx 0.3\text{–}0.5$（取决于Airfoil设计）。

### A.4 Wave-Making Resistance标度
$$R_w \propto \rho g A_\text{ship} \cdot f(\text{Fr})$$

其中 $f(\text{Fr}) \sim e^{-1/\text{Fr}^2}$ 在低 Fr，过渡到 $\sim \text{Fr}^4$ 在 Fr > 0.4。

---

*Froude Limit是经典流体力学的直接Result——不依赖 SCVC。SCVC 的贡献在CavitationCeiling：$P_\text{vap}$（由 H 键能设定）→ Propeller和水翼的绝对速度约束。*