# Army-wide holders ON v OFF: early reading at 49 games (2026-11-18 10:00 UTC)

Build 95a3d390 (bj3s5r), both sides the overhaul's pricing; the only difference is holder-assignment. Switch side checked in every game
so far: HOLDER ASSIGNMENT rows on the on side only (12-68 a game).

## Claimed v happened (turn table, on side)

| Assigned to | Assignments | Claimed (mean VP of the row) | Holder scored it that round |
| --- | --- | --- | --- |
| Marker | 363 | 71 | 69% |
| The hill | 17 | 112 | 24% |
| Herdstone / special feature / baggage | 165 / 107 / 95 | - | not measured (scored at end or no per-turn row) |

(scripts/assigned.py. job_claims.py's hold row reads no picks on this branch: five-option jobs are named differently, so it shows nothing.)

## Markers (scripts/markers.py, objective_holders.py)

| | ON | OFF |
| --- | --- | --- |
| Marker player-turns scored (nobody: 33%; baseline 50%) | 35% | 32% |
| Marker/hill VP a game | 397 | 364 |
| Points of the scoring unit, mean (median) | 268 (139) | 272 (173) |
| Scored by a 210+ unit | 38% | 45% |
| Scored by the cheapest able unit alive | 35% | 38% |

## Headline

| | ON | OFF |
| --- | --- | --- |
| Charges declared a game | 3.0 | 2.6 |
| First round won when charging (claimed v happened) | 66% v 70% | 61% v 71% |
| Net points per charged fight | +80 | +56 |
| Points lost a game | 434 | 488 |
| Free units caught in flank/rear a game | 1.0 | 0.94 |
| Thinking time | 6.2 min a game, longest 12.8 (both sides in every game; smoke 4.2 on v 4.4 off) |

VP margin ON v OFF: +83 ±235 (21 won, 17 lost, 11 drawn): noise at 49 games.

Leads only (not checked in code): the cheapest-able share did not rise, so the table's "gives up least" does not yet pick the cheapest
unit; the hill holder reaches it only 24% of the time.
