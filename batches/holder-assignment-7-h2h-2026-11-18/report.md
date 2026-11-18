# Holders batch 7 (dcce2247: real ground + his one quarter), ON v OFF: final report (STOPPED at 66 of 288 games)

**Verdict: walks to far markers still fail, unchanged from batch 6. Table quarters are now right. Nothing is broken.**
Stopped by the coordinator at 22:20 UTC after the 54-game reading (early-reading-54.md) because the known walk fault was unchanged.
All 8 parts ran the right switch side (0 wrong-side rows, checked in each part's games), no crashes, 6.7 min a game.
VP margin ON-OFF: -0 ±197 (34 won, 32 lost): noise.

## Claimed v happened (ON side, 66 games)

| Objective | Claims | Claimed | Happened |
| --- | --- | --- | --- |
| Far marker walks (arrives in 2+ turns) | 83 | 94% arrive | that unit scored it by the claimed turn 7 (8%), ever 9 |
| Near marker walks (1 more turn) | 57 | 94% | that unit scored it by the claimed turn 14, ever 19 |
| Special feature, last row "holds" | 23 games | 88% / 216 VP | held at the end 17, 227 VP |
| Special feature, last row "walks" | 6 games | 85% / 170 VP | held 1, 33 VP |
| Herdstone, last row "holds" | 19 games | 99% / 282 VP | held 15, 233 VP |
| Herdstone, last row "walks" | 6 games | 91% / 182 VP | held 0 |
| Own baggage train, round 5+ | 21 holds, 5 walks | 101 VP | 52 VP (holds kept 15 of 21, walks 0 of 5) |
| Quarters controlled / more than twice / uncontested | 274 | 68 / 57 / 33% | 66 / 55 / 27% |

- Holding what a unit already stands on is claimed about right (feature) or a little high (Herdstone 99% v 15 of 19).
- Every kind of WALK fails: far markers, feature, Herdstone, baggage train.
- Quarters: the batch 6 under-claim is gone (his-one-quarter). Quarter VP a Domination game ON 337 v OFF 362 (38 games, noise-sized).

## Far walks: what the units did

| Far walk (83) | Count |
| --- | --- |
| Moved toward the marker, median a turn | 3.2" (6.0" needed) |
| Covered its share of the way | 17 |
| A move onto the assigned marker was among the rows weighed | 29 |
| Took a move onto that marker | 5 |
| Took a move onto a different objective | 37 |
| Took a move toward or against an enemy | 14 |
| A wider-search spot / other | 11 / 16 |
| Taken move elsewhere that still carried the walk's credit | 24 |
| Taken move elsewhere with no walk credit at all | 54 |

REAL GROUND changed a claim's turn count 37 times in 66 games (+1 turn 32, +2 turns 3, -1 turn 2): as the build warned, most spots
still count the same whole number of turns.

## Leads (not checked in code)

1. **The table's walk does not reach the move choice.** In 54 of 83 far walks the move the unit took carried no credit for the walk,
   and a move onto the assigned marker was weighed in only 29 of 83. The table says "walks to Marker N"; the Movement phase then
   picks among moves that mostly do not include going there (37 went onto a different objective). Where the walk's credit is on
   the taken row, it is on rows that make no progress too (24), so it does not separate them.
2. **ONTO cannot show a far walk.** The new "ONTO <objective>: rank N of M" tag says "no spot in its range weighed" for every far
   walk (it only looks at spots that end in range this turn). Measuring a far walk needs progress toward it, not a spot in range.
3. **Planned spot not reached (the build's lead): evidence mostly AGAINST a general movement bug.** Planned = the "move to (x, y)"
   on the unit's rule rows, ended = the unit's place at the end of its Movement phase (ON side, plan7.py). Wider-search sideways
   spots ended within 1" 252 of 298 times; of the 46 misses 23 fell short, 8 went elsewhere, 7 failed a march test, 8 charge/flee/
   random. Objective moves missed 159 of 632, 95 of them short, most saying on their own row that the wheel and the way end them
   short. Spot-checks of unexplained "short" rows found they came from lead 4.
4. **A unit that "gives way" stands still.** When THE DEARER SUM KEEPS ITS PLAN makes a unit give way, it did not move at all that
   turn in 63 of 144 cases ON and 44 of 158 OFF (giveway7.py). Example L0423-3-1 turn 1: Hobgoblin Wolf Riders took "move onto
   Marker 2 (march)", gave way to Hobgoblin Cutthroats 2, then stood the whole turn. Whether standing was its next best or a lost
   move is for the build to check.

## Where everything is

- Replays: WarhammerOldWorldSimulator branch claude/project-thread-r55dno, commit 2aa280de (on dcce2247): deploy/sim-replays/
  h7-mine-dcce224-p1..4 and h7-opp-dcce224-p1..4 (66 games); on-site.txt lists these 8.
- Logs: archived to OldWorldSimulations, branch claude/project-thread-r55dno (see the commit there), never merged to its main.
- Scripts here (python3 -I <script> <root holding mine-N/ and opp-N/ folders>): walks6.py, a5.py, a4.py, walkmoves6.py (taken move by
  kind), onto7.py (ONTO rows), credit7.py (walk credit on taken rows), plan7.py (planned v ended), spot7.py (wider search, REAL GROUND
  claim counts), giveway7.py.
- Parts stopped at 11, 12, 12, 4 (Mine ON) and 10, 5, 6, 6 (Opponent ON) games.
