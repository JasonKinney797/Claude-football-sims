# RBVA Universe · Merged Annex v1.1
### How the RBVA Rulebook fits the Voetbal Vlaanderen Youth Rulebook v1.6 and the UEFA Youth Framework v1.4, and the models used to simulate it

*The **RBVA Rulebook** (`structure/rbva/RBVA_Rulebook.md`) is the source of every RBVA rule. **Where this annex and the rulebook differ, the rulebook applies.** This annex only covers what the rulebook doesn't: how RBVA sits next to the club structure, and the simulation models.*

---

## Part I. How the systems fit together

| Topic | Rule |
|---|---|
| **What RBVA is** | **A private academy**, not a club. It plays no domestic league and never enters a UEFA competition, the Youth Beker or the UEFA Elite Summer |
| **Registered club** (Art. 32) | Every RBVA player on a split schedule stays registered at a club, which plays him in its league, cup and European matches. **Belgian Elite, IP, Provinciaal and Gewestelijk tables carry on unchanged** |
| **Europe** | RBVA players reach the Youth Champions, Europa and Conference Leagues **only through their registered club** |
| **Uplayer** | **Development only.** No Competitive, Pro or Pro+ in RBVA universes. RBVA does the international matches |
| **VV app** | **Shows club matches only.** RBVA matches, stats and minutes are not on a player's profile. RBVA's own streams (Art. 12) stay public |
| **International transfers** | **UEFA Framework rule: from age 13**, for every UEFA association (instead of RBVA Part XI's "any age"). RBVA's fees (Arts. 38, 40, 41) apply on top |
| **Opponents** | International only (Art. 9), **except the season opener** |

---

## Part II. Club week or RBVA week

| Fixture in an RBVA week | Who gets the player |
|---|---|
| **UEFA youth competition** (group phase, knockouts, final) | **The club** |
| **Youth Beker**, every round | **The club** |
| **League match, ordinary** | **RBVA** |
| **League match, decisive** | **The club** |
| League play-offs (provincial, IP, Gewestelijk) | **The club** (always decisive) |

### II.1 What counts as decisive

A league match is decisive when, **on the Monday of that week**, the result can mathematically settle **any** of these for the player's team:
- the title
- a promotion place or a play-off place
- relegation

Clubs can't declare a match decisive themselves. **The Voetbal Vlaanderen app flags it on Monday from the table**, and RBVA releases the player automatically. A match flagged on Monday stays decisive even if other results that weekend settle the question before kick-off.

---

## Part III. Fees

**All fees follow the rulebook (Arts. 38–46)**, including Article 43 as amended: **no fee for a domestic move below 1B, unless the club is a sister or affiliate of a 1A/1B club.**

**Sister and affiliate clubs (clarification of Art. 43):**
- A club counts as a sister or affiliate only if the partnership is **registered with the RBFA by 1 July** of that season. A partnership registered later counts from the next season.
- **Parking:** if a player moves fee-free to a club below 1B and **a 1A/1B club, or one of its registered affiliates, signs him within 24 months**, that club owes the fee it would have paid at the time of the first move.

---

## Part IV. The scouting model (Arts. 17–25)

### IV.1 Reference lines by age

All ratings use the universal FC26-style scale. **The lines are fixed against the level of Belgian youth football at each age.** They are the model's reference for the four-point scale and for tier placement:

| Age | **D line** (IP average) | **C** | **B** | **A** (Elite 1 average) |
|---|---|---|---|---|
| U12 | 36 | 38.5 | 41 | 44 |
| U13 | 39 | 41.5 | 44 | 47 |
| U14 | 43 | 45.5 | 48 | 51 |
| U15 | 47 | 49.5 | 52 | 55 |
| U16 | 50 | 52.5 | 55 | 58 |
| U17 | 53 | 55.5 | 58 | 61 |
| U18 | 56 | 58.5 | 61 | 64 |
| U19 | 58 | 60.5 | 63 | 66 |

### IV.2 What a scout can see: the read

A scout doesn't see potential. He sees the player now, plus **as much of the future as the player shows**.

> **Read = current + w × r × (potential − current) + match form + noise**

| Term | Meaning | Values |
|---|---|---|
| **w** | How far ahead this scout projects | Discovery 0.25 · Assessment 0.35 · Decision 0.40 |
| **r** (readability) | **A hidden trait, rolled at creation**: how visible a player's future is. High for boys whose decisions and technique already show it; low for small, late-maturing or raw boys | 0–1; drifts ±0.05 a season; **+0.10 in a growth-spurt season** |
| **Match form** | How he played in the watched match (from the match model) | Roughly −3 to +3 |
| **Noise** | Scout error | Full match: sd 3.5 (discovery), 2.5 (assessment), 2.0 (decision). Half a match: ×1.4 |

### IV.3 The workforce (Arts. 17–19)

| | Discovery (30%) | Assessment (30%) | Decision (40%) |
|---|---|---|---|
| **Gewestelijk + Provinciaal** (60% of 10,000) | 1,800 | 1,800 | 2,400 |
| **IP + Elite 2 + Elite 1** (40%) | 1,200 | 1,200 | 1,600 |
| **International** (1,000) | 300 | 300 | 400 |

**Discovery scouts work in the windows only** (Art. 20). Assessors and deciders work year-round.

### IV.4 Stage 1: Discovery, the year roster

- **Scouts don't choose their matches.** On 1 August every discovery scout receives a **year roster**: a fixed list of matches across the three windows, **four matches a week** (two on Saturday, two on Sunday).
- The roster is built **evenly and blind**: every U12–U19 team in a block gets the same expected number of visits, whatever its results, reach or reputation.
- **Visits per team-match** = (discovery scouts in the block × roster matches per window × 2 teams) ÷ (team-matches in the block per window). Each match is then rolled at that rate.
- **What it means** (sim estimate: about 7,900 G+P teams and 670 IP+Elite teams from U12 to U19): **about 1.8 scouts at an average Gewestelijk or Provinciaal match, about 14 at an average IP or Elite match.**

The scout reads everyone who plays at least half the match and rates him on the four-point scale (Art. 21.1):

| Read vs the age's lines | Discovery rating |
|---|---|
| Below D − 3 | **Not logged** (no record at all) |
| D − 3 to below D | **Low Priority** |
| D to below D + 3 | **Moderate Priority** |
| D + 3 to below A − 1 | **High Priority** |
| A − 1 or higher | **Sign Immediately** |

**More than one scout, one record:** when several scouts read the same boy in a window, he enters the assessment queue if at least a quarter of them logged him, and his rating is **the median of the logged reads**.

### IV.5 Stage 2: Assessment (Art. 21.2)

- Cases are handled in order **Sign Immediately → High → Moderate → Low**, nearest first within a priority.
- The assessor attends **the player's following fixtures** (the model: one club match plus one training session) and rates him on the same four-point scale, with the assessor's w and noise; match form counts half.
- **Every case is resolved within the same season, ideally within a month** (Art. 22). Parents and the club are told when the assessment is complete, without the rating (Art. 24.1).

### IV.6 Stage 3: Decision (Art. 21.3)

The decider attends **the next fixtures**, knowing the discovery and assessment ratings:

> **Score = 0.50 × assessment read + 0.35 × decision read + 0.15 × discovery read**

| Score | Decision |
|---|---|
| A − 1 or higher | **Sign Immediately** |
| D − 1 to below A − 1 | **Trial**: the player trains with RBVA for three sessions; **the trial coach's read** (w 0.40, noise 1.5) **at the D line or above signs him**, below it is a reject |
| Below D − 1 | **Reject** (he can be discovered again in a later window) |

- **No places limit.** Tiers add sub-teams when they fill up (Art. 7), so every signed player gets a place.
- **Tier placement:** the highest tier whose line his score reaches (A, B, C, D), then the **Promotion Index** (Art. 37) moves him during the season. A player can be released after three months of data.
- **Scholarship** (Art. 25): Sign Immediately at both assessment and decision means a **residential scholarship**.
- **Notification** of the final decision to parents and the club (Art. 24.2).

### IV.7 Why a late bloomer can be missed

A boy whose current level is well below the D line can only be logged if **r × (potential − current)** lifts his read over D − 3. A future perfect player with **low readability** may go through several windows unlogged. That comes from the read formula and his rolled r, not from the story.

---

## Part V. The academy

| | |
|---|---|
| **Campus** | **Grimbergen** (Art. 2: in or near Brussels): 6 synthetic pitches, 3 natural grass pitches, 5 small-sided pitches |
| **Residence and study hall** | As Arts. 33–35 |
| **Kit** | **The senior national team's second kit**, with the player's **name and number on the back** |
| **Launch** | **2026-27**: the first season RBVA is public and scouts nationally (28 August 2026) |

---

## Part VI. Simulation models

### VI.1 RBVA training

| | |
|---|---|
| **Training level** | **A and B tiers: about La Masia level. C and D tiers: about Anderlecht level** |
| **Development rate** | **A/B: 1.20× base. C/D: about 1.15×.** On a split schedule the rate is weighted by weeks |
| **Match frequency** | 5 to 9 a month per team (Art. 10). A split player plays them in his RBVA weeks |

### VI.2 The development model

> **Gain this year = (curve step for his age) × potential × rate + noise**

| Age | Normal curve (share of potential at 1.00×) |
|---|---|
| 11 | 45% |
| 12 | 50% |
| 13 | 55% |
| 14 | 61% |
| 15 | 67% |
| 16 | 72% |
| 17 | 77% |
| 18 | 82% |
| 19 | 86% |
| 21 | 90% |
| 23–24 (peak) | 92% |

The rate starts at **1.00×** and moves with environment and minutes (Elite 1 academy about 1.15, starter +0.05, playing up +0.08, work ethic +0.05, **Uplayer Development +0.05, plus up to +0.03 for individual sessions (VI.4)**, overload −0.05; it decays without training). **The cap is 1.35×.** Potential is a hard ceiling. A perfect player develops physically only.

### VI.3 The catch-up rule

**Who:** only players rolled as **late maturers** at creation (from their height and growth curve). A boy who is behind his curve because he doesn't train or doesn't play gets **no catch-up**.

> **Catch-up this year = k × gap × rate**
> **gap = (normal curve for his age × potential) − current level** (only when positive)

| Phase | k |
|---|---|
| Before his growth spurt | **0.10** |
| **Growth-spurt years** (rolled and sealed; usually two seasons) | **0.30** |
| After the spurt, up to 21 | **0.15** |
| From 21 | **0** |

**Limits:** catch-up only closes the gap, never lifts a player above his curve; **no catch-up in a year his rate falls below 1.00×**.

### VI.4 Uplayer Sundays and the individual session

1. General group session
2. **Individual session for one boy**, while the rest do the day's pillar group session
3. Match

**The boys rotate**, one per group per Sunday.

> **Uplayer bonus = +0.05 + 0.03 × (his individual Sundays ÷ Sundays he attended)**

Group size is rolled per band each season. A boy who misses Sundays loses his place in the rotation for those weeks.
