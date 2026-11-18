# Holders batch 5 (8766b98a, special feature / Herdstone / far markers by the odds, ON v OFF): final report at 76 games (2026-11-18)

**Stopped by Morten at 19:14 UTC with 76 of 288 games played (40 Mine ON, 36 Opponent ON).**

**Nothing is BROKEN.** No game crashed, stalled or hit the time limit. The longest game took 11.4 min, the average 6.0. The holder
rows appear only on the ON side: 2,624 HOLDER ASSIGNMENT, 929 HOLD ODDS and 290 QUARTER ODDS rows, against 0 on the OFF side. The ON
side does not play clearly worse. Every VP gap is inside its noise band. The largest is kills at -77 ±134, which is a lead and not a
fault.

**Verdict:** the special feature is fixed. The ON side now ends with it as often as the OFF side (22 v 21 of 47). In batch 4 it
trailed 21 v 35. Claims for standing on an objective run 5-20% above what happens. Two kinds of walk do not work: walking on to an
end-of-battle objective in the last turns, and walking to a far marker.

Build 8766b98a on branch claude/project-thread-bj3s5r. The OFF side runs with `holder-assignment` and `quarter-odds` off. These are
the same pairs as batches 3 and 4. Of the 76 games, 44 are Domination, 47 have a special feature and 29 a Herdstone.

## Claimed v happened (ON side)

| | Batch 5 (76) | Batch 4 (97) | Batch 3 (288) |
| --- | --- | --- | --- |
| Special feature held at the end, ON v OFF | **22 v 21 of 47** | 21 v 35 of 63 | - |
| Feature, last table row "holds it": held at the end | 21 of 32 (66%), claimed 73% | 20 of 39 (51%) | - |
| ... claimed v scored | 215 v 177 VP | (fixed 250-450 figure) | - |
| ... lost to an OFF unit, holder not in the enemy's VP list | 8 of 10 | 15 of 19 | - |
| Feature, last row "walks on" (all from round 4): held | **1 of 8** (each claimed 100%) | 1 of 18 | - |
| Herdstone held at the end, ON v OFF | 11 v 16 of 29 | - | - |
| Herdstone, last row "holds it": held / claimed v scored | 10 of 18 (claimed 64%) / 160 v 123 VP | - | - |
| Herdstone, last row "walks on": held | **0 of 6** | - | - |
| Own baggage train, last row round 5+: claimed v scored | 102 v 75 VP (holds 14 of 22, walks 0 of 7) | 98 v 74 | - |
| Quarter claims (191 units): controlled / more than twice / uncontested | 65 v 61% / 50 v 46% / 30 v 23% | not in log | - |
| Far marker walks ("arrives in 2+ turns"): rows / claimed arrival | 106 / 93% | - | - |
| ... same unit sent there again the next turn | **22 of 106** | - | - |
| ... the same unit scored it | **1** | - | - |
| ... ON scored it by the claimed turn (any unit) | 22 | - | - |
| Far markers (at first turn) never scored by the side, ON v OFF | 65% v 63% | - | 59% v 63% |
| Marker player-turns scored, ON v OFF | 32% v 34% | - | - |

## VP a game, ON v OFF

| | Batch 5 (76) | Batch 4 (97) | Batch 3 (288) |
| --- | --- | --- | --- |
| Special feature | +3 ±34 | -29 ±30 | +15 ±17 |
| Herdstone | -13 ±27 | +2 ±21 | -1 |
| Baggage held | +14 ±15 | +13 ±13 | +5 |
| Quarters | +5 ±59 | +7 ±44 | -13 ±35 |
| Markers | -23 ±59 | +10 ±49 | +17 ±26 |
| Hill | -7 ±45 | +4 ±42 | +4 |
| Kills | -77 ±134 | - | - |
| **VP margin** | **-98 ±219 (33 won, 43 lost): noise** | -36 ±178 | +27 ±143 |
| Minutes a game | 6.0 (longest 11.4) | 5.9 | 7.5 |

## Leads (not checked in code)

- **Far markers:** a walk to a marker two or more turns away claims 93% to arrive. The next turn's table sends the same unit there
  again only 22 times in 106, and that unit scored the marker once. The plan is redrawn every turn and nothing in it carries a far
  walk on. The holders build has this as the next root cause.
- **Walk-ons in the last turns** (feature and Herdstone) claim the end VP at 100% and score 1 of 14. Part of the cause can be seen in
  the code (read, not tested): when the computer plays second, `HeldAtTheEnd` counts the first moment at kept^0 = 100%. A walk that
  arrives in the last turn therefore claims 100% held, even if an enemy unit will stand nearer at the end (the out-stood chance is
  inside `kept`). Not checked further.
- Standing claims (feature, Herdstone, baggage) run 20-35 VP above what is scored. "Out-stood" is read from today's board, which is
  a limit already named in the hand-over.

Pending part: 8 parts stopped at 13, 3, 13, 11, 13, 12, 9 and 2 games. Script: scripts/a5.py (plus a4.py, eob2.py, far.py, markers.py).
