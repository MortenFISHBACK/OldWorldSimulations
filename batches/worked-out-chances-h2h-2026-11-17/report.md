# Worked-out chances against simpler pricing: head-to-head (2026-11-17)

**Verdict on the odds: "legal charges only" fixes what it was built for. "Shot or charge" is sound but rarely comes up, so it barely moves anything.**
Picked charges that never get declared drop from 13% to 2%. Shoot jobs that never fire at their target move only from 30% to 28%. All the other
claims are still off by the same amounts as in simpler pricing, because these two switches do not touch them (table 1).
**VP: +57 a game, give or take 64.** That is within noise and inside the keep band (not worse than -30).

Batch: 288 games, the same 144 DKTC pairs as today's other batches (static v static, seed 1, scenarios mix), each pair played both ways.
Build `claude/project-thread-60g6hv` at `b0077eed4`. ON = both switches on (legal-charges-only, shot-or-charge), OFF = simpler pricing.
All 288 games ended, with no crashes and no stuck games. I checked in every part's logs that the switch lines come only from the ON side.
The measuring uses the corrected turn windows from branch 6skrm4.

## 1. Odds: what the computer claimed against what happened

| Claim | ON | OFF (simpler) |
| --- | --- | --- |
| **Picked charges declared that turn** | **98%** | 87% |
| Declared charges that made contact | 73% | 72% |
| Win first round: claimed v happened | 67% v 74% | 67% v 73% |
| Charge pick: claimed VP v net points two turns later | 89 v +57 | 88 v +53 |
| **Shoot picks that fire at their target** | **72%** | 70% |
| Shoot pick: claimed VP v VP of wounds done that turn | 19 v 6 | 20 v 5 |
| Close in: claimed VP, and charged that target next turn | 54, 14% | 54, 14% |
| Advance: claimed VP, and charged that target next turn | 6, 4% | 6, 4% |
| Hold an objective: claimed VP v scored | 74 v 23 | 71 v 24 |
| Risk of the picked jobs (a game): claimed v points lost in the enemy's next turn | 737 v 450 | 746 v 462 |

What this shows:
- **The charge figure now agrees with the game's own list.** 2% of charge picks are still not declared: 20 picks in 288 games. I did not
  check these case by case. The list is read once at the start of the turn, so these are probably charges that a move earlier in the
  same turn changed (my reading, not checked).
- **The first-round win chance is slightly cautious on both sides** (67% claimed, 74% won). It is not an overclaim.
- **The overclaims are unchanged.** These items are later in the plan: shoot (3x), hold (3x), close in (claims 54 VP but charges next turn 14% of
  the time), and risk (about 1.6x).

## 2. Headline

| # | Number | **ON** | **OFF** |
| --- | --- | --- | --- |
| 1 | VP margin per game | **+57 ±64** | -57 |
| 2 | First round won when charging | 75% | 74% |
| 3 | Net points per charged fight | +74 | +73 |
| 4 | Points lost per game | 711 | 749 |
| 5 | Free units caught in flank or rear (per game) | 0.64 | 0.59 |

ON as Mine -54, ON as Opponent +169 (the Opponent seat is stronger in these pairs either way). Going first +47, second +67.
Won / drawn / lost 121 / 46 / 121. Pairs ahead 58, behind 59.

**VP by source (per game):** kills 790 v 748, objectives 574 v 564, leaders 57 v 52. Charges declared 4.8 a game on both sides.

## 3. Shot or charge

It priced a shot and a friend's charge together **124 times in 288 games** (0.4 a game).

| Shoot picks that did not fire at their target | ON | OFF |
| --- | --- | --- |
| Share of shoot picks | 28% | 30% |
| ...shot another enemy instead | 54% | 53% |
| ...did not shoot at all | 46% | 47% |
| ...a friend had charged the target that turn | 24% | 31% |

The switch removes some of the "a friend charged it first" cases, but those were only a quarter of the misses. The other causes are
untouched: the unit has no shot from where it stands, or its own move loses the line. The gain-risk finding named both.

## 4. Charges left off, and what blocked them (Morten: "include charge lines and paths")

ON left off **14.8 charges a game** that its own estimate would have offered, at an average estimated reach of 85%. A charge that stays out of reach is
counted again each turn.

| Why the game does not offer it | Share | Of them, reach 50%+ by the estimate |
| --- | --- | --- |
| **Outside its front arc** | 49% | 1,827 of 2,106 |
| Way or sight blocked | 42% | 1,616 of 1,776 |
| Rallied this turn | 4% | |
| Stupidity | 3% | |
| Scouts (no charge in turn 1) | 2% | |
| Miasmic Mirage | 1% | |

**Cause 1 (from the code and the log lines):** the reach estimate gives reach to targets that the computer's own front-arc check says are
outside the arc. Half of the charges left off are such targets, at 85% estimated reach on average, and the game never allows them.

For "way or sight blocked", what lies on the straight line from the charger to the target. This is the measuring script's own corridor, as wide
as the charger's front, so it is an estimate:

| What lies on the straight line | Share |
| --- | --- |
| Nothing (see below) | 63% |
| Another enemy unit | 15% |
| A friend that is not charging | 9% |
| A hill or a wood (sight) | 12% |
| A friend charging another enemy | 1% |
| **A friend charging the same target (a joint charge)** | 1% (10 in 288 games) |
| Impassable terrain | 1% |

**Cause 2 (my reading of the code, not proved case by case):** for "nothing on the straight line", the game measures the path including the
wheel the charge needs against the maximum charge range. It also needs half the models to see the target. The estimate uses the straight gap.

**The build thread's warning (the second unit of a joint charge):** in 472 cases (1.6 a game) a charge was left off while a friend did charge
that same target that turn. In only **10 of them (in 288 games)** was that friend standing on the path. Most were outside the front arc
(225) or had nothing on the straight line (126). The cost of the warning is small. None of the left-off units charged that target later in the turn.

## 5. For a follow-up

- **The reach estimate should check the front arc**, and the way with its wheel, as the game does. Then nothing needs leaving off: the
  estimate and the list would agree from the start. This removes cause 1 and probably most of cause 2.
- Shoot jobs: 28% still miss their target, for causes these switches do not touch (no shot from where it stands, own move). This is item 12
  of the plan (the move carries out the job).

Scripts: `scripts/` here (odds.py, measures.py, leftoff.py, build.py, h.py; job_claims.py is the corrected one from 6skrm4).
