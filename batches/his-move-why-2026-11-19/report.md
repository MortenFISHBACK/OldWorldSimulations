# His move why: report (2026-11-19, logging only)

Head c1e47a93c on claude/project-thread-60g6hv. Everything-on side (overhaul) against true simpler, 72 of try 15's pairs played both
ways = **144 games, all ended, none failed**. Two logging rows were on for the everything-on side: HIS MOVE WHY (one row per enemy unit
whose move we assumed, written at his own Movement phase) and PROMISE BELOW ZERO. This batch does not judge play; it only counts.
Batches: hmw-mine-c1e47a9-p1, -p2 (overhaul = Mine), hmw-opp-c1e47a9-p1, -p2 (overhaul = Opponent).

## Verdict
1. **His real move matched the move we assumed in 46 of 100 cases** (2,329 of 5,047). "Stand" is right 71% of the time; an assumed
   move or march only 27-32%; an assumed charge 54%.
2. **Our own turn moving off the plan is NOT the main cause.** In turns where our units ended where our table put them, his move still
   differed 54% of the time, against 56% when our turn changed the board. So our run of his chooser and his real chooser disagree on
   (nearly) the same board: that points at the two not being the same decision (question 1a: same code path), not at the board.
3. The biggest single miss is **the same kind of job on another target** (mostly "advance on": 408 rows, 8% of all), then the right job
   at another spot (773 rows, 15%, about half more than 3" off), then a switch of job (advance / close in to charge / shoot, ~10%).
4. **Promised charges turned down below zero (39 rows, 31 games): the risk, not the gain, sinks them.** The gain now (~80 VP mean) is
   about what the promise said (~75 VP at 90%); the risk is ~158 VP. RISK BY ARC is the most negative part in 14 of 39, and the largest
   negative share on average (-53 VP a row); NO DOUBLE ROUNDS (-33) and HONEST WORTH (-23) are on nearly every row.
5. Promises match try 15: **claimed 88 in 100, came 25** (try 15: 86 v 23). 499 promises, 3.5 a game.

## (1) His move against the move we assumed (5,047 rows)
| What he did | Rows | Share | Our turn had changed the board |
| --- | --- | --- | --- |
| As assumed | 2,329 | 46% | - |
| Other job (his row names another job or target) | 1,401 | 28% | 69% |
| Same job, other spot (more than 1" off) | 773 | 15% | 69% |
| Charged where we did not assume that charge | 338 | 7% | 68% |
| Assumed to charge, did not charge | 152 | 3% | 66% |
| No objective row of his for the unit | 39 | 1% | 67% |
| Our sum named the action, not his chooser | 15 | 0.3% | 100% |

By what we assumed:
| Assumed | Rows | As assumed | Other job | Other spot | Charged instead | Did not charge |
| --- | --- | --- | --- | --- | --- | --- |
| stand | 1,765 | 71% | 19% | 8% | 3% | - |
| move | 1,545 | 32% | 36% | 22% | 9% | - |
| march | 1,292 | 27% | 39% | 23% | 8% | - |
| charge | 445 | 54% | - | - | 11% (other target) | 34% |

Does our own turn explain it? (per enemy Movement phase; "changed" = the row says some of our units were not where our rows put them)
| Our turn | His phases | Rows | Not as assumed |
| --- | --- | --- | --- |
| Changed the board | 504 | 3,381 | 56% |
| Did not change it (phases with at least one miss) | 254 | 1,543 | 54% |
| Did not change it, every unit as assumed | 29 | 123 | 0% |
Even counting the 29 clean phases with the unchanged ones, the miss rate on an unchanged board is about 50%.

### The misses grouped, biggest first (with example games: part/game, his turn, unit)
| Reason (from the row text) | Rows | Share of all | Examples |
| --- | --- | --- | --- |
| Other job: same kind (advance on), another target | 408 | 8.1% | mine-1/L0102-6-1 t1 Gors (Obsidian Lodestone); mine-2/L0206-2-1 t1 Dwarf Warriors; opp-1/L0135-3-1 t4 Harpies; opp-2/L0122-2-1 t3 Gors |
| Same job, other spot 3-6" | 251 | 5.0% | mine-1/L0102-6-1 t1 Razorgor 2; mine-2/L0106-4-1 t2 Thunderers 2; opp-1/L0118-4-1 t3 Gors; opp-2/L0206-2-1 t3 Wargor |
| Same job, other spot 1-3" | 235 | 4.7% | mine-1/L0102-6-1 t1 Razorgor 3; mine-2/L0106-4-1 t2 Rangers; opp-1/L0135-3-1 t5 Primal Warherd; opp-2/L0122-2-1 t2 Ungors 1 |
| Same job, other spot 6-12" | 221 | 4.4% | mine-1/L0102-6-1 t3 Razorgor 2; mine-2/L0106-4-1 t5 Gyrobomber; opp-1/L0102-6-1 t6 Ungors 1; opp-2/L0206-2-1 t5 Wargor |
| Other job: close in to charge -> advance on | 160 | 3.2% | mine-1/L0102-6-1 t2 Tuskgor Chariot 1; mine-2/L0206-2-1 t1 Gyrobomber; opp-1/L0218-2-1 t1 Tuskgor Chariot 2; opp-2/L0206-2-1 t6 Razorgor 2 |
| Assumed charge, did not charge | 152 | 3.0% | mine-1/L0118-4-1 t4 Hunter; mine-2/L0106-4-1 t3 Gyrobomber; opp-1/L0118-4-1 t4 Harpies; opp-2/L0122-2-1 t2 Harpies |
| Charged; we assumed a move | 138 | 2.7% | mine-1/L0102-6-1 t2 Razorgor 1; mine-2/L0122-2-1 t2 Skeleton Chariot; opp-1/L0102-6-1 t4 Primal Warherd; opp-2/L0206-2-1 t3 Razorgor 1 |
| Other job: advance on -> shoot | 118 | 2.3% | mine-1/L0102-6-1 t1 Gors (Ring of Doom); mine-2/L0106-4-1 t5 Thunderers 2; opp-1/L0118-4-1 t4 Ungors 2; opp-2/L0106-4-1 t1 Primal Warherd |
| Other job: advance on -> close in to charge | 104 | 2.1% | mine-1/L0102-6-1 t4 Tuskgor Chariot 2; mine-2/L0106-4-1 t4 Gyrobomber; opp-1/L0733-1-1 t4 General of the Empire; opp-2/L0206-2-1 t3 Razorgor 2 |
| Charged; we assumed a march | 99 | 2.0% | mine-1/L0102-6-1 t2 Wargor; mine-2/L0106-4-1 t2 Doomseeker; opp-1/L0235-1-1 t4 Wargor; opp-2/L0528-6-1 t6 Doomseeker |
| Other job: same kind (close in to charge), another target | 93 | 1.8% | mine-1/L0118-4-1 t4 Ironguts; mine-2/L0122-2-1 t4 Necrosphinx 1; opp-1/L0218-2-1 t2 Tuskgor Chariot 2; opp-2/L0206-2-1 t4 Razorgor 3 |
| Other job: shoot -> advance on | 84 | 1.7% | mine-1/L0118-4-1 t3 Ironguts; mine-2/L0106-4-1 t2 Gyrocopter; opp-1/L0118-4-1 t4 Primal Warherd; opp-2/L0106-4-1 t3 Primal Warherd |
| Same job, other spot 12"+ | 66 | 1.3% | mine-1/L0102-6-1 t1 Razorgor 1; mine-2/L0307-1-1 t1 General of the Empire; opp-1/L0102-6-1 t6 Ungors 2; opp-2/L0122-2-1 t2 Ungors 2 |
| Charged; we assumed another target | 51 | 1.0% | mine-1/L0218-2-1 t2 Sabretusks 2; mine-2/L0222-6-1 t2 Necrosphinx 1; opp-1/L0218-2-1 t4 Razorgor 1; opp-2/L0632-2-1 t3 Doomseeker |
| Charged; we assumed it would stand | 50 | 1.0% | mine-1/L0135-3-1 t3 Wardancers 2; mine-2/L0122-2-1 t3 Skeleton Chariot; opp-1/L0102-6-1 t5 Primal Warherd; opp-2/L1026-6-1 t6 Shugengan Lord |
| Other job: same kind (shoot), another target | 40 | 0.8% | mine-1/L0319-1-1 t6 Orc Boar Boys; mine-2/L0721-1-1 t2 Weapon Team 1; opp-1/L0118-4-1 t6 Primal Warherd; opp-2/L0632-2-1 t6 Gyrobomber |
The row says WHAT he did differently; it does not say WHY his chooser differed from our run of it (the row has his row's summary, not
his figures). That needs a replay of one of the example games with both choosers' figures side by side.

## (2) Promised charges turned down below zero (39 rows in 31 games; 24 on the Opponent arm, 15 on Mine)
Mean: promised ~75 VP at 90%; now gain ~80 VP, risk ~158 VP, worth ~-73 VP. Gain fell below the promise in 16 of 39.

Most negative part of the sum (FIVE ACTION left out: it is the total itself in 30 of 39 rows):
| Most negative part | Rows | Examples |
| --- | --- | --- |
| RISK BY ARC | 14 | mine-1/L1114-4-1 t2; mine-2/L1135-1-1 t3; opp-1/L1625-5-1 t6; opp-1/L2127-3-1 t2 |
| NO DOUBLE ROUNDS | 5 | mine-2/L0206-2-1 t5; opp-1/L1527-3-1 t2; opp-1/L0118-4-1 t4; opp-2/L1531-1-1 t2 |
| HONEST WORTH | 4 | mine-1/L2531-5-1 t3; mine-2/L1323-3-1 t4; opp-1/L2025-3-1 t5; opp-2/L1927-1-1 t2 |
| GIVES UP | 3 | mine-1/L0717-3-1 t2; opp-1/L0524-2-1 t3; opp-1/L0102-6-1 t2 |
| JOINT CHARGE NOW | 3 | mine-1/L1431-3-1 t2; mine-2/L1435-1-1 t5; opp-2/L0307-1-1 t5 |
| WHAT THE JOINER ADDS | 3 | mine-2/L1927-1-1 t4; mine-1/L2025-3-1 t4; opp-1/L0524-2-1 t5 |
| FOUR ROUNDS / CHARGER SLAIN LOST / STAND AND SHOOT / RUN DOWN | 2 / 2 / 2 / 1 | mine-2/L0206-2-1 t2; opp-1/L0102-6-1 t4; opp-2/L0810-6-1 t3; opp-1/L1823-5-1 t3 |

Each part's share, per row on average (negative first):
| Part | On rows | Negative on | Mean VP a row |
| --- | --- | --- | --- |
| RISK BY ARC | 33 | 22 | -52.9 |
| NO DOUBLE ROUNDS | 30 | 30 | -33.0 |
| HONEST WORTH | 33 | 33 | -23.2 |
| GIVES UP | 7 | 7 | -13.2 |
| WHAT THE JOINER ADDS | 10 | 9 | -7.9 |
| STAND AND SHOOT | 14 | 14 | -7.6 |
| JOINT CHARGE NOW | 8 | 7 | -5.2 |
| RUN DOWN | 23 | 23 | -4.8 |
| CHARGER SLAIN LOST | 8 | 8 | -4.5 |
| FOUR ROUNDS (positive) | 38 | - | +35.4 |
| TIED UP BY THE SUM (positive) | 9 | - | +23.0 |
| OVERRUNS AWAY (positive) | 15 | - | +17.8 |

## (3) Promises claimed v came (scripts/analysis/promises.py)
| | This batch (144) | Try 15 (69) |
| --- | --- | --- |
| Promises | 499 (3.5 a game) | 211 (3.1) |
| Claimed v came, in 100 | 88 v 25 | 86 v 23 |
| 95-100% band came | 30% | 31% |
| His move within 1" of the assumed place | 41% | 42% |
Matches try 15, as expected (nothing in play changed).

## Leads (for the build to check in code; not checked)
1. Our run of his chooser and his real chooser disagree about half the time even when our own turn went as planned. Lead: the two are
   not the same decision (inputs or code path), which is question 1a's default.
2. "Advance on" another target is the largest single group: lead that the target pick of his advance differs (e.g. a nearest-v-best
   target rule, or a target list read before/after our moves).
3. A promised charge's risk roughly doubles its gain by the time it is due: RISK BY ARC was either not in the promise's own sum or is
   much larger a turn later. Compare one example's promise row with its below-zero row.
4. WHAT THE JOINER ADDS appears twice in the parts of 5 of 39 rows: possibly counted twice.
5. FIVE ACTION is not equal to the total in 9 of 39 rows: 8 of those 9 carry JOINT CHARGE NOW (a joint charge's own sum on top).
