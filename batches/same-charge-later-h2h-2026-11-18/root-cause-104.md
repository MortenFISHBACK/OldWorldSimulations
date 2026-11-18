# Root cause from the stopped try 7 (104 games, build c73418e64, 2026-11-18 ~06:00 UTC)

Morten stopped the batch at 104 games (05:38 UTC). VP -163 ±235 (W36 L48 D20). Switch side right in all 8 parts.

## Root cause 1 (charges): waiting always wins a tie, because the charge next turn is priced the same as the charge now
| | 104 games |
| --- | --- |
| Promised charge next turn: claimed v came | 87% v 18% (457 move-to-charge picks, 82 came) |
| Kept promises (321): charged it / on offer, put off again / charged another / not on offer | 73 / 108 / 43 / 71 |
| Charges on offer put off for the SAME target | 55 of 271 (20%); came next turn 11 of 55 |
The promise is honest about what the charge is worth: promised median 47 VP, the same charge when on offer next turn 48 VP.
But the wait is priced as "next turn's charge (about the same as charging now, at ~90-100%) + this turn's own gains". In the 16 cases where
the unit put the same charge off a second time: next-turn charge 139 v charge now 130, plus this turn's gains 30 (objectives 22) and
support for friends 14. Example: Varghulf L0126 turns 3 and 4: charge now 96, stand "next turn" 80 + support 23 = 103, twice.
So any small gain this turn (an objective held, support, a shot) tips it to waiting, every turn. The next-turn charge carries no cost
of the turn given up (the enemy's turn to move, flee, shoot or charge first; one fight round fewer) and its chance is "can it charge",
not "will this unit pick it". Fix by class (agrees with the coordinator's note): the next-turn charge is worth the charge times the
chance the unit's own next-turn pick is that charge, worked out by the same sum (which includes waiting again).

## Root cause 2 (shot danger counted 2x): rank-and-file wounds priced as a share of the unit AND its characters
| New side, a game | picks | shot claim | lost to shots+magic |
| --- | --- | --- | --- |
| All picks | 3,668 | 416 | 203 |
| Unit priced at >1.3x its own points (characters / general VP inside) | 217 | **182** | **25** |
| Unit priced at about its own points | 582 | 234 | 106 |
The shot claim = DeathCost x (wounds expected / unit's wounds left). DeathCost adds every joined character's VP (and the General's), but the
wounds are the rank and file's. Example L0102 turn 6: Primal Warherd (317 pts) "4.7 of its 13 wounds" = 320 VP shot risk, more than the
whole unit. Gors (Monster Hunter's Tapestry, 322 pts): 3.1 of 40 wounds = 69 VP. 148 picks were priced at more than twice the unit's own
points. Fix by class: price shot wounds at the points of the models they kill (rank and file first; a character only by its own wounds
and Look Out chance), not as a share of the whole group's death cost. (Points lost here count only the unit's own models: a joined
character shot dead would be missed, but that is rare.)

## Also seen (not new): shoot picks claim 47 VP v 6 VP of wounds done (simpler 17 v 6). Worth a look by the same class (target worth).

## Other numbers (104 games)
| | New | Simpler | try 5 (288) |
| --- | --- | --- | --- |
| Risk claimed v lost, charges | 242 v 224 | | 378 v 251 |
| Risk claimed v lost, shots + magic | 416 v 216 | | 262 v 148 |
| He charged the unit counted at risk | 24% (another 15%, weighed did else 12%, not on list 20%) | | 21% |
| First round won claimed v happened | 70 v 75 | 63 v 70 | 73 v 78 |
| Net points per charged fight | +49 | +69 | +71 v +73 |
| Picked with win chance under 50% | 67 of 301 (22%), net +25; 6 carry HIS CHARGE DENIED | 102 of 378 (27%), net +63 | |
| Charges declared a game | 3.2 | 4.5 | 3.4 v 5.0 |
| Charge picked when on offer | 53% (308 of 579) | 79% (428 of 544) | 45 v 78 |
| Points lost a game | 716 | 580 | 690 v 606 |
| Own units caught in flank/rear | 1.43 | 1.00 | 1.63 v 1.23 |
Scripts: putoff3.py, promise7.py, shotrisk7.py, lowwin.py in scripts/.
