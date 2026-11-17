# Five actions against simpler pricing head-to-head (2026-11-17) - one part

Does the computer with five-action on beat the simpler pricing? Both sides play the same build with the simpler-pricing switches ON
(advance-worth, idle-cost, risk-once, one-sum). In every game ONE side also has five-action ON (with all its parts); the other side has
five-action OFF (`--rules-off five-action@<side>`). Everything else stays ON for both sides. The VP margin of the five-action side decides.

144 DKTC games (Hero v Hero = static-static, seed 1, scenarios mix), the same pairs and seeds as the earlier head-to-heads,
played twice so side and first-turn effects cancel. 8 parts of 36 games, one per thread. No Haiku.

| Part thread | Folder | Pairs file | Five-action ON for | `--rules-off` file | Batch name |
| --- | --- | --- | --- | --- | --- |
| part 1 | mine-1 | pairs-1.txt | Mine | off-for-opponent.txt | fa-h2h-mine-8a94331-p1 |
| part 2 | mine-2 | pairs-2.txt | Mine | off-for-opponent.txt | fa-h2h-mine-8a94331-p2 |
| part 3 | mine-3 | pairs-3.txt | Mine | off-for-opponent.txt | fa-h2h-mine-8a94331-p3 |
| part 4 | mine-4 | pairs-4.txt | Mine | off-for-opponent.txt | fa-h2h-mine-8a94331-p4 |
| part 5 | opp-1 | pairs-1.txt | Opponent | off-for-mine.txt | fa-h2h-opp-8a94331-p1 |
| part 6 | opp-2 | pairs-2.txt | Opponent | off-for-mine.txt | fa-h2h-opp-8a94331-p2 |
| part 7 | opp-3 | pairs-3.txt | Opponent | off-for-mine.txt | fa-h2h-opp-8a94331-p3 |
| part 8 | opp-4 | pairs-4.txt | Opponent | off-for-mine.txt | fa-h2h-opp-8a94331-p4 |

(Parts 1-4 switch five-action off for Opponent; parts 5-8 switch it off for Mine.)

Build: branch `claude/project-thread-d723p0` at `8a943319` = five-action branch gkwq7b 9320f692 plus two fixes (RUN DOWN only on the
deciding side; five-action ON in simulations - the 6d6fc47b build played it OFF on both sides, so its games are void: delete
your own ~/owwt-sim/fa-h2h-*-6d6fc47-* folders, they must not be resumed or copied). Older gkwq7b heads can crash with "Sequence contains no elements": do not use them.

Do NOT touch other batch folders on the shared folder. Delete nothing there.

## Commands

    cd <repo> && git fetch origin claude/project-thread-d723p0 && git checkout -B fa-h2h 8a943319
    git log --oneline -1   # must start 8a943319
    dotnet --version     # if it is not 10.x: bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"; export DOTNET_ROOT="$HOME/.dotnet"
    D=/mnt/project-files/five-action-h2h-2026-11-17

  Parts 1-4 (folder mine-N, five-action ON for Mine):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-opponent.txt)" --keep-as measurement --batch fa-h2h-mine-8a94331-pN \
      --look-for $D/look-for.md > ~/fa-h2h-mine-N.log 2>&1

  Parts 5-8 (folder opp-N, five-action ON for Opponent):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-mine.txt)" --keep-as measurement --batch fa-h2h-opp-8a94331-pN \
      --look-for $D/look-for.md > ~/fa-h2h-opp-N.log 2>&1

N is the pairs number from the table (part 5 uses pairs-1, part 6 pairs-2, ...). Run it with the Bash tool's run_in_background
(timeout 7200000), and re-run the same command when it stops before 36 games.

**Resumable**: a part that stops (the 2-hour run limit, a container restart, "No space left on device") resumes with exactly the same
command - games with a `done` marker in the batch folder are skipped. Out of disk: delete old ~/owwt-sim/<batch> folders and the test
bin/obj folders first (in your own container only).

**"Another simulation is running in this container"** with nothing running: a leftover MSBuild node still holds the lock.
Run `dotnet build-server shutdown; pkill -f MSBuild.dll` and the same command again.

**Report early**: message the owner thread ("Test five-action against simpler pricing", cmsg_01UAkEmFCZaVyiEY4rv4XRKj59pNesKJwCfHcW8Yqb4iM8)
with your game count after the first ~5 games and about every 45 minutes after. Also append one line to
$D/counts.log: `<UTC time> part N <games done>/36`. Say if any game hit the Movement phase time limit, or crashed (the log or game report says so).
A game that is much slower than ~4 minutes: say so too (five-action prices more moves).

**Check after the first 2-3 games**: the batch's rules-off.txt names FIVE ACTION and its parts (LIKELY CHARGE, FALLS SHORT, ...,
AFTERMATH IN POINTS), each @Opponent (parts 1-4) or @Mine (parts 5-8), and NOT advance worth / idle cost / risk once / one sum.
The five-action side's game logs should show "FIVE ACTION" rows and "; FIVE:" in its JOB RISK rows; the other side shows JOB RISK rows
without "; FIVE:". A game that stops with "is switched off for one side only, but this check does not say for which side" is a check
the port missed: stop and tell the owner thread with the game id and the last log lines.

**Keep it small**: the shared folder is near its limit (10 GB / 50,000 files). Copy only the batch folder and the log, nothing else
(no build output, no databases).

**Shared folder**: copy ONLY when the part is done, then check the copy: `du -sb` of source and copy must match and every game-*.txt must
be non-empty. A refused write looks saved but is not kept - if sizes differ, tell the owner thread at once.

**When done**: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<mine|opp>-N/,
create an empty file $D/<mine|opp>-N/done, and message the owner thread with your game count and any findings the log names.
No add-sim-replays, no commits: the owner does that.
