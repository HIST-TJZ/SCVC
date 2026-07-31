# One-Way Speed of Light: Rotating Laser Burn Mark Method

## Abstract

We propose a tabletop-to-medium-scale experiment to measure the one-way speed of light without relying on remote clock synchronization. The core idea: **encode the photon flight time \(R/c\) as a spatial offset \(\Delta x\) on a recording surface via uniform motion, then amplify that offset to a measurable scale using the laser's angular velocity \(\omega\).** On the unwrapped recording surface, the experiment reduces to an elementary geometric problem — "two lines, one angle." Measure the vertical distance \(z_{\min}\) from the burn mark's lowest point to the base, and the angle \(\alpha\) between the burn mark and the horizontal:

\[
\boxed{c = \frac{\omega R^2}{z_{\min} / \tan\alpha}}
\]

All measured quantities are spatial and obtained within a single rigid reference frame. Recommended entry parameters: \(R = 5\)–\(10\) m, \(\omega = 300\)–\(1000\) rad/s, yielding \(\Delta x = 25\)–\(330\) μm, measurable with an optical microscope.

---

## 1. Introduction: Why the One-Way Speed Has Never Been Measured

All known light-speed experiments — Fizeau's gear wheel (1849), Foucault's rotating mirror (1862), Michelson's interferometer (1887), modern laser ranging — measure the **round-trip speed of light** (A→B→A). The one-way speed (A→B, no return) has never been directly measured.

The reason is not a technical limitation but a logical circularity: measuring the one-way time from A to B requires clocks at A and B to be precisely synchronized — **and synchronizing those clocks itself requires knowing the speed of light.**

Einstein addressed this circularity in 1905 by declaring it a **convention**: he *defined* the one-way speed to equal the round-trip speed. All of Special Relativity is built upon this definition.

> "Defined equal" does not mean "measured and confirmed equal."

In the 120 years since, philosophers of science — Reichenbach, Grünbaum, and others — have systematically argued for the "conventionality of simultaneity": the \(\varepsilon\)-synchronization framework shows that any \(\varepsilon \in (0,1)\) yields a logically self-consistent physics. Einstein chose \(\varepsilon = 1/2\) for simplicity, not by experimental necessity.

This proposal attempts to break the deadlock: not through remote clock synchronization, but by **encoding time into space via motion**.

---

## 2. Core Idea: Motion Encodes Time

### 2.1 Why Motion Encodes Time

The circularity of the traditional approach stems from a single implicit fixation — **one must know when the light departed.**

Consider the following geometry: a cylinder moves along its axis at constant velocity \(v\). A laser at the cylinder's center rotates at constant angular velocity \(\omega\). At time \(t\), the laser points to angle \(\theta(t) = \omega t + \theta_0\) (where \(\theta_0\) is an unknown initial angle).

A photon emitted at this moment travels radially for \(R/c\) seconds to reach the cylinder wall. Upon arrival, the cylinder has moved forward by \(vR/c\). In the cylinder's own coordinate system (origin at the base), the burn mark height is:

\[
z'(t) = v\left(t + \frac{R}{c}\right) = \frac{v}{\omega}(\theta - \theta_0) + \frac{vR}{c}
\]

where \(\theta = \omega t + \theta_0\) is the emission angle. Eliminating \(t\), the burn mark trajectory in the \((\theta, z')\) plane is:

\[
\boxed{z'(\theta) = \frac{v}{\omega}\theta - \frac{v}{\omega}\theta_0 + \frac{vR}{c}}
\]

**Key insight**: the axial motion \(v\) and the angular motion \(\omega\) share the same time parameter \(t\). The finite speed of light \(R/c\) introduces a constant vertical offset \(vR/c\) in the burn mark. This offset is independent of the unknown initial angle \(\theta_0\) — \(\theta_0\) only shifts the burn mark as a whole along the angular axis, without affecting local geometry.

### 2.2 Geometry on the Unwrapped Surface: Two Lines, One Angle

Cut the cylinder along any vertical line and unwrap it into a plane. The horizontal axis is \(x = R\theta\) (arc length), the vertical axis is \(z'\) (height).

On this plane, the burn mark equation is:

\[
z'(x) = \frac{v}{\omega R}x - \frac{v}{\omega}\theta_0 + \frac{vR}{c}
\]

This is a **straight line with slope \(s = v/(\omega R)\)**.

The burn mark has a **natural lowest point** (visual starting point) — this corresponds to the first photon that reached the cylinder wall. At \(t = 0\) (the moment the cylinder base just reaches the laser plane), the laser points to \(\theta_0\). The photon takes \(R/c\) to arrive, during which the cylinder descends by \(vR/c\). Hence the lowest point height:

\[
z_{\min} = \frac{vR}{c}
\]

On the unwrapped surface, you now see:

```
            ╱ ← Burn mark (straight line)
          ╱
        ╱
      ● ← Lowest point (x = Rθ₀, z = z_min)
     ╱│
   ╱  │ z_min
 ╱    │
●─────┴──── z = 0 (cylinder base)
   Δx
```

- **Line 1**: Cylinder base — horizontal line \(z' = 0\)
- **Line 2**: Burn mark — straight line with slope \(s = v/(\omega R)\)
- **One angle**: \(\alpha\) between burn mark and horizontal, \(\tan\alpha = s = \dfrac{v}{\omega R}\)

Extend the burn mark downward from the lowest point to the base (\(z' = 0\)). The **horizontal projection** of this extension is \(\Delta x\):

\[
\boxed{\Delta x = \frac{z_{\min}}{\tan\alpha} = \frac{vR/c}{v/(\omega R)} = \frac{\omega R^2}{c}}
\]

### 2.3 The One-Way Speed of Light Formula

From the above:

\[
\boxed{c = \frac{\omega R^2}{\Delta x}}
\]

Meaning and measurement of each quantity:

| Quantity | Physical meaning | Measurement tool |
|:---:|------|------|
| \(\omega\) | Laser angular velocity | Optical encoder / tachometer |
| \(R\) | Distance from center to wall | Laser interferometer / ruler |
| \(\Delta x\) | Horizontal projection of extension segment | Ruler / microscope (on unwrapped surface) |

**All three are purely spatial quantities. No clock synchronization, no remote time transfer, no period constraint \(H/v = 2\pi/\omega\).** The unknown initial angle \(\theta_0\) cancels in the derivation of \(\Delta x\) (both the lowest point and the extension endpoint contain \(\theta_0\); the difference eliminates it). The descent velocity \(v\) also cancels.

---

## 3. Experimental Setup

### 3.1 Core Components

```
                    Cylinder R = 5–10 m, H = 0.5–1 m
                    ┌──────────────────────┐
                    │                      │
                    │    ╱ ← Laser         │ ← Photosensitive inner wall
                    │  ╱                  │
                    │╱                    │
                    ● ← Laser (rotating at ω)
                    │                      │
                    ├──────────────────────┤ ← Laser plane (fixed)
                    │         ↓ v          │
                    └──────────────────────┘
```

- **Cylinder**: Radius \(R\), height \(H\). Inner wall coated with photosensitive material — sprayed photoresist, or flexible polyimide film pre-coated with photographic emulsion
- **Laser**: Fixed at center, rotates at constant \(\omega\) in the horizontal plane. Can be implemented with a fixed laser + rotating mirror, or a rotating platform directly driving a laser diode
- **Laser plane**: Fixed in the laboratory frame. The cylinder descends at constant velocity through the laser plane
- **Descent mechanism**: Air-bearing guideway, pulley system, or drop tower. Must ensure constant \(v\)
- **Vacuum chamber**: Optional but recommended — eliminates air refractive index fluctuations (\(\delta n \approx 10^{-6}\) at \(10^{-3}\) torr)

### 3.2 No Period Constraint Required

Earlier versions of this proposal required \(H/v = 2\pi/\omega\) (the cylinder's transit time through the laser plane equals one full laser rotation), so that the "gap" in a full spiral trajectory would reveal \(\Delta x\).

**In the "two lines, one angle" formulation, this constraint is unnecessary.** Regardless of the values of \(v\) and \(\omega\), the local geometric quantity \(\Delta x = z_{\min} / \tan\alpha\) locked by the burn mark's lowest point and slope is always equal to \(\omega R^2 / c\), independent of cylinder height or descent velocity. \(H\) need only be large enough for the burn mark to span sufficient length for accurate slope measurement.

### 3.3 Recording Method

Recommended: **metal film laser direct writing**. Sputter a 100 nm aluminum film on the cylinder inner wall. A pulsed nanosecond laser ablates the aluminum, leaving a transparent trench as the burn mark. Advantages: no chemical development, extremely high contrast, line width limited by diffraction.

Alternative: high-sensitivity photoresist + development + AFM scanning.

---

## 4. Measurement Procedure

| # | Operation | Tool |
|:---:|------|------|
| 1 | Release cylinder from above laser plane; let it descend at constant velocity through the plane | Descent mechanism |
| 2 | Laser burns inner wall, forming a spiral burn mark | — |
| 3 | Remove cylinder liner → cut along any vertical line → unwrap into a plane | — |
| 4 | Locate burn mark lowest point on unwrapped surface; measure its vertical distance \(z_{\min}\) to base edge | Microscope + scale |
| 5 | Take a sufficiently long segment of the burn mark; measure \(\Delta z\) and corresponding \(\Delta x\) → compute slope \(s = \Delta z / \Delta x\) → \(\tan\alpha = s\) | Microscope + scale |
| 6 | Compute \(\Delta x = z_{\min} / \tan\alpha\) | — |
| 7 | \(c = \omega R^2 / \Delta x\) | — |

### Equivalent Alternative

If direct slope measurement is inconvenient, take any two widely separated points \((x_1, z_1)\) and \((x_2, z_2)\) on the burn mark:

\[
\tan\alpha = \frac{|z_2 - z_1|}{|x_2 - x_1|}
\]

Then \(\Delta x = z_{\min} / \tan\alpha\) as before.

---

## 5. Order of Magnitude

| \(R\) | \(\omega\) | \(z_{\min}\) (\(v = 1\) m/s) | \(\tan\alpha\) (\(v=1\)) | \(\Delta x\) | Measurement tool |
|:---:|:---:|:---:|:---:|:---:|---|
| 0.3 m | 300 rad/s | 1 nm | 0.011 | 90 nm | AFM |
| 2 m | 300 rad/s | 6.7 nm | 0.0017 | 4 μm | Microscope |
| **5 m** | **300 rad/s** | **17 nm** | **0.00067** | **25 μm** | **Microscope** |
| **10 m** | **300 rad/s** | **33 nm** | **0.00033** | **100 μm** | **Microscope, clear** |
| 10 m | 1000 rad/s | 33 nm | 0.0001 | 330 μm | Naked eye + ruler |

**Key relationships**: \(\Delta x \propto R^2\) — increasing radius gives quadratic returns. \(\Delta x \propto \omega\) — increasing angular velocity gives linear returns.

**Recommended entry configuration: \(R = 5\)–\(10\) m, \(\omega = 300\)–\(1000\) rad/s.** Under these parameters, \(\Delta x\) is in the 25–330 μm range, clearly measurable with an optical microscope.

Foucault in 1862 used a 20 m optical path and approximately 2500 rad/s rotating mirror to successfully measure the round-trip speed of light (error ~5%). This proposal matches Foucault's experiment in both optical path and rotational speed, but measures the **one-way** speed, and uses modern photosensitive materials and microscopes for readout.

---

## 6. Error Analysis

### 6.1 Error Propagation

From \(c = \omega R^2 / \Delta x\) and \(\Delta x = z_{\min} / \tan\alpha\):

\[
\frac{\delta c}{c} = \sqrt{
\left(\frac{\delta\omega}{\omega}\right)^2 +
\left(2\frac{\delta R}{R}\right)^2 +
\left(\frac{\delta z_{\min}}{z_{\min}}\right)^2 +
\left(\frac{\delta(\tan\alpha)}{\tan\alpha}\right)^2
}
\]

### 6.2 Component Estimates

| Error source | Typical precision | Relative error |
|:---|:---|:---:|
| \(\omega\) (optical encoder) | 0.01% | 0.01% |
| \(R\) (laser interferometer) | 10 μm / 10 m | 10⁻⁴% |
| \(\tan\alpha\) (long burn mark segment, averaged) | ≈0.1% | 0.1% |
| **\(z_{\min}\)** | **1 μm (microscope) / 17–33 nm (theoretical)** | **3%–6%** |

**Dominant term: \(z_{\min}\) measurement.** The theoretical value \(z_{\min} = vR/c\) is only 17–33 nm under recommended parameters — far below the optical microscope's resolution limit (≈200 nm).

### 6.3 Systematic Bias in \(z_{\min}\) and Its Elimination

What is actually measured is the *visible* lowest point of the burn mark — this position is determined by the ablation threshold of the photosensitive material, and is slightly higher than the theoretical lowest point. Let this bias be \(\Delta z_{\text{bias}}\):

\[
z_{\min}^{\text{(meas)}} = z_{\min}^{\text{(true)}} + \Delta z_{\text{bias}}
\]

Measure \(z_{\min,1}\) and \(z_{\min,2}\) at two different descent velocities \(v_1\) and \(v_2\):

\[
z_{\min,1} - z_{\min,2} = \frac{(v_1 - v_2)R}{c}
\]

\(\Delta z_{\text{bias}}\) cancels. Then:

\[
c = \frac{(v_1 - v_2)R}{z_{\min,1} - z_{\min,2}}
\]

This differential method reduces the systematic bias in \(z_{\min}\) to the statistical noise level.

---

## 7. The \(\omega\) Amplification Mechanism

The core amplification mechanism of this proposal lies in \(\omega\) converting a femtosecond-scale time delay into a micron-to-millimeter spatial offset:

\[
\Delta x = \frac{\omega R}{v} \times z_{\min} = \frac{\omega R}{v} \times \frac{vR}{c} = \frac{\omega R^2}{c}
\]

| | Direct \(z_{\min}\) measurement | \(\Delta x\) measurement (this method) |
|---|---|---|
| Physical quantity | Descent distance during photon flight | Horizontal projection of burn mark extension |
| Magnitude (R=10m) | 33 nm | 100–330 μm |
| **Amplification factor (ω)** | 1 | **3000–10000×** |
| Measurability | ❌ Requires nanometrology | ✅ Optical microscope |

Angular velocity \(\omega\) essentially plays the same role as the rotating mirror in Foucault's experiment — amplifying a tiny time difference into a macroscopic spatial offset. The difference: Foucault's rotating mirror changes the direction of reflected light; this method's rotating laser changes the slope of the burn mark — both use \(\omega\) as an amplifier.

---

## 8. Engineering Considerations

### 8.1 Large-Radius Cylinder Construction

A full-circumference cylinder of \(R = 10\) m is expensive to machine. Recommended: **arc-shaped panel assembly**.

- Divide 360° into 8–16 arc-shaped panels (22.5°–45° each)
- Mount panels on a precision frame, ensuring cylindricity
- Seal gaps between panels with light-proof tape to avoid disrupting burn mark continuity

### 8.2 Photosensitive Liner

Recommended: flexible polyimide (PI) film pre-coated with photosensitive material. Affix to cylinder inner wall before experiment, remove and flatten after. This avoids chemical processing on curved surfaces.

### 8.3 Descent Velocity Uniformity

Air-bearing guideways can maintain \(v\) fluctuations at the 0.1% level. For higher precision, use a drop tower (free fall, constant acceleration \(g\)). Note: under acceleration, the burn mark becomes a parabola rather than a straight line — the formula requires modification, but the principle of extracting \(\Delta x\) remains unchanged.

### 8.4 Vacuum

Air refractive index fluctuations \(\delta n \approx 3 \times 10^{-6}\) over an optical path of \(R = 10\) m introduce an additional optical path difference \(\delta z \approx 30\) μm — comparable to \(\Delta x\) itself. Recommended: operate at \(10^{-3}\) torr vacuum, reducing \(\delta n\) to the \(10^{-11}\) level, completely eliminating this error source.

---

## 9. Comparison with Historical Methods

| | Foucault (1862) | Michelson (1879) | **This method** |
|---|---|---|---|
| Optical path | Round-trip 40 m | Round-trip 700 m | **One-way** \(R\) |
| Rotating element | Small mirror | Octagonal mirror | Rotating laser |
| Recording | Spot displacement | Spot displacement | **Burn mark trajectory** |
| Signal amplification | Mirror amplification | Long path + mirror | **\(\omega\) amplification** |
| Clock sync | Not needed | Not needed | **Not needed** |
| Reference frame | Mirror + fixed mirror + screen | Mirror + fixed mirror + screen | **Single rigid body (cylinder)** |

The essential difference between this method and Foucault/Michelson lies not in the signal amplification technique, but in the **reference frame**: Foucault and Michelson's measurements are distributed across at least three spatial positions (rotating mirror, fixed mirror, screen), whereas this method's \(\Delta x\) readout occurs entirely on the same unwrapped cylinder surface — eliminating cross-reference-frame measurement controversy.

---

## 10. Discussion

### Does This Bypass the Einstein Synchronization Convention?

This method encodes the one-way photon flight time \(R/c\) as a spatial offset \(\Delta x\) on a single rigid body. The measurement of \(\Delta x\) involves no remote signal transmission and no remote clock synchronization. In this sense, the method does bypass the clock-synchronization circularity inherent in traditional one-way speed measurements.

However, the calibration of the descent velocity \(v\) still relies on a laboratory clock (high-speed camera timestamps, or the gravitational acceleration measurement for free-fall). A thoroughgoing critic could argue that the measurement of \(v\) implicitly assumes a simultaneity convention in the laboratory frame. But this objection is far weaker than the traditional circularity — \(v\) is a local quantity (same location, short distance), whereas the traditional circularity involves long-distance clock synchronization.

### What It Measures, and What It Does Not

The primary value of this method is not in yielding an absolute number \(c = 299792458\) m/s — limited by the \(z_{\min}\) measurement precision, the accuracy is far below existing round-trip measurements. Its value lies in:

1. **Providing the first direct constraint on the one-way speed of light that does not rely on remote clock synchronization**
2. **Testing whether the speed of light is isotropic** — if \(c(\theta)\) varies with direction within the plane, the burn mark will deviate from a perfect straight line
3. **Providing a platform for measuring c's response to physical conditions** — changing medium, temperature, electromagnetic field, gravitational gradient, and detecting changes in burn mark curvature

---

## 11. Conclusion

We have proposed a one-way speed-of-light measurement scheme based on a rotating laser and a moving recording surface. The core innovation is encoding the photon flight time as a spatial offset via motion, then amplifying that offset to a measurable scale using the laser's angular velocity.

On the unwrapped recording surface, the experiment reduces to an elementary geometric problem: the burn mark and the base edge form "two lines, one angle" — measure \(z_{\min}\) and \(\alpha\), and obtain \(c = \omega R^2 / (z_{\min} / \tan\alpha)\).

Recommended entry configuration: \(R = 5\)–\(10\) m, \(\omega = 300\)–\(1000\) rad/s, yielding \(\Delta x = 25\)–\(330\) μm, measurable with an optical microscope. The dominant error source — systematic bias in \(z_{\min}\) — can be eliminated via differential measurement at different descent velocities.

**This method does not rely on remote clock synchronization. All spatial quantities are obtained within a single rigid reference frame. The principle is self-consistent, and the engineering is feasible.**

---

*Created: 2026-07-31*