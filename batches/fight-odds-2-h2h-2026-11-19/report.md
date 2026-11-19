# Fight odds 2: the new fight estimate v the old one (2026-11-19), 288 games

Head dde35ebb (branch claude/project-thread-1s0bz5). Both sides true simpler (worked-out-chances, five-action, standing-by-numbers off
for both). NEW = exact-round, one-joint-figure and challenge-odds (duel-stops-at-the-kill, duellist-one-model, one-challenge-test) ON;
OLD = all of those off. Same 144 WTC pairs as fight odds 1, seed 1, scenarios mix, both ways. Switches checked in all 8 parts from the
merged logs: rules-off names the five new-estimate tags for the old side only, and EXACT ROUND rows appear on the new side only
(182-328 a part, 0 on the other side). Part 8 (opp-4) included: Mine 0 rows, Opponent 225.
286 of 288 games ended; 2 stopped with a sim finding (below).

## Verdict
**The challenge fix works: the new side no longer throws lone heroes at fights it should lose.** Lone characters charging at a claim
under 20% fell from 19 (old) to 2 (new), and challenge fights from 94 to 29. **Overall the claims are not closer:** Brier 0.131 new v
0.125 old (lower is better), band gap 3.9 v 1.8 points. The new side's weak spot is the under-20% band without a challenge (mostly
non-hero units into chaff, war machines and lone characters): claimed 11%, won 41% (17 fights). VP margin -57 ±148: noise.

## 1. First round won when charging: claimed v happened (repo matching: side, turn, chargers AND target)
| Claimed win | NEW fights | NEW claimed v won | OLD fights | OLD claimed v won |
|---|---|---|---|---|
| 0-20% | 33 | 9% v 36% | 43 | 5% v 12% |
| 20-40% | 24 | 28% v 42% | 39 | 29% v 33% |
| 40-60% | 66 | 51% v 55% | 85 | 51% v 56% |
| 60-80% | 112 | 70% v 70% | 143 | 70% v 69% |
| 80-100% | 415 | 94% v 92% | 445 | 92% v 93% |
| All | 650 | 79% v 80% | 755 | 75% v 76% |

## 2. Challenges and one unit charging alone (scripts/challenge-fights.py, stricter match, fewer fights)
| Split | NEW claimed v won (fights) | OLD claimed v won (fights) |
|---|---|---|
| Challenge fought, any band | 60% v 48% (29) | 56% v 49% (94) |
| Challenge, claimed 80%+ | 89% v 78% (9) | 89% v 81% (27) |
| Challenge 80%+, hero's later blows cut off | 87% v 50% (2) | 91% v 73% (15) |
| One unit alone, claimed 80%+ | 93% v 87% (169) | 92% v 90% (212) |
| One unit alone, claimed under 20% | 10% v 37% (19) | 5% v 18% (28) |
| Under 20%, challenge fought | 3% v 0% (2) | 5% v 24% (17) |
| Under 20%, no challenge | 11% v 41% (17) | 3% v 9% (11) |
| Under 20%, "slain or flees" 40%+ (cause B) | none | 4% v 29% (14) |

## 3. Lone heroes (characters) charging a unit at a claim under 20%
| | NEW | OLD |
|---|---|---|
| Charges | 2 | 19 |
| Won first round | 1 (Orc Warboss into Ironguts, 11 v 1) | 5 |
| Lost and fled | 1 (Black Orc Warboss into Thunderers) | 7 |
At 80%+ the hero split is not in the logs without unit types; the challenge 80%+ rows above are the nearest (9 v 27 fights).

## 4. Joint charges (two or more chargers)
NEW 126 fights claimed 87% v won 87%, Brier 0.111; OLD 109 fights 81% v 84%, Brier 0.108. NEW 60-80% band: 12 fights 69% v 42% (small).

## 5. Brier score (lower is better)
| | NEW | OLD |
|---|---|---|
| All charged fights | 0.131 | 0.125 |
| One charger | 0.136 | 0.128 |
| Two or more | 0.111 | 0.108 |
| Fight odds 1 (for reference) | ON 0.142 | OFF 0.133 |

## Headline
| | NEW | OLD |
|---|---|---|
| Charges declared a game | 4.4 | 4.8 |
| Net points per charged fight (2 turns) | +86 ±11 | +80 ±10 |
| Points lost a game | 722 | 682 |
| Own units caught in flank/rear a game | 1.64 | 1.60 |
| VP margin (NEW minus OLD) | -57 ±148 (noise) | |
Games won/lost/drawn by NEW: 107 / 115 / 64 (286 ended).

## Sim findings (2 games did not end)
- S-d8a88d new: opp-2 L2429-5-1 (A Chance Encounter), turn 2 Opponent (NEW side) Strategy: "The computer stopped: '0' cannot be greater
  than -4." An exception in the computer's own code; whether the new estimate raises it is not checked.
- S-59a570 new: opp-4 L1719-3-1 (Drawn Battlelines), turn 3 Mine (OLD side) Combat: "found no move it may make with Saurus Oldblood
  (Blade of Revered Tzunki) after the combat" (aftermath stuck).

## Leads (not checked in code)
1. NEW under-20% fights without a challenge win 41% (17): Necrosphinx, Maneaters, Sabretusks, Fell Bats, Orc Warboss into small or
   fragile targets. The exact round may under-rate a charger against a target with few models or no ranks (wipe-out or static points).
2. The old side's 19 lone-hero charges under 20% match the finding's cause B ("slain or flees" 40-92%); the new side has none, so B is fixed.

## Where the data is
Scripts here: scripts/claims-final.py (band tables), scripts/challenge-fights.py (challenge, lone, under-20% lists), scripts/build.py +
flank.py (charges, flank), scripts/report.py (headline), early-reading-62.md (the 62-game check).
Game logs: see the archive line at the end once archived. Replays: see the replay line at the end.
