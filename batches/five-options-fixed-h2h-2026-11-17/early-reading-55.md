# Early reading at 55 games (2026-11-17 ~22:00 UTC), build 21301cb47

Switch side checked in all 8 parts (FIVE ACTION rows only on the new side; rules-off.txt on the other).

| | New | Simpler |
| --- | --- | --- |
| VP margin | -318 ±210 | |
| Won / lost / drawn | 16 / 28 / 11 | |
| Points lost a game | 619 | 454 |
| Charge on offer, per unit decision | 7% | 13% |
| Charge picked when on offer | 42% | 71% |
| Charges declared a game | 1.7 | 4.7 |
| Stand still (new) / hold (simpler) | 11% | 16% |

Move to charge next turn (new side, 147 picks): promised 82% (90% from under 12"), charged that target 16% (stopped batch: 4%).
| Distance next turn | picks | promised | came |
| <6" | 10 | 93% | 20% |
| 6-12" | 55 | 90% | 22% |
| 12-18" | 38 | 81% | 16% |
| 18-24" | 33 | 73% | 12% |
| 24"+ | 11 | 63% | 0% |

Charge now (new side, 69 picks with the played-out split): reach 92% claimed v 70% contact; first round won 64% v 61%;
target destroyed 34% v 46%; charger lost 25% v 25%. Simpler: first round won 70% claimed v 80%.

Why the promised charge did not come (123 cases where both units were still there next turn): 24 charged; 12 offered but
another option picked; 33 the same charge next turn priced at about -97 VP (median) and dropped as "below zero" after it was
promised at +VP; 16 path or sight blocked; ~48 simply not in reach next turn (about half after the target moved, half with the
target standing still).
Scripts: scripts/fixed.py (tables), report.py, build.py + odds.py; trace at /tmp only.
