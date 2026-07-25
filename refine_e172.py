import re, os

path = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations\Vol5_Medicine_Drugs\E172_Non_Toxic_Multi_Target_Cancer_Lockout.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# E172-specific translations - targeted at remaining Chinese paragraphs
T = [
    # Title and header
    ("SCVC 医学工程  E172  无毒多靶点cancer封杀——弱×多=强", "SCVC Medical Engineering  E172  Non-Toxic Multi-Target Cancer Lockout — Weak × Many = Strong"),
    ("【输入常数】(来自 _SCVC工程常数reference table.md 及 E168-E171)", "[Input Constants] (from _SCVC Engineering Constants Reference.md and E168-E171)"),
    
    # Core constants
    ("DNA 聚合酶速度 ≈ 50 bp/s/复制叉              (E168: S期 ~6-8 h 硬墙)", "DNA polymerase speed ≈ 50 bp/s/replication fork    (E168: S-phase ~6-8 h hard wall)"),
    ("突变率 ≈ 10⁻⁹/碱基/代                         (E169: α → H键识别能)", "Mutation rate ≈ 10⁻⁹/base/generation                (E169: α → H-bond recognition energy)"),
    ("氧扩散系数 D_O2 ≈ 2×10⁻⁹ m²/s                 (E170: Krogh 半径 ~200 μm)", "Oxygen diffusion coefficient D_O2 ≈ 2×10⁻⁹ m²/s      (E170: Krogh radius ~200 μm)"),
    ("MHC-I 正常表达 ~10⁵/细胞, NK 去抑制阈value ~20-50% (E171: 双重束缚)", "MHC-I normal expression ~10⁵/cell, NK disinhibition threshold ~20-50% (E171: double bind)"),
    ("ATP 产量: 氧化磷酸化 ~36 ATP/葡萄糖, 糖酵解 ~2 ATP/葡萄糖", "ATP yield: oxidative phosphorylation ~36 ATP/glucose, glycolysis ~2 ATP/glucose"),
    ("细胞 ATP 预算: ~10⁹ ATP/s/细胞 (典型), 分裂成本 ~10¹⁰ ATP", "Cellular ATP budget: ~10⁹ ATP/s/cell (typical), division cost ~10¹⁰ ATP"),
    ("蛋白质合成成本: ~4 ATP/氨基酸, 平均蛋白质 ~400 aa → ~1600 ATP", "Protein synthesis cost: ~4 ATP/amino acid, average protein ~400 aa → ~1600 ATP"),
    
    # Section 1
    ("1. 核心猜想: 弱×多 = 强", "1. Core Hypothesis: Weak × Many = Strong"),
    ("1.1 传统化疗的逻辑 — 及其失败", "1.1 The Logic of Traditional Chemotherapy — and Its Failure"),
    ("传统化疗 = \"找一种对癌细胞足够毒的毒素\"", 'Traditional chemotherapy = "find a toxin sufficiently poisonous to cancer cells"'),
    ("→ 必须强效 → 但癌细胞和正常细胞共享 99% 的生化机制", "→ Must be potent → but cancer cells and normal cells share 99% of biochemical machinery"),
    ("→ 强效 = 对正常细胞也毒 → 副作用 → 剂量受限", "→ Potency = toxicity to normal cells too → side effects → dose limitation"),
    ("→ 剂量受限 → 一些癌细胞存活 → 复发 + 耐药", "→ Dose limitation → some cancer cells survive → relapse + resistance"),
    ("⚫ 传统化疗的前提 (癌细胞=外来病原体) 是错的。", "⚫ The premise of traditional chemotherapy (cancer cell = foreign pathogen) is wrong."),
    ("癌细胞是\"自己人\" — 不能像抗生素杀菌那样\"地毯式轰炸\"。", 'Cancer cells are "one of us" — you cannot "carpet-bomb" them like antibiotics kill bacteria.'),
    ("1.2 SCVC 的替代逻辑", "1.2 SCVC's Alternative Logic"),
    ("E168-E171 揭示: 癌细胞必须遵守四条物理墙:", "E168-E171 reveal: cancer cells must obey four physical walls:"),
    ("墙 1 (E168): 分裂速度Ceiling ≈ 12-14 h/周期", "Wall 1 (E168): Division Speed Ceiling ≈ 12-14 h/cycle"),
    ("DNA 聚合酶 ~50 bp/s → S 期不可压缩", "DNA polymerase ~50 bp/s → S-phase incompressible"),
    ("癌细胞比正常细胞仅快 ~2×, 且不能更快", "Cancer cells only ~2× faster than normal cells, and cannot be faster"),
    ("墙 2 (E169): 突变率地板 ≈ 10⁻⁹/碱基/代", "Wall 2 (E169): Mutation Rate Floor ≈ 10⁻⁹/base/generation"),
    ("驱动突变积累需数十年 → cancer是\"时间病\"", 'Driver mutation accumulation requires decades → cancer is a "disease of time"'),
    ("但这也意味着: 癌细胞需要持续积累突变来\"适应\"", 'But this also means: cancer cells need to continuously accumulate mutations to "adapt"'),
    ("墙 3 (E170): 氧扩散墙 ≈ 200 μm", "Wall 3 (E170): Oxygen Diffusion Wall ≈ 200 μm"),
    ("无血管肿瘤 ≤ 0.01 mm³ → 血管新生是物理瓶颈", "Avascular tumor ≤ 0.01 mm³ → angiogenesis is a physical bottleneck"),
    ("血管永远追不上肿瘤 → 核心坏死是必然", "Blood vessels can never catch up to the tumor → core necrosis is inevitable"),
    ("墙 4 (E171): MHC-NK 双重束缚", "Wall 4 (E171): MHC-NK Double Bind"),
    ("高 MHC-I → T 细胞识别 → 被杀", "High MHC-I → T cell recognition → killed"),
    ("低 MHC-I → NK 细胞\"missing self\" → 被杀", 'Low MHC-I → NK cell "missing self" → killed'),
    ("逃逸窗口存在 (选择性等位基因丢失), 但需要试错时间", "Escape window exists (selective allele loss), but requires trial-and-error time"),
    ("⚫ 关键洞察: 每条墙独立施加 = 癌细胞需要独立\"绕过\"", '⚫ Key Insight: each wall applied independently = cancer cells need to independently "bypass"'),
    ("⚫ 同时紧四条墙 = 癌细胞需要同时满足四个互相矛盾的物理约束", "⚫ Tighten all four walls simultaneously = cancer cells must satisfy four mutually contradictory physical constraints"),
    ("⚫ 正常细胞不需要满足任何一个 (不分裂/不突变/不新生血管/不逃逸免疫)", "⚫ Normal cells need not satisfy any of them (not dividing / not mutating / no angiogenesis / no immune escape)"),
    ("⚫ → 治疗窗口天然巨大 — 不需要强效, 只需要多效", "⚫ → The therapeutic window is naturally enormous — you don't need potency, you need multi-efficacy"),
    
    # Section 2
    ("2. 类比 E158: 从\"15联用抗生素\"到\"4联用抗癌\"", '2. Analogy with E158: From "15-Antibiotic Combination" to "4-Drug Anticancer Combination"'),
    ("细菌耐药 (E158)         cancer多靶点 (E172)", "Bacterial Resistance (E158)         Cancer Multi-Target (E172)"),
    ("敌人          外来生物                 自己的细胞", "Enemy          Foreign organism                 Own cells"),
    ("适应机制      获取耐药基因             突变+表观+克隆选择", "Adaptation      Acquire resistance genes         Mutation + epigenetics + clonal selection"),
    
    # More comprehensive section translations
    ("耐药基因天花板 12-18 个           物理墙 4 条 (E168-E171)", "Resistance gene ceiling 12-18              Physical walls 4 (E168-E171)"),
    ("攻击策略      14类+再开发4-6种          4靶点同时+多机制", "Attack strategy  14 classes + 4-6 new          4 targets simultaneously + multi-mechanism"),
    ("结果          物理绝杀                    逃逸窗口闭合", "Outcome         Physical checkmate                   Escape window closed"),
    ("SCVC 工程常数         决定               对cancer的意义", "SCVC Engineering Constant     Determines               Significance for Cancer"),
    ("DNA 聚合酶速度 ~50 bp/s", "DNA polymerase speed ~50 bp/s"),
    ("癌细胞分裂不能快于 ~12 h/周期", "Cancer cell division cannot be faster than ~12 h/cycle"),
    ("正常干细胞更新更快 (肠道 3-5 d, 骨髓 ~数周)", "Normal stem cells renew faster (gut 3-5 d, bone marrow ~weeks)"),
    ("突变率 10⁻⁹/碱基/代", "Mutation rate 10⁻⁹/base/generation"),
    ("每个耐药突变需要 ~10⁹ 次细胞分裂 → 数月到数年", "Each resistance mutation requires ~10⁹ cell divisions → months to years"),
    ("四靶点同时需要 4 个独立耐药突变 → 4×(10⁹)² 概率 → 宇宙年龄尺度", "Four targets require 4 independent resistance mutations → 4×(10⁹)² probability → age-of-universe timescale"),
    ("O₂ 扩散系数 2×10⁻⁹ m²/s", "O₂ diffusion coefficient 2×10⁻⁹ m²/s"),
    ("抗血管生成 = 把肿瘤锁在 <0.01 mm³", "Anti-angiogenesis = lock tumor at <0.01 mm³"),
    ("MHC-I 表达调控能垒 ~0.1-0.3 eV (表观遗传)", "MHC-I expression regulation barrier ~0.1-0.3 eV (epigenetic)"),
    ("表观遗传药物可恢复 MHC-I → T 细胞可见", "Epigenetic drugs can restore MHC-I → visible to T cells"),
    ("NK 激活阈值  ~20-50% MHC-I 降低", "NK activation threshold ~20-50% MHC-I reduction"),
    ("NK engager 可杀伤低 MHC-I 细胞", "NK engagers can kill low-MHC-I cells"),
    
    # Drug specifics
    ("已上市药物, 低剂量, 四轴同时", "Already-Marketed Drugs, Low Dose, Four Axes Simultaneously"),
    ("靶点/机制", "Target/Mechanism"),
    ("作用", "Action"),
    ("SCVC 物理依据", "SCVC Physical Basis"),
    ("二甲双胍 (Metformin)", "Metformin"),
    ("线粒体 Complex I 抑制 → 降低 ATP → 压制糖酵解", "Mitochondrial Complex I inhibition → reduced ATP → suppressed glycolysis"),
    ("ATP 预算墙 (E168: 分裂成本 10¹⁰ ATP) → 饿死分裂中的癌细胞", "ATP budget wall (E168: division cost 10¹⁰ ATP) → starve dividing cancer cells"),
    ("阿司匹林 (Aspirin)", "Aspirin"),
    ("COX-2 抑制 → 降低 PGE₂ → 减少血管新生 + 抗炎", "COX-2 inhibition → reduced PGE₂ → reduced angiogenesis + anti-inflammatory"),
    ("氧扩散墙 (E170) + 炎症 → 突变率关联 (E169)", "Oxygen diffusion wall (E170) + inflammation → mutation rate coupling (E169)"),
    ("地高辛 (Digoxin)", "Digoxin"),
    ("Na⁺/K⁺-ATPase 抑制 → Ca²⁺ 升高 → 表观遗传重塑 → MHC-I 恢复", "Na⁺/K⁺-ATPase inhibition → Ca²⁺ elevation → epigenetic remodeling → MHC-I restoration"),
    ("MHC-NK 双重束缚 (E171) → 恢复 T 细胞可见性", "MHC-NK double bind (E171) → restore T-cell visibility"),
    ("心得安 (Propranolol)", "Propranolol"),
    ("β-阻断 → 降低 cAMP → 抑制应激诱导的免疫逃逸", "β-blockade → reduced cAMP → suppressed stress-induced immune escape"),
    ("MHC-NK 双重束缚 (E171) → 压制肾上腺素 → 免疫逃逸通路", "MHC-NK double bind (E171) → suppress adrenaline → immune escape pathway"),
    
    # Key sentences
    ("为什么这个组合在物理上\"不可逃逸\"？", 'Why is this combination physically "inescapable"?'),
    ("每个药独立攻击一条墙，但逃逸需要同时满足四个条件", "Each drug independently attacks one wall, but escape requires simultaneously satisfying four conditions"),
    ("这四种逃逸所需的细胞状态互相矛盾", "These four escape-required cellular states are mutually contradictory"),
    ("临床可行路径", "Clinically Feasible Pathway"),
    ("立即可以启动的临床试验设计", "Clinical Trial Design That Can Start Immediately"),
    ("Phase II 窗口试验 (可手术患者)", "Phase II Window Trial (operable patients)"),
    ("Phase II/III 晚期cancer (标准治疗失败后)", "Phase II/III Advanced Cancer (after standard treatment failure)"),
    ("Phase III 辅助治疗 (术后防复发)", "Phase III Adjuvant Therapy (post-surgery recurrence prevention)"),
    ("为什么是这四个药？—— SCVC 筛选逻辑", "Why These Four Drugs? — SCVC Selection Logic"),
    ("时间窗口", "Time Window"),
    ("耐药概率", "Resistance Probability"),
    ("SCVC 常数 → 四个药的选择不是随机的", "SCVC constants → the selection of these four drugs is not random"),
    ("有数千个已上市药物，但只有极少数同时满足", "There are thousands of marketed drugs, but very few simultaneously satisfy"),
    ("安全（低剂量可用）", "Safety (usable at low dose)"),
    ("覆盖SCVC 的 4 条物理墙", "Cover SCVC's 4 physical walls"),
    ("机制正交（不互相拮抗）", "Orthogonal mechanisms (no mutual antagonism)"),
    ("广泛可及（已过专利期）", "Broadly accessible (off-patent)"),
    ("每个墙的\"守门员\"不止一个", 'Each wall has more than one "gatekeeper"'),
    ("备用药物", "Backup Drugs"),
    ("物理终局: 为什么这是\"封杀\"而非\"治疗\"？", 'Physical Endgame: Why This Is "Lockout" Rather Than "Treatment"?'),
    ("\"治疗\"意味着敌人还在、只是被压制。\"封杀\"意味着敌人无法出现。", '"Treatment" means the enemy is still there, merely suppressed. "Lockout" means the enemy cannot emerge.'),
    ("SCVC 说: 只要四轴同时施压，耐药的概率在物理上低于人类寿命尺度。", "SCVC says: as long as all four axes are pressured simultaneously, the probability of resistance is physically below human-lifespan timescales."),
    ("这不是\"可能有curative效果\"。这是\"物理学保证curative效果\"。", 'This is not "possibly curative." This is "physically guaranteed curative."'),
    ("前提", "Prerequisites"),
    ("肿瘤负荷足够低（手术减负后）", "Tumor burden sufficiently low (after surgical debulking)"),
    ("四药同时、长期维持（类似 ART 控制 HIV）", "Four drugs simultaneously, long-term maintenance (analogous to ART controlling HIV)"),
    ("免疫系统基本完整", "Immune system basically intact"),
    ("没有已形成的耐药克隆", "No pre-existing resistant clones"),
    ("诚实局限", "Honest Limitations"),
    ("这不是\"明天就能用\"的方案 — 需要临床试验验证", 'This is not a "use it tomorrow" protocol — it requires clinical trial validation'),
    ("血脑屏障可能限制脑转移（需要单独策略）", "Blood-brain barrier may limit brain metastases (requires separate strategy)"),
    ("部分cancer类型可能需要调整药物组合（守门员替换）", "Some cancer types may require adjusted drug combinations (gatekeeper substitution)"),
    ("晚期广泛转移的cancer不在封杀范围内（肿瘤负荷过大）", "Late-stage widely metastatic cancer is outside lockout range (tumor burden too large)"),
    ("cancer 物理终局全景", "Cancer Physical Endgame Panorama"),
    ("物理常数", "Physical Constant"),
    ("对cancer的约束", "Constraint on Cancer"),
    ("工程策略", "Engineering Strategy"),
    ("封杀效果", "Lockout Effect"),
    ("分裂严格遵循 ~12 h/周期墙", "Division strictly obeys ~12 h/cycle wall"),
    ("二甲双胍 → 能量压制", "Metformin → energy suppression"),
    ("无法通过加速分裂来\"逃逸\"", 'Cannot "escape" by accelerating division'),
    ("突变需要数十年，四个靶点同时耐药的期望时间 > 10⁹ 年", "Mutations require decades; expected time for simultaneous 4-target resistance > 10⁹ years"),
    ("阿司匹林 → 抗炎 → 降低突变率", "Aspirin → anti-inflammatory → reduce mutation rate"),
    ("耐药在物理上不可能", "Resistance is physically impossible"),
    ("无血管阶段被锁在 0.01 mm³", "Avascular stage locked at 0.01 mm³"),
    ("阿司匹林 → COX-2 → 抗血管新生", "Aspirin → COX-2 → anti-angiogenesis"),
    ("肿瘤永远停留在\"临床不可见\"阶段", 'Tumor permanently stays in "clinically invisible" stage'),
    ("逃逸窗口 = MHC 矛盾 + 试错选择", "Escape window = MHC contradiction + trial-and-error selection"),
    ("地高辛 → 表观遗传 → MHC 恢复  心得安 → β阻断 → 去应激", "Digoxin → epigenetics → MHC restoration  Propranolol → β-blockade → de-stress"),
    ("逃逸窗口物理闭合", "Escape window physically closed"),
    ("总结：物理学保证的curative效果", "Summary: Physically Guaranteed Curative Effect"),
    ("SCVC的贡献不是\"发现新药\"", 'SCVC\'s contribution is not "discovering new drugs"'),
    ("SCVC的贡献是\"证明现有的四个便宜药联用 = 物理绝杀\"", 'SCVC\'s contribution is "proving that four existing cheap drugs in combination = physical checkmate"'),
    ("这不是\"可能有效\"。这是\"物理学保证有效\"。", 'This is not "possibly effective." This is "physically guaranteed effective."'),
    ("下一步: 启动临床试验。", "Next step: Initiate clinical trials."),
]

for old, new in T:
    content = content.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

# Count remaining Chinese
cn_count = len(re.findall(r'[\u4e00-\u9fff]', content))
print(f"E172 refined. Remaining Chinese: {cn_count} chars out of {len(content)}")
