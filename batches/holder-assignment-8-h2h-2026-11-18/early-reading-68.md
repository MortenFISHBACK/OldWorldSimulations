# Holders batch 8 (6ec093ab, risk on the way), reading at 68 games (23:50 UTC)

**Verdict: the known walk fault is UNCHANGED. Nothing broken** (no crashes, all 8 parts on the right side, 0 wrong-side rows,
5.7 min a game). RISK ON THE WAY works as built (90 claims priced, median 79% not charged off) but walkers still do not arrive.
VP margin ON-OFF -67 ±196 (31 won, 36 lost): noise.

## Claimed v happened (ON side)

| Objective | Claims | Claimed | Happened (batch 7 for comparison) |
| --- | --- | --- | --- |
| Far marker walks (2+ turns) | 65 | 89% arrive | that unit scored it on time 6 (9%), ever 7 (b7: 4 of 60) |
| Near marker walks (1 turn) | 69 | 93% | scored on time 16 (23%), ever 23 (b7: 12 of 42) |
| Special feature, last row "holds" | 26 games | 94% / 250 VP | held 17, 225 VP |
| Special feature, last row "walks" | 5 games | 86% / 172 VP | held 1, 40 VP |
| Herdstone, last row "holds" | 21 games | 99% / 291 VP | held 15, 185 VP |
| Herdstone, last row "walks" | 4 games | 86% / 173 VP | held 0 |
| Own baggage train round 5+ | 18 holds, 6 walks | 101 VP | 55 VP (walks 0 of 6) |
| Quarters controlled / twice / uncontested | 260 | 67 / 54 / 36% | 72 / 56 / 27% (b7 claimed 67/54/32 v 65/53/29) |

Feature ends ON 20 v OFF 19 of 43 games. Herdstone ON 16 v OFF 13 of 32.

## The new rows

WALK FOLLOW-UP (188 walkers, the turn after the table sent them):

| Next turn | Count |
| --- | --- |
| same unit keeps the marker | 49 (26%; b7 33 of 141 = 23%) |
| marker goes to another unit | 70 |
| marker stays empty | 69 |
| walker has NO row for it at all ("picks no job, or no spot of its move holds it or gets nearer it") | 85 |
| walker has a row, net fell 30+ VP | 39 of 103 |

Far walkers move 3.0" toward the marker a turn (median) where 6.1" is needed (b7 2.9 v 5.9).

WALK CHECK (423 move rows for units the table sent to an objective they are not on): the spot nearest it ranked 1st 218, taken 244;
taken elsewhere 179; the nearest spot carries no walk 58.

## Leads for the build (to check in code, not findings)

1. The biggest single part of the drop is the walker having no table row at all the turn after (85 of 188): the table does not
   offer that unit the marker any more, rather than pricing it lower. Why (job choice, or no spot of its move counted as getting nearer)
   is for the build to read.
2. In 179 of 423 WALK CHECKs the taken move is not the spot nearest the given objective, and in 58 that nearest spot carries no walk.
3. Give way then stand still: ON 72 of 157 give-ways (b7 63 of 144); OFF 62 of 185. Not this fix (the build said so).

Scripts in scripts/: walks6.py, a5.py, a4.py, giveway7.py, credit7.py, fu8.py, fu8b.py, wc8.py (python3 -I <script> <root>).
