# SCVC V3.0 — TeX Mathematical Formatting Specification

**Applies to**: All `.md` files. Ensures proper compilation under MathJax/KaTeX.

---

## Inline formulas

Use single dollar sign `$...$`:

```markdown
The fine-structure constant $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi = 137.036304$
The Planck mass $M_{Pl} = 2.35 \times 10^{18}\ \text{GeV}$
The Weinberg angle $\sin^2\theta_W(M_Z) = 0.2326$
```

---

## Display formulas

Use double dollar signs `$$...$$`:

```markdown
$$\boxed{\alpha^{-1} = 4\pi^3 + \pi^2 + \pi}$$

$$\boxed{Z_{7D} = \sum_{p \in \text{Fix}(T^4)} Z_p}$$

$$\boxed{M_{Pl} = 2.35 \times 10^{18}\ \text{GeV}\quad(\text{deviation }-3.5\%)}$$
```

---

## Superscripts and subscripts

| Syntax | Renders as |
|:---|:---|
| `$M_{Pl}$` | $M_{Pl}$ |
| `$10^{18}$` | $10^{18}$ |
| `$\alpha_s^{-1}$` | $\alpha_s^{-1}$ |
| `$\alpha_s(M_Z)$` | $\alpha_s(M_Z)$ |
| `$\Lambda_4^{1/4}$` | $\Lambda_4^{1/4}$ |

---

## Greek letters

| Syntax | Renders as | Syntax | Renders as |
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

## Operators and symbols

| Syntax | Renders as | Meaning |
|:---|:---|:---|
| `$\times$` | $\times$ | Multiplication |
| `$\cdot$` | $\cdot$ | Dot product |
| `$\approx$` | $\approx$ | Approximately |
| `$\propto$` | $\propto$ | Proportional to |
| `$\sim$` | $\sim$ | Order of |
| `$\rightarrow$` | $\rightarrow$ | Right arrow |
| `$\Rightarrow$` | $\Rightarrow$ | Implies |
| `$\pm$` | $\pm$ | Plus-minus |
| `$\partial$` | $\partial$ | Partial derivative |
| `$\int$` | $\int$ | Integral |
| `$\sum$` | $\sum$ | Sum |
| `$\prod$` | $\prod$ | Product |
| `$\infty$` | $\infty$ | Infinity |
| `$\det$` | $\det$ | Determinant |
| `$\dim$` | $\dim$ | Dimension |
| `$\text{Tr}$` | $\text{Tr}$ | Trace |
| `$\otimes$` | $\otimes$ | Tensor product |
| `$\oplus$` | $\oplus$ | Direct sum |

---

## Fractions, roots, brackets

```markdown
Fraction: $\frac{8\pi^2}{3}$
Large fraction: $$\frac{8\pi^2}{3}$$

Root: $\sqrt{|\det L_p|}$
nth root: $\Lambda_4^{1/4}$

Absolute value: $|W(SU(3))|$
Norm: $\|e_T\|$

Adaptive brackets: $\left(\frac{3}{2}\right)^5$
```

---

## Text and whitespace

```markdown
Text within formulas: $\text{GeV}$, $\text{Fix}(T^4)$
Spacing: $\quad$ (1em), $\qquad$ (2em), $\ $ (thin space)
Line break (within $$): \\
```

---

## Common symbol combinations

```markdown
Fine-structure constant:              $\alpha^{-1}$
Strong coupling:                       $\alpha_s(M_Z)$
Weinberg angle:                        $\sin^2\theta_W(M_Z)$
Planck mass:                           $M_{Pl}$
KK scale:                              $M_{KK}$
7D Planck mass:                        $M_7$
Higgs VEV:                             $v$
Higgs mass:                            $m_H$
Electron mass:                         $m_e$
Neutrino mass sum:                     $\Sigma m_\nu$
Hubble constant:                       $H_0$
Cosmological constant:                 $\Lambda_4$
Casimir coefficient:                   $C_{cas}$
Topological constant:                  $K$
Enhancement factor:                    $\eta$
Black hole entropy:                    $S$
Inflationary spectral index:           $n_s$
Generation number:                     $N_g$
Liquid drop model coefficient:         $a_s$
Vortex core energy:                    $E_{core}$
BEC density parameter:                 $\rho_s$
Fixed point set:                       $\text{Fix}(T^4)$
Euler characteristic:                  $\chi(CP^2)$
Weyl group order:                      $|W(SU(3))|$
Fubini-Study volume:                   $\text{Vol}_4(CP^2)$
```

---

## Formulas in tables

```markdown
| Quantity | Formula | Value |
|:---|:---|:--:|
| $\alpha^{-1}$ | $4\pi^3+\pi^2+\pi$ | $137.036304$ |
| $M_{Pl}$ | $\sqrt{M_7^5\cdot V_R\cdot(1+\eta)}$ | $2.35\times 10^{18}$ |
```

---

## Matrices

```markdown
$$\begin{pmatrix}
V_{ud} & V_{us} & V_{ub} \\
V_{cd} & V_{cs} & V_{cb} \\
V_{td} & V_{ts} & V_{tb}
\end{pmatrix}$$
```

---

## Multi-line formulas

```markdown
$$\begin{aligned}
C_{cas} &= \left(\frac{\chi(CP^2)}{\dim_\mathbb{C}(CP^2)}\right)^{D-2} / \pi^{\dim_{int}} \\
        &= \left(\frac{3}{2}\right)^5 / \pi^3 \\
        &= 0.24491
\end{aligned}$$
```

---

## Color coding

```markdown
🟢 Mathematical theorem: strictly holds, deviation = 0
🟡 Physical derivation: deviation < 5%
🔴 Order-of-magnitude estimate: deviation 10-50%
🔵 Falsifiable prediction: awaiting experimental verification
```

---

## Prohibited

- ❌ Do not use Unicode superscripts/subscripts (e.g. `¹⁸`) — use `$10^{18}$`
- ❌ Do not use Unicode Greek letters (e.g. `α`) — use `$\alpha$`
- ❌ Do not wrap plain text in `$` outside formulas
- ❌ Do not mix `$` and `$$` in the same paragraph
- ❌ Do not use complex formulas in table header rows (causes alignment issues in some renderers)