# Early reading at 60 games (2026-11-18 ~04:35 UTC), build 2e2e69947 (try 6: his legal moves, his move and shot, his turn denied, the promise adds)

Switch side: smoke game L0102 (Mine only: HIS LEGAL MOVES 4, HIS MOVE AND SHOT 4) and the first 9 batch games (all four tags on the new side
only, in both arms; THE PROMISE ADDS seen only in opp parts so far). Scripts: try 5's fixed set + putoff.py, putoff2.py, flank.py (scripts/).

## 1. Charge next turn: promised v came
| | try 6 | try 5 |
| --- | --- | --- |
| Move-to-charge picks; charged that target next turn | 248; 17% (promised ~84%) | 229; 17% (~90%) |
Of 180 kept promises: charged it 35, **on offer next turn but not taken 67**, charged another 19, target stood but not on own list 24,
target moved/charged, not on offer 19, charged by the enemy first 9, in combat/fleeing 7.
The promise is not too LOW anywhere: it is still far too high.
Charges on offer, not taken: 167 (try 5: 183). Picked a move/march/stand "to charge the SAME target next turn": **36** (try 5: 45);
another target next turn 38; no next-turn target 93.
| Target kind of the 36 | put off | charge came next turn |
| --- | --- | --- |
| shooter/wizard | 17 | 3 |
| mobile (cavalry, chariot, monster, swarm) | 14 | 3 |
| plain block | 5 | 1 |
Median worth: the charge now +60 VP, the delay picked instead +97 VP.

## 2. Risk of picked jobs v points lost in the enemy turn after (a game)
| | claimed | lost | try 5 |
| --- | --- | --- | --- |
| New, enemy charges | 322 | 202 (charged/fought) | 348 v 180 |
| New, shots + magic | 349 | 183 (120 shot + 63 magic) | 325 v 186 |
| New, all | 575 | 393 | 570 v 374 |
| Simpler, all | 705 | 327 | 670 v 341 |
Enemy charges counted (409, claimed 85% on average): he charged this unit 23%, another unit 16%, weighed it but did else 12%,
never weighed it 36%, no list / dead / we charged first 13% (try 5: 22/18/12/39%).
Priced NO risk then hit: 108 of 1,680 shooter pairs (81 of 1,204 "must move first"; HIS MOVE AND SHOT did not close that), 4 of 230 charge pairs.

## 3. Charge odds
| | New | Simpler | try 5 (new) |
| --- | --- | --- | --- |
| Contact when the target held: claimed v happened | 89% v 85% | 92% v 89% | 81% |
| First round won: claimed v happened | 65% v 71% | 63% v 75% | 70 v 68 |

## 4. Headline (60 games)
| | New | Simpler | try 5 at 52 |
| --- | --- | --- | --- |
| VP margin | −243 ±263 (W15 L29 D16): inside noise, leaning bad | | −89 ±280 |
| Charges declared a game | 3.0 | 4.5 | 2.9 v 4.1 |
| Charge picked when on offer | 48% (157 of 324) | 77% (236 of 308) | 41% v 77% |
| Stand share of picks | 13% | hold 16% | |
| Points lost a game | 646 | 451 | 574 v 521 |
| Net points per charged fight | +39 | +78 | +60 v +52 |
| Own units caught in flank/rear, a game | 1.32 | 0.80 | 1.25 v 0.96 |

## Next root cause
**The charge next turn is still priced without the terms the charge now pays.** In the 36 put-off cases the charge now carries, on
average, NO DOUBLE ROUNDS −27, HONEST WORTH −24, WIDER SPREAD −8, RUN DOWN −4 (and BLOWS WHERE AIMED −126 where it applies); the delay
carries MOVE TO CHARGE COMPUTED +100 and none of those terms. Example L0122 turn 5: Gors charge now +338 after HONEST WORTH −94 and BLOWS
WHERE AIMED −126; it marched for +417 "next turn: #12137". THE PROMISE ADDS only cuts the case where a friend charges the target now (4 of 36).
The same sum then repeats next turn: 67 of 180 kept promises are on offer and again not taken, so the charge comes 17% as in try 5.
Fix by class: the next-turn charge figure runs through the same charge-now sum (the same honest-worth, double-rounds, spread and aimed-blows
terms), discounted only by what the turn of waiting actually risks.
