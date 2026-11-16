# Battle groups on v off: 144 DKTC games each way (12 November)

Branch claude/project-thread-uezmnz at 789c37f6a (GROUP AIM + the new tracing), Hero v Hero, seed 1, scenarios mix. "On" = every rule;
"off" = `--rules-off battle-groups` (escort, cover, redirect counter, hunt in pairs, screen steps aside, group broken, group aim).
143 games ended both ways. Per-part comparisons: compare/compare-1..4.md; totals: compare/aggregate.py.

## In short
- **No measurable difference.** VP a side a game 1,415 on v 1,403 off. Margin change -96 VP a game, give or take 207 (noise). 69 of 143 games
  changed result.
- **Joint charges did not rise.** Fights with 2+ chargers: Mine 10% on v 9% off, Opponent 16% v 16%.
- **GROUP AIM barely fires and does not deliver.** 0.6 rows a game (both sides); it changed the move 3 times in 144 games. Of 65 aims
  (unit + target), 1 unit charged its target within three rounds, 0 with its partner. Groups (a 250+ block with a cheap fast escort in
  24") are rare, and the aim loses to the units' other jobs.
- **Counter-charge cover does steer moves but the counters still do not come.** 17.7 cover rows a game; the pick check says the cover
  changed the move in 12% of them (316). When a covered unit was charged (24%), a counter came 13% of the time, by the friend the cover
  named in only 30% of those. Unanswered: the named friend charged nothing 44%, the charger was gone or fled 35%, the friend charged another
  enemy 10%, the friend was gone 8%. REDIRECT COUNTER: counter 16% when charged, by the named friend 23% of those; friend charged nothing 66%.
- **Escort**: 0.8 rows a game, changed the move 3 times. **Hunt in pairs**: 0.8 a game, changed 10 times. **Screen steps aside**: 2 rows.

## Bugs
- L2127-3-1 (on): stall in Turn 3 Combat, "Sequence contains no matching element" - same game and message as S-4a0408 from round-robin 12b.
- L2433-3-1 (off): Deepwood Hounds 1 left 0.63-0.78" inside impassable terrain (S-dc01c1, new; looks like the S-b8d020 class).

## Reading
The figures the battle groups add are real (they change a move now and then), but the plan behind them is never carried out: nothing makes
the friend charge when the moment comes, and an enemy that charged is often gone by then. The new aim fires too rarely to matter.
