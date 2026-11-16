# Charge odds + band + honest worth: head-to-head against main (2026-11-16)

**Verdict: no gain in the game result. The side with all three changes is behind by -7 VP a game, give or take 110 VP: a dead heat**
(last night, odds + band without honest worth: -14 ±99, also a dead heat). Honest worth did what it was built to do on the charges: the
changed side made a third fewer long shots and a quarter fewer overkill piles than last night, its charges are now honest (planned 80 VP,
won 97 VP a charge job; main plans 103 and wins 87), and its first round is won 76% of the time against 71% for main. But it charges less
(748 charged fights against 868), destroys less in combat, and the gains per fight do not add up to a better score.

Batch: 288 games, the same 144 DKTC pairs and seeds as the charge-band, charge-odds and shooting-plan head-to-heads (Hero v Hero, seed 1,
scenarios mix), each pair played twice. Changed side: branch `claude/project-thread-5irtu9` at `3cc170f19` (charge-odds fixes + charge band +
honest worth). Other side: `charge-odds`, `charge-band` and `honest-worth` switched off = main. mine-1..4: changes on for Mine; opp-1..4:
changes on for Opponent. 288 of 288 games ended, no stalls, no re-runs (mine-3 and opp-4 lost their first start in the build and restarted).
Every part's rules-off list named all eight tags for the right side, and no row of HONEST WORTH or CHARGE BAND was written on the
switched-off side (no leak). One finding (see the end).

## 1. Morten's five headline numbers

| # | Number | **Changes on** | **Changes off (main)** | Read |
| --- | --- | --- | --- | --- |
| 1 | VP margin per game | **-7** | +7 | **-7 ±110** (paired over 144 pairs), inside noise |
| 2 | First round won when charging | **76%** | 71% | 5 points better (last night 72 v 72) |
| 3 | Net points per charged fight | +76 | +78 | same (damage counted: +81 v +78) |
| 4 | Points lost per game | 734 | 717 | 17 more, within noise |
| 5 | Free units caught in flank or rear (per game, lower is better) | 0.73 | 0.62 | a little worse, within noise |

W/D/L of the changed side 113 / 60 / 115; pairs ahead over both games 65, behind 79. For comparison: odds + band -14 ±99, charge odds
alone +4 ±102, shooting plan -19 ±92.

Diagnostics (not targets): charge contacts a game 3.5 v 3.8; points that never fought 38% v 36%; lone characters that fought 76% v 78%.

## 2. Charges by odds band (what this change should move)

Fights the side charged into, by the odds it was told. Net per 100 charger points, damage counted. Overkill = target under 250 pts and
chargers over 3x its points. Last night's changed side (odds + band, no honest worth) beside it.

| Band | Changes on: fights, first round won, net per 100 | Main: fights, first round won, net per 100 | Last night, odds + band: fights |
| --- | --- | --- | --- |
| under 50% | **117**, 30%, +26 ±21 | 146, 30%, +14 ±17 | 165 |
| 50-59% | 52, 58%, +17 ±19 | 48, 40%, +20 ±24 | 66 |
| 60-75% | 133, 74%, +28 ±11 | 115, 52%, +22 ±16 | 136 |
| 76-89% | 182, 85%, +33 ±9 | 197, 80%, +30 ±10 | 192 |
| 90%+ not overkill | 194, 94%, +40 ±9 | **280**, 91%, +45 ±8 | 193 |
| 90%+ overkill | **70**, 97%, +20 ±5 | 82, 93%, +19 ±7 | 96 |
| **All** | **748** | **868** | 908 |

- Honest worth took out 48 long shots and 26 overkill piles against last night; the 55-89% charges stayed. The long shots it still makes
  earn more (+26 v +14 per 100 points).
- The gap in sure charges (90%+ not overkill: 194 v 280) is the honest odds, as in both earlier batches (193 v 292 last night), not
  honest worth. Main's "sure" charges win 91%; the changed side's win 94%.
- Every band from 50% up wins its first round more often on the changed side; 60-75% by 22 points (74 v 52%).

### The band rule: help asked and came

| | Changes on |
| --- | --- |
| Charges where the band asked for help | 45 in 288 games (0.16 a game; last night 33, 0.11) |
| Alone v together (average) | 66% alone, 93% together |
| Of those, the charge was made | 32 (24 with 2-3 chargers, 8 with one) |
| First round of those 32 | 25 won, 2 drawn, 5 lost (78%; the line had said 85%) |
| Net per 100 charger points | +32 (chargers 408 pts, targets 184 pts) |
| Support requests answered (helper made contact too), all supports | 49% (97 of 198) v main 46% (85 of 185) |
| Joint charges a game (2+ units on one target) | 0.5 v 0.5; share of targets hit by 2+ units 17% v 13% |

Still far too rare to move the result (about 1 fight in 9 games).

### What honest worth did (HONEST WORTH rows)

2,346 rows on the changed side (8.1 a game): charge 839, close in 979, advance 510. It changed the chosen option only 107 times (0.37 a
game: 16 charges, 51 close-ins, 40 advances); the rest of the time the same option won with a lower figure (a charge's worth by about
-33 VP). So the change mostly relabels; where it does decide, it drops a long shot or an overkill pile for something else.

## 3. Do stated odds match results?

| Odds band | Changes on: fights, said, won | Main: fights, said, won |
| --- | --- | --- |
| under 50 | 117, 26%, 30% ±8 | 146, 24%, 30% ±7 |
| 50-59 | 52, 55%, 58% ±13 | 48, 54%, 40% ±14 |
| 60-75 | 133, 67%, 74% ±7 | 115, 68%, 52% ±9 |
| 76-89 | 182, 83%, 85% ±5 | 197, 83%, 80% ±6 |
| 90-94 | 80, 92%, **90% ±7** | 76, 92%, 89% ±7 |
| 95-100 | 184, 98%, **97% ±3** | 286, 99%, **92% ±3** |

Too sure, in points (said minus won), fights at 60%+: changes on -1.4 (579 fights), main +7.0 (674). Fights with joined characters,
challenges or combat spells +1.6 v +15.3. The 90-94% band, 8 points too sure in both earlier batches, is right this time (90 v 92).

## 4. Other KPIs side by side

| Measure | Changes on | Main |
| --- | --- | --- |
| Charges declared / contacts a game | 5.0 / 3.5 | 5.4 / 3.8 |
| Games where this side made the first charge contact | 46% | 54% |
| Sides that never made charge contact | 11% | 7% |
| Charge objectives carried out (made contact) | 47% | 49% |
| Close-in set-ups that charged that target next turn | 15% | 14% |
| Joined characters whose unit fought | 47% | 37% |
| Charged fights on a top-3 enemy unit | 164 | 198 |
| Points destroyed in combat a game | 345 | 373 |
| Points run down a game | 91 | 94 |
| Points destroyed by magic a game | 58 | 45 |
| Points destroyed by war machines a game | 56 | 47 |
| Winner followed up or pursued | 92% | 89% |
| Idle units a game | 1.4 | 1.4 |
| Points that never moved of their own a game | 228 | 217 |
| Turned to face a threat (FACES THE THREAT) a game | 1.56 | 1.54 |
| Stood instead of an exposed move (SAFER THAN THE JOB) a game | 1.02 | 0.86 |
| Turns played defensive | 16% | 17% |
| Magic missiles tried each own turn (when they could be) | 33% (48%) | 34% (48%) |

Full side-by-side tables: kpis-on-v-off.md (remapped to changes on / main) and compare-all.md (A = mine arm, B = opp arm); bands.md.

### Jobs claimed v happened (all jobs of each side)

| Job | Changes on: jobs, happened, planned v won VP a job | Main |
| --- | --- | --- |
| charge | 1068, 58%, **80 v 97** | 1223, 55%, 103 v 87 |
| close in | 1450, 25%, 50 v 27 | 1428, 25%, 64 v 27 |
| advance | 3634, 16%, 18 v 27 | 3624, 17%, 21 v 27 |
| shoot | 1960, 61%, 10 v 75 | 1924, 59%, 11 v 74 |
| hold | 1260, 34%, 61 v 0 | 1272, 34%, 63 v 0 |
| support | 1388, 90%, -8 v 0 | 1287, 88%, -8 v 0 |
| join | 210, 97%, 34 v 0 | 213, 94%, 32 v 0 |

A charge now promises less than it wins (80 v 97); main promises more than it wins (103 v 87). Close-ins still promise twice what they win.

### Stance split (gunline = the 49 army-games the framework played defensively in head-to-head 2)

| Set | Army-games | Margin, changes on | main | Paired difference | Better / worse |
| --- | --- | --- | --- | --- | --- |
| Gunline armies | 49 | -298 | -261 | -37 ±381 | 23 / 26 |
| Other armies | 239 | +52 | +62 | -10 ±170 | 107 / 132 |

### VP by source (per game)

| Source | Changes on | Main |
| --- | --- | --- |
| Kills | 769 | 773 |
| Objectives | 565 | 564 |
| Leaders | 49 | 54 |
| Points lost | 734 | 717 |
| Units lost | 4.9 | 4.9 |

Going first v second (changed side's margin): first +9, second -24. As Mine -77, as Opponent +63 (the lists; pairing cancels it).

## 5. What this means (warnings, not plans)

- The three changes make the charges honest and better chosen (fewer long shots and overkill, first round won 76% v 71%, 95%+ wins 97%),
  but the side that has them simply charges less: 120 fewer charged fights in 288 games, 28 fewer points destroyed in combat a game.
  The better fights and the fewer fights cancel out.
- The biggest single gap is still the "sure, not overkill" charges main makes and the honest side does not (280 v 194, all three batches).
  Main wins those 91% for +45 per 100 points; at the honest odds many of them are 85-90% charges the changed side passes up.
- Honest worth decided the option only 0.37 times a game; its weight is mostly a relabel, like the honest odds were.
- The band rule still fires 0.16 times a game.

## Files

- Results: mine-1..4, opp-1..4; counts.log.
- Replays: branch `claude/project-thread-ljncvb` at `bff6438d3` (8 batch folders cw-h2h-{mine,opp}-3cc170f-p1..4; on-site.txt lists
  them). Not on main.
- scripts/: last night's scripts with the folder changed, plus worth.py (HONEST WORTH and CHARGE BAND rows, leak check).
  compare-all.md from cb.py (the corrected first-round reading); the missile row from the repo's own compare-batches.py.
- Finding: sim bug S-07892d, game L2131 (mine-2): two Marauder Horsemen units of one side overlap by 1.03", noticed late in turn 6. Same
  game and bug as last night; its fix (S-67c2af) is on main but not on this branch, so it is expected here.
