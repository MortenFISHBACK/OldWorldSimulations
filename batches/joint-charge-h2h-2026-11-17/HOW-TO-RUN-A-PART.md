# Joint charge pricing against simpler pricing, head-to-head (2026-11-17) - one part

Both sides play the same build (simpler pricing + joint charge pricing). In every game ONE side has `second-charger-adds` ON,
the other has it OFF (= simpler pricing). `friend-in-reach` (log only) stays ON for both. 144 DKTC pairs (static-static, seed 1,
scenarios mix), the same pairs as the five-action batches, played both ways = 288 games. 8 parts of 36 games.

| Part thread | Arm + N (the two words after run-part.sh) | Folder here | Pairs file | Adds ON for |
| --- | --- | --- | --- | --- |
| part 1 | `mine 1` | mine-1 | pairs-1.txt | Mine |
| part 2 | `mine 2` | mine-2 | pairs-2.txt | Mine |
| part 3 | `mine 3` | mine-3 | pairs-3.txt | Mine |
| part 4 | `mine 4` | mine-4 | pairs-4.txt | Mine |
| part 5 | `opp 1` | opp-1 | pairs-1.txt | Opponent |
| part 6 | `opp 2` | opp-2 | pairs-2.txt | Opponent |
| part 7 | `opp 3` | opp-3 | pairs-3.txt | Opponent |
| part 8 | `opp 4` | opp-4 | pairs-4.txt | Opponent |

Build: branch `claude/project-thread-eyy865` at `1e5408d1`. Do NOT use any other head. Touch no other folder here; delete nothing.

## GATE: wait for the file `go`

Set up and build now; start the games only when `/mnt/project-files/joint-charge-h2h-2026-11-17/go` exists. If `STOP` exists
instead, read it. Check every few minutes (end your turn between checks, no sleep loops).

## Set-up (now)

    cd ~ && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd WarhammerOldWorldSimulator && git fetch origin claude/project-thread-eyy865 && git checkout -B jc 1e5408d1
    git log --oneline -1          # must start 1e5408d1

.NET 10: `ci.dot.net` is blocked here, so scripts/cloud-setup.sh fails on `--channel`. Install a fixed version instead:

    /usr/local/share/dotnet/dotnet --list-sdks | grep -q '^10\.' || { curl -sSL https://dot.net/v1/dotnet-install.sh -o /tmp/di.sh && bash /tmp/di.sh --version 10.0.100 --install-dir /usr/local/share/dotnet; }
    export DOTNET_ROOT=/usr/local/share/dotnet PATH=/usr/local/share/dotnet:$PATH
    dotnet build OldWorldWarTable.sln -c Release --nologo -v q

(If your repo is not at ~/WarhammerOldWorldSimulator, put `REPO=<path>` in front of the run line below.)

## Run (after `go`) - DETACHED, so it survives your shell

    setsid nohup bash /mnt/project-files/joint-charge-h2h-2026-11-17/run-part.sh <arm> <N> > ~/jc-part.log 2>&1 < /dev/null &

Use your row's two words (e.g. part 6: `opp 2`). Do not use the Bash tool's foreground or run_in_background for the run itself.
The script makes a sparse simulation-data clone (a full one is 12 GB and fills the disk), runs your 36 games 3 at a time, pushes
each finished game to simulation-data, and copies finished games to `<folder>/` here every 3 minutes (`<folder>/count.txt` = count).
At the end it appends your count to counts.log and creates `<folder>/done` when all 36 are in.

**Resumable**: after a stop, a container restart or "No space left on device", run the SAME line again; finished games are skipped.
Check it is alive with `pgrep -af simulate-local` and `tail ~/jc-part.log`.
**"Another simulation is running in this container"** with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`, run again.

## Check after the first 2-3 games

`~/owwt-sim/jc-<arm>-1e5408d-p<N>/data/measurements/<batch>/rules-off.txt` names SECOND CHARGER ADDS @Opponent (parts 1-4) or
@Mine (parts 5-8) and nothing else. Logs of the ON side may show "SECOND CHARGER ADDS" rows; both sides show "FRIEND IN REACH".
If the rules-off file is wrong, stop (`pkill -f simulate-local`) and tell the owner thread with the game id.

## Report

Message the owner thread ("Test joint charge pricing against simpler", cmsg_01UAkEmFCZaVyiEY4rv4XRKjEMRkxj5qUNCd2GNSoxA3nD) with your
count after the first ~5 games and about every 45 minutes, and append `<UTC hh:mm> part N <done>/36` to counts.log here. Name any game
that crashed or hit the time limit (the log says "FAILED" or the game report says so). When `done` exists: message the owner with
the count, and stop. No add-sim-replays, no commits: the owner does that.

## KEEP YOUR TURN OPEN (added 13:21 UTC)

Containers are reset while a thread sits idle, and that kills even a detached run. After starting (or restarting) the run, keep the
turn open with a Bash `run_in_background` wait such as
`until [ -f /mnt/project-files/joint-charge-h2h-2026-11-17/<folder>/done ] || ! pgrep -f simulate-local >/dev/null; do sleep 60; done`
(timeout 7200000), and when it returns, restart if not done. Do not end the turn with no wait running.

## FILE LIMIT: STOP COPYING TO THE SHARED FOLDER (added 14:30 UTC)

The shared folder is near its 50,000-file limit. Games now live on simulation-data only (every game is pushed there). Do this now:

1. Stop the copier and the run-part.sh wrapper (its last step would copy all files again), but NOT the games:
   `for p in $(pgrep -f run-part.sh); do kill $p; done` - simulate-local keeps playing (check with `pgrep -af simulate-local`).
2. Keep your turn open with `until ! pgrep -f simulate-local >/dev/null; do sleep 60; done` (run_in_background, timeout 7200000).
3. When it stops: `bash /mnt/project-files/joint-charge-h2h-2026-11-17/finish-part.sh <arm> <N>`. It checks your games on
   simulation-data and writes count.txt / done. If not complete, restart with run-part.sh, then do step 1 again at once.
Do not copy any game files to the shared folder. The owner removes the copies already there.
