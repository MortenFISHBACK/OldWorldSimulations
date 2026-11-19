# Holders batch 8 (6ec093ab, risk on the way), ON against OFF - report (2026-11-19)

**Verdict: the walk fault is UNCHANGED, so the batch was stopped.** The coordinator stopped it at 23:48 UTC under Morten's standing
rule, after the 68-game reading. 80 of 288 games were played. Nothing broke: no crashes, all 8 parts played the right side,
0 wrong-side rows, 5.6 min a game. RISK ON THE WAY prices each stop of a walk as built (107 claims, median 80% not charged off on
the way). Even so, walkers still do not get to their marker. Quarters and the special feature stay right.
VP margin ON-OFF -55 ±184 (won 36, lost 43, drawn 1): noise.

## Claimed v happened (ON side, 80 games)

| Objective | Claims | Claimed | Happened | Batch 7 |
| --- | --- | --- | --- | --- |
| Far marker walks (2+ turns) | 86 | 89% arrive | that unit scored on time 9 (10%), ever 10 | 7 of 83 |
| Near marker walks (1 turn) | 90 | 93% | on time 17 (19%), ever 29 | 12 of 42 |
| Herdstone, last row "walks" | 4 games | 86% | held 0 | 0 of 6 |
| Own baggage train walks, round 5+ | 7 | - | held 0 | 0 of 5 |
| Special feature, last row "holds" | 28 games | 94% / 255 VP | held 18, 222 VP | 86% / 218 v 15, 231 |
| Herdstone, last row "holds" | 21 games | 99% / 291 VP | held 15, 185 VP | 99% / 271 v 14, 218 |
| Quarters controlled / twice / uncontested | 348 | 71 / 57 / 36% | 73 / 58 / 27% | 68/57/33 v 66/55/27 |

Feature ends ON 22 v OFF 19 of 46 games. Herdstone ON 16 v OFF 13 of 32. Far walkers moved 2.7" toward the marker a turn (median)
where 6.0" was needed.

## The new rows

WALK FOLLOW-UP: what happened the turn after, for each walker the table sent (233 walkers):

| Next turn | Count |
| --- | --- |
| the same unit keeps the marker | 60 (26%; batch 7 33 of 141 = 23%) |
| the marker goes to another unit | 89 |
| the marker stays empty | 84 |
| the walker has NO row for it ("picks no job this turn, or no spot of its move holds it or gets nearer it") | 100 |
| the walker has a row, and its net fell 30+ VP | 54 of 132 |

WALK CHECK (511 move rows, for units the table sent to an objective they are not on):

| | Count |
| --- | --- |
| the spot nearest the objective ranked 1st | 260 |
| the move taken = that nearest spot | 294 |
| taken elsewhere | 217 |
| the nearest spot carries no walk | 68 |

Give way, then stand still: ON 89 of 200 give-ways, OFF 75 of 211 (batch 7 ON 63 of 144). The build said this has a separate cause
that this head does not fix.

## Leads for the root-cause analysis (to check in code, not findings)

1. The biggest part of the drop: the turn after, 100 of 233 walkers have no table row for their marker at all. The table does not
   offer them the marker any more, which is different from pricing it lower. Why (the job choice, or no spot of its move counted
   as getting nearer) is for the analysis to read.
2. In 217 of 511 WALK CHECKs the move taken is not the spot nearest the objective, and in 68 that nearest spot carries no walk.
3. Claims stay at 89-93% arrive while about 10-19% happen, and the gap is about the same as batches 6 and 7. RISK ON THE WAY lowered
   the claimed survival (median 80%), but the walk usually ends because the table drops it, not because the enemy charges it off.

## Where the data is

- Every WALK CHECK and WALK FOLLOW-UP row (ON side, 80 games, with game, part, turn, unit and full text): `walk-rows.tsv` in this
  folder (744 rows), made by scripts/rows8.py.
- Early reading: early-reading-68.md. Scripts (python3 -I <script> <root holding mine-N/ and opp-N/ folders): walks6.py, a5.py,
  a4.py, giveway7.py, credit7.py, fu8.py (follow-up kinds), fu8b.py (net now v last turn), wc8.py (walk checks), rows8.py.
- Replays: WarhammerOldWorldSimulator branch claude/project-thread-rjpfen, commit e4e685d9 (on 6ec093ab): deploy/sim-replays/
  h8-mine-6ec093a-p1..4 and h8-opp-6ec093a-p1..4 (80 games). on-site.txt lists these 8.
- Logs: archived to OldWorldSimulations, branch claude/project-thread-rjpfen (never merged to its main), folder
  batches/holder-assignment-8-h2h-2026-11-18/ (<arm>-N.tar.gz, one per part; SHA256SUMS; FILECOUNTS.txt).
