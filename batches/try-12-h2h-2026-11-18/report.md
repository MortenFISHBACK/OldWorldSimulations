# Try 12, final reading at 85 games (2026-11-18 19:15 UTC) - stopped by Morten at 19:04 UTC

Head 9ffac812. New side = everything on; simpler = worked-out-chances, five-action, standing-by-numbers off. Switch side checked in all 8 parts.
Try 11 (167 games) in brackets.

## Verdict
Nothing is BROKEN: 85 of 85 games ended, 0 crashes, 0 sim findings, longest game 17 min (3 side by side). No side plays clearly worse:
VP -17 ±220 (noise), new side loses a little more in kills (-55 VP) and wins on objectives (+44).
Promised charge comes has NOT moved: claimed 85, came 24.7 in 100 (85 v 21.5). The table now binds the move phase (promised move not made
1.3 in 100, was 26.1), so the loss moved to the enemy's turn: target moved 20.4 (14.0), target dead, fleeing or in a fight first 21.0 (11.3).
Heads B and C (his one move, honest waits) address that; try 13 tests them.

## 1. Promised charges, per 100 (372 promises, 4.4 a game)
| | Try 12 | (Try 11) |
| --- | --- | --- |
| Claimed / charged the promised target | 85 / 24.7 | (85 / 21.5) |
| Own move phase: promised move not made | 1.3 | (26.1) |
| Target moved in its turn | 20.4 | (14.0) |
| Target dead, fleeing or in a fight first | 21.0 | (11.3) |
| Charged another target | 10.2 | (9.4) |
| On offer next turn, not taken / nothing moved yet none listed | 6.7 / 6.5 | |
| Own unit dead, fleeing, charged or pinned | 5.1 | |
| Own figure at/below zero | 4.0 | (2.8) |
| Promise rows kept v withdrawn | 367 v 5 | |

## 2. The new rows (new side, a game)
| | |
| --- | --- |
| THE TABLE AGAIN: rows / units priced again / rows changed | 6.0 / 42.1 / 7.9 |
| THE TABLE AGAIN: thinking time | 75 s a game |
| SHOTS AFTER THE MOVES: rows / shoot rows priced again / changed | 2.8 / 8.0 / 0.6 |
| SHOTS AFTER THE MOVES: thinking time | 13 s a game |
| THE TABLE BINDS: rows carried out | 28.7 |
| Whole game, both sides (wall clock, 3 games side by side) | 7.4 min (6.6 at 153) |
Total thinking time per side is not written in the logs; only these two rows carry seconds.

## 3. Charges and joint sets (a game)
| | New | Simpler |
| --- | --- | --- |
| Charges declared | 3.3 | 3.8 |
| - second or later on the same target | 0.42 | 0.86 |
| Contact made by declared charges | 69% (73%) | 71% (68%) |
| JOINT CHARGE NOW sets (25): all in claimed v both in | 77% v 64% (63 v 64) | - |
| - first round won with both in, claimed v won | 80 v 75 (n 16) | - |
| First round won, claimed v happened | 72 v 71 | 61 v 72 |
| Charge pick: claimed VP v net points 2 turns | 191 v +39 (174 v +62) | 89 v +53 (87 v +46) |
| Net points per charged fight | +65 (+85) | +74 (+76) |
| Risk of picked jobs, claimed v lost | 367 v 326 | 641 v 389 |

## 4. Holds (claimed v scored this turn and the enemy's next; NOT the same measure as try 11's three moments)
| | New | Simpler |
| --- | --- | --- |
| New as Mine | 101 v 26 (10.2 a game) | 81 v 23 |
| New as Opponent | 106 v 27 (12.4 a game) | 99 v 29 |
The new side's holds are read from HOLDER ASSIGNMENT rows (rebuilt script); both sides over-claim by this measure.

## 5. Headline (85 games)
| | New | Simpler |
| --- | --- | --- |
| VP margin | -17 ±220 (W36 L30 D19); objectives +44, kills -55 | |
| Points lost a game | 554 | 518 |

## Leads (from the logs only, not checked in code)
- Promises are now lost in the enemy's turn (target moves or is killed/caught first). LEAD: the assumed enemy move does not match his real one.
- The charge pick over-claims more than in try 11 (191 v +39). LEAD only.
