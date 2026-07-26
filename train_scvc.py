import os, json, torch
from transformers import (
    AutoModelForCausalLM, AutoTokenizer,
    TrainingArguments, Trainer, DataCollatorForSeq2Seq
)
from peft import LoraConfig, get_peft_model, TaskType
from datasets import Dataset

MODEL_PATH = './models/models/qwen--Qwen2.5-0.5B-Instruct/snapshots/master'
DATA_FILE = r'C:\Users\20606\Desktop\SCVC-github\scvc_qa_final.jsonl'
OUTPUT_DIR = './scvc_lora_0.5b'
SYSTEM_PROMPT = '你基于几何约束框架推理。追溯物理现象到几何锚。不自洽的推导自动排除。无法追溯的问题诚实说无法得到结果。'

print('=== SCVC LoRA Training ===')

print('\n[1/4] Loading model...')
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH, torch_dtype=torch.float32, device_map='cpu', trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

print('\n[2/4] Applying LoRA...')
lora_config = LoraConfig(
    r=8, lora_alpha=16,
    target_modules=['q_proj', 'k_proj', 'v_proj', 'o_proj'],
    lora_dropout=0.05, bias='none', task_type=TaskType.CAUSAL_LM,
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

print('\n[3/4] Loading data...')
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    raw_data = [json.loads(line) for line in f if line.strip()]

def fmt(ex):
    return {
        'text': f'<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n<|im_start|>user\n{ex["instruction"]}<|im_end|>\n<|im_start|>assistant\n{ex["output"]}<|im_end|>'
    }

dataset = Dataset.from_list(raw_data).map(fmt)

def tok(examples):
    t = tokenizer(examples['text'], truncation=True, max_length=512)
    t['labels'] = [ids.copy() for ids in t['input_ids']]
    return t

dataset = dataset.map(tok, batched=True, remove_columns=['text','instruction','input','output'])
print(f'Loaded {len(dataset)} samples')

print('\n[4/4] Training...')
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR, per_device_train_batch_size=1,
    gradient_accumulation_steps=4, num_train_epochs=2,
    learning_rate=2e-4, fp16=False, logging_steps=20,
    save_strategy='epoch', save_total_limit=2,
    report_to='none', remove_unused_columns=False,
)

trainer = Trainer(
    model=model, args=training_args, train_dataset=dataset,
    data_collator=DataCollatorForSeq2Seq(tokenizer, model=model, padding=True),
)
trainer.train()
model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print(f'\nDone! Saved to {OUTPUT_DIR}')

print('\n=== Quick Test ===')
model.eval()
test = '精细结构常数alpha的数值是多少？'
fmt_test = f'<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n<|im_start|>user\n{test}<|im_end|>\n<|im_start|>assistant\n'
inputs = tokenizer(fmt_test, return_tensors='pt')
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=150, temperature=0.1, do_sample=True)
result = tokenizer.decode(outputs[0], skip_special_tokens=True)
if '<|im_start|>assistant' in result:
    result = result.split('<|im_start|>assistant')[-1].strip()
print(f'Q: {test}')
print(f'A: {result[:300]}')
