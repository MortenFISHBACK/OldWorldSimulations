# Holder batch: the end-of-battle objectives, checked in code and logs (165 games, 2026-11-18)

## Verdict

The lead does not hold. Special feature, Herdstone and baggage together cost the ON side about 2 VP a game (noise).
The end-of-battle gap sits in the **table quarters** (Domination): -32 VP a game, ±38, so still noise. The table does not assign quarters at all.

## End-of-battle VP a game, ON side v OFF side (from each game's final score; scripts-build/eob2.py)

| What | ON | OFF | Difference |
| --- | --- | --- | --- |
| Markers | 340 | 313 | +27 ±38 |
| Hill | 46 | 49 | -3 ±26 |
| Special feature (end) | 47 | 57 | -10 ±22 |
| Herdstone (end) | 18 | 10 | +9 ±11 |
| Baggage train held (end) | 14 | 15 | -1 ±8 |
| Baggage train destroyed | 3 | 6 | -3 ±7 |
| Table quarters (end) | 199 | 231 | -32 ±38 |
| Kills | 649 | 661 | -13 ±106 |

## Which figure the table uses for feature, Herdstone and baggage

The old one, unchanged (ruling 5a, "later"):

- The end-of-battle VP counts 0 until the second-to-last own turn, half then, in full in the last turn (fixed shares).
- Herdstone and special feature add a per-turn worth: before round 5 the Herdstone's flat 30 plus its buffs as worked out, the feature its buffs only; from round 5 the flat 75 and 50 (Morten's own figures of 10-31 and 11-16).
- All of it is cut by half the chance the holder loses a fight there (a fixed half).
- The enemy's baggage train: 100 VP by the same end-of-battle shares, no per-turn worth.

## What the table does with them (ON side, scripts-build/eob3.py)

| Objective | Rounds | Assignments | Only walking towards it | Mean worth claimed | Mean given up |
| --- | --- | --- | --- | --- | --- |
| Baggage | 1-4 | 248 | 100% | 47 | 7 |
| Baggage | 5+ | 88 | 81% | 70 | 15 |
| Herdstone | 1-4 | 114 | 65% | 99 | 6 |
| Herdstone | 5+ | 50 | 48% | 251 | 38 |
| Special feature | 1-4 | 213 | 54% | 69 | 7 |
| Special feature | 5+ | 137 | 31% | 244 | 23 |
| Marker | 1-4 | 920 | 21% | 83 | 9 |
| Marker | 5+ | 220 | 5% | 45 | 6 |

What stands out: in rounds 1 to 4 the table gives a unit to the enemy's baggage train 248 times, every time only to walk towards it,
for a claimed 47 VP, although the train scores nothing before the end. A unit holds one objective in the table, so that unit is no
longer in the running for a marker that turn. The units give up little by their own sums (7 VP), so the table sees no cost.
Warning, not a proposal: this is what the code does today; whether it costs marker VP is not measured.

## Options for Morten

1. **(default) Change nothing here now.** Let the batch run to 288 and read the quarters row again; -32 ±38 is not a result yet.
2. Walking towards an end-of-battle objective no longer takes the unit out of the running for a marker before the second-to-last turn
   (the walk stays in the unit's own sum; only the table's "one objective" claim goes). About 1 hour, own switch-free change inside holder-assignment, next head.
3. Replace the fixed end-of-battle shares (0, half, full; half the lose chance) by the worked-out chance the unit still holds it at the end.
   This is ruling 5a's "later" item and touches the sums the move table build owns: for that thread.
4. Give the table quarters a row in the table (Unit Strength per quarter at the end). A planner step, not a holder fix.

Default: 1 now; 2 on the next head if the 288 reading still shows the quarters or marker gap; 3 and 4 go to the planner's steps.
