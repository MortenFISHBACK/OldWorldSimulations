# Try 14 against true simpler: final report (2026-11-18, stopped at 61 games)

Head bc0e08cec on claude/project-thread-60g6hv (H wounds kept, D promise knows the fight, E spot as the game moves, F one promise a target,
G his move as he decides, large-sums items). New side = everything on; simpler = worked-out-chances, five-action, standing-by-numbers off.
Same pairs as tries 9-13, both ways. Stopped by the coordinator at 23:42 UTC (known fault unchanged at the 55-game reading). 61 games,
none failed. Try 13 (54 games) in brackets.

## Verdict
**The promise fault is unchanged:** 89 claimed, 24 came in 100 (91 v 23). Fewer promises are made (1.1 a game v 2.7), and the losses
moved from our own army (41 in 100, was about 65) to the enemy's turn (28 in 100, was about 12). His move as he decides works: the
assumed enemy action matched 76% (21%). VP -108 ±265 is noise; net points per charged fight +41 v simpler +86.

## Promised charges, per 100 (66 promises; one row each in promises-61.tsv)
| What happened | per 100 |
| --- | --- |
| Charged the promised target | 24 |
| OWN ARMY: friend charged the target the same turn / first next turn | 6 / 5 |
| OWN ARMY: target dead or fled in our same turn | 5 |
| OWN ARMY: on offer next turn, not taken / charged another target | 11 / 6 |
| OWN ARMY: promised move not made / own figure at or below zero | 6 / 5 |
| ENEMY TURN: target moved, no charge left | 17 |
| ENEMY TURN: our unit dead, fleeing, charged or pinned / target charged | 8 / 3 |
| Unclear: target dead or fled in his turn or before our charges | 5 |
| Nothing moved, yet no charge listed | 2 |

## His one move: assumed v did (1,864 checks)
76% as assumed (1,419). Stand and move are mostly right; an assumed charge came about 1 time in 4.

## Big picks above 300 (114 picks, 1.9 a game)
| Kind | Picks | Claimed | Happened |
| --- | --- | --- | --- |
| Charge, fight within the target's points | 15 | 539 (fight gain 238) | target lost by the end 43% |
| Charge, fight above the target's points | 1 | 494 (kills 531 on a 440 target, lone models) | target lost |
| Charge, flee reaction | 6 | 557 | target lost 59% |
| Promise, fight within the target's points | 9 | 468 at 98% | charged next turn 22% |
| Promise, fight above the target's points | 1 | 406 (Black Orc Warboss on 41-point Giant Rats, 356 claimed) | not charged |
| Objectives / quarters (turn 5-6) | 18 / 32 | 413 / 456 | not measured here |
| Shooting and magic | 28 | 400 | not measured here |

## BOARD BOUND findings (filed as sim bugs with the replays)
Fight kills: 8 games, every one a fight with a Doomseeker (a loss smaller than the board's -50, e.g. -19 claimed).
Promise: 4 games; the largest 316 over (L0421 turn 5, Warboss on Giant Rats, 356 claimed, the board gives 40).

## Thinking time (new side, s a game)
Table again 129, his one move 76, his move as he decides 29, promise by its own sum 23, shots after the moves 10. Whole game 8.9 min.

## Headline
| | New | Simpler |
| --- | --- | --- |
| VP margin | -108 ±265 (W22 L25 D14), noise | |
| First round won when charging, claimed v happened | 66 v 69 | 65 v 78 |
| Net points per charged fight | +41 | +86 |
| Points lost a game | 598 | 479 |
| Free units caught in flank/rear a game | 1.28 | 0.84 |
| Charge pick: claimed VP v net over 2 turns | 146 v +10 | 103 v +55 |
| Shoot pick: claimed VP v VP of wounds done | 57 v 5 | 14 v 5 |

## Leads (for the build to check in code; not checked)
1. Targets that move away in the enemy's turn are now the largest single loss (17 in 100), although his move is assumed right 76%:
   check whether the promise reads the assumed move at all.
2. "On offer next turn, not taken" rose to 11 in 100: the charge was there and positive, and another pick won.
3. BOARD BOUND fight kills on a Doomseeker: the check may read the Doomseeker's own rule (it dies anyway) as a bound breach.
4. Charges above 400 claim about 540-670 on a fight gain near 240: most of the figure is not the fight.

## Where the data is
Readings: early-reading-55.md, this report, promises-61.tsv (one row per promise: part, game, turn, unit, target, claim, outcome).
Scripts: scripts/ (promise9.py with the own-army / enemy-turn split and PROMISE_TSV output; all.sh; large-sums/).
Game logs: archive repo MortenFISHBACK/OldWorldSimulations, branch claude/project-thread-bajbau, batches/try-14-h2h-2026-11-18/<part>.tar.gz.
Replays: WarhammerOldWorldSimulator branch claude/project-thread-bajbau 60800d922 (deploy/sim-replays/t14-*-bc0e08c-p1..4).
