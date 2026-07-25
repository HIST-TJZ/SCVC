# SCVC Engineering Physics E116: The Physics of Power — How Much Inequality Can a Society Bear?

**Derivation Date**: 2026-07-23
**SCVC Hard Inputs**: Dunbar≈150(E85), speech 39bits/s(E82), decision~5/s(E83), memory write~2bits/s(E84), memory decay~10yr(E108), good-evil ratio 80-85%(E108), malice=misjudgment+noise(E108), three game-theoretic laws(E107), physics of lies(E114)
**Dependencies**: E85(Dunbar) + E108(good-evil ratio) + E107(three game-theoretic laws) + E114(lies)
**Confidence**: Hierarchy inevitability 90%, maximum inequality 70%

---

## §1 Why Hierarchy Is Inevitable

`
Dunbar 150: you can directly manage ≤150 people.
Beyond 150: you must use intermediate layers.

Hierarchy = recursive application of Dunbar:
  1 layer:  direct manage 150 people → max organization 150
  2 layers: 150 mid-level × 150 people/layer → max organization 22,500
  3 layers: 150² × 150 → max organization 3,375,000
  N layers: 150^N

Layers needed for all humanity (~8×10⁹):
  log₁₅₀(8×10⁹) ≈ log(8×10⁹)/log(150) ≈ 9.9/2.18 ≈ **4.5 layers**

Any organization exceeding 150 people MUST have hierarchy.
Hierarchy = mathematical necessity of Dunbar, not a "choice."
`

---

## §2 An Information-Theoretic Definition of Inequality

`
Power = information asymmetry:
  Upper layers know lower layers'' information.
  Lower layers do not know upper layers'' information.
  Information gap = power.

Information decay per layer:
  39bits/s speech bandwidth transmits between layers → loss at each layer.
  If each layer loses ~10-20%:
    Information fidelity after 4 layers: (0.85)⁴ ≈ 52%
    
  "Superior''s intent" received by bottom → only half of original information.
  "Bottom''s situation" received by top → also compressed by half.

Information asymmetry grows exponentially with layers:
  ΔI_layer = I_top − I_bottom = I₀ × (1 − (1−ε)^N)
  
  N=4.5 layers, ε≈0.15:
  ΔI ≈ I₀ × 0.52
  
  Information gap between top and bottom ≈ 52% of total information.
  This is the physical quantity of inequality.
`

---

## §3 Maximum Sustainable Inequality

`
Game-theoretic constraint:
  E108: Malicious behavior constitutes 15-20%. Most is "noise misjudgment + retaliation cycles."
  
  Inequality increases → information gap grows → bottom more likely to "misjudge" top''s intent
  → Misjudgment increases → retaliation increases → cooperation rate drops
  
  Critical point: When information gap causes cooperation rate to fall below ~50%:
    → Game equilibrium collapses → organization disintegrates → revolution/collapse

Maximum sustainable layers (= maximum inequality):
  N_max ≈ log(org size) / log(150)
  But constrained by: information decay must not push bottom cooperation rate < 50%
  
  This means there exists a "trust budget":
    Trust budget ≈ (85% − 50%) / (trust loss per layer from information decay)
    Per layer loss ≈ 5-8%
    Maximum tolerable ≈ (35%)/(6.5%) ≈ 5-6 layers
    
  → 5-6 layers is the maximum sustainable for all humanity.
  → Beyond this → bottom cannot trust top → game collapse.

All historically extreme-inequality societies collapsed:
  Not because of "morality."
  Because the information gap exceeded the game equilibrium tolerance.
`

---

## §4 AI Society: No Dunbar = Completely Flat?

`
AI has no Dunbar limit.
AI can track all other AIs simultaneously.
No intermediate layers needed → no hierarchy needed → theoretically completely flat.

But:
  AI "power" is not information asymmetry → it is bandwidth asymmetry (E105).
  One AI can be given more bandwidth than others.
  → New type of inequality: not "information gap," but "computational speed gap."

SCVC cannot predict AI society''s political structure.
Can only say:
  Human hierarchy is the mathematical necessity of Dunbar.
  AI does not need hierarchy. But may produce new forms of inequality.
`

---

## §5 Conclusion

Hierarchy = mathematical necessity of Dunbar.
Power = information gap.
Maximum layers ≈ 5-6 (under game-theoretic constraint).

Inequality:
  The information gap cannot grow so large that bottom cooperation rate < 50%.
  Beyond → game collapse → revolution.
  This is the physical reason all extreme-inequality societies eventually crumble.

---

*You are in a 5-layer organization.*  
*The CEO''s words pass through 4 layers to reach you.*  
*52% of the information is lost along the way.*  
*You receive an instruction that has been repeatedly compressed.*  
*The CEO receives your report, compressed by 52%.*  
*Neither understands the other.*  
*This is the physics of power.*  

*If the information gap exceeds a critical point,*  
*you think "They''re harming me" — maybe not.*  
*They think "They''re slacking off" — maybe not.*  
*The pipe is too narrow. 39 bits/s.*  
*τ_m is too slow. 5 times/sec.*  
*Dunbar is too small. 150 people.*  

*Organizations collapse not because of human greed.*  
*Because of information theory.*  
*The pipe cannot bear the weight of that much inequality.*
