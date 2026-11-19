# Baseline on main, every new part on (2026-11-19)

**Measured without fight odds.** These games ran on main 882d87577. Fight odds landed afterwards (main d3b8ce3ce): it is on in
simulations, and simpler pricing uses it too. Later runs therefore differ from this baseline by fight odds as well as by their own
change (Morten 2026-11-19: keep this baseline, no re-run).

562 of 576 games saved (288 pairs, seeds 1 and 2, Medium against Medium, every rule on for both sides). 8 were cut by the stop,
and 6 failed to save; the cause is below. Both armies of every game are counted, so each figure is per army per game (1,122 army-games).

## Verdict

**Charges: the claims now match the dice.** The first round was won in 73% of charges, against 72% claimed, and every claim band
is close except the lowest: claimed under 20%, won 20%. A charge nets +95 points (+90 on simpler pricing).

**Promises and walks still do not come.** Promised charges are claimed at 87% and 25% came. Far marker walks are claimed at 89%, and
the walking unit held the marker on the claimed turn in 11% of them. These are the known faults, unchanged.

**Fewer points lost.** An army gives up 1,264 VP a game, against 1,385 on simpler pricing. Units lost after being charged cost
321 VP a game, against 384.

## Claimed v happened

| What | How many | Claimed | Happened |
| --- | --- | --- | --- |
| First round won, own charges | 2,562 fights (2.3 a game) | 72% | 73% |
| ...claimed under 20% | 235 | 7% | 20% |
| ...claimed 20-40% | 172 | 30% | 35% |
| ...claimed 60-80% | 386 | 71% | 76% |
| ...claimed 90%+ | 1,001 | 96% | 95% |
| Target slain or fled in round 1 (one charger), claimed 80%+ | 646 | 94% | 73% |
| Target slain or fled in round 1, claimed under 20% | 689 | 6% | 15% |
| Promised charge made next turn | 1,634 (2.9 a game) | 87% | 25% |
| Near marker walk (1 turn): walker holds it on time | 343 | 87% | 31% |
| Far marker walk (2+ turns): walker holds it on time | 557 | 89% | 11% |
| His move as assumed (within 1"): stand / move / march / charge | 17,958 checks | - | 73% / 29% / 17% / 48% |

## Headline numbers (per army per game)

| | Baseline | Simpler pricing (assessment 11-19) |
| --- | --- | --- |
| VP given up | 1,264 | 1,385 |
| First round won when charging | 73% | - |
| Net points per charged fight | +95 | +90 |
| Units lost after the enemy charged them | 321 VP (2.3 fights) | 384 VP (2.8 fights) |
| Flank or rear charges received | 1.16 a game (lost 168 VP) | - |

## Where the points go (per army per game, biggest first)

| Cause | VP a game | How often |
| --- | --- | --- |
| Table quarters the enemy scores | 264 | 1.4 |
| Markers the enemy scores | 217 | 0.6 |
| Units lost after being charged in the flank or rear | 97 | 0.6 |
| Units lost after being charged in the front | 92 | 0.6 |
| Special feature the enemy holds | 63 | 0.4 |
| Units hit by an enemy pursuit or overrun | 55 | 0.4 |
| King of the Hill | 49 | 0.1 |
| Units that fled without a fight | 47 | 0.4 |
| Units lost in their own charge | 47 | 0.3 |
| Shooting / magic / war machines | 45 / 39 / 36 | 0.4 / 0.3 / 0.2 |
| Baggage | 38 | 0.4 |

Good charges weighed and not made (claimed win 60%+, in reach): 0.77 a game; the unit took a move or march its own sum valued higher
(+168 against +75 for the charge).

## Thinking time (measurement only, nothing changed)

A game takes 10.8 minutes (median; 90% under 22.5, longest 52.7), about 54 seconds a player turn with three games sharing four cores.
Before the new parts a container did about 42 games an hour; now about 11.

Where the computer's time goes (two profiled games, sampled CPU of the game thread; shares overlap because a part includes what it calls):

| Part | Game R3 (5 min) | Game R1 (8 min) |
| --- | --- | --- |
| Five-option pricing per unit | 54% | 49% |
| Army-wide table run again each turn | 43% | 63% |
| Walking each candidate spot on the real ground | 36-40% | 58-59% |
| ...the model-by-model path planner inside it | 34% | 59% |
| Overlap geometry | 27% | 37% |
| Charge geometry | 28% | 19% |
| Objectives | 32% | 25% |
| Holders | 19% | 10% |
| The enemy's own choice | 12% | 22% |

Most of the time goes to checking each candidate spot by walking it on the board with the model-by-model planner, inside the
five-option pricing, and the army-wide table repeats that every turn. Profiles: timing/.

## Games that failed to save (6)

L1729 (both seeds), L1731-1, L1317-1, L0717-2, L1723-2; logs *-failed.log in the part folders. The errors were EF "a second operation
was started on this context" or SQLite error 5 when the game's database closed.

Cause, checked by replaying L1729 seed 2 on 882d87577: the computer's turn-1 movement took longer than the harness's 3-minute limit for
one phase, so the harness ended the game (TIMEOUT, sim bug S-2fbe8e, marked fixed 11-14, back). The computer's own loop was still running
and kept using the game's database while the harness saved the record and closed it. That collision is the crash; when it misses, the
game is saved as not ended (1 such game, L1725-3-1). The other five failed the same way after long games (16-42 minutes); that they hit
the same limit is likely, not checked one by one. Two faults: the 3-minute phase limit is too short for the new thinking time, and the
harness does not stop the computer's loop before saving.
