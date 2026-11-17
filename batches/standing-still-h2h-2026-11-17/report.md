# Standing still by numbers against simpler pricing: head-to-head (2026-11-17)

**Verdict: standing still by numbers plays level with simpler pricing, a little ahead: +37 VP a game, give or take 100.**
That is not proof it is better (the range runs from -63 to +137), but it is well inside the "keep if not worse than about -30" band
used for these batches, so by that rule it is **kept**. It kills a little more and loses a little less; objectives come out the same.

Batch: 288 games, the same 144 DKTC pairs and seeds as the five-action and joint-charge batches (Hero v Hero = scripted v scripted,
seed 1, scenarios mix), each pair played both ways. Build `claude/project-thread-3c34nw` at `06f55ceb` (simpler pricing + split log
+ the six standing-still switches). **All 288 games ended**; no engine errors, no stuck games, nothing hit the time limit.
Pairs ahead 72, behind 72.

## 1. Headline

| # | Number | **Standing still ON** | **Simpler pricing** |
| --- | --- | --- | --- |
| 1 | VP margin per game | **+37 ±100** | -37 |
| 2 | First round won when charging | 71% | 73% |
| 3 | Net points per charged fight | +82 | +79 |
| 4 | Points lost per game | 704 | 720 |
| 5 | Free units caught in flank or rear (per game) | 0.59 | 0.59 |

Standing still as Mine -59, as Opponent +133 (both within noise); going first +24, second +50.

## 2. VP by source (per game)

| Source | Standing still ON | Simpler pricing |
| --- | --- | --- |
| Objectives | 571 | 568 |
| Kills | 771 | 742 |
| Leaders | 54 | 47 |
| Units lost | 4.7 | 4.8 |
| Charged fights a game | 3.0 | 3.0 |

## 3. What the switches did (the computer's own rows, per game on the side that had them)

| Switch | Fired a game | Changed the pick a game | VP it added to the figure a game |
| --- | --- | --- | --- |
| TIME ON OUR SIDE (no idle cost while out-shooting) | 14.2 | 2.4 | +244 |
| FALLS SHORT (stay pays only its shortfall) | 10.5 | 1.2 | +158 |
| NEARER NOT NEEDED (move under 1" nearer still serves) | 10.3 | 3.2 | +580 |
| NO FORCED ADVANCE (no job = best spot, not the nearest enemy) | 2.5 | 2.5 | - |
| CHEAPEST HOLDER (objective counts only for the cheapest holder) | 1.4 | 0 | -52 |
| HARD STAY DROPPED (Hard only) | 0.9 | 0 | 0 |

About 9 picks a game changed. The plain idle cost dropped from 17.7 rows a game to 6.0 on the standing-still side.

## 4. Claims against what happened

| | Standing still ON | Simpler pricing |
| --- | --- | --- |
| Units that stayed: the computer's figure for staying (VP) | +39 | +13 |
| Share of moves that stayed | 51% as Mine, 39% as Opponent | the same: 51% and 39% |
| Objective moves made a game | 6.7 | 5.7 |
| Objectives reached a game | 1.95 | 2.25 |
| Points that never fought | 40% | 40% |
| Units over 100 points that earned nothing | 58% | 59% |

What this says: staying now looks worth three times as much to the computer, but units do **not** stay more often, and the units
that stayed earned the same as before (objective VP equal, idle points 248 v 254 a game). The gain came from kills (+29) and
leaders (+6), most likely from NEARER NOT NEEDED and NO FORCED ADVANCE (units go where the figures say instead of walking at the
nearest enemy). CHEAPEST HOLDER fired rarely and never changed a pick, so cheap holders did not change objective play.

Warning (what the tool would do): the "happened" column of the claimed-against-happened table shows 0 for every charge and shot in
this build's logs, so the per-job claims check could not be read this time. Likely the split log changed a line the tool reads;
worth a look before the next batch that needs it.

## 5. Bugs

- Sim bug **S-e67bc6** (new): L0122 King of the Hill, two Tomb Kings overlapping by 0.37" (found in turn 6, on the simpler side).
  Filed by add-sim-replays as a sim finding.
- Batch running: detached (setsid) runs died whenever a part's session went idle; runs as Bash background tasks did not.
  The shared folder hit its file limit mid-batch; games were read from simulation-data instead.

## 6. Where things are

- Replays: branch `claude/project-thread-dluprl` (8 folders ss-mine/ss-opp-06f55ce-p1..p4, on-site list replaced). Not on main.
- Full comparison: compare-all.md in this folder. Logs archived to MortenFISHBACK/OldWorldSimulations (see the thread).
