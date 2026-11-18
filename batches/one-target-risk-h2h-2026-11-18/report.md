# One-target risk against simpler pricing, try 4 (288 games, build e5ebca621) - 2026-11-18

**Verdict: the new side still loses clearly, −283 VP ±127 a game (W 93 / L 139 / D 56). The 61-game check (−93 ±205) was noise.
The one-target rule works where it acts, but the risk is still claimed about twice what is lost, and charges promised for next turn
come 12% of the time. Both gaps trace to one cause: "next turn" (his shot or charge at us, our charge at him) is figured with tests
that are not the game's own lists (legal charges, shot targets).**

Switch side checked in every part (ONE TARGET A SHOOTER / FIVE ACTION rows only on the new side; rules-off lists the group on the
simpler side). Scripts in scripts/ (report.py, risk.py, build.py + odds.py; new: notrisk3.py, promise5.py, shotgap2.py).

## 1. Risk of the picked job: claimed v points lost in the enemy turn after (a game)
| | claimed | lost | try 3 (71 games) |
| --- | --- | --- | --- |
| New, all | 907 | 439 | 1,736 v 449 |
| New, enemy charges | 466 | 261 (charged/fought) | 518 v 204 |
| New, shots + magic | 570 | 164 (135 shot + 29 magic) | 1,404 v ~230 |
| Simpler, all | 768 | 362 | 670 v 374 |

## 2. Enemies priced as no risk: did they hit the unit anyway?
| | pairs | hit this unit | hit the named better target | acted at all |
| --- | --- | --- | --- | --- |
| Shooter "has a better target" | 19,306 | 5% | 9% | 26% shot something |
| Charger "charges #X instead" | 1,527 | 5% | 9% | 23% declared a charge |
The rule holds: units it cleared were rarely hit. The enemies still COUNTED rarely act: 2,621 enemy charges counted at 87% reach on
average; he declared on that unit 11%, the charge was on his own list next turn 26%, taken 65% when it was.

## 3. Why the shot risk is 570 claimed v 164 lost (coordinator's question)
Claimed shot VP of picked jobs (a game), by what the enemy's shooters and wizards did with the unit in their next turn:
| What happened | picks | claimed VP a game |
| --- | --- | --- |
| Enemy made no shot or spell list at all that turn (no shooter or wizard had any target) | 1,085 | 247 |
| Unit was on no list; enemy shot or cast at others | 410 | 99 |
| On a list, another target picked | 171 | 47 |
| Charged instead | 106 | 25 |
| Shot or cast at (here the claim meets a loss of about 164) | 511 | 182 |
58% of the claim sits on units no enemy shooter or wizard could target at all. The cause in the code: a shooter counts as a threat
when the unit is within its range plus its move (AssessmentService), at full weight, or half when it must move first, with no line of
sight, no front-arc turn, and no check that it is free to shoot (in combat, fleeing, marched, charged). The game's own list
(CANDIDATES SHOT / MISSILE) applies those tests. Magic is weighted by cast-and-stands; shooting has no such chance. Most of these
claims log a chance to be shot dead under 10% while still counting wound points (SHOT RISK POINTS).

## 4. Charge odds
| | New | Simpler | try 3 |
| --- | --- | --- | --- |
| Contact when the target held | 85% | 80% | 89% |
| First round won: claimed v happened | 68% v 74% | 66% v 79% | 59 v 62 |
| Charge next turn: promised v charged that target | 90% v 12% (1,408 picks) | | 87 v 24 |
| Charge pick: claimed VP v net points over 2 turns | 137 v +63 | 85 v +63 | |
PROMISE KEPT 1,043 / WITHDRAWN 308. Of the 1,043 kept (unit ended on the promised spot): charged it 136, charged another 95, on offer
but not taken 118, in combat or fleeing 63, unit dead 46, charged first by the enemy 44, and **541 where the charge was not on its own
legal list next turn (344 with the target standing still)**; of those, 278 are characters (likely inside a unit, cannot charge alone)
and 144 promised the same charge "next turn" again.

## 5. Headline
| | New | Simpler |
| --- | --- | --- |
| VP margin | −283 ±127 | |
| VP by source (new minus simpler) | objectives −144, kills −135 | |
| Charges declared a game | 2.8 | 5.1 |
| Charge picked when on offer | 45% (658 of 1,448) | 74% (1,298 of 1,761) |
| Points lost a game | 669 | 536 |
| Net points per charged fight | +76 | +80 |
| Units caught in flank/rear by a charge, a game | 1.7 | 1.0 |
| Shoot picks firing at their target; claimed v wounds done | 73%; 36 v 5 VP | 71%; 22 v 7 VP |

## Next root cause (one cause, two places)
The next-turn figures do not use the game's own tests. (a) Our promised charge: MOVE TO CHARGE COMPUTED and the enemy-charge threat
(ArcThreats) are not checked against the legal charge list (characters inside units, skirmisher sight, the way), so 541 of 1,043 kept
promises were not legal next turn. (b) His shooting: a shooter in range plus move counts at full weight with no sight, arc or
free-to-shoot test, so 58% of the shot claim lands where nobody could shoot. Fixing (a) and (b) is the root cause, not a share.

Replays: branch claude/project-thread-6qw5kt (commit 1e44bb72a), folders deploy/sim-replays/t4-mine-e5ebca6-p1..4 and
t4-opp-e5ebca6-p1..4 (on-site.txt lists these 8). Archive: MortenFISHBACK/OldWorldSimulations, branch claude/project-thread-6qw5kt.
