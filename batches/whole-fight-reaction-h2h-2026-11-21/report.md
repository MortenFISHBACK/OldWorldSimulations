# Whole fight reaction head-to-head (2026-11-21): result

**Verdict: no measurable difference.** The rule-on side scored +72 VP a game more, ±180 (95% range): noise. On pairs played both
ways: +37 ±85, also noise. It changed the reaction 30 times in 144 games, mostly a unit now fleeing one charger.

Build a92c1601 (branch claude/project-thread-41u08n). 72 pairs of the 11-20 danger head-to-head, seed 1, scenario mix, played both ways
(parts 1-24: rule off for Mine; 25-48: off for Opponent). All other rules on for both sides. Rules-off file checked in every part (all right).

| | Games | Margin per game (on minus off) |
| --- | --- | --- |
| All scored | 133 | +72 ±180 |
| Rule on for Opponent | 67 | -2 |
| Rule on for Mine | 66 | +147 |
| Pairs scored both ways | 64 | +37 ±85 |

Average VP: on 1,280, off 1,208. Wins: on 67, off 66.

Unscored (stopped early, 11): L2335 (p11), L1527 + L1723 (p33), L0717 (p5, p29), L1625 + L1723 (p9), L1727 (p21, p45), L1827 (p46),
L2535 (p48). Faults: "'0' cannot be greater than -4" crash (also in 12 games of the play-for-margin replays on main and in the 11-20
batch: not this change) and the known stall S-3714f4.

## How often the choice changed (rule rows)

189 reactions priced by the new figure in 77 games. 30 changed the choice against the old one-charger figure:

| Change | Times |
| --- | --- |
| now flees one charger (fight played out over several rounds) | 26 |
| now flees several chargers | 2 |
| now holds against several chargers | 2 |

Several chargers on one unit came up 16 times in 144 games.

Unchecked: whether the 30 changed choices won or lost points in their own games.

Replays: deploy/sim-replays/wfr-a92c160-p1..p48 on the branch. Logs archived: OldWorldSimulations, branch claude/project-thread-41u08n,
batches/whole-fight-reaction-h2h-2026-11-21.
