import json, os

TR = {}

# Read current E172 to find exact Chinese text blocks
path = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations\Vol5_Medicine_Drugs\E172_Non_Toxic_Multi_Target_Cancer_Lockout.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

import re
# Find all paragraphs with Chinese
paras = content.split("\n\n")
cn_paras = []
for p in paras:
    cn = len(re.findall(r'[\u4e00-\u9fff]', p))
    if cn > 10:
        cn_paras.append(p.strip())

print(f"Found {len(cn_paras)} Chinese paragraphs")

# Save them for manual inspection
with open(r"C:\Users\20606\Desktop\SCVC-github\_cn_paras_e172.txt", "w", encoding="utf-8") as f:
    for i, p in enumerate(cn_paras):
        f.write(f"=== PARA {i} ===\n{p}\n\n")

print("Chinese paragraphs saved to _cn_paras_e172.txt")
print(f"First para preview: {cn_paras[0][:100]}...")
