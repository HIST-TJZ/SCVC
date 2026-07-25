import re, os

path = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations\Vol5_Medicine_Drugs\E172_Non_Toxic_Multi_Target_Cancer_Lockout.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Translations matching ACTUAL remaining Chinese in the file
T = {}

# Input constants
T['MHC-I \u6b63\u5e38\u8868\u8fbe ~10\u2075/\u7ec6\u80de, NK \u53bb\u6291\u5236\u9608value ~20-50% (E171: \u53cc\u91cd\u675f\u7f1a)'] = 'MHC-I normal expression ~10\u2075/cell, NK disinhibition threshold ~20-50% (E171: double bind)'

# Chemo paragraph (matching the mixed version in the file)
T['    \u4f20\u7edf\u5316\u7597 = \"\u627e\u4e00\u79cd\u5bf9\u764c\u7ec6\u80de\u8db3\u591f\u6bd2\u7684\u6bd2\u7d20\"'] = '    Traditional chemotherapy = "find a toxin sufficiently poisonous to cancer cells"'
T['    \u2192 \u5fc5\u987b\u5f3a\u6548 \u2192 \u4f46\u764c\u7ec6\u80de\u548c\u6b63\u5e38\u7ec6\u80de\u5171\u4eab 99% \u7684\u751f\u5316\u673a\u5236'] = '    \u2192 Must be potent \u2192 but cancer cells and normal cells share 99% of biochemical machinery'
T['    \u2192 \u5f3a\u6548 = \u5bf9\u6b63\u5e38\u7ec6\u80de\u4e5f\u6bd2 \u2192 \u526fAction \u2192 \u5242\u91cf\u53d7\u9650'] = '    \u2192 Potency = toxicity to normal cells too \u2192 side effects \u2192 dose limitation'
T['    \u2192 \u5242\u91cf\u53d7\u9650 \u2192 \u4e00\u4e9b\u764c\u7ec6\u80de\u5b58\u6d3b \u2192 \u590d\u53d1 + \u8010\u836f'] = '    \u2192 Dose limitation \u2192 some cancer cells survive \u2192 relapse + resistance'

# Wall box lines
T['    \u2502 \u5899 1 (E168): \u5206\u88c2\u901f\u5ea6Ceiling \u2248 12-14 h/\u5468\u671f               \u2502'] = '    \u2502 Wall 1 (E168): Division Speed Ceiling \u2248 12-14 h/cycle              \u2502'
T['    \u2502   DNA \u805a\u5408\u9176 ~50 bp/s \u2192 S \u671f\u4e0d\u53ef\u538b\u7f29                     \u2502'] = '    \u2502   DNA polymerase ~50 bp/s \u2192 S-phase incompressible                 \u2502'
T['    \u2502   \u764c\u7ec6\u80de\u6bd4\u6b63\u5e38\u7ec6\u80de\u4ec5\u5feb ~2\u00d7, \u4e14\u4e0d\u80fd\u66f4\u5feb                     \u2502'] = '    \u2502   Cancer cells only ~2\u00d7 faster than normal, and cannot go faster       \u2502'
T['    \u2502 \u5899 2 (E169): \u7a81\u53d8\u7387\u5730\u677f \u2248 10\u207b\u2079/\u78b1\u57fa/\u4ee3                  \u2502'] = '    \u2502 Wall 2 (E169): Mutation Rate Floor \u2248 10\u207b\u2079/base/generation         \u2502'
T['    \u2502   \u9a71\u52a8\u7a81\u53d8\u79ef\u7d2f\u9700\u6570\u5341\u5e74 \u2192 cancer\u662f\"\u65f6\u95f4\u75c5\"                   \u2502'] = '    \u2502   Driver mutation accumulation requires decades \u2192 cancer is a "disease of time" \u2502'
T['    \u2502   \u4f46\u8fd9\u4e5f\u610f\u5473\u7740: \u764c\u7ec6\u80de\u9700\u8981\u6301\u7eed\u79ef\u7d2f\u7a81\u53d8\u6765\"\u9002\u5e94\"             \u2502'] = '    \u2502   But this also means: cancer cells need continuous mutations to "adapt"    \u2502'
T['    \u2502 \u5899 3 (E170): \u6c27\u6269\u6563\u5899 \u2248 200 \u03bcm                           \u2502'] = '    \u2502 Wall 3 (E170): Oxygen Diffusion Wall \u2248 200 \u03bcm                    \u2502'
T['    \u2502   \u65e0\u8840\u7ba1\u80bf\u7624 \u2264 0.01 mm\u00b3 \u2192 \u8840\u7ba1\u65b0\u751f\u662f\u7269\u7406\u74f6\u9888             \u2502'] = '    \u2502   Avascular tumor \u2264 0.01 mm\u00b3 \u2192 angiogenesis is a physical bottleneck  \u2502'
T['    \u2502   \u8840\u7ba1\u6c38\u8fdc\u8ffd\u4e0d\u4e0a\u80bf\u7624 \u2192 \u6838\u5fc3\u574f\u6b7b\u662f\u5fc5\u7136                     \u2502'] = '    \u2502   Blood vessels can never catch up \u2192 core necrosis is inevitable      \u2502'
T['    \u2502 \u5899 4 (E171): MHC-NK \u53cc\u91cd\u675f\u7f1a                               \u2502'] = '    \u2502 Wall 4 (E171): MHC-NK Double Bind                               \u2502'
T['    \u2502   \u9ad8 MHC-I \u2192 T \u7ec6\u80de\u8bc6\u522b \u2192 \u88ab\u6740                            \u2502'] = '    \u2502   High MHC-I \u2192 T cell recognition \u2192 killed                            \u2502'
T['    \u2502   \u4f4e MHC-I \u2192 NK \u7ec6\u80de\"missing self\" \u2192 \u88ab\u6740                 \u2502'] = '    \u2502   Low MHC-I \u2192 NK cell "missing self" \u2192 killed                     \u2502'
T['    \u2502   \u9003\u9038\u7a97\u53e3\u5b58\u5728 (\u9009\u62e9\u6027\u7b49\u4f4d\u57fa\u56e0\u4e22\u5931), \u4f46\u9700\u8981\u8bd5\u9519\u65f6\u95f4        \u2502'] = '    \u2502   Escape window exists (selective allele loss), but requires trial-and-error time \u2502'

# Key insight paragraph - MATCHING FILE CONTENT
T['    \u26ab \u5173\u952e\u6d1e\u5bdf: \u6bcf\u6761\u5899\u72ec\u7acb\u65bd\u52a0 = \u764c\u7ec6\u80de\u9700\u8981\u72ec\u7acb\"\u7ed5\u8fc7\"\n    \u26ab \u540c\u65f6\u7d27\u56db\u6761\u5899 = \u764c\u7ec6\u80de\u9700\u8981\u540c\u65f6\u6ee1\u8db3\u56db\u4e2a\u4e92\u76f8\u77db\u76fe\u7684\u7269\u7406\u7ea6\u675f\n    \u26ab \u6b63\u5e38\u7ec6\u80de\u4e0d\u9700\u8981\u6ee1\u8db3\u4efb\u4f55\u4e00\u4e2a (\u4e0d\u5206\u88c2/\u4e0d\u7a81\u53d8/\u4e0d\u65b0\u751f\u8840\u7ba1/\u4e0d\u9003\u9038\u514d\u75ab)\n    \u26ab \u2192 \u6cbb\u7597\u7a97\u53e3\u5929\u7136\u5de8\u5927 \u2014 \u4e0d\u9700\u8981\u5f3a\u6548, \u53ea\u9700\u8981\u591a\u6548'] = '    \u26ab Key insight: each wall applied independently = cancer cells need to independently "bypass"\n    \u26ab Tighten all four walls simultaneously = cancer cells must satisfy four mutually contradictory physical constraints\n    \u26ab Normal cells need not satisfy any of them (not dividing / not mutating / no angiogenesis / no immune escape)\n    \u26ab \u2192 The therapeutic window is naturally enormous \u2014 you do not need potency, you need multi-efficacy'

# Bacteria vs cancer table - MATCHING FILE CONTENT  
T['    \u2502              \u7ec6\u83cc\u8010\u836f (E158)         cancer\u591a\u9776\u70b9 (E172)     \u2502'] = '    \u2502              Bacterial Resistance (E158)    Cancer Multi-Target (E172) \u2502'
T['    \u2502 \u654c\u4eba          \u5916\u6765\u751f\u7269                 \u81ea\u5df1\u7684\u7ec6\u80de          \u2502'] = '    \u2502 Enemy          Foreign organism            Own cells                \u2502'
T['    \u2502 \u9002\u5e94\u673a\u5236      \u83b7\u53d6\u8010\u836f\u57fa\u56e0             \u7a81\u53d8+\u8868\u89c2+\u514b\u9686\u9009\u62e9  \u2502'] = '    \u2502 Adaptation      Acquire resistance genes     Mutation + epigenetics   \u2502'
T['    \u2502 Ceiling        \u86cb\u767d\u8d28\u5408\u6210\u6210\u672c            ATP+\u6c27+\u65f6\u95f4        \u2502'] = '    \u2502 Ceiling         Protein synthesis cost       ATP + oxygen + time      \u2502'
T['    \u2502              (~15\u4e2a\u8010\u836f\u57fa\u56e0Ceiling)       (\u591a\u6761\u7269\u7406\u5899)       \u2502'] = '    \u2502               (~15 resistance gene ceiling)  (multiple physical walls) \u2502'
T['    \u2502 \u8054\u5408\u6570\u91cf     ~15 \u79cd\u6297\u751f\u7d20             ~3-5 \u4e2a\u5f31\u6548\u5e72\u9884     \u2502'] = '    \u2502 Combination     ~15 antibiotics              ~3-5 weak interventions   \u2502'
T['    \u2502 \u6bd2\u6027Source      \u6297\u751f\u7d20\u5bf9\u5bbf\u4e3b\u7ec6\u80de          \u8fd1\u96f6 (\u6b63\u5e38\u7ec6\u80de      \u2502'] = '    \u2502 Toxicity source  Antibiotic side effects      Near-zero (normal cells  \u2502'
T['    \u2502               \u7684\u526fAction                  \u4e0d\u53d7\u5f71\u54cd)          \u2502'] = '    \u2502                on host cells                 unaffected)              \u2502'
T['    \u2502 \u5173\u952e\u5dee\u5f02      \u7ec6\u83cc\u53ef\u4ee5\"\u653e\u5f03\"\u8010\u836f        \u764c\u7ec6\u80de\u4e0d\u80fd          \u2502'] = '    \u2502 Key difference   Bacteria can "abandon"       Cancer cells cannot      \u2502'
T['    \u2502               (\u4ee3\u4ef7: \u751f\u957f\u6162)           \"\u653e\u5f03\"\u5206\u88c2/\u4fee\u590d    \u2502'] = '    \u2502                (cost: slow growth)           "abandon" division/repair \u2502'
T['    \u2502                                         /\u8840\u7ba1/\u9003\u9038 = \u6b7b\u4ea1  \u2502'] = '    \u2502                                         /vessels/escape = death   \u2502'

# Essential difference
T['    \u26ab \u672c\u8d28\u533a\u522b: \u7ec6\u83cc\u53ef\u4ee5\"\u9009\u62e9\"\u4e0d\u751f\u957f (persister cells) \u6765\u8eb2\u907f\u6297\u751f\u7d20\u3002\n      \u764c\u7ec6\u80de\u4e0d\u80fd \u2014 \"\u4e0d\u751f\u957f\"\u5bf9\u5b83\u6765\u8bf4\u7b49\u4e8e\u88ab\u514d\u75ab\u7cfb\u7edf\u6e05\u9664\u6216\u88ab\u7269\u7406\u7ea6\u675f\u538b\u6b7b\u3002\n      \u8fd9\u4f7fcancer\u7684\u591a\u9776\u70b9\u8054\u5408\u6bd4\u6297\u751f\u7d20\u8054\u5408\u5728\u7269\u7406\u4e0a\u66f4\u6709\u5229\u3002'] = '    \u26ab Essential difference: bacteria can "choose" not to grow (persister cells) to evade antibiotics.\n      Cancer cells cannot \u2014 "not growing" for them equals being cleared by the immune system or crushed by physical constraints.\n      This makes cancer multi-target combinations physically more advantageous than antibiotic combinations.'

# Section 3
T['3. \u4e3a\u4ec0\u4e48\"\u5f31\u6548\u65e0\u6bd2\"\u662f\u5173\u952e \u2014 \u80fd\u91cf\u4f1a\u8ba1'] = '3. Why "Weak and Non-Toxic" Is Key \u2014 Energy Accounting'
T['3.1 \u764c\u7ec6\u80de\u7684\u8d44\u6e90\u9884\u7b97'] = '3.1 The Cancer Cell Resource Budget'
T['    \u4e00\u4e2a\u764c\u7ec6\u80de\u7ef4\u6301\u751f\u5b58+\u5206\u88c2\u7684\u65e5\u5e38\u5f00\u652f:'] = '    The daily operating expenses of a cancer cell maintaining survival + division:'
T['    \u9879\u76ee                    ATP \u6210\u672c (\u76f8\u5bf9)        \u5360\u603b\u9884\u7b97'] = '    Item                    ATP Cost (relative)        Share of Budget'
T['    \u57fa\u7840\u4ee3\u8c22 (\u7ef4\u6301\u819c\u7535\u4f4d\u3001      ~30%                 30%'] = '    Basal metabolism (maintain membrane       ~30%                 30%'

# "Freedom budget" paragraph
T['    \u26ab \u764c\u7ec6\u80de\u7684\"\u81ea\u7531\u9884\u7b97\"\u4ec5 ~5% \u2014 \u56e0\u4e3a\u5b83\u5728\u5feb\u901f\u5206\u88c2\u4e0a\u7684\u6295\u5165\u5df2\u7ecf\u5f88\u9ad8\u3002\n    \u26ab \u4efb\u4f55\u989d\u5916\u538b\u529b\u90fd\u4ece\u8fd9 5% \u4e2d\u6263\u9664 \u2014 \u6216\u8005\u4ece\u5176\u4ed6\u5fc5\u8981\u9879\u76ee\u4e2d\u501f\u3002\n    \u26ab \u4ece\u5fc5\u8981\u9879\u76ee\u501f \u2192 \u5206\u88c2\u6162 / \u4fee\u590d\u5dee / \u4ee3\u8c22\u5d29\u6e83\u3002'] = '    \u26ab The cancer cell''s "freedom budget" is only ~5% \u2014 because its investment in rapid division is already very high.\n    \u26ab Any additional stress is deducted from this 5% \u2014 or borrowed from other essential items.\n    \u26ab Borrowing from essential items \u2192 slower division / worse repair / metabolic collapse.'

# 3.2 section
T['3.2 \u56db\u4e2a\u5f31\u6548\u5e72\u9884\u7684\u53e0\u52a0 \u2014 \u975e\u52a0\u6027, \u662f\u4e58\u6cd5'] = '3.2 The Superposition of Four Weak Interventions \u2014 Not Additive, but Multiplicative'
T['    \u5173\u952e: \u56db\u4e2a\u5899\u4e0d\u662f\u72ec\u7acb\u7684, \u5b83\u4eec\u5728\u4ee3\u8c22\u4e0a\u8026\u5408:'] = '    Key point: the four walls are not independent; they are metabolically coupled:'

# ATP coupling paragraph
T['    \u26ab \u6838\u5fc3\u673a\u5236: \u56db\u4e2a\u5e72\u9884\u540c\u65f6\u6307\u5411 ATP \u2014 \u764c\u7ec6\u80de\u7684\u901a\u7528\"\u80fd\u6e90\u8d27\u5e01\"\u3002\n      \u00b7 E170 \u2192 ATP \u4ea7\u51fa \u2193 (\u7f3a\u6c27 \u2192 \u7cd6\u9175\u89e3\u6548\u7387\u4f4e 18\u00d7)\n      \u00b7 E168 \u2192 ATP \u9700\u6c42\u7ef4\u6301\u5728\u5206\u88c2\u6c34\u5e73\n      \u00b7 E169 \u2192 \u4fee\u590d\u6210\u672c \u2191 (PARP \u6d88\u8017 NAD\u207a)\n      \u00b7 E171 \u2192 immune escape\u86cb\u767d\u5408\u6210 \u2191 (\u9700\u8981 ATP)'] = '    \u26ab Core mechanism: all four interventions simultaneously target ATP \u2014 the universal "energy currency" of cancer cells.\n      \u00b7 E170 \u2192 ATP output \u2193 (hypoxia \u2192 glycolysis efficiency 18\u00d7 lower)\n      \u00b7 E168 \u2192 ATP demand maintained at division level\n      \u00b7 E169 \u2192 repair cost \u2191 (PARP consumes NAD\u207a)\n      \u00b7 E171 \u2192 immune escape protein synthesis \u2191 (requires ATP)'

# Multiplicative effect
T['    \u26ab \u8fd9\u4e0d\u662f 5% + 3% + 10% + 5% = 23%\n      \u800c\u662f\u6bcf\u4e2a\u90fd\u8ba9\u764c\u7ec6\u80de\u66f4\u96be\u83b7\u5f97\u548c\u4f7f\u7528 ATP,\n      \u5728 ATP \u5df2\u7ecf\u7d27\u5f20\u7684\u80cc\u666f\u4e0b \u2192 \u4e58\u6570\u6548\u5e94!'] = '    \u26ab This is not 5% + 3% + 10% + 5% = 23%\n      Rather, each intervention makes it harder for cancer cells to obtain and use ATP,\n      against the backdrop of already-tight ATP \u2192 multiplicative effect!'

# Apply all
replaced = 0
for old, new in T.items():
    if old in content:
        content = content.replace(old, new)
        replaced += 1

cn = len(re.findall(r'[\u4e00-\u9fff]', content))
with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"E172: {cn} CN / {len(content)} total ({round(cn/len(content)*100,1)}%) - {replaced} replacements")
