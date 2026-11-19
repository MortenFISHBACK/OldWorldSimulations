# Baseline on the new main, every rule on (2026-11-19) - one part

Both sides play main's computer opponent (static-static) with EVERY rule on (no `--rules-off`). This is the new baseline that later
builds are measured against. 288 DKTC pairs (8 files of 36), seeds 1 and 2, scenarios mix = 576 games, 16 parts of 36. Other batches
use their own folders on this mount: touch only this one.

| Part thread | The two words after run-part.sh | Folder here | Pairs file | Seed |
| --- | --- | --- | --- | --- |
| Baseline part 1 | `1 1` | s1-1 | pairs-1.txt | 1 |
| Baseline part 2 | `1 2` | s1-2 | pairs-2.txt | 1 |
| Baseline part 3 | `1 3` | s1-3 | pairs-3.txt | 1 |
| Baseline part 4 | `1 4` | s1-4 | pairs-4.txt | 1 |
| Baseline part 5 | `1 5` | s1-5 | pairs-5.txt | 1 |
| Baseline part 6 | `1 6` | s1-6 | pairs-6.txt | 1 |
| Baseline part 7 | `1 7` | s1-7 | pairs-7.txt | 1 |
| Baseline part 8 | `1 8` | s1-8 | pairs-8.txt | 1 |
| Baseline part 9 | `2 1` | s2-1 | pairs-1.txt | 2 |
| Baseline part 10 | `2 2` | s2-2 | pairs-2.txt | 2 |
| Baseline part 11 | `2 3` | s2-3 | pairs-3.txt | 2 |
| Baseline part 12 | `2 4` | s2-4 | pairs-4.txt | 2 |
| Baseline part 13 | `2 5` | s2-5 | pairs-5.txt | 2 |
| Baseline part 14 | `2 6` | s2-6 | pairs-6.txt | 2 |
| Baseline part 15 | `2 7` | s2-7 | pairs-7.txt | 2 |
| Baseline part 16 | `2 8` | s2-8 | pairs-8.txt | 2 |

Build: `main` at the sha written as the first word of the `go` file. run-part.sh checks it out and builds it itself (Release).

## GATE: wait for the file `go`

Do the set-up now; start the games only when `/mnt/project-files/baseline-576-2026-11-19/go` exists. If `STOP` exists instead, read it.
Check every few minutes (end your turn between checks, no sleep loops).

## Set-up (now)

    cd ~ && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd WarhammerOldWorldSimulator && git fetch origin main

.NET 10: `ci.dot.net` is blocked, so scripts/cloud-setup.sh fails. Install a fixed version instead:

    /usr/local/share/dotnet/dotnet --list-sdks | grep -q '^10\.' || { curl -sSL https://dot.net/v1/dotnet-install.sh -o /tmp/di.sh && bash /tmp/di.sh --version 10.0.100 --install-dir /usr/local/share/dotnet; }

(If your repo is not at ~/WarhammerOldWorldSimulator or /home/user/WarhammerOldWorldSimulator, put `REPO=<path>` in front of the run line.)

## Run (after `go`) - DETACHED, so it survives your shell

    setsid nohup bash /mnt/project-files/baseline-576-2026-11-19/run-part.sh <seed> <N> >> ~/base-part.log 2>&1 < /dev/null &

Use your row's two words (e.g. part 11: `2 3`). The script checks out the go sha, builds (Release), makes a sparse simulation-data clone,
runs your 36 games 3 at a time, and every 3 minutes writes ONE packed file `<folder>/batch.tgz` here (plus `<folder>/count.txt`).
No loose files on the mount. At the end it appends your count to counts.log and creates `<folder>/done` when all 36 are in, printing
PART DONE (or PART NOT COMPLETE: run the line again).

## KEEP YOUR CONTAINER AWAKE

Your container is stopped soon after your turn ends with nothing running, and the detached run dies with it. Right after starting
(or restarting) the run, ALSO start this waiter with the Bash tool's `run_in_background` (timeout 7200000):

    D=/mnt/project-files/baseline-576-2026-11-19; F=<your folder, e.g. s1-1>; while [ ! -f $D/$F/done ]; do pgrep -f simulate-local >/dev/null || pgrep -f run-part.sh >/dev/null || { echo DIED; exit 1; }; sleep 60; done; echo DONE

When it ends: DIED = run the run line again (it resumes; finished games are skipped) and a new waiter; DONE = report; timeout = start the waiter again.
**"Another simulation is running in this container"** with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`, run again.
Check it is alive with `pgrep -af simulate-local` and `tail ~/base-part.log`.

## Check after the first 2-3 games

`~/owwt-sim/base-s<seed>-<sha7>-p<N>/data/measurements/<batch>/rules-off.txt` is empty or absent (every rule on). In a game log
(`.txt` or `.log.jsonl`), the new parts show on BOTH sides: HOLDER ASSIGNMENT rows for Mine and Opponent, and five-option
CANDIDATES JOB rows for both. Put one line with what you saw in your first report. If it is wrong, stop
(`pkill -f simulate-local; pkill -f run-part.sh`) and tell the owner thread with the game id. Also tell the owner if a game takes more
than 30 minutes.

## Report

Message the owner thread (the landing thread, cmsg_01UAkEmFCZaVyiEY4rv4XRKjRtH2w1opggwHcjf3WRBDVk) with your count after the first ~5 games and about
every 45 minutes, and append `<UTC hh:mm> part N <done>/36` to counts.log here. Name any game that crashed or hit the time limit.
When `done` exists: message the owner with the count, and stop. Do not delete your container's ~/owwt-sim folder until the owner has
merged. No add-sim-replays, no commits: the owner does that.
