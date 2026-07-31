# One-Way Speed of Light Measurement — Experimental Conjecture (From Laboratory to Cosmos)

> **Nature**: Pure experimental conjecture. Does not depend on any theoretical framework.  
> **Core Question**: The one-way speed of light has never been measured. Is the speed of light a fundamental constant, or the macroscopic emergence of some underlying medium? The following experiments attempt to answer.

---

## Why the One-Way Speed of Light Has Never Been Measured

All known light-speed experiments — Fizeau gear, Foucault rotating mirror, Michelson interferometry, laser ranging — measure the **round-trip speed of light** (A→B→A). The one-way speed (A→B, no return) has never been directly measured.

The reason is simple: measuring one-way speed requires clocks at A and B to be precisely synchronized — and **synchronizing clocks itself requires knowing the speed of light**. This is a logical circularity. Einstein bypassed it in 1905: he **defined** the one-way speed to equal the round-trip speed. All of Special Relativity is built upon this definition.

"Defined equal" ≠ "measured and confirmed equal."

---

## The Key Breakthrough: Using Motion to Convert Time into Space

The circularity of the traditional approach stems from an implicit fixation — **you must know when the light departed, you must place a clock at both A and B, and those two clocks must be synchronized.**

The fundamental innovation of the rotating-laser experiment is: **not relying on synchronized clocks, but on motion.**

Core insight:

> Let a cylinder move along its axis at constant velocity v, while a laser at its center rotates at constant angular velocity ω. **The axial motion v and the angular motion ω share the same time t.** The finite speed of light R/c causes the trajectory to exhibit a spatial gap — motion converts "time that cannot be synchronized" into "distance that can be measured with a ruler."

You don't need to know when the laser fired or at what angle it started. You don't need two clocks. You don't need synchronization. You only need two things:
1. A cylinder moving uniformly through a laser plane
2. An etched trajectory left on its inner wall

---

## Conjecture Layer 1: Uniform Cylinder + Rotating Laser (Core Experiment)

### Experimental Setup

```
         ← Cylinder moves along its axis at velocity v →
         ┌──────────────────────┐
         │                      │
         │     ╱  ← Laser beam  │
         │    ╱                 │
         │   ●──────────────────│← Etched track on cylinder wall
         │   Laser source       │
         │   (rotating at ω)    │
         │                      │
         └──────────────────────┘
                  Radius R
              ↑ Laser plane fixed at z=0 ↑
```

- Cylinder of radius R, height H, moving at constant velocity v along its axis (e.g., sliding on a horizontal plane, or drifting in space)
- Laser plane fixed in space; laser at center rotates at constant angular velocity ω
- **Constraint**: The time for the cylinder to pass completely through the laser plane = one full rotation period, i.e., `H/v = 2π/ω`
- The inner wall of the cylinder is coated with photosensitive material; the laser sweep leaves an etched trajectory

### Why a Stationary Cylinder Doesn't Work

If the cylinder is stationary, light emitted from the laser propagates radially in a straight line, and its impact position on the wall **depends only on the emission direction**. The trajectory is merely a record of "what angle the laser swept" — whether the speed of light is 3×10⁸ m/s or infinite, the angular range covered by the trajectory is exactly the same. c does not enter the trajectory.

**A second dimension of motion must be introduced to encode time.**

---

### Trajectory Equation and Mathematical Derivation

At time t, the laser points at θ = ωt. The emitted photon travels radially for **R/c** time to reach the cylinder wall. Upon arrival the cylinder has moved forward. In the cylinder's own coordinate system (origin at the base of the cylinder), the trajectory height is:

```
z'(θ) = v·(θ/ω + R/c)
      = (v/ω)·θ  +  vR/c
        ────────     ─────
        From rotation    From finite light speed!
```

**The trajectory on the unwrapped surface is a straight line.** The slope is determined by v/ω. The critical part is the intercept term **vR/c** — if the speed of light were infinite (c → ∞), the intercept would be zero; with finite light speed, the intercept > 0.

### Start and End: The Emergence of a Gap

The cylinder only exists in z' ∈ [0, H] (base to top). The trajectory begins at the base and ends at the top.

**Starting point** (θ=0, cylinder base just passed the laser plane):
```
z' = vR/c    (Not zero! Finite light speed means the track does not begin at the base edge)
```

**Ending point** (trajectory reaches the cylinder top at z'=H):
```
H = (v/ω)·θ_end + vR/c
θ_end = (ω/v)(H − vR/c) = 2π − ωR/c   (using the constraint H/v=2π/ω)
```

**The trajectory does not complete a full circle!** From θ=0 to θ_end, it falls short by ωR/c radians.

The corresponding arc-length gap:
```
Δx = R·(2π − θ_end) = R·ωR/c = ωR²/c
```

### One-Way Speed of Light Formula

```
c = ωR² / Δx
```

**All three quantities are purely spatial:**

| Quantity | Meaning | How to measure |
|---|---|---|
| ω | Laser angular velocity | Tachometer |
| R | Cylinder radius | Ruler |
| Δx | Horizontal gap from endpoint to directly below the start point | Unwrap cylinder, measure with ruler |

**No time measurement whatsoever. No clock synchronization. v cancels out in the final formula.**

---

### Physical Intuition

```
Δx = ωR × (R/c)
     ────   ────
     Wall    Time for light to travel
     linear  from center to wall
     speed
```

A photon takes R/c seconds to fly from the center to the wall. During this interval, the laser continues to rotate, "sweeping" an arc length of ωR·(R/c) along the wall. Cut the cylinder vertically along the starting meridian, unwrap it into a plane — this swept-but-unmarked arc is the visible horizontal gap.

**If any gap Δx > 0 exists, it proves the speed of light is not infinite. The size of the gap directly yields the numerical value of c.**

---

### Order-of-Magnitude Estimates

| Radius R | Angular velocity ω | Gap Δx | Measurable? |
|---|---|---|---|
| 1 m | 100 rad/s | 333 nm | Extremely difficult (below visible wavelength) |
| 10 m | 100 rad/s | 3.3 μm | Requires microscopic interferometry |
| 10 m | 1000 rad/s | 33 μm | Optical methods feasible |
| 100 m | 100 rad/s | 33 μm | Optical methods feasible |
| 100 m | 1000 rad/s | 330 μm | Easy |


---

## Conjecture Layer 2: Scaled-Up Version — Light Speed Measurement Apparatus

### Principle

Identical to Layer 1. Scale up R and ω to bring Δx into the measurable range:

- Radius R = 10–100 m
- Laser source mounted at center, precision-rotating
- Cylinder slides uniformly along its axis through the laser plane
- Trajectory measured via optical microscopy; gap Δx → directly yields c

### What It Can Measure

- **Absolute one-way speed of light**: c = ωR²/Δx
- **Anisotropy**: if the speed of light differs in different radial directions, the slope of the trajectory will exhibit localized variations

---

## Conjecture Layer 3: Deeper Treasure — Microstructure of the Trajectory

### Average Light Speed Is Only the Beginning

The above derivation assumes the speed of light is strictly constant, yielding a perfect straight line.

**But what if the speed of light is not a fundamental constant, but the macroscopic emergence of an underlying structure?**

Emergence implies that the speed of light is like water temperature — macroscopically uniform and constant, but microscopically a statistical average of countless underlying degrees of freedom. During the photon's R/c ≈ 3.3 ns flight (for R = 1 m), the speed of light may have tiny random fluctuations.

**The trajectory records not just the average speed of light — it records a continuous time series.** Each infinitesimal segment:

```
z'(θ + dθ) − z'(θ) = (v/ω)·dθ + v·d(R/c_instant)
```

The second term `v·d(R/c_instant)` is a **direct encoding of instantaneous light-speed fluctuations.** If c fluctuates, the trajectory is not simply a straight line — magnified, it reveals microscopic distortions.

### A Trajectory Under the Microscope

```
↑ z'
│
│   Macroscopically: a perfect straight line
│      ╱
│     ╱
│    ╱
│   ╱
│  ╱
│ ╱
│╱__________________→ x (arc length)
│
│   Magnified 1000×:
│      ╱╲ ╱
│     ╱  ╲
│    ╱    ╲╱
│   ╱       ╲___________
│  Microscopic distortions — "fossils" of light-speed fluctuations
```

### Why This Is a "Brownian Motion Level" Discovery

In 1905, Einstein used the random jitter of pollen grains in a liquid (Brownian motion) to indirectly prove the existence of atoms. Molecular collisions cannot be seen directly, but the pollen's trajectory can.

**This experiment applies the same logic to light:**

| Brownian Motion (1905) | Rotating Laser Cylinder |
|---|---|
| Pollen is the probe | Light is the probe |
| Water molecules are the substrate | Spacetime microstructure is the substrate |
| Microscope observes pollen jitter | Microscope observes trajectory distortions |
| Proved the existence of atoms | May prove spacetime is emergent |

If the trajectory exhibits statistically significant, noise-irreducible microscopic distortions under a microscope — that would be the **first laboratory signal of quantum gravity.**

### A Null Result Is Equally Important

Trajectory perfectly smooth under a microscope (no distortions beyond noise) → light-speed fluctuations constrained to extremely low levels → new experimental upper bounds for emergent spacetime theories. This probes a parameter space that has barely been touched by laboratory methods.

---

## Detection Sensitivity Analysis: What Can This Experiment See?

### Signal Formula Recap

RMS amplitude of trajectory micro-fluctuations:

```
σ_z = (v/c) · √(Rλ) · (δc/c)

σ_z  = RMS deviation of trajectory from ideal straight line (m)
v    = Cylinder axial velocity (m/s)
R    = Cylinder radius (m)
λ    = Spatial correlation length of the emergent medium (m)
δc/c = Relative fluctuation amplitude of light speed within each cell

Number of independent samples: N = L/λ    (L = trajectory arc length)
```

**v is the key amplifier.** Without v, σ_z would be sub-atomic time jitter — no clock could measure it. Multiplying by v = 300 m/s converts it into nanometer-scale spatial displacements, easily detectable by AFM.

### Optimal Experimental Parameters

| Parameter | Optimal Value | Limiting Factor |
|---|---|---|
| R | 300 m | Building scale limit (experimental hall) |
| v | 300 m/s | Subsonic (noise, aerodynamic heating) |
| ω | 10,000 rad/s | Air-bearing spindle (~100,000 RPM) |
| Trajectory arc length L | 2πR ≈ 1885 m | From a single experimental run |
| Arc segment required | 10–100 cm | Much less than a full circle — a small segment suffices |

**Key Insight: A complete cylinder is not needed.** Light-speed fluctuations are a stationary random process — you don't need the entire history, a representative sample is enough. As long as the arc segment spans 10–100 times λ (e.g., 10 cm when λ = 1 cm, giving N = 10 independent fluctuation cycles), there are sufficient statistical degrees of freedom to extract the variance and correlation structure of fluctuations. The σ_z expression contains neither H nor the total angular span — only √(Rλ). The cylinder height only needs to be a few millimeters to a few centimeters, cut as a thin ring.

### Recording Method: Why Photoresist Is the Optimal Solution

| Method | Spatial Resolution | Cost | Assessment |
|---|---|---|---|
| **Photoresist + development** | <0.1 μm | Very low (coating + chemical development) | ✅ One-shot recording of complete trajectory, permanent archive, post-hoc AFM slow scan |
| Holographic plate | <0.2 μm | Low (~$50/plate) | ✅ High resolution, requires darkroom |
| Photosensitive paper | ~10 μm | Very low | ❌ Insufficient resolution, thermal diffusion blur |
| CMOS line sensor array | ~3–7 μm/pixel | Medium (~$1000) | ❌ Resolution insufficient for nanometer-scale distortions |
| Fluorescent screen + microscope camera | ~1 μm | Medium | ❌ Diffraction + scattering blur |

**Core approach: Not a "narrow-strip sensor betting on probability."** A narrow-strip scheme records only micron-scale fragments each time, with effective sampling spacing (v·2π/ω ≈ 60 cm) far larger than the fluctuation characteristic scale (mm–cm), completely losing the signal. **Coat the entire inner wall ring with photoresist; one experiment freezes the complete trajectory.** R = 300 m, coat a 10 cm tall ring ≈ 190 m², photoresist cost ≈ $1000.

### Systematic Errors and Countermeasures

AFM z-resolution for photoresist trajectory ≈ 0.5 nm (including substrate roughness + measurement noise). After statistical averaging, equivalent noise ≈ 0.03–0.1 nm (full trajectory length 1885 m provides tens to hundreds of thousands of independent samples).

| Error Source | Magnitude | Countermeasure |
|---|---|---|
| Laser pointing jitter | 0.1 μrad → δz ≈ 30 nm | Quadrant detector + piezo mirror active beam stabilization → <0.02 μrad → δz < 0.6 nm |
| Substrate surface error | 1–5 nm (turning tool marks) | AFM pre-scan of one circumference before exposure for calibration, post-hoc subtraction |
| Vacuum refractive index fluctuation | 10⁻⁶ torr → δn ≈ 3×10⁻¹¹ | Negligible |
| Thermal drift | — | Experiment duration only ~6 ms (one revolution), thermal time constant > minutes → negligible |
| Earth rotation (Sagnac) | δz < 0.005 nm | Negligible |

**System noise floor ≈ 0.5 nm; after statistical averaging, equivalent noise reduced to 0.03 nm.**

### Single-Point Detection Threshold and Statistical Enhancement

Taking v = 300 m/s, R = 300 m:

| λ | √(Rλ) | σ_z / (δc/c) | Single-point minimum detectable δc/c | After statistical averaging |
|---|---|---|---|---|
| 1 μm | 0.017 m | 1.7×10⁻⁸ | 2.9% | — |
| 1 mm | 0.55 m | 5.5×10⁻⁷ | 0.09% | 0.01% |
| **1 cm** | 1.73 m | 1.7×10⁻⁶ | 0.03% | **0.002%** |
| **10 cm** | 5.48 m | 5.5×10⁻⁶ | 0.009% | **0.0009%** |
| **1 m** | 17.3 m | 1.7×10⁻⁵ | 0.003% | **0.0005%** |

**This experiment under optimal conditions can detect light-speed relative fluctuations at the parts-per-million level — provided emergence occurs at the centimeter-to-meter scale.**

---

## How Large an Emergent Medium Can Be Detected? — "Grain" Size Under Three Models

The core question is: **what is the emergent unit cell size λ of spacetime?** The answer depends on the specific model of spacetime emergence.

### Model 1: Poisson Grain (Shot Noise)

Suppose spacetime consists of discrete grains of size λ₀, and light crossing each grain experiences an independent random fluctuation δc/c = 1/√N_grain, where N_grain is the number of "internal degrees of freedom" per grain.

For a photon path of length R, the number of grains crossed: N_cells = R/λ₀.
Fluctuation per cell: δc/c = 1/√N_grain.
Accumulated fluctuation: σ_z = (v/c) · √(Rλ₀) · δc/c = (v/c) · √(Rλ₀/N_grain).

For detectability with the optimal setup (σ_z > 0.03 nm): √(λ₀/N_grain) > 3×10⁻⁸.
If N_grain ~ 1: λ₀ > 10⁻¹⁵ m (nuclear scale). If N_grain ~ 10⁶: λ₀ > 10⁻⁹ m (nanometer scale).

### Model 2: Independent Cells

Each cell of size λ has an independent fractional fluctuation δc/c. This is the model used in the sensitivity table above. Minimum detectable λ at optimal parameters: ~30 μm (when δc/c ~ 10⁻²) to ~30 μm (when δc/c ~ 1/N_cell saturates).

### Model 3: Thermodynamic Gas Analogy

If light-speed fluctuations behave like density fluctuations in a gas: δc/c ∝ 1/√N_particles, where N_particles is the number of "spacetime elements" within the sampled volume. The sampled volume during one flight: ~R·λ² (radial path of length R through a cross-section of ~λ²). So δc/c ∝ 1/√(R·λ²/ℓ_P³), where ℓ_P is the fundamental element scale.

This gives a very different scaling from the independent-cell model.

---

## Key Insight: Why Microscopic Grain Size Is Not the Fundamental Issue

The experiment does not need to directly resolve individual "spacetime atoms." It searches for **collective fluctuation modes** — which can be far larger than the microscopic constituents:

```
System                Microscopic Unit          Collective Mode           Observable Signature
─────────────────────────────────────────────────────────────────────────────────────
Water molecules (0.3 nm)    Critical density fluctuations (500 nm)    Critical opalescence (visible to naked eye)
Lattice atoms (0.3 nm)      Phonons (μm–mm)                          Thermal expansion (mechanically measurable)
Magnetic domains (nm)       Spin waves (μm)                          Giant magnetoresistance
Spacetime "atoms" (?)       Collective modes (μm–m)                  Trajectory distortions (AFM)
                                      ↑
                               Experiment searches here
```

**This experiment does not ask "how large are spacetime atoms?" — it asks "do collective fluctuation modes exist at ANY scale?"** Regardless of whether the microscopic substrate is at the Planck scale, quark scale, or any other scale, emergence can produce collective excitations far larger than the microscopic constituents — just as phonon wavelengths can be millions of times larger than the lattice spacing.

### Emergence Detection Window Overview

```
Emergence Model              Minimum Detectable Medium Scale λ_min
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Poisson grain (shot noise)      30 μm          ← Most optimistic
Independent cell (δc/c=0.01)    30 μm          ← Coincidentally close
Independent cell (δc/c=0.001)   3 mm
Thermodynamic gas analogy       3 mm
Holographic noise (N_g)        ~10¹⁴ m       ← Far out of reach
Quantum gravity foam           ~10³¹ m       ← Physically impossible
```

### Parameter Space Exclusion by a Null Result

Even with a null result (perfectly smooth trajectory), the experiment provides an exclusion boundary for a parameter space never previously constrained:

```
                               Undetectable region
  δc/c                          ╱
  10⁰  │  ••••••••••••••••• ╱
       │  •               •╱
  10⁻² │  •           •  ╱
       │  •       •    ╱
  10⁻⁴ │  •   •      ╱
       │  • •       ╱
  10⁻⁶ │  •        ╱    ← Null result excludes above this line
       │  •       ╱
  10⁻⁸ │  •      ╱
       │        ╱
  10⁻¹⁰│───────╱─────────────────→ λ
        10⁻⁶   10⁻³   10⁰   10³
        Quark  Atom   mm    m   km
```

**A null result excludes any collective fluctuations with δc/c > 10⁻⁵ in the millimeter-to-kilometer scale range.** This is a parameter space completely unconstrained by any existing method:

| Existing Method | What It Constrains | Sensitivity at What λ |
|---|---|---|
| Interferometry (Michelson type) | Round-trip light-speed anisotropy | Does not constrain spatial fluctuations |
| High-energy astrophysics (GRB, AGN) | Lorentz violation (frequency-dependent) | Does not constrain spatial fluctuations |
| Cold-atom interferometry | Fine-structure constant variation | Does not constrain spatial fluctuations |
| **This experiment** | **Spatial fluctuations** | **μm–m → First probe of this window** |


---

## Conjecture Layer 4: Natural "Mega-Tower" — Mercury Transit Shadow Edge

### Logic

No construction needed. **The Sun is the light source, Mercury is the occluding body, and Earth's surface is the recording plane.**

Sun-Earth distance = 1.5×10¹¹ m. If the speed of light is emergent, underlying fluctuations will cause tiny random jitter in the propagation time of light near Mercury's edge. During a Mercury transit, this jitter manifests as: **statistically significant jagged jitter in the shadow edge of Mercury on Earth's surface.**

### Experiment

- **Equipment**: High-speed line-scan camera (MHz sampling rate)
- **Timing**: Next Mercury transit **November 2032**
- **Operation**: Continuously image the shadow edge; Fourier-analyze the time series of edge position

### Exclusion Criteria

Observe from **multiple geographic locations** simultaneously along the transit band. Shadow edge perfectly smooth under MHz sampling → no detectable fluctuations along the light propagation path. Statistically significant jaggedness correlated across stations → rules out atmospheric turbulence (local) and instrumental noise (random).

### Cost

Nearly zero. Just wait until 2032.

---

## Conjecture Layer 5: Exoplanet Transit Retrospective (Zero-Cost Data Mining)

### Logic

Mercury transits occur only once every decade or so, but they are not the only opportunity:

- Kepler and TESS have accumulated tens of thousands of exoplanet transit light curves
- Asteroid occultations occur frequently, with fast-moving shadows
- Venus transit data from 2012 still exists and can be retrospectively analyzed

Perform edge-sharpness analysis on all transit/occultation light curves. If statistically significant blurring or jaggedness exists and correlates with distance — that's a signal.

### Cost

Zero — data are publicly available.

---

## Conjecture Layer 6: Pulsar Arrival Time Fluctuations (Galactic-Scale Test)

### Logic

If the speed of light has tiny fluctuations, distant pulsar arrival times will contain non-white-noise components. NANOGrav/EPTA/FAST have accumulated decades of sub-microsecond precision data.

Spatially correlated arrival-time fluctuations among pulsars in different directions — if they exist — can be separated from the gravitational wave background using statistical methods.

### Cost

Zero. Data already exist.

---

## Experimental Layer Overview (From Small to Large)

| Layer | Method | What It Measures | Scale | Cost | Timing |
|:---:|------|------|:---:|:---:|------|
| **1** | Uniform cylinder + rotating laser | Absolute one-way light speed & micro-fluctuations | ~1–10 m | Low–Medium | Anytime |
| **2** | Scaled-up light-speed apparatus | Absolute one-way light speed & anisotropy | ~10–100 m | Medium–High | Requires construction |
| **3** | Trajectory microstructure analysis | Light-speed fluctuations (emergence signal) | ~1–100 m | Low | Anytime (data analysis) |
| **4** | Mercury transit shadow edge | Light-speed fluctuations (emergence signal) | 1.5×10¹¹ m | Nearly zero | November 2032 |
| **5** | Exoplanet transit retrospective | Light-speed fluctuations (emergence signal) | ~10¹⁷–10¹⁹ m | Zero | Anytime |
| **6** | Pulsar timing array | Light-speed fluctuations (emergence signal) | ~10¹⁹–10²² m | Zero | Anytime |

---

### Conceptual Prudence Note on the Astronomical Layers

Layers 4–6 extend the experimental scale from meters to astronomical distances, demonstrating the universality of the measurement principle in methodology — any observation involving light propagation time can be reinterpreted within the emergence framework. However, **their numerical feasibility requires independent verification**:

**Mercury Transit (Layer 4)**: Mercury blocks only ~0.004% of sunlight; what reaches the ground is an extremely faint dimming, not a sharp "shadow edge." Atmospheric seeing (~1 arcsecond) corresponds to ~750 km of blurring on the solar surface, far exceeding the c-fluctuation spatial jitter signal (~1.2 mm for δc/c ~ 10⁻⁵). This scheme is not feasible within the currently accessible parameter range; it is retained as a conceptual demonstration of "using natural light sources in place of artificial apparatus."

**Exoplanet Transits (Layer 5)**: Light propagation distance ~10¹⁷–10¹⁹ m. The √N averaging effect reduces sensitivity to λ ~ 1 m fluctuations by ~10⁹× compared to the laboratory version. However, from the reverse perspective — if a c-fluctuation signal is discovered and calibrated in the laboratory, transit data can serve as an **independent extrapolation test at large distances**: do the predicted light-curve residuals, obtained by plugging the laboratory-measured (δc/c, λ) into transit data, match observations?

**Pulsar Timing (Layer 6)**: NANOGrav/EPTA timing precision ~100 ns, corresponding to (δc/c)·√λ ~ 10⁻⁹ — 4 orders of magnitude more sensitive than the laboratory version. However, two caveats apply: (1) this sensitivity is based on the white-noise assumption, and the spectral characteristics of pulsar timing residuals are strongly degenerate with the gravitational-wave background and intrinsic spin noise; (2) the constraint applies to nanohertz-frequency (year-timescale) fluctuations, which may belong to a completely different spectral regime from the laboratory microsecond–millisecond timescale fluctuations.

**The core value of Layers 4–6** lies not in their independent detection sensitivity — but in the fact that **if the laboratory version discovers a non-zero signal**, they provide three independent extrapolation test targets (Solar System scale, Galactic scale, cosmological scale). These six layers constitute a complete verification chain from desktop to cosmos.

---

### Extension: Multi-Messenger Comparison — At Which Layer Does Emergence Occur?

All of the above analysis concerns photons. A natural question is: **if spacetime is emergent, does it affect only photons, or all particles?**

```
Photon (mass 0)              → c is the only propagation speed
Neutrino (mass ~0.1 eV)      → v ≈ c, but with tiny mass-dependent delay
Gravitational wave (mass 0)  → v = c (GR prediction)
Cosmic rays (protons, electrons) → v < c, determined by energy
```

Using existing multi-messenger astronomical events (e.g., GW170817 gravitational wave + photon, SN1987A neutrino + photon, IceCube high-energy neutrinos and gamma-ray burst associations), one can directly compare arrival-time fluctuation spectra across different messengers:

```
If all messengers show the same fluctuation spectrum:
  → Emergence is at the spacetime level (affects all propagation)
  → δc is a property of the spacetime medium, not the electromagnetic field

If only photons fluctuate:
  → Emergence is at the electromagnetic level
  → c-fluctuations arise from electromagnetic coupling between photons and emergent structure

If different messengers have different fluctuation amplitudes:
  → One can measure the "coupling coefficient" as a function of particle species
  → Opens the parameter space of "emergence phenomenology"
```

**Cost**: Zero. All multi-messenger data are already in public archives. Only a unified statistical analysis framework is needed — the same scripts as Layers 5 and 6, extended to non-photon channels.

**Caveat**: Multi-messenger events are rare (to date, gravitational wave + photon: only GW170817), limiting statistical significance. But with each new event, the constraint tightens by one step. This is a measurement that "automatically becomes more precise over time."

---

## Historical Analogy: Where This Experiment Sits

| Experiment | Era | What It Did | Consequence |
|---|---|---|---|
| Michelson-Morley | 1887 | Measured Earth's velocity through the ether | Null result → catalyzed Special Relativity |
| Brownian Motion | 1905 | Random jitter of pollen grains | Indirectly proved the existence of atoms |
| **Rotating Laser Cylinder** | ? | Measures one-way light speed & micro-fluctuations | Null result → confirms c as fundamental constant / Non-zero → first evidence of spacetime emergence |

This experiment simultaneously possesses the characteristics of Michelson-Morley (ingenious experimental design) and Brownian motion (inferring underlying microstructure from macroscopic traces).

---

## Why Suspect Spacetime Is Emergent? — Theoretical Premises of the Experiment

### The Experiment Does Not Ask Questions in a Vacuum

The motivation for this experiment does not stem from the curiosity of "measuring a never-verified constant" — but from a gradually converging consensus in modern theoretical physics: **spacetime may not be fundamental.**

### Six Major Quantum Gravity Programs Point in the Same Direction

Current mainstream quantum gravity candidate programs are mutually incompatible in detail, but are remarkably convergent on one conclusion:

| Program | Status of Spacetime |
|---|---|
| **Loop Quantum Gravity** | Space is woven from spin networks — area and volume have minimum units |
| **Causal Dynamical Triangulations** | Spacetime is built from 4D simplices, taking the continuum limit at large scales |
| **Causal Set Theory** | Spacetime consists of discrete causal events — "order" is more fundamental than "coordinates" |
| **AdS/CFT Duality** | (d+1)-dimensional gravitational spacetime is **exactly equivalent** to d-dimensional non-gravitational field theory on the boundary — spacetime emerges from the boundary |
| **String Theory (ER=EPR)** | Quantum entanglement = spacetime geometry — entanglement builds the skeleton of spacetime |
| **Verlinde Emergent Gravity** | Gravity is not a fundamental force — it is a macroscopic manifestation of entropic forces |

**Six mutually incompatible theories, highly convergent on the conclusion that "spacetime is not fundamental."** This is extremely rare in the history of theoretical physics — the usual interpretation is that they are climbing the same mountain from different faces.

### Holographic Duality: The Strongest Theoretical Evidence

AdS/CFT is one of the few **exact results** in quantum gravity. It states: a higher-dimensional gravitational theory is completely equivalent to a lower-dimensional non-gravitational theory — spacetime and the gravity within it emerge from the boundary theory. In one specific model, this is not a metaphor but a precise mathematical conclusion. Although our universe is not anti-de Sitter space, if emergent spacetime has been proven possible in one model, it is a reasonable extrapolation to the real universe.

### Historical Pattern: Everything "Fundamental" Eventually Isn't

| What | Once Considered | Later Found To Be |
|---|---|---|
| Matter | Continuum | Composed of atoms |
| Heat | Caloric fluid | Molecular kinetic energy |
| Light | Continuous wave | Photons |
| Vacuum | Empty nothingness | Quantum field ground state (full of fluctuations) |
| **Spacetime** | **Fundamental continuous manifold** | **?** |

Every row in this table ultimately resolved to "emergent." Would spacetime be the sole exception?

### Existing Signs of Unease

Several long-standing puzzles in physics all find natural explanatory directions under the "spacetime is emergent" perspective:

- **Black hole information paradox**: If the vicinity of the horizon has microstructure, information can be encoded within it without loss — emergent spacetime naturally provides this structure
- **Vacuum catastrophe**: Quantum field theory predicts vacuum energy 10¹²⁰ times larger than observed. If the vacuum is emergent, the "excess energy" may be absorbed by the emergence process
- **The "G mystery"**: Different laboratories measure the gravitational constant with discrepancies beyond their error bars — may hint at microscopic fluctuations in gravity
- **Temporal ambiguity in quantum mechanics**: Phenomena like delayed choice and quantum erasure, in which "time" behaves in ways that suggest it may not be a fundamental manifold

**No single clue is decisive — but multiple independent clues pointing in the same direction constitute sufficient motivation to pose the experimental question.**

---

## If the Trajectory Is Perfectly Smooth — Possibly More Disturbing Than Finding Fluctuations

The usual intuition is: "null result = boring, non-null result = revolutionary." But the logic of this experiment happens to be inverted.

### Two Scenarios, Two Types of Upheaval

```
                Experiment completed
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
   Trajectory has                Trajectory perfectly
   nanoscale distortions         smooth
   (δc/c > 10⁻⁵)                (no fluctuations beyond noise)
        │                         │
        ▼                         ▼
  "c is emergent"               "c is strictly fundamental"
  Spacetime has                  Spacetime is absolutely
  microstructure                 smooth
```

### Path A: Fluctuations Found (Revolutionary — But Path Is Clear)

- The speed of light is demoted from axiom to derived quantity
- Spacetime is emergent — experiment provides the first empirical anchor
- Quantum gravity theory development now has a target: explain the experimentally measured (δc/c, λ)
- Consequences: massive, but directionally clear — akin to how Brownian motion guided atomic theory

### Path B: Perfectly Smooth — Deeper Problems

#### Problem 1: Spacetime Would Be the Only "Truly Continuous" Entity in Physics

```
Planck scale (10⁻³⁵ m)                    Macroscopic world (smooth to 10⁻⁵)
  │                                            │
  │←──────── 30 orders of magnitude ──────────→│
  │                                            │
  │     No transition signal whatsoever?       │
  │     No amplification effect?               │
  │                                            │
  └────────────────────────────────────────────┘
```

This has **no precedent whatsoever** in condensed matter physics. The transition from crystalline solid discreteness (atomic spacing ~0.3 nm) to the applicability range of continuum elasticity theory spans only 3–4 orders of magnitude. Emergent phenomena in nature always leave observable traces at some intermediate scale — **if spacetime is uniquely the exception that "leaves no trace," it would be a singular entity in known physics.**

#### Problem 2: The Black Hole Information Paradox Hardens

If spacetime has no microstructure → neither does the vicinity of the black hole horizon → no carrier for information encoding → **Hawking radiation cannot carry information.** All currently popular resolutions of the information paradox (firewalls, fuzzballs, ER=EPR) assume spacetime has structure at the Planck scale. A perfectly smooth trajectory is tantamount to nailing the "experimentally unsupported" label onto all of these resolutions.

#### Problem 3: The Vacuum Catastrophe Has No Escape

If spacetime is emergent → vacuum energy can be "absorbed" by the emergence process. If spacetime is fundamentally smooth → **vacuum is vacuum, no absorption mechanism** → the 10¹²⁰ discrepancy returns to the table intact, becoming a pure computational disaster of theory.

#### Problem 4: The "Why" of c Becomes a Dead Question

If the trajectory has fluctuations → c has a physical explanation like the speed of sound (a property of the medium). If the trajectory is perfectly smooth → **c is a bare value, written on the first line of the universe's code.** "Why 299,792,458 m/s and not some other number?" — this question is demoted from a physics question to a philosophical one. The boundary of scientific explicability is severed here.

#### Problem 5: The Historical Pattern Breaks at Spacetime

```
Matter → not continuous, composed of atoms → verified ✓
Heat   → not caloric, molecular kinetic energy → verified ✓
Light  → not continuous wave, photons → verified ✓
Vacuum → not empty, quantum fields → verified ✓
Spacetime → not fundamental, is...? → if smooth → ✗ historical pattern broken
```

**The law that "everything is emergent" suddenly halts when human inquiry reaches the layer of spacetime.** The universe seems to be saying: you can keep dismantling downward — but spacetime itself is the floor, and there is no basement beneath the floor. This is philosophically possible, but has no precedent in the history of physics.

### A Duel of Two Outcomes

| | Trajectory Has Distortions | Trajectory Perfectly Smooth |
|---|---|---|
| For standard physics | Revolutionary — c is not constant | Confirmatory — c experimentally confirmed |
| For quantum gravity | Major support — direction activated | Heavy blow — all paths lose experimental support |
| For the "why" question | Opens a new layer — c has a deeper explanation | Seals the path — c cannot be explained further |
| For experimental physics | A new round of experimental arms race | Forced to search for signals at even smaller scales |
| Historical analogy | Brownian motion → atoms | **No analogy — has never happened** |

### The Ironic Conclusion

**Typically, "non-null results" are considered more revolutionary, but this experiment is precisely the opposite:** seeing fluctuations, while overturning c as a constant, provides an experimental anchor for quantum gravity and opens a corridor to deeper understanding. Perfect smoothness, while superficially validating standard physics, simultaneously freezes shut **all** entrances to deeper understanding, breaking the centuries-old scientific law that "everything is emergent" at the doorstep of spacetime.

**The physical significance of this experiment lies not in what the result is — but in the fact that regardless of the outcome, physics must digest a monumental consequence.**

---

## Honest Declaration

1. **These are conjectures.** No known physical theory predicts these effects.
2. **No one has ever performed an experiment from this angle.** The one-way speed of light has never been directly measured. Using a rotating laser + uniform cylinder to encode flight time as a spatial gap is an experimental scheme not previously proposed. This experiment fills not merely a data point, but a logical gap — transforming "one-way speed equals round-trip speed" from an Einsteinian convention into a testable experimental proposition.
3. **A null result is not "wasted effort."** A perfectly smooth trajectory constrains light-speed fluctuations to δc/c < 10⁻⁵ (at mm–m scales), excluding a parameter space never before touched by experiment, while simultaneously blocking the path to experimental verification for all quantum gravity theories — this is not boredom, it is indigestibility.
4. **A non-null result means the speed of light is not a fundamental constant, and spacetime has microstructure.** That would be the deepest revision to the foundations of physics since 1905. In its logical structure, this experiment simultaneously possesses the features of Michelson-Morley (testing whether the most basic assumption is true) and Brownian motion (inferring microscopic structure from macroscopic traces) — and history has shown that both types of experiments can change the course of physics.


---

## Experimental Variants: Using the Same Methodology to Open More Detection Windows

The following 16 variants are sorted by scientific significance.

### Variant 1: Critical Point Experiment — Natural Amplifier (Highest-Sensitivity Variant)

**Setup**: Fill the cylinder with a fluid near its critical point (e.g., CO₂ at 31°C / 73 atm, or SF₆ at 45°C / 38 atm).

Near the critical point, density fluctuations diverge — the correlation length ξ expands from molecular scale to the μm–mm range, producing visible critical opalescence.

```
⟨(δρ)²⟩ ∝ 1/|T − T_c|^γ       γ ≈ 1.24 (3D Ising universality class)
ξ ∝ 1/|T − T_c|^ν              ν ≈ 0.63
```

**Standard prediction**: Trajectory roughness is determined by Ornstein-Zernike scattering theory + dynamic scaling; critical exponents are known and thoroughly verified.

**Non-standard signal**: If the observed scaling exponents near the critical point deviate from OZ theory → an additional fluctuation source exists — not density fluctuations, but spacetime fluctuations — which couples to density fluctuations and is amplified by criticality.

---

### Variant 2: Different Substances, Same Refractive Index — Decoupling Composition from Electromagnetism

**Setup**: Prepare two (or more) liquids with refractive indices precisely matched but different chemical compositions.

```
Liquid A: Glycerol-water solution, adjusted to n = 1.4000
Liquid B: Sucrose-water solution, adjusted to n = 1.4000
Liquid C: Silicone oil, n = 1.4000 (naturally matched)

Fill the cylinder with each liquid separately; perform one experiment per liquid.
```

**Standard prediction**: All three trajectories are **exactly identical** — Maxwell's equations care only about the macroscopic refractive index n, not chemical composition. Within the Maxwell framework, no parameter can distinguish glycerol from sucrose.

**Non-standard signal**: Any statistically significant difference between any two trajectories → **the speed of light is not solely a function of n** → chemical composition affects the speed of light through a non-electromagnetic channel (i.e., spacetime-medium coupling). This is a signal that "should not exist" theoretically. Any difference, no matter how small, is new physics.

---

### Variant 3: Acoustic Standing Waves — Relaxation Time of the Spacetime Medium

**Setup**: Use an ultrasonic transducer to establish an acoustic standing wave in the liquid, creating spatially periodic density modulation.

```
Density distribution: ρ(z') = ρ₀ + Δρ·sin(k_sound·z')

Standard prediction:
  Trajectory exhibits sinusoidal modulation, amplitude precisely determined by dn/dρ
  Modulation phase fully synchronized with the acoustic density wave (EM response is instantaneous)
```

**Non-standard signal**: If the trajectory modulation amplitude exceeds the dn/dρ prediction, or — more critically — if there is a **phase lag** between the trajectory modulation and the acoustic density wave → the spacetime medium has a finite response time (relaxation time τ). A phase lag cannot be explained by any Maxwell-equation adjustment — it is a binary existence proof.

---

### Variant 4: Electromagnetic Field Loading — "Polarizability" of the Spacetime Medium

**Setup**: Apply a strong electrostatic or magnetostatic field across the cylinder region.

```
Electric field: Parallel plate electrodes, ~10⁶ V/m (pre-breakdown limit in air)
Magnetic field: Superconducting magnet or Halbach array, ~1–10 T

Laser path passes through the uniform field region; trajectory compared to the zero-field case.
```

**Standard prediction**: DC Kerr effect and Cotton-Mouton effect on n are at the 10⁻¹⁰–10⁻¹² level — at experimental precision, **the trajectory should be completely unaffected. The standard-prediction signal is zero.**

**Non-standard signal**: Any trajectory change → c depends on the electromagnetic field → vacuum has nonlinear electromagnetic response beyond QED vacuum polarization → the speed of light is field-controllable.

---

### Variant 5: Sharp Interface — The Refractive-Index Jump Fingerprint

**Setup**: Place two immiscible transparent liquids (e.g., water and silicone oil) in the cylinder, or maintain a stable horizontal interface between air and liquid. The laser plane crosses the interface during rotation.

```
Air/water interface (n jumps from 1.000 to 1.333):

Standard prediction:
  Trajectory has a clean, sharp vertical jump between the two segments
  Δz' = vR(n₂−n₁)/c
  
  For R=3 m, v=10 m/s: Δz' ≈ 33 nm (AFM resolution 0.5 nm is fully adequate)
```

**Non-standard signals**:
- Standard: clean jump → anomaly 1: transition width >> physical interface width (spacetime relaxation)
- Anomaly 2: small oscillations after the jump (spacetime "ringing")
- Anomaly 3: trajectory begins deviating before reaching the interface — "premonition" (non-local precursor)
- Anomaly 4: entry ≠ exit asymmetry (emergent hysteresis)

---

### Variant 6: Temperature Gradient — "Thermal Response" of the Spacetime Medium

**Setup**: Heat the bottom of the cylinder and cool the top to establish a vertical temperature gradient. Density varies with temperature → refractive index varies continuously.

```
T(z') varies linearly from 20°C (top) to 5°C (bottom)
ρ(T) nonlinear (water density maximum at 4°C)
n(T) = n(ρ(T)) precisely calculable

Standard prediction: Trajectory curvature fully determined by ∫₀ᴿ n(T(z'), r) dr
```

**Non-standard signal**: Trajectory curvature deviates from n(T) prediction. More importantly — **if temperature directly affects the "stiffness" of the spacetime medium**, rather than merely changing the density of the physical medium. In emergent systems, temperature is often the key parameter controlling the "degree of order" (the critical point being an extreme example). A mild temperature gradient far from the critical point may still change c by altering the elastic modulus of the spacetime medium.

---

### Variant 7: Flowing Medium — An Emergent Version of Fizeau Drag

**Setup**: Liquid flows radially within the cylinder (pump-driven, circulating outward from center or inward from periphery). Photons traverse the flowing medium along their flight path.

```
Water flowing outward: flow direction = photon flight direction (co-flow)
Water flowing inward: flow direction ← photon flight direction (counter-flow)

Perform two experiments and compare Δx.
```

**Standard prediction** (Fresnel-Fizeau drag, verified since 1851): effective light speed = c/n ± v_flow(1−1/n²).

**Non-standard signal**: If the drag coefficient deviates from f = 1−1/n² → the medium drags not merely the electromagnetic phase velocity, but partially drags the spacetime medium itself. If the drag exhibits asymmetry (co-flow vs. counter-flow deviations not symmetric) → spacetime-medium flow has "chirality."

---

### Variant 8: Multi-Wavelength Dispersion — "Band Structure" of the Spacetime Medium

**Setup**: Use two (or more) lasers of different wavelengths, either simultaneously or alternately. Record two trajectories on the same cylinder.

```
Laser 1: λ₁ = 633 nm (He-Ne red)
Laser 2: λ₂ = 405 nm (semiconductor violet)

Standard prediction:
  The two trajectories have different Δx because n(λ₁) ≠ n(λ₂)
  Δ(Δx) = (vR/c)·[n(λ₂)−n(λ₁)]
  Fully determined by the standard dispersion relation (Sellmeier formula)
```

**Non-standard signal**: If the Δ(Δx) relationship between different wavelengths deviates from the Sellmeier formula → the dispersion of the spacetime medium differs from the EM dispersion of the physical medium. If anomalous dispersion peaks appear at specific frequencies → the spacetime medium has a "band structure" akin to a crystal lattice.

---

### Variant 9: Rotating the Entire Apparatus — Searching for a Preferred Reference Frame

**Setup**: Instead of rotating the laser at the cylinder center — **rotate the entire apparatus (laser + cylinder + medium) as a rigid body about a vertical axis at angular velocity Ω.**

```
Entire apparatus rotates about a vertical axis → photon flight path rotates with the apparatus

Standard prediction (Sagnac effect):
  Extra deflection angle sensed by the photon ≈ 2ΩR/c
  For R=3 m, Ω=10 rad/s → ~2×10⁻⁷ rad → far below resolution
  → Standard prediction: no observable effect
```

**Non-standard signal**: If emergent spacetime has a preferred reference frame (analogous to the 19th-century "ether frame" but deeper), the one-way speed of light measured in different directions will differ when the apparatus moves relative to that frame. The trajectory will exhibit a θ-dependent periodic modulation with period 2π — which is the single-pass version of the Michelson-Morley experiment, waiting 140 years.

---

### Variant 10: Time-Varying Medium — "Memory Effect" of the Spacetime Medium

**Setup**: Actively change the medium density during the brief interval (~6 ms) in which the laser sweeps the cylinder. E.g., rapidly inject/withdraw a small amount of liquid, or switch a heater on/off.

```
t = 0: Laser begins emission, medium in state A
t = 3 ms: Rapid switch to state B (pressure pulse or thermal pulse)
t = 6 ms: One revolution complete

Standard prediction:
  Trajectory shows a continuous transition at the angle corresponding to t=3 ms
  Transition slope determined by dn/dt (density change rate)
```

**Non-standard signal**: If the trajectory begins deviating **before** the density change — the speed of light changes before the medium does → **the spacetime medium has "premonition" of an impending change** (in emergent systems, "time" may not be global, but emerges from underlying correlations → strict causal ordering may be blurred).

Or the opposite — the trajectory slowly catches up **after** the density change → **the spacetime medium has inertia/memory**, requiring finite time to "receive" the medium change.

---

### Variant 11: Static Gravitational Gradient — Does Gravity Influence c Beyond GR?

**Setup**: Place a high-density mass (lead or tungsten block, 10³–10⁴ kg) fixed beside the cylinder. Photons emitted in different θ directions have different closest-approach distances to the mass.

```
                ┌──────────────────────┐
                │                      │
                │    ╲  ← toward mass  │
                │   ●──────────────────│──→ ·M
                │    ╱  ← away from mass│  (10³–10⁴ kg)
                │                      │
                └──────────────────────┘

Different θ → different gravitational potential depth → different Shapiro delay
```

**Standard prediction (General Relativity)**: Shapiro delay Δt(θ) ≈ (2GM/c³)·ln(geometric factor). For M = 10⁴ kg, D = 5 m, R = 3 m — the differential Shapiro delay between different θ is ~10⁻³¹ s, corresponding to trajectory deviation ~10⁻³⁰ m. **At experimental precision, strictly zero. The standard GR-predicted signal is zero.**

**Non-standard signal**: If, within the emergence framework, matter influences the speed of light not by curving spacetime but by directly modifying the "elastic modulus" of the spacetime medium, the effect may far exceed the GR Shapiro delay. The trajectory exhibits a θ-dependent modulation with a minimum in the direction of the mass — at an amplitude within the experimentally measurable range.

**Relationship to existing variants**: Complements Variant 4 (EM field loading). Variant 4 tests "can electromagnetic forces change c?"; this variant tests "can gravity change c?" Together they cover the possible emergent coupling channels for two of the fundamental forces (excluding the strong and weak interactions) within the Standard Model.

---

### Variant 12: Accelerating Cylinder — Single-Pass Test of the Equivalence Principle

**Setup**: The cylinder falls with constant acceleration a (free-fall or mechanically driven, e.g., drop tower or acceleration track). Axial velocity varies with time: v(t) = v₀ + at.

```
Cylinder falls with acceleration a
    ↓
Velocity of laser plane relative to cylinder continuously changes
    ↓
Trajectory is not a straight line — it's a parabola
```

Trajectory equation becomes:

```
z'(θ) = v₀(θ/ω + R/c) + (a/2)(θ/ω + R/c)²
```

On the unwrapped surface, this is a **parabola** whose curvature is fully determined by the independently measured acceleration a.

**Standard prediction**: A precise parabola — determined entirely by the independently measured a and v₀, with zero first-order free parameters. The equivalence principle (a cornerstone of GR) asserts that an accelerating reference frame is locally equivalent to a uniform gravitational field, so the parabola should hold perfectly.

**Non-standard signal**: Deviation from the standard parabola → the equivalence principle is violated at the single-pass light-propagation level. This has **never been tested experimentally** — all existing equivalence-principle tests use round-trip light signals or non-optical probes (torsion balances, atom interferometers, lunar laser ranging for the Nordtvedt effect).

**Relationship to existing variants**: Complements Variant 9 (rotating the entire apparatus). Variant 9 tests rotational inertia; this variant tests accelerational inertia. Together they constitute a dual test of Lorentz invariance + equivalence principle in the single-pass regime — a regime never before covered by any experiment.

---

### Variant 13: Polarization Dependence — Does the Spacetime Medium Have an "Optical Axis"?

**Setup**: Same cylinder, multiple runs — switching the laser polarization state each time.

```
Run A: Horizontal linear polarization (E⃗ parallel to cylinder axis)
Run B: Vertical linear polarization (E⃗ perpendicular to cylinder axis)
Run C: Left/right circular polarization

Record trajectories separately; compare Δx and microscopic features.
```

**Standard prediction (in vacuum)**: All polarization states yield exactly the same trajectory. Vacuum is perfectly isotropic in Maxwell's equations — no "optical axis," no birefringence. In a medium, known birefringence can be precisely calculated and subtracted from the dielectric tensor.

**Non-standard signal**: Statistically significant differences between polarization states → the spacetime medium itself has intrinsic anisotropy — a "preferred direction." This is a signal predicted by Lorentz-violating extensions of the Standard Model (SME), but has **never been searched for in a single-pass experiment.** All existing polarization tests are based on interferometers (round-trip), with upper bounds coming from the second-order residuals after round-trip cancellation.

**Cost**: A set of polarizers/wave plates + repeat the experiment a few times. Virtually zero.

---

### Variant 14: Rotating Medium (Vortex) — Angular Momentum Coupling

**Setup**: Liquid rotates within the cylinder at angular velocity Ω_fluid about the axis, forming a stable vortex. Photons traverse different angular-velocity layers of the rotating fluid during radial flight.

```
         ┌──────────────────────┐
         │   ↻  Water rotates   │
         │     ╱               │
         │    ●────────────────│
         │     ╲               │
         │   ↻  ω_fluid(r)     │
         └──────────────────────┘
```

**Standard prediction**: For radially propagating photons, the radial projection of the rotational Fresnel-Fizeau drag is zero (medium velocity is perpendicular to the light propagation direction). At non-relativistic rotation rates, standard EM predicts a trajectory **exactly identical** to the stationary-medium case.

**Non-standard signal**: The angular momentum of the medium directly "drags" the spacetime medium — analogous to frame-dragging in GR (Lense-Thirring effect) but appearing at the desktop scale. The radial light speed exhibits a θ-dependent modulation.

**Relationship to existing variants**: Complements Variant 7 (radially flowing medium). Variant 7 tests linear momentum coupling; this variant tests angular momentum coupling. In the emergence framework, the two may be different projections of the same "momentum-spacetime coupling constant"; comparing the two results can determine the tensor structure of that constant.

---

### Variant 15: Combined Strong Field + Gravitational Loading — Nonlinear Coupling

**Setup**: Simultaneously load Variant 4 (EM field) and Variant 11 (gravitational gradient). Perform four runs for differential analysis.

```
Run 1: E=0, M=0 (baseline trajectory)
Run 2: E>0, M=0 (EM loading only)
Run 3: E=0, M>0 (gravitational loading only)
Run 4: E>0, M>0 (combined loading)

Compare: effect of Run 4 ?=? effect of Run 2 + effect of Run 3
```

**Standard prediction**: Linear superposition of the two effects. Both individual effects ≈ zero at experimental precision → superposition ≈ zero.

**Non-standard signal**: Combined effect > linear superposition of individual effects → emergent coupling is nonlinear — the EM field changes the responsiveness of the spacetime medium to gravity ("the EM field softens the spacetime spring; gravity then presses on it with amplified effect").

**Physical analogy**: In condensed matter physics, an electric field can change the elastic modulus of a material by modifying the electronic structure, thereby indirectly changing the speed of sound. If spacetime is emergent, a similar mechanism may exist — two independent loadings share the same response channel at the底层 (fundamental level); individually they are too small to see, but under combined loading they are nonlinearly amplified.

**Relationship to existing variants**: This is the only variant that tests "cross-coupling." All other variants assume the loading channels are independent — if they are not independent, only combined loading can discover it.

---

### Variant 16: Cylinder Self-Rotation — Is Vacuum a Medium?

**Setup**: The cylinder rotates at angular velocity Ω_cyl about its own axis. The interior of the cylinder is **vacuum** (or stationary air). The laser rotates at ω; both share the same axis.

```
              Laser rotates at ω
              ●──────────────→
             ╱                │
            ╱   Cylinder at   │
           ╱    Ω_cyl (high   │
          ╱     speed)        │
         ╱    Interior: VACUUM│
        ●──────────────────────│
```

**Standard prediction**: In the laboratory frame, the photon travels in a purely radial straight line — the flight time R/c is entirely independent of whether the cylinder is rotating. The interior is vacuum; there is no medium to be "dragged." The standard-predicted signal is **strictly zero**.

**Non-standard signal**: Δx varies with Ω_cyl. This means:

```
The speed of light in vacuum depends on the rotational state of nearby matter
    ↓
"Vacuum" is not truly empty — it is a medium that can be influenced by nearby matter through rotation
    ↓
The rotating boundary "drags" that medium → changes the speed of light within it
    ↓
c is not a fundamental constant written on the first line of the universe's code
c is a function of the elastic modulus of that medium
    ↓
Vacuum = medium, speed of light = property of the medium
```

**Among all 16 variants, this is logically the least likely but philosophically the most profound.** If it yields a positive signal, no material filling, no electromagnetic field, no gravity — merely a rotating metal cylinder — changes the speed of light in the vacuum within it. The concept of "vacuum" itself requires a complete rewrite: it is not "nothing," but a physical entity that can be influenced by matter in motion. The standard prediction is absolute zero — no GR or QFT mechanism exists that could explain a non-zero signal. Precisely for this reason, any non-zero signal is clean, indisputable new physics.

---

## Variant Summary Table

| # | Variant | Difficulty | Standard Predicted Signal | Scientific Significance | Core Question |
|---|------|:---:|:---:|:---:|------|
| 1 | Critical point experiment | Medium | Precisely described by OZ theory | 5 | Do critical fluctuations amplify spacetime coupling? |
| 2 | Different substances, same n | Low | Trajectories exactly identical | 4 | Does chemical composition affect light speed? |
| 3 | Acoustic standing wave phase | Low | Trajectory synchronized with density wave | 4 | Does the spacetime medium have a relaxation time? |
| 4 | EM field loading | Medium | Zero (at experimental precision) | 3 | Can EM fields polarize the spacetime medium? |
| 5 | Sharp interface | Low | Clean kink | 4 | Transition width = interface width? |
| 6 | Temperature gradient | Low | Curvature determined by n(T) | 3 | Does temperature directly affect spacetime stiffness? |
| 7 | Flowing medium | Medium | Fizeau drag f = 1−1/n² | 3 | Does the drag coefficient deviate from the standard value? |
| 8 | Multi-wavelength dispersion | Low | Sellmeier dispersion | 2 | Does the spacetime medium have a "band structure"? |
| 9 | Rotate entire apparatus | High | Zero (at experimental precision) | 2 | Does a preferred reference frame exist? |
| 10 | Time-varying medium | Medium | Continuous transition | 3 | Does the spacetime medium have "memory"/"premonition"? |
| 11 | Static gravitational gradient | Medium | Zero (at experimental precision) | 3 | Does gravity influence c beyond GR? |
| 12 | Accelerating cylinder | Medium | Precise parabola | 4 | Does the equivalence principle hold at the single-pass light level? |
| 13 | Polarization dependence | Very low | Zero (in vacuum) | 3 | Does the spacetime medium have an intrinsic optical axis? |
| 14 | Rotating medium (vortex) | Medium | ≈ Zero (radial path) | 3 | Does angular momentum drag the spacetime medium? |
| 15 | Strong field + gravity combined | High | Zero (linear superposition ≈ zero) | 2 | Is emergent coupling nonlinear? |
| 16 | Cylinder self-rotation | Medium | Strictly zero | 5 | Is vacuum a medium? |

---

### Final Note on the Experimental Variants

All these variants share the same core logic:

```
Use ordinary matter as a "probe" to perturb the environment of light propagation
    ↓
If the response of the speed of light is fully described by Maxwell's equations → the emergence window is excluded
If the response of the speed of light partially deviates from Maxwell's predictions → the spacetime medium exists and couples to matter
```

**And Maxwell's equations often make predictions for these variants that are either extremely precise or exactly zero — meaning any deviation is a clean signal, without the need to argue about "whether it's an electromagnetic effect."** A null result excludes the coupling; a non-null result proves its existence. Either way, the information density is orders of magnitude higher than the single original experiment.


---

## Supplementary Notes: Principle Rigor, Geometric Necessity, and Parameter Space

> The following content addresses the most critical theoretical objections to the experimental design, and uses the exclusion boundaries of existing experiments to precisely locate this experiment in parameter space.

---

### I. Rigorous Verification of No Clock Synchronization

The core objection: the derivation z'(θ) = v(θ/ω + R/c) introduces a time parameter τ — does it surreptitiously use a distant clock?

**No.** The entire derivation needs only a single clock at the laser position. Step-by-step verification:

**1. Measurement of v:** Cylinder base passes the laser → record τ = 0. Cylinder trailing edge passes the laser → record τ = Δτ_pass. Both events occur at the laser's location. v = H/Δτ_pass. Single clock throughout.

**2. Measurement of ω:** Laser completes one rotation → detector (fixed beside the laser) receives two reflection signals. T_rot = time difference between the two signals. Same detector, same clock.

**3. Establishment of constraint H/v = 2π/ω:** Compare two time intervals — Δτ_pass and T_rot — using **the same clock** reading. Adjust v or ω or H until equality holds. No distant clock involved.

**4. Distance from cylinder base to laser:** The cylinder base departs from the co-located position at τ = 0. After τ seconds, distance = v·τ. This is a **kinematic integral** — initial condition (co-located, distance = 0) + equation of motion (constant v). It is not "measuring the position of the distant cylinder base at time τ." v·τ as a computed quantity requires no simultaneity convention.

**5. Origin of photon flight time Δτ:** When the photon reaches the cylinder wall, the laser clock does not record it (the arrival event is not at the laser). But Δτ is **back-inferred** from spatial measurements: Δx = ωR·Δτ → Δτ = Δx/(ωR) → c = R/Δτ = ωR²/Δx. Δx is measured with a ruler on the stationary cylinder; ω is measured with the laser clock at the co-located position; R is measured with a ruler. Δτ is not a clock reading — it is a combination of three spatial-mechanical measured quantities.

**6. Essential test:** The emission and arrival events are not on the same worldline. In relativity, the "time interval between two events" generally depends on the simultaneity convention. But this experiment **does not relate them via simultaneity** — instead, it relates them through the accumulated quantities of two independent physical processes:

```
How many degrees the laser rotated from emission to arrival → angular displacement = ω·Δτ
How far the cylinder moved from emission to arrival       → axial displacement = v·Δτ
```

Each process independently measures the same Δτ. The linearity of the trajectory is itself a cross-validation of these two independent measures. If they disagree (non-straight trajectory), the experiment detects that too. If they agree — Δτ is a physical reality, independent of any simultaneity convention.

**Verdict: The experiment does not depend on the Einstein synchronization convention. All temporal quantities use a single clock; all spatial quantities use a single ruler. Δτ is cross-validated from two independent channels and does not require distant-clock alignment.**

---

### II. Necessity of the Constraint H/v = 2π/ω

Superficially, this appears to be a convenience condition for mathematical simplification — without it, the derivation of c = ωR²/Δx still holds (v and H cancel in the final formula). But **experimentally, without this constraint, the signal cannot be measured.**

**What happens without the constraint:**

```
Total time for cylinder to pass through laser plane = H/v
Total angle swept by laser θ_total = ω·(H/v)  ← can be any angle

Trajectory endpoint θ_end = ωH/v − ωR/c
Gap Δθ = θ_total − θ_end = ωR/c
```

The problem lies in θ_total — the "virtual endpoint the laser would have swept to but didn't mark" — it has **no physical mark whatsoever** on the cylinder wall. The cylinder has already passed. How do you locate this "nothing" position?

**The constraint makes θ_total = 2π — i.e., 0 — i.e., the angular position of the trajectory start point.** The cylinder is a closed surface; θ = 2π and θ = 0 are physically the same meridian. Thus:

```
Start point = physical mark (there is indeed an etched trace on the cylinder)
End point   = physical mark (there is indeed an etched trace on the cylinder)
Gap         = blank arc length between two physical marks on the unwrapped surface
```

Δx transforms from a virtual quantity that requires indirect inference from slope s = v/ω and H (two quantities with measurement errors, compounded in their quotient) into a **quantity directly measurable with a ruler.** At Δθ ~ 10⁻⁷ rad, indirect inference would be swamped by error; in direct measurement, it is simply a blank segment under the ruler.

**The constraint is not a "convenience condition" — it is the dividing line that makes the experiment transition from mathematically correct to physically executable.**

---

### III. Geometric Necessity of Round-Trip Cancellation

Why have Michelson-type experiments consistently yielded null results for 140 years? This does not necessarily mean "no fluctuations exist" — it is because the round-trip path naturally cancels the first-order effect of fluctuations.

**Geometric fact (independent of any theory):**

```
Round-trip path:
  A ──────→ B ──────→ A
       c₁           c₂

  Total time t = L/c₁ + L/c₂

  If c₁ = c₀(1−ε), c₂ = c₀(1+ε):
  t = L/c₀ · [1/(1−ε) + 1/(1+ε)]
    ≈ (2L/c₀) · (1 + ε² + ε⁴ + …)
                      ↑
              The first-order term ε vanishes — leaving ε² (second-order)

Single-pass path (this experiment):
  A ──────→ B
       c

  Total time t = L/c  ← ε is directly exposed
```

Interferometers are inherently differential measurements — the two arms cancel each other, and the round trip within the same arm also cancels. All experiments based on round-trip light paths — Michelson, Foucault, laser ranging, GPS carrier phase — are naturally insensitive to the **first-order effect** of fluctuations.

**This does not mean no fluctuations exist. It only means that if fluctuations do exist, the round-trip path consumes them.**

More precisely: if the fluctuations are **vector-type** (directional preference — eastward fast, westward slow), a Michelson interferometer's two orthogonal arms perform a differential measurement, treating the residual as signal. But if the fluctuations are **scalar-type** (all directions synchronously fast or slow), both arms experience the same ε → null result is completely unsurprising. This experiment is pure single-pass, pure radial — there is no differential cancellation geometry.

**This experiment's sensitivity is several orders of magnitude worse than Michelson-type experiments — but it observes a class of signals that Michelson fundamentally cannot see. Precision is not the point; geometry is.**

---

### IV. Parameter Space Exclusion Map

This experiment is not competing with Cassini, LLR, or GPS on sensitivity. It is covering a **(δc/c, λ) window that has never been experimentally constrained.**

**Exclusion boundaries of existing experiments:**

The cumulative effect of spatial light-speed fluctuations follows white-noise statistics — a beam of light traveling distance D (D ≫ correlation length λ) traverses N ≈ D/λ independent fluctuation cells; the accumulated timing error is compressed by the √N averaging effect:

```
Fractional distance error: σ_D/D = (δc/c) · √(λ/D)
Equivalent constraint quantity: (δc/c) · √λ = (σ_D/D) · √D
```

| Experiment | D (m) | σ_D (m) | (δc/c)·√λ upper bound | Covered λ range |
|------|------:|------:|:---:|:---:|
| Optical clock fiber link | 10⁴ | 3×10⁻¹⁶ | **~10⁻¹⁷** | < 1 μm |
| Cassini Saturn ranging | 1.3×10¹² | ~1 m | **~10⁻⁸** | < 1 mm |
| LLR APOLLO | 3.8×10⁸ | ~0.01 m | **~5×10⁻⁸** | < 0.1 m |
| GPS carrier phase | 2×10⁷ | ~0.001 m | **~2×10⁻⁷** | 0.01–1 m |
| VLBI | 6×10⁶ | ~0.001 m | **~1×10⁻⁶** | 0.01–1 m |
| **This experiment (desktop)** | **~3** | **Trajectory σ_z~0.5 nm** | **~5.8×10⁻²** | **0.1–10 m** |

Converted to δc/c exclusion upper bounds at specific λ:

| Experiment | λ=1 μm | λ=1 mm | **λ=1 m** | λ=1 km |
|------|:---:|:---:|:---:|:---:|
| Cassini | 1×10⁻⁵ | 4×10⁻⁷ | **1×10⁻⁸** | 4×10⁻¹⁰ |
| LLR | 5×10⁻⁵ | 2×10⁻⁶ | **5×10⁻⁸** | 2×10⁻⁹ |
| GPS | 2×10⁻⁴ | 7×10⁻⁶ | **2×10⁻⁷** | 7×10⁻⁹ |
| VLBI | 1×10⁻³ | 4×10⁻⁵ | **1×10⁻⁶** | 4×10⁻⁸ |
| **This experiment** | **58** | **1.8** | **0.058** | **2×10⁻³** |

**In practice, experiments cover windows rather than lines. The exclusion map in the (δc/c, λ) plane is as follows (illustrative, not to precise scale):**

```
δc/c
  ↑
10⁰ │                           ┌──────────────────┐
     │                           │  Completely unknown│
     │                           │  λ ~ 0.1–10 m    │
10⁻² │                           │  δc/c arbitrary  │
     │                           │                  │
     │                           │  ← This experiment's │
     │                           │     window       │
     │                           └──────────────────┘
10⁻⁴ │  │← Cassini ──→│              ░░░░░░░░░░░
     │  │  │← LLR →│  │              ░ Unconstrained░
10⁻⁶ │  │  │  │GPS│  │              ░░░░░░░░░░░
     │  │  │  │   │  │
10⁻⁸ │  │  │  │   │  │
     │──┴──┴──┴───┴──┴───────────────────────────→ λ
     nm   μm   mm   m    10m   100m   km

Excluded region: ████████████████████████████████████
Unknown region (first probed by this experiment): ░░░░░░░░
```

**This experiment's sensitivity is 4–6 orders of magnitude worse than Cassini. But the window it observes — λ ~ 0.1–10 m — had an upper bound of "unconstrained" before it (δc/c could be 100%, 50%, any value). Even merely pushing the upper bound from ∞ to 5.8% represents a three-order-of-magnitude advance.** Precision experiments do "push the known exclusion line a bit lower." This experiment does "draw the first exclusion line where none existed." The latter is pioneering; pioneering does not require precision — it only requires arriving first.

**Note on the √N averaging effect:** The above exclusion boundaries are based on the white-noise assumption (cells independently random). If the emergent system produces 1/f-type noise (long-range correlations, memory), the √N averaging advantage of long-path experiments is substantially weakened. In condensed matter physics, collective fluctuations in emergent systems exhibit 1/f spectra as the norm rather than the exception. If spacetime behaves likewise — the "advantage" of long-path experiments may be an illusion, while the short-path experiment can directly observe the fluctuation pattern.

---

### V. On the Implementation of the 16 Experimental Variants

The 16 variants described above share the same core apparatus (uniform cylinder + rotating laser); most only require replacing the medium inside the cylinder or applying an external field. Sorted by difficulty:

| Difficulty | Variants | Core Addition |
|:---:|------|------|
| Very low | Sharp interface, same-n different substances, acoustic standing wave, multi-wavelength dispersion, polarization dependence | Replace liquid / add transducer / change laser wavelength / add polarizer |
| Low | Temperature gradient, time-varying medium | Temperature control / injection system |
| Medium | Critical point, EM field loading, flowing medium, gravitational gradient, accelerating cylinder, rotating medium, cylinder self-rotation | High-pressure chamber / magnet / circulation pump / mass / drop tower / vortex generator / rotation platform |
| High | Rotate entire apparatus, strong-field + gravity combined | Rotating mechanical platform / combined loading system |

Since all variants reuse the same core apparatus and the same analysis workflow (unwrap cylinder → microscopically scan trajectory → extract gap and fluctuation features), **the 16 variants can be designed as a single experimental sequence and run consecutively on the same apparatus, without prioritization.** The time to change media and apply external fields is far less than the time to build and align the apparatus.

A reasonable implementation timeline:

```
Weeks 1–2: Build core apparatus (cylinder + rotating laser + photoresist coating)
Week 3:    Original experiment (air/vacuum) → baseline trajectory
Week 4:    Sharp interface + same-n different substances + acoustic standing wave + polarization dependence (liquid/optics group)
Week 5:    Temperature gradient + time-varying medium + flowing medium (controlled-environment group)
Week 6:    Gravitational gradient + rotating medium + cylinder self-rotation (mechanical loading group)
Weeks 7–8: Critical point experiment (high-pressure chamber — most complex but highest potential return)
Week 9:    Accelerating cylinder + rotating entire apparatus (inertial group — may require external facilities like a drop tower)
Week 10:   EM field loading + strong-field gravity combined (EM group + combined loading)
Week 11:   Data analysis — trajectory comparison across all 16 variants
```

**If there is anything in the window: it is too large to miss on the first attempt. If there is nothing in the window: the aggregate null result of all 16 variants will, for the first time, exclude δc/c > 5.8% fluctuations in the λ ~ 0.1–10 m scale range, while simultaneously excluding emergent coupling across six independent channels: electromagnetic, gravitational, inertial, polarization, angular momentum, and chemical composition. Either outcome represents a physical territory never before touched by experiment.**

Furthermore, the 16 variants collectively constitute a **phenomenological scanning matrix** that does not depend on any theoretical presupposition — each variant measures the response partial derivative of c with respect to a different physical variable:

```
Variant 6 (temperature gradient)  → ∂c/∂ρ       (c's dependence on density)
Variant 4 (EM field)              → ∂c/∂(E²)    (c's dependence on EM field)
Variant 12 (accelerating cylinder)→ ∂c/∂a       (c's dependence on acceleration)
Variant 11 (gravitational gradient)→ ∂c/∂(GM/r) (c's dependence on gravitational potential)
Variant 2 (different substances)  → whether c is determined solely by n (decoupling test)
```

If any non-zero signal exists, this set of partial derivatives can — without any presupposed theory — distinguish whether "c is merely an alias for Maxwell's refractive index" or "c is the local value of an independent emergent quantity": the former requires all ∂c to be reducible to ∂n, while the latter allows ∂c to be independent of ∂n. **These 16 variants are not 16 independent experiments — they are a single measurement matrix for the partial derivatives of c(x).**

---

### Engineering Optimization: Reverse Rotation to Amplify the Signal

In the original experiment, the cylinder does not rotate (Ω_cyl = 0). If the cylinder is rotated in the direction opposite to the laser (Ω_cyl = −kω, k > 0):

```
Relative angular velocity: ω_rel = ω − Ω_cyl = (1+k)ω
Gap amplification:         Δx = (1+k)·ωR²/c
Signal enhancement:        (1+k)×
```

k = 1 (cylinder and laser rotating at equal and opposite speeds) is the optimal cost-benefit ratio — the gap doubles without changing any other experimental parameters (R, ω, v unchanged; accept that the trajectory covers only half a revolution). The limitation is the cylinder's centrifugal stress: wall linear velocity = kωR, centrifugal force ∝ k². For R = 3 m, ω = 1000 rad/s, k = 1, centrifugal acceleration ≈ 9×10⁵ g, requiring carbon-fiber composite cylinders.

**This is not a new variant — it is a pure engineering optimization of the original experiment, changing no physical principle, merely amplifying the signal by a factor of two.**

---

*Created: 2026-07-31 | Revised: 2026-07-31 (corrected experimental principle; added uniform-cylinder derivation, microstructure analysis, detection sensitivity calculations, emergent-medium scale estimates, recording methods and error analysis, theoretical premises, null-result impact analysis, 16 experimental variants, supplementary notes: principle verification, constraint necessity, round-trip cancellation, parameter space, implementation roadmap, astronomical-layer prudence note, multi-messenger extension)*

