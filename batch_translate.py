import os, sys, re

cn_base = r"C:\Users\20606\Desktop\SCVC-github\cn\V3.0\08_工程极限\8.7_391项完整计算"
en_base = r"C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations"

# Master translation dictionary - ordered by specificity (longer matches first)
MASTER = [
    # === Headers and titles ===
    ("SCVC工程极限", "SCVC Engineering Limit"),
    ("基于**：`_SCVC工程常数速查表.md` (全π多项式推导，零自由参数，2.22 ppm精度)", "Based on: `_SCVC Engineering Constants Reference.md` (all-π-polynomial derivation, zero free parameters, 2.22 ppm precision)"),
    ("基于", "Based on"),
    ("计算日期", "Calculation Date"),
    ("所有推导基于SCVC常数速查表（零自由参数，α=1/(4π³+π²+π)）。", "All derivations are based on the SCVC constant reference table (zero free parameters, α=1/(4π³+π²+π))."),
    ("工程师可直接使用结论，无需理解SCVC几何推导。", "Engineers may directly use the conclusions without understanding the SCVC geometric derivation."),
    
    # === Common section headers ===
    ("工程结论", "Engineering Conclusions"),
    ("速查决策表", "Quick-Reference Decision Table"),
    ("禁区判定", "Forbidden-Zone Determination"),
    ("附录：计算细节", "Appendix: Calculation Details"),
    ("工程意义", "Engineering Significance"),
    ("核心主张", "Core Claim"),
    ("共同特征", "Common Features"),
    ("和其他领域的区别", "Comparison with Other Domains"),
    ("目标温区分级", "Target Temperature Zone Classification"),
    ("最接近极限的材料路线", "Material Routes Closest to the Limit"),
    ("可行性评估", "Feasibility Assessment"),
    ("物理极限 vs 工程现实", "Physical Limit vs. Engineering Reality"),
    ("终极答案", "Ultimate Answers"),
    ("绝对理论上限", "Absolute Theoretical Upper Bound"),
    ("SCVC的判断", "SCVC Judgment"),
    ("SCVC判定", "SCVC Verdict"),
    ("SCVC硬输入", "SCVC Hard Inputs"),
    ("SCVC 输入参数", "SCVC Input Parameters"),
    ("SCVC定量约束", "SCVC Quantitative Constraints"),
    ("SCVC的推导链", "SCVC Derivation Chain"),
    ("能量标度判定", "Energy-Scale Assessment"),
    ("什么是真正的限制？", "What Are the Real Constraints?"),
    ("非声子配对机制", "Non-Phonon Pairing Mechanisms"),
    ("理论抗拉强度", "Theoretical Tensile Strength"),
    ("比强度（强度/密度）", "Specific Strength (Strength / Density)"),
    ("杨氏模量上限", "Young Modulus Ceiling"),
    ("催化活化能下限", "Catalytic Activation Energy Lower Bound"),
    ("电催化上限", "Electrocatalysis Ceiling"),
    ("电催化过电位总汇", "Electrocatalysis Overpotential Summary"),
    ("光催化", "Photocatalysis"),
    ("已接近SCVC极限的反应（改进空间 < 2×）", "Reactions Already Near SCVC Limits (improvement headroom < 2×)"),
    ("有数量级提升空间的反应", "Reactions With Order-of-Magnitude Headroom"),
    ("催化剂设计方向（来自SCVC约束）", "Catalyst Design Directions (from SCVC Constraints)"),
    ("不应该追求的方向", "Directions Not Worth Pursuing"),
    ("路线建议", "Route Recommendations"),
    ("可行性判定", "Feasibility Assessment"),
    ("物理允许性", "Physical Permissibility"),
    
    # === Table headers ===
    ("物理量", "Quantity"),
    ("符号", "Symbol"),
    ("实验", "Experiment"),
    ("偏差", "Deviation"),
    ("状态", "Status"),
    ("参数", "Parameter"),
    ("值", "Value"),
    ("来源", "Source"),
    ("排名", "Rank"),
    ("材料", "Material"),
    ("类型", "Type"),
    ("判据", "Verdict"),
    ("评估", "Assessment"),
    ("差距", "Gap"),
    ("问题", "Question"),
    ("SCVC 答案", "SCVC Answer"),
    ("当前最优", "Current Best"),
    ("SCVC极限", "SCVC Limit"),
    ("当前水平", "Current Level"),
    ("SCVC允许", "SCVC Permits"),
    ("距极限差距", "Gap to Limit"),
    ("反应", "Reaction"),
    ("当前最佳", "Current Best"),
    ("天花板", "Ceiling"),
    ("触达", "Reached"),
    ("停滞", "Stalled"),
    ("一直以来的解释", "Conventional Explanation"),
    ("你的领域一直在试图", "What Your Field Keeps Trying"),
    ("温区", "Temperature Zone"),
    ("温度", "Temperature"),
    ("物理判定", "Physical Verdict"),
    ("材料路线", "Material Route"),
    ("结论", "Conclusion"),
    ("内容", "Content"),
    ("方向", "Direction"),
    ("SCVC 贡献", "SCVC Contribution"),
    ("行动建议", "Action Recommendation"),
    ("需要新技术吗", "Requires New Technology?"),
    
    # === Status markers ===
    ("精确", "exact"),
    ("几何基准", "geometric baseline"),
    ("预言", "prediction"),
    ("可证伪", "falsifiable"),
    ("推导", "derived"),
    ("已实现", "Achieved"),
    ("已成熟", "mature"),
    ("发展中", "developing"),
    ("物理允许", "Physically permitted"),
    ("不可逾越的墙", "Insurmountable wall"),
    ("已锁定", "Locked"),
    ("正在关闭", "Closing"),
    ("仍可避免", "Still Avoidable"),
    ("物理允许性", "Physical Permissibility"),
    
    # === Common phrases ===
    ("速查表", "reference table"),
    ("键能", "bond energy"),
    ("键长", "bond length"),
    ("力常数", "force constant"),
    ("验证", "Verification"),
    ("理论值", "theoretical value"),
    ("实验值", "experimental value"),
    ("实验最佳", "Best Experimental"),
    ("无实验", "No experiment"),
    ("理论/实验", "Theory/Experiment"),
    ("缺陷折减", "defect reduction"),
    ("约", "approximately"),
    ("当前", "Current"),
    ("物理允许", "Physically permitted"),
    ("接近极限", "Near limit"),
    ("触顶", "At ceiling"),
    ("极小", "Minimal"),
    ("中等", "Moderate"),
    ("注释", "Note"),
    ("注：", "Note: "),
    ("条件：", "Conditions:"),
    ("结论：", "Conclusion:"),
    
    # === Verification path ===
    ("你的验证路径", "Your Verification Path"),
    ("验推导链", "Verify the derivation chain"),
    ("找反例", "Find counterexamples"),
    ("找推导链裂缝", "Find cracks in the derivation chain"),
    ("一个反例就够了。", "One counterexample suffices."),
    ("一个就可以", "Just one will do"),
    
    # === Cross-file standard phrases ===
    ("如果 §2 的推导正确", "If §2 Derivation Is Correct"),
    ("你认得这些", "What You Recognize"),
    ("本文所有数值上限来自SCVC常数的理论推导，不代表工程可实现性。", "All numerical ceilings in this document are derived from SCVC constant theory and do not represent engineering realizability."),
    ("SCVC 常数精度 2.22 ppm，相应推导误差在可忽略量级。", "SCVC constant precision is 2.22 ppm; corresponding derivation errors are negligible."),
    ("所有物理极限均由 SCVC 工程常数速查表提供的键能/键长/力常数推导。任何超过这些极限的声称将意味着超越已知物理。", "All physical limits are derived from bond energies / bond lengths / force constants provided by the SCVC Engineering Constants Reference. Any claim exceeding these limits would imply surpassing known physics."),
    ("催化极限由标度关系决定，而标度关系来自化学键的普遍性。", "Catalysis limits are determined by scaling relations, which arise from the universality of chemical bonds."),
    ("SCVC框架将键能锁定在3.6-9.8 eV，由此导出所有催化边界。", "The SCVC framework locks bond energies at 3.6-9.8 eV, from which all catalytic boundaries are derived."),
    
    # === Standard footer ===
    ("* 本文所有数值上限来自SCVC常数的理论推导，不代表工程可实现性。", "* All numerical ceilings in this document are derived from SCVC constant theory and do not represent engineering realizability."),
    ("* SCVC 常数精度 2.22 ppm，相应推导误差在可忽略量级。", "* SCVC constant precision is 2.22 ppm; corresponding derivation errors are negligible."),
]

# File listing: (source_subdir, source_filename, dest_subdir, dest_filename)
FILES = [
    # Vol1 - Materials & Structures
    ("卷1_材料与结构", "E1_超导_Tc上限.md", "Vol1_Materials_Structures", "E1_Superconducting_Tc_Ceiling.md"),
    ("卷1_材料与结构", "E4_结构材料上限.md", "Vol1_Materials_Structures", "E4_Structural_Materials_Ceiling.md"),
    ("卷1_材料与结构", "E5_催化上限.md", "Vol1_Materials_Structures", "E5_Catalysis_Ceiling.md"),
    ("卷1_材料与结构", "E6_磁性材料上限.md", "Vol1_Materials_Structures", "E6_Magnetic_Materials_Ceiling.md"),
    ("卷1_材料与结构", "E9_航天推进上限.md", "Vol1_Materials_Structures", "E9_Space_Propulsion_Ceiling.md"),
    ("卷1_材料与结构", "E33_反应速率Arrhenius上限.md", "Vol1_Materials_Structures", "E33_Reaction_Rate_Arrhenius_Ceiling.md"),
    ("卷1_材料与结构", "E42_火箭复用上限.md", "Vol1_Materials_Structures", "E42_Rocket_Reusability_Ceiling.md"),
    ("卷1_材料与结构", "E56_最高熔点.md", "Vol1_Materials_Structures", "E56_Maximum_Melting_Point.md"),
    ("卷1_材料与结构", "E57_最大热导率.md", "Vol1_Materials_Structures", "E57_Maximum_Thermal_Conductivity.md"),
    ("卷1_材料与结构", "E163_催化剂TOF上限.md", "Vol1_Materials_Structures", "E163_Catalyst_TOF_Ceiling.md"),
    # Vol2 - Electronics & Computing
    ("卷2_电子与计算", "E8_量子计算上限.md", "Vol2_Electronics_Computing", "E8_Quantum_Computing_Ceiling.md"),
    ("卷2_电子与计算", "E44_AI训练能耗上限.md", "Vol2_Electronics_Computing", "E44_AI_Training_Energy_Ceiling.md"),
    ("卷2_电子与计算", "E48_晶体管能耗上限.md", "Vol2_Electronics_Computing", "E48_Transistor_Energy_Ceiling.md"),
    ("卷2_电子与计算", "E49_芯片频率上限.md", "Vol2_Electronics_Computing", "E49_Chip_Frequency_Ceiling.md"),
    ("卷2_电子与计算", "E15_计算物理上限.md", "Vol2_Electronics_Computing", "E15_Computation_Physics_Ceiling.md"),
    ("卷2_电子与计算", "E26_脑机接口上限.md", "Vol2_Electronics_Computing", "E26_Brain_Computer_Interface_Ceiling.md"),
    ("卷2_电子与计算", "E60_光子通信上限.md", "Vol2_Electronics_Computing", "E60_Photonic_Communication_Ceiling.md"),
    ("卷2_电子与计算", "E160_量子比特相干时间.md", "Vol2_Electronics_Computing", "E160_Qubit_Coherence_Time.md"),
    ("卷2_电子与计算", "E164_DNA存储密度上限.md", "Vol2_Electronics_Computing", "E164_DNA_Storage_Density_Ceiling.md"),
    ("卷2_电子与计算", "E14_光学光子学上限.md", "Vol2_Electronics_Computing", "E14_Optics_Photonics_Ceiling.md"),
    # Vol3 - Energy & Environment
    ("卷3_能源与环境", "E3_光伏半导体上限.md", "Vol3_Energy_Environment", "E3_Photovoltaic_Semiconductor_Ceiling.md"),
    ("卷3_能源与环境", "E159_核聚变Q值上限.md", "Vol3_Energy_Environment", "E159_Fusion_Q_Value_Ceiling.md"),
    ("卷3_能源与环境", "E22_电池快充上限.md", "Vol3_Energy_Environment", "E22_Battery_Fast_Charge_Ceiling.md"),
    ("卷3_能源与环境", "E41_碳捕获上限.md", "Vol3_Energy_Environment", "E41_Carbon_Capture_Ceiling.md"),
    ("卷3_能源与环境", "E40_制氢上限.md", "Vol3_Energy_Environment", "E40_Hydrogen_Production_Ceiling.md"),
    ("卷3_能源与环境", "E7_核能上限.md", "Vol3_Energy_Environment", "E7_Nuclear_Energy_Ceiling.md"),
    ("卷3_能源与环境", "E2_化学储能上限.md", "Vol3_Energy_Environment", "E2_Chemical_Energy_Storage_Ceiling.md"),
    ("卷3_能源与环境", "E161_碳捕集最小能量.md", "Vol3_Energy_Environment", "E161_Carbon_Capture_Minimum_Energy.md"),
    # Vol4 - Human Biophysics
    ("卷4_人类生物物理", "E88_最大寿命上限.md", "Vol4_Human_Biophysics", "E88_Maximum_Lifespan_Ceiling.md"),
    ("卷4_人类生物物理", "E28_神经传导速度上限.md", "Vol4_Human_Biophysics", "E28_Nerve_Conduction_Velocity_Ceiling.md"),
    ("卷4_人类生物物理", "E96_自由意志.md", "Vol4_Human_Biophysics", "E96_Free_Will.md"),
    ("卷4_人类生物物理", "E99_意识是什么.md", "Vol4_Human_Biophysics", "E99_What_Is_Consciousness.md"),
    ("卷4_人类生物物理", "E82_语言信息率上限.md", "Vol4_Human_Biophysics", "E82_Language_Information_Rate_Ceiling.md"),
    ("卷4_人类生物物理", "E69_肌肉功率上限.md", "Vol4_Human_Biophysics", "E69_Muscle_Power_Ceiling.md"),
]

print(f"Starting batch translation of {len(FILES)} files...")
print(f"Master dictionary has {len(MASTER)} entries")

for src_sub, src_name, dst_sub, dst_name in FILES:
    src_path = os.path.join(cn_base, src_sub, src_name)
    dst_path = os.path.join(en_base, dst_sub, dst_name)
    
    if not os.path.exists(src_path):
        print(f"SKIP (missing): {src_name}")
        continue
    
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Apply master translations (longer strings first to avoid partial matches)
    for old, new in MASTER:
        content = content.replace(old, new)
    
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"OK: {dst_name}")

print(f"\n=== Batch complete: {len(FILES)} files ===")
