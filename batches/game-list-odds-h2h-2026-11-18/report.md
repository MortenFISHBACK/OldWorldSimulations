# Game-list odds against simpler pricing, try 5 (288 games, build 6439d0d19) - 2026-11-18

**Verdict: the new side still loses, −183 VP ±133 a game (W 99 / L 132 / D 57), better than try 4 (−283 ±127) but well outside the band.
The odds got closer: risk claimed 528 v 422 lost (try 4: 907 v 439), first round won 73% claimed v 78%, contact when held 84% on both
sides. The big gap left is the charge itself: a charge promised for next turn comes 16% of the time, mostly because the unit then puts
the same charge off again. The new side declares 3.4 charges a game against 5.0.**

Switch side checked in every part: rules-off lists the 35 rules of the group on the simpler side only, and FIVE ACTION / HIS SHOT LIST
rows appear on the new side only (about 5,600-6,500 rows a part, none on the other side).

## 1. Risk of the picked job: claimed v points lost in the enemy turn after (a game)
| | claimed | lost | try 4 |
| --- | --- | --- | --- |
| New, all | 528 | 422 | 907 v 439 |
| New, enemy charges | 378 | 251 (charged or fought) | 466 v 261 |
| New, shots + magic | 262 | 148 (119 shot + 29 magic) | 570 v 164 |
| Simpler, all | 749 | 418 | |

Enemy charges counted as a risk (2,025, claimed 87% on average): he charged this unit 21%, charged another unit 15%, had it on his
weighed list but did something else 11%, did not weigh it at all 41%, was charged by us first or died 10%.
His charge could happen; his choice is what is missing.

Shots: 188 VP a game of the claim is on units that were then shot or cast at. A further 43 VP is on units no enemy shooter listed, 40 VP
where he listed them but picked another target, and 31 VP on units charged instead.

Priced NO risk (the new lists):
| Reason given | pairs | then shot or charged this unit |
| --- | --- | --- |
| HIS SHOT LIST: "must move first" | 5,892 | 6% |
| HIS SHOT LIST: "outside its arc" | 3,582 | 5% |
| HIS SHOT LIST: "in a fight" | 1,022 | 2% |
| HIS CHARGE LIST (cannot see it, and similar) | 935 | 1.5% |
About 2.8 hits a game on units priced safe from that shooter (move-and-shoot weapons, or turned into arc). Screens dying was not measured.

## 2. Charge next turn: promised v came
| | New | try 4 |
| --- | --- | --- |
| Move-to-charge picks; charged that target next turn | 1,648; 16% (promised ~90%) | 1,408; 12% |

The unit stayed on the promised spot 1,218 times. In its next turn:

| What happened | times |
| --- | --- |
| Charged the promised target | 239 |
| **The charge was on offer but not taken** | **496** |
| Charged another target | 127 |
| Not on its list: the target stood | 154 |
| Not on its list: the target moved | 90 |
| Charged by the enemy first | 69 |

## 3. Charge odds
| | New | Simpler | try 4 |
| --- | --- | --- | --- |
| Contact when the target held | 84% | 84% | 85 v 80 |
| First round won: claimed v happened | 73% v 78% | 65% v 75% | 68 v 74 |
| Charge pick: claimed VP v net points over 2 turns | 127 v +59 | 89 v +56 | 137 v +63 |
| Shoot pick: claimed VP v VP of wounds done | 45 v 6 | 19 v 7 | 36 v 5 |

## 4. Headline
| | New | Simpler | try 4 |
| --- | --- | --- | --- |
| VP margin | −183 ±133 | | −283 ±127 |
| VP by source (new minus simpler) | objectives −90, kills −83 | | −144, −135 |
| Charges declared a game | 3.4 | 5.0 | 2.8 v 5.1 |
| Charge picked when on offer | 45% (850 of 1,882) | 78% (1,312 of 1,682) | 45% v 74% |
| Points lost a game | 690 | 606 | 669 v 536 |
| Net points per charged fight | +71 | +73 | +76 v +80 |
| Own units caught in flank/rear by a charge, a game | 1.63 | 1.23 | 1.7 v 1.0 |

## A measuring fix (affects try 4's reading)
Three of try 4's scripts (notrisk3, shotgap2, promise5) took the enemy turn to start at the first line the other side wrote. When the other
side writes a line in our Strategy phase (a dispel), that cut the turn short. promise5 also read the job list from the CANDIDATES line, which
the log cuts short ("| 1 more"). The fixed scripts (idle2, shotgap3, promise6, notrisk4 in scripts/) use the turn windows of job_claims.py and
the full JOB SPLIT row. So try 4's "541 of 1,043 kept promises not on the legal list" and "58% of the shot claim where nobody could shoot"
were very likely inflated. Here, with the fixed scripts, 21% of kept promises were off the list, and almost no shot claim sat on enemies that
made no lists. risk.py and odds.py were already right.

## Next root cause
**A charge on offer is put off for the same charge next turn, and the delay is priced on a rosier sum than the charge now.**
On the new side, 1,032 charges were on offer and not taken. 282 of them picked a move, march or stand "to charge the SAME target next turn",
worth a median +113 VP, against +74 VP for making that charge at once. A further 312 went to "charge another target next turn".
The charge now pays its other costs and the after-term. Example: Iron Daemon against Stone Trolls had reach 100% and a 98% win chance,
worth +112 VP after −39 other costs and −80 after. It moved instead, for +234 VP, with "next turn: #12147". The next-turn promise carries the
next-turn charge without those terms. Next turn the charge is on offer again (496 of 1,218 kept promises) and is again not taken. So the
promise comes 16% of the time, charges fall to 3.4 a game, and objectives and kills both suffer.
The honest sum prices a charge made next turn with the same terms as the charge now, plus what the turn of waiting risks.

Second cause: the enemy-charge risk is his reach (87%), not his choice (21% came). His own figures for his other jobs decide that choice.

Replays and archive: see the end of this file.

Replays: WarhammerOldWorldSimulator branch claude/project-thread-dlmmhz (commit 086142e6e), folders deploy/sim-replays/t5-mine-6439d0d-p1..4
and t5-opp-6439d0d-p1..4 (on-site.txt lists these 8). Archive: MortenFISHBACK/OldWorldSimulations, branch claude/project-thread-dlmmhz,
batches/game-list-odds-h2h-2026-11-18/ (one tar.gz per part + scripts.tar.gz, SHA256SUMS).
