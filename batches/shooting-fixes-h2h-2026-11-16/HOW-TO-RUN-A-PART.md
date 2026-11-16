# Shooting target fixes head-to-head (2026-11-16) - one part

Does the computer with the full shooting plan AND this morning's three target fixes (every wound counts, honest threat figure, one
yardstick) beat main? In every game ONE side plays everything on, the other side plays as main (switches `shooting-plan` and
`target-fixes` off for that side). The VP margin of the plan side decides.

144 DKTC games (Hero v Hero = static-static, seed 1, scenarios mix), shooting-heavy pairs only (at least one list with 3+ war machines
or 30%+ of its points in shooting units), played twice so side and first-turn effects cancel:

- **mine-1..4**: plan ON for Mine, OFF for Opponent (`--rules-off` from `off-for-opponent.txt`);
- **opp-1..4**: plan ON for Opponent, OFF for Mine (`--rules-off` from `off-for-mine.txt`).

8 parts of 36 games (pairs-1..4.txt). One part per thread. No Haiku.

Build: branch `claude/project-thread-tvghcc` at `439415943c037cd8ea414ca1cce0a02ec135fabe` (code green at
4cf9d6a2; hand-over /mnt/project-files/shooting-plan-target-fixes-2026-11-16/hand-over.md).

## Commands

    cd <repo> && git fetch origin claude/project-thread-tvghcc && git checkout -B sf-h2h 439415943c037cd8ea414ca1cce0a02ec135fabe
    dotnet --version     # if it is not 10.x:  bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"
    D=/mnt/project-files/shooting-fixes-h2h-2026-11-16

  mine-N (plan side = Mine):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-opponent.txt)" --keep-as measurement --batch sf-h2h-mine-4394159-pN \
      --look-for $D/look-for.md > ~/sf-h2h-mine-N.log 2>&1

  opp-N (plan side = Opponent):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-mine.txt)" --keep-as measurement --batch sf-h2h-opp-4394159-pN \
      --look-for $D/look-for.md > ~/sf-h2h-opp-N.log 2>&1

Replace N with your part number (pairs file, batch name, log name). Run it with the Bash tool's run_in_background (timeout 7200000).

**Resumable**: a part that stops (the 2-hour run limit, a container restart, "No space left on device") resumes with exactly the same
command - finished games are skipped. Out of disk: delete old ~/owwt-sim/<batch> folders and the test bin/obj folders first.

**"Another simulation is running in this container"** with nothing running: a leftover MSBuild node holds the lock.
Run `dotnet build-server shutdown; pkill -f MSBuild.dll` and the same command again.

**Check after the first 2-3 games**: the log's first lines say `Rules off: shooting-plan@opponent,target-fixes@opponent` (or `@mine`);
the game logs' "Rules off" line names the tags as `TAG@Opponent` (or `@Mine`) and includes fire-plan and every-wound-counts. A game
that stops with "is switched off for one side only, but this check does not say for which side" is a check the port missed: stop and
tell the owner thread with the game id and the last log lines.

**Report early**: message the owner thread ("Run shooting target fixes head-to-head",
cmsg_01UAkEmFCZaVyiEY4rv4XRKjRCf4GJJ6X35WQfXVuZmB2d) with your game count after the first ~5 games and about every 30-45 minutes after.

**When done**: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<mine|opp>-N/, check the
copy (`du -sb` of source and copy match, every game-*.txt non-empty), create an empty file $D/<mine|opp>-N/done, and message the owner
thread with your game count and any findings the log names. No add-sim-replays, no commits: the owner does that.
