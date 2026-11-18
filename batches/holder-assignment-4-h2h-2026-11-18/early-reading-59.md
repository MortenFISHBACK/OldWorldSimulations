# Holders batch 4 (holder table + quarters by the odds, ON v OFF) - early reading at 59 games (17:31 UTC)

**Verdict: too early to read; nothing alarming.** Quarters are not better yet (-9 ±57 VP a game). Baggage trains are held more
(+20 ±15). The VP margin, -72 ±207, is noise at 59 games. The switches are on the right side in all 59 games.

Build bbe86176 on branch claude/project-thread-bj3s5r. The OFF side runs with `holder-assignment` and `quarter-odds` off. These
are the same 144 pairs as batch 3, played both ways. Of the 59 games, 35 are Domination and 53 have baggage trains. Rule rows on
the ON side: HOLDER ASSIGNMENT 1990, HOLD ODDS 426, QUARTER ODDS 218. The OFF side has 0 of each. Batch 3 (288 games, no quarter
odds) is in brackets.

## Claimed v happened (ON side)

| | Batch 4 at 59 | (Batch 3) |
| --- | --- | --- |
| Marker, "holds it this turn": scored that round / next round | 82% / 64% (334) | (82% / 60%) |
| Marker, "walks on to it": that round / next round | 0% / 4% (47) | (1% / 12%) |
| Hold row: claimed v scored over its three moments (Mine ON / Opp ON) | 67 v 65 / 80 v 68 | (76-77 v 63-65) |
| Own baggage train held from round 5 (last table row): claimed v scored | 100 v 75 VP (20 rows) | (not measured) |
| Quarter (unit's last QUARTER ODDS row from round 5 with a gain, the quarter where it ended): claimed | +151 VP (139 units) | (new) |
| ... that quarter at the end: controlled / more than twice / uncontested | 57% / 42% / 17% | (new) |

The game log does not print each outcome's chance. The option line has them, but it is not logged. So the quarter claim cannot
yet be matched outcome by outcome. The row above uses a stand-in: the claimed gain, and what that unit's quarter scored at the end.

## Quarters at the end, per Domination game (35 games)

| | ON | OFF |
| --- | --- | --- |
| Quarters controlled | 1.86 | 2.03 |
| ... more than twice | 1.54 | 1.54 |
| ... uncontested | 0.83 | 0.80 |
| Quarter VP | 346 | 360 |

## Objectives (ON v OFF, VP a game over all 59 games)

| | Diff | (Batch 3) |
| --- | --- | --- |
| Markers | +32 ±62 | (+17 ±26) |
| Table quarters | -9 ±57 | (-13 ±35) |
| Baggage held (end) / destroyed | +20 ±15 / -9 | (+5 / -1) |
| Special feature (end) | -58 ±35 | (+15 ±17) |
| Herdstone (end) | +14 ±32 | (-1) |
| Hill | -17 ±50 | (+4) |
| Units ending own turn within 6" of own baggage train | 5.5 v 3.6 | (4.5 v 4.0) |

Lead, not checked in code: the special feature is down 58. Units held by their quarter or their train may be leaving the centre
piece. The ± is wide at 59 games, so this needs the 150 reading before it means anything.

## Headline

| | Batch 4 at 59 | (Batch 3) |
| --- | --- | --- |
| VP margin | -72 ±207 (24 won, 35 lost) - noise | (+27 ±143) |
| Game length | 5.8 min a game, longest 12.2 | (7.5, longest 14.4) |

Part 5 (`opp 1`) had not started 25 minutes after go. The owner runs it in its own container.
