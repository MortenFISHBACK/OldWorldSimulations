# Staying to shoot: head-to-head against today's main (2026-11-15)

**Verdict: inside the noise. The changed side is ahead by +65 VP a game, give or take 101 VP. Not a proven gain, and not a loss.**
Every one of Morten's five headline numbers points the same way (the changed side slightly better), but none is clearly outside chance.
The gain sits in the offensive armies (+77 VP a game, about at the noise edge); the gunline armies these changes were built for did not
gain anything (+6 VP a game, ±159).

Batch: 288 games, 144 DKTC pairs played twice (Hero v Hero, seed 1, scenarios mix), the same pairs and seeds as head-to-head 2. In every
game one side plays branch `claude/project-thread-dnukaz` at `7c46ffc15` with the seven changes on, the other side plays with
`shots-over-turns` switched off for it = main 8a44e6692. shots-mine-1..4: changes on for Mine; shots-opp-1..4: changes on for Opponent.
All 288 games ended; no findings, no stalls, no one-side-only errors; every part's rules-off list named all seven tags for the right side.
Figures from compare-batches.py of the branch with the first-round-won fix of `claude/first-round-won-fix` 407077ff applied on top
(scripts/report/compare-batches.py). Analysis scripts of the shots-and-missiles report skip pair L1731 (286 games) as they did before.

## 1. Morten's five headline numbers

| # | Number | **With the changes** | **Main** | Difference | Read |
| --- | --- | --- | --- | --- | --- |
| 1 | VP margin per game | **+65** | -65 | **+65 ±101** (paired over 144 pairs) | inside noise |
| 2 | First round won when charging | 72% | 72% | 0 | same |
| 3 | Net points per charged fight | +88 | +78 | +10 | small, better |
| 4 | Points lost per game | 734 | 773 | -39 ±64 | better, inside noise |
| 5 | Free units caught in flank or rear (per game, lower is better) | 0.59 | 0.66 | -0.07 | slightly better |

W/D/L of the changed side 127 / 46 / 115; pairs where the changed side is ahead over both games 72, behind 67.
For comparison, head-to-head 2 (framework v old brain) was +59 ±108.

## 2. Who gained: offensive v gunline armies

Gunline = the 49 army-games the framework played defensively in head-to-head 2 (defensive-stance-2026-11-14/report.md): the same
armies on the same sides here. Each row pair is the same army in the same pair, once with the changes and once as main (VP margin of that army).

| Set | Army-games | VP margin of that army | Ahead | Kills VP | Objectives VP | Leaders VP | Points lost | Enemy kills VP | Enemy objectives VP | Enemy points lost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gunline armies, with the changes | 49 | -475 ±344 | 16 | 648 | 512 | 37 | 819 | 845 | 736 | 607 |
| Same gunline armies, as main | 49 | -488 ±357 | 20 | 677 | 493 | 32 | 819 | 843 | 752 | 628 |
| Other armies, with the changes | 239 | +175 ±170 | 140 | 852 | 599 | 65 | 716 | 766 | 525 | 807 |
| Other armies, as main | 239 | +22 ±170 | 112 | 800 | 575 | 62 | 763 | 812 | 550 | 755 |

Paired, changes minus main for the same army: gunline **+13 ±317** per army-game (24 better, 25 worse); other armies **+153 ±159**
(120 better, 109 worse); all +129 ±142 per army-game (= +65 a game). The gunlines still lose about -480 a game whoever plays them:
that is the lists, as the stance report found.

## 3. VP by source (per game, changed side v main)

| Source | With the changes | Main | Difference (paired) |
| --- | --- | --- | --- |
| Kills | 817 | 779 | +38 ±63 |
| Objectives | 584 | 561 | +24 ±41 |
| Leaders | 60 | 56 | +4 |
| Other | 1 | 2 | 0 |
| Units lost | 4.9 | 5.3 | -0.4 |
| Points lost | 734 | 773 | -39 ±64 |

Going first v second (changed side's margin): first +121 ±213 (67/23/54), second +8 ±226 (60/23/61). As Mine -84, as Opponent +213:
the side split is the lists (Mine and Opponent hold different armies), the pairing cancels it.

## 4. What the changes were meant to move

### Missiles tried (target 50% of the army's missiles each round, every wizard counted)

| Missiles tried each own turn | With the changes | Main |
| --- | --- | --- |
| All missile wizards | 34% | 31% |
| ...when they could be (not in combat, slain, fleeing, off table) | 49% | 46% |
| Fighting wizards (monster, chariot, monstrous mount) | 30% | 26% |
| - round 1 | 18% | 22% |
| - rounds 2+ | 32% | 27% |
| Other wizards | 38% | 35% |
| - round 1 | 36% | 32% |
| - rounds 2+ | 38% | 36% |
| Magic missiles cast a game | 1.5 | 1.4 |
| Wounds by magic missiles a game | 2.6 | 2.2 |
| Points destroyed by magic (all spells) a game | 59 | 56 |

Up 3 points; still far from 50%. Fighting wizards in round 1 went down (18% v 22%).

### Shots given up to marching (shooting units and missile wizards that marched)

| | With the changes | Main |
| --- | --- | --- |
| Marches by shooters, all armies (per army-game) | 1.67 (477) | 2.08 (596) |
| ...with a target already in range before the march | 0.71 (202) | 1.02 (292) |
| Gunline armies: marches by shooters (per army-game) | 3.0 (149) | 3.8 (184) |
| ...with a target already in range before the march | 1.6 (78) | 2.1 (105) |

Down about a quarter: fewer volleys thrown away. Shots by shooting units a game 9.9 v 9.4; points destroyed by shooting units 63 v 59.

### War machine shots at the enemy's top killer (the enemy unit that took most of this side's points in fights)

| | With the changes | Main |
| --- | --- | --- |
| All armies: war machine shots at the top killer | 18% | 21% |
| ...when the top killer was free to be shot | 25% | 30% |
| Gunlines: war machine shots at the top killer | 18% | 22% |
| ...when it was free | 26% | 28% |
| Shooting units at the top killer when free (all / gunlines) | 42% / 37% | 38% / 41% |
| Points destroyed by war machines a game | 43 | 50 |

No better, slightly worse: THREAT IN THE KILL did not turn the guns onto the killer. (The top killer is read after the game, so a side
that kills the killer early has a different top killer; read with care.)

## 5. The seven changes: how often, and claimed v happened

Rows = the hidden OpponentRule rows a game on the changed side; changed = the row says the rule CHANGED the choice. Followed up = the
job's PLAN RESULT row in a later turn (planned VP, the VP it won).

| Item | Rows a game | Changed the choice a game | Jobs followed up | Happened | Planned v won a job | Changed jobs: happened, planned v won |
| --- | --- | --- | --- | --- | --- | --- |
| 1 STAY WORTH | 15.1 | 1.03 | 1,578 | 53% | 44.5 v 59.9 | 34% of 181, **63.0 v 30.6** |
| 2 BEST MOVE FOR SHOOTERS | 0.91 | 0.91 | (spot moves, no plan row) | | | claimed +68 / +86 VP a change |
| 3 THREAT IN THE KILL | 8.8 | 0.68 | 1,018 | 63% | 44.4 v 86.2 | 69% of 128, 21.6 v 79.8 |
| 4 FOCUS OVER TURNS | 1.17 | 0.56 | 266 | 74% | 2.2 v 58.2 | 72% of 120, 2.1 v 41.8 |
| 5 MISSILES IN THE PLAN | 0.79 | 0.01 | 17 | 71% | 83.8 v 73.2 | 2 only |
| 6 FACE THE CAST | 0.06 | 0.06 | (reform, no plan row) | | | 17 in 286 games |
| 7 WIZARD FRONT RANK | 0.01 | 0.01 | - | | | 3 in 286 games, all on Opponent |

Jobs by kind (all units, changed side v main): shoot jobs 1,936 v 1,836, happened 63% v 61%, planned 29 v 9 VP, won 71 v 77 VP.
Charge 61% v 56% happened; close in 29% v 26%.

Read: STAY WORTH is the big one and over-claims where it changes the choice (says 63 VP, wins 31, and only a third of those jobs
happen). FOCUS OVER TURNS under-claims (2 v 42). Items 5-7 almost never decide anything: 5 changed 2 choices, 6 17, 7 3 in 286 games.

## 6. Every KPI side by side

Full tables (changes v main, with the Mine-game / Opp-game split): kpis-changes-v-main.md in this folder. Full comparison output:
compare-all.md. Short list:

| KPI | With the changes | Main |
| --- | --- | --- |
| Charges declared / contact a game | 5.3 / 3.9 | 5.2 / 3.7 |
| Sides that never made charge contact | 8% | 11% |
| Charges in flank or rear (contact) | 49% | 49% |
| Joint charges a game | 0.5 | 0.5 |
| Set-ups that charged next turn | 17% | 17% |
| Points that never fought | 36% | 36% |
| Infantry points that never fought | 48% | 50% |
| Units over 100 pts that earned no points | 56% | 58% |
| Joined characters whose unit fought | 45% | 39% |
| Lone characters that fought | 77% | 79% |
| Turned to face a threat (FACES THE THREAT) a game | 1.38 | 1.54 |
| Stood instead of an exposed job (SAFER THAN THE JOB) a game | 0.63 | 0.92 |
| Pursued after the loser fell back in good order | 92% | 86% |
| Points run down a game | 119 | 87 |
| Points destroyed in combat a game | 384 | 374 |
| Net per 100 charger points, damage counted | +31.9 | +27.1 |
| Charges by band: sweet spot 55-75% (count) | 72 | 56 |
| Turns played defensive | 16% | 18% |

## 7. Warnings (what the code would do; not checked in code here)

- **THREAT IN THE KILL fires on the switched-off side too**: 201 rows in 286 games on the main side (0.7 a game, against 8.8 on the
  changed side), 18 of them changing a choice; 180 of the 201 are shots or casts at enemy characters. So the "main" side is not quite
  main: the switch misses one path. The effect on the result is small (18 changed choices in 286 games, about a tenth of the changed
  side's 0.68 a game) and, if anything, makes the gain look smaller. The cause is not yet found.
- WIZARD FRONT RANK fired 3 times, all on the Opponent side: likely just rare, but never on Mine.

## 8. What this means

- Not a proven gain: +65 ±101. On Morten's rule ("hold until sims have proven its worth") this does not earn the push on its own.
- Real movements, each small: fewer volleys given up to marching (-25%), missiles tried +3 points, points lost -39, net per fight +10.
- The target armies (gunlines) did not gain; the gain is in offensive armies. The guns still do not hunt the top killer.
- STAY WORTH over-claims on the jobs it changes; items 5-7 barely act.
- Options for planning: a second head-to-head on another seed (288 more games would narrow the band to about ±70) to see whether +65
  holds, or first fix the THREAT IN THE KILL leak and the STAY WORTH over-claim and then rerun.

## Files

- Parts: shots-mine-1..4, shots-opp-1..4 (game logs, records, units). counts.log: part counts as reported.
- compare-all.md (A = shots Mine, B = shots Opp), kpis-changes-v-main.md (remapped to changes / main).
- scripts/report/: h.py (headline), g.py (gunline split, VP by source), items.py (the seven items), remap.py, compare-batches.py used.
- Replays: branch `claude/project-thread-vsuxxo` at 1f1a5cce6 carries deploy/sim-replays/shots-h2h-{mine,opp}-7c46ffc-p1..4 (288 games,
  added to on-site.txt, earlier batches kept). Not pushed to main.
