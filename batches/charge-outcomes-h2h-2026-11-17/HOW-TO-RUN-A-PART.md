# Charge outcomes against simpler pricing, head-to-head (2026-11-17) - one part

Both sides play the same build (simpler pricing + split log + charge outcomes). In every game ONE side has `charge-outcomes` ON
(switches break-outcomes, overrun-on, stand-and-shoot, flees-from-charge), the other has it OFF (= simpler pricing). The split log
(JOB SPLIT, MOVE SPLIT) is written by both sides. 144 DKTC pairs (static-static, seed 1, scenarios mix), the same pairs as the
five-action, joint-charge and honest-chances batches, played both ways = 288 games. 8 parts of 36 games. Three other batches run at
the same time in their own folders: touch only this one.

| Part thread | Arm + N (the two words after run-part.sh) | Folder here | Pairs file | Charge outcomes ON for |
| --- | --- | --- | --- | --- |
| part 1 | `mine 1` | mine-1 | pairs-1.txt | Mine |
| part 2 | `mine 2` | mine-2 | pairs-2.txt | Mine |
| part 3 | `mine 3` | mine-3 | pairs-3.txt | Mine |
| part 4 | `mine 4` | mine-4 | pairs-4.txt | Mine |
| part 5 | `opp 1` | opp-1 | pairs-1.txt | Opponent |
| part 6 | `opp 2` | opp-2 | pairs-2.txt | Opponent |
| part 7 | `opp 3` | opp-3 | pairs-3.txt | Opponent |
| part 8 | `opp 4` | opp-4 | pairs-4.txt | Opponent |

Build: branch `claude/project-thread-pf70ph` at `a57fba0d`. Do NOT use any other head. Touch no other folder here; delete nothing.

## GATE: wait for the file `go`

Set up and build now; start the games only when `/mnt/project-files/charge-outcomes-h2h-2026-11-17/go` exists. If `STOP` exists
instead, read it. Check every few minutes (end your turn between checks, no sleep loops).

## Set-up (now)

    cd ~ && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd WarhammerOldWorldSimulator && git fetch origin claude/project-thread-pf70ph && git checkout -B co a57fba0d
    git log --oneline -1          # must start a57fba0d

.NET 10: `ci.dot.net` is blocked here, so scripts/cloud-setup.sh fails on `--channel`. Install a fixed version instead:

    /usr/local/share/dotnet/dotnet --list-sdks | grep -q '^10\.' || { curl -sSL https://dot.net/v1/dotnet-install.sh -o /tmp/di.sh && bash /tmp/di.sh --version 10.0.100 --install-dir /usr/local/share/dotnet; }
    export DOTNET_ROOT=/usr/local/share/dotnet PATH=/usr/local/share/dotnet:$PATH
    dotnet build OldWorldWarTable.sln -c Release --nologo -v q

(If your repo is not at ~/WarhammerOldWorldSimulator, put `REPO=<path>` in front of the run line below.)

## Run (after `go`) - DETACHED, so it survives your shell

    setsid nohup bash /mnt/project-files/charge-outcomes-h2h-2026-11-17/run-part.sh <arm> <N> > ~/co-part.log 2>&1 < /dev/null &

Use your row's two words (e.g. part 6: `opp 2`). Do not use the Bash tool's foreground or run_in_background for the run itself.
The script makes a sparse simulation-data clone (a full one is 12 GB and fills the disk), runs your 36 games 3 at a time, pushes
each finished game to simulation-data, and copies finished games to `<folder>/` here every 3 minutes (`<folder>/count.txt` = count).
At the end it appends your count to counts.log and creates `<folder>/done` when all 36 are in.

**Resumable**: after a stop, a container restart or "No space left on device", run the SAME line again; finished games are skipped.
Check it is alive with `pgrep -af simulate-local` and `tail ~/co-part.log`.
**"Another simulation is running in this container"** with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`, run again.

## Check after the first 2-3 games

`~/owwt-sim/co-<arm>-a57fba0-p<N>/data/measurements/<batch>/rules-off.txt` names the four switches (BREAK OUTCOMES, OVERRUN ON,
STAND AND SHOOT, FLEES FROM CHARGE) @Opponent (parts 1-4) or @Mine (parts 5-8) and nothing else (the run log's first line says
`Rules off: charge-outcomes@...`). Logs of the ON side show some of those four tags; the OFF side none. If the rules-off is wrong,
stop (`pkill -f simulate-local`) and tell the owner thread with the game id.

## Report

Message the owner thread ("Test charge outcomes against simpler", cmsg_01UAkEmFCZaVyiEY4rv4XRKjLKn9zTqc5BZ6vcytPesHgH) with your
count after the first ~5 games and about every 45 minutes, and append `<UTC hh:mm> part N <done>/36` to counts.log here. Name any game
that crashed or hit the time limit (the log says "FAILED" or the game report says so). When `done` exists: message the owner with
the count, and stop. Do not delete your container's ~/owwt-sim folder until the owner has merged (the full logs are needed). No add-sim-replays, no commits: the owner does that.

## KEEP YOUR CONTAINER AWAKE (added 13:55 UTC)

Your container is stopped soon after your turn ends with nothing running, and the detached run dies with it (all 8 parts died
twice so far). After starting (or restarting) the run, ALSO start a waiter with the Bash tool's `run_in_background` (timeout 7200000):

    D=/mnt/project-files/charge-outcomes-h2h-2026-11-17; F=<your folder, e.g. mine-1>; while [ ! -f $D/$F/done ]; do pgrep -f simulate-local >/dev/null || { echo DIED; exit 1; }; sleep 60; done; echo DONE

When it ends: DIED = restart the run line and the waiter; DONE = report; timeout = start the waiter again.

## SWITCH TO run-part2.sh (14:30 UTC) - the shared folder is near its file limit

The mount now gets ONE packed file per part (`<folder>/batch.tgz`, rewritten every 3 minutes), not loose game files. Do this once:

    pkill -f run-part.sh          # stops the old copier only; the games keep playing

then start, with the Bash tool's `run_in_background` (timeout 7200000):

    bash /mnt/project-files/charge-outcomes-h2h-2026-11-17/run-part2.sh <arm> <N> >> ~/co-part.log 2>&1

If games are still playing it only packs until they end; otherwise it (re)starts them (resumable). From now on use this line for
every restart, never run-part.sh. Keep your waiter. Do not delete anything on the mount: the owner removes the old loose files
after checking your batch.tgz. When it ends it prints PART DONE (and creates `done`) or PART NOT COMPLETE (run the line again).
