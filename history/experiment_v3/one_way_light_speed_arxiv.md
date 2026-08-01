# Measuring the One-Way Speed of Light with a Rotating Laser: Disc Method and Conical-Ring Method

**Date**: August 1, 2026
**Classification**: Experimental proposal -- Instrumentation and measurement

---

## Abstract

This paper proposes two experimental schemes for measuring the one-way speed of light with a rotating laser: the planar-disc method and the conical-ring method. The common idea is to encode the one-way photon flight time $R/c$ as a geometric angle on a recording surface by means of a uniformly rotating laser, thereby bypassing, at the operational level, the logical loop that measuring a one-way transit time requires synchronizing two spatially separated clocks. The disc method gives

$$
\Delta X = \frac{\omega R}{c}, \qquad c = \frac{\omega R}{\Delta X},
$$

where $\Delta X$ is the angle between the kink radius and the stop-direction radius on the disc; the conical-ring method gives, under the two postulates that the laser rotation is uniform and the ring descent is uniform,

$$
c = \frac{d}{(\theta_{\mathrm{stop}}-\varphi)/\omega - \Delta z/v}.
$$

Under the ideal rigid-body postulate, both schemes use only a single rigid recording surface and a locally calibrated angular velocity $\omega$; at the operational level they require no remote clock synchronization and no stopwatch. Finite material rigidity and trigger/stopping time differences enter the readout directly; their effects are discussed in Section 2.5.3 and Appendix A.1.

The paper presents the apparatus design, geometric derivation, experimental procedure, order-of-magnitude estimates, and error budget, and discusses the relation between the rigid-body simultaneity postulate and the $\varepsilon$-synchronization convention. It also lists the conclusions for five structural variants and a family of 16 controlled variants designed to probe the dependence of the one-way speed of light on medium, temperature, electromagnetic fields, gravitational gradients, rotation, and other external conditions.

It should be emphasized that the numerical values above are one-way light speeds in the time coordinates defined by the postulates. Special relativity (SR) does not predict a specific numerical value for the one-way speed of light, so the schemes do not constitute a test or a refutation of SR. The convention-independent observational signal is the raw geometric readout: if the straightness of the etch trace, $\Delta X$, or the ring azimuth changes with apparatus orientation or controlled conditions, that is a candidate for physics beyond SR.

**Keywords**: one-way speed of light; light-speed convention; $\varepsilon$-synchronization; anisotropy; rotating laser; experimental design

---

## 1. Introduction

### 1.1 The one-way speed problem

All historically influential measurements of the speed of light -- Fizeau (1849) [4], Foucault (1862) [5], Michelson (1879) [6], and modern laser ranging -- measure the round-trip speed ($A \to B \to A$). The one-way speed ($A \to B$, without return) has never been measured directly.

The obstacle is not technological but logical: measuring a one-way transit time requires placing and synchronizing clocks at $A$ and $B$, and synchronizing remote clocks itself requires knowing the speed of light. This is a genuine logical loop.

Einstein (1905) [1] resolved the impasse by convention: the one-way speed of light was defined to equal the round-trip speed. Reichenbach (1928) [2] and Grünbaum (1973) [3] further argued that the $\varepsilon$-synchronization framework permits any $\varepsilon \in (0,1)$ to yield a logically self-consistent physics; the choice $\varepsilon = 1/2$ is one of simplicity, not empirical necessity. Therefore, under a given synchronization convention, the experiment yields a definite numerical value of the one-way speed in that convention; whether it equals the round-trip value is determined jointly by the convention and by physics. The point of the experiment is to separate postulates from observations.

Round-trip measurements also have a structural blind spot. The round-trip time

$$
t_{\mathrm{round}} = \frac{L}{c(\theta)} + \frac{L}{c(\theta+\pi)} \tag{1}
$$

cancels the direction-antisymmetric terms of $c(\theta)$ and $c(\theta+\pi)$; Michelson-Morley-type experiments are therefore sensitive only at order $O(v^2/c^2)$, whereas one-way experiments retain the first-order direction asymmetry $O(v/c)$. In the present schemes the laser beam is absorbed upon reaching the recording surface and there is no return path, so they probe the direction asymmetry that round-trip experiments cannot detect in principle. The cost is the absence of round-trip common-mode cancellation: systematic errors from temperature, density, vibration, and similar effects are harder to suppress and must be isolated variant by variant with control groups (Section 4 and Appendix A.2).

### 1.2 Structure and postulates

Section 2 presents the apparatus, derivation, procedure, magnitudes, and errors of the disc method; Section 3 presents the conical-ring method; Section 4 gives the structural variants and the list of 16 controlled variants; Section 5 gives the conclusions; Appendix A gives formal arguments on rigid-body simultaneity, criteria for beyond-prediction signals, and the classification of one-way versus round-trip paths; Appendix B gives the sensitivity estimate.

Two postulates are adopted throughout:

1. The laser rotation is uniform, i.e., the angular velocity $\omega$ is constant, and $\omega$ is calibrated at the laser site;
2. The motion of the recording surface (disc or ring) is uniform, i.e., $v$ is constant.

In the time coordinates defined by these postulates, both experiments yield a definite one-way light-speed value. That value is a result in the chosen coordinates and is not to be compared with an SR prediction: SR does not predict a specific numerical value of the one-way speed. The freezing of the disc and the stopping of the laser are defined by the same rigid-body contact event, so no second clock is introduced.

---

## 2. Disc method

### 2.1 Design idea

Think of the rotating laser as a continuously rotating sprinkler: the water takes $R/c$ to reach the disc; after the disc presses down on the sprinkler, the water already emitted continues to fall, completing the final part of the trace up to the stop direction. Translated to photons:

- The photon that arrives at the disc exactly at the stopping instant was emitted when the laser pointed at $\theta_{\mathrm{stop}} - \omega R/c$;
- The last in-flight photon is emitted along the stop direction $\theta_{\mathrm{stop}}$;
- The central angle between the two impact points on the disc is $\omega R/c$.

This angular difference is the encoding of the speed of light. Photons emitted earlier form the rest of the trace and are irrelevant to the measurement.

### 2.2 Apparatus and key parameters

The core components are listed in Table 1.

**Table 1: Core components**

| Component | Function | Notes |
|---|---|---|
| Rotating laser | Rotates at constant angular velocity $\omega$ and emits continuously | With angle encoder; either a rotating laser head or a fixed laser plus rotating mirror |
| Planar disc | Records the laser etch trace | Concentric with the rotation axis; surface has a photosensitive/etchable coating |
| Central trigger | Integral with the disc | Defines the single event "disc freezes + laser stops" when the disc presses the laser |
| Descent mechanism | Makes the disc fall vertically | The descent speed $v$ need not be measured precisely |
| Angle readout | Reads angles on the disc | Precision turntable, goniometer, microscope |

The key geometric parameters are:

- $R$: distance from the laser rotation center to the disc recording region, i.e., the beam flight distance;
- $\omega$: angular velocity of the laser, calibrated locally;
- $v$: descent speed of the disc; it cancels in the derivation and need not be measured;
- $\theta_0$: initial pointing direction of the laser at the start of the experiment; it cancels in the derivation and need not be aligned.

Two design facts require comment. First, the recording surface is a planar disc rather than a cylinder: the disc, the central trigger, and the etch layer form a single rigid body, and the single mechanical contact "the disc presses the laser" simultaneously defines "the disc freezes" and "the laser stops"; no two clocks and no clock-like synchronization are needed. This simultaneity definition is part of the ideal rigid-body postulate; with real materials, finite rigidity makes time differences enter $\Delta X$ directly (Section 2.5.3). Second, a real laser is not a zero-thickness geometric ray. To obtain a clear etch trace, the beam should strike the disc surface at a near-grazing but nonzero angle. This design choice affects only the line width of the etch and the localization of the kink; it does not change the definition of $R$ as the geometric flight distance. The structure of the trace and the definition of $\Delta X$ are given in Section 2.3.

### 2.3 Geometric derivation

#### 2.3.1 Time parameterization

Let $t=0$ be the instant at which the disc begins to be illuminated. The pointing angle of the laser is

$$
\theta(t) = \omega t + \theta_0, \tag{2}
$$

where $\theta_0$ is the (unknown) pointing angle at $t=0$. The photon travels the distance $R$ from the laser to the recording region, so its flight time is

$$
\tau = \frac{R}{c}. \tag{3}
$$

In the disc's own polar coordinates, the azimuth $\varphi$ of a mark corresponds one-to-one to the emission azimuth of the laser; the descending motion of the disc encodes the arrival time as the radial position of the mark.

#### 2.3.2 Temporal structure of the trace

The full etch trace has three parts:

1. Moving segment (before stopping): the disc is still descending and photons keep arriving; each mark lands at a different radial position, so the trace is a slanted line or spiral. This segment spans the total exposure time $T$, with an azimuthal span of about $\omega T$, and contains no information about the speed of light;
2. Stopping event ($t=T$): the disc presses the laser; the disc freezes and the laser stops;
3. Frozen segment ($T < t < T + R/c$): photons already emitted but still in flight continue to arrive. The disc is no longer moving, so these marks lie at the same radial position and form a circular arc extending from the kink $K$ to the stop-direction radius.

#### 2.3.3 The frozen segment and $\Delta X$

At the stopping instant ($t=T$) the laser points at

$$
\theta_{\mathrm{stop}} = \theta(T) = \theta_0 + \omega T. \tag{4}
$$

The photon that arrives at the disc exactly at $t=T$ was emitted at $t = T - R/c$, with emission angle

$$
\theta(T - R/c) = \theta_{\mathrm{stop}} - \omega\,\frac{R}{c}. \tag{5}
$$

This mark is the kink $K$ between the moving and frozen segments. The last in-flight photon is emitted along the stop direction and arrives on the stop-direction radius; this is the etch endpoint $P_2$. Joining $K$ and $P_2$ to the center, the angle between the two radii is

$$
\Delta X = \theta_{\mathrm{stop}} - \left(\theta_{\mathrm{stop}} - \omega\frac{R}{c}\right) = \frac{\omega R}{c}, \tag{6}
$$

from which

$$
c = \frac{\omega R}{\Delta X}. \tag{7}
$$

If the arc length $\Delta x$ along the recorded arc is measured instead,

$$
\Delta x = R\,\Delta X = \frac{\omega R^2}{c}, \qquad c = \frac{\omega R^2}{\Delta x}. \tag{8}
$$

#### 2.3.4 Why $v$, $T$, and $\theta_0$ do not appear

$\Delta X$ is the angular width of the frozen segment (after the disc has stopped) and is determined only by the rotation during the flight time $R/c$; hence $v$ does not appear. The speed $v$ affects only the slope of the moving segment, and the existence of the moving segment ($v \neq 0$) merely makes the kink identifiable. The frozen-segment width is independent of the total exposure time $T$ and depends only on $R/c$. The initial angle $\theta_0$ merely translates the whole trace rigidly and does not affect the angle between the two radii. The angular velocity $\omega$ must be calibrated at the laser site with an encoder, stroboscope, or period counting; this is a local single-point measurement and does not involve remote clock synchronization.

### 2.4 Experimental procedure

#### 2.4.1 Preparation

The preparation consists of: a rotating laser (with angle encoder, capable of continuous rotation and continuous emission); a planar disc of radius $R$ (surface coated with photoresist, aluminum film, or another etchable layer); a central trigger integral with the disc; a descent mechanism (guide rails, electromagnetic release, or drop tower); laser safety goggles, a light shield, and an emergency stop; and angle-readout tools (precision turntable, microscope, goniometer).

#### 2.4.2 Calibration

Calibrate the angular velocity $\omega$ by measuring the laser rotation rate with a rotary encoder, stroboscope, or period counter; this is a local single-point measurement. Calibrate the radius $R$ by measuring the distance from the laser rotation center to the disc recording region with a tape measure or laser rangefinder. Check alignment: the disc center is concentric with the rotation axis, the beam strikes the disc surface at a near-grazing incidence, and the relative position of the trigger and the laser is fixed so that the stop direction is well defined.

#### 2.4.3 Operation

1. Start the laser and let it rotate stably at $\omega$ while emitting continuously;
2. Release the disc so that it falls vertically; the laser etches the moving segment on the disc;
3. The disc presses the laser; in the same mechanical contact event the disc freezes and the laser stops;
4. In-flight photons continue to arrive and complete the frozen segment on the frozen disc (this segment is completed within $R/c$; if the laser continues to emit along the stop direction after stopping, the trace extends along the stop radius and does not affect $\Delta X$);
5. Remove the disc and preserve the etch trace.

#### 2.4.4 Readout and computation

1. Read the laser angle $\theta_{\mathrm{stop}}$ at stopping to determine the stop-direction radius;
2. Locate the kink $K$ on the disc, i.e., the boundary between the moving segment (slanted line/spiral) and the frozen segment (arc at constant radius); this is the impact point of the photon that arrives exactly at the stopping instant;
3. Locate $P_2$, the intersection of the frozen segment with the stop-direction radius (the etch endpoint);
4. Join $K$ and $P_2$ to the center and read the angle $\Delta X$ (in radians) with a turntable, goniometer, or microscope;
5. Substitute into $c = \omega R / \Delta X$; if the arc length $\Delta x$ is measured directly, use $c = \omega R^2 / \Delta x$.

#### 2.4.5 Verification and repetition

The following checks are recommended: repeat the run with the same parameters and check the reproducibility of $\Delta X$; vary the drop height or descent mode and confirm that the angular width of the frozen segment is unchanged (verifying that $v$ and $T$ indeed cancel); reverse the laser rotation and repeat to check directional symmetry, i.e., a direct probe of one-way anisotropy; vary $\omega$ or $R$ and verify that the value of $c$ is self-consistent. If the frozen segment is not an arc at a single radius, or if $\Delta X$ changes markedly with direction, the one-way speed may be anisotropic and requires separate analysis.

#### 2.4.6 Data analysis and statistics

The kink $K$ should not be located by eye. We recommend fitting the moving and frozen segments separately, e.g., a spiral or straight-line model for the moving segment and a circular-arc model for the frozen segment, and estimating the location of $K$ and its uncertainty by segmented regression or changepoint detection. The point $P_2$ is the intersection of the frozen segment with the stop-direction radius. The stop-direction radius is transferred from the encoder angle $\theta_{\mathrm{stop}}$ to the disc coordinate system via reference marks on the disc, and the transfer error should be included in the systematic budget. For each run, record $\omega$, $R$, $\theta_{\mathrm{stop}}$, $\Delta X$, ambient temperature, and vibration monitoring. We recommend at least $N=10$ repeats, reporting the mean, standard deviation, and 95% confidence interval of $\Delta X$; if the goal is an anisotropy upper limit, report the one-sided upper limit on $|\delta c|/c = \delta(\Delta X)/\Delta X$. As a worked example, with $R=10$ m, $\omega=1000$ rad/s, $\Delta X=3.3\times10^{-5}$ rad, and $\delta(\Delta X)=1$ μrad, $|\delta c|/c \approx 3\%$.

### 2.5 Magnitudes and errors

#### 2.5.1 Signal size

From $\Delta X = \omega R/c$, the signal is very small at benchtop scales. Table 2 gives $\Delta X$ for representative parameters.

**Table 2: Angular signal $\Delta X$ for different parameters**

| $\omega$ (rad/s) | $R = 2$ m | $R = 10$ m |
|---|---:|---:|
| $10^2$ | $6.7\times10^{-7}$ rad | $3.3\times10^{-6}$ rad |
| $10^3$ | $6.7\times10^{-6}$ rad | $3.3\times10^{-5}$ rad |

The corresponding arc length is $\Delta x = R\Delta X$; for $R = 10$ m and $\omega = 1000$ rad/s, $\Delta x \approx 330$ μm, measurable with an optical microscope.

#### 2.5.2 Error sources

From $c = \omega R / \Delta X$, the error propagation is

$$
\frac{\delta c}{c} = \sqrt{
\left(\frac{\delta\omega}{\omega}\right)^2 +
\left(\frac{\delta R}{R}\right)^2 +
\left(\frac{\delta(\Delta X)}{\Delta X}\right)^2
}. \tag{9}
$$

The main error sources are listed in Table 3. The dominant term is $\Delta X$, which requires precise localization of the kink and the stop-direction radius.

**Table 3: Error sources**

| Source | Typical precision | Notes |
|---|---|---|
| $\omega$ | $0.01\%$ | Encoder, stroboscope |
| $R$ | $0.01\%$ | Tape measure, laser rangefinder |
| $\Delta X$ | Dominant error | Kink and stop-direction localization; turntable/microscope readout |

#### 2.5.3 The kink and the stopping event

Both endpoints of $\Delta X$ come from the same rigid-body event, namely the instant at which the disc freezes; this statement holds only under the ideal rigid-body postulate. The kink $K$ is localized by the change in slope of the trace, and the stop-direction radius is localized by the laser encoder. Any real time difference $\delta t$ -- whether a contact-trigger delay, the propagation time of the freezing wave in the material, or the laser deceleration time -- enters $\Delta X$ directly: $\Delta X = \omega(R/c + \delta t)$. In real materials the freezing propagates at the sound speed $c_s$, with $\delta t \sim R/c_s$; for $R=10$ m and $c_s \sim 5$ km/s this is about 2 ms, larger than $R/c \sim 33$ ns by about $6\times10^4$ (about five orders of magnitude), and it would completely overwhelm the signal if uncontrolled. The disc method must therefore state "disc freezes = laser stops" as an ideal rigid-body postulate and at the same time satisfy the engineering condition that the recording surface stops writing over a time scale much smaller than $R/c$ (e.g., a photosensitive layer or shutter array gated by a common electrical signal); the laser stopping time must also be included in the error budget. The relation between finite rigidity and synchronization conventions is discussed in Appendix A.1.

### 2.6 Discussion

#### 2.6.1 Role of clock synchronization

The apparatus introduces no second asynchronous clock. The traditional deadlock is that two spatially separated clocks must be synchronized, and synchronization requires knowing the speed of light. In the present apparatus, the disc is a recording surface rather than a clock and $v$ does not enter the final formula; the trigger is a contact event on one rigid body rather than a clock; and the only time base is the locally calibrated $\omega$ of the laser, which is not aligned with any remote clock.

Strictly speaking, "motion-encoded time" still implicitly adopts a synchronization convention of the laboratory frame. The precise statement is therefore that the scheme bypasses the remote-clock-synchronization deadlock but does not bypass all synchronization conventions. It replaces "a second clock" with "one event on a rigid body plus a recording surface."

More fully, the time-base structure of the scheme consists of three layers of postulates. The emitter time axis comes from the laser rotation angle, and "angle difference = time difference" relies on constant $\omega$; the receiver time axis comes from the recording-surface position (the etch radius or the ring height), and "position difference = time difference" relies on constant $v$; the time pairing between the two sites is defined by the rigid-body contact, namely that the disc freezes and the laser stops simultaneously. The experiment actually measures only geometric quantities (angles, distances, position differences); time does not appear independently but is defined jointly by these three layers of postulates. At the operational level there are no two clocks to compare; logically this is equivalent to projecting receiver events onto the emitter time coordinate. The synchronization problem has not disappeared; it has become a postulate.

#### 2.6.2 Comparison with historical methods

Table 4 compares the present scheme with Foucault (1862) [5] and Michelson (1879) [6].

**Table 4: Comparison with historical methods**

| | Foucault (1862) | Michelson (1879) | This scheme |
|---|---|---|---|
| Light path | Round trip | Round trip | One way |
| Rotating element | Small mirror | Octagonal mirror | Rotating laser |
| Recording | Spot shift | Spot shift | Etch angle on planar disc |
| Second clock | None | None | None (replaced by rigid-body event) |
| Reference frame | Multiple separated components | Multiple separated components | Single rigid disc |

#### 2.6.3 Scope and relation to SR

In principle the scheme gives the angular encoding $c = \omega R / \Delta X$ of the one-way speed. Its main value is to place a direct constraint on the one-way speed at benchtop scale and to probe anisotropy through changes in $\Delta X$ under different directions and physical conditions. Because $\Delta X$ is very small, a first-generation apparatus should emphasize reproducibility, directional symmetry, and cross-parameter self-consistency rather than trying to exceed the absolute precision of existing round-trip measurements.

Further discussion of the rigid-body simultaneity postulate is given in Appendix A.1; the question of whether beyond-prediction results can occur under the postulates is analyzed in Section 5.2 and Appendix A.2.

#### 2.6.4 Classification of one-way and round-trip light paths

At the level of the light path, the experiment is a one-way-light experiment: photons travel once from the rotating laser to the disc and are absorbed, with no return path and no reliance on a return signal. This differs completely, in path structure, from round-trip experiments such as Fizeau's and Michelson's $A \to B \to A$. The classification criterion is the number of legs in the measurement light path, not "whether the photon is ultimately absorbed": historical experiments placed a mirror at the far end, and removing the mirror immediately destroys the measurement, so they are two-leg paths; the present scheme has only an absorbing surface at the far end and is a one-leg path.

The absorbing surface may re-emit photons after excitation, in the form of fluorescence, phosphorescence, or thermal radiation, but the re-emission is delayed, random in direction, incoherent, and usually at a different wavelength; it does not return along the original path, cannot be used for round-trip timing, and counts as background noise. Only the addition of a mirror or phase-conjugate mirror would turn the scheme into a round-trip experiment. A fuller argument is given in Appendix A.3.

At the level of the physical quantity, one must distinguish "a one-way-light experiment" from "a strict measurement of the one-way speed of light": the raw geometric readouts (trace shape, $\Delta X$) are convention-independent one-way propagation effects, whereas converting them to a numerical value $c$ gives only the one-way speed in the chosen coordinates. This distinction is the basis of the conclusions in Section 5.

### 2.7 Summary

The disc method has only three actions: start the laser, let the disc fall and press it, and measure one angle. The key physical step is that, after stopping, in-flight photons continue to arrive and complete the trace up to the stop-direction radius; the central angle between the impact point of the photon arriving exactly at the stopping instant (the kink) and the stop-direction radius is $\Delta X = \omega R/c$, so $c = \omega R/\Delta X$. Under the ideal rigid-body postulate and the design condition of synchronized stopping of writing, no two clocks, no clock comparison, and no stopwatch are needed at the operational level; the core engineering challenge is to read the tiny angle accurately and to ensure that the freeze/stopping time difference is much smaller than $R/c$.

---

## 3. Conical-ring method

### 3.1 Apparatus and geometry

The rotating laser lies on the cone axis and rotates at constant angular velocity $\omega$ while emitting continuously, so the beam sweeps out a cone with the rotation axis as its axis. A very thin horizontal ring (radius $\rho$) descends slowly along the axis at speed $v$, assumed uniform; this is a postulate, not a measured result.

When the ring reaches a certain height it intersects the beam; this intersection is the "photon hit." The ring marks the azimuth $\varphi$ of the hit point relative to the $x$-axis on its own circumference. The ring continues to descend and finally triggers the laser to stop; the final rotation angle $\theta_{\mathrm{stop}}$ is recorded at stopping. The vertical displacement of the ring from the hit point to the stopping point is denoted $\Delta z$, and the straight-line distance from the hit point to the laser is denoted $d$. Let $\gamma$ be the half-angle of the beam cone and $z_a$ the height of the hit point; then $d = \rho/\sin\gamma = z_a/\cos\gamma$ and $z_a = \rho/\tan\gamma$.

The two angles must be interpreted carefully: $\varphi$ is the emission azimuth recorded by the ring, i.e., the pointing angle of the beam at the instant of emission of the photon that hits the ring; $\theta_a$ is the pointing angle given by the laser encoder at the instant the photon arrives at the ring, and their difference $\theta_a-\varphi = \omega d/c$ encodes the flight time. The actual procedure does not read $\theta_a$ directly; instead it reads $\theta_{\mathrm{stop}}$ after stopping and subtracts the ring descent time.

### 3.2 Measured quantities and formulas

If the laser pointing $\theta_a$ could be read simultaneously with the instant at which the ring is hit, then

$$
c = \frac{d\,\omega}{\theta_a - \varphi}. \tag{10}
$$

In the actual scheme the ring triggers the stop and $\theta_{\mathrm{stop}}$ is read afterward; the intervening time is supplied by the ring descent:

$$
t_{\mathrm{stop}} - t_a = \frac{\Delta z}{v}, \tag{11}
$$

so that

$$
c = \frac{d}{(\theta_{\mathrm{stop}} - \varphi)/\omega - \Delta z/v}. \tag{12}
$$

The measured quantities are therefore: $\varphi$ (ring azimuth), $\theta_{\mathrm{stop}}$ (final laser angle), $\Delta z$ (displacement), $d$ (distance), and the postulate parameters $\omega$ and $v$.

### 3.3 Interpretation of the result

The experiment is one-way light: light travels once from the laser to the ring and has no return path; the classification is based on the designed light path rather than on absorption/re-emission (Section 2.6.4 and Appendix A.3). Under the two postulates of uniform laser rotation and uniform ring descent, Eq. (12) gives a definite number, namely the one-way light speed in the time coordinates defined by those postulates. It need not be compared with an SR prediction: SR does not predict a specific numerical value of the one-way speed; SR predicts round-trip speeds, raw geometric traces, and other convention-independent quantities. Thus "measure under the postulates, obtain a definite value, and record it as the one-way light speed in those coordinates" is a complete and self-consistent statement. The value is unrelated to any SR prediction and neither confirms nor refutes SR.

### 3.4 Experimental procedure

#### 3.4.1 Geometry and parameter table

Before the experiment, calibrate $\omega$ (encoder/stroboscope), $v$ (two light gates or a high-speed camera), $\rho$ and $\gamma$ (mechanical survey), from which $d = \rho/\sin\gamma$ follows; place angular reference marks on the ring for reading $\varphi$. Table 5 gives a set of suggested parameters.

**Table 5: Representative parameters for the conical-ring method**

| Parameter | Symbol | Suggested value | Notes |
|---|---|---|---|
| Rotation angular velocity | $\omega$ | 1000 rad/s | Locally calibrated |
| Cone half-angle | $\gamma$ | $30^\circ$ | Determines $d$ and hit height |
| Ring radius | $\rho$ | 0.5 m | Matched with $z_a = \rho/\tan\gamma$ |
| Flight distance | $d$ | 1.0 m | $d = \rho/\sin\gamma$ |
| Descent speed | $v$ | 1 m/s | Postulate parameter; needs high-precision calibration |
| Hit-to-trigger displacement | $\Delta z$ | 1 m | Determines $\Delta z/v$ |
| Arrival/emission angle difference | $\theta_a - \varphi$ | $\sim 3.3\times10^{-6}$ rad | Equal to $\omega d/c$ |

#### 3.4.2 Calibration

Calibrate $\omega$, $v$, $\rho$, $\gamma$, the trigger position, and $d$; establish the transfer relation between the ring angular reference and the encoder zero. The uniformity of $v$ should be monitored independently with a velocity curve, because Eq. (12) depends directly on $v$.

#### 3.4.3 Operation

1. The laser rotates at $\omega$ and emits continuously;
2. Release the ring; the ring descends at $v$;
3. The beam leaves a hit mark on the ring, which records the emission azimuth $\varphi$;
4. The ring triggers the stop; record $\theta_{\mathrm{stop}}$ and $\Delta z$;
5. Recover the ring and read $\varphi$ and $\Delta z$.

#### 3.4.4 Readout and computation

1. Check the consistency condition $(\theta_{\mathrm{stop}}-\varphi)/\omega > \Delta z/v$;
2. Compute $\theta_a = \theta_{\mathrm{stop}} - \omega\Delta z/v$;
3. Substitute into $c = d\omega/(\theta_a-\varphi)$ or Eq. (12).

#### 3.4.5 Repetition and verification

Repeat with different $\omega$, $v$, and $\Delta z$ and check self-consistency; rotate the entire apparatus to test directional dependence; record the velocity curve $v(t)$ in every run to confirm that the uniform-descent postulate holds.

### 3.5 Magnitudes, errors, and consistency conditions

The denominator of Eq. (12) must be positive:

$$
\frac{\theta_{\mathrm{stop}}-\varphi}{\omega} > \frac{\Delta z}{v}, \tag{13}
$$

which is equivalent to $\theta_a > \varphi$, i.e., positive flight time; if the two sides approach each other, the error diverges.

The error propagation is as follows. Let $\Delta\theta = \theta_{\mathrm{stop}}-\varphi$ and $D = \Delta\theta/\omega - \Delta z/v = d/c$; then

$$
\frac{\delta c}{c} = \sqrt{\left(\frac{\delta d}{d}\right)^2 + \left(\frac{\delta D}{D}\right)^2}, \qquad
\delta D = \sqrt{\left(\frac{\delta\Delta\theta}{\omega}\right)^2 + \left(\frac{\Delta\theta\,\delta\omega}{\omega^2}\right)^2 + \left(\frac{\delta\Delta z}{v}\right)^2 + \left(\frac{\Delta z\,\delta v}{v^2}\right)^2}. \tag{14}
$$

The magnitudes are given in Table 6. Numerically $D = d/c \sim 3$ ns while $\Delta z/v \sim 1$ s; Eq. (12) is the subtraction of two large numbers to obtain a nanosecond difference. Even if $\delta v/v$ and $\delta\Delta z/\Delta z$ are both $10^{-6}$, $\delta(\Delta z/v) \sim 1$ μs, still about 300 times larger than $D$. Absolute extraction of $c$ with the conical-ring method therefore requires measuring $\Delta z/v$ to nanoseconds, which is equivalent to clock-transport synchronization. The practical feasibility of the scheme lies mainly in anisotropy/raw-geometry probing; the absolute numerical channel is limited by this requirement, consistent with Appendix A.1.

**Table 6: Dominant error magnitudes in the conical-ring method**

| Term | Value | Contribution to $D$ |
|---|---|---|
| $d/c$ | 3.3 ns | Signal |
| $\Delta z/v$ | 1 s | Cancellation term |
| $\delta(\Delta z/v)$, relative precision $10^{-6}$ | 1 μs | Dominant error |
| $\delta\Delta\theta/\omega$, about 1 arcsec | 5 ns | Same order as signal |

---

## 4. Variants and controlled conditions

### 4.1 Structural variants

The conclusions for five structural variants are as follows.

**Variant A: Inverted version (fixed plane + descending rotating laser).** It cannot measure the speed of light. The etch point depends only on the state at emission (laser height + pointing angle) and its intersection with the fixed plane; the flight time determines "when it is written," not "where it is written." The trace is independent of $c$ (identical for finite or infinite light speed), and $v$ no longer cancels; the pitch of the spiral is set by $v/\omega$.

**Variant B: Conical trace + thin-ring version.** This is the scheme of Section 3. The thin ring is a one-dimensional falling disc, i.e., a moving arrival-end clock. If the laser pointing $\theta_a$ could be read simultaneously with the photon hit, Eq. (10) would apply; but "simultaneous readout" is precisely synchronization. In the actual stop-trigger procedure, the step $\Delta z/v$ in Eq. (12) is clock-transport synchronization. The scheme is indeed one-way light, but it cannot bypass the simultaneity convention.

**Variant C: Two independent plates descending in the same horizontal plane.** Using "same height" to replace rigid-body simultaneity: "same height = simultaneous" for the two plates is clock-transport synchronization; the two plates are two moving clocks, and "initially same height and identical descent" is a synchronization assumption. "Simultaneous release" itself requires a mechanism: a rigid frame corresponds to the rigidity postulate, while an optical/electrical trigger returns to the synchronization problem. Only the carrier has changed.

**Variant D: Inertial-clock version.** Using uniform inertial motion to define time. Inertia can define the local rate of a clock (the time parameter along a worldline) but does not define "the same instant" across space; in Newtonian spacetime the family of inertial motions can define global absolute time, whereas in SR geodesics do not define a unique global simultaneity surface. The loop "judging uniform motion requires time, and judging time requires uniform motion" can only be closed by a postulate, not by measurement.

**Variant E: Acceleration or large-mass field version.** Accelerating the whole apparatus or placing a large mass on one side produces real effects: clock-rate differences, gravitational redshift, geodesic deviation, and light-path bending. These are metric and geometric effects, not a convention-independent one-way light speed. The same physical process in an accelerated elevator frame (Rindler coordinates) and in a free-fall frame gives different coordinate one-way light speeds but identical observables; choosing an external reference frame is itself a convention.

### 4.2 Family of 16 controlled variants

The same core apparatus supports a family of 16 controlled variants that vary the medium, temperature, electromagnetic fields, gravitational gradients, rotation, and similar conditions one at a time; each has a null hypothesis from standard theory (Table 7). Switching between variants requires only replacing the medium enclosed by the recording surface, adding external field sources (magnets, electrodes, transducers), or changing the mechanical platform.

**Table 7: The 16 controlled variants**

| # | Variant | Probes |
|:---:|---|---|
| 1 | Vacuum baseline | Reference trace |
| 2 | Air at standard conditions | Refractive-index effect |
| 3 | Liquid media (water, ethanol, oil) | $c$ in dense media |
| 4 | Same refractive index, different chemical composition | Medium-specific coupling beyond refractive index |
| 5 | Temperature gradient across panel | Thermal sensitivity of one-way $c$ |
| 6 | Time-varying medium (pulsed heating/injection) | Transient response |
| 7 | Near-critical-point fluid | Critical opalescence and fluctuation enhancement |
| 8 | Static electric field across medium | Electro-optic coupling |
| 9 | Static magnetic field across medium | Magneto-optic coupling |
| 10 | Acoustic standing wave in medium | Acousto-optic modulation of one-way $c$ |
| 11 | Flowing medium (pumped circulation) | Drag effects (cf. Fizeau 1851) [7] |
| 12 | Gravitational gradient (heavy mass near panel) | Gravitational coupling |
| 13 | Accelerated descent (drop tower/centrifuge) | Inertial coupling |
| 14 | Co- or counter-rotating panel | Angular-momentum coupling (signal amplification up to 2x) |
| 15 | Rotating the entire apparatus | Absolute-rotation coupling |
| 16 | Strong field + gravitational loading | Cross-coupling terms |

### 4.3 Decision procedure for representative variants

Writing complete null hypotheses, observables, and controls for all 16 variants is beyond the scope of this paper; the following three representative entries give directly executable decision procedures.

**Variant 4 (same refractive index, different chemical composition).** Null hypothesis: the trace shape and $\Delta X$ are unchanged when the media are interchanged. Observable: whether the difference in fitted curvature or $\Delta X$ between the two media exceeds the 3σ statistical uncertainty. Controls: same temperature, pressure, density, and flow speed; alternate "medium A-B-A-B" with at least 6 repetitions.

**Variant 11 (flowing medium).** Null hypothesis: there is no additional one-way coupling beyond Fresnel drag, and the standard-theory drag displacement is far below the detection limit of the apparatus. Observable: whether the trace deviation between flowing and static media exceeds the sensitivity limit of Appendix B. Controls: same refractive index and temperature, flow in both directions with two runs each, excluding temperature gradients and pump vibration.

**Variant 12 (gravitational gradient).** Null hypothesis: there is no gravitational coupling beyond the prediction of general relativity. Observable: whether $\Delta X$ changes with the position of the heavy mass as it is moved near and far. Controls: baseline repetition with the mass far away, apparatus position, and ground-vibration monitoring; the standard GR displacement is far below the detection limit, so a positive signal corresponds to non-GR coupling.

---

## 5. Conclusions and outlook

### 5.1 Main conclusions

Given the two postulates "laser rotation is uniform ($\omega$ constant)" and "recording-surface motion is uniform ($v$ constant)," both the disc method and the conical-ring method give a definite one-way light-speed value in that time coordinate: $c = \omega R/\Delta X$ for the disc method and Eq. (12) for the conical-ring method. This value is a coordinate quantity: it is unrelated to any SR prediction, need not be compared with the SR value $c$, and does not constitute a test or refutation of SR.

SR predicts convention-independent quantities: the round-trip speed, the raw geometric trace (disc $\Delta X$, ring azimuth), redshifts, and so on. To test for new physics, we recommend rotating the entire apparatus and checking whether the raw geometric readouts change with direction: SR predicts no change, while Lorentz-violating test theories may predict a change.

### 5.2 Criteria for beyond-prediction signals

"Beyond prediction" must be distinguished by target. For the postulates themselves: the postulates define the time coordinates, and the one-way light speed in those coordinates is a definite number, so there is no internal sense of "beyond prediction"; an unexpected result means only that the postulates fail, e.g., nonuniform laser rotation, unstable recording-surface motion, or non-rigid behavior, all of which are systematic errors rather than new physics. For SR predictions: SR predicts convention-independent raw geometry, including whether the trace is straight, whether $\Delta X$ changes with direction, round-trip quantities, and redshifts; only direction-dependent or curved raw geometry is beyond SR. For the numerical value of the one-way speed: SR makes no prediction of this value, so a measured value different from $c$ is not beyond prediction; it is merely the result in the chosen coordinates.

If the one-way speed really exhibits systematic variation, four forms can be distinguished: directional dependence, in which different apparatus orientations give different values, indicating a preferred direction; temporal dependence, in which the same apparatus gives different values at different times, indicating a hidden variable or evolution of the vacuum; conditional dependence, in which temperature, medium, electromagnetic fields, gravitational gradients, etc., change the value, indicating a new coupling channel; and motion-state dependence, in which the value changes with the apparatus motion relative to some reference frame, indicating a preferred frame or ether-like structure. The direction-antisymmetric component and some conditional-dependence channels are precisely the parts that round-trip experiments cannot detect in principle and that the present scheme probes directly. If directional dependence is confirmed, the light-cone structure becomes direction-dependent and causal limits may be anisotropic.

Beyond-prediction results are therefore possible, and this is precisely the target of anisotropy detection: a curved trace is a positive detection, and a straight trace is an upper-limit constraint. The three cleanest forms of a "beyond-prediction" result are: internal inconsistency of repeated experiments under the same postulates; a change of raw geometry with apparatus direction or orientation; and a channel deviation beyond known physics in some variant (e.g., a one-way Fresnel drag different from the round-trip value, or rotation coupled into light propagation).

Attribution requires a test theory. The apparatus itself is subject to the same dynamics: Lorentz violation would affect laser uniformity, disc rigidity, and clock rates simultaneously, so a curved trace alone only says "something is wrong" and must be isolated with SME-type models and cross-variants. The same-refractive-index control, temperature-gradient, electromagnetic-field, and gravitational-gradient variants in Table 7 are designed for exactly this purpose.

The expectation is biased toward null: existing SME constraints bound round-trip anisotropy at about $10^{-17}$ [8], while the sensitivity of the present experiment in the $\lambda \sim 0.1$--$10$ m one-way channel is about $|\delta c|/c \sim 5.8\%$ (derivation in Appendix B). One-way and round-trip channels are complementary, so a positive signal would require a large effect not covered by existing constraints; this is not impossible, but the primary expectation is null. A positive result would be transformative and would be a physical signal independent of the "measuring the one-way speed under postulates" framework.

It must be emphasized that any positive signal must reside in the raw geometry: if the speed of light really depends on direction, time, or conditions, the uniformity of the laser rotation, the motion of the recording surface, and clock rates may be affected by the same hidden variable. Only convention-independent readouts such as trace curvature, direction-dependent $\Delta X$, or phase-lock misalignment between adjacent segments are beyond-SR signals. The converted numerical value of the one-way speed is not an SR prediction, and a measured value different from $c$ is not evidence for new physics. If directional or motion-state dependence is confirmed, the Reichenbach $\varepsilon$ convention degenerates in that situation from a definition to a coordinate choice, and "simultaneity" becomes a physical fact.

### 5.3 Revised statement

This discussion does not deny postulate-based measurement: once postulates are separated from measurements, "uniform rotation/uniform descent" defines the time coordinates, and the one-way light speed is a computed quantity in those coordinates, a definite number. This number is unrelated to SR predictions; it neither "violates SR" nor "shows SR was wrong," because SR does not give a numerical prediction for the one-way speed. The ring experiment, the disc experiment, and the two-plate experiment can each give a definite one-way light speed under their own postulates; numerical differences between them reflect differences in the postulates (time coordinates), not errors in any experiment.

---

## Appendix A: Key postulates and common objections

### A.1 Rigid-body simultaneity and the $\varepsilon$-convention

The core relation $\Delta X = \omega R/c$ of the disc method presupposes that "disc freezing" and "laser stopping" occur simultaneously in the laboratory frame (at time $T$). These are two spatially separated events; guaranteeing their simultaneity by a single rigid body is essentially equivalent to choosing a synchronization convention. More generally, the one-way speed of light is convention-dependent (the Reichenbach $\varepsilon$ convention [2,3]): the same raw geometric readout gives different values of $c$ under different conventions.

Replacing the disc with two independent plates does not bypass the problem: "same height = simultaneous" for the two plates is clock-transport synchronization, the two plates are two moving clocks, and "initially same height and identical descent" is a synchronization assumption. "Simultaneous release" requires a mechanism: a rigid frame is the rigidity postulate, and an optical/electrical trigger returns to the synchronization problem. Taking the inertial law as a root assumption is equally insufficient: inertia can define the local rate of a clock but does not define "the same instant" across space; in Newtonian spacetime the family of inertial motions can define global absolute time, while in SR geodesics do not define a unique global simultaneity surface. The loop "judging uniform motion requires time, and judging time requires uniform motion" can only be closed by a postulate, not by measurement.

Acceleration or gravitational scenarios produce real effects -- clock-rate differences, gravitational redshift, geodesic deviation, light-path bending -- but these are metric and geometric effects, not a convention-independent one-way light speed. The same physical process in an accelerated elevator frame (Rindler coordinates) and in a free-fall frame gives different coordinate one-way light speeds but identical observables. At near-light uniform motion, the relativity principle states that internal experiments are identical to those in a stationary laboratory; differences appear only when an external reference frame is chosen, and choosing that frame is itself a convention.

The uniformity of any clock can only be a postulate, and postulates must be separated from measurements: uniform rotation/descent defines the time coordinates, and the one-way light speed is a computed result in those coordinates. Under different conventions the one-way value may legitimately differ from the round-trip $c$; "not matching" is not an error but a manifestation of convention, and repeated consistency only shows that the clock is repeatable. Only if the raw geometric readout (without conversion to $c$) changes with apparatus direction might it indicate physics beyond relativity (e.g., Lorentz violation).

The unprovability of postulates is not a difficulty peculiar to relativity. Newtonian mechanics likewise requires postulates such as absolute time and inertial structure; "there is no object that can be known to move uniformly without measurement" is a loop common to all axiomatized physics. The substance of general relativity is also not the vague statement "spacetime is not uniform" but the specific structures of a dynamical metric, matter-geometry coupling, geodesic free fall, and the local equivalence principle; what is testable is the whole theory's implications, not a single postulate. The present paper is therefore methodologically in the same family as the Newtonian and Einsteinian frameworks: choose postulates, define time, derive, and test implications; the difference is that the synchronization convention is made explicit. The genuinely empirical content lies in convention-independent raw geometric readouts and round-trip quantities.

### A.2 Postulate failure and identification of beyond-prediction signals

Identifying a "beyond-prediction" result requires distinguishing the target. For the postulates themselves: the postulates define the time coordinates, and the one-way light speed in those coordinates is a definite number, so there is no internal sense of "beyond prediction"; an anomaly means only that the postulates fail, namely nonuniform laser rotation, unstable recording-surface motion, or non-rigid behavior, all systematic errors rather than new physics. For SR predictions: SR predicts convention-independent observables, i.e., raw geometry (whether the trace is straight, whether $\Delta X$ is direction-independent, round-trip quantities, redshifts, etc.); direction-dependent or curved raw geometry is beyond SR. For "the numerical value of the one-way speed": SR makes no prediction of this value at all, so a measured value different from $c$ is not beyond prediction; it is simply the result in the chosen coordinates.

The three cleanest forms of a beyond-prediction result are: internal inconsistency of repeated experiments under the same postulates (broken reproducibility); a change of raw geometry with apparatus direction or orientation (anisotropy signal); and a channel deviation beyond known physics in some variant (e.g., a one-way Fresnel drag coefficient different from the round-trip value, or rotation coupled into light propagation). Once such a result appears and systematic errors are excluded, it is an SR beyond-prediction result, i.e., a new-physics candidate.

Attribution must be careful: the apparatus itself is physical, and rotation, descent, rigidity, and clocks are governed by the same dynamics. If Lorentz violation exists, it would not only change $c(\theta)$ but also the uniformity of the laser, the rigidity of the disc, and clock rates; a curved trace alone only says "something is wrong." Attributing it to light-speed anisotropy rather than mechanical/clock anomalies requires a test theory (SME-type models) and cross-variants; the same-refractive-index control, temperature-gradient, electromagnetic-field, and gravitational-gradient variants of Section 4.2 do exactly this.

In principle a beyond-prediction result is possible, but the expectation is biased toward null. Existing SME constraints bound round-trip anisotropy at about $10^{-17}$ [8], while the sensitivity of the present experiment in the $\lambda \sim 0.1$--$10$ m one-way channel is about $|\delta c|/c \sim 5.8\%$ (derivation in Appendix B). A positive beyond-prediction result at this sensitivity requires a large effect not covered by existing constraints; one-way and round-trip channels are complementary, so this is not impossible, but the primary expectation is null. A positive result would be transformative: it would be a signal of new physics, not evidence that "the framework for measuring the one-way speed under postulates is wrong."

Round-trip experiments cancel the direction-antisymmetric term, i.e., the difference between $c(\theta)$ and $c(\theta+\pi)$ (Eq. (1)). If $c(\theta) = c + \delta$ and $c(\theta+\pi) = c - \delta$, then $\delta$ cancels in the sum and the round-trip time retains only even-order terms. This is why Michelson-Morley experiments are sensitive only at $O(v^2/c^2)$ and one-way experiments can detect first-order asymmetry $O(v/c)$. The rotating-laser version is genuinely one-way: the beam is absorbed at the recording surface and has no return path, so the asymmetry between $c(\theta)$ and $c(\theta+\pi)$ is not cancelled geometrically; a curved trace or a phase-lock misalignment between adjacent segments exposes the direction asymmetry directly.

The cost of a one-way experiment is the absence of round-trip common-mode cancellation: in a round-trip experiment the same path is traversed twice, so fluctuations in temperature, density, vibration, etc. affect the two directions almost identically and are subtracted automatically. A one-way experiment has no such cancellation, so systematic errors are harder to suppress, and any "beyond-prediction" result must first exclude medium, mechanical vibration, thermal gradients, stray fields, and similar effects. Within a test-theory framework, the one-way variants are complementary channels that round-trip experiments cannot replace; they test whether the direction asymmetry of light propagation is zero.

### A.3 Classification of one-way and round-trip paths

The classification criterion is not "whether the photon is ultimately absorbed" but whether the experimental design contains a return light path. Photons in any experiment are ultimately absorbed; this does not affect whether the experiment is round-trip or one-way.

Historical experiments can be identified as round-trip by construction: the Fizeau gear method [4], the Michelson rotating-mirror method [6], and the Foucault method [5] all place a mirror at the far end, the beam $A \to B$ is reflected back to $A$, and the detector is at $A$. Removing or blocking the far-end mirror immediately destroys the return signal and the measurement cannot be completed, proving that the timing relies on the return path. The present scheme likewise proves by construction that it is not round-trip: the receiving end is an absorbing surface with no mirror, no return path, and no signal returning to the emitter; the etch on the disc/ring records only the first arrival. There is no second optical path from the receiving end back to the emitter anywhere in the apparatus.

The absorbing surface does release photons: it converts photon energy into excited states, which may subsequently re-emit photons as fluorescence, phosphorescence, or thermal radiation. These re-emitted photons have a delay (the absorption-re-emission time constant), random directions (isotropic spontaneous emission), no fixed phase relation (incoherence), and usually different wavelengths (Stokes shift, thermal spectrum). They do not return along the original path and cannot be used for round-trip timing; this "release" is precisely the manifestation of irreversibility. Making the path strictly reversible requires deterministic elements that send the beam back along its original route, such as mirror reflection, a corner-cube retroreflector, or optical phase conjugation; an absorbing surface is low-reflectance and dissipative and cannot do this. Adding a mirror or phase-conjugate mirror to the receiving end would turn the design into a round-trip experiment.

Although time-reversal amplitudes exist at the microscopic level, the experiment does not measure them: statistically they are completely swamped by the large number of independent arrival events, cannot serve as part of the timing signal, and do not constitute a designed optical path.

Thus round-trip/one-way is determined by the number of legs in the measurement light path: historical experiments are two-leg ($A \to B \to A$) because of the far-end mirror; the present scheme is one-leg ($A \to B$) because the far end is only an absorbing surface. The strict statement is: it is a one-way-light experiment -- the optical path is indeed one-way; it is not a "strict measurement of the one-way speed of light" -- the one-way light speed has no convention-independent value in SR, and any experiment can give only a value under a convention. The raw geometric readout corresponds to the convention-independent one-way propagation effect (the anisotropy-detection role of Method A in the companion document), while converting it to a numerical value $c$ is constrained by the synchronization convention (the absolute-value attempt of Method B).

---

## Appendix B: Sensitivity estimate

The bound $|\delta c|/c \lesssim 5.8\%$ used in Section 5.2 and Appendix A.2 is obtained as follows. For the trace-curvature channel, take trace length $L \sim 10$ cm and microscope pixel resolution $\delta_{\mathrm{pix}} \sim 1$ μm; the number of independent resolution elements is $N = L/\delta_{\mathrm{pix}} \sim 10^5$, so the minimum resolvable deviation from straightness is

$$
\delta z'_{\min} \sim \frac{\delta_{\mathrm{pix}}}{\sqrt{N}} \sim 3\ \mathrm{nm}. \tag{15}
$$

From $\delta z' = vR\,|\delta(1/c)|$, with $v = 1$ m/s and $R = 10$ m, the single-run sensitivity is

$$
\left|\frac{\delta c}{c}\right|_{\min} \sim \frac{\delta z'_{\min}\,c}{vR} \sim 0.09. \tag{16}
$$

Averaging over multiple runs, multi-segment stitching, and illumination optimization can improve this further; for a first-generation apparatus we conservatively take $|\delta c|/c \lesssim 5.8\%$. If instead the angular channel of the disc method is used, $|\delta c|/c \approx \delta(\Delta X)/\Delta X$; with $\Delta X = 3.3\times10^{-5}$ rad and $\delta(\Delta X) = 1$ μrad this is about 3%, the same order of magnitude.

---

## References

1. Einstein, A. (1905). "Zur Elektrodynamik bewegter Körper." *Annalen der Physik*, 322(10), 891-921.
2. Reichenbach, H. (1928). *Philosophie der Raum-Zeit-Lehre*. Walter de Gruyter.
3. Grünbaum, A. (1973). *Philosophical Problems of Space and Time*. D. Reidel.
4. Fizeau, H. (1849). "Sur une expérience relative à la vitesse de propagation de la lumière." *Comptes Rendus*, 29, 90-92.
5. Foucault, L. (1862). "Détermination expérimentale de la vitesse de la lumière." *Comptes Rendus*, 55, 501-503, 792-796.
6. Michelson, A. A. (1879). "Experimental determination of the velocity of light." *Proceedings of the American Association for the Advancement of Science*, 28, 124-160.
7. Fizeau, H. (1851). "Sur les hypothèses relatives à l'éther lumineux." *Comptes Rendus*, 33, 349-355.
8. Kostelecký, V. A. & Russell, N. (2011). "Data tables for Lorentz and CPT violation." *Reviews of Modern Physics*, 83(1), 11-31.
