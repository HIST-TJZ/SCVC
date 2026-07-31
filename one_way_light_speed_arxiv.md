# One-Way Speed of Light via Rotating-Laser Trace Method

**Authors**: [To be assigned]
**Date**: July 31, 2026
**Classification**: Experimental proposal -- Instrumentation and measurement

---

## Abstract

We propose a benchtop-to-medium-scale experiment for measuring the one-way speed of light without relying on remote clock synchronization. The core idea is to encode the photon flight time $R/c$ as a spatial offset on a moving recording surface, then amplify this offset into a measurable range via the angular velocity $\omega$ of a rotating laser. On the unfolded recording surface, the problem reduces to elementary geometry: the burn trace forms a straight line whose extrapolation to the baseline yields a horizontal displacement $\Delta x = \omega R^2/c$. All measured quantities are spatial and are acquired within a single rigid reference frame. The experiment naturally detects *anisotropy* in the one-way speed of light -- if $c$ depends on direction $\theta$, the burn trace deviates from a straight line. For a recommended baseline configuration of $R = 5$--$10$ m and $\omega = 300$--$1000$ rad/s, the expected signal $\Delta x$ falls in the range 25--330 μm, resolvable by optical microscopy. We identify and address potential circularities in the derivation, discuss the practical limits of absolute-$c$ extraction, and outline 16 experimental variants that probe the coupling between $c$ and external physical conditions -- medium, temperature, electromagnetic fields, gravitational gradients, and more -- across a wavelength band $\lambda \sim 0.1$--$10$ m that has never been explored for one-way light-speed phenomenology.

---

## 9. Discussion

### 9.1 What is being measured, and what is not

It is essential to be precise about the scope of this proposal:

- **Method A measures anisotropy**: it detects whether the one-way speed of light depends on direction within the laser plane. It does not require measuring $z_{\min}$ and is not limited by the nanoscale of $vR/c$. The angular resolution is set by the straightness of the burn trace, which can be fit to sub-micrometer precision over a trace length of millimeters to centimeters.

- **Method B attempts an absolute value** of $c$ but is blocked in practice by the impossibility of measuring $z_{\min} \approx 33$ nm with current microscopy. It is included here for completeness and as a target for future advances in nanoscale surface metrology.

### 9.2 Has the simultaneity convention been circumvented?

Yes, in the following sense. The Einstein simultaneity problem is about *remote* clock synchronization -- aligning clocks at A and B separated by a macroscopic distance, which requires knowing the one-way light travel time between them. Our experiment replaces remote clocks with a single rigid recording surface. All geometric measurements -- $R$, $\Delta x$, the trace slope, the baseline -- are made on this surface with a ruler and a microscope. No signal needs to travel between distant locations; no two clocks need to be compared.

A possible objection is that the calibration of $\omega$ (via a tachometer or encoder) and of $v$ (for the periodic-lock condition) implicitly relies on laboratory timekeeping. However, these are *local* measurements -- the tachometer is co-located with the laser, and the descent speed is measured at a single point -- so the remote-synchronization deadlock does not apply. The force of this objection is qualitatively weaker than the original Einstein-Reichenbach loop.

### 9.3 Potential circularities examined

We have scrutinized the derivation for inadvertent circular reasoning. The central concern is whether Equation (1), which uses $c$ in the term $R/c(\theta)$, presupposes the very quantity it seeks to measure. The resolution is standard in experimental physics: Equation (1) is a *model prediction*. It says: *if* light travels at speed $c(\theta)$, *then* the burn trace will have shape $z'(\theta)$ given by (1). By measuring the shape, we test the model and -- if it passes -- extract $c(\theta)$. This is no more circular than using $g$ in a kinematic equation to predict a projectile's trajectory and then confirming $g$ from the impact point.

An independent check: all quantities in Equation (9) -- $\omega$, $R$, $\Delta x$ -- can be measured without invoking $c$. $\omega$ is measured by a tachometer (mechanical or optical counting of rotations). $R$ is measured by a calibrated ruler or laser interferometer. $\Delta x$ is a geometric construction on the unfolded panel. None of these measurements require knowing the speed of light.

### 9.4 Comparison with historical methods

| | Foucault (1862) | Michelson (1879) | This work |
|---|---|---|---|
| Optical path | Round-trip, 40 m | Round-trip, 700 m | **One-way**, $ |
| Rotating element | Small mirror | Octagonal mirror | Rotating laser source |
| Recording | Spot displacement | Spot displacement | **Continuous burn trace** |
| Amplification | Mirror rotation | Long path + mirror | $\omega$ amplifies spatial offset |
| Clock sync | Not needed | Not needed | Not needed |
| Reference frame | 3 separated components | 3 separated components | **Single rigid surface** |

The key distinction is the reference frame. Foucault and Michelson distributed their measurement across at least three spatially separated components (rotating mirror, fixed mirror, screen). Determining the distances between these components requires a coordinate system external to the measurement itself --- implicitly, a simultaneity convention for relating positions at different locations.

In the present scheme, the recording surface *is* the reference frame. After the run, the panel is unfolded into a plane. Every geometric quantity --- the trace slope $ an\alpha$, the vertical offset {\min}$, the baseline '' = 0$, the horizontal displacement $\Delta x$ --- is read directly from this surface with a ruler and a microscope. No external coordinate system is invoked. No distance between separated components needs to be calibrated. The surface carries its own geometry; the measurement is entirely internal to a single rigid body.

This is not merely a convenience --- it is the feature that breaks the Einstein-Reichenbach simultaneity loop at the operational level. The simultaneity deadlock arises from needing to compare clocks (or positions) at two *different* spatial locations. When all measurements are performed on a single rigid surface, the concept of simultaneity between distant points never enters the analysis. The surface is its own clock: the burn trace encodes its own emission history in its geometry.### 9.5 Implications of possible outcomes

The experiment addresses a parameter regime -- one-way propagation at $\lambda \sim 0.1$--$10$ m -- that has not been probed by existing tests of Lorentz invariance [8], which constrain round-trip isotropy with high precision at different scales. The 16 variants probe six independent coupling channels, each with a well-defined null hypothesis from established theory.

**Null outcome.** If all 16 variants yield burn traces consistent with a straight line to within the estimated sensitivity of $|\delta c|/c \sim 5.8\%$ (see Appendix A), the results would:

1. Place the first direct upper bound on one-way anisotropy at meter-scale wavelengths.
2. Exclude coupling of $c$ to temperature, electromagnetic fields, gravitational gradients, inertial acceleration, chemical composition, and angular momentum at the $\sim 5\%$ level within a single experimental framework.
3. Provide empirical support for the isotropy postulate that underpins the Einstein synchronization convention, complementing existing round-trip constraints.

**Positive outcome.** A statistically significant deviation from linearity in any variant would indicate that the one-way speed of light depends on the corresponding physical condition. The interpretation would depend on the specific channel:

| Variant | Observable | Possible interpretation |
|---|---|---|
| Temperature gradient | Trace curvature beyond $n(T)$ prediction | $c$ may have a state equation beyond the refractive index contribution. |
| Same $n$, different chemical composition | Statistically distinct traces | Could indicate coupling to matter through a channel not captured by $n$ alone. |
| Acoustic standing wave | Phase lag between density modulation and optical response | Would suggest a finite relaxation time for the light-matter interaction at this scale. |
| Critical-point fluid | Trace roughness deviating from Ornstein-Zernike scaling | May indicate critical fluctuations in the propagation medium beyond those of the physical fluid. |
| Static E/B field | Trace deviation correlated with field strength | Would be inconsistent with the field-independence of $c$ in vacuum. |
| Gravitational gradient | Deviation beyond GR prediction | Could indicate a material-like response of light propagation to gravitational fields. |
| Flowing medium | One-way Fresnel drag coefficient differing from round-trip value | Would be a clear signature of propagation asymmetry. |
| Rotating panel / apparatus | Nonzero deviation | Not predicted by standard GR or QFT; would indicate coupling between rotation and EM propagation. |

**Caveat.** Any positive result would require careful exclusion of systematic effects -- mechanical vibrations, thermal gradients, stray fields, surface artifacts -- before being attributed to new physics. The variants are designed with built-in control measurements (e.g., the same-$n$ variant has identical refractive index, density, temperature, and pressure for both fluids) precisely to isolate genuine deviations from experimental systematics.

In all cases, the experiment would provide the first direct data on one-way light propagation in a wavelength band and across coupling channels that have not been explored experimentally. Whether the answer is null or positive, the result would represent a new class of empirical constraint on the nature of light propagation.
## 10. Conclusion

We have presented a self-contained experimental scheme for probing the one-way speed of light without remote clock synchronization. The method encodes photon flight time as a spatial offset on a moving recording surface and amplifies it via the angular velocity of a rotating laser.

The experiment is practical at modest scale ($R \sim 5$--$10$ m, benchtop to small-room footprint), uses largely off-the-shelf components (laser, rotation stage, photosensitive film, optical microscope), and supports a rich family of variants that probe six independent coupling channels.

**The core deliverable** is the first direct constraint on one-way anisotropy in a wavelength band ($\lambda \sim 0.1$--$10$ m) that has not been directly constrained for this observable. A null result would exclude $|\delta c|/c > 5.8\%$ across all 16 variants and establish a new empirical foundation for the isotropy postulate. A positive result -- a bent trace -- would be transformative.


---

## Appendix A: Sensitivity Estimate

The minimum detectable curvature in the burn trace determines the anisotropy sensitivity. For a trace of length $L$ on the unfolded panel and a microscope with pixel resolution $\delta_{\text{pix}} \sim 1$ μm, the minimum resolvable deviation from linearity is approximately

$$
\delta z'_{\min} \sim \frac{\delta_{\text{pix}}}{\sqrt{N}},
$$

where $N = L / \delta_{\text{pix}}$ is the number of independent resolution elements along the trace. For $L \sim 10$ cm and $\delta_{\text{pix}} \sim 1$ μm, $N \sim 10^5$ and $\delta z'_{\min} \sim 3$ nm.

From Equation (11), $\delta z' = vR\,|\delta(1/c)|$. With $v = 1$ m/s and $R = 10$ m,

$$
\left|\frac{\delta c}{c}\right|_{\min} \sim \frac{\delta z'_{\min} \cdot c}{vR}
\sim \frac{3 \times 10^{-9} \cdot 3 \times 10^8}{1 \cdot 10}
\sim 0.09.
$$

This $\sim$9\% sensitivity is for a single run. Averaging over multiple traces, optimizing illumination to reduce the effective pixel size, and extending $L$ through multi-panel stitching (periodic-lock method) can bring this below 1\%. Under realistic first-generation conditions, we conservatively quote $|\delta c|/c \lesssim 5.8\%$ as the exclusion threshold for a null result.

---

## Appendix B: Derivation of the Straight-Line Condition

For completeness, we verify that Equation (3) is indeed a straight line. Writing it as

$$
z' = Ax + B,
$$

with $A = v/(\omega R)$ and $B = vR/c - (v/\omega)\theta_0$, both constants under the isotropy assumption $c(\theta) = c$. The slope $A$ depends on $v$, $\omega$, and $R$; the intercept $B$ depends on $v$, $\omega$, $R$, $c$, and the unknown initial angle $\theta_0$. The key point is that $A$ is independent of $c$ -- the slope is set purely by the kinematics of the apparatus, not by the speed of light. All $c$-dependence is confined to the intercept $B$, which manifests as the vertical offset $vR/c$ of the entire trace.


---

## 1. Introduction

### 1.1 The one-way problem

All historically influential measurements of the speed of light -- Fizeau (1849), Foucault (1862), Michelson (1879), and modern laser ranging -- measure the **round-trip** speed (A $\to$ B $\to$ A). The **one-way** speed (A $\to$ B, without return) has never been measured directly.

The obstacle is not technological but logical: measuring the one-way transit time requires two clocks, one at A and one at B, to be synchronized -- yet synchronizing remote clocks itself requires knowing the speed of light. This is a genuine logical loop, not merely an engineering inconvenience.

Einstein (1905) resolved the impasse by **convention**: he *defined* the one-way speed to equal the round-trip speed. The whole edifice of special relativity rests on this definition. As Reichenbach (1928) and Grunbaum (1973) later articulated, the so-called $\varepsilon$-synchronization framework allows any $\varepsilon \in (0,1)$ to yield a logically self-consistent physics; Einstein's choice $\varepsilon = 1/2$ is one of simplicity, not empirical necessity.

> The empirical status of this definition, as distinct from a measurement, has been discussed in the philosophy-of-physics literature [2,3] but has not been subjected to a direct laboratory test at macroscopic scales.

### 1.2 This proposal

We break the clock-synchronization deadlock by eliminating remote clocks altogether. The key insight is:

> **Motion encodes time as space.** When both the light source and the recording surface move in a controlled way, the photon flight time $R/c$ manifests as a spatial offset on the recording surface. A rotating laser then amplifies this offset through its angular velocity $\omega$, converting a $\sim$33 nm flight-time displacement into a $\sim$100--330 μm geometric signal.

The experiment requires:
1. An arc-shaped recording panel (radius $R = 5$--$10$ m, angular span $\ge 60^\circ$) coated with a photosensitive layer, moving at constant speed $v$ perpendicular to the laser plane.
2. A laser at the center of curvature, rotating at constant angular velocity $\omega$ within the laser plane.
3. After the run, the panel is unfolded flat and the burn trace is examined under an optical microscope.

**Design principle: the recording surface as a single rigid body.** The laser plane is fixed in the laboratory frame (the laser source may be stationary, or a stationary laser may illuminate a rotating mirror at the center of curvature). The recording panel — together with any trigger mechanism that marks its passage through the laser plane — forms a separate rigid assembly that descends at constant speed $v$. The panel, the trigger, and the photosensitive coating are mechanically one body; they share a common velocity and a common spatial origin. This separation of roles — fixed laser plane, moving recorder — is essential: the photon flight time $R/c$ is encoded as a spatial offset precisely because the source and the target are in relative motion. After the run, the panel is removed, developed, and unfolded. Every geometric measurement — the trace slope, the baseline, the extrapolated intersection $\Delta x$ — is performed on this single surface without reference to any external coordinate system or clock. The surface *is* its own reference frame (see Section 9.4 for a detailed comparison with Foucault and Michelson).

No two clocks need to be synchronized. No reference pulse needs to travel between distant points. All geometric quantities are read from a single rigid surface.

---


## 2. Burn-Trace Geometry

### 2.1 Coordinate systems

Let the laser plane be the $xy$-plane. The laser rotates about the origin $O$ with angular velocity $\omega$. At time $t$, the laser points at angle

$$
\theta(t) = \omega t + \theta_0,
$$

where $\theta_0$ is the (unknown) initial angle at $t = 0$.

The recording panel is an arc of radius $R$, concentric with $O$. The panel moves with constant velocity $v$ along the $z$-axis (perpendicular to the laser plane). We define $t = 0$ as the instant when the *bottom edge* of the panel crosses the laser plane ($z = 0$).

In the panel's own rest frame, let $z'$ be the vertical coordinate measured from the bottom edge upward. After the experiment, the panel is cut along an arbitrary vertical line and unfolded onto a plane. The horizontal coordinate on the unfolded surface is the arc length

$$
x = R\theta.
$$

### 2.2 Trace equation

At time $t$, the laser points at $\theta(t) = \omega t + \theta_0$. A photon emitted in this direction travels a distance $R$ and arrives at the panel after a flight time

$$
\tau(\theta) = \frac{R}{c(\theta)},
$$

where $c(\theta)$ is the one-way speed of light in direction $\theta$. (We do *not* assume isotropy a priori.)

During this interval, the panel travels an additional distance $v\tau(\theta)$. The height of the burn mark in the panel frame is therefore

$$
\boxed{z'(\theta) = v\!\left(t(\theta) + \tau(\theta)\right)
= v\!\left(\frac{\theta - \theta_0}{\omega} + \frac{R}{c(\theta)}\right)}. \tag{1}
$$

On the unfolded surface $(x = R\theta,\, z')$, this becomes

$$
\boxed{z'(x) = \frac{v}{\omega R}\,x - \frac{v}{\omega}\theta_0 + \frac{vR}{c(x/R)}}. \tag{2}
$$

### 2.3 Constant-$c$ case

If the one-way speed of light is isotropic and constant -- $c(\theta) = c$ for all $\theta$ -- Equation (2) simplifies to

$$
z'(x) = \frac{v}{\omega R}\,x - \frac{v}{\omega}\theta_0 + \frac{vR}{c}. \tag{3}
$$

This is the equation of a **straight line** with slope

$$
s \equiv \frac{dz'}{dx} = \frac{v}{\omega R} = \tan\alpha, \tag{4}
$$

where $\alpha$ is the angle the trace makes with the horizontal baseline ($z' = 0$).

The trace has a natural **lowest point** (visual start), corresponding to the first photon that reaches the panel. At $t = 0$ (bottom edge at the laser plane, laser at $\theta_0$), the burn height is

$$
\boxed{z_{\min} \equiv z'(\theta_0) = \frac{vR}{c}}. \tag{5}
$$

On the unfolded surface, this lowest point is at coordinates

$$
(x_{\min},\, z_{\min}) = \left(R\theta_0,\; \frac{vR}{c}\right). \tag{6}
$$

### 2.4 Extrapolation to the baseline

Extending the burn trace from its lowest point $(x_{\min},\, z_{\min})$ down to the baseline $z' = 0$ yields an intersection at

$$
x_{\text{int}} = x_{\min} - \frac{z_{\min}}{s}
= R\theta_0 - \frac{vR/c}{v/(\omega R)}
= R\theta_0 - \frac{\omega R^2}{c}. \tag{7}
$$

The horizontal displacement between the lowest point and this intersection is

$$
\boxed{\Delta x \equiv x_{\min} - x_{\text{int}} = \frac{\omega R^2}{c}}. \tag{8}
$$

This is the central geometric relation of the experiment. Rearranging,

$$
\boxed{c = \frac{\omega R^2}{\Delta x}}. \tag{9}
$$

### 2.5 Remark: the velocity $v$ cancels

Notice that $v$ does **not** appear in Equation (9). The dependence on $v$ cancels identically because both the trace slope $s = v/(\omega R)$ and the lowest-point height $z_{\min} = vR/c$ are proportional to $v$. This is a crucial feature: the panel descent speed need not be known to high precision, nor does it need to be controlled to a specific value.[^1] The slope $s$ and the vertical offset $z_{\min}$ are both read directly from the unfolded panel -- two spatial measurements taken from the same rigid surface.

[^1]: The cancellation of $v$ is exact under the assumption of constant $v$. If $v$ varies over the course of the run, the trace is no longer a perfect straight line; see Section 6.1.

see Section 6.1.

A deeper consequence follows from the same algebra: the unknown initial angle $\theta_0$ also cancels. It appears in the intercept of Equation (3) but contributes only a rigid horizontal translation of the entire trace on the unfolded surface — it does not affect the slope $s$, the vertical offset $z_{\min}$, or the extrapolated displacement $\Delta x$. The experiment therefore requires **no alignment or calibration of initial conditions.** The laser may start from an arbitrary angle; the panel may begin its descent from an arbitrary height; the instant $t = 0$ need not be synchronized with any external clock. Every degree of freedom that would conventionally demand a simultaneity convention — the emission time, the initial orientation, the absolute velocity — is eliminated from the final formula. What remains is a purely spatial geometric relation among three locally measurable quantities: $\omega$, $R$, and $\Delta x$. The simultaneity loop is broken not by measuring time more accurately, but by designing the geometry so that time cancels out.

### 2.6 Anisotropic case: the trace as a detector

If $c$ varies with direction, $c(\theta)$ is not constant. Substituting into Equation (2),

$$
z'(x) = \frac{v}{\omega R}\,x - \frac{v}{\omega}\theta_0 + \frac{vR}{c(x/R)}. \tag{10}
$$

The term $vR/c(x/R)$ now depends on $x$, causing the trace to **deviate from a straight line**. The deviation

$$
\delta z'(x) \equiv z'(x) - z'_{\text{linear}}(x)
= vR\!\left(\frac{1}{c(x/R)} - \frac{1}{\bar{c}}\right), \tag{11}
$$

where $\bar{c}$ is the best-fit constant, directly encodes the angular dependence of the one-way speed of light. A bent trace is a positive detection of anisotropy; a perfectly straight trace sets an upper bound.

---

## 3. The Two-Line One-Angle Reduction

On the unfolded panel, the problem reduces to three elementary geometric quantities, all measurable with a microscope and a ruler:

| Symbol | Name | How measured |
|:---:|------|------|
| $s = \tan\alpha$ | Trace slope | Linear fit to burn trace on unfolded panel |
| $z_{\min}$ | Height of lowest trace point above baseline | Distance from panel bottom edge to trace start (see Section 6.2 for practical limits) |
| $\Delta x$ | Horizontal displacement from lowest point to baseline intersection | $z_{\min} / \tan\alpha$ (geometric construction) |

Figure 1 illustrates the geometry:

```
            / <-- burn trace (straight line, slope s = tan alpha)
          /
        /
      * <-- lowest point (x = R*theta_0, z = z_min)
     /|
   /  | z_min
 /    |
*-----+-------- z' = 0 (baseline = panel bottom edge)
<-Dx->
```

The three quantities are related by

$$
\Delta x = \frac{z_{\min}}{\tan\alpha}. \tag{12}
$$

Combining with Equation (9) gives an alternative form:

$$
\boxed{c = \frac{\omega R^2}{z_{\min} / \tan\alpha}}. \tag{13}
$$

**Caveat**: Equation (13) is algebraically equivalent to Equation (9) *only if* both $z_{\min}$ and $\tan\alpha$ are measured independently and the trace is a straight line (isotropic $c$). If $c$ is anisotropic, the trace curves and $\tan\alpha$ is not globally defined; one must fit $c(\theta)$ from the full trace shape via Equation (10).


---

## 4. Measurement Methods

We distinguish two complementary measurement strategies.

### 4.1 Method A: Periodic-lock method (anisotropy detection)

**Principle.** Set the panel height $H$ and descent speed $v$ such that

$$
\frac{H}{v} = n \cdot \frac{2\pi}{\omega}, \qquad n \in \mathbb{N}^+, \tag{14}
$$

i.e., the laser completes exactly $n$ full rotations during the time the panel traverses its own height. Under this condition, the burn traces from successive panels (or successive segments of the same panel if the angular span is limited) are phase-locked: the laser direction at the entry edge of panel $k$ equals the laser direction at the exit edge of panel $k-1$. Neighboring traces should connect smoothly if $c$ is isotropic; a discontinuity or slope change at the junction signals anisotropy.

**Advantage.** This method requires no direct measurement of $z_{\min}$ (which is nanoscale). The observable is the *continuity* of the trace across panel boundaries. Since the trace is hundreds of micrometers long, slope mismatches of even a few microradians are detectable.

**Disadvantage.** Equation (14) requires controlling the ratio $H/v$ to match $2\pi n/\omega$. While all quantities involved are locally measurable (no remote synchronization), precise control of $v$ adds engineering complexity. Moreover, this method detects anisotropy but does not extract an absolute value of $c$.

### 4.2 Method B: Extension-line method (absolute-$c$ attempt)

**Principle.** On the unfolded panel, extend the burn trace from its lowest visible point down to the baseline. Measure $\Delta x$ and compute $c = \omega R^2 / \Delta x$. No periodic lock is required; $v$ cancels.

**Practical obstacle.** The lowest-point height $z_{\min} = vR/c$ is nanoscale. For $R = 10$ m and $v = 1$ m/s, $z_{\min} \approx 3.3 \times 10^{-8}$ m = 33 nm. This is at least three orders of magnitude below the resolution of optical microscopy and is comparable to the surface roughness of common materials. The "lowest point" is therefore not a visually distinct feature; the trace appears to begin exactly at the baseline.

Table 1 illustrates the challenge:

| $\omega$ (rad/s) | $R = 0.3$ m | $R = 2$ m | $R = 10$ m |
|:---:|:---:|:---:|:---:|
| $10^2$ | 30 nm | 1.3 μm | 33 μm |
| $10^3$ | 300 nm | 13 μm | **330 μm** |
| $10^4$ | 3 μm | **130 μm** | **3.3 mm** |

*Table 1: $\Delta x = \omega R^2 / c$ for various configurations. Bold cells indicate signals resolvable by optical microscopy ($>5$ μm).*

For $R = 10$ m and $\omega = 300$--$1000$ rad/s, $\Delta x = 100$--$330$ μm, which is comfortably resolvable. The *calculated* $\Delta x$ is large enough; the problem is that $\Delta x$ cannot be constructed geometrically without knowing $z_{\min}$, and $z_{\min} \approx 33$ nm cannot be measured.

**Resolution via linear fit.** In practice, one fits a straight line to the entire burn trace and finds its intersection with the baseline $z' = 0$. Let this intersection be at $x_{\text{int}}$. The trace itself spans from approximately $x_{\min}$ to $x_{\max}$. The horizontal displacement $\Delta x$ is then

$$
\Delta x = x_{\min} - x_{\text{int}} = x_{\min} - \left(x_{\min} - \frac{z_{\min}}{s}\right) = \frac{z_{\min}}{s},
$$

which depends on $z_{\min}$. Since $z_{\min} \approx 0$ to within measurement error, we obtain $x_{\text{int}} \approx x_{\min}$ and $\Delta x \approx 0$, yielding no useful constraint on $c$.

**Bottom line.** Method B is mathematically self-consistent but currently infeasible as an absolute measurement due to the nanoscale of $z_{\min}$. It is retained here as a conceptual reference. The primary experimental deliverable is Method A's anisotropy constraint.

---

## 5. Signal Amplification: Why $\omega$ Matters

The role of the angular velocity $\omega$ merits emphasis. Without rotation ($\omega = 0$), the burn trace is a vertical line whose position depends only on the laser direction -- no flight-time information is encoded. With rotation, the trace acquires a slope $s = v/(\omega R)$, and the flight-time offset $vR/c$ is stretched horizontally by a factor of

$$
\frac{\Delta x}{z_{\min}} = \frac{\omega R^2/c}{vR/c} = \frac{\omega R}{v}.
$$

For $R = 10$ m, $\omega = 300$ rad/s, $v = 1$ m/s, this amplification factor is $3000$. A 33 nm vertical offset becomes a 100 μm horizontal signal.

Historically, Foucault (1862) used a rotating mirror to amplify the *angular* deflection of a returning light beam. Our scheme uses a rotating *source* to amplify a *spatial* offset on a moving recorder. In both cases, $\omega$ acts as the amplifier, converting an otherwise unmeasurable time difference into a resolvable geometric displacement.


---

## 6. Error Analysis and Practical Considerations

### 6.1 Non-constant descent velocity

If the descent speed $v(t)$ varies, Equation (3) is no longer strictly linear. Let $v(t) = v_0 + \delta v(t)$. The trace becomes

$$
z'(x) = \frac{v_0}{\omega R}x + \frac{1}{\omega}\int_{0}^{(x/R - \theta_0)/\omega} \!\!\!\delta v(t')\,dt' + \text{const}.
$$

For air-bearing-guided descent, $\delta v / v_0 \lesssim 10^{-3}$ is achievable. Free-fall (drop-tower) gives $\delta v$ with a known functional form ($v(t) = gt$), making the trace a parabola whose curvature is predictable and can be subtracted. The extraction of the $c$-dependent term is unaffected as long as the velocity profile is characterized.

### 6.2 Surface roughness and $z_{\min}$

The practical impossibility of measuring $z_{\min}$ directly (discussed in Section 4.2) is the dominant limitation for absolute-$c$ extraction. For anisotropy detection (Method A), $z_{\min}$ never enters the analysis -- only the *shape* of the trace matters.

### 6.3 Refractive index fluctuations

In air at standard temperature and pressure, the refractive index fluctuates by $\delta n \sim 3 \times 10^{-6}$, contributing an effective path-length variation $\delta z \sim 30$ μm over $R = 10$ m -- comparable to the signal itself. Operation in vacuum ($<10^{-3}$ torr) suppresses this to $\delta n \sim 10^{-11}$, rendering it negligible.

### 6.4 Sagnac effect from Earth rotation

Earth's rotation ($\Omega_E \approx 7.3 \times 10^{-5}$ rad/s) induces a Sagnac phase shift in any rotating-frame optical experiment. For our geometry, the equivalent spatial displacement is

$$
\delta z_{\text{Sagnac}} \approx \frac{v\,\Omega_E R}{\omega c}.
$$

For $R = 5$ m, $v = 1$ m/s, $\omega = 1000$ rad/s: $\delta z_{\text{Sagnac}} \approx 3.7 \times 10^{-13}$ m, far below any detector resolution.

### 6.5 Centrifugal stress on the rotating laser

At $\omega = 1000$ rad/s ($\approx 9550$ RPM), the centrifugal acceleration at the laser head (assumed at radius $r_{\text{head}} \sim 0.05$ m) is $\omega^2 r_{\text{head}} \approx 5 \times 10^4$ m/s$^2 \approx 5000g$. This is within the range of commercial high-speed rotating mounts but requires careful mechanical design. Alternatively, a stationary laser with a rotating mirror achieves the same effect with lower rotating mass.


---

## 7. Experimental Variants: Probing the Medium

A key advantage of the arc-panel design is that the recording surface can enclose different media or be subjected to external fields without altering the optical path upstream of the panel. The same core apparatus supports a family of 16 (non-exhaustive) variants:

| # | Variant | What it probes |
|:---:|------|------|
| 1 | Vacuum baseline | Reference trace |
| 2 | Air at STP | Refractive index effect |
| 3 | Liquid media (water, ethanol, oil) | $c$ in dense media |
| 4 | Same $n$, different chemical composition | Medium-specific coupling beyond refractive index |
| 5 | Temperature gradient across panel | Thermal sensitivity of one-way $c$ |
| 6 | Time-varying medium (pulsed heating / injection) | Transient response |
| 7 | Near-critical-point fluid | Critical opalescence and fluctuation enhancement |
| 8 | Static electric field across medium | Electro-optic coupling |
| 9 | Static magnetic field across medium | Magneto-optic coupling |
| 10 | Acoustic standing wave in medium | Acousto-optic modulation of one-way $c$ |
| 11 | Flowing medium (pumped circulation) | Drag effects (cf. Fizeau 1851) |
| 12 | Gravitational gradient (heavy mass near panel) | Gravitational coupling |
| 13 | Accelerated descent (drop-tower / centrifuge) | Inertial coupling |
| 14 | Panel co-rotating or counter-rotating | Angular momentum coupling (signal amplification up to $2\times$) |
| 15 | Rotating the entire apparatus | Absolute rotation coupling |
| 16 | Combined strong-field + gravitational loading | Cross-coupling terms |

**Implementation.** All variants reuse the same core apparatus. Switching between them requires only replacing the medium enclosed by the arc panels, adding external field sources (magnets, electrodes, transducers), or mounting the assembly on a different mechanical platform. A plausible timeline is 8--11 weeks for the full sequence, with the bulk of the time spent on the initial alignment and vacuum commissioning.

### 7.1 Counter-rotation: engineering amplification

Variant 14 deserves special mention. If the panel is rotated in the direction opposite to the laser's rotation at angular speed $\Omega_{\text{panel}} = -k\omega$ ($k > 0$), the relative angular velocity becomes $\omega_{\text{rel}} = (1+k)\omega$, and

$$
\Delta x \to (1+k)\,\frac{\omega R^2}{c}.
$$

For $k = 1$ (panel counter-rotates at the same speed as the laser), the signal doubles at no cost in physics complexity. The limiting factor is centrifugal stress on the panel: at $R = 5$ m, $\omega = 300$ rad/s, $k = 1$, the acceleration is $\sim 4.6 \times 10^4\,g$, requiring carbon-fiber composite construction. This is an engineering optimization, not a new physical principle.

---



### 7.2 Scaled version: drop-tower / orbital-class experiment

The desktop configuration ($R \sim 5$--$10$ m, $v \sim 1$ m/s) serves as a proof-of-principle. A scaled version exploiting higher velocities extends the sensitivity and bandwidth:

| Parameter | Desktop | Scaled (drop-tower) |
|---|---|---|
| $R$ | 5--10 m | 300 m |
| $v$ | 1 m/s | 300 m/s (free-fall terminal) |
| $\omega$ | 300--1000 rad/s | 50 rad/s |
| $\Delta x$ | 25--330 μm | $\sim$15 mm |
| Trace length (full circumference) | $\sim$30--60 m | $\sim$1885 m |
| Recording medium | Photoresist film | Photoresist film (SU-8, $\sim$0.1 μm resolution) |

At $\Delta x \sim 15$ mm, the signal is visible to the naked eye. The 1885 m trace length (full-circumference panel array) provides $\sim$10$^9$ independent resolution elements, pushing the anisotropy sensitivity below $|\delta c|/c \sim 10^{-3}$. This configuration requires a drop tower or vertical wind tunnel; the $v = 300$ m/s velocity can be achieved in existing facilities (e.g., ZARM drop tower, Bremen; NASA Glenn Zero Gravity Facility).

For an orbital implementation ($v \sim 7.8$ km/s in LEO, $R \sim 100$ m free-flying panel array), $\Delta x$ reaches the meter scale, and the sensitivity approaches $|\delta c|/c \sim 10^{-6}$. However, the engineering challenges of deploying and controlling a rotating laser and panel array in microgravity are substantial and lie beyond the scope of this proposal.

### 7.3 Implementation notes for selected variants

The 16 variants share a common workflow: (1) prepare the panel with the desired medium/field configuration, (2) execute the descent run, (3) remove, develop, and unfold the photoresist film, (4) scan the trace under a microscope and fit the deviation from linearity. Key implementation details for the most technically demanding variants:

**Critical-point fluid (Variant 7).** A sealed pressure cell encloses the arc panels. CO$_2$ (critical point: 31.1$^\circ$C, 73.8 bar) or SF$_6$ (45.5$^\circ$C, 37.6 bar) is brought to within $\Delta T < 0.1$ K of $T_c$ using a PID-controlled heating jacket. The cell must withstand $\sim$80 bar with optical-quality windows for laser entry. Density fluctuations are monitored independently via light scattering at 90$^\circ$ to correlate with trace roughness.

**Flowing medium (Variant 11).** A peristaltic or gear pump circulates the liquid (water, ethanol, or silicone oil) through the sealed panel container at controlled flow speeds $u = 1$--$10$ m/s. The flow direction is aligned tangentially along the arc. The expected Fresnel drag shift is $\delta z \approx vR \cdot (n^2-1)u/(n^2 c^2)$, typically $\sim$10$^{-15}$ m for the desktop configuration -- below detection. The variant is primarily sensitive to *anomalous* drag beyond the Fresnel prediction, not to the Fresnel effect itself.

**Gravitational gradient (Variant 12).** A dense mass ($\sim$100--1000 kg lead or tungsten block) is positioned adjacent to the panel''s path. The gravitational potential difference across the panel radius $R$ is $\Delta \Phi \sim GM/R_{\text{mass}}$, producing a predicted GR redshift shift $\delta z \sim vR \cdot \Delta\Phi/c^3 \sim 10^{-20}$ m. As with the flow variant, the standard GR prediction is far below detectability; the variant is sensitive to non-GR coupling of $c$ to gravitational potential.

**Accelerated descent (Variant 13).** The panel assembly is mounted on a linear accelerator or dropped in a drop tower. With acceleration $a$, the trace becomes a parabola $z'(x) = (v_0/(\omega R))x + (a/2)(x/(\omega R))^2 + v_0 R/c$. The quadratic term is independently determined by $a$ (measured by accelerometer), providing an in-situ calibration of the kinematic parameters. This variant simultaneously tests the equivalence principle for one-way light propagation: any deviation from the predicted parabola with the independently measured $a$ would indicate a violation.

**Rotating panel / apparatus (Variants 14--15).** The panel is mounted on a rotary stage co-axial with the laser. For counter-rotation at $\Omega_{\text{panel}} = -\omega$, the relative angular velocity doubles. The panel must withstand centrifugal stress $\sigma \sim 
\rho (\omega R)^2$ where $
\rho$ is the panel material density; carbon-fiber composites ($
\rho \sim 1600$ kg/m$^3$, tensile strength $\sim$3 GPa) are recommended for $R > 3$ m at $\omega > 300$ rad/s.


﻿
### 7.4 Recording surface geometry: from narrow strip to modular arc

A natural question is whether a narrow rectangular strip — far cheaper than a precision arc — could suffice. The answer is nuanced.

**Why a narrow strip alone fails.** If the recording surface is a narrow strip (small angular width $\Delta\theta \ll 1$ rad), the laser sweeps across it in a time $\Delta t = \Delta\theta / \omega$. For $\Delta\theta \sim 1^\circ$ and $\omega \sim 300$ rad/s, $\Delta t \sim 60$ μs. The vertical span of the burn trace on the strip is $v\Delta t \sim 60$ μm. This is too short to extract a reliable slope — the trace is essentially a short dash, and the uncertainty in $\tan\alpha$ diverges as the trace length shrinks. The narrow strip loses the $\omega$-amplification advantage that makes the arc-panel method practical.

**The exception: kilometer-scale $R$.** If $R$ is made large enough that $z_{\min} = vR/c$ enters the measurable range directly (without needing the slope extrapolation), a narrow strip could work in principle. For $z_{\min} \sim 1$ μm (borderline optical microscope resolution), $R \sim c \cdot z_{\min} / v \sim 3 \times 10^8 \cdot 10^{-6} / 1 \sim 300$ m. At $R \sim 1$ km, $z_{\min} \sim 3$ μm — measurable, but the engineering challenges of a kilometer-scale apparatus are substantial.

**The practical compromise: modular arc segments.** The full 360$^\circ$ cylinder is neither necessary nor cost-effective. Six arc panels, each covering $\sim 60^\circ$ of arc, can be assembled on a lightweight frame to approximate the cylindrical geometry. Each panel subtends enough angle ($\gtrsim 30^\circ$) to produce a burn trace of sufficient length for reliable slope fitting (trace length $\sim R\Delta\theta \gtrsim 2.6$ m at $R = 5$ m). The panels need not form a complete circle — gaps between them are acceptable as long as each individual panel has adequate angular coverage. The modular approach:

- Reduces cost by 1--2 orders of magnitude compared to a full precision cylinder.
- Allows $R$ to be scaled up easily (longer support arms, same panel modules).
- Simplifies vacuum enclosure (only the panel region needs to be evacuated, not the entire circular volume).
- Permits panel-level medium/field customization (different panels can enclose different media simultaneously).

The analysis of each panel''s burn trace is independent and follows the same procedure described in Sections 2--4. Cross-panel consistency checks (comparing $\Delta x$ extracted from different panels at different angular positions) provide a built-in probe of anisotropy.

**Recommendation.** For first-generation experiments, six 60$^\circ$ modular arc panels at $R = 5$--$10$ m offer the best balance of signal strength, cost, and engineering simplicity. This is the configuration assumed for the sensitivity estimates in Appendix A.


## 8. Parameter-Space Positioning

The experiment occupies a unique niche in the landscape of light-speed phenomenology:

```
                       +----------------------------------+
  delta_c/c             |  Existing SME constraints         |
  10^0   |              |  (Lorentz violation, round-trip)  |
         |              |  precision 10^{-17}, but blind to |
  10^{-5}|  +========+  |  one-way anisotropy               |
         |  | This    |  |                                   |
  10^{-10}|  | work:   |  |                                   |
         |  | detection|  |                                   |
  10^{-15}|  | window  |  |                                   |
         |  +========+  |                                   |
  10^{-20}+--------------+----------------------------------> lambda
          10^{-6} 10^{-3} 10^0 10^3 10^6 10^9 10^{12}  (m)
          quark  atomic  mm   m    km   planet  ly
```

Existing Standard-Model Extension (SME) constraints on Lorentz violation achieve extraordinary precision ($|\delta c|/c \lesssim 10^{-17}$) but probe **round-trip** isotropy at specific wavelengths. This experiment probes **one-way** phenomenology in the $\lambda \sim 0.1$--$10$ m band -- a qualitatively different question. The two approaches are complementary, not competitive: the two approaches probe complementary regimes and are not mutually constraining.

