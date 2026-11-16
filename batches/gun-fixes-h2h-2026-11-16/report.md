# Shooting plan with the gun fixes: head-to-head against main, shooting-heavy pairs (2026-11-16 afternoon)

**Verdict: cannot tell at this sample, and nothing points to an improvement. The side with the full shooting plan and the four
gun fixes is behind by 33 VP a game, give or take 100 VP. This morning, on the same pairs and seeds without the gun fixes, the plan
was ahead by 74 ±107. Today minus this morning, pair by pair, is -107 ±142: also noise. Across the three shooting-plan batches
(-19, +74, -33) the plan averages about +7 VP a game: no sign that it plays better than main. The gun fixes fired (1-3 times a game)
but changed little you can see: guns shot about as often, killed about as much and were blocked by their own units about as often
as main's.**

## What was played

- **Plan side**: branch `claude/project-thread-iol9md` at `0533c462` = main c7c800290 + shooting plan + target fixes + the four gun
  fixes (gun-figures, gun-mask, gun-view, gun-threat), everything on.
- **Main side**: the same build with `shooting-plan, target-fixes, gun-figures, gun-mask, gun-view, gun-threat` switched off for that
  side, which plays as main. Checked: main's side wrote none of the plan's or the gun fixes' rows in 288 games.
- Hero v Hero (script opponent both sides), seed 1, scenarios mix, no Haiku. The **same 144 shooting-heavy DKTC pairs and seeds as
  this morning** (/mnt/project-files/shooting-fixes-h2h-2026-11-16/), each played twice (plan as Mine, then as Opponent): 288 games,
  all ended, 0 failed, 0 sim-bug findings.

## 1. Morten's five headline numbers

| # | Number | **Plan + gun fixes** | **Main** | Difference | This morning (plan, no gun fixes v main) |
| --- | --- | --- | --- | --- | --- |
| 1 | VP margin per game | **-33** | +33 | **-33 ±100** (paired over 144 pairs) | +74 ±107 |
| 2 | First round won when charging | 74% (524 of 709) | 72% (518 of 715) | +2 points | 71% v 71% |
| 3 | Net points per charged fight | +100 | +96 | +4 | +92 v +92 |
| 4 | Points lost per game | 675 | 687 | -12 ±63 | 720 v 751 |
| 5 | Free units caught in flank or rear (per game, lower is better) | 0.42 | 0.47 | -0.05 | 0.51 v 0.56 |

W/D/L of the plan side 112 / 65 / 111; pairs ahead over both games 69, behind 75. Plan going first -77, going second +7 (each ±180).
Plan as Mine -281 and as Opponent +216 is the lists (the heavy lists play Mine more often); the pairing cancels it.

**Did the gun fixes add anything?** Today minus this morning, pair by pair: **-107 ±142**, better in 63 pairs, worse in 81. The two
batches' games went separate ways from the first decision (pair results correlate 0.05), so pairing them does not narrow the band.
Read: no sign the gun fixes helped; a 288-game batch cannot show a change smaller than about 100 VP either way.

Diagnostics (not targets):

| | Plan + gun fixes | Main |
| --- | --- | --- |
| Charges that made contact a game | 2.9 | 2.9 |
| Points that never fought | 50% | 49% |
| Lone characters that fought | 62% | 62% |
| Joined characters whose unit fought | 30% | 34% |

## 2. The gun fixes: how often each was used (hidden rule count)

Rows the plan side wrote (main writes none). "Changed" = the fix picked another option than it would have without it.

| Fix | Rows a game | Changed a game | What it does |
| --- | --- | --- | --- |
| GUN FIGURES | 3.0 | (figure only) | guns that roll to hit (Organ Gun, Helblaster, bolt throwers) judged by what they really do |
| GUN THREAT | 2.1 | 0.20 | a gun prefers the unit that can destroy it next turn |
| GUN VIEW | 1.2 | 0.52 | a war machine deployed where it sees the best target |
| GUN MASK | 0.5 | 0.04 | a move that blocks own guns' sight pays for it |

Reading: gun-view moved a war machine's deployment about once every two games; gun-mask almost never changed a move (once in 25
games); gun-threat changed a gun's target once in five games.

## 3. War machines, the top killer and sight

| Per game and side | Plan + gun fixes | Main | This morning (plan v main) |
| --- | --- | --- | --- |
| War machine shots | 7.7 | 7.8 | - |
| Points destroyed by war machines | 100 | 105 | 92 v 90 |
| Points destroyed per war machine shot | 13.0 | 13.4 | 14.8 v 14.6 |
| Points destroyed by other shooting units | 101 | 93 | 105 v 93 |
| Points destroyed by magic | 29 | 31 | 43 v 30 |
| Own war machines destroyed in close combat (charged / run down) | 0.23 | 0.23 | - |
| Own war machines lost in all | 0.75 (215 of 544) | 0.68 (197 of 544) | - |
|   of which fled off the table | 0.10 | 0.06 | - |
|   of which own misfires | 0.13 | 0.15 | - |

Top killer (the enemy unit that took most of this side's points in fights) and the enemy's dearest unit, read from the new GUN
SIGHT rows (one per gun at the end of each Movement phase; open = in range, not in a fight, in sight):

| War machine shots | Plan + gun fixes | Main |
| --- | --- | --- |
| Top killer open to the gun | 9% (185 of 1,984) | 10% (186 of 1,893) |
| ...shot when open | **35%** (65 of 185) | **45%** (83 of 186) |
| Top killer in range but out of sight (of open + out of sight) | 30% (78 of 263) | 30% (81 of 267) |
| ...blocked by an own unit | 44 | 60 |
| Dearest enemy unit open to the gun | 56% (1,296 of 2,312) | 57% (1,332 of 2,324) |
| ...shot when open | 39% | 42% |
| ...not open because an own unit was on the line | 12.6% | 14.6% |

Reading: this morning's finding said 37% of the top killer's misses were "in range but not in sight". With the new measure it is 30%
on both sides: gun-mask and gun-view did not open up the guns' sight (own units block 12.6% v 14.6% of the dearest-unit lines, a
small gap). The plan's guns shoot an open top killer less often than main's (35% v 45%, small numbers): the plan spreads shots by
its own figures, and gun-threat sends some at whatever threatens the gun.

Older measure (top killer free = alive, not in a unit or fight), for comparison with this morning: war machine shots at the top killer
when free 23% v 23% (morning 20% v 24%); top killer dead by round 3 7% v 10%; dead by the end 26% v 29%.

## 4. Movement choices (diagnostics)

| | Plan + gun fixes | Main |
| --- | --- | --- |
| Took the best spot by worth of all it weighed | 63% | 63% |
| Moved (did not stay) | 45% | 45% |
| Worth given up against the best spot (VP a move) | 18.3 | 18.3 |
| Stayed although a move was worth more | 35% | 33% |
| Set-ups followed by a charge job on that target next turn | 12% | 12% |
| Volleys lost to marching a game | 2.33 | 3.04 |
| Magic missiles tried each own turn (target 50%) | 35% | 35% |
| Turns the army played defensive | 29% | 26% |

The one clear difference, as in every shooting-plan batch: the plan side stays to shoot instead of marching (0.7 fewer volleys lost
a game).

## 5. VP by source and army type

| Per game | Plan + gun fixes | Main |
| --- | --- | --- |
| Kills VP | 724 | 717 |
| Objectives VP | 560 | 598 |
| Leaders VP | 48 | 49 |
| Units lost | 4.7 | 4.7 |

The plan side loses its ground on objectives (-38 VP a game), not on kills. Same army with the plan minus without, by kind of army
(army-games, twice the game scale): shooting-heavy armies -69 ±195, the others -89 ±207.

## 6. Sim bugs

- 0 findings. Two warnings, both the same kind: "DRIVER STOOD IN" on accepting a challenge ("Refuses the challenge" stalled the
  computer): L0916 scenario 4 (plan as Mine, State Troops champion), L1516 scenario 4 (plan as Opponent, Silver Helms champion).
  Not checked whether this is known.

## Verdict

**Improves play: cannot tell at this sample, and the figures lean to no.** Margin -33 ±100 (morning without gun fixes +74 ±107,
11-15 night -19 ±92). The five headline numbers are level within noise (first round won +2 points, net per fight +4, points lost -12,
flank caught -0.05, all small and in the plan's favour), but the VP margin is not, because the plan side scores 38 VP less on
objectives. The gun fixes did their mechanical job (fired 1-3 times a game, gun-view moved half the games' deployments) but did not
change what the guns shot, how much they killed, or how often own units blocked them.

## Files

- Parts: mine-1..4 (plan as Mine), opp-1..4 (plan as Opponent); counts.log; HOW-TO-RUN-A-PART.md.
- compare-all.md (compare-batches.py on the merged batches); scripts/ (h.py margin, vsmorning.py the pair-by-pair comparison with
  this morning, wm.py war machines, leak2.py switch check and rule counts, tk.py / extra.py from this morning's batch).
- Replays: branch `claude/project-thread-xtvkre` at `e8401db3f` (from main b15083ae) carries deploy/sim-replays/gf-h2h-mine-0533c46 and
  gf-h2h-opp-0533c46 (288 games, on-site.txt set to these two). Not pushed to main.
- Game logs archived to MortenFISHBACK/OldWorldSimulations (see the thread for the result); nothing deleted.
