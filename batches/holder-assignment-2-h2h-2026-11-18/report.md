# Army-wide objective holders, SECOND head, ON v OFF - head-to-head report (2026-11-18)

**Verdict: no clear gain; all 288 games played.** The fixed table does its job when it names a unit that is already there: that unit
scores the marker that round 78% of the time. But a unit sent to "walk on" to a marker scores it the next round only 9%, and the hold
claim is about twice what is scored. Markers gain +25 VP a game (±28) and baggage trains held +17 (±8); table quarters -12, hill -8.
All objectives +12 a game, VP margin **+29 ±139** (noise). Cheaper units are still not chosen as holders more often (41% v 44%).

Build 83c90997 (code c80da14c, branch claude/project-thread-bj3s5r). Both sides play the overhaul's pricing; the only difference is
`holder-assignment`, off for one side (`@opponent` in mine-1..4, `@mine` in opp-1..4), the same 144 pairs both ways as batch 1.
Switch side checked in all 288 games (scripts/sides.py): holder-table rows on the ON side only. Smoke L0103: 58 rows on the ON side, 0 off.
No game failed or timed out; one game has a finding.

## Claimed v happened (ON side; scripts/extra.py, assigned.py, repo scripts/job_claims.py)

| | Batch 2 (288) | Batch 1 (168) |
| --- | --- | --- |
| Marker, table says "holds it this turn": scored that round / next round | 78% / 61% (1588 rows) | 78% / 60% |
| Marker, table says "walks on to it": that round / next round | 1% / 9% (358) | 0% / 10% |
| Hill, "holds it this turn": that round / next | 51% / 28% (123) | 49% / 23% |
| Hill, "walks on to it": that round / next | 2% / 14% (108) | 0% / 5% |
| Per-unit holder row: marker / hill holder scored that round | 64% / 28% | 65% / 24% |
| job_claims Hold row: claimed VP v scored (this turn + enemy's next) | 88-90 v 42-44 | (did not read) |

Why the claim is about twice (the build thread's claims-check-56.md, checked in code): the hold figure is 30 VP for up to three own
turns less half the lose chance (two fixed numbers), and a walk-on is not owed next turn (the table is made from scratch each turn:
next turn 25% were sent to a baggage train instead, 22% got nothing, 21% scored).

## Objectives (ON v OFF, a game)

| | Batch 2 ON | OFF | Diff | Batch 1 diff |
| --- | --- | --- | --- | --- |
| Marker player-turns scored (nobody 34%) | 34% | 32% | | 35% v 32% |
| Markers VP | 309 | 284 | +25 ±28 | +27 |
| Hill VP | 65 | 73 | -8 ±23 | -3 |
| Table quarters VP (end) | 195 | 207 | -12 ±34 | -32 |
| Special feature / Herdstone (end) | 50 / 7 | 54 / 9 | -4 / -2 | -10 / +9 |
| Baggage train held (end) / destroyed | 30 / 5 | 14 / 10 | +17 ±8 / -4 | -1 / -3 |
| All objective VP | | | +12 | -12 |
| Scored by the cheapest able unit alive | 41% | 44% | | 42% v 46% |
| Points of the scoring unit, mean (median) | 211 (162) | 204 (162) | | 227 v 220 |
| Units ending own turn within 6" of own baggage train | 4.3 | 4.0 | | 4.7 v 4.3 |

## Headline (ON v OFF)

| | Batch 2 | Batch 1 |
| --- | --- | --- |
| Charges declared a game | 4.1 v 4.1 | 3.7 v 3.4 |
| First round won when charging, claimed v happened | 67% v 74% / 70% v 76% | 65% v 76% / 67% v 76% |
| Net points per charged fight | +81 v +79 | +81 v +77 |
| Points lost a game | 598 v 609 | 581 v 576 |
| Free units caught in flank/rear a game | 1.52 v 1.48 | 1.25 v 1.27 |
| Thinking time | 7.3 min a game, longest 18.6, none timed out | 6.4, longest 12.8 |

VP margin ON v OFF: **+29 ±139** (116 won, 108 lost, 64 drawn); objectives +12, kills +16. Noise.
(The 150-game reading showed quarters -49 ±43; at 288 it is -12 ±34: that lead faded.)

## Leads (from logs, not checked in code beyond claims-check-56.md)

- The table works for "already there" holders; the loss is in walk-ons (9% next round): the walk is not owed next turn. The build thread's
  default fix (a walk the table gave is owed next turn; the hold figure from the chance it still holds at each scoring moment) goes to the
  move table build.
- The baggage-train figure did not fall (4.3 v 4.0) although baggage held at the end rose +17 VP: the ON side keeps more units home.
- Cheaper holders are still not picked more often.

## Files

Parts mine-1..4 / opp-1..4 (batch.tgz), early-reading-56.md, reading-150.md, claims-check-56.md (build thread), scripts/ (sides.py,
markers.py, assigned.py, extra.py), scripts-build/ (eob2.py etc.). Archived to MortenFISHBACK/OldWorldSimulations.
