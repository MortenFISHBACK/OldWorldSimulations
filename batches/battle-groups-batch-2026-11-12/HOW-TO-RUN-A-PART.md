# Battle groups on v off, one part (owner: thread "Rework battle groups and combined arms")

144 DKTC games (Hero v Hero, seed 1, scenarios mix) on branch claude/project-thread-uezmnz at 789c37f6a, twice: parts on-1..4 with all
rules on, parts off-1..4 the same games with the battle groups off. 36 games a part (about 50 min).

    cd <repo> && git fetch origin claude/project-thread-uezmnz && git checkout -B bg-batch 789c37f6a
    bash scripts/cloud-setup.sh       # if dotnet --version is not 10
    D=/mnt/project-files/battle-groups-batch-2026-11-12

  on-N:
    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/on-N-pairs.txt)" --seeds 1 --scenarios mix \
      --keep-as measurement --batch bg-on-789c37f-pN --look-for $D/look-for.md > ~/bg-on-N.log 2>&1
  off-N:
    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/off-N-pairs.txt)" --seeds 1 --scenarios mix --rules-off battle-groups \
      --keep-as measurement --batch bg-off-789c37f-pN --look-for $D/look-for.md > ~/bg-off-N.log 2>&1

Run it with the Bash tool's run_in_background (nohup dies when the session idles). A stopped run resumes with the same command.
When done: copy the whole batch folder ($BATCH_DIR printed in the log, under the run's data/measurements/<batch>/: game logs, records.db, games.csv) and the log to $D/<on|off>-N/ and tell
the owner thread. No add-sim-replays, no commits: the owner does that.
