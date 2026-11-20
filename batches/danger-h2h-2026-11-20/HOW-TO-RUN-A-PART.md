# Danger-figure head-to-head: the overhaul with all of the danger-figure work v true simpler pricing (2026-11-20) - one part

Both sides play the same build (the sha written as the first word of the `go` file; the build comes in `build.bundle` in this folder).
The OVERHAUL side has every rule on. The SIMPLER side has `worked-out-chances`, `five-action` and `standing-by-numbers` OFF. The same 144
pairs as fight odds 1 and 2, seed 1, scenarios mix, played both ways = 288 games. 16 parts of 18 games. Other batches use their own folders
on this mount: touch only this one.

| Part thread | Arm + N (the two words after run-part.sh) | Folder here | Pairs file | Side with the overhaul |
| --- | --- | --- | --- | --- |
| Danger head-to-head part 1 | `mine 1` | mine-1 | pairs-1.txt | Mine |
| Danger head-to-head part 2 | `mine 2` | mine-2 | pairs-2.txt | Mine |
| Danger head-to-head part 3 | `mine 3` | mine-3 | pairs-3.txt | Mine |
| Danger head-to-head part 4 | `mine 4` | mine-4 | pairs-4.txt | Mine |
| Danger head-to-head part 5 | `mine 5` | mine-5 | pairs-5.txt | Mine |
| Danger head-to-head part 6 | `mine 6` | mine-6 | pairs-6.txt | Mine |
| Danger head-to-head part 7 | `mine 7` | mine-7 | pairs-7.txt | Mine |
| Danger head-to-head part 8 | `mine 8` | mine-8 | pairs-8.txt | Mine |
| Danger head-to-head part 9 | `opp 1` | opp-1 | pairs-1.txt | Opponent |
| Danger head-to-head part 10 | `opp 2` | opp-2 | pairs-2.txt | Opponent |
| Danger head-to-head part 11 | `opp 3` | opp-3 | pairs-3.txt | Opponent |
| Danger head-to-head part 12 | `opp 4` | opp-4 | pairs-4.txt | Opponent |
| Danger head-to-head part 13 | `opp 5` | opp-5 | pairs-5.txt | Opponent |
| Danger head-to-head part 14 | `opp 6` | opp-6 | pairs-6.txt | Opponent |
| Danger head-to-head part 15 | `opp 7` | opp-7 | pairs-7.txt | Opponent |
| Danger head-to-head part 16 | `opp 8` | opp-8 | pairs-8.txt | Opponent |

Build: the sha written as the first word of the `go` file. run-part.sh fetches it from build.bundle, checks it out and builds it (Release).

## GATE: wait for the file `go`

Do the set-up now; start the games only when `/mnt/project-files/danger-h2h-2026-11-20/go` exists. If `STOP` exists
instead, read it. (A Bash `run_in_background` waiter such as
`while [ ! -f /mnt/project-files/danger-h2h-2026-11-20/go ]; do sleep 60; done` with a long timeout is fine.)

## Set-up (now)

    cd ~ && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd WarhammerOldWorldSimulator && git fetch origin main

.NET 10: `ci.dot.net` is blocked, so scripts/cloud-setup.sh fails. Install a fixed version instead:

    /usr/local/share/dotnet/dotnet --list-sdks | grep -q '^10\.' || { curl -sSL https://dot.net/v1/dotnet-install.sh -o /tmp/di.sh && bash /tmp/di.sh --version 10.0.100 --install-dir /usr/local/share/dotnet; }

(If your repo is not at ~/WarhammerOldWorldSimulator or /home/user/WarhammerOldWorldSimulator, put `REPO=<path>` in front of the run line.)

## Run (after `go`) - DETACHED, so it survives your shell

    setsid nohup bash /mnt/project-files/danger-h2h-2026-11-20/run-part.sh <arm> <N> >> ~/dh2-part.log 2>&1 < /dev/null &

Use your row's two words (e.g. part 6: `opp 2`). The script checks out the go sha, builds (Release), makes a sparse simulation-data
clone, runs your 18 games 3 at a time, and every 3 minutes writes ONE packed file `<folder>/batch.tgz` here (plus `<folder>/count.txt`).
No loose files on the mount. At the end it appends your count to counts.log and creates `<folder>/done` when all 18 are in, printing
PART DONE (or PART NOT COMPLETE: run the line again).

## KEEP YOUR CONTAINER AWAKE

Your container is stopped soon after your turn ends with nothing running, and the detached run dies with it. Right after starting
(or restarting) the run, ALSO start this waiter with the Bash tool's `run_in_background` (timeout 7200000):

    D=/mnt/project-files/danger-h2h-2026-11-20; F=<your folder, e.g. mine-1>; while [ ! -f $D/$F/done ]; do pgrep -f simulate-local >/dev/null || pgrep -f run-part.sh >/dev/null || { echo DIED; exit 1; }; sleep 60; done; echo DONE

When it ends: DIED = run the run line again (it resumes; finished games are skipped) and a new waiter; DONE = report; timeout = start the waiter again.
**"Another simulation is running in this container"** with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`, run again.
Check it is alive with `pgrep -af simulate-local` and `tail ~/dh2-part.log`.

## Check after the first 2-3 games

`~/owwt-sim/dh2-<arm>-<sha7>-p<N>/data/measurements/<batch>/rules-off.txt` must name `worked-out-chances`, `five-action` and
`standing-by-numbers` for `@Opponent` only (parts 1-8, arm mine) or `@Mine` only (parts 9-16, arm opp). Also check a game log (.log.jsonl):
rows tagged `THE TABLE BINDS` appear for Mine only in parts 1-8 and for Opponent only in parts 9-16 (e.g. `grep -c "THE TABLE BINDS"` per
side). Put one line with what you saw in your first report. If it is wrong, stop (`pkill -f simulate-local; pkill -f run-part.sh`) and tell
the owner thread with the game id. Tell the owner if a game takes more than 60 minutes.

## Report

Message the owner thread ("Make the danger figure match the dice", cmsg_01UAkEmFCZaVyiEY4rv4XRKjATJpVUuh1LeECtoRoE2yEv) with your
count after the first ~5 games and about every 45 minutes, and append `<UTC hh:mm> part N <done>/18` to counts.log here. Name any
game that crashed or hit the time limit. When `done` exists: message the owner with the count, and stop. Do not delete your
container's ~/owwt-sim folder until the owner has merged. No add-sim-replays, no commits: the owner does that.

## If this container ran an earlier batch

Old ~/owwt-sim folders are from earlier batches: leave them. If an earlier simulate-local is still running, the run script only packs
until it ends: stop it first (`pkill -f simulate-local; pkill -f run-part.sh`) and run your line again.
