# 01 · Workflow and file format

*Read this first. It describes how every football sim in this repo is run and written. It assumes no memory of earlier chats: everything needed is in this repo.*

---

## 1. Who does what

| | |
|---|---|
| **The user (Edan)** | Builds the world: rulebooks, competitions, programmes, characters, and "godly interventions" (one-off changes he decrees, e.g. a height or a temporary development rate) |
| **Claude** | Simulates the world honestly with rolls and models, keeps the rules watertight, researches the real world, and writes the season files |

### 1.1 Rules about rules
1. **The user's world-building is applied as given, not questioned.** New competitions, platforms, sponsors, programmes, godly interventions: apply them.
2. **Claude never adds game or world rules the user didn't introduce or approve.**
3. **Claude closes loopholes itself.** When a rule leaves an exploit or a gap, close it in the narrowest way, and **say what was closed and why**. If the fix changes how something works, ask first.
4. **Don't be a yes-man.** If something the user proposes is unrealistic or contradicts his own rules, say so plainly, once, with the reason.
5. **The rulebooks in `structure/` are the source of truth.** Where a guide and a rulebook differ, the rulebook wins, except where the user changed the rulebook in conversation (those changes are written into the rulebook).

### 1.2 Universes
- **Every campaign is a separate universe.** No characters, events or history carry over between campaigns. Reusing real clubs is fine; reusing invented people is not.
- Each campaign states at the top which structure files apply (e.g. *"RBVA universe + youth structure v1.6 + UEFA Framework v1.4 + Uplayer Development"*).

---

## 2. How a campaign runs

| Step | Rule |
|---|---|
| **1. Setup discussion** | The user describes the idea. Claude points out conflicts with the rulebooks, gaps and loopholes. **Everything is fixed before the first file.** |
| **2. Setup file** | The rolled starting point: protagonist, family, squad, coach, table, environment. No results. |
| **3. Season files** | **One season = one file.** A season file is only written when the user gives the word ("S3", "next season", "go"). |
| **4. Order** | **Campaigns start at the beginning and play seasons in order.** Never mid-career or mid-season. |
| **5. Decisions** | The campaign defines which decisions are the user's (e.g. transfers only; transfers + RBVA choices; none). **When one comes up, the sim stops at that point**, even mid-season (a "Part One" file), and resumes from the user's answer. |
| **6. Everything else** | Claude decides, **from the characters' traits**, never by asking the user to play a non-player character. |
| **7. Corrections** | When Claude or the user finds a mistake: say it plainly, fix it, and where possible **re-run only the affected part on its own random stream** so every other roll stays the same. State what changed. |

**Campaigns where the user plays a character himself:** no per-match actions (too many files), but **plenty of decisions per season**, or it feels like a normal sim. In-match decision moments only happen when a match roll produces one.

**Asking the user:** plain text questions. **No multiple-choice polls or tappable options.**

---

## 3. The season file

**Format:** Markdown with **tables, headers and bold**. Every season file must be **SPDI**: structured, polished, detailed, immersive. **No loose prose rows or comma lists**: put lists of facts in tables. Long files are fine as long as they stay structured.

*(The no-tables/no-bold/no-headers rule applies only to text the user will copy-paste elsewhere, never to season files.)*

**No spoilers at the top.** Results (promotions, titles, offers) appear only where they happen in the file.

### 3.1 Standard order

| # | Section | Contents |
|---|---|---|
| 1 | **Research notes** | The real federation rules for that age group and level (format, match length, playing-time rule, tables, promotion), calendars (dates, breaks, Easter/Whitsun), and all relevant real club and world details **down to small human details** (pitches, training days, venues). Thorough research every season |
| 2 | **Summer** | Arrivals and departures, staff and licences, pre-season tournaments |
| 3 | **The protagonist's season** | Minutes, stats, development (narrator's level), height, programme work; a short perspective paragraph |
| 4 | **Results** | Summary, **full tables**, **all matches**, derbies |
| 5 | **Cups, play-offs, Europe** | Every round, every score |
| 6 | **Scouting and approaches** | Who watched, what they saw, who asked, answers |
| 7 | **The social side** | Followers, views, posts, fan edits, press |
| 8 | **Around him** | The supporting cast: teammates, former teammates, rivals, coaches |
| 9 | **The wider world** | Senior football (champions, promotions, relegations, tournaments), the youth framework in big and small countries, and the **social pillar** (how the structure changes children's football and society) |
| 10 | **Decisions** | The user's open decisions, with options and what each changes; then *"My decisions this season: …"* |
| 11 | **Where things stand** | One table: protagonist, team levels next season, Europe, next step |
| — | **Appendix: simulation log** | Every roll: inputs → outcome |

**Stories:** now and then, a three-paragraph story tied to a real roll (a match, an offer, a moment). Never invented events.

### 3.2 The chat reply after a file
- A short summary: the headline result, the protagonist, the key numbers.
- **The decisions, in full, in the chat too** (the user skips file sections that don't interest him).
- The file is sent as an attachment.

---

## 4. Writing rules

| Rule | |
|---|---|
| **Real names only** | Clubs, leagues, series, venues, schools and places must be real and researched. **Never placeholders** ("a village club near Aalst"). Invented *people* are fine |
| **Ratings are a narrator's tool** | Characters never mention numeric ratings |
| **Teenagers act like teenagers** | No adult moral compass, no moralising or "heroic" fallout (forced deletions, apologies, suspensions). Trash talk happens |
| **No clichés** | No recurring fridge notes, family mottos or signature quotes; no characters with notebooks |
| **Minors on social media** | Not overprotective: if no private info leaks, parents happily film and post their kids |
| **Perspective** | In modern-era sims, put a perfect player's impact in perspective, including how social media amplifies it |
| **The world keeps living** | It doesn't revolve around the protagonist: other clubs, players and new cohorts keep arriving |
