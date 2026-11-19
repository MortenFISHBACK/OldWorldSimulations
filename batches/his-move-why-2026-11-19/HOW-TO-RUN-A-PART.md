# His move why (2026-11-19) - one part

A LOGGING-ONLY batch. Both sides play the same build. One side has everything on (the overhaul, whose assumptions get explained);
the other side plays "true simpler": `worked-out-chances,five-action,standing-by-numbers` OFF. 72 of try 15's pairs (its pairs-1 and
pairs-2), seed 1, scenarios mix, played both ways = 144 games. 4 parts of 36 games. Other batches use their own folders on this mount:
touch only this one.

| Part thread | Arm + N (the two words after run-part.sh) | Folder here | Pairs file | Side with everything ON |
| --- | --- | --- | --- | --- |
| His move why batch part 1 | `mine 1` | mine-1 | pairs-1.txt | Mine |
| His move why batch part 2 | `mine 2` | mine-2 | pairs-2.txt | Mine |
| His move why batch part 3 | `opp 1` | opp-1 | pairs-1.txt | Opponent |
| His move why batch part 4 | `opp 2` | opp-2 | pairs-2.txt | Opponent |

Build: branch `claude/project-thread-60g6hv` at the sha written as the first word of the `go` file (c1e47a93c...).
run-part.sh checks it out and builds it itself (Release).

## GATE: wait for the file `go`

Start the games only when `/mnt/project-files/his-move-why-2026-11-19/go` exists. If `STOP` exists instead, read it.

## Set-up (now)

    cd ~ && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd WarhammerOldWorldSimulator && git fetch origin claude/project-thread-60g6hv

.NET 10: `ci.dot.net` is blocked, so scripts/cloud-setup.sh fails. Install a fixed version instead:

    /usr/local/share/dotnet/dotnet --list-sdks | grep -q '^10\.' || { curl -sSL https://dot.net/v1/dotnet-install.sh -o /tmp/di.sh && bash /tmp/di.sh --version 10.0.100 --install-dir /usr/local/share/dotnet; }

(If your repo is not at ~/WarhammerOldWorldSimulator or /home/user/WarhammerOldWorldSimulator, put `REPO=<path>` in front of the run line.)

## Run (after `go`) - DETACHED, so it survives your shell

    setsid nohup bash /mnt/project-files/his-move-why-2026-11-19/run-part.sh <arm> <N> >> ~/hmw-part.log 2>&1 < /dev/null &

Use your row's two words (e.g. part 3: `opp 1`). The script checks out the go sha, builds (Release), makes a sparse simulation-data
clone, runs your 36 games 3 at a time, and every 3 minutes writes ONE packed file `<folder>/batch.tgz` here (plus `<folder>/count.txt`).
No loose files on the mount. At the end it appends your count to counts.log and creates `<folder>/done` when all 36 are in, printing
PART DONE (or PART NOT COMPLETE: run the line again).

## KEEP YOUR CONTAINER AWAKE

Right after starting (or restarting) the run, ALSO start this waiter with the Bash tool's `run_in_background` (timeout 7200000):

    D=/mnt/project-files/his-move-why-2026-11-19; F=<your folder, e.g. mine-1>; while [ ! -f $D/$F/done ]; do pgrep -f simulate-local >/dev/null || pgrep -f run-part.sh >/dev/null || { echo DIED; exit 1; }; sleep 60; done; echo DONE

DIED = run the run line again (it resumes; finished games are skipped) and a new waiter; DONE = report; timeout = start the waiter again.
**"Another simulation is running in this container"** with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`, run again.

## Check after the first 2-3 games

`~/owwt-sim/hmw-<arm>-<sha7>-p<N>/data/measurements/<batch>/rules-off.txt` says
`worked-out-chances@opponent,five-action@opponent,standing-by-numbers@opponent` (parts 1-2) or the same with `@mine` (parts 3-4).
In a finished game's .log.jsonl, count `grep -c "HIS MOVE WHY: #"` (should be more than 0; these rows sit on the SIMPLER side's
Movement phase, from turn 2, and explain what the everything-on side assumed) and `grep -c "PROMISE BELOW ZERO"` (may be 0 in one game).
`grep -c "ARMY TABLE"` should show up for the everything-on side only. Put one line with what you saw in your first report. If it is
wrong, stop (`pkill -f simulate-local; pkill -f run-part.sh`) and tell the owner thread with the game id. Tell the owner if a game
takes more than 60 minutes.

## Report

Message the owner thread ("Log why his move differs", cmsg_01UAkEmFCZaVyiEY4rv4XRKjX4e6eVhz5E794caisRfFnm) with your count after the
first ~5 games and about every 45 minutes, and append `<UTC hh:mm> part N <done>/36` to counts.log here. Name any game that crashed or
hit the time limit. When `done` exists: message the owner with the count, and stop. Do not delete your container's ~/owwt-sim folder
until the owner has merged. No add-sim-replays, no commits: the owner does that.

## If this container ran an earlier batch

Old ~/owwt-sim folders are from earlier batches: leave them. If an earlier simulate-local is still running, stop it first
(`pkill -f simulate-local; pkill -f run-part.sh`) and run your line again.
