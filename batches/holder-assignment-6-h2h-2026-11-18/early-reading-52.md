# Holders batch 6 (0333a160, walk promise + quarter rulings + buffs by the odds, ON v OFF): first reading at 52 games (2026-11-18 20:45 UTC)

**Nothing is BROKEN.** No crash, stall or time limit (average 6.2 min, longest 14.3). Holder rows on the ON side only in all 8 parts
(HOLDER ASSIGNMENT 1,825 / HOLD ODDS 723 / QUARTER ODDS 372 / WALK PROMISE 21 rows, 0 on the OFF side).

**Verdict: the walk fix does not work yet.** Units claimed to walk to a marker move about half the ground the claim needs, and the
far ones almost never arrive. Standing claims (feature, baggage) now come true. Quarter claims now run LOW.

## Claimed v happened (ON side)

| | Batch 6 (52) | Batch 5 (76) |
| --- | --- | --- |
| Walk, 1 more turn: claims / claimed arrival | 47 / 94% | - |
| ... that unit scored the marker by the claimed turn | **12 of 47** | - |
| Walk, 2+ more turns (far): claims / claimed arrival | 62 / 94% | 106 / 93% |
| ... that unit scored it by the claimed turn | **3 of 62** | 1 of 106 |
| ... next turn: same unit still sent / passed to another unit / left empty | 10 / 31 / 18 | 22 / - / - |
| ... claim already "a turn later" (WALK PROMISE) | 29 (5) | - |
| Ground moved toward the marker this turn, all walks: median v needed | **3.0-3.6" v 6.8"** (covered its share 12 of 109) | 25 of 180 |
| Special feature held at the end, ON v OFF | **19 v 11 of 32** | 22 v 21 of 47 |
| Feature, last row "holds": held / claimed v scored | 18 of 20 / 251 v 253 VP | 21 of 32 / 215 v 177 |
| Feature, last row "walks on": held | 1 of 4 | 1 of 8 |
| Herdstone held at the end, ON v OFF | 13 v 14 of 31 | 11 v 16 of 29 |
| Herdstone, last row "holds": held / claimed v scored | 13 of 22 / 199 v 147 VP | 10 of 18 / 160 v 123 |
| Herdstone, last row "walks on": held | 0 of 4 | 0 of 6 |
| Own baggage train round 5+: holds held / walks held / claimed v scored | 15 of 18 / 0 of 5 / 100 v 75 | 14 of 22 / 0 of 7 / 102 v 75 |
| Quarters (211 claims): controlled / more than twice / uncontested, claimed v happened | 59 v 75% / 41 v 59% / 21 v 28% | 65 v 61% / 50 v 46% / 30 v 23% |

## Who holds at the end, and VP

- Marker player-turns scored: ON 32%, OFF 33%, nobody 35%. Far markers at first turn never scored: 62% both sides.
- Domination quarters a game: controlled 1.94 v 1.94, more than twice 1.41 v 1.66, uncontested 0.72 v 1.16.
- **VP margin ON-OFF -16 ±248 (26 won, 26 lost): noise.**

## Leads (not checked in code)

- Walks: in the move phase the move TAKEN by a unit whose table row walks it to a marker was "onto that marker" in 11 of 114; 43 went
  onto another objective, 28 toward an enemy, 32 to another spot. Read from the MOVE SPLIT line's label (the build notes say its
  figures are the old parts, so only the label is used here). The walk the table claims and the move the unit makes look like two
  different decisions.
- Quarters now under-claim by 7-18 points: enemy units that "could walk in" are counted at 100% in most rows seen; they may not come.

Scripts: scripts/walks6.py (new), a5.py, a4.py, markers.py, far.py.
