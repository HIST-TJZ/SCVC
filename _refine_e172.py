import re, os

# Read the cn source and en target
cn_path = r'C:\Users\20606\Desktop\SCVC-github\cn\V3.0\08_工程极限\8.7_391项完整计算\卷5_医学与药物\E172_无毒多靶点癌症封杀.md'
en_path = r'C:\Users\20606\Desktop\SCVC-github\en\V3.0\08_Engineering_Limits\8.7_391_Calculations\Vol5_Medicine_Drugs\E172_Non_Toxic_Multi_Target_Cancer_Lockout.md'

with open(cn_path, 'r', encoding='utf-8') as f:
    cn = f.read()

# Apply all master batch translations first (same as batch_translate_v2.py)
MASTER = []
with open(r'C:\Users\20606\Desktop\SCVC-github\batch_translate_v2.py', 'r', encoding='utf-8') as f:
    exec_text = f.read()
# Extract translations from the MASTER list
import ast
start = exec_text.find('MASTER = [')
end = exec_text.find('\n\n# Files to process')
master_block = exec_text[start:end]
# Parse it safely
local_ns = {}
exec(master_block, {}, local_ns)
MASTER = local_ns['MASTER']

content = cn
for old, new in MASTER:
    if old in content:
        content = content.replace(old, new)

# Additional E172-specific translations
E172_EXTRA = [
    ('SCVC \u533b\u5b66\u5de5\u7a0b  E172  \u65e0\u6bd2\u591a\u9776\u70b9cancer\u5c01\u6740\u2014\u2014\u5f31\u00d7\u591a=\u5f3a',
     'SCVC Medical Engineering  E172  Non-Toxic Multi-Target Cancer Lockout \u2014 Weak \u00d7 Many = Strong'),
    ('\u3010\u8f93\u5165\u5e38\u6570\u3011(\u6765\u81ea _SCVC\u5de5\u7a0b\u5e38\u6570\u901f\u67e5\u8868.md \u53ca E168-E171)',
     '[Input Constants] (from _SCVC Engineering Constants Reference.md and E168-E171)'),
    ('DNA \u805a\u5408\u9176\u901f\u5ea6 \u2248 50 bp/s/\u590d\u5236\u53c9              (E168: S\u671f ~6-8 h \u786c\u5899)',
     'DNA polymerase speed \u2248 50 bp/s/replication fork    (E168: S-phase ~6-8 h hard wall)'),
    ('\u7a81\u53d8\u7387 \u2248 10\u207b\u2079/\u78b1\u57fa/\u4ee3                         (E169: \u03b1 \u2192 H\u952e\u8bc6\u522b\u80fd)',
     'Mutation rate \u2248 10\u207b\u2079/base/generation                (E169: \u03b1 \u2192 H-bond recognition energy)'),
    ('\u6c27\u6269\u6563\u7cfb\u6570 D_O2 \u2248 2\u00d710\u207b\u2079 m\u00b2/s                 (E170: Krogh \u534a\u5f84 ~200 \u03bcm)',
     'Oxygen diffusion coefficient D_O2 \u2248 2\u00d710\u207b\u2079 m\u00b2/s      (E170: Krogh radius ~200 \u03bcm)'),
    ('MHC-I \u6b63\u5e38\u8868\u8fbe ~10\u2075/\u7ec6\u80de, NK \u53bb\u6291\u5236\u9608\u503c ~20-50% (E171: \u53cc\u91cd\u675f\u7f1a)',
     'MHC-I normal expression ~10\u2075/cell, NK disinhibition threshold ~20-50% (E171: double bind)'),
    ('ATP \u4ea7\u91cf: \u6c27\u5316\u78f7\u9178\u5316 ~36 ATP/\u8461\u8404\u7cd6, \u7cd6\u9175\u89e3 ~2 ATP/\u8461\u8404\u7cd6',
     'ATP yield: oxidative phosphorylation ~36 ATP/glucose, glycolysis ~2 ATP/glucose'),
    ('\u7ec6\u80de ATP \u9884\u7b97: ~10\u2079 ATP/s/\u7ec6\u80de (\u5178\u578b), \u5206\u88c2\u6210\u672c ~10\u00b9\u2070 ATP',
     'Cellular ATP budget: ~10\u2079 ATP/s/cell (typical), division cost ~10\u00b9\u2070 ATP'),
    ('\u86cb\u767d\u8d28\u5408\u6210\u6210\u672c: ~4 ATP/\u6c28\u57fa\u9178, \u5e73\u5747\u86cb\u767d\u8d28 ~400 aa \u2192 ~1600 ATP',
     'Protein synthesis cost: ~4 ATP/amino acid, average protein ~400 aa \u2192 ~1600 ATP'),
    ('\u03b1 = 1/137.0363', '\u03b1 = 1/137.0363'),
]

for old, new in E172_EXTRA:
    if old in content:
        content = content.replace(old, new)

# Count remaining Chinese
cn_count = len(re.findall(r'[\u4e00-\u9fff]', content))
print(f'Remaining Chinese after E172_EXTRA: {cn_count} / {len(content)}')

with open(en_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('E172 written.')
