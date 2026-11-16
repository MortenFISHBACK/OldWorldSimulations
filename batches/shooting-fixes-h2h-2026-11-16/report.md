# Shooting plan with the target fixes: head-to-head against main, shooting-heavy pairs (2026-11-16)

**Verdict: no proof either way. The side with the fixed shooting plan is ahead by 74 VP a game, give or take 107 VP: inside the noise.
Last night the plan without the fixes was -19 ±92 (on other pairs). The fixes did what they were built for: the plan no longer
prefers cheap targets, its claims are half as inflated, and units with missiles join charges as often as main's (more, in fact).
But the guns still do not go at the enemy's top killer more than main's do. The finding expected a prize of 15-25 VP a game; a
288-game batch (band ±107) cannot show a prize that size, and this one does not.**

## What was played

- Option 4 of the finding (Morten 05:43: "4. Yes"). The finding does not name the two sides, so this is the comparison that decides
  landing: **the full shooting plan with the three fixes** (every wound counts, honest threat, one yardstick) on one side, **main**
  on the other (switches `shooting-plan` and `target-fixes` off for that side).
- Build: branch `claude/project-thread-tvghcc` at `43941594`. Hero v Hero (static-static), seed 1, scenarios mix.
- **144 shooting-heavy DKTC pairs**, each played twice (plan as Mine, then plan as Opponent), 288 games, all ended.
  Shooting-heavy list = 3+ war machines or 30%+ of its points in shooting units and war machines (wizards not counted):
  9 of the 35 DKTC lists (Chaos Dwarfs Maltese, Dwarfs Hannani and Thorgrizzly, Empire Windfeld, Pierce and Christensen,
  High Elves Malte Dueholm, Ogres PJ Kuczynski, Tomb Kings Holmboe). Every pair has at least one: all 36 heavy-v-heavy pairs and
  12 other opponents per heavy list. These are **not** last night's pairs, so the two results are side by side, not paired.
- No switch leak: main's side wrote none of the plan's rows in 288 games.

## 1. Morten's five headline numbers

| # | Number | **With the fixed plan** | **Main** | Difference |
| --- | --- | --- | --- | --- |
| 1 | VP margin per game | **+74** | -74 | **+74 ±107** (paired over 144 pairs) |
| 2 | First round won when charging | 71% (566 of 799) | 71% (577 of 816) | 0 |
| 3 | Net points per charged fight | +92 | +92 | 0 |
| 4 | Points lost per game | 720 | 751 | -31 ±67 |
| 5 | Free units caught in flank or rear (per game, lower is better) | 0.51 | 0.56 | -0.05 |

W/D/L of the plan side 126 / 61 / 101; pairs ahead over both games 73, behind 71. Going first -7, going second +156 (each ±200+).
Plan as Mine -231 and as Opponent +380 is the lists, not the plan (the lower-numbered lists, where the heavy ones are, play Mine);
the pairing cancels it.

Last night, plan without the fixes, other pairs: -19 ±92; first round won 69% v 73%; net per fight +77 v +80; lost 761 v 749.
The drop in first round won is gone.

Diagnostics (not targets):

| | Fixed plan | Main |
| --- | --- | --- |
| Charges that made contact a game | 3.3 | 3.35 |
| Points that never fought | 43% | 43.5% |
| Lone characters that fought | 70% | 68% |
| Joined characters whose unit fought | 40% | 41% |

## 2. The finding's four numbers

| | Fixed plan | Main | Finding (last night: plan v main) |
| --- | --- | --- | --- |
| Points destroyed per war machine shot | 14.8 | 14.6 | about 13-18 by target |
| Share of war machine shots at units under 150 points | **34%** | 35% | 39% v 32% |
| What the plan says a shot adds v points it really destroyed: war machine shot | 86 VP v 15 | - | 103 v 20 |
| ...the same, other shooting per volley | 45 VP v 6 | - | 52 v 7 |
| What a shoot job claimed (mean VP) | 23 | 11 | 61 v 14 |
| Joint charges with a unit that has missiles | **68** | 55 | 54 v 78 |
| All joint charges (fights with 2+ chargers) | 122 | 119 | 111 v 139 |

Reading: fix 1 and 2 took the plan off cheap targets (34% now, as main). Fix 3 halved what shoot jobs claim against main
(2x main's figure, was 4x), and missile units now join charges at least as often as main's. The plan's own "this shot adds" figure
(the target choice, which keeps threat and wound shares on purpose) still reads 5-7 times the points a shot really destroys: warning,
not a proposal, that figure is still not an honest forecast of points, only a ranking.

War machine shots by target (points destroyed per shot): biggest hammer 11.0 v 12.6, units 150+ 16.8 v 16.5, under 150 14.6 v 13.6.

## 3. The guns and the top killer

Top killer = the enemy unit that took most of this side's points in fights (read after the game). Free = alive, not in a unit,
not in a fight, when the shot was fired.

| | Fixed plan | Main | Last night (plan v main) |
| --- | --- | --- | --- |
| **War machine shots at the top killer when it was free** | **20%** (216 of 1,067) | 24% (248 of 1,024) | 24% v 28% |
| **Magic missiles at the top killer when it was free** | 23% (61 of 264) | 20% (47 of 234) | 18% v 28% |
| Other shooting at the top killer when free | 23% (503 of 2,171) | 26% (479 of 1,834) | 22% v 32% |
| Top killer dead by round 3 | 5% (11 of 231) | 4% (10 of 225) | 6% v 6% |
| Top killer dead by the end | 27% | 24% | 28% v 23% |
| Enemy's dearest unit dead by round 3 | 12% | 12% | 10% v 14% |
| Shots at enemy war machines | 5% of war machine shots | 6% | 5% v 5% |

Reading: the plan still spreads its war machine shots over the 150+ point units, not the eventual top killer. That fits the
finding: nobody knows the top killer in advance, and a shot at any dear unit is worth about the same.

## 4. Shooting, magic and marches

| Per game | Fixed plan | Main |
| --- | --- | --- |
| Points destroyed by shooting units | 105 | 93 |
| Points destroyed by war machines | 92 | 90 |
| Points destroyed by magic (all spells) | 43 | 30 |
| **Volleys lost to marching** (shots not taken because the unit marched) | **2.45** | 3.07 |
| Missiles lost to marching | 0.57 | 0.61 |
| Magic missiles tried each own turn (target 50%) | 31% | 32.5% |

Staying to shoot instead of marching shows again (third batch in a row).

## 5. VP by source, stance, jobs

| Per game | Fixed plan | Main |
| --- | --- | --- |
| Kills VP | 790 | 753 |
| Objectives VP | 601 | 561 |
| Leaders VP | 57 | 58 |
| Units lost | 5.0 | 5.2 |
| Turns the army played defensive | 27% | 27% |

Same army with the plan minus without it, by kind of army (army-games; this is twice the game margin's scale):
shooting-heavy armies +147 ±214 (171 army-games), the others +151 ±223 (117). The plan helps (or not) both kinds alike.

Jobs: shoot jobs claimed 23 VP v 11 (section 2); "happened" for shoot jobs reads 0.0 on this build for both sides, so that
column is not usable here. Charge jobs declared 71-79% on both sides.

## 6. Sim bugs (none fixed here)

- **S-228177, new**: L0322 (opp-1, plan on Opponent): Tomb King (Armour of Destiny) overlaps impassable terrain by 0.14", seen in
  turn 6. Not checked whether it is the refused-join cause already fixed on main (S-67c2af, f3d2be2c); this branch lacks that fix.
- Nothing else: 0 stalls, 0 failed games.

## Files

- Parts: mine-1..4, opp-1 (first 18 pairs, run late), opp-1b (last 18 pairs of opp-1, run by the owner), opp-2..4.
- Replays: branch `claude/project-thread-2yjopn` at `21e4d720` (from main 4af290e8) carries deploy/sim-replays/sf-h2h-mine-4394159
  and sf-h2h-opp-4394159 (288 games, on-site.txt set to these two). Not pushed to main.
- Figures: compare-all.md (compare-batches.py, game by game); scripts/ (h.py margins, tk.py top killer and army split, extra.py
  marches and characters, leak.py switch check, classify-lists.py the heavy lists, from-finding/ the finding's d, h, f scripts;
  2 of 288 games could not be matched to their unit records there: L2122 mine-2, L1722 opp-2).
