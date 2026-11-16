# Charge odds head-to-head (2026-11-15) - one part

Does the computer with the six charge-odds fixes (the `charge-odds` group: joint-knows-challenge, refusing-retires, blows-where-aimed,
spells-in-the-fight, charger-slain-lost, wider-spread) beat the same computer without them? In every game ONE side plays with the fixes and
the other side plays as main 8a44e6692. The VP margin of the fixed side decides.

144 DKTC games (Hero v Hero = static-static, seed 1, scenarios mix), the SAME pairs and seeds as the staying-to-shoot head-to-head
(/mnt/project-files/shots-head-to-head-2026-11-15/), played twice so side and first-turn effects cancel:

- **mine-1..4**: fixes ON for Mine, OFF for Opponent (`--rules-off` from `off-for-opponent.txt` = `charge-odds@opponent`);
- **opp-1..4**: fixes ON for Opponent, OFF for Mine (`--rules-off` from `off-for-mine.txt` = `charge-odds@mine`).

8 parts of 36 games (pairs-1..4.txt). One part per thread. No Haiku. Everything else stays ON for both sides.

Build: branch `claude/project-thread-qcp1ro` at `324c3427502a1fd715ab41b44cdf149cf493e1f4` (on main 8a44e6692; build hand-over
/mnt/project-files/charge-odds-fixes-2026-11-15/hand-over.md).

Do NOT touch /mnt/project-files/top-killer-h2h-2026-11-15/ (another batch running).

## Commands

    cd <repo> && git fetch origin claude/project-thread-qcp1ro && git checkout -B co-h2h 324c3427502a1fd715ab41b44cdf149cf493e1f4
    bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"     # if dotnet --version is not 10
    D=/mnt/project-files/charge-odds-h2h-2026-11-15

  mine-N (fixed side = Mine):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-opponent.txt)" --keep-as measurement --batch co-h2h-mine-324c342-pN \
      --look-for $D/look-for.md > ~/co-h2h-mine-N.log 2>&1

  opp-N (fixed side = Opponent):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-mine.txt)" --keep-as measurement --batch co-h2h-opp-324c342-pN \
      --look-for $D/look-for.md > ~/co-h2h-opp-N.log 2>&1

Replace N with your part number (pairs file, batch name, log name). Run it with the Bash tool's run_in_background.

**Resumable**: a part that stops (the 2-hour run limit, a container restart, "No space left on device") resumes with exactly the same
command - games with a `done` marker in the batch folder are skipped. Out of disk: delete old ~/owwt-sim/<batch> folders and the test
bin/obj folders first.

**"Another simulation is running in this container"** with nothing running: a leftover MSBuild node from the build still holds the lock.
Run `dotnet build-server shutdown; pkill -f MSBuild.dll` and the same command again.

**Report early**: message the owner thread ("Run charge odds head-to-head and report", cmsg_01UAkEmFCZaVyiEY4rv4XRKjF1hTSyWH1LgDTZWwLRZoDc)
with your game count after the first ~5 games and about every 30-45 minutes after.

**Check after the first 2-3 games**: the log's first lines say `Rules off: charge-odds@opponent` (or `@mine`); the game logs' "Rules off"
line and the batch's rules-off.txt name the tags as `TAG@Opponent` (or `@Mine`), and the list includes the six fix names. A game that stops
with "is switched off for one side only, but this check does not say for which side" is a check the port missed: stop and tell the owner
thread with the game id and the last log lines.

**When done**: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<mine|opp>-N/,
create an empty file $D/<mine|opp>-N/done, and message the owner thread with your game count and any findings the log names.
No add-sim-replays, no commits: the owner does that.

## Reading the result (owner)

- Fixed side: Mine in mine-*, Opponent in opp-*. Its VP margin = (fixed side's VP - other side's VP) over all 288 games.
