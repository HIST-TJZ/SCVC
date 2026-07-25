import re

cn_path = r"C:\Users\20606\Desktop\SCVC-github\cn\V3.0\08_工程极限\8.7_391项完整计算\卷9_末日倒计时_最后窗口_E201-E220\E212_永生时间线_ABCvs现代社会_逃逸速度.md"
en_path = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations\Vol9_Doomsday_Countdown\E212_Immortality_Timeline_ABC_vs_Modern_Society.md"

with open(cn_path, "r", encoding="utf-8") as f:
    content = f.read()

reps = [
    ("# E212: 永生实现时间线 — ABC vs 现代社会，长寿逃逸速度",
     "# E212: Immortality Realization Timeline — ABC vs Modern Society, Longevity Escape Velocity"),
    ("> **输入**：SCVC常数（H键0.20eV→蛋白质折叠稳定性、C-C键3.6eV→AGEs交联天花板、ATP 0.3eV→代谢率约束、Landauer 2.85e-21 J/bit→AI研究能耗地板、意识带宽~100bps→主观寿命、脑容量~5e15 bits→记忆溢出）",
     "> **Inputs**: SCVC constants (H-bond 0.20eV \u2192 protein folding stability, C-C bond 3.6eV \u2192 AGEs crosslink ceiling, ATP 0.3eV \u2192 metabolic rate constraint, Landauer 2.85e-21 J/bit \u2192 AI research energy floor, consciousness bandwidth ~100bps \u2192 subjective lifespan, brain capacity ~5e15 bits \u2192 memory overflow)"),
]
# Too many reps for inline - let me use a different approach

print(f"CN source: {len(content)} chars, {len(re.findall(r'[\u4e00-\u9fff]', content))} CN chars")
# Read current EN to compare
with open(en_path, "r", encoding="utf-8") as f:
    en_content = f.read()
print(f"Current EN: {len(en_content)} chars, {len(re.findall(r'[\u4e00-\u9fff]', en_content))} CN chars remaining")
