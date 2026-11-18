# Early reading at 61 games (2026-11-18 00:15 UTC), build e5ebca621 (try 4: one target per enemy shooter/charger)

Switch side checked in the smoke game and in parts mine-1 / opp-1 (ONE TARGET A SHOOTER, ONE CHARGE A CHARGER, FIVE ACTION, STANDS STILL
only on the new side; rules-off.txt lists the full group on the simpler side only).
Scripts: scripts/report.py, risk.py, build.py + odds.py; new: notrisk3.py (item 2), promise5.py (kept promises), in scripts/.

## 1. Risk of picked jobs: claimed v points lost in the enemy turn after (a game)
| | claimed | lost | try 3 |
| --- | --- | --- | --- |
| New, all | 927 | 401 | 1,736 v 449 |
| New, enemy charges | 414 | 220 (charged/fought) | 518 v 204 |
| New, shots + magic | 637 | 174 (130 shot + 44 magic) | 1,404 v ~230 |
| Simpler, all | 711 | 341 | 670 v 374 |
Shots still claimed ~3.7x what happens; charges ~1.9x.

## 2. Enemies priced as no risk ("better target" / "charges #X instead"): did they hit the unit anyway?
| | pairs | hit this unit | went for the named better target | did that at all |
| --- | --- | --- | --- | --- |
| Shooter with a better target | 4,220 | 6% | 7% shot it | 25% shot anything |
| Charger that "charges #X instead" | 257 | 5% | 7% | 16% declared any charge |
The one-target rule is right where it bites (few hits on units it cleared). But the enemies still COUNTED as risk rarely act:
of 532 enemy charges counted (claimed reach 86% on average), he declared on that unit 11%, declared at all 15%, and the charge was
even on his own list next turn only 28% (taken 59% when it was).

## 3. Charge odds
| | New | Simpler | try 3 |
| --- | --- | --- | --- |
| Contact when the target held (declared) | 78% | 76% | 89% |
| First round won: claimed v happened | 65% v 66% | 64% v 77% | 59 v 62 |
| Move to charge next turn: promised v charged that target | 87% v 10% (263 picks) | | 87 v 24 |
PROMISE KEPT 190 / WITHDRAWN 65. Withdrawn: 29 "promised spot not taken though worth more", 8 "charge no longer there from the spot".
Of the 190 kept (unit ended on the promised spot): charged it 24, charged another 22, on offer but not taken 21, in combat/fleeing 17,
charged first by the enemy 8, and 98 where the charge was NOT on its own legal list next turn (target moved 41, target stood 56);
of those 98, 31 promised the same charge "next turn" again, 32 are characters (likely inside a unit, cannot declare alone).

## 4. Headline
| | New | Simpler | try 3 (new v simpler) |
| --- | --- | --- | --- |
| VP margin | -93 ±205 (W 22 / L 27 / D 12) | | -331 ±218 |
| Charges declared a game | 2.4 | 4.6 | 2.0 v 5.1 |
| Charge picked when on offer | 42% (121/286) | 74% (239/324) | 51% v 72% |
| Points lost a game | 549 | 505 | 628 v 466 |
| Net points per charged fight | +59 | +61 | |
| Free units caught in flank/rear by a charge (a game) | 1.3 | 0.6 | not measured |

## Most likely next root cause
"Charge next turn" (ours promised and his counted as risk) is figured from a spot by a reach test that is not the game's legal-charge
test. Evidence: own kept promises at 87% came 13% and in 98 of 190 the charge was not on the unit's own legal list next turn even when
the target stood (56); enemy charges counted at 86% were on his own list 28%. LEGAL CHARGES ONLY filters charges NOW only; the next-turn
figure (MOVE TO CHARGE COMPUTED / ArcThreats) is not checked against the same legality (characters in units, sight/arc, way).
