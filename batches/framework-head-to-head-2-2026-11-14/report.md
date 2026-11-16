# Job framework head-to-head 2: framework with the five charge fixes v the old brain (2026-11-14)

Build `1eea44e9` (branch claude/project-thread-281ndx: the framework, the one-side switch, the deployment/Orion fix c6fc19ce and the five
charge fixes Morten said "make sense" to on 11-13). Script opponent v script opponent (Medium v Medium), the same 144 Danish Team
Championship pairs, seed 1 and scenarios as batch 1. Every pair played twice: framework on Mine (fwmine) and framework on Opponent
(fwopp), the other side with the framework and all five fixes switched off (= the old brain). No Haiku, cost $0.

**Games: 288 played, 287 ended, 143 matched pairs (286 games) compared.** Left out: L1731 (fwopp half stalled, section 6) and its fwmine game.
Unlike batch 1, every army deployed with its normal deployment plan, and the three Orion pairs (L2033, L2433, L3033) played normally.

## 1. Headline: from -81 to +59 VP a game. Better, but still inside the noise band

| | Games | Framework VP margin a game | Noise band (95%) | Framework won / drew / lost | **Batch 1** margin | Batch 1 won / drew / lost |
| --- | --- | --- | --- | --- | --- | --- |
| **All matched games** | 286 | **+59** | ±108 (paired) | 130 / 43 / 113 | **-81 ±100** | 97 / 61 / 122 |
| Framework on Mine | 143 | -36 | ±213 | 63 / 21 / 59 | -122 | 45 / 31 / 64 |
| Framework on Opponent | 143 | +155 | ±226 | 67 / 22 / 54 | -40 | 52 / 30 / 58 |
| Framework side went first | 146 | +88 | ±217 | 68 / 23 / 55 | +104 | 57 / 28 / 55 |
| Framework side went second | 140 | +30 | ±223 | 62 / 20 / 58 | **-265** | 40 / 33 / 67 |

- Margin = framework side's VP minus the old brain's VP, a game. The band comes from the 143 pairs with each pair's two games summed, so
  army, side and first-turn effects cancel. Pairs ahead / behind: 71 / 72.
- **The swing from batch 1 is +140 VP a game** (-81 to +59). That is about at the edge of what two batches of this size can tell apart
  (about ±147), and batch 1 also had the deployment fault, so part of the swing may come from that fix and not from the five charge fixes.
- **Going second is no longer a loss** (+30 against -265). The framework side won 130 and lost 113 games (batch 1: 97 won, 122 lost).
- Batch 1 caveat stays: its -81 was measured with both sides deploying without their plan.

VP by kind, a game:

| | Framework | Old brain | Batch 1 framework | Batch 1 old brain |
| --- | --- | --- | --- | --- |
| VP from kills | **841** | 790 | 732 | 796 |
| VP from objectives | 554 | 554 | 547 | 557 |
| VP from the General (leaders) | 68 | 61 | 56 | 60 |
| Units lost | 4.9 | 5.5 | 5.1 | 4.8 |
| Points lost | **751** | 799 | 752 | 690 |

The framework now kills about 51 VP a game more than the old brain and loses about 48 points a game less (batch 1: 64 less and 62 more).

## 2. Charges: the fixes did what they were meant to

| | Framework | Old brain | Batch 1 framework | Batch 1 old brain |
| --- | --- | --- | --- | --- |
| Charges declared a game | **5.6** | 4.9 | 4.7 | 5.8 |
| Charge contacts made a game | **4.0** | 3.5 | 3.3 | 4.1 |
| Charge contacts received a game | 3.5 | 4.0 | 4.1 | 3.3 |
| Games where this side made the first charge contact | **53%** | 47% | 40% | 60% |
| Round of the first charge contact | 2.5 | 2.7 | 2.9 | 2.5 |
| Sides that never made charge contact | 7% | 10% | 14% | 8% |
| Fights charged into a game | 3.5 | 3.1 | 2.9 | 3.5 |
| Net points per charged fight, damage counted | +85 | +90 | +84 | +81 |
| First round won (charged fights) | 62% | 62% | 68% | 66% |
| Net points per supported fight | +160 | +132 | +132 | +108 |
| Joint charges a game (2+ units, one target, one turn) | 0.5 | 0.4 | - | - |
| Charges by odds over the batch: long shot / sweet spot / overkill / 90%+ not overkill | 135 / 132 / 107 / 310 | 113 / 118 / 90 / 268 | | |

The framework now charges 14% more than the old brain (batch 1: 19% less), gets the first contact in 53% of games (40%) and is charged
less often. Its fights are as good one by one as the old brain's. It takes a few more long shots (135 against 113).

## 3. Jobs: claimed against what happened

Read by scripts/job_claims.py from all 288 game logs.

| Job | Side | Picks a game | Claimed (mean VP) | Happened | Batch 1 picks / claim / happened |
| --- | --- | --- | --- | --- | --- |
| Charge | framework | **5.2** | 122 | net 55 VP in 2 turns; declared 75% | 3.8 / 123 / net 50, 80% |
| Charge | old brain | 4.2 | 116 | net 56 VP in 2 turns; declared 76% | 4.8 / 108 / net 63, 77% |
| Close in to charge next turn | framework | 5.1 | **60** | charged that target next turn 13% | 6.1 / **117** / 11% |
| Close in to charge next turn | old brain | 5.3 | 63 | 11% | 5.2 / 59 / 10% |
| Advance on an enemy | framework | 19.6 | **25** | charged that target next turn 4% | 23.8 / **47** / 3% |
| Advance on an enemy | old brain | 14.7 | 35 | 6% | 17.1 / 32 / 5% |
| Shoot | framework | 7.7 | 18 | 5.0 VP of wounds that turn | 5.8 / 22 / 3.8 |
| Shoot | old brain | 7.0 | 20 | 4.7 | 6.8 / 17 / 4.6 |
| Hold a marker, hill, feature | framework | 5.1 | 73 | 23.4 VP scored this turn and the next | 4.4 / 78 / 21.9 |
| Hold a marker, hill, feature | old brain | 4.5 | 78 | 25.2 | 4.6 / 78 / 26.0 |
| Screen | framework / old brain | 0.2 / 2.9 | 3 / 50 | guarded unit lost 0.05 / 0.30 wounds | 0.1 / 2.7 |
| Redirect | framework / old brain | 0.3 / 2.6 | 1 / 23 | enemy charged the chaff 16% / 4% | 0.3 / 2.5 |
| Lure | framework / old brain | 0.1 / 0.7 | -14 / 114 | | 0.0 / 0.9 |
| Join a unit | framework / old brain | 0.9 / 0.8 | 48 / 42 | | 1.5 / 1.6 |

Different jobs a side used in a game: framework 5.2, old brain 6.4 (batch 1: 5.1 / 6.4).

Framework rule rows (fired a game; batch 1 in brackets), from the Opponent rules table below:

| Rule | Framework, batch 2 | Batch 1 | Note |
| --- | --- | --- | --- |
| CHARGE NOW FIRST (new) | 3.1 | - | charge at 75%+ reach taken before any waiting job |
| WAIT AFTER COSTS (new) | 7.3 | - | waiting jobs valued after costs, at 50/35/35/25% |
| SUPPORT NARROWED (new) | 7.3 | - | |
| WAR ENGINE CHARGES (new) | 0.1 | - | rarely decides: few war engines in these lists |
| DEFENSIVE FLOOR (new) | 0.1 | - | |
| MOVE TO CHARGE | 3.8 | 6.8 | |
| SUPPORTS | 4.5 | 7.8 | |
| INVITES THE FIGHT | 1.5 | 3.5 | |
| WALKS TO THE FIGHT | 1.5 | 1.8 | |
| WAR ENGINE JOBS | 0.4 | 0.7 | |
| GIVES UP | 0.1 | 1.0 | old brain 1.2 |
| BEST PREY | 0.8 | 0.8 | old brain 4.6 (5.2) |
| KILLS COUNT NEXT TURN | 6.2 | 6.8 | old brain 9.5 (10.7) |

- "Close in" now claims what it did before the framework (60 VP, against 117 in batch 1) and is followed by a charge 13% of the time.
- "Advance" claims half of batch 1 (25 against 47). It is still the biggest job (44% of picks) and still rarely followed by a charge (4%).
- Support requests answered (helper made contact too): framework 46%, old brain 50%.

## 4. Defensive and offensive armies; VP by source

With the floor, the framework side played defensive in 18% of its turns (batch 1: 38%; 28% in the fwmine half, 8% in the fwopp half).
The old brain has no stance.

### Framework side, per turn by its stance that turn

| Stance | Turns | VP won by shooting + magic a turn | VP won in fights a turn | VP lost to shooting + magic a turn | VP lost in fights a turn | Net kills a turn | Batch 1 net |
| --- | --- | --- | --- | --- | --- | --- | --- |
| defensive | 252 | 60 | 46 | 15 | 148 | **-58** | +20 |
| offensive | 1174 | 23 | 143 | 33 | 100 | **+33** | -25 |

### By army type (defensive = played defensive in half or more of its framework turns; the same label is used when it plays without)

| Framework army | Other army | Games | Framework VP margin a game | Framework won / lost | Fw VP shooting + magic | Fw VP in fights | Fw VP objectives | Other VP shooting + magic | Other VP fights | Other VP objectives | Batch 1 margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| defensive | offensive | 49 | **-441 (±372)** | 21 / 28 | 372 | 250 | 491 | 79 | 782 | 710 | +92 (±239) |
| offensive | defensive | 49 | **+773 (±307)** | 38 / 11 | 118 | 949 | 746 | 384 | 237 | 452 | -196 (±234) |
| offensive | offensive | 188 | +4 (±190) | 101 / 87 | 143 | 680 | 521 | 134 | 661 | 539 | -202 (±274) |
| offensive | all | 238 | **+166 (±168)** | 140 / 98 | 137 | 738 | 568 | 185 | 573 | 521 | -198 (±178) |
| all | all | 287 | +63 (±155) | 161 / 126 | 177 | 655 | 555 | 167 | 609 | 554 | -77 (±140) |

(Won / lost here = VP ahead / behind; level games are counted as neither.)

Reading it:
- **Offensive armies now gain with the framework**: +166 a game (batch 1: -198, outside noise). They win 738 VP a game in fights against 573.
- **Defensive armies now lose with it: -441 a game, outside noise** (49 games; batch 1 +102). Playing defensive, the framework side
  shoots well (372 VP) but loses 782 VP in fights and 710 in objectives to the old brain, which simply charges it. Per turn, a
  defensive turn nets -58 VP. So the floor makes fewer armies defensive, but the ones still labelled defensive stand and get charged.
- Mirror image: when the OLD brain's army is the defensive kind (it plays it offensively), the framework side wins by +773.
  Together this says: in this matchup, playing an army defensively loses and charging wins.

Framework VP margin by army (small numbers per army; a pointer only):

| Army | Games with the framework | Its VP margin with the framework | Games against the framework | Framework side's margin against it |
| --- | --- | --- | --- | --- |
| Tomb Kings of Khemri | 21 | +1185 | 21 | -630 |
| Kingdom of Bretonnia | 7 | +541 | 7 | -392 |
| Grand Cathay | 23 | +503 | 23 | -408 |
| Lizardmen | 7 | +422 | 6 | -1260 |
| Vampire Counts | 33 | +316 | 33 | -368 |
| High Elf Realms | 26 | +249 | 26 | -288 |
| Chaos Dwarfs | 15 | +171 | 15 | -456 |
| Warriors of Chaos | 36 | +44 | 37 | +195 |
| Wood Elf Realms | 25 | -34 | 25 | +100 |
| Dwarfen Mountain Holds | 17 | -152 | 17 | +848 |
| Beastmen Brayherds | 18 | -179 | 18 | +579 |
| Skaven | 15 | -601 | 15 | +1005 |
| Empire of Man | 25 | -632 | 25 | +570 |
| Ogre Kingdoms | 10 | -721 | 10 | +332 |
| Orc & Goblin Tribes | 9 | -836 | 9 | +1131 |

## 5. Every KPI side by side

Framework = Mine in fwmine games plus Opponent in fwopp games; old brain = the other side. The last two columns show the two halves
(framework on Mine games / framework on Opponent games). Counts "(x of y)" are pooled; other numbers are the mean of the two halves.
Batch 1's version of these tables is in /mnt/project-files/framework-head-to-head-2026-11-13/report.md section 2; the raw two-batch
tables are in compare-all.md beside this report (A = framework on Mine, B = framework on Opponent).

Headline KPI changes against batch 1 (framework / old brain): defensive turns 18% / 0% (38%); points that never fought 35% / 34%
(36% / 37%); infantry points that never fought 50% / 47% (44% / 48%); magic missiles tried each turn 30% / 29% (32% / 32%); follow up or
pursue 90% / 90% (87% / 90%); FACES THE THREAT 1.54 / 1.07 a game (1.58 / 1.38).

## KPIs (Morten 2026-11-10)

| KPI | Target | **Framework** | **Old brain** | fw (Mine games) / fw (Opp games) | off (Mine games) / off (Opp games) |
| --- | --- | --- | --- | --- | --- |
| Turns the army played defensive (its shooting and magic 1.5x the enemy's; else offensive) |  | 18% | 0% | 28% / 8% | 0% / 0% |
| Winner chose to follow up after the loser gave ground |  | 98% | 96% | 96%; on the table 97% / 99%; on the table 99% | 97%; on the table 97% / 96%; on the table 97% |
| Winner chose to pursue after the loser fell back in good order |  | 90% | 92% | 98%; on the table 98% / 83%; on the table 86% | 93%; on the table 93% / 91%; on the table 98% |
| Winner chose to pursue after the loser fled |  | 75% | 76% | 74%; on the table 78% / 76%; on the table 85% | 78%; on the table 81% / 73%; on the table 78% |
| Winner chose to follow up or pursue (all three) |  | 90% | 90% | 90%; on the table 92% / 89%; on the table 93% | 90%; on the table 92% / 90%; on the table 93% |
| Magic missiles tried each own turn | 50%+ | 30% | 29% | 30% / 30% | 29% / 29% |
| tried when they could be (not in combat, slain, fleeing or off the table) | 50%+ | 44% | 44% | 45% / 42% | 42% / 45% |
| Random moves turned off the straight line at the nearest enemy (risk weighed) |  | 57% | - | 59% / 55% | - / - |
| Points that never fought | lower | 35% | 34% | 35% / 35% | 36% / 32% |
| infantry points that never fought | lower | 50% | 47% | 46% / 54% | 57% / 37% |
| Units over 100 pts that earned no points (no kill, no objective) | lower | 56% | 58% | 55% / 58% | 58% / 57% |
| Bound items with a magic missile used (at least once a game) |  | 86% | 82% | 94% / 79% | 76% / 88% |
| Bound items with another spell used |  | 50% | 47% | 58% / 42% | 33% / 61% |
| One-use items used (Chalice of Dark Rain, Arch-Lightning Rod ...) |  | 53% | 56% | 56% / 50% | 56% / 56% |
| their share of the points of units over 100 pts | lower | 50% | 52% | 49% / 51% | 51% / 52% |

## KPIs (Morten 2026-11-10)

| Measure | **Framework** | **Old brain** | fw (Mine games) / fw (Opp games) | off (Mine games) / off (Opp games) |
| --- | --- | --- | --- | --- |
| Charged units hit only in a flank or rear (% of formed units charged) | 49% | 47% | 53% (167) / 45% (130) | 48% (149) / 46% (175) |
| ...free all their last turn and able to turn (per game) | 0.59 | 0.63 | 0.65 / 0.53 | 0.58 / 0.68 |
| ...left out: fought, charged, random mover or war machine in their own turn (per game) | 0.21 | 0.23 | 0.22 / 0.19 | 0.24 / 0.22 |
| ...with the charger already in that arc before they moved (per game) | 0.36 | 0.44 | 0.39 / 0.33 | 0.38 / 0.50 |
| Turned to face a threat or took a way out: FACES THE THREAT (per game) | 1.54 | 1.07 | 1.82 / 1.26 | 0.92 / 1.22 |
| Stood instead of an exposed job's move: SAFER THAN THE JOB (per game) | 0.90 | 0.71 | 1.12 / 0.68 | 0.74 / 0.69 |
| Kept its job with an enemy able to reach its flank or rear: NOT TURNED (per game) | 5.80 | 6.36 | 5.72 / 5.89 | 6.41 / 6.31 |

### Charges a game and per unit by the wizard it carries

| Charges | **Framework** | **Old brain** | fw (Mine games) / fw (Opp games) | off (Mine games) / off (Opp games) |
| --- | --- | --- | --- | --- |
| Charges declared a game | 5.6 | 4.9 | 4.6 / 6.6 | 5.5 / 4.3 |
| Charges that made contact a game | 4.0 | 3.5 | 3.4 / 4.6 | 3.8 / 3.2 |
| per unit a game, units carrying a magic-missile wizard (or one alone) | 0.76 declared, 0.56 contact | 0.84 declared, 0.63 contact | 0.92 declared, 0.70 contact (88 units) / 0.60 declared, 0.42 contact (60 units) | 0.79 declared, 0.54 contact (61 units) / 0.89 declared, 0.72 contact (87 units) |
| per unit a game, units carrying another wizard (or one alone) | 1.08 declared, 0.81 contact | 1.11 declared, 0.76 contact | 0.76 declared, 0.68 contact (25 units) / 1.41 declared, 0.95 contact (44 units) | 1.18 declared, 0.79 contact (38 units) / 1.04 declared, 0.72 contact (25 units) |
| per unit a game, the other units (no war machines, no joined characters) | 0.67 declared, 0.47 contact | 0.57 declared, 0.41 contact | 0.59 declared, 0.42 contact (971 units) / 0.75 declared, 0.53 contact (1138 units) | 0.61 declared, 0.43 contact (1138 units) / 0.53 declared, 0.39 contact (977 units) |

## Movement (Morten 2026-11-11)

| Measure | **Framework** | **Old brain** | fw (Mine games) / fw (Opp games) | off (Mine games) / off (Opp games) |
| --- | --- | --- | --- | --- |
| Games where this side made the first charge contact | 53% (152 of 287) | 47% (135 of 287) | 48% (69 of 143) / 58% (83 of 144) | 52% (74 of 143) / 42% (61 of 144) |
| Round of a side's first charge contact (sides that made one) | 2.5 | 2.7 | 2.6 / 2.4 | 2.6 / 2.7 |
| Sides that never declared a charge | 4% (11 of 288) | 7% (19 of 288) | 8% (11 of 144) / 0% (0 of 144) | 2% (3 of 144) / 11% (16 of 144) |
| Sides that never made charge contact | 7% (20 of 288) | 10% (28 of 288) | 12% (18 of 144) / 1% (2 of 144) | 5% (7 of 144) / 15% (21 of 144) |
| Charges declared a game | 5.6 | 4.9 | 4.7 / 6.5 | 5.4 / 4.4 |
| Charge contacts made a game | 4.0 | 3.5 | 3.5 / 4.6 | 3.7 / 3.3 |
| Charge contacts received a game | 3.5 | 4.0 | 3.7 / 3.3 | 3.5 / 4.6 |
| Joint charges a game (2+ units on one target in one turn) | 0.5 | 0.4 | 0.4 / 0.5 | 0.4 / 0.4 |
| share of charged targets hit by 2+ units | 13% (135 of 1007) | 12% (108 of 880) | 13% (58 of 437) / 14% (77 of 570) | 11% (53 of 470) / 13% (55 of 410) |
| Lone charges that a friend follows on the same target next turn | 6% (55 of 872) | 6% (46 of 772) | 7% (26 of 379) / 6% (29 of 493) | 6% (23 of 417) / 6% (23 of 355) |
| Set-ups (close in to charge next turn) that charged that target next turn | 16% (233 of 1473) | 14% (213 of 1518) | 16% (98 of 620) / 16% (135 of 853) | 15% (132 of 857) / 12% (81 of 661) |
| ... and made contact | 11% (165 of 1473) | 10% (157 of 1518) | 12% (72 of 620) / 11% (93 of 853) | 11% (96 of 857) / 9% (61 of 661) |
| ... with a friend on it too | 3% (43 of 1473) | 3% (39 of 1518) | 3% (16 of 620) / 3% (27 of 853) | 2% (21 of 857) / 3% (18 of 661) |
| Set-ups missed (no charge on that target next turn) | 84% (1240 of 1473) | 86% (1305 of 1518) | 84% (522 of 620) / 84% (718 of 853) | 85% (725 of 857) / 88% (580 of 661) |
| Charge contacts in the flank or rear (arc known) | 47% (550 of 1158) | 49% (491 of 1006) | 49% (247 of 501) / 46% (303 of 657) | 52% (279 of 535) / 45% (212 of 471) |
| in the rear | 9% (107 of 1158) | 9% (92 of 1006) | 9% (46 of 501) / 9% (61 of 657) | 10% (51 of 535) / 9% (41 of 471) |
| Declared charges in the flank or rear (arc known) | 46% (749 of 1618) | 50% (704 of 1405) | 48% (324 of 682) / 45% (425 of 936) | 51% (398 of 774) / 48% (306 of 631) |
| Marches that gave up a magic missile a game (made: a failed march test or a MARCH CHECK turn left out) | 0.4 | 0.4 | 0.5 / 0.3 | 0.3 / 0.6 |

## Quality by phase (per game and side)

| Phase | Number | **Framework** | **Old brain** | fw (Mine games) / fw (Opp games) | off (Mine games) / off (Opp games) |
| --- | --- | --- | --- | --- | --- |
| Deployment | Characters standing alone | 3.2 | 3.2 | 3.0 / 3.5 | 3.5 / 3.0 |
| Strategy | Charge objectives carried out (made contact) | 48% (715 of 1489) | 48% (576 of 1202) | 51% (321 of 635) / 46% (394 of 854) | 44% (293 of 673) / 53% (283 of 529) |
| Strategy | Shoot objectives carried out (shot that target) | 48% (1063 of 2229) | 51% (1032 of 2009) | 46% (701 of 1522) / 51% (362 of 707) | 55% (375 of 676) / 49% (657 of 1333) |
| Strategy | Close-in objectives charged next turn | 16% (234 of 1473) | 14% (215 of 1518) | 16% (98 of 620) / 16% (136 of 853) | 16% (134 of 857) / 12% (81 of 661) |
| Strategy | Support requests answered (helper made contact too) | 46% (82 of 180) | 50% (85 of 169) | 44% (30 of 68) / 46% (52 of 112) | 40% (40 of 99) / 64% (45 of 70) |
| Strategy | Augments that last this turn, on a unit that fought or charged that turn | 89% (17 of 19) | 88% (15 of 17) | 92% (12 of 13) / 83% (5 of 6) | 83% (5 of 6) / 91% (10 of 11) |
| Strategy | Hexes on a unit its side charged or shot that turn | 51% (44 of 87) | 44% (44 of 100) | 45% (24 of 53) / 59% (20 of 34) | 58% (19 of 33) / 37% (25 of 67) |
| Strategy | Joined characters whose unit fought | 44% (136 of 307) | 52% (141 of 272) | 51% (89 of 176) / 36% (47 of 131) | 45% (57 of 126) / 58% (84 of 146) |
| Strategy | Lone characters that fought | 79% (589 of 746) | 78% (609 of 783) | 79% (293 of 373) / 79% (296 of 373) | 78% (300 of 383) / 77% (309 of 400) |
| Movement | Charges halted short of contact | 0.2 | 0.2 | 0.2 / 0.3 | 0.2 / 0.2 |
| Movement | Idle units | 1.4 | 1.5 | 1.1 / 1.7 | 1.9 / 1.1 |
| Movement | Points that never moved of their own | 236.0 | 242.6 | 305.1 / 166.8 | 157.6 / 327.5 |
| Movement | Fights charged into per game | 3.5 | 3.1 | 3.0 / 4.0 | 3.3 / 2.9 |
| Movement | Charges with odds: long shots (under 50%) | 68 | 56 | 48 of 393, net +92 / 87 of 492, net +40 | 67 of 394, net +64 / 46 of 371, net +64 |
| Movement | Charges with odds: sweet spot (55-75%) | 66 | 59 | 63 of 393, net +26 / 69 of 492, net +113 | 65 of 394, net +94 / 53 of 371, net -11 |
| Movement | Charges with odds: overkill (90%+, target under 250 pts, chargers over 3x) | 54 | 45 | 64 of 393, net +78 / 43 of 492, net +71 | 29 of 394, net +81 / 61 of 371, net +78 |
| Movement | Charges with odds: 90%+ not overkill (target 250+ pts or chargers up to 3x) | 155 | 134 | 138 of 393, net +114 / 172 of 492, net +119 | 143 of 394, net +147 / 125 of 371, net +100 |
| Shooting | Shots by shooting units (incl. breath weapons) | 9.6 | 8.9 | 9.8 / 9.3 | 9.3 / 8.5 |
| Shooting | aimed at a top-3 enemy unit or that turn's charge target | 50% (581 of 1157) | 51% (593 of 1169) | 53% (492 of 932) / 40% (89 of 225) | 39% (89 of 228) / 54% (504 of 941) |
| Shooting | Points destroyed by shooting units | 62.2 | 61.0 | 83.8 / 40.6 | 48.1 / 74.0 |
| Shooting | War machine shots | 4.0 | 4.0 | 6.5 / 1.6 | 1.6 / 6.5 |
| Shooting | Points destroyed by war machines | 51.2 | 52.8 | 84.2 / 18.1 | 24.2 / 81.3 |
| Magic | Magic missiles cast | 1.4 | 1.4 | 1.8 / 1.0 | 1.0 / 1.7 |
| Magic | aimed at a top-3 enemy unit or that turn's charge target | 31% (120 of 390) | 35% (131 of 379) | 30% (77 of 254) / 32% (43 of 136) | 34% (48 of 141) / 35% (83 of 238) |
| Magic | Wounds caused by magic missiles | 2.7 | 2.8 | 4.0 / 1.4 | 1.7 / 3.9 |
| Magic | Wounds caused by other spells | 1.3 | 1.1 | 1.6 / 1.0 | 0.6 / 1.6 |
| Magic | Points destroyed by magic (all spells) | 63.2 | 52.2 | 85.7 / 40.6 | 19.9 / 84.4 |
| Magic | Augments / hexes / assailments / vortexes cast | 1.5 | 1.5 | 1.2 / 0.4 / 0.7 / 0.1 / 1.9 / 0.4 / 0.5 / 0.2 | 1.9 / 0.3 / 0.3 / 0.1 / 1.1 / 0.5 / 0.8 / 0.1 |
| Combat | Points destroyed in combat | 404.4 | 379.4 | 369.7 / 439.1 | 426.3 / 332.4 |
| Combat | Points run down | 109.1 | 101.2 | 80.8 / 137.4 | 102.0 / 100.5 |
| Combat | Net points per charged fight, damage counted | +85 | +90 | +82 / +88 | +105 / +75 |
| Combat | Net per 100 charger points, damage counted | +30.2 | +32.1 | +29.3 / +31.1 | +37.8 / +26.5 |
| Combat | First round won (charged fights) | 62% | 62% | 63% / 61% | 59% / 65% |
| Combat | Net points per charged fight | +86 | +88 | +82 / +89 | +102 / +74 |
| Combat | Net points per supported fight / lone fight | +160 | +132 | +190 / +66 / +131 / +82 | +151 / +96 / +112 / +67 |
| Combat | Charged fights on a top-3 enemy unit | 194 | 182 | 136 of 437 / 251 of 569 | 221 of 470 / 142 of 410 |
| Game | Points lost | 750.7 | 801.1 | 746.1 / 755.2 | 768.5 / 833.7 |
| Game | VP from objectives | 555.0 | 553.5 | 535.6 / 574.5 | 579.9 / 527.1 |
| Game | Lone holders (player turns) | 2.4 | 2.5 | 2.4 / 2.4 | 2.4 / 2.6 |


## Opponent rules (fired a game, figure / won / lost VP a game)

| Rule | **Framework** | **Old brain** | fw (Mine games) / fw (Opp games) | off (Mine games) / off (Opp games) |
| --- | --- | --- | --- | --- |
| ADVANCE LANE KEPT | 0.6 | 0.6 | 0.6 (+0 / 0 / 0) / 0.6 (+0 / 0 / 1) | 0.6 (+0 / 0 / 0) / 0.6 (+0 / 0 / 0) |
| ALREADY CARRIED | 0.1 (+0 / 0 / 0) | 0.0 (+0 / 2 / 0) | 0.1 (+0 / 0 / 0) / - | - / 0.0 (+0 / 2 / 0) |
| ARRIVAL HUNT | 0.0 (+1 / 0 / 0) | 0.0 | - / 0.0 (+1 / 0 / 0) | 0.0 (+0 / 0 / 1) / 0.0 (+0 / 0 / 0) |
| ARTILLERY RE-ROLL WEIGHED | 0.8 | 0.9 | 1.5 (+0 / 0 / 25) / 0.2 (+0 / 0 / 3) | 0.3 (+0 / 0 / 2) / 1.5 (+0 / 0 / 28) |
| BACKUP TARGETS | 1.1 | 1.1 | 1.0 (+9 / 0 / 25) / 1.1 (+12 / 0 / 25) | 1.2 (+14 / 0 / 21) / 1.0 (+7 / 0 / 23) |
| BEST FACING | 0.6 | - | 0.7 (+22 / 0 / 18) / 0.6 (+27 / 0 / 38) | - / - |
| BEST FIRST | 4.0 | - | 4.2 (+183 / 153 / 79) / 3.8 (+168 / 110 / 77) | - / - |
| BEST OVERALL | 0.6 | 0.3 | 0.7 (+40 / 0 / 19) / 0.5 (+36 / 0 / 27) | 0.3 (+22 / 0 / 13) / 0.3 (+14 / 0 / 13) |
| BEST PREY | 0.8 | 4.6 | 0.7 (+31 / 17 / 8) / 0.8 (+36 / 27 / 14) | 4.8 (+353 / 221 / 123) / 4.4 (+285 / 165 / 148) |
| BEST PRIZE | 0.1 | 0.0 | 0.1 (-5 / 6 / 9) / 0.1 (-4 / 7 / 4) | 0.0 (+1 / 6 / 3) / 0.0 (-1 / 1 / 0) |
| BIG CHARACTER SAFETY | 0.2 | 0.2 | 0.1 (-0 / 0 / 12) / 0.2 (+0 / 0 / 17) | 0.2 (-1 / 0 / 13) / 0.1 (-0 / 0 / 6) |
| BLOCKED CHARGE HANDED OVER | 0.0 (+1 / 2 / 0) | - | - / 0.0 (+1 / 2 / 0) | - / - |
| BLOCKED CHARGE SKIPPED | 0.1 | 0.1 | 0.1 (+0 / 2 / 0) / 0.1 (+0 / 6 / 2) | 0.1 (+0 / 6 / 0) / 0.1 (+0 / 11 / 1) |
| BLOCKED WHEEL | 0.5 | 0.5 | 0.4 (+9 / 0 / 4) / 0.5 (+4 / 0 / 5) | 0.5 (+3 / 0 / 4) / 0.4 (+5 / 0 / 6) |
| BOMBING RUN | 0.1 (+2 / 3 / 0) | 0.0 | 0.1 (+2 / 3 / 0) / - | 0.0 (+0 / 1 / 0) / 0.0 (+1 / 1 / 0) |
| BOUND ASSAILMENT | 0.0 (+0 / 0 / 0) | 0.0 | 0.0 (+0 / 0 / 0) / - | 0.0 (+0 / 0 / 1) / 0.0 (+0 / 0 / 3) |
| CANNON PLAN MISSED | 0.5 | 0.4 | 0.8 (+0 / 109 / 12) / 0.2 (+0 / 18 / 2) | 0.2 (+0 / 16 / 4) / 0.7 (+0 / 92 / 9) |
| CANNON PLANNED TARGET | 3.2 | 3.2 | 5.2 (+151 / 368 / 93) / 1.1 (+41 / 60 / 22) | 1.1 (+45 / 62 / 15) / 5.2 (+184 / 388 / 103) |
| CANNON SIGHT KEPT | 0.8 | 0.8 | 1.2 (+0 / 0 / 4) / 0.3 (+0 / 0 / 0) | 0.3 (+0 / 0 / 2) / 1.2 (+0 / 0 / 2) |
| CARRIES OUT COUNTER | 0.1 | 0.0 | 0.1 (+0 / 3 / 8) / 0.0 (-1 / 2 / 0) | 0.0 (+0 / 9 / 0) / 0.0 (-0 / 4 / 1) |
| CARRIES OUT SET-UP | 0.1 | 0.1 | 0.1 (-1 / 10 / 3) / 0.1 (-4 / 26 / 1) | 0.1 (-1 / 12 / 0) / 0.1 (-2 / 5 / 5) |
| CAST JOB | 0.5 | 0.7 | 0.7 (+24 / 48 / 20) / 0.3 (+9 / 26 / 9) | 0.4 (+9 / 22 / 12) / 0.9 (+23 / 55 / 17) |
| CASTER AWAY FROM SCREEN | 0.2 | 0.2 | 0.3 (+0 / 0 / 0) / 0.2 (+0 / 0 / 0) | 0.1 (+0 / 0 / 0) / 0.3 (+0 / 0 / 0) |
| CASTING BLOCK | 0.2 | 0.3 | 0.3 (+32 / 19 / 14) / 0.1 (+3 / 2 / 1) | 0.1 (+6 / 5 / 1) / 0.5 (+49 / 24 / 16) |
| CASTS AFTER FRIENDS | 0.6 | 0.5 | 0.7 (+0 / 0 / 34) / 0.4 (+0 / 0 / 21) | 0.3 (+0 / 0 / 9) / 0.7 (+0 / 0 / 9) |
| CASTS FROM BEHIND | 0.2 | 0.2 | 0.1 (+0 / 0 / 0) / 0.2 (+0 / 0 / 0) | 0.2 (+0 / 0 / 0) / 0.1 (+0 / 0 / 0) |
| CATCH FLIERS | 0.0 | 0.0 | 0.0 (+1 / 0 / 0) / 0.0 (+0 / 0 / 0) | 0.0 (+0 / 0 / 0) / 0.0 (+1 / 0 / 3) |
| CATCH ODDS | 0.0 (+0 / 0 / 0) | 0.0 (+0 / 0 / 1) | 0.0 (+0 / 0 / 0) / - | 0.0 (+0 / 0 / 1) / - |
| CHAFF PASSED | 0.2 | 0.2 | 0.3 (-1 / 10 / 8) / 0.2 (-1 / 7 / 4) | 0.2 (-1 / 2 / 6) / 0.3 (-0 / 1 / 8) |
| CHAMPION TAKES THE CHALLENGE | 0.0 (+0 / 2 / 0) | 0.0 | - / 0.0 (+0 / 2 / 0) | 0.0 (+0 / 2 / 0) / 0.0 (+0 / 1 / 0) |
| CHARGE NOW FIRST | 3.1 | - | 2.9 (+0 / 266 / 86) / 3.4 (+0 / 338 / 99) | - / - |
| CHARGE NOW WEIGHED | 0.5 | 0.6 | 0.5 (-44 / 23 / 30) / 0.4 (-30 / 9 / 12) | 0.6 (-41 / 17 / 24) / 0.6 (-34 / 19 / 20) |
| CHARIOT NO STATIC JOB | 0.0 (+0 / 4 / 1) | 0.3 | 0.0 (+0 / 4 / 1) / - | 0.1 (+0 / 0 / 1) / 0.5 (+0 / 10 / 11) |
| CHARIOT WIZARD CAREFUL | 0.1 | 0.1 | 0.1 (-1 / 3 / 3) / 0.1 (-1 / 7 / 7) | 0.1 (-2 / 3 / 0) / 0.0 (-0 / 2 / 7) |
| CHEAP HELPER | 0.1 | 0.1 | 0.1 (+0 / 7 / 2) / 0.1 (+0 / 16 / 2) | 0.1 (+0 / 7 / 3) / 0.1 (+0 / 2 / 3) |
| COMBAT PIVOT | 0.6 | 0.5 | 0.5 (+0 / 31 / 36) / 0.6 (+0 / 35 / 45) | 0.5 (+0 / 30 / 33) / 0.5 (+0 / 35 / 55) |
| CONTINUE AHEAD WEIGHED | 0.0 | 0.0 (+0 / 0 / 0) | 0.0 (+0 / 0 / 3) / 0.0 (+0 / 0 / 0) | - / 0.0 (+0 / 0 / 0) |
| CONVEYANCE SEARCH | 0.6 | 0.4 | 0.7 (+103 / 17 / 18) / 0.4 (+57 / 12 / 23) | 0.3 (+58 / 4 / 14) / 0.6 (+88 / 20 / 12) |
| COUNTER-CHARGE COVER | 8.5 | 7.7 | 9.6 (+810 / 0 / 218) / 7.4 (+671 / 0 / 178) | 7.2 (+603 / 0 / 128) / 8.2 (+620 / 0 / 244) |
| DEFENSIVE ARMY | 0.2 | - | 0.3 (+0 / 18 / 5) / 0.1 (+0 / 3 / 5) | - / - |
| DEFENSIVE FLOOR | 0.1 | - | 0.1 (+3 / 4 / 2) / 0.0 (+1 / 3 / 1) | - / - |
| EDGE GIVE GROUND | 0.2 | 0.2 | 0.2 (+9 / 18 / 1) / 0.3 (+10 / 39 / 5) | 0.2 (+9 / 32 / 6) / 0.1 (+7 / 15 / 3) |
| ELIXIR WORTH | 0.0 | 0.0 | 0.0 (+0 / 0 / 2) / 0.0 (+0 / 0 / 0) | 0.0 (+1 / 0 / 0) / 0.0 (+0 / 0 / 2) |
| ENGINEER BY LORE | 0.1 (+0 / 0 / 1) | 0.1 (+0 / 0 / 0) | 0.1 (+0 / 0 / 1) / - | - / 0.1 (+0 / 0 / 0) |
| FACES THE THREAT | 1.6 | 1.1 | 1.8 (+129 / 0 / 53) / 1.3 (+107 / 0 / 66) | 0.9 (+69 / 0 / 20) / 1.2 (+106 / 0 / 57) |
| FALLBACK BY WORTH | 5.1 | 6.7 | 4.7 (+62 / 0 / 58) / 5.5 (+63 / 0 / 46) | 7.2 (+97 / 0 / 101) / 6.1 (+76 / 0 / 105) |
| FIGHT LIFT | 0.1 | 0.1 | 0.1 (+1 / 13 / 13) / 0.0 (+1 / 0 / 0) | 0.0 (+1 / 7 / 3) / 0.1 (+1 / 3 / 0) |
| FIRE AND FLEE | 0.0 | 0.1 | 0.0 (+1 / 0 / 3) / 0.0 (+0 / 0 / 5) | 0.1 (+1 / 4 / 4) / 0.1 (+1 / 0 / 1) |
| FLANK NOT WEIGHED | 5.5 | 6.1 | 5.6 (+0 / 0 / 153) / 5.5 (+0 / 0 / 143) | 6.0 (+0 / 0 / 142) / 6.2 (+0 / 0 / 219) |
| FOCUS FIRE | 0.0 | 0.0 (+0 / 0 / 0) | 0.0 (+0 / 0 / 0) / 0.0 (+1 / 1 / 0) | 0.0 (+0 / 0 / 0) / - |
| FOLLOW UP WEIGHED | 1.2 | 1.2 | 1.2 (+156 / 0 / 51) / 1.2 (+172 / 0 / 29) | 1.2 (+186 / 0 / 30) / 1.2 (+158 / 0 / 53) |
| FRIENDS SHOTS CHECKED | 0.2 | 0.2 | 0.2 (+13 / 0 / 7) / 0.2 (+12 / 0 / 4) | 0.1 (+7 / 0 / 3) / 0.3 (+19 / 0 / 18) |
| GIVES UP | 0.1 | 1.2 | 0.0 (-0 / 8 / 0) / 0.1 (-3 / 14 / 4) | 1.4 (-52 / 204 / 37) / 1.0 (-32 / 124 / 35) |
| GIVES UP ITS SCREEN | 0.1 | 0.8 | 0.0 (-0 / 0 / 1) / 0.1 (-0 / 3 / 1) | 0.9 (-23 / 61 / 16) / 0.6 (-19 / 43 / 14) |
| GROUND FLIERS | 0.0 | 0.0 | 0.0 (+1 / 0 / 0) / 0.0 (+0 / 0 / 0) | 0.0 (+0 / 0 / 0) / 0.0 (+1 / 0 / 2) |
| HELPER ALREADY ASKED | 0.1 | 0.1 | 0.0 (+0 / 6 / 1) / 0.1 (+0 / 11 / 0) | 0.1 (+0 / 5 / 1) / 0.0 (+0 / 3 / 0) |
| HELPER UNSEEN | 0.4 | 0.2 | 0.4 (+0 / 30 / 13) / 0.4 (+0 / 47 / 2) | 0.3 (+0 / 21 / 12) / 0.2 (+0 / 27 / 7) |
| HILL BY ITS CHANCE | 0.3 | - | 0.3 (-33 / 0 / 8) / 0.4 (-40 / 0 / 5) | - / - |
| HOLDS AMBUSHERS | 0.6 | 0.6 | 0.4 (+0 / 0 / 0) / 0.7 (+0 / 0 / 0) | 0.7 (+0 / 0 / 0) / 0.4 (+0 / 0 / 0) |
| HORN WORTH | 0.0 (+1 / 0 / 0) | 0.0 (+1 / 0 / 0) | - / 0.0 (+1 / 0 / 0) | 0.0 (+1 / 0 / 0) / - |
| HUNT ADVANCE | 0.2 | 0.2 | 0.1 (+4 / 6 / 1) / 0.2 (+5 / 6 / 6) | 0.2 (+7 / 10 / 3) / 0.1 (+4 / 9 / 3) |
| HUNT DROPPED | 0.1 | 0.1 | 0.0 (+0 / 0 / 1) / 0.1 (+0 / 8 / 3) | 0.1 (+0 / 4 / 1) / 0.0 (+0 / 0 / 1) |
| HUNT IN PAIRS | 0.5 | 0.5 | 0.4 (+22 / 0 / 9) / 0.5 (+24 / 0 / 9) | 0.5 (+32 / 0 / 9) / 0.4 (+29 / 0 / 8) |
| HUNT KEPT | 0.1 | 0.1 | 0.1 (+3 / 3 / 1) / 0.1 (+2 / 4 / 2) | 0.1 (+4 / 14 / 4) / 0.1 (+2 / 10 / 1) |
| HUNT RESULT | 0.2 | 0.2 | 0.1 (+8 / 0 / 2) / 0.2 (+28 / 9 / 7) | 0.2 (+27 / 15 / 6) / 0.1 (+13 / 0 / 1) |
| HUNT THE GUNS | 0.2 | 0.2 | 0.1 (+28 / 6 / 0) / 0.3 (+89 / 23 / 7) | 0.2 (+86 / 16 / 4) / 0.1 (+36 / 10 / 2) |
| INVITES THE FIGHT | 1.5 | - | 1.7 (+37 / 61 / 24) / 1.3 (+26 / 55 / 15) | - / - |
| JOINT CHARGE PLAN | 0.2 | 0.1 | 0.1 (+10 / 5 / 3) / 0.2 (+8 / 12 / 6) | 0.2 (+17 / 6 / 5) / 0.0 (+0 / 4 / 3) |
| KEEP FALLS | 0.1 | 0.1 | 0.1 (+2 / 0 / 2) / 0.0 (+0 / 0 / 0) | 0.0 (+1 / 0 / 0) / 0.1 (+1 / 0 / 0) |
| KEEPS ITS PREY | 0.1 | 0.2 | 0.0 (+0 / 0 / 0) / 0.1 (+0 / 1 / 4) | 0.3 (+3 / 13 / 14) / 0.2 (+2 / 9 / 6) |
| KEEPS ITS TARGET | 2.0 | 2.0 | 1.8 (+54 / 165 / 41) / 2.2 (+66 / 203 / 49) | 2.2 (+67 / 213 / 59) / 1.7 (+50 / 152 / 46) |
| KEEPS SCOUTS OR AMBUSH | 0.0 | 0.0 | 0.0 (+0 / 0 / 0) / 0.0 (+0 / 0 / 0) | 0.0 (+0 / 0 / 0) / 0.0 (+0 / 0 / 0) |
| KILLS COUNT | 2.1 | 1.8 | 1.8 (+75 / 145 / 39) / 2.5 (+114 / 203 / 57) | 1.9 (+96 / 159 / 50) / 1.7 (+87 / 151 / 56) |
| KILLS COUNT NEXT TURN | 6.2 | 9.5 | 5.3 (+177 / 193 / 133) / 7.0 (+264 / 325 / 177) | 10.6 (+479 / 430 / 251) / 8.4 (+285 / 407 / 210) |
| LONE CHARACTER SAFE SPOT | 0.5 | 0.5 | 0.5 (+23 / 13 / 22) / 0.4 (+9 / 23 / 4) | 0.5 (+14 / 17 / 18) / 0.5 (+23 / 14 / 11) |
| LONE WIZARD HOLDS BACK | 0.2 | 0.2 | 0.1 (+0 / 4 / 0) / 0.4 (+0 / 11 / 12) | 0.2 (+0 / 2 / 14) / 0.1 (+0 / 3 / 4) |
| LONE WIZARD KEPT IN | 0.4 | 0.4 | 0.6 (+38 / 0 / 0) / 0.3 (+23 / 0 / 0) | 0.3 (+23 / 0 / 0) / 0.6 (+38 / 0 / 0) |
| LONG SHOT | 0.5 | - | 0.5 (-3 / 36 / 8) / 0.5 (-1 / 24 / 8) | - / - |
| LOST CHARGE | 2.5 | - | 2.8 (-46 / 106 / 115) / 2.3 (-36 / 79 / 81) | - / - |
| LURE BY WHAT IT DRAWS | 0.1 | - | 0.1 (-6 / 0 / 0) / 0.1 (-7 / 0 / 0) | - / - |
| MAKE SURE TOGETHER | 0.6 | 0.8 | 0.6 (+50 / 6 / 15) / 0.7 (+85 / 33 / 20) | 0.9 (+63 / 19 / 18) / 0.6 (+41 / 24 / 12) |
| MANOEUVRE | 0.2 | 0.2 | 0.2 (+6 / 0 / 1) / 0.1 (+4 / 0 / 4) | 0.2 (+5 / 0 / 4) / 0.1 (+4 / 0 / 2) |
| MARCH AT ESCAPER | 0.1 | 0.1 | 0.1 (+1 / 0 / 8) / 0.0 (+0 / 0 / 1) | 0.1 (+1 / 0 / 6) / 0.0 (+0 / 0 / 0) |
| MARCH CHECK | 0.6 | 0.6 | 0.6 (+24 / 0 / 10) / 0.5 (+20 / 0 / 9) | 0.6 (+30 / 0 / 15) / 0.6 (+29 / 0 / 12) |
| MARCH ODDS | 0.2 | 0.7 | 0.3 (+20 / 16 / 7) / 0.2 (+14 / 7 / 4) | 0.6 (+38 / 17 / 23) / 0.8 (+59 / 40 / 17) |
| MARCH OVER CASTS | 0.4 | 0.5 | 0.5 (+43 / 0 / 23) / 0.3 (+22 / 0 / 4) | 0.4 (+19 / 0 / 10) / 0.6 (+29 / 0 / 19) |
| MAX FOR POSITIONING | 4.8 | 5.0 | 4.6 (+170 / 0 / 119) / 4.9 (+185 / 0 / 132) | 5.3 (+212 / 0 / 98) / 4.7 (+186 / 0 / 126) |
| MISSILES IN THE MOVE | 3.5 | 3.4 | 4.1 (+155 / 0 / 107) / 2.9 (+53 / 0 / 94) | 3.0 (+54 / 0 / 89) / 3.7 (+130 / 0 / 95) |
| MISSILES NEXT TURN | 4.2 | 4.2 | 4.9 (+98 / 0 / 150) / 3.5 (+37 / 0 / 103) | 3.7 (+41 / 0 / 111) / 4.7 (+88 / 0 / 131) |
| MODEL FACING | 0.2 | 0.2 | 0.3 (+69 / 0 / 2) / 0.1 (+22 / 0 / 1) | 0.1 (+15 / 0 / 0) / 0.2 (+50 / 0 / 1) |
| MONSTER WIZARD ROAMS | 0.2 | 0.2 | 0.2 (+0 / 6 / 5) / 0.2 (+0 / 15 / 0) | 0.2 (+0 / 6 / 6) / 0.2 (+0 / 17 / 3) |
| MOVE AND CAST | 0.2 | 0.2 | 0.3 (+21 / 0 / 10) / 0.2 (+10 / 0 / 4) | 0.2 (+8 / 0 / 9) / 0.2 (+9 / 0 / 6) |
| MOVE SPELL IN RANGE | 0.1 | 0.2 (+6 / 0 / 4) | 0.2 (+5 / 0 / 8) / 0.0 (+0 / 0 / 0) | - / 0.2 (+6 / 0 / 4) |
| MOVE SPELL NOT WORTH | 0.0 (-0 / 0 / 0) | 0.0 (-0 / 0 / 0) | - / 0.0 (-0 / 0 / 0) | 0.0 (-0 / 0 / 0) / - |
| MOVE SPELL OUT OF RANGE | 0.2 | 0.3 | 0.4 (-33 / 5 / 23) / 0.1 (-5 / 0 / 5) | 0.1 (-3 / 0 / 16) / 0.5 (-45 / 0 / 18) |
| MOVE SPELL SPOT | 0.2 | 0.2 | 0.3 (+0 / 0 / 18) / 0.1 (+0 / 0 / 5) | 0.1 (+0 / 0 / 3) / 0.4 (+0 / 0 / 15) |
| MOVE TO CHARGE | 3.8 | - | 3.0 (+190 / 112 / 82) / 4.6 (+355 / 225 / 130) | - / - |
| MOVES UNITS SPELL | 0.1 | 0.1 | 0.1 (+3 / 0 / 0) / 0.1 (+1 / 0 / 0) | 0.1 (+1 / 0 / 0) / 0.1 (+3 / 0 / 0) |
| NEEDED THERE | 0.1 | 0.1 | 0.0 (+5 / 5 / 1) / 0.1 (+11 / 13 / 0) | 0.1 (+10 / 10 / 4) / 0.0 (+4 / 4 / 0) |
| NO RALLY LEFT | 0.0 | 0.0 | 0.0 (+6 / 0 / 1) / 0.0 (+1 / 0 / 0) | 0.0 (+1 / 0 / 3) / 0.0 (+3 / 0 / 2) |
| NOT NEEDED | 0.3 | 0.2 | 0.3 (-19 / 30 / 2) / 0.4 (-21 / 44 / 4) | 0.3 (-16 / 25 / 10) / 0.2 (-13 / 16 / 2) |
| NOT TURNED | 5.8 | 6.3 | 5.7 (+115 / 0 / 131) / 5.9 (+81 / 0 / 105) | 6.4 (+120 / 0 / 131) / 6.3 (+103 / 0 / 181) |
| NOT WORTH A CAST | 0.6 | 0.5 | 0.7 (-1 / 0 / 43) / 0.5 (-0 / 0 / 0) | 0.4 (-1 / 0 / 4) / 0.6 (-0 / 0 / 23) |
| OFF BEST | 15.2 | 17.1 | 15.4 (-757 / 9 / 271) / 14.9 (-818 / 18 / 271) | 17.1 (-1009 / 42 / 292) / 17.2 (-935 / 27 / 403) |
| OPENS A LANE | 0.2 | 0.2 | 0.2 (+2 / 24 / 1) / 0.1 (+1 / 6 / 4) | 0.1 (+0 / 12 / 0) / 0.2 (+0 / 22 / 0) |
| OPENS UP | 0.3 | 0.2 | 0.3 (+22 / 16 / 12) / 0.3 (+34 / 11 / 14) | 0.2 (+20 / 10 / 2) / 0.2 (+13 / 11 / 1) |
| OVERRUN THREAT | 0.0 (+0 / 0 / 1) | 0.0 | 0.0 (+0 / 0 / 1) / - | 0.0 (+0 / 0 / 0) / 0.0 (+0 / 0 / 0) |
| OVERRUNS AWAY | 0.6 | 0.6 | 0.5 (+16 / 50 / 22) / 0.6 (+15 / 46 / 18) | 0.6 (+14 / 60 / 25) / 0.5 (+13 / 37 / 20) |
| PATHS CROSS | 2.5 | 2.3 | 2.2 (+155 / 0 / 36) / 2.7 (+226 / 0 / 43) | 2.8 (+206 / 0 / 45) / 1.9 (+121 / 0 / 24) |
| PERIAPT WORTH | 0.0 | 0.0 | 0.0 (+2 / 0 / 0) / 0.0 (+4 / 0 / 8) | 0.0 (+3 / 0 / 4) / 0.0 (+2 / 0 / 0) |
| PIVOT GUARDS FLANK | 0.2 | 0.1 | 0.1 (-3 / 0 / 4) / 0.2 (-2 / 0 / 8) | 0.1 (-1 / 0 / 3) / 0.1 (-1 / 0 / 3) |
| PLAN RESULT | 38.5 | 37.3 | 38.1 (+1474 / 1491 / 998) / 38.9 (+1370 / 1494 / 1012) | 38.4 (+1258 / 1402 / 1045) / 36.3 (+1428 / 1360 / 1077) |
| PURSUES BIG PREY | 0.1 | 0.1 | 0.1 (-6 / 0 / 0) / 0.1 (-11 / 0 / 3) | 0.1 (-8 / 0 / 3) / 0.0 (-3 / 0 / 3) |
| PURSUES ON | 0.0 (-0 / 0 / 0) | 0.0 (+0 / 0 / 1) | 0.0 (-0 / 0 / 0) / - | - / 0.0 (+0 / 0 / 1) |
| RAIDS THE BAGGAGE | 0.0 | 0.0 (+5 / 0 / 0) | 0.0 (+1 / 0 / 0) / 0.0 (+6 / 0 / 0) | 0.0 (+5 / 0 / 0) / - |
| RAIDS THE BAGGAGE NEXT TURN | 0.1 | 0.1 | 0.0 (+3 / 0 / 0) / 0.1 (+7 / 0 / 1) | 0.1 (+5 / 0 / 0) / 0.1 (+5 / 0 / 0) |
| RANDOM MOVE BY FIGURES | 1.2 | - | 0.9 (+16 / 0 / 18) / 1.6 (+18 / 0 / 48) | - / - |
| RANDOM MOVER NO PROMISE | 0.3 | - | 0.2 (-15 / 1 / 6) / 0.4 (-19 / 16 / 9) | - / - |
| REDIRECT BY WHAT IT STOPS | 0.3 | - | 0.2 (-3 / 0 / 1) / 0.4 (-7 / 0 / 6) | - / - |
| REDIRECT COUNTER | 3.1 | 3.8 | 2.1 (+141 / 0 / 28) / 4.1 (+323 / 0 / 56) | 4.5 (+333 / 0 / 87) / 3.1 (+173 / 0 / 58) |
| REDIRECT WEIGHED | 0.3 | 0.3 | 0.2 (+3 / 6 / 13) / 0.4 (+17 / 13 / 9) | 0.4 (+11 / 8 / 7) / 0.2 (+6 / 7 / 6) |
| RESERVE FALL BACK | 0.7 | - | 0.6 (+15 / 0 / 9) / 0.8 (+25 / 0 / 14) | - / - |
| RESTRAINS TO SHOOT | 0.1 | 0.1 | 0.1 (+3 / 0 / 3) / 0.1 (+5 / 0 / 3) | 0.0 (+4 / 0 / 1) / 0.1 (+4 / 0 / 5) |
| RISK BY ARC | 3.3 | 2.6 | 3.1 (+105 / 280 / 101) / 3.5 (+69 / 317 / 97) | 2.7 (+53 / 256 / 96) / 2.5 (+85 / 212 / 97) |
| SAFE SURE CHARGE | - | 0.0 (-0 / 0 / 0) | - / - | - / 0.0 (-0 / 0 / 0) |
| SAFER THAN THE JOB | 0.9 | 0.7 | 1.1 (+65 / 0 / 25) / 0.7 (+43 / 0 / 39) | 0.7 (+44 / 0 / 29) / 0.7 (+36 / 0 / 36) |
| SCOUT SPOT | 0.3 | 0.3 | 0.4 (+1 / 0 / 1) / 0.3 (+1 / 0 / 1) | 0.3 (+1 / 0 / 0) / 0.4 (+1 / 0 / 0) |
| SCOUT WAITS | 0.3 | 0.3 | 0.4 (+0 / 0 / 1) / 0.3 (+0 / 0 / 1) | 0.3 (+0 / 0 / 0) / 0.4 (+0 / 0 / 0) |
| SCREEN BY WHAT IT SAVES | 0.2 | - | 0.1 (-1 / 0 / 1) / 0.3 (-13 / 0 / 1) | - / - |
| SEARCH SPOT | 2.5 | 1.8 | 2.4 (+119 / 0 / 48) / 2.7 (+147 / 0 / 32) | 1.8 (+116 / 0 / 28) / 1.8 (+95 / 0 / 39) |
| SECOND HUNTER | 0.0 | 0.0 | 0.0 (-0 / 1 / 1) / 0.0 (-0 / 3 / 0) | 0.0 (-0 / 4 / 0) / 0.0 (-0 / 2 / 1) |
| SELF MOVE SPELL | 0.2 | 0.2 | 0.3 (+19 / 0 / 17) / 0.2 (+16 / 0 / 19) | 0.2 (+21 / 0 / 10) / 0.3 (+30 / 0 / 5) |
| SET UP TOGETHER | 1.1 | 1.4 | 0.9 (+80 / 15 / 21) / 1.4 (+157 / 55 / 39) | 1.9 (+143 / 38 / 51) / 0.9 (+66 / 41 / 20) |
| SET-UP ANY TARGET | 0.3 | 0.2 | 0.4 (+60 / 8 / 8) / 0.2 (+19 / 7 / 15) | 0.2 (+20 / 3 / 9) / 0.3 (+45 / 8 / 5) |
| SET-UP MISSED | 0.1 | 0.0 | 0.1 (+8 / 1 / 1) / 0.0 (+6 / 0 / 2) | 0.0 (+8 / 1 / 0) / 0.0 (+5 / 3 / 0) |
| SHOOTER COUNTED ONCE | 0.0 (-0 / 0 / 0) | - | - / 0.0 (-0 / 0 / 0) | - / - |
| SHOOTERS IN TWO RANKS | 0.3 | 0.3 | 0.4 (+1 / 0 / 0) / 0.2 (+0 / 0 / 0) | 0.2 (+0 / 0 / 0) / 0.4 (+1 / 0 / 0) |
| SHOOTS FROM THE BEST SPOT | 0.9 | - | 1.1 (+45 / 76 / 11) / 0.7 (+25 / 30 / 11) | - / - |
| SHORT GUN FORWARD | 0.2 | 0.2 | 0.2 (+0 / 0 / 1) / 0.1 (+0 / 0 / 1) | 0.1 (+0 / 0 / 2) / 0.2 (+0 / 0 / 2) |
| SHOT REPLANNED | 0.5 | 0.4 | 0.7 (+0 / 136 / 10) / 0.3 (+0 / 44 / 1) | 0.2 (+0 / 41 / 6) / 0.6 (+0 / 126 / 11) |
| SHOTS IN THE MOVE | 11.5 | 10.8 | 14.3 (+576 / 0 / 234) / 8.7 (+265 / 0 / 150) | 8.7 (+285 / 0 / 131) / 13.0 (+576 / 0 / 247) |
| SPELL CATCH ODDS | 0.0 | 0.0 (-2 / 0 / 0) | 0.0 (-1 / 4 / 3) / 0.0 (-0 / 0 / 0) | - / 0.0 (-2 / 0 / 0) |
| SPELL SETS UP CHARGE | 0.3 | 0.3 | 0.5 (+98 / 8 / 8) / 0.2 (+41 / 7 / 17) | 0.2 (+39 / 3 / 11) / 0.4 (+74 / 10 / 6) |
| SPELL WORTH | 1.6 | 1.6 | 1.1 (+23 / 69 / 71) / 2.0 (+37 / 95 / 92) | 2.1 (+38 / 64 / 62) / 1.1 (+16 / 63 / 63) |
| STABLE ROLE | 11.0 | - | 11.4 (+0 / 397 / 154) / 10.6 (+0 / 397 / 154) | - / - |
| STANDS TO CAST | 0.0 | 0.0 | 0.0 (+1 / 0 / 0) / 0.0 (+1 / 0 / 2) | 0.0 (+1 / 3 / 1) / 0.0 (+2 / 7 / 2) |
| STAY WEIGHED | 0.0 | - | 0.0 (+1 / 0 / 0) / 0.0 (+2 / 0 / 1) | - / - |
| STOPS | 0.1 | 0.1 | 0.0 (+2 / 2 / 1) / 0.1 (+5 / 20 / 2) | 0.1 (+6 / 18 / 4) / 0.0 (+1 / 6 / 0) |
| STOPS SHORT OF THE FLANK | 0.5 | 0.4 | 0.5 (+23 / 0 / 15) / 0.4 (+19 / 0 / 19) | 0.3 (+15 / 0 / 6) / 0.5 (+23 / 0 / 13) |
| STUCK PIVOT | 0.2 | 0.2 | 0.1 (+0 / 0 / 1) / 0.2 (+0 / 0 / 6) | 0.4 (+0 / 0 / 10) / 0.1 (+0 / 0 / 4) |
| SUPPORT JOB KEPT | 0.0 (+0 / 0 / 0) | 0.0 | - / 0.0 (+0 / 0 / 0) | 0.0 (+0 / 0 / 0) / 0.0 (+0 / 1 / 0) |
| SUPPORT NARROWED | 7.3 | - | 6.4 (-53 / 359 / 119) / 8.2 (-59 / 482 / 119) | - / - |
| SUPPORTS | 4.5 | - | 3.9 (+57 / 154 / 59) / 5.1 (+62 / 212 / 59) | - / - |
| SURE CHARGE BEATS ADVANCE | 0.1 | 0.2 | 0.1 (-6 / 9 / 4) / 0.1 (-3 / 5 / 0) | 0.1 (-6 / 9 / 2) / 0.2 (-8 / 15 / 3) |
| SURE REACH TOGETHER | 0.5 | 0.6 | 0.5 (-2 / 12 / 20) / 0.5 (+0 / 0 / 10) | 0.7 (-2 / 13 / 12) / 0.4 (-1 / 17 / 13) |
| THROUGH LINE OF FIRE | 0.3 | 0.2 | 0.5 (+15 / 0 / 5) / 0.2 (+9 / 0 / 1) | 0.2 (+13 / 0 / 4) / 0.3 (+12 / 0 / 11) |
| TURN WORTH | 0.6 | 0.3 | 0.6 (-45 / 55 / 16) / 0.6 (-46 / 49 / 7) | 0.3 (-22 / 20 / 9) / 0.4 (-30 / 39 / 6) |
| TWO OR MORE ARRIVE | 0.3 | 0.3 | 0.3 (+3 / 9 / 7) / 0.3 (+3 / 25 / 6) | 0.4 (+3 / 6 / 10) / 0.3 (+2 / 9 / 5) |
| WAIT AFTER COSTS | 7.3 | - | 6.9 (-294 / 247 / 125) / 7.8 (-397 / 344 / 174) | - / - |
| WALKS TO THE FIGHT | 1.5 | - | 1.9 (+41 / 51 / 12) / 1.2 (+22 / 27 / 17) | - / - |
| WAR ENGINE CHARGES | 0.1 | - | 0.1 (+9 / 5 / 3) / 0.0 (+5 / 2 / 0) | - / - |
| WAR ENGINE JOBS | 0.4 | - | 0.7 (+0 / 43 / 9) / 0.2 (+0 / 9 / 9) | - / - |
| WEARS DOWN | 1.6 | 1.1 | 1.5 (+61 / 167 / 48) / 1.6 (+51 / 166 / 37) | 1.3 (+43 / 146 / 48) / 1.0 (+48 / 108 / 43) |
| WHO HITS BACK | 0.2 | 0.2 | 0.3 (+18 / 0 / 18) / 0.2 (+21 / 0 / 8) | 0.2 (+21 / 0 / 14) / 0.3 (+28 / 0 / 12) |
| WHOLE FIGHT | 0.5 | 0.3 | 0.4 (+27 / 52 / 8) / 0.5 (+16 / 83 / 10) | 0.4 (+22 / 71 / 7) / 0.3 (+6 / 41 / 6) |
| WHOLE FIGHT GAIN | 0.5 | 0.4 | 0.3 (+41 / 47 / 6) / 0.7 (+57 / 64 / 11) | 0.6 (+47 / 34 / 15) / 0.3 (+34 / 32 / 11) |
| WOUNDED STAYS OUT | 0.0 (+0 / 1 / 3) | - | - / 0.0 (+0 / 1 / 3) | - / - |

## 6. Sim bugs and stalls

- **Stall, L1731 in fwopp-3** (Drawn Battlelines, framework on Opponent): the computer's Turn 2 Opponent Movement did not end within
  3 minutes ("computer settled False"). Filed as sim bug **S-2fbe8e**, marked fixed 2026-11-10, so it is **back**. The same pair failed in
  batch 1 too (then in the lessons step after the game). Its fwmine game ended normally. Game log in fwopp-3/game-L1731-3-1.*.
- **Late SETUP POSITION findings (checked in turn 6), 3 games**: L1823 fwmine-1 (Mine Gnoblar Fighters 2 overlaps Mine Gorger by 0.15"),
  L0827 fwmine-2 (Mine Nuln Veteran State Troops overlaps impassable terrain by 0.62"), L1531 fwmine-2 (Mine Lothern Skycutter overlaps
  Opponent Marauder Horsemen by 0.33"). All three on the framework side (Mine in fwmine); small overlaps.
- The Orion pairs that never started in batch 1 (L2033, L2433, L3033) all played in both halves.
- Containers restarted several times (fwmine-3 lost its first 40 minutes); its last 18 pairs were run in two other containers
  (fwmine-3b, fwmine-3c). Two games played twice by that split (L1122, L1216) are counted once.

## 7. What this means

With the five charge fixes the framework went from -81 to **+59 VP a game (±108)**: it now charges more than the old brain, gets the
first contact more often, kills more and loses less, and no longer loses when going second. The margin is positive but **still inside the
noise band**, so it is not yet a measured win. The clear signal is by army: **offensive armies gain (+166)** while armies the framework
calls **defensive lose badly (-441, outside noise)**: standing and shooting loses to the old brain's charges.

By Morten's rule (VP margin decides; improvement can be pushed on his word, otherwise discuss), this is an improvement over batch 1 but
not a measured gain over the old brain. Push, or first look at the defensive stance (e.g. a run with only the defensive army switched off
on the framework side), is Morten's call.

Files: the parts in this folder (fwmine-1..4, fwmine-3b, fwmine-3c, fwopp-1..4); compare-all.md; scripts/ (headline2.py, merge.py,
remap.py, stance.py, jobs.py). Replays committed on branch claude/project-thread-9kben2 (40e8476fb, from main 101d908c): deploy/sim-replays/
fw-h2h2-mine-1eea44e-p1, -p2, -p3, -p3b, -p3c, -p4 and fw-h2h2-opp-1eea44e-p1..p4, added to on-site.txt with the earlier batches kept.
Nothing pushed to main.
