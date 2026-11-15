# 03 · Models

*Every number in a season file comes from these models. All rolls use a seeded random generator (one seed per season; corrections re-run on their own seed so other rolls stay unchanged). Ratings are on the FC26-style scale.*

---

## 1. Development

### 1.1 The gain

> **Gain per month = (curve step for his age ÷ 9) × potential × rate + noise (sd ≈ 0.25)**

A season has nine development months (September–May). A season's gain is the sum of its months, so a change of rate (a transfer, a godly intervention) applies from the month it happens.

### 1.2 The normal curve

The share of potential a player reaches **at 1.00×**:

| Age | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 21 | 23–24 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Curve** | 45% | 50% | 55% | 61% | 67% | 72% | 77% | 82% | 86% | 90% | **92% (peak)** |

The **curve step** for a season is the difference between the curve at his age at the start of the season and at the next age (e.g. 14 → 15 = 6% of potential).

### 1.3 The rate multiplier

**1.00× = a player who doesn't train.** Without training, after a month the rate **falls 0.10 a month to a floor of 0.60**. When training resumes the rate returns at once to the environment's value; lost months stay lost.

**Environment (the base rate):**

| Environment | Rate |
|---|---|
| **Amateur club**, regular training | **1.05** minimum |
| + coach's licence | none +0.00 · UEFA C +0.01 · UEFA B +0.02 · UEFA A +0.03 |
| + written playing philosophy for every age group and level | +0.02 |
| + structured sessions (technical, physical and tactical blocks every session) | +0.02 |
| + sessions per week | 2: +0.00 · 3: +0.01 · 4: +0.02 |
| + facilities (synthetic pitch, small-sided pitches, proper equipment) | +0.01 |
| + Uplayer coaches co-coaching every session (KVK Ninove) | +0.02 |
| **Amateur cap** | **1.14** |
| **Professional academy (Elite 2 / Elite 1); RBVA C/D** | **1.15** |
| **Top academy or top first team (La Masia level); RBVA A/B** | **1.20** |

**Research each real club's setup** (sessions, licences, pitches, philosophy) from its website and social media; roll only what can't be found.

**Personal factors (added to the environment):**

| Factor | Effect |
|---|---|
| Starter (most of the season's minutes) | +0.05 |
| Playing up an age group | +0.08 |
| Work ethic (a stated trait) | +0.05 |
| Uplayer Development | +0.05, plus 0.03 × (his individual Sundays ÷ Sundays attended) |
| Overload (long daily commute, too many matches) | −0.05 |
| **Overall cap** | **1.35×** (only a godly intervention exceeds it) |

**Split schedules** (e.g. RBVA and a club): the environment is weighted by weeks.

### 1.4 The catch-up rule (late maturers only)

Only for players **rolled as late maturers** at creation (from height and growth curve). A boy behind his curve because he doesn't train or play gets nothing.

> **Catch-up per season = k × gap × rate**, where **gap = curve(age at season start) × potential − current level** (only when positive)

| Phase | k |
|---|---|
| Before the growth spurt | 0.10 |
| **Growth-spurt seasons** (timing rolled and sealed; usually two) | **0.30** |
| After the spurt, up to 21 | 0.15 |
| From 21 | 0 |

Catch-up only closes the gap, never lifts a player above his curve, and doesn't apply in a season whose rate is below 1.00×.

### 1.5 Perfect players and ageing

| | |
|---|---|
| **Perfect (99)** | Develops **physically only**. Every other attribute is already perfect |
| **Perfect from the start** (a "born perfect" child) | **Rating = physical + (99 − physical) × 0.25**: the mind is perfect, but the body still develops along the model |
| **Becomes perfect by development** | Perfect the moment his level reaches 99 |
| **Ageing (everyone)** | From **31**, the body declines **0.4 to 1.1 a year** (rolled). A perfect player's decisions, technique and execution stay perfect; only the physical part falls |

### 1.6 Height and growth

- **Adult height is projected at creation** (rolled from the parents and the boy's current height) and **sealed**. Doctors' estimates may be told as a range.
- **Peak height velocity (the spurt) is rolled and sealed**, typically at 12–14 for early maturers, 14–15 for late maturers.
- A godly intervention can fix any height or growth detail ("1.78 m by 16, no balance issues").
- Without "no balance issues", a fast-growing non-perfect player can roll a coordination dip during the spurt.

---

## 2. Teams and matches

### 2.1 Line-up and team strength

- **Line-up:** the best available players by **level + 0.25 × (tactical intelligence − the age norm)**, one goalkeeper plus the format's outfield number (5v5 → 4, 8v8 → 7, 11v11 → 10). The playing-time rule (half a match each) is applied over the squad.
- **Team strength:** average level of the line-up **+ coach effect + tactical modifier**:

> **strength = line-up average + (tactical rating − 50) / 10 × 0.7 + tactical modifier**

### 2.2 Tactical integration (how well the team knows its system)

Each team has **U** (understanding of its system, 0–100) and **C** (cohesion, 0–100).

> **ΔU per month = 0.06 × (100 − U) × method × age factor × (0.6 + coach tactical / 100) × 1.05 × TI factor × complexity**

| Term | Values |
|---|---|
| **Method** (how the system is taught) | Sessions built around the system in technical, physical and tactical blocks (VK Pollare): **1.35** · partly structured: **1.10** · only explained, like school: **0.85** |
| **Age factor** | 5v5 ages (≤ U8) 0.85 · ≤ U11 0.92 · ≤ U14 1.00 · older 1.05 |
| **TI factor** | (average tactical intelligence of the line-up ÷ age norm)^0.8, between 0.7 and 1.3 |
| **Complexity** | 5v5 1.2 · 8v8 1.0 · 11v11 0.75 |

> **ΔC per month = 4 × (0.5 + coach man management / 100)**, capped at 100

**Resets:** each summer U × 0.9; moving 5v5 → 8v8 × 0.8; 8v8 → 11v11 × 0.75; squad turnover × (1 − 0.6 × share of new players); new coach −15%.

**Tactical modifier:** **−2 + 5 × (0.6 U + 0.4 C) / 100** (from −2 to +3).

**Execution in a match:**

> **E = sigmoid((line-up average − opponent) / 8 + (U − 50) / 25 + (C − 50) / 40 + leaders − weakest link)**

- **Leaders:** sum of how far the two highest-TI players are above the age norm × 0.05.
- **Weakest link:** how far the lowest-TI player in the goalkeeper–defence–holding-midfield chain is below the norm, ÷ 20.
- Poor execution concedes extra chances against a press: + press × (1 − E) × 0.5 to the opponent's λ. **Press by level:** Gewestelijk 0.3 · Provinciaal 0.45 · IP 0.6 · Elite 2 0.75 · Elite 1 0.85 · foreign academies 0.9.

### 2.3 Goals

> **λ = 1.35 × exp(1.625 × tanh(strength gap / 25)) + 0.12 at home**

Goals are **Poisson(λ)** for each side. A team's own understanding also lowers the opponent's λ by × (1 − 0.15 U / 100).

### 2.4 Opponents

**Base level by age (Gewestelijk):**

| Age | U6 | U7 | U8 | U9 | U10 | U11 | U12 | U13 | U14 | U15 | U16 | U17 | U18 | U19 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Base** | 12 | 14 | 17 | 20 | 24 | 27 | 30 | 33 | 37 | 41 | 44 | 47 | 50 | 52 |

| Level | Bonus |
|---|---|
| Provinciaal | +3 |
| Interprovinciaal | +6 |
| Elite 2 | +10 |
| Elite 1 | +14 (professional academies weighted toward the top: about +1 to +2 for the biggest) |
| Professional academies in IP (U10–U12) | +13 |
| Renowned IP clubs (KVK Ninove, FCV Dender) | +3.5 |
| Foreign top academies | +12 to +14 |

Each opponent gets its base ± about 2.6 (rolled once a season) and grows through the season. **Opponent U and C:** Gewestelijk 40 · Provinciaal 50 · IP 58 · Elite 2 62 · Elite 1 66 (± 10) for U; 60 ± 10 for C.

### 2.5 Knockouts

| | |
|---|---|
| **Extra time** | λ ÷ 3 per side. **Up to U13, a draw goes straight to penalties**; from U14, extra time first |
| **Penalties** | Each kick scores 72–78% (senior 76–78%); sudden death after five |
| **Two-legged ties** | Aggregate; then extra time in the second leg; then penalties |

### 2.6 Goals and assists

Each goal is attributed to a scorer weighted by **level² × minutes share**, and in 55% of goals to an assister weighted the same way (midfielders' assist weight × 1.3; a perfect CM × 1.5).

---

## 3. Scouting and approaches (clubs)

> **P(club approaches a player) = club base × (matches the club saw him in) × (his level − the club's line) / 6**, capped at 0.9

- **Club base:** neighbouring amateur clubs 0.10–0.30 · IP clubs 0.25–0.35 · professional academies 0.05–0.35 depending on distance and how often they watch.
- **What they saw** counts double when the player beat them, kept a clean sheet against them or scored against them.
- **The answer** (stay/leave) is rolled from the family's situation, the level offered and the distance (a long commute or moving away weighs against).

**RBVA's own scouting** (four-point scale, Trial, the read formula with readability) is in `structure/rbva/RBVA_Universe_Merged_Annex_v1.1.md`.

---

## 4. Social media

> **Views = median for the account type × status × looks × log-normal noise (σ ≈ 0.8–1.0)**

| Account type | Median (youth, no status) |
|---|---|
| A parent's post | 300–900 |
| A small amateur club page | 1,000–2,500 |
| An IP/Elite club page, RBVA or Uplayer posts | 5,000–25,000 |
| A fan edit | 10,000–80,000 |
| A professional club's first-team account | 500,000+ |

| Multiplier | |
|---|---|
| **Status** | × 1 (amateur) · × 2–4 (IP/Elite, RBVA, youth internationals) · × 10+ (professional first team) · × 100+ (world stars) |
| **Looks (1–10)** | × 0.6 at 3 · × 1.0 at 5 · × 1.6 at 7 · × 2.5 at 9 · × 3 at 10. **Weighted heavier for content where skill isn't needed** (slideshows, photo dumps, snap branchés) |
| **Followers** | Log-normal around the year's expected growth; **never below last year's count** (accounts don't lose a big share of followers in a year) |

---

## 5. The world

| | |
|---|---|
| **Senior football** | Champions, promotions, relegations, the Champions League, the Euros and World Cups: weighted rolls every season, by the clubs' and nations' real standing, then carried forward |
| **National teams** | Youth and senior selection rolled on level, minutes and caps |
| **Awards** | Ballon d'Or and other awards: a score from level, trophies (Champions League, league, international tournament) and output, against about 30 rolled rivals |
| **Supporting cast** | Same development model, same approach and transfer rolls |
