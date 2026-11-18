# Early reading at 52 games (2026-11-18 03:07 UTC), build 6439d0d19 (try 5: his charge list, his shot list, tied up by the sum)

Switch side checked: smoke game (Mine only: HIS SHOT LIST 62, FIVE ACTION 46) and part 8's report (rows on the new side only).
Scripts in scripts/: report.py, risk.py, build.py + odds.py (as try 4); new: idle2.py, notrisk4.py, shotgap3.py, promise6.py.

**Measuring note.** Three of try 4's own scripts (notrisk3, shotgap2, promise5) found "the enemy turn" by the first line of the other side,
which cuts a turn short when the other side writes a line in our Strategy phase (a dispel); promise5 also read the job list from the
CANDIDATES line, which is cut ("| 1 more"). The new scripts use the turn windows of job_claims.py and the full JOB SPLIT row.
On try 5's games the old scripts gave "51% of kept promises not on the own list" and "107 VP a game of shot claim on enemies that made
no lists"; the fixed ones give 19% and 3 VP. Try 4's "541 of 1,043 not legal" and "58% of the shot claim where nobody could shoot" were
very likely inflated the same way. risk.py and odds.py were already right.

## 1. Risk of picked jobs: claimed v lost in the enemy turn after (a game)
| | claimed | lost | try 4 final |
| --- | --- | --- | --- |
| New, all | 570 | 374 | 907 v 439 |
| New, enemy charges | 348 | 180 (charged/fought) | 466 v 261 |
| New, shots + magic | 325 | 186 (128 shot + 58 magic) | 570 v 164 |
| Simpler, all | 670 | 341 | |

Enemy charges counted as risk (316, claimed 86% on average): he charged this unit 22%; charged another unit 18%; the charge was on his
weighed list but not taken 12%; not weighed at all 39%; we charged him first / he died / fled 9%. The claim is right that he CAN; it is
wrong that he WILL: the risk is his reach, not his choice.
Shots: of the shot claim, 60% sits on units that were then shot or cast at; 16% on units no shooter listed; 14% on a list but another
target picked.

The other direction (priced NO risk):
| | pairs | then hit this unit |
| --- | --- | --- |
| HIS SHOT LIST: "must move first" | 1,306 | 6% |
| HIS SHOT LIST: "outside its arc" | 697 | 9% |
| HIS SHOT LIST: "in a fight" | 141 | 6% |
| HIS CHARGE LIST: "cannot see it" etc. | 174 | 2% |
About 3 hits a game on units priced safe from that shooter (move-and-shoot, or turned into arc). Screens dying: not measured yet.

## 2. Charge next turn: promised v came
| | New | try 4 |
| --- | --- | --- |
| Move-to-charge picks; charged that target next turn | 229; 17% (promised ~90%) | 90 v 12 |
Of 162 kept promises (unit ended on the spot): charged it 38, **on offer next turn but not taken 70**, charged another 14,
not on its list 31 (target moved 12, target stood 19), in combat/fleeing 7, charged first by the enemy 2.

## 3. Charge odds
| | New | Simpler | try 4 |
| --- | --- | --- | --- |
| Contact when the target held | 81% | 86% | 85 v 80 |
| First round won: claimed v happened | 70% v 68% | 62% v 72% | 68 v 74 |

## 4. Headline (52 games)
| | New | Simpler | try 4 final |
| --- | --- | --- | --- |
| VP margin | −89 ±280 (W19 L19 D14) | | −283 ±127 |
| Charges declared a game | 2.9 | 4.1 | 2.8 v 5.1 |
| Charge picked when on offer | 41% (128 of 311) | 77% (199 of 258) | 45% v 74% |
| Points lost a game | 574 | 521 | 669 v 536 |
| Net points per charged fight | +60 | +52 | +76 v +80 |
| Own units caught in flank/rear, a game | 1.25 | 0.96 | 1.7 v 1.0 |

## Next root cause
**A charge on offer is put off for the same charge next turn, priced on a rosier sum.** 183 times a charge was on offer and not taken;
45 of them picked a move/march/stand "to charge the SAME target next turn", worth a median +78 VP against +39 for that charge now. The
charge now pays its other costs and after-term (e.g. Iron Daemon v Stone Trolls: reach 100%, win 98%, worth +112 after −40 other costs
and −80 after; it moved instead for +234 with "next turn: #12147"); the next-turn promise carries the full next-turn charge without the same
terms. Then the promise is kept and the charge is again on offer but not taken (70 of 162), so it comes 17%. A further 40 passed-over
charges went to "charge another target next turn". The honest sum prices a delayed charge with the same terms as the charge now, minus
what the turn's wait risks.
Second: the enemy charge risk is his reach (86%), not his choice (22% came); his own figures for his other jobs decide that.
