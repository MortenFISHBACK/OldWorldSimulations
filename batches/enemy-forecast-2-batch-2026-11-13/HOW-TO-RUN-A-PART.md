# Expected enemy turn (second version): one side predicts, the other does not - one part

Owner: thread "Predict the enemy's next turn". Replaces the round robin of the night of 12-13 Nov (Morten 23:36 UTC).
144 DKTC games (Hero v Hero, seed 1, scenarios mix; the same pairs as the first enemy-forecast batch) on branch claude/project-thread-oaxa63
at f5fe7c8140e2ce2e7eaa23902f08ce20878c5747, twice:
- mine-1..4: only the computer playing Mine uses the prediction (--rules-off enemy-forecast@opponent);
- opp-1..4: the same games, only the computer playing Opponent uses it (--rules-off enemy-forecast@mine).
36 games a part (about 1-1.5 h; a part that hits the 2-hour run limit resumes with the same command).

    cd <repo> && git fetch origin claude/project-thread-oaxa63 && git checkout -B ef2-batch f5fe7c8140e2ce2e7eaa23902f08ce20878c5747
    bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"     # if dotnet --version is not 10
    D=/mnt/project-files/enemy-forecast-2-batch-2026-11-13

  mine-N:
    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/mine-N-pairs.txt)" --seeds 1 --scenarios mix \
      --rules-off enemy-forecast@opponent --keep-as measurement --batch ef2-mine-f5fe7c8-pN --look-for $D/look-for.md > ~/ef2-mine-N.log 2>&1
  opp-N:
    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/opp-N-pairs.txt)" --seeds 1 --scenarios mix \
      --rules-off enemy-forecast@mine --keep-as measurement --batch ef2-opp-f5fe7c8-pN --look-for $D/look-for.md > ~/ef2-opp-N.log 2>&1

Run it with the Bash tool's run_in_background. No Haiku. One part per thread.
When done: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<mine|opp>-N/ and message
the owner thread. No add-sim-replays, no commits: the owner does that.

Disk: each batch clones the simulation data (~3 GB). If the run stops with "No space left on device", delete old ~/owwt-sim/<batch> folders and the test bin/obj folders, then rerun the same command (it resumes).
