# Try 13, first reading at 50 games (2026-11-18 20:00 UTC)

Head 24f3d18eb (A+B+C). New side = everything on; simpler = worked-out-chances, five-action, standing-by-numbers off. Try 12 (85 games) in brackets.

## Verdict
Nothing BROKEN: 50/50 games ended, 0 failed, 0 sim findings; new rows on the new side only in every part (checked from the logs of all 8 parts).
Promised charges are NOT fixed: claimed 91, came 22.6 in 100 (85 v 24.7). Promise by its own sum took off 135 promises (2.7 a game), so fewer
promises are made, but the share that comes did not move. LEAD (not checked in code): the one assumed enemy action matched what the enemy did
only 21% of the time, and an assumed enemy charge came 17% of the time.

## Promised charges, per 100 (137 promises, 2.7 a game; try 12 4.4)
| | Try 13 | (Try 12) |
| --- | --- | --- |
| Claimed / charged the promised target | 91 / 22.6 | (85 / 24.7) |
| Target dead, fleeing or in a fight first | 30.7 | (21.0) |
| Target moved in its turn | 16.8 | (20.4) |
| Charged another target | 13.9 | (10.2) |
| On offer next turn, not taken | 5.1 | (6.7) |
| Own figure at/below zero | 4.4 | (4.0) |
| Own move not made / own unit dead, fleeing, pinned | 2.9 / 2.9 | (1.3 / 5.1) |

## His one move: assumed v what the enemy did (1,529 checks)
| Assumed | as assumed | not |
| --- | --- | --- |
| stand | 169 | 168 |
| move | 81 | 539 |
| march | 43 | 400 |
| charge | 22 | 107 |
| all | 315 (21%) | 1,214 |

## Second look: 10 charges (0.2 a game)
8 made contact (2 of them hit another target than the one looked at), 1 halted, 1 short. First round: 3 won, 2 drawn, 1 lost.
Net over 2 turns +25 a charge (n 10: noise).

## Joint and holds
| | New | Simpler |
| --- | --- | --- |
| JOINT CHARGE NOW: all in claimed v both in | 85% v 67% (77 v 64) | - |
| First round won, both in, claimed v won | 83 v 73 (n 11) | - |
| Holds as Mine: claimed v scored | 105 v 25 | 73 v 23 |
| Holds as Opponent | 101 v 25 | 109 v 29 |

## Thinking time (new side, a game)
| | |
| --- | --- |
| HIS ONE MOVE | 57 s |
| THE TABLE AGAIN | 137 s (75) |
| SHOTS AFTER THE MOVES | 12 s (13) |
| Whole game, both sides, wall clock | 9.6 min (7.4) |
PROMISE BY ITS OWN SUM and SECOND LOOK write no seconds.

## Headline
| | New | Simpler |
| --- | --- | --- |
| VP margin | -36 ±297 (W21 L17 D12) - noise | |
| First round won when charging, claimed v happened | 71 v 70 | 63 v 68 |
| Net points per charged fight | +62 (+65) | +90 (+74) |
| Charge pick: claimed VP v net 2 turns | 172 v +36 | 103 v +58 |
| Points lost a game | 505 | 477 |
| Free units caught in flank/rear a game | 1.54 | 1.06 |
