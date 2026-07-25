import re, os

BASE = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations\Vol5_Medicine_Drugs"

# ========================
# E176: HIV Cure
# ========================
T176 = {}

# Title and header
T176['SCVC \u533b\u5b66\u5de5\u7a0b  E176  HIV cure \u2014 \u6f5c\u4f0f\u50a8\u5e93\u7684\u7269\u7406\u969c\u7887'] = 'SCVC Medical Engineering  E176  HIV Cure \u2014 The Physical Barriers of the Latent Reservoir'
T176['\u3010\u8f93\u5165\u5e38\u6570\u3011(\u6765\u81ea_SCVC\u5de5\u7a0b\u5e38\u6570reference table.md)'] = '[Input Constants] (from _SCVC Engineering Constants Reference.md)'

# Input constant lines  
T176['\u9006\u8f6c\u5f55\u9176\u9519\u8bef\u7387 \u2248 10\u207b\u2074-10\u207b\u2075/\u78b1\u57fa          (\u03b1 \u2192 H\u952e\u8bc6\u522b, \u65e0\u6821\u5bf9)'] = 'Reverse transcriptase error rate \u2248 10\u207b\u2074-10\u207b\u2075/base          (\u03b1 \u2192 H-bond recognition, no proofreading)'
T176['HIV \u57fa\u56e0\u7ec4 \u2248 9.2 kb                       (Gag, Pol, Env + \u8f85\u52a9\u57fa\u56e0)'] = 'HIV genome \u2248 9.2 kb                       (Gag, Pol, Env + accessory genes)'
T176['CD4\u207a \u8bb0\u5fc6 T \u7ec6\u80delifespan \u2248 \u6570\u5e74-\u6570\u5341\u5e74        (\u7aef\u7c92\u957f\u5ea6 + \u5206\u88c2\u7387\u63a8\u5bfc)'] = 'CD4\u207a memory T cell lifespan \u2248 years to decades        (telomere length + division rate derived)'
T176['\u8bb0\u5fc6 T \u7ec6\u80de\u5206\u88c2\u7387 \u2248 0.1-1%/\u5929 (\u7a33\u6001)     (IL-7, IL-15 \u9a71\u52a8\u7684\u7a33\u6001\u589e\u6b96)'] = 'Memory T cell division rate \u2248 0.1-1%/day (steady state)     (IL-7, IL-15-driven homeostatic proliferation)'
T176['\u6f5c\u4f0f\u50a8\u5e93\u534a\u8870\u671f \u2248 44 \u4e2a\u6708 (Siliciano \u7814\u7a76)'] = 'Latent reservoir half-life \u2248 44 months (Siliciano study)'
T176['ART \u4e0b\u8840\u6d46\u75c5\u6bd2\u8f7d\u91cf < 20-50 \u62f7\u8d1d/mL'] = 'Plasma viral load under ART < 20-50 copies/mL'
T176['ART \u4e0b\u6f5c\u4f0f\u50a8\u5e93\u5927\u5c0f \u2248 10\u2075-10\u2077 \u7ec6\u80de'] = 'Latent reservoir size under ART \u2248 10\u2075-10\u2077 cells'
T176['\u524d\u75c5\u6bd2\u6574\u5408: \u9006\u8f6c\u5f55 \u2192 \u53cc\u94fe DNA \u2192 \u6574\u5408\u9176 \u2192 \u5bbf\u4e3b\u67d3\u8272\u4f53'] = 'Provirus integration: reverse transcription \u2192 double-stranded DNA \u2192 integrase \u2192 host chromosome'
T176['\u6f5c\u4f0f\u673a\u5236: \u6574\u5408\u5728\u8f6c\u5f55\u6c89\u9ed8\u533a\u57df + \u65e0 Tat \u6fc0\u6d3b'] = 'Latency mechanism: integration in transcriptionally silent regions + no Tat activation'

# Section 1
T176['1. Question\u7684\u7269\u7406\u672c\u8d28'] = '1. The Physical Nature of the Question'
T176['1.1 \u4e3a\u4ec0\u4e48 ART \u4e0d\u80fd\u6cbb\u6108 HIV?'] = '1.1 Why Cannot ART Cure HIV?'
T176['    ART (\u6297\u9006\u8f6c\u5f55\u75c5\u6bd2\u6cbb\u7597) \u53ef\u4ee5\u5c06\u8840\u6d46\u75c5\u6bd2\u8f7d\u91cf\u538b\u5230\u68c0\u6d4b\u4e0d\u5230,'] = '    ART (antiretroviral therapy) can suppress plasma viral load to undetectable levels,'
T176['    \u4f46\u505c\u836f\u540e\u5e73\u5747 ~2-4 \u5468\u5185\u75c5\u6bd2\u53cd\u5f39\u81f3\u6cbb\u7597\u524d\u6c34\u5e73\u3002'] = '    but after stopping, virus rebounds to pre-treatment levels within an average of ~2-4 weeks.'
T176['    \u7269\u7406\u539f\u56e0: \u6f5c\u4f0f\u50a8\u5e93\u3002'] = '    Physical reason: the latent reservoir.'
T176['    HIV \u7684\u751f\u547d\u5468\u671f:'] = '    HIV life cycle:'

# Section headers
T176['1.2 \u6f5c\u4f0f\u50a8\u5e93\u7684\u7269\u7406\u7279\u6027'] = '1.2 Physical Properties of the Latent Reservoir'
T176['1.3 \u4e3a\u4ec0\u4e48\u201cshock and kill\u201d\u5931\u8d25\u4e86'] = '1.3 Why "Shock and Kill" Failed'
T176['1.4 \u201cblock and lock\u201d\u7684\u7269\u7406\u57fa\u7840'] = '1.4 The Physical Basis of "Block and Lock"'
T176['2. \u4eceSCVC\u770b HIV cure\u7684\u53ef\u80fd\u8def\u5f84'] = '2. Possible HIV Cure Pathways from the SCVC Perspective'
T176['2.1 \u57fa\u56e0\u7f16\u8f91 (CRISPR) \u2014 \u5207\u9664\u524d\u75c5\u6bd2'] = '2.1 Gene Editing (CRISPR) \u2014 Excising Provirus'
T176['2.2 \u514d\u75ab\u4ecb\u5bfc\u7684\u50a8\u5e93\u6e05\u9664'] = '2.2 Immune-Mediated Reservoir Clearance'
T176['2.3 \u5e72\u7ec6\u80de\u79fb\u690d + ART \u2014 \u67cf\u6797\u60a3\u8005\u8def\u7ebf'] = '2.3 Stem Cell Transplant + ART \u2014 The Berlin Patient Pathway'
T176['3. SCVC\u7684\u5224\u65ad'] = '3. SCVC Verdict'
T176['3.1 \u6cbb\u6108\u7684\u7269\u7406\u5b9a\u4e49'] = '3.1 Physical Definition of Cure'
T176['3.2 \u54ea\u6761\u8def\u6700\u6709\u5e0c\u671b'] = '3.2 Which Path Is Most Promising'
T176['3.3 \u65f6\u95f4\u8868'] = '3.3 Timeline'

# ========================
# E188: Complete Longevity Protocol
# ========================
T188 = {}

T188['SCVC lifespan\u5de5\u7a0b E188\uff1a\u5b8c\u6574longevity protocol \u2014 \u4f11\u7720 + \u57fa\u56e0\u5197\u4f59 + \u7eb3\u7c73\u7ef4\u62a4'] = 'SCVC Lifespan Engineering E188: Complete Longevity Protocol \u2014 Hibernation + Gene Redundancy + Nano-Maintenance'
T188['\u3010\u8f93\u5165\u5e38\u6570\u3011(\u6765\u81ea SCVC\u5de5\u7a0b\u5e38\u6570\u901f\u67e5\u8868 + \u524d\u7f6e\u6587\u4ef6 E179/E186/E187)'] = '[Input Constants] (from SCVC Engineering Constants Reference + preceding files E179/E186/E187)'
T188['\u7aef\u7c92\u7f29\u77ed\u901f\u7387 \u2248 50-100 bp/\u4ee3'] = 'Telomere shortening rate \u2248 50-100 bp/generation'
T188['AGEs \u4ea4\u8054\u534a\u8870\u671f \u2248 10-15 \u5e74 (\u80f6\u539f\u86cb\u767d\u66ff\u6362\u901f\u7387)'] = 'AGEs crosslink half-life \u2248 10-15 years (collagen protein turnover rate)'
T188['mtDNA \u7a81\u53d8\u4fee\u590d\u6f0f\u8fc7\u7387 ~1% (\u0394\u0394G \u2248 0.1-0.3 eV \u2248 k_B T)'] = 'mtDNA mutation repair leakage rate ~1% (\u0394\u0394G \u2248 0.1-0.3 eV \u2248 k_B T)'
T188['\u4f11\u7720\u4ee3\u8c22\u7387\u964d\u4f4e: H\u2082S \u2192 10-15% \u57fa\u7840\u4ee3\u8c22, \u5b89\u5168\u8fde\u7eed 4-6 \u6708'] = 'Hibernation metabolic rate reduction: H\u2082S \u2192 10-15% basal metabolism, safe continuous 4-6 months'

# Section headers
T188['1. \u4e09\u5c42\u7b56\u7565\u6982\u8ff0'] = '1. Three-Layer Strategy Overview'
T188['2. \u5c42 1: \u4f11\u7720\u2014\u2014\u201c\u6162\u4e0b\u65f6\u949f\u201d'] = '2. Layer 1: Hibernation \u2014 "Slowing the Clock"'
T188['2.1 \u4f11\u7720\u7684\u7269\u7406\u57fa\u7840'] = '2.1 Physical Basis of Hibernation'
T188['2.2 \u5b89\u5168\u8fde\u7eed\u4f11\u7720\u7684\u6781\u9650'] = '2.2 Limits of Safe Continuous Hibernation'
T188['2.3 \u95f4\u6b47\u6027\u4f11\u7720\u65b9\u6848'] = '2.3 Intermittent Hibernation Protocol'
T188['3. \u5c42 2: \u57fa\u56e0\u5197\u4f59\u2014\u2014\u201c\u9632\u6b62\u7834\u635f\u201d'] = '3. Layer 2: Gene Redundancy \u2014 "Preventing Breakage"'
T188['3.1 \u5173\u952e\u57fa\u56e0\u7684\u5197\u4f59\u5907\u4efd'] = '3.1 Redundant Backups of Key Genes'
T188['3.2 \u7aef\u7c92\u9176\u8c03\u63a7'] = '3.2 Telomerase Regulation'
T188['4. \u5c42 3: \u7eb3\u7c73\u7ef4\u62a4\u2014\u2014\u201c\u4e3b\u52a8\u4fee\u590d\u201d'] = '4. Layer 3: Nano-Maintenance \u2014 "Active Repair"'
T188['4.1 AGEs \u4ea4\u8054\u6e05\u9664'] = '4.1 AGEs Crosslink Clearance'
T188['4.2 mtDNA \u4fee\u590d\u589e\u5f3a'] = '4.2 mtDNA Repair Enhancement'
T188['5. \u5bff\u547d\u5ef6\u957f\u9884\u4f30'] = '5. Lifespan Extension Estimate'
T188['6. \u5b9e\u65bd\u8def\u7ebf\u56fe'] = '6. Implementation Roadmap'

# ========================
# E187: Aging Reversal
# ========================
T187 = {}

T187['SCVC lifespan\u5de5\u7a0b  E187  \u56de\u62e8\u8870\u8001\u2014\u2014\u54ea\u4e9b\u53ef\u9006\uff0c\u54ea\u4e9b\u9501\u6b7b\uff1f'] = 'SCVC Lifespan Engineering  E187  Aging Reversal \u2014 What Is Reversible, What Is Locked?'
T187['\u3010\u8f93\u5165\u5e38\u6570\u3011(\u6765\u81ea SCVC\u5de5\u7a0b\u5e38\u6570\u901f\u67e5\u8868 + E179)'] = '[Input Constants] (from SCVC Engineering Constants Reference + E179)'
T187['1. \u8870\u8001\u7684\u4e09\u5c42\u7269\u7406\u6a21\u578b'] = '1. The Three-Layer Physical Model of Aging'
T187['1.1 \u5206\u5b50\u5c42: \u5927\u5206\u5b50\u635f\u4f24'] = '1.1 Molecular Layer: Macromolecular Damage'
T187['1.2 \u7ec6\u80de\u5c42: \u5e72\u7ec6\u80de\u8017\u7aed'] = '1.2 Cellular Layer: Stem Cell Exhaustion'
T187['1.3 \u7cfb\u7edf\u5c42: \u7ec4\u7ec7\u91cd\u5851\u5931\u8d25'] = '1.3 Systemic Layer: Tissue Remodeling Failure'
T187['2. \u53ef\u9006\u6027\u5206\u7ea7'] = '2. Reversibility Classification'
T187['3. \u5177\u4f53\u5e72\u9884\u7684\u7269\u7406\u53ef\u80fd\u6027'] = '3. Physical Feasibility of Specific Interventions'
T187['4. \u9501\u6b7b\u7684\u90e8\u5206\u2014\u2014\u4e0d\u53ef\u9006\u8f6c\u7684\u5668\u5b98\u8870\u8001'] = '4. The Locked Parts \u2014 Irreversible Organ Aging'
T187['5. SCVC\u7ed3\u8bba'] = '5. SCVC Conclusion'

# Process files
all_translations = {
    "E176_HIV_Cure_Ceiling.md": T176,
    "E188_Complete_Longevity_Protocol.md": T188,
    "E187_Aging_Reversal_Reversibility.md": T187,
}

for fname, translations in all_translations.items():
    path = os.path.join(BASE, fname)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    replaced = 0
    for old, new in translations.items():
        if old in content:
            content = content.replace(old, new)
            replaced += 1
    
    cn = len(re.findall(r'[\u4e00-\u9fff]', content))
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{fname[:25]}: {cn} CN / {len(content)} total ({round(cn/len(content)*100,1)}%) - {replaced} repl")

print("\nAll done.")
