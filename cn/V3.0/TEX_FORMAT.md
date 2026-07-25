# SCVC V3.0 —— TeX 数学格式规范

**适用于**: 全部 `.md` 文件。确保 MathJax/KaTeX 可正常编译。

---

## 行内公式

使用单美元符号 `$...$`：

```markdown
精细结构常数 $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi = 137.036304$
普朗克质量 $M_{Pl} = 2.35 \times 10^{18}\ \text{GeV}$
Weinberg 角 $\sin^2\theta_W(M_Z) = 0.2326$
```

---

## 独立公式

使用双美元符号 `$$...$$`：

```markdown
$$\boxed{\alpha^{-1} = 4\pi^3 + \pi^2 + \pi}$$

$$\boxed{Z_{7D} = \sum_{p \in \text{Fix}(T^4)} Z_p}$$

$$\boxed{M_{Pl} = 2.35 \times 10^{18}\ \text{GeV}\quad(\text{偏差}-3.5\%)}$$
```

---

## 上下标

| 写法 | 渲染 |
|:---|:---|
| `$M_{Pl}$` | $M_{Pl}$ |
| `$10^{18}$` | $10^{18}$ |
| `$\alpha_s^{-1}$` | $\alpha_s^{-1}$ |
| `$\alpha_s(M_Z)$` | $\alpha_s(M_Z)$ |
| `$\Lambda_4^{1/4}$` | $\Lambda_4^{1/4}$ |

---

## 希腊字母

| 写法 | 渲染 | 写法 | 渲染 |
|:---|:---|:---|:---|
| `$\alpha$` | $\alpha$ | `$\beta$` | $\beta$ |
| `$\gamma$` | $\gamma$ | `$\Gamma$` | $\Gamma$ |
| `$\delta$` | $\delta$ | `$\Delta$` | $\Delta$ |
| `$\epsilon$` | $\epsilon$ | `$\varepsilon$` | $\varepsilon$ |
| `$\theta$` | $\theta$ | `$\Theta$` | $\Theta$ |
| `$\lambda$` | $\lambda$ | `$\Lambda$` | $\Lambda$ |
| `$\mu$` | $\mu$ | `$\nu$` | $\nu$ |
| `$\pi$` | $\pi$ | `$\Pi$` | $\Pi$ |
| `$\rho$` | $\rho$ | `$\sigma$` | $\sigma$ |
| `$\Sigma$` | $\Sigma$ | `$\tau$` | $\tau$ |
| `$\phi$` | $\phi$ | `$\varphi$` | $\varphi$ |
| `$\chi$` | $\chi$ | `$\psi$` | $\psi$ |
| `$\omega$` | $\omega$ | `$\Omega$` | $\Omega$ |
| `$\eta$` | $\eta$ | `$\xi$` | $\xi$ |

---

## 运算符与符号

| 写法 | 渲染 | 说明 |
|:---|:---|:---|
| `$\times$` | $\times$ | 乘号 |
| `$\cdot$` | $\cdot$ | 点乘 |
| `$\approx$` | $\approx$ | 约等于 |
| `$\propto$` | $\propto$ | 正比于 |
| `$\sim$` | $\sim$ | 量级 |
| `$\rightarrow$` | $\rightarrow$ | 箭头 |
| `$\Rightarrow$` | $\Rightarrow$ | 蕴含 |
| `$\pm$` | $\pm$ | 正负 |
| `$\partial$` | $\partial$ | 偏导 |
| `$\int$` | $\int$ | 积分 |
| `$\sum$` | $\sum$ | 求和 |
| `$\prod$` | $\prod$ | 求积 |
| `$\infty$` | $\infty$ | 无穷 |
| `$\det$` | $\det$ | 行列式 |
| `$\dim$` | $\dim$ | 维度 |
| `$\text{Tr}$` | $\text{Tr}$ | 迹 |
| `$\otimes$` | $\otimes$ | 张量积 |
| `$\oplus$` | $\oplus$ | 直和 |

---

## 分数、根号、括号

```markdown
分数: $\frac{8\pi^2}{3}$
大分数: $$\frac{8\pi^2}{3}$$

根号: $\sqrt{|\det L_p|}$
n次根: $\Lambda_4^{1/4}$

绝对值: $|W(SU(3))|$
范数: $\|e_T\|$

括号适配: $\left(\frac{3}{2}\right)^5$
```

---

## 文本与空格

```markdown
公式中插入文本: $\text{GeV}$, $\text{Fix}(T^4)$
空格: $\quad$ (1em), $\qquad$ (2em), $\ $ (thin)
换行 (在 $$ 内): \\
```

---

## 常用符号组合

```markdown
精细结构常数:         $\alpha^{-1}$
强耦合:               $\alpha_s(M_Z)$
Weinberg 角:          $\sin^2\theta_W(M_Z)$
普朗克质量:           $M_{Pl}$
KK 标度:              $M_{KK}$
7D 普朗克质量:        $M_7$
希格斯 VEV:           $v$
希格斯质量:           $m_H$
电子质量:             $m_e$
中微子质量和:         $\Sigma m_\nu$
哈勃常数:             $H_0$
宇宙学常数:           $\Lambda_4$
Casimir 系数:         $C_{cas}$
拓扑常数:             $K$
增强因子:             $\eta$
黑洞熵:               $S$
暴涨谱指数:           $n_s$
三代数:               $N_g$
液滴模型系数:         $a_s$
涡旋核心能:           $E_{core}$
BEC 密度参数:         $\rho_s$
不动点集:             $\text{Fix}(T^4)$
Euler 示性数:         $\chi(CP^2)$
Weyl 群阶:            $|W(SU(3))|$
Fubini-Study 体积:    $\text{Vol}_4(CP^2)$
```

---

## 表格中的公式

```markdown
| 物理量 | 公式 | 数值 |
|:---|:---|:--:|
| $\alpha^{-1}$ | $4\pi^3+\pi^2+\pi$ | $137.036304$ |
| $M_{Pl}$ | $\sqrt{M_7^5\cdot V_R\cdot(1+\eta)}$ | $2.35\times 10^{18}$ |
```

---

## 矩阵

```markdown
$$\begin{pmatrix}
V_{ud} & V_{us} & V_{ub} \\
V_{cd} & V_{cs} & V_{cb} \\
V_{td} & V_{ts} & V_{tb}
\end{pmatrix}$$
```

---

## 多行公式

```markdown
$$\begin{aligned}
C_{cas} &= \left(\frac{\chi(CP^2)}{\dim_\mathbb{C}(CP^2)}\right)^{D-2} / \pi^{\dim_{int}} \\
        &= \left(\frac{3}{2}\right)^5 / \pi^3 \\
        &= 0.24491
\end{aligned}$$
```

---

## 颜色标记

```markdown
🟢 数学定理: 严格成立, 偏差 0
🟡 物理推导: 偏差 <5%
🔴 量级估计: 偏差 10-50%
🔵 可证伪预言: 待实验检验
```

---

## 禁止事项

- ❌ 不用 Unicode 上下标 (如 `¹⁸`) —— 用 `$10^{18}$`
- ❌ 不用 Unicode 希腊字母 (如 `α`) —— 用 `$\alpha$`
- ❌ 不在公式外用 `$` 包裹普通文本
- ❌ 不混用 `$` 和 `$$` 在同一段落
- ❌ 不在表格标题行使用复杂公式（会导致某些渲染器错位）
