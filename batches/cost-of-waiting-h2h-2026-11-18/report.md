# Cost of waiting against simpler pricing, try 6 (288 games, build 2e2e69947) - 2026-11-18

**Verdict: the new side still loses, −110 VP ±128 a game (W 95 / L 128 / D 65). That is better than try 5 (−183 ±133) and try 4
(−283 ±127), but still outside the band. The odds are closer again: risk claimed 546 v 438 lost, first round won 72% claimed v 76%,
contact when the target held 90% claimed v 89%. The gap left is the same as in try 5: a charge promised for next turn comes 18% of the
time, because the unit puts the same charge off again. The new side declares 3.9 charges a game against 4.9.**

All 288 games ended, none failed, no sim findings. Switch side checked in every part: rules-off.txt names the group on the simpler side
only, and FIVE ACTION / HIS LEGAL MOVES / HIS MOVE AND SHOT / HIS TURN DENIED / THE PROMISE ADDS rows appear on the new side only (all
four new rows fire in every part, for example 88-221 HIS TURN DENIED rows a part; none on the other side).

## 1. Charge next turn: promised v came
| | try 6 | try 5 |
| --- | --- | --- |
| Move-to-charge picks; charged that target next turn | 1,466; 18% (promised ~88%) | 1,648; 16% (~90%) |

The promise is not too LOW for any kind of target; it is still far too high.
The unit stayed on the promised spot 1,066 times. In its next turn:
| What happened | try 6 | try 5 (of 1,218) |
| --- | --- | --- |
| Charged the promised target | 239 | 239 |
| **The charge was on offer but not taken** | **369** | **496** |
| Charged another target | 139 | 127 |
| Not on its list: the target stood | 139 | 154 |
| Not on its list: the target moved | 80 | 90 |
| Charged by the enemy first | 63 | 69 |
| In combat or fleeing | 37 | |

Charges on offer and not taken (new side): 927 (counted by putoff.py; try 5 counted 1,032 in its own way). 199 of them picked a move, march
or stand "to charge the SAME target next turn" (try 5: 282); 272 picked "charge another target next turn".
| Target of the put-off charge | put off | the charge came next turn |
| --- | --- | --- |
| Shooter or wizard | 75 | 11 |
| Mobile (cavalry, chariot, monster, swarm) | 70 | 9 |
| Plain block | 54 | 8 |
Median worth: the charge now +72 VP, the delay picked instead +102 VP.

## 2. Risk of the picked job: claimed v points lost in the enemy turn after (a game)
| | claimed | lost | try 5 |
| --- | --- | --- | --- |
| New, all | 546 | 438 | 528 v 422 |
| New, enemy charges | 363 | 262 (charged or fought) | 378 v 251 |
| New, shots + magic | 287 | 153 (123 shot + 30 magic) | 262 v 148 |
| Simpler, all | 717 | 432 | 749 v 418 |

Enemy charges counted as a risk (1,965, claimed 87% on average):
| What he did | try 6 | try 5 |
| --- | --- | --- |
| Charged this unit | 22% | 21% |
| Charged another unit | 14% | 15% |
| Weighed it, did something else | 10% | 11% |
| Never weighed it | 39% | 41% |
| We charged first, he died, no list | 15% | 10% |

Priced NO risk, then hit:
| Reason given | pairs | then shot or charged this unit |
| --- | --- | --- |
| HIS SHOT LIST: "must move first" | 4,896 | 6% |
| HIS SHOT LIST: "outside its arc" | 1,039 | 5% |
| HIS SHOT LIST: "in a fight" | 1,023 | 6% |
| HIS CHARGE LIST (cannot see it, and similar) | 934 | 4% |
HIS MOVE AND SHOT cut the "must move first" pairs from 5,892 to 4,896, but the hit share stayed at 6%.

## 3. Charge odds
| | New | Simpler | try 5 (new) |
| --- | --- | --- | --- |
| Contact when the target held: claimed v happened | 90% v 89% | 91% v 89% | 84% |
| First round won: claimed v happened | 72% v 76% | 67% v 76% | 73 v 78 |
| Charge pick: claimed VP v net points over 2 turns | 147 v +56 | 87 v +57 | 127 v +59 |
| Shoot pick: claimed VP v VP of wounds done | 45 v 6 | 14 v 6 | 45 v 6 |

## 4. Headline
| | New | Simpler | try 5 |
| --- | --- | --- | --- |
| VP margin | −110 ±128 | | −183 ±133 |
| VP by source (new minus simpler) | kills −61, objectives −44 | | −83, −90 |
| Charges declared a game | 3.9 | 4.9 | 3.4 v 5.0 |
| Charge picked when on offer | 52% (1,009 of 1,936) | 76% (1,281 of 1,687) | 45% v 78% |
| Stand share of picks | 13% | hold 14% | |
| Points lost a game | 706 | 640 | 690 v 606 |
| Net points per charged fight | +70 | +73 | +71 v +73 |
| Own units caught in flank/rear by a charge, a game | 1.60 | 1.42 | 1.63 v 1.23 |
The 60-game check read −243 ±263: noise, as at the earlier checks tonight.

## Next root cause
**The charge next turn is still priced without the terms the charge now pays.** In the 199 put-off cases the charge now carries, on
average, NO DOUBLE ROUNDS −35, HONEST WORTH −28, BLOWS WHERE AIMED −11, RUN DOWN −6, GIVES UP −5, SHOT OR CHARGE −4 and WIDER SPREAD −4.
The delay carries MOVE TO CHARGE COMPUTED +129 and none of those terms. Its only cuts are THE PROMISE ADDS −11 (in 18 of the 199 cases),
NEXT CHARGE BY LIST −3 and REFORMS TO MEET IT −2.
Example L0122 turn 5: the Gors charge now was worth +338 after HONEST WORTH −94 and BLOWS WHERE AIMED −126. It marched instead for +417,
"next turn: #12137". THE PROMISE ADDS (try 6) covers only a target a friend charges now. The same uneven sum then repeats in the next turn:
369 of 1,066 kept promises have the charge on offer and it is not taken.
Fix by class: work out the next-turn charge with the same charge-now sum (its honest worth, double rounds, aimed blows, run down, gives up,
spread and shot-or-charge terms), cut only by what the turn of waiting really risks.

Second cause, unchanged: the enemy-charge risk is his reach (87% claimed), not his choice (22% came).

Scripts: try 5's fixed set (idle2, notrisk4, shotgap3, promise6, risk, build + odds, reach/reach2/reach3, report) + putoff.py (put-off
charges by target kind), putoff2.py (rule terms of charge now v delay), flank.py, in scripts/. Early reading: early-reading-60.md.
