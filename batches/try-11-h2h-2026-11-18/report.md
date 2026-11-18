# Try 11: army table + holders by the odds + joint charges that find room, against true simpler - stopped at 167 games (2026-11-18)

Build 4d2ef422 (branch claude/project-thread-60g6hv). New side: everything on (try 10's head + promise reads the table, support worked
out, WHO GETS IN, HOLD ODDS, a joint set priced for the units that find room to land, joint look back). Simpler side: worked-out-chances,
five-action, standing-by-numbers off. Same pairs as tries 9 and 10, both ways, static-static, seed 1, scenarios mix. Switch side checked
in the game logs of all 8 parts (ARMY TABLE, HOLD ODDS, JOINT CHARGE NOW on the new side only). **Stopped by the coordinator at 16:20
UTC** (167 of 288: promises unchanged, their root-cause fix is being built). Parts 1, 2, 6 started ~25 min late, so pairs from parts
3-5, 7-8 weigh more (part counts 16, 13, 25, 27 / 28, 13, 26, 19). No crashed or stalled games. Try 10 (254 games, its report) in brackets.

## Verdict
Two claims are now honest. Joint sets land as claimed: all in 63% claimed v both in 64% (80 v 59). Holds score close to their claim:
claimed 78-83 v scored 64-71 over the same three moments (simpler 73-84 v 31-40). Promises have not moved: claimed 85, came 21.5 in 100
(85 v 19.2). The charge pick still over-claims: 174 VP claimed v +62 net (simpler 87 v +46). VP +35 ±167, inside the noise (try 10
+29 ±149), carried by objectives (+44).

## 1. Promised charges, per 100 (648 promises, 3.9 a game)
| | Try 11 | (Try 10) |
| --- | --- | --- |
| Claimed / charged the promised target | 85 / 21.5 | (85 / 19.2) |
| Own move phase: promised move not made | 27.6 | |
| - promised march left though worth more | 3.5 (23) | (3.4) |
| - charge gone from the spot reached | 12.5 | (11.9) |
| - spot no longer legal / another move worth more | 5.7 / 4.8 | |
| Target moved in its turn | 14.7 | |
| Target dead, fleeing or in a fight first | 11.9 | |
| Charged another target | 8.8 | |
| Own figure at/below zero | 2.5 | |

## 2. Charges and joint sets (a game)
| | New | Simpler |
| --- | --- | --- |
| Charges declared | 3.7 (4.2) | 4.2 (4.7) |
| - second or later on the same target | 0.50 (0.52) | 0.92 (0.92) |
| Charge picked when offered | 67% | 76% |
| JOINT CHARGE NOW sets: all in claimed v both in | 63% v 64% (80 v 59) | - |
| - first round won with both in, claimed v won | 76 v 66 | - |
| - kills less own losses, claimed v net | +176 v +62 | - |
| Joint fights: first round won claimed v won / net points | 76 v 62 / +74 | 62 v 84 / +49 (best single unit's figure) |
| WHO GETS IN rows / JOINT LOOK BACK joins / PROMISE READS THE TABLE rows | 37 / 1 / 11 in 167 games | - |
| Second charger halted by a friend in its own set | 4 in 167 games (try 10 5 in 156) | - |

## 3. Odds, risk, holds
| | New | Simpler |
| --- | --- | --- |
| Declared charges that made contact | 73% | 69% |
| First round won, claimed v happened | 75 v 72 | 64 v 76 |
| Charge pick: claimed VP v net points 2 turns | 174 v +62 (169 v +53) | 87 v +46 (92 v +61) |
| Net points per charged fight | +85 | +76 |
| Risk of picked jobs, claimed v lost a game | 472 v 398 | 800 v 463 |
| Hold row: claimed v scored, three moments (new as Mine / as Opponent) | 78 v 71 / 83 v 64 | 84 v 40 / 73 v 31 |

## 4. Headline (167 games)
| | New | Simpler |
| --- | --- | --- |
| VP margin | +35 ±167 (W63 L59 D45), noise; objectives +44, kills -6, leaders -1 | |
| Points lost a game | 632 | 628 |
| Own units caught in flank/rear a game | 1.34 | 1.28 |
| Game length (whole game, both sides) | 6.6 min (try 10 7.3) | |

## Leads (from the logs only)
- Second chargers that declare without room: 3 of the 4 halted by a friend in their own set had a WHO GETS IN row saying they would land
  0-33% (L0230 R5, L0926 R2, L0725 R5), yet declared. The coordinator reports this is confirmed in code and fixed in the joint charges build.
- JOINT LOOK BACK joined once in 167 games. LEAD, not checked in code: its condition is seldom met.
- Promises: the biggest losses are still "charge gone from the spot reached" (12.5) and "target moved in its turn" (14.7) per 100.
- Thinking time per side is not in the logs; only the whole game's length.

## Replays and archive
- Replays: WarhammerOldWorldSimulator branch `claude/project-thread-ch2rk0` (f0feddd4), deploy/sim-replays/t11-{mine,opp}-4d2ef42-p1..p4
  (167 games, 0 findings); on-site.txt lists these 8. They reach the test site's replay page when the branch is merged to main.
- Game logs: OldWorldSimulations branch `claude/project-thread-ch2rk0`, batches/try-11-h2h-2026-11-18/ (one tar.gz per part + SHA256SUMS).
