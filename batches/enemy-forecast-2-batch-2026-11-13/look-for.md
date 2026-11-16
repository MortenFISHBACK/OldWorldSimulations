# Expected enemy turn, second version (on v off)

The computer now predicts the enemy's next turn by running its own objective figures from the enemy's side: each enemy unit's best option (charge whom, shoot whom, hold which marker, advance on whom) is what it is expected to do, and a planned move says where the unit should end. Shots use the shooting phase's own target figure; a charge is only expected when it is worth 60 VP or more unless the enemy's own plan says so. An enemy that can reach a unit but plans something else counts as a threat to it only by the chance it picks it (at least 25%); an enemy that plans to charge it counts in full.

Watch for:
- units walking into charges the forecast said would go elsewhere (the price of trusting it);
- fewer turns to face and safer-than-job moves, more advances and charges;
- the hidden FORECAST RESULT rows: how often the expected action was right (charge, shoot, move) - first batch: charge 30-33%, shoot 23%, move 87% - and how close the expected end of a move was to where the unit ended.

One side predicts, the other does not: in mine-1..4 only the computer playing Mine uses the prediction, in opp-1..4 (the same games) only the one playing Opponent. Both sides still write the prediction rows.
