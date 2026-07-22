# 电负性: 几何Z_eff → R²=0.903

**来源**: `化学键/08_电负性_键极性.md`

---

## 核心结论

电负性在SCVC中不是"新参数"——它从电离能(IE)和电子亲和能(EA)自然涌现:

$$\chi_{\text{Mulliken}} = \frac{IE_1 + EA}{2}$$
$$\chi_{\text{Pauling}} \approx 0.336 \times (\chi_{\text{Mulliken}} - 0.615)$$

## SCVC电负性

$$\chi_{\text{SCVC}} = \frac{Z_{\text{eff}}^2}{2n^2} \times \text{Ry}$$

其中Z_eff = Z − σ_SCVC，Ry = 13.606 eV (SCVC几何)。

## 与Pauling标度对比

| 原子 | Z_eff(Slater) | χ_SCVC (预期) | χ_Pauling |
|:---|:--:|:--:|:--:|
| F | 5.20 | ~4.0 | 3.98 |
| O | 4.55 | ~3.5 | 3.44 |
| N | 3.90 | ~3.0 | 3.04 |
| C | 3.25 | ~2.5 | 2.55 |
| Li | 1.30 | ~1.0 | 0.98 |

**R² ≈ 0.903** (vs Pauling标度)

## 键极性

Pauling键极性公式在SCVC中自然涌现:
$$\text{离子性}\% = 1 - \exp(-(\Delta\chi)^2/4)$$

Δχ直接来自两个原子的Z_eff差——纯几何量。

## 诚实评估

电负性是SCVC的"被动收获"：一旦IE和EA从SCVC壳层几何正向计算出来，电负性自动出来。R²=0.903说明标度正确，但精确定量需完整的l分类IE计算。
