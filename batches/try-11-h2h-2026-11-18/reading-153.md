# Try 11, reading at 153 games (2026-11-18 16:25 UTC)

Build 4d2ef422. New side = everything on; simpler = worked-out-chances, five-action, standing-by-numbers off. Switch side checked in the
logs of all 8 parts (ARMY TABLE, HOLD ODDS, JOINT CHARGE NOW on the new side only). Parts 1, 2, 6 lag (started late). Try 10 at 156
games in brackets.

## Verdict
Two claims are now honest: joint sets land as claimed (all in 62% claimed v both in 62%; try 10 79 v 56), and holds score close to their
claim (claimed 80-84 v scored 65-71 over the same three moments; simpler 75-83 v 31-39). Promises have not moved: claimed 85, came 22.3 in
100 (85 v 20.6). The charge pick still over-claims (173 VP v net +58; simpler 86 v +53). VP -24 ±163: inside the noise, a little below
try 10's +32 ±182.

## 1. Promised charges, per 100 (564 promises, 3.7 a game)
| | Try 11 | (Try 10) |
| --- | --- | --- |
| Claimed / charged the promised target | 85 / 22.3 | (85 / 20.6) |
| Own move phase: promised move not made | 26.1 | (23.9) |
| - promised march left though worth more | 3.0 (17) | (3.7) |
| - charge gone from the spot / spot not legal / another move worth more | 12.2 / 5.1 / 4.4 | (11.4 / 3.7 / 4.1) |
| Target moved in its turn | 14.0 | (11.4) |
| Target dead, fleeing or in a fight first | 11.3 | (15.3) |
| Charged another target | 9.4 | (9.2) |
| Own figure at/below zero | 2.8 | (4.1) |

## 2. Charges and joint sets (a game)
| | New | Simpler |
| --- | --- | --- |
| Charges declared | 3.6 (3.7) | 4.1 (4.2) |
| - second or later on the same target | 0.49 (0.51) | 0.92 (0.90) |
| Charge picked when offered | 67% (64%) | 75% (78%) |
| JOINT CHARGE NOW sets: all in claimed v both in | 62% v 62% (79 v 56) | - |
| - first round won with both in, claimed v won | 75 v 65 (75 v 59) | - |
| - kills less own losses, claimed v net | +174 v +57 (+153 v +56) | - |
| Joint fights: net points | +69 (+47) | +70 (+28) |
| WHO GETS IN rows / JOINT LOOK BACK joins | 31 / 1 in 153 games | - |
| Second charger halted by a friend in its own set | 3 in 153 games (try 10: 5 in 156) | - |

## 3. Odds, risk, holds
| | New | Simpler |
| --- | --- | --- |
| Contact made by declared charges | 73% | 68% |
| First round won, claimed v happened | 75 v 72 (76 v 71) | 64 v 76 (65 v 74) |
| Charge pick: claimed VP v net points 2 turns | 173 v +58 (169 v +55) | 86 v +53 (91 v +57) |
| Net points per charged fight | +81 (+76) | +85 (+75) |
| Risk of picked jobs, claimed v lost a game | 460 v 386 (495 v 397) | 793 v 434 (766 v 458) |
| Hold row: claimed v scored, three moments (new as Mine / as Opponent) | 80 v 71 / 84 v 65 | 83 v 39 / 75 v 31 |

## 4. Headline (153 games)
| | New | Simpler |
| --- | --- | --- |
| VP margin | -24 ±163 (W54 L56 D43); objectives +21, kills -35, leaders -9 | |
| Points lost a game | 630 (622) | 601 (618) |
| Own units caught in flank/rear a game | 1.27 (1.43) | 1.25 (1.35) |
| Game length (whole game, both sides) | 6.6 min (7.3) | |

## Leads (from the logs only, not checked in code)
- All 3 halted second chargers had a WHO GETS IN row saying they would rarely or never land (L0230 R5 Razorgor 2 0%, L0926 R2 Vampire Lord
  0%, L0725 R5 Spirit Hosts 33%), yet they still declared. LEAD: the set is priced without the unit, but the unit itself is not told to
  stay out of the charge.
- JOINT LOOK BACK joined once in 153 games: it rarely fires. LEAD: its condition may seldom be met; not checked.
- Promises: the largest loss is still "charge gone from the spot reached" (12.2 per 100) and the target moving (14.0). Unchanged by
  PROMISE READS THE TABLE (8 rows in 153 games).
- Thinking time per side is not in the logs; the whole game is 6.6 min (try 10 7.3).
