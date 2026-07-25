# E169: Mutation Time Window — Physical Upper Limit

## Core
Cancer evolution requires sequential mutation accumulation. Each step has a physical time floor.

### Mutation Rate Physics
```
Mutation rate μ ~ 10⁻⁹-10⁻¹⁰ per base per division (DNA polymerase fidelity)
Driver mutations needed: ~3-10 (Vogelstein model)
Cell divisions available: ~70 (Hayflick limit, E168)
```

### Minimum Evolution Time
```
t_min = (driver mutations needed) × (divisions per selective sweep) × (cell cycle time)
      = 5 × 100 × 14 h ≈ 7000 h ≈ 0.8 years (absolute minimum, zero death)
      = 5 × 1000 × 3 days ≈ 15000 days ≈ 41 years (in vivo realistic)
```

### SCVC Key Insight
Cancer is not instantaneous. The physical constraints of DNA replication fidelity (α → H-bond recognition → polymerase error rate) mean:
- **Minimum latency: ~1 year** (perfect conditions, impossible in vivo)
- **Typical latency: 5-30 years**
- This is the **mutation time window** — the period during which intervention can prevent cancer from reaching the "escape velocity" of multi-driver mutations.

### Clinical Implication
Annual screening can catch most solid tumors before they accumulate >3 driver mutations → still therapeutically vulnerable. SCVC provides the physical basis for screening interval optimization.
