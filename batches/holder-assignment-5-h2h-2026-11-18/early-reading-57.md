# Holders batch 5 (8766b98a, feature / Herdstone / far markers by the odds, ON v OFF): reading at 57 games (2026-11-18 19:10 UTC)

**Verdict at 57 games: the special feature is fixed, and nothing is broken.** The ON side now ends with the feature as often as the OFF side. In batch 4 it trailed by a wide margin. The claims for standing on the feature, the Herdstone, baggage trains and quarters run 5-15% above what happens. Two things still do not work: walking on in the last turns, and walking to far markers. The VP margin is noise.

Switch side: 57 games; the ON side has 1,974 HOLDER ASSIGNMENT, 685 HOLD ODDS and 224 QUARTER ODDS rows, the OFF side 0. No game failed. The longest game took 10.7 min. Part 8 has not finished a game yet.

## Claimed v happened (ON side)

| | Batch 5 (57) | Batch 4 (97) | Batch 3 (288) |
| --- | --- | --- | --- |
| Special feature held at the end, ON v OFF | 17 v 16 of 36 | 21 v 35 of 63 | - |
| Feature, last row "holds it": claimed v scored | 210 v 178 VP (72% claimed, 16 of 23 held) | 20 of 39 held | - |
| Feature, last row "walks on" (all from round 4): held at the end | 1 of 8 (claimed 100% each time) | 1 of 18 | - |
| Feature, "holds it" lost to an OFF unit with the holder alive | 6 of 6 | 15 of 19 | - |
| Herdstone, last row "holds it": claimed v scored | 187 v 160 VP (10 of 15 held) | - | - |
| Herdstone, last row "walks on": held | 0 of 6 | - | - |
| Herdstone held at the end, ON v OFF | 11 v 14 of 25 | - | - |
| Own baggage train, last row round 5+: claimed v scored | 106 v 79 VP (holds 10 of 16, walks 0 of 6) | 98 v 74 | - |
| Quarter claims (146 units): controlled / more than twice / uncontested, claimed v happened | 64 v 61% / 47 v 44% / 27 v 23% | not in log | - |
| Far marker walks ("arrives in 2+ turns", 73): claimed arrival | 93% | - | - |
| ... the same unit scored it | 1 | - | - |
| ... ON scored it by the claimed turn (any unit) | 14 | - | - |
| ... the same unit sent there again the next turn | 16 of 73 | - | - |
| Far markers never scored by the side, ON v OFF | 63% v 61% | - | 59% v 63% |

## VP a game, ON v OFF

| | Diff |
| --- | --- |
| Special feature | +4 ±39 (batch 4 -29 ±30) |
| Herdstone | -11 ±34 |
| Baggage held | +14 ±18 |
| Quarters | +17 ±69 |
| Markers | -20 ±70 (batch 3 +17 ±26) |
| Hill | -11 ±55 |
| **VP margin** | **-37 ±266 (27 won, 30 lost): noise at 57 games** |

Time: 5.9 min a game (batch 4 5.9, batch 3 7.5).

## Leads (not checked in code)

- **Far markers:** the plan is drawn up again each turn, and a walk to a far marker is kept only 16 times in 73. The 93% arrival claim
  is for a walk that is almost never carried out. Lead: nothing in the table holds a far walk on the next turn.
- **Walks on to the feature in the last turns** claim 100% held and score 1 of 8; Herdstone walks score 0 of 6 (their row does not
  match my pattern; needs a look).
Script: scripts/a5.py.
