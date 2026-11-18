# Holders batch 2: the two claim leads, checked in code and logs (136 games, 2026-11-18)

## Lead 1: the hold row claims about 88 VP and about 46 is scored

Verdict: mostly two different yardsticks, with a real fault underneath.

- The claim is the one sum's hold figure (`HoldGainAt`): 30 VP for each of the unit's own turns left, **at most three**, less **half** the
  chance it loses a fight there. So a marker reads ~90 from round 1 to round 4.
- The measure counts two player turns (this turn and the enemy's next): at most 60.
- Like for like: the assigned holder scores that round 81% and the next round 63%. Over the claim's own three turns that is about
  55 to 60 VP of the 90 on own turns. The marker also scores at the end of the enemy's turns, which the claim does not count at all.

The fault: the figure is built from two fixed numbers (three turns, half the lose chance), not from the chance the unit still holds the
marker at each scoring moment. It claims the same 90 for a unit that will be charged off next turn and for one nobody can reach.
This is the "hold worth keeps its old shares" limit in the hand-over; the figure lives in the one sum (the move table build's code).

## Lead 2: a holder that "walks on" scores 2% that round and 16% the next

2% that round is as meant (it is not in range yet). The next round is the fault. Of 107 walk-ons the table said would arrive next turn
(all in rounds 1 to 3; scripts-build/walk3.py):

| What happened the next turn | Count | Share |
| --- | --- | --- |
| The table sent the same unit to walk towards a baggage train instead | 27 | 25% |
| The same unit got no objective (its other options beat the marker now) | 24 | 22% |
| It scored a marker | 23 | 21% |
| Still walking to the same marker (arrived a turn late) | 15 | 14% |
| Sent to a special feature or Herdstone instead | 12 | 11% |
| Sent to another marker | 6 | 6% |

Root cause, one for all rows but the third: **the table is made from scratch every turn and owes nothing to last turn's walk.**
The walk is paid for this turn (its worth is the VP of arriving), and next turn the same unit is priced as if it had never set out.
It is the same class as the promised marches the move table build found: a promise priced in one turn and not owed in the next.

Already fixed on 9f94dc5b: the largest row (25%, re-sent towards a baggage train) cannot happen before round 5 any more.

## Options for Morten

1. **(default) A walk the table gave is owed next turn.** The unit that walked on is priced next turn with the walk it has already paid:
   giving the marker up costs what was claimed for arriving ("a promise is worth what is left", his ruling of 11-18 for marches).
   This belongs with the move table build's next head (promises from table rows); built there, not here.
2. The hold figure counts every scoring moment left (own and enemy turns) at the worked-out chance the unit still holds it then, in place
   of "three turns, half the lose chance". Also the one sum's code: for the move table build, after option 1.
3. Leave both until batch 2 ends at 288 and read the table again on the round-5 head.

Default: 1 and 2 go to the move table build as its next two items; batch 2 runs on.
