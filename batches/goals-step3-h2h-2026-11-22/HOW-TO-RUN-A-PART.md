# How to run a part: goals-first step 3 head-to-head (2026-11-22)

Owner: the thread "Build goals-first planning for units". 96 parts, numbers 1 to 96, three games each (one round: the three play side
by side in your container). The 144 pairs of the danger head-to-head of 2026-11-20, scenario mix, seed 1, played both ways: parts 1-48
have the four step 3 switches (goal-on-time, nearest-to-goal, goal-route, foot-first) OFF for Mine (on for Opponent), parts 49-96 the same
pairs with them OFF for Opponent. Every other rule (the speed cuts included) is on for both sides. Build: the commit in `build.txt` on
branch claude/project-thread-hp0jtb. Your part's three pairs and the side that has them off are the line of `parts.txt` that starts with
your number. Touch only your own `part-<N>` folder. No commits, no add-sim-replays: the owner does that.

If your container ran another batch before: that is fine. The run script checks out this build itself (detached) and plays in its own
folder `~/owwt-sim/gs3-<build>-p<N>`; do not reuse another batch's folder, and do not delete it. Make sure nothing else is running first
(`pgrep -af simulate-local` empty).

## GATE: wait for the file `go`

Do the set-up now; start the games only when `/mnt/project-files/goals-step3-h2h-2026-11-22/go` exists. If `STOP` exists
instead, read it. A Bash `run_in_background` waiter (timeout 7200000) is fine:

    while [ ! -f /mnt/project-files/goals-step3-h2h-2026-11-22/go ]; do [ -f /mnt/project-files/goals-step3-h2h-2026-11-22/STOP ] && { echo STOP; exit 1; }; sleep 30; done; echo GO

## Set-up (now)

If a git or download step fails with a proxy error (403/407, connection reset), wait a minute and try again; the run script
retries its own network steps 5 times. If it still fails, the container's proxy is stale: say so in your thread and stop.


    cd /home/user && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd /home/user/WarhammerOldWorldSimulator && git fetch -q origin claude/project-thread-hp0jtb

## Run (after `go`) - DETACHED, so it survives your shell

    setsid nohup bash /mnt/project-files/goals-step3-h2h-2026-11-22/run-part.sh <N> >> ~/gs3-part.log 2>&1 < /dev/null &

`<N>` is your part number only (e.g. part 7: `run-part.sh 7`). The script installs .NET 10 if needed, checks out the build, builds, makes a
sparse simulation-data clone, plays your 3 games side by side, and every 3 minutes writes ONE packed file `part-<N>/batch.tgz` here (plus
`part-<N>/count.txt`). At the end it appends a line to counts.log and creates `part-<N>/done` when all 3 games (logs and records) are in,
printing PART DONE (or PART NOT COMPLETE: run the line again). On a set-up fault it writes `part-<N>/error.txt`: say so and stop, fix nothing.

## KEEP YOUR CONTAINER AWAKE

Right after starting (or restarting) the run, ALSO start this waiter with the Bash tool's `run_in_background` (timeout 7200000):

    P=/mnt/project-files/goals-step3-h2h-2026-11-22/part-<N>; while [ ! -f $P/done ]; do [ -f $P/error.txt ] && { cat $P/error.txt; exit 2; }; pgrep -f simulate-local >/dev/null || pgrep -f run-part.sh >/dev/null || { echo DIED; exit 1; }; sleep 60; done; echo DONE

When it ends: DIED = run the run line again (it resumes; finished games are skipped) and a new waiter; DONE = report; timeout = start
the waiter again. "Another simulation is running in this container" with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`,
run again. Check it is alive with `pgrep -af simulate-local` and `tail ~/gs3-part.log`.

## Check after the first game

`~/owwt-sim/gs3-<build>-p<N>/data/measurements/gs3-<build>-p<N>/rules-off.txt` (or the `out` folder's) must name exactly
the four tags GOAL ON TIME, NEAREST TO GOAL, GOAL ROUTE and FOOT FIRST, for the side your parts.txt line says (`@Mine`
for parts 1-48, `@Opponent` for 49-96), and nothing else.
Put one line with what you saw in your thread.

## Report

The owner cannot read your thread and goes by the `done` files. When `part-<N>/done` exists: reply in your thread with the last line of
`~/gs3-part.log` and the count, then stop. Do not delete ~/owwt-sim. A game that crashed or hit the time limit: name it in your reply.

