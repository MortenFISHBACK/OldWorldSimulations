# Army-wide holders: the four leads checked in the logs and the code (2026-11-18, 55 games)

Build thread's check of the early reading. Logs: the 55 games on the mount at 10:57 CET, on side only. Scripts: `scripts-build/`
(an6.py sorts every assignment, an3.py compares points, an2.py reads the "stays empty" lines). Nothing was changed in the game code.

## 1. Why the scoring unit is not cheaper

The table does what was ruled (gives up least; one unit, one objective). It cannot pick cheaper units because there are more objectives
than cheap units. Of 406 marker assignments:

| | Assignments |
| --- | --- |
| Only one unit could hold it | 60 |
| The assigned unit was the cheapest of those listed | 184 |
| A cheaper unit was listed, but every one of them already held another objective | 141 |
| A cheaper unit was free, and gave up more by its own sum (the ruling) | 10 |
| A cheaper unit was free and gave up the same: the unit holding it now kept it | 11 |

- Half of all assignments (400 of 806) go to the Herdstone, the special feature and the baggage trains, and they take the cheap units.
  Example (L0313, round 3): Infernal Ironsworns, 314 points, hold Marker 3 while Hobgoblin Cutthroats 2, 95 points, give up the same,
  because the Cutthroats were given another objective.
- 436 of 525 "stays empty" lines are empty for that reason (its best unit holds something else), not because "no unit gains" as the
  line says. The line's text is wrong there.
- The 11 ties are my tie-break: the current holder before the fewer points. Morten's answer 1a says points break ties.

## 2. Why assigned holders do not score the same round

51 of the 406 marker assignments are "walks on to it": never meant to score that round. Of the 355 "holds it this turn":

| What happened | Assignments | Share |
| --- | --- | --- |
| The assigned unit scored it | 267 | 75% |
| Another unit of ours, nearer the marker, scored it (the side got the VP) | 31 | 9% |
| Its move stopped 2"+ short of the spot it chose | 10 | 3% |
| At the spot it chose the sum counted the marker, the board measured it outside 6" (9 of them by under an inch) | 14 | 4% |
| In range, but also within 6" of a baggage train or the special feature: the game gives a unit one object only, and that one first | 11 | 3% |
| In range, an enemy unit nearer or as near | 9 | 3% |
| Its Reserve Move after shooting took it off the marker | 6 | 2% |
| Moved away by its own army's movement spell | 2 | 1% |
| The move phase chose another spot or stayed; under Unit Strength 10; destroyed | 5 | 1% |

Checked in code:
- The game (AreaControlService) gives each object to the NEAREST able unit, one object a unit, in the order special feature, hill,
  baggage train, markers, and an enemy nearer takes it. The table and the move figure (MoveWorth "now", KeptTurns) only test "within 6"
  and able". That one difference is behind the nearer friend (31), the one-object cases (11) and the enemy cases (9).
  Example (L0525, rounds 2-4): Thunderers 2 stand 5" from Marker 1 and 3" from their own baggage train; the sum counts 90 VP for the
  marker each turn, the game gives them the train and nobody scores the marker.
- The Reserve Move fall-back (ReserveFallBack) weighs only the expected loss and the shooting: it does not count an objective it
  steps off.
- Moves that stop short: the spot is the move phase's own choice and the board ends the move earlier (L0423 round 1: Wolf Riders
  chose (37.0, 32.6), moved 2.8" round Iron Daemon 1 which was to give way). Same class as the promised marches in the overhaul build.
  It is not a lane refusal of the promised spot: the promised spot was taken or tied in the cases read.

## 3. The hill at 24%

24 assignments: 11 are "walks on to it" (0 score that round by design). Of the 13 in range the side scored the hill 11 times (85%), the
assigned unit itself 6 times; in 5 a nearer friend held it. Same cause as point 2, first bullet. Small numbers.

## 4. The claims script

`scripts/job_claims.py` now reads the table: a holder's pick in range counts as Hold (claimed = what the table says the objective is
worth there, which covers up to three turns; happened = VP scored this turn and the enemy's next), a walk-on as Advance toward an
objective, and the Herdstone, feature and baggage as their own row. On these 55 games: Hold 3.3 picks a game, claimed 82-90, scored
40-42 that round.

## Proposed fixes (not built)

1. The table and the move figure use the game's own control rule at the end spot (nearest able unit, one object a unit in the game's
   order, an enemy nearer takes it). About 4 h. Covers 51 of the 88 misses.
2. Points break ties before the current holder (answer 1a). 0.5 h.
3. The Reserve Move fall-back and own movement spells count the objective the unit steps off. 2 h.
4. The "stays empty" line says the real reason. 0.5 h.
5. Moves that stop short, and the spots the sum counts in range that the board measures just outside: to the overhaul build with the
   24 cases (an6.py lists them).
6. For Morten: cheap units are drawn to the Herdstone, feature and baggage by the figures the sum has for them (answer 5a left those
   for later). Markers then fall to dear units. No change proposed until that item is planned.
