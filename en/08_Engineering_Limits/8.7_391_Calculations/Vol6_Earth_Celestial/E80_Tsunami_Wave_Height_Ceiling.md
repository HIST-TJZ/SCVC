# SCVC Engineering Limit: Maximum Tsunami Wave Height — Physical Ceiling of Seismic Energy + Seafloor Topography

> Combined with E78 earthquake limit derivation. Tsunami wave height is jointly determined by earthquake/landslide/impact energy, ocean depth, and shoaling amplification.
> SCVC locks the physical ceiling through rock strength (bond energy → E78) and gravity (g=9.81 m/s², not an SCVC constant but accepted as given).

---

## §1. Seismic Tsunami Wave Height Ceiling

### 1.1 Energy Coupling

A tsunami extracts only a small fraction of the total energy released by an earthquake:

```
E_tsunami = η × E_seismic
η ≈ 0.001–0.01 (coupling efficiency, 0.1–1%)

Maximum earthquake (Mw 9.5, derived in E78):
  E_seismic ≈ 1.1×10¹⁹ J (Mw 9.5, Gutenberg-Richter)
  E_tsunami ≈ 10¹⁷–10¹⁸ J
```

| Mw | E_seismic (J) | E_tsunami (J, η=0.5%) | Equivalent Nuclear Yield | Historical Event |
|----|---------------|----------------------|----------|----------|
| 7.0 | 2.0×10¹⁵ | 1.0×10¹³ | 2.4 kt | Haiti 2010 |
| 8.0 | 6.3×10¹⁶ | 3.2×10¹⁴ | 76 kt | — |
| 8.5 | 3.5×10¹⁷ | 1.8×10¹⁵ | 0.4 Mt | — |
| 9.0 | 2.0×10¹⁸ | 1.0×10¹⁶ | 2.4 Mt | Japan 2011 |
| 9.2 | 4.0×10¹⁸ | 2.0×10¹⁶ | 4.8 Mt | Alaska 1964 |
| 9.5 | 1.1×10¹⁹ | 5.6×10¹⁶ | 13 Mt | Chile 1960 |

### 1.2 Deep-Ocean Wave Height

Tsunami wave energy density (per unit wavefront length):

```
E / L_front = (1/8) × ρ × g × H² × λ

H = √(8 × E_tsunami / (ρ × g × λ × L_front))

ρ = 1025 kg/m³ (seawater)
λ ≈ 150–300 km (tsunami wavelength)
L_front ≈ 1000–2000 km (rupture zone length)
```

| Mw | Deep-Ocean Wave Height (m) | Notes |
|----|-------------|------|
| 8.0 | **0.9** | Almost imperceptible (open ocean) |
| 8.5 | **2.2** | Small tsunami |
| 9.0 | **5.1** | 2011 Japan ~5 m deep-ocean |
| 9.2 | **7.3** | 1964 Alaska ~7 m deep-ocean |
| **9.5** | **12** | Chile 1960 ~10–15 m deep-ocean |

> Deep-ocean tsunami wave heights are only a few meters — this is precisely why sailors often do not feel a tsunami (wavelength 200 km, slope <1:10,000).

### 1.3 Shoaling Amplification

As a tsunami enters shallow water, wave speed decreases and energy conservation demands wave height increases:

```
Green's Law: H_shallow / H_deep = (v_deep / v_shallow)^(1/2)

Wave speed: v = √(g×d)    d: water depth

Depth 4000m → 10m: amplification ≈ √(√(4000g)/√(10g)) ≈ 4.5×
Plus refraction/focusing effects: additional 2–3×
Total amplification: ~9–14×
```

**Coastline wave height = deep-ocean wave height × 9–14**

| Mw | Deep-Ocean (m) | Coastline (m) | Historical Observation |
|----|---------|-----------|----------|
| 8.0 | 0.9 | **~8** | Small tsunami |
| 8.5 | 2.2 | **~20** | Moderate tsunami |
| 9.0 | 5.1 | **~46** | Japan 2011: ~40 m |
| 9.2 | 7.3 | **~65** | Alaska 1964: ~67 m |
| 9.5 | 12 | **~109** | Chile 1960: ~25 m (non-optimal geometry) |

> Chile 1960 had Mw 9.5 but wave height "only" ~25 m — because the rupture direction was parallel to the coast (rather than perpendicular), energy was not focused toward the coastline.

### 1.4 Extreme Optimal Scenario

Pushing all parameters to the limit — optimal geometry (rupture zone perpendicular to coast), maximum coupling efficiency (1%), shortest wavelength (150 km), narrowest wavefront (1000 km) + extreme shoaling (from 5000 m to 5 m) + bay focusing:

```
Optimal scenario maximum coastline wave height: ~340 m
```

**SCVC-locked seismic tsunami coastline wave height ceiling: ~300–500 m.** This is the physical limit under Mw 9.5+ with optimal geometry. Actual historical maximum is approximately 67 m (1964 Alaska, recorded).

---

## §2. Landslide Tsunamis

### 2.1 Lituya Bay 1958 — Record Holder at 524 m

```
Rock mass: 30 million m³
Fall height: ~900 m
Potential energy = mgh ≈ 7×10¹⁴ J
Wave height: 524 m (highest run-up mark on opposite slope)
```

Lituya Bay's extreme wave height comes from **extreme energy concentration in a narrow fjord** — wavefront only ~1 km. This was not an open-ocean tsunami but a localized surge.

### 2.2 Volcanic Flank Collapse — The "Mega-Tsunami" Scenario

**Canary Islands (La Palma, Cumbre Vieja):**

```
Collapse volume: ~500 km³ (5×10¹¹ m³)
PE = 5×10¹¹ × 2700 × 9.81 × 6000 ≈ 8×10¹⁹ J
     ≈ energy of an Mw 10.1 earthquake (~7× that of Mw 9.5)

Coupling efficiency: landslide-to-water ~5% (far higher than earthquake 0.5%)
Tsunami energy: ~4×10¹⁸ J
Deep-ocean wave height (100 km wavefront): ~800 m (but exceeds ocean depth → breaking wave)

Actual physical constraint: wave height cannot exceed water depth
Water depth ~4 km → wave height cap ~4 km (breaking wave)
```

**Coastline run-up (near-source):**
```
After height saturation → propagates as breaking wave
Near-source islands: 500–1000 m run-up
Regional (1000 km): 50–100 m
Far-field (5000+ km): 10–30 m (but extreme wavelength → widespread inundation)
```

### 2.3 SCVC Landslide Limit

Maximum landslide is constrained by mountain height. SCVC rock strength ceiling:

```
h_mountain_max ≈ σ_c / (ρ×g) ≈ 200 MPa / (2700×9.81) ≈ 7.6 km

Reality: Mauna Kea ~10 km (measured from seafloor)
Maximum collapse volume: ~10,000 km³ (entire island flank)
```

SCVC maximum landslide tsunami energy ~2×10²¹ J → ~1000× larger than maximum earthquake tsunami (~10¹⁸ J). **But wave height is still constrained by ocean depth (~5 km breaking), coastline run-up cap ~1000–2000 m.**

---

## §3. Asteroid Impact Tsunamis

### 3.1 Chicxulub-Class (Dinosaur Extinction)

```
Impactor: r=7.5 km, ρ=3000 kg/m³, v=20 km/s
KE = ½ × (4/3)πr³ × ρ × v² ≈ 1.1×10²⁴ J
     ≈ 260,000 Gt TNT (humanity's total nuclear arsenal × millions)

Water depth at impact site: ~0 (shallow sea, Yucatán Peninsula)
Instantaneous crater: water column zeroed to zero within seconds
First wave: ~4–5 km (equals ocean depth, physical ceiling)
Global coastlines: model predictions ~100–300 m run-up
Nearest coastline to impact: possibly >1000 m (evidence: Cretaceous-Paleogene deposits around Gulf of Mexico)
```

### 3.2 SCVC-Allowed Maximum Impact

Largest near-Earth objects in the Solar System — but SCVC does not prohibit even larger impacts (extremely rare). 10–20 km class impactors occur approximately once every ~100 million years.

```
Maximum credible impactor: r=15 km
KE: ~8.5×10²⁴ J (~8× Chicxulub)
Coastline run-up: ~200–500 m (global)
Near-impact point: >2000 m
```

**Design basis:** Asteroid impact tsunami return periods (>10⁷ years) far exceed engineering structure design lifetimes (~100–1000 years) → **not required for routine engineering design.** However, for ultra-critical facilities such as nuclear power plants, they can serve as "beyond-design-basis" extreme scenario assessments.

---

## §4. Engineering Conclusions

### 4.1 Coastal Nuclear Plant Seawalls — Maximum Design Wave Height

| Tsunami Source | Maximum Run-up (m) | Annual Probability | Include in Design? |
|----------|------------|--------|-------------|
| Earthquake Mw 9.0 (regional subduction zone) | **30–50** | ~10⁻²–10⁻³ | ✅ Design basis |
| Earthquake Mw 9.5 (maximum credible earthquake) | **50–100** | ~10⁻⁴ | ✅ Beyond-design-basis |
| Earthquake extreme geometry | **~300** | ~10⁻⁵–10⁻⁶ | ⚠️ Under discussion |
| Landslide tsunami (regional) | **100–500** | ~10⁻⁴–10⁻⁵ | ⚠️ Site-specific |
| Landslide tsunami (far-field) | **10–50** | ~10⁻⁴ | ⚠️ Requires assessment |
| Asteroid impact | **100–500** | ~10⁻⁷–10⁻⁸ | ❌ Not included |

**Recommended design basis (SCVC-supported):**

```
Routine coastal protection: 10–30 m (Mw 8.5–9.0)
Nuclear plants / critical facilities: 30–50 m (Mw 9.0–9.2)
+ additional freeboard (extreme geometry + landslide contingency): +20–30 m
→ Total design height: 50–80 m
```

Japan 2011 Fukushima design wave height ~5.7 m → actual ~14 m → **underestimated by a factor of 2.5.** Referencing the SCVC physical ceiling, designing **50–80 m seawalls** covers Mw 9.5-class earthquakes and far-field landslide tsunamis.

### 4.2 Tsunami Warning Systems

| Detection Method | Response Time | Accuracy |
|----------|---------|------|
| Seismometer (P-wave detection) | **<3 minutes** | Magnitude estimate ±0.3 |
| GPS crustal deformation | **<5 minutes** | Direct fault slip measurement |
| Deep-ocean pressure gauge (DART buoy) | **10–30 minutes** | Direct tsunami wave height measurement |
| Coastal tide gauge | **At tsunami arrival** | Verification |

**SCVC-constrained warning time window:**

```
Seismic wave propagation: v_P ≈ 6–8 km/s → 30 seconds to any point on Earth
Tsunami propagation: v_tsunami ≈ √(g×4000) ≈ 200 m/s = 720 km/h

1000 km from epicenter: tsunami arrival ~1.4 hours → warning window ~1.3 hours
5000 km from epicenter: tsunami arrival ~7 hours → warning window ~7 hours
```

Physical limit: **Seismic P-waves travel 30–40× faster than tsunamis → warnings are always possible (SCVC-permitted), provided detection and communication are sufficiently fast.**

### 4.3 Optimal Tsunami Defense Portfolio

| Measure | Effect | Cost | SCVC Constraint |
|------|------|------|----------|
| **Seawalls** | Direct blocking | Extremely high | Structural strength bounded by bond energy (E4) |
| **Mangroves / coastal forests** | Attenuate 30–50% wave energy | Low | Tree height ~20–50 m (biomechanics) |
| **Early warning + evacuation** | Save lives | Medium | Communication delay ~seconds |
| **Land-use planning** | Avoid exposure | Low (political cost high) | — |

**Optimal strategy: Warning + evacuation as core (save lives), seawalls to protect critical infrastructure (nuclear plants), mangroves as low-cost supplement (ecological co-benefit).**

### 4.4 SCVC Tsunami Limit Summary

| Mechanism | Deep-Ocean Wave Height | Coastline Run-up | Historical Maximum | SCVC Ceiling |
|------|---------|----------|----------|----------|
| Earthquake Mw 9.5 | **~12 m** | **~100 m** | 67 m (1964 AK) | **~300–500 m** |
| Landslide (local) | — | **~500 m** | 524 m (Lituya) | **~1000 m** |
| Landslide (far-field) | ~50 m | **~100 m** | — | **~200 m** |
| Asteroid impact | — | **~300 m** | 100–300 m (modeled) | **>2000 m (near-source)** |
| **SCVC absolute physical ceiling** | **~5 km** (water depth) | **~5–10 km** | — | Wave height ≤ ocean depth |

> SCVC absolute ceiling: Tsunami wave height cannot exceed ocean depth (waves break when H>d). The deepest point, Mariana Trench ~11 km → H_max_absolute ~5–10 km. Any "tsunami" exceeding this value is no longer a water wave — it is the ocean being bodily "pushed aside" (asteroid impact scenario).

---

## Appendix: SCVC Derivation Chain (Tsunami Wave Height)

```
π → α → bond energy → rock strength → maximum earthquake magnitude Mw≤9.5 (E78)
                        ↓
                   E_seismic ≤ 10¹⁹ J
                        ↓ η~0.5%
                   E_tsunami ≤ 5×10¹⁶ J
                        ↓
              Deep-ocean wave height H² ∝ E/(ρgλL)
              H_deep ≤ 12 m (Mw 9.5)
                        ↓ Green's Law ~9–14×
              Coastline run-up ≤ 300–500 m
              
Landslide ceiling: bond energy → rock strength → maximum mountain height ~8 km → PE ≤ 2×10²¹ J
         → E_tsunami ≤ 10²⁰ J → wave height constrained by water depth at ~5 km

Asteroid ceiling: Solar System body KE ≤ 10²⁵ J → wave height exceeds water depth → ocean bodily pushed aside
```

The ultimate physical ceiling on tsunami wave height = maximum ocean depth (~11 km). SCVC locks the energy ceiling for earthquakes and landslides through rock strength (bond energy), thereby locking tsunami wave height.
