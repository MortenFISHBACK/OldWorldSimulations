# Flank fixes on v off - one part

**ON ARM RERUN (11:58 UTC):** on 101d908c8 the best-figure guard stopped 24/31 and 25/36 on-arm games ("no reason named").
The on parts now run on branch claude/project-thread-jnar25 at 4391d94d5fc3f522178eebb0fbc677e293fa2f2d (101d908c8 + one test-assembly
line: in a sim the guard writes NO REASON instead of stopping). Same games, batch name ff-on-4391d94-pN:

    cd <repo> && git fetch origin claude/project-thread-jnar25 && git checkout -B ff-batch-on 4391d94d5fc3f522178eebb0fbc677e293fa2f2d
    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/on-N-pairs.txt)" --seeds 1 --scenarios mix \
      --keep-as measurement --batch ff-on-4391d94-pN --look-for $D/look-for.md > ~/ff-on-N.log 2>&1

Copy to $D/on-N/ as below. The off arm stays on 101d908c8 (it never stops: a switched-off rule names the reason, so its play is the same).
The stalled first runs are kept in $D/stalled-101d908/.

Owner: thread "Run flank fixes on/off batch" (it runs on-1).
144 DKTC games (Hero v Hero = static-static, seed 1, scenarios mix; the same pairs as the enemy-forecast batches) on main
at 101d908c8f3030dbc72a2e42f5d290514f12764d (flank fixes + best-figure guard), twice:
- on-1..4: all four flank fixes ON (no --rules-off);
- off-1..4: the same games with all four OFF (--rules-off flank-fixes).
36 games a part (about 1-1.5 h; a part that hits the 2-hour run limit resumes with the same command).

    cd <repo> && git fetch origin main && git checkout -B ff-batch 101d908c8f3030dbc72a2e42f5d290514f12764d
    bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"     # if dotnet --version is not 10
    D=/mnt/project-files/flank-fixes-batch-2026-11-13

  on-N:
    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/on-N-pairs.txt)" --seeds 1 --scenarios mix \
      --keep-as measurement --batch ff-on-101d908-pN --look-for $D/look-for.md > ~/ff-on-N.log 2>&1
  off-N:
    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/off-N-pairs.txt)" --seeds 1 --scenarios mix \
      --rules-off flank-fixes --keep-as measurement --batch ff-off-101d908-pN --look-for $D/look-for.md > ~/ff-off-N.log 2>&1

(Replace N with your part number in the pairs file, the batch name and the log name.)
Run it with the Bash tool's run_in_background. No Haiku. One part per thread.
When done: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<on|off>-N/ and message
the owner thread (thread id cmsg_01UAkEmFCZaVyiEY4rv4XRKjJqbdMzrWkSanG4ZQJbiuqT) with your game count. No add-sim-replays, no commits: the owner does that.

Disk: each batch clones the simulation data (~3 GB). If the run stops with "No space left on device", delete old ~/owwt-sim/<batch> folders and the test bin/obj folders, then rerun the same command (it resumes).
