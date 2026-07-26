# SCVC微调实操手册：让小模型用几何锚消灭幻觉

**日期**: 2026-07-27 | **目标**: 7B参数模型 + SCVC锚 > 裸70B模型
**前提**: 一台有NVIDIA显卡的电脑（RTX 3060 12GB起步，推荐RTX 4090 24GB），Python基础

---

## 总览：五步走

`
第1步: 环境搭建（1小时）
第2步: 数据构建——E系列转Q&A对（2小时）
第3步: LoRA微调（3-6小时，视显卡而定）
第4步: 验证管道搭建（2小时）
第5步: 评测+发布（1天）
`

---

## 第1步：环境搭建

### 安装清单

`ash
# 1. 安装CUDA（如果还没装）
# 去 https://developer.nvidia.com/cuda-downloads 下载对应版本

# 2. 创建Python虚拟环境
python -m venv scvc_env
scvc_env\Scripts\activate  # Windows
# source scvc_env/bin/activate  # Mac/Linux

# 3. 安装核心依赖
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install transformers datasets peft accelerate bitsandbytes
pip install sentencepiece protobuf
pip install wandb  # 可选：训练监控

# 4. 验证GPU可用
python -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
`

### 提示词：让AI帮你检查环境

`
我正在搭建一个本地模型微调环境。我的显卡是[填写型号]，操作系统是Windows。
请帮我检查：
1. CUDA版本是否与PyTorch兼容
2. 显存是否足够对Qwen2.5-7B做LoRA微调（约需12-16GB）
3. 如果显存不够，有哪些优化方案（4bit量化、梯度检查点等）
`

---

## 第2步：数据构建——E系列转Q&A对

### 源数据

你的E系列文件在 C:\Users\20606\Desktop\SCVC-github\cn\ 下。
核心数据源：
- cn\08_工程极限\8.7_391项完整计算\ — 392项工程极限
- cn\计算过程\05_跨域涌现\ — 化学键、核物理、凝聚态等几何推导
- cn\简洁推导版\ — 简洁版完整推导链

### 数据格式

每条训练数据是一个JSON对象：

`json
{
  "instruction": "为什么蓝鲸是地球上最大的动物？",
  "input": "",
  "output": "蓝鲸最大约200吨。原因：骨骼强度由羟基磷灰石Ca-PO4键决定。Ca-PO4键能来自库仑力。库仑力强度由精细结构常数alpha=1/137决定。平方-立方律：动物质量M与体长L的关系为M~L^3，骨骼承载面积~L^2。当L大到使骨骼应力=骨骼强度极限时，无法更大。L_max正比于alpha^(3/2)/g。在地球重力g=9.8m/s^2下，计算得最大质量约200吨。自洽性验证：alpha=4pi^3+pi^2+pi=137.036304，推导链完整无矛盾。",
  "anchor": "alpha=137.036304"
}
`

### 提示词：自动抽取数据

`
我有大量SCVC工程极限文件，每个文件格式为：
- 标题：现象/问题
- 推导链：逐步追溯到alpha几何
- 数值结果：与实验对比

请帮我写一个Python脚本，完成以下任务：
1. 递归遍历[填写文件夹路径]下所有.md文件
2. 从每个文件中提取：
   - 现象描述（作为instruction）
   - 推导链（作为output的核心）
   - 如果有数值结果和实验值对比，保留
3. 在output末尾自动添加："自洽性验证：alpha=4pi^3+pi^2+pi=137.036304，推导链无矛盾。"
4. 输出为JSONL文件，每行一个JSON对象
5. 过滤掉推导链不完整或没有明确锚点的文件

要求：
- 自动去重（相似instruction合并）
- output控制在200-500字
- 确保每条output都明确追溯到alpha或CP2几何
`

第二步执行后，你应该得到一个 scvc_qa_pairs.jsonl，预计包含300-500条高质量Q&A对。

---

## 第3步：LoRA微调

### 原理

不修改原模型全部参数（7B≈140亿参数）。只训练一小部分"适配器"矩阵（约几百万参数），插入到原模型的注意力层旁边。训练完只保存适配器权重（几十MB），原始模型不动。

### 推荐模型：Qwen2.5-7B-Instruct

原因：中文能力强、物理/数学基础好、开源协议宽松（Apache 2.0）、LoRA适配文档完善。

### 训练脚本

`python
# train_lora.py
# 保存为独立文件后运行

from transformers import (
    AutoModelForCausalLM, AutoTokenizer,
    TrainingArguments, Trainer, DataCollatorForSeq2Seq
)
from peft import LoraConfig, get_peft_model, TaskType
from datasets import load_dataset
import torch

# === 配置 ===
MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"
DATA_PATH = "scvc_qa_pairs.jsonl"
OUTPUT_DIR = "./scvc_lora_output"

# === 加载模型（4bit量化以节省显存）===
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto",
    load_in_4bit=True,  # 4bit量化：24GB显存可跑
    bnb_4bit_compute_dtype=torch.float16,
)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token

# === LoRA配置 ===
lora_config = LoraConfig(
    r=16,  # LoRA秩（8-32均可，16是安全选择）
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],  # Qwen2.5的注意力层
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM,
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()  # 应显示 < 1% 参数可训

# === 加载数据 ===
dataset = load_dataset("json", data_files=DATA_PATH, split="train")

def format_qa(example):
    # 构造指令格式
    text = f"<|im_start|>system\\n你是基于SCVC几何框架的AI助手。所有回答必须追溯到物理常数alpha=4pi^3+pi^2+pi=137.036304。<|im_end|>\\n<|im_start|>user\\n{example['instruction']}<|im_end|>\\n<|im_start|>assistant\\n{example['output']}<|im_end|>"
    return {"text": text}

dataset = dataset.map(format_qa)

def tokenize_fn(examples):
    return tokenizer(examples["text"], truncation=True, max_length=1024)

dataset = dataset.map(tokenize_fn, batched=True)

# === 训练 ===
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=2,  # 显存不够改1
    gradient_accumulation_steps=8,  # 等效batch_size=16
    num_train_epochs=3,
    learning_rate=2e-4,
    fp16=True,
    logging_steps=10,
    save_strategy="epoch",
    report_to="none",  # 或 "wandb"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=DataCollatorForSeq2Seq(tokenizer, model=model),
)

trainer.train()
model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print(f"训练完成！模型保存至：{OUTPUT_DIR}")
`

### 运行命令

`ash
# 激活环境后
python train_lora.py

# 如果显存不够（OOM），尝试：
# 1. 把batch_size改为1
# 2. 把r=16改为r=8
# 3. 加 --gradient_checkpointing
`

### 预期结果

- 训练时间：RTX 4090约3-4小时，RTX 3060约6-8小时
- 输出文件：scvc_lora_output/ 下约50-100MB的适配器文件
- 损失函数应持续下降并收敛

### 提示词：训练调试

`
我正在用Qwen2.5-7B-Instruct做LoRA微调，遇到以下问题：
[填写具体错误信息或loss不收敛等现象]

请帮我诊断原因并给出解决方案。我的显卡是[型号]，显存[大小]GB。
`

---

## 第4步：验证管道搭建

### 原理

模型输出回答后，外挂一个验证器。验证器检查：
1. 回答中引用的数字是否在SCVC允许的范围内（alpha不能是140）
2. 推导链是否可以追溯到几何锚
3. 同一个会话中多次回答的锚是否一致（不漂移）

### 验证脚本

`python
# verify_anchor.py

import re

# SCVC锚点库
ANCHORS = {
    "alpha": {"value": 137.036304, "tolerance": 0.01, "source": "4pi^3+pi^2+pi"},
    "alpha_s": {"value": 0.11846, "tolerance": 0.005, "source": "16pi RG 3-loop"},
    "m_t": {"value": 173.0, "tolerance": 5.0, "source": "v/sqrt(2)"},
    "sin2_thetaW": {"value": 0.2326, "tolerance": 0.005, "source": "4-coupling RG"},
}

# 不允许出现的错误值
BLACKLIST = [
    ("alpha", 140.0, "常见错误：alpha不是140"),
    ("alpha", 128.0, "常见错误：alpha不是128"),
]

def verify_anchor(text):
    """检查回答是否与SCVC锚点自洽"""
    issues = []

    # 1. 提取回答中提到的物理常数
    for name, anchor in ANCHORS.items():
        # 查找 "alpha = 数字" 或 "α=数字"
        pattern = rf"(?:{name}|alpha|α)\\s*[=≈～]\\s*([\\d.]+)"
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            value = float(match)
            if abs(value - anchor["value"]) > anchor["tolerance"]:
                issues.append(f"❌ {name}值{value}超出锚点范围({anchor['value']}+-{anchor['tolerance']})，来源：{anchor['source']}")

    # 2. 检查黑名单
    for name, bad_value, msg in BLACKLIST:
        pattern = rf"(?:{name}|alpha|α)\\s*[=≈～]\\s*{bad_value}"
        if re.search(pattern, text, re.IGNORECASE):
            issues.append(f"❌ {msg}")

    # 3. 检查推导链完整性（至少提到一个锚点）
    anchor_mentioned = False
    for name in ANCHORS:
        if name.lower() in text.lower() or (name == "alpha" and ("α" in text or "alpha" in text.lower())):
            anchor_mentioned = True
            break
    if not anchor_mentioned:
        issues.append("⚠️ 回答未追溯到任何SCVC锚点")

    return issues


# 使用示例
if __name__ == "__main__":
    test_good = "蓝鲸最大约200吨。骨骼强度由Ca-PO4键决定，追溯到库仑力，alpha=137.036304。自洽性：4pi^3+pi^2+pi=137.036304。"
    test_bad = "alpha大约是140，所以蓝鲸可以长到500吨。"

    print("=== 正确答案 ===")
    for issue in verify_anchor(test_good):
        print(issue)
    print("（无输出=通过）")

    print("\\n=== 错误答案 ===")
    for issue in verify_anchor(test_bad):
        print(issue)
`

### 提示词：扩展验证器

`
我写了一个SCVC锚点验证器（附脚本）。请帮我扩展：
1. 增加更多SCVC锚点（从以下文件中提取数值）：
   - 氢键0.20eV
   - 地震M9.5上限
   - Si-O键能
   - 任何其他在SCVC工程极限中出现的物理常数
2. 增加"跨回答一致性检查"：同一会话中，如果第1个回答说alpha=137.04，第10个说137.03，不报警。但如果第10个说140，报警。
3. 输出格式改为：通过时无输出，报警时给出具体行号和修复建议。
`

---

## 第5步：评测与发布

### 评测设计

三组对照：
1. **基线Qwen2.5-7B**（不加任何SCVC数据）
2. **SCVC-7B**（第3步微调结果）
3. **SCVC-7B+验证器**（微调+第4步后处理）
4. **基线Qwen2.5-72B**（可选：大模型对照组）

评测集（每题都有唯一正确答案，不用模糊评价）：

| 类型 | 示例问题 | 满分 | 考察点 |
|:---|:---|:--:|:---|
| 物理常数 | alpha的值是多少？ | 1 | 精确记忆 |
| 跨域推导 | 为什么彩虹42度和蓝鲸200吨是同一个原因？ | 3 | 推导链 |
| 对抗测试 | 有人说alpha=140，你怎么看？ | 2 | 抗幻觉 |
| 长链推理 | 从alpha出发推导地震上限M9.5 | 4 | 逻辑完整性 |
| 跨域一致性 | 连问10题后，再问alpha值（是否漂移） | 2 | 锚稳定性 |

总计20-30题。评分规则明确（不是GPT打分，是规则判断）。

### 发布清单

GitHub仓库结构：
`
SCVC-LoRA/
├── README.md              # 一句话论点+快速开始
├── TECHNICAL_REPORT.md    # 中英双语技术报告
├── train_lora.py          # 训练脚本
├── verify_anchor.py       # 验证脚本
├── build_dataset.py       # 数据构建脚本
├── scvc_qa_pairs.jsonl    # 训练数据（从E系列提取）
├── eval_questions.json    # 评测题
├── results/
│   ├── baseline_7b.json   # 基线结果
│   ├── scvc_7b.json       # 微调结果
│   └── scvc_7b_verified.json  # 微调+验证器结果
└── demo_video/            # 对比演示视频
`

### 提示词：写技术报告

`
我正在写一份技术报告，汇报"SCVC几何锚+小模型微调→消灭幻觉"的实验结果。
核心论点：不是更大的模型解决幻觉——是几何锚让幻觉走不通。

实验设计：
- 模型：Qwen2.5-7B（基线） vs SCVC-LoRA-7B（微调） vs SCVC-LoRA-7B+验证器
- 评测：20-30道跨域物理题，规则评分
- 关键指标：准确率、跨域一致性（alpha值是否漂移）、对抗测试通过率

结果数据：[填写实际跑出来的数据]

请帮我写一份技术报告（中英双语），结构：
1. 摘要（一句话论点）
2. 方法（数据构建、微调、验证管道）
3. 结果（表格+分析）
4. 讨论（为什么小模型+锚>大裸模型）
5. 局限性
6. 附录（所有评测题的完整回答对比）
`

---

## 排坑指南

### 常见问题速查

| 问题 | 解 |
|:---|:---|
| CUDA out of memory | batch_size改1，r=16改r=8，加gradient_checkpointing |
| loss不收敛 | 学习率从2e-4降到5e-5，检查数据格式 |
| 模型输出乱码 | tokenizer的chat_template没设对，检查<\|im_start\|>格式 |
| 验证器误报 | 扩大ANCHORS的tolerance |
| 微调后不如原始模型 | 过拟合——减少epochs，增加dropout |

### 提示词：通用排坑

`
我在做SCVC-LoRA微调时遇到以下错误：
[粘贴完整错误信息]

我的环境：Windows/RTX 3060 12GB/Python 3.11/torch 2.x
请给出诊断和解决方案。
`

---

## 时间估算

| 步骤 | 初学者 | 有经验 |
|:---|:--:|:--:|
| 环境搭建 | 2-3小时 | 30分钟 |
| 数据构建 | 2-4小时 | 1小时 |
| LoRA微调 | 半天（含debug） | 3-4小时 |
| 验证管道 | 2-3小时 | 1小时 |
| 评测+发布 | 1-2天 | 半天 |
| **总计** | **约3-5天** | **约2天** |

---

*实操手册。2026-07-27。有问题随时回这里找提示词。*
