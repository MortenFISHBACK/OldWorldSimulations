# Charge outcomes against simpler pricing: head-to-head (2026-11-17)

**Verdict: level. Charge outcomes is +26 VP a game, give or take 73. That is within noise, and inside the "not worse than -30" band, so it can be kept.**
It changed very few choices: about one decision in every three games. Three of the four switches priced about right or better. "Flees from charge" made
bad charges: the 25 charges it added lost 30 points each on average.

Batch: 288 games, the same 144 DKTC pairs as the other batches today (static v static, seed 1, scenarios mix), each pair played both ways.
Build `claude/project-thread-pf70ph` at `a57fba0d` (simpler pricing + split log + four switches). ON = all four switches on, OFF = simpler pricing.
All 288 games ended. No engine errors and no stuck games. One known sim finding (S-640712, Herdstone destroyed scores nothing, L0226). Pairs ahead 64, behind 53.

## 1. Headline

| # | Number | **Charge outcomes (ON)** | **Simpler (OFF)** |
| --- | --- | --- | --- |
| 1 | VP margin per game | **+26 ±73** | -26 |
| 2 | First round won when charging | 72% | 71% |
| 3 | Net points per charged fight | +94 | +87 |
| 4 | Points lost per game | 716 | 742 |
| 5 | Free units caught in flank or rear (per game) | 0.58 | 0.64 |

ON as Mine -87, as Opponent +139 (the Opponent seat is stronger in these pairs either way); going first +41, second +11. Won / drawn / lost 118 / 52 / 118.

## 2. VP by source (per game)

| Source | ON | OFF |
| --- | --- | --- |
| Objectives | 572 | 565 |
| Kills | 777 | 759 |
| Leaders | 53 | 52 |
| Charges declared | 4.9 | 4.9 |
| Charges that made contact | 71% | 72% |

## 3. Each switch: how often, what it claimed, what happened

| Switch | Charges it priced (a game) | Choices it changed (all 288 games) | Claimed | What happened |
| --- | --- | --- | --- | --- |
| Break outcomes (give ground / fall back) | 2.4 | 24 into a charge, 8 away from one | -1 VP on average (+26 where it changed the choice) | Changed charges: contact 90%, net **+72** each |
| Overrun on (into a fresh enemy) | 0.4 | 9 into a charge, 5 away | +34 VP | Went on into a fresh enemy 15% (OFF 9%), 102 points of that enemy lost when it did, so about 15 VP a charge. **Overclaims about 2x.** Changed charges net +93 (only 9) |
| Stand & Shoot | 0.2 | **none** | -11.5 VP | The target stood and shot 87%, cost 10.2 VP. **Well priced**, but it never changed a choice |
| Flees from charge | 0.5 | 25 into a charge | +20 VP (+90 where it changed the choice) | The target fled 89% as predicted, but only 44% were gone two turns later. Changed charges: **net -30** each |

**Read for a follow-up:**
- **Flees from charge** looks harmful: the 48% of the fleeing unit's points it counts is about twice what happens. That number would need to drop to roughly 20%, or the switch be tested alone.
- **Overrun on** overclaims about 2x but changed few choices. The results of those few were good.
- **Break outcomes** looks sound. It is the most used switch, and the charges it changed did well.
- **Stand & Shoot** is accurate but too small to change anything. It is harmless to keep.

## 4. Stand & Shoot by defending army (charges where the target stood)

| Defender | ON charges | ON S&S | ON VP lost a charge | OFF charges | OFF S&S | OFF VP lost a charge |
| --- | --- | --- | --- | --- | --- | --- |
| Lizardmen | 34 | 68% | 6.1 | 38 | 68% | 11.0 |
| **Dwarfen Mountain Holds** | 47 | 23% | **5.1** | 52 | 23% | **3.9** |
| High Elf Realms | 91 | 25% | 3.1 | 109 | 31% | 4.2 |
| Wood Elf Realms | 89 | 26% | 3.8 | 90 | 29% | 3.2 |
| Tomb Kings | 78 | 28% | 2.3 | 80 | 28% | 2.3 |
| Empire | 112 | 12% | 2.3 | 99 | 14% | 2.1 |
| Ogre Kingdoms | 43 | 30% | 2.2 | 45 | 33% | 0.7 |
| all others | | under 10% | under 0.5 | | | |

Dwarfs: the ON side charged them as often as the OFF side did and lost slightly more to their volleys (5.1 against 3.9 VP a charge, 47 charges: noise).
The switch priced Dwarf volleys, but the price was never big enough to call a charge off.

## 5. Charge outcomes, ON against OFF (contact charges)

| Outcome | ON share | ON net (2 turns) | OFF share | OFF net |
| --- | --- | --- | --- | --- |
| Won, target wiped out | 27% | +92 | 25% | +105 |
| Won, target fled | 17% | +97 | 16% | +112 |
| Won, target gave ground | 12% | +50 | 12% | +83 |
| Won, target fell back in good order | 11% | +111 | 10% | +101 |
| Draw | 6% | +58 | 5% | +16 |
| Lost, gave ground | 5% | +50 | 5% | -9 |
| Lost, wiped out | 5% | -62 | 5% | -64 |

Scripts and the full comparison: compare-all.md in this folder. Next: replay page, archive.
