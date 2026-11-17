# Deployment by the figures against main: head-to-head (2026-11-17)

**Verdict: level. The new deployment is +30 VP a game, give or take 77. That is within noise, and inside the "not worse than -30" band, so
it can be kept.** It changes almost every drop (88% of its spots carry a figure, against 9% on main), but the fights it leads to are no
better: first round won and net points per fight are a little lower. The gain comes from objectives (+19) and kills (+16).

Batch: 576 games, all ended. 288 DKTC pairs (the usual 144 plus the 144 lying midway between them in the list of all 595 pairings of the
35 lists), static v static, seed 1, scenarios mix, each pair played both ways. Build `claude/project-thread-1vnftw` at `13df7bd5`.
ON = the three switches (holder at deployment, lane by figures, deploy by figures); OFF = main's deployment. The "no spot given" fix is on
for both. Pairs ahead 142, behind 146.

## 1. Headline

| # | Number | **New deployment (ON)** | **Main (OFF)** |
| --- | --- | --- | --- |
| 1 | VP margin per game | **+30 ±77** | -30 |
| 2 | First round won when charging | 73% | 75% |
| 3 | Net points per charged fight | +85 | +90 |
| 4 | Points lost per game | 685 | 705 |
| 5 | Free units caught in flank or rear (per game) | 0.59 | 0.59 |

Usual 144 pairs +11 ±110, new 144 pairs +48 ±109 (the two halves agree). ON as Mine -21, as Opponent +81; going first -14, second +73.
Won / drawn / lost 243 / 108 / 225.

## 2. Deployment (per side and game)

| Measure | ON | OFF |
| --- | --- | --- |
| Drops whose spot carries a figure of 1 VP or more | 88% | 9% |
| Drop order changed by "what seeing the enemy first is worth" | 518 of 576 games | - |
| Placed by the automatic search | 3% | 3% |
| "No spot given" left (fix on both sides) | 18 drops | 18 drops |
| Character could not join the unit it asked for (placed alone) | 56 | 54 |
| Holder rows (a unit offered a spot to hold a marker) | 1.0 a game, 47% changed the spot | - |
| Holder spots actually taken | 0.2 a game | 0.0 |
| Own-side markers with a unit within 8" at the start | 72% | 67% |
| Big lone characters (250+) taking a lane instead of beside their unit | 93% (498 of 535) | 0% |
| Screens in front of the dearest block | 0.3 a game | 0.0 |
| Hold-up chaff in front of an enemy unit | 0.0 | 0.15 |

**Holders look over-valued.** Each holder row claims about 170 VP (most between 100 and 234 VP, the cap the build warned of), while
the whole ON side gains 19 VP of objectives a game. The holder figure is not yet tied to what holding returns. It changed 264 spots.

**Lanes:** big lone characters left their unit's side 93% of the time, with a claimed +44 VP each. Not measured per character here; overall the ON side
lost 19 points a game fewer and won 5 VP less from enemy leaders, and its fights were not better.

**Orion and other joiners:** Orion deployed in all 38 Wood Elf games with him. Characters that could not join their unit (placed alone
by the automatic search) are as frequent ON as OFF (56 v 54), mostly Vampire Counts and Warriors of Chaos characters.

## 3. VP by source (per game)

| Source | ON | OFF |
| --- | --- | --- |
| Objectives | 589 | 570 |
| Kills | 741 | 724 |
| Leaders | 49 | 54 |
| Charged fights a game | 2.9 | 2.8 |

By scenario (ON margin): Encirclement +113, Close Quarters +112, Upon the Field of Glory +76, Drawn Battlelines +9, A Chance Encounter
+7, King of the Hill -139 (each about ±220: noise).

## 4. Results by army (ON margin in the pairs that army plays in, both ways)

| Army | Pairs | ON margin |
| --- | --- | --- |
| Lizardmen | 15 | +411 ±230 |
| Wood Elf Realms | 51 | +132 ±188 |
| High Elf Realms | 49 | +106 ±179 |
| Empire of Man | 47 | +94 ±172 |
| Kingdom of Bretonnia | 16 | +88 ±334 |
| Vampire Counts | 64 | +86 ±147 |
| Ogre Kingdoms | 18 | +60 ±310 |
| Grand Cathay | 48 | +54 ±175 |
| Warriors of Chaos | 72 | +25 ±149 |
| Tomb Kings of Khemri | 33 | +4 ±258 |
| Dwarfen Mountain Holds | 33 | -27 ±200 |
| Beastmen Brayherds | 33 | -74 ±251 |
| Skaven | 33 | -141 ±220 |
| Orc & Goblin Tribes | 16 | -175 ±539 |
| Chaos Dwarfs | 32 | -211 ±247 |

Only Lizardmen is outside noise (15 pairs).

## 5. Bugs and errors

No engine errors, no stuck games, no game over the time limit. Three sim findings: S-fef937 **new** (L0610, Jade Lancers with a joined
Captain found out of position in turn 6), S-44ed5a **back** (L2131, Doomwheel 0.11" off the table in turn 6; marked fixed 2026-11-12),
S-640712 known (L0224, destroyed Herdstone scores nothing). None is at deployment. Pushes to simulation-data raced between the 16 parts
(about 25 first-try failures); every game was carried by a later push, 576 of 576 checked on the branch.

Full tables: compare-all.md beside this report. Replays: WarhammerOldWorldSimulator branch `claude/project-thread-vea0oi`
(deploy/sim-replays/dep-{mine,opp}-13df7bd-p1..8, on-site.txt lists those 16). Logs archived to OldWorldSimulations.
