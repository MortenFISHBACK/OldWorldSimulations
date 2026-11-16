# Gun fixes head-to-head (2026-11-16 afternoon) - one part

Does the computer with the full shooting plan, its target fixes AND the four gun fixes (gun-figures, gun-mask, gun-view, gun-threat)
beat main? In every game ONE side plays everything on, the other side plays as main (all six switches off for that side).

144 DKTC games (Hero v Hero = static-static, seed 1, scenarios mix), the same shooting-heavy pairs as this morning's batch
(/mnt/project-files/shooting-fixes-h2h-2026-11-16/), played twice so side and first-turn effects cancel:

- **Parts 1-4 = mine-1..4**: everything ON for Mine, OFF for Opponent (`--rules-off` from `off-for-opponent.txt`), pairs-1..4.txt;
- **Parts 5-8 = opp-1..4**: everything ON for Opponent, OFF for Mine (`--rules-off` from `off-for-mine.txt`), pairs-1..4.txt
  (part 5 = opp-1 = pairs-1.txt, part 6 = opp-2, part 7 = opp-3, part 8 = opp-4).

36 games per part. One part per thread. No Haiku. No commits, no pushes.

Build: branch `claude/project-thread-iol9md` at `0533c462` (= main c7c800290 + shooting plan + target fixes + gun fixes).

## Commands

    cd <repo> && git fetch origin claude/project-thread-iol9md && git checkout -B gf-h2h 0533c462
    git log --oneline -1          # must start 0533c462
    dotnet --version              # if it is not 10.x:  bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"
    D=/mnt/project-files/gun-fixes-h2h-2026-11-16

  mine-N (parts 1-4, N = part number):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-opponent.txt)" --keep-as measurement --batch gf-h2h-mine-0533c46-pN \
      --look-for $D/look-for.md > ~/gf-h2h-mine-N.log 2>&1

  opp-N (parts 5-8, N = part number minus 4):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-mine.txt)" --keep-as measurement --batch gf-h2h-opp-0533c46-pN \
      --look-for $D/look-for.md > ~/gf-h2h-opp-N.log 2>&1

Run it with the Bash tool's run_in_background (timeout 7200000).

**Resumable**: a part that stops (the 2-hour run limit, a container restart, "No space left on device") resumes with exactly the same
command - finished games are skipped. Out of disk: delete old ~/owwt-sim/<batch> folders and the test bin/obj folders first.

**"Another simulation is running in this container"** with nothing running: a leftover MSBuild node holds the lock.
Run `dotnet build-server shutdown; pkill -f MSBuild.dll` and the same command again.

**Check after the first 2-3 games**: the log's first lines say `Rules off:` with the six names `@opponent` (or `@mine`); the game logs'
"Rules off" line names the tags as `TAG@Opponent` (or `@Mine`) and includes FIRE PLAN / fire-plan, every-wound-counts, GUN FIGURES,
GUN MASK, GUN VIEW and GUN THREAT. A game that stops with "is switched off for one side only, but this check does not say for which
side" is a check the port missed: stop and tell the owner thread with the game id and the last log lines.

**Report early**: message the owner thread ("Run gun fixes shooting head-to-head", cmsg_01UAkEmFCZaVyiEY4rv4XRKjBYiPC51xuDg75oRuSVSFVJ)
with your game count after the first ~5 games and about every 30-45 minutes after. If you hit the 2-hour limit, say so and resume.

**When done**: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<mine|opp>-N/, check the
copy (`du -sb` of source and copy match, every game-*.txt non-empty), create an empty file $D/<mine|opp>-N/done, and message the owner
thread with your game count and any findings the log names. No add-sim-replays, no commits: the owner does that.
Do NOT touch /mnt/project-files/join-bonus-h2h-2026-11-16/ (another batch).
