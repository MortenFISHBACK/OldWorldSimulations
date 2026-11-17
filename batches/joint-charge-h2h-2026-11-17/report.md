# Joint charge pricing against simpler pricing: head-to-head (2026-11-17)

**Verdict: joint charge pricing is level with simpler pricing, slightly ahead: +36 VP a game, give or take 53.** Not proven better,
but by the band set beforehand (keep if not worse than about -30) it can be kept. It changes little: the new rule picked a second
charger only 0.3 times a game, and joint charges went from 0.4 to 0.5 a game.

Batch: 288 games, the same 144 DKTC pairs and seeds as the five-action batches (Hero v Hero, seed 1, scenarios mix), each pair played
both ways. Build `claude/project-thread-eyy865` at `1e5408d1`; one side with `second-charger-adds` on, the other off (= simpler
pricing); the log rows (`friend-in-reach`) on for both. All 288 games ended, no engine errors, no stuck games, no sim findings.
Pairs ahead 59, behind 49, identical 36 (the rule never changed a pick in those).

## 1. Headline

| # | Number | **Joint pricing** | **Simpler pricing** |
| --- | --- | --- | --- |
| 1 | VP margin per game | **+36 ±53** | -36 |
| 2 | First round won when charging | 74% | 72% |
| 3 | Net points per charged fight | +91 | +84 |
| 4 | Points lost per game | 711 | 737 |
| 5 | Own free units caught in flank or rear (per game) | 0.60 | 0.57 |

Joint pricing as Mine -71, as Opponent +143 (both inside the noise); going first +20, second +52.

## 2. VP by source (per game)

| Source | Joint pricing | Simpler pricing |
| --- | --- | --- |
| Objectives | 578 | 561 |
| Kills | 775 | 755 |
| Leaders | 51 | 51 |

## 3. Claims against what happened

The computer's own figure for each charge it picked (FRIEND IN REACH rows): worth alone against worth with the best friend in reach.

| Per charge picked | Joint pricing | Simpler pricing |
| --- | --- | --- |
| Charges picked a game | 4.4 | 4.4 |
| A friend could have joined | 60% | 58% |
| Worth alone / with that friend (VP) | 81 / 119 (+38) | 79 / 115 (+36) |
| ...the friend charged it too | 47% | 48% |
| ...the friend's charge was below zero alone | **3%** | 14% |
| ...on the friend's list but not taken | **19%** | 9% |
| ...not among the friend's best, or unseen | 31% | 29% |

The new pricing did its job on paper: a friend's charge that was "below zero alone" is now valued by what it adds (14% -> 3%). But in
most of those cases the friend still took another job, so the share of charges with the friend on it did not grow (47% v 48%).

| What happened (per game) | Joint pricing | Simpler pricing |
| --- | --- | --- |
| Second charger priced by what it adds, and taken | 0.3 | - |
| Joint charges (2+ units on one target in one turn) | 0.5 | 0.4 |
| Charged targets hit by 2+ units | 16% (142) | 14% (123) |
| Help asked / answered (helper made contact), whole batch | 288 / 108 (38%) | 162 / 83 (51%) |
| Net points per fight with support / alone | +122 / +85 | +122 / +78 |

Help is now asked almost twice as often (no 55% gate), and answered a little more often in total, but most asks are not answered.

## 4. Bugs

None: 288 of 288 games ended, no engine errors, no sim findings.

## Files

Games: simulation-data `measurements/jc-<mine|opp>-1e5408d-p1..4` (mine = joint pricing on for Mine). Scripts: `scripts/` here
(h.py margin, merge.py + compare-batches.py + remap.py for the headline tables, friend.py for the claims).
