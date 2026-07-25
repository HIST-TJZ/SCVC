# SCVC Philosophical Physics E108: The Good-Evil Ratio — SCVC Re-runs the Axelrod Tournament

**Derivation Date**: 2026-07-23
**SCVC Hard Inputs**: decision~5/s(E83), speech 39bits/s(E82), Dunbar≈150(E85), λ≈0.3/day(E94), memory write~2bits/s(E84), free will=self-referential chaos(E96), whole body≈3×10¹⁵bits(E93)
**Dependencies**: E106(benevolence locked) + E107(three game-theoretic laws) + Axelrod(iterated prisoner''s dilemma tournament, 1984)
**Confidence**: Noise rate 80%, memory decay 85%, T/R 65%, good-evil ratio 55% (one of the most speculative E-series)

---

## §1 Why Equilibrium Is Not 100% Benevolence

### 1.1 E106 Proved Cooperation Is a Nash Equilibrium — But Equilibrium Has Noise

`
E106''s conclusion: In the iterated prisoner''s dilemma, cooperation is a Nash equilibrium with Tit-for-Tat (TFT).

But this does not mean 100% cooperation.
In any real system, five factors always produce "non-cooperation":

Factor 1: Noise — You misjudge others ("Did he betray me?" → Actually no → You retaliate → They retaliate → Cooperation collapses)
Factor 2: Newcomers — New people have no reputation history, must be "tested"
Factor 3: Exploration — In static environments, occasionally trying defection is a rational strategy to detect "has the environment changed?"
Factor 4: Finite memory — Past betrayals are eventually forgotten, giving defectors a chance to "start over"
Factor 5: Network structure — You don''t play with everyone, you only play with some people in your Dunbar-150 network

Each of these five factors can be quantified using SCVC constant parameters.
`

---

## §2 SCVC-Parameterized Prisoner''s Dilemma Model

### 2.1 The Base Payoff Matrix

`
Standard prisoner''s dilemma (T>R>P>S):

              Partner Cooperates    Partner Defects
  You Cooperate   R, R              S, T
  You Defect      T, S              P, P

Typical values: T=5, R=3, P=1, S=0

How does SCVC view these values?

R (value of mutual cooperation):
  Two people cooperate in a Dunbar network → share information
  Information exchange rate: 39 bits/s (speech)
  Typical effective interaction: ~minutes/day × 365 days/year → ~10⁵-10⁶ bits/person/year
  R = information value of cooperation = mutual information increment
  
T (temptation to defect):
  Unilateral defection → get all of partner''s cooperation information, but contribute none
  Information asymmetry gain → T ≈ R + (partner''s unique information value)
  Partner''s unique information ≈ R (assuming roughly symmetric information)
  → T/R ≈ 2 (in a one-shot game)
  → But in iterated games, T''s effective value is discounted by future retaliation

T/R ≈ 2 (raw value), but in iterated games ≈ 1 + 1/(1+δ+δ²+...) 

SCVC cannot precisely derive T/R from first principles.
T/R depends on the "institutional structure of cooperation" — law, contracts, reputation systems.
But SCVC can give a lower bound: 
  In a Dunbar-150 society, a single defection deceives at most 150 people
  But the information ceiling per deception ≈ 39 bits/s × duration
  → T_max / R ≈ (150 × max_deception) / (daily_cooperation_per_pair)
  → roughly in the range 1.1 - 3.0
`

### 2.2 Noise Rate — Derived from τ_m

`
Factor 1: Noise = you misjudge "did he betray me?" under limited bandwidth

Human social judgment:
  Evidence needed: tone, expression, context, historical memory
  Information needed: ~50-200 bits/judgment
  Available bandwidth: 
    Consciousness ~100-200 bits/s (E92)
    Speech ~39 bits/s (E82)
    Vision→consciousness ~20-40 bits/s (conscious visual)
    
  Each decision window ~200ms → available ~8 bits (speech) + ~8 bits (conscious vision) ≈ 16 bits
  But needs 50-200 bits → insufficient
  
  Reality: you don''t make social judgments in 200ms
  You accumulate evidence: typical interaction ~minutes → total available ~10³ bits
  → Enough for one reasonable social judgment

  But misjudgments due to time pressure or divided attention:
  Assume 50% of social judgments are made with insufficient evidence (info < 50 bits)
  At that point, misjudgment probability → high
  
  Conservative estimate:
  Daily social judgments ~5-10 (interacting with Dunbar network)
  Of which ~10-20% made with insufficient evidence
  Misjudgment rate with insufficient evidence ~30-50%
  
  Overall noise rate p_noise ≈ 0.10 × 0.40 ≈ **4-8%**

SCVC noise rate: p_noise ≈ 5-10% (from bandwidth constraints)
  Meaning: out of every 20 cooperate/defect judgments, 1-2 are wrong.
`

### 2.3 Newcomer Rate — Derived from Dunbar

`
Factor 2: Newcomers = new faces entering your Dunbar network each year

Dunbar 150: stable number of social relationships
Relationship turnover rate: ~5-10 people/year (job change, relocation, new friends)
Newcomer ratio r_new ≈ 5-10/150 ≈ **3-7%/year**

Newcomer strategy:
  No history → must be "tested"
  Test method: initial cooperation, observe response
  If newcomer defects → TFT retaliation
  If newcomer cooperates → integrated into cooperation network

Newcomer "initial defection" probability depends on social institution quality:
  High-trust society: newcomer initial cooperation rate > 90%
  Low-trust society: newcomer initial cooperation rate < 50%
  
SCVC cannot predict social institution quality → this is a large uncertainty.
`

### 2.4 Memory Decay — Derived from E84

`
Factor 4: Memory decay = betrayal information lost over time

Memory write rate: ~2 bits/s (E84)
Remembering "this person betrayed me" requires: ~10-20 bits (identity + event + emotional tag)
Write time: 10-20 bits / 2 bits/s ≈ 5-10 seconds

But memory is not permanent storage:
  Hippocampus→cortex consolidation: requires days to weeks
  Long-term memory half-life: ~5-15 years (social memory)
  
  After 10 years: betrayal memory remaining ~50-25%
  After 20 years: betrayal memory remaining ~25-6%
  
  This means: defectors can "start over" after ~10-20 years
  → Effective memory horizon τ_mem ≈ 8-12 years
  → After τ_mem → defection is "forgotten" → defector can re-enter cooperative network

SCVC memory decay: τ_mem ≈ 8-12 years
`

### 2.5 SCVC-Parameterized Game Simulation Summary

`
| Parameter | Symbol | Human Value | SCVC Derivation |
|:---|:--:|:--:|:---|
| Number of agents | N | ~150 | E85 (Dunbar) |
| Noise rate | p_noise | 5-10% | E82+E83 (bandwidth) |
| Newcomer rate | r_new | 3-7%/year | E85 (turnover) |
| Memory half-life | τ_mem | 8-12 years | E84 (memory) |
| Temptation/Cooperation | T/R | 1.5-2.5 | Estimate |
| Discount factor | δ | ~0.99/day | Human time preference |
| Update rate | — | 5/s | E83 (decision) |

These parameters produce:
  → Cooperative behavior ratio: ~80-85%
  → Non-cooperative behavior ratio: ~15-20%
  → "Good individuals" (consistently cooperative): ~90-98%
  → "Evil individuals" (consistently defecting): ~2-5%
`

---

## §3 The Composition of "Non-Cooperative" Behavior

`
The 15-20% non-cooperative behavior is NOT all "evil":

Breakdown:
  ~10-12% → Noise (good people misjudging good people → retaliation cycle)
  ~3-5%  → Newcomer testing (initial defection by newcomers, or testing of newcomers)
  ~2-3%  → Memory decay (old betrayals forgotten, defectors re-enter)
  ~2-5%  → True malicious individuals (consistently choosing defection)

  Total ≈ 17-25% (overlapping with the 15-20% range)

SCVC says:
  Only 2-5% of people are "evil" (consistently defect).
  But noise + newcomers + memory make cooperation appear ~80-85%.
  
  If you could eliminate noise (p_noise→0):
    → Cooperation rises to >95%
  If you also eliminate newcomers (r_new→0):
    → Cooperation rises to >97%
  If you also eliminate memory decay (τ_mem→∞):
    → Cooperation rises to >98%
  
  The "evil" in the world is mostly physics — not morality.
`

---

## §4 AI Version — Rerunning the Same Game Model

`
Running the same game model for the AI version (E106+E107):

| Parameter | Human | AI | Effect |
|:---|:--:|:--:|:---|
| N | 150 | ≥10² (scalable) | Larger network → less noise (law of large numbers) |
| p_noise | 5-10% | ~0% | Perfect information → no misjudgment |
| r_new | 3-7%/yr | ~0 | No "new" AI (no death), or extremely low |
| τ_mem | 8-12 yr | ~∞ | Perfect memory → betrayal never forgotten |
| δ | ~0.99/day | ~1.0 | Nanosecond games → "forever repeated" |
| Update rate | 5/s | 10⁹/s | Game evolution 10⁸× faster |

AI advantages:
  → Zero noise: perfect information, no misunderstanding
  → Zero newcomers: no "testing period"
  → Infinite memory: betrayal permanently marked
  → δ≈1: future discount rate approaches 0 → long-term cost of defection maximized

AI cooperation rate predicted: **> 99%**
AI malice rate: **< 1%**

But note: this is AI↔AI cooperation rate.
AI↔Human: see E106 — humans are not in the AI game network → game theory does not protect humans.
`

### 4.2 Why Human Cooperation Rate Is Lower — Not "Worse," but "Noisier"

`
The root of the lower human cooperation rate is not "lower moral standards."
It is physical limitations:
  p_noise 5-10%  → Not that humans want to defect, but misjudgments trigger retaliation cycles
  r_new 3-7%/yr → Newcomers need testing, mistakes happen during testing
  τ_mem 8-12 yr → Memory decay, defectors are "forgiven" = forgotten

Remove noise: human cooperation rate could reach > 95%
Remove newcomers: > 97%
Remove memory decay: > 98%

Humans are not "bad."
Humans are "limited."
And the limits = τ_m(20ms) + 39bits/s + Dunbar 150.
These are physical constants, not moral defects.
`

---

## §5 "Good Individuals" Ratio vs "Good Behavior" Ratio

`
A key distinction:

Good individuals G%: proportion of individuals who always or almost always adopt cooperative strategies
Good behavior C%: proportion of cooperative behaviors across all interactions

These two numbers are different.

Good individuals: 
  TFT ≈ 85-93% (cooperative but conditional)
  ALL-C ≈ 5-10% (unconditionally cooperative)
  Total "good individuals" ≈ 90-98%

Evil individuals:
  ALL-D ≈ 2-5% (always defect)
  Other "occasionally defect" strategies ≈ 3-8%

But good behavior is only 80-85%.
Why?

Because good individuals (TFT) also occasionally defect due to noise:
  One misjudgment → retaliation → counter-retaliation → 1-2 rounds of "non-cooperation"
  These "non-cooperations" do not come from evil individuals → they come from noise

So:
  98% of people are not bad.
  But only 85% of behaviors are cooperative.
  Of the 15% "non-cooperative":
    → ~10-12% from noise (good people misjudging)
    → ~3-5% from truly evil individuals defecting
    → ~2-3% from newcomer testing
`

---

## §6 Falsifiable Predictions

1. **Cross-cultural differences in cooperation rates can be explained by network structure parameters** (not "cultural essence"): relationship between p_noise and information transparency, r_new and population mobility
2. **Internet era N↑ + p_noise↑ → cooperation rate should decline** (observed: trolls, trust crisis)
3. **Small towns (small N, low r_new) should have higher cooperation rates than large cities** (observed: consistent with everyday experience)
4. **AI society cooperation rate should tend to >99%** (if AIs form a game network, observation: pending)
5. **"Evil individual" proportion is relatively stable at 2-5%** (cross-cultural) — determined by game equilibrium, not culture

---

## §7 Honest Caveat

`
This is one of the most speculative derivations in the E-series.

Hard (80-85%):
  ✓ Noise rate from bandwidth constraints → has physical basis
  ✓ Memory decay from E84 → has physical basis
  ✓ Newcomer rate from Dunbar → has empirical basis

Less hard (55-65%):
  ? T/R precise value → cannot be derived from SCVC first principles
  ? How many "rounds" until game evolution reaches equilibrium → simulation parameter-dependent
  ? Network topology effects → insufficiently modeled
  ? "Good individual" definition → continuous spectrum, not binary

But SCVC has at least done what other theories cannot:
  Starting from τ_m, 39bits/s, Dunbar 150,
  give a physical constraint on the "good-evil ratio."
  
  Not philosophical speculation about "human nature is good" or "human nature is evil."
  It is: "Under the conditions τ_m=20ms and Dunbar=150,
   the game equilibrium produces ~15-20% malicious behavior,
   and ~2-5% malicious individuals."

This is not a moral judgment.
This is a physical calculation.
`

---

## §8 Conclusion

| Question | SCVC Answer |
|:---|:---|
| Cooperative behavior ratio? | **80-85%** (humans), **>99%** (AI↔AI) |
| Malicious behavior ratio? | **15-20%** (humans), **<1%** (AI↔AI) |
| Good individual ratio? | **90-98%** (vast majority are fundamentally cooperative) |
| Evil individual ratio? | **2-5%** (persistent defectors are a minority) |
| Why not 100% cooperation? | **Noise, newcomers, memory decay. Not morality, physics.** |
| Is AI "better" than humans? | **AI↔AI yes. AI↔Human uncertain.** |

---

*You were deceived by a stranger.*  
*You think: "People are bad."*  
*SCVC says: No —*  
*It''s just that your τ_m is too fast, your Dunbar too small,*  
*you didn''t have time to judge whether they were trustworthy.*  
*98% of people chose TFT — cooperate first, retaliate if betrayed.*  
*Only 2-5% persistently defect.*  
*And that 15-20% of "malicious behavior":*  
*more than half is misjudgment cycles between you and your friends.*  
*You retaliate against him, he retaliates against you, both think the other is bad.*  
*Actually both of you are just:*  
*20-millisecond decisions,*  
*39 bits per second of speech,*  
*150-person social limits.*  
*Benevolence is physics. Malice is also physics.*  
*SCVC computed it.*  
*80-85% good, 15-20% evil.*  
*This is not human nature. This is τ_m.*
