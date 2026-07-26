# SCVC + AI: Geometric Anchor Fine-Tuning

The AI training experiments have moved to their own repository:

? **[SCVC-LoRA](https://github.com/HIST-TJZ/SCVC-LoRA)**

## What's There

Six versions of fine-tuning a 0.5B model (Qwen2.5-0.5B-Instruct) with SCVC geometric constraint data:

| Version | Method | Key Result |
|:---|:---|:---|
| v1-v3 | Single-stage SFT | First correct alpha formula: ?=1/(4??+??+?) |
| v4 | Three-stage SFT | 14/15 evaluation pass, 24/30 causal arrows |
| v5 | DPO optimization | Boundary honesty improvement |
| v6 | Continuous spectrum | Fusion of rational + intuitive reasoning |

## Key Finding

A 0.5B model + SCVC geometric constraints can outperform much larger models on physics reasoning. The model learns to:
- Trace physical phenomena to geometric anchors
- Mark certainty percentages at each reasoning tier
- Say "cannot determine" when constraints run out

## Related Papers (this repo)

- [E279: SCVC??AI??](E279_SCVC??AI??_??.md)
- [E280: AGI??SCVC](E280_AGI??SCVC_???????.md)
- [E282: SCVC??AI???](E282_SCVC??AI???_????????.md)
- [E283: ????????](E283_????????_?????????????.md)
- [E284: v1-v6????](E284_v1_v6_????_SCVC?????.md)

---

*See [SCVC-LoRA](https://github.com/HIST-TJZ/SCVC-LoRA) for reproduction scripts, training data, and adapter weights.*
