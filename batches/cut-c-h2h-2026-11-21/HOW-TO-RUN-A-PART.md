# How to run a part: cut C head-to-head (2026-11-21)

Owner: the thread "Cut repeated opponent thinking". 48 parts, numbers 1 to 48, three games each (one round: the three play side
by side in your container). 72 pairs of the danger head-to-head of 2026-11-20, scenario mix, seed 1, played both ways: parts 1-24 have
cut C (the three cuts of repeated thinking, switch group cut-c) OFF for Mine (on for Opponent), parts 25-48 the same pairs with it OFF for Opponent. Every other rule is
on for both sides. Build: the commit in `build.txt` on branch claude/project-thread-rjmkp1. Your part's three pairs and the side that has
it off are the line of `parts.txt` that starts with your number. Touch only your own `part-<N>` folder. No commits, no add-sim-replays:
the owner does that.

## GATE: wait for the file `go`

Do the set-up now; start the games only when `/mnt/project-files/cut-c-h2h-2026-11-21/go` exists. If `STOP` exists
instead, read it. A Bash `run_in_background` waiter (timeout 7200000) is fine:

    while [ ! -f /mnt/project-files/cut-c-h2h-2026-11-21/go ]; do [ -f /mnt/project-files/cut-c-h2h-2026-11-21/STOP ] && { echo STOP; exit 1; }; sleep 30; done; echo GO

## Set-up (now)

    cd /home/user && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd /home/user/WarhammerOldWorldSimulator && git fetch -q origin claude/project-thread-rjmkp1

## Run (after `go`) - DETACHED, so it survives your shell

    setsid nohup bash /mnt/project-files/cut-c-h2h-2026-11-21/run-part.sh <N> >> ~/ccut-part.log 2>&1 < /dev/null &

`<N>` is your part number only (e.g. part 7: `run-part.sh 7`). The script installs .NET 10 if needed, checks out the build, builds, makes a
sparse simulation-data clone, plays your 3 games side by side, and every 3 minutes writes ONE packed file `part-<N>/batch.tgz` here (plus
`part-<N>/count.txt`). At the end it appends a line to counts.log and creates `part-<N>/done` when all 3 games (logs and records) are in,
printing PART DONE (or PART NOT COMPLETE: run the line again). On a set-up fault it writes `part-<N>/error.txt`: say so and stop, fix nothing.

## KEEP YOUR CONTAINER AWAKE

Right after starting (or restarting) the run, ALSO start this waiter with the Bash tool's `run_in_background` (timeout 7200000):

    P=/mnt/project-files/cut-c-h2h-2026-11-21/part-<N>; while [ ! -f $P/done ]; do [ -f $P/error.txt ] && { cat $P/error.txt; exit 2; }; pgrep -f simulate-local >/dev/null || pgrep -f run-part.sh >/dev/null || { echo DIED; exit 1; }; sleep 60; done; echo DONE

When it ends: DIED = run the run line again (it resumes; finished games are skipped) and a new waiter; DONE = report; timeout = start
the waiter again. "Another simulation is running in this container" with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`,
run again. Check it is alive with `pgrep -af simulate-local` and `tail ~/ccut-part.log`.

## Check after the first game

`~/owwt-sim/ccut-<build>-p<N>/data/measurements/ccut-<build>-p<N>/rules-off.txt` (or the `out` folder's) must name exactly
the three tags END REPLAY OUT OF THE WAIT, NO SECOND RUN and NO OLD ONE-MOVE GUESS, each for the side your parts.txt line says (`@Mine`
for parts 1-24, `@Opponent` for 25-48), and nothing else.
Put one line with what you saw in your thread.

## Report

The owner cannot read your thread and goes by the `done` files. When `part-<N>/done` exists: reply in your thread with the last line of
`~/ccut-part.log` and the count, then stop. Do not delete ~/owwt-sim. A game that crashed or hit the time limit: name it in your reply.

