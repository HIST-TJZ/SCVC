# E274：GW不变量交叉验证 — SCVC DH求和 vs 已知等变Gromov-Witten值

## 背景

SCVC在CP2xS1上做DH局域化，得到alpha-1 = 4pi3+pi2+pi = 137.036304。
DH局域化在数学上等价于等变Gromov-Witten不变量（Atiyah-Bott, Berline-Vergne, Duistermaat-Heckman）。
因此4pi3+pi2+pi就是CP2xS1的某个等变GW不变量的具体值。

## 任务

交叉验证：SCVC的DH求和结果是否与已知GW文献值一致？

---

## 步骤1：确认数学等价性

DH局域化公式 = 等变上同调中的Berline-Vergne定位公式 = 等变GW不变量的不动点计算法。
确认：SCVC对CP2xS1的DH计算对应GW理论中的哪个具体不变量？
- 什么等变参数？
- 什么稳定条件（genus 0？）
- 什么上同调类插入？

---

## 步骤2：查找已知GW值

CP2的等变GW不变量已知文献：
- Givental (1996): Equivariant Gromov-Witten invariants
- Lian-Liu-Yau (1997): Mirror principle
- Okounkov-Pandharipande (2006): Gromov-Witten theory of CP2

查找CP2（或CP2xS1）在相关等变参数下的GW不变量数值。

---

## 步骤3：数值对照

| 来源 | 计算方法 | 数值 |
|------|----------|------|
| SCVC | DH局域化（6不动点） | 4pi3+pi2+pi = 137.036304 |
| GW文献 | 等变局域化/镜像定理 | ？ |

---

## 步骤4：体积解释的验证

M7M4发现：
- 4pi3 = 4 x Vol(CP2 x S1)
- pi2 = 2 x Vol(CP2)
- pi = (1/2) x Vol(S1)

这三个系数(4,1,1)是否有GW理论的独立解释？它们是否对应CP2xS1的某些基本类的GW不变量？

---

## 输出要求

1. 数学等价性确认（引用定理）
2. SCVC的DH计算在GW语言中的翻译
3. 已知GW文献值（如果有）
4. 对照结论：匹配 / 不匹配 / 无对照值（=新结果）
5. 如果不匹配：差异来源分析
6. 体积系数(4,1,1)的GW解释

## 诚实性
- 如果找不到精确对照值 -> 诚实标注「文献中未找到此等变参数下的GW计算」= 新结果
- 如果对照值存在但不完全匹配 -> 分析差异原因
- 引用具体文献页码/公式编号