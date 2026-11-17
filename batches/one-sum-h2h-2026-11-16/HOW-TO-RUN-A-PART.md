# Simpler pricing head-to-head (2026-11-16) - one part

Does the computer with seven changes on (advance-worth, idle-cost, risk-once and the four one-sum rules) beat main?
In every game ONE side plays with all seven on and the other side plays with all seven off (= main e8dd114c3). Everything else
stays ON for both sides. The VP margin of the change side decides.

144 DKTC games (Hero v Hero = static-static, seed 1, scenarios mix), the same pairs and seeds as the earlier head-to-heads,
played twice so side and first-turn effects cancel. 8 parts of 36 games, one per thread. No Haiku.

| Part thread | Folder | Pairs file | Change ON for | `--rules-off` file | Batch name |
| --- | --- | --- | --- | --- | --- |
| part 1 | mine-1 | pairs-1.txt | Mine | off-for-opponent.txt | os-h2h-mine-779e261-p1 |
| part 2 | mine-2 | pairs-2.txt | Mine | off-for-opponent.txt | os-h2h-mine-779e261-p2 |
| part 3 | mine-3 | pairs-3.txt | Mine | off-for-opponent.txt | os-h2h-mine-779e261-p3 |
| part 4 | mine-4 | pairs-4.txt | Mine | off-for-opponent.txt | os-h2h-mine-779e261-p4 |
| part 5 | opp-1 | pairs-1.txt | Opponent | off-for-mine.txt | os-h2h-opp-779e261-p1 |
| part 6 | opp-2 | pairs-2.txt | Opponent | off-for-mine.txt | os-h2h-opp-779e261-p2 |
| part 7 | opp-3 | pairs-3.txt | Opponent | off-for-mine.txt | os-h2h-opp-779e261-p3 |
| part 8 | opp-4 | pairs-4.txt | Opponent | off-for-mine.txt | os-h2h-opp-779e261-p4 |

(Parts 1-4 switch the changes off for Opponent; parts 5-8 switch them off for Mine.)

Build: branch `claude/project-thread-7uh7a9` at `779e2613` (on top of bxyvbn bc15267e, built on main e8dd114c3; repo note
docs/claude-memory/project_one_sum_2026-11-16.md).

Do NOT touch other batch folders on the shared folder. Delete nothing there.

## Commands

    cd <repo> && git fetch origin claude/project-thread-7uh7a9 && git checkout -B os-h2h 779e2613
    git log --oneline -1   # must start 779e2613
    dotnet --version     # if it is not 10.x: bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"; export DOTNET_ROOT="$HOME/.dotnet"
    D=/mnt/project-files/one-sum-h2h-2026-11-16

  Parts 1-4 (folder mine-N, change ON for Mine):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-opponent.txt)" --keep-as measurement --batch os-h2h-mine-779e261-pN \
      --look-for $D/look-for.md > ~/os-h2h-mine-N.log 2>&1

  Parts 5-8 (folder opp-N, change ON for Opponent):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-mine.txt)" --keep-as measurement --batch os-h2h-opp-779e261-pN \
      --look-for $D/look-for.md > ~/os-h2h-opp-N.log 2>&1

N is the pairs number from the table (part 5 uses pairs-1, part 6 pairs-2, ...). Run it with the Bash tool's run_in_background
(timeout 7200000), and re-run the same command when it stops before 36 games.

**Resumable**: a part that stops (the 2-hour run limit, a container restart, "No space left on device") resumes with exactly the same
command - games with a `done` marker in the batch folder are skipped. Out of disk: delete old ~/owwt-sim/<batch> folders and the test
bin/obj folders first (in your own container only).

**"Another simulation is running in this container"** with nothing running: a leftover MSBuild node still holds the lock.
Run `dotnet build-server shutdown; pkill -f MSBuild.dll` and the same command again.

**Report early**: message the owner thread ("Test simpler pricing against main", cmsg_01UAkEmFCZaVyiEY4rv4XRKjVPjSp2vJZgS1c2NEGbJGze)
with your game count after the first ~5 games and about every 45 minutes after. Also append one line to
$D/counts.log: `<UTC time> part N <games done>/36`. Say if any game hit the Movement phase time limit (the log or game report says so).

**Check after the first 2-3 games**: the log's first lines say the rules off with `@opponent` (parts 1-4) or `@mine` (parts 5-8);
the batch's rules-off.txt names ADVANCE WORTH, IDLE COST, RISK ONCE, ONE FIGHT FORMULA, COVER ONCE, CHAFF IN THE MOVE and
ONE OBJECTIVE FORMULA, each @Opponent (or @Mine). The change side's game logs should show some of those tags; both sides show
"JOB RISK" rows. A game that stops with "is switched off for one side only, but this check does not say for which side" is a check
the port missed: stop and tell the owner thread with the game id and the last log lines.

**Keep it small**: the shared folder is near its limit (10 GB / 50,000 files). Copy only the batch folder and the log, nothing else
(no build output, no databases).

**Shared folder**: copy ONLY when the part is done, then check the copy: `du -sb` of source and copy must match and every game-*.txt must
be non-empty. A refused write looks saved but is not kept - if sizes differ, tell the owner thread at once.

**When done**: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<mine|opp>-N/,
create an empty file $D/<mine|opp>-N/done, and message the owner thread with your game count and any findings the log names.
No add-sim-replays, no commits: the owner does that.
