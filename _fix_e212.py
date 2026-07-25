import re, os

path = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations\Vol9_Doomsday_Countdown\E212_Immortality_Timeline_ABC_vs_Modern_Society.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

T = []

# (chinese_pattern, english_replacement)
T.append((
    '> **输入**：SCVC常数（H键0.20eV→蛋白质折叠稳定性、C-C键3.6eV→AGEs交联Ceiling、ATP 0.3eV→代谢率约束、Landauer 2.85e-21 J/bit→AI研究能耗地板、consciousness带宽~100bps→主观lifespan、脑容量~5e15 bits→记忆溢出）\n> **方法**：长寿逃逸速度定义 → ABC复利式永生4轮推演 → 现代社会4死锁负效率分析 → 100%覆盖数学证明 → 滚动永生哲学\n> **核心命题**：ABC约60-80年达到逃逸速度（每年突破>1年lifespan），现代社会概率<0.1%。ABC不是"让永生更快"——是让永生从"不可能"变成"必然"。',
    '> **Inputs**: SCVC constants (H-bond 0.20eV → protein folding stability, C-C bond 3.6eV → AGEs crosslink Ceiling, ATP 0.3eV → metabolic rate constraint, Landauer 2.85e-21 J/bit → AI research energy floor, consciousness bandwidth ~100bps → subjective lifespan, brain capacity ~5e15 bits → memory overflow)\n> **Method**: Longevity escape velocity definition → ABC compound-interest immortality 4-round projection → modern society 4-deadlock negative-efficiency analysis → 100% coverage mathematical proof → rolling immortality philosophy\n> **Core Thesis**: ABC achieves escape velocity in approximately 60-80 years (annual breakthroughs > 1 year lifespan), modern society probability < 0.1%. ABC does not "make immortality faster" — it makes immortality go from "impossible" to "inevitable."'
))

# escape velocity table
T.append((
    '定义: 每年医学/生物科技进步增加的人类健康lifespan > 1年',
    'Definition: Annual medical/biotechnological progress increases healthy human lifespan by > 1 year'
))
T.append((
    '状态              年延寿率    结果',
    'Status              Annual Extension    Result'
))
T.append((
    '亚逃逸             0.3年/年    每年老1年，医学补0.3年\n                              净老化 +0.7年/年 → 终将死亡',
    'Sub-escape          0.3 yr/yr    Age 1 year annually, medicine adds 0.3 yr\n                              Net aging +0.7 yr/yr → will eventually die'
))
T.append((
    '临界               1.0年/年    每年老1年，医学补1.0年\n                              净老化 0 → lifespan暂停，但未延长',
    'Critical            1.0 yr/yr    Age 1 year annually, medicine adds 1.0 yr\n                              Net aging 0 → lifespan paused, but not extended'
))
T.append((
    '逃逸               1.1年/年    每年老1年，医学补1.1年\n                              净延寿 +0.1年/年 → 离死亡越来越远',
    'Escape              1.1 yr/yr    Age 1 year annually, medicine adds 1.1 yr\n                              Net extension +0.1 yr/yr → getting farther from death'
))
T.append((
    '强逃逸             1.5年/年    净延寿 +0.5年/年 → 快速远离死亡\n                              此后不再需要计算具体lifespanCeiling',
    'Strong Escape       1.5 yr/yr    Net extension +0.5 yr/yr → rapidly pulling away from death\n                              No longer need to compute specific lifespan Ceiling'
))
T.append((
    '"逃逸速度"不是永生——是"死亡永远追不上你"',
    '"Escape velocity" is not immortality — it is "death can never catch up to you"'
))
T.append((
    '关键洞察:\n  逃逸前: 你在和时间赛跑，且快输了\n  逃逸后: 时间在和你赛跑，且永远赢不了\n  \n  逃逸速度不是一个"技术"——是一个"交叉点"\n  在此交叉点之前，每轮突破买的是"更多研究时间"\n  在此交叉点之后，永生是自然结果，不需要再"解决"',
    'Key insight:\n  Before escape: you are racing against time, and about to lose\n  After escape: time is racing against you, and can never win\n  \n  Escape velocity is not a "technology" — it is an "inflection point"\n  Before this inflection point, each round of breakthroughs buys "more research time"\n  After this inflection point, immortality is a natural consequence; no further "solution" is needed'
))

# prerequisites
T.append((
    '技术前提:\n  (1) 基础健康lifespan >= 120-150岁（给研究争取50-70年窗口）\n  (2) 衰老机制被分解为可独立处理的模块（5条路径: E179）\n  (3) AI辅助研究成熟（加速每一轮突破的发现->临床周期）\n  (4) 社会稳定性（不被战争/动荡中断研究链条）\n  (5) 资金充足且持续（不被腐败/浪费大量分流）',
    'Technical prerequisites:\n  (1) Baseline healthy lifespan >= 120-150 years (securing a 50-70 year research window)\n  (2) Aging mechanisms decomposed into independently treatable modules (5 pathways: E179)\n  (3) AI-assisted research mature (accelerating discovery→clinical cycle for each round of breakthroughs)\n  (4) Social stability (research chain not interrupted by war/instability)\n  (5) Sufficient and sustained funding (not massively diverted by corruption/waste)'
))
T.append((
    '其中 (4) 和 (5) 是现代社会最薄弱的环节\nABC通过制度设计消除了这两个瓶颈',
    'Of these, (4) and (5) are the weakest links in modern society\nABC eliminates both bottlenecks through institutional design'
))

# SCVC constraints
T.append((
    'SCVC约束:\n  可优化路径: 端粒、线粒体、表观遗传（工程墙，非物理墙）\n  不可压缩:   DNA自发突变（热力学）、AGEs交联（C-C键3.6eV）\n  绕过策略:   基因冗余N=3（E186）、酮代谢（E188）、纳米维护（E189）',
    'SCVC constraints:\n  Optimizable pathways: telomeres, mitochondria, epigenetics (engineering walls, not physical walls)\n  Incompressible: DNA spontaneous mutation (thermodynamics), AGEs crosslinking (C-C bond 3.6eV)\n  Bypass strategies: gene redundancy N=3 (E186), ketone metabolism (E188), nano-maintenance (E189)'
))

# Round 1
T.append((
    '### 2.2 第一轮 (T=0到20年): 基础寿命延长 → 120-130岁',
    '### 2.2 Round 1 (T=0 to 20 years): Baseline Lifespan Extension → 120-130 years'
))
T.append((
    '### 2.3 第二轮 (T=20到50年): 纳米维护成熟 → 180-200岁',
    '### 2.3 Round 2 (T=20 to 50 years): Nano-Maintenance Matures → 180-200 years'
))
T.append((
    '### 2.4 第三轮 (T=50到80年): 攻克大多数衰老模块 → 250-350岁',
    '### 2.4 Round 3 (T=50 to 80 years): Conquering Most Aging Modules → 250-350 years'
))
T.append((
    '### 2.5 第四轮 (T=80到120年): 逃逸巩固 → 永生成为默认',
    '### 2.5 Round 4 (T=80 to 120 years): Escape Consolidation → Immortality Becomes Default'
))

# Section headers
T.append((
    '## 1. 长寿逃逸速度的定义',
    '## 1. Definition of Longevity Escape Velocity'
))
T.append((
    '### 1.1 什么是"逃逸速度"',
    '### 1.1 What Is "Escape Velocity"'
))
T.append((
    '### 1.2 达到逃逸速度需要的五个前提',
    '### 1.2 Five Prerequisites for Achieving Escape Velocity'
))
T.append((
    '## 2. ABC路径——复利式永生（4轮滚动）',
    '## 2. The ABC Pathway — Compound-Interest Immortality (4 Rolling Rounds)'
))
T.append((
    '### 2.1 复利模型',
    '### 2.1 The Compound-Interest Model'
))
T.append((
    '### 2.6 ABC永生时间线总览',
    '### 2.6 ABC Immortality Timeline Overview'
))
T.append((
    '## 3. ABC的100%覆盖——不是慈善，是数学',
    '## 3. ABC 100% Coverage — Not Charity, Mathematics'
))
T.append((
    '### 3.1 为什么必须100%',
    '### 3.1 Why 100% Is Necessary'
))
T.append((
    '### 3.2 为什么ABC能做到100%而现代社会做不到',
    '### 3.2 Why ABC Can Achieve 100% and Modern Society Cannot'
))
T.append((
    '## 4. 现代社会路径——为何是负效率',
    '## 4. The Modern Society Pathway — Why It Is Negative Efficiency'
))
T.append((
    '### 4.1 四个结构性死锁',
    '### 4.1 Four Structural Deadlocks'
))
T.append((
    '### 4.2 现代社会的"拖后腿"量化',
    '### 4.2 Quantifying Modern Society\'s "Drag"'
))
T.append((
    '### 4.3 现代社会达到逃逸速度的条件概率',
    '### 4.3 Conditional Probability of Modern Society Achieving Escape Velocity'
))
T.append((
    '### 4.4 现代社会时间线（如果奇迹般一切顺利）',
    '### 4.4 Modern Society Timeline (If, Miraculously, Everything Goes Right)'
))
T.append((
    '## 5. ABC加速因子的汇总',
    '## 5. Summary of ABC Acceleration Factors'
))
T.append((
    '## 6. 综合对比',
    '## 6. Comprehensive Comparison'
))
T.append((
    '## 7. "滚动永生"的哲学含义',
    '## 7. Philosophical Implications of "Rolling Immortality"'
))
T.append((
    '## 附录A：关键SCVC常数',
    '## Appendix A: Key SCVC Constants'
))
T.append((
    '## 附录B：关键公式',
    '## Appendix B: Key Formulas'
))
T.append((
    '## 附录C：不确定性声明',
    '## Appendix C: Uncertainty Declaration'
))

# Key sentences
T.append((
    'ABC不是"让永生更快"——是让永生从"不可能"变成"必然"',
    'ABC does not "make immortality faster" — it makes immortality go from "impossible" to "inevitable"'
))
T.append((
    '现代社会被四个死锁卡住',
    'Modern society is trapped by four deadlocks'
))
T.append((
    '这些不是技术问题——是制度问题',
    'These are not technical problems — they are institutional problems'
))
T.append((
    '4轮滚动: 120岁→200岁→300岁→逃逸, 约60-80年',
    '4 rolling rounds: 120 yr → 200 yr → 300 yr → escape, approximately 60-80 years'
))
T.append((
    'ABC通过B层透明+零利率+货币重置+碳预算, 消除了所有归零因子',
    'ABC, through B-layer transparency + zero interest rate + currency reset + carbon budget, eliminates all zeroing-out factors'
))

rep = 0
for old, new in T:
    if old in content:
        content = content.replace(old, new)
        rep += 1

cn = len(re.findall(r'[\u4e00-\u9fff]', content))
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
total = len(content)
print(f"E212: {cn} CN chars / {total} total = {round(cn/total*100,1)}% CN remaining | {rep}/{len(T)} replacements applied")
