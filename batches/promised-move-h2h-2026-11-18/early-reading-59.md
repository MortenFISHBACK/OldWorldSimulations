# Try 8 (44aac6ae1) at 59 games, 07:19 UTC - check against try 6 (288)

Switch side right in all 8 parts (rules-off and every new-only row on the new side only). Counting: scripts/promise8.py, run on both
batches the same way (try 6 re-read from the archive with it: 23.5 / 17.1 / 11.3 ... close to the finding's 22.7 / 17.7 / 11.3).

## 1. Promised charges per 100 (claimed 86% both)
| | Try 8 (226) | Try 6 (1,394) |
| --- | --- | --- |
| Promises a game | 3.8 | 4.8 |
| Charged the promised target | 16.8 | 17.1 |
| Own move phase: promised move not made | 24.8 | 23.5 |
| - of it "spot not taken though worth more" | 12.8 (29) | 13.4 (187) |
| -- march promises | 11.5 (26) | 7.4 (103) |
| -- move promises | 1.3 (3) | 2.9 (41) |
| Target moved in its turn | 13.3 | 11.3 |
| Target dead/fleeing/in a fight first | 11.1 | 15.1 |
| On offer next turn, not taken | 9.7 | 9.3 |
| - same charge put off again | 4.9 (11 of 22) | 4.3 (60 of 129) |
| Charged another target | 8.4 | 10.0 |
| Nothing moved, no charge listed | 7.5 | 3.4 |
| Own figure at/below zero | 4.4 | 4.5 |
| Own unit gone | 4.0 | 5.7 |
New-side rows: WAITS AGAIN 103, WOUNDS ON THE RANKS 81, FRIEND SHOOTS FIRST 26, THE PROMISED MOVE 19, SAME CHARGE LATER 11, FRIEND CHARGES FIRST 9.

## 2. Risk claimed v lost (a game)
| | Try 8 | Try 6 |
| --- | --- | --- |
| Charges | 231 v 192 | 363 v 262 |
| Shots + magic | 238 v 167 | 287 v 153 |
| Shot claim, wound share 20%+ | 172 v 78 | 187 v 68 |

## 3-4. Fights and headline
| | New | Simpler | Try 6 new v simpler |
| --- | --- | --- | --- |
| Contact when target held, claimed v made | 90 v 86 | 91 v 86 | 90 v 89 |
| First round won, claimed v happened | 70 v 70 | 58 v 72 | 72 v 76 |
| Net points per charged fight | +54 | +57 | +70 v +73 |
| Charges declared a game | 3.3 | 4.7 | 3.9 v 4.9 |
| Charge picked when offered | 55% (182/330) | 79% (246/312) | 52% v 76% |
| Stand share of picks | 12% | | 13% |
| Points lost a game | 591 | 554 | 706 v 640 |
| Own units caught flank/rear a game | 1.25 | 1.07 | 1.60 v 1.42 |
VP margin -37 ±281 (W21 L25 D13): noise at 59 games (try 6 final -110 ±128).

## Root cause (most likely next)
THE PROMISED MOVE fixed plain moves (spot not taken 2.9 -> 1.3 per 100) but not MARCHES (7.4 -> 11.5): 26 of the 29 "worth more, not
taken" cases are march promises, mostly 10-18" marches well inside double M (Razorgors, lone characters, fliers). In these the move
phase's list (ranked by the same five sum) shows lower spots taken, so the promised march spot was not in the served list. The logs
cannot say which gate dropped it: WithPromisedSpot's early returns for a march, or the lane rules (LaneProblem marks it as a Problem;
the withdrawal row's own legality test does not include lane rules, so a lane refusal reads as "not taken though worth more"). A test
on one of these boards settles it, e.g. L0222 mine-2 turn 1 Razorgor 3 (#12146): promised march to (34.6, 33.6) for #12161, 31.8 VP v
the marker move taken at 11.1. Second: the waiting loop is not gone (same charge put off again 11 of 22 on offer, despite WAITS AGAIN).
