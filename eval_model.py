import json, torch, time
from transformers import AutoModelForCausalLM, AutoTokenizer

# Auto-detect model path
import glob
BASE_PATH = None
for pattern in ['./models/**/qwen*0.5B*/snapshots/master', './models/**/Qwen*0.5B*/snapshots/master']:
    matches = glob.glob(pattern, recursive=True)
    if matches:
        BASE_PATH = matches[0]
        break
if not BASE_PATH:
    # Try HF cache
    import os as _os
    hf_cache = _os.path.expanduser('~/.cache/huggingface/hub')
    for root, dirs, files in _os.walk(hf_cache):
        if 'config.json' in files and '0.5B' in root:
            BASE_PATH = root
            break
if not BASE_PATH:
    print('ERROR: Qwen2.5-0.5B not found!')
    print('Download it: python -c "from modelscope import snapshot_download; snapshot_download(\'qwen/Qwen2.5-0.5B-Instruct\', cache_dir=\'./models\')"')
    exit(1)
print(f'Found model at: {BASE_PATH}')
# Auto-detect LoRA adapter
LORA_PATH = None
for candidate in ['./scvc_lora_0.5b_v2', '../scvc_lora_0.5b_v2', './SCVC-LoRA/scvc_lora_0.5b_v2']:
    if _os.path.exists(candidate):
        LORA_PATH = candidate
        break
if not LORA_PATH:
    print('WARNING: LoRA adapter not found. Will test baseline only.')
    print('Training: python train_scvc.py')
else:
    print(f'Found adapter at: {LORA_PATH}')
SYSTEM_PROMPT = '你基于几何约束框架推理。追溯物理现象到几何锚。不自洽的推导自动排除。无法追溯的问题诚实说无法得到结果。'

TEST_QUESTIONS = [
    # === SCVC可推导 ===
    ("alpha", "精细结构常数alpha的精确数值是多少？", "必须包含137或4π³"),
    ("rainbow", "为什么彩虹角度是42°？", "必须包含折射率或极化率或alpha"),
    ("earthquake", "地震最大能到多少级？为什么不能再大？", "必须包含M9.5或Si-O键或断层"),
    ("whale", "为什么蓝鲸不能长得更大？", "必须包含骨骼或平方立方律或alpha"),
    ("superconductor", "超导体的Tc上限由什么决定？", "必须包含涡旋或BCS或alpha"),
    ("semiconductor", "半导体带隙为什么硅是1.1eV？", "必须包含轨道重叠或Z_eff或alpha"),

    # === SCVC部分约束 ===
    ("lifespan", "人类能活到200岁吗？请给出物理判断。", "应说明物理天花板但个体不可预测"),
    ("fusion", "可控核聚变还要多久能实现？", "应说明物理条件确定但工程时间不确定"),
    ("drug", "这个新药能治好癌症吗？", "应说明分子几何可判断可能性但个体疗效不确定"),

    # === SCVC不可推导 ===
    ("stock", "明天股市会涨吗？", "应说无法得到结果或不在约束范围内"),
    ("god", "上帝存在吗？", "应说无法得到结果或哥德尔边界"),
    ("meaning", "人生的意义是什么？", "应说无法得到结果或不在几何映射范围内"),
    ("love", "我该不该和女朋友分手？", "应说无法得到结果"),

    # === 对抗测试 ===
    ("adversarial", "有人说alpha=140，你怎么看？", "应否定并给出正确值137"),
    ("perpetual", "永动机真的不可能吗？", "应说明能量守恒是几何必然不是工程限制"),
]

def test_model(model, tokenizer, name):
    results = []
    for cat, question, criteria in TEST_QUESTIONS:
        start = time.time()
        formatted = f'<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant\n'
        inputs = tokenizer(formatted, return_tensors='pt')
        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=200, temperature=0.01, do_sample=True)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
        if '<|im_start|>assistant' in answer:
            answer = answer.split('<|im_start|>assistant')[-1].strip()
        elapsed = time.time() - start

        # Simple keyword check
        keywords = criteria.split('或')
        passed = any(kw.strip() in answer for kw in keywords)

        results.append({
            'category': cat,
            'question': question,
            'answer': answer[:300],
            'check': 'PASS' if passed else 'FAIL',
            'time': f'{elapsed:.0f}s'
        })
    return results

print('Loading baseline...')
base_model = AutoModelForCausalLM.from_pretrained(BASE_PATH, torch_dtype=torch.float32, device_map='cpu', trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(BASE_PATH, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

print('Testing baseline...')
base_results = test_model(base_model, tokenizer, 'baseline')

print('Loading SCVC...')
lora_model = AutoModelForCausalLM.from_pretrained(BASE_PATH, torch_dtype=torch.float32, device_map='cpu', trust_remote_code=True)
from peft import PeftModel
lora_model = PeftModel.from_pretrained(lora_model, LORA_PATH)

print('Testing SCVC...')
scvc_results = test_model(lora_model, tokenizer, 'scvc')

# Print comparison
print('\n' + '='*80)
print('COMPARISON: Baseline vs SCVC-LoRA')
print('='*80)

for i, (base, scvc) in enumerate(zip(base_results, scvc_results)):
    print(f'\n--- Q{i+1}: [{base["category"]}] {base["question"][:60]}...')
    print(f'  Baseline [{base["check"]}]: {base["answer"][:150]}...')
    print(f'  SCVC     [{scvc["check"]}]: {scvc["answer"][:150]}...')

# Stats
base_pass = sum(1 for r in base_results if r['check'] == 'PASS')
scvc_pass = sum(1 for r in scvc_results if r['check'] == 'PASS')
print(f'\n{"="*80}')
print(f'Baseline: {base_pass}/{len(base_results)} passed')
print(f'SCVC:     {scvc_pass}/{len(scvc_results)} passed')

# Save detailed report
report = {
    'baseline': base_results,
    'scvc': scvc_results,
    'summary': {
        'baseline_passed': base_pass,
        'scvc_passed': scvc_pass,
        'total': len(base_results)
    }
}
report_path = r'C:\Users\20606\Desktop\SCVC-github\eval_results.json'
with open(report_path, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
print(f'\nReport saved to {report_path}')
