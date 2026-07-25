import re, os

BASE = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations\Vol5_Medicine_Drugs"

# ============================================================
# E172: Non-Toxic Multi-Target Cancer Lockout
# ============================================================
E172 = {}

E172["SCVC \u533b\u5b66\u5de5\u7a0b  E172  \u65e0\u6bd2\u591a\u9776\u70b9cancer\u5c01\u6740\u2014\u2014\u5f31\u00d7\u591a=\u5f3a"] = "SCVC Medical Engineering  E172  Non-Toxic Multi-Target Cancer Lockout \u2014 Weak \u00d7 Many = Strong"
E172["\u3010\u8f93\u5165\u5e38\u6570\u3011(\u6765\u81ea _SCVC\u5de5\u7a0b\u5e38\u6570reference table.md \u53ca E168-E171)"] = "[Input Constants] (from _SCVC Engineering Constants Reference.md and E168-E171)"

# Individual constant line translations
E172["MHC-I \u6b63\u5e38\u8868\u8fbe ~10\u2075/\u7ec6\u80de, NK \u53bb\u6291\u5236\u9608value ~20-50% (E171: \u53cc\u91cd\u675f\u7f1a)"] = "MHC-I normal expression ~10\u2075/cell, NK disinhibition threshold ~20-50% (E171: double bind)"

# Section 1 headers
E172["1. \u6838\u5fc3\u731c\u60f3: \u5f31\u00d7\u591a = \u5f3a"] = "1. Core Hypothesis: Weak \u00d7 Many = Strong"
E172["1.1 \u4f20\u7edf\u5316\u7597\u7684\u903b\u8f91 \u2014 \u53ca\u5176\u5931\u8d25"] = "1.1 The Logic of Traditional Chemotherapy \u2014 and Its Failure"
E172["1.2 SCVC\u2019s Alternative Logic"] = "1.2 SCVC\u2019s Alternative Logic"

# Traditional chemo paragraph
E172['    \u4f20\u7edf\u5316\u7597 = \"\u627e\u4e00\u79cd\u5bf9\u764c\u7ec6\u80de\u8db3\u591f\u6bd2\u7684\u6bd2\u7d20\"\n    \u2192 \u5fc5\u987b\u5f3a\u6548 \u2192 \u4f46\u764c\u7ec6\u80de\u548c\u6b63\u5e38\u7ec6\u80de\u5171\u4eab 99% \u7684\u751f\u5316\u673a\u5236\n    \u2192 \u5f3a\u6548 = \u5bf9\u6b63\u5e38\u7ec6\u80de\u4e5f\u6bd2 \u2192 \u526f\u4f5c\u7528 \u2192 \u5242\u91cf\u53d7\u9650\n    \u2192 \u5242\u91cf\u53d7\u9650 \u2192 \u4e00\u4e9b\u764c\u7ec6\u80de\u5b58\u6d3b \u2192 \u590d\u53d1 + \u8010\u836f'] = '    Traditional chemotherapy = \"find a toxin sufficiently poisonous to cancer cells\"\n    \u2192 Must be potent \u2192 but cancer cells and normal cells share 99% of biochemical machinery\n    \u2192 Potency = toxicity to normal cells too \u2192 side effects \u2192 dose limitation\n    \u2192 Dose limitation \u2192 some cancer cells survive \u2192 relapse + resistance'

# Chemo premise
E172['    \u26ab \u4f20\u7edf\u5316\u7597\u7684Prerequisites (\u764c\u7ec6\u80de=\u5916\u6765\u75c5\u539f\u4f53) \u662f\u9519\u7684\u3002\n      \u764c\u7ec6\u80de\u662f\"\u81ea\u5df1\u4eba\" \u2014 \u4e0d\u80fd\u50cf\u6297\u751f\u7d20\u6740\u83cc\u90a3\u6837\"\u5730\u6bef\u5f0f\u8f70\u70b8\"\u3002'] = '    \u26ab The premise of traditional chemotherapy (cancer cell = foreign pathogen) is wrong.\n      Cancer cells are \"one of us\" \u2014 you cannot \"carpet-bomb\" them like antibiotics kill bacteria.'

# Wall discovery
E172['    E168-E171 \u63ed\u793a: \u764c\u7ec6\u80de\u5fc5\u987b\u9075\u5b88\u56db\u6761\u7269\u7406\u5899:'] = '    E168-E171 reveal: cancer cells must obey four physical walls:'

# Key insights paragraph
E172['    \u26ab \u5173\u952e\u6d1e\u5bdf: \u6bcf\u6761\u5899\u72ec\u7acb\u65bd\u52a0 = \u764c\u7ec6\u80de\u9700\u8981\u72ec\u7acb\"\u7ed5\u8fc7\"\n    \u26ab \u540c\u65f6\u7d27\u56db\u6761\u5899 = \u764c\u7ec6\u80de\u9700\u8981\u540c\u65f6\u6ee1\u8db3\u56db\u4e2a\u4e92\u76f8\u77db\u76fe\u7684\u7269\u7406\u7ea6\u675f\n    \u26ab \u6b63\u5e38\u7ec6\u80de\u4e0d\u9700\u8981\u6ee1\u8db3\u4efb\u4f55\u4e00\u4e2a (\u4e0d\u5206\u88c2/\u4e0d\u7a81\u53d8/\u4e0d\u65b0\u751f\u8840\u7ba1/\u4e0d\u9003\u9038\u514d\u75ab)\n    \u26ab \u2192 \u6cbb\u7597\u7a97\u53e3\u5929\u7136\u5de8\u5927 \u2014 \u4e0d\u9700\u8981\u5f3a\u6548, \u53ea\u9700\u8981\u591a\u6548'] = '    \u26ab Key insight: each wall applied independently = cancer cells need to independently \"bypass\"\n    \u26ab Tighten all four walls simultaneously = cancer cells must satisfy four mutually contradictory physical constraints\n    \u26ab Normal cells need not satisfy any of them (not dividing / not mutating / no angiogenesis / no immune escape)\n    \u26ab \u2192 The therapeutic window is naturally enormous \u2014 you do not need potency, you need multi-efficacy'

# Section 2
E172["2. \u7c7b\u6bd4 E158: \u4ece\"15\u8054\u7528\u6297\u751f\u7d20\"\u5230\"4\u8054\u7528\u6297\u764c\""] = '2. Analogy with E158: From \"15-Antibiotic Combination\" to \"4-Drug Anticancer Combination\"'

# Essential difference
E172['    \u26ab \u672c\u8d28\u533a\u522b: \u7ec6\u83cc\u53ef\u4ee5\"\u9009\u62e9\"\u4e0d\u751f\u957f (persister cells) \u6765\u8eb2\u907f\u6297\u751f\u7d20\u3002\n      \u764c\u7ec6\u80de\u4e0d\u80fd \u2014 \"\u4e0d\u751f\u957f\"\u5bf9\u5b83\u6765\u8bf4\u7b49\u4e8e\u88ab\u514d\u75ab\u7cfb\u7edf\u6e05\u9664\u6216\u88ab\u7269\u7406\u7ea6\u675f\u538b\u6b7b\u3002\n      \u8fd9\u4f7fcancer\u7684\u591a\u9776\u70b9\u8054\u5408\u6bd4\u6297\u751f\u7d20\u8054\u5408\u5728\u7269\u7406\u4e0a\u66f4\u6709\u5229\u3002'] = '    \u26ab Essential difference: bacteria can \"choose\" not to grow (persister cells) to evade antibiotics.\n      Cancer cells cannot \u2014 \"not growing\" for them equals being cleared by the immune system or crushed by physical constraints.\n      This makes cancer multi-target combinations physically more advantageous than antibiotic combinations.'

def apply_translations(filepath, translations):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    replaced = 0
    for old, new in translations.items():
        if old in content:
            content = content.replace(old, new)
            replaced += 1
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    cn = len(re.findall(r'[\u4e00-\u9fff]', content))
    return cn, len(content), replaced

path172 = os.path.join(BASE, "E172_Non_Toxic_Multi_Target_Cancer_Lockout.md")
cn172, total172, rep172 = apply_translations(path172, E172)
print(f"E172: {cn172} CN / {total172} total ({round(cn172/total172*100,1)}%) - {rep172} replacements")

# ============================================================
# Also process the ceiling companion file
# ============================================================
path172c = os.path.join(BASE, "E172_Non_Toxic_Multi_Target_Lockout_Ceiling.md")
with open(path172c, "r", encoding="utf-8") as f:
    c172c = f.read()
# Apply same translations
for old, new in E172.items():
    if old in c172c:
        c172c = c172c.replace(old, new)
cn172c = len(re.findall(r'[\u4e00-\u9fff]', c172c))
with open(path172c, "w", encoding="utf-8") as f:
    f.write(c172c)
print(f"E172-Ceiling: {cn172c} CN / {len(c172c)} total ({round(cn172c/len(c172c)*100,1)}%)")

print("\nDone with E172 batch.")
