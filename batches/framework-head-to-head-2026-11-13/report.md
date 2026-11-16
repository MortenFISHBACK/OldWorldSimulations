# Job framework head-to-head: framework on one side only (2026-11-13)

> **Caveat (added 22:00 UTC, from the switch builder):** in all 288 games of this batch BOTH sides deployed without the computer's
> deployment plan. The one-side switch made the plan's role check fail silently for both sides (fixed at c6fc19ce on
> claude/project-thread-ks71g3). It was symmetric, so neither side was favoured, but the games were played from different, probably
> worse, deployments than normal play. Read the -81 VP with that in mind. A rerun on c6fc19ce would measure the framework with normal deployment.

Build e44102839 (branch claude/project-thread-ks71g3: framework candidate db7ca9c5d plus the one-side switch). Script opponent v script opponent
(Medium v Medium), 144 Danish Team Championship pairs, seed 1, scenarios mixed. Every pair played twice: once with the framework on Mine
(fwmine-1..4) and once with it on Opponent (fwopp-1..4), so army, side and first-turn effects cancel. 8 parts of 36 games, each in its own
4-core container; my part (fwmine-1) took 1 h 41 min.

**Games: 281 of 288 ended. 140 matched pairs (280 games) are compared.** Left out: pairs L2033, L2433 and L3033 in both halves (the game
never starts, see section 6) and L1731 in fwopp-3 (fails after the game, so its fwmine game is left out too).

## 1. Headline: the framework side loses slightly. Within noise, but no sign of a gain

| | Games | Framework VP margin a game | Noise band (95%) | Framework won / drew / lost |
| --- | --- | --- | --- | --- |
| **All matched games** | 280 | **-81** | ±100 (paired) | 97 / 61 / 122 |
| Framework on Mine | 140 | -122 | ±202 | 45 / 31 / 64 |
| Framework on Opponent | 140 | -40 | ±196 | 52 / 30 / 58 |
| Framework side went first | 140 | +104 | ±216 | 57 / 28 / 55 |
| Framework side went second | 140 | -265 | ±176 | 40 / 33 / 67 |

- Margin = framework side's VP minus the other side's VP, a game. The band is from the 140 pairs, with each pair's two games summed
  (army and first-turn effects cancel within a pair). Over the pairs, the framework side came out ahead in 65 and behind in 75.
- The side split (Mine -122, Opponent -40) is within noise of each other, so the side effect cancels as intended.
- **Going second is where it loses**: -265 VP a game, outside the noise band. Going first it is level (+104 ± 216). Section 5 shows why:
  the framework side charges less and waits, so when it goes second it is charged first.
- First interim (72 games, parts 1) said +178 ± 193. The full batch moved it to -81 ± 100. The interim was noise.

VP by kind, a game (from games.csv):

| | Framework | No framework |
| --- | --- | --- |
| VP from kills | 732 | 796 |
| VP from objectives | 547 | 557 |
| VP from the General (leaders) | 56 | 60 |
| Units lost | 5.1 | 4.8 |
| Points lost | 752 | 690 |

The framework side scores about the same on objectives but kills about 64 VP a game less and loses about 62 points a game more.

## 2. Every KPI side by side

Framework = Mine in fwmine games plus Opponent in fwopp games; No framework = the other side. The last two columns show the two halves
separately (framework on Mine games / framework on Opponent games). Counts "(x of y)" are pooled; other numbers are the mean of the two halves.

## KPIs (Morten 2026-11-10)

| KPI | Target | **Framework** | **No framework** | fw (Mine games) / fw (Opp games) | off (Mine games) / off (Opp games) |
| --- | --- | --- | --- | --- | --- |
| Turns the army played defensive (its shooting and magic 1.5x the enemy's; else offensive) |  | 38% | 0% | 55% / 21% | 0% / 0% |
| Winner chose to follow up after the loser gave ground |  | 96% | 98% | 97%; on the table 98% / 96%; on the table 97% | 99%; on the table 99% / 96%; on the table 97% |
| Winner chose to pursue after the loser fell back in good order |  | 80% | 88% | 72%; on the table 78% / 87%; on the table 87% | 87%; on the table 93% / 90%; on the table 92% |
| Winner chose to pursue after the loser fled |  | 72% | 70% | 68%; on the table 75% / 77%; on the table 81% | 82%; on the table 85% / 57%; on the table 69% |
| Winner chose to follow up or pursue (all three) |  | 87% | 90% | 86%; on the table 89% / 88%; on the table 90% | 92%; on the table 94% / 87%; on the table 90% |
| Magic missiles tried each own turn | 50%+ | 32% | 32% | 33% / 32% | 31% / 32% |
| tried when they could be (not in combat, slain, fleeing or off the table) | 50%+ | 49% | 46% | 49% / 49% | 46% / 46% |
| Random moves turned off the straight line at the nearest enemy (risk weighed) |  | 52% | - | 53% / 50% | - / - |
| Points that never fought | lower | 36% | 37% | 36% / 36% | 38% / 36% |
| infantry points that never fought | lower | 44% | 48% | 39% / 50% | 54% / 43% |
| Units over 100 pts that earned no points (no kill, no objective) | lower | 58% | 56% | 56% / 60% | 57% / 56% |
| Bound items with a magic missile used (at least once a game) |  | 76% | 82% | 85% / 66% | 72% / 91% |
| Bound items with another spell used |  | 48% | 50% | 53% / 44% | 44% / 55% |
| One-use items used (Chalice of Dark Rain, Arch-Lightning Rod ...) |  | 50% | 48% | 55% / 44% | 46% / 51% |
| their share of the points of units over 100 pts | lower | 52% | 50% | 51% / 54% | 50% / 51% |

## KPIs (Morten 2026-11-10)

| Measure | **Framework** | **No framework** | fw (Mine games) / fw (Opp games) | off (Mine games) / off (Opp games) |
| --- | --- | --- | --- | --- |
| Charged units hit only in a flank or rear (% of formed units charged) | 50% | 47% | 49% (198) / 52% (165) | 45% (113) / 49% (154) |
| ...free all their last turn and able to turn (per game) | 0.83 | 0.63 | 0.88 / 0.79 | 0.57 / 0.69 |
| ...left out: fought, charged, random mover or war machine in their own turn (per game) | 0.21 | 0.15 | 0.28 / 0.14 | 0.09 / 0.20 |
| ...with the charger already in that arc before they moved (per game) | 0.57 | 0.46 | 0.61 / 0.54 | 0.42 / 0.50 |
| Turned to face a threat or took a way out: FACES THE THREAT (per game) | 1.58 | 1.38 | 1.85 / 1.30 | 1.12 / 1.64 |
| Stood instead of an exposed job's move: SAFER THAN THE JOB (per game) | 0.97 | 0.90 | 1.04 / 0.89 | 0.88 / 0.92 |
| Kept its job with an enemy able to reach its flank or rear: NOT TURNED (per game) | 7.41 | 7.08 | 7.30 / 7.52 | 7.47 / 6.69 |

### Charges a game and per unit by the wizard it carries

| Charges | **Framework** | **No framework** | fw (Mine games) / fw (Opp games) | off (Mine games) / off (Opp games) |
| --- | --- | --- | --- | --- |
| Charges declared a game | 4.8 | 5.8 | 3.8 / 5.7 | 6.5 / 5.0 |
| Charges that made contact a game | 3.3 | 4.0 | 2.8 / 3.9 | 4.5 / 3.6 |
| per unit a game, units carrying a magic-missile wizard (or one alone) | 0.54 declared, 0.41 contact | 0.76 declared, 0.57 contact | 0.60 declared, 0.47 contact (100 units) / 0.48 declared, 0.34 contact (82 units) | 0.64 declared, 0.46 contact (80 units) / 0.88 declared, 0.67 contact (98 units) |
| per unit a game, units carrying another wizard (or one alone) | 0.56 declared, 0.36 contact | 0.97 declared, 0.76 contact | 0.34 declared, 0.17 contact (35 units) / 0.77 declared, 0.55 contact (53 units) | 1.15 declared, 0.85 contact (54 units) / 0.79 declared, 0.66 contact (29 units) |
| per unit a game, the other units (no war machines, no joined characters) | 0.55 declared, 0.39 contact | 0.66 declared, 0.45 contact | 0.48 declared, 0.36 contact (974 units) / 0.62 declared, 0.42 contact (1190 units) | 0.70 declared, 0.48 contact (1183 units) / 0.62 declared, 0.43 contact (975 units) |

## Movement (Morten 2026-11-11)

| Measure | **Framework** | **No framework** | fw (Mine games) / fw (Opp games) | off (Mine games) / off (Opp games) |
| --- | --- | --- | --- | --- |
| Games where this side made the first charge contact | 40% (112 of 281) | 60% (169 of 281) | 35% (49 of 141) / 45% (63 of 140) | 65% (92 of 141) / 55% (77 of 140) |
| Round of a side's first charge contact (sides that made one) | 2.9 | 2.5 | 3.0 / 2.7 | 2.5 / 2.6 |
| Sides that never declared a charge | 7% (20 of 287) | 6% (16 of 287) | 9% (13 of 144) / 5% (7 of 143) | 5% (7 of 144) / 6% (9 of 143) |
| Sides that never made charge contact | 14% (39 of 287) | 8% (22 of 287) | 17% (24 of 144) / 10% (15 of 143) | 5% (7 of 144) / 10% (15 of 143) |
| Charges declared a game | 4.7 | 5.8 | 3.8 / 5.6 | 6.4 / 5.1 |
| Charge contacts made a game | 3.3 | 4.1 | 2.8 / 3.8 | 4.5 / 3.7 |
| Charge contacts received a game | 4.1 | 3.3 | 4.5 / 3.7 | 2.8 / 3.8 |
| Joint charges a game (2+ units on one target in one turn) | 0.5 | 0.6 | 0.4 / 0.5 | 0.6 / 0.5 |
| share of charged targets hit by 2+ units | 16% (128 of 804) | 15% (153 of 1001) | 15% (51 of 351) / 17% (77 of 453) | 16% (86 of 547) / 15% (67 of 454) |
| Lone charges that a friend follows on the same target next turn | 5% (36 of 676) | 6% (50 of 848) | 5% (15 of 300) / 6% (21 of 376) | 6% (26 of 461) / 6% (24 of 387) |
| Set-ups (close in to charge next turn) that charged that target next turn | 14% (238 of 1746) | 14% (204 of 1495) | 13% (89 of 675) / 14% (149 of 1071) | 14% (115 of 824) / 13% (89 of 671) |
| ... and made contact | 9% (160 of 1746) | 10% (155 of 1495) | 10% (70 of 675) / 8% (90 of 1071) | 10% (82 of 824) / 11% (73 of 671) |
| ... with a friend on it too | 2% (41 of 1746) | 3% (40 of 1495) | 3% (17 of 675) / 2% (24 of 1071) | 3% (22 of 824) / 3% (18 of 671) |
| Set-ups missed (no charge on that target next turn) | 86% (1508 of 1746) | 86% (1291 of 1495) | 87% (586 of 675) / 86% (922 of 1071) | 86% (709 of 824) / 87% (582 of 671) |
| Charge contacts in the flank or rear (arc known) | 48% (456 of 951) | 50% (581 of 1171) | 46% (188 of 405) / 49% (268 of 546) | 49% (319 of 648) / 50% (262 of 523) |
| in the rear | 11% (106 of 951) | 9% (107 of 1171) | 11% (44 of 405) / 11% (62 of 546) | 9% (56 of 648) / 10% (51 of 523) |
| Declared charges in the flank or rear (arc known) | 49% (663 of 1355) | 49% (806 of 1658) | 48% (263 of 552) / 50% (400 of 803) | 48% (450 of 928) / 49% (356 of 730) |
| Marches that gave up a magic missile a game (made: a failed march test or a MARCH CHECK turn left out) | 0.6 | 0.4 | 0.7 / 0.4 | 0.3 / 0.6 |

## Quality by phase (per game and side)

| Phase | Number | **Framework** | **No framework** | fw (Mine games) / fw (Opp games) | off (Mine games) / off (Opp games) |
| --- | --- | --- | --- | --- | --- |
| Deployment | Characters standing alone | 0.0 | 0.0 | 0.0 / 0.0 | 0.0 / 0.0 |
| Strategy | Charge objectives carried out (made contact) | 49% (523 of 1077) | 48% (651 of 1367) | 54% (236 of 440) / 45% (287 of 637) | 46% (359 of 782) / 50% (292 of 585) |
| Strategy | Shoot objectives carried out (shot that target) | 46% (762 of 1661) | 46% (895 of 1943) | 44% (498 of 1136) / 50% (264 of 525) | 49% (314 of 645) / 45% (581 of 1298) |
| Strategy | Close-in objectives charged next turn | 14% (241 of 1746) | 14% (204 of 1495) | 13% (90 of 675) / 14% (151 of 1071) | 14% (115 of 824) / 13% (89 of 671) |
| Strategy | Support requests answered (helper made contact too) | 53% (68 of 129) | 56% (92 of 165) | 68% (27 of 40) / 46% (41 of 89) | 58% (66 of 113) / 50% (26 of 52) |
| Strategy | Augments that last this turn, on a unit that fought or charged that turn | 90% (9 of 10) | 89% (8 of 9) | 86% (6 of 7) / 100% (3 of 3) | 100% (3 of 3) / 83% (5 of 6) |
| Strategy | Hexes on a unit its side charged or shot that turn | 42% (50 of 118) | 63% (81 of 129) | 44% (24 of 54) / 41% (26 of 64) | 62% (40 of 65) / 64% (41 of 64) |
| Strategy | Joined characters whose unit fought | 40% (85 of 214) | 39% (91 of 235) | 42% (56 of 134) / 36% (29 of 80) | 36% (30 of 83) / 40% (61 of 152) |
| Strategy | Lone characters that fought | 71% (582 of 817) | 72% (573 of 798) | 73% (294 of 405) / 70% (288 of 412) | 67% (277 of 414) / 77% (296 of 384) |
| Movement | Charges halted short of contact | 0.2 | 0.2 | 0.1 / 0.2 | 0.3 / 0.2 |
| Movement | Idle units | 1.4 | 1.5 | 1.0 / 1.7 | 1.9 / 1.1 |
| Movement | Points that never moved of their own | 205.6 | 205.4 | 267.2 / 144.0 | 144.6 / 266.3 |
| Movement | Fights charged into per game | 2.9 | 3.5 | 2.5 / 3.2 | 3.9 / 3.2 |
| Movement | Charges with odds: long shots (under 50%) | 36 | 53 | 27 of 298, net +1 / 45 of 350, net +9 | 61 of 462, net +19 / 45 of 400, net +38 |
| Movement | Charges with odds: sweet spot (55-75%) | 46 | 70 | 36 of 298, net +66 / 56 of 350, net +98 | 79 of 462, net +67 / 61 of 400, net +74 |
| Movement | Charges with odds: overkill (90%+, target under 250 pts, chargers over 3x) | 44 | 58 | 47 of 298, net +104 / 41 of 350, net +97 | 53 of 462, net +103 / 62 of 400, net +76 |
| Movement | Charges with odds: 90%+ not overkill (target 250+ pts or chargers up to 3x) | 121 | 151 | 120 of 298, net +108 / 122 of 350, net +133 | 165 of 462, net +139 / 137 of 400, net +107 |
| Shooting | Shots by shooting units (incl. breath weapons) | 8.7 | 8.6 | 8.5 / 8.8 | 8.4 / 8.8 |
| Shooting | aimed at a top-3 enemy unit or that turn's charge target | 50% (586 of 1161) | 52% (613 of 1190) | 52% (489 of 932) / 42% (97 of 229) | 38% (90 of 237) / 55% (523 of 953) |
| Shooting | Points destroyed by shooting units | 49.8 | 56.1 | 74.9 / 24.7 | 36.5 / 75.8 |
| Shooting | War machine shots | 4.0 | 4.2 | 6.5 / 1.6 | 1.6 / 6.7 |
| Shooting | Points destroyed by war machines | 49.3 | 52.7 | 79.3 / 19.4 | 30.0 / 75.4 |
| Magic | Magic missiles cast | 1.5 | 1.5 | 1.9 / 1.1 | 1.1 / 1.9 |
| Magic | aimed at a top-3 enemy unit or that turn's charge target | 38% (164 of 437) | 42% (176 of 418) | 36% (100 of 279) / 41% (64 of 158) | 35% (54 of 153) / 46% (122 of 265) |
| Magic | Wounds caused by magic missiles | 2.8 | 2.5 | 4.1 / 1.4 | 1.4 / 3.7 |
| Magic | Wounds caused by other spells | 1.3 | 1.2 | 1.7 / 0.9 | 0.9 / 1.6 |
| Magic | Points destroyed by magic (all spells) | 58.8 | 60.5 | 92.8 / 24.8 | 36.8 / 84.2 |
| Magic | Augments / hexes / assailments / vortexes cast | 1.4 | 1.4 | 1.2 / 0.4 / 0.7 / 0.2 / 1.7 / 0.6 / 0.4 / 0.1 | 1.7 / 0.6 / 0.4 / 0.1 / 1.1 / 0.5 / 0.6 / 0.1 |
| Combat | Points destroyed in combat | 327.4 | 356.6 | 281.0 / 373.7 | 396.7 / 316.6 |
| Combat | Points run down | 98.3 | 103.7 | 72.9 / 123.8 | 119.5 / 87.9 |
| Combat | Net points per charged fight, damage counted | +84 | +81 | +71 / +96 | +90 / +72 |
| Combat | Net per 100 charger points, damage counted | +29.7 | +27.4 | +26.1 / +33.3 | +30.7 / +24.0 |
| Combat | First round won (charged fights) | 68% | 66% | 72% / 64% | 62% / 70% |
| Combat | Net points per charged fight | +79 | +78 | +68 / +90 | +90 / +67 |
| Combat | Net points per supported fight / lone fight | +132 | +108 | +137 / +56 / +127 / +83 | +112 / +86 / +103 / +61 |
| Combat | Charged fights on a top-3 enemy unit | 155 | 209 | 116 of 351 / 194 of 453 | 250 of 547 / 168 of 454 |
| Game | Points lost | 752.3 | 689.9 | 774.9 / 729.7 | 697.5 / 682.3 |
| Game | VP from objectives | 547.5 | 556.5 | 543.5 / 551.4 | 565.0 / 548.1 |
| Game | Lone holders (player turns) | 2.5 | 2.5 | 2.5 / 2.6 | 2.3 / 2.8 |

## Opponent rules (fired a game; in each half: figure / won / lost VP a game). Rules marked "-" for no framework are framework-only rules (fired a game, figure / won / lost VP a game)

| Rule | **Framework** | **No framework** | fw (Mine games) / fw (Opp games) | off (Mine games) / off (Opp games) |
| --- | --- | --- | --- | --- |
| ALREADY CARRIED | 0.0 (+0 / 0 / 0) | 0.0 (+0 / 0 / 0) | 0.0 (+0 / 0 / 0) / - | - / 0.0 (+0 / 0 / 0) |
| ARRIVAL HUNT | 0.1 | 0.1 | 0.0 (+0 / 0 / 0) / 0.1 (+2 / 0 / 1) | 0.1 (+1 / 0 / 0) / 0.0 (+0 / 0 / 0) |
| ARTILLERY RE-ROLL WEIGHED | 0.5 | 0.6 | 0.8 (+0 / 0 / 6) / 0.2 (+0 / 0 / 3) | 0.2 (+0 / 0 / 1) / 0.9 (+0 / 0 / 6) |
| BACKUP TARGETS | 1.3 | 1.1 | 1.3 (+10 / 0 / 27) / 1.3 (+11 / 0 / 28) | 1.2 (+10 / 0 / 16) / 1.0 (+7 / 0 / 30) |
| BEST FACING | 0.6 | - | 0.7 (+24 / 0 / 18) / 0.6 (+26 / 0 / 19) | - / - |
| BEST FIRST | 3.4 | - | 3.6 (+166 / 165 / 59) / 3.2 (+136 / 87 / 56) | - / - |
| BEST OVERALL | 0.6 | 0.5 | 0.6 (+32 / 0 / 26) / 0.7 (+50 / 0 / 20) | 0.4 (+24 / 0 / 15) / 0.5 (+23 / 0 / 23) |
| BEST PREY | 0.8 | 5.2 | 0.8 (+40 / 34 / 11) / 0.8 (+41 / 29 / 13) | 5.4 (+313 / 251 / 119) / 5.1 (+306 / 239 / 92) |
| BEST PRIZE | 0.1 | 0.1 | 0.1 (-3 / 2 / 4) / 0.1 (+0 / 4 / 5) | 0.1 (-1 / 6 / 5) / 0.1 (-1 / 3 / 1) |
| BIG CHARACTER SAFETY | 0.2 | 0.2 | 0.3 (-1 / 0 / 13) / 0.2 (-1 / 0 / 15) | 0.2 (-0 / 0 / 10) / 0.2 (-1 / 0 / 7) |
| BLOCKED CHARGE HANDED OVER | 0.0 (+2 / 2 / 0) | 0.0 (+1 / 1 / 0) | - / 0.0 (+2 / 2 / 0) | - / 0.0 (+1 / 1 / 0) |
| BLOCKED CHARGE SKIPPED | 0.2 | 0.1 | 0.1 (+0 / 3 / 0) / 0.2 (+0 / 15 / 3) | 0.1 (+0 / 7 / 1) / 0.0 (+0 / 3 / 0) |
| BLOCKED WHEEL | 0.5 | 0.5 | 0.4 (+10 / 0 / 5) / 0.5 (+11 / 0 / 6) | 0.5 (+1 / 0 / 7) / 0.5 (+11 / 0 / 8) |
| BOMBING RUN | 0.1 (+3 / 0 / 2) | 0.1 | 0.1 (+3 / 0 / 2) / - | 0.0 (+0 / 0 / 1) / 0.1 (+2 / 2 / 2) |
| BOUND ASSAILMENT | 0.0 | - | 0.0 (+0 / 0 / 1) / 0.0 (+0 / 0 / 1) | - / - |
| CANNON PLAN MISSED | 0.5 | 0.5 | 0.8 (+0 / 83 / 11) / 0.1 (+0 / 7 / 3) | 0.1 (+0 / 13 / 0) / 0.9 (+0 / 102 / 10) |
| CANNON PLANNED TARGET | 3.0 | 3.1 | 4.9 (+179 / 363 / 96) / 1.1 (+40 / 42 / 22) | 1.2 (+55 / 84 / 18) / 5.0 (+191 / 321 / 86) |
| CARRIES OUT COUNTER | 0.1 | 0.0 | 0.1 (-1 / 4 / 3) / 0.0 (-2 / 2 / 0) | 0.0 (-1 / 6 / 1) / 0.0 (-0 / 0 / 0) |
| CARRIES OUT SET-UP | 0.1 | 0.1 | 0.1 (-1 / 14 / 1) / 0.1 (-1 / 22 / 7) | 0.1 (+1 / 16 / 0) / 0.1 (-3 / 16 / 6) |
| CAST JOB | 0.3 | 0.7 | 0.3 (+12 / 26 / 4) / 0.3 (+5 / 26 / 13) | 0.6 (+13 / 26 / 38) / 0.8 (+30 / 50 / 9) |
| CASTING BLOCK | 0.0 | 0.1 | 0.0 (+10 / 5 / 0) / 0.0 (+0 / 1 / 0) | 0.0 (+0 / 0 / 0) / 0.3 (+22 / 15 / 1) |
| CASTS AFTER FRIENDS | 0.7 | 0.6 | 0.8 (+0 / 0 / 42) / 0.5 (+0 / 0 / 17) | 0.3 (+0 / 0 / 27) / 0.8 (+0 / 0 / 45) |
| CATCH FLIERS | 0.0 | 0.0 | 0.0 (+1 / 0 / 0) / 0.0 (+0 / 0 / 0) | 0.0 (+0 / 0 / 0) / 0.0 (+1 / 0 / 0) |
| CATCH ODDS | - | 0.0 (+1 / 0 / 0) | - / - | - / 0.0 (+1 / 0 / 0) |
| CHAFF PASSED | 0.2 | 0.2 | 0.2 (-0 / 3 / 12) / 0.2 (-0 / 1 / 4) | 0.1 (-0 / 4 / 3) / 0.2 (-1 / 1 / 3) |
| CHAMPION TAKES THE CHALLENGE | 0.0 (+0 / 2 / 0) | 0.0 | - / 0.0 (+0 / 2 / 0) | 0.0 (+0 / 0 / 0) / 0.0 (+3 / 0 / 0) |
| CHARGE NOW WEIGHED | 0.5 | 0.6 | 0.5 (-41 / 24 / 10) / 0.5 (-51 / 9 / 19) | 0.6 (-42 / 23 / 30) / 0.6 (-60 / 21 / 16) |
| CHARIOT NO STATIC JOB | 0.1 (+0 / 3 / 2) | 0.2 | 0.1 (+0 / 3 / 2) / - | 0.1 (+0 / 6 / 3) / 0.4 (+0 / 10 / 4) |
| CHARIOT WIZARD CAREFUL | 0.1 | 0.1 | 0.1 (-1 / 5 / 10) / 0.1 (-1 / 3 / 16) | 0.1 (-1 / 3 / 13) / 0.1 (-1 / 0 / 10) |
| CHEAP HELPER | 0.1 | 0.1 | 0.0 (+0 / 4 / 0) / 0.1 (+0 / 1 / 1) | 0.1 (+0 / 6 / 2) / 0.0 (+0 / 2 / 2) |
| COMBAT PIVOT | 0.5 | 0.4 | 0.4 (+0 / 11 / 22) / 0.5 (+0 / 20 / 37) | 0.4 (+0 / 28 / 14) / 0.4 (+0 / 14 / 30) |
| CONVEYANCE SEARCH | 0.8 | 0.6 | 0.9 (+132 / 41 / 47) / 0.6 (+97 / 14 / 30) | 0.4 (+69 / 16 / 36) / 0.8 (+146 / 31 / 53) |
| COUNTER-CHARGE COVER | 9.0 | 7.5 | 9.5 (+822 / 0 / 215) / 8.5 (+775 / 0 / 167) | 7.0 (+624 / 0 / 139) / 7.9 (+639 / 0 / 170) |
| DEFENSIVE ARMY | 0.3 | - | 0.4 (-0 / 29 / 8) / 0.3 (-0 / 0 / 1) | - / - |
| EDGE GIVE GROUND | 0.1 | 0.1 | 0.1 (+5 / 18 / 0) / 0.1 (+5 / 12 / 7) | 0.1 (+3 / 16 / 1) / 0.1 (+4 / 21 / 3) |
| ELIXIR WORTH | 0.0 | 0.0 | 0.0 (+0 / 0 / 0) / 0.0 (+2 / 0 / 0) | 0.0 (+1 / 0 / 2) / 0.0 (+0 / 0 / 0) |
| ENGINEER BY LORE | 0.1 (+0 / 0 / 0) | 0.1 (+0 / 0 / 0) | 0.1 (+0 / 0 / 0) / - | - / 0.1 (+0 / 0 / 0) |
| FACES THE THREAT | 1.6 | 1.4 | 1.9 (+140 / 0 / 66) / 1.3 (+101 / 0 / 49) | 1.1 (+89 / 0 / 24) / 1.6 (+141 / 0 / 45) |
| FALLBACK BY WORTH | 5.3 | 7.5 | 4.7 (+61 / 0 / 60) / 5.9 (+59 / 0 / 61) | 8.3 (+94 / 0 / 86) / 6.6 (+94 / 0 / 83) |
| FIGHT LIFT | 0.0 | 0.1 | 0.0 (+1 / 2 / 2) / 0.0 (+0 / 0 / 0) | 0.0 (+0 / 1 / 0) / 0.1 (+0 / 0 / 2) |
| FIRE AND FLEE | 0.0 | 0.0 | 0.0 (+1 / 0 / 1) / 0.0 (+0 / 0 / 2) | 0.0 (+0 / 0 / 2) / 0.0 (+0 / 0 / 3) |
| FLANK NOT WEIGHED | 7.0 | 6.6 | 7.1 (+0 / 0 / 214) / 6.9 (+0 / 0 / 173) | 6.6 (+0 / 0 / 161) / 6.6 (+0 / 0 / 165) |
| FLEE LOSES BLESSING | 0.0 (+0 / 0 / 2) | - | - / 0.0 (+0 / 0 / 2) | - / - |
| FOCUS FIRE | 0.0 | 0.0 | 0.0 (+0 / 1 / 0) / 0.0 (+1 / 1 / 0) | 0.0 (+0 / 0 / 0) / 0.0 (+1 / 2 / 0) |
| FOLLOW UP WEIGHED | 1.0 | 1.2 | 1.0 (+113 / 0 / 39) / 1.0 (+148 / 0 / 31) | 1.2 (+147 / 0 / 32) / 1.2 (+147 / 0 / 39) |
| FRIENDS SHOTS CHECKED | 0.2 | 0.2 | 0.2 (+8 / 0 / 8) / 0.1 (+7 / 0 / 2) | 0.2 (+9 / 0 / 2) / 0.3 (+19 / 0 / 10) |
| GATEWAY ESCAPE | 0.0 (+1 / 0 / 0) | - | - / 0.0 (+1 / 0 / 0) | - / - |
| GIVES UP | 1.0 | 1.6 | 0.8 (-33 / 86 / 37) / 1.2 (-64 / 140 / 29) | 1.8 (-70 / 243 / 35) / 1.3 (-36 / 175 / 27) |
| GIVES UP ITS SCREEN | 0.1 | 0.7 | 0.0 (-0 / 3 / 0) / 0.1 (-1 / 7 / 1) | 0.8 (-18 / 59 / 16) / 0.5 (-9 / 39 / 10) |
| GROUND FLIERS | 0.0 | 0.0 (+1 / 0 / 0) | 0.0 (+1 / 0 / 0) / 0.0 (+0 / 0 / 0) | - / 0.0 (+1 / 0 / 0) |
| HELPER ALREADY ASKED | 0.1 (+0 / 6 / 2) | 0.1 | - / 0.1 (+0 / 6 / 2) | 0.1 (+0 / 12 / 0) / 0.0 (+0 / 2 / 1) |
| HELPER UNSEEN | 0.2 | 0.4 | 0.1 (+0 / 15 / 2) / 0.3 (+0 / 22 / 11) | 0.5 (+0 / 29 / 15) / 0.3 (+0 / 29 / 13) |
| HILL BY ITS CHANCE | 0.3 | - | 0.2 (-18 / 0 / 5) / 0.5 (-53 / 0 / 3) | - / - |
| HOLDS AMBUSHERS | 0.6 | 0.6 | 0.4 (+0 / 0 / 0) / 0.7 (+0 / 0 / 0) | 0.7 (+0 / 0 / 0) / 0.4 (+0 / 0 / 0) |
| HORN WORTH | 0.0 (+0 / 0 / 0) | 0.0 (+0 / 0 / 0) | - / 0.0 (+0 / 0 / 0) | 0.0 (+0 / 0 / 0) / - |
| HUNT ADVANCE | 0.2 | 0.2 | 0.2 (+5 / 10 / 7) / 0.3 (+11 / 15 / 8) | 0.3 (+15 / 31 / 8) / 0.2 (+5 / 28 / 5) |
| HUNT DROPPED | 0.1 | 0.1 | 0.1 (+0 / 6 / 1) / 0.1 (+0 / 5 / 4) | 0.1 (+0 / 5 / 4) / 0.0 (+0 / 2 / 1) |
| HUNT IN PAIRS | 0.6 | 0.6 | 0.5 (+15 / 0 / 6) / 0.7 (+29 / 0 / 20) | 0.6 (+25 / 0 / 9) / 0.5 (+15 / 0 / 12) |
| HUNT KEPT | 0.1 | 0.1 | 0.1 (+3 / 9 / 4) / 0.1 (+7 / 6 / 3) | 0.1 (+6 / 16 / 4) / 0.1 (+3 / 14 / 2) |
| HUNT RESULT | 0.2 | 0.2 | 0.2 (+13 / 11 / 3) / 0.3 (+25 / 8 / 8) | 0.3 (+34 / 15 / 10) / 0.2 (+24 / 20 / 5) |
| HUNT THE GUNS | 0.2 | 0.2 | 0.2 (+73 / 14 / 4) / 0.3 (+115 / 19 / 9) | 0.3 (+125 / 27 / 9) / 0.2 (+78 / 24 / 5) |
| INVITES THE FIGHT | 3.5 | - | 3.9 (+245 / 163 / 105) / 3.0 (+190 / 72 / 46) | - / - |
| JOINT CHARGE PLAN | 0.2 | 0.2 | 0.1 (+4 / 2 / 1) / 0.2 (+14 / 3 / 7) | 0.3 (+20 / 6 / 1) / 0.1 (+2 / 7 / 4) |
| KEEP FALLS | 0.1 | 0.1 | 0.1 (+1 / 0 / 5) / 0.0 (+0 / 0 / 0) | 0.0 (+0 / 0 / 0) / 0.1 (+1 / 0 / 8) |
| KEEPS ITS PREY | 0.0 (+0 / 1 / 1) | 0.3 | - / 0.0 (+0 / 1 / 1) | 0.4 (+4 / 12 / 14) / 0.3 (+2 / 12 / 9) |
| KEEPS ITS TARGET | 2.2 | 2.1 | 1.9 (+56 / 166 / 47) / 2.6 (+79 / 174 / 70) | 2.4 (+72 / 207 / 40) / 1.8 (+55 / 191 / 56) |
| KILLS COUNT | 1.7 | 2.1 | 1.5 (+71 / 94 / 46) / 1.9 (+101 / 148 / 36) | 2.3 (+136 / 230 / 43) / 2.0 (+101 / 168 / 60) |
| KILLS COUNT NEXT TURN | 6.8 | 10.7 | 5.5 (+160 / 250 / 123) / 8.1 (+267 / 340 / 183) | 11.4 (+450 / 542 / 238) / 9.9 (+318 / 544 / 204) |
| LONE CHARACTER SAFE SPOT | 0.6 | 0.5 | 0.6 (+29 / 15 / 33) / 0.6 (+12 / 17 / 17) | 0.5 (+15 / 17 / 23) / 0.5 (+19 / 13 / 6) |
| LONE WIZARD HOLDS BACK | 1.2 | 0.8 | 0.8 (+0 / 23 / 24) / 1.6 (+0 / 41 / 58) | 1.2 (+0 / 32 / 47) / 0.5 (+0 / 11 / 18) |
| LONG SHOT | 0.5 | - | 0.4 (+1 / 22 / 11) / 0.5 (+1 / 24 / 7) | - / - |
| LOST CHARGE | 2.5 | - | 2.8 (-57 / 137 / 102) / 2.1 (-38 / 88 / 54) | - / - |
| LURE BY WHAT IT DRAWS | 0.0 | - | 0.0 (-4 / 0 / 0) / 0.0 (-6 / 0 / 2) | - / - |
| MAKE SURE TOGETHER | 0.9 | 0.7 | 0.5 (+28 / 24 / 9) / 1.3 (+108 / 53 / 23) | 0.8 (+52 / 21 / 7) / 0.5 (+17 / 17 / 10) |
| MANOEUVRE | 0.3 | 0.2 | 0.3 (+8 / 0 / 7) / 0.3 (+9 / 0 / 7) | 0.2 (+5 / 0 / 0) / 0.2 (+7 / 0 / 4) |
| MARCH AT ESCAPER | 0.1 | 0.1 | 0.1 (+0 / 0 / 3) / 0.1 (+1 / 0 / 3) | 0.1 (+0 / 0 / 0) / 0.1 (+1 / 0 / 0) |
| MARCH CHECK | 0.6 | 0.7 | 0.7 (+29 / 0 / 34) / 0.4 (+16 / 0 / 19) | 0.6 (+24 / 0 / 15) / 0.8 (+40 / 0 / 8) |
| MARCH ODDS | 0.1 | 0.6 | 0.1 (+8 / 1 / 9) / 0.1 (+9 / 5 / 7) | 0.4 (+29 / 8 / 13) / 0.8 (+57 / 53 / 18) |
| MARCH OVER CASTS | 0.6 | 0.5 | 0.8 (+58 / 0 / 29) / 0.4 (+19 / 0 / 19) | 0.3 (+21 / 0 / 10) / 0.7 (+40 / 0 / 13) |
| MAX FOR POSITIONING | 5.3 | 4.5 | 5.3 (+218 / 0 / 107) / 5.4 (+240 / 0 / 130) | 4.5 (+186 / 0 / 96) / 4.6 (+167 / 0 / 115) |
| MISSILES IN THE MOVE | 3.5 | 3.6 | 4.2 (+140 / 0 / 121) / 2.8 (+46 / 0 / 95) | 2.9 (+51 / 0 / 106) / 4.3 (+134 / 0 / 100) |
| MISSILES NEXT TURN | 4.4 | 4.5 | 5.2 (+103 / 0 / 152) / 3.6 (+39 / 0 / 133) | 3.7 (+42 / 0 / 123) / 5.3 (+101 / 0 / 117) |
| MODEL FACING | 0.2 | 0.2 | 0.3 (+56 / 0 / 4) / 0.1 (+10 / 0 / 0) | 0.1 (+17 / 0 / 1) / 0.3 (+86 / 0 / 3) |
| MONSTER WIZARD ROAMS | 0.2 | 0.2 | 0.2 (+0 / 11 / 6) / 0.2 (+0 / 8 / 3) | 0.2 (+0 / 4 / 0) / 0.2 (+0 / 3 / 0) |
| MOVE AND CAST | 0.2 | 0.2 | 0.2 (+13 / 0 / 2) / 0.2 (+6 / 0 / 11) | 0.2 (+6 / 0 / 14) / 0.3 (+11 / 0 / 5) |
| MOVE SPELL IN RANGE | 0.5 | 0.4 | 0.7 (+23 / 0 / 23) / 0.3 (+10 / 0 / 16) | 0.3 (+10 / 0 / 23) / 0.6 (+20 / 0 / 29) |
| MOVE SPELL NOT WORTH | 0.0 (-0 / 0 / 0) | - | 0.0 (-0 / 0 / 0) / - | - / - |
| MOVE SPELL OUT OF RANGE | 0.4 | 0.4 | 0.6 (-19 / 6 / 24) / 0.2 (-8 / 2 / 10) | 0.2 (-11 / 1 / 29) / 0.6 (-23 / 9 / 31) |
| MOVE SPELL SPOT | 0.2 | 0.2 | 0.4 (+0 / 0 / 17) / 0.1 (+0 / 0 / 4) | 0.1 (+0 / 0 / 5) / 0.4 (+0 / 0 / 14) |
| MOVE TO CHARGE | 6.8 | - | 5.2 (+343 / 213 / 109) / 8.4 (+706 / 335 / 201) | - / - |
| MOVES UNITS SPELL | 0.1 | 0.1 | 0.1 (+3 / 0 / 0) / 0.1 (+1 / 0 / 0) | 0.1 (+1 / 0 / 0) / 0.1 (+3 / 0 / 0) |
| NEEDED THERE | 0.1 | 0.1 | 0.0 (+2 / 2 / 0) / 0.1 (+11 / 9 / 0) | 0.1 (+9 / 10 / 4) / 0.1 (+5 / 3 / 0) |
| NO RALLY LEFT | 0.0 (+1 / 0 / 2) | 0.0 | 0.0 (+1 / 0 / 2) / - | 0.0 (+1 / 0 / 2) / 0.0 (+3 / 0 / 2) |
| NOT NEEDED | 0.3 | 0.3 | 0.2 (-13 / 20 / 2) / 0.4 (-25 / 37 / 4) | 0.4 (-27 / 42 / 4) / 0.3 (-15 / 33 / 4) |
| NOT TURNED | 7.4 | 7.1 | 7.3 (+168 / 0 / 184) / 7.5 (+146 / 0 / 173) | 7.5 (+97 / 0 / 163) / 6.7 (+132 / 0 / 144) |
| NOT WORTH A CAST | 0.4 | 0.5 | 0.6 (-0 / 0 / 31) / 0.3 (-1 / 0 / 7) | 0.3 (-0 / 0 / 4) / 0.7 (-0 / 0 / 12) |
| OFF BEST | 15.9 | 18.7 | 15.9 (-756 / 2 / 324) / 16.0 (-827 / 8 / 288) | 18.6 (-1096 / 75 / 325) / 18.8 (-999 / 59 / 307) |
| OPENS A LANE | 0.1 | 0.2 | 0.1 (+0 / 12 / 1) / 0.1 (+0 / 3 / 0) | 0.1 (+1 / 5 / 0) / 0.3 (+1 / 16 / 2) |
| OPENS UP | 0.2 | 0.2 | 0.2 (+14 / 7 / 5) / 0.2 (+15 / 8 / 6) | 0.2 (+26 / 12 / 5) / 0.2 (+17 / 13 / 5) |
| OVERRUN THREAT | 0.0 (+1 / 0 / 3) | 0.0 | 0.0 (+1 / 0 / 3) / - | 0.0 (+1 / 0 / 0) / 0.0 (+2 / 0 / 2) |
| OVERRUNS AWAY | 0.5 | 0.7 | 0.5 (+10 / 40 / 22) / 0.5 (+11 / 45 / 14) | 0.7 (+11 / 60 / 31) / 0.7 (+20 / 82 / 14) |
| PATHS CROSS | 3.2 | 2.6 | 2.7 (+179 / 0 / 31) / 3.8 (+269 / 0 / 56) | 3.1 (+204 / 0 / 40) / 2.1 (+133 / 0 / 33) |
| PERIAPT WORTH | 0.0 | 0.0 | 0.0 (+2 / 0 / 8) / 0.0 (+3 / 0 / 0) | 0.0 (+3 / 0 / 0) / 0.0 (+2 / 0 / 4) |
| PIVOT GUARDS FLANK | 0.1 | 0.1 | 0.1 (-2 / 0 / 2) / 0.1 (-3 / 0 / 5) | 0.1 (-3 / 0 / 5) / 0.1 (-3 / 0 / 2) |
| PLAN RESULT | 40.1 | 40.2 | 38.9 (+1219 / 1563 / 1090) / 41.3 (+993 / 1406 / 1097) | 41.3 (+1283 / 1496 / 1034) / 39.2 (+1599 / 1533 / 945) |
| PURSUES BIG PREY | 0.1 | 0.1 | 0.1 (-12 / 0 / 2) / 0.1 (-4 / 0 / 0) | 0.1 (-15 / 0 / 0) / 0.1 (-5 / 0 / 1) |
| RAIDS THE BAGGAGE | 0.0 (+3 / 0 / 0) | - | 0.0 (+3 / 0 / 0) / - | - / - |
| RAIDS THE BAGGAGE NEXT TURN | 0.0 | 0.0 | 0.0 (+3 / 0 / 1) / 0.0 (+4 / 0 / 0) | 0.0 (+3 / 0 / 1) / 0.0 (+1 / 0 / 0) |
| RANDOM MOVE BY FIGURES | 1.2 | - | 0.7 (+8 / 0 / 19) / 1.8 (+24 / 0 / 46) | - / - |
| RANDOM MOVER NO PROMISE | 0.3 | - | 0.2 (-12 / 5 / 7) / 0.4 (-23 / 29 / 9) | - / - |
| REDIRECT BY WHAT IT STOPS | 0.2 | - | 0.1 (-3 / 0 / 2) / 0.4 (-2 / 0 / 3) | - / - |
| REDIRECT COUNTER | 3.0 | 3.6 | 2.3 (+174 / 0 / 41) / 3.8 (+332 / 0 / 64) | 3.9 (+232 / 0 / 71) / 3.3 (+185 / 0 / 45) |
| REDIRECT WEIGHED | 0.3 | 0.5 | 0.2 (+6 / 6 / 8) / 0.5 (+15 / 16 / 18) | 0.5 (+14 / 15 / 4) / 0.4 (+10 / 11 / 5) |
| RESERVE FALL BACK | 0.5 | - | 0.4 (+9 / 0 / 7) / 0.6 (+11 / 0 / 16) | - / - |
| RESTRAINS TO SHOOT | 0.1 | 0.1 | 0.1 (+4 / 0 / 5) / 0.1 (+3 / 0 / 2) | 0.1 (+2 / 0 / 4) / 0.1 (+10 / 0 / 2) |
| RISK BY ARC | 2.2 | 2.9 | 1.9 (+77 / 160 / 62) / 2.5 (+52 / 212 / 75) | 3.1 (+68 / 305 / 91) / 2.7 (+89 / 253 / 70) |
| SAFER THAN THE JOB | 0.9 | 0.9 | 1.0 (+59 / 0 / 35) / 0.9 (+58 / 0 / 21) | 0.9 (+58 / 0 / 35) / 0.9 (+53 / 0 / 30) |
| SCREEN BY WHAT IT SAVES | 0.2 | - | 0.1 (-4 / 0 / 0) / 0.2 (-11 / 0 / 1) | - / - |
| SEARCH SPOT | 3.8 | 1.8 | 3.5 (+166 / 0 / 71) / 4.1 (+190 / 0 / 57) | 1.9 (+102 / 0 / 23) / 1.7 (+98 / 0 / 23) |
| SECOND HUNTER | 0.0 | 0.1 | 0.0 (-0 / 1 / 1) / 0.0 (-1 / 3 / 1) | 0.0 (-0 / 3 / 0) / 0.1 (-1 / 13 / 1) |
| SELF MOVE SPELL | 0.2 | 0.2 | 0.3 (+26 / 0 / 18) / 0.2 (+30 / 0 / 17) | 0.2 (+26 / 0 / 16) / 0.3 (+32 / 0 / 7) |
| SET UP TOGETHER | 1.4 | 1.2 | 0.8 (+53 / 32 / 17) / 2.0 (+154 / 70 / 32) | 1.6 (+91 / 31 / 13) / 0.8 (+42 / 21 / 22) |
| SET-UP ANY TARGET | 0.2 | 0.2 | 0.3 (+56 / 17 / 17) / 0.2 (+34 / 4 / 13) | 0.1 (+17 / 10 / 14) / 0.4 (+65 / 15 / 22) |
| SET-UP MISSED | 0.1 | 0.1 | 0.1 (+9 / 2 / 2) / 0.1 (+17 / 0 / 3) | 0.1 (+13 / 1 / 2) / 0.1 (+19 / 4 / 4) |
| SHOOTER COUNTED ONCE | 0.0 | - | 0.0 (-0 / 0 / 0) / 0.0 (-0 / 0 / 0) | - / - |
| SHOOTS FROM THE BEST SPOT | 0.6 | - | 0.7 (+24 / 40 / 10) / 0.6 (+12 / 23 / 10) | - / - |
| SHOT REPLANNED | 0.3 | 0.2 | 0.5 (+0 / 95 / 10) / 0.1 (+0 / 19 / 1) | 0.1 (+0 / 19 / 0) / 0.4 (+0 / 79 / 2) |
| SHOTS IN THE MOVE | 10.7 | 10.8 | 13.0 (+514 / 0 / 251) / 8.3 (+199 / 0 / 136) | 8.3 (+230 / 0 / 131) / 13.3 (+569 / 0 / 213) |
| SPELL CATCH ODDS | 0.1 | 0.0 | 0.1 (-2 / 4 / 5) / 0.0 (-0 / 0 / 0) | 0.0 (-0 / 0 / 0) / 0.0 (-0 / 0 / 0) |
| SPELL SETS UP CHARGE | 0.3 | 0.3 | 0.4 (+77 / 30 / 25) / 0.3 (+79 / 8 / 16) | 0.2 (+43 / 10 / 19) / 0.5 (+89 / 17 / 25) |
| SPELL WORTH | 1.5 | 1.5 | 1.1 (+21 / 83 / 90) / 1.8 (+35 / 106 / 105) | 1.9 (+37 / 89 / 89) / 1.1 (+21 / 75 / 74) |
| STABLE ROLE | 12.2 | - | 13.0 (+0 / 452 / 220) / 11.4 (+0 / 374 / 194) | - / - |
| STANDS TO CAST | 0.0 | 0.1 | 0.0 (+0 / 0 / 0) / 0.0 (+1 / 0 / 4) | 0.1 (+1 / 1 / 6) / 0.0 (+1 / 0 / 0) |
| STOPS | 0.1 | 0.1 | 0.1 (+2 / 8 / 1) / 0.1 (+9 / 9 / 4) | 0.1 (+7 / 11 / 3) / 0.0 (+3 / 8 / 2) |
| STOPS SHORT OF THE FLANK | 0.6 | 0.5 | 0.6 (+20 / 0 / 18) / 0.6 (+28 / 0 / 24) | 0.4 (+12 / 0 / 13) / 0.5 (+21 / 0 / 16) |
| STUCK PIVOT | 0.2 | 0.2 | 0.1 (+0 / 0 / 0) / 0.2 (+0 / 0 / 1) | 0.3 (+0 / 0 / 3) / 0.1 (+0 / 0 / 4) |
| SUPPORT JOB KEPT | 0.0 (+0 / 2 / 0) | 0.0 (+0 / 1 / 0) | 0.0 (+0 / 2 / 0) / - | 0.0 (+0 / 1 / 0) / - |
| SUPPORTS | 7.8 | - | 7.1 (+289 / 264 / 133) / 8.5 (+311 / 279 / 122) | - / - |
| SURE CHARGE BEATS ADVANCE | 0.2 | 0.1 | 0.1 (-13 / 16 / 5) / 0.2 (-16 / 14 / 0) | 0.1 (-6 / 10 / 6) / 0.1 (-6 / 11 / 5) |
| SURE REACH TOGETHER | 0.6 | 0.6 | 0.4 (+1 / 4 / 5) / 0.7 (+0 / 18 / 15) | 0.8 (+3 / 8 / 8) / 0.4 (+4 / 6 / 11) |
| THROUGH LINE OF FIRE | 0.2 | 0.3 | 0.3 (+10 / 0 / 5) / 0.2 (+13 / 0 / 7) | 0.2 (+12 / 0 / 2) / 0.4 (+14 / 0 / 5) |
| TURN WORTH | 0.3 | 0.5 | 0.4 (-24 / 28 / 8) / 0.2 (-13 / 14 / 10) | 0.4 (-27 / 30 / 9) / 0.6 (-39 / 51 / 10) |
| TWO OR MORE ARRIVE | 0.4 | 0.4 | 0.3 (+4 / 7 / 5) / 0.6 (+3 / 27 / 7) | 0.5 (+4 / 10 / 4) / 0.3 (+3 / 13 / 2) |
| WALKS TO THE FIGHT | 1.8 | - | 2.3 (+110 / 44 / 36) / 1.4 (+65 / 35 / 29) | - / - |
| WAR ENGINE JOBS | 0.7 | - | 0.9 (+0 / 54 / 17) / 0.4 (+0 / 7 / 11) | - / - |
| WEARS DOWN | 1.0 | 1.1 | 0.8 (+26 / 97 / 23) / 1.2 (+39 / 122 / 45) | 1.3 (+47 / 142 / 42) / 0.9 (+36 / 107 / 22) |
| WHO HITS BACK | 0.3 | 0.2 | 0.4 (+27 / 0 / 11) / 0.2 (+10 / 0 / 5) | 0.2 (+14 / 0 / 7) / 0.2 (+18 / 0 / 5) |
| WHOLE FIGHT | 0.2 | 0.4 | 0.2 (+6 / 37 / 2) / 0.3 (+13 / 57 / 4) | 0.5 (+21 / 57 / 5) / 0.3 (+11 / 54 / 0) |
| WHOLE FIGHT GAIN | 0.3 | 0.5 | 0.2 (+16 / 19 / 3) / 0.5 (+59 / 42 / 11) | 0.7 (+60 / 55 / 13) / 0.3 (+19 / 19 / 6) |
| WOUNDED STAYS OUT | 0.0 | - | 0.0 (+0 / 0 / 0) / 0.0 (+0 / 1 / 0) | - / - |


## 3. Jobs per side: how many, how often, claimed against what happened

Read by scripts/job_claims.py from all 287 game logs (claimed = the VP the pick's line said; happened = what followed).

287 games read.

Different jobs a side used in a game: framework 5.1, no framework 6.4.

Different jobs used over the batch: framework 9 (advance, charge, close-in, hold, join, lure, redirect, screen, shoot); no framework 9 (advance, charge, close-in, hold, join, lure, redirect, screen, shoot).

| Job | Side | Picks a game | Share of picks | Claimed (mean VP) | Claimed VP a game | Happened |
| --- | --- | --- | --- | --- | --- | --- |
| Charge | framework | 3.8 | 8% | 122.5 | 446 | net 50 VP in 2 turns; declared 80% |
| Charge | no framework | 4.8 | 10% | 107.6 | 486 | net 63 VP in 2 turns; declared 77% |
| Shoot | framework | 5.8 | 13% | 22.1 | 105 | 3.8 VP of wounds that turn |
| Shoot | no framework | 6.8 | 15% | 16.6 | 93 | 4.6 VP of wounds that turn |
| Hold a marker, the hill, a feature | framework | 4.4 | 10% | 77.6 | 323 | 21.9 VP scored this turn and the enemy's next |
| Hold a marker, the hill, a feature | no framework | 4.6 | 10% | 78.4 | 338 | 26.0 VP scored this turn and the enemy's next |
| Close in to charge next turn | framework | 6.1 | 13% | 117.4 | 706 | charged that target next turn 11% |
| Close in to charge next turn | no framework | 5.2 | 11% | 59.4 | 301 | charged that target next turn 10% |
| Advance on an enemy | framework | 23.8 | 52% | 47.1 | 870 | charged that target next turn 3% |
| Advance on an enemy | no framework | 17.1 | 37% | 31.6 | 342 | charged that target next turn 5% |
| Screen | framework | 0.1 | 0% | 2.6 | 0 | guarded unit lost 0.06 wounds (line said 2.36 a turn) |
| Screen | no framework | 2.7 | 6% | 37.8 | 91 | guarded unit lost 0.34 wounds (line said 4.80 a turn) |
| Redirect | framework | 0.3 | 1% | 24.5 | 2 | enemy charged the guarded friend 7%, the chaff 7% |
| Redirect | no framework | 2.5 | 5% | 21.0 | 32 | enemy charged the guarded friend 2%, the chaff 3% |
| Lure | framework | 0.0 | 0% | 23.9 | 1 | enemy charged the guarded friend 11%, the chaff 11% |
| Lure | no framework | 0.9 | 2% | 114.7 | 92 | enemy charged the guarded friend 19%, the chaff 2% |
| Join a unit | framework | 1.5 | 3% | 51.7 | 62 | - |
| Join a unit | no framework | 1.6 | 4% | 45.0 | 59 | - |


What it says:
- **The framework side uses fewer kinds of job a game: 5.1 against 6.4.** Over the batch both sides used the same 9 kinds; the framework
  almost never picks screen (0.1 a game against 2.7), redirect (0.3 against 2.5) or lure (0.0 against 0.9). That follows the rulings (one-turn
  jobs only when the spot is in reach) and the screen figure now claims what it saves (2.6 VP a pick against 37.8 before).
- **The framework moves those picks to "advance on an enemy"**: 23.8 picks a game (52% of all picks) against 17.1, claiming 47 VP a pick
  against 32, yet only 3% of them charge that target next turn (5% without the framework).
- **"Close in to charge next turn" claims twice as much (117 VP against 59)** for the same result (11% charged that target next turn,
  against 10%). The best-spot figure overstates next turn's charge.
- Charge picks: fewer (3.8 against 4.8), declared about as often (80% against 77%), and the two-turn net is lower (50 VP against 63).
- Shooting picks: 3.8 VP of wounds that turn against 4.6.
- The framework's own rule rows (section 2, Opponent rules): STABLE ROLE 12.2 a game, SUPPORTS 7.8, MOVE TO CHARGE 6.8, SEARCH SPOT 3.8
  (1.8 without), INVITES THE FIGHT 3.5, BEST FIRST 3.4, LOST CHARGE 2.5, WALKS TO THE FIGHT 1.8, RANDOM MOVE BY FIGURES 1.2. In return,
  BEST PREY fires 0.8 a game against 5.2 and KILLS COUNT NEXT TURN 6.8 against 10.7: the framework replaces the hunting rules that produced charges.

## 4. Defensive and offensive armies; VP by source

Only the framework side has a stance (the off side always plays offensive). The framework side played defensive in 38% of its turns
(55% in the fwmine half, 21% in the fwopp half: the Mine lists of these pairs shoot more).

### Framework side, per turn by its stance that turn

| Stance | Turns | VP won by shooting + magic a turn | VP won in fights a turn | VP lost to shooting + magic a turn | VP lost in fights a turn | Net kills a turn |
| --- | --- | --- | --- | --- | --- | --- |
| defensive | 521 | 48 | 97 | 14 | 111 | +20 |
| offensive | 874 | 18 | 106 | 41 | 108 | -25 |

### By army type (an army is defensive when it played defensive in half or more of its turns with the framework; the same label is used for it when it played without)

| Framework army | Other army | Games | Framework VP margin a game | Framework VP ahead / level / behind | Framework VP by shooting + magic | Framework VP in fights | Framework VP from objectives | Other VP by shooting + magic | Other VP in fights | Other VP from objectives |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| defensive | defensive | 10 | +130 (±739) | 6 / 0 / 4 | 132 | 455 | 632 | 246 | 422 | 465 |
| defensive | offensive | 102 | +92 (±239) | 52 / 0 / 50 | 284 | 519 | 555 | 68 | 630 | 542 |
| defensive | all | 113 | +102 (±225) | 59 / 0 / 54 | 268 | 517 | 563 | 83 | 610 | 534 |
| offensive | defensive | 102 | -196 (±234) | 44 / 0 / 58 | 60 | 603 | 526 | 252 | 588 | 561 |
| offensive | offensive | 66 | -202 (±274) | 26 / 0 / 40 | 137 | 491 | 554 | 204 | 574 | 588 |
| offensive | all | 168 | -198 (±178) | 70 / 0 / 98 | 90 | 559 | 537 | 233 | 582 | 572 |
| all | defensive | 112 | -167 (±223) | 50 / 0 / 62 | 66 | 590 | 536 | 251 | 573 | 552 |
| all | offensive | 168 | -23 (±182) | 78 / 0 / 90 | 226 | 508 | 555 | 121 | 608 | 560 |
| all | all | 281 | -77 (±140) | 129 / 0 / 152 | 162 | 542 | 547 | 173 | 593 | 557 |


Reading it:
- **Per turn, Morten's expectation holds for shooting.** In its defensive turns the framework side won 48 VP a turn by shooting and magic
  (18 in offensive turns) and lost only 14 to enemy shooting. In fights it won 97 a turn defensive and 106 offensive.
- **Per army, the framework helps defensive armies a little and hurts offensive armies.** With a defensive army the framework side is
  +102 ± 225 a game; with an offensive army it is **-198 ± 178, outside noise**.
- **Offensive armies with the framework earn less in fights**: 559 VP a game against 608 for offensive armies without it. So "more VP from
  charge and combat when offensive" is **not met**; it goes the other way.
- Defensive armies earn about the same by shooting with or without it (268 against 251 a game, row "defensive / all" against "all / defensive").
- **Against which**: the framework does worst against defensive armies (-167 a game, row "all / defensive") and close to level against
  offensive ones (-23).

Framework VP margin by army (small numbers per army, read as a pointer only):

| Army | Games with the framework | Its VP margin with the framework | Games against the framework | Framework side's margin against it |
| --- | --- | --- | --- | --- |
| Lizardmen | 7 | +852 | 6 | -733 |
| Tomb Kings of Khemri | 21 | +666 | 21 | -833 |
| Grand Cathay | 23 | +438 | 23 | -664 |
| Warriors of Chaos | 35 | +414 | 36 | -115 |
| Chaos Dwarfs | 15 | +123 | 15 | -398 |
| High Elf Realms | 26 | +107 | 26 | -109 |
| Wood Elf Realms | 22 | -41 | 22 | +181 |
| Kingdom of Bretonnia | 7 | -86 | 7 | -925 |
| Orc & Goblin Tribes | 9 | -241 | 9 | +947 |
| Ogre Kingdoms | 10 | -410 | 10 | +395 |
| Empire of Man | 25 | -501 | 25 | +196 |
| Vampire Counts | 32 | -502 | 32 | -67 |
| Dwarfen Mountain Holds | 17 | -650 | 17 | +156 |
| Beastmen Brayherds | 18 | -671 | 18 | +127 |
| Skaven | 14 | -811 | 14 | +764 |


## 5. Random moves, charges and contacts

| | Framework | No framework |
| --- | --- | --- |
| Random moves turned off the straight line at the nearest enemy (risk weighed) | 52% | - (rule off) |
| Charges declared a game | 4.7 | 5.8 |
| Charge contacts made a game | 3.3 | 4.1 |
| Charge contacts received a game | 4.1 | 3.3 |
| Games where this side made the first charge contact | 40% | 60% |
| Round of the first charge contact | 2.9 | 2.5 |
| Sides that never made charge contact | 14% | 8% |
| Fights charged into a game | 2.9 | 3.5 |
| Net points per charged fight, damage counted | +84 | +81 |
| First round won (charged fights) | 68% | 66% |
| Net points per supported fight | +132 | +108 |
| Long shots (under 50%) / sweet spot (55-75%) charges over the batch | 72 / 92 | 106 / 140 |

The framework's charges are as good or better one by one (+84 net a fight, 68% first round won, supported fights +132 against +108),
but it makes 19% fewer of them, gets the first contact in only 40% of games, and is charged more often. The on/off batch showed the
same (4.6 against 5.2 declared); here the gap is larger because the other side keeps its charge rules.

## 6. Sim bugs and stalls

- **Game never starts, 3 pairs in both halves (6 games)**: L2033 (scenario 5), L2433 (3), L3033 (3). Opponent Wood Elves: "SETUP: Opponent
  Orion, the King in the Woods (General) is not deployed after Quick Test Game", then a time-out on the Play Turn page. It happens both
  with the framework on Mine and on Opponent, and again when re-run (fwmine-3 pairs, re-run in my container). The same games played
  fine in the on/off batch. The switch builder is on it.
- **L1731 in fwopp-3**: fails twice in the post-game lessons step with "A second operation was started on this context instance" (log
  fwopp-3/L1731-1.log). The game itself is not saved.
- **L0819 in fwmine-4**: SETUP (checked late, turn 6) POSITION finding for Opponent Goblin Wolf Riders 2 joined by an Orc Bigboss.
- No stalls in the 281 games that started. No Haiku calls (cost $0.00).

## 7. What this means

The job framework, as built, does not beat the same computer without it: -81 VP a game (± 100), and **-198 a game with offensive armies**
and **-265 when going second**, both outside noise. Its fights are good, but it charges less, waits, and gives the enemy the first charge.
The likely causes, from the numbers: "advance" and "close in" picks claim far more than happens (claims 47 and 117 VP; 3% and 11% followed by
a charge) and replace BEST PREY / KILLS COUNT NEXT TURN, which produced the charges. Whether to push, tune (e.g. weigh the best-spot
figure by what happened, keep the hunting rules for offensive armies) or park is Morten's call.

Files: the 8 parts in this folder; merged tables in compare-all.md (raw A = framework on Mine, B = framework on Opponent).
Replays on branch claude/project-thread-jdurue (deploy/sim-replays/fw-h2h-*-e441028-p1..4, added to on-site.txt).
