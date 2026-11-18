# Batch 4: is the special feature lost to quarters or baggage trains? (80 games read, 50 with a special feature; 2026-11-18)

## Verdict

**The lead does not hold.** Units are not pulled off the centre piece by a quarter or a train. The holder table gives the special
feature to a unit as often as before, and that unit's pick goes for the feature every time. What the ON side loses is the feature
**at the end of the battle to an enemy unit that ends nearer**, with its own holder still alive. That loss was already there in
batch 2; at 50 games the difference to batch 2 is thin.

## Who holds the special feature at the end

| | Batch 4 (bbe86176), 50 games | Batch 2 (83c90997), 83 games |
| --- | --- | --- |
| ON side | 15 (30%) | 33 (40%) |
| OFF side | 31 (62%) | 36 (43%) |
| Nobody | 4 | 14 |

Batch 4 split: Domination games ON 3, OFF 11; games without Domination ON 12, OFF 20. So the ON side also trails where the quarter
rule does nothing.

## What the table and the picks did (ON side)

| | Batch 4 | Batch 2 |
| --- | --- | --- |
| Rounds 5+: feature "holds it this turn" / "walks on" / "stays empty" | 46 / 20 / 4 | 80 / 38 / 5 |
| Last table row says "holds it": ON held it at the end | 14 of 32 (44%) | 32 of 56 (57%) |
| ... lost with the holder still alive and not in the enemy's VP list | 14 of 18 | 20 of 24 |
| Last table row says "walks on to it": ON held it at the end | 1 of 14 | 0 of 18 |

In the 35 games the ON side did not win, the assigned unit made 38 picks in rounds 5 and 6. Every one went for the feature
(its sum's "objectives" part or "next turn on The special feature"). A quarter gain was in 7 of them, on top of the feature, not
in place of it. No pick chose a baggage train over the feature.

## What this shows instead (warnings: this is what the code does today, not a proposal)

1. **"Holds it" is claimed in full and kept about half the time.** The special feature still has the old fixed figure: 250 to 450 VP
   in the last turns, whatever enemy unit can end nearer. The marker formula (30 + 60 x chance kept) and the baggage train already
   count the chance of being out-stood; the feature and the Herdstone do not.
2. **"Walks on to it" in round 5 almost never scores** (1 of 32 over both batches), yet it is claimed at about 195 VP. The old
   walk figure (not from the board) is still used for the feature.
3. Why the OFF side picks up more features than in batch 2 (62% v 43%, "nobody" down from 14 to 4) is not explained by the logs I
   read. It may be noise at 50 games; read it again at 150.

## Options

1. **(default) Give the special feature and the Herdstone the same footing as the baggage train**: their end-of-battle VP times the
   chance the unit is on it and keeps it to the end (out-stood, charged off), walk-ons by the chance of arriving; the per-turn buffs
   stay as they are. About 1 hour, inside holder-assignment.
2. Wait for the 150 reading first.

Scripts: scripts-build/feat2.py (picks of the assigned unit), scripts-build/feat3.py (table rows and who held it at the end).
