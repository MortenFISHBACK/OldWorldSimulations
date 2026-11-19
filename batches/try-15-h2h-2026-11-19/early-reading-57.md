# Try 15: reading at 57 games (2026-11-19 ~01:50 UTC)

Head 9aabb0675 (promise steps 0-3) v true simpler, same pairs as tries 9-14, both ways. 57 finished games, none failed.
Counted with scripts/analysis/promises.py (PROMISE PLANNED rows, KEPT and NOT KEPT both). Try 14 (61 games, same counting) in brackets.

## Verdict
**The known fault is unchanged.** Promised charges: 85 claimed, 22 came in 100 (88 v 26). 183 promises, 3.2 a game (2.4).
The claim does not fall toward the result: 114 of 183 promises still say 95-100%. Unit off its spot: 18 in 100 (14).
VP -30 ±299 is noise.

## Claimed v came, by band
| Claimed | Promises | Came |
| --- | --- | --- |
| 0-50% | 24 | 1 (4%) |
| 50-75% | 17 | 2 (12%) |
| 75-95% | 28 | 4 (14%) |
| 95-100% | 114 | 34 (30%) |

## Which step is off ("PROMISE IN STEPS", 150 of 183 promises carry it)
| Step | Promises | Claimed (mean) |
| --- | --- | --- |
| in reach after his turn | 150 | 92% |
| free of his charges | 150 | 99% |
| the fight still on | 11 | 33% |
| march test passed | 4 | 73% |
| still there after our turn's shots | 1 | 82% |

The product is almost always "in reach after his turn" x "free of his charges", and it says 91% where about 25% came.
Our own turn's shots and the march test are almost never a step (5 of 150).

## Where the promise breaks (from the promise's own check rows)
| Check | Promises | Charge still there | Came |
| --- | --- | --- | --- |
| After our own moves, same turn | 96 | 59 (61%) | 18 |
| At the start of our next turn | 84 | 12 (14%) | 23 |

Off the spot: 15 of 96 after our moves (12 of them more than 3"), 18 of 84 at the start of the next turn.

## His move, assumed v did (1,749 checks)
Within 1" of the assumed place 42% (43%): stand 65%, move 27%, march 27%, assumed charge declared 51%.

## Headline
| | New | Simpler |
| --- | --- | --- |
| VP margin | -30 ±299 (W21 L22 D14), noise | |
| First round won when charging, claimed v happened | 74 v 77 | 65 v 75 |
| Net points per charged fight | +45 | +87 |
| Points lost a game | 574 | 534 |
| Free units caught in flank/rear a game | 1.12 | 0.75 |
| Charge pick: claimed VP v net over 2 turns | 153 v +10 | 99 v +55 |
| Shoot pick: claimed VP v VP of wounds done | 73 v 4 | 19 v 5 |

## Leads (not checked in code)
1. "In reach after his turn" is the step that is off: 92% claimed, about 25% came. It looks unchanged by heads 0-3, which mostly touch our own turn.
2. The start-of-next-turn check says the charge is "not there" for 72 of 84, yet 23 of those 84 came: that check disagrees with what the game then allowed.
3. 39% of promises already fail the check right after our own moves while standing on the spot ("from where it stands that charge is not there").
4. 33 of 183 PROMISE PLANNED rows carry no PROMISE IN STEPS text.
5. Off the spot did not drop (18 v 14 in 100).
