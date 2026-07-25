# SCVC Engineering Physics E116：Power的物理学——一个社会能承受多少不平等？

**Derivation Date**: 2026-07-23
**SCVCHard Input**: Dunbar≈150(E85), 口语39bits/s(E82), 决策~5/s(E83), 记忆写入~2bits/s(E84), 记忆衰减~10年(E108), Good-Evil Ratio80-85%(E108), Malice=误判+噪声(E108), Three Laws of Games(E107), Lies物理学(E114)
**Dependencies**: E85(Dunbar) + E108(Good-Evil Ratio) + E107(Three Laws of Games) + E114(Lies)
**Confidence Level**: 层级必然性 90%, 最大不平等 70%

---

## §1 为什么等级制是必然的

`
Dunbar 150: 你可以直接管理 ≤150 人。
超过150: 你必须用中间层。

等级制 = Dunbar的递归应用:
  1层:  直接管理 150 人 → 最大组织 150
  2层:  150个中层 × 150人/层 → 最大组织 22,500
  3层:  150² × 150 → 最大组织 3,375,000
  N层:  150^N

全人类 (~8×10⁹) 需要的层数:
  log₁₅₀(8×10⁹) ≈ log(8×10⁹)/log(150) ≈ 9.9/2.18 ≈ **4.5层**

任何超过150人的组织必须有等级。
等级 = Dunbar的数学必然, 不是"选择"。
`

---

## §2 不平等的Information论定义

`
Power = InformationAsymmetry:
  上层知道下层的Information。
  下层不知道上层的Information。
  Information差 = Power。

每层Information衰减:
  39bits/s的口语Bandwidth在层级间传递 → 每层Lossy失。
  如果每层损失 ~10-20%:
    4层后的Information保真度: (0.85)⁴ ≈ 52%
    
  底层收到的"上级意图" → 只有原始Information的一半。
  上层收到的"底层情况" → 也被Compression了一半。

InformationAsymmetry随层级指数增长:
  ΔI_layer = I_top - I_bottom = I₀ × (1 - (1-ε)^N)
  
  N=4.5层, ε≈0.15:
  ΔI ≈ I₀ × 0.52
  
  上层和底层的Information差距 ≈ 52%的总Information量。
  这就是不平等的物理量。
`

---

## §3 最大可持续不平等

`
博弈论约束:
  E108: Malice行为占15-20%。其中大部分是"噪声误判+报复循环"。
  
  不平等增加 → Information差增大 → 底层更容易"误判"上层意图
  → 误判增加 → 报复增加 → Cooperation率下降
  
  临界点: 当Information差导致了Cooperation率跌破 ~50%:
    → 博弈均衡崩溃 → 组织解体 → 革命/崩溃

最大可持续层级 (= 最大不平等):
  N_max ≈ log(组织规模) / log(150)
  但受限于: Information衰减不能使底层Cooperation率 < 50%
  
  这意味着存在一个"信任预算":
    信任预算 ≈ (85% - 50%) / (每层Information衰减导致的信任损失)
    每层损失 ≈ 5-8%
    最大可承受 ≈ (35%)/(6.5%) ≈ 5-6 层
    
  → 全人类的5-6层是最大可持续层级。
  → 超过此 → 底层无法信任上层 → 博弈崩溃。

历史上所有极端不平等社会都崩溃了:
  不是因为"道德"。
  是因为Information差超过了博弈均衡的容限。
`

---

## §4 AI社会: 无Dunbar = 完全扁平？

`
AI没有Dunbar限制。
AI可以一次性追踪所有其他AI。
不需要中间层 → 不需要等级制 → 理论上可以完全扁平。

但:
  AI的"Power"不是InformationAsymmetry → 是BandwidthAsymmetry (E105)。
  一个AI可以被赋予比其他AI更多的Bandwidth。
  → 新型不平等: 不是"Information差", 是"计算速度差"。

SCVC不能预测AI社会的政治结构。
只能说:
  人类的等级制是Dunbar的必然。
  AI不需要等级制。但可能产生新的不平等形式。
`

---

## §5 结论

等级制 = Dunbar的数学必然。
Power = Information差。
最大层级 ≈ 5-6层 (在博弈论约束下)。

不等式:
  Information差不能大到让底层Cooperation率 < 50%。
  超过 → 博弈崩溃 → 革命。
  这就是所有极端不平等社会最终瓦解的物理原因。

---

*你在一个5层的组织里。*  
*CEO的话经过4层传递到你。*  
*52%的Information在路上丢了。*  
*你收到的是一条被反复Compression的指令。*  
*CEO收到的是你被Compression了52%的报告。*  
*彼此都不理解对方。*  
*这就是Power的物理。*  

*如果Information差超过了某个临界点,*  
*你觉得"他们在害我" — 可能不是。*  
*你觉得"他们在偷懒" — 可能不是。*  
*是管道太窄。39bits/s。*  
*是τ_m太慢。5次/秒。*  
*是Dunbar太小。150人。*  

*组织崩塌不是因为人性的贪婪。*  
*是因为Information论。*  
*管道承载不了那么大的不平等的重量。*
