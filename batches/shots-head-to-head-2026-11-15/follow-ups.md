# Head-to-head follow-ups (2026-11-15): switch leak and war machines at the top killer

Branch claude/project-thread-dnukaz, now 9c11d448 (full suite 16,652 passed, 0 failed). Script: scripts/war-machines-top-killer.py.

## 1. Switch leak: found and fixed

A shot or a magic missile at an enemy HEAVY HITTER (a monster lord that none of our units beats) counted "the better of its wear and
toward a kill + threat". With THREAT IN THE KILL switched off the threat part was 0, but the "better of" stayed, so the off side
still added "toward a kill" over the wear whenever that was bigger, and wrote a THREAT IN THE KILL row. Main counts the wear alone.
That is why 180 of the 201 off-side rows were at characters. Three places had it: the shoot job, the cast job of a casting block,
and the missile's target row. Now switched off means exactly main's figure. Test: HeavyHittersTests
.ThreatInTheKill_SwitchedOff_AShotAtTheHeavyHitterCountsItsWearAlone_AsOnMain (fails with the old code, passes now).

Also fixed: the SHOT OPTIONS rows were written with the shot's reason instead of their own text (best three targets, dearest threat).
The batch therefore had no target lists; the next batch will.

## 2. War machines at the top killer: the cause, with numbers (changed side, 288 army-games)

| | Changed | Main |
| --- | --- | --- |
| War machine shots | 877 | 941 |
| at the top killer | 20% | 23% |
| from the turn's shoot job ("its objective this turn") | 74% | 72% |
| THREAT IN THE KILL rows on war machine shots | 531 | 78 (the leak) |
| ...that changed the target | 34 (6%) | 10 |
| ...at the top killer | 167 (31%) | 42 |
| threat VP a shot: at the top killer / at another target | median 13 / 17 | |
| what the figure says the top killer "takes when it gets there" | median 117 VP | |
| what the top killer actually took in the game | median 379 VP | 372 VP |

Read: the figure points the guns at other multi-wound threats (chariots, monstrous cavalry, small monsters) more than at the top
killer, because:

1. **It is per wound of the whole model.** The shot's part is its share of the target's wounds x what the target takes. A cannon's
   ~0.5 wound is 7% of a 7-wound lord but 17% of a 3-wound chariot, so the smaller threat gets the bigger figure (13 v 17 VP median).
2. **"Takes" is one charge.** It is the best single fight on one of our units (chance it destroys it x its points). The top killer
   takes about three times that over a game (117 v 379 VP): it kills several units, the others kill one at most.
3. **It rarely decides.** Three quarters of the war machine shots follow the shoot job picked in the Movement phase, which already
   counts the threat; the figure changed the target in 6% of the rows. It adds to the target the job had chosen.

Proposed fix (not built; it changes the valuation, so it waits for your word):

- A. "Takes" over the turns left, not one charge: its best prey each turn it can still fight, each later turn at the walk's 65%
  share (as STAY WORTH counts later volleys). Lifts the top killer about 2-3x, a one-charge chariot hardly at all.
- B. The kill share toward where it stops being a threat (half its wounds or 2 left, the HEAVY HITTER "worn down" point), not over
  all its wounds, for every target with 3+ wounds a model. A wound on a 7-wound lord then counts about twice as much.
- Then a head-to-head on the same pairs (A and B on one side, today's branch on the other), with the new SHOT OPTIONS rows to check
  that the top killer is the dearest threat and gets the shots.
