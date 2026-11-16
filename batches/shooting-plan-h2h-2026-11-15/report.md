# Shooting plan: head-to-head against main (2026-11-15)

**Verdict: no gain. The side with the shooting plan is behind by 19 VP a game, give or take 92 VP: a dead heat. The plan does kill
more by shooting (about 1 more enemy unit every 4 games, +23 points a game), but it picks easy kills, so it shoots the enemy's top
killer LESS often than main does (war machines 24% v 28%, magic missiles 18% v 28%).**

Batch: 288 games, the same 144 DKTC pairs and seeds as today's top-killer and charge-odds head-to-heads (Hero v Hero, seed 1, scenarios
mix), each played twice. One side plays branch `claude/project-thread-58bw08` at `89601eaf` with the whole `shooting-plan` group on
(11 tags, FIRE PLAN and the rest); the other side has it switched off = main. mine-*: plan on for Mine; opp-*: plan on for Opponent.
287 games ended; 1 stalled (L0413 in opp-3, a combat-phase stall, see Findings), so 143 pairs are compared. Main's side wrote no rows of
the switched-off tags: no switch leak.

## 1. Morten's five headline numbers

| # | Number | **With the plan** | **Main** | Difference |
| --- | --- | --- | --- | --- |
| 1 | VP margin per game | **-19** | +19 | **-19 ±92** (paired over 143 pairs) |
| 2 | First round won when charging | 69% | 73% | -4 points |
| 3 | Net points per charged fight | +77 | +80 | -3 |
| 4 | Points lost per game | 761 | 749 | +12 ±53 |
| 5 | Free units caught in flank or rear (per game, lower is better) | 0.56 | 0.58 | -0.02 |

W/D/L of the plan side 114 / 55 / 117; pairs where it is ahead over both games 68, behind 69. As Mine -74, as Opponent +35 (the lists,
the pairing cancels it). Going first +136, second -175.

Diagnostics (not targets):

| | With the plan | Main |
| --- | --- | --- |
| Charges that made contact a game | 3.75 | 3.8 |
| Points that never fought | 37% | 35% |
| Lone characters that fought | 78% | 78% |
| Joined characters whose unit fought | 39% | 44% |

## 2. What the plan was for: the guns

Top killer = the enemy unit that took most of this side's points in fights (read after the game). "Free" = alive, not inside a unit,
not in a fight, when the shot was fired.

| | With the plan | Main |
| --- | --- | --- |
| **War machine shots at the top killer when it was free** | **24%** (151 of 633) | 28% (169 of 596) |
| **Magic missiles at the top killer when it was free** | **18%** (69 of 382) | 28% (98 of 351) |
| Other shooting at the top killer when free | 22% (385 of 1,759) | 32% (514 of 1,588) |
| Top killer dead by round 3 | 6% (16 of 256) | 6% (15 of 252) |
| Top killer dead by the end | 28% | 23% |
| Enemy's dearest unit dead by round 3 (does not depend on who killed what) | 10% | 14% |
| Enemy units destroyed by shooting, war machines and magic a game | **1.37 (180 pts)** | 1.11 (157 pts) |
| ...of them finished by 2+ of the army's shooters in the same phase | 0.39 | 0.32 |
| Shots at enemy war machines (a main target by the ruling) | 5% of war machine shots, 3% of other shots | 5%, 2% |

Why, read from the plan's own rows: it picks its main target by the chance to kill it this turn and next. In the sample games that
was Fell Bats, Horse Archers, a Corpse Cart: cheap units it can finish. So more units die to shooting, but the units that win the fights
are left alone. Warning, not a proposal: as built, the plan prefers what it can kill over what hurts most; the threat figure is there
(SHOOTERS ARE THREATS, THREAT AT FULL SIZE) but changed only 0.24 choices a game.

How often the plan's parts changed a choice (rows a game on the plan side, 288 games):

| Tag | Rows a game | Changed a choice a game |
| --- | --- | --- |
| FIRE PLAN | 13.6 | 4.7 |
| SHOOTERS TO THE PRIMARY | 4.8 | 0.35 |
| MISSILES IN THE FIRE PLAN | 2.7 | 0.25 |
| KEEPS THE TARGET | 1.35 | 0.44 |
| SHOOTERS ARE THREATS | 3.2 | 0.14 |
| THREAT AT FULL SIZE | 7.1 | 0.10 |
| FIRE IN ORDER | 0.65 | 0.65 |
| BEST MOVE FOR SHOOTERS | 0.84 | 0.84 |
| STAY WORTH | 13.8 | 0.59 |

## 3. Shooting-heavy armies v the rest

Shooting-heavy = 30%+ of the army's points in shooting units and war machines (characters not counted; a rough stand-in for the 11-14
definition, which is not on this build). Paired: the same army in the same pair, with the plan minus as main.

| Set | Army-games | With the plan | As main | Plan minus main | Better / worse |
| --- | --- | --- | --- | --- | --- |
| Shooting-heavy | 45 | -524 | -528 | **+4 ±261** | 21 / 24 |
| The rest | 241 | +75 | +122 | -47 ±152 | 116 / 115 |

Neither is more than noise.

## 4. Missiles and marches

| | With the plan | Main |
| --- | --- | --- |
| Missiles tried each own turn (target 50%) | 32% | 31% |
| ...when they could be (not in combat, slain, fleeing, off table) | 48% | 46% |
| Fighting wizards (monster, chariot, monstrous mount) | 27% | 25% |
| Other wizards | 37% | 36% |
| **Volleys lost to marching** (shooter turns not shot because it marched, a game) | **1.5** | 2.2 |
| Missiles lost to marching a game | 0.85 | 0.85 |
| Points destroyed by shooting units a game | 58 | 62 |
| Points destroyed by war machines a game | 54 | 44 |
| Points destroyed by magic (all spells) a game | 72 | 55 |

## 5. VP by source, stance, jobs

| Per game | With the plan | Main |
| --- | --- | --- |
| Kills VP | 789 | 797 |
| Objectives VP | 566 | 570 |
| Leaders VP | 51 | 59 |
| Units lost | 5.1 | 5.1 |

| Stance | With the plan | Main |
| --- | --- | --- |
| Turns the army played defensive | 17% | 18% |
| VP margin, armies mostly defensive | -436 (51 games) | -405 (50) |
| VP margin, armies mostly offensive | +70 (235) | +110 (237) |

| Jobs | With the plan | Main |
| --- | --- | --- |
| Shoot jobs that happened | 60% | 57% |
| What a shoot job claimed (mean VP) | about 61 | about 14 |
| Charge jobs that happened | 58% | 58% |

The plan's shoot jobs claim four times as much as main's and do not happen much more often.

## 6. Findings (filed as sim bugs by the sites)

- L0413 (opp-3, A Chance Encounter): the computer found no next step in its Combat phase, turn 5 (Chaos Dwarf Warriors with 1 of 12
  models in the fight against an Archmage and Silver Helms). Game left out.
- L1131 and L1731 (mine side): Marauder units end overlapping impassable terrain by 1.06" and 0.40".

## Files

- Parts: mine-1..4 (mine-3 holds pairs up to L1731), mine-3b (the last 9 pairs of mine-3, run by the owner), opp-1..4.
- Replays: branch `claude/project-thread-qeh5wt` at `df94a0bb5` carries deploy/sim-replays/sp-h2h-mine-89601ea and sp-h2h-opp-89601ea
  (288 games, on-site.txt set to these two). Not pushed to main.
- Figures: compare-batches.py on this build (game by game: compare-all.md); top-killer, kills and split figures by scripts/ in this folder.
