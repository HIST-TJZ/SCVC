# SCVC V3.0 — 微分几何统一物理常数 / Unifying Physical Constants via Differential Geometry

> **一个假设：真空是 F=1 旋量玻色-爱因斯坦凝聚。**
> **一个结果：标准模型全部26个无量纲常数 + 392项工程极限，从同一个几何根长出。**
>
> *One hypothesis: vacuum is an F=1 spinor BEC.*
> *One result: all 26 dimensionless SM constants + 392 engineering limits, from a single geometric root.*

---

## 🧭 你是谁？从这里进 / Who Are You? Start Here

| 你是… / You are… | 从这里开始 / Start here | 需要什么背景 / Background needed |
|:---|:---|:---|
| 🧮 **数学家 / Mathematician** | [E271_几何即物理_纯几何验证清单](E271_几何即物理_纯几何验证清单.md) ([EN](en/E271_Geometry_Equals_Physics_Pure_Geometry_Verification_Checklist.md)) | 微分几何 / toric Kähler |
| 🔬 **物理学家 / Physicist** | [cn/全面推导版/](cn/全面推导版/) ([EN](en/Full_Derivation/)) | QFT + Standard Model |
| 📖 **想看结论 / Quick Conclusions** | [cn/简洁推导版/](cn/简洁推导版/) ([EN](en/Summary_Derivation/)) | College physics |
| 🔧 **工程师/好奇 / Engineer/Curious** | [E000 工程极限总字典](cn/08_工程极限/E000_工程极限总字典.md) | None — browse what interests you |
| 🌍 **中文读者** | [cn/README.md](cn/README.md) | — |
| 🌐 **English readers** | [en/README.md](en/README.md) | — |

---

## 核心数字 / Key Numbers

| 物理量 / Quantity | 几何公式 / Geometric Formula | 预言值 / Predicted | 实验值 / Experiment | 偏差 / Dev. |
|:---|:---|:--:|:--:|:--:|
| 精细结构常数 / Fine-structure constant | α⁻¹ = 4π³ + π² + π | 137.036304 | 137.035999 | **2.22 ppm** |
| 强耦合 / Strong coupling (M_KK) | α_s⁻¹ = 16π | 50.27 | — | geometric baseline |
| 哈勃常数 / Hubble constant | H₀ = 67.47 | 67.47 | 67.4 | **+0.10%** |
| μ子/电子质量比 / Muon/electron mass ratio | m_μ/m_e = 4π³·(5/3) | 206.71 | 206.77 | **−0.03%** |
| τ/电子质量比 / Tau/electron mass ratio | m_τ/m_e = 36π⁴ | 3509 | — | −0.9% |
| 费米子代数 / Fermion generations | N_g = 3 | 3 | 3 | **0%** |
| 希格斯/W 质量比 / Higgs/W mass ratio | m_H/m_W = π/2 | 1.5708 | 1.556 | +0.9% |
| 原初谱指数 / Primordial spectral index | n_s = 1−2/N_e | 0.964 | 0.9649 | −0.1% |

---

## 为什么这不是"拟合" / Why This Isn't Curve-Fitting

- **0 个自由参数 / 0 free parameters.** 26 SM constants forward-derived from the same geometric manifold (CP²×S¹) using the same computational framework (DH/GKM localization).
- **精度不是调出来的 / Precision is not tuned.** The integers (4,1,1) in α⁻¹=4π³+π²+π are the only combination that matches experiment among all integer triples — change any one, the result collapses.
- **392 项工程极限互相印证 / 392 engineering limits cross-validate each other.** From superconducting Tc to the rainbow's 42°, from earthquake M9.5 to cell size ~10μm — all from the same set of bond energies, which trace back to the same α.

---

## 文件结构 / Structure

`
SCVC-github/
├── README.md                                          ← You are here
├── E271_几何即物理_纯几何验证清单.md                      ← Mathematician hook (CN)
├── E270_SCVC反哺数学_截锥DH不变量猜想.md                  ← Math deep dive (CN)
├── cn/                                                ← Chinese V3.0
│   ├── README.md
│   ├── 全面推导版/        (Full Derivation)
│   ├── 简洁推导版/        (Summary)
│   ├── 计算过程/          (Calculation Process)
│   ├── 08_工程极限/       (Engineering Limits: E000 index + 392 items)
│   └── 附录/              (Appendix)
├── en/                                                ← English V3.0
│   ├── README.md
│   ├── Full_Derivation/
│   ├── Summary_Derivation/
│   ├── Calculation_Process/
│   ├── 08_Engineering_Limits/
│   ├── E271_Geometry_Equals_Physics_...
│   └── E270_SCVC_Feedback_to_Mathematics_...
├── simulation/                                        ← Godot visualizations
├── calculations/                                      ← Python verification scripts
└── 历史存档/v2.0/                                      ← V2.0 archive
`

---

> **"先别信。自己算。" / "Don't believe it. Compute it yourself."**
> 
> 数学家 / Mathematicians → [E271](E271_几何即物理_纯几何验证清单.md): 24 pure geometry calculations, each matching a physical constant. One is coincidence. Twenty-four?
> 
> 其他人 / Everyone else → [E000 总字典 / Index](cn/08_工程极限/E000_工程极限总字典.md): Browse any topic — rainbow, earthquake, cancer, superconductor — trace how it all starts from the same α.
