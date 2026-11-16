# Shooting plan head-to-head (2026-11-15) - one part

Does the computer with the army-wide shooting plan (switch group `shooting-plan`) beat the same computer without it? In every game ONE
side plays with the plan and the other side plays as main (the plan switched off). The VP margin of the plan side decides.

144 DKTC games (Hero v Hero = static-static, seed 1, scenarios mix), the SAME pairs and seeds as the top-killer head-to-head
(/mnt/project-files/top-killer-h2h-2026-11-15/), played twice so side and first-turn effects cancel:

- **mine-1..4**: plan ON for Mine, OFF for Opponent (`--rules-off` from `off-for-opponent.txt` = `shooting-plan@opponent`);
- **opp-1..4**: plan ON for Opponent, OFF for Mine (`--rules-off` from `off-for-mine.txt` = `shooting-plan@mine`).

8 parts of 36 games (pairs-1..4.txt). One part per thread. No Haiku. Everything else stays ON for both sides.

Build: branch `claude/project-thread-58bw08` at `89601eafa9e19e20737fe37e3849b6aebd048c5e` (hand-over
/mnt/project-files/shooting-plan-2026-11-15/hand-over.md).

## Commands

    cd <repo> && git fetch origin claude/project-thread-58bw08 && git checkout -B sp-h2h 89601eafa9e19e20737fe37e3849b6aebd048c5e
    bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"     # if dotnet --version is not 10
    D=/mnt/project-files/shooting-plan-h2h-2026-11-15

  mine-N (plan side = Mine):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-opponent.txt)" --keep-as measurement --batch sp-h2h-mine-89601ea-pN \
      --look-for $D/look-for.md > ~/sp-h2h-mine-N.log 2>&1

  opp-N (plan side = Opponent):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-mine.txt)" --keep-as measurement --batch sp-h2h-opp-89601ea-pN \
      --look-for $D/look-for.md > ~/sp-h2h-opp-N.log 2>&1

Replace N with your part number (pairs file, batch name, log name). Run it with the Bash tool's run_in_background.

**Resumable**: a part that stops (the 2-hour run limit, a container restart, "No space left on device") resumes with exactly the same
command - games with a `done` marker in the batch folder are skipped. Out of disk: delete old ~/owwt-sim/<batch> folders and the test
bin/obj folders first.

**"Another simulation is running in this container"** with nothing running: a leftover MSBuild node still holds the lock.
Run `dotnet build-server shutdown; pkill -f MSBuild.dll` and the same command again.

**Report early**: message the owner thread ("Run shooting plan head-to-head and report", cmsg_01UAkEmFCZaVyiEY4rv4XRKj1BL5ZpGfm8xQPojTnNzJFQ)
with your game count after the first ~5 games and about every 30-45 minutes after.

**Check after the first 2-3 games**: the log's first lines say `Rules off: shooting-plan@opponent` (or `@mine`); the game logs' "Rules off"
line and the batch's rules-off.txt name the tags as `TAG@Opponent` (or `@Mine`) and include fire-plan. A game that stops with "is switched
off for one side only, but this check does not say for which side" is a check the port missed: stop and tell the owner thread with the
game id and the last log lines.

**Shared folder is nearly full**: copy ONLY when the part is done, then check the copy: `du -sb` of source and copy must match and every
game-*.txt must be non-empty. A refused write looks saved but is not kept - if sizes differ, tell the owner thread at once.

**When done**: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<mine|opp>-N/,
create an empty file $D/<mine|opp>-N/done, and message the owner thread with your game count and any findings the log names.
No add-sim-replays, no commits: the owner does that.
