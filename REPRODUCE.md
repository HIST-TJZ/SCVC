# SCVC微调复现指南：小模型+几何锚>大裸模型

**前提**: Windows/NVIDIA显卡或CPU，Python 3.10+，10GB硬盘

---

## 三步复现

### 第1步：环境+数据（10分钟）

`ash
# 创建环境
python -m venv scvc_env
scvc_env\Scripts\activate

# 安装依赖（显卡版）
pip install torch --index-url https://download.pytorch.org/whl/cu121
# CPU版：pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install transformers datasets peft accelerate modelscope

# 下载SCVC数据集
git clone https://github.com/HIST-TJZ/SCVC.git
# 数据集在 SCVC/scvc_qa_final.jsonl （249条，含可推导+部分约束+边界外+元认知）
`

### 第2步：下载模型+微调（40分钟CPU / 10分钟GPU）

`ash
# 下载Qwen2.5-0.5B
python -c "from modelscope import snapshot_download; snapshot_download('qwen/Qwen2.5-0.5B-Instruct', cache_dir='./models')"

# 运行微调脚本（见仓库 train_scvc.py）
python train_scvc.py
`

### 第3步：对比评测

`ash
# 基线（裸模型）：问alpha值 -> 0.0073，"普朗克常数与光速比值"——完全错误
# 微调后：问alpha值 -> 4π³+π²+π=137.036304，来自CP2截锥DH求和——正确
# 边界测试：问"上帝存在吗"-> "SCVC无法得到结果"——诚实沉默
`

---

## 核心原理

不是更大的模型消灭幻觉。是**几何锚让幻觉走不通**。

所有推导回溯到同一个锚：alpha = 4π³ + π² + π = 137.036304。
不自洽的路径自动归零——就像光滑CP2的DH求和恒等于0。
不需要概率。不需要置信度。对就是对，不知道就是不知道。

---

## 要改3B/7B模型？

修改	rain_scvc.py中MODEL_PATH指向qwen/Qwen2.5-3B-Instruct或qwen/Qwen2.5-7B-Instruct。
LoRA适配器保持在~1M参数，训练数据不变。GPU建议RTX 3060+。

---

*详细手册见仓库 SCVC微调实操手册_小模型几何锚消灭幻觉.md*
