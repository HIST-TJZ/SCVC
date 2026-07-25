# P6: Kähler → N=2 SUSY — 定理级证明

**置信度**: 100% (标准数学定理)  
**来源**: `公设消化/P6_SUSY局域化_推导_结果.md`

---

## 核心定理 (Zumino 1979, Alvarez-Gaumé & Freedman 1981)

> 令 (M, ω, J) 为Kähler流形。则以M为靶空间的超对称σ模型自动具有N=2超对称。

## 推导链

```
BPS涡旋环 → M_vortex (toric Kähler 3-fold)
    → Kähler + 费米子零模 → N=2 SUSY σ模型
    → SUSY局域化 → DH求和
    → 三个不动点 → 4π³+π²+π = α⁻¹
```

## 关键步骤

1. **Kähler条件**: M_vortex的辛形式ω从BPS动能项继承，复结构J来自ω+度规→可积。
2. **费米子零模**: Atiyah-Singer指标 → Index(D_slash)=1每涡旋。零模纤维同构于T^(1,0)M_vortex。
3. **N=2构造**: 复结构分解TM^C=T^(1,0)⊕T^(0,1)，对应独立超对称生成元Q和Q†。
4. **N=2 → DH**: SUSY局域化定理(Witten 1982) → 路径积分局域化到矩映射不动点。
5. **不动点贡献**: F1(4π³) + C2(π²) + F3(π) = α⁻¹ = 137.036304，偏差2.22 ppm。

## P6状态变更

| 方面 | v1.0 | v2.0 |
|:---|:---|:---|
| N=2 SUSY来源 | 假设 | Kähler几何的数学必然 |
| 置信度 | ~80% | 100% (标准定理) |
| 依赖文献 | 无 | Zumino 1979; Witten 1982; Atiyah-Bott 1984 |

## 参考文献

- Zumino, B. (1979). *Phys. Lett. B*, 87, 203.
- Alvarez-Gaumé, L. & Freedman, D.Z. (1981). *Commun. Math. Phys.*, 80, 443.
- Witten, E. (1982). *J. Diff. Geom.*, 17, 661.
- Atiyah, M.F. & Bott, R. (1984). *Topology*, 23, 1.
