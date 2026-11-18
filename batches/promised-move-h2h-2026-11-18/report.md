# Try 8: promised moves against simpler pricing - stopped at 78 games (2026-11-18)

Build 44aac6ae1 (branch claude/project-thread-60g6hv). New side: everything on, incl. friend-charges-first, friend-shoots-first,
waits-again, wounds-on-the-ranks, the-promised-move. Simpler side: worked-out-chances, five-action, standing-by-numbers off. Same pairs
both ways. Stopped by the coordinator at 07:22 UTC (promises still kept ~17-19 per 100; Morten's rule: next root cause). Switch side
checked in every part's game logs: right in all 8. Try 6 (288 games) re-read with the same scripts for the comparison.

## Verdict
The odds are still off. A promised charge is claimed at 87% and comes 18.8 times in 100 (try 6: 86% v 17.1). THE PROMISED MOVE halved the
plain moves that were not made (3.4 -> 1.8 per 100) but did nothing for marches (10.0 -> 10.3 per 100), which are most promises (184 of
282). The waiting loop is also still there (same charge put off again 5.0 per 100 v 4.3).

## 1. Promised charges, per 100 (claimed 87% v try 6 86%)
| | Try 8 (282, 3.6 a game) | Try 6 (1,394, 4.8 a game) |
| --- | --- | --- |
| Charged the promised target | 18.8 | 17.1 |
| Own move phase: promised move not made | 23.4 | 23.5 |
| - "spot not taken though worth more", march | 10.3 (29) | 10.0 (139) |
| - same, move | 1.8 (5) | 3.4 (48) |
| - another move worth more / charge gone from spot / not legal | 5.7 / 3.9 / 1.4 | 3.9 / 4.3 / 1.1 |
| Target moved in its turn | 13.8 | 11.3 |
| Target dead, fleeing or in a fight first | 10.3 | 15.1 |
| On offer next turn, not taken | 8.9 | 9.3 |
| - same charge put off again | 5.0 (14) | 4.3 (60) |
| Charged another target | 8.2 | 10.0 |
| Nothing moved, no charge listed | 7.8 | 3.4 |
| Own unit gone | 4.6 | 5.7 |
| Own figure at/below zero | 4.3 | 4.5 |
New-side rule rows: WAITS AGAIN 124, WOUNDS ON THE RANKS 105, FRIEND SHOOTS FIRST 31, THE PROMISED MOVE 21, SAME CHARGE LATER 12, FRIEND CHARGES FIRST 11.

## 2. Risk claimed v lost (a game)
| | Try 8 | Try 6 |
| --- | --- | --- |
| All picked jobs | 404 v 400 | 546 v 438 |
| Charges | 232 v 199 | 363 v 262 |
| Shots + magic | 243 v 177 | 287 v 153 |
| Shot claim, wound share 20%+ | 175 v 79 | 187 v 68 |
WOUNDS ON THE RANKS brought the shot claim down (try 7: 416 v 216); the charge risk is now close to what is lost.

## 3. Fights
| | New | Simpler | Try 6 new v simpler |
| --- | --- | --- | --- |
| Contact when the target held, claimed v made | 90 v 87 | 91 v 86 | 90 v 89 |
| First round won, claimed v happened | 70 v 71 | 58 v 73 | 72 v 76 |
| Net points per charged fight | +44 | +64 | +70 v +73 |

## 4. Headline (78 games: margins are noise)
| | New | Simpler | Try 6 |
| --- | --- | --- | --- |
| VP margin | -106 ±234 (W24 L35 D19) | | -110 ±128 |
| Charges declared a game | 3.2 | 4.5 | 3.9 v 4.9 |
| Charge picked when offered | 55% (230/420) | 76% (303/398) | 52% v 76% |
| Stand share of picks | 13% | | 13% |
| Points lost a game | 622 | 554 | 706 v 640 |
| Own units caught in flank/rear a game | 1.24 | 1.01 | 1.60 v 1.42 |

## Most likely next root cause
March promises: the promised march spot is still not taken in the move phase (29 of 34 "worth more, not taken"), at 10-18", inside
double M (Razorgors, lone characters, fliers). The move phase serves by the same five sum, and the spot it took is far lower, so the
promised spot was not in the served list. The logs cannot say which gate drops it: WithPromisedSpot's early returns for a march, or the
lane rules (LaneProblem marks the spot as a Problem; the withdrawal row's own legality test ignores lanes, so a lane refusal reads
"not taken though worth more"). Test board: L0222 (mine-2) turn 1, Razorgor 3 #12146, promised march to (34.6, 33.6) for #12161 at
31.8 VP, took the marker move at 11.1. Sent to the build thread by the coordinator.

Scripts: scripts/promise8.py (grouping as in the finding), verify8.py, analyse8.sh, pull8.sh, and the try 6/7 scripts.
