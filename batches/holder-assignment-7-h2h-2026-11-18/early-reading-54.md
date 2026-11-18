# Holders batch 7 (dcce2247, real ground + his one quarter), reading at 54 games (22:17 UTC)

**Verdict: the known walk fault is UNCHANGED. Quarters are now fixed. Nothing broken** (no crashes, all 8 parts on the right side,
0 wrong-side rows, 6.6 min a game). VP margin ON-OFF -24 ±216 (27 won, 27 lost): noise.

## Claimed v happened (ON side)

| Objective | Claims | Claimed | Happened |
| --- | --- | --- | --- |
| Far marker walks (arrives in 2+ turns) | 60 | 96% arrive | that unit scored it by the claimed turn 4 (7%), ever 5 |
| Near marker walks (1 more turn) | 42 | 96% | that unit scored it by the claimed turn 12, ever 14 |
| Special feature, last row "holds" | 20 games | 86% / 218 VP | held at end 15, 231 VP |
| Special feature, last row "walks" | 5 games | 88% / 176 VP | held 1, 40 VP |
| Herdstone, last row "holds" | 17 games | 99% / 271 VP | held 14, 218 VP |
| Herdstone, last row "walks" | 6 games | 91% / 182 VP | held 0 |
| Own baggage train round 5+ | 18 holds, 5 walks | 101 VP | 55 VP (walks 0 of 5) |
| Quarters controlled / twice / uncontested | 218 | 67 / 54 / 32% | 65 / 53 / 29% |

Quarters: claims now come true (batch 6 under-claimed). Quarter VP still ON 319 v OFF 384 a Domination game (31 games, noise-sized).
Markers overall: scored 31% of marker turns ON v 32% OFF.

## Why far walks still fail

- Walkers move 2.9" toward the marker a turn (median) where 5.9" is needed; 12 of 60 covered their share.
- REAL GROUND changed a claim's turn count only 27 times in 54 games (+1 turn 23, +2 turns 2, -1 turn 2). As the build warned, the board
  gives most spots the same whole number of turns, so it changes little.
- What the 60 far walkers took in their Movement phase: a move onto that marker 4; a different objective 23; toward/against an enemy 12;
  a wider-search spot 7; other 14. A move row onto the assigned marker was among the rows weighed only 22 of 60 times.
- Of the 56 taken moves that were not onto that marker, 20 still carried the walk's credit ("Marker N in K more turns") and 36 carried
  none: the move phase mostly weighs and takes moves without the table's walk in them. LEAD (to check in code): the walk the table
  assigns does not reach the move list as a move toward that marker, and where it does it ties with moves that make no progress.
- The new ONTO tag says "no spot in its range weighed" for all 34 far-walk rows read (it only looks at spots ending in range this turn),
  so it cannot show a far walk's progress.

## Lead from the build: planned spot not reached (evidence, not a finding)

Planned spot = the "move to (x, y)" on the unit's rule rows; ended = the unit's place at the end of its Movement phase (ON side, scripts/plan7.py):

| Taken move | Moves | Ended 1"+ from plan | of which: shorter than planned / elsewhere / march test failed / charge-flee-random |
| --- | --- | --- | --- |
| wider search spot | 235 | 39 | 20 / 7 / 6 / 6 |
| onto an objective | 502 | 126 | 77 / 10 / 19 / 20 |
| promised spot | 52 | 12 | 4 / 4 / 0 / 4 |
| toward/against enemy | 243 | 51 | 20 / 10 / 8 / 13 |

Wider-search spots (the sideways "keeping its facing" moves) are mostly reached (196 of 235 within 1"), which is evidence AGAINST a general
movement bug there. Most "shorter" objective moves say on their own row that the wheel and the way end them short, but not all.
A separate lead found on the way (scripts/giveway7.py): when THE DEARER SUM KEEPS ITS PLAN makes a unit "give way", that unit did not move
at all in 44 of 105 cases ON and 36 of 126 OFF. Example L0423-3-1 turn 1: Hobgoblin Wolf Riders took "move onto Marker 2 (march)",
gave way to Hobgoblin Cutthroats 2, and then stood still the whole turn (frames show no move). Whether standing was its next best or a
lost move is for the build to check.

Scripts: scripts/walks6.py, a5.py, a4.py, walkmoves6.py, onto7.py, credit7.py, plan7.py, spot7.py, giveway7.py (python3 -I <script> <root>).
