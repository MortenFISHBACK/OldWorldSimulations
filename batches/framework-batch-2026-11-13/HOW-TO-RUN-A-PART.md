# Job framework on v off - one part

Owner: thread "Run job framework on/off batch" (thread id cmsg_01UAkEmFCZaVyiEY4rv4XRKjQJ3Yc5bSmoPdj5Zs4M8Fx8). It runs on-1.

144 DKTC games (Hero v Hero = static-static, seed 1, scenarios mix; the same pairs as the flank fixes and enemy-forecast batches), on the
framework candidate claude/project-thread-goduf0 at db7ca9c5d (full suite green, 16,604), twice:
- on-1..4: every rule on (no --rules-off);
- off-1..4: the same games with the job framework and its single rules OFF (list below).
36 games a part. A part that hits the 2-hour run limit resumes with the same command.

    cd <repo> && git fetch origin claude/project-thread-goduf0 && git checkout -B fw-batch db7ca9c5d
    bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"     # if dotnet --version is not 10
    D=/mnt/project-files/framework-batch-2026-11-13
    OFF=job-framework,stay-weighed,best-first,random-move-by-figures,random-mover-no-promise,stable-role,wounded-stays-out,best-facing,lost-charge,screen-by-what-it-saves,redirect-by-what-it-stops,shooter-counted-once,lure-by-what-it-draws,hill-by-its-chance,war-engine-jobs

  on-N:
    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/on-N-pairs.txt)" --seeds 1 --scenarios mix \
      --keep-as measurement --batch fw-on-db7ca9c-pN --look-for $D/look-for.md > ~/fw-on-N.log 2>&1
  off-N:
    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/off-N-pairs.txt)" --seeds 1 --scenarios mix \
      --rules-off $OFF --keep-as measurement --batch fw-off-db7ca9c-pN --look-for $D/look-for.md > ~/fw-off-N.log 2>&1

(Replace N with your part number in the pairs file, the batch name and the log name. Flank fixes stay ON in both arms.)
Run it with the Bash tool's run_in_background. No Haiku. One part per thread.

Check after the first 2-3 games: they must end (the best-figure guard writes NO REASON in sims and plays on). A game that stalls: tell
the owner thread at once with the game id and the last log lines.

When done: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<on|off>-N/, create an empty
file $D/<on|off>-N/done, and message the owner thread with your game count and any findings the log names.
No add-sim-replays, no commits: the owner does that.

Disk: each batch clones the simulation data (~3 GB). If the run stops with "No space left on device", delete old ~/owwt-sim/<batch>
folders and the test bin/obj folders, then rerun the same command (it resumes).
