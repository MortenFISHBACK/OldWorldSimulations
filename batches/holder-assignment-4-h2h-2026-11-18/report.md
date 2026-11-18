# Holders batch 4 (holder table + baggage trains + quarters by the odds, ON v OFF): final report at 97 games (2026-11-18)

**Stopped by Morten at 17:40 UTC with 97 of 288 games played, to turn to the special feature.** The verdict at 97 games: quarters and
baggage trains are slightly up, the special feature is down, and the VP margin is noise.

- Quarters: +7 ±44 VP a game.
- Baggage trains: +13 ±13.
- Special feature: -29 ±30. The ON side ends with it in 21 of 63 feature games, the OFF side in 35.
- VP margin: -36 ±178. That is noise at 97 games.

Build bbe86176 on branch claude/project-thread-bj3s5r. The OFF side runs with `holder-assignment` and `quarter-odds` off. These are
the same pairs as batch 3, played both ways. The batch was cut short, so the 97 games are not evenly spread over pairs and sides:
57 Mine ON and 40 Opponent ON. Of the 97 games, 52 are Domination, 89 have baggage trains and 63 have a special feature. The switch
side was checked in all 97 games. The ON side has HOLDER ASSIGNMENT 3237, HOLD ODDS 728 and QUARTER ODDS 326 rows; the OFF side
has 0 of each. No game failed. Batch 3 (288 games) is in brackets.

## Claimed v happened (ON side)

| | Batch 4 (97) | (Batch 3) |
| --- | --- | --- |
| Marker, "holds it this turn": scored that round / next round | 83% / 64% (567) | (82% / 60%) |
| Marker, "walks on to it": that round / next round | 1% / 7% (105) | (1% / 12%) |
| Hold row: claimed v scored over its three moments (Mine ON / Opp ON) | 70 v 70 / 82 v 68 | (76-77 v 63-65) |
| Own baggage train from round 5 (last table row): claimed v scored | 98 v 74 VP (35 rows) | (not measured) |
| Special feature, last table row "holds it": held at the end | 20 of 39 (51%) | (not measured) |
| Special feature, last table row "walks on to it": held at the end | 1 of 18 | (not measured) |
| Quarter (unit's last QUARTER ODDS row from round 5 with a gain): claimed | +144 VP (211 units) | (new) |
| ... that unit's quarter at the end: controlled / more than twice / uncontested | 61% / 43% / 17% | (new) |

This head's log does not hold the chance of each quarter outcome, so the quarter row is a stand-in. The next head prints the
chances in brackets on the QUARTER ODDS row, as the build thread said.

## Quarters at the end, per Domination game (52)

| | ON | OFF |
| --- | --- | --- |
| Quarters controlled | 1.94 | 1.92 |
| ... more than twice | 1.54 | 1.46 |
| ... uncontested | 0.85 | 0.77 |
| Quarter VP | 356 | 342 |

## Objectives (ON v OFF, VP a game over all 97 games)

| | Diff | (Batch 3) |
| --- | --- | --- |
| Markers | +10 ±49 | (+17 ±26) |
| Table quarters | +7 ±44 | (-13 ±35) |
| Baggage held (end) / destroyed | +13 ±13 / -5 | (+5 / -1) |
| Special feature (end) | -29 ±30 | (+15 ±17) |
| Herdstone (end) | +2 ±21 | (-1) |
| Hill | +4 ±42 | (+4) |
| Units ending own turn within 6" of own baggage train | 5.7 v 4.3 | (4.5 v 4.0) |

## Special feature (63 games)

| Who holds it at the end | Games |
| --- | --- |
| ON side | 21 (33%) |
| OFF side | 35 (56%) |
| Nobody | 7 |

- When the ON side's last table row said "holds it" and the side lost it (19 games), the holder was still on the table in 15. An
  enemy unit ended nearer. The build thread checked 50 of these games (special-feature-check-80.md): no unit was pulled off the
  feature by a quarter or a baggage train. The feature still uses the old fixed figure of 250 to 450 VP in the last turns, which
  does not count the chance of being out-stood or charged off.
- A "walks on to it" row in the last turns is claimed at about 195 VP and scored once in 18 tries.
- The feature pricing is being fixed in the build thread now: the end VP times the chance the unit is on it and keeps it, as for
  baggage trains.

## Headline

| | Batch 4 (97) | (Batch 3) |
| --- | --- | --- |
| VP margin | -36 ±178 (49 won, 48 lost) - noise | (+27 ±143) |
| Game length (thinking time, both sides together) | 5.9 min a game, longest 12.2 | (7.5, longest 14.4) |

Part 5 (`opp 1`) never started. The owner ran it from 17:29 UTC (4 games). Scripts: scripts/a4.py (VP, rows, quarters, baggage
claim), scripts-build/eob2.py, feat3.py, scripts/markers.py, extra.py and job_claims3.py.
