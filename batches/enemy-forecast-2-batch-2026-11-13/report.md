# Expected enemy turn, second version: one side predicts (2026-11-13)

Branch `claude/project-thread-oaxa63` @ f5fe7c814 (replays committed ffa23d7ec). The same 144 DKTC games (Hero v Hero) played twice:
in "Mine predicts" only the computer playing Mine used the prediction, in "Opponent predicts" only the one playing Opponent. Comparing
the same game both ways cancels the edge of lists and sides. 288 of 288 games ended. One sim finding: S-9bb92e (new), Marauder Horsemen
1.34" off the table after a FACES THE THREAT reform (game L2531-5-1) - the same class as last night's S-9ee78d (Dragon Ogres off the table).

## Result: the prediction is now much better, but using it still wins nothing

| | Mine predicts | Opponent predicts |
| --- | --- | --- |
| Mine won / drew / lost | 56 / 20 / 68 | 56 / 25 / 63 |
| Margin Mine - Opponent | -168 | -106 |

The side that predicts does 31 VP a game worse, give or take 120: noise, and if anything slightly negative.

Play hardly moves either: charges 5.2 v 5.1 a game, flank or rear hits on units free to turn 0.77/0.66 (predicting) v 0.79/0.68
(not), FACES THE THREAT slightly fewer for the predicting side (1.24 v 1.34 Mine, 0.83 v 0.93 Opponent).

## How good the prediction is now (right of judged)

| Expected | First version (12 Nov) | Now |
| --- | --- | --- |
| Charge | 30-33% | 58-65% |
| Shoot / cast | 23% | 36-44% |
| Move (incl. hold / advance) | 86-88% | 71-77% |

The enemy's own plan (the computer's objective figures run from the enemy's side) doubled the charge hit rate. Where a moving unit ends
is still poor: the straight march toward its target misses by 6.6" (median) against 4.0" for simply guessing "it stays where it is".

## Speed

About 6.4 minutes a game against about 5.2 in last night's batch (different containers, so rough): roughly +20-25% for the extra look
from the enemy's side. A two-turn look would add about three such looks a turn.

## What next (for Morten)

1. Park it [recommended]: keep the branch and the prediction rows for later (two-turn foresight would build on them), land nothing,
   and go back to the unforced errors.
2. Land it as it is: better prediction, no VP gain, ~20% slower games.
3. Go on to two-turn foresight now (about a day), accepting that one turn ahead showed no gain.

Files: compare/compare-all.md (full comparison), compare/merge.sh.
