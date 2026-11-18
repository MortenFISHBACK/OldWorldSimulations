# Why joint pricing does not raise joint charges (batch A, 18 November 2026)

Analysis only, no code changed. Base: the 105 games of batch A pulled so far (f9a8036a; ON = joint charge now + aftermath with
friends). Batch games were replayed in code with a trace of the joint sum; the replays match the batch to the digit (same worths,
same unit ids), so the figures below are the code's own sums on the real boards. 5 of 18 replays were finished when this was
written; the rest are running and I only come back if they change the picture.

## Verdict

1. **ON v OFF is not "joint pricing v none".** The OFF side still prices a second charger in the Strategy phase by the older rules,
   and gets as many second chargers (58 v 63). Batch A compares two ways of pricing, and they pick about equally often.
2. **My joint sum has a fault: the enemy strikes every charger in full.** One enemy model's attacks are counted once for each unit
   that charges it. So two chargers are given twice the blows back, lose the combat result more often, and in 2 of 3 pair figures
   the pair is priced BELOW the better unit alone. That is the largest single reason the second unit stays out.
3. **"All in" 80 claimed v 50 came is not the dice.** Where every charger declared and nothing was in the way, 83 claimed v 81 came.
   The gap is chargers that roll enough and still do not get in: they block each other's landing, or something stands in the path.
4. **The joint net figure is not held against the same yardstick.** Round one of a joint fight where everyone got in is honest
   (+59 claimed v +65 came). The "+103 v +19" compares the whole fight in wounds with two turns in whole models; single charges
   show the same gap (+131 v +62).

## 1. Why the second unit did not charge

ON side, 163 ready pairs: both charged 44, one 63, none 56. The 119 where not both charged:

| What the figures said | Cases | Share |
| --- | --- | --- |
| The pair is priced at or below the lead alone | 53 | 45% |
| The pair adds, but something else is worth more | 57 | 48% |
| Nothing to gain (alone and together at or below zero, or the charge ends below zero) | 8 | 7% |
| Second unit picked the charge, the game offered it no charge | 1 | 1% |

The joint figure was worked out in every case. The first unit declaring first is not the problem.

**The pair priced at or below the lead alone (53):**

| Why | Cases |
| --- | --- |
| The enemy strikes both chargers in full (target of 1 model: 11, of 2 to 4: 3, of 5 or more: 11) | 25 |
| The second unit loses more than it adds, no double blows seen (it loses its own fight too) | 18 |
| The target's reaction changes: it flees from two where it holds against one (4), or the other way (1) | 5 |
| The pair is ahead after two rounds and behind over the whole fight | 3 |
| Nothing above zero either way | 2 |

Over all 1,101 pair figures in the batch (both sides): 749 price the pair below the better unit alone, and 468 give the pair a LOWER
chance to win round one than the better unit alone. In 587 the enemy's blows land on both chargers in full; 203 of those are
single-model targets, where that cannot happen (rule: a model divides its attacks, tow.whfb.app/the-combat-phase/dividing-attacks).
For bigger targets it is right only when the two chargers touch different models; the sum never checks that.
Example (game L0717, turn 6): Bastiladon charged by Empire Knights alone: own losses 62. By the Wizard Lord alone: 69. By both: 130.

**The pair adds, but something else is worth more (57):**

| What was worth more (for the second unit, or for the friend asked to come) | Cases |
| --- | --- |
| Next turn's charge (9 of them on the SAME target) | 18 |
| What it does this turn where it stands (shots, an objective held) | 16 |
| Another charge this turn | 12 |
| Support and other jobs for friends | 7 |
| Next turn's objective walk | 4 |

Replayed in code (5 games, 115 charge options priced; 61 with a friend in reach still to pick or a set to join): pair at or below
the unit alone 32, pair adds but the friend gives up more 15, joins but another option higher 4, plan made or charge taken 10.
Same picture as the logs.

**Also found: an older join rule still decides at declaration, on both sides.** A unit that did not plan a charge joins a friend's
charge when the friend alone wins the first round under 55% and together 55%+ and 15 points more. No points figure, fixed gates.
It made 20 joint charges on ON and 12 on OFF, also where the joint sum had just said no (game L0122, turn 1: sum said -470 and -12,
both joined by the old rule, the fight was won).

## 2. "All in": 80 claimed v 50 came

46 joint rows on ON = 34 real sets that claimed a fight (6 claimed the target flees, 6 were a unit alone).

| What happened to the set | Sets |
| --- | --- |
| All made contact | 17 |
| A charge roll failed and nothing else (the claim expects about 7) | 4 |
| A charger halted short: it would have ended on the other charger, or no room on that side (3 sure, 2 likely) | 5 |
| Another unit in the charger's path: an own unit (1), an enemy unit (3; in one of them a roll failed too) | 4 |
| The target fled (claimed: it holds), chargers redirected | 2 |
| The game offered no charge at declaration, or no result logged | 2 |

The claim is the product of each unit's own reach, each worked out alone on the board as it stands. It never asks whether both can
land. The order of declaration plays no part.

## 3. Joint net: +103 claimed v +19 came

| | Claimed | Came |
| --- | --- | --- |
| Joint, everyone got in, round one (17 sets) | +59 | +65 |
| Joint, everyone got in, whole fight v two turns | +82 | +21 |
| Joint, only part of the set got in (9 sets), whole fight v two turns | +78 | -5 |
| Single charges ON side (170), round one | +72 | +36 |
| Single charges ON side, whole fight v two turns | +131 | +62 |
| Single charges OFF side (165), whole fight v two turns | +128 | +72 |

Three parts:
- **Not the same yardstick.** The claim counts wounds as a share of the unit's points, to the end of the battle, with the points a
  dead general or banner costs. "Came" counts whole models lost over two turns at list points. A wounded monster that lives counts
  nothing. Single charges show the same factor of two on both sides, so this is not a joint fault.
- **The row claims everyone in.** In 9 of 26 sets with contact only part got in (section 2). Priced for those who got in: +81.
- **After round one** the joint fights that were all in lost points in play (+65 after round one, +21 after two turns) where the sum
  expects them to keep earning. 17 sets is too few to name a cause; the double blows cannot be it (they make the claim lower).

## What step 3 (sets as rows on the army table) must do

| Cause | What to do | Where |
| --- | --- | --- |
| The enemy strikes every charger in full | Count each enemy model's attacks once: from the single fights, how many of its models touch each charger; when together they need more models than it has on that side, the blows are shared out. Then "pair wins round one less often than the lead alone" must be gone from the log | My sum, before step 3. No table needed |
| Chargers block each other | A set is a row group with a landing for each member, tried in the table's declaration order; "all in" is worked out from the board for that order (room on the side, paths), and a set that cannot all land is priced for those who can | Step 3, on step 2's order |
| Next turn's charge on the same target beats joining now | A promise on a target a friend charges this turn is worth only what is left (already agreed) | Build 1's next head |
| Support for a friend beats joining its charge | On the table the friend's row says it charges; the support figure is worked out against that row, not the standing board. It also carries a fixed "half for the wait" | Build 1, flagged |
| A fight that ends sooner is priced below a slow one | When the enemy falls back or gets away the sum stops, while a slow fight keeps earning every round. The free units' next turn is priced by the next table (plan step 7) | Step 7; note until then |
| The old join rule at declaration (fixed gates) | Off on the new side once sets are rows, with the old battle groups | Step 3 switch |
| Joint claim v happened | The joint row says round one and each later round in the same units the report counts, for the units that got in | Step 3 log + batch script |

## Questions (defaults marked)

1. The double blows in my sum: a) I fix it now on my branch, test first, so batch A's successor and step 3 start from a right sum
   (default; under 1 hour by my recent clock). b) Wait and fix it inside step 3.
2. The old join rule at declaration: a) off on the new side together with the old battle groups, under your earlier "3a" (default).
   b) Keep it until step 3's batch shows the table does better.
3. Batch A itself: a) let it run to 288 as the baseline it was meant to be; its joint figures are known to be too low (default).
   b) Stop it, since the sum it tests has a known fault.
