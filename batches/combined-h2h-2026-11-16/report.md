# Charge changes + shooting changes together: head-to-head against main (2026-11-16)

**Verdict: no gain. The side with everything on is behind by -31 VP a game, give or take 95 VP: inside the noise.** The two lines
add up rather than help or hurt each other: the charge changes alone were -7 ±110 on these same pairs, the shooting plan alone
(without its fixes) -19 ±92, sum -26, here -31. The shooting side kills more by shooting and magic (+27 points a game) but charges
less and destroys less in combat (-32 a game, -12 run down), so kills come out even. On pairs with a shooting-heavy list the
combined side is level (+5 ±134), on the other pairs behind (-63 ±135); neither is outside the noise.

Batch: 288 games, the same 144 DKTC pairs and seeds as the charge worth head-to-head (Hero v Hero, seed 1, scenarios mix), each pair
played twice. Changed side: branch `claude/project-thread-tnhumk` at `ea652ef11` (main f3d2be2c + honest charge odds + charge band +
honest worth + shooting plan with its three target fixes). Other side: `charge-odds`, `charge-band`, `honest-worth`, `shooting-plan`
switched off = main. 288 of 288 games ended, no stalls, no re-runs. Every part's rules-off list named all 22 tags for the right side;
no HONEST WORTH, CHARGE BAND or shooting-plan row was written on the switched-off side (no leak). **No sim bugs** (0 findings).

## 1. Morten's five headline numbers

| # | Number | **Changes on** | **Main** | Read |
| --- | --- | --- | --- | --- |
| 1 | VP margin per game | **-31** | +31 | **-31 ±95** (paired over 144 pairs), inside noise |
| 2 | First round won when charging | 74% | 74% | same |
| 3 | Net points per charged fight | +78 | +96 | 18 worse (damage counted +80 v +98) |
| 4 | Points lost per game | 755 | 740 | 15 more, within noise |
| 5 | Free units caught in flank or rear (per game, lower is better) | 0.68 | 0.63 | a little worse, within noise |

W/D/L of the changed side 111 / 56 / 121; pairs ahead over both games 61, behind 83. Going first -70, second +7 (each ±200+).
As Mine -211, as Opponent +149: the lists; the pairing cancels it.

Note on row 2: this is the repo's compare-batches reading. The charge worth report used another script for this row (76 v 71);
read 74 v 74 as "no difference" rather than against that figure.

Diagnostics (not targets): charge contacts a game 3.5 v 3.8; points that never fought 36% v 38%; lone characters that fought
78% v 75%; joined characters whose unit fought 47% v 41%.

## 2. Do the two lines add up? (question a)

All on the same 144 pairs unless said. Margin of the changed side per game.

| Batch | All pairs | Pairs with a shooting-heavy list (67) | Other pairs (77) |
| --- | --- | --- | --- |
| **Combined (this batch)** | **-31 ±95** | **+5 ±134** | **-63 ±135** |
| Charge worth alone (same pairs, same seeds) | -7 ±110 | -85 ±148 | +60 ±159 |
| Combined minus charge worth, pair by pair | -24 ±118 | +90 ±172 | -123 ±162 |
| Shooting plan without the fixes (last night, same pairs) | -19 ±92 | - | - |
| Shooting plan with the fixes (this morning, 144 shooting-heavy pairs, other pairs) | - | +74 ±107 | - |

Shooting-heavy list = the 9 lists the shooting fixes batch used (3+ war machines or 30%+ points in shooting units).

Reading (warnings, not plans):
- **They add up.** Charge worth -7 plus shooting plan -19 = -26; combined -31. On heavy pairs, charge worth -85 plus the fixed plan
  +74 = -11; combined +5. Nothing points to the two cancelling each other, and nothing to a bonus from having both.
- Pair by pair against charge worth, adding the shooting changes is worth about +90 on heavy pairs and -123 on the others. Both are
  inside their bands, but the direction fits the shooting batch: the plan helps armies that shoot and costs armies that do not.
  Same army with the changes minus without, by kind of army: shooting-heavy armies -67 ±227 (100 army-games), others -60 ±180 (188).
- Stance split (gunline = the 49 army-games of head-to-head 2): gunline armies -86 ±312, others -58 ±149.

## 3. Shoot or charge: the one-yardstick question (question b)

The merge builder's worry: a charge now pays for the charger's own expected losses, a shoot job pays nothing for the shooter's
risk, so close calls should tilt to shooting. What the logs show:

| | Changes on | Main |
| --- | --- | --- |
| Close calls where a unit **shot instead of charging** (chosen shoot, runner-up a charge) | **61** (0.21 a game) | 53 (0.18) |
| Close calls where it **charged instead of shooting** | 184 (0.64 a game) | 189 (0.66) |
| Share of shoot-or-charge close calls that went to shooting | 25% | 22% |
| What the shots earned (VP of the wounds that unit's shooting did that turn) | +11 ±6 | +10 ±6 |
| What the charges earned (target VP gone minus own VP lost over 2 turns) | +43 ±22 | +45 ±25 |
| ...and the charge was declared that turn | 60% | 60% |
| ONE YARDSTICK rows that decided between a shot and a charge | 7 in 288 games | - |

A close call is counted where the unit's rule rows that turn name the taken job and a runner-up, one a shot and the other a charge
(the log names only one runner-up, so close calls outside rule rows are not seen).

Reading (warnings, not plans): the tilt is real in direction but small, 3 points of close calls (8 more shots in 288 games), well
inside the noise. The one-yardstick figure itself almost never sits between a shot and a charge (7 times). Shots taken over a
charge earn about a quarter of what charges taken over a shot earn, but over one turn against two: not a like-for-like price, only
a sign that the trade is not a bargain. Not big enough to explain the combat loss below.

## 4. Charges by odds band

Fights the side charged into, by the odds it was told; net per fight in brackets (first: as Mine, second: as Opponent).

| Band | Changes on | Main | Charge worth batch: on / main |
| --- | --- | --- | --- |
| Long shots (under 50%) | 126 (+29 / +75) | 130 (+96 / +41) | 117 / 146 |
| Sweet spot (55-75%) | 138 (+41 / +87) | 126 (+55 / +96) | 133 (60-75%) / 115 |
| 90%+ not overkill | **214** (+84 / +160) | **269** (+169 / +93) | 194 / 280 |
| 90%+ overkill | **61** (+68 / +96) | **86** (+100 / +92) | 70 / 82 |
| All charged fights | **758** | **823** | 748 / 868 |

- Same shape as the charge worth batch: fewer sure charges (214 v 269) and fewer overkill piles (61 v 86); long shots now even.
- The gap in charged fights is smaller with the shooting plan on (65 fewer, against 120 fewer alone).

## 5. Other KPIs side by side (per game)

| Measure | Changes on | Main |
| --- | --- | --- |
| Charges declared / contacts | 5.0 / 3.5 | 5.2 / 3.8 |
| Games where this side made the first charge contact | 47% | 53% |
| Sides that never made charge contact | 11% | 10% |
| Joint charges (2+ units on one target) | 0.4 | 0.4 |
| Close-in set-ups that charged that target next turn | 15% | 15% |
| Charge contacts in the flank or rear | 52% | 48% |
| Points destroyed in combat | **350** | **382** |
| Points run down | 83 | 95 |
| Points destroyed by shooting units | **58** | **48** |
| Points destroyed by war machines | **61** | **52** |
| Points destroyed by magic | 61 | 53 |
| Volleys lost to marching | **1.64** | 2.02 |
| Missiles lost to marching | 0.81 | 0.89 |
| Shoot objectives carried out (shot the named target) | 33% | 49% |
| Magic missiles tried each own turn (when they could be) | 33% (48%) | 35% (48%) |
| Winner followed up or pursued | 90% | 88% |
| Idle units | 1.4 | 1.5 |
| Points that never moved of their own | 240 | 222 |
| Turns played defensive | 16% | 16% |

"Shoot objectives carried out" drops because the fire plan re-picks the target at the Shooting phase; the unit still shoots
(shoot jobs happened 59% v 61%), at another target.

Full tables: compare-all.md (A = mine arm, B = opp arm) and kpis-on-v-off.md (remapped to changes on / main).

### Jobs claimed v happened

| Job | Changes on: jobs, happened, planned v won VP a job | Main |
| --- | --- | --- |
| charge | 1072, 59%, **81 v 94** | 1192, 59%, 98 v 99 |
| close in | 1408, 25%, 46 v 28 | 1457, 26%, 61 v 30 |
| advance | 3641, 17%, 18 v 28 | 3573, 17%, 19 v 27 |
| shoot | 1963, 59%, 15 v 75 | 1917, 61%, 9 v 76 |
| hold | 1300, 35%, 60 v 0 | 1228, 35%, 62 v 0 |
| support | 1336, 91%, -7 v 0 | 1329, 90%, -8 v 0 |
| join | 209, 97%, 39 v 0 | 201, 96%, 29 v 0 |

Charges stay honest with the shooting plan on (81 promised, 94 won). HONEST WORTH changed the option 96 times (0.33 a game).

### VP by source (per game)

| Source | Changes on | Main |
| --- | --- | --- |
| Kills | 786 | 796 |
| Objectives | 562 | 575 |
| Leaders | 52 | 61 |
| Points lost | 755 | 740 |
| Units lost | 5.0 | 5.0 |

## 6. Shots at the top killer

Top killer = the enemy unit that took most of this side's points in fights (read after the game). Free = alive, not in a unit,
not in a fight, when the shot was fired.

| | Changes on | Main |
| --- | --- | --- |
| War machine shots at the top killer when it was free | 24% (124 of 512) | 26% (155 of 592) |
| Magic missiles at the top killer when it was free | 19% (68 of 354) | 19% (69 of 354) |
| Other shooting at the top killer when free | **23%** (363 of 1,572) | **31%** (498 of 1,581) |
| Top killer dead by round 3 | 9% (22 of 255) | 6% (15 of 256) |
| Top killer dead by the end | 27% | 27% |
| Enemy's dearest unit dead by round 3 | 12% | 11% |

As in the shooting fixes batch: the plan does not put more shots on the eventual top killer; it spreads them over the dear units.

## 7. What this means (warnings, not plans)

- Neither line, alone or together, shows a gain in the result on these pairs. The changes make the charges honest and the guns
  busier (+27 points a game by shooting and magic, fewer volleys lost to marching), but the side charges less and destroys 32 fewer
  points a game in combat, and the two cancel.
- The shoot-for-charge tilt the builder feared is there in direction but tiny (0.03 a game); it is not the cause of the combat gap.
  The combat gap is the honest odds passing up 85-90% "sure" charges, the same as in all three charge batches.
- The split by pair kind points one way: shooting changes help shooting-heavy pairs and cost the others. That is a hypothesis
  inside the noise, not a result.

## Files

- Results: mine-1..4, opp-1..4; counts.log; compare-all.md; kpis-on-v-off.md.
- Replays: branch `claude/project-thread-01z2l1` (8 batch folders ch-h2h-{mine,opp}-ea652ef-p1..4; on-site.txt lists them).
  Not on main.
- scripts/: the charge worth batch's scripts with the folder changed, the shooting fixes batch's tk.py, extra.py, leak.py, plus
  split.py (pair kinds and pair-by-pair against charge worth) and shoot_or_charge.py (question b).
