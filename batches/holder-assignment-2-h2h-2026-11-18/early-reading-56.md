# Holders batch 2 (head 83c90997): reading at 56 games (2026-11-18 11:30 UTC)

Verdict so far: the fixed table does what it says a little more often, and the ON side leads, but every figure is still noise at 56 games.
The holder named "holds it this turn" scores that marker that round 81% (first batch 78%); a holder that "walks on to it" scores
2% that round and 16% the round after. Marker VP +55 a game (first batch +28), table quarters still behind (-37 ±72). VP margin +80 ±220.

## Claimed v happened (ON side; scripts/extra.py, assigned.py, repo job_claims.py)

| | Batch 2 | Batch 1 (168 games) |
| --- | --- | --- |
| Marker, "holds it this turn": scored that round / next round | 81% / 63% (344 rows) | 78% / 60% |
| Marker, "walks on to it": scored that round / next round | 2% / 16% (56) | 0% / 10% |
| Hill, "holds it this turn": that round / next | 61% / 33% (18) | 49% / 23% |
| Hill, "walks on to it": that round / next | 0% / 27% (11) | 0% / 5% |
| Per-unit holder row: marker / hill holder scored that round | 70% / 38% | 65% / 24% |
| job_claims Hold row: claimed VP v VP scored (this turn + enemy's next) | 84-93 v 44-47 | (did not read) |

## Objectives (ON v OFF)

| | Batch 2 ON | OFF | Batch 1 ON | OFF |
| --- | --- | --- | --- | --- |
| Marker player-turns scored (nobody 32%; batch 1 33%) | 37% | 32% | 35% | 32% |
| Marker VP a game | 378 | 323 | 340 | 313 |
| Hill VP a game | 46 | 52 | 46 | 49 |
| Table quarters VP a game | 200 | 237 | 199 | 231 |
| Special feature / Herdstone / baggage held (end) | 50 / 32 / 32 | 61 / 43 / 13 | 47 / 18 / 14 | 57 / 10 / 15 |
| Scored by the cheapest able unit alive | 39% | 41% | 42% | 46% |
| Points of the scoring unit, mean (median) | 277 (139) | 248 (137) | 227 (171) | 220 (164) |
| Units ending own turn within 6" of own baggage train, a game | 3.9 | 3.6 | 4.7 | 4.3 |

All objective VP ON minus OFF: +2 a game (batch 1 -12).

## Headline (ON v OFF)

| | Batch 2 | Batch 1 |
| --- | --- | --- |
| Charges declared a game | 2.5 v 3.1 | 3.7 v 3.4 |
| First round won when charging, claimed v happened | 64% v 70% / 68% v 75% | 65% v 76% / 67% v 76% |
| Net points per charged fight | +60 v +62 | +81 v +77 |
| Points lost a game | 464 v 516 | 581 v 576 |
| Free units caught in flank/rear a game | 1.07 v 0.79 | 1.25 v 1.27 |
| Thinking time | 6.3 min a game, longest 11.8, no failures | 6.4, longest 12.8 |

VP margin ON v OFF: **+80 ±220** (23 won, 20 lost, 13 drawn); kills +68, objectives +2, leaders +11. Noise at 56 games.

Leads only (from logs, not checked in code): the charge drop on the ON side (2.5 v 3.1) and fewer charges on both sides than batch 1
may be just the first 56 pairs; read again at 150. Cheaper holders still not chosen more often; the baggage-train figure has not dropped.
