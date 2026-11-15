# The American Basketball Club System
### Structuring · From the announcement (2022/23) to summer 2026 · US Basketball universe

*A separate universe. The leagues, clubs, arenas, universities and senior results are real up to summer 2026. Only the rulebook, how everyone reacts to it, and the youth system it creates are fictional. Everything below the research notes was rolled (seed 20230218). The structuring stops on 1 July 2026, the day the 2026/27 divisions are published.*

---

## 1. Research notes

| Topic | Details used |
|---|---|
| **The practice-court problem** | Almost every NBA club has **one practice court, and it belongs to the senior team**. An academy runs U12–U19 A teams plus women's teams from U16, which comes to **at least eleven teams** needing a court four or five evenings a week. **None of them fit in the senior building.** Every club has to build, rent or partner |
| **Lakers** | **UCLA Health Training Center, El Segundo** (opened 2017): the Lakers' practice facility and the South Bay Lakers' home court, **750 seats** |
| **Clippers** | **Intuit Dome, Inglewood** (3930 West Century Blvd, opened 15 August 2024, 18,000 seats). The Clippers **moved all operations there in 2024**, including an 85,000 sq ft practice facility, and the campus has public outdoor courts. The old training centre in **Playa Vista** has **two regulation courts** and was left empty |
| **G League, 2022/23** | **30 clubs**: 27 owned by their NBA parent, **3 hybrids** (Grand Rapids Gold, Rio Grande Valley Vipers, Texas Legends) with independent owners and one NBA affiliate each, the independent **Mexico City Capitanes**, and the NBA-run **G League Ignite**. **Portland and Phoenix** had no affiliate |
| **G League venues under 4,000** (the G League licence needs 4,000) | South Bay Lakers 750, Delaware Blue Coats 2,500, Greensboro Swarm 2,500, Santa Cruz Warriors 2,505, Motor City Cruise 3,000, Maine Celtics 3,100, Sioux Falls Skyforce 3,250, College Park Skyhawks 3,500, Wisconsin Herd 3,500 |
| **Real G League moves kept** | Ignite folds after 2023/24. Lakeland Magic → **Osceola Magic** (Kissimmee, 2024). Ontario Clippers → **San Diego Clippers** (Frontwave Arena, Oceanside, 7,500; 2024). Fort Wayne Mad Ants → Indiana Mad Ants (2023) → **Noblesville Boom** (2025). Birmingham Squadron → **Laketown Squadron** (Pontchartrain Center, Kenner, 4,600; 2026) |
| **Outside the NBA family** | **Overtime Elite**, Atlanta: players aged 16–20; the **OTE Arena** at Atlantic Station seats **1,200** on its showcase court, with two smaller courts. **The Basketball League (TBL)** is semi-professional: small venues and travel paid by the clubs. The **ABA** is a step below |
| **Senior results** (real; nothing in the rulebook touches senior play before 2026/27) | NBA champions: **Denver 2023, Boston 2024, Oklahoma City 2025, New York Knicks 2026** (4–1 over the Spurs, Brunson Finals MVP). G League: **Delaware 2023, OKC Blue 2024, Stockton 2025, Greensboro 2026**. NCAA: **UConn 2023 and 2024, Florida 2025, Michigan 2026** (over UConn) |
| **Before tier 4 exists** | Tier 4 starts in 2026/27. So when the academies recruited from AAU programmes in 2025, **there was no training compensation to pay** (Art. 26 only covers tier 4 players) |

---

## 2. Models used

| Model | How it works |
|---|---|
| **Youth team level** (narrator) | The football bases carry over: U12 30, U13 33, U14 37, U15 41, U16 44, U17 47, U18 50, U19 52. **Tier bonus, using your mapping**: NBA academy league +14 (Elite 1), G League academy league +10 (Elite 2), AAND academies +6 (IP). Plus how well the club recruits (local talent, brand), its academy grade (Platinum +1.5, Gold +0.7), the owner's investment, and noise. **U16 and older −1.5 in 2025/26**, because those squads were put together in a single summer |
| **Game result** (new, basketball) | **Margin = 1.6 × level gap + 2 at home + noise (sd 11 points).** A 5-point level gap wins about 82% of the time. Replaces the football Poisson model for basketball. Approved; in `guides/06_Basketball.md` |
| **Clubs' choices** (affiliation, venues, facilities, applications) | Weighted rolls on what each club can afford and what's realistically on offer locally |
| **Academy grade** | Facilities (centre open / under construction / rented) + owner investment + coaching and medical + education, rolled. Platinum / Gold / Silver |
| **AAND placement** (Art. 58) | Each conference takes its **16 strongest licensed clubs**. Licensed clubs that don't fit go to SD1 |

---

## 3. 2022/23: the announcement

**Saturday 18 February 2023, All-Star weekend in Salt Lake City.** The NBA and USA Basketball present the rulebook at the commissioner's annual All-Star press conference: one pyramid, no draft, academies from U12, relegation from the NBA "once the system is stable", and the full system in play **from 2026/27**.

### 3.1 The union (Art. 56)

The players' union agrees to the rulebook in the **2023 CBA (April 2023)**. The academy contracts at 14 and 16 and the end of the draft are both in it. **The rolled date for the end of the draft: the last NBA draft is in June 2027.** The 2026 draft goes ahead as normal, the 2027 draft is the last one, and Article 31 applies from summer 2027.

### 3.2 The G League chooses (affiliation or independence)

An independent G League club can be promoted, eventually all the way to the NBA. An affiliate never can (Art. 12.4). **Only the three hybrids had a real choice**, because the other 27 are owned outright by their NBA parent.

| Club | Owner | Choice | What it means |
|---|---|---|---|
| **Rio Grande Valley Vipers** (Edinburg, TX) | Independent group | **INDEPENDENT** | The Rockets lose their affiliate. Bert Ogden Arena holds 9,000, so the Vipers already meet the licence |
| **Texas Legends** (Frisco, TX) | Independent group | **INDEPENDENT** | The Mavericks lose their affiliate, in their own metro area |
| Grand Rapids Gold (MI) | Independent group | **Affiliate** (Denver) | Stays with the Nuggets |
| Mexico City Capitanes | Independent | Independent | No change |
| G League Ignite | The NBA | **Folds after 2023/24** | With academies from U12 and the draft ending, it has no purpose left |

Existing affiliation contracts run until **summer 2026**, so senior seasons are unchanged until then.

**The Ignite's place.** The Board keeps the G League at **30** and gives the Ignite's place to one NBA club without an affiliate. **Rolled: Portland.** The **Rip City Remix** start in **2024/25** at the **Chiles Center** (4,852). That leaves **the Mavericks, the Rockets and the Suns without an affiliate in 2026/27.** For now they develop seniors in their U19 teams and through loans from 17 (Art. 30). The Valley Suns are never founded in this universe.

### 3.3 The practice-court problem

None of the academies fit in a senior building, so every NBA club made a plan in 2022/23. **Rolled on how much each owner invests:**

| Club | Academy plan | Centre opens |
|---|---|---|
| **Detroit Pistons** | New **6-court** academy centre | **2025** |
| **Atlanta Hawks** | New 4-court centre | **2025** |
| **Cleveland Cavaliers** | New 3-court centre | **2025** |
| **Minnesota Timberwolves** | New 4-court centre | **2025** |
| **New Orleans Pelicans** | New 4-court centre | **2025** |
| **Oklahoma City Thunder** | New 4-court centre | **2025** |
| **Los Angeles Clippers** | **Takes over the empty Playa Vista training centre (2 courts) for the academy, and builds a 4-court academy centre in Inglewood** | Playa Vista from 2025 · **Inglewood: December 2026** |
| Dallas Mavericks | New 6-court centre | 2026 |
| Toronto Raptors | New 6-court centre | 2026 |
| Charlotte Hornets | New 3-court centre | 2026 |
| Memphis Grizzlies | New 4-court centre | 2026 |
| Philadelphia 76ers | New 4-court centre | 2026 |
| Sacramento Kings | New 4-court centre | 2026 |
| Utah Jazz | New 4-court centre | 2026 |
| Washington Wizards | New 4-court centre | 2026 |
| Brooklyn Nets | New 4-court centre | 2027 |
| San Antonio Spurs | New 4-court centre | 2027 |
| Phoenix Suns | New 3-court centre | 2027 |
| **Los Angeles Lakers** | **Rents high school gyms** around El Segundo and the South Bay; the senior court stays the Lakers' | — |
| Boston Celtics, Milwaukee Bucks | Rent high school gyms | — |
| Chicago Bulls, Denver Nuggets, Golden State Warriors, Houston Rockets, Indiana Pacers, Miami Heat, New York Knicks, Orlando Magic, Portland Trail Blazers | Rent university gyms | — |

Clubs whose centres open after 2025 **rent gyms until then.** Each G League affiliate runs **its own academy** too. When an affiliate is close to its parent, it uses the parent's centre; otherwise it rents gyms locally.

---

## 4. 2023/24: building and applying

- **Building:** the academy centres go up; the official platform is built.
- **Applications open for the AAND and the State Divisions.** An AAND club that wins promotion twice reaches the NBA without paying an expansion fee, so **investor groups in cities without an NBA team** founded new clubs and applied. **Rolled: seven of the twenty cities that had a realistic case.**

| New club | Founded | Arena |
|---|---|---|
| **Tampa Bay Basketball Club** | 2023 | Amalie Arena |
| **Cincinnati Basketball Club** | 2023 | Heritage Bank Center |
| **Columbus Basketball Club** | 2024 | Nationwide Arena |
| **Pittsburgh Basketball Club** | 2024 | PPG Paints Arena |
| **Austin Basketball Club** | 2024 | Moody Center |
| **Nashville Basketball Club** | 2024 | Bridgestone Arena |
| **Jacksonville Basketball Club** | 2024 | VyStar Veterans Memorial Arena |

**No new club was founded in Seattle, Las Vegas, San Diego, Kansas City or Louisville (rolled).**

- **Overtime Elite** applies, and expands the OTE Arena's showcase court to **1,600 seats** to meet the 1,500 rule.
- **From the TBL**, only the **Raleigh Firebirds** put together a licence application that holds up. They expand their home gym at St. Augustine's University with temporary stands to reach 1,500.

---

## 5. 2024/25: licences and grades

### 5.1 G League venues (the 4,000 rule)

| Club | Solution (rolled) |
|---|---|
| **South Bay Lakers** | **Move to Acrisure Arena, Thousand Palms (11,000), as the Coachella Valley Lakers**, from 2026/27. They play 2025/26 in El Segundo on a transitional licence |
| Delaware Blue Coats | Home games at the **Xfinity Mobile Arena**, Philadelphia (formerly Wells Fargo Center) |
| Greensboro Swarm | The **Greensboro Coliseum** main arena, next door to the Fieldhouse |
| Santa Cruz Warriors | **Kaiser Permanente Arena expanded to 4,000** |
| Motor City Cruise | **Little Caesars Arena** |
| Maine Celtics | **Cross Insurance Arena**, Portland |
| Sioux Falls Skyforce | **Sanford Premier Center**, Sioux Falls |
| College Park Skyhawks | **McCamish Pavilion**, Georgia Tech (8,600) |
| Wisconsin Herd | **Oshkosh Arena expanded to 4,000** |
| Mad Ants / Boom | The Pacers' Noblesville arena is **redesigned to 4,200** and opens in 2025, as in reality |

### 5.2 Academy grades (awarded in spring 2025)

**Platinum and Gold academies may sign players from outside their state before age 15 (Art. 9.2).**

| Grade | NBA academies | G League academies |
|---|---|---|
| **Platinum** | **Detroit Pistons, New Orleans Pelicans, Phoenix Suns, Toronto Raptors** | **Capital City Go-Go** |
| **Gold** | Atlanta, Boston, Brooklyn, Charlotte, Cleveland, Dallas, Denver, Golden State, Houston, Indiana, **LA Clippers, LA Lakers**, Miami, Minnesota, New York, Oklahoma City, Philadelphia, Sacramento, San Antonio, Utah, Washington | Cleveland Charge, Memphis Hustle, Salt Lake City Stars, Santa Cruz Warriors, Sioux Falls Skyforce |
| **Silver** | Chicago Bulls, Memphis Grizzlies, Milwaukee Bucks, Orlando Magic, Portland Trail Blazers | Every other G League club, including the **South Bay / Coachella Valley Lakers**, the **San Diego Clippers**, and the independents (RGV Vipers, Texas Legends, Capitanes) |

**Phoenix is Platinum before its centre even opens**, on coaching, medical staff and education. **The Lakers are Gold despite renting high school gyms.**

### 5.3 AAND licences for non-university clubs

All nine applicants above were licensed: the **seven new clubs, Overtime Elite and the Raleigh Firebirds**. Their academies start in 2025/26. **The platform goes live.**

---

## 6. 2025/26: the academies start

### 6.1 The youth leagues

**The NBA and USA Basketball decided the formats**: every age group U12–U19, conferences, weekend games (Art. 22).

| League | Clubs | Format |
|---|---|---|
| **NBA Academy League** (Elite 1) | 30 | East and West, 15 each. **U12–U14: 14 games** (single round robin). **U15–U19: 28 games** (home and away). Each conference's top two go to a final four |
| **G League Academy League** (Elite 2) | 30 (14 East, 16 West) | Same format |
| **AAND Academy League** (IP) | 9 | One national table. 8 games U12–U14, 16 games U15–U19 |
| **National Women's Academy League** | 60 | U16, U17, U19 (Art. 47). Not simulated here |

### 6.2 Champions

| Age | NBA Academy League | G League Academy League | AAND Academy League | National Youth Cup |
|---|---|---|---|---|
| U12 | **Toronto Raptors** | **Westchester Knicks** | Columbus BC | — (from U14) |
| U13 | **Dallas Mavericks** | **Delaware Blue Coats** | Columbus BC | — |
| U14 | **Los Angeles Clippers** | **Memphis Hustle** | Pittsburgh BC | **Detroit Pistons** |
| U15 | **Los Angeles Lakers** | **San Diego Clippers** | Cincinnati BC | **Dallas Mavericks** |
| U16 | **Chicago Bulls** | **College Park Skyhawks** | Raleigh Firebirds | **Austin Spurs** (G League) |
| U17 | **Los Angeles Clippers** | **South Bay Lakers** | Jacksonville BC | **New York Knicks** |
| U18 | **Philadelphia 76ers** | **Grand Rapids Gold** | Columbus BC | **Los Angeles Clippers** |
| U19 | **Philadelphia 76ers** | **Capital City Go-Go** | Pittsburgh BC | **Philadelphia 76ers** (double) |

**Los Angeles had the best first season of any city: three NBA academy league titles** (Clippers U14 and U17, Lakers U15) **and the Clippers' U18 Youth Cup**, plus two G League titles (San Diego Clippers U15, South Bay Lakers U17). **The Austin Spurs won the U16 Youth Cup from the G League**, the only cup any non-NBA academy won.

### 6.3 U12, 2025/26 (the age group above your player's)

**NBA Academy League U12, West** (14 games)

| # | Club | W–L |
|---|---|---|
| 1 | Golden State Warriors | 11–3 |
| 2 | Dallas Mavericks | 10–4 |
| 3 | **Los Angeles Lakers** | 10–4 |
| 4 | **Los Angeles Clippers** | 9–5 |
| 5 | Phoenix Suns | 8–6 |
| 6 | Portland Trail Blazers | 8–6 |
| 7 | Houston Rockets | 7–7 |
| 8 | Denver Nuggets | 6–8 |
| 9 | New Orleans Pelicans | 6–8 |
| 10 | Oklahoma City Thunder | 6–8 |
| 11 | Sacramento Kings | 6–8 |
| 12 | San Antonio Spurs | 5–9 |
| 13 | Utah Jazz | 5–9 |
| 14 | Memphis Grizzlies | 4–10 |
| 15 | Minnesota Timberwolves | 4–10 |

The final four was Golden State, Dallas, Chicago and Toronto; **Toronto won it.**

**G League Academy League U12, West** (15 games)

| # | Club | W–L |
|---|---|---|
| 1 | **South Bay Lakers** | 12–3 |
| 2 | Austin Spurs | 9–6 |
| 3 | Birmingham Squadron | 9–6 |
| 4 | Mexico City Capitanes | 9–6 |
| 5 | **San Diego Clippers** | 9–6 |
| 6 | Santa Cruz Warriors | 9–6 |
| 7 | Oklahoma City Blue | 8–7 |
| 8 | Salt Lake City Stars | 8–7 |
| 9 | Stockton Kings | 8–7 |
| 10 | Memphis Hustle | 7–8 |
| 11 | Rio Grande Valley Vipers | 7–8 |
| 12 | Sioux Falls Skyforce | 7–8 |
| 13 | Rip City Remix | 7–8 |
| 14 | Grand Rapids Gold | 5–10 |
| 15 | Texas Legends | 5–10 |
| 16 | Iowa Wolves | 1–14 |

**Westchester won the final four.** The South Bay Lakers won the West but lost in the semi-final.

### 6.4 Spring 2026: the universities apply

**68 of the 161 programmes looked at applied in the main round**, plus **41 other programmes** (smaller Division I schools, Division II, NAIA), all of which start in SD1. The choice was hard. A university club's first team plays in the pyramid, and only its **second team, the B team, is its NCAA team** (Art. 64). So the programme's best players leave March Madness, and the tournament is played by the B team. **Many of the biggest names stayed out.**

**Did not apply** (main round), among others: **Michigan** (the 2026 national champion), **Gonzaga, UCLA, USC, Arizona**, Michigan State, Purdue, Alabama, Auburn, St. John's, Creighton, Ohio State, Kansas State, Missouri.

**Applied but failed the AAND licence** (so they start in SD1):

| University | Why |
|---|---|
| **Saint Mary's** | Debt above the limit |
| **Marquette**, **Butler**, Drake, NC State, **Memphis** | Debt above the limit |
| **Villanova**, Saint Joseph's | Partner academies for U12–U16 not in place |
| **Virginia**, **VCU**, Georgia, New Mexico, Saint Louis, Seattle U, UC Riverside, UTEP | No proof of national travel funding |
| Hawaii | No proof of national travel funding. Placed in Hawaii's own league (Art. 5.3) |

**The main round left the AAND four short**: 60 licensed clubs for 64 places. So **the Board held a supplementary round in May 2026.** Ten more universities applied. **The four strongest got the places: Iowa State, Kentucky, Kansas, North Carolina.** The six that missed out (Louisville, Texas A&M, Mississippi State, Cincinnati, UCF, Oklahoma State) **withdrew** and stay NCAA-only: they had applied only for an AAND place.

---

## 7. Summer 2026: the system for 2026/27

### 7.1 NBA (tier 1)

The 30 clubs as in reality. No promotion or relegation until the Board declares the system established (Art. 55).

### 7.2 G League (tier 2): 30 clubs

| East | Affiliate of | Arena | Academy |
|---|---|---|---|
| Capital City Go-Go | Wizards | CareFirst Arena | **Platinum** |
| Cleveland Charge | Cavaliers | Public Auditorium | Gold |
| College Park Skyhawks | Hawks | McCamish Pavilion | Silver |
| Delaware Blue Coats | 76ers | Xfinity Mobile Arena | Silver |
| Greensboro Swarm | Hornets | Greensboro Coliseum | Silver |
| Long Island Nets | Nets | Nassau Coliseum | Silver |
| Maine Celtics | Celtics | Cross Insurance Arena | Silver |
| Motor City Cruise | Pistons | Little Caesars Arena | Silver |
| Noblesville Boom | Pacers | Riverview Health Arena (4,200) | Silver |
| Osceola Magic | Magic | Silver Spurs Arena | Silver |
| Raptors 905 | Raptors | Mississauga | Silver |
| Westchester Knicks | Knicks | Westchester County Center | Silver |
| Windy City Bulls | Bulls | Now Arena | Silver |
| Wisconsin Herd | Bucks | Oshkosh Arena (4,000) | Silver |

| West | Affiliate of | Arena | Academy |
|---|---|---|---|
| Austin Spurs | Spurs | H-E-B Center | Silver |
| **Coachella Valley Lakers** | Lakers | Acrisure Arena, Thousand Palms | Silver |
| Grand Rapids Gold | Nuggets | Van Andel Arena | Silver |
| Iowa Wolves | Timberwolves | Casey's Center | Silver |
| Laketown Squadron | Pelicans | Pontchartrain Center | Silver |
| Memphis Hustle | Grizzlies | Landers Center | Gold |
| **Mexico City Capitanes** | ***independent*** | Arena CDMX | Silver |
| Oklahoma City Blue | Thunder | Paycom Center | Silver |
| **Rio Grande Valley Vipers** | ***independent*** | Bert Ogden Arena | Silver |
| Rip City Remix | Trail Blazers | Chiles Center | Silver |
| Salt Lake City Stars | Jazz | Maverik Center | Gold |
| **San Diego Clippers** | Clippers | Frontwave Arena, Oceanside | Silver |
| Santa Cruz Warriors | Warriors | Kaiser Permanente Arena (4,000) | Gold |
| Sioux Falls Skyforce | Heat | Sanford Premier Center | Gold |
| Stockton Kings | Kings | Adventist Health Arena | Silver |
| **Texas Legends** | ***independent*** | Comerica Center | Silver |

**Three independents can be promoted**: the Capitanes, the Vipers and the Legends.

### 7.3 AAND (tier 3): 64 clubs

The Board moved the clubs nearest the borders so that each conference has 16: **Texas Tech, TCU and North Texas to the West; Kentucky, Murray State and Western Kentucky to the Midwest; the Raleigh Firebirds and Liberty to the East.** Strongest first (narrator).

| West | Midwest | East | South |
|---|---|---|---|
| Texas Tech | Iowa State | **Duke** | **Houston** |
| BYU | Illinois | **UConn** | **Florida** |
| San Diego State | **Kentucky** | Maryland | Tennessee |
| Oregon | Wisconsin | **Pittsburgh BC** *(new)* | Arkansas |
| Utah State | **Columbus BC** *(new)* | North Carolina | Baylor |
| Stanford | **Kansas** | Pittsburgh | **Austin BC** *(new)* |
| Utah | Xavier | Syracuse | **Tampa Bay BC** *(new)* |
| TCU | Indiana | Liberty | Texas |
| North Texas | **Cincinnati BC** *(new)* | Wake Forest | Clemson |
| Washington | Dayton | Seton Hall | **Jacksonville BC** *(new)* |
| Colorado | Northern Iowa | St. Bonaventure | **Nashville BC** *(new)* |
| California | Notre Dame | Temple | South Carolina |
| UC Santa Barbara | Murray State | Princeton | **Overtime Elite** |
| **Loyola Marymount** | Western Kentucky | **Raleigh Firebirds** *(TBL)* | Belmont |
| Wyoming | DePaul | Drexel | Georgia Tech |
| UC Davis | Kent State | Hofstra | Samford |

**55 university clubs and 9 others.** **A university club's NCAA team is its B team**: the second team, made up of students outside the first-team squad. It plays in the NCAA division the university belonged to before (Art. 64).

### 7.4 California, tier 4 seniors

**California SD1** (statewide): **Saint Mary's** (failed the AAND licence and is by far the strongest club), **UC Riverside**, Cal Poly, Pacific, Cal Poly Pomona, Chico State, Point Loma, Cal State San Bernardino, Concordia Irvine, and **El Camino College** (Torrance). That's **ten college clubs.** Art. 6 needs at least 12, so **the last two places go to adult clubs from the state's open registration.** Three real semi-pro clubs had a case (rolled on strength):

| Adult club | Background | Home | Result |
|---|---|---|---|
| **San Diego Sharks** | TBL since 2022 | Canyon Crest Academy, San Diego (2,900) | **SD1** |
| **San Diego Surf** | ABA from 2009 | HourGlass Arena, Miramar College | **SD1** |
| Bakersfield Majestics | TBL since 2022 | Bakersfield College | **Did not apply** (rolled): registers in tier 4 below SD1 |

**California SD1 2026/27: twelve clubs.**

**Southern California SD2 and the SD3 metro divisions** (including **SD3 Los Angeles**) are open entry: adult clubs, pro-am sides, college clubs below SD1.

### 7.5 The youth ladder in 2026/27 (your mapping)

| Belgian equivalent | Basketball | Who plays there |
|---|---|---|
| **Elite 1** | **NBA Academy League** | 30 NBA academies |
| **Elite 2** | **G League Academy League** | 30 G League academies |
| **Interprovinciaal** | **AAND Academy League** | 64 AAND academies: the 9 from 2025/26, plus the **university clubs' partner academies** (U12–U16, Art. 61) and their own U17 and U19 teams. **The AAND academy league grows from 9 clubs to 64** |
| **Provinciaal** | **Youth SD1** (California) | Tier-4 youth programmes. **Starts 2026/27** |
| **Gewestelijk** | **Youth SD2 Southern California, Youth SD3 Los Angeles** | Tier-4 youth programmes. **Starts 2026/27**. Pay-to-play allowed |

**Tier-4 youth placement** (which AAU programmes go into Youth SD1, SD2 and SD3, by age group) was decided by the state in spring 2026, on each programme's application and its AAU record. **I'll research the U12 level around Inglewood for the setup file.**

### 7.6 Academies within reach of Inglewood

| Academy | Level | Where they train | Distance from Inglewood |
|---|---|---|---|
| **Los Angeles Clippers** | NBA (Gold) | **Playa Vista** (2 courts). **The Inglewood academy centre opens in December 2026**, next to the Intuit Dome | Playa Vista ~10 km; the new centre is in Inglewood |
| **Los Angeles Lakers** | NBA (Gold) | Rented high school gyms, El Segundo and the South Bay | ~10 km |
| **Loyola Marymount** partner academy | AAND | Westchester (LMU campus and partner schools) | ~5 km |
| **San Diego Clippers** | G League (Silver) | Oceanside | ~140 km |
| **Coachella Valley Lakers** | G League (Silver) | Thousand Palms | ~200 km. **The academy moved with the club in summer 2026.** Its LA boys aged U12–U14 can move freely (Art. 24) |

**The South Bay Lakers' move leaves LA without a G League academy in 2026/27.** So the Elite 2 level effectively disappears from the LA map, apart from Oceanside. Between the tier-4 clubs and the two NBA academies there's **LMU's AAND partner academy**, five kilometres from Inglewood.

---

## 8. Where things stand: 1 July 2026

| | |
|---|---|
| **Seniors** | NBA 30 · G League 30 (three independents) · AAND 64 · State Divisions open |
| **Last draft** | **June 2027** |
| **Academies** | 60 in tiers 1–2 (5 Platinum, 26 Gold, 29 Silver), 64 in the AAND |
| **LA** | Clippers (Playa Vista, then Inglewood from December), Lakers (rented gyms), LMU partner academy (AAND), tier-4 programmes in Youth SD1–SD3 |
| **Next** | **The setup file**: your player, his family, and the real tier-4 clubs around Inglewood for your first transfer decision |

**Settled with you after the first draft:** the basketball game model is approved; California SD1 is filled with adult clubs; a university club's NCAA team is its B team.

---

## Sources

- [NBA G League (Wikipedia): teams, arenas, ownership, moves](https://en.wikipedia.org/wiki/NBA_G_League)
- [List of NBA G League champions](https://en.wikipedia.org/wiki/List_of_NBA_G_League_champions)
- [UCLA Health Training Center](https://en.wikipedia.org/wiki/UCLA_Health_Training_Center)
- [Los Angeles Clippers Training Center](https://en.wikipedia.org/wiki/Los_Angeles_Clippers_Training_Center)
- [Intuit Dome](https://en.wikipedia.org/wiki/Intuit_Dome)
- [Atlanta Jewish Times: the Overtime Elite complex](https://www.atlantajewishtimes.com/overtime-elite-complex-attracting-fans-scouts/)
- [2026 TBL season](https://en.wikipedia.org/wiki/2026_TBL_season) · [Raleigh Firebirds](https://en.wikipedia.org/wiki/Raleigh_Firebirds)
- [94x50 League (San Diego Sharks)](https://en.wikipedia.org/wiki/94x50_League) · [San Diego Surf](https://en.wikipedia.org/wiki/Oceanside_Surf) · [Bakersfield Majestics](https://en.wikipedia.org/wiki/Bakersfield_Majestics)
- [ABC7: Knicks win the 2026 NBA title over the Spurs](https://abc7news.com/amp/post/new-york-knicks-win-first-nba-title-1973-94-90-victory-san-antonio-spurs-game-5/19292501/)
- [iHeart: Michigan wins the 2026 national championship](https://www.iheart.com/content/2026-04-06-michigan-wins-national-championship/)
