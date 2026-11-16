# Staying to shoot head-to-head (2026-11-15) - one part

Does the computer with the seven shooting and missile changes ("shots over turns") beat the same computer without them? In every game ONE
side plays with the changes and the other side plays as main 8a44e6692. The VP margin of the changed side decides whether it lands.

144 DKTC games (Hero v Hero = static-static, seed 1, scenarios mix), the same pairs and seeds as head-to-head 2
(/mnt/project-files/framework-head-to-head-2-2026-11-14/), played twice so side and first-turn effects cancel. Same convention as head-to-head 2:

- **shots-mine-1..4**: changes ON for Mine, OFF for Opponent (`--rules-off` from `off-for-opponent.txt` = `shots-over-turns@opponent`);
- **shots-opp-1..4**: changes ON for Opponent, OFF for Mine (`--rules-off` from `off-for-mine.txt` = `shots-over-turns@mine`).

8 parts of 36 games (pairs-1..4.txt). One part per thread. No Haiku. Everything else (job framework, charge fixes, flank fixes) stays ON for both sides.

Build: branch `claude/project-thread-dnukaz` at `7c46ffc15` (main 8a44e6692 merged in; build hand-over
/mnt/project-files/shots-and-missiles-2026-11-14/build-handover.md).

## Commands

    cd <repo> && git fetch origin claude/project-thread-dnukaz && git checkout -B shots-h2h 7c46ffc15
    bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"     # if dotnet --version is not 10
    D=/mnt/project-files/shots-head-to-head-2026-11-15

  shots-mine-N (changed side = Mine):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-opponent.txt)" --keep-as measurement --batch shots-h2h-mine-7c46ffc-pN \
      --look-for $D/look-for.md > ~/shots-h2h-mine-N.log 2>&1

  shots-opp-N (changed side = Opponent):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-mine.txt)" --keep-as measurement --batch shots-h2h-opp-7c46ffc-pN \
      --look-for $D/look-for.md > ~/shots-h2h-opp-N.log 2>&1

Replace N with your part number (pairs file, batch name, log name). Run it with the Bash tool's run_in_background.

**Resumable**: a part that stops (the 2-hour run limit, a container restart, "No space left on device") resumes with exactly the same
command - games with a `done` marker in the batch folder are skipped. Out of disk: delete old ~/owwt-sim/<batch> folders and the test
bin/obj folders first.

**"Another simulation is running in this container"** with nothing running: a leftover MSBuild node from the build still holds the lock.
Run `dotnet build-server shutdown; pkill -f MSBuild.dll` and the same command again.

**Report early**: message the owner thread ("Run shots head-to-head and report", cmsg_01UAkEmFCZaVyiEY4rv4XRKjXgpFsVHKUqFGjsdiH4dDmK)
with your game count after the first ~5 games and about every 30-45 minutes after.

**Check after the first 2-3 games**: the log's first lines say `Rules off: shots-over-turns@opponent` (or `@mine`); the game logs' "Rules off"
line and the batch's rules-off.txt name the tags as `TAG@Opponent` (or `@Mine`). A game that stops with "is switched off for one side only, but
this check does not say for which side" is a check the port missed: stop and tell the owner thread with the game id and the last log lines.

**When done**: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<shots-mine|shots-opp>-N/,
create an empty file $D/<shots-mine|shots-opp>-N/done, and message the owner thread with your game count and any findings the log names.
No add-sim-replays, no commits: the owner does that.

## Reading the result (owner)

- Changed side: Mine in shots-mine-*, Opponent in shots-opp-*. Its VP margin = (changed side's VP - other side's VP) over all 288 games.
