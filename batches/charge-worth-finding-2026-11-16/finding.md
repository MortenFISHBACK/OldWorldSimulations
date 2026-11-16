# Why honest odds changed nothing, and what would (16 November 2026)

Analysis only: nothing built, nothing pushed, no batch run. Data: the charge odds + band head-to-head (288 games,
/mnt/project-files/charge-band-h2h-2026-11-15/). "Honest side" = odds fixes and band on; "main" = both off.

## Short answer

1. **The honest side did not drop sure charges. It makes the same charges and calls them by lower numbers.**
2. **Honest odds cannot change play much, because the charge's worth hardly looks at the odds.** The worth figure promises about
   +120 VP for a 13% charge and for a 92% charge alike. Really they earn +11 and +102.
3. **The band rule is rare because a helper is rarely there.** In 2 of 3 charges at 55-75% no free friendly unit stands within 12" of
   the target. Joint charges are lost a turn earlier: 84% of "close in to charge next turn" moves never charge that target.
4. **The 90-94% band (says 92, wins 84) is one sample, not two,** and looks like noise.

## 1. The "missing" sure charges (question B)

Main shows 146 "sure, not overkill" charges against 97. But over the whole batch the two sides fight the same fights:

| Per side, 288 games | Honest side | Main |
| --- | --- | --- |
| Charged fights | 965 | 953 |
| Charger points per fight | 282 | 285 |
| Fights against a unit with a joined character | 18% | 21% |
| Fights against a lone character | 17% | 17% |
| First round won | 72% | 71% |
| Odds said, on average | 72% | 76% |

**Same position, same charge, lower number.** Each pair of lists was played twice with the sides swapped, so both games are identical
until the first decision that differs. In 141 pairs I found that point. Where both sides picked the same charge from the same position:

| Game | Charge | Main said | Honest said |
| --- | --- | --- | --- |
| L0729 | Exalted Champion on Empire Knights | 96% | 91% |
| L0628 | Gyrobomber on Chaos Warhounds | 94% | 89% |
| L1719 | Skink Chief on Goblin Wolf Riders | 96% | 92% |
| L2029 | Giant Rats on Chaos Warhounds | 95% | 92% |
| L0311 | Shugengan Lord on Daemonsmith Sorcerer | 81% | 72% |
| L1823 | Sabretusks on Skeleton Horse Archers | 76% | 70% |

A charge main calls 94-96% is called 89-92% by the honest side: it leaves the "90%+" count without anything changing on the table.
That is why the honest side's lower bands win more than main's (76-89%: 83% v 77%; 60-75%: 68% v 57%): main's better fights moved
down into them.

**Charges only one side made, same position:** 7 by the honest side only, 4 by main only. The 4 main-only ones were all long shots
(L0102 Razorgor on Primal Warherd 0%, Tuskgor Chariot on it 1%; L0612 Gyrobomber on Shugengan General 15%, Gyrocopter on him 42%).
The honest side closed in or advanced instead. In no case did the honest side skip a sure charge main made.

**No bar is tuned to the old odds in a way that bites.** The rules that compare odds with a bar fire about as often on both sides
(a game: charge now first 2.9 v 3.0, long shot 0.5 v 0.6, sure charge beats advance 0.1 v 0.1, pile-on halved 0.3 v 0.2).

## 2. Why honest odds do not change play (the real finding)

The computer picks by the charge's **worth in VP**, not by the odds. The worth counts the target's points by the chance it is slain or
flees, a fifth of them for a won round that goes on, and takes off the wounds it expects back and the chance it flees and is caught.
A lost first round as such costs nothing. So the worth is nearly the same whatever the odds:

| Odds said (lone chargers, both sides) | Fights | Worth the charge line said | Points really earned, net | First round won |
| --- | --- | --- | --- | --- |
| under 25% | 99 | +117 | **+11** | 13% |
| 25-49% | 117 | +115 | +54 | 41% |
| 50-59% | 85 | +97 | +65 | 61% |
| 60-75% | 172 | +131 | +73 | 65% |
| 76-89% | 240 | +128 | +93 | 81% |
| 90%+ | 393 | +135 | **+102** | 92% |

What a first round really decides (all 1,913 fights): **won** = the target gives 83% of its points and the charger loses 12% of its own
(net +114 a fight); **lost** = the target gives 30% and the charger loses 45% (net -30).

So the odds are now honest, but the figure that decides is not. One charge in six is still made under 50% (and wins 28%).

## 3. Why the band rule almost never fires (question A)

- The honest side declared 287 charges at 55-75% alone (1 a game). In **188 of them (66%) no free friendly unit (characters not
  counted) was within 12" of the target.** In half of all charges the nearest free friend is more than 14" from the target.
- Where a friend was near (99): help was asked 24 times, the friend charged the same target anyway 14 times, and 61 times it had its
  own job (31 advancing elsewhere, 12 closing in on another target, 7 charging another target, 6 holding a marker, 5 other).
- So "+15 points and 76% together" is not the main brake. The rule sits at the last step. The step before it leaks: the computer
  plans 1.4 "close in together" moves a game, yet only 16% of all close-in moves (244 of 1,490) charge that target next turn, and
  joint charges stay at 0.5 a game.

## 4. The 90-94% band (question 3)

The odds-only batch and this batch are the same games (244 of 252 shared games ended with the same score), so "84% in both batches"
is one sample of 76 fights: 64 won, 5 drawn, 7 lost, where 6 not won were expected and 12 came. Main's side in the same band: 63 of 69
won. Both sides together: 12% not won against 8% said, inside noise. The 12 are small fights with low scores (draws 1-1, 2-2, 3-3;
four of the seven losses by one point), with no challenge, spell or joined character in 10 of them. No fault found; watch it in the
next batch that plays different games.

## 5. Options (numbers both brains read; no labels, no special cases)

| # | Option | Default | Hours |
| --- | --- | --- | --- |
| 1 | **Make the charge's worth honest, as the odds were.** Count a lost first round at what it really costs (charger loses about 45% of its points and the target gives 30%; won: 12% and 83%), so the worth follows the odds. Long shots drop by about 100 VP against sure charges; waiting a turn for a surer or joint charge, and a helper that lifts the odds, start to pay by the figures. Built on the honest-odds branch, with its own switch. | [Yes] | 6-8 build, then one head-to-head |
| 2 | **Find why set-ups do not become charges** (84% of close-in moves never charge their target; joint charges 0.5 a game). Analysis thread, ends with a plan. This is where multi-unit charges are lost, and where "friends too far apart" belongs. | [Yes, alongside 1] | 3-4 |
| 3 | **Honest odds and band rule: keep on the branch, land together with option 1** after its head-to-head (they are a dead heat alone, and option 1 needs them). Alternative: land now. | [Keep, land with 1] | 0 |
| 4 | **Loosen the band rule** (drop "+15 points", or ask from 50%). Would lift 33 asks to about 45 a batch: still too rare to matter. | [No] | 2 |
| 5 | **90-94% band:** leave as is and re-check on a batch with different games. Alternative: widen the spread once more. | [Leave] | 0 (alternative 1 + batch) |

What option 1 can and cannot do: if every charge under 50% were left out, first round won would rise from 72% to about 80%. It will not
reach Morten's 96% alone; his other half is joint and flank charges set up a turn ahead (option 2) and running down what breaks
(369 points a game against the computer's 97). Long shots still earn a little on average (+11 to +54), so the VP gain depends on what
those units do instead; only a head-to-head can show it.

## Files

scripts/div.py (first different decision per pair), scripts/help.py (free friends near each charge's target). The per-fight tables
come from the batch's own scripts (charge-band-h2h-2026-11-15/scripts).
