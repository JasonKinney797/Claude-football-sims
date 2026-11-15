# 04 · Perfect players

*A "mathematically perfect" player or coach is a recurring campaign type. These rules apply in every campaign that has one.*

---

## 1. What perfect means

| | |
|---|---|
| **On the pitch** | Perfect **decisions, technique, execution and biomechanics** (perfect control of the body: leverage, timing, shielding, movement) |
| **Like a computer** | The instant a new input appears (an opponent's new counter-strategy), the optimal counter is produced. No "realising it after a few weeks" |
| **Teammates** | He knows every teammate's strengths, weaknesses, exact level and **sealed potential** by heart, and designs the play around them. **He never plays a pass a teammate can't use** (input → output) |
| **Team impact** | **Don't underestimate it** |
| **Size** | A small or late-maturing perfect player isn't weak: perfect biomechanics largely neutralise size in duels |
| **Off the pitch** | **Perfect only in football.** Outside football he decides like an ordinary kid his age (social media use depends on house rules, peers, etc.) |
| **Development** | Physical only (`03_Models.md` §1.5) |
| **Rank** | **Perfection has no rank.** Two perfect players are equals with different roles; when they face each other, **their guarantees cancel out** and the result depends on their teammates' execution |

## 2. The guarantees, by position

| Position | Guarantee |
|---|---|
| **Attacker** | **Never a blank**: at least one goal or assist in every match he plays. If opponents keep the ball away from him, his output adapts rather than failing |
| **Central midfielder** | **His team never loses a match he plays in full** (draws allowed). It applies **everywhere**, including festivals without standings |
| **Centre-back / defender** | **A clean sheet while he's on the pitch.** He commands the line and his teammates; if opponents avoid his side he changes position. Only a **very rare, uncoverable goal** is allowed, and it must be explained. No recurring excuses |
| **Full-back** | **The clean sheet is his only guarantee**: no attacking guarantee |
| **Goalkeeper** | **A clean sheet every match.** Perfect positioning and organisation prevent the shots he couldn't reach. No deflections or own goals as recurring excuses |
| **Coach** | Not a guarantee but a standard: **he never waits for half-time** (any change is made the instant it's needed, e.g. the 5th minute); he has perfect player vision, so he is also a perfect scout; **after every draw or defeat the model produces, check whether a perfect coach could have prevented it** and don't explain his limits by appealing to authority ("bigger clubs") |

**Reporting:** a perfect defender's file reports duels (dribblers tackled %, aerial duels won %, ground duels won %) and territory (interceptions, recoveries, clearances, blocks). A perfect midfielder without an attacking guarantee gets full midfield stats.

## 3. How the central midfielder's guarantee is modelled

The match is played in **four phases**:

| Score during the phase | His team's λ | Opponent's λ |
|---|---|---|
| **Behind** | × 1.5 | × 1.15 |
| **Level** | × 1.0 | × 1.0 |
| **Ahead** | × 0.85 | × 0.6 |

- **If his team is still behind at the end, he equalises.** The file reports how often the guarantee had to equalise.
- **Two-legged ties:** each leg is guaranteed; extra time is part of the match.
- **Shoot-outs are outside the guarantee.** His own penalty always scores.
- **Not in full** (substituted, came on, sent off): no guarantee for that match.

## 4. When the guarantee starts

**At perfection.** A player who has the *potential* to be perfect only gets his guarantee **the day his level reaches 99**. Before that he plays inside the normal model.

## 5. Basketball

Basketball guarantees and how they're modelled: `06_Basketball.md` §7.
