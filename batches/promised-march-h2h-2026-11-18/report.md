# Try 9: promised marches against simpler pricing - stopped at 119 games (2026-11-18)

Build e62ea8a60 (branch claude/project-thread-60g6hv). New side: everything on, incl. the new march-by-the-sum, fight-to-the-end,
the-dearer-sum-keeps-its-plan, and a charge priced two or more turns out now counts the target's reform. Simpler side:
worked-out-chances, five-action, standing-by-numbers off. Same pairs both ways. Stopped by Morten at 08:39 UTC. Switch side checked in
all 8 parts' game logs: right in every one. Same scripts as try 8 (plus scripts/promise9.py, which splits march and move).

## Verdict
The odds are still off, and the promised marches are still not made. A promised charge is claimed at 86% and comes 15.1 times in 100
(try 8: 87% v 18.8). The promised march spot not taken though worth more: 10.4 per 100 (try 8 10.3). MARCH BY THE SUM fired only 39
times in 119 games. Fight-to-the-end did not worsen the fights: net points per charged fight +68 v simpler +65 (try 8 +44 v +64).

## 1. Promised charges, per 100 (404 promises, 3.4 a game)
| | Try 9 | Try 8 (78 games) |
| --- | --- | --- |
| Claimed | 86 | 87 |
| Charged the promised target | 15.1 | 18.8 |
| Own move phase: promised move not made | 20.0 | 23.4 |
| - promised MARCH spot not taken though worth more | 10.4 (42) | 10.3 (29) |
| - promised plain MOVE spot not taken though worth more | 1.2 (5) | 1.8 (5) |
| - another move worth more / charge gone from spot / not legal | 2.5 / 3.7 / 1.7 | 5.7 / 3.9 / 1.4 |
| Target moved in its turn | 13.9 | 13.8 |
| Charged another target | 13.4 | 8.2 |
| Target dead, fleeing or in a fight first | 12.9 | 10.3 |
| Nothing moved, no charge listed | 8.2 | 7.8 |
| Own unit gone | 7.7 | 4.6 |
| On offer next turn, not taken | 6.2 | 8.9 |
| - same charge put off again | 2.7 (11) | 5.0 (14) |
| Own figure at/below zero | 2.7 | 4.3 |
New-side rule rows: THE DEARER SUM KEEPS ITS PLAN 484, WAITS AGAIN 161, WOUNDS ON THE RANKS 151, FIGHT TO THE END 145, THE PROMISED MOVE 43,
MARCH BY THE SUM 39, FRIEND SHOOTS FIRST 37, FRIEND CHARGES FIRST 15, SAME CHARGE LATER 10.

## 2. Risk claimed v lost (a game)
| | New | Simpler | Try 8 new |
| --- | --- | --- | --- |
| All picked jobs | 510 v 429 | 808 v 397 | 404 v 400 |
| Enemy charges, claimed v lost when charged | 252 v 220 | (no split) | 232 v 199 |
| Shots + magic | 322 v 187 | (no split) | 243 v 177 |

## 3. Fights
| | New | Simpler | Try 8 new v simpler |
| --- | --- | --- | --- |
| Contact when the target held, claimed v made | 87 v 80 | 90 v 88 | 90 v 87 / 91 v 86 |
| First round won, claimed v happened | 67 v 75 | 63 v 69 | 70 v 71 / 58 v 73 |
| Charge pick: claimed VP v net points over 2 turns | 148 v +46 | 92 v +52 | |
| Net points per charged fight | +68 | +65 | +44 v +64 |

## 4. Headline (119 games)
| | New | Simpler | Try 8 |
| --- | --- | --- | --- |
| VP margin | -168 ±190 (W40 L47 D32) | | -106 ±234 |
| Charges declared a game | 3.6 | 4.6 | 3.2 v 4.5 |
| Charge picked when offered | 56% (383/680) | 76% (501/663) | 55% v 76% |
| Points lost a game | 661 | 581 | 622 v 554 |
| Own units caught in flank/rear a game | 1.34 | 1.08 | 1.24 v 1.01 |

## Leads (from the logs only; the analysis thread "Find why promised marches are not made" verifies)
The withdrawal rows say the promised march spot was "not taken though it is worth more by the same sum", often by a wide margin
(Razorgor 3: ~26.0 VP at the promised march spot v ~7.8 for the spot taken; a unit promised on Chaos Warhounds: ~23.5 v ~0.0).
MARCH BY THE SUM fires rarely, so the march check is seldom the gate; the promised march spot seems still missing from what the move
phase serves, as in try 8. Contact when the target held fell on the new side (80% made v 87% claimed; dice short 12% v 7%).

Scripts: scripts/promise9.py, analyse9.sh, pull9.sh and the try 8 scripts. Game logs stay on the mount for the analysis thread.
