# Army-wide holders ON v OFF: reading at 155 games (2026-11-18 10:25 UTC)

Verdict so far: the switch does what it says on markers only a little (+17 marker VP a game) and costs more elsewhere: VP margin -35 ±163
(noise), objectives -21 VP a game overall. The assigned holder reaches and scores its marker 65% of the time; the hill 24%.
The cheapest able unit does NOT score more often on the on side (42% v 47%). Batch runs on to 288.

## Claimed v happened (turn table, on side; scripts/assigned.py)

| Assigned to | Assignments | Claimed (mean VP of the row) | Holder scored it that round |
| --- | --- | --- | --- |
| Marker | 1210 | 69 | 65% |
| The hill | 78 | 128 | 24% |
| Herdstone / special feature / baggage | 171 / 351 / 329 | - | not measured (scored at the end) |

## Objectives

| | ON | OFF |
| --- | --- | --- |
| Marker player-turns scored (nobody 32%; baseline 50%) | 35% | 33% |
| Marker VP a game | 339 | 318 |
| Hill VP a game | 48 | 52 |
| Objective VP a game, all kinds (end-of-battle included), ON minus OFF | -21 | |
| Points of the scoring unit, mean (median) | 231 (171) | 221 (164) |
| Scored by a 210+ unit | 38% | 37% |
| Scored by the cheapest able unit alive | 42% | 47% |

## Headline

| | ON | OFF |
| --- | --- | --- |
| Charges declared a game | 3.7 | 3.4 |
| First round won when charging (claimed v happened) | 66% v 78% | 66% v 75% |
| Net points per charged fight | +80 | +73 |
| Points lost a game | 577 | 569 |
| Free units caught in flank/rear a game | 1.23 | 1.28 |
| Thinking time | 6.4 min a game, longest 12.8, none timed out (smoke on v off 4.2 v 4.4) |

VP margin ON v OFF: -35 ±163 (51 won, 64 lost, 40 drawn): noise.

Leads only (not checked in code): markers +21 and hill/baggage -7 from per-turn rows leave about -35 a game on end-of-battle objectives
(special feature, Herdstone, baggage) - the ones the hand-over says use the old figure (5a, later); the table still assigns them 851 times.
"Gives up least" does not land on the cheapest unit; the hill holder rarely gets there.
