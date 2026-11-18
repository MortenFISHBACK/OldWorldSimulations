# Holders batch 6 (0333a160, walk promise + quarter rulings + buffs by the odds, ON v OFF): final report at 67 games (2026-11-18)

**Stopped by the coordinator at 20:46 UTC with 67 of 288 games (34 Mine ON, 33 Opponent ON): the walk fault is unchanged.**

**Nothing is BROKEN.** No crash, stall or time limit (average 6.1 min, longest 14.3). Holder rows on the ON side only in all 8 parts
(HOLDER ASSIGNMENT 2,273 / HOLD ODDS 913 / QUARTER ODDS 498 rows, 0 on the OFF side; WALK PROMISE rows ON side only).

**Verdict:** the walk fix does not work. A unit the table sends to a marker claims 94% to arrive; it moves about half the ground
needed and almost never arrives. Standing claims (feature, baggage) come true. Quarter claims now run 4-13 points LOW.

Build 0333a160 on branch claude/project-thread-bj3s5r. OFF side: `holder-assignment`, `quarter-odds`, `walk-promise` off. Same pairs
as batches 3-5. Of the 67 games, 40 are Domination, 40 have a special feature, 32 a Herdstone.

## Claimed v happened (ON side)

| | Batch 6 (67) | Batch 5 (76) |
| --- | --- | --- |
| Marker walk, 1 more turn: claims / claimed arrival | 59 / 94% | - |
| ... that unit scored it by the claimed turn | **13 of 59** | - |
| Marker walk, 2+ more turns (far): claims / claimed arrival | 76 / 94% | 106 / 93% |
| ... that unit scored it by the claimed turn | **3 of 76** | 1 of 106 |
| ... next turn: same unit still sent / passed to another unit / left empty | 13 / 36 / 24 | 22 / - / - |
| ... the claim already "a turn later" (of those by WALK PROMISE) | 35 (6) | - |
| Ground moved toward the marker this turn: median v share needed | **3-4" v 6.8"** (covered 13 of 135) | 25 of 180 |
| Special feature held at the end, ON v OFF | **21 v 15 of 40** | 22 v 21 of 47 |
| Feature, last row "holds": held / claimed v scored | 20 of 24 / 231 v 233 VP | 21 of 32 / 215 v 177 |
| Feature, last row "walks on": held | 1 of 6 | 1 of 8 |
| Herdstone held at the end, ON v OFF | 13 v 15 of 32 | 11 v 16 of 29 |
| Herdstone, last row "holds": held / claimed v scored | 13 of 23 / 190 v 140 VP | 10 of 18 / 160 v 123 |
| Herdstone, last row "walks on": held | 0 of 4 | 0 of 6 |
| Own baggage train round 5+: holds held / walks held / claimed v scored | 20 of 23 / 0 of 5 / 100 v 80 | 14 of 22 / 0 of 7 / 102 v 75 |
| Quarters (279 claims): controlled / more than twice / uncontested, claimed v happened | 63 v 76% / 49 v 61% / 27 v 31% | 65 v 61% / 50 v 46% / 30 v 23% |

## The 140 walk claims to a marker: what the unit did instead (move phase, same turn)

The move TAKEN, by the label of its MOVE SPLIT row (the build notes say that row's figures are the old parts, so only its label and
its rank in CANDIDATES MOVE are used):

| Move taken | Near (1 more turn), 64 | Far (2+ more turns), 76 |
| --- | --- | --- |
| Onto that marker | 6 | 6 |
| Onto another objective (feature, other marker, baggage train) | 18 | 32 |
| Toward or against an enemy (charge reach, shot spot, "towards the nearest enemy") | 21 | 15 |
| A spot the wider search found | 9 | 9 |
| Other (stay, step back, ...) | 10 | 14 |
| A move row onto that marker was weighed at all | 33 | 32 |
| The taken row was the top row of CANDIDATES MOVE | 45 | 57 |

The strategy phase picked "march by the five-action sum" (76) or "move by the five-action sum" (64) every time.

## Who holds at the end, and VP

- Marker player-turns scored: ON 33%, OFF 33%, nobody 35%.
- Domination quarters a game: controlled 2.08 v 1.82, more than twice 1.52 v 1.55, uncontested 0.82 v 1.02.
- **VP margin ON-OFF +72 ±228 (35 won, 32 lost): noise.**

## Leads (not checked in code)

- **The marker's worth rides on moves that do not go there.** In 58 of the 140 the taken move was NOT onto the marker, yet its
  "later" part still counted that marker ("Marker 1 (top) in 1 more turn", often with NEARER NOT NEEDED), e.g. L0432 turn 2
  Hobgoblin Cutthroats 2 "stay [TAKEN]: later +45.0 ... (Marker 1 (top) in 1 more turn)". If every move gets the walk's worth, the
  walk adds nothing to the move that carries it out, and the tie goes to whatever else the move is worth. Fits the 3-4" moved.
- In more than half the walks (75 of 140) no move row onto that marker was among the rows weighed at all.
- Quarters now under-claim: enemy units that "could walk in" are mostly counted at 100%.

Scripts in scripts/: walks6.py, walkmoves6.py (new), a5.py, a4.py, markers.py, far.py.
Parts stopped at 7, 10, 11, 6, 10, 10, 6, 7 games.
