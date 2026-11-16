# Charge-odds fixes: head-to-head against today's main (2026-11-15)

**Verdict: no gain in the game result. The fixed side is ahead by +4 VP a game, give or take 102 VP: a dead heat.**
The fixes did what they were built for: sure charges now win about as often as they say, also with joined characters, challenges and
combat spells (95%+ charges won 96%, against 92% on the side without the fixes). But that did not turn into more VP. The fixed side makes
a third fewer "sure, not overkill" charges (its figures are lower where the old ones were too high) and more long shots, and its
sure-but-not-overkill charges earned less per point. The two effects cancel.

Batch: 288 games, the same 144 DKTC pairs and seeds as the staying-to-shoot and top-killer head-to-heads (Hero v Hero, seed 1, scenarios
mix), each pair played twice. Fixed side: branch `claude/project-thread-qcp1ro` at `324c3427`. Other side: `charge-odds` switched off for it
= main 8a44e669. mine-1..4: fixes on for Mine; opp-1..4: fixes on for Opponent. 288 of 288 games ended, 0 findings, 0 stalls; every part's
rules-off list named all six tags for the right side, and no fix wrote a single rule row on the switched-off side (no leak).
Figures: compare-batches.py with the corrected first-round-won reading (407077ff), the review's per-fight reading (calibv2) and its bands.

## 1. Morten's five headline numbers

| # | Number | **Fixes on** | **Fixes off (main)** | Read |
| --- | --- | --- | --- | --- |
| 1 | VP margin per game | **+4** | -4 | **+4 ±102** (paired over 144 pairs), inside noise |
| 2 | First round won when charging | 72% | 70% | slightly better |
| 3 | Net points per charged fight | +72 | +76 | same, within noise |
| 4 | Points lost per game | 752 | 741 | same, within noise |
| 5 | Free units caught in flank or rear (per game, lower is better) | 0.63 | 0.64 | same |

W/D/L of the fixed side 114 / 53 / 121; pairs ahead over both games 70, behind 74. For comparison: staying-to-shoot +65 ±101,
head-to-head 2 (framework v old brain) +59 ±108.

Diagnostics (not targets): charge contacts a game 3.8 v 3.8; points that never fought 36% v 36%; lone characters that fought 79% v 78%.

## 2. Do charges now win by the odds they were given?

Each charged fight by the first-round chance the side's own figure gave it, and what happened in the first round. "Plain" = no enemy
character joined to the target, no challenge, no enemy spell in the round, one enemy unit, not a mirror match (the review's clean set).
Intervals are 95%.

### All fights

| Odds band | Fixes on: fights | said | won | Fixes off: fights | said | won |
| --- | --- | --- | --- | --- | --- | --- |
| below 50 | 167 | 26% | 29% ±7 | 136 | 24% | 27% ±7 |
| 50-59 | 61 | 55% | 61% ±12 | 50 | 55% | 54% ±14 |
| 60-75 | 135 | 68% | 67% ±8 | 122 | 68% | 58% ±9 |
| 76-89 | 196 | 84% | 83% ±5 | 161 | 83% | 76% ±7 |
| 90-94 | 76 | 92% | 84% ±8 | 70 | 92% | 90% ±7 |
| 95-100 | 217 | 98% | **96% ±3** | 304 | 99% | **92% ±3** |

### Plain fights v fights with joined characters, challenges or combat spells

| Odds band | Plain, fixes on | Plain, fixes off | Other, fixes on | Other, fixes off |
| --- | --- | --- | --- | --- |
| below 50 | 31% said, 42% won (65) | 25% / 29% (48) | 22% / 22% (102) | 23% / 26% (88) |
| 50-59 | 56% / 61% (38) | 55% / 63% (27) | 54% / 61% (23) | 55% / 43% (23) |
| 60-75 | 69% / 75% (83) | 68% / 70% (67) | 67% / 56% (52) | 67% / 44% (55) |
| 76-89 | 84% / 85% (144) | 83% / 89% (95) | 83% / 77% (52) | 82% / 58% (66) |
| 90-94 | 92% / 84% (56) | 92% / 92% (40) | 92% / 85% (20) | 92% / 87% (30) |
| 95-100 | 98% / **96%** (168) | 99% / **95%** (193) | 98% / **94%** (49) | 98% / **87%** (111) |
| 99%+ only | 100% / 97% (87) | 100% / 95% (131) | 100% / 93% (15) | 100% / 92% (63) |

Too sure, in points (said minus won), fights at 60%+:

| Set | Fixes on | Fixes off |
| --- | --- | --- |
| All | +2.1 (624 fights) | +6.6 (657) |
| Plain | +0.3 (451) | 0.0 (395) |
| Other | **+7.1** (173) | **+16.5** (262) |

Against the review (before the fixes: 99% won 96% plain and 85% otherwise; 95%+ won 92.5%): the "other" fights went from 13-19 points too
sure to 7; 95%+ charges now win 96%. Plain fights stayed right, as they were. Still off: the 90-94% band wins 84% (8 points short, both
plain and other, 76 fights), and "other" fights at 60-89% are 10 points too sure.

### Is the wider spread (x1.15, untuned) right?

Not clearly wrong, and probably still a little narrow. In plain fights with the fixes on, the low bands win more than they say
(below 50: 31% said, 42% won; 60-75: 69% / 75%) and the 90-94 band wins less (92% / 84%). That is the pattern of a spread still too narrow
(figures too far from 50% at both ends). But each gap is inside its own noise (±10-16 points), the 95%+ band is right (98% / 96%),
and plain fights at 60%+ are on the mark overall (+0.3). Leave 1.15 for now; a re-check with more fights (or a factor around 1.25-1.3
tried as its own switch) would settle it.

## 3. Net points per 100 charger points, by band (for the "76%+ and not overkill" decision)

Overkill = the 2026-11-10 rule (target under 250 pts and chargers over 3x its points), here applied from 76% up for the second table.

| Band | Fixes on: fights, won 1st round, net per 100 | Fixes off: fights, won 1st round, net per 100 |
| --- | --- | --- |
| below 50% | 167, 29%, +23 ±16 | 136, 27%, +3 ±18 |
| 50-59% | 61, 61%, +25 ±23 | 50, 54%, +16 ±21 |
| 60-75% | 135, 67%, +29 ±11 | 122, 58%, +19 ±15 |
| 76-89% | 196, 83%, +28 ±9 | 161, 76%, +35 ±10 |
| 90%+ not overkill | 195, 90%, +37 ±10 | 292, 92%, +47 ±8 |
| 90%+ overkill | 98, 99%, +16 ±4 | 82, 91%, +22 ±8 |
| **76%+ not overkill** | 353, 86%, **+35 ±8** | 423, 86%, **+45 ±7** |
| **76%+ overkill** | 136, 95%, **+17 ±4** | 112, 91%, **+22 ±7** |

On both sides, 76%+ and not overkill earns the most per point (+35 to +45), about twice the overkill charges (+17 to +22), with 60-75%
in between (+19 to +29). This matches the review and supports the band change. With the fixes on, the low bands earn more and the high
bands less than without them: the fixes move some fights down a band, so the same kind of fight is now filed lower.

## 4. The six fixes: how often they moved a charge

A rule row is written when a charge was taken and the fix moved its win figure by 1 point or more (REFUSING RETIRES: when it moved a
challenge answer in the Combat phase). CHANGED = the fix changed which option was taken. 288 games; rows on the switched-off side: 0 for all six.

| Fix | Charges it moved (fixed side) | a game | Changed the pick | Charge jobs followed up: happened, planned v won VP |
| --- | --- | --- | --- | --- |
| JOINT KNOWS CHALLENGE | 25 | 0.09 | 0 | 23, 30%, 104 v 81 |
| REFUSING RETIRES (Combat phase) | 44 | 0.15 | 12 | - |
| BLOWS WHERE AIMED | 82 | 0.28 | 2 | 74, 61%, 220 v 112 |
| SPELLS IN THE FIGHT | 223 | 0.77 | 12 | 201, 44%, 92 v 93 |
| CHARGER SLAIN LOST | 199 | 0.69 | 3 | 160, 49%, 28 v 90 |
| WIDER SPREAD | 958 | 3.33 | 18 | 814, 58%, 87 v 88 |

WIDER SPREAD touches most charges; the others are rare. BLOWS WHERE AIMED still over-claims (220 planned v 112 won). JOINT KNOWS CHALLENGE
almost never fires (25 in 288 games): joint charges are only 0.5 a game.

## 5. Other KPIs side by side

| Measure | Fixes on | Fixes off |
| --- | --- | --- |
| Charges declared / contacts a game | 5.3 / 3.8 | 5.3 / 3.8 |
| Charge objectives carried out (made contact) | 48% | 48% |
| Charges by band a game: long shots / 55-75% / 90%+ not overkill / overkill (counts over 144 games each) | 84 / 84 / 98 / 49 | 68 / 75 / 146 / 41 |
| Net per 100 charger points, damage counted | +26 | +27 |
| Points destroyed in combat a game | 365 | 371 |
| Points run down a game | 98 | 101 |
| Support requests answered | 43% | 45% |
| Joined characters whose unit fought | 44% | 45% |
| Idle units a game | 1.4 | 1.3 |
| Points that never moved of their own a game | 226 | 217 |
| Turned to face a threat (FACES THE THREAT) a game | 1.67 | 1.52 |
| Turns played defensive | 16% | 18% |
| Magic missiles tried each own turn (when they could be) | 30% (44%) | 30% (46%) |
| Points destroyed by magic a game | 59 | 44 |

Full side-by-side KPI tables: kpis-fixes-v-main.md (remapped to fixes on / off) and compare-all.md (A = mine arm, B = opp arm).

### Jobs claimed v happened (all jobs of each side)

| Job | Fixes on: jobs, happened, planned v won VP a job | Fixes off |
| --- | --- | --- |
| charge | 1239, 57%, 93 v 87 | 1175, 54%, 104 v 87 |
| close in | 1486, 25%, 59 v 25 | 1448, 26%, 67 v 31 |
| shoot | 1890, 60%, 7 v 77 | 1862, 60%, 11 v 73 |
| advance | 3557, 16%, 19 v 27 | 3612, 18%, 23 v 27 |
| hold | 1281, 37%, 63 v 0 | 1251, 34%, 63 v 0 |
| support | 1265, 90%, -9 v 0 | 1309, 88%, -9 v 0 |

The charge job's over-claim shrank from +17 VP to +6 VP a job: the fixed figures are closer to what charges win.

### Stance split (gunline = the 49 army-games the framework played defensively in head-to-head 2)

| Set | Army-games | Margin of that army, fixes on | fixes off | Paired difference | Better / worse |
| --- | --- | --- | --- | --- | --- |
| Gunline armies | 49 | -359 | -253 | -105 ±304 | 20 / 29 |
| Other armies | 239 | +79 | +47 | +32 ±162 | 120 / 119 |

Both inside noise.

### VP by source (per game)

| Source | Fixes on | Fixes off |
| --- | --- | --- |
| Kills | 786 | 786 |
| Objectives | 572 | 560 |
| Leaders | 50 | 57 |
| Points lost | 752 | 741 |
| Units lost | 5.0 | 5.1 |

Going first v second (fixed side's margin): first -80 ±205, second +88 ±220. As Mine -137, as Opponent +146 (the lists; pairing cancels it).

### Fighting v other wizards

Not available in this batch: the split reads the MissileWizard log rows that only the staying-to-shoot branch writes; main and this
branch do not. All wizards together: 30% v 30% tried.

## 6. What this means (warnings, not plans)

- The fixes make the figures honest, but by themselves they do not win games. Where the old figure said 95%+ and the fight was
  complicated, the fixed side now sees 80-90% and charges something else or nothing; the side without the fixes still makes those charges,
  wins 87% of them and earns well from them. The odds are only half the decision; what the computer does with the lower figure (the band
  rule) is the other half.
- The 90-94% band is now the least honest (says 92%, wins 84%, 76 fights).
- The band data on both sides favour "76%+ and not overkill" (+35 to +45 per 100 points) over 60-75% (+19 to +29) and overkill (+17 to +22).

## Files

- Results: mine-1..4, opp-1..4 (opp-1 nested one level); counts.log.
- Replays: branch `claude/project-thread-dtt5z8` at `f27966626` (8 batch folders co-h2h-{mine,opp}-324c342-p1..4, on-site.txt lists
  them). Not on main.
- scripts/: calib.py (per fight), net.py, bands.py, items.py, stance.py, h.py, remap.py, cb.py (compare-batches with the corrected
  first-round reading, plus the fight key).
