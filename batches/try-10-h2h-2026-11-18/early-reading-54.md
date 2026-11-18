# Try 10, early reading at 54 games (2026-11-18 13:50 UTC)

Build ba3e30a3 (claude/project-thread-1btznt): army table steps 1-2, fixed holders, joint charges step 3. New side = everything on;
simpler side = worked-out-chances, five-action, standing-by-numbers off. Same pairs as try 9. Switch side right in all parts so far
(ARMY TABLE, HOLDER ASSIGNMENT, JOINT CHARGE NOW rows on the new side only). Parts 1, 6 and 7 started ~45 min late (nudged): the 54
games lean to parts 2-5 and 8. Try 9 (119 games) in brackets. 54 games is early: VP margin is noise.

## Verdict
Better than try 9 on the promises, not fixed. A promised charge is claimed at 82% and comes 20.9 times in 100 (try 9: 86 v 15.1).
The promised march spot left though worth more halves: 5.3 per 100 (10.4). The new side still charges less (3.4 v 4.5 a game) and
brings fewer second chargers than simpler (0.57 v 1.19 a game). Joint charges over-claim: both in 57% against 74% claimed, and
first round won with both in 50% against 73% claimed (12 sets, small). JOINT ON THE TABLE does fire in play (9 rows).

## 1. Promised charges, per 100 (187 promises, 3.5 a game)
| | Try 10 | (Try 9) |
| --- | --- | --- |
| Claimed | 82 | (86) |
| Charged the promised target | 20.9 | (15.1) |
| Own move phase: promised move not made | 26.7 | (20.0) |
| - promised MARCH spot not taken though worth more | 5.3 (10) | (10.4) |
| - charge gone from the spot / spot not legal | 10.2 / 6.4 | (3.7 / 1.7) |
| Target moved in its turn | 13.4 | (13.9) |
| Charged another target | 4.3 | (13.4) |
| On offer next turn, not taken | 8.6 | (6.2) |

## 2. Charges, joint fights (a game, new v simpler)
| | New | Simpler |
| --- | --- | --- |
| Charges declared | 3.4 (3.6) | 4.5 (4.6) |
| - second or later charger on the same target | 0.57 (0.54) | 1.19 (1.43) |
| Charge picked when offered | 61% (56%) | 80% (76%) |
| Joint fights: first round won claimed v won | 73 v 67 (24) | 65 v 74 (38; best single unit's figure) |
| Joint fights: net points | +59 | +44 |
| JOINT CHARGE NOW rows / sets | 1.04 / 21 sets | - |
| - all in claimed v both in | 74% v 57% | - |
| - first round won with both in, claimed v won | 73 v 50 (12) | - |
| - claimed: kills less own losses v net | +101 v +64 (19) | - |
| JOINT ON THE TABLE rows | 9 (friend behind charged the target in 6) | - |

## 3. New measures (a game, new side)
| | Count | A game |
| --- | --- | --- |
| A friend gives way on the same ground (dearer sum keeps its plan) | 109 | 2.0 |
| Move ends in a friend's line of fire | 29 | 0.5 |
| Move order changed: crossing paths / ends in a path | 19 / 78 | 0.35 / 1.44 |
| Joint figure below the lead alone | 9 of 56 rows | 0.17 |
| Joiner's own figure below its fight alone (row says CHANGED) | 22 of 56 | 0.41 |
| Charges halted short by a unit in the way (new v simpler) | 10 v 5 | 0.19 v 0.09 |
| - of these in a set of 2+ chargers on the target | 4 v 1 | |

## 4. Odds, risk, fights
| | New | Simpler |
| --- | --- | --- |
| Contact when the target held, claimed v made | 90 v 86 (87 v 80) | 89 v 90 (90 v 88) |
| First round won, claimed v happened | 77 v 71 (67 v 75) | 65 v 75 (63 v 69) |
| Charge pick: claimed VP v net points 2 turns | 145 v +43 (148 v +46) | 95 v +66 (92 v +52) |
| Net points per charged fight | +85 (+68) | +84 (+65) |
| Risk of picked jobs, claimed v lost a game | 438 v 319 (510 v 429) | 660 v 423 (808 v 397) |

## 5. Headline (54 games)
| | New | Simpler |
| --- | --- | --- |
| VP margin | -18 ±277 (W24 L23 D7): noise at 54 | |
| Points lost a game | 533 (661) | 529 (581) |
| Own units caught in flank/rear a game | 1.57 (1.34) | 1.31 (1.08) |
| Game length (whole game, both sides) | 7.4 min | |

## Leads (from the logs only, not checked in code)
- In two JOINT ON THE TABLE sets the friend behind was halted by the lead itself ("blocked short of contact, X is in the way"):
  L0118 round 4 (Maneaters behind Gnoblar Fighters 2), L0332 round 3 (Exalted Champion behind Marauder Horsemen 1). Same in L0206 R2
  (Chaos Warhounds blocked by Tuskgor Chariot 1). LEAD: the landing room for the second charger is still not checked against the lead's end.
- A JOINT ON THE TABLE row claims +502 VP for Ironblaster 1 behind Gnoblar Fighters 3 (L0118 R5): LEAD, a large figure to look at.
- 22 of 56 JOINT CHARGE NOW rows lower the joiner's own figure ("CHANGED: +44 v +92 instead of its own fight alone", smoke L0717):
  the joiner gives up a better fight of its own to join. LEAD: could be right (set worth more) or the joint sum under-pricing.
- Thinking time per side is not in the logs; only the whole game's minutes.
Scripts: scripts/m10.py (section 3), scripts/joint/joint.py (section 2), try 9's scripts for the rest (analyse10.sh).
