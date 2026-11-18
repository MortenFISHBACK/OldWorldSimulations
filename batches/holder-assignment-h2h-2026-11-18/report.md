# Army-wide objective holders ON v OFF - head-to-head report (2026-11-18)

**Verdict: no gain yet. Stopped by the coordinator at 168 of 288 games** (10:27 UTC), because the known faults stay unchanged on this
head: the table tests "within 6 inches and able" while the game gives an objective to the NEAREST able unit, one object per unit; and
end-of-battle objectives (special feature, Herdstone, baggage) still use the old figure. A fixed head gets a fresh batch.
The assigned marker holder scores its marker that round 65% of the time; the hill holder 24%. Markers gain +28 VP a game, objectives
overall -12 (the gap is in table quarters, which the table does not assign), VP margin -21 ±160 (noise). The cheapest able unit does not score more often (42% v 46%).

Build 95a3d390 (claude/project-thread-bj3s5r, from the overhaul e62ea8a6). Both sides play the overhaul's pricing; the only difference
is `holder-assignment`, off for one side (`@opponent` in mine-1..4, `@mine` in opp-1..4, same pairs both ways). 144 DKTC pairs chosen
so every game has markers or the hill (no A Chance Encounter), seed 1, scenarios mix. Switch side checked in every game: HOLDER
ASSIGNMENT rows on the on side only. Smoke L0103: 4.2 min on v 4.4 min all off.

## Claimed v happened (turn table, on side; scripts/assigned.py)

| Assigned to | Assignments | Claimed (mean VP of the row) | Holder scored it that round |
| --- | --- | --- | --- |
| Marker | 1320 | 69 | 65% |
| The hill | 78 | 128 | 24% |
| Herdstone / special feature / baggage | 171 / 376 / 348 | - | not measured (scored at the end) |

job_claims.py's hold row reads no picks on this head (the build's code-check says it reads the table from 36199b7b on).

## Objectives (scripts/markers.py, scripts/objective_holders.py)

| | ON | OFF |
| --- | --- | --- |
| Marker player-turns scored (nobody 33%; baseline 50%) | 35% | 32% |
| Marker VP a game | 343 | 315 |
| Hill VP a game | 45 | 48 |
| All objective VP a game, ON minus OFF (end-of-battle included) | -12 | |
| Points of the scoring unit, mean (median) | 227 (171) | 220 (164) |
| Scored by a 210+ unit | 38% | 37% |
| Scored by the cheapest able unit alive | 42% | 46% |

## Headline

| | ON | OFF |
| --- | --- | --- |
| Charges declared a game | 3.7 | 3.4 |
| First round won when charging (claimed v happened) | 65% v 76% | 67% v 76% |
| Net points per charged fight | +81 | +77 |
| Points lost a game | 581 | 576 |
| Free units caught in flank/rear a game | 1.25 | 1.27 |
| Risk claimed v points lost next enemy turn | 541 v 407 | 505 v 423 |
| Thinking time | 6.4 min a game, longest 12.8; none timed out, no findings | |

VP margin ON v OFF: **-21 ±160** (56 won, 69 lost, 43 drawn); by source: objectives -12, kills -14, leaders +5. Noise at 168 games.

## Leads (from logs, not checked in code; the build thread's code-check-55.md covers the causes)

- CORRECTED (the build thread checked my end-of-battle lead in code and logs, end-of-battle-check-155.md): special feature, Herdstone and
  baggage together cost the ON side only about 2 VP a game (feature -10 ±22, Herdstone +9 ±11, baggage -4). The end-of-battle gap sits
  in the TABLE QUARTERS (Domination): 199 v 231, -32 ±38 (noise), and the table does not assign quarters at all.
- "Gives up least" does not land on the cheapest unit: more objectives than cheap units, so cheap units are spent on feature/baggage.
- The hill holder rarely gets there (24%).

## Files

Parts mine-1..4 / opp-1..4 (batch.tgz each, 168 games), early-reading-49.md, reading-155.md, scripts/ (sides.py, markers.py, assigned.py).
Game logs KEPT on the mount (coordinator: the build thread still reads them).
