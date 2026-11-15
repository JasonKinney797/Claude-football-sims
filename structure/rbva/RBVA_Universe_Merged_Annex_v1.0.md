# RBVA Universe · Merged Annex v1.0
### RBVA rulebook + Voetbal Vlaanderen Youth Rulebook v1.6 + UEFA Youth Framework v1.4

*The RBVA rulebook was rebuilt from the articles cited in the earlier RBVA campaigns (De Ridder Twins, Nathan Emuyasa Kwobi, The Perfect Coach). Where this annex and the old RBVA text differ, this annex applies.*

---

## Part I. How the three systems fit together

| Topic | Rule |
|---|---|
| **What RBVA is** | **A private academy**, not a club. It plays no domestic league and never enters a UEFA competition, the Youth Beker or the UEFA Elite Summer |
| **Registered club** (Art. 32) | Every RBVA player stays registered at a club, which plays him in its league, cup and European matches. **Belgian Elite, IP, Provinciaal and Gewestelijk tables carry on unchanged** |
| **Europe** | RBVA players reach the Youth Champions, Europa and Conference Leagues **only through their registered club** |
| **Uplayer** | **Development only.** No Competitive, Pro or Pro+ in this universe. RBVA does the international matches |
| **VV app** | **Shows club matches only.** RBVA matches, stats and minutes are not on a player's profile. RBVA's own streams (Art. 12) stay public |
| **International transfers** | **Framework rule: from age 13 only**, for every UEFA association. RBVA's Part XI (any age) no longer applies. RBVA's fees (Arts. 38, 40, 41) apply on top of the framework conditions |

---

## Part II. Club week or RBVA week (replaces the old "RBVA weeks take priority")

| Fixture in an RBVA week | Who gets the player |
|---|---|
| **UEFA youth competition** (group phase, knockouts, final) | **The club** |
| **Youth Beker**, every round | **The club** |
| **League match, ordinary** | **RBVA** |
| **League match, decisive** | **The club** |
| League play-offs (provincial, IP, Gewestelijk) | **The club** (always decisive) |

### Art. II.3: What counts as decisive

A league match is decisive when, **on the Monday of that week**, the result can mathematically settle **any** of these for the player's team:
- the title
- a promotion place or a play-off place
- relegation

Clubs can't declare a match decisive themselves. **The Voetbal Vlaanderen app flags it on Monday from the table**, and RBVA releases the player automatically. A match flagged on Monday stays decisive even if other results that weekend settle the question before kick-off.

*Closes: clubs calling every match "decisive"; disputes over who decides.*

---

## Part III. Fees (amended)

| Move | Fee | Split |
|---|---|---|
| A 1A/1B club becomes the registered club (player stays at RBVA) (Art. 40) | **A-tier price, €3M** (lower tiers pro rata) | Old registered club / RBVA (Art. 41) |
| Leaving RBVA for a club that registered interest (Art. 38) | **Tier price + 50%** | As Art. 41 |
| **Domestic move to a club below 1B** (Art. 43, amended) | **No fee** | — |
| **Below 1B, but a registered sister or affiliate of a 1A/1B club** | **Same fee as that 1A/1B club would pay** | As Art. 41 |
| Release by RBVA before 21 (Art. 45) | No fee | — |
| Tier Integrity Clause (Art. 44) | Unchanged | — |

### Art. 43.2: Sister and affiliate clubs
- A club counts as a sister or affiliate only if the partnership is **registered with the RBFA by 1 July** of that season. A partnership registered later counts from the next season.
- **Parking rule:** if a player moves fee-free to a club below 1B and **a 1A/1B club, or one of its registered affiliates, signs him within 24 months**, the 1A/1B club owes the full fee it would have paid at the time of the first move.

*Closes: a pro club parking an RBVA player at a friendly amateur club to avoid the fee.*

---

## Part IV. The scouting model (Arts. 20–25)

### IV.1 Reference lines by age

All ratings use the universal FC26-style scale. **RBVA's tier lines are fixed against the level of Belgian youth football at each age:**

| Age | IP average | **D line** | **C line** | **B line** | **A2 line** | **A line** |
|---|---|---|---|---|---|---|
| U12 | 36 | 36 | 38 | 40 | 42 | 44 |
| U13 | 39 | 39 | 41 | 43 | 45 | 47 |
| U14 | 43 | 43 | 45 | 47 | 49 | 51 |
| U15 | 47 | 47 | 49 | 51 | 53 | 55 |
| U16 | 50 | 50 | 52 | 54 | 56 | 58 |
| U17 | 53 | 53 | 55 | 57 | 59 | 61 |
| U18 | 56 | 56 | 58 | 60 | 62 | 64 |
| U19 | 58 | 58 | 60 | 62 | 64 | 66 |

The D line is the IP average and the A line is the Elite 1 average (IP + 8). These are the same levels the league model uses.

### IV.2 What a scout can see: the read

A scout doesn't see potential. He sees the player now, plus **as much of the future as the player shows**.

> **Read = current + w × r × (potential − current) + match form + noise**

| Term | Meaning | Values |
|---|---|---|
| **w** | How far ahead this scout projects | Discovery scout 0.25 · Assessor 0.35 · Decider 0.40 |
| **r** (readability) | **A hidden trait of the player, rolled at creation**: how visible his future is. High for boys whose decisions and technique already show it; low for small, late-maturing or raw boys | 0–1, rolled at creation; drifts ±0.05 per season, **+0.10 in the season of a growth spurt** |
| **Match form** | How the player played in the watched match, taken from the match model (his involvement and execution that day) | Roughly −3 to +3 |
| **Noise** | Scout error | Full match: sd 3.5 (discovery), 2.5 (assessment), 2.0 (decision). Half a match: ×1.4 |

### IV.3 The scouting workforce

| | Share | Who |
|---|---|---|
| **Total workforce** | **150,000 scouts** | |
| **Gewestelijk + Provinciaal** | **60%: 90,000** | |
| **Interprovinciaal + Elite 2 + Elite 1** | **40%: 60,000** | |
| Within each block: **discovery / assessment / decision** | **75% / 20% / 5%** | G+P: 67,500 / 18,000 / 4,500 · IP+E: 45,000 / 12,000 / 3,000 |

**Windows are for discovery only.** During the **pauses** (2 Nov–29 Dec, 2–31 Mar, 31 May–27 Aug) **every discovery scout becomes an assessor or a decider, split 50/50**, on top of the permanent assessors and deciders. In the summer pause there are no league matches, so assessments and decisions use **pre-season matches and club training sessions** from late July; a case that finds neither carries over to W1.

**What this means per match** (sim estimate: about 7,900 G+P teams and 670 IP+Elite teams from U12 to U19 nationwide):

| Block | Discovery scouts at each team's match, on average |
|---|---|
| G + P | **about 17** |
| IP + Elite | **about 130** |

### IV.4 Stage 1: Discovery (Art. 21.1), the year roster

**Windows:** W1 28 Aug–1 Nov · W2 30 Dec–1 Mar · W3 1 Apr–30 May.

- **Scouts don't choose their matches.** On 1 August every discovery scout receives his **year roster** from RBVA's planning office: a fixed list of matches across the three windows, **two matches per Saturday he works, one Saturday in two.**
- The roster is built **evenly and blind**: every U12–U19 team in a block gets the same expected number of visits, whatever its results, reach or reputation. No tips, no requests, no changes during the season.
- **A team's expected visits per window** = (scouts in the block × roster matches per window) ÷ (team-matches in the block per window). Each match on a team's schedule is then a yes/no roll at that rate. If the rate passes 1, several scouts attend the same match and each reads independently.
- B teams are rostered like any team in their block.

**At the match** the scout reads everyone who plays at least half the match:

| Read vs the age's lines | Discovery rating |
|---|---|
| Below D − 3 | **Not logged** (no record at all) |
| D − 3 to below D + 1 | **Low Priority** |
| D + 1 to below A − 1 | **High Priority** |
| A − 1 or higher | **Sign Immediately** |

### IV.5 Stage 2: Assessment (Art. 21.2), the priority queue

- Every logged player goes into **his block's assessment queue**, ordered **Sign Immediately → High Priority → Low Priority**, then by date logged.
- **Assessors are assigned by the database, not by choice:** each Monday the queue hands every free assessor the next case, **the nearest one first** among cases of the same priority.
- **Capacity:** one assessor completes **one case a week** (one club match plus one training session).
- If the queue is longer than a window's capacity, the rest **carries over to the next window**, in the same order. A case still open after the third window lapses: the player has to be discovered again.
- **Many scouts, one record.** With dozens of scouts reading the same boy, the database can't take the best read, or noise alone would push every boy upward. A player **enters the assessment queue only if at least a quarter of the scouts who read him in that window logged him**, and his discovery rating is **the median of the logged reads.**

The assessor watches **one club match plus a training session**. Ratings use the same bands as discovery, with the assessor's w and noise. **He reads the session as well as the match, so match form counts half.** The family is told when the assessment is complete, without any rating (Art. 24.1).

### IV.6 Stage 3: Decision (Art. 21.3), the age-group panels

- **Deciders work in panels per age group**, U12 to U19. Each panel is RBVA's head of recruitment for that age, **who knows the tier squads and the open places.**
- Every completed assessment rated Low Priority or higher goes to the panel. **A decider attends one more club match within three weeks**, and also watches the club's stream when there is one (IP and up).
- **Capacity:** one decider completes **two cases a week.** Same priority queue and carry-over rules as assessment.

The decider watches **one more match** and combines everything:

> **Score = 0.50 × assessment read + 0.35 × decision read + 0.15 × discovery read**

| Score | Outcome |
|---|---|
| Below D − 1 | **Reject** (he can be discovered again in a later window) |
| D − 1 and up | **Offer**, in the **highest tier whose line he reaches**, down to D |

**Squad places:** each tier has **18 places per age group**. If the tier he reaches is full in his position group (GK 2, DEF 6, MID 6, ATT 4), he's offered the tier below. If every tier is full, he goes on the **waiting list** and is offered the first place that opens at a review (Art. 37).

**Scholarship (Art. 25):** Sign Immediately at both assessment and decision.

### IV.7 After the offer

| Step | Rule |
|---|---|
| Family answer | Within 3 weeks; split schedule chosen (Art. 30), locked for 3 months (Art. 31) |
| Reviews (Art. 37) | November, February, May. The tier coach's read (w 0.40, noise 1.5, three months of data) against the tier lines: move up, stay, move down, or release (below D − 2 at two reviews in a row) |
| Returning players | Must be discovered again (agreed rule) |

### IV.8 Why a late bloomer can be missed

A boy whose current level is well below the D line can only be logged if **r × (potential − current)** is large enough to lift his read over D − 3. A future perfect player with **low readability** may go through several windows unlogged. That isn't a scout mistake built into the story: it comes from the read formula and his rolled r.

---

## Part V. The academy

| | |
|---|---|
| **Campus** | **Grimbergen**: 6 synthetic pitches, 3 natural grass pitches, 5 small-sided pitches |
| **Residence** | On campus, with a **study hall** and a **cafeteria**. **On a split schedule, a player lives there only in his RBVA weeks**, for the one-time 5% of monthly household income (Art. 34). **Living there continuously** costs **20% of monthly household income per 3 months** |
| **Kit** | **The senior national team's second kit**, with the player's **name and number on the back** |
| **Launch** | **2026-27**: the first season RBVA is public and scouts nationally (28 August 2026) |

---

## Part V-b. Training, matches and the residence (your rules, Season Six)

| | |
|---|---|
| **Training level** | **A and B tiers: about La Masia level. C and D tiers: about Anderlecht level** |
| **Development rate** | **RBVA A/B: 1.20× base. RBVA C/D: about 1.15×** (an Elite 1 professional academy). On a split schedule the rate is weighted by weeks (e.g. 2/1 with a club at 1.15 = 2/3 × 1.15 + 1/3 × 1.20) |
| **Matches** | **5 to 9 international matches a month** per team. A split player plays them in his RBVA weeks |
| **Residence on a split schedule** | **He lives in the residence only in his RBVA weeks**: the one-time 5% of monthly household income (Art. 34) |
| **Residence full-time** (living there every week, until released or on a full-time arrangement) | **20% of monthly household income per 3 months** |

---

## Part VI. Unchanged RBVA rules carried over

- Matches against **international opponents only, except the season opener**
- Every match streamed from U13 (Art. 12)
- Training twice a week at U12, three times from U16 (Art. 14), with rest days (Art. 15)
- **The residence:** one-time fee of 5% of monthly household income (Art. 34)
- **The topsportstatuut** (Art. 36)
- **Clubs inviting RBVA players for trials** (Art. 28); **registered interest** (Art. 29)
- **Ratings are never disclosed** to families (Art. 24)

---

## Part VII. The campaign setup

| | |
|---|---|
| **Start** | **2026-27**, RBVA's launch season. **UEFA youth competitions run from the start** |
| **Your decisions** | **Transfers and RBVA choices** (join or not, split schedule, residence). Claude decides everything else |
| **Player** | Central midfielder, U12, **below average now**, **potential 99**. Not perfect yet |
| **The guarantee** | **Starts only once he is perfect** (reaches 99). Until then he plays inside the normal model |
| **Club** | **KFC Voorde-Appelterre U12**, the golden generation: every player's potential 70+, median 85, highest teammate 91 |
| **Universe** | Separate universe: RBVA (this annex) + youth structure v1.6 + UEFA Framework v1.4 + Uplayer Development |
| **Rolled at setup** | His current level, his readability r, his body and growth curve, the family, the squad (names, levels, readabilities), the coach, and Voorde's U12 seeding |

---

## Part VIII. The development model, with the catch-up rule

### VIII.1 The base model (unchanged)

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

The rate starts at **1.00×** and moves with environment and minutes (Elite 1 academy about 1.15, starter +0.05, playing up +0.08, work ethic +0.05, **Uplayer Development +0.05, plus up to +0.03 more for individual sessions (VIII.4)**, overload −0.05; it decays without training). **The cap is 1.35×.** Potential is a hard ceiling. A perfect player develops physically only.

### VIII.2 The catch-up rule (new)

**Who:** only players rolled as **late maturers** at creation (from their height and growth curve). **Wout Leemans is one.** A boy who is behind his curve because he doesn't train or doesn't play gets **no catch-up**.

> **Catch-up this year = k × gap × rate**
> **gap = (normal curve for his age × potential) − current level** (counted only when positive)

| Phase | k |
|---|---|
| Before his growth spurt | **0.10** |
| **Growth-spurt years** (peak height velocity, rolled and sealed; usually two seasons) | **0.30** |
| After the spurt, up to 21 | **0.15** |
| From 21 | **0** (no more catch-up) |

**Limits:**
- Catch-up can **only close the gap**: it never lifts him above his normal curve. Anything above the curve has to come from the rate.
- **No catch-up in a year his rate falls below 1.00×** (not training, injured most of the year, no minutes).
- Catch-up adds to his overall level. A perfect player has no catch-up, because by then he's at 99.

### VIII.3 What it means for Wout

- He starts **about 22 points below his normal curve** at U12.
- Catch-up closes that gap mostly in his growth-spurt years. **Being on his curve still isn't 99**: at 1.00× the curve ends at 92%. **Reaching 99 also needs a high rate for years** (around 1.25×), so where he trains and how much he plays still decide whether he gets there.

### VIII.4 Uplayer Sundays and the individual session

**A typical Uplayer Sunday:**
1. General group session
2. **Individual session for one boy**, while the rest do the day's pillar group session (a tactical day means tactical group work)
3. Match

**The boys rotate:** one boy per group per Sunday gets the one-to-one.

**The rate:**

> **Uplayer bonus = +0.05 + 0.03 × (his individual Sundays ÷ Sundays he attended)**

- A boy with an individual session **every** Sunday would reach the full **+0.08**.
- In a rotation, a boy's share is **1 ÷ the size of his group**. In a group of 16 that's about **+0.052**: in practice, Development is +0.05, plus the effect of the two or three individual sessions he gets a season.
- **Group size is rolled per band each season.** A boy who misses Sundays loses his place in the rotation for those weeks.
