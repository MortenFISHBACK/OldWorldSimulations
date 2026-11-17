# Simpler pricing: head-to-head against main (2026-11-16/17)

**Verdict: the simpler pricing is at least as strong as main, and ahead on the number: +44 VP a game, give or take 98 VP.**
That is above the +30 line, so by the rule set beforehand it is kept, and it would also become the bar the five-action framework is
tested against. But ±98 means it is not proven better than main; "not worse, maybe better" is the honest read.
The gain comes mostly from objectives (+30 VP a game), not from fighting.

Batch: 288 games, the same 144 DKTC pairs and seeds as the earlier head-to-heads (Hero v Hero, seed 1, scenarios mix), each pair played
twice so both sides get the changes. Changed side: branch `claude/project-thread-7uh7a9` at `779e2613` with all seven switches on
(advance-worth, idle-cost, risk-once, one-fight-formula, cover-once, chaff-in-the-move, one-objective-formula). Other side: all seven
off = main e8dd114c3. 288 of 288 games ended, no time-limit stops. No row of the seven rules was written by the switched-off side (no leak).
Part 1's container restarted three times, so its games were played by me (10) and part 3 (17 + 9); part 2's second half by me.

## 1. Morten's five headline numbers

| # | Number | **Changes on** | **Main** | Read |
| --- | --- | --- | --- | --- |
| 1 | VP margin per game | **+44** | -44 | **+44 ±98** (paired over 144 pairs); pairs ahead 76, behind 68 |
| 2 | First round won when charging | 73% | 74% | same |
| 3 | Net points per charged fight | +81 | +88 | a little lower, within noise (damage counted: +84 v +90) |
| 4 | Points lost per game | 703 | 710 | 7 fewer, same |
| 5 | Free units caught in flank or rear (per game, lower is better) | 0.59 | 0.61 | same |

W/D/L of the changed side 126 / 48 / 114. Going first +125, going second -38. Earlier batches for comparison: charge worth -7 ±110,
combined charge + shooting -31 ±95, shooting plan -19 ±92.

Diagnostics (not targets): charge contacts a game 3.5 v 3.2; charged fights 866 v 823; points that never fought 40% v 40%;
first charge contact made in 52% of games v 48%.

## 2. Where the VP came from (per game)

| Source | Changes on | Main |
| --- | --- | --- |
| Objectives | **595** | 565 |
| Kills | 758 | 745 |
| Leaders | 53 | 51 |
| Units lost | 4.7 | 4.8 |

## 3. How often the seven rules fired (changed side only)

"Changed the pick" = the unit did something else than it would have without the rule.

| Rule | Rows a game | Changed the pick a game |
| --- | --- | --- |
| ADVANCE WORTH | 5.0 | 0.84 |
| IDLE COST | 17.3 | 0.59 |
| RISK ONCE | 3.7 | 0.73 |
| ONE FIGHT FORMULA | 8.8 | 0.73 |
| COVER ONCE | 7.3 | 1.13 |
| CHAFF IN THE MOVE | 1.4 | 0.88 |
| ONE OBJECTIVE FORMULA | 2.3 | 0.05 |

Together they changed about 5 picks a game. The batch cannot split the +44 between the seven rules. Older rules now fire less on the
changed side, e.g. BEST FIRST 1.1 v 4.3 a game and COUNTER-CHARGE COVER 0 v 9.1 (replaced by COVER ONCE) - fewer layers deciding.

## 4. Jobs claimed v happened

| Job | Changes on: jobs, happened, planned v won VP a job | Main |
| --- | --- | --- |
| charge | 899, 58%, 81 v 96 | 630, 59%, 82 v 90 |
| close in | 1397, 24%, 52 v 25 | 941, 25%, 52 v 30 |
| advance | 2606, 16%, **10 v 28** | 2321, 17%, 18 v 28 |
| shoot | 1087, 58%, 8 v 59 | 2032, 62%, 14 v 82 |
| hold | 952, 38%, 64 v 0 | 1076, 34%, 59 v 0 |
| support | 1333, 90%, -5 v 0 | 1023, 89%, -4 v 0 |
| join | 204, 96%, 46 v 0 | 130, 94%, 28 v 0 |

- Advances no longer promise more than they earn (10 v 28; before 18 v 28).
- The changed side takes many more charge jobs (899 v 630) and fewer shoot jobs (1087 v 2032), but it shoots just as much: points
  destroyed by shooting units 70 v 66, war machines 47 v 42, magic 61 v 55 a game.

**Risk claimed v points lost** (JOB RISK rows, summed over every job picked; a unit can carry risk in more than one turn, so this is a
rough check): changes on claim 670 VP of risk a game and lose 703 points; main claims 830 and loses 710. The changed side's risk figure
is much closer to what it really loses (main counted its risk about a sixth too high).

## 5. Other KPIs side by side

| Measure | Changes on | Main |
| --- | --- | --- |
| Charges declared / contacts a game | 4.8 / 3.5 | 4.8 / 3.2 |
| Joint charges a game | 0.3 | 0.3 |
| Close-in set-ups that charged that target next turn | 14% | 16% |
| Points destroyed in combat a game | 346 | 341 |
| Points run down a game | 76 | 91 |
| Idle units a game | 1.5 | 1.4 |
| Points that never moved of their own a game | 236 | 231 |
| Turned to face a threat / stood instead of an exposed move a game | 1.6 / 0.8 | 1.7 / 1.0 |
| Magic missiles tried each own turn | 36% | 32% |
| Turns played defensive | 17% | 16% |

Full tables: kpis-on-v-off.md (changes on / main) and compare-all.md (A = mine arm, B = opp arm).

## 6. What this means (warnings, not plans)

- By the rule set beforehand the result is in the top band (+44 > +30): keep it, and test five-action against it. The noise (±98) is
  as large as in every batch this week, so "better than main" is likely but not shown.
- Idle cost fires 17 times a game but idle units did not drop (1.5 v 1.4): it mostly re-ranks moves of units that were moving anyway.
- One objective formula almost never changes a pick (0.05 a game); the objective gain more likely comes from idle cost and the
  advance figures than from that rule.

## Sim bugs

- S-e7050e (new), game L3033 (part mine-2b): Glade Riders of the switched-off side overlap impassable terrain by 2.52", noticed late
  in turn 6 (set-up check). One game in 288.

## Files

- Results: mine-1a, mine-1b, mine-1c, mine-2, mine-2b, mine-3, mine-4, opp-1..4 (until archived); counts.log.
- Replays: work branch `claude/project-thread-3yh4lo` at `10848a676` (11 batch folders os-h2h-{mine,opp}-779e261-*; on-site.txt lists
  them). Not on main.
- scripts/: h.py (margin), rules7.py (the seven rules and JOB RISK), plans.py (jobs), remap.py, merge.py.
