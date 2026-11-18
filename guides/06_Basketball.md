# 06 · Basketball (US Basketball universe)

*Everything a basketball sim needs that the football guides and the rulebook don't cover. Read `01` to `05` first: workflow, file format, realism, rolls, social reach, the wider world and the meaning of "perfect" all carry over unchanged. This guide only covers what is different in basketball. **The rulebook is [`structure/basketball/US_Basketball_Club_System_Rulebook.md`](../structure/basketball/US_Basketball_Club_System_Rulebook.md) and takes precedence.***

---

## 1. The universe

| | |
|---|---|
| **Timetable** | Announced **18 February 2023** (All-Star weekend, Salt Lake City). **Full system in play from 2026/27** (rulebook Art. 55) |
| **Structuring** | Done once, from the announcement to **1 July 2026**: [`structure/basketball/US_Basketball_Structuring_2022-2026.md`](../structure/basketball/US_Basketball_Structuring_2022-2026.md). It settles the G League, the AAND, the academy grades, the 2025/26 youth season, the university clubs and California's tier 4. **Every 2026/27 campaign starts from it**; don't re-roll it. The script is in [`structure/basketball/scripts/`](../structure/basketball/scripts/) (seed 20230218) |
| **Real world** | Leagues, clubs, arenas, universities and senior results are real up to summer 2026. From 2026/27, senior seasons are rolled like football (`02_Realism.md`) |
| **Uplayer** | Football only. It doesn't exist in basketball universes |

## 2. Levels: the football mapping

The user's mapping. **The football level bases and bonuses (`03_Models.md`) carry over unchanged.**

| Belgian football | Basketball | Bonus over the base |
|---|---|---|
| Gewestelijk 1–3 | **Youth SD3 and SD2** (tier 4) | 0 |
| Provinciaal 1–3 | **Youth SD1** (tier 4) | +3 |
| Interprovinciaal | **AAND academies** (tier 3) | +6 |
| Elite 2 | **G League Academy League** | +10 |
| Elite 1 | **NBA Academy League** | +14 |

**Bases by age** (as in football): U12 30, U13 33, U14 37, U15 41, U16 44, U17 47, U18 50, U19 52.

**A youth team's level** = base + tier bonus + recruitment (local talent, brand) + academy grade (**Platinum +1.5, Gold +0.7, Silver 0**) + owner investment + noise. In 2025/26 only, U16 and older got −1.5, because those squads were put together in one summer.

## 3. Ratings

**An NBA 2K-style overall** is the basketball version of the FC26 scale: **absolute and realistic, one scale from an SD3 U12 to an NBA starter.** As in football, ratings are a narrator's tool and characters never mention them.

## 4. The game model (approved)

**Margin = 1.6 × level gap + 2 at home + noise (sd 11 points).** It replaces the football Poisson model.

- A 5-point level gap wins about 82% of the time.
- **Overtime** is part of the game (no draws in basketball).
- **Coaches** are rated on tactical intelligence and man management, as in football. **Their tactical modifier is added to the team's level** before the margin is rolled (`03_Models.md`, tactical integration and execution).
- **Knockout games:** one game, the higher seed at home, unless the competition says otherwise. In the **Youth Cup** the lower-tier club plays at home (as in the senior cup, Art. 15.3).

## 5. Youth league formats (2025/26 onwards)

Set by the NBA and USA Basketball in the structuring. Club games are at **weekends**, high school games on **weekdays** (Art. 22).

| League | Clubs | Format |
|---|---|---|
| **NBA Academy League** | 30 | East and West, 15 each. **U12–U14: 14 games** (single round robin). **U15–U19: 28 games** (home and away). Each conference's top two go to a **final four** |
| **G League Academy League** | 30 (14 East, 16 West) | The same |
| **AAND Academy League** | 9 in 2025/26, **64 from 2026/27** | 2025/26: one national table. **From 2026/27: four conferences of 16** (East, Midwest, South, West), with the format the NBA league uses |
| **State Youth Leagues** (tier 4) | Open | **Youth SD1, SD2 and SD3** from 2026/27 (Art. 17.2). Placement by each state, from applications and AAU records |
| **Youth promotion into the AAND Academy League** (Art. 17.4–17.13, user ruling, November 2026) | — | **Per age group:** top 2 of a Youth SD1 + the club holds the **full AAND Club Licence** + win the **regional youth play-off** (one per AAND conference). One up and one down per conference. **Possible without an AAND senior team.** The place follows the cohort; no promotion out of U19; the G League and NBA Academy Leagues stay closed; a promoted team plays under tier 1–3 rules (no pay-to-play, Arts. 24–25 movement, AAND training compensation) and the whole club is graded under Art. 9 |
| **National Basketball Youth Cup** | Tiers 1–3 | U14 and older. AAND academies first, then the G League, then the NBA (Art. 18) |
| **State Youth Cup** | Tier 4 | U14 and older. SD3 first, then SD2, then SD1 (Art. 19) |

## 6. Rulebook points settled with the user

| Topic | Ruling |
|---|---|
| **University clubs' B team** (Art. 64) | **A university club's NCAA team *is* its B team.** The first team plays in the pyramid; the second team (students outside the first-team squad) plays in the NCAA, in the university's old division. **There is no separate NCAA "A team"** |
| **Academy tryouts** (Art. 21) | **No open tryouts.** Pro academies scout, then invite. An invited trial is free (Art. 21 bans charging in tiers 1–3). **A boy who has never been seen gets in by playing in tier 4 and being seen there.** Approaches are rolled on what each club saw (`02_Realism.md`) |
| **Art. 6 shortfall** | When a division has fewer applicants than its minimum size, **adult clubs from the state's open registration fill the remaining places** (California SD1 2026/27: the San Diego Sharks and the San Diego Surf) |
| **The union** (Art. 56) | The union agreed in the **April 2023 CBA**; the roll set the timing. **The last NBA draft is in June 2027.** Art. 31 applies from summer 2027 |
| **Training compensation before 2026/27** | Tier 4 starts in 2026/27, so **academies paid nothing for AAU players they signed in 2025** (Art. 26 only covers tier 4 players) |
| **G League size** | Fixed at **30**. The Ignite's place went to the Rip City Remix (2024/25). Valley Suns never founded |
| **Practice courts** | **Almost every NBA club has one practice court, and the seniors use it.** Academies need their own courts: they build, rent or partner (see the structuring) |
| **Youth teams and the AAND** | **Ruled in November 2026:** a youth team **can** go up into the AAND Academy League on results while its senior team stays in tier 4, **if the club holds the AAND Club Licence**. Written into the rulebook as Art. 17.4–17.13, with the loopholes closed (licence timing and venue, cohort principle, closed NBA/G League leagues, pay-to-play, movement, grading) |
| **Minutes in youth basketball** | **No minimum-minutes rule** in the rulebook, unlike football's half-a-match rule. The coach and the model decide minutes |

## 7. Perfect basketball players

Everything in `04_Perfect_Players.md` §1 applies (decisions, execution, biomechanics, teammates, computer-like adaptation, physical development only, no rank between perfect players).

**Basketball specifics:**
- **Height matters more than in football.** Perfect biomechanics make up for a lot of size, but not everything: a guard contesting at the rim against someone 30 cm taller still loses some of those.
- **Perfect from day one:** a "born perfect" player has his rating from his first game (physical + (99 − physical) × 0.25), even if he has never played. The guarantee applies from his first game.
- **Free throws and open shots always go in**, at every position.

### 7.1 Guarantees by position

Claude's proposal from the setup discussion, apart from the user's own choice in the US Basketball campaign:

| Position | Guarantee |
|---|---|
| **Point guard** | **Never loses his minutes**: his team wins or ties the minutes he's on the court |
| **Shooting guard** | Never a blank quarter: a point or an assist in every quarter he plays at least half of |
| **Small forward** | Wins his matchup |
| **Power forward** | Wins the boards |
| **Centre** | The paint is closed |

**The US Basketball campaign:** the user's protagonist is a **shooting guard** ("the one who scores, the striker equivalent"), and the user gave him the guarantee **"never loses his minutes"**.

### 7.2 How "never loses his minutes" is modelled

Like the football midfielder's guarantee (`04_Perfect_Players.md` §3):
- **Each stint** he plays is rolled with the normal model.
- **If the minutes he played still come out negative**, the last stint is corrected to level.
- **A game he plays in full therefore can't be lost.** A tied game goes to overtime, and overtime is part of his minutes.
- **A game he doesn't play in full can be lost**, through the minutes he sat.
- The file reports how often the guarantee had to step in.

## 8. The US Basketball campaign (state at setup)

| | |
|---|---|
| **Protagonist** | A perfect **shooting guard**, **11** in 2026/27 (born 2015, **U12**), lives in **Inglewood**. **Has never played basketball** |
| **The user's decisions** | **Transfers only** |
| **First club** | He has no club in summer 2026. **His first club is a tier-4 club** (Youth SD3/SD2/SD1 around Inglewood), and that's the user's first transfer decision. Academies only come in through invitations after scouting |
| **First pro contract** | At 14 if officially measured at 6'3" or taller (twice, six months apart), otherwise at 16 (Arts. 32–33). Agents from six months before (Art. 35) |
| **High school** | From 14, if his club allows it (Art. 22). That's the user's decision |
| **Academies near Inglewood, 2026/27** | **Clippers** (NBA, Gold): Playa Vista, then their **Inglewood academy centre from December 2026**. **Lakers** (NBA, Gold): rented gyms in the South Bay. **Loyola Marymount** partner academy (AAND): Westchester, ~5 km. **No G League academy in LA** (the South Bay Lakers moved to the Coachella Valley; the San Diego Clippers are in Oceanside) |

## 9. The street model (US Basketball campaign, approved)

Rolled **once per season**. Each figure is the chance the event happens **at least once that season**, on a lower-income Inglewood block.

| Event | Age 11–12 | 13–14 | 15–17 |
|---|---|---|---|
| Hears gunfire nearby | 40% | 50% | 55% |
| Someone he knows is shot | 15% | 27% | 40% |
| "Where you from?" / pressure to claim | 4% | 30% | 50% |
| Robbed or jumped | 3% | 11% | 18% |
| Stopped by police | 2% | 15% | 35% |
| Joins a gang or starts claiming | 0.5% | 7% | 13% |
| Shot | 0.2% | 0.9% | 3.6% |

**Modifiers:**

| Factor | Effect |
|---|---|
| No curfew | **+10%** |
| A parent drives him | Robbery and claim pressure −30% (−15% if he takes the bus some days) |
| Father involved and a structured club schedule | Claiming −50% |
| Being known | Claim pressure −20%, robbery +50% |
| His own traits: hates the hood and plans his exit | Claiming −50% |
| His own traits: pre-mortem routes | Robbery −20% |
| Moving | Everything resets to the new area's level |

**It changes dynamically with his own choices:**
- A **provocative social media post** (disrespecting a set or an area, signs, a beef): that season, claim pressure ×1.5, robbery ×1.3, shot ×1.5.
- A **public beef that escalates**: ×2 on the same three.
- **Ordinary trash talk at basketball rivals** doesn't count.

**Consequences come only from the rolls.** No events are invented for the story, and nobody moralises. He reacts like the kid his age.

## 10. The protagonist's personality (the user's setting)

| Trait | Applies |
|---|---|
| **Struggles with sloth** | Off the court: homework, chores, skipped optional workouts (**−0.03 on his development rate**) |
| **IQ 126, hidden behind an act of about 80** | Off the court: teachers and adults underestimate him |
| **Very deceptive** | Off the court with adults and on the street. On the court it's part of perfect play anyway |
| **Decisive overthinker** | He runs every angle and worst case, sets a deadline, picks a path with an exit plan and adjusts in real time. **Off the court this shapes his choices** (routes, fallbacks, decisions under pressure) |
| **Hates the hood with all his soul** | Wants out. **Basketball is the way out** |
