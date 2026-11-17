# Honest next-turn chances against simpler pricing: head-to-head (2026-11-17)

**Verdict: honest chances plays slightly worse than simpler pricing alone, at -79 VP a game, give or take 98.** That is inside
the noise, but below the keep line (not worse than -30). It is worse on all five headline numbers. Its figures for next turn's charge
are now close to what happens (counted 20%, happened 14%), but that did not turn into better play.

Batch: 288 games, all ended (no engine errors, no stuck games, no sim findings). These were the same 144 DKTC pairs as the five-action and
joint-charge batches (scripted v scripted, seed 1, scenarios mix), and each pair was played both ways. The build was
`claude/project-thread-3d2v3f` at `31c41bfb`. One side had `honest-chances` (measured-next-charge + run-down) switched off. Pairs: 60 ahead,
83 behind, 1 level.

## 1. Headline

| # | Number | **Honest chances** | **Simpler pricing** |
| --- | --- | --- | --- |
| 1 | VP margin per game | **-79 ±98** | +79 |
| 2 | First round won when charging | 72% | 77% |
| 3 | Net points per charged fight | +92 | +103 |
| 4 | Points lost per game | 759 | 708 |
| 5 | Own free units caught in flank or rear (per game) | 0.62 | 0.51 |

Honest as Mine scored -244 and as Opponent +85. Going first it scored -88, going second -71. Charged fights per game were 2.8 for honest and 3.0 for simpler.

## 2. VP by source (per game)

| Source | Honest | Simpler |
| --- | --- | --- |
| Objectives | 558 | 585 |
| Kills | 748 | 796 |
| Leaders | 53 | 58 |

## 3. What the rules did

| Per game, honest side only | Rows | Changed the pick |
| --- | --- | --- |
| MEASURED NEXT CHARGE | 9.4 | 1.4 |
| RUN DOWN | 1.9 | 0.04 |

Run-down almost never changes a pick. Nearly all of the difference comes from measured-next-charge. Neither tag appears on the simpler side.

| Per game | Honest | Simpler |
| --- | --- | --- |
| Gain claimed (taken jobs) | 1,875 | 2,079 |
| Risk claimed (taken jobs) | 820 | 770 |
| Points actually lost | 759 | 708 |

## 4. Claims against what happened (first table, from the split log)

### Next turn's charge

| Pick | Side | Picks | Counted chance | Happened |
| --- | --- | --- | --- | --- |
| Close in to charge X next turn: contact with X | honest | 852 | 20% | 14% |
| | simpler | 1,408 | 43% | 12% |
| Close in: charged X at all next turn | honest | 852 | 20% | 17% |
| | simpler | 1,408 | 43% | 15% |
| Move spot counted for next turn's charge (measured row) | honest | 1,023 | 20% | 15% |

The reach printed in the close-in bracket (about 90%) is far from the 12-14% contact. The 0.22 factor is what brings the honest figure close.

### Charge picks (charge declared as picked)

| Chance logged on the pick | Side | Picks | Claimed | Happened |
| --- | --- | --- | --- | --- |
| Charge declared on the picked target | honest / simpler | 1,125 / 1,216 | 100% | 89% / 87% |
| Reach (all declared) | honest / simpler | 998 / 1,057 | 90% / 91% | 65% / 68% |
| Reach (target did not flee as its reaction) | honest / simpler | 710 / 776 | 89% / 91% | 91% / 92% |
| Win the first round | honest / simpler | 459 / 497 | 66% / 66% | 71% / 74% |
| Target slain | honest / simpler | 459 / 497 | 18% / 21% | 16% / 16% |
| Target flees | honest / simpler | 459 / 497 | 22% / 21% | 11% / 13% |
| Target falls back in good order | honest / simpler | 459 / 497 | 15% / 15% | 5% / 7% |
| Target gives ground | honest / simpler | 459 / 497 | 28% / 30% | 19% / 20% |
| Any of the four (target loses) | honest / simpler | 459 / 497 | 83% / 86% | 51% / 56% |
| Stand & shoot wounds on the charger | honest / simpler | 998 / 1,057 | 0.17 / 0.20 | 0.07 / 0.05 |
| A broken (fleeing) target ends as points | honest / simpler | 52 / 67 | 82% / 84% | 67% / 85% |

How to read it:
- **Reach is right once the target stands.** About a third of declared charges miss because the target flees as its reaction. The odds do
  not count that (charge-outcomes option 6, not built).
- **The outcome chances are too high.** The computer expects the target to lose (slain, flee, fall back or give ground) 83-86% of the time,
  but it happens 51-56% of the time. Flees and falls back are about twice too high. Slain is about right.
- Stand & shoot is over-counted about 3x.
- "Ends as points" is close for simpler and 15 points too high for honest, on few cases.

Limits of this first table: the outcome rows cover the 459/497 charges whose first-round result line could be tied to the charger.
"Happened" is read from the break-test lines of the charge turn. A flee "ends as points" when the unit is later caught or destroyed, or
flees off the table. Script: `scripts/claims.py`. Headline: `scripts/headline.py` (compare-batches.py charged_fights, flank_charges.py).

## 5. Bugs

None. All 288 games ended, with no engine errors, no time-limit stops and no sim findings.

## 6. Where the data is

- Full game logs (split log included) for all 288 games are in git: the OldWorldSimulations archive (see the end of this report), and
  simulation-data `measurements/hc-{mine,opp}-31c41bf-p{1..4}`.
- The per-game copies on this mount were checked identical to simulation-data and removed (project file limit).
- Archive: MortenFISHBACK/OldWorldSimulations, branch `claude/project-thread-god4i0`, folder `batches/honest-chances-h2h-2026-11-17/`
  (one tar.gz per part, SHA256SUMS, FILECOUNTS.txt, scripts/). The branch is not merged into the archive's main, because this thread may only push its own branch.
