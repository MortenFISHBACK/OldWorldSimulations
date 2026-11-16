# Top-killer fix: head-to-head against today's main (2026-11-15)

**Verdict: inside the noise, and no better than the last batch. The changed side is ahead by +52 VP a game, give or take 104 VP
(last batch, without the top-killer fix: +65 ±101). The top-killer fix makes the figure bigger, but the guns still do not go for the
enemy's top killer: 26% of free war machine shots with the changes, 30% on main.**

Batch: 288 games, the same 144 DKTC pairs and seeds as the staying-to-shoot head-to-head (Hero v Hero, seed 1, scenarios mix), each played
twice. One side plays branch `claude/project-thread-dnukaz` at `949ddcd` with the whole `shots-over-turns` group on (9 tags, including the
two new ones, THREAT OVER THE TURNS and THREAT TO WORN DOWN); the other side has the group switched off = main 8a44e6692.
tk-mine: changes on for Mine; tk-opp: changes on for Opponent. All 288 games ended; no findings, no stalls; every part's rules-off list named
all 9 tags for the right side. Main's side wrote **no** rows of the switched-off tags (0.00 a game): the switch leak of the last batch is gone.
Figures from compare-batches.py with the corrected first-round-won reading (407077ff). The shot and missile analysis scripts skip pair
L1731 (286 games) as before.

## 1. Morten's five headline numbers

| # | Number | **With the changes** | **Main** | Difference | Last batch (difference) |
| --- | --- | --- | --- | --- | --- |
| 1 | VP margin per game | **+52** | -52 | **+52 ±104** (paired over 144 pairs) | +65 ±101 |
| 2 | First round won when charging | 72% | 72% | 0 | 0 (72% v 72%) |
| 3 | Net points per charged fight | +84 | +78 | +6 | +10 |
| 4 | Points lost per game | 753 | 771 | -17 ±67 | -39 ±64 |
| 5 | Free units caught in flank or rear (per game, lower is better) | 0.59 | 0.66 | -0.07 | -0.07 |

W/D/L of the changed side 127 / 47 / 114; pairs where it is ahead over both games 72, behind 69. Going first +69 ±218, second +35 ±206.
As Mine -28, as Opponent +133: the side split is the lists, the pairing cancels it.

Diagnostics (not targets):

| | With the changes | Main |
| --- | --- | --- |
| Charges that made contact a game | 3.9 | 3.7 |
| Points that never fought | 36% | 34% |
| Lone characters that fought | 77% | 80% |
| Joined characters whose unit fought | 41% | 47% |

## 2. Who gained: gunline v offensive armies

Gunline = the same 49 army-games as in the last batch (the armies the framework played defensively in head-to-head 2). Paired, the same
army with the changes minus as main:

| Set | Army-games | Changes minus main, per army-game | Better / worse | Last batch |
| --- | --- | --- | --- | --- |
| Gunline armies | 49 | **+196 ±322** | 26 / 23 | +13 ±317 |
| Other armies | 239 | +86 ±163 | 118 / 115 | +153 ±159 |
| All | 288 | +105 ±146 (= +52 a game) | 144 / 138 | +129 ±142 |

| Set | VP margin of that army | Kills VP | Objectives VP | Points lost | Enemy kills VP | Enemy points lost |
| --- | --- | --- | --- | --- | --- | --- |
| Gunline, with the changes | -235 ±338 | 773 | 556 | 800 | 823 | 715 |
| Same gunline, as main | -431 ±351 | 707 | 488 | 779 | 818 | 656 |
| Other, with the changes | +111 ±166 | 836 | 578 | 744 | 795 | 782 |
| Other, as main | +25 ±164 | 818 | 559 | 769 | 826 | 773 |

The gain moved from the offensive armies to the gunlines this time. Both bands are far wider than either swing, so read it as "no
proven change", not as a trade.

## 3. VP by source (per game, changed side v main)

| Source | With the changes | Main | Difference (paired) |
| --- | --- | --- | --- |
| Kills | 825 | 800 | +25 ±65 |
| Objectives | 574 | 547 | +27 ±44 |
| Leaders | 57 | 57 | 0 |
| Units lost | 5.0 | 5.1 | -0.1 |
| Points lost | 753 | 771 | -17 ±67 |

## 4. The top killer (what the fix was for)

Top killer = the enemy unit that took most of this side's points in fights (read after the game). "Free" = alive, on the table, not in a
fight, not inside a unit, when the shot was fired. Same script on both batches.

| War machine shots | This batch: changes | This batch: main | Last batch: changes | Last batch: main |
| --- | --- | --- | --- | --- |
| Top killer free when the shot was fired | 67% | 68% | 68% | 70% |
| **Shot at it when it was free** | **26%** | **30%** | 25% | 30% |
| Gunline armies: shot at it when free | 22% | 30% | 26% | 28% |
| Shooting units: shot at it when free | 39% | 40% | 42% | 38% |
| Points destroyed by war machines a game | 47 | 53 | 43 | 50 |

What the fix changed, and why it is not enough:

- **The figure grew as meant.** What the shot's row says the top killer will take: median 228 VP now, against 117 VP before the fix. What
  it actually took: median 420 VP. So the figure went from about a third to about half of the truth.
- **The share of it one shot claims stays small.** A war machine shot's THREAT IN THE KILL row at the top killer is worth median 13 VP,
  at another target median 11 VP. That is too small a gap to change the target: 27 of 630 war machine rows changed the shot, 8 of them
  onto the top killer.
- In plain words: the gun now knows the killer is dangerous, but still prices one shot at it at about the same as a shot at anything else.

## 5. The two new tags (and the other seven)

They were on together, so their VP effect is **not separable** in this batch; what can be read is how often each fired and what its
changed choices claimed against what they won. Rows = hidden OpponentRule rows a game on the changed side.

| Item | Rows a game | Changed the choice a game | Jobs followed up | Happened | Planned v won a job | Changed jobs: happened, planned v won |
| --- | --- | --- | --- | --- | --- | --- |
| STAY WORTH | 15.2 | 0.91 | 1,623 | 55% | 63.9 v 66.2 | 33% of 172, **71.1 v 37.2** |
| BEST MOVE FOR SHOOTERS | 0.89 | 0.89 | - | - | - | - |
| THREAT IN THE KILL | 10.0 | 0.43 | 1,226 | 61% | 68.1 v 93.7 | 65% of 100, 39.4 v 77.0 |
| FOCUS OVER TURNS | 0.96 | 0.48 | 221 | 76% | 12.6 v 60.7 | 79% of 97, 10.3 v 52.7 |
| MISSILES IN THE PLAN | 0.62 | 0.02 | 15 | 80% | 97.5 v 65.4 | 67% of 6 |
| FACE THE CAST | 0.04 | 0.04 | - | - | - | - |
| WIZARD FRONT RANK | 0.01 | 0.01 | - | - | - | - |
| **THREAT OVER THE TURNS** (new, A) | 8.0 | **0.29** | 1,182 | 61% | 70.3 v 94.8 | 64% of 76, 33.3 v 73.4 |
| **THREAT TO WORN DOWN** (new, B) | 9.7 | **0.69** | 1,214 | 61% | 68.7 v 94.4 | 69% of 162, 17.2 v 96.2 |

- THREAT TO WORN DOWN changes about 0.7 choices a game, OVER THE TURNS 0.3. Their changed jobs won more than they claimed, so they are not
  over-reaching; they are simply too small to move the guns (section 4).
- STAY WORTH still over-claims where it changes a choice (71 v 37 VP), as last batch (63 v 31).
- The last three items still almost never decide anything.

## 6. Missiles, marches, stance, jobs

### Missiles tried (target 50% of the army's missiles each round)

| Missiles tried each own turn | With the changes | Main |
| --- | --- | --- |
| All missile wizards | 33% | 30% |
| ...when they could be (not in combat, slain, fleeing, off table) | 49% | 45% |
| **Fighting wizards** (monster, chariot, monstrous mount) | 29% | 24% |
| - round 1 | 20% | 22% |
| - rounds 2+ | 32% | 25% |
| **Other wizards** | 36% | 36% |
| - round 1 | 34% | 30% |
| - rounds 2+ | 37% | 37% |
| Magic missiles cast a game | 1.5 | 1.4 |
| Wounds by magic missiles a game | 2.7 | 2.4 |
| Points destroyed by magic (all spells) a game | 63 | 57 |

Last batch: 34% v 31%. Same small rise; still far from 50%.

### Shots given up to marching

| | With the changes | Main | Last batch |
| --- | --- | --- | --- |
| Marches by shooters and missile wizards, all armies (286 games) | 457 | 623 | 477 v 596 |
| ...with a target already in range before the march | 206 | 322 | 202 v 292 |
| Gunline armies: marches by shooters | 143 | - | 149 v 184 |

About a quarter fewer marches that gave up shots, as last batch.

### Stance and jobs

| | With the changes | Main |
| --- | --- | --- |
| Turns the army played defensive | 17% | 18% |
| Shoot jobs: count, happened, planned v won a job | 2,054, 62%, 47.2 v 76.8 | 1,851, 60%, 6.2 v 71.9 |
| Charge jobs | 1,172, 60%, 102.9 v 93.8 | 1,157, 57%, 102.9 v 91.3 |
| Close-in jobs | 1,426, 29%, 68.5 v 31.6 | 1,382, 26%, 58.0 v 25.5 |
| Advance jobs | 3,465, 16%, 24.4 v 27.0 | 3,578, 18%, 20.3 v 27.1 |
| Hold jobs | 1,233, 34%, 65.7 v 0 | 1,270, 36%, 64.2 v 0 |

## 7. Other KPIs, side by side

| | With the changes | Main |
| --- | --- | --- |
| Shots by shooting units a game | 9.9 | 9.3 |
| Points destroyed by shooting units a game | 55 | 56 |
| War machine shots a game | 4.0 | 4.1 |
| Charged units hit only in a flank or rear | 46% | 48% |
| Turned to face a threat (FACES THE THREAT) a game | 1.38 | 1.52 |
| Stood instead of an exposed job (SAFER THAN THE JOB) a game | 0.67 | 0.88 |
| Joint charges a game | 0.4 | 0.5 |
| Charge objectives carried out | 49% | 46% |
| Points destroyed in combat a game | 396 | 378 |
| Points run down a game | 107 | 104 |
| Net per 100 charger points, damage counted | +29.9 | +27.4 |
| Charges in the sweet spot 55-75% (count) | 72 | 60 |
| Charged fights on a top-3 enemy unit | 192 | 180 |

All KPIs: kpis-changes-v-main.md (pooled per side); game by game: compare-all.md.

## 8. What this means

- Two batches, same pairs, same answer: about +50 to +65 VP a game, inside the noise. Pooled over both (576 games) it is about +58 ±72 (a little
  optimistic, since the same pairs repeat), still inside the noise, but every one of Morten's five numbers points the same way in both batches.
- The top-killer fix did what its figure was meant to do (the threat counted is twice as big), but it does not turn the guns: the
  per-shot share stays near a shot at anything else. Getting the guns onto the killer needs the shot to be priced at the share of the
  killer's damage it prevents, not at a few VP.
- No warning this time: the switch leak is gone (no rows on main's side).

## Files

- Parts: tk-mine-1..4, tk-mine-2b / tk-mine-3b (the last pairs of the two slow parts, run by the owner; the 9 pairs both ran use mine-3's
  games), tk-opp-1..4. counts.log: part counts as reported.
- compare-all.md (A = changes as Mine, B = changes as Opponent), kpis-changes-v-main.md (pooled to changes / main).
- Replays: branch `claude/project-thread-21i2b8` at c685e5547 carries deploy/sim-replays/tk-h2h-mine-949ddcd and tk-h2h-opp-949ddcd
  (288 games, on-site.txt set to these two, earlier batches kept). Not pushed to main.
