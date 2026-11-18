# Early reading at 62 games (2026-11-18 ~05:40 UTC), build c73418e64 (try 7: he shoots or charges, his random move, his charge denied, same charge later)

Switch side: smoke L0102 (Mine only) and all 8 parts at the check: FIVE ACTION, HE SHOOTS OR CHARGES, HIS RANDOM MOVE, HIS CHARGE DENIED,
SAME CHARGE LATER rows appear on the new side only (mine parts: Mine; opp parts: Opponent). 62 games is noise for VP.
Scripts: try 6's set + putoff3.py (promise total v charge-now total, wait split from the JOB RISK SPLIT row) + lowwin.py.

## 1. Charge next turn: promised v came
| | try 7 (62) | try 5 (288) |
| --- | --- | --- |
| Move-to-charge picks; charged that target next turn | 281; 19% (promised ~84%) | 1,648; 16% (~90%) |
| Kept promises on offer next turn, not taken again | 68 of 200 (34%) | 496 of 1,218 (41%) |
| Charges on offer put off for the SAME target | 38 of 181 (21%) | 282 of 1,032 (27%) |
| ... charge came next turn | 7 of 38 (18%) | |
| SAME CHARGE LATER cut on those waits | 12 of 38 | n/a |
Other kept promises: charged it 44, target stood but not on list 30, charged another 27, target moved 14, in combat 9, charged first 8.
What the wait carried over the charge now (36 with a split; promise total v charge-now total, not rule rows):
charge now median +50, wait +93; mean wait minus now +34 = next-turn charge minus charge now +6, this turn's own A +35
(objectives +22 in 7 cases, shots +7 in 9, missiles +2, feature +3), support for friends +10.5 (26 of 36). Next-turn charge chance claimed ~0.9-1.0.

## 2. Risk of picked jobs v lost in the enemy turn after (a game)
| | claimed | lost | try 5 |
| --- | --- | --- | --- |
| New, enemy charges | 228 | 200 (charged/fought) | 378 v 251 |
| New, shots + magic | 420 | 212 (152 shot + 60 magic) | 262 v 148 |
| New, all | 572 | 427 | 528 v 422 |
| Simpler, all | 689 | 337 | 749 v 418 |
Enemy charges counted (276, claimed 83%): he charged this unit 26%, another 13%, weighed it but did else 14%, never weighed 31%
(not on list 17 + list cut short 14), dead/we charged first/no list 14% (try 5: 21/15/11/41%).
The charge claim is now close; the SHOT claim doubled while the charge claim fell (try 6: 363 charges / 337 shots; now 228 / 420).
Priced NO risk then hit: 100 of 1,683 shooter pairs (84 of 1,260 "must move first"), 6 of 195 charge pairs.

## 3. Charge odds
| | New | Simpler | try 5 (new) |
| --- | --- | --- | --- |
| Declared charges that made contact (all, not only held) | 74% | 69% | |
| First round won: claimed v happened | 69% v 74% | 62% v 67% | 73 v 78 |
| Net points per charged fight | +46 | +72 | +71 v +73 |
| Picked with win chance under 50% | 41 of 173 (24%): won 10, lost 19, draw 2, no contact 10; net +10 | 64 of 237 (27%), net +71 | |
| Charges carrying HIS CHARGE DENIED | 17 (3 under 50%): won 8, lost 3, no contact 6; net -5 | | |
HIS CHARGE DENIED does not make losing charges get picked (3 cases).

## 4. Headline (62 games)
| | New | Simpler | try 5 (288) |
| --- | --- | --- | --- |
| VP margin | -156 ±303 (W23 L27 D12): noise | | -183 ±133 |
| VP by source | objectives -45, kills -112 | | -90, -83 |
| Charges declared a game | 3.2 | 4.8 | 3.4 v 5.0 |
| Charge picked when on offer | 50% (179 of 360) | 82% (272 of 332) | 45% v 78% |
| Stand share of picks | 12% | hold 17% | |
| Points lost a game | 691 | 564 | 690 v 606 |
| Own units caught in flank/rear, a game | 1.55 | 0.97 | 1.63 v 1.23 |

## Next root cause
**The promise prices next turn's charge as taken, but next turn the unit runs the same sum again and waits again.** The wait wins by
this turn's own gains (objective held, support, shots) on top of a next-turn charge priced about equal to the charge now (+6) at ~90%;
next turn the same gains are there again, so 34% of kept promises are on offer and put off again and the charge comes 18-19%.
The next-turn charge's chance is "can it charge" (reach and list), never "will this unit pick it" by its own next-turn sum. Fix by class:
B's chance = the chance the unit's own next-turn pick is that charge (its next-turn options by the same sum, incl. waiting again).
Second, smaller: the shot claim doubled (420 v 212 lost) since HE SHOOTS OR CHARGES moved enemies from charge risk to shot risk; check
whether such a shooter is then counted at every unit it could shoot instead of its one best target.
