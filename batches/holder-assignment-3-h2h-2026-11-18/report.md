# Army-wide objective holders, THIRD head (HOLD ODDS), ON v OFF - head-to-head report (2026-11-18)

**Verdict: claims are now honest, results unchanged; all 288 games played.** A hold claims 76-77 VP and scores 63-65 over the same
three moments (batch 2 claimed 88-90 against 42-44 over two moments). The named holder scores that round 82% (78%). Walk-ons are
rarer (123 v 358) and still arrive the next round only 12% (9%). Markers +17 ±26 a game (+25), all objectives +25. VP margin
**+27 ±143** (batch 2 +29 ±139): noise, same as batch 2. Far markers are NOT left empty more often on the new side: 59% v 63% never
scored all game.

Build efe7e340 (branch claude/project-thread-bj3s5r). Both sides play the overhaul's pricing; the only difference is
`holder-assignment` (with HOLD ODDS inside it), off for one side (`@opponent` in mine-1..4, `@mine` in opp-1..4), the same 144 pairs
both ways as batches 1 and 2. Switch side checked in all 288 games: HOLDER ASSIGNMENT / HOLD ODDS rows on the ON side only, in every
game. Smoke L0103: 43 + 13 rows on the ON side, 0 off. No game failed or timed out. Batch 2 at 288 games in brackets.

## Claimed v happened (ON side)

| | Batch 3 | (Batch 2) |
| --- | --- | --- |
| Marker, table says "holds it this turn": scored that round / next round | 82% / 60% (1590 rows) | (78% / 61%, 1588) |
| Marker, table says "walks on to it": that round / next round | 1% / 12% (123) | (1% / 9%, 358) |
| Hill, "holds it this turn": that round / next | 56% / 30% (161) | (51% / 28%) |
| Hill, "walks on to it": that round / next | 0% / 10% (59) | (2% / 14%) |
| Hold row: claimed VP v scored over the claim's three moments (scripts/job_claims3.py) | 76-77 v 63-65 | (not measured) |
| Hold row: claimed VP v scored, first two moments only (as batch 2) | 76-77 v 46-47 | (88-90 v 42-44) |

## Objectives (ON v OFF, VP a game)

| | Diff | (Batch 2) |
| --- | --- | --- |
| Markers | +17 ±26 | (+25 ±28) |
| Marker player-turns scored ON v OFF (nobody 35%) | 33% v 31% | (34% v 32%) |
| Hill | +4 ±25 | (-8 ±23) |
| Table quarters | -13 ±35 | (-12 ±34) |
| Special feature (end) | +15 ±17 | (-4) |
| Herdstone (end) | -1 ±7 | (-2) |
| Baggage held (end) / destroyed | +5 ±7 / -1 | (+17 ±8 / -4) |
| All objective VP | +25 | (+12) |
| Scored by the cheapest able unit, ON v OFF | 40% v 43% | (41% v 44%) |
| Units ending own turn within 6" of own baggage train | 4.5 v 4.0 | (4.3 v 4.0) |

## Far markers (the open decision; scripts/far.py)

A marker is "far" for a side when no non-character unit of that side can get within 6" of it in one move at the side's first turn
(reach = the longest single-turn move that unit made in the game; dead units keep their last spot). Most are the markers in the enemy's half.

| | ON | OFF |
| --- | --- | --- |
| Markers far at own first turn | 39% (299/772) | 38% (297/772) |
| of those, never scored by that side all game | 59% | 63% |
| of those, still far at every own turn start | 45% | 43% |
| Markers in reach at first turn: never scored all game | 29% | 30% |

Answer for the decision: with "two or more turns away counts nothing", far markers stay empty all game no more often than on the old
side (59% v 63%). The rule does not cost far markers in these games.

## Headline (ON v OFF)

| | Batch 3 | (Batch 2) |
| --- | --- | --- |
| VP margin | +27 ±143 (117 won, 112 lost, 59 drawn) | (+29 ±139) |
| Charges declared a game | 3.9 v 4.2 | (4.1 v 4.1) |
| First round won when charging, claimed v happened | 70% v 74% / 66% v 72% | (67% v 74% / 70% v 76%) |
| Net points per charged fight | +90 v +78 | (+81 v +79) |
| Points lost a game | 615 v 622 | (598 v 609) |
| Free units caught in flank/rear a game | 1.54 v 1.57 | (1.52 v 1.48) |
| Thinking time | 7.5 min a game, longest 14.4, none timed out | (7.3, longest 18.6) |

VP by source: objectives +25, kills +4. Noise.

## Leads (from logs, not checked in code)

- The hold figure now matches the board within ~12 VP; the remaining gap may be holders charged off or out-stood more often than the
  odds said, or the battle ending early.
- Walk-ons stay the weak point: one in eight arrives and scores the next round. The table is made fresh each turn, so a walk is not
  owed next turn (as found in batch 2's claims-check-56.md).
- Cheaper holders are still not picked more often (40% v 43%).
- Table quarters stay behind (-13 ±35), as in both earlier batches; the table does not assign quarters (planning question open).

## Files

Parts mine-1..4 / opp-1..4 (batch.tgz; archived, then removed from the mount), early-reading-49.md, reading-150.md, scripts/ (sides.py,
markers.py, assigned.py, extra.py, far.py, job_claims3.py), scripts-build/ (eob2.py etc.). Archived to MortenFISHBACK/OldWorldSimulations.
