# SCVC V3.0 英文翻译工程 — AI 提示词

**来源**: `C:\Users\20606\Desktop\SCVC-github\cn\V3.0\`
**目标**: `C:\Users\20606\Desktop\SCVC-github\en\V3.0\`
**文件数**: 74 .md + 14 .py = 88 文件 (~205 KB 中文)
**语言**: 简体中文 → 学术英文

---

## 翻译原则（必须在提示词中明确）

1. **TeX 数学公式完全不改。** `$\alpha^{-1}=4\pi^3+\pi^2+\pi$` 保持原样。只翻译公式外的中文。
2. **物理术语使用标准英文**：`精细结构常数` → `fine-structure constant`, `涡旋` → `vortex`, `不动点` → `fixed point`, `局域化` → `localization`, `涌现` → `emergence`, `流形` → `manifold`, `等距群` → `isometry group`, `示性数` → `Euler characteristic`, `旋量` → `spinor`, `序参量` → `order parameter`。
3. **保持客观叙述语气**。中文原文已经是"无口气、纯叙述"，英文对应为学术论文风格。不用 hype 词汇（`remarkable`, `astonishing`, `revolutionary`）。
4. **数值和符号逐字保留**。`2.35×10¹⁸` 保持格式，`−3.5%` 保持负号。
5. **表格保持对齐**。Markdown 表格的 `|:---|` 对齐语法不改。
6. **保留所有 emoji 状态标记**：🟢🟡🔴🔵。
7. **保留所有交叉引用**：`§1.2`, `见全面推导版` → `see Full Derivation Edition`。
8. **文件命名**：保持中文文件名或翻译为英文？→ **翻译为英文**（如 `1.1_唯一公设_真空F1旋量BEC.md` → `1.1_Postulate_F1_Spinor_BEC_Vacuum.md`）。
9. **方框公式保留**：`\boxed{...}` 不变。
10. **诚实标注保持**："已知裂缝" → "Known Issues", "诚实评估" → "Honest Assessment"。

---

## 分阶段翻译计划

### Stage E0: 骨架
- `README.md`
- `TEX_FORMAT.md`
- `全面推导版/00_总纲.md` → `Full_Derivation/00_Overview.md`
- `简洁推导版/00_总纲.md` → `Simplified/00_Overview.md`
- `校验报告.md` → `Validation_Report.md`

### Stage E1: §1 公设与几何 (5 × 2 = 10 files)
### Stage E2: §2 规范扇区 (5 × 2 = 10 files)
### Stage E3: §3 引力扇区 (5 × 2 = 10 files)
### Stage E4: §4 粒子谱 (7 × 2 = 14 files)
### Stage E5: §5 跨域涌现 (3 × 2 = 6 files)
### Stage E6: §6 宇宙学 (4 × 2 = 8 files)
### Stage E7: §7 预言与评估 (3 × 2 = 6 files)
### Stage E8: 附录 (4 files)
### Stage E9: 计算脚本 README (1 file)
### Stage E10: 英文母语润色 + 术语一致性检查

---

## 可直接使用的翻译 AI 提示词模板

将以下提示词发给翻译 AI，每次一个 Stage：

```
你是一位学术物理翻译专家。请将以下 SCVC V3.0 的中文 Markdown 文件翻译为学术英文。

## 严格规则

1. TeX 数学公式完全不改。保持所有 $...$ 和 $$...$$ 内容原样。
2. 物理术语使用标准英文学术表达。
3. 保持客观叙述语气——不使用 hype 词汇。
4. 保留所有数值格式、emoji 状态标记（🟢🟡🔴🔵）、表格对齐。
5. 保留所有交叉引用结构，将"§1.2"改为"§1.2"，"见全面推导版"改为"see Full Derivation Edition"。
6. 文件名翻译为英文（用下划线代替空格）。
7. 输出 UTF-8 编码的 .md 文件。

## 术语表（使用这些英文表达）

| 中文 | English |
|:---|:---|
| 精细结构常数 | fine-structure constant |
| 强耦合 | strong coupling |
| 涡旋 | vortex |
| 不动点 | fixed point |
| 局域化 | localization |
| 涌现 | emergence |
| 流形 | manifold |
| 等距群 | isometry group |
| 示性数 | Euler characteristic |
| 旋量 | spinor |
| 序参量 | order parameter |
| 公设 | postulate |
| 模空间 | moduli space |
| 规范群 | gauge group |
| 希格斯 | Higgs |
| 费米子 | fermion |
| 玻色子 | boson |
| 拉格朗日量 | Lagrangian |
| 作用量 | action |
| 路径积分 | path integral |
| 重整化群 | renormalization group |
| 宇宙学常数 | cosmological constant |
| 暗物质 | dark matter |
| 暴涨 | inflation |
| 重子生成 | baryogenesis |
| 可证伪 | falsifiable |
| 预言 | prediction |
| 诚实评估 | Honest Assessment |
| 已知裂缝 | Known Issues |

请翻译以下文件的内容，保持 Markdown 结构完全不变：
[在此粘贴 .md 文件内容]
```

---

## 注意事项

- V3.0 约 205 KB 中文，预计英文版本约 150-170 KB（英文通常更紧凑）。
- Python 脚本（.py）不需要翻译——注释可选择性翻译。
- Stage E10（母语润色）建议找英文母语的物理研究生或使用 Claude/GPT-4 的高级润色模式。
- 术语一致性是关键——建议先翻译 `TEX_FORMAT.md` 和术语表作为参考，再翻译正文。
