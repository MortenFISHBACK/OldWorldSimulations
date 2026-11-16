# Set-ups into charges: head-to-head against main (2026-11-16)

**Verdict: no gain in the game result. The side with the set-up rules is behind by -31 VP a game, give or take 114 VP: a dead heat.**
The rules did part of what they were built for: a close-in move now ends in charge range and facing more often (41% v 37%), and a
close-in job charges its target next turn more often (19% v 15%). But the side makes fewer close-in jobs (4.3 v 5.1 a game), so the
number of charges that come from a set-up is about the same (0.80 v 0.76 a game). Charged fights, joint charges and the points per
fight did not move. The extra searches cost no time (games take as long as in the last batch, no phase hit its 3-minute limit).

Batch: 288 games, the same 144 DKTC pairs and seeds as the charge worth head-to-head (Hero v Hero, seed 1, scenarios mix), each pair
played twice. Changed side: branch `claude/project-thread-hqoqsm` at `e45904b98` (set-up spot + carries out close-in + joint as one).
Other side: those three switched off = today's main (which already has honest odds, the charge band and honest worth). NO CHARGE WHY
was on for both sides (log only: 0 of 1,826 rows changed a pick). mine-1..4: rules on for Mine; opp-1..4: rules on for Opponent
(opp-4 was split: its thread played 18 games after a lost start, the owner played the other 18 as opp-4b).
288 of 288 games saved, 287 ended (L1723 opp stopped in turn 6, see findings), so 143 matched pairs. No leak: none of the three rules
wrote a row on the switched-off side.

## 1. Morten's five headline numbers

| # | Number | **Set-up rules on** | **Off (main)** | Read |
| --- | --- | --- | --- | --- |
| 1 | VP margin per game | **-31** | +31 | **-31 ±114** (paired over 143 pairs), inside noise |
| 2 | First round won when charging | 73% | 76% | 3 points worse, within noise |
| 3 | Net points per charged fight (damage counted) | +87 | +87 | same |
| 4 | Points lost per game | 725 | 701 | 24 more, within noise |
| 5 | Free units caught in flank or rear (per game, lower is better) | 0.61 | 0.67 | a little better, within noise |

W/D/L of the changed side 112 / 60 / 114; pairs ahead over both games 71, behind 70. Earlier: charge worth -7 ±110, odds + band -14 ±99.

Diagnostics (not targets): charge contacts a game 3.5 v 3.55; points that never fought 39% v 37%; lone characters that fought 74% v 77%.

## 2. The numbers this change had to move

Close-in jobs ("close in to charge next turn"), traced to the unit's next own turn with the finding's own scripts (trace.py, cls.py).
The finding's baseline is the charge-band batch (both sides pooled); "off" is main in this batch.

| Measure | Rules on | Off (main) | Finding's baseline |
| --- | --- | --- | --- |
| Close-in jobs | 1,244 (4.3 a game) | 1,476 (5.1 a game) | 2,945 in 288 games, both sides |
| **Charged that target next turn** | **18.6%** | 14.9% | 15% |
| ... alone | 11.7% | 8.3% | 10% |
| ... with a friend | 6.9% | 6.6% | 5% |
| Charges on the set-up target, per game | 0.80 | 0.76 | |
| Charged another enemy instead | 11.9% | 12.3% | 14% |
| Target gone / unit charged first | 9.4% / 4.7% | 7.2% / 6.7% | 7% / 5% |
| After its own move (units with known range: 776 v 1,005): outside max charge range | **45%** | 51% | 49% |
| ... in range, not facing | 14% | 12% | 14% |
| ... in range and facing | **41%** | 37% | 29% (75%+ reach) + 9% long shot |
| Of those in range and facing: charged the target / another | 22% / 10% | 21% / 10% | 30% / 16% (75%+ reach) |
| Two or more close-ins on one enemy in one turn (groups) | 168 | 219 | |
| ... 2+ of them in range and facing | 11% | 13% | 2% (75%+ reach, so not the same yardstick) |
| ... 2+ of them charged it | 12% | 13% | |
| Charged fights (all) | **849** | **858** | last batch 748 v 868 |
| Joint charges a game (2+ units on one target) | 0.5 | 0.5 | |
| Share of charged targets hit by 2+ units | 16% | 17% | |

Max charge range = the unit's own "it charges up to N" (NO CHARGE WHY) or an enemy's "staying out of its charge reach (N)", else
catalogue Movement + 6 (infantry) / + 9 (cavalry); 35% of close-in units have no known range and are left out of the "after its own
move" rows. Facing = the target in the unit's front arc.

- The set-up spot works where it fires: 6 points fewer close-in moves end out of range, 4 more end in range and facing.
- The charges did not come back from last batch's loss because of these rules: main itself now has honest worth, so both sides charge
  about the same (849 v 858). The 748 v 868 gap of the last batch is gone on both sides.
- Joint set-ups did not improve: pairs on one enemy are fewer (joint as one drops groups whose friend cannot arrive), and the share
  where both are ready or both charge is the same.

### What the rules did (rows on the changed side, per game)

| Rule | Rows a game | Changed the pick a game |
| --- | --- | --- |
| SET-UP SPOT | 5.0 | 2.5 |
| JOINT AS ONE | 2.3 | 0.25 |
| CARRIES OUT CLOSE-IN | 0.45 | 0.06 |
| NO CHARGE WHY (both sides, log only) | 2.9 v 3.5 | 0 |

SET-UP SPOT is the only one that decides often. CARRIES OUT CLOSE-IN changed the pick 18 times in 288 games: almost always the
remembered charge was already first, or the target was no longer charged at 50%+.

### Why no charge on last turn's set-up target (NO CHARGE WHY, by class)

| Class | Rules on | Off (main) |
| --- | --- | --- |
| range (out of its charge range) | 226 (27%) | 321 (32%) |
| gone (target destroyed or off the table) | 132 (16%) | 152 (15%) |
| reach (charge roll reaches it under 5%) | 139 (17%) | 140 (14%) |
| arc (not in its front arc) | 120 (15%) | 128 (13%) |
| way (blocked by a unit or terrain) | 81 (10%) | 102 (10%) |
| in combat | 57 (7%) | 70 (7%) |
| sight | 40 (5%) | 46 (5%) |
| target flees / unit fleeing / may not charge | 32 (4%) | 40 (4%) |
| **All** | **827** | **999** |

The 25% "in range and facing, yet no charge" of the finding splits into reach 14-17%, arc 13-15%, way 10%, sight 5%. Range is still
the biggest single cause on both sides.

## 3. Charges by odds band (net per fight and per 100 charger points, damage counted)

| Band | Rules on: fights, net, per 100 | Main: fights, net, per 100 |
| --- | --- | --- |
| under 50% | 120, +32, +14 | 108, +87, +39 |
| 50-54% | 31, +78, +29 | 30, +123, +48 |
| 55-75% | 146, +86, +29 | 160, +80, +26 |
| 76-89% | 184, +104, +37 | 181, +80, +29 |
| 90%+ not overkill | 201, +136, +47 | 227, +106, +38 |
| 90%+ overkill | 62, +96, +19 | 56, +71, +15 |
| no odds | 105, +30, +12 | 96, +69, +27 |
| **All** | **849, +87, +30** | **858, +87, +31** |

The changed side earns more from its 76%+ charges and less from long shots; the totals come out the same.

## 4. Other KPIs side by side

| Measure | Rules on | Main |
| --- | --- | --- |
| Charges declared / contacts a game | 4.9 / 3.5 | 4.9 / 3.55 |
| Charge objectives carried out (made contact) | 48% | 47% |
| Points destroyed in combat a game | 348 | 352 |
| Net per supported fight / lone fight | +83, +194 / +72, +70 (Mine arm / Opp arm) | +190, +128 / +89, +51 |
| Turned to face a threat (FACES THE THREAT) a game | 1.6 | 1.6 |
| Magic missiles tried each own turn (when they could be) | 34% (48%) | 36% (48%) |
| Game time, mean / 90th percentile / slowest | 5.8 / 7.6 / 13.3 min | last batch 5.8 / 7.9 / 9.8 min |

Movement phase time: no game hit the 3-minute stall limit (that would be a finding; none). The phase times are not logged one by one, so
the slowest phases cannot be named; the slowest games are the same pairs in both arms (L1831 13.3 and 11.7 min, L2223, L2235, L1422),
so it is the lists, not the rules. Games an hour per 4-core container: about 26-28 in the part threads (same as earlier batches); 36 an
hour in the owner's container.

### Jobs claimed v happened

| Job | Rules on: picks a game, claimed VP, happened | Main |
| --- | --- | --- |
| Charge | 4.3, ~94 VP, declared 75% | 4.3, ~86 VP, declared 72% |
| Close in | 4.3, ~38 VP, charged it next turn ~16% | 5.1, ~52 VP, charged it next turn ~13% |
| Advance | 20.1, ~22 VP, 3.5% | 19.4, ~24 VP, 3.5% |

A close-in now promises less (38 v 52 VP) and comes closer to what it delivers: the set-up spot prices the spot it can really reach.

### VP by source (per game)

| Source | Rules on | Main |
| --- | --- | --- |
| Kills | 745 | 765 |
| Objectives | 576 | 593 |
| Leaders | 55 | 50 |
| Points lost | 725 | 701 |
| Units lost | 4.8 | 4.6 |

Going first v second (changed side's margin): first -90, second +27. As Mine -148, as Opponent +85 (the lists; pairing cancels it).

## 5. Option 5: what the data suggests (Morten still to choose)

- Fights with 2+ chargers earn far more than lone ones on both sides (net about +130 to +190 a fight against +50 to +90), but joint
  charges stay at 0.5 a game and did not rise with joint as one.
- Joint as one mostly removes groups (2.3 rows a game, 0.25 changed picks); it made joint plans honest, not more common. The friends that
  do close in on the same enemy are both ready no more often than before (11% v 13%).
- So the data points to the bonus for joining a friend's target (5a) as the lever left: the group gate (5b) has little to open, because
  there are few groups whose friends can really arrive. This is a reading, not a measurement: neither was built or tested here.

## 6. What this means (warnings, not plans)

- The set-up rules make close-ins honest (fewer, priced lower, more often in range and facing) but do not add charges or VP.
- The biggest remaining cause is still range: 45% of close-in moves end outside max charge range even with the set-up spot.
- reach/arc/way together are about 40% of the NO CHARGE WHY rows: a unit in range that still cannot charge.

## Findings (sim bugs, none fixed)

- **S-e2a05d / S-04d49c (new)**, game L1723 (opp-1), turn 6: a unit that had succumbed to Stupidity was offered Flee when charged and the
  charge code refused it ("must Hold if charged", ChargePhaseService.Reactions.cs:269). The game stopped. The answer comes from the charge
  reaction pick, not from these rules.
- **S-185bc1 (new)**, game L2025 (mine-1): Spirit Hosts overlap Hexwraiths of the same side by 1.71", noticed late in turn 6.
- Warning only: L1216 (opp-3) "DRIVER STOOD IN at Turn 5 Mine Combat: Accept with Jade Warriors (Champion)"; the game ended.

## Files

- Results: mine-1..4, opp-1..4, opp-4b; counts.log.
- Replays: branch `claude/project-thread-fo2qdk` at `7c075ae63` (9 batch folders su-h2h-{mine,opp}-e45904b-p1..4 and p4b; on-site.txt
  lists them). Not on main.
- scripts/: the finding's trace scripts (trace.py, cls.py, pos.py for range and facing, rng3.py for ranges, rules.py for the rule rows
  and NO CHARGE WHY classes) and the charge worth batch's (merge.py, h.py, remap.py). compare-all.md from scripts/compare-batches.py
  (A = mine arm, B = opp arm); kpis-on-v-off.md remapped to rules on / main.
