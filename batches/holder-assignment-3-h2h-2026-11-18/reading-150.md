# Holders batch 3 (HOLD ODDS, head efe7e340): reading at 150 games (2026-11-18 14:50 UTC)

Verdict so far: no gain, and the marker gain of batch 2 is gone. Claims are now close to what happens: a hold claims 71-77 VP and
scores 62-64 over the same three moments. Named holders still score that round 81%. But markers are only +4 VP a game (batch 2 +25),
and walk-ons are rare and almost never arrive (6% next round). Far markers are not left empty more often on the new side (58% v 63%).
VP margin **-19 ±172** (58 won, 59 lost, 33 drawn): noise.

Switch side checked in all 150 games: HOLDER ASSIGNMENT and HOLD ODDS rows on the ON side only. No failed or timed-out games.
Batch 2 at 288 games in brackets.

## Claimed v happened (ON side)

| | Batch 3 (150) | (Batch 2, 288) |
| --- | --- | --- |
| Marker, "holds it this turn": scored that round / next round | 81% / 60% (880 rows) | (78% / 61%) |
| Marker, "walks on to it": that round / next round | 1% / 6% (70 rows) | (1% / 9%, 358 rows) |
| Hill, "holds it this turn": that round / next | 64% / 33% (55) | (51% / 28%) |
| Hill, "walks on to it": that round / next | 0% / 12% (24) | (2% / 14%) |
| Hold row: claimed VP v scored, the claim's three moments (job_claims3.py) | 71-77 v 62-64 | (not measured) |
| Hold row: claimed VP v scored, first two moments only (as batch 2) | 71-77 v 45-46 | (88-90 v 42-44) |

## Objectives (ON v OFF, VP a game)

| | Diff | (Batch 2) |
| --- | --- | --- |
| Markers | +4 ±38 | (+25 ±28) |
| Marker player-turns scored ON v OFF | 33% v 33% | (34% v 32%) |
| Hill | -11 ±32 | (-8) |
| Table quarters | -29 ±43 | (-12 ±34) |
| Special feature (end) | +19 ±23 | (-4) |
| Herdstone (end) | -3 ±13 | (-2) |
| Baggage held (end) | +6 ±9 | (+17 ±8) |
| All objective VP | -14 | (+12) |
| Scored by the cheapest able unit, ON v OFF | 38% v 44% | (41% v 44%) |
| Units ending own turn within 6" of own baggage train | 5.1 v 4.3 | (4.3 v 4.0) |

## Far markers (ON v OFF; scripts/far.py)

A marker is "far" for a side when no non-character unit of that side can get within 6" of it in one move at the side's first turn
(reach = the longest single-turn move that unit made in the game). Most are the markers in the enemy's half.

| | ON | OFF |
| --- | --- | --- |
| Markers far at own first turn | 40% (169/423) | 39% (164/423) |
| of those, never scored by that side all game | 58% | 63% |
| of those, still far at every own turn start | 41% | 43% |
| Markers in reach at first turn: never scored all game | 25% | 25% |

So far: the "two or more turns away counts nothing" rule does not leave far markers empty more often than the old side does.

## Headline (ON v OFF)

| | Batch 3 (150) | (Batch 2, 288) |
| --- | --- | --- |
| VP margin | -19 ±172 (58 won, 59 lost, 33 drawn) | (+29 ±139) |
| Charges declared a game | 3.3 v 3.4 | (4.1 v 4.1) |
| First round won when charging, claimed v happened | 69% v 75% / 65% v 69% | (67% v 74% / 70% v 76%) |
| Net points per charged fight | +77 v +57 | (+81 v +79) |
| Points lost a game | 547 v 552 | (598 v 609) |
| Free units caught in flank/rear a game | 1.23 v 1.31 | (1.52 v 1.48) |
| Thinking time | 7.0 min a game, longest 13.3 | (7.3, longest 18.6) |

## Leads (from logs, not checked in code)

- Walk-ons fell from ~1.2 to ~0.5 a game and still arrive only 6% of the time: the table now sends fewer units, but those it sends
  still mostly do not get there the next round.
- Markers +4 v batch 2's +25 at about the same ±: may be the slice of pairs played so far; read again at 288.
- Table quarters stay behind (-29 ±43), as in both earlier batches; the table does not assign quarters (a planning question already open).
