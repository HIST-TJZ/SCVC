import re, os

cn_base = r"C:\Users\20606\Desktop\SCVC-github\cn\V3.0\08_工程极限\8.7_391项完整计算\卷9_末日倒计时_最后窗口_E201-E220"
en_base = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations\Vol9_Doomsday_Countdown"

# Load master
MASTER = []
with open(r"C:\Users\20606\Desktop\SCVC-github\batch_translate_v2.py", "r", encoding="utf-8") as f:
    exec_text = f.read()
start = exec_text.find("MASTER = [")
end = exec_text.find("\n\n# Files to process")
exec(exec_text[start:end])

E204 = [
    # Title
    ('# E204: SCVC生存分析 — 末日生存：为什么一个人或几个人活不了', '# E204: SCVC Survival Analysis — Doomsday Survival: Why One Person or a Few Cannot Survive'),
    ('**输入**：SCVC常数（C-C键3.6 eV、N≡N键9.8 eV、H键0.20 eV）、MVP~500-5000人、供应链接力深度、CO₂大气寿命数百年', '**Inputs**: SCVC constants (C-C bond 3.6 eV, N≡N bond 9.8 eV, H-bond 0.20 eV), MVP ~500-5,000 people, supply chain relay depth, CO₂ atmospheric lifetime of centuries'),
    ('**方法**：从SCVC物理链推导个体生存极限 + 最小技术社会门槛 + 知识衰减速率 → 证明末日生存主义的物理不可能性', '**Method**: Derive individual survival limits + minimum technological society threshold + knowledge decay rate from the SCVC physical chain → prove the physical impossibility of doomsday survivalism'),
    ('**核心命题**：文明崩塌后，个体生存是不可能的。这不是能力问题，不是意志力问题——是物理问题。C-C键不会因为你在掩体里而降低键能。N≡N键不会因为你需要化肥而降低活化能。唯一的生存方案：不让崩塌发生', '**Core Proposition**: After civilizational collapse, individual survival is impossible. This is not a question of ability or willpower — it is a question of physics. C-C bonds do not lower their bond energy just because you are in a bunker. N≡N bonds do not lower their activation energy just because you need fertilizer. The only survival plan: prevent collapse from happening'),

    # §1
    ('## §1. 个体生存的物理天花板：13.8天', '## §1. The Physical Ceiling of Individual Survival: 13.8 Days'),
    ('### 1.1 一个人能背多少？', '### 1.1 How Much Can One Person Carry?'),
    ('单人背包极限 (50 kg，强壮成年人):', 'Single-person backpack limit (50 kg, fit adult):'),
    ('最优分配: 水 41.4 kg + 食物 8.6 kg', 'Optimal allocation: water 41.4 kg + food 8.6 kg'),
    ('水消耗: 3 L/天', 'Water consumption: 3 L/day'),
    ('食物消耗: ~0.63 kg/天 (2,500 kcal ÷ 4,000 kcal/kg)', 'Food consumption: ~0.63 kg/day (2,500 kcal ÷ 4,000 kcal/kg)'),
    ('最大自持时间: 50 / (3 + 0.625) ≈ 13.8 天', 'Maximum self-sustaining time: 50 / (3 + 0.625) ≈ 13.8 days'),
    ('日行距离: ~35 km → 总活动半径: ~480 km', 'Daily travel distance: ~35 km → total activity radius: ~480 km'),
    ('分配方案', 'Allocation Plan'),
    ('水 (kg)', 'Water (kg)'),
    ('食物 (kg)', 'Food (kg)'),
    ('自持 (天)', 'Self-sustain (days)'),
    ('结局', 'Outcome'),
    ('纯水', 'Pure water'),
    ('饿死在水用完之前', 'Starve before water runs out'),
    ('纯食物', 'Pure food'),
    ('渴死在粮食吃完之前', 'Die of thirst before food runs out'),
    ('25水+25食', '25 water + 25 food'),
    ('其中之一先耗尽', 'One runs out first'),
    ('**最优**', '**Optimal**'),
    ('**同时耗尽**', '**Simultaneous depletion**'),
    ('SCVC: 人体代谢率 ~100W（基础代谢）', 'SCVC: human metabolic rate ~100W (basal metabolism)'),
    ('→ 这是 C-H/C-O 键断裂释放的化学能', '→ This is the chemical energy released by breaking C-H/C-O bonds'),
    ('→ 没有任何"不吃不喝的超人"——这是生物化学，不是意志力问题', '→ There is no "superhuman who needs no food or water" — this is biochemistry, not a willpower problem'),
    ('水源约束:', 'Water source constraint:'),
    ('地表可用水源间距: 1-50 km', 'Surface water source spacing: 1-50 km'),
    ('日行上限: ~35 km', 'Daily travel upper limit: ~35 km'),
    ('→ 如果水源间距 > 35 km → 无法在耗尽前到达 → 死亡', '→ If water source spacing > 35 km → cannot reach before depletion → death'),
    ('→ 干旱/核污染/CBRN → 可用水源归零 → 3天内死亡', '→ Drought / nuclear contamination / CBRN → zero available water → death within 3 days'),
    ('结论: 在没有补给的情况下，单人的最大生存半径是480 km，', 'Conclusion: without resupply, a single person maximum survival radius is 480 km,'),
    ('最大生存时间是13.8天。这是物理天花板。', 'maximum survival time is 13.8 days. This is the physical ceiling.'),
    ('"躲进山里靠打猎活下去"的前提是: 山里有猎物+有水源+', '"Hide in the mountains and live by hunting" presupposes: prey in the mountains + water source +'),
    ('猎物会持续出现+你不会受伤+不需要医疗。', 'prey will continue to appear + you will not get injured + you need no medical care.'),
    ('→ 所有这些前提在文明崩塌后都不成立。', '→ All of these presuppositions become false after civilizational collapse.'),

    # §2
    ('## §2. 最小技术社会：不是50人，是最少3,700人', '## §2. Minimum Technological Society: Not 50 People, but at Least 3,700'),
    ('### 2.1 你以为你需要 vs 实际需要', '### 2.1 What You Think You Need vs. What You Actually Need'),
    ('生存主义者准备了: 水、食物、弹药、种子。', 'Survivalists have prepared: water, food, ammunition, seeds.'),
    ('他们没有准备——而且一个人也准备不了的:', 'What they have not prepared — and what one person cannot prepare:'),
    ('你需要               供应链人数      为什么一个人做不了', 'What You Need         Supply Chain People    Why One Person Cannot Do It'),
    ('抗生素 (一片)         ~600 人        深层发酵+溶媒萃取+无菌分装', 'Antibiotic (one pill)  ~600 people         Deep fermentation + solvent extraction + aseptic filling'),
    ('胰岛素               ~500 人        rDNA技术+蛋白质纯化+冷链', 'Insulin               ~500 people         rDNA technology + protein purification + cold chain'),
    ('一颗子弹             ~800 人        铜矿→弹壳, 硝酸→火药, 雷汞→底火', 'One bullet            ~800 people         Copper ore → casing, nitric acid → gunpowder, mercury fulminate → primer'),
    ('一部手机            ~70,000 人      芯片光刻+显示屏+电池+摄像头', 'One mobile phone      ~70,000 people      Chip lithography + display + battery + camera'),
    ('一升柴油            ~3,700 人       勘探→采油→炼油→配送', 'One liter of diesel   ~3,700 people       Exploration → extraction → refining → distribution'),
    ('电网 (最小)          ~200-500 人     发电+输电+变电+继电保护', 'Power grid (minimum)  ~200-500 people     Generation + transmission + transformation + relay protection'),
    ('半导体 (一颗芯片)   ~50,000 人      从沙子到芯片 ~5000 道工序', 'Semiconductor (one chip) ~50,000 people   From sand to chip ~5,000 process steps'),

    # 2.2
    ('### 2.2 逐系统分解', '### 2.2 System-by-System Breakdown'),
    ('**抗生素——以青霉素为例：**', '**Antibiotics — Penicillin as an Example:**'),
    ('步骤                             专业知识              最少人数', 'Step                             Expertise              Minimum People'),
    ('菌种保存 (冷冻/PDA斜面)           微生物学              2', 'Strain preservation (freezing/PDA slant) Microbiology            2'),
    ('无菌操作                          微生物学+设备          3', 'Aseptic technique                 Microbiology + equipment 3'),
    ('发酵罐 (灭菌/温控/通气)           化学工程+机械工程      5', 'Fermenter (sterilization/temp/aeration) Chemical + mechanical eng. 5'),
    ('下游处理 (过滤/萃取/结晶)         有机化学              3', 'Downstream processing (filtration/extraction/crystallization) Organic chemistry 3'),
    ('质量控制 (效价/HPLC)              分析化学              2', 'Quality control (potency/HPLC)     Analytical chemistry    2'),
    ('分装/储存                         药剂学                2', 'Filling/storage                   Pharmaceutics           2'),
    ('原料供应 (玉米浆/乳糖)            农业+物流             10', 'Raw material supply (corn steep liquor/lactose) Agriculture + logistics 10'),
    ('能源 (电/蒸汽)                    电力工程              5', 'Energy (electricity/steam)        Power engineering       5'),
    ('水处理 (纯化水/注射用水)          水处理                3', 'Water treatment (purified/WFI)    Water treatment         3'),
    ('设备维修 (阀门/泵/管路)           机械维修              5', 'Equipment maintenance (valves/pumps/piping) Mechanical maintenance 5'),
    ('小计:                                                   ~40人', 'Subtotal:                                                ~40 people'),
    ('加上食物/住房/安保/教育/医疗:                           +60人', 'Plus food/housing/security/education/healthcare:          +60 people'),
    ('总计:                                                  ~100人 (仅抗生素!)', 'Total:                                                   ~100 people (antibiotics alone!)'),
    ('**从沙子到芯片——半导体供应链：**', '**From Sand to Chip — The Semiconductor Supply Chain:**'),
    ('阶段                    工序数    所需基础设施', 'Stage                   Process Steps  Required Infrastructure'),
    ('高纯硅 (Siemens法)       ~20      石英矿+HCl+高纯H₂', 'High-purity Si (Siemens) ~20      Quartz ore + HCl + high-purity H₂'),
    ('单晶生长 (Czochralski)   ~10      超纯坩埚+惰性气体', 'Single crystal (Czochralski) ~10  Ultra-pure crucible + inert gas'),
    ('晶圆加工 (切/磨/抛)      ~15      超精密机床+金刚石', 'Wafer processing (cut/grind/polish) ~15 Ultra-precision machines + diamond'),
    ('光刻 (DUV/EUV)           ~50      光源+光刻胶+超纯化学品', 'Lithography (DUV/EUV)    ~50      Light source + photoresist + ultra-pure chemicals'),
    ('刻蚀 (干法/湿法)         ~10      等离子体+超高纯气体', 'Etching (dry/wet)        ~10      Plasma + ultra-high-purity gases'),
    ('沉积 (CVD/PVD/ALD)       ~15      高真空+靶材+前驱气体', 'Deposition (CVD/PVD/ALD) ~15      High vacuum + targets + precursor gases'),
    ('离子注入                 ~10      加速器+掺杂气体', 'Ion implantation         ~10      Accelerator + dopant gases'),
    ('CMP (化学机械抛光)        ~5      超纯浆料+抛光垫', 'CMP (chemical mechanical polish) ~5 Ultra-pure slurry + polishing pad'),
    ('测试/封装                ~30      探针台+引线键合+塑封', 'Testing/packaging        ~30      Probe station + wire bonding + molding'),
    ('→ ~5000 道工序', '→ ~5,000 process steps'),
    ('→ ~2000-3000 种专业技术工种', '→ ~2,000-3,000 specialized technical trades'),
    ('→ 支撑总人口: ~50,000-100,000 人', '→ Supporting population: ~50,000-100,000 people'),

    # 2.3
    ('### 2.3 综合最小技术社会', '### 2.3 Composite Minimum Technological Society'),
    ('系统', 'System'),
    ('最少直接人员', 'Minimum Direct Personnel'),
    ('含家属+冗余', 'Including Dependents + Redundancy'),
    ('累积依赖', 'Cumulative Dependency'),
    ('抗生素生产', 'Antibiotic production'),
    ('电力 (最小电网)', 'Electricity (minimum grid)'),
    ('需要燃料/零件', 'Requires fuel/parts'),
    ('基础冶金 (钢/铜/铝)', 'Basic metallurgy (steel/copper/aluminum)'),
    ('需要矿石+能源', 'Requires ore + energy'),
    ('基础化工 (酸/碱/溶剂)', 'Basic chemicals (acids/bases/solvents)'),
    ('需要原料', 'Requires raw materials'),
    ('农业 (养活所有人)', 'Agriculture (feed everyone)'),
    ('需要化肥+农机', 'Requires fertilizer + machinery'),
    ('医疗 (外科+急救+公卫)', 'Healthcare (surgery + emergency + public health)'),
    ('需要药品+器械', 'Requires drugs + instruments'),
    ('水处理/卫生', 'Water treatment / sanitation'),
    ('交通/物流', 'Transport / logistics'),
    ('需要燃料', 'Requires fuel'),
    ('通信 (无线电最小)', 'Communications (minimum radio)'),
    ('需要零件', 'Requires parts'),
    ('基础教育 (下一代)', 'Basic education (next generation)'),
    ('**合计**', '**Total**'),
    ('人口级别', 'Population Level'),
    ('技术状态', 'Technological Status'),
    ('人均寿命', 'Life Expectancy'),
    ('<1,000 人  →  退回前工业时代 (铁器-青铜)      ~35-40 岁', '<1,000 people  →  Return to pre-industrial era (Iron-Bronze)  ~35-40 years'),
    ('~3,000 人  →  勉强维持基本工业 (小电网+基础医疗) ~40-50 岁', '~3,000 people  →  Barely maintain basic industry (small grid + basic healthcare) ~40-50 years'),
    ('~10,000 人 →  可维持抗生素+基础化工 (~1930年代) ~50-60 岁', '~10,000 people →  Can maintain antibiotics + basic chemicals (~1930s) ~50-60 years'),
    ('~50,000 人 →  可维持半导体+抗生素 (~1950年代)  ~60-70 岁', '~50,000 people →  Can maintain semiconductors + antibiotics (~1950s) ~60-70 years'),
    ('~100,000+  →  接近现代技术基线                     ~75-80 岁', '~100,000+ →  Near modern technological baseline                  ~75-80 years'),
    ('任何 <10,000 人的群体，必然退回到抗生素以前的医疗水平。', 'Any group of <10,000 people will inevitably regress to pre-antibiotic levels of healthcare.'),
    ('人均寿命从 80 岁降到 35-40 岁。', 'Life expectancy drops from 80 years to 35-40 years.'),
    ('每两个婴儿中有一个活不到 5 岁。', 'One out of every two infants will not live to age 5.'),
    ('阑尾炎 = 死刑。伤口感染 = 死刑。1 型糖尿病 = 几周内死亡。', 'Appendicitis = death sentence. Wound infection = death sentence. Type 1 diabetes = death within weeks.'),

    # §3
    ('## §3. 时间窗口：掩体寿命 << CO₂ 持续期', '## §3. The Time Window: Shelter Lifetime << CO₂ Persistence'),
    ('### 3.1 两边的时间尺度', '### 3.1 The Two Time Scales'),
    ('CO₂ 大气寿命 (脉冲衰减):', 'CO₂ atmospheric lifetime (pulse decay):'),
    ('10 年后:    85% 残留 — 地表仍可居住 (如果有文明)', 'After 10 years:   85% remains — surface still habitable (if civilization exists)'),
    ('50 年后:    60% 残留 — 掩体设计寿命上限', 'After 50 years:   60% remains — shelter design lifetime ceiling'),
    ('100 年后:   40% 残留 — 一切人造物开始全面腐蚀', 'After 100 years:  40% remains — all man-made objects begin comprehensive corrosion'),
    ('200 年后:   30% 残留 — 地貌改变', 'After 200 years:  30% remains — landscape alteration'),
    ('500 年后:   22% 残留 — 海平面仍在上升', 'After 500 years:  22% remains — sea level still rising'),
    ('1000 年后:  18% 残留 — 地质时间尺度', 'After 1,000 years: 18% remains — geological timescale'),
    ('掩体系统故障率 (MTBF, 崩塌后无替换件的实际寿命):', 'Shelter system failure rates (MTBF, actual lifetime without replacement parts after collapse):'),
    ('组件              MTBF     崩塌后实际    能维修吗?', 'Component           MTBF     Post-Collapse Actual   Repairable?'),
    ('HEPA 过滤器        1-3 年    ~2 年        否 (需工厂)', 'HEPA filter         1-3 yr    ~2 yr         No (requires factory)'),
    ('水泵               5-10 年    ~3 年        部分', 'Water pump          5-10 yr   ~3 yr         Partially'),
    ('柴油发电机         5-15 年    ~3 年        部分', 'Diesel generator    5-15 yr   ~3 yr         Partially'),
    ('太阳能板          20-30 年   ~15 年        否 (需半导体)', 'Solar panel         20-30 yr  ~15 yr        No (requires semiconductors)'),
    ('电池 (铅酸)        3-5 年     ~3 年        否', 'Battery (lead-acid) 3-5 yr    ~3 yr         No'),
    ('电池 (锂)          5-10 年    ~5 年        否', 'Battery (lithium)   5-10 yr   ~5 yr         No'),
    ('电路板/控制器     10-20 年    ~5 年        否 (需半导体)', 'Circuit board/controller 10-20 yr ~5 yr     No (requires semiconductors)'),
    ('混凝土结构        50-100 年   ~30 年       部分', 'Concrete structure  50-100 yr ~30 yr        Partially'),
    ('金属管道/阀门     20-50 年    ~10 年(腐蚀) 部分', 'Metal pipes/valves  20-50 yr  ~10 yr (corrosion) Partially'),
    ('致命的不等式:', 'The Fatal Inequality:'),
    ('掩体最脆弱组件 (泵/过滤器/电池) 寿命:   ~2-5 年', 'Most fragile shelter component (pump/filter/battery) lifetime: ~2-5 years'),
    ('掩体最可靠组件 (太阳能板) 寿命:         ~15-20 年', 'Most reliable shelter component (solar panels) lifetime:     ~15-20 years'),
    ('CO₂ 地表不适宜的最短持续期:            >100 年', 'Minimum duration of CO₂ surface uninhabitability:            >100 years'),
    ('CO₂ 海平面上升的持续期:                数百年-数千年', 'Duration of CO₂ sea-level rise:                             centuries to millennia'),
    ('→ 掩体寿命 << CO₂ 持续期', '→ Shelter lifetime << CO₂ persistence'),
    ('→ 掩体的每一个组件都会在崩塌结束前失效', '→ Every component of the shelter will fail before the collapse ends'),
    ('→ 没有工业文明 → 没有替换件 → 掩体 = 棺材', '→ No industrial civilization → no replacement parts → shelter = coffin'),
    ('→ 掩体是延长死亡，不是生存方案', '→ A shelter prolongs death; it is not a survival plan'),
    ('SCVC的残酷数学:', 'SCVC Brutal Mathematics:'),
    ('唯一真正可持续的"掩体"就是地球生态系统本身。', 'The only truly sustainable "shelter" is the Earth ecosystem itself.'),
    ('唯一真正可替换的"组件"就是活着的人类文明。', 'The only truly replaceable "component" is a living human civilization.'),

    # Continue with remaining sections...
    ('## §4. 知识熵增：文明的不可逆遗忘', '## §4. Knowledge Entropy: The Irreversible Forgetting of Civilization'),
    ('### 4.1 存储介质——全都短命', '### 4.1 Storage Media — All Short-Lived'),
    ('介质              物理寿命        崩后实际', 'Medium              Physical Lifetime    Post-Collapse Actual'),
    ('人脑 (专家)        ~70 年         ~40 年 (压力↑寿命↓)', 'Human brain (expert) ~70 yr         ~40 yr (stress ↑ lifetime ↓)'),
    ('→ 死亡 = 知识永久消失', '→ Death = permanent loss of knowledge'),
    ('纸张/书籍          ~100-500 年    ~50 年 (火灾/潮湿/虫蛀)', 'Paper/books         ~100-500 yr    ~50 yr (fire/moisture/insects)'),
    ('硬盘 (HDD)         ~5-10 年       ~3 年 (无温控=磁畴衰减)', 'Hard drive (HDD)    ~5-10 yr       ~3 yr (no temp control = magnetic domain decay)'),
    ('固态硬盘 (SSD)     ~5-10 年       ~3 年 (浮栅电荷泄漏)', 'SSD                 ~5-10 yr       ~3 yr (floating gate charge leakage)'),
    ('光盘 (CD/DVD)      ~20-100 年     ~15 年 (染料降解)', 'Optical disc (CD/DVD) ~20-100 yr   ~15 yr (dye degradation)'),
    ('磁带               ~10-30 年      ~5 年', 'Magnetic tape       ~10-30 yr      ~5 yr'),
    ('→ 所有数字存储介质在 3-15 年内失效', '→ All digital storage media fail within 3-15 years'),
    ('→ 之后只能依赖纸张和口传', '→ Thereafter only paper and oral transmission remain'),
    ('### 4.2 代际知识衰减', '### 4.2 Intergenerational Knowledge Decay'),
    ('代际知识衰减模型 (每代丢失 ~35%):', 'Intergenerational knowledge decay model (~35% loss per generation):'),
    ('第 1 代 (25 年后):   65.0% — 仍可维持基本工业', 'Gen 1 (after 25 yr):  65.0% — can still maintain basic industry'),
    ('第 2 代 (50 年后):   42.3% — 退回铁器时代水平', 'Gen 2 (after 50 yr):  42.3% — regress to Iron Age level'),
    ('第 3 代 (75 年后):   27.4% — 退回青铜时代', 'Gen 3 (after 75 yr):  27.4% — regress to Bronze Age'),
    ('第 4 代 (100 年后):  17.9% — 犁耕农业', 'Gen 4 (after 100 yr): 17.9% — plow agriculture'),
    ('第 5 代 (125 年后):  11.6% — 口传铁器技术', 'Gen 5 (after 125 yr): 11.6% — orally transmitted iron technology'),
    ('第 6 代 (150 年后):   7.5% — 退回石器时代', 'Gen 6 (after 150 yr):  7.5% — regress to Stone Age'),
    ('第一代就永久丢失的知识:', 'Knowledge permanently lost in the first generation:'),
    ('→ 半导体制造 (需数千人协作 + ~5000 道工序)', '→ Semiconductor manufacturing (requires thousands collaborating + ~5,000 process steps)'),
    ('→ 抗生素合成 (需有机化学知识 + 菌种保藏)', '→ Antibiotic synthesis (requires organic chemistry knowledge + strain preservation)'),
    ('→ 电网维护 (需继电保护 + 电力电子)', '→ Power grid maintenance (requires relay protection + power electronics)'),
    ('→ Haber-Bosch 合成氨 (高温高压催化参数无人记得)', '→ Haber-Bosch ammonia synthesis (high-temperature high-pressure catalytic parameters remembered by no one)'),
    ('→ 疫苗生产 (细胞培养 + 病毒灭活 → 极其脆弱)', '→ Vaccine production (cell culture + viral inactivation → extremely fragile)'),
    ('SCVC: 知识的退化和碳键的退化一样不可逆。', 'SCVC: The degradation of knowledge is as irreversible as the degradation of carbon bonds.'),
    ('你不能"重新发现"抗生素——你需要活着的人记得怎么做。', 'You cannot "rediscover" antibiotics — you need living people who remember how to make them.'),
    ('而这些人在崩塌的第一代就死了。', 'And those people die in the first generation of collapse.'),

    # §5
    ('## §5. 基因瓶颈：50个人 → 三代内崩溃', '## §5. The Genetic Bottleneck: 50 People → Collapse Within Three Generations'),
    ('### 5.1 最小可存活种群 (MVP)', '### 5.1 Minimum Viable Population (MVP)'),
    ('50 人:  短期 (1-2代) 避免近亲繁殖的下限', '50 people:  short-term (1-2 generations) lower limit to avoid inbreeding'),
    ('→ 严重近交衰退 → 隐性遗传病爆发', '→ Severe inbreeding depression → outbreak of recessive genetic disorders'),
    ('→ 长期不可行', '→ Long-term non-viable'),
    ('500 人: 维持遗传多样性的长期下限', '500 people: long-term lower limit to maintain genetic diversity'),
    ('→ 随机遗传漂变 → 有害等位基因频率上升', '→ Random genetic drift → harmful allele frequencies rise'),
    ('→ 勉强可行, 但社会结构脆弱', '→ Barely viable, but social structure fragile'),

    # §6  
    ('## §6. 供应链接力：你 = 10 万人的最后一棒', '## §6. The Supply Chain Relay: You = the Last Baton of 100,000 People'),
    
    # §7
    ('## §7. 崩塌数学：为什么没有"部分崩塌"', '## §7. Collapse Mathematics: Why There Is No "Partial Collapse"'),

    # §8
    ('## §8. SCVC的残酷结论', '## §8. The Brutal Conclusion of SCVC'),
    ('### 8.1 末日生存主义的四个物理谬误', '### 8.1 The Four Physical Fallacies of Doomsday Survivalism'),
    ('### 8.2 唯一的生存方案', '### 8.2 The Only Survival Plan'),
    ('SCVC 不提供"末日怎么活"的指南。', 'SCVC does not provide a guide for "how to survive the apocalypse."'),
    ('因为 SCVC 的物理结论是: 末日之后，活着是不可能的。', 'Because the physical conclusion of SCVC is: after the apocalypse, survival is impossible.'),
    ('这不是能力问题。不是意志力问题。', 'This is not a question of ability. Not a question of willpower.'),
    ('是物理问题。', 'It is a question of physics.'),
    ('C-C 键 3.6 eV — 不会因为你在掩体里而变成 2.0 eV。', 'C-C bond 3.6 eV — it will not become 2.0 eV just because you are in a bunker.'),
    ('N≡N 键 9.8 eV — 不会因为你需要化肥而降低活化能。', 'N≡N bond 9.8 eV — it will not lower its activation energy just because you need fertilizer.'),
    ('芯片需要 EUV 光刻 — 一个人做不了光刻机。', 'Chips require EUV lithography — one person cannot build a lithography machine.'),
    ('青霉素需要无菌发酵 — 一个人做不了发酵罐。', 'Penicillin requires aseptic fermentation — one person cannot build a fermenter.'),
    ('每一个现代人 = 10 万人的供应链接力的最后一棒。', 'Every modern person = the last baton in a 100,000-person supply chain relay.'),
    ('断裂了就是断裂了。', 'When it breaks, it is broken.'),
    ('短期的混乱可以熬 (数周到数月)。', 'Short-term chaos can be endured (weeks to months).'),
    ('长期的崩塌 (数百年 CO₂ + 海平面上升) → 不可熬。', 'Long-term collapse (centuries of CO₂ + sea-level rise) → cannot be endured.'),
    ('唯一的生存方案: 不让崩塌发生。', 'The only survival plan: prevent collapse from happening.'),
    ('E202 画出了管控红线。E203 画出了替代路径。', 'E202 draws the management red lines. E203 draws the alternative path.'),
    ('在还剩 ~20 年碳预算的时候，', 'While ~20 years of carbon budget remain,'),
    ('强迫所有人合作。', 'force everyone to cooperate.'),
    ('"末日准备"不是挖掩体。', '"Doomsday preparation" is not digging bunkers.'),
    ('"末日准备"是确保人类永远不会需要掩体。', '"Doomsday preparation" is ensuring humanity will never need bunkers.'),
    ('这是 SCVC 能给出的最诚实的回答。', 'This is the most honest answer SCVC can give.'),

    # Appendices
    ('## 附录A：本次使用的SCVC常数', '## Appendix A: SCVC Constants Used in This Document'),
    ('塑料/有机分子的稳定性 → 一个人无法合成的材料', 'Stability of plastics/organic molecules → materials one person cannot synthesize'),
    ('固氮的能量代价 → 化肥的工业必需性', 'Energy cost of nitrogen fixation → industrial necessity of fertilizer'),
    ('蛋白质折叠 → 抗生素/胰岛素的结构基础', 'Protein folding → structural basis of antibiotics/insulin'),
    ('CO₂ 稳定 → 大气寿命数百年', 'CO₂ stability → atmospheric lifetime of centuries'),
    ('人体代谢率', 'Human metabolic rate'),
    ('基础代谢 → 最低食物/水需求', 'Basal metabolism → minimum food/water requirements'),
    ('遗传多样性的物理下限', 'Physical lower limit of genetic diversity'),
    ('## 附录B：关键公式速查', '## Appendix B: Key Formula Quick Reference'),
    ('个体自持时间:    T_max = M_carry / (r_water + r_food)', 'Individual self-sustain time:  T_max = M_carry / (r_water + r_food)'),
    ('代际知识留存:    K_n = K_0 × (1 − δ)^n', 'Intergenerational knowledge retention: K_n = K_0 × (1 − δ)^n'),
    ('δ ≈ 0.35, n = 25 年/代', 'δ ≈ 0.35, n = 25 years/generation'),
    ('掩体可行性:      τ_shelter ≈ 2-20 年 (组件级)', 'Shelter feasibility:    τ_shelter ≈ 2-20 years (component-level)'),
    ('τ_CO2 ≈ 100-1000 年', 'τ_CO2 ≈ 100-1,000 years'),
    ('τ_shelter << τ_CO2 → 不可行', 'τ_shelter << τ_CO2 → non-viable'),
    ('最小技术社会:    N_min ≈ Σ(每个技术系统的最低人数) × 冗余因子', 'Minimum technological society: N_min ≈ Σ(minimum people per technical system) × redundancy factor'),
    ('N_min ≈ 1,160 × 3.2 ≈ 3,700 人 (最小)', 'N_min ≈ 1,160 × 3.2 ≈ 3,700 people (minimum)'),
    ('N_semiconductor ≈ 50,000-100,000 人 (现代基线)', 'N_semiconductor ≈ 50,000-100,000 people (modern baseline)'),
    ('本文档从SCVC常数出发，严格证明末日生存主义是物理上不可能的错误信念。供应链接力深度 = 数万到数十万人/个体。掩体寿命 (2-20年) << CO₂持续期 (>100年)。知识衰减 (~35%/代) > 代际传递。基因瓶颈在 50 人中三代内导致灭绝。唯一的生存方案: 不让崩塌发生。这不是意识形态——这是物理常数的最后通牒。', 'This document rigorously proves from SCVC constants that doomsday survivalism is a physically impossible false belief. Supply chain relay depth = tens to hundreds of thousands of people per individual. Shelter lifetime (2-20 years) << CO₂ persistence (>100 years). Knowledge decay (~35%/generation) exceeds intergenerational transmission. Genetic bottleneck in 50 people leads to extinction within three generations. The only survival plan: prevent collapse from happening. This is not ideology — it is the ultimatum of physical constants.'),
]

# Apply
src_path = os.path.join(cn_base, "E204_末日生存不可能.md")
dst_path = os.path.join(en_base, "E204_Doomsday_Survival_Impossible.md")

with open(src_path, "r", encoding="utf-8") as f:
    content = f.read()

for old, new in MASTER:
    if old in content:
        content = content.replace(old, new)

replaced = 0
for old, new in E204:
    if old in content:
        content = content.replace(old, new)
        replaced += 1

cn = len(re.findall(r'[\u4e00-\u9fff]', content))
with open(dst_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"E204: {cn} CN / {len(content)} total ({round(cn/len(content)*100,1)}%) - {replaced} replacements")
