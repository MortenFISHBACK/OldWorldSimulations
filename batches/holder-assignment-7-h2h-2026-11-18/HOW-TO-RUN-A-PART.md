# Army-wide objective holders, BATCH 7 (real ground, his one quarter), ON against OFF (2026-11-18) - one part

Both sides play the same build (the overhaul's new pricing, worked-out chances, on both sides). The ONLY difference: one side has
`holder-assignment`, `quarter-odds` AND `walk-promise` OFF. 144 DKTC pairs (same as batches 1-6), seed 1, scenarios mix, played both
ways = 288 games. 8 parts of 36 games. Other batches use their own folders on this mount: touch only this one.

| Part thread | Arm + N (the two words after run-part.sh) | Folder here | Pairs file | Side with holders ON |
| --- | --- | --- | --- | --- |
| Holder 7 batch part 1 | `mine 1` | mine-1 | pairs-1.txt | Mine |
| Holder 7 batch part 2 | `mine 2` | mine-2 | pairs-2.txt | Mine |
| Holder 7 batch part 3 | `mine 3` | mine-3 | pairs-3.txt | Mine |
| Holder 7 batch part 4 | `mine 4` | mine-4 | pairs-4.txt | Mine |
| Holder 7 batch part 5 | `opp 1` | opp-1 | pairs-1.txt | Opponent |
| Holder 7 batch part 6 | `opp 2` | opp-2 | pairs-2.txt | Opponent |
| Holder 7 batch part 7 | `opp 3` | opp-3 | pairs-3.txt | Opponent |
| Holder 7 batch part 8 | `opp 4` | opp-4 | pairs-4.txt | Opponent |

Build: branch `claude/project-thread-bj3s5r` at the sha written as the first word of the `go` file (dcce2247...).
run-part.sh checks it out and builds it itself (Release). NEW folder: never touch older holder-assignment-*-h2h folders.

## GATE: wait for the file `go`

Do the set-up now; start the games only when `/mnt/project-files/holder-assignment-7-h2h-2026-11-18/go` exists. If `STOP` exists
instead, read it.

## Set-up (now)

    cd ~ && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd WarhammerOldWorldSimulator && git fetch origin claude/project-thread-bj3s5r

.NET 10: `ci.dot.net` is blocked, so scripts/cloud-setup.sh fails. Install a fixed version instead:

    /usr/local/share/dotnet/dotnet --list-sdks | grep -q '^10\.' || { curl -sSL https://dot.net/v1/dotnet-install.sh -o /tmp/di.sh && bash /tmp/di.sh --version 10.0.100 --install-dir /usr/local/share/dotnet; }

(If your repo is not at ~/WarhammerOldWorldSimulator or /home/user/WarhammerOldWorldSimulator, put `REPO=<path>` in front of the run line.)

## Run (after `go`) - DETACHED, so it survives your shell

    setsid nohup bash /mnt/project-files/holder-assignment-7-h2h-2026-11-18/run-part.sh <arm> <N> >> ~/h7-part.log 2>&1 < /dev/null &

Use your row's two words (e.g. part 6: `opp 2`). The script checks out the go sha, builds (Release), makes a sparse simulation-data
clone, runs your 36 games 3 at a time, and every 3 minutes writes ONE packed file `<folder>/batch.tgz` here (plus `<folder>/count.txt`).
No loose files on the mount. At the end it appends your count to counts.log and creates `<folder>/done` when all 36 are in, printing
PART DONE (or PART NOT COMPLETE: run the line again).

## KEEP YOUR CONTAINER AWAKE

Your container is stopped soon after your turn ends with nothing running, and the detached run dies with it. Right after starting
(or restarting) the run, ALSO start this waiter with the Bash tool's `run_in_background` (timeout 7200000):

    D=/mnt/project-files/holder-assignment-7-h2h-2026-11-18; F=<your folder, e.g. mine-1>; while [ ! -f $D/$F/done ]; do pgrep -f simulate-local >/dev/null || pgrep -f run-part.sh >/dev/null || { echo DIED; exit 1; }; sleep 60; done; echo DONE

When it ends: DIED = run the run line again (it resumes; finished games are skipped) and a new waiter; DONE = report; timeout = start the waiter again.
**"Another simulation is running in this container"** with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`, run again.
Check it is alive with `pgrep -af simulate-local` and `tail ~/h7-part.log`.

## Check after the first 2-3 games

`~/owwt-sim/h7-<arm>-dcce224-p<N>/data/measurements/<batch>/rules-off.txt` says `holder-assignment@Opponent`, `quarter-odds@Opponent` and
`walk-promise@Opponent` (parts 1-4) or the same with `@Mine` (parts 5-8). Also check a game log (`grep -c "HOLDER ASSIGNMENT"` per side
in the game's .txt or .log.jsonl): HOLDER ASSIGNMENT and HOLD ODDS rows appear for Mine only in parts 1-4, for Opponent only in parts 5-8
(WALK PROMISE, REAL GROUND claims and, in Domination from round 5, QUARTER ODDS likewise on the ON side only; the off side may show HOLDER AT DEPLOYMENT or
CHEAPEST HOLDER instead). Put one line with what you saw in your first report. If it is wrong, stop
(`pkill -f simulate-local; pkill -f run-part.sh`) and tell the owner thread with the game id. Also tell the owner if a game takes more
than 25 minutes.

## Report

Message the owner thread ("Test holders on real ground against off", cmsg_01UAkEmFCZaVyiEY4rv4XRKjDFzm6LPeFUADXbdKL9J8yf) with your
count after the first ~5 games and about every 45 minutes, and append `<UTC hh:mm> part N <done>/36` to counts.log here. Name any
game that crashed or hit the time limit. When `done` exists: message the owner with the count, and stop. Do not delete your
container's ~/owwt-sim folder until the owner has merged. No add-sim-replays, no commits: the owner does that.

## If this container ran an earlier holder batch

Old folders ~/owwt-sim/ha-*, h2-* ... h6-* are from earlier batches: leave them. If an older simulate-local is still running, the run
script only packs until it ends: stop it first (`pkill -f simulate-local; pkill -f run-part.sh`) and run your line again.
