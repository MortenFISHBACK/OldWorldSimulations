# Try 10: army table + fixed holders + joint charges against true simpler - stopped at 254 games (2026-11-18)

Build ba3e30a3 (branch claude/project-thread-1btznt). New side: everything on (army-wide move table steps 1-2, fixed holders,
joint charges step 3). Simpler side: worked-out-chances, five-action, standing-by-numbers off. Same pairs as try 9, both ways,
static-static, seed 1, scenarios mix. Switch side checked in the game logs of all 8 parts: ARMY TABLE and JOINT CHARGE NOW rows on the
new side only. **Stopped by the coordinator at 14:55 UTC** (254 of 288; the fixed head 4d2ef4228 gets try 11). One game stalled
(L1633, opp-3: sim bug S-d31045, new: no move found for Hounds of Orion after a combat), so VP counts 253 games. Try 9 (119 games)
in brackets.

## Verdict
Better than try 9, but the odds are still off. A promised charge is claimed at 85 and comes 19.2 times in 100 (86 v 15.1). The promised
march left though worth more fell to 3.4 per 100 (10.4), but more promises now end with "charge gone from the spot reached" (11.9 per
100, try 9 3.7). The charge pick over-claims as before: 169 VP claimed v +53 net a fight (simpler 92 v +61). Joint sets over-claim
reach: all in 80% claimed v both in 59%. The new side still charges less (4.2 v 4.7 a game) with fewer second chargers (0.52 v 0.92).
VP +29 ±149: the first green margin of the overhaul, inside the noise, carried by objectives (+45).

## 1. Promised charges, per 100 (1,095 promises, 4.3 a game)
| | Try 10 | (Try 9) |
| --- | --- | --- |
| Claimed | 85 | (86) |
| Charged the promised target | 19.2 | (15.1) |
| Own move phase: promised move not made | 25.4 | (20.0) |
| - promised MARCH spot not taken though worth more | 3.4 (37) | (10.4) |
| - promised plain MOVE spot not taken though worth more | 0.5 (5) | (1.2) |
| - charge gone from the spot reached | 11.9 (130) | (3.7) |
| - spot no longer legal / another move worth more | 4.7 / 4.6 | (1.7 / 2.5) |
| Target dead, fleeing or in a fight first | 13.4 | (12.9) |
| Target moved in its turn | 12.7 | (13.9) |
| Charged another target | 10.0 | (13.4) |
| Own unit gone | 6.4 | (7.7) |
| On offer next turn, not taken / same charge put off again | 5.2 / 1.9 | (6.2 / 2.7) |
| Own figure at/below zero | 3.2 | (2.7) |

## 2. Charges and joint fights (a game)
| | New | Simpler |
| --- | --- | --- |
| Charges declared | 4.2 (3.6) | 4.7 (4.6) |
| - alone / lead / second or later | 3.17 / 0.47 / 0.52 (second 0.54) | 3.03 / 0.75 / 0.92 (second 1.43) |
| Charge picked when offered | 65% (56%) | 78% (76%) |
| Ready pairs (2+ units with a charge on one target): both charged | 0.43 of 1.90 | 0.53 of 2.24 |
| Joint fights: first round won, claimed v won | 77 v 70 (89 fights) | 67 v 80 (147; best single unit's figure) |
| Joint fights: net points over 2 turns | +63 | +48 |
| JOINT CHARGE NOW: rows / sets | 1.03 a game / 100 sets | - |
| - all in claimed v both in | 80% v 59% | - |
| - first round won with both in, claimed v won | 76 v 68 (57 sets) | - |
| - kills less own losses, claimed v net | +176 v +64 (87) | - |
| JOINT ON THE TABLE rows / friend behind charged that target | 20 / 13 | - |

## 3. New measures (new side, 254 games)
| | Count | A game |
| --- | --- | --- |
| Same ground: a friend gives way (the dearer sum keeps its plan) | 641 | 2.52 |
| Move ends in a friend's line of fire (dearer sum) | 171 | 0.67 |
| Move order changed: crossing paths / move ends in a friend's path | 103 / 405 | 0.41 / 1.59 |
| Pair priced below the lead alone (JOINT CHARGE NOW "joint ~X against ~Y without it", X < Y) | 34 of 261 rows | 0.13 |
| Joiner's own figure below its own fight alone (row CHANGED) | 89 of 261 | 0.35 |
| Charges halted short by a unit in the way (new v simpler) | 36 v 34 | 0.14 v 0.13 |
| - in a set of 2+ chargers on that target (chargers blocking each other) | 10 v 8 | 0.04 v 0.03 |
| BLOCKED CHARGE SKIPPED (friend in the way of landing on every roll) | 4 v 10 | |
(Try 9 and batch A had no "marches refused for same ground" rows: these rows are new in this build.)

## 4. Odds, risk, fights
| | New | Simpler |
| --- | --- | --- |
| Contact when the target held, claimed v made | 90 v 86 (87 v 80) | 89 v 86 (90 v 88) |
| First round won, claimed v happened | 76 v 74 (67 v 75) | 66 v 74 (63 v 69) |
| Charge pick: claimed VP v net points 2 turns | 169 v +53 (148 v +46) | 92 v +61 (92 v +52) |
| Net points per charged fight | +74 (+68) | +72 (+65) |
| Risk of picked jobs, claimed v lost a game | 429 v 390 (510 v 429) | 738 v 452 (808 v 397) |
| - enemy charges / shots claimed (new) | 284 / 201 | |
| Shoot pick: claimed VP v VP of wounds done | 44 v 6 | 21 v 6 |

## 5. Headline
| | New | Simpler |
| --- | --- | --- |
| VP margin (253 games) | +29 ±149 (W107 L99 D47) (-168 ±190) | |
| VP by source | objectives +45, kills -12, leaders -4 | |
| Points lost a game | 658 (661) | 649 (581) |
| Own units caught in flank/rear a game | 1.66 (1.34) | 1.55 (1.08) |
| Game length (whole game, both sides) | 7.8 min | |
Thinking time per side is not in the logs; only the whole game's length.

## Leads (from the logs only, not checked in code)
- The promise loss moved from "march not made" to "charge gone from the spot reached" (130 of 1,095). LEAD: the march is made, but
  the spot's charge seems judged against where the target stood when the promise was made.
- Joint sets: all in 80% claimed v 59% happened. In 3 of the first 9 JOINT ON THE TABLE sets the friend behind was halted by the lead
  itself (L0118 R4, L0332 R3, L0206 R2). The joint-charges build reports these gone on 5ec7da7d (WHO GETS IN).
- 89 of 261 JOINT CHARGE NOW rows lower the joiner's own figure to join (e.g. smoke L0717: +44 v +92 "instead of its own fight
  alone"). LEAD: may be right when the set is worth more, or the joint sum under-prices.
- Shoot picks still claim seven times the wounds they do (44 v 6 VP); simpler claims 21 v 6.

Scripts in scripts/: analyse10.sh + try 9's (report.py now skips unfinished games), promise9.py, joint/joint.py, m10.py (section 3).
Readings: early-reading-54.md, reading-156.md.

## Where things are
- Replays: WarhammerOldWorldSimulator branch claude/project-thread-aves0y a0351a4c (deploy/sim-replays/t10-<mine|opp>-ba3e30a-p1..4,
  on-site.txt = only these 8); they show on the test site after the next push to main.
- Sim bugs: S-d31045 (L1633, Hounds of Orion: no move found after a combat, game stalled) and S-fef937 (L0210, Jade Lancers set-up
  position; already listed as a sim bug without a thread).
- Archive: OldWorldSimulations branch claude/project-thread-aves0y (8 part tarballs, 254 games, verified by blob hash).
- Game logs (batch.tgz per part) STAY on the mount until the coordinator says the analysis "Find why promised charges vanish" is done.
