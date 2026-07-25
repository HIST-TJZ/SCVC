# Compute vs. Lookup: SCVC Breakeven Line & Optimal Precomputation Strategy

**Status**: 🟢 85% (Energy spectrum 🟢; cache hierarchy 🟢; decomposed LUT 🟢; exact operation energy 🟡 process-dependent)

---

# 1. Physical Energy Map

## 1.1 Compute Operation Energy Spectrum

| Operation | Energy | Physical Origin | SCVC Chain |
|:---|:---|:---|:---|
| INT add | ~0.1 pJ | C_gate·V² | C ∝ ε₀ ∝ 1/α |
| INT multiply | ~0.5 pJ | Multi-level gates | ← same × stage count |
| FP32 FMA | ~5 pJ | Pipeline + registers | C × stage count |
| FP64 division | ~100 pJ | Newton-Raphson ~10 FMA steps | ← |
| sin/cos | ~1000+ pJ | CORDIC iteration | ← |
| exp/log | ~1000+ pJ | Polynomial approximation | ← |
| AES S-box | ~10000+ pJ | GF(2⁸) inversion | ← |
| Physics sim step | 10³-10⁶ pJ | Many-body ODE | ← |

Bottom layer: C_gate ∝ ε₀(A/d) ∝ 1/α. V² ∝ (k_BT/q)² (thermal noise floor). All compute energy scales ∝ C·V² ∝ 1/α.

## 1.2 Memory Access Energy Spectrum

| Cache Level | Latency | Energy/64B | Energy/bit | Capacity | SCVC |
|:---|:---|:---|:---|:---|:---|
| Register | ~0.1 ns | ~0.1 pJ | ~0.001 pJ | <1 KB | — |
| L1 (SRAM) | ~1 ns | ~10 pJ | ~0.02 pJ | 32-64 KB | E265 computed |
| L2 | ~5 ns | ~50 pJ | ~0.1 pJ | ~1 MB | ← |
| L3 | ~15 ns | ~200 pJ | ~0.4 pJ | ~10-100 MB | ← |
| HBM (off-chip) | ~100 ns | ~100 pJ | ~0.2 pJ | ~GB | E266 computed |
| SSD | ~10 μs | ~10⁵ pJ | ~200 pJ | ~TB | NAND floating gate |
| Network | ~ms | ~10⁸ pJ | — | ∞ | Light-speed wall |

---

# 2. Breakeven Formula

## 2.1 Core Inequality

\[
E_{\text{lookup}} < E_{\text{compute}}
\]

Where:
\[
E_{\text{lookup}} = E_{\text{storage\_amortized}} + E_{\text{access}}
\]
\[
E_{\text{storage\_amortized}} = \frac{E_{\text{precompute}}}{N_{\text{hits}}}
\]

**Key**: More hits → lower amortization. For high-frequency operations (10⁹ calls/sec), precompute once → amortized to negligible.

## 2.2 Decomposed Lookup Table

For combinatorial explosion problems (e.g., 100³ = 10⁶ entries), decompose:

\[
E_{\text{decomposed}} = N_{\text{sub}} \times E_{\text{access}} + E_{\text{combine}}
\]

Example: 100³ → 3 × 100-entry lookup + 2 multiplies = 3×10 pJ + 2×0.5 pJ = **~31 pJ** vs. direct compute ~1000 pJ → **save 33×**.

---

# 3. Cache-Level Breakeven Phase Diagram

## 3.1 Simplified Rules

```
Cheap to compute (<10 pJ)     → Always compute     (INT add/mul, FP32 FMA)
Medium (10-100 pJ)            → L1 lookup          (FP64 div, sin/cos)
Expensive (100-1000 pJ)       → L2/HBM lookup      (exp, interpolation, complex polynomials)
Very expensive (>1000 pJ)     → Must lookup         (crypto S-box, complex simulation)
```

## 3.2 SCVC Verdict Per Operation

| Operation | Energy | Verdict | Reason |
|:---|:---|:---|:---|
| INT8 add | ~0.1 pJ | **Compute** | Register lookup costs more than compute |
| INT8 multiply | ~0.5 pJ | **Compute** | Lookup (10 pJ) much more expensive than compute |
| FP32 FMA | ~5 pJ | **Compute** | L1 lookup (~10 pJ) slightly more expensive |
| FP64 division | ~100 pJ | **L1 lookup** | sin/cos table already covers |
| sin/cos | ~1000 pJ | **L1 lookup** | 360°×4B = 1.4 KB → fits in L1 |
| exp/log | ~1000 pJ | **L2 lookup** | Larger domain → needs interpolation |
| AES S-box | ~10000 pJ | **L1 lookup** | 256×1B = 256 B → L1 easily |
| Complex simulation | >10000 pJ | **HBM lookup** | Must precompute |

---

# 4. Bit-Width Effect — SCVC Verdict for AI Inference

## 4.1 Lower Bit Width → Lookup Wins More

For a binary operation on two N-bit inputs, all possible inputs = N²:

| Bit Width | Input Combos | Table Size | Best Cache | Lookup Energy | Compute Energy | Winner |
|:---|:---|:---|:---|:---|:---|:---|
| FP32 | 2⁶⁴ | ∞ | — | — | ~5 pJ | **Compute** |
| FP16 | 65536 | 128 KB | L2 | ~200 pJ | ~2 pJ | **Compute** |
| INT8 | 256 | 512 B | L1 | ~10 pJ | ~0.5 pJ | **Compute** |
| **INT4** | 16 | **32 B** | **Register** | **~0.1 pJ** | ~0.05 pJ | 🟡 Tie |
| INT2 | 4 | 8 B | Register | ~0.05 pJ | ~0.02 pJ | 🟡 Near-tie |
| 1-bit | 2 → XOR | 0 B | — | — | ~0.01 pJ | **Compute** |

## 4.2 SCVC Optimal Bit Width: INT4

```
INT4: 16×16 = 256 combos → 512 B table → register-level (0.1 pJ/lookup)
      Compute vs. lookup near balance → can mix (JIT build table for hot spots + direct compute cold paths)
INT2: 4×4 = 16 combos → 32 B table → but compute is extremely cheap → lookup advantage small
1-bit: XOR → 1 gate → lookup meaningless
```

## 4.3 Three-Input Lookup: INT4 Ternary Operation

3 INT4 inputs → 16³ = 4096 combos → 8 KB → L1-level → ~10 pJ.
Compute needs 2 multiplies + 1 add → ~1 pJ → compute still cheaper.
But if the operation itself is expensive (e.g., three-input division) → lookup wins immediately.

## 4.4 Why FPGA/ASIC Dominate Low-Bit-Width Inference Over GPU

**This is the physical essence of "digital lookup":** FPGA = LUT (Look-Up Table) = hardware lookup engine. INT4 LUT energy ~0.1 pJ vs. GPU compute ~0.5 pJ → FPGA naturally dominant at low bit widths. GPU must "simulate lookup" (shared memory → registers) to catch up → adds latency and power.

---

# 5. Decomposed Lookup — Escape from Combinatorial Explosion

## 5.1 Principle

n-dimensional input → direct table = Nⁿ entries → combinatorial explosion.
Decompose → n × 1D lookups + (n−1) combiner operations → O(n) scale.

## 5.2 Example: 100³ = 10⁶

| Method | Operations | Energy |
|:---|:---|:---|
| Direct compute | 2 multiplies + 1 add | ~1 pJ (INT8) |
| Full table lookup | 10⁶ entries → 1 MB → L2 lookup | ~200 pJ ❌ |
| **Decomposed lookup** | 3×100-entry lookup + 2 multiplies | 3×10 pJ + 2×0.5 pJ = **~31 pJ** |
| Decomposed (expensive op) | Same structure, but direct compute ~1000 pJ | 31 pJ vs. 1000 pJ → **save 33×** |

## 5.3 SCVC Decision Matrix

| Op Cost | Bit Width | Full Table Feasible? | Decomposed? | Direct Compute? |
|:---|:---|:---|:---|:---|
| <1 pJ (INT arithmetic) | Any | ❌ | ❌ | ✅ |
| ~5 pJ (FP32 FMA) | FP32 | ❌ | ❌ (combiner cost > compute) | ✅ |
| ~100 pJ (FP64 div) | FP64 | ❌ | 🟡 (needs interpolation) | 🟡 |
| ~1000 pJ (sin/trig) | FP32 | ❌ | ✅ (L1 table + interpolation) | ❌ |
| >10000 pJ (crypto/sim) | Any | 🟡 | ✅ | ❌ |

---

# 6. Optimal Strategy for AI Inference

## 6.1 Current Trends vs. SCVC Verdict

| Trend | SCVC Analysis |
|:---|:---|
| INT8 → INT4 → INT2 | ✅ Lower bit width → larger lookup advantage |
| INT4 mixed precision | ✅ **Optimal bit width** — small table (512 B) + compute/lookup balance |
| Sparse + asynchronous | ✅ E265 already computed → 10³-10⁴× headroom |
| In-memory compute | ✅ Eliminates data movement → directly hits Landauer direction |

## 6.2 "Digital Lookup" Endgame

```
INT4 + register lookup + L1 hot-spot JIT table build = optimal energy efficiency
  → High-frequency sub-matrix products → auto-build table (JIT)
  → Cold paths → direct compute
  → Compiler auto-decides "compute vs. lookup" → guided by physical breakeven line

GPU final form: part "compute engine," part "hardware lookup engine" (tensor cores are essentially this)
FPGA/ASIC: born as "programmable digital lookup" — this is the physical advantage for low-bit-width inference
```

---

# 7. Quick Reference

| Question | SCVC Answer |
|:---|:---|
| INT add/mul lookup? | **Never** — compute too cheap |
| FP32 FMA lookup? | **No** — 5 pJ < 10 pJ (L1) |
| sin/cos lookup? | **L1 lookup** — 360°×4B = 1.4 KB |
| AES S-box lookup? | **L1 lookup** — 256 B |
| INT4 matrix multiply lookup? | 🟡 Tie — can mix |
| INT2 matrix multiply lookup? | 🟡 Near-tie — compute slightly wins |
| 100³ full table lookup? | ❌ 10⁶ entries too expensive |
| 100³ decomposed lookup? | ✅ Save 33× (if operation is expensive) |
| AI optimal bit width? | **INT4** — register table + compute/lookup balance |
| Why FPGA wins at low bit width? | LUT = hardware lookup engine, 0.1 pJ vs GPU's 0.5 pJ |

---

*SCVC verdict: Compute vs. lookup is not "whether to" — it's "at what bit width, at what cache level, at what hit rate." Lower bit width → lookup wins more. INT4 is the sweet spot. FPGA/ASIC's physical advantage in low-bit-width inference comes from "they ARE programmable lookup engines." This is the engineering conclusion of SCVC's full chain: α → C_gate → energy spectrum → breakeven line.*