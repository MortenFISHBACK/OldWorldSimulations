# Try 13, final reading at 54 games (2026-11-18 20:05 UTC) - stopped at 19:57 UTC (known fault unchanged at 50)

Head 24f3d18eb (A + B his-one-move + C promise-by-its-own-sum, second-look). New side = everything on; simpler = worked-out-chances,
five-action, standing-by-numbers off. Switch side checked from the game logs of all 8 parts and in a smoke game. Try 12 (85 games) in brackets.

## Verdict
Nothing BROKEN: 54 of 54 games ended, 0 failed, 0 sim findings. New rows on the new side only.
Promised charges NOT fixed: claimed 91, came 23.1 in 100 (85 v 24.7). Promise by its own sum took 142 promises off (2.6 a game), so fewer are made
(2.7 a game v 4.4), but the share that comes did not move. The biggest loss is now "target dead, fleeing or in a fight first" (30.6),
and in 19 of its 45 cases OUR OWN other unit charged the target first.

## 1. Promised charges, per 100 (147 promises)
| What happened | Try 13 | (Try 12) |
| --- | --- | --- |
| Claimed / charged the promised target | 91 / 23.1 | (85 / 24.7) |
| Target dead, fleeing or in a fight first | 30.6 | (21.0) |
| Target moved in its turn | 15.6 | (20.4) |
| Charged another target | 15.0 | (10.2) |
| On offer next turn, not taken | 4.8 | (6.7) |
| Own figure at/below zero | 4.1 | (4.0) |
| Own move not made / own unit dead, fleeing, pinned | 2.7 / 2.7 | (1.3 / 5.1) |

### Who got to the target first (the 45 "dead, fleeing or in a fight")
| | count |
| --- | --- |
| Our other unit charged it first, at our next turn | 19 |
| Gone: our shooting or magic hit it | 8 |
| Gone: in a fight already going on | 8 |
| The target charged (its own action) | 6 |
| Gone with no hit by us seen (panic, own fault, other enemy action) | 4 |

## 2. His one move: assumed v what the enemy unit did in his turn (1,676 checks)
The row's own check ("as assumed" = ends within 1" of the assumed spot) says 348 (21%). By kind of action:
| Assumed (n) | charged | fled | marched | moved | shot | stood / nothing seen | row says as assumed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| charge (141) | 78 (70 same target) | 8 | 15 | 21 | 6 | 13 | 26 |
| march (474) | 37 | 25 | 179 | 78 | 41 | 114 | 48 |
| move (684) | 42 | 29 | 132 | 196 | 117 | 168 | 93 |
| stand (377) | 13 | 12 | 79 | 74 | 75 | 123 | 181 |
No flee or shoot is ever assumed (the action kinds are stand, move, march, charge). The assumed action is worked out with our army on the
ends of our table's moves (where we will be). Assumed charges that came in fights count as "not as assumed" by the row's check unless he
is in a fight; 70 of 141 charged the assumed target.

## 3. Promises taken off and second looks
| | |
| --- | --- |
| PROMISE BY ITS OWN SUM: promises taken off | 142 (2.6 a game) |
| Promises kept / withdrawn in the move phase | 143 / 4 |
| SECOND LOOK charges | 12 (0.2 a game): 9 contact (2 on another target), 1 halted, 1 short, 1 caught by a chase |
| - first round | 5 won, 2 drawn, 1 lost; net over 2 turns +43 a charge (n 12: noise) |

## 4. Joint and holds
| | New | Simpler |
| --- | --- | --- |
| JOINT CHARGE NOW sets: all in claimed v both in | 85% v 68% (77 v 64) | - |
| First round won, both in, claimed v won | 84 v 71 (n 14) | - |
| Holds as Mine: claimed v scored (this turn + enemy's next) | 107 v 24 | 73 v 21 |
| Holds as Opponent | 100 v 25 | 105 v 29 |

## 5. Thinking time (new side, a game)
| | |
| --- | --- |
| HIS ONE MOVE | 58 s |
| THE TABLE AGAIN | 139 s (75) |
| SHOTS AFTER THE MOVES | 12 s (13) |
| Whole game, both sides, wall clock | 9.7 min (7.4) |
PROMISE BY ITS OWN SUM and SECOND LOOK write no seconds.

## 6. Headline (54 games)
| | New | Simpler |
| --- | --- | --- |
| VP margin | -31 ±293 (W23 L19 D12) - noise; objectives -28, kills -7 | |
| First round won when charging, claimed v happened | 72 v 70 | 63 v 67 |
| Net points per charged fight | +61 (+65) | +93 (+74) |
| Charge pick: claimed VP v net 2 turns | 174 v +32 | 102 v +60 |
| Points lost a game | 508 | 498 |
| Free units caught in flank/rear a game | 1.50 | 1.15 |

## Leads (from the logs only, not checked in code)
- A promise is most often lost to our own army: another of our units charges the promised target first (19 of 147 promises).
- The enemy in these sims plays the simpler pricing, while his one move prices his action by our own sum: we may predict a different enemy than the one we face.
- THE TABLE AGAIN nearly doubled its thinking time (75 -> 139 s a game).

Scripts: scripts/all.sh (pull + all measures), promise10.py (with who got there first), hom.py (his one move by kind), rows.py.
Game logs stay in <arm>-N/batch.tgz on the mount until the analysis thread "Find why promised charges never come" is done.
