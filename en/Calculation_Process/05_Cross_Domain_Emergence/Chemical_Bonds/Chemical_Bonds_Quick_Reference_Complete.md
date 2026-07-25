# SCVC Chemical Bonds Quick Reference (Including Heteronuclear & H-Bonds)

**Updated**: 2026-07-25 | Honesty System: GREEN/YELLOW/RED

---

## Homonuclear Diatomics (SCVC MO ab initio derived)

| Bond | $D_e$ (eV) | Method | Honesty |
|:---|:--:|:---|:--:|
| H-H | 4.75 | MO + SCVC $\alpha/m_e$ | GREEN |
| N≡N | 9.80 | MO + SCVC $\alpha/m_e$ | GREEN |
| O=O | 5.12 | MO + SCVC $\alpha/m_e$ | GREEN |
| F-F | 1.62 | MO + SCVC $\alpha/m_e$ | GREEN |
| Cl-Cl | 2.48 | MO + SCVC $\alpha/m_e$ | GREEN |

## Heteronuclear Bonds (SCVC Electronegativity + Standard Physical Chemistry)

| Bond | $D$ (eV) | Method | Source | Honesty |
|:---|:--:|:---|:---|:--:|
| C-H | 4.3 | Pauling + SCVC $\chi$ | 5.2 Appendix | YELLOW |
| Si-O | 4.6 | Pauling + SCVC $\chi$ | 5.2 Appendix | YELLOW |
| C-C | 3.6 | Scaling estimate / Exp standard | 5.2 Appendix | YELLOW |
| Ca-O | 3.5 | Born-Haber + SCVC $\alpha$ | 5.2 Appendix | YELLOW |

## Intermolecular Forces

| Interaction | Energy (eV) | Method | Source | Honesty |
|:---|:--:|:---|:---|:--:|
| H-bond (O-H···O) | 0.20 | SCVC $\chi$ + Experiment | 5.2 Appendix | RED |

---

## Honesty Classification System

| Label | Meaning |
|:---|:---|
| GREEN | SCVC ab initio derived, zero empirical parameters |
| YELLOW | SCVC locks inputs, standard empirical correlation / physical chemistry yields output |
| RED | Pure experimental value, SCVC provides physical consistency |

---

*SCVC does not replace Pauling/Born-Haber — SCVC locks the physical input parameters of these methods.*
