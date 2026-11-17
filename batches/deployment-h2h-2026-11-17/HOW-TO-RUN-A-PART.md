# Deployment by the figures against main, head-to-head (2026-11-17) - one part

Both sides play main's computer opponent (static-static). In every game ONE side also has the new deployment ON (switches
holder-at-deployment, lane-by-figures, deploy-by-figures; group `deployment`), the other has it OFF. 288 DKTC pairs (the usual 144 +
the 144 midway between them), seed 1, scenarios mix, each played both ways = 576 games, 16 parts of 36. Other batches run at the
same time in their own folders: touch only this folder, and only the files named below.

| Part thread | The two words after run-part.sh | Pairs file | New deployment ON for |
| --- | --- | --- | --- |
| part 1 | `mine 1` | pairs-1.txt | Mine |
| part 2 | `mine 2` | pairs-2.txt | Mine |
| part 3 | `mine 3` | pairs-3.txt | Mine |
| part 4 | `mine 4` | pairs-4.txt | Mine |
| part 5 | `mine 5` | pairs-5.txt | Mine |
| part 6 | `mine 6` | pairs-6.txt | Mine |
| part 7 | `mine 7` | pairs-7.txt | Mine |
| part 8 | `mine 8` | pairs-8.txt | Mine |
| part 9 | `opp 1` | pairs-1.txt | Opponent |
| part 10 | `opp 2` | pairs-2.txt | Opponent |
| part 11 | `opp 3` | pairs-3.txt | Opponent |
| part 12 | `opp 4` | pairs-4.txt | Opponent |
| part 13 | `opp 5` | pairs-5.txt | Opponent |
| part 14 | `opp 6` | pairs-6.txt | Opponent |
| part 15 | `opp 7` | pairs-7.txt | Opponent |
| part 16 | `opp 8` | pairs-8.txt | Opponent |

Build: branch `claude/project-thread-1vnftw` at `13df7bd5`. Do NOT use any other head (the script refuses).

## THE SHARED FOLDER IS NEARLY FULL (file limit): NO GAMES ON IT

Games are NOT copied here. `scripts/simulate-local.sh` pushes every finished game to the `simulation-data` branch
(measurements/dep-<arm>-13df7bd-p<N>/); that branch is the source of truth. Here you write only `status-<arm>-<N>.txt`,
one line in `counts.log`, and `done-<arm>-<N>` (the script does all three). Create no other files or folders here; delete nothing.

## GATE: wait for the file `go`

Set up and build now; start the games only when `/mnt/project-files/deployment-h2h-2026-11-17/go` exists. If `STOP` exists
instead, read it. Check every few minutes (end your turn between checks, no sleep loops).

## Set-up (now)

    cd ~ && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd WarhammerOldWorldSimulator && git fetch origin claude/project-thread-1vnftw && git checkout -B dep 13df7bd5
    git log --oneline -1          # must start 13df7bd5

.NET 10 (`ci.dot.net` is blocked, so scripts/cloud-setup.sh fails; install a fixed version):

    /usr/local/share/dotnet/dotnet --list-sdks | grep -q '^10\.' || { curl -sSL https://dot.net/v1/dotnet-install.sh -o /tmp/di.sh && bash /tmp/di.sh --version 10.0.100 --install-dir /usr/local/share/dotnet; }
    export DOTNET_ROOT=/usr/local/share/dotnet PATH=/usr/local/share/dotnet:$PATH
    dotnet build OldWorldWarTable.sln -c Release --nologo -v q

(If your repo is not at ~/WarhammerOldWorldSimulator, put `REPO=<path>` in front of the run line.)

## Run (after `go`)

Start it with the Bash tool's `run_in_background` and timeout 7200000 (NOT in the foreground, NOT setsid/nohup: today detached
runs died when the container idled between turns; a run_in_background task keeps the container awake and wakes you when it ends):

    bash /mnt/project-files/deployment-h2h-2026-11-17/run-part.sh <arm> <N> >> ~/dep-part.log 2>&1

It runs your 36 games 3 at a time (a sparse simulation-data clone in ~/owwt-sim; a full clone is 12 GB). When it ends it prints
PART DONE (and creates `done-<arm>-<N>` here) or PART NOT COMPLETE: then run the SAME line again (resumable: games already on
simulation-data are skipped). Same after a container restart, a 2-hour timeout or "No space left on device".
Alive? `pgrep -af simulate-local` and `tail ~/dep-part.log`.
"Another simulation is running in this container" with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`, run again.

## Check after the first 2-3 games

`~/owwt-sim/dep-<arm>-13df7bd-p<N>/data/measurements/<batch>/rules-off.txt` names the three switches (HOLDER AT DEPLOYMENT,
LANE BY FIGURES, DEPLOY BY FIGURES) @Opponent (parts 1-8) or @Mine (parts 9-16) and nothing else (the run log's first line says
`Rules off: deployment@...`). Every "saved to simulation-data" line in ~/dep-part.log is a game safely pushed; a line
"WARNING: kept in this container only" means a push failed: tell the owner. If rules-off is wrong, stop (`pkill -f simulate-local`)
and tell the owner thread with the game id.

## Report

Message the owner thread ("Test deployment improvements against main", cmsg_01UAkEmFCZaVyiEY4rv4XRKjQuyMrWByFtPDn9YQRi8oLp) with your
count after the first ~5 games and about every 45 minutes (your status file has it). Name any game that crashed or hit the time limit
(the log says "FAILED"). When `done-<arm>-<N>` exists: message the owner with the count, and stop. Keep your container's ~/owwt-sim
until the owner has merged. No add-sim-replays, no commits: the owner does that.
