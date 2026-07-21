# sin²θ_W 因子-2 修复：完整 7D→4D KK 约化

**计算者：Codex** | **日期：2026-07-21** | **流形：M_vac = (S²×S¹)/Z₂**

---

## 0. 前置

### 问题陈述

框架得出 sin²θ_W = 1/3 的 KK 约化中存在一个**因子-2 的不确定性**。五份外部分析指出：此因子-2 很可能来自 SU(2) 规范场的标准归一化约定 Tr(T^a T^b) = ½ δ^{ab}。

本文件完整展开 7D → 4D 的 KK 约化，每一步显式，确定该因子-2 是否闭合。

### M_vac 基本数据

```
M_vac = (S² × S¹) / Z₂
内部度规: ds²_M = R_S²² (dθ² + sin²θ dϕ²) + R_S¹² dφ²
体积: V₃ = 4π² R_S¹ R_S²²
```

### 等距群 → 规范群

| 内部空间 | 等距群 | 4D 规范群 | Killing 矢量 |
|:---|:---|:---|:---|
| S¹ | U(1) | U(1)_Y | K_Y = ∂_φ |
| S² | SO(3) ≅ SU(2)/Z₂ | SU(2)_L | K_a (a=1,2,3) |

---

## 1. 7D 作用量与度规展开

### 1.1 7D Einstein-Hilbert 作用量

\[
S_{7D} = \frac{1}{2\kappa_7^2} \int d^7x \sqrt{-g_7} \, R_7
\]

κ_7² 的量纲：[质量]⁻⁵（自然单位 ℏ=c=1）。κ_7 是 7D 引力耦合常数。

### 1.2 KK 度规拟设

4D 坐标 x^μ (μ=0,1,2,3)，内部坐标 y^m = (θ, ϕ, φ)：

\[
\boxed{ds^2 = g_{\mu\nu}(x)dx^\mu dx^\nu + \gamma_{mn}(y)\big(dy^m + A_\mu^I(x) K_I^m(y) dx^\mu\big)\big(dy^n + A_\nu^J(x) K_J^n(y) dx^\nu\big)}
\]

其中：
- γ_{mn} 是 M_vac 上的度规：diag(R_S²², R_S²² sin²θ, R_S¹²)
- K_I^m 是 Killing 矢量（I 遍历 U(1)_Y 和 SU(2)_L 的生成元）
- A_μ^I(x) 是 4D 规范场（量纲 0）

### 1.3 7D 度规的块矩阵形式

定义 ĝ_{MN} (M,N = 0,...,6)：

\[
\hat{g}_{MN} = \begin{pmatrix}
g_{\mu\nu} + \gamma_{mn} A_\mu^I A_\nu^J K_I^m K_J^n & \gamma_{mn} A_\mu^I K_I^m \\[4pt]
\gamma_{mn} A_\nu^I K_I^n & \gamma_{mn}
\end{pmatrix}
\]

### 1.4 行列式与体积元

\[
\sqrt{-\hat{g}} = \sqrt{-g_4} \cdot \sqrt{\gamma}
\]

其中 √γ = R_S²² sin θ · R_S¹。

---

## 2. Ricci 标量展开：规范动能项

### 2.1 展开到 A 的二次方

7D Ricci 标量在 A=0 附近展开。对规范动能有关的项来自 Christoffel 符号中 ∂_μ A_ν 的二次交叉项。

标准 KK 约化结果（见 Bailin & Love, Phys. Rept. 167, 1988；Overduin & Wesson, Phys. Rept. 283, 1997）：

\[
R_7 \supset -\frac{1}{4} \gamma_{mn} K_I^m K_J^n \, F_{\mu\nu}^I F^{J\,\mu\nu}
\]

其中 F_μν^I = ∂_μ A_ν^I − ∂_ν A_μ^I + f^I_{JK} A_μ^J A_ν^K（非 Abel 情况含结构常数）。

### 2.2 代入作用量

\[
S_{gauge} = \frac{1}{2\kappa_7^2} \int d^4x \sqrt{-g_4} \int_{M_{vac}} d^3y \sqrt{\gamma}
            \left(-\frac{1}{4}\right) \gamma_{mn} K_I^m K_J^n \, F_{\mu\nu}^I F^{J\,\mu\nu}
\]

\[
\boxed{S_{gauge} = -\frac{1}{8\kappa_7^2} \int d^4x \sqrt{-g_4} \; \mathcal{I}_{IJ} \; F_{\mu\nu}^I F^{J\,\mu\nu}}
\]

其中定义了**Killing 积分矩阵**：

\[
\boxed{\mathcal{I}_{IJ} \equiv \int_{M_{vac}} d^3y \sqrt{\gamma} \; \gamma_{mn} K_I^m K_J^n}
\]

---

## 3. U(1)_Y 的 Killing 积分

### 3.1 Killing 矢量

S¹ 的等距 Killing 矢量：
\[
K_Y = \partial_\varphi, \quad K_Y^m = (0, 0, 1)
\]

### 3.2 被积函数

\[
\gamma_{mn} K_Y^m K_Y^n = \gamma_{\varphi\varphi} \cdot 1 \cdot 1 = R_{S^1}^2
\]

（γ_{φφ} = R_S¹²，因为 ds²_M = ... + R_S¹² dφ²）

### 3.3 积分

\[
\mathcal{I}_{YY} = \int_{M_{vac}} d^3y \sqrt{\gamma} \; R_{S^1}^2
                = R_{S^1}^2 \cdot V_3
\]

M_vac 体积 V₃ = Vol(S²×S¹)/|Z₂| = (4πR_S²² · 2πR_S¹)/2 = 4π² R_S¹ R_S²²。

\[
\boxed{\mathcal{I}_{YY} = 4\pi^2 R_{S^1}^3 R_{S^2}^2}
\]

### 3.4 U(1)_Y 耦合常数

匹配标准 4D U(1) 动能项 L = −¼ g_Y^{−2} F_μν^Y F^{Y μν}：

\[
\frac{1}{4g_Y^2} = \frac{\mathcal{I}_{YY}}{8\kappa_7^2}
\]

\[
\boxed{\frac{1}{g_Y^2} = \frac{\mathcal{I}_{YY}}{2\kappa_7^2} = \frac{2\pi^2}{\kappa_7^2} R_{S^1}^3 R_{S^2}^2}
\]

---

## 4. SU(2)_L 的 Killing 积分

### 4.1 S² 上的 Killing 矢量

S² 的 SO(3) 等距群有三个生成元。在标准角坐标 (θ, ϕ) 下：

\[
\begin{aligned}
K_1 &= -\sin\phi \,\partial_\theta - \cot\theta \cos\phi \,\partial_\phi \\
K_2 &= \cos\phi \,\partial_\theta - \cot\theta \sin\phi \,\partial_\phi \\
K_3 &= \partial_\phi
\end{aligned}
\]

### 4.2 |K_a|² 的计算

对 K_3（最简单）：
\[
\gamma_{mn} K_3^m K_3^n = \gamma_{\phi\phi} \cdot 1 \cdot 1 = R_{S^2}^2 \sin^2\theta
\]

对 K_1：
\[
\gamma_{mn} K_1^m K_1^n = \gamma_{\theta\theta}(-\sin\phi)^2 + \gamma_{\phi\phi}(-\cot\theta\cos\phi)^2
= R_{S^2}^2 \sin^2\phi + R_{S^2}^2 \cos^2\theta \cos^2\phi
\]

对 K_2：
\[
\gamma_{mn} K_2^m K_2^n = R_{S^2}^2 \cos^2\phi + R_{S^2}^2 \cos^2\theta \sin^2\phi
\]

**关键恒等式**（三个生成元之和）：
\[
\gamma_{mn} (K_1^m K_1^n + K_2^m K_2^n + K_3^m K_3^n) = 2 R_{S^2}^2
\]

验证：
- K_1² + K_2² + K_3² = R_S²²[sin²ϕ+cos²θcos²ϕ + cos²ϕ+cos²θsin²ϕ + sin²θ]
= R_S²²[1 + cos²θ + sin²θ] = 2 R_S²² ✓

### 4.3 对 S² 积分（单个生成元，如 K_3）

\[
\int_{S^2} d\theta d\phi \, R_{S^2}^2 \sin\theta \cdot R_{S^2}^2 \sin^2\theta
= R_{S^2}^4 \int_0^\pi d\theta \int_0^{2\pi} d\phi \, \sin^3\theta
= R_{S^2}^4 \cdot 2\pi \cdot \frac{4}{3}
= \frac{8\pi}{3} R_{S^2}^4
\]

由 SO(3) 对称性，三个生成元的积分相同。

### 4.4 对 M_vac 完整积分

包含 S¹ 因子和 Z₂ 商化：

\[
\mathcal{I}_{ab}^{(SU2)} = \delta_{ab} \cdot \frac{1}{2} \int_0^{2\pi} d\varphi \, R_{S^1} \cdot \frac{8\pi}{3} R_{S^2}^4
\]

\[
= \delta_{ab} \cdot \frac{1}{2} \cdot 2\pi R_{S^1} \cdot \frac{8\pi}{3} R_{S^2}^4
\]

\[
\boxed{\mathcal{I}_{ab}^{(SU2)} = \delta_{ab} \cdot \frac{8\pi^2}{3} R_{S^1} R_{S^2}^4}
\]

其中 δ_{ab} 来自 SO(3) 对称性（不同生成元的交叉积分为零）。

### 4.5 SU(2)_L 耦合常数

对每个生成元 a，匹配标准 4D 动能项 L = −¼ g_2^{−2} F_μν^a F^{a μν}：

\[
\frac{1}{4g_2^2} = \frac{\mathcal{I}_{aa}^{(SU2)}}{8\kappa_7^2}
\]

\[
\boxed{\frac{1}{g_2^2} = \frac{\mathcal{I}_{aa}^{(SU2)}}{2\kappa_7^2} = \frac{4\pi^2}{3\kappa_7^2} R_{S^1} R_{S^2}^4}
\]

---

## 5. 耦合常数比与 sin²θ_W

### 5.1 比值

\[
\frac{g_Y^2}{g_2^2} = \frac{1/g_2^2}{1/g_Y^2}
= \frac{\frac{4\pi^2}{3\kappa_7^2} R_{S^1} R_{S^2}^4}{\frac{2\pi^2}{\kappa_7^2} R_{S^1}^3 R_{S^2}^2}
= \frac{4\pi^2}{3\kappa_7^2} \cdot \frac{\kappa_7^2}{2\pi^2} \cdot \frac{R_{S^1} R_{S^2}^4}{R_{S^1}^3 R_{S^2}^2}
\]

\[
\boxed{\frac{g_Y^2}{g_2^2} = \frac{2}{3} \cdot \frac{R_{S^2}^2}{R_{S^1}^2}}
\]

### 5.2 sin²θ_W

\[
\sin^2\theta_W^{\text{tree}} = \frac{g_Y^2}{g_Y^2 + g_2^2}
= \frac{1}{1 + g_2^2/g_Y^2}
\]

\[
\boxed{\sin^2\theta_W^{\text{tree}} = \frac{1}{1 + \frac{3}{2}\frac{R_{S^1}^2}{R_{S^2}^2}}}
\]

### 5.3 满足 sin²θ_W = 1/3 的条件

\[
\frac{1}{1 + \frac{3}{2}\frac{R_{S^1}^2}{R_{S^2}^2}} = \frac{1}{3}
\quad\Longrightarrow\quad
1 + \frac{3}{2}\frac{R_{S^1}^2}{R_{S^2}^2} = 3
\quad\Longrightarrow\quad
\frac{R_{S^1}^2}{R_{S^2}^2} = \frac{4}{3}
\]

\[
\boxed{\frac{R_{S^1}}{R_{S^2}} = \frac{2}{\sqrt{3}} \approx 1.155 \quad\text{(完整计算)}}
\]

---

## 6. 因子-2 分析：对比"朴素"计算

### 6.1 朴素计算（假设 |K_a|² = R_S²² 为常数）

如果不对 S² 上 Killing 矢量的角度依赖做精确积分，而直接取 |K_a|² ≈ R_S²²（忽略 sin²θ 等因子）：

```
朴素 I_YY = V₃ · R_S¹² = 4π² R_S¹³ R_S²²        （与精确相同 ✓——U(1) 的 K_Y 确实是常数）
朴素 I_aa = V₃ · R_S²² = 4π² R_S¹ R_S²⁴        （与精确不同 ✗——缺少 2/3 因子）
```

对比：
| 量 | 朴素计算 | 精确计算 | 比值 朴素/精确 |
|:---|:---|:---|:---:|
| I_YY | 4π² R_S¹³ R_S²² | 4π² R_S¹³ R_S²² | 1 |
| I_aa (SU2) | 4π² R_S¹ R_S²⁴ | (8π²/3) R_S¹ R_S²⁴ | **3/2** |
| g_Y²/g_2² | R_S²² / R_S¹² | (2/3) R_S²² / R_S¹² | 3/2 |
| R_S¹/R_S² (sin²θ_W=1/3) | √2 ≈ 1.414 | 2/√3 ≈ 1.155 | √(3/2) ≈ 1.225 |

### 6.2 朴素计算的 3/2 因子来自何处？

朴素计算忽略了 S² 上 Killing 矢量的**角度依赖**。具体地，|K_a|² ∝ sin²θ（对 K_3）等，而体积元 ∝ sin θ。球面上的平均：

\[
\langle |K_a|^2 \rangle_{S^2} = \frac{\int_{S^2} d\Omega \, |K_a|^2}{\int_{S^2} d\Omega}
= \frac{(8\pi/3)R_{S^2}^4}{4\pi R_{S^2}^2}
= \frac{2}{3} R_{S^2}^2
\]

所以 Killing 矢量的 S²-平均值不是 R_S²²，而是 **(2/3) R_S²²**。这解释了朴素计算与精确计算之间的 3/2 差异。

### 6.3 因子-2 是否来自 Tr(T^a T^b) = ½ δ^{ab}？

现在回答委托书的核心问题。

**委托书的假设**：SU(2) 生成元归一化 Tr(T^a T^b) = ½ δ^{ab} 在 1/g_2² 中引入一个因子 2（相对于 1/g_Y²），从而修正 sin²θ_W 的推导。

**实际检查**：

在标准约定下，SU(2) 规范动能有两种等价写法：
```
写法 A: L = −¼ g_2^{−2} F_μν^a F^{a μν}           （分量形式，3 个生成元独立求和）
写法 B: L = −½ g_2^{−2} Tr(F_μν F^{μν})           （矩阵形式，Tr 自动处理归一化）
```

因为 Tr(T^a T^b) = ½ δ^{ab}，有 Tr(F_μν F^{μν}) = ½ F_μν^a F^{a μν}，两种写法等价。

KK 约化产生的是**分量形式**（F_μν^a 来自度规的 A_μ^a K_a^m 项），匹配到写法 A。**Tr(T^a T^b) = ½ 的因子不会在匹配中额外出现**——它已经隐含在标准约定中。

### 6.4 那么，框架的"因子-2 不确定性"到底在哪里？

经过完整的显式计算，发现**框架的朴素推导中有一个 3/2 因子缺失**（不是因子-2）。

| 来源 | 因子 | 类型 |
|:---|:---:|:---|
| Killing 矢量角度平均 ⟨|K_a|²⟩ = (2/3)R_S²² | 2/3 | 几何：S² 上的非平凡积分 |
| Tr(T^a T^b) = ½ δ^{ab} | 1 | 规范约定：已隐含在标准形式中 |
| Z₂ 商化 (1/2) | 1/2 | 两者都受同样影响，在比值中抵消 |
| **净效应** | **2/3（相对朴素）** | |

### 6.5 因子-2 是否可能来自其他地方？

考虑了以下可能性：

**(a) 费米子表示的归一化**

如果框架在计算 SU(2) 耦合时使用了与 U(1) 不同的归一化约定（例如，SU(2) 双重态有两个分量，每个分量的 U(1) 荷不同），可能引入额外因子。但这是表示的动力学，不是 KK 约化的几何。

**(b) SO(3) → SU(2) 的覆盖因子**

SO(3) ≅ SU(2)/Z₂。S² 的等距群是 SO(3)，但物理规范群是 SU(2)。在将 SO(3) Killing 矢量映射到 SU(2) 生成元时，覆盖映射 π: SU(2) → SO(3) 是 2:1。如果框架的映射有歧义，可能有因子 2。但在 KK 约化中，规范变换直接来自等距，覆盖因子不影响耦合常数。

**(c) 规范动能项的约定模糊性**

如果框架在某个中间步骤使用了非标准约定（例如，用 L = −½ F² 而非 −¼ F²），会导致表面上差一个因子 2。但我们的计算全程使用标准约定 L = −¼g⁻² F²。

---

## 7. 精确数值与几何条件

### 7.1 最终结果

\[
\boxed{\sin^2\theta_W^{\text{tree}} = \frac{1}{1 + \frac{3}{2}\frac{R_{S^1}^2}{R_{S^2}^2}}}
\]

\[
\boxed{\sin^2\theta_W^{\text{tree}} = \frac{1}{3} \;\Longleftrightarrow\; \frac{R_{S^1}}{R_{S^2}} = \frac{2}{\sqrt{3}} \approx 1.155}
\]

### 7.2 KK 标度

若取 R_S¹ ≈ R_S²（数量级），则 M_KK ∼ 1/R_S¹ ∼ 1/R_S²。具体的 KK 标度取决于 R 的绝对值，而 R 的绝对值目前无法在框架中唯一确定（见 F 线分析）。

### 7.3 与朴素结果的对比

| | 朴素（|K_a|² = R_S²²） | 精确（含角度积分） |
|:---|:---:|:---:|
| g_Y²/g_2² | R_S²² / R_S¹² | (2/3) R_S²² / R_S¹² |
| R_S¹/R_S² 条件 | √2 ≈ 1.414 | 2/√3 ≈ 1.155 |
| 差异因子 | — | √(3/2) ≈ 1.225 |

朴素结果和精确结果都**可以**通过适当选择 R_S¹/R_S² 达到 sin²θ_W = 1/3。差异仅体现在所需的几何比值上。

### 7.4 sin²θ_W = 1/3 是否"自然"成立？

sin²θ_W = 1/3 成立的条件是 R_S¹/R_S² = 2/√3。这为两个半径的比值提供了一个几何约束。但是：

- **仅给出比值关系**，不给出绝对标度
- 需要验证这个比值能否与框架中其他约束（如辛面积整性、涡旋环动力学）自洽
- R_S¹ 和 R_S² 的绝对值仍需至少一个额外物理输入才能确定

---

## 8. 因子-2 问题的诚实判定

### 8.1 框架的"因子-2 不确定性"是否闭合？

| 声明 | 判定 | 说明 |
|:---|:---:|:---|
| "因子-2 来自 Tr(T^a T^b) = ½" | 🟡 部分正确 | Tr(T^a T^b) = ½ 确实在 SU(2) 规范理论中引入相对归一化，但此归一化已隐含在标准约定中；KK 约化匹配到分量形式时，它不产生**额外的**因子-2 |
| "因子-2 闭合 → sin²θ_W = 1/3 自然成立" | 🟡 方向正确但数字需修正 | 精确计算发现差异是 **3/2 因子**（来自 Killing 矢量的 S² 角度平均），而非 2。两种情况下 sin²θ_W = 1/3 都可以通过选择 R_S¹/R_S² 成立 |
| "框架 sin²θ_W 从 🟡 → 🟢" | 🟡 | 在给定 R_S¹/R_S² = 2/√3 的约束下成立，但 sin²θ_W 本身仍是一个**比值约束**，不是独立的数值预言 |

### 8.2 剩余不确定性

1. **3/2 因子需要框架的数值管线确认**：框架内部是否使用了朴素 |K_a|² = R_S²² 假定？如果是，则 R_S¹/R_S² = √2 需要修正为 2/√3。

2. **sin²θ_W = 1/3 不是独立预言**：它等价于对 R_S¹/R_S² 的一个约束。要成为预言，需要从独立的几何原理确定 R_S¹/R_S² = 2/√3，而目前该比值仅来自 sin²θ_W 的实验值（或对称性假设）。

3. **R_S¹ 和 R_S² 的绝对值仍未确定**：sin²θ_W 只固定比值。绝对标度需要额外的物理输入。

---

## 9. 结论

### 完整的 7D→4D KK 约化已显式完成

每一步都写清楚了。核心结果：

\[
\frac{1}{g_Y^2} = \frac{2\pi^2}{\kappa_7^2} R_{S^1}^3 R_{S^2}^2, \qquad
\frac{1}{g_2^2} = \frac{4\pi^2}{3\kappa_7^2} R_{S^1} R_{S^2}^4
\]

\[
\frac{g_Y^2}{g_2^2} = \frac{2}{3}\frac{R_{S^2}^2}{R_{S^1}^2}, \qquad
\sin^2\theta_W = \frac{1}{1 + \frac{3}{2}\frac{R_{S^1}^2}{R_{S^2}^2}}
\]

### 因子-2 问题

- 委托书假设的"因子-2 来自 Tr(T^a T^b) = ½"在精确计算中表现为 **3/2 因子**（来自 |K_a|² 的 S² 角度平均），而非精确的 2。
- Tr(T^a T^b) = ½ 的归一化因子在标准约定中不产生额外修正——它已经隐含在标准耦合常数定义中。
- sin²θ_W = 1/3 可以在 R_S¹/R_S² = 2/√3 ≈ 1.155 的条件下成立。这不是独立预言，而是对几何比值的一个约束。

### 状态更新

| 指标 | 之前 | 之后 |
|:---|:---:|:---:|
| sin²θ_W 因子-2 问题 | 🟡 不确定 | 🟡 精确为 3/2 因子，可闭合 |
| KK 约化显式性 | 🔴 未完成 | 🟢 每一步已显式写出 |
| sin²θ_W 作为几何预言 | 🟡 | 🟡 是比值约束，非独立预言 |
| 因子-2 = Tr(T^a T^b) 假设 | 🟡 未经检验 | 🟡 不完全匹配（差 3/2 vs 2） |

---

*Task 2 完毕。完整 KK 约化已显式完成。因子-2 假设经检验后发现实际是 3/2 因子，来自 Killing 矢量的 S² 角度平均。sin²θ_W = 1/3 在 R_S¹/R_S² = 2/√3 时成立。*
