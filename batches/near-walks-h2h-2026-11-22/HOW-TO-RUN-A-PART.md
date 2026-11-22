# How to run a part: Walk 2 head-to-head, 144 games (2026-11-22)

Owner: the thread "Cut repeated opponent thinking". 48 parts, numbers 1 to 48; each part plays ONE round of 3 games side by side
(`parts.txt`: part, three pairs, the switch that is off). Parts 1-24 have Walk 2 off for "mine", parts 25-48 the same pairs with it
off for "opponent". Build: the commit in `build.txt` on branch claude/project-thread-rjmkp1 (not main). Touch only your own
`part-<N>` folder. No commits, no add-sim-replays: the owner does that.

## GATE: wait for the file `go`

Do the set-up now; start the games only when `/mnt/project-files/near-walks-h2h-2026-11-22/go` exists. If `STOP` exists instead,
read it. Wait with the Bash tool's `run_in_background` (timeout 7200000):

    while [ ! -f /mnt/project-files/near-walks-h2h-2026-11-22/go ]; do [ -f /mnt/project-files/near-walks-h2h-2026-11-22/STOP ] && { echo STOP; exit 1; }; sleep 30; done; echo GO

## Set-up (now)

If a git or download step fails with a proxy error (403/407, connection reset), wait a minute and try again; the run script retries
its own network steps 5 times. If it still fails, the container's proxy is stale: say so in your thread and stop.

    cd /home/user && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd /home/user/WarhammerOldWorldSimulator && git fetch -q origin claude/project-thread-rjmkp1

The run script discards every changed tracked file in your clone before its checkout, so a changed `scripts/__pycache__` file
cannot block it. If an older run's games are still playing (`pgrep -af "[s]imulate-local.sh --opponent"` shows one), wait until
it ends.

## Run (after `go`) - in the FOREGROUND of a background Bash call

Start it with the Bash tool's `run_in_background` and timeout 7200000. Do NOT use setsid, nohup or `&`: a detached run or a separate
waiter dies with the shell in these containers, the background Bash call keeps the container awake until the run ends.

    bash /mnt/project-files/near-walks-h2h-2026-11-22/run-part.sh <N> >> ~/nw-part.log 2>&1; tail -3 ~/nw-part.log

`<N>` is your part number only (part 7: `run-part.sh 7`). The script installs .NET 10 if needed, checks out the build, builds, makes
a sparse simulation-data clone, plays the 3 games side by side and every 3 minutes writes ONE packed file `part-<N>/batch.tgz` here
(plus `part-<N>/count.txt`). A round takes about 15-20 minutes.

When the call ends, read the last lines:
- `PART DONE`: report (below). A game that was saved but did not end (time limit, crash) still counts as saved: do not re-run it.
- `PART NOT COMPLETE`: run the same line again once (it resumes; saved games are skipped).
- `no go file yet`: wait for `go`. On a set-up fault the script writes `part-<N>/error.txt`: say so and stop, fix nothing.
- "Another simulation is running in this container" with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`,
  run again.

## Check after the first game

`~/owwt-sim/nw22-<build>-p<N>/data/measurements/nw22-<build>-p<N>/rules-off.txt` (or the `out` folder's) says the one switch of your
line in `parts.txt` (near-walks-only@mine or @opponent). Put one line with what you saw in your thread.

## Report

The owner goes by the `done` files. When `part-<N>/done` exists: reply in your thread with the last line of `~/nw-part.log`, then
stop. Do not delete ~/owwt-sim. A game that crashed or hit the time limit: name it in your reply.
