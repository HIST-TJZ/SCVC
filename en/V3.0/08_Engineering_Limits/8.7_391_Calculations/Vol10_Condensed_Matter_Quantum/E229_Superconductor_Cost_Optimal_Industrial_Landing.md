# Superconductor Cost Optimization — Industrial Landing Point

**Date**: 2026-07-25 | **Status**: 🟡 Engineering analysis

## Core Question
Given SCVC-predicted superconductor candidates, which ones are industrially viable?

## Cost Decomposition
```
Total Cost = Synthesis Cost + Pressure Maintenance + Cooling + Material Cost

Synthesis: ∝ P^2 (pressure squared — diamond anvil cell scaling)
Pressure Maintenance: ∝ P · V (large-volume press)
Cooling: ∝ log(T_ambient/Tc) (Carnot efficiency)
Material: ∝ (constituent element cost)
```

## Key Industrial Constraints
1. **Pressure < 10 GPa**: Large-volume press feasible, industrial scale
2. **Tc > 77K**: Liquid nitrogen cooling (cheap)
3. **Tc > 150K**: Standard refrigeration (very cheap)
4. **No toxic/radioactive elements**: Industrial safety

## SCVC-Optimized Landing Points

### Tier 1: Near-term (0-5 years)
- Existing: MgB₂ (39K, 0 GPa), Nb₃Sn (18K, 0 GPa)
- New: V-based hydrides at moderate P

### Tier 2: Medium-term (5-15 years)
- Be-B compounds at 5-10 GPa (Tc ~100-150K)
- C-S-H optimized at 10-20 GPa

### Tier 3: Long-term (15+ years)
- Room-temperature ambient pressure: requires new physics beyond current SCVC framework
- Metallic hydrogen metastable phases

## Conclusion: The industrial sweet spot is Tc=100-200K at P<10 GPa. SCVC guides material search to this window.
