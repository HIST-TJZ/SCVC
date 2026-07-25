import os, re

cn_base = r"C:\Users\20606\Desktop\SCVC-github\cn\V3.0\08_工程极限\8.7_391项完整计算"
en_base = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations"

# Reuse master dictionary + add Vol9-specific terms
MASTER = []

# Load master from batch_translate_v2.py
with open(r"C:\Users\20606\Desktop\SCVC-github\batch_translate_v2.py", "r", encoding="utf-8") as f:
    exec_text = f.read()
start = exec_text.find("MASTER = [")
end = exec_text.find("\n\n# Files to process")
exec(exec_text[start:end])

# Add Vol9-specific translations
VOL9_EXTRA = [
    # Climate
    ("SCVC气候物理", "SCVC Climate Physics"),
    ("SCVC气候工程", "SCVC Climate Engineering"),
    ("SCVC文明工程", "SCVC Civilization Engineering"),
    ("SCVC生存分析", "SCVC Survival Analysis"),
    ("SCVC文明分析", "SCVC Civilization Analysis"),
    ("SCVC地质分析", "SCVC Geological Analysis"),
    ("SCVC社会工程", "SCVC Social Engineering"),
    ("SCVC哲学社会", "SCVC Philosophy & Society"),
    ("冰河期谎言", "The Ice Age Lie"),
    ("冰河期结束", "End of Ice Age"),
    ("物理谎言", "Physical Lie"),
    ("全球变暖管控方案", "Global Warming Management Plan"),
    ("物理常数的最后通牒", "Ultimatum from Physical Constants"),
    ("大替代", "The Great Replacement"),
    ("大替代方案", "The Great Replacement Plan"),
    ("化石文明的平滑过渡方案", "Smooth Transition Plan for Fossil Civilization"),
    ("末日生存", "Doomsday Survival"),
    ("末日生存不可能", "Doomsday Survival Is Impossible"),
    ("为什么一个人或几个人活不了", "Why Individuals or Small Groups Cannot Survive"),
    ("文明不可重启", "Civilization Cannot Be Restarted"),
    ("煤挖完了就是挖完了", "Coal Gone Is Gone"),
    ("资源不可再生", "Resources Are Non-Renewable"),
    ("容易能量", "Easy Energy"),
    ("过期特价", "Expired Sale Price"),
    ("AI救不了末日", "AI Cannot Save Doomsday"),
    ("信息赢不了物理", "Information Cannot Beat Physics"),
    ("ABC透明战时社会", "ABC Transparent Wartime Society"),
    ("敌人是物理常数，武器是透明", "The Enemy Is Physical Constants; the Weapon Is Transparency"),
    ("ABC完整设计", "ABC Complete Design"),
    ("反向博弈论", "Reverse Game Theory"),
    ("永生是根，反向博弈论是方法", "Immortality Is the Root; Reverse Game Theory Is the Method"),
    ("ABC效率提升", "ABC Efficiency Gains"),
    ("富裕阶层声望量化", "Wealthy Class Reputation Quantification"),
    ("强制合作证明", "Proof of Forced Cooperation"),
    ("ABC普通人收益", "ABC Benefits for Ordinary People"),
    ("痛苦指数", "Misery Index"),
    ("工作量", "Workload"),
    ("AI红利", "AI Dividend"),
    ("全面量化", "Full Quantification"),
    ("永生时间线", "Immortality Timeline"),
    ("ABCvs现代社会", "ABC vs Modern Society"),
    ("长寿逃逸速度", "Longevity Escape Velocity"),
    ("不选ABC的代价", "The Cost of Not Choosing ABC"),
    ("AI经济缺口", "AI Economic Gap"),
    ("终产者陷阱", "The Final Owner Trap"),
    ("资本自毁时间线", "Capital Self-Destruction Timeline"),
    ("单一ABC国家", "Single ABC Nation"),
    ("竞争力差距", "Competitiveness Gap"),
    ("强制变革", "Forced Transformation"),
    ("ABC与意识形态", "ABC and Ideology"),
    ("没有敌人是优势", "Having No Enemy Is an Advantage"),
    ("ABC下的每一种人", "Every Type of Person Under ABC"),
    ("气质多样性自发共存", "How Temperament Diversity Spontaneously Coexists"),
    ("ABC漏洞全面评估", "ABC Comprehensive Vulnerability Assessment"),
    ("合并版", "Merged Edition"),
    ("深层矛盾与最终判决", "Deep Contradictions and Final Verdict"),
    ("ABC内在逻辑矛盾审计", "ABC Internal Logical Contradiction Audit"),
    ("剥离实现，只看涌现逻辑", "Stripping Implementation, Examining Emergent Logic Only"),
    ("生产浪费与资源极限", "Production Waste vs Resource Limits"),
    ("垃圾GDP", "Garbage GDP"),
    ("ABC有用生产100%的物理账本", "ABC 100% Useful Production: The Physical Ledger"),
    ("废墟重建方案", "Ruins Rebuilding Plan"),
    ("ABC最低版本", "ABC Minimum Version"),
    ("知识保存", "Knowledge Preservation"),
    ("文明重启", "Civilization Restart"),
    ("人类能否自我救赎", "Can Humanity Self-Redeem?"),
    ("计算结果 vs 行动概率的诚实评估", "Honest Assessment: Calculations vs Action Probability"),
    ("星际旅行与火星移民", "Interstellar Travel and Mars Migration"),
    ("逃离地球是出路还是幻觉？", "Escape from Earth: Way Out or Illusion?"),
    ("当计算无法说服", "When Calculation Cannot Persuade"),
    ("知识的个人意义", "The Personal Meaning of Knowledge"),
    ("大过滤器", "Great Filter"),
    ("费米悖论", "Fermi Paradox"),
    ("物理常数", "physical constants"),
    ("文明终局", "Civilization Endgame"),
    ("最后窗口", "Final Window"),
    ("末日倒计时", "Doomsday Countdown"),
    ("社会契约", "Social Contract"),
    ("透明社会", "Transparent Society"),
    ("战时社会", "Wartime Society"),
    ("永生", "immortality"),
    ("逃逸速度", "escape velocity"),
]

MASTER.extend(VOL9_EXTRA)

# Vol9 file mapping
VOL9_FILES = [
    ("E201_冰河期谎言.md", "E201_Ice_Age_Lie.md"),
    ("E202_全球变暖管控方案.md", "E202_Global_Warming_Management.md"),
    ("E203_大替代方案.md", "E203_Great_Replacement_Plan.md"),
    ("E204_末日生存不可能.md", "E204_Doomsday_Survival_Impossible.md"),
    ("E205_文明不可重启.md", "E205_Civilization_Cannot_Restart.md"),
    ("E206_资源不可再生.md", "E206_Resources_Non_Renewable.md"),
    ("E207_AI救不了末日.md", "E207_AI_Cannot_Save_Doomsday.md"),
    ("E208_ABC透明战时社会.md", "E208_ABC_Transparent_Wartime_Society.md"),
    ("E209_ABC完整设计_反向博弈论.md", "E209_ABC_Complete_Design_Reverse_Game_Theory.md"),
    ("E210_ABC效率提升_富裕阶层声望量化.md", "E210_ABC_Efficiency_Wealthy_Reputation_Quantification.md"),
    ("E211_ABC普通人收益_工作量_AI红利_全面量化.md", "E211_ABC_Ordinary_People_Benefits_Full_Quantification.md"),
    ("E212_永生时间线_ABCvs现代社会_逃逸速度.md", "E212_Immortality_Timeline_ABC_vs_Modern_Society.md"),
    ("E213_不选ABC的代价_AI经济缺口_终产者陷阱.md", "E213_Cost_of_Not_Choosing_ABC.md"),
    ("E214_单一ABC国家_竞争力差距_强制变革.md", "E214_Single_ABC_Nation_Competitiveness_Gap.md"),
    ("E215_ABC与意识形态_没有敌人是优势.md", "E215_ABC_and_Ideology_No_Enemy_Advantage.md"),
    ("E216_ABC下的每一种人_气质多样性自发共存.md", "E216_Every_Type_Under_ABC_Temperament_Diversity.md"),
    ("E217_ABC漏洞全面评估_合并版.md", "E217_ABC_Vulnerability_Assessment_Merged.md"),
    ("E218_ABC内在逻辑矛盾审计.md", "E218_ABC_Internal_Logic_Contradiction_Audit.md"),
    ("E218附_生产浪费与资源极限.md", "E218_Appendix_Production_Waste_Resource_Limits.md"),
    ("E219_废墟重建方案_ABC最低版本_知识保存_文明重启.md", "E219_Ruins_Rebuilding_ABC_Minimum_Knowledge_Preservation.md"),
    ("E219附_人类能否自我救赎.md", "E219_Appendix_Can_Humanity_Self_Redeem.md"),
    ("E220_星际旅行_火星移民_逃离幻觉.md", "E220_Interstellar_Travel_Mars_Migration_Escape_Illusion.md"),
    ("E220附_当计算无法说服.md", "E220_Appendix_When_Calculation_Cannot_Persuade.md"),
]

src_sub = "卷9_末日倒计时_最后窗口_E201-E220"
dst_sub = "Vol9_Doomsday_Countdown"

count = 0
for src_name, dst_name in VOL9_FILES:
    src_path = os.path.join(cn_base, src_sub, src_name)
    dst_path = os.path.join(en_base, dst_sub, dst_name)
    
    if not os.path.exists(src_path):
        print(f"SKIP (missing): {src_name}")
        continue
    
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    for old, new in MASTER:
        if old in content:
            content = content.replace(old, new)
    
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    cn = len(re.findall(r'[\u4e00-\u9fff]', content))
    count += 1
    print(f"OK: {dst_name} ({cn} CN / {len(content)} total)")

print(f"\nVol9 done: {count} files")
