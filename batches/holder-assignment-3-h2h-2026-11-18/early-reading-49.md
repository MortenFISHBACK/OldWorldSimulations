# Holders batch 3 (HOLD ODDS, head efe7e340): reading at 49 games (2026-11-18 14:05 UTC)

Verdict so far: same picture as batch 2, nothing worse. Named holders still score that round 81% of the time; walk-ons are now rare
(21 in 49 games) and still score the next round only 10%. The hold claim fell from ~89 to ~77 VP but is still well above what is scored.
Far markers are NOT left empty more often on the new side (60% v 70% never scored). VP margin **+26 ±277: noise at 49 games.**

Switch side checked in all 49 games: HOLDER ASSIGNMENT and HOLD ODDS rows on the ON side only (parts 1-4 Mine, 5-8 Opponent).
No failed or timed-out games. Batch 2 at 288 games in brackets.

## Claimed v happened (ON side)

| | Batch 3 (49) | (Batch 2, 288) |
| --- | --- | --- |
| Marker, "holds it this turn": scored that round / next round | 81% / 63% (286 rows) | (78% / 61%) |
| Marker, "walks on to it": that round / next round | 0% / 10% (21 rows) | (1% / 9%, 358 rows) |
| Hill, "holds it this turn": that round / next | 44% / 22% (18) | (51% / 28%) |
| Hold row: claimed VP v scored this turn + enemy's next | 75-79 v 43-47 | (88-90 v 42-44) |
| Hold row: claimed VP v scored over the claim's three moments (+ own next turn; scripts/job_claims3.py, added 14:10 UTC) | 75-79 v 60-67 | (not measured) |

Note on the hold row: the new claim covers three moments (now, enemy's turn end, our next turn end); the "scored" column counts only the
first two (a scoring script limit, max 60). So part of the gap is the measure, not the claim.

## Objectives (ON v OFF, VP a game)

| | Diff | (Batch 2) |
| --- | --- | --- |
| Markers | +26 ±66 | (+25 ±28) |
| Marker player-turns scored ON v OFF | 34% v 31% | (34% v 32%) |
| Hill | -12 ±45 | (-8) |
| Table quarters | -45 ±85 | (-12 ±34) |
| Special feature (end) | +29 ±42 | (-4) |
| Herdstone (end) | -8 ±41 | (-2) |
| Baggage held (end) | +4 ±20 | (+17 ±8) |
| Scored by the cheapest able unit, ON v OFF | 32% v 39% | (41% v 44%) |
| Units ending own turn within 6" of own baggage train | 5.0 v 4.4 | (4.3 v 4.0) |

## Far markers (ON v OFF; new script far.py)

A marker is "far" for a side when no non-character unit of that side can get within 6" of it in one move at the side's first turn
(reach = the longest single-turn move that unit made in the game).

| | ON | OFF |
| --- | --- | --- |
| Markers far at own first turn | 37% (53/144) | 33% (47/144) |
| of those, never scored by that side all game | 60% | 70% |
| of those, still far at every own turn start | 45% | 47% |
| Markers in reach at first turn: never scored all game | 26% | 28% |

## Headline (ON v OFF)

| | Batch 3 (49) | (Batch 2, 288) |
| --- | --- | --- |
| VP margin | +26 ±277 (19 won, 20 lost, 10 drawn) | (+29 ±139) |
| Charges declared a game | 3.0 v 2.5 | (4.1 v 4.1) |
| First round won when charging, claimed v happened | 63% v 72% / 62% v 57% | (67% v 74% / 70% v 76%) |
| Net points per charged fight | +92 v +47 | (+81 v +79) |
| Points lost a game | 424 v 453 | (598 v 609) |
| Free units caught in flank/rear a game | 0.82 v 1.27 | (1.52 v 1.48) |
| Thinking time | 6.5 min a game, longest 12.3 | (7.3, longest 18.6) |

Leads only (not checked in code): fewer walk-ons is what the ruling says should happen (two or more turns away counts 0); the first
49 pairs are not a random slice of the 144, so charges, points lost and flank figures may move by 150.
