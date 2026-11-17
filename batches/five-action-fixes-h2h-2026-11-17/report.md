# Fixed five-action against simpler pricing: head-to-head (2026-11-17)

**Verdict: the fixed five-action is clearly worse than simpler pricing: -378 VP a game, give or take 105.**
It is worse than last night's version (-279 ±99). The fixes brought its claims down to the same size as the other side's,
but it still charges less, holds fewer objectives and loses more. By the rule set beforehand (keep only if not worse than about -30)
it is dropped. **Morten dropped it at 11:47 CET.**

Batch: 288 games, the same 144 DKTC pairs and seeds as last night (Hero v Hero, seed 1, scenarios mix), each pair played both ways.
Build `claude/project-thread-1nluyr` at `5e477c59` (five-action plus next-charge-by-list, next-objective-nearer, no-double-rounds,
scaled-chance; likely-charge off). 287 of 288 games ended: L1135 (five-action as Opponent) stopped on an engine error, "This unit has
already pursued this turn and cannot pursue again" (filed as a sim finding). Pairs ahead 40, behind 103.

## 1. Headline

| # | Number | **Five-action (fixed)** | **Simpler pricing** |
| --- | --- | --- | --- |
| 1 | VP margin per game | **-378 ±105** | +378 |
| 2 | First round won when charging | 69% | 76% |
| 3 | Net points per charged fight | +82 | +87 |
| 4 | Points lost per game | **685** | 519 |
| 5 | Free units caught in flank or rear (per game) | 0.70 | 0.39 |

Five-action as Mine -428, as Opponent -328; going first -481, second -274.

## 2. VP by source (per game)

| Source | Five-action | Simpler pricing |
| --- | --- | --- |
| Objectives | **468** | 683 |
| Kills | **557** | 715 |
| Leaders | 37 | 42 |
| Charged fights a game | 1.9 | 2.8 |

## 3. Claims against what happened

| | Five-action | Simpler pricing |
| --- | --- | --- |
| Gain claimed a game (all jobs) | 2,213 | 2,218 |
| Risk claimed a game | 891 | 803 |
| Charge plans a game / made | 1.8 / 56% | 3.4 / 63% |
| Charge planned v won (VP a charge) | 117 v 97 | 73 v 92 |

The fix worked on the size of the claims: last night it claimed 1.5 times the other side, now the same. It still lost more, so the
size of the claims was not the whole problem.

## 4. Against last night

| | Last night | Fixed |
| --- | --- | --- |
| VP margin | -279 ±99 | **-378 ±105** |
| Gain claimed a game, five-action v other | 3,176 v 2,174 | 2,213 v 2,218 |
| Objectives | 498 v 638 | 468 v 683 |
| Kills | 622 v 756 | 557 v 715 |
| Points lost | 720 v 579 | 685 v 519 |

## 5. The questions the analysis left open (from the new SPLIT rows)

### Which part of the risk figure is wrong

| Per pick (move, march, stand, shoot) | Claimed | Happened |
| --- | --- | --- |
| Enemy charges expected | 0.46 | 0.09 |
| Points lost when charged | 62 (listed charger's figure) | 65 |
| Points lost when not charged (shots, magic) | 4.6 | 5.7 |
| Real chargers that were on the list | | 68% (696 of 1,027) |

- **The points a charge takes off are right** (62 v 65), and so are shots.
- **The list of who can charge is wrong both ways.** It expects five times too many charges (each enemy in reach counted in full,
  with likely-charge off), and a third of the enemies that really charged were not on the list at all.
- Overall the risk is now too high, not too low (claimed 21, lost 10 a pick). The "too low" part is the unlisted chargers: picks
  that claimed no risk were still charged 4% of the time.

### The 3-round fight: claimed v real, round by round

Charges it really made, where it did not expect the target to flee (305):

| Round | Claimed kills / losses | Real kills / losses | Claimed net | Real net |
| --- | --- | --- | --- | --- |
| 1 | 111 / 33 | 70 / 21 | +77 | +49 |
| 2 | 38 / 17 | 36 / 20 | +21 | +16 |
| 3 | 23 / 10 | 25 / 14 | +13 | +11 |

**Rounds 2 and 3 are about right** (they are weighted by the chance the fight goes on). **Round 1 is the error:** it expects about
40 points more killed than it gets. That is where most of last night's unexplained VP sit. (Real rounds are counted by player turn, so
they include shooting and magic on the two units; a rough check.)

### Flee as the charge reaction

- It assumed the target would flee in 32% of the charges it made (141 of 446), cutting each by about 78 VP.
- The target really fled in 11% (50). Of the 141 it expected to flee, 23 did; 27 fled where it expected a stand.
- So the flee guess is mostly wrong, and it cuts charges that would have been good.

## For simpler pricing (warning: what the numbers suggest, not a plan)

Two of these may also hold for simpler pricing: the round-1 kill figure and the list of who can charge. Neither was measured on the
simpler side here.

Scripts: `scripts/` beside this file (s1.py for section 5). Replays: branch `claude/project-thread-vt8lkk` (not main).
Logs: archived to OldWorldSimulations, `batches/five-action-fixes-h2h-2026-11-17`.
