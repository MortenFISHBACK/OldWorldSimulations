# Fight odds 1: exact first round ON v OFF (2026-11-19), 288 games

Head a6e9b4f87 (branch claude/project-thread-1s0bz5, fight odds head 2). Both sides true simpler (worked-out-chances, five-action,
standing-by-numbers off for both). ON = `exact-round` on, OFF = the old bell-curve estimate. 144 WTC pairs, seed 1, scenarios mix,
played both ways. Switch checked in all 8 parts: EXACT ROUND rows on the ON side only (73-146 a part, 0 on the other side).
No crashes, no time limits.

## Verdict
**No better in real games.** With the exact round on, the first-round claims match what happens no more closely than with it off:
both are already close overall (ON claims 76% and wins 76%; OFF claims 75% and wins 78%), the gap across bands is 4.2 points for both,
and the Brier score is slightly worse with it on (0.142 v 0.133; lower is better). The one clear miss is the same on both sides:
fights claimed under 20% are won about a quarter of the time (ON 7% v 26%, OFF 5% v 20%). Charging results are the same within noise.

## First round won when charging: claimed v happened (matched the repo way: same side, turn, chargers and target)
| Claimed win | ON fights | ON claimed v won | OFF fights | OFF claimed v won |
|---|---|---|---|---|
| 0-20% | 50 | 7% v 26% | 40 | 5% v 20% |
| 20-40% | 38 | 29% v 29% | 41 | 30% v 37% |
| 40-60% | 63 | 53% v 59% | 90 | 50% v 63% |
| 60-80% | 139 | 71% v 71% | 134 | 71% v 75% |
| 80-100% | 426 | 94% v 90% | 421 | 92% v 91% |
| All | 716 | 76% v 76% | 726 | 75% v 78% |

| Split | ON claimed v won (fights), Brier | OFF claimed v won (fights), Brier |
|---|---|---|
| One charger | 75% v 74% (582), 0.146 | 73% v 76% (611), 0.138 |
| Two or more chargers (head 3, not fixed yet) | 84% v 84% (134), 0.123 | 85% v 88% (115), 0.105 |

All claims here are the charger's, made the same turn as the charge; the logs hold no claim for the charged side and none for a fight
claimed a turn earlier (promises are counted elsewhere), so those splits cannot be made from these logs.

## Combat result and target breaks
No expected combat result is logged per charge, so "claimed v happened" cannot be given for it. Happened: the average result margin
rises with the claimed band on both sides (ON +2.5, OFF +2.8 overall).
Target slain or flees (claim from the job line, target checked; happened = wiped or failed its round-1 Break test, which also counts
falling back in good order, so "happened" is a little high): single-charger fights ON 41% v 51%, OFF 45% v 51%.

## Headline
| | ON | OFF |
|---|---|---|
| Charges declared a game | 4.8 | 4.7 |
| Net points per charged fight (2 turns) | +71 ±10 | +80 ±10 |
| Points lost a game | 725 | 706 |
| Own units caught in flank/rear a game | 1.62 | 1.66 |
| VP margin (ON minus OFF) | -40 ±153 (noise) | |
Games won/lost/drawn by ON: 110 / 117 / 61.

## Leads (not checked in code)
1. Both sides' low-band claims (under 20%) win 20-26%. Both estimates may miss something the game gives the charger in a fight it
   "should" lose (e.g. the defender's position or rank count at contact, or a flee before the fight), since it is shared by both.
2. The 39-fight harness improved from 5 to 20 matches, but the fights the general actually picks are mostly 80%+ claims, where both
   estimates were already within 1-4 points; the harness's hard fights are rare in real play.

## Where the data is
Readings: early-reading-59.md (its tables are WRONG, see its correction line), this report. Scripts: scripts/claims-final.py
(the band tables; needs the repo's scripts/compare-batches.py), scripts/claims-by-band.py (the build thread's original), scripts/fo1.py.
