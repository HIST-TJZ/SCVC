# SCVC Nucleon-Nucleon Potential Derivation Request

## Background
SCVC already derives quark confinement, mass spectrum, and Pauli exclusion from geometry/topology. The simulation currently lacks a nucleon-nucleon interaction layer -- inter-proton forces use quark-level pairwise forces as approximation, causing inaccuracies in multi-nucleon systems.

## SCVC Locked Parameters
- alpha_s = 1/(16*pi) = 0.01989  (strong coupling, from vortex geometry)
- E_CORE = 2.1322  (GP vortex core energy)
- G_STRONG = 3.30  (vortex interaction strength)
- xi = 0.25  (vortex core radius)
- RHO_S = 6.5797 = 2*pi^2/3  (superfluid density)
- m_u/m_e = 3*sqrt(2), m_d/m_u = (5/3)^(3/2)
- E_SCALE_BEC = 0.4793 MeV per sim energy unit

## Request: Three Derivations

### 1. Pion Mass and Coupling
From alpha_s and quark masses, derive:
- m_pi (SCVC-derived value)
- g_piNN (pion-nucleon coupling)
- Expected scale: m_pi ~ 140 MeV, g_piNN ~ 13

### 2. Nucleon-Nucleon Residual Strong Force (OPEP)
From one-pion exchange:
- V_pi(r) = (g_piNN^2/4*pi) * (m_pi^2/12*M_N^2) * (tau1*tau2)(sigma1*sigma2) * exp(-m_pi*r)/r
- Need SCVC versions of tau*tau and sigma*sigma factors (from quark windings)
- Output: V_NN(r) functional form with ALL parameters in sim units

### 3. Hard Repulsive Core
From omega meson exchange or vortex topology overlap:
- Equivalent potential: V_core(r) = A * exp(-m_omega*r)/r  or  A/r^12
- m_omega ~ 782 MeV, derive from alpha_s and m_pi scaling
- Output: A and m_omega SCVC-derived values

## Output Format
For each result:
1. Derivation steps (verifiable)
2. Final formula (LaTeX)
3. Numerical values (sim units AND physical MeV)
4. SCVC constant provenance (NO free parameters)

## Critical Constraint
All parameters MUST derive from SCVC locked values. No parameter tuning accepted. If approximation is needed, label the approximation type and estimate error.