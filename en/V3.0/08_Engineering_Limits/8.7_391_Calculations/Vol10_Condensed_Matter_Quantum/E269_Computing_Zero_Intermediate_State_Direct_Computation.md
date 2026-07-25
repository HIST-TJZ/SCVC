# Zero-Intermediate-State Direct Computation: SCVC Physical Limits & Four Pathways

**Status**: 🟢 80% (Landauer 🟢; reversible theory 🟢; K-LUT 🟢; photonic 🟡; area-for-energy 🟡)

---

# 1. Where Intermediate States Come From — Why They Exist

## 1.1 Root Cause: Combinatorial Explosion

Arbitrary N-input M-output function → truth table 2^N rows. N = 32 → 4G rows → physically impossible to store directly → must decompose into multi-level gates → each level's output = next level's input → **intermediate states**.

## 1.2 Physical Cost of Intermediate States

```
Creating intermediate state:   Capacitive charging → ~5×10⁻¹⁸ J (E265 computed)
Erasing intermediate state:    Landauer → kT ln 2 ≈ 3×10⁻²¹ J
```

**Seems erasing is cheaper? No.** Intermediate states are created + erased → both steps must be paid. In one FP32 FMA (~5 pJ), ~95% is the create/erase cycle of intermediate states, only ~5% is "the logical result actually needed."

## 1.3 SCVC Quantification

| Operation | Total Energy | Intermediate Erase Fraction | "Net Logic" Energy |
|:---|:---|:---|:---|
| INT add | ~0.1 pJ | ~90% | ~0.01 pJ |
| FP32 FMA | ~5 pJ | ~95% | ~0.25 pJ |
| FP64 division | ~100 pJ | ~99% (10 iterative steps) | ~1 pJ |
| sin/cos (CORDIC) | ~1000 pJ | ~99.9% (multi-step iteration) | ~1 pJ |

**Conclusion**: Current computing energy is almost entirely the cost of intermediate states. Eliminate intermediate state erasure → energy drops 10-1000×.

---

# 2. The Essence of Direct Computation

## 2.1 Definition

**Direct computation** = input → signal routing → output, **zero intermediate state erasure**.

Not "no intermediate states" (signal propagation necessarily passes through multiple physical nodes), but "intermediate states are not erased" — each intermediate result stays in its own register/wire; the next stage consuming it only reads, never erases.

## 2.2 Information-Conservation Perspective

```
Traditional: input → [intermediate 1] → [erase] → [intermediate 2] → [erase] → output
                  create      destroy        create      destroy
                  entropy ↑                   entropy ↑

Direct:       input → intermediate 1 → intermediate 2 → ... → output
                  retained       retained           retained
                  zero entropy increase (reversible limit)
```

---

# 3. Four Pathways

## Pathway 1: FPGA/LUT (Small-Function Direct)

| Parameter | Value | SCVC |
|:---|:---|:---|
| K-LUT | K=6 → 64-bit table → register-level | Zero intermediate state |
| Single LUT latency | ~0.1 ns | RC |
| Single LUT energy | ~0.1 pJ | Capacitive charging |
| Interconnect latency | 1 cm = 70 ps | Light-speed wall 🟢 |
| Interconnect energy | ~1 pJ/cm | Wire capacitance |

**Bottleneck**: Interconnect overwhelms LUT. On a 10×10 cm FPGA, cross-chip = 700 ps → already exceeds single LUT latency → total delay of multi-level LUT cascade is light-speed locked.

## Pathway 2: ASIC Hardwired (Pure Combinational Logic)

Direct synthesis to gate-level combinational logic — zero registers, zero erasure.

N=32 arbitrary function → a few thousand gates → feasible. Maximum N limited by:
- Gate fan-in (~4-5)
- Wire delay (~1 ps/μm)
- Critical path depth log₂N

**Energy**: Only gate capacitive charging → ~0.01 pJ/gate × few thousand gates → ~tens of pJ → **10-100× savings** over FP32 FMA (~5 pJ) GPU path (multi-stage pipeline + registers + erasure).

## Pathway 3: CAM/Associative Memory (Hardware Lookup)

CAM = input matching → parallel compare all entries → output. N inputs → 2^N entries → O(2^N) energy.

| N | Entries | Energy | Verdict |
|:---|:---|:---|:---|
| 8 | 256 | ~10 pJ | ✅ L1-level |
| 12 | 4096 | ~100 pJ | 🟡 L2-level |
| 16 | 65536 | ~1000 pJ | 🔴 Starts losing |
| 20 | 1M | ~10⁴ pJ | ❌ |

**SCVC**: CAM direct wins over ALU when N < 12. This is exactly how FPGA LUT works — K=6 → 64 entries → perfect.

## Pathway 4: Photonic/Analog (Ultimate Direct)

A lens does Fourier transform: light field enters → diffracts → focal plane = spectrum. **Zero intermediate states, zero Joule heat.**

| | Electronic | Photonic |
|:---|:---|:---|
| Signal carrier | Charge (e⁻) | Photon (γ) |
| Joule heat | Yes (I²R) | **Zero** |
| Energy floor | Capacitive ~5×10⁻¹⁸ J | Shot noise ~1.4×10⁻¹⁷ J |
| Interconnect latency | RC + light-speed | **Light-speed only** |
| Fourier transform | O(N log N) gates | **1 lens** |

**SCVC**: Photonic shot noise floor ~88 eV/bit ≈ 1.4×10⁻¹⁷ J — ~3× higher than electronic (~5×10⁻¹⁸ J). But photonics crushes electronics on long-distance interconnect (zero Joule heat + light-speed latency only).

---

# 4. Example: Direct Adder

## 4.1 Carry Propagation = Unavoidable Intermediate States

8-bit addition → carry propagates from bit 0 to bit 7 → 8 levels of dependency → 8 intermediate states → all erased.

## 4.2 Carry-Select Adder = Eliminate Intermediate States

```
Traditional: A₀+B₀ → c₁ → A₁+B₁+c₁ → c₂ → ... → 8-level propagation

Direct: Precompute both "carry=0/1" cases for each 4-bit block
        → 2×16 = 32 entries → 64 B → register-level
        → Higher block selects based on actual carry → multiplexer
        → 3 levels (2×4-bit lookup + 1 MUX) → zero carry propagation
```

**Result**: 8-bit addition = 3 levels → ~0.3 ns, ~0.3 pJ. Industry already does this — Carry-Select Adder. The principle is exactly "eliminate intermediate state propagation."

---

# 5. Reversible Computing — Ultimate Theory

## 5.1 Bennett 1973

Reversible logic gates (Fredkin, Toffoli): inputs = outputs → information conserved → **zero Landauer cost**. Garbage outputs retained or cleared by reverse computation.

## 5.2 Space/Time for Energy Trade

| Strategy | Cost | Gain |
|:---|:---|:---|
| Retain all intermediates | O(N) storage | Zero erasure energy |
| Reverse-compute to clear | O(2N) time | Zero erasure + zero storage |
| Hybrid (checkpoint) | O(√N) storage, O(N√N) time | Optimal trade-off |

## 5.3 Why Not Yet Commercial

Landauer erasure (~3×10⁻²¹ J) is far smaller than capacitive charging (~5×10⁻¹⁸ J). **Current bottleneck is not erasure — it's creating intermediate states (capacitive charging).** Eliminating erasure saves only 0.1% of energy. Must first solve the capacitive charging problem → 3D stacking to shorten wire lengths → reduce C → then reversible computing becomes meaningful.

---

# 6. SCVC Optimal Direct Architecture

| Function Scale | Best Pathway | Energy | Latency |
|:---|:---|:---|:---|
| K ≤ 6 (small) | FPGA LUT direct | ~0.1 pJ | ~0.1 ns |
| 6 < K ≤ 12 (medium) | CAM / decomposed LUT | ~10 pJ | ~1 ns |
| 12 < K ≤ 32 (large) | ASIC pure combinational | ~100 pJ | ~10 ns |
| K > 32 (very large) | Reversible pipeline | ~nJ | ~100 ns |
| Fourier / convolution | **Photonic analog** | ~fJ | ~ps |

---

# 7. Core Quick Reference

| Question | SCVC Answer |
|:---|:---|
| Where do intermediate states come from | Large-function decomposition → multi-level gates → information created then erased |
| Energy fraction | ~95% of FP32 FMA is intermediate-state cost |
| Is FPGA LUT direct computation | ✅ K ≤ 6 → zero intermediate states |
| Why can't LUTs be larger | 2^K explosion → K > 6 infeasible |
| Electronic ultimate ceiling | Reversible + 3D stacking → ~0.005 aJ/op |
| Photonic ultimate ceiling | Shot noise ~1.4×10⁻¹⁷ J/bit |
| Lens doing FT | Zero intermediate + zero Joule heat → ultimate direct |
| Why isn't reversible computing commercial yet | Erasure isn't the bottleneck → capacitance is → needs 3D stacking |

---

*SCVC verdict: Direct computation (zero intermediate state erasure) is the correct physical direction. Landauer proved erasure is the only necessary energy cost — eliminating it → energy drops 10-1000×. Four pathways from LUT to photonics cover all function scales. A lens doing Fourier transform is the universe's most perfect direct computer — zero intermediate states, zero Joule heat, one optical element replacing O(N log N) transistors. This is not science fiction — it is physical fact, used in every optics lab every day.*