import re, os

BASE = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations\Vol5_Medicine_Drugs"

files = {
    "E176": "E176_HIV_Cure_Ceiling.md",
    "E188": "E188_Complete_Longevity_Protocol.md",
    "E187": "E187_Aging_Reversal_Reversibility.md",
}

results = {}
for label, fname in files.items():
    path = os.path.join(BASE, fname)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    cn_before = len(re.findall(r'[\u4e00-\u9fff]', content))
    results[label] = (cn_before, len(content))
    # Extract first 5 Chinese-majority lines for diagnostics
    lines = content.split("\n")
    cn_samples = []
    for line in lines:
        cn = len(re.findall(r'[\u4e00-\u9fff]', line))
        if cn > 8:
            cn_samples.append(line.strip()[:120])
            if len(cn_samples) >= 8:
                break
    
    print(f"\n=== {label}: {cn_before} CN / {len(content)} total ({round(cn_before/len(content)*100,1)}%) ===")
    for s in cn_samples:
        print(f"  {s}")

print("\nReady for translation.")
