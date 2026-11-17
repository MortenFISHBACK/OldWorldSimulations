# Five options with worked-out chances v simpler pricing (stopped early, 17 Nov 2026)

**Verdict: clearly worse, and the odds are not right.** The new side loses by 490 VP a game (±182) over 110 games. It almost never
charges: a charge is offered half as often and, when offered, usually loses to a move toward a charge "next turn" that then happens
4% of the time. Stopped at 110 of 288 games on Morten's word (the margin is clear); the cause goes to the build thread.

Build `9ba9963da` (branch claude/project-thread-60g6hv). Same 144 DKTC pairs as worked-out-chances-h2h-2026-11-17, both ways.
New side: everything on. Off side (exact list): `worked-out-chances,five-action,standing-by-numbers@<side>` = plain simpler pricing.
Smoke game: the new rules wrote rows on the tested side only.

## 1. Are the odds right?

**Charge now**

| | New | Simpler |
| --- | --- | --- |
| Decisions with a charge on offer | 305 of 5,013 (6%) | 663 of 5,264 (13%) |
| Charge taken when on offer | 116 (38%) | 492 (74%) |
| Charges declared | 150 | 528 |
| Charges that made contact | 107 | 364 |

The 189 charges passed over went to: move 81, march 59, stand 31, shoot 13, support 5. Picked option's claimed worth median +39 VP;
best charge on offer median −6 VP; 54% of them ≤ 0, although their own win chance was mostly 62-92%. What turns them negative is the
"after" term (−11 to −222 VP in the examples) and the risk, not the fight (examples in the message to the build thread).

**Move to charge (next turn)**

| Claimed worth of the move | Picks | Charged that target next round | Any charge next round |
| --- | --- | --- | --- |
| 0-25 VP | 162 | 4% | 11% |
| 25-50 | 131 | 4% | 5% |
| 50-100 | 200 | 2% | 6% |
| 100+ | 245 | 6% | 10% |
| All | 738 (median +63) | 4% | 8% |

The claimed worth does not track what happens at all: the higher the claim, the charge is no more likely. This is the biggest gap.

**Standing still**: 14% of new-side decisions v 14% "hold" on the simpler side. Not the old 70%. The STANDS STILL rows give the
two sums compared, not a reason in words, so "what they were doing" cannot be split further from this build's log.

Not measured in this short run: enemy-charge risk (his win chance >50%), shoot jobs that never fired, charges left off by reason.

## 2. Headline

| | New | Simpler |
| --- | --- | --- |
| VP margin | −490 ±182 | |
| Won / lost / drawn | 22 / 69 / 19 | |
| Points lost a game | 679 | 410 |

VP by source (new minus simpler, a game): objectives −212, kills −263, leaders −17.

Data: `<arm-N>/batch.tgz` here (110 games); script `scripts/report.py <folder with the unpacked parts>`.
