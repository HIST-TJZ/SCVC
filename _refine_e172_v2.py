import re, os

path = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations\Vol5_Medicine_Drugs\E172_Non_Toxic_Multi_Target_Cancer_Lockout.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Paragraph-level translations for the remaining Chinese
para_translations = [
    # Section 1
    ("1. 核心猜想: 弱\u00d7多 = 强", "1. Core Hypothesis: Weak \u00d7 Many = Strong"),
    ("1.1 传统化疗的逻辑 \u2014 及其失败", "1.1 The Logic of Traditional Chemotherapy \u2014 and Its Failure"),
    ("1.2 SCVC 的替代逻辑", "1.2 SCVC\u2019s Alternative Logic"),
    
    # Section 2
    ("2. 类比 E158: 从\u201c15联用抗生素\u201d到\u201c4联用抗癌\u201d", '2. Analogy with E158: From \u201c15-Antibiotic Combination\u201d to \u201c4-Drug Anticancer Combination\u201d'),
    
    # Section 3
    ("3. 四个药 \u2014 每个为什么、在哪个墙", "3. The Four Drugs \u2014 Why Each One, at Which Wall"),
    ("3.1 二甲双胍 (Metformin) \u2014 攻击墙1 (ATP/能量墙)", "3.1 Metformin \u2014 Attacks Wall 1 (ATP / Energy Wall)"),
    ("3.2 阿司匹林 (Aspirin) \u2014 攻击墙2+3 (突变率 + 血管新生)", "3.2 Aspirin \u2014 Attacks Walls 2+3 (Mutation Rate + Angiogenesis)"),
    ("3.3 地高辛 (Digoxin) \u2014 攻击墙4 (MHC-I 表观遗传恢复)", "3.3 Digoxin \u2014 Attacks Wall 4 (MHC-I Epigenetic Restoration)"),
    ("3.4 心得安 (Propranolol) \u2014 攻击墙4 (免疫逃逸的肾上腺素轴)", "3.4 Propranolol \u2014 Attacks Wall 4 (Adrenergic Axis of Immune Escape)"),
    
    # Section 4
    ("4. ATP 危机 \u2014 四联的物理交汇点", "4. The ATP Crisis \u2014 Physical Convergence Point of the Four-Drug Combination"),
    ("4.1 正常细胞 vs 癌细胞的 ATP 预算", "4.1 ATP Budget: Normal Cells vs. Cancer Cells"),
    ("4.2 四联如何制造 ATP 赤字", "4.2 How the Four-Drug Combination Creates an ATP Deficit"),
    
    # Section 5
    ("5. 耐药概率 \u2014 为什么四联=物理绝杀", "5. Resistance Probability \u2014 Why Four Drugs = Physical Checkmate"),
    ("5.1 单药耐药的时间线", "5.1 Single-Drug Resistance Timeline"),
    ("5.2 联合耐药的组合爆炸", "5.2 Combinatorial Explosion of Multi-Drug Resistance"),
    
    # Section 6
    ("6. 低剂量策略 \u2014 颠覆\u201c最大耐受剂量\u201d范式", '6. The Low-Dose Strategy \u2014 Subverting the \u201cMaximum Tolerated Dose\u201d Paradigm'),
    ("6.1 为什么低剂量反而更强？", "6.1 Why Is Low Dose Actually Stronger?"),
    ("6.2 多墙耐受 \u2014 最大的风险，但被锁死", "6.2 Multi-Wall Tolerance \u2014 The Greatest Risk, But Locked Down"),
    
    # Section 7
    ("7. SCVC 结论 \u2014 \u201c弱\u00d7多=强\u201d的物理基础", '7. SCVC Conclusion \u2014 The Physical Foundation of \u201cWeak \u00d7 Many = Strong\u201d'),
    
    # Final block
    ("E172 结论", "E172 Conclusion"),
    
    # Remaining scattered Chinese phrases
    ("\u764c\u7ec6\u80de\u5206\u88c2\u4e0d\u80fd\u5feb\u4e8e ~12 h/\u5468\u671f", "Cancer cell division cannot be faster than ~12 h/cycle"),
    ("\u6b63\u5e38\u5e72\u7ec6\u80de\u66f4\u65b0\u66f4\u5feb (\u80a0\u9053 3-5 d, \u9aa8\u9ac4 ~\u6570\u5468)", "Normal stem cells renew faster (gut 3-5 d, bone marrow ~weeks)"),
    ("\u6bcf\u4e2a\u8010\u836f\u7a81\u53d8\u9700\u8981 ~10\u2079 \u6b21\u7ec6\u80de\u5206\u88c2 \u2192 \u6570\u6708\u5230\u6570\u5e74", "Each resistance mutation requires ~10\u2079 cell divisions \u2192 months to years"),
    ("\u56db\u9776\u70b9\u540c\u65f6\u9700\u8981 4 \u4e2a\u72ec\u7acb\u8010\u836f\u7a81\u53d8 \u2192 4\u00d7(10\u2079)\u00b2 \u6982\u7387 \u2192 \u5b87\u5b99\u5e74\u9f84\u5c3a\u5ea6", "Four targets require 4 independent resistance mutations \u2192 4\u00d7(10\u2079)\u00b2 probability \u2192 age-of-universe timescale"),
    ("\u6297\u8840\u7ba1\u65b0\u751f = \u628a\u80bf\u7624\u9501\u5728 <0.01 mm\u00b3", "Anti-angiogenesis = lock tumor at <0.01 mm\u00b3"),
    ("\u8868\u89c2\u9057\u4f20\u836f\u7269\u53ef\u6062\u590d MHC-I \u2192 T \u7ec6\u80de\u53ef\u89c1", "Epigenetic drugs can restore MHC-I \u2192 visible to T cells"),
    ("NK engager \u53ef\u6740\u4f24\u4f4e MHC-I \u7ec6\u80de", "NK engagers can kill low-MHC-I cells"),
    ("\u5df2\u4e0a\u5e02\u836f\u7269, \u4f4e\u5242\u91cf, \u56db\u8f74\u540c\u65f6", "Already-Marketed Drugs, Low Dose, Four Axes Simultaneously"),
    ("\u9776\u70b9/\u673a\u5236", "Target/Mechanism"),
    ("\u4f5c\u7528", "Action"),
    ("SCVC \u7269\u7406\u4f9d\u636e", "SCVC Physical Basis"),
    ("\u4e8c\u7532\u53cc\u80cd (Metformin)", "Metformin"),
    ("\u7ebf\u7c92\u4f53 Complex I \u6291\u5236 \u2192 \u964d\u4f4e ATP \u2192 \u538b\u5236\u7cd6\u9175\u89e3", "Mitochondrial Complex I inhibition \u2192 reduced ATP \u2192 suppressed glycolysis"),
    ("ATP \u9884\u7b97\u5899 (E168: \u5206\u88c2\u6210\u672c 10\u00b9\u2070 ATP) \u2192 \u997f\u6b7b\u5206\u88c2\u4e2d\u7684\u764c\u7ec6\u80de", "ATP budget wall (E168: division cost 10\u00b9\u2070 ATP) \u2192 starve dividing cancer cells"),
    ("\u963f\u53f8\u5339\u6797 (Aspirin)", "Aspirin"),
    ("COX-2 \u6291\u5236 \u2192 \u964d\u4f4e PGE\u2082 \u2192 \u51cf\u5c11\u8840\u7ba1\u65b0\u751f + \u6297\u708e", "COX-2 inhibition \u2192 reduced PGE\u2082 \u2192 reduced angiogenesis + anti-inflammatory"),
    ("\u6c27\u6269\u6563\u5899 (E170) + \u708e\u75c7 \u2192 \u7a81\u53d8\u7387\u5173\u8054 (E169)", "Oxygen diffusion wall (E170) + inflammation \u2192 mutation rate coupling (E169)"),
    ("\u5730\u9ad8\u8f9b (Digoxin)", "Digoxin"),
    ("Na\u207a/K\u207a-ATPase \u6291\u5236 \u2192 Ca\u00b2\u207a \u5347\u9ad8 \u2192 \u8868\u89c2\u9057\u4f20\u91cd\u5851 \u2192 MHC-I \u6062\u590d", "Na\u207a/K\u207a-ATPase inhibition \u2192 Ca\u00b2\u207a elevation \u2192 epigenetic remodeling \u2192 MHC-I restoration"),
    ("MHC-NK \u53cc\u91cd\u675f\u7f1a (E171) \u2192 \u6062\u590d T \u7ec6\u80de\u53ef\u89c1\u6027", "MHC-NK double bind (E171) \u2192 restore T-cell visibility"),
    ("\u5fc3\u5f97\u5b89 (Propranolol)", "Propranolol"),
    ("\u03b2-\u963b\u65ad \u2192 \u964d\u4f4e cAMP \u2192 \u6291\u5236\u5e94\u6fc0\u8bf1\u5bfc\u7684\u514d\u75ab\u9003\u9038", "\u03b2-blockade \u2192 reduced cAMP \u2192 suppressed stress-induced immune escape"),
    ("MHC-NK \u53cc\u91cd\u675f\u7f1a (E171) \u2192 \u538b\u5236\u80be\u4e0a\u817a\u7d20 \u2192 \u514d\u75ab\u9003\u9038\u901a\u8def", "MHC-NK double bind (E171) \u2192 suppress adrenaline \u2192 immune escape pathway"),
    
    # Key rationale sentences
    ("\u4e3a\u4ec0\u4e48\u8fd9\u4e2a\u7ec4\u5408\u5728\u7269\u7406\u4e0a\u201c\u4e0d\u53ef\u9003\u9038\u201d\uff1f", '\u201cWhy is this combination physically \u201cinescapable\u201d?'),
    ("\u6bcf\u4e2a\u836f\u72ec\u7acb\u653b\u51fb\u4e00\u6761\u5899\uff0c\u4f46\u9003\u9038\u9700\u8981\u540c\u65f6\u6ee1\u8db3\u56db\u4e2a\u6761\u4ef6", "Each drug independently attacks one wall, but escape requires simultaneously satisfying four conditions"),
    ("\u8fd9\u56db\u79cd\u9003\u9038\u6240\u9700\u7684\u7ec6\u80de\u72b6\u6001\u4e92\u76f8\u77db\u76fe", "These four escape-required cellular states are mutually contradictory"),
    ("\u4e34\u5e8a\u53ef\u884c\u8def\u5f84", "Clinically Feasible Pathway"),
    ("\u7acb\u5373\u53ef\u4ee5\u542f\u52a8\u7684\u4e34\u5e8a\u8bd5\u9a8c\u8bbe\u8ba1", "Clinical Trial Design That Can Start Immediately"),
    ("Phase II \u7a97\u53e3\u8bd5\u9a8c (\u53ef\u624b\u672f\u60a3\u8005)", "Phase II Window Trial (operable patients)"),
    ("Phase II/III \u665a\u671fcancer (\u6807\u51c6\u6cbb\u7597\u5931\u8d25\u540e)", "Phase II/III Advanced Cancer (after standard treatment failure)"),
    ("Phase III \u8f85\u52a9\u6cbb\u7597 (\u672f\u540e\u9632\u590d\u53d1)", "Phase III Adjuvant Therapy (post-surgery recurrence prevention)"),
    ("\u4e3a\u4ec0\u4e48\u662f\u8fd9\u56db\u4e2a\u836f\uff1f\u2014\u2014 SCVC \u7b5b\u9009\u903b\u8f91", "Why These Four Drugs? \u2014 SCVC Selection Logic"),
    ("\u65f6\u95f4\u7a97\u53e3", "Time Window"),
    ("\u8010\u836f\u6982\u7387", "Resistance Probability"),
    ("SCVC \u5e38\u6570 \u2192 \u56db\u4e2a\u836f\u7684\u9009\u62e9\u4e0d\u662f\u968f\u673a\u7684", "SCVC constants \u2192 the selection of these four drugs is not random"),
    ("\u6709\u6570\u5343\u4e2a\u5df2\u4e0a\u5e02\u836f\u7269\uff0c\u4f46\u53ea\u6709\u6781\u5c11\u6570\u540c\u65f6\u6ee1\u8db3", "There are thousands of marketed drugs, but very few simultaneously satisfy"),
    ("\u5b89\u5168\uff08\u4f4e\u5242\u91cf\u53ef\u7528\uff09", "Safety (usable at low dose)"),
    ("\u8986\u76d6SCVC \u7684 4 \u6761\u7269\u7406\u5899", "Cover SCVC\u2019s 4 physical walls"),
    ("\u673a\u5236\u6b63\u4ea4\uff08\u4e0d\u4e92\u76f8\u62ee\u6297\uff09", "Orthogonal mechanisms (no mutual antagonism)"),
    ("\u5e7f\u6cdb\u53ef\u53ca\uff08\u5df2\u8fc7\u4e13\u5229\u671f\uff09", "Broadly accessible (off-patent)"),
    ("\u6bcf\u4e2a\u5899\u7684\u201c\u5b88\u95e8\u5458\u201d\u4e0d\u6b62\u4e00\u4e2a", '\u201cEach wall has more than one \u201cgatekeeper\u201d'),
    ("\u5907\u7528\u836f\u7269", "Backup Drugs"),
    ("\u7269\u7406\u7ec8\u5c40: \u4e3a\u4ec0\u4e48\u8fd9\u662f\u201c\u5c01\u6740\u201d\u800c\u975e\u201c\u6cbb\u7597\u201d\uff1f", '\u201cPhysical Endgame: Why Is This \u201cLockout\u201d Rather Than \u201cTreatment\u201d?'),
    ("\u201c\u6cbb\u7597\u201d\u610f\u5473\u7740\u654c\u4eba\u8fd8\u5728\u3001\u53ea\u662f\u88ab\u538b\u5236\u3002\u201c\u5c01\u6740\u201d\u610f\u5473\u7740\u654c\u4eba\u65e0\u6cd5\u51fa\u73b0\u3002", '\u201c\u201cTreatment\u201d means the enemy is still there, merely suppressed. \u201cLockout\u201d means the enemy cannot emerge.'),
    ("SCVC \u8bf4: \u53ea\u8981\u56db\u8f74\u540c\u65f6\u65bd\u538b\uff0c\u8010\u836f\u7684\u6982\u7387\u5728\u7269\u7406\u4e0a\u4f4e\u4e8e\u4eba\u7c7b\u5bff\u547d\u5c3a\u5ea6\u3002", "SCVC says: as long as all four axes are pressured simultaneously, the probability of resistance is physically below human-lifespan timescales."),
    ("\u8fd9\u4e0d\u662f\u201c\u53ef\u80fd\u6709curative\u6548\u679c\u201d\u3002\u8fd9\u662f\u201c\u7269\u7406\u5b66\u4fdd\u8bc1curative\u6548\u679c\u201d\u3002", '\u201cThis is not \u201cpossibly curative.\u201d This is \u201cphysically guaranteed curative.\u201d'),
    ("\u524d\u63d0", "Prerequisites"),
    ("\u80bf\u7624\u8d1f\u8377\u8db3\u591f\u4f4e\uff08\u624b\u672f\u51cf\u8d1f\u540e\uff09", "Tumor burden sufficiently low (after surgical debulking)"),
    ("\u56db\u836f\u540c\u65f6\u3001\u957f\u671f\u7ef4\u6301\uff08\u7c7b\u4f3c ART \u63a7\u5236 HIV\uff09", "Four drugs simultaneously, long-term maintenance (analogous to ART controlling HIV)"),
    ("\u514d\u75ab\u7cfb\u7edf\u57fa\u672c\u5b8c\u6574", "Immune system basically intact"),
    ("\u6ca1\u6709\u5df2\u5f62\u6210\u7684\u8010\u836f\u514b\u9686", "No pre-existing resistant clones"),
    ("\u8bda\u5b9e\u5c40\u9650", "Honest Limitations"),
    ("\u8fd9\u4e0d\u662f\u201c\u660e\u5929\u5c31\u80fd\u7528\u201d\u7684\u65b9\u6848 \u2014 \u9700\u8981\u4e34\u5e8a\u8bd5\u9a8c\u9a8c\u8bc1", '\u201cThis is not a \u201cuse it tomorrow\u201d protocol \u2014 it requires clinical trial validation'),
    ("\u8840\u8111\u5c4f\u969c\u53ef\u80fd\u9650\u5236\u8111\u8f6c\u79fb\uff08\u9700\u8981\u5355\u72ec\u7b56\u7565\uff09", "Blood-brain barrier may limit brain metastases (requires separate strategy)"),
    ("\u90e8\u5206cancer\u7c7b\u578b\u53ef\u80fd\u9700\u8981\u8c03\u6574\u836f\u7269\u7ec4\u5408\uff08\u5b88\u95e8\u5458\u66ff\u6362\uff09", "Some cancer types may require adjusted drug combinations (gatekeeper substitution)"),
    ("\u665a\u671f\u5e7f\u6cdb\u8f6c\u79fb\u7684cancer\u4e0d\u5728\u5c01\u6740\u8303\u56f4\u5185\uff08\u80bf\u7624\u8d1f\u8377\u8fc7\u5927\uff09", "Late-stage widely metastatic cancer is outside lockout range (tumor burden too large)"),
    ("cancer \u7269\u7406\u7ec8\u5c40\u5168\u666f", "Cancer Physical Endgame Panorama"),
    ("\u7269\u7406\u5e38\u6570", "Physical Constant"),
    ("\u5bf9cancer\u7684\u7ea6\u675f", "Constraint on Cancer"),
    ("\u5de5\u7a0b\u7b56\u7565", "Engineering Strategy"),
    ("\u5c01\u6740\u6548\u679c", "Lockout Effect"),
    ("\u5206\u88c2\u4e25\u683c\u9075\u5faa ~12 h/\u5468\u671f\u5899", "Division strictly obeys ~12 h/cycle wall"),
    ("\u4e8c\u7532\u53cc\u80cd \u2192 \u80fd\u91cf\u538b\u5236", "Metformin \u2192 energy suppression"),
    ("\u65e0\u6cd5\u901a\u8fc7\u52a0\u901f\u5206\u88c2\u6765\u201c\u9003\u9038\u201d", '\u201cCannot \u201cescape\u201d by accelerating division'),
    ("\u7a81\u53d8\u9700\u8981\u6570\u5341\u5e74\uff0c\u56db\u4e2a\u9776\u70b9\u540c\u65f6\u8010\u836f\u7684\u671f\u671b\u65f6\u95f4 > 10\u2079 \u5e74", "Mutations require decades; expected time for simultaneous 4-target resistance > 10\u2079 years"),
    ("\u963f\u53f8\u5339\u6797 \u2192 \u6297\u708e \u2192 \u964d\u4f4e\u7a81\u53d8\u7387", "Aspirin \u2192 anti-inflammatory \u2192 reduce mutation rate"),
    ("\u8010\u836f\u5728\u7269\u7406\u4e0a\u4e0d\u53ef\u80fd", "Resistance is physically impossible"),
    ("\u65e0\u8840\u7ba1\u9636\u6bb5\u88ab\u9501\u5728 0.01 mm\u00b3", "Avascular stage locked at 0.01 mm\u00b3"),
    ("\u963f\u53f8\u5339\u6797 \u2192 COX-2 \u2192 \u6297\u8840\u7ba1\u65b0\u751f", "Aspirin \u2192 COX-2 \u2192 anti-angiogenesis"),
    ("\u80bf\u7624\u6c38\u8fdc\u505c\u7559\u5728\u201c\u4e34\u5e8a\u4e0d\u53ef\u89c1\u201d\u9636\u6bb5", '\u201cTumor permanently stays in \u201cclinically invisible\u201d stage'),
    ("\u9003\u9038\u7a97\u53e3 = MHC \u77db\u76fe + \u8bd5\u9519\u9009\u62e9", "Escape window = MHC contradiction + trial-and-error selection"),
    ("\u5730\u9ad8\u8f9b \u2192 \u8868\u89c2\u9057\u4f20 \u2192 MHC \u6062\u590d  \u5fc3\u5f97\u5b89 \u2192 \u03b2\u963b\u65ad \u2192 \u53bb\u5e94\u6fc0", "Digoxin \u2192 epigenetics \u2192 MHC restoration  Propranolol \u2192 \u03b2-blockade \u2192 de-stress"),
    ("\u9003\u9038\u7a97\u53e3\u7269\u7406\u95ed\u5408", "Escape window physically closed"),
    ("\u603b\u7ed3\uff1a\u7269\u7406\u5b66\u4fdd\u8bc1\u7684curative\u6548\u679c", "Summary: Physically Guaranteed Curative Effect"),
    ("SCVC\u7684\u8d21\u732e\u4e0d\u662f\u201c\u53d1\u73b0\u65b0\u836f\u201d", '\u201cSCVC\u2019s contribution is not \u201cdiscovering new drugs\u201d'),
    ("SCVC\u7684\u8d21\u732e\u662f\u201c\u8bc1\u660e\u73b0\u6709\u7684\u56db\u4e2a\u4fbf\u5b9c\u836f\u8054\u7528 = \u7269\u7406\u7edd\u6740\u201d", '\u201cSCVC\u2019s contribution is \u201cproving that four existing cheap drugs in combination = physical checkmate\u201d'),
    ("\u8fd9\u4e0d\u662f\u201c\u53ef\u80fd\u6709\u6548\u201d\u3002\u8fd9\u662f\u201c\u7269\u7406\u5b66\u4fdd\u8bc1\u6709\u6548\u201d\u3002", '\u201cThis is not \u201cpossibly effective.\u201d This is \u201cphysically guaranteed effective.\u201d'),
    ("\u4e0b\u4e00\u6b65: \u542f\u52a8\u4e34\u5e8a\u8bd5\u9a8c\u3002", "Next step: Initiate clinical trials."),
    
    # ATP crisis section specific
    ("\u6b63\u5e38\u7ec6\u80de vs \u764c\u7ec6\u80de\u7684 ATP \u9884\u7b97", "ATP Budget: Normal Cells vs. Cancer Cells"),
    ("\u56db\u8054\u5982\u4f55\u5236\u9020 ATP \u8d64\u5b57", "How the Four-Drug Combination Creates an ATP Deficit"),
    ("\u5355\u836f\u8010\u836f\u7684\u65f6\u95f4\u7ebf", "Single-Drug Resistance Timeline"),
    ("\u8054\u5408\u8010\u836f\u7684\u7ec4\u5408\u7206\u70b8", "Combinatorial Explosion of Multi-Drug Resistance"),
    ("\u4f4e\u5242\u91cf\u7b56\u7565 \u2014 \u98a0\u8986\u201c\u6700\u5927\u8010\u53d7\u5242\u91cf\u201d\u8303\u5f0f", 'The Low-Dose Strategy \u2014 Subverting the \u201cMaximum Tolerated Dose\u201d Paradigm'),
    ("\u4e3a\u4ec0\u4e48\u4f4e\u5242\u91cf\u53cd\u800c\u66f4\u5f3a\uff1f", "Why Is Low Dose Actually Stronger?"),
    ("\u591a\u5899\u8010\u53d7 \u2014 \u6700\u5927\u7684\u98ce\u9669\uff0c\u4f46\u88ab\u9501\u6b7b", "Multi-Wall Tolerance \u2014 The Greatest Risk, But Locked Down"),
    
    # More common Chinese phrases in this file
    ("\u6bcf\u4e2a\u836f\u72ec\u7acb\u653b\u51fb\u4e00\u6761\u5899", "Each drug independently attacks one wall"),
    ("\u9003\u9038\u9700\u8981\u540c\u65f6\u6ee1\u8db3\u56db\u4e2a\u6761\u4ef6", "escape requires simultaneously satisfying four conditions"),
    ("\u8fd9\u56db\u79cd\u9003\u9038\u6240\u9700\u7684\u7ec6\u80de\u72b6\u6001\u4e92\u76f8\u77db\u76fe", "These four escape-required cellular states are mutually contradictory"),
    ("\u6bcf\u4e2a\u836f\u72ec\u7acb\u653b\u51fb\u4e00\u6761\u5899\uff0c\u4f46\u9003\u9038\u9700\u8981\u540c\u65f6\u6ee1\u8db3\u56db\u4e2a\u6761\u4ef6", "Each drug independently attacks one wall, but escape requires simultaneously satisfying four conditions"),
]

for old, new in para_translations:
    if old in content:
        content = content.replace(old, new)

cn_count = len(re.findall(r'[\u4e00-\u9fff]', content))
print(f'Remaining Chinese: {cn_count} / {len(content)} ({round(cn_count/len(content)*100,1)}%)')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('E172 refined.')
