# One-figure charges against simpler pricing (2026-11-17, third try) - STOPPED at 71 of 288 games

Build 9f58d5bf9 (branch claude/project-thread-60g6hv). New side = everything on; simpler = `worked-out-chances,five-action,standing-by-numbers`
off. Same army pairs as the two stopped batches, both ways. Switch side checked in all 8 parts (FIVE ACTION rows only on the new side,
rules-off.txt names the other side). Stopped 23:02 UTC on Morten's standing word (50+ check, margin still large) and his "Stop and fix
risk then run again".

**Verdict: still a large loss (-346 ±199). The charge odds are now mostly honest; the risk figure is not. The new side expects about
four times more loss than happens (1,736 VP a game claimed v 449 points lost), mostly from enemy shooting (1,404 claimed v ~230 lost to
shooting and magic). That makes it charge 1.9 times a game against 4.8.**

## 1. Odds: claimed v happened

| | New | Simpler |
| --- | --- | --- |
| Reach, targets that held | 91% v 90% | 88% v 86% |
| Targets that fled as charge reaction (not in the odds yet) | 19% got away | 18% |
| First round won when charging | 60% v 61% | 66% v 75% |
| Target destroyed (contact, by end of next own turn) | 34% v 51% | |
| Charger lost | 19% v 26% | |
| Charge pick: claimed VP v net points over 2 turns | 108 v +36 | 90 v +52 |
| **Risk of picked jobs a game: claimed v points lost next enemy turn** | **1,736 v 449** | 684 v 376 |
| Shoot pick: claimed VP v VP of wounds done | 3 v 5 | 24 v 5 |

Risk by source, new side, per game: claimed enemy charges 518 / shots 1,404 / lost-charge 31; lost when charged or fighting 204, shot 171,
magic 59, other 15. Tables per job type: risk-evidence/risk-tables.md.

Move to charge next turn (125 picks): promised 87%, came 23% (stopped batches: 4%, 15%).

| Distance at next turn | picks | promised | came |
| --- | --- | --- | --- |
| <6" | 8 | 92% | 12% |
| 6-12" | 54 | 89% | 28% |
| 12-18" | 33 | 84% | 30% |
| 18-24" | 21 | 83% | 14% |
| 24"+ | 9 | 87% | 0% |

Why it did not come: charged 23%; target moved out of reach 20%; offered next turn but priced below zero 17%; unit or target gone 17%;
other option taken 8%; not in reach with the target standing 7%; in combat or fleeing 4%; way or sight blocked 2%; target fleeing 2%.
The 55 "moved out of reach" and "below zero" cases: risk-evidence/failed-promises.tsv.

## 2. Headline

| | New | Simpler |
| --- | --- | --- |
| VP margin | -346 ±199 (stopped batches: -423, -490) | |
| Won / lost / drawn | 16 / 33 / 22 | |
| Points lost a game | 647 | 478 |
| Net points per charged fight | +66 | +75 |
| Charge on offer, per unit decision | 7% | 12% (simpler offers some charges the game refuses) |
| Charge picked when on offer | 51% | 72% |
| Charges declared a game | 1.9 | 4.8 |
| Stand still (new) / hold (simpler) | 13% | 16% |

Passed-over charges (new side, 90 of 143 parsed): median worth +14 = fight +53, second term +18, other-costs -51, after -3, risk -14
(shots -4 median, -30 mean). 26 were at or below zero; 13 of those would be above zero without the risk term. Moves and marches
were picked instead (57 of 90). List: risk-evidence/passed-over-charges.tsv.

Not measured here: free units caught in flank/rear and charge lines/paths (no time before the stop).

## 3. What the logs point at (warning, not a conclusion)

The shot risk on a unit ("SHOT RISK POINTS: 5.1 of its 3 wounds, shot dead alone 50.6") looks like it counts every enemy gun that can
see the unit as firing at it. Summed over the army that is 1,404 VP a game against ~230 lost to shooting and magic. Each enemy gun
fires once a turn, so the same gun is counted against many units. That is what the code WOULD need checking for.

Data: `<arm-N>/batch.tgz` here (71 games); scripts: scripts/report.py, fixed.py, build.py + odds.py, risk.py, reach*.py, nextturn.py.
