# Five actions against simpler pricing: head-to-head (2026-11-17)

**Verdict: five-action is clearly worse than the simpler pricing: -279 VP a game, give or take 99 VP.**
The whole ± range is far below zero, so this is a real loss, not noise. Five-action is behind in 105 of 144 pairs and ahead in 39,
and it loses whichever side of the table it plays and whether it goes first or second. By the rule set beforehand the simpler
pricing stays the bar; five-action in this form should not go on.

The main reason in one line: **five-action promises more than it earns.** It claims about 1.5 times the gain of the other side
(3,176 v 2,174 VP a game, summed over the jobs it picks) and then scores less. It charges a third less, overrates the charges it
does take (planned 150 VP a charge, won 101), holds objectives less, and loses more points.

Batch: 288 games, the same 144 DKTC pairs and seeds as the earlier head-to-heads (Hero v Hero, seed 1, scenarios mix), each pair
played twice so both sides get five-action. Both sides: branch `claude/project-thread-d723p0` at `8a943319` (five-action branch gkwq7b
9320f692 plus two fixes, below) with the simpler-pricing switches on. One side also had five-action on; the other had it off
(`--rules-off five-action@side`). 288 of 288 games ended; no crashes, no time-limit stops, no sim bugs found.

## 1. Morten's five headline numbers

| # | Number | **Five-action** | **Simpler pricing** | Read |
| --- | --- | --- | --- | --- |
| 1 | VP margin per game | **-279** | +279 | **-279 ±99**; pairs ahead 39, behind 105 |
| 2 | First round won when charging | 71% | 76% | worse |
| 3 | Net points per charged fight | +82 | +91 | worse |
| 4 | Points lost per game | 720 | 579 | **141 more lost** |
| 5 | Free units caught in flank or rear (per game, lower is better) | 0.71 | 0.49 | worse |

W/D/L of the five-action side 83 / 62 / 143. Margin with five-action as Mine -348, as Opponent -209; going first -280, second -277.

## 2. Where the VP came from (per game)

| Source | Five-action | Simpler pricing |
| --- | --- | --- |
| Objectives | **498** | 638 |
| Kills | **622** | 756 |
| Leaders | 44 | 49 |
| Units lost | 4.9 | 3.9 |

Diagnostics (not targets): charges declared 3.2 v 4.8 a game; fights charged into 2.2 v 3.0; points run down 63 v 86; lone objective
holders 2.5 v 3.3 player turns; idle units 1.8 v 1.6; points that never fought 46% v 46%.

## 3. Claims v what happened (the computer's own logged figures)

| Job | Five-action: jobs, happened, planned v won VP a job | Simpler pricing |
| --- | --- | --- |
| charge | 634, 62%, **150 v 101** | 965, 61%, 81 v 95 |
| shoot | 1761, 60%, 39 v 72 | 2174, 59%, 16 v 74 |
| move (five-action's move/march/stand) | 8868, 93%, 51 v (not measured) | - |
| advance / close in / hold | - (folded into "move") | 3207 / 1724 / 1476 |
| join | 200, 92%, 40 v 0 | 190, 97%, 35 v 0 |
| support | 59, 68% | 1865, 91% |

- Charges: five-action plans 150 VP a charge and wins 101 (half again too sure); simpler pricing plans 81 and wins 95.
- Risk claimed v points lost (JOB RISK rows, rough check): five-action claims 668 VP of risk a game and loses 720; simpler pricing
  claims 824 and loses 579. Five-action counts its risk too LOW, which fits it losing more.
- Next-turn part (the "B" of the spot sum, x its chance): 1,243 VP a game claimed. This is the part with no outcome to check it
  against, and it is the biggest single reason the claimed total is so high (warning: my reading, not measured).
- Actions picked a game: move 15.4, march 11.8, stand 7.4, shoot 7.3, charge 2.8.

## 4. How often the five-action parts fired (five-action side, per game)

"Changed the pick" = the unit did something else than it would have without that part.

| Part | Rows a game | Changed the pick a game |
| --- | --- | --- |
| FIVE ACTION | 44.6 | 0.50 |
| CHARGE LOSSES | 11.3 | 1.54 |
| FOUR ROUNDS | 2.7 | 0.90 |
| FEATURE BUFFS | 0.9 | 0.24 |
| AFTERMATH IN POINTS | 0.2 | 0.18 |
| GUN MASK | 0.4 | 0.07 |
| FALL BACK GOOD ORDER | 1.9 | 0.03 |
| TIME ON OUR SIDE, RUN DOWN, FALLS SHORT, CHARACTER GUNS, STAND AND SHOOT | 0.2-2.0 | 0.00 |
| LIKELY CHARGE, GETS AWAY CHANCE | 0 | 0 |

"Changed the pick" only counts a part's own row; most of five-action's effect is the whole sum replacing the old jobs, which no row
can isolate. The batch cannot split the -279 between the parts. No five-action row was written by the switched-off side (no leak).

## 5. Two fixes made before the run (branch d723p0)

1. **Five-action was OFF on both sides in every sim** before 8a943319: the test assembly that runs sims switched it off at start-up
   (FiveActionTestDefault). Any earlier sim of the gkwq7b branch played without five-action. Fixed (on under OWWT_SIMULATE=1), with a test.
   The first start of this batch (6d6fc47b) was void for that reason and was thrown away; part 3 spotted it.
2. RUN DOWN was switched by the chaser's side, so the side without five-action borrowed it when deciding hold-or-flee. Fixed, with a test.
   Both commits should go to gkwq7b if five-action is kept for anything.

## 6. What this means (warnings, not plans)

- Five-action as built loses badly to the simpler pricing. It overrates its own moves (above all next turn's "best thing" and its
  charges) and underrates its risk, so it charges less, holds less and loses more.
- The guesses Morten flagged as starting points (next-turn chances 0.5 / 0.25 / 0.10, LikelyMinor 0.25, Hatred 1/4) feed exactly the
  overclaimed parts.
- Fewer support jobs (59 v 1,865) and fewer objective holders: the old layers it bypasses (hold jobs, the 210-pt holder rule, support)
  seem to have been worth points.

## Files

- Results: mine-1, mine-2, mine-3a/3b/3c, mine-4, opp-1..4 (until archived); counts.log.
- Full tables: kpis-five-v-simpler.md (five-action / simpler pricing), compare-all.md (A = mine arm, B = opp arm).
- Replays: work branch `claude/project-thread-d723p0` at `797f7bcd` (10 batch folders fa-h2h-{mine,opp}-8a94331-*; on-site.txt lists them). Not on main.
- scripts/: h.py (margin), rules5.py (parts, JOB RISK), plans.py (jobs), merge.py, remap.py.
