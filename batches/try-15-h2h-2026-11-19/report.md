# Try 15 against true simpler: final report (2026-11-19, stopped at 57 games)

Head 9aabb0675 on claude/project-thread-60g6hv: the overhaul plus steps 0-3 of the promise finding (march of the table, promise holds
the spot, promise shot away, own cast first, promise in steps). New side = everything on; simpler = worked-out-chances, five-action,
standing-by-numbers off. Same pairs as tries 9-14, both ways. Stopped by the coordinator at 01:36 UTC under the standing rule (known fault
unchanged at the 57-game reading, early-reading-57.md). 69 finished games, none failed. Try 14 (61 games) in brackets.
Promises counted with scripts/analysis/promises.py (PROMISE PLANNED rows; KEPT and NOT KEPT both).

## Verdict
**The promise fault is unchanged:** 86 claimed, 23 came in 100 (88 v 26). 211 promises, 3.1 a game (2.4). The claim does not fall
toward the result: 134 of 211 promises still say 95-100%, and 31% of those came. The step that is off is "in reach after his turn"
(93% claimed). A unit ending off its spot did not drop (15-21 in 100, was 14). VP -14 ±268 is noise.

## Claimed v came, by band
| Claimed | Promises | Came |
| --- | --- | --- |
| 0-50% | 26 | 1 (4%) |
| 50-75% | 21 | 2 (10%) |
| 75-95% | 30 | 4 (13%) |
| 95-100% | 134 | 41 (31%) |

## Which step is off (PROMISE IN STEPS on 172 of 211 promises)
| Step | Promises | Claimed (mean) |
| --- | --- | --- |
| in reach after his turn | 172 | 92% |
| free of his charges | 172 | 98% |
| the fight still on | 12 | 33% |
| march test passed | 4 | 73% |
| still there after our turn's shots | 2 | 88% |

Nearly every promise is "in reach after his turn" x "free of his charges" and claims about 91%; about 25% came.

## Where the promise breaks (its own check rows)
| Check | Promises | Charge still there | Came |
| --- | --- | --- | --- |
| After our own moves, same turn | 123 | 73 (59%) | 25 |
| At the start of our next turn | 85 | 12 (14%) | 23 |

Off the spot by more than 1": 18 of 123 after our moves (13 by more than 3"), 18 of 85 at the start of the next turn.

## His move, assumed v did (2,113 checks)
Within 1" of the assumed place 42% (43%): stand 65%, move 28%, march 28%, assumed charge declared 51%.

## Headline
| | New | Simpler |
| --- | --- | --- |
| VP margin | -14 ±268 (W26 L26 D17), noise | |
| First round won when charging, claimed v happened | 74 v 77 | 65 v 76 |
| Net points per charged fight | +59 | +93 |
| Points lost a game | 577 | 541 |
| Free units caught in flank/rear a game | 1.25 | 0.75 |
| Charge pick: claimed VP v net over 2 turns | 146 v +22 | 103 v +62 |
| Shoot pick: claimed VP v VP of wounds done | 71 v 5 | 14 v 5 |

## Leads (for the build to check in code; not checked)
1. "In reach after his turn" claims 92% and is the step that is off. Heads 0-3 mostly changed our own turn, so this step looks untouched.
2. The start-of-next-turn check says "not there" for 73 of 85, yet 23 of those 85 came: that check disagrees with what the game then allowed.
3. 41% of promises fail the check right after our own moves while standing on the spot ("from where it stands that charge is not there").
4. 39 of 211 PROMISE PLANNED rows carry no PROMISE IN STEPS text.
5. "Free of his charges" at 98% looks high (try 14's finding had our unit charged first in about 8 of 100).

## Files
- promises-69.tsv: one row per promise (part, game, unit, target, claimed %, each step, both checks, inches off the spot, came, the full PROMISE PLANNED row).
- early-reading-57.md: the reading the stop was based on.
- Replays: WarhammerOldWorldSimulator branch claude/project-thread-279h77 (8 batch folders t15-*-9aabb06-p1..p4).
- Logs archived: OldWorldSimulations branch claude/project-thread-279h77, batches/try-15-h2h-2026-11-19.
