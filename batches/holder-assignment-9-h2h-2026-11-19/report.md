# Holders batch 9 (81fb82cd, one route), ON against OFF - report (2026-11-19)

**Verdict: the walk fault is UNCHANGED, so the batch was stopped.** The coordinator stopped it at 02:24 UTC under Morten's standing
rule, after the 57-game reading. 70 of 288 games were played. Nothing broke: no crashes, all 8 parts played the right side (rules-off
9 tags on the off side, holder rows on the ON side only), 5.9 min a game (median 5.5, max 11.8; batch 8 5.6), so the slow-down the
build warned of did not show. Quarters, the special feature and the Herdstone holds stay near their claims.
VP margin ON-OFF -198 ±232 (won 24, lost 46): noise at this size, though on the losing side for the third batch running.

## Claimed v happened (ON side, 70 games)

| Objective | Claims | Claimed | Happened | Batch 8 |
| --- | --- | --- | --- | --- |
| Far marker walks (2+ turns) | 78 | 86% arrive | that unit scored on time 6 (8%), ever 8 | 9 of 86 (10%) |
| Near marker walks (1 turn) | 44 | 92% | on time 10 (23%), ever 22 | 17 of 90 (19%) |
| Herdstone, last row "walks" | 5 games | 96% / 192 VP | held 0 | 0 of 4 |
| Feature, last row "walks" | 4 games | 66% / 132 VP | held 0 | - |
| Own baggage train walks, round 5+ | 0 | - | - | 0 of 7 |
| Special feature, last row "holds" | 24 games | 91% / 258 VP | held 17, 238 VP | 94% / 255 v 18, 222 |
| Herdstone, last row "holds" | 15 games | 92% / 223 VP | held 11, 180 VP | 99% / 291 v 15, 185 |
| Own baggage train holds, round 5+ | 23 | 96 VP | held 17, 70 VP | - |
| Quarters controlled / twice / uncontested | 289 | 73 / 60 / 35% | 67 / 52 / 34% | 71/57/36 v 73/58/27 |

Inches: far walkers moved 2.8" toward the marker a turn (median) where 5.3" was needed (20 of 78 covered their share; 10 did not move).
Near walkers 4.7" v 6.3". Batch 8 far: 2.7" v 6.0".

## The turn after (WALK FOLLOW-UP, 164 walkers)

| Next turn | Count |
| --- | --- |
| the same unit keeps the marker | 46 (28%; batch 8 26%) |
| the marker goes to another unit | 50 |
| the marker stays empty | 68 |
| the walker has NO row for it (counted apart from the three above) | 72 (44%; batch 8 43%) |

Why no row (the new reason text, top ones):

| Reason | Count |
| --- | --- |
| "the walk is worth nothing from the nearest spots ... (late by two turns or more ...)" | ~16 |
| "its spots in range are worth nothing there" | 13 |
| "no legal move ends X\" nearer" | 11 |
| "it may not hold it (Unit Strength or troop type)" | 7 |
| "the walk never gets there from the nearest spots (its moves stop gaining)" | 6 |
| "its next turn from the nearest spots is a charge or a cast" | 4 |
| in a fight, fleeing or off the table | 2 |

WALK CHECK (398 move rows): the spot nearest the objective ranked 1st 176; the move taken = that spot 203, elsewhere 195.

## Leads (to check in code, not findings)

1. The ONE ROUTE count still claims 86% arrive for far walks while 8% do, and walkers still cover about half the inches the claim
   needs. The one-route count does not yet match what the unit moves.
2. Some walks are already priced "late by two turns or more" or "earliest 98" the turn after: the count from the new spot jumps.
3. "No legal move ends nearer" (11) for a unit the table sent to walk the turn before.

## Where the data is

- Every WALK CHECK and WALK FOLLOW-UP row (ON side, 70 games, with game, part, turn, unit and full text incl. the "no row" reasons):
  `walk-rows.tsv` in this folder (562 rows), made by scripts/rows8.py. Early reading: early-reading-57.md.
- Scripts (python3 -I <script> <root holding mine-N/ and opp-N/ folders): walks6.py, a5.py, fu9.py (follow-up + no-row reasons), rows8.py.
- Replays: WarhammerOldWorldSimulator branch claude/project-thread-o40l8a, commit ea8e2c76 (on 81fb82cd): deploy/sim-replays/
  h9-mine-81fb82c-p1..4 and h9-opp-81fb82c-p1..4 (70 games). on-site.txt lists these 8.
- Logs: archived to OldWorldSimulations, branch claude/project-thread-o40l8a (never merged to its main), folder
  batches/holder-assignment-9-h2h-2026-11-19/ (<arm>-N.tar.gz, one per part; SHA256SUMS; FILECOUNTS.txt).
