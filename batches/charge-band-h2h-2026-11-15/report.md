# Charge odds + charge band: head-to-head against main (2026-11-16)

**Verdict: no gain in the game result. The side with both changes is behind by -14 VP a game, give or take 99 VP: a dead heat.**
The honest odds still work as in the odds-only batch (95%+ charges win 95%, against 92% without). But the band rule almost never fires:
help was asked under the new rule 33 times in 144 games (0.23 a game), and only 19 of those charges were made. So the count of sure
charges, long shots and 60-75% charges is the same as in the odds-only batch, and the result moved from +4 to -14 VP, both inside noise.

Batch: 288 games, the same 144 DKTC pairs and seeds as the charge-odds and shooting-plan head-to-heads (Hero v Hero, seed 1, scenarios mix),
each pair played twice. Changed side: branch `claude/project-thread-tzp2le` at `24b8cfb4` (charge-odds fixes + charge band). Other side:
`charge-odds` and `charge-band` switched off = main. mine-1..4: changes on for Mine; opp-1..4: changes on for Opponent.
288 of 288 games ended, no stalls, no re-runs. Every part's rules-off list named all seven tags for the right side, and no rule of the two
changes wrote a single row on the switched-off side (no leak). One finding (see the end).

## 1. Morten's five headline numbers

| # | Number | **Changes on** | **Changes off (main)** | Read |
| --- | --- | --- | --- | --- |
| 1 | VP margin per game | **-14** | +14 | **-14 ±99** (paired over 144 pairs), inside noise |
| 2 | First round won when charging | 72% | 72% | same |
| 3 | Net points per charged fight | +73 | +78 | same, within noise |
| 4 | Points lost per game | 758 | 734 | 24 more, within noise |
| 5 | Free units caught in flank or rear (per game, lower is better) | 0.64 | 0.62 | same |

W/D/L of the changed side 112 / 54 / 122; pairs ahead over both games 71, behind 73. For comparison: charge odds alone +4 ±102,
shooting plan -19 ±92, staying-to-shoot +65 ±101.

Diagnostics (not targets): charge contacts a game 3.8 v 3.8; points that never fought 36% v 36%; lone characters that fought 79% v 77%.

## 2. The band rule: how often help was asked, and what it earned

Help asked for a charge that wins 55-75% alone, when together it wins 76%+ and is not overkill (CHARGE BAND row).

| | Changes on |
| --- | --- |
| Charges where the band asked for help | 33 in 144 games (0.23 a game): 25 in the Strategy phase, 9 joins in the Movement phase |
| Alone v together (average) | 66% alone, 92% together |
| Of those, the charge was made | 19 (13 arrived together, 6 with one charger only) |
| First round of those 19 | 15 won, 2 drawn, 2 lost (79%; the line had said 81% on average) |
| Net per fight / per 100 charger points | +162 / **+37** (chargers 438 pts, targets 213 pts) |

The joint charges the rule made earned about as well as the best band (76%+ not overkill, +34 per 100 points), against +25 for a
60-75% charge. But 19 fights in 288 games is far too few to move the result: the gain is about +2 VP a game at most, invisible in ±99.
14 of the 33 asks led to no charge that turn (the main charger or the helper did not go).

## 3. Charges by odds band, per side

Net points per 100 charger points, damage counted. Overkill = target under 250 pts and chargers over 3x its points.

| Band | Changes on: fights, first round won, net per 100 | Changes off: fights, first round won, net per 100 |
| --- | --- | --- |
| under 50% | 165, 29%, +23 ±16 | 135, 27%, +4 ±18 |
| 50-59% | 66, 61%, +27 ±22 | 51, 55%, +16 ±20 |
| 60-75% | 136, 68%, +25 ±10 | 120, 57%, +20 ±16 |
| 76-89% | 192, 83%, +27 ±9 | 163, 77%, +35 ±10 |
| 90%+ not overkill | 193, 89%, +36 ±10 | 292, 92%, +47 ±8 |
| overkill (90%+) | 96, 99%, +16 ±5 | 81, 91%, +22 ±8 |
| **76%+ not overkill** | 348, 86%, **+34 ±8** | 425, 86%, **+45 ±7** |
| **76%+ overkill** | 133, 95%, **+17 ±4** | 111, 92%, **+21 ±7** |

### Sure charges and long shots compared with the odds-only batch (charges a batch, 144 games a side)

| Kind | Changes on, this batch | Odds only (fixes on) | Main, this batch | Main, odds-only batch |
| --- | --- | --- | --- | --- |
| Long shots (under 50%) | 83 | 84 | 68 | 68 |
| 55-75% | 86 | 84 | 74 | 75 |
| 90%+ not overkill | 97 | 98 | 146 | 146 |
| Overkill | 48 | 49 | 40 | 41 |
| Joint charges a game | 0.5 | 0.5 | 0.5 | 0.5 |

No movement: the band rule did not take 60-75% charges out or add joint 76%+ ones in any number you can see. The honest odds alone
explain the whole difference against main (a third fewer "sure, not overkill" charges, more long shots).

## 4. Do stated odds match results?

| Odds band | Changes on: fights, said, won | Changes off: fights, said, won |
| --- | --- | --- |
| under 50 | 165, 26%, 29% ±7 | 135, 24%, 27% ±8 |
| 50-59 | 66, 55%, 61% ±12 | 51, 55%, 55% ±14 |
| 60-75 | 136, 68%, 68% ±8 | 120, 68%, 57% ±9 |
| 76-89 | 192, 84%, 83% ±5 | 163, 83%, 77% ±6 |
| 90-94 | 76, 92%, **84% ±8** | 69, 92%, 91% ±7 |
| 95-100 | 213, 98%, **95% ±3** | 304, 99%, **92% ±3** |
| 99%+ only | 102, 100%, 95% ±4 | 195, 100%, 94% ±3 |

Too sure, in points (said minus won), fights at 60%+: changes on +2.3 (617 fights), off +6.3 (656). Plain fights +0.2 v -0.2; fights
with joined characters, challenges or combat spells +7.5 v +16.2. Same as the odds-only batch: the odds are honest, and the 90-94% band
is still the weak spot (says 92, wins 84, both batches).

## 5. Other KPIs side by side

| Measure | Changes on | Changes off |
| --- | --- | --- |
| Charges declared / contacts a game | 5.3 / 3.8 | 5.3 / 3.8 |
| Charge objectives carried out (made contact) | 47% | 48% |
| Support requests answered (helper made contact too) | 42% (80 of 190) | 45% (77 of 171) |
| Joined characters whose unit fought | 44% | 44% |
| Charged fights on a top-3 enemy unit | 184 | 192 |
| Net per 100 charger points, damage counted | +26 | +27 |
| Points destroyed in combat a game | 363 | 375 |
| Points run down a game | 97 | 98 |
| Points destroyed by magic a game | 57 | 47 |
| Points destroyed by war machines a game | 46 | 58 |
| Idle units a game | 1.4 | 1.4 |
| Points that never moved of their own a game | 224 | 214 |
| Turned to face a threat (FACES THE THREAT) a game | 1.65 | 1.51 |
| Turns played defensive | 16% | 17% |
| Magic missiles tried each own turn (when they could be) | 30% (44%) | 31% (45%) |
| Sides that never made charge contact | 9% | 6% |

Full side-by-side tables: kpis-on-v-off.md (remapped to changes on / off) and compare-all.md (A = mine arm, B = opp arm).

### Jobs claimed v happened (all jobs of each side)

| Job | Changes on: jobs, happened, planned v won VP a job | Changes off |
| --- | --- | --- |
| charge | 1237, 57%, 92 v 87 | 1172, 54%, 104 v 88 |
| close in | 1481, 25%, 60 v 25 | 1450, 26%, 67 v 30 |
| shoot | 1891, 61%, 7 v 78 | 1859, 60%, 10 v 74 |
| advance | 3559, 16%, 19 v 27 | 3604, 17%, 23 v 27 |
| hold | 1277, 37%, 63 v 0 | 1256, 34%, 63 v 0 |
| support | 1267, 90%, -9 v 0 | 1309, 88%, -9 v 0 |
| join | 204, 97%, 35 v 0 | 205, 94%, 35 v 0 |

### Stance split (gunline = the 49 army-games the framework played defensively in head-to-head 2)

| Set | Army-games | Margin, changes on | changes off | Paired difference | Better / worse |
| --- | --- | --- | --- | --- | --- |
| Gunline armies | 49 | -390 | -255 | -135 ±293 | 20 / 29 |
| Other armies | 239 | +63 | +69 | -6 ±157 | 122 / 117 |

Both inside noise (the same pattern as the odds-only batch).

### VP by source (per game)

| Source | Changes on | Changes off |
| --- | --- | --- |
| Kills | 780 | 792 |
| Objectives | 569 | 563 |
| Leaders | 49 | 57 |
| Points lost | 758 | 734 |
| Units lost | 5.0 | 5.0 |

Going first v second (changed side's margin): first -77 ±204, second +49 ±216. As Mine -143, as Opponent +115 (the lists; pairing cancels it).

### Fighting v other wizards

Not available in this batch: the split reads log rows only the shooting-plan branch writes. All wizards together: 30% v 31% tried.

## 6. What this means (warnings, not plans)

- The band rule as built is too narrow to matter: 0.23 asks a game. It only fires when a 55-75% charge already exists and a free helper
  can reach the same target that turn without making it overkill; that is rare.
- The odds fixes still cost "sure, not overkill" charges (97 v 146) that main makes and wins 92% of the time for +47 per 100 points.
  That, not the band rule, is what decides this head-to-head, as in the odds-only batch.
- The 90-94% band is still 8 points too sure in both batches (76 fights each).

## Files

- Results: mine-1..4, opp-1..4; counts.log.
- Replays: branch `claude/project-thread-6zkghv` (8 batch folders cb-h2h-{mine,opp}-24b8cfb-p1..4, on-site.txt lists them). Not on main.
- scripts/: the odds-only batch's scripts with the folder changed, plus band.py (the band rule's charges) and plans.py (jobs table).
  compare-all.md from cb.py (the corrected first-round reading); the missile row from the branch's own compare-batches.py.
- Finding: sim bug S-07892d (new), game L2131 (mine-2): two Marauder Horsemen units of one side overlap by 1.03", noticed late in turn 6.
