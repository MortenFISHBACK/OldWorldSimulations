# Holders batch 2 (head 83c90997): reading at 150 games (2026-11-18 11:58 UTC)

Verdict so far: no gain, same picture as batch 1. The holder that "holds it this turn" scores 80% that round (batch 1 78%), but
walk-ons still rarely pay (10% next round) and the claim is about twice what is scored. Markers +25 VP a game, table quarters -49 ±43
(the one source near its limit), all objectives -28, VP margin -4 ±170 (noise). Running on to 288.

## Claimed v happened (ON side; scripts/extra.py, assigned.py, repo job_claims.py)

| | Batch 2 | Batch 1 (168) |
| --- | --- | --- |
| Marker, "holds it this turn": scored that round / next round | 80% / 62% (883 rows) | 78% / 60% |
| Marker, "walks on to it": that round / next round | 2% / 10% (176) | 0% / 10% |
| Hill, "holds it this turn": that round / next | 62% / 34% (53) | 49% / 23% |
| Hill, "walks on to it": that round / next | 0% / 15% (41) | 0% / 5% |
| Per-unit holder row: marker / hill holder scored that round | 67% / 35% | 65% / 24% |
| job_claims Hold row: claimed VP v VP scored (this turn + enemy's next) | 87-92 v 44-46 | (did not read) |

Why the claim is about twice (claims-check-56.md, build thread, checked in code): the hold figure is 30 VP for up to three own turns
less half the lose chance (two fixed numbers), measured here over two player turns; and walk-ons are not owed the next turn.

## Objectives (ON v OFF)

| | Batch 2 ON | OFF | Batch 1 ON | OFF |
| --- | --- | --- | --- | --- |
| Marker player-turns scored (nobody 33%) | 35% | 32% | 35% | 32% |
| Marker VP a game | 329 | 304 | 340 | 313 |
| Hill VP a game | 58 | 66 | 46 | 49 |
| Table quarters VP a game | 178 | 227 | 199 | 231 |
| Special feature / Herdstone / baggage held (end) | 50 / 13 / 29 | 52 / 17 / 13 | 47 / 18 / 14 | 57 / 10 / 15 |
| All objective VP a game, ON minus OFF | -28 | | -12 | |
| Scored by the cheapest able unit alive | 40% | 44% | 42% | 46% |
| Points of the scoring unit, mean (median) | 238 (171) | 226 (168) | 227 (171) | 220 (164) |
| Units ending own turn within 6" of own baggage train, a game | 4.7 | 4.1 | 4.7 | 4.3 |

## Headline (ON v OFF)

| | Batch 2 | Batch 1 |
| --- | --- | --- |
| Charges declared a game | 3.4 v 3.6 | 3.7 v 3.4 |
| First round won when charging, claimed v happened | 64% v 76% / 71% v 79% | 65% v 76% / 67% v 76% |
| Net points per charged fight | +73 v +74 | +81 v +77 |
| Points lost a game | 564 v 576 | 581 v 576 |
| Free units caught in flank/rear a game | 1.29 v 1.15 | 1.25 v 1.27 |
| Thinking time | 6.7 min a game, longest 16.8, no failures | 6.4, longest 12.8 |

VP margin ON v OFF: **-4 ±170** (59 won, 55 lost, 36 drawn); objectives -28, kills +24. Noise.

Leads only (logs, not code): quarters -49 ±43 is the one gap near its limit; the table sends units to baggage trains and markers and
none count quarters (batch 1 said the same: -32 ±38). The baggage-train figure the build expected to fall did not (4.7 v 4.1).
