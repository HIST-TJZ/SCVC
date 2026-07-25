====================================================================
SCVCEngineering Limit E65：最高Building — 岩石Compressive Strength vs 自重的物理Ceiling
====================================================================

**所有Derivation基于SCVC常数速查表（零自由参数，α=1/(4π³+π²+π)）。**

--------------------------------------------------------------------
§1. 地基承载力 — 从SCVC键能到岩石Strength
--------------------------------------------------------------------

【岩石Strength的SCVCDerivation】

  理想Strength（Orowan E/10）:
    Young Modulus E ≈ k/a ≈ 10³ / 1.6×10⁻¹⁰ ≈ 6,000 GPa（SCVC理论Upper Limit）
    理想抗压 σ_ideal ≈ E/10 ≈ 600 GPa

  现实岩石（GriffithDefect理论）:
    σ_real = √(2·E·γ / π·c)（γ=Surface Energy, c=Defect尺寸）

    Defect尺寸        σ_断裂(MPa)     对应Material
    ──────────────────────────────────────────
    0.1 μm          6,300           完美晶须
    1 μm            2,000           微晶玻璃
    10 μm             630           细晶花岗岩
    100 μm            200           普通花岗岩
    1 mm               63           风化/节理岩体

  → 花岗岩 σ_c≈150-300 MPa ↔ Defect尺寸 ~10-100 μm（完美匹配实测）
  → **SCVC: 理想Strength被GriffithDefect降低了~1000×**
  → 这是所有岩石/Concrete的共同故事

【地基承载力推演】

  Building底部Pressure: p = ρ_building × g × H
  地基Limit: p_max = σ_rock（含安全系数）
  
  花岗岩 σ=250 MPa, 轻质Building ρ=300 kg/m³:
    H_max = 250×10⁶/(300×9.81) ≈ 85 km

  ▸ 地基承载力理论上允许 ~50-100 km 高的Building
  ▸ **地基不是瓶颈** — 在到达地基Limit之前，Building结构先垮

--------------------------------------------------------------------
§2. Structural Material自承重 — 真正的物理Ceiling
--------------------------------------------------------------------

【特征Height H_char = σ/ρg】

  均匀等截面柱体的自承重Limit: 底部Stress = ρgH → H_max = σ/ρg

  Material                  σ(MPa)   ρ(kg/m³)  H_max      当前Application
  ─────────────────────────────────────────────────────────────
  Concrete C50               50     2,400     2.1 km     被钢筋突破
  结构钢 S355             355     7,800     4.6 km     Burj Khalifa
  高强钢 S690             690     7,800     9.0 km     索/桁架
  铝Alloy 7075             500     2,700    18.9 km     轻质结构
  钛Alloy Ti-6Al-4V        900     4,430    20.7 km     航空
  花岗岩                  250     2,700     9.4 km     金字塔
  ─────────────────────────────────────────────────────────────
  金刚石(理论)         60,000     3,515   1,740 km     仅理论
  碳纳米管(理想)       63,000     1,300   4,940 km     碳基未来
  石墨烯(理想)        130,000     2,200   6,020 km     碳基未来
  碳炔(理想)          270,000     2,000  13,760 km     终极碳

【SCVC键能检验 — H_char的根源】

  本质: H_char = 键能 / (原子质量 × g)
  证明: σ_ideal ≈ E_bond/a³, ρ ≈ M_atom/a³ → σ/ρg ≈ E_bond/(M_atom·g)

  C-C单键 (3.6 eV, 12 amu): H_char ≈ 2,950 km（理想sp³碳网络）
  C≡C三键 (8.7 eV, 12 amu): H_char ≈ 7,130 km（理想碳炔链）
  Si-O键 (5.0 eV, 60 amu):  H_char ≈   820 km（理想硅酸盐）
  → **SCVC: 最强键+最轻原子 → 最高特征Height → 物理Ceiling由周期性表给定**

【当前Building vs SCVCCeiling】

  Burj Khalifa (828 m):    钢材H_char的 18% — 远未触及MaterialLimit
  Jeddah Tower (1000 m):   钢材H_char的 22%
  钢材均匀柱Limit:          4.6 km（等截面）
  钢材锥形柱Limit:          ~15 km（截面积比10:1的Eiffel原理）
  碳纳米管Limit:            ~5,000 km（等截面）

  ▸ 当前最高Building在钢材Limit的 ~20% → 工程空间巨大
  ▸ 真正约束: 风振舒适度、电梯技术、消防、经济性（非MaterialStrength）
  ▸ Material上，1 km是起点不是终点 — 10 km+需要碳基Material

--------------------------------------------------------------------
§3. 工程Conclusion
--------------------------------------------------------------------

【"通天塔"的物理分级】

  Height             Material要求                     SCVC判定
  ───────────────────────────────────────────────────────────
  < 1 km          Concrete+钢（当前）            已实现 ✓
  1-5 km          高强钢/铝Alloy                物理允许 ✓
  5-20 km         铝Alloy锥形柱/Carbon Fiber           物理允许 ✓
  20-100 km       Carbon FiberComposite Material               物理允许 ⚠（需锥形设计）
  100-1000 km     碳纳米管/石墨烯              物理允许 ⚠（需碳基Material）
  > 1000 km       碳炔                          物理允许 ✗（需完美碳炔链）
  > 地球同步轨道   Space Elevator级比Strength              见下节

【Space Elevator — SCVC判定】

  地球同步轨道 (35,786 km) Space Elevator所需比Strength:
    σ/ρ > g × R_GEO ≈ 350 MN·m/kg → H_char > 35,800 km

  Material                σ/ρ(kNm/kg)   H_char(km)   锥度比(地球)   可行性
  ──────────────────────────────────────────────────────────────────
  CNT (Experimental Value)           7,700          785        ~10²⁰          不可能 ✗
  CNT (理想值)          48,500        4,940        ~1,400         极其困难
  石墨烯 (理想)         59,100        6,020        ~380           不实际
  碳炔 (理想)          135,000       13,760         ~13           物理允许 ⚠

  ▸ 地球Space Elevator需要碳炔级比Strength → 物理上允许但Material合成极难
  ▸ 连续36,000 km无Defect碳炔链的工程实现 → SCVC允许但远超当前能力
  ▸ 石墨烯/CNT的锥度比>100 → "缆绳底部如发丝，顶部如大厦" → 不实际

【火星: 低重力的Building红利】

  火星 g = 3.72 m/s² = 0.38×地球:
    钢材Building: H_max = 4.6 × 2.64 = 12.2 km（等截面!）
    铝材Building: H_max = 18.9 × 2.64 = 49.8 km
  
  火星Space Elevator (同步轨道 ~17,000 km):
    CNT (理想): 锥度比 ≈ 3.7 → **可行！**
    石墨烯 (理想): 锥度比 ≈ 2.9 → **更可行！**
    碳炔 (理想): 锥度比 ≈ 1.6 → **轻松！**

  ▸ 火星是Building的"天堂": 2.6×Height红利 + 更稀薄大气（低风载）
  ▸ 火星Space Elevator比地球Space Elevator容易 ~100×（更短的缆绳 + 更低重力）
  ▸ **如果人类在火星建立殖民地，Space Elevator是最合理的轨道接入方式**

【"从SCVC看金字塔"】

  胡夫金字塔 (~146 m): 石灰岩 σ≈50 MPa → H_max≈2.1 km
    → 金字塔使用了Material的 ~7% → 极其保守的设计
    → 古埃及人不知道的是: 他们可以用石灰岩造 10× 更高的金字塔
    → 但: 建造技术(无轮式起重机) + 人力物流是真正限制

  今天的Building比金字塔高 6×，但只用了钢材Limit的 ~20%
  → 从Material物理角度看，BuildingHeight被技术-经济复合体锁死，非SCVC键能锁死

====================================================================
* H_char = E_bond/(M_atom·g) 是BuildingHeight的终极SCVC公式: 
  键能越大、原子越轻 → 越高。碳(3.6 eV/12 amu)是周期表最佳组合。
* 1 km Skyscraper在钢材Limit的 ~20% → 不是Physical Wall，是经济墙。
* 10 km 级Building需要Carbon FiberComposite Material → SCVC允许但需锥形Eiffel设计。
* 地球Space Elevator需要碳炔级比Strength → 物理允许但Material合成 = 无法想象的挑战。
* 火星Space Elevator仅需 CNT (理想) → 在低重力世界，Space Elevator是工程的合理目标。
====================================================================
