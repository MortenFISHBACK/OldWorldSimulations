# Combined charge + shooting head-to-head (2026-11-16) - one part

Does the computer with ALL of this morning's changes (honest charge odds + charge band + honest worth + shooting plan with its target
fixes) beat the same computer as main? In every game ONE side plays with the changes and the other side has them all switched off.

144 DKTC games (Hero v Hero = static-static, seed 1, scenarios mix), the SAME pairs and seeds as the charge worth head-to-head
(/mnt/project-files/charge-worth-h2h-2026-11-16/), played twice so side and first-turn effects cancel:

- **mine-1..4**: changes ON for Mine, OFF for Opponent (`--rules-off` from `off-for-opponent.txt` =
  `charge-odds@opponent,charge-band@opponent,honest-worth@opponent,shooting-plan@opponent`);
- **opp-1..4**: changes ON for Opponent, OFF for Mine (`--rules-off` from `off-for-mine.txt` =
  `charge-odds@mine,charge-band@mine,honest-worth@mine,shooting-plan@mine`).

(`shooting-plan` = fire plan incl. the three target fixes + shots-over-turns.) 8 parts of 36 games (pairs-1..4.txt). One part per
thread. No Haiku. Everything else stays ON for both sides.

Build: branch `claude/project-thread-tnhumk` at `ea652ef11` (main f3d2be2c + charge line 5irtu9 + shooting line tvghcc, suite green).

Do NOT touch other batch folders on the shared folder. Delete nothing there.

## Commands

    cd <repo> && git fetch origin claude/project-thread-tnhumk && git checkout -B combined-h2h FETCH_HEAD
    git log -1 --format=%h       # must print ea652ef1 - if not, stop and tell the owner thread
    dotnet --version     # if it is not 10.x: bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"; export DOTNET_ROOT="$HOME/.dotnet"
    D=/mnt/project-files/combined-h2h-2026-11-16

  mine-N (changed side = Mine):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-opponent.txt)" --keep-as measurement --batch ch-h2h-mine-ea652ef-pN \
      --look-for $D/look-for.md > ~/ch-h2h-mine-N.log 2>&1

  opp-N (changed side = Opponent):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-mine.txt)" --keep-as measurement --batch ch-h2h-opp-ea652ef-pN \
      --look-for $D/look-for.md > ~/ch-h2h-opp-N.log 2>&1

Replace N with your part number (pairs file, batch name, log name). Run it with the Bash tool's run_in_background.

**Resumable**: a part that stops (the 2-hour run limit, a container restart, "No space left on device") resumes with exactly the same
command - games with a `done` marker in the batch folder are skipped. Out of disk: delete old ~/owwt-sim/<batch> folders and the test
bin/obj folders first (in your own container only).

**"Another simulation is running in this container"** with nothing running: a leftover MSBuild node still holds the lock.
Run `dotnet build-server shutdown; pkill -f MSBuild.dll` and the same command again.

**Report early**: message the owner thread ("Run combined charge and shooting head-to-head",
cmsg_01UAkEmFCZaVyiEY4rv4XRKjNuvwJh2mtjQkRLetU6zQ5C) with your game count after the first ~5 games and about every 30-45 minutes after.

**Check after the first 2-3 games**: the log's first lines say `Rules off: charge-odds@opponent,charge-band@opponent,honest-worth@opponent,shooting-plan@opponent`
(or `@mine`); the game logs' "Rules off" line and the batch's rules-off.txt name the tags as `TAG@Opponent` (or `@Mine`) and include
CHARGE BAND, HONEST WORTH and FIRE PLAN. A game that stops with "is switched off for one side only, but this check does not say for which
side" is a check the merge missed: stop and tell the owner thread with the game id and the last log lines.

**Shared folder**: copy ONLY when the part is done, then check the copy: `du -sb` of source and copy must match and every game-*.txt must
be non-empty. A refused write looks saved but is not kept - if sizes differ, tell the owner thread at once.

**When done**: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<mine|opp>-N/,
create an empty file $D/<mine|opp>-N/done, and message the owner thread with your game count and any findings the log names.
No add-sim-replays, no commits: the owner does that.
