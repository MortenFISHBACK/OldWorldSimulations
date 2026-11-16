# Bonus for joining a friend's charge: head-to-head against main (2026-11-16)

**Verdict: no. The bonus does not improve play.** The side with the bonus is behind by **-17 VP a game, give or take 40 VP** (paired
over 144 pairs): a dead heat that leans slightly the wrong way. The reason is plain: the bonus almost never changes what the computer does.
It was weighed 631 times (2.2 a game) but changed the chosen option only 59 times (0.2 a game), and only **once** into a charge. In
**113 of the 144 pairs the two games came out move-for-move the same** (same score with the bonus on either side). Joint charges on
250+ point targets: 41 with the bonus against 38 without, earning the same per 100 charger points.

Batch: 288 games, the same 144 DKTC pairs and seeds as today's charge worth and set-up head-to-heads (Hero v Hero = script opponent both
sides, seed 1, scenarios mix), each pair played twice. Bonus side: branch `claude/project-thread-u9nplz` at `b54c22600` (main c7c800290 +
JOINS A FRIEND). Other side: `joins-a-friend` switched off = today's main (charge odds, charge band and honest worth ON for both sides).
opp-1..4: bonus on for Opponent; mine-1..4: bonus on for Mine. 288 of 288 games ended, no stalls, no re-runs (mine-2 lost its first start
in the build and restarted), no Movement time-limit hits. No leak: no JOINS A FRIEND row on the switched-off side. One sim finding
(known, see the end).

## 1. Morten's five headline numbers

| # | Number | **Bonus on** | **Off (main)** | Read |
| --- | --- | --- | --- | --- |
| 1 | VP margin per game | **-17** | +17 | **-17 ±40** (paired over 144 pairs), inside noise |
| 2 | First round won when charging | 73% (632 of 869) | 74% (642 of 873) | same |
| 3 | Net points per charged fight (damage counted) | +89 | +91 | same |
| 4 | Points lost per game | 712 | 717 | same |
| 5 | Free units caught in flank or rear (per game, lower is better) | 0.62 | 0.64 | same |

W/D/L of the bonus side 118 / 56 / 114. Pairs ahead over both games 16, behind 15, level 113.
In the 31 pairs where the bonus changed anything: -79 VP a game ±183 (noise; a few big swings either way decide it).
The ±40 is narrower than the ±110 of earlier head-to-heads because most pairs played identically, not because the effect is measured better.
Earlier today: charge worth -7 ±110, set-up rules -31 ±114, combined -31 ±95.

Diagnostics (not targets): charge contacts a game 3.5 v 3.5; points that never fought 39% v 38%; lone characters that fought 75% v 75%.

## 2. What the bonus had to move: joint charges on 250+ point targets

Every charged fight, by the number of chargers and the target's points (with its joined characters). Net = points won minus lost with damage
counted; ± is the 95% range.

| Fights | Bonus on: fights, first round won, net per fight, per 100 charger pts | Off (main): same |
| --- | --- | --- |
| All | 870, 73%, +89 ±14, +32 ±5 | 875, 74%, +91 ±14, +33 ±5 |
| **Joint (2+ chargers), target 250+** | **41**, 73%, +204 ±83, **+36 ±14** | **38**, 74%, +185 ±91, **+33 ±15** |
| Lone, target 250+ | 199, 50%, +88 ±44, +27 ±13 | 195, 54%, +108 ±46, +34 ±14 |
| Joint, target under 250 | 88, 93%, +155 ±43, +35 ±8 | 90, 92%, +141 ±42, +32 ±8 |
| Lone, target under 250 | 542, 78%, +70 ±11, +32 ±5 | 552, 77%, +71 ±11, +33 ±5 |
| Joint, all targets | 129, 87%, +170 ±40, +35 ±7 | 128, 87%, +154 ±40, +32 ±7 |

Chargers / target points in joint fights on 250+ targets: 573 / 352 with the bonus, 569 / 359 without.

- Joint charges a game: 0.5 v 0.5; share of charged targets hit by 2+ units 15% v 15%.
- Lone charges that a friend follows on the same target next turn: 6% (42) v 5% (35).
- Support requests answered (helper made contact too): 53% v 52%.

So the joint fights on big targets did not become more common (3 more in 288 games) and did not earn more per point.

### How often the bonus was used (JOINS A FRIEND rows, bonus side only)

| Option it raised | Rows | Changed the pick |
| --- | --- | --- |
| Advance on the target | 412 | 45 |
| Close in to charge it next turn | 206 | 13 |
| Charge it now | 13 | **1** |
| **All** | **631 (2.2 a game)** | **59 (0.2 a game)** |

The hidden rule count agrees: JOINS A FRIEND fired 1.8 a game (bonus on for Mine) and 2.6 a game (bonus on for Opponent); "Rule changes"
0.15 and 0.26 a game (22 and 37 changed picks). The bonus mostly lands on advance and close-in options, where it is small (+2 to +23 VP) next to the option's own worth,
and it is almost never weighed on a charge: when a friend already charges a 250+ target, a second unit that can reach it usually already
picks that charge, or cannot reach it at all.

## 3. Every KPI side by side

Full tables in `kpis-on-v-off.md` (bonus on v off, pooled over both arms) and `compare-all.md` (A = mine arm, B = opp arm). Nothing moved
outside noise. Selected rows:

| Measure | Bonus on | Off (main) |
| --- | --- | --- |
| Charges declared / contacts a game | 4.8 / 3.5 | 4.9 / 3.5 |
| Charges by odds: long shot / 55-75% / 90%+ not overkill / overkill | 61 / 66 / 106 / 30 | 60 / 70 / 108 / 30 |
| Net per 100 charger points (damage counted) | +31.4 | +32.5 |
| Net per joint fight / lone fight (damage counted) | +170 / +75 | +154 / +81 |
| Set-ups (close in) that charged that target next turn | 14% | 15% |
| Charge contacts in flank or rear | 50% | 49% |
| Points destroyed in combat / run down | 337 / 88 | 343 / 95 |
| VP from objectives / kills (per game) | 577 / 756 | 591 / 761 |
| Magic missiles tried each own turn | 34% | 34% |
| Points that never fought | 39% | 38% |
| Joined characters whose unit fought | 38% | 42% |

### Movement choices (diagnostics)

| Measure | Bonus on | Off (main) |
| --- | --- | --- |
| Move decisions with candidates a game | 40.5 | 40.5 |
| Took the best spot by WORTH of all it weighed | 59% | 59% |
| Took a spot among the best three | 76% | 76% |
| WORTH given up against the best spot (VP a move) | +21.9 | +21.4 |
| Moved (did not stay) | 53% | 53% |
| Stayed although a move was worth more | 39% | 38% |
| Set-ups: next turn a charge job on the same target / closes in again / another job / no job | 12% / 13% / 62% / 14% | 12% / 12% / 62% / 14% |

## 4. Verdict and what it means for Morten's ruling

**Does the bonus improve play? No.** -17 ±40 VP a game, every headline number the same, joint charges on 250+ targets 41 v 38 with the same
earnings. It barely changes a decision (0.2 a game, one charge in 288 games).

Morten's ruling (12:47 UTC): if it does not improve, drop the bonus AND the charge band from main. This batch tests the bonus only; the charge
band was ON for both sides. The band's own figures here: CHARGE BAND fired 0.1-0.2 a game per side and changed a pick about 0.27 a game (both sides together), as rare
as in the earlier batches (charge worth head-to-head: 45 band charges in 288 games). Removal is for a build thread; the repo note
docs/claude-memory/project_joins_a_friend_2026-11-16.md lists what removing both touches. Nothing was removed here.

## Findings

- S-185bc1 (known): L2025, mine-1 game, Opponent Spirit Hosts overlap Opponent Hexwraiths by 1.71" (setup, checked late in turn 6). Same
  finding as the set-up head-to-head; the fix is on the Tomb King branch (thread "Fix Spirit Hosts overlapping Hexwraiths").

## Files

- mine-1..4, opp-1..4: the parts (games.csv, game-*.txt, logs). counts.log: part counts.
- compare-all.md: scripts/compare-batches.py, A = mine arm, B = opp arm; kpis-on-v-off.md: remapped to bonus on / main.
- scripts/: merge.py, h.py, remap.py (from the set-up batch); the joint-fight table from compare-batches.charged_fights.
