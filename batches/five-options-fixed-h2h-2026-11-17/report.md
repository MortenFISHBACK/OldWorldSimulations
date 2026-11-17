# Fixed five options v simpler pricing (stopped early, 17 Nov 2026)

**Verdict: still clearly worse, and the odds are still not right.** The new side loses by 423 VP a game (±190) over 72 games.
The move-to-charge fix helped (the promised charge now comes 15% of the time, was 4%), but it is still promised at 83%. The new side
still charges a third as often as simpler pricing. Stopped at 72 of 288 games on Morten's rule at the 50-game check (margin still large).

Build `21301cb47` (branch claude/project-thread-60g6hv). Same DKTC pairs as the stopped batch, both ways. New side: everything on.
Off side: `worked-out-chances,five-action,standing-by-numbers@<side>` = true simpler pricing. Smoke game and all 8 parts checked:
the new rules wrote rows on the new side only.

## 1. Are the odds right?

**Move to charge next turn** (new side, 162 picks), by distance to the target at the start of the next turn:

| Distance | Picks | Promised | Charged that target |
| --- | --- | --- | --- |
| under 6" | 14 | 94% | 14% |
| 6-12" | 63 | 90% | 21% |
| 12-18" | 41 | 81% | 15% |
| 18-24" | 33 | 73% | 12% |
| 24"+ | 11 | 63% | 0% |
| All | 162 | 83% | 15% |

Why it did not come (148 promises where both units were still there): charged 25; offered but another option taken 14;
**the same charge priced below zero next turn and dropped 38** (median −95 VP, while the promise was priced at +VP and was
priced again the next turn); path or sight blocked 17; out of reach about 48 (25 after the target moved, 23 with it standing).

**Charge now** (new side, 84 picks)

| | Claimed | Happened |
| --- | --- | --- |
| Reach (declared to contact) | 92% | 67% |
| First round won | 63% | 63% |
| Target destroyed (by end of the next own turn) | 37% | 48% |
| Charger lost | 25% | 25% |

Simpler side: first round won 68% claimed v 77%.

**Charges**

| | New | Simpler |
| --- | --- | --- |
| Charge on offer, per unit decision | 6% | 13% |
| Charge picked when on offer | 43% | 72% |
| Charges declared a game | 1.5 | 4.8 |
| Net points per charged fight | +64 | +79 |

**Standing still**: 1,041 STANDS STILL rows on the new side: 668 stand to shoot, 356 a tie with moving (both worth the same),
17 waiting for a charge next turn.

## 2. Headline

| | New | Simpler |
| --- | --- | --- |
| VP margin | −423 ±190 | |
| Won / lost / drawn | 17 / 40 / 15 | |
| Points lost a game | 649 | 413 |

## 3. Next root cause (what the logs point at)

The promise of a charge next turn and the charge now are still priced by different sums. Example: L0319-1-1 turn 4, Iron Daemon 1
promises +84 VP on Orc Boar Boys at 100%; next turn the charge now is −115 VP and the move "next turn" is priced +509, so it moves
again. 38 such cases are listed in promised-then-below-zero.md (first 55 games: 39). Second: the reach figure does not check path or
sight (17), and does not expect the target to move (25).

Data: `<arm-N>/batch.tgz` here; scripts: scripts/fixed.py, report.py, build.py + odds.py.
