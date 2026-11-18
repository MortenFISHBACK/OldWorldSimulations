# Joint charges batch A: joint charge now on v off, stopped at 205 games (2026-11-18)

Build f9a8036a (branch claude/project-thread-1btznt). Both sides play the overhaul's new pricing, with `his-fight-together` and
`set-up-by-the-set` off on both. The ON side also has JOINT CHARGE NOW and AFTERMATH WITH FRIENDS. Same DKTC pairs both ways,
static-static, seed 1, scenarios mix. The switch side was checked in the game logs of all 8 parts: JOINT CHARGE NOW rows appear on the
ON side only, and HIS FIGHT TOGETHER and SET UP BY THE SET appear on neither side. **The coordinator stopped the batch at 10:48 UTC**
(205 of 288 games): the build thread found the cause in its own joint sum (see finding.md beside this file), and the fixed head gets a fresh batch.

## Verdict
The rule fires, and its round-one claim with both units in the fight is close (71 claimed v 77 won). It does not change how often the
army charges together. Second chargers come 0.55 a game on both sides, and ready pairs where both charge are 0.38 v 0.39 a game.
The joint figure over-claims reach (all in 79% v both in 60%) and points (+147 claimed v +49 net). The cause, per finding.md: the
enemy strikes every charger in full, and chargers block each other's landing. VP margin -90 ±168 is noise.

## 1. Claimed v happened
| | ON | OFF |
| --- | --- | --- |
| First round won ALONE, claimed v won | 71 v 73 (454 fights) | 72 v 76 (462) |
| First round won JOINT, claimed v won | 65 v 76 (78; set figure) | 52 v 77 (82; best single unit's own figure) |
| Of these, JOINT CHARGE NOW sets with both in | 71 v 77 (31) | - |
| All in (every charger reaches), claimed v came | 79% v 60% (52 sets) | - |
| Net points per fight, joint set: claimed v happened | +147 v +49 (46) | - |
| Net points per fight, alone: pick gain v net | +192 v +69 (441) | +188 v +77 (456) |

"Happened" net = target's points lost minus all chargers' points lost, over about two game turns from the declaration (models lost x
points per model, a unit gone counts in full). finding.md shows that this is not the same yardstick as the claim, which is the whole
fight in wounds. Measured the same way, round one of a joint fight with everyone in is honest (+59 claimed v +65).

## 2. Charges and ready pairs (a game)
| | ON | OFF |
| --- | --- | --- |
| Charges alone / lead of a set / second or later | 3.06 / 0.47 / 0.55 | 3.10 / 0.50 / 0.55 |
| JOINT CHARGE NOW rows (sets claimed) | 0.53 (52 sets; 51 had 2+ declare, 31 had 2+ in contact) | 0 |
| Ready pairs (2+ units with a charge on the same target in their weighed options) | 2.18 | 2.33 |
| - both charged / one / none | 0.38 / 0.88 / 0.93 | 0.39 / 0.97 / 0.97 |
| Charge picked when offered | 58% (749/1298) | 59% (773/1307) |

## 3. Headline
| | ON | OFF |
| --- | --- | --- |
| Net points per charged fight, alone / joint | +64 / +33 | +71 / +51 |
| Points lost a game | 644 | 600 |
| Own units caught in flank/rear a game | 1.50 | 1.45 |
| VP margin (ON minus OFF) | -90 ±168 (W81 L89 D35); noise | |

## Cause
In finding.md (build thread, games replayed in code): (1) the OFF side still prices second chargers by the older rules, so this is two
pricings against each other, not joint against none; (2) the joint sum strikes every charger with the enemy's full attacks, so in 2 of
3 cases the pair is priced below the better unit alone; (3) "all in" fails because chargers block each other's landing, not because of
the dice; (4) the joint net was not held against the same yardstick.

Scripts: scripts/joint.py (these tables), build.py (charges.pkl), report.py, flank.py.
