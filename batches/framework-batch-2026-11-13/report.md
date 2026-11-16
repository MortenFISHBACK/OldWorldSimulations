# Job framework on v off - batch report (2026-11-13)

288 games: the same 144 DKTC games (Hero v Hero, seed 1, scenarios mix; the pairs of the flank-fixes and enemy-forecast batches) played
twice on the framework candidate (claude/project-thread-goduf0 at db7ca9c5d): **on** = every rule on, **off** = the job framework and its
14 single rules switched off (`--rules-off job-framework,stay-weighed,best-first,random-move-by-figures,random-mover-no-promise,
stable-role,wounded-stays-out,best-facing,lost-charge,screen-by-what-it-saves,redirect-by-what-it-stops,shooter-counted-once,
lure-by-what-it-draws,hill-by-its-chance,war-engine-jobs`). Flank fixes and the spears/halberds fix are in both arms.
All 288 games ended; 0 sim findings, 0 stalls; the best-figure guard wrote NO REASON 0.10 times a game and played on.
Full tables: `compare/compare-all.md` (compare-batches.py, same games), `compare/stance.md` (VP by source per stance).

## Verdict

**No improvement shown. Recommendation: do not push on this evidence; discuss with Morten.**

1. **VP margin: within noise.** Mean margin (Mine - Opponent) on -36, off +76: on is -113 a game against off, give or take 228 (two
   standard errors). Mine won/drew/lost 53/34/57 on v 60/27/57 off.
2. **The test cannot show a gain by its design.** Both sides play the same brain in each arm (the framework is on for both sides or for
   neither), so a better brain lifts both sides and the margin only moves by chance. A direct VP test needs the framework on for ONE
   side only (a per-side switch; it exists only on the parked forecast branch oaxa63, not on the candidate). That is the batch that
   would settle "improvement or not".
3. **What the same games do show is a quieter game with fewer kills:** charges declared 4.8 v 5.2 per side a game, contacts 3.5 v 3.7,
   points traded 1,358 v 1,558 a game (-13%), VP per side 1,348 v 1,448 (-100), units lost 4.5 v 5.2. Offensive armies lose most:
   own VP -137 a game (±118, the one difference outside noise).
4. **Stance (Morten's expectation): half met.** With the framework, defensive armies do better against offensive ones (+213 margin on v
   +63 off, a gain of +150 ±232, within noise), but NOT by shooting more: their shooting+war machine kills fall (163 v 193 VP a game);
   offensive armies kill less in combat (454 v 534).

## 1. Every KPI, on v off (per side and game; "both" = both sides)

| KPI | on | off | Note |
| --- | --: | --: | --- |
| VP margin Mine - Opponent | -36 | +76 | noise (±228) |
| Mine won / drew / lost | 53 / 34 / 57 | 60 / 27 / 57 | |
| VP per side a game | 1,348 | 1,448 | -100 |
| VP from objectives, Mine / Opponent | 561 / 570 | 586 / 533 | |
| VP from kills, Mine / Opponent | 720 / 727 | 846 / 798 | fewer kills |
| VP from leaders, Mine / Opponent | 49 / 66 | 55 / 77 | |
| Units lost, Mine / Opponent | 4.6 / 4.5 | 5.2 / 5.3 | |
| Points traded a game (both sides' losses) | 1,358 | 1,558 | -13% |
| Side that went first won | 54 of 110 | 60 of 117 | |
| Charges declared a game (both) | 4.8 | 5.2 | |
| Charge contacts a game (both) | 3.5 | 3.7 | |
| Round of first charge contact | 2.8 | 2.6 | later |
| Sides that never declared a charge | 6% | 5% | |
| Sides that never made contact | 10% | 8% | |
| Joint charges a game | 0.4 | 0.4 | |
| Share of charged targets hit by 2+ units | 15% | 12% | up |
| Set-ups (close in) that charged next turn | 15% | 15% | |
| Charge contacts in flank or rear | 51% | 48% | up |
| Charged fights a game, Mine / Opponent | 2.6 / 3.3 | 3.2 / 3.4 | |
| Net points per charged fight, Mine / Opponent | +74 / +92 | +80 / +92 | |
| Net per supported fight, Mine / Opponent | +162 / +126 | +85 / +129 | supported fights pay more |
| First round won (charged fights), Mine / Opponent | 72% / 56% | 71% / 59% | |
| Charge objectives carried out (contact) | 55% / 45% | 53% / 45% | |
| Shoot objectives carried out | 49% / 58% | 47% / 48% | up |
| Support requests answered | 35% / 51% | 52% / 39% | mixed |
| Shots by shooting units, Mine / Opponent | 10.9 / 9.8 | 9.0 / 9.3 | more shots |
| Points destroyed by shooting units | 74.8 / 36.4 | 72.7 / 42.6 | |
| Points destroyed by war machines | 73.7 / 15.3 | 96.1 / 16.6 | down |
| Magic missiles cast | 1.9 / 1.1 | 1.7 / 1.1 | |
| Magic missiles tried each own turn (both; target 50%) | 33% | 30% | up |
| Points destroyed by magic | 68.5 / 23.4 | 76.5 / 32.6 | down |
| Points destroyed in combat | 323 / 406 | 391 / 392 | |
| Points run down | 81 / 93 | 73 / 140 | |
| Winner followed up after Give Ground | 97% | 96% | |
| Winner pursued after Fall Back in Good Order | 82% | 92% | down |
| Winner pursued a flee | 74% | 78% | |
| Points that never fought | 37% | 34% | up (worse) |
| Infantry points that never fought | 47% | 48% | |
| Units over 100 pts that earned nothing | 59% | 57% | |
| Points that never moved of their own | 219 | 239 | better |
| Idle units, Mine / Opponent | 1.1 / 1.7 | 1.2 / 1.8 | |
| FACES THE THREAT a game, Mine / Opponent | 2.05 / 1.60 | 1.35 / 0.74 | more turning to face |
| Flank/rear hits on units free to turn, a game | 0.70 / 0.56 | 0.69 / 0.58 | unchanged |
| Bound items with another spell used | 42% | 55% | down |
| One-use items used | 53% | 57% | |
| Marches that gave up a magic missile a game | 0.6 | 0.4 | |
| **Random moves turned off the straight line** | **58%** (Mine 54%, Opponent 61%) | - | new KPI; off arm has no such choice |
| Turns played defensive (ARMY STANCE) | 41% | (not logged: rule off) | |
| Game length | ~8 min | ~8.5 min | no speed cost |

## 2. Jobs: how many used, picks per job, claimed v happened

Both arms use the same 9 job kinds (charge, shoot, hold, close in, advance, screen, redirect, lure, join). The framework adds 6 jobs that
decide moves as rule rows, all used every game: MOVE TO CHARGE, SUPPORTS, LONG SHOT, SHOOTS FROM THE BEST SPOT, RESERVE FALL BACK,
DEFENSIVE ARMY. So **15 jobs on v 9 off.**

Picks a game per side (Mine / Opponent):

| Job | on picks | on claimed VP | on happened | off picks | off claimed VP | off happened |
| --- | --- | --- | --- | --- | --- | --- |
| Charge | 3.4 / 5.0 | 112 / 122 | net 50 / 53 VP in 2 turns; declared 71-73% | 4.1 / 4.8 | 111 / 122 | net 53 / 45; declared 75% |
| Shoot | 9.1 / 4.0 | 26 / 28 | 2.9 / 6.2 VP of wounds | 9.5 / 4.3 | 23 / 15 | 3.9 / 7.3 |
| Hold marker / hill / feature | 4.6 / 4.4 | 75 / 81 | 23 / 26 VP scored | 4.9 / 4.6 | 77 / 83 | 29 / 27 |
| Close in to charge next turn | 4.7 / 6.8 | 124 / 131 | charged next turn 10% / 14% | 4.3 / 5.5 | 60 / 69 | 13% / 13% |
| Advance on an enemy | 21.9 / 24.2 | 51 / 44 | charged next turn 3% / 2% | 14.3 / 15.8 | 30 / 39 | 5% / 5% |
| Screen | 0.1 / 0.2 | 4 / 1 | guarded lost 0.0 / 0.3 wounds | 2.2 / 3.4 | 65 / 43 | 0.4 / 0.4 (line said 4-6) |
| Redirect | 0.1 / 0.4 | -8 / 36 | | 1.9 / 3.4 | 12 / 25 | |
| Lure | 0.1 / 0.0 | | | 0.8 / 0.6 | 114 / 98 | |
| Join a unit | 0.7 / 0.8 | 42 / 39 | | 0.7 / 0.8 | 34 / 52 | |

Framework rule rows on (fired a game, Mine / Opponent; figure added; VP won / lost after it):

| Rule | Mine | Opponent |
| --- | --- | --- |
| MOVE TO CHARGE | 5.0 (+435 / 206 / 77) | 7.6 (+660 / 273 / 193) |
| SUPPORTS | 7.5 (+361 / 270 / 115) | 9.0 (+364 / 256 / 114) |
| STABLE ROLE | 11.6 | 10.7 |
| BEST FIRST | 3.6 (+166 / 102 / 73) | 2.9 (+137 / 68 / 41) |
| LOST CHARGE | 3.1 (-55 / 130 / 90) | 2.3 (-42 / 59 / 85) |
| BEST FACING | 1.0 | 0.8 |
| WAR ENGINE JOBS | 1.1 | 0.4 |
| RANDOM MOVE BY FIGURES | 0.9 | 1.8 |
| SHOOTS FROM THE BEST SPOT | 0.6 | 0.4 |
| DEFENSIVE ARMY | 0.6 | 0.3 |
| RESERVE FALL BACK | 0.5 | 0.8 |
| LONG SHOT | 0.4 | 0.5 |
| RANDOM MOVER NO PROMISE | 0.3 | 0.4 |
| SCREEN / REDIRECT / LURE BY ... , HILL BY ITS CHANCE | 0.0-0.4 each | |
| STAY WEIGHED, SHOOTER COUNTED ONCE, WOUNDED STAYS OUT | ~0 | |

Reading: screens, redirects and lures nearly vanish (one-turn rule working as Morten ruled). The freed picks go to "advance on an enemy"
(+50%), whose claim rose (51 v 30 VP) while it led to a charge next turn even less (2-3% v 5%). The close-in claim doubled (124-131 v
60-69) with no more charges following it (10-14% v 13%). Both figures are now further from what happens than before: the
framework's move-to-charge value is the biggest overstatement in the batch.

## 3. Defensive v offensive army, per game, side and turn

Each computer side logs ARMY STANCE every turn (on arm only: with the defensive-army rule off the line is not written, so each off-arm
side takes the stance it had in the same on-arm game). 41% of all turns were defensive; 113 of 288 sides were mostly defensive (4.9
defensive turns a game), 175 mostly offensive (0.25). In every game with a defensive side the other side was offensive.

| Stance | Arm | Sides | VP a game | Margin a game | Kills: shooting + war machines | magic | charge + combat | fled off the table | shooting+magic share |
| --- | --- | --: | --: | --: | --: | --: | --: | --: | --: |
| Defensive | on | 113 | 1,439 | +213 | 163 | 75 | 447 | 76 | 35% |
| Defensive | off | 113 | 1,483 | +63 | 193 | 79 | 443 | 110 | 38% |
| Offensive | on | 175 | 1,289 | -137 | 59 | 27 | 454 | 121 | 16% |
| Offensive | off | 175 | 1,426 | -41 | 63 | 39 | 534 | 164 | 16% |

Paired on the same games: defensive sides' margin +150 ±232 (noise), own VP -44 ±137; offensive sides' margin -97 ±219, own VP -137 ±118.
Defensive sides led on VP in 66 of 113 games on v 61 off.

## 4. VP by source: Morten's expectation tested

Expectation: defensive armies gain more VP from shooting, offensive armies more from charges and combat.
- **Defensive: not met.** Shooting + war machine kills fall 30 VP a game (163 v 193), magic flat, combat flat; they win more because the
  offensive enemy kills less, not because they shoot better. War machine kills overall fall (73.7 v 96.1 for Mine).
- **Offensive: not met.** Combat kills fall 80 VP a game (454 v 534) and fewer enemies flee off the table (121 v 164). Fewer charges
  (offensive sides charge less with MOVE TO CHARGE waiting for a better spot), later first contact (round 2.8 v 2.6) and fewer pursuits
  after Fall Back in Good Order (82% v 92%).

## 5. Random moves turned off the straight line

58% of random-mover moves were turned off the straight line at the nearest enemy (Mine 54%, Opponent 61%; RANDOM MOVE BY FIGURES 0.9-1.8 a
game, RANDOM MOVER NO PROMISE 0.3-0.4). Whether cannons ground them less cannot be read from the batch tables (no per-mover loss count by
war machines); points destroyed by enemy war machines overall fell (Mine 73.7 v 96.1, Opponent 15.3 v 16.6), consistent with fewer
easy targets but not proof of it.

## 6. Sim bugs and stalls

- 0 findings in 288 games; every game ended at its turn limit or a wipe-out.
- Best-figure guard: NO REASON 0.10 a game in the on arm, games played on (the fix holds).
- Part on-2's first run died in its container at 15:25 UTC with no games saved (container restarts kill background runs when a thread
  idles); rerun split three ways. Not a game bug. Lesson: part threads must stay attended (a monitor) while the run goes.

## 7. Options for Morten (planning, not decided here)

1. **One-sided batch** (recommended next): framework on for one side, off for the other, same 144 games; this is the only test where VP
   margin can show an improvement. Needs the per-side switch ported from oaxa63 (about 1 h build) plus a 2-3 h batch.
2. Tune before re-testing: the advance and close-in claims (now 2-10x what happens) and MOVE TO CHARGE's waiting, which cost offensive
   armies charges and combat kills.
3. Push as it is: not supported by this batch (no VP gain shown, fewer kills, quieter games).

Replays: branch claude/project-thread-4rlmql at b6e6359f7 (candidate db7ca9c5d + 10 batch folders fw-on-db7ca9c-p1/p2/p2b/p2c/p3/p4 and
fw-off-db7ca9c-p1..p4, added to on-site.txt beside the earlier batches; the on games carry the new job colours).
