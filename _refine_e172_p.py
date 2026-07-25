# E172 paragraph-level translation
import re, os

path = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations\Vol5_Medicine_Drugs\E172_Non_Toxic_Multi_Target_Cancer_Lockout.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Each entry: (exact_old_paragraph_text, new_english_text)
# Match on the full paragraph text to ensure exact replacement
replacements = []

# Read the file paragraph by paragraph and build replacements
paras = content.split("\n\n")
for p in paras:
    p_stripped = p.strip()
    if len(p_stripped) < 30:
        continue
    cn_chars = len(re.findall(r'[\u4e00-\u9fff]', p_stripped))
    total_chars = len(p_stripped)
    if total_chars == 0:
        continue
    if cn_chars / total_chars < 0.15:
        continue
    
    # This paragraph needs translation - identify and translate
    # We'll store the exact match for replacement
    replacements.append(p_stripped)

print(f"Found {len(replacements)} Chinese-majority paragraphs to translate")

# Now I need to provide translations for each.
# Since I can't auto-translate, let me at least count them
# and show the user the status.

# Actually - let me do manual translation paragraph by paragraph.
# I'll identify each unique paragraph and replace it.

# For now, let me just do the key ones I can identify clearly.

translations = {
    # Para: traditional chemo logic
    '''1.1 The Logic of Traditional Chemotherapy \u2014 and Its Failure
--------------------------------------------------------------
    \u4f20\u7edf\u5316\u7597 = \"\u627e\u4e00\u79cd\u5bf9\u764c\u7ec6\u80de\u8db3\u591f\u6bd2\u7684\u6bd2\u7d20\"
    \u2192 \u5fc5\u987b\u5f3a\u6548 \u2192 \u4f46\u764c\u7ec6\u80de\u548c\u6b63\u5e38\u7ec6\u80de\u5171\u4eab 99% \u7684\u751f\u5316\u673a\u5236
    \u2192 \u5f3a\u6548 = \u5bf9\u6b63\u5e38\u7ec6\u80de\u4e5f\u6bd2 \u2192 \u526f\u4f5c\u7528 \u2192 \u5242\u91cf\u53d7\u9650
    \u2192 \u5242\u91cf\u53d7\u9650 \u2192 \u4e00\u4e9b\u764c\u7ec6\u80de\u5b58\u6d3b \u2192 \u590d\u53d1 + \u8010\u836f''': 
    '''1.1 The Logic of Traditional Chemotherapy \u2014 and Its Failure
--------------------------------------------------------------
    Traditional chemotherapy = "find a toxin sufficiently poisonous to cancer cells"
    \u2192 Must be potent \u2192 but cancer cells and normal cells share 99% of biochemical machinery
    \u2192 Potency = toxicity to normal cells too \u2192 side effects \u2192 dose limitation
    \u2192 Dose limitation \u2192 some cancer cells survive \u2192 relapse + resistance''',
    
    # Para: chemo premise is wrong
    '''\u26ab \u4f20\u7edf\u5316\u7597\u7684Prerequisites (\u764c\u7ec6\u80de=\u5916\u6765\u75c5\u539f\u4f53) \u662f\u9519\u7684\u3002
      \u764c\u7ec6\u80de\u662f\"\u81ea\u5df1\u4eba\" \u2014 \u4e0d\u80fd\u50cf\u6297\u751f\u7d20\u6740\u83cc\u90a3\u6837\"\u5730\u6bef\u5f0f\u8f70\u70b8\"\u3002''':
    '''\u26ab The premise of traditional chemotherapy (cancer cell = foreign pathogen) is wrong.
      Cancer cells are "one of us" \u2014 you cannot "carpet-bomb" them like antibiotics kill bacteria.''',
}

for old, new in translations.items():
    if old in content:
        content = content.replace(old, new)
        print(f"Replaced: {old[:50]}...")

cn_count = len(re.findall(r'[\u4e00-\u9fff]', content))
print(f"After: {cn_count} Chinese chars / {len(content)} total")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
