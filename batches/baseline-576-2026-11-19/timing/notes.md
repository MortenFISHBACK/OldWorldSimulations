# Thinking time on main 882d87577, every rule on, Medium v Medium (measurement only)

Two CPU-sampled windows of the game thread (dotnet-trace, sampled thread time): pair R3 seed 1 (5 min) and pair R1 seed 1 (8 min, a
26-minute game). Inclusive share of the game thread's time; a method's share includes everything it calls.

| What | R3 window | R1 window |
| --- | --- | --- |
| Moves planned per unit (PlanMovesCore) | 52% | 80% |
| Five-option pricing per unit (FiveMoveOptions / FiveAt) | 54% / 50% | 49% / 66% |
| Army-wide table run again each turn (TableAgain) | 43% | 63% |
| Walking a candidate spot on real ground (WalkRealGround, RepairSpot) | 36% / 40% | 58% / 59% |
| ... of which the model-by-model path planner (SkirmishStraightMove.PlanUnit) | 34% | 59% |
| Overlap geometry (TryGetMinimumTranslation / MinDistance / BoxGap) | 27% / 23% / 15% | 37% / 16% / 24% |
| Charge geometry (FindBestChargeApproach) | 28% | 19% |
| Holders (BuildHolders / MakeHolderTable) | 19% | 10% |
| The enemy's own choice (HisOwnChoice) | 12% | 22% |
| Objectives (BuildObjectives) | 32% | 25% |

Reading so far: most of the time goes to checking each candidate spot by walking it on the real board with the model-by-model path
planner (sidestepping blockers, overlap geometry) inside the five-option pricing, repeated by the army-wide table each turn.
