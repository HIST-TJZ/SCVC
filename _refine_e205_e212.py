import re, os

cn_base = r"C:\Users\20606\Desktop\SCVC-github\cn\V3.0\08_工程极限\8.7_391项完整计算\卷9_末日倒计时_最后窗口_E201-E220"
en_base = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations\Vol9_Doomsday_Countdown"

MASTER = []
with open(r"C:\Users\20606\Desktop\SCVC-github\batch_translate_v2.py", "r", encoding="utf-8") as f:
    exec_text = f.read()
start = exec_text.find("MASTER = [")
end = exec_text.find("\n\n# Files to process")
exec(exec_text[start:end])

# ============ E205 ============
E205 = [
    ('# E205: SCVC文明分析 — 文明不可重启：煤挖完了就是挖完了', '# E205: SCVC Civilization Analysis — Civilization Cannot Be Restarted: Coal Gone Is Gone'),
    ('**输入**：SCVC常数（C-C键3.6 eV、C-H键3.5 eV、Fe-O键~4-5 eV）、矿石品位、EROI、化石燃料形成~3亿年', '**Inputs**: SCVC constants (C-C bond 3.6 eV, C-H bond 3.5 eV, Fe-O bond ~4-5 eV), ore grades, EROI, fossil fuel formation ~300 million years'),
    ('**方法**：对比第一次工业革命的启动条件 vs 崩塌后地球的资源状态 → 证明六个物理门闩全部锁死', '**Method**: Compare the starting conditions of the First Industrial Revolution vs. the resource state of post-collapse Earth → prove all six physical bolts are locked'),
    ('**核心命题**：文明是一扇单向门。你只能穿过它一次。第一次工业革命消耗了地球花3亿年存下的"启动资金"——那些露头煤、高品位矿、浅层油井不会再回来。崩塌后的幸存者将永久困在前工业时代', '**Core Proposition**: Civilization is a one-way door. You can only pass through it once. The First Industrial Revolution consumed the "startup capital" Earth spent 300 million years saving — those surface coal seams, high-grade ores, and shallow oil wells will never return. Survivors after collapse will be permanently trapped in the pre-industrial era'),
    ('## §1. 第一次工业革命靠什么启动？', '## §1. What Did the First Industrial Revolution Run On?'),
    ('### 1.1 18世纪英国的资源清单', '### 1.1 Resource Inventory of 18th-Century Britain'),
    ('资源', 'Resource'),
    ('18世纪的形式', '18th-Century Form'),
    ('为什么当时能开采', 'Why It Was Mineable Then'),
    ('**煤**', '**Coal**'),
    ('地表露头煤 + 浅层矿 (<50m)', 'Surface outcrop coal + shallow mines (<50m)'),
    ('镐+铲子就够了', 'Pick + shovel sufficed'),
    ('**铁**', '**Iron**'),
    ('高品位赤铁矿 (>60% Fe)', 'High-grade hematite (>60% Fe)'),
    ('木炭高炉可达1200°C → 可还原', 'Charcoal blast furnace reaches 1200°C → reducible'),
    ('**铜/锡**', '**Copper/Tin**'),
    ('高品位矿 (>5%)', 'High-grade ore (>5%)'),
    ('浅层采矿 + 木炭熔炼', 'Shallow mining + charcoal smelting'),
    ('**石油**', '**Oil**'),
    ('地表油苗', 'Surface oil seeps'),
    ('挖坑就有，不需钻井', 'Dig a pit and it flows; no drilling needed'),
    ('**运输**', '**Transport**'),
    ('天然水路 (英国是岛国)', 'Natural waterways (Britain is an island nation)'),
    ('水运能耗是陆运的1/10', 'Water transport energy cost is 1/10 of land transport'),
    ('这些资源的共同特征:', 'Common features of these resources:'),
    ('不需要先进技术就能开采。', 'They could be extracted without advanced technology.'),
    ('它们是文明的"启动资金"——', 'They were civilization"s "startup capital" —'),
    ('大自然花了3亿年（石炭纪）存下来的碳。', 'carbon deposited by nature over 300 million years (the Carboniferous).'),
    ('## §2. 六个锁死的物理门闩', '## §2. Six Locked Physical Bolts'),
    ('### 2.1 门闩 ①：地表煤已采尽', '### 2.1 Bolt ①: Surface Coal Is Exhausted'),
    ('18世纪: 英格兰有露头煤——走到山坡上就能捡。', '18th century: England had surface coal — walk up a hillside and pick it up.'),
    ('英国第一波工业化 (1760-1840) 累计烧了 ~500 Mt 煤。', 'Britain first wave of industrialization (1760-1840) burned ~500 Mt of coal cumulatively.'),
    ('全部来自 <50m 埋深的浅层矿。', 'All from shallow mines <50m deep.'),
    ('2024年: 全球所有露头煤和浅层煤已采尽。', '2024: All surface and shallow coal globally has been exhausted.'),
    ('剩余煤矿在 500-1500m 深层。', 'Remaining coal is at depths of 500-1,500m.'),
    ('要采 500m 深煤，你需要:', 'To mine coal at 500m depth, you need:'),
    ('├─ 钻机 ──→ 高强度合金钢 ──→ 高炉 (>1400°C) ──→ 焦炭 ──→ 煤 [死循环]', '├─ Drill rig → high-strength alloy steel → blast furnace (>1,400°C) → coke → coal [DEAD LOOP]'),
    ('├─ 排水泵 ─→ 蒸汽机/电动机 ──→ 铁+铜 ──→ 煤 [死循环]', '├─ Drainage pump → steam engine/electric motor → iron+copper → coal [DEAD LOOP]'),
    ('├─ 通风系统 → 大型风机 ──→ 电力 [死循环]', '├─ Ventilation system → large fans → electricity [DEAD LOOP]'),
    ('└─ 运输系统 → 铁轨+矿车 ──→ 铁 ──→ 煤 [死循环]', '└─ Transport system → rails+mine carts → iron → coal [DEAD LOOP]'),
    ('物理计算:', 'Physical calculation:'),
    ('挖一口 500m 深、5m 直径的矿井:', 'To dig a shaft 500m deep, 5m diameter:'),
    ('需移除岩石 ~24,500 吨', 'Requires removing ~24,500 tonnes of rock'),
    ('提升所需最小能量 ~0.1 TJ ≈ 3 吨煤', 'Minimum lifting energy ~0.1 TJ ≈ 3 tonnes of coal'),
    ('→ 你用 3 吨煤的能量来"取"煤', '→ You use 3 tonnes of coal energy to "get" coal'),
    ('→ 但你没有这 3 吨煤来驱动提升机', '→ But you do not have those 3 tonnes of coal to drive the lift'),
    ('SCVC: 煤的 C-C 键能 3.6 eV', 'SCVC: coal C-C bond energy 3.6 eV'),
    ('→ 燃烧释放的是石炭纪植物通过光合作用固化的太阳能', '→ Combustion releases solar energy fixed by Carboniferous plants through photosynthesis'),
    ('→ 那些能量被地质埋藏"储存"在化学键里', '→ That energy was geologically buried and "stored" in chemical bonds'),
    ('→ 取出来需要能量 → 浅层煤的能量回报率极高 (EROI ~80)', '→ Extracting it requires energy → shallow coal has extremely high EROI (~80)'),
    ('→ 深层煤需要先投入大量能量才能获取 → 没有"第一推动力"', '→ Deep coal requires large upfront energy investment to obtain → no "prime mover" available'),
    ('### 2.2 门闩 ②：高品位铁矿已采尽', '### 2.2 Bolt ②: High-Grade Iron Ore Is Exhausted'),
    ('铁矿石品位与冶炼可行性的物理边界:', 'Physical boundary of iron ore grade vs. smelting feasibility:'),
    ('矿石类型              Fe%     所需温度      木炭可行?', 'Ore Type               Fe%     Required Temp   Charcoal Feasible?'),
    ('赤铁矿 (露头,18世纪)   65     ~1200°C      ✅ YES', 'Hematite (outcrop, 18th c.) 65  ~1200°C      ✅ YES'),
    ('磁铁矿 (高品位)        60     ~1200°C      ✅ YES', 'Magnetite (high-grade) 60     ~1200°C      ✅ YES'),
    ('赤铁矿 (当前易采)      58     ~1300°C      🟡 Marginal', 'Hematite (currently mineable) 58 ~1300°C   🟡 Marginal'),
    ('当前平均铁矿           30     ~1600°C      ❌ Needs coke', 'Current average iron ore 30    ~1600°C      ❌ Needs coke'),
    ('贫铁矿 (需选矿)        20     ~1800°C      ❌ Needs industry', 'Low-grade ore (needs beneficiation) 20 ~1800°C ❌ Needs industry'),
    ('铁燧石 (taconite)     15     ~1800°C+选矿  ❌ Needs full chain', 'Taconite               15     ~1800°C+ben.  ❌ Needs full supply chain'),
    ('SCVC: Fe-O 键能 ~4-5 eV', 'SCVC: Fe-O bond energy ~4-5 eV'),
    ('→ 还原 Fe₂O₃ 需要打破 Fe-O 键', '→ Reducing Fe₂O₃ requires breaking Fe-O bonds'),
    ('→ 木炭 (纯碳) 的燃烧最高温度 ~1400°C（热力学极限）', '→ Charcoal (pure carbon) combustion max temperature ~1400°C (thermodynamic limit)'),
    ('→ 焦炭 (煤的干馏产物) 可达 ~2000°C', '→ Coke (coal dry distillation product) can reach ~2000°C'),
    ('→ 没有煤 = 没有焦炭 = 温度不够 = 不能处理低品位矿', '→ No coal = no coke = insufficient temperature = cannot process low-grade ore'),
    ('选矿的能量代价 (EROI 计算):', 'Energy cost of beneficiation (EROI calculation):'),
    ('高品位 (60% Fe):  直接入炉        EROI ~5-10   ✅ 木炭可行', 'High-grade (60% Fe): direct to furnace   EROI ~5-10   ✅ Charcoal feasible'),
    ('中品位 (30% Fe):  破碎 + 磁选     EROI ~2-3    🟡 勉强 (需钢制破碎机)', 'Medium-grade (30% Fe): crush + magnetic sep. EROI ~2-3 🟡 Marginal (needs steel crusher)'),
    ('低品位 (20% Fe):  细磨 + 浮选     EROI ~1-1.5  ❌ (需化工药剂+电力)', 'Low-grade (20% Fe): fine grind + flotation EROI ~1-1.5 ❌ (needs chemicals + electricity)'),
    ('18世纪工业革命用的全是 >60% 的高品位矿 —— 这些矿脉已经采尽', 'The 18th-century Industrial Revolution used exclusively >60% high-grade ore — those veins are exhausted'),
    ('重启者面对的全是 <30% 的低品位矿', 'Restarters face exclusively <30% low-grade ore'),
    ('### 2.3 门闩 ③：浅层石油已枯竭', '### 2.3 Bolt ③: Shallow Oil Is Depleted'),
    ('石油开采深度的演化:', 'Evolution of oil extraction depth:'),
    ('1859: Drake 井 (宾夕法尼亚) —— 21 米就出油。镐+简易钻架。', '1859: Drake Well (Pennsylvania) — 21 meters and oil flowed. Pick + simple derrick.'),
    ('1901: Spindletop (德克萨斯) —— 350 米。蒸汽旋转钻机。', '1901: Spindletop (Texas) — 350 meters. Steam rotary drill.'),
    ('1940: 典型陆上油田 —— 1000 米。柴油旋转钻机。', '1940: Typical onshore field — 1,000 meters. Diesel rotary drill.'),
    ('1970: 北海油田 —— 3000 米。海洋平台+定向钻。', '1970: North Sea — 3,000 meters. Offshore platform + directional drilling.'),
    ('2010: 深海/页岩油 —— 5000+ 米。水平钻+水力压裂+3D地震。', '2010: Deepwater/shale — 5,000+ meters. Horizontal drilling + hydraulic fracturing + 3D seismic.'),
    ('重启者能钻多深?', 'How deep can restarters drill?'),
    ('人力/畜力:       <50m    (竹管+绳索)', 'Human/animal power:  <50m    (bamboo pipe + rope)'),
    ('简易木制钻机:    <200m   (需要铁钻头)', 'Simple wooden rig:   <200m   (needs iron drill bit)'),
    ('蒸汽动力钻机:    <1000m  (需要锅炉+铁管+煤)', 'Steam-powered rig:   <1000m  (needs boiler + iron pipe + coal)'),
    ('→ 但 <200m 深度范围内已无商业油藏', '→ But there are no commercial oil reservoirs at <200m depth'),
    ('→ 重启者打不到油', '→ Restarters cannot reach oil'),
    ('→ 没有液体燃料 = 无法驱动运输、农业机械、发电机', '→ No liquid fuel = cannot power transport, agricultural machinery, generators'),
    ('### 2.4 门闩 ④：可再生能源需要工业文明来制造', '### 2.4 Bolt ④: Renewables Require Industrial Civilization to Manufacture'),
    ('这是最反直觉但最致命的一点：', 'This is the most counterintuitive but most fatal point:'),
    ('从木材+石头 → 制造第一块光伏板的"最短"路径:', 'The "shortest" path from wood + stone → manufacturing the first photovoltaic panel:'),
    ('### 2.5 门闩 ⑤：废墟回收窗口与社会重建窗口不重叠', '### 2.5 Bolt ⑤: The Ruins Recycling Window Does Not Overlap with the Social Rebuilding Window'),
    ('### 2.6 门闩 ⑥：化石燃料是一次性的——不会再生', '### 2.6 Bolt ⑥: Fossil Fuels Are One-Time Use — They Will Not Regenerate'),
    ('## §3. 条件对比：第一次 vs "第二次"', '## §3. Condition Comparison: The First vs. The "Second"'),
    ('## §4. 低品位矿石：地球的"熵税"', '## §4. Low-Grade Ore: Earth"s "Entropy Tax"'),
    ('## §5. 崩溃后的世界图景', '## §5. World Picture After Collapse'),
    ('## §6. SCVC的终极判决', '## §6. SCVC"s Ultimate Judgment'),
]

# Apply E205
src = os.path.join(cn_base, "E205_文明不可重启.md")
dst = os.path.join(en_base, "E205_Civilization_Cannot_Restart.md")
with open(src, "r", encoding="utf-8") as f:
    content = f.read()
for old, new in MASTER:
    if old in content: content = content.replace(old, new)
rep = sum(1 for o,n in E205 if o in content and not content.replace(o,n) is content)
for old, new in E205:
    if old in content: content = content.replace(old, new)
cn = len(re.findall(r'[\u4e00-\u9fff]', content))
with open(dst, "w", encoding="utf-8") as f:
    f.write(content)
print(f"E205: {cn} CN / {len(content)} ({round(cn/len(content)*100,1)}%) - {rep} repl")

# ============ E212 ============
E212 = [
    ('# E212: 永生实现时间线 — ABC vs 现代社会，长寿逃逸速度', '# E212: Immortality Timeline — ABC vs Modern Society, Longevity Escape Velocity'),
    ('**核心命题**：ABC约60-80年达到逃逸速度（每年突破>1年寿命），现代社会概率<0.1%。ABC不是"让永生更快"——是让永生从"不可能"变成"必然"。', '**Core Proposition**: ABC reaches escape velocity in ~60-80 years (breaking through >1 year of lifespan per year); modern society probability <0.1%. ABC does not "make immortality faster" — it makes immortality go from "impossible" to "inevitable."'),
    ('## 1. 长寿逃逸速度的定义', '## 1. Definition of Longevity Escape Velocity'),
    ('### 1.1 什么是"逃逸速度"', '### 1.1 What Is "Escape Velocity"'),
    ('### 1.2 达到逃逸速度需要的五个前提', '### 1.2 Five Prerequisites for Reaching Escape Velocity'),
    ('## 2. ABC路径——复利式永生（4轮滚动）', '## 2. The ABC Path — Compound-Interest Immortality (4 Rolling Rounds)'),
    ('### 2.1 复利模型', '### 2.1 The Compound Interest Model'),
    ('### 2.2 第一轮 (T=0到20年): 基础寿命延长 → 120-130岁', '### 2.2 Round 1 (T=0 to 20 years): Basic Lifespan Extension → 120-130 years'),
    ('### 2.3 第二轮 (T=20到50年): 纳米维护成熟 → 180-200岁', '### 2.3 Round 2 (T=20 to 50 years): Nano-Maintenance Matures → 180-200 years'),
    ('### 2.4 第三轮 (T=50到80年): 攻克大多数衰老模块 → 250-350岁', '### 2.4 Round 3 (T=50 to 80 years): Conquering Most Aging Modules → 250-350 years'),
    ('### 2.5 第四轮 (T=80到120年): 逃逸巩固 → 永生成为默认', '### 2.5 Round 4 (T=80 to 120 years): Escape Consolidation → Immortality Becomes Default'),
    ('### 2.6 ABC永生时间线总览', '### 2.6 ABC Immortality Timeline Overview'),
    ('## 3. ABC的100%覆盖——不是慈善，是数学', '## 3. ABC"s 100% Coverage — Not Charity, but Mathematics'),
    ('### 3.1 为什么必须100%', '### 3.1 Why 100% Is Necessary'),
    ('### 3.2 为什么ABC能做到100%而现代社会做不到', '### 3.2 Why ABC Can Achieve 100% and Modern Society Cannot'),
    ('## 4. 现代社会路径——为何是负效率', '## 4. The Modern Society Path — Why It Is Negative Efficiency'),
    ('### 4.1 四个结构性死锁', '### 4.1 Four Structural Deadlocks'),
    ('### 4.2 现代社会的"拖后腿"量化', '### 4.2 Quantifying Modern Society"s "Drag"'),
    ('### 4.3 现代社会达到逃逸速度的条件概率', '### 4.3 Conditional Probability of Modern Society Reaching Escape Velocity'),
    ('### 4.4 现代社会时间线（如果奇迹般一切顺利）', '### 4.4 Modern Society Timeline (If Everything Goes Miraculously Well)'),
    ('## 5. ABC加速因子的汇总', '## 5. Summary of ABC Acceleration Factors'),
    ('## 6. 综合对比', '## 6. Comprehensive Comparison'),
    ('## 7. "滚动永生"的哲学含义', '## 7. The Philosophical Implications of "Rolling Immortality"'),
]

src2 = os.path.join(cn_base, "E212_永生时间线_ABCvs现代社会_逃逸速度.md")
dst2 = os.path.join(en_base, "E212_Immortality_Timeline_ABC_vs_Modern_Society.md")
with open(src2, "r", encoding="utf-8") as f:
    content2 = f.read()
for old, new in MASTER:
    if old in content2: content2 = content2.replace(old, new)
rep2 = sum(1 for o,n in E212 if o in content2)
for old, new in E212:
    if old in content2: content2 = content2.replace(old, new)
cn2 = len(re.findall(r'[\u4e00-\u9fff]', content2))
with open(dst2, "w", encoding="utf-8") as f:
    f.write(content2)
print(f"E212: {cn2} CN / {len(content2)} ({round(cn2/len(content2)*100,1)}%) - {rep2} repl")
