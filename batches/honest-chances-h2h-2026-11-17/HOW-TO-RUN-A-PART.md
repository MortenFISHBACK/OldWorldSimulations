# Honest next-turn chances against simpler pricing, head-to-head (2026-11-17) - one part

Both sides play the same build (simpler pricing + split log + honest chances). In every game ONE side has `honest-chances` ON
(switches measured-next-charge and run-down), the other has it OFF (= simpler pricing). The split log (JOB SPLIT, MOVE SPLIT) is
written by both sides. 144 DKTC pairs (static-static, seed 1, scenarios mix), the same pairs as the five-action and joint-charge
batches, played both ways = 288 games. 8 parts of 36 games. Two other batches run at the same time in their own folders: touch only this one.

| Part thread | Arm + N (the two words after run-part.sh) | Folder here | Pairs file | Honest ON for |
| --- | --- | --- | --- | --- |
| part 1 | `mine 1` | mine-1 | pairs-1.txt | Mine |
| part 2 | `mine 2` | mine-2 | pairs-2.txt | Mine |
| part 3 | `mine 3` | mine-3 | pairs-3.txt | Mine |
| part 4 | `mine 4` | mine-4 | pairs-4.txt | Mine |
| part 5 | `opp 1` | opp-1 | pairs-1.txt | Opponent |
| part 6 | `opp 2` | opp-2 | pairs-2.txt | Opponent |
| part 7 | `opp 3` | opp-3 | pairs-3.txt | Opponent |
| part 8 | `opp 4` | opp-4 | pairs-4.txt | Opponent |

Build: branch `claude/project-thread-3d2v3f` at `31c41bfb`. Do NOT use any other head. Touch no other folder here; delete nothing.

## GATE: wait for the file `go`

Set up and build now; start the games only when `/mnt/project-files/honest-chances-h2h-2026-11-17/go` exists. If `STOP` exists
instead, read it. Check every few minutes (end your turn between checks, no sleep loops).

## Set-up (now)

    cd ~ && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd WarhammerOldWorldSimulator && git fetch origin claude/project-thread-3d2v3f && git checkout -B hc 31c41bfb
    git log --oneline -1          # must start 31c41bfb

.NET 10: `ci.dot.net` is blocked here, so scripts/cloud-setup.sh fails on `--channel`. Install a fixed version instead:

    /usr/local/share/dotnet/dotnet --list-sdks | grep -q '^10\.' || { curl -sSL https://dot.net/v1/dotnet-install.sh -o /tmp/di.sh && bash /tmp/di.sh --version 10.0.100 --install-dir /usr/local/share/dotnet; }
    export DOTNET_ROOT=/usr/local/share/dotnet PATH=/usr/local/share/dotnet:$PATH
    dotnet build OldWorldWarTable.sln -c Release --nologo -v q

(If your repo is not at ~/WarhammerOldWorldSimulator, put `REPO=<path>` in front of the run line below.)

## Run (after `go`) - DETACHED, so it survives your shell

    setsid nohup bash /mnt/project-files/honest-chances-h2h-2026-11-17/run-part.sh <arm> <N> > ~/hc-part.log 2>&1 < /dev/null &

Use your row's two words (e.g. part 6: `opp 2`). Do not use the Bash tool's foreground or run_in_background for the run itself.
The script makes a sparse simulation-data clone (a full one is 12 GB and fills the disk), runs your 36 games 3 at a time, pushes
each finished game to simulation-data, and copies finished games to `<folder>/` here every 3 minutes (`<folder>/count.txt` = count).
At the end it appends your count to counts.log and creates `<folder>/done` when all 36 are in.

**Resumable**: after a stop, a container restart or "No space left on device", run the SAME line again; finished games are skipped.
Check it is alive with `pgrep -af simulate-local` and `tail ~/hc-part.log`.
**"Another simulation is running in this container"** with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`, run again.

## Check after the first 2-3 games

`~/owwt-sim/hc-<arm>-31c41bf-p<N>/data/measurements/<batch>/rules-off.txt` names HONEST CHANCES @Opponent (parts 1-4) or
@Mine (parts 5-8) and nothing else (the run log's first line says `Rules off: honest-chances@...`). Logs of the ON side show
"MEASURED NEXT CHARGE" and "RUN DOWN" rows; both sides show "JOB SPLIT". If the rules-off is wrong, stop (`pkill -f simulate-local`)
and tell the owner thread with the game id.

## Report

Message the owner thread ("Test honest chances against simpler", cmsg_01UAkEmFCZaVyiEY4rv4XRKjWckgd5hoVJrX9pGivho1kG) with your
count after the first ~5 games and about every 45 minutes, and append `<UTC hh:mm> part N <done>/36` to counts.log here. Name any game
that crashed or hit the time limit (the log says "FAILED" or the game report says so). When `done` exists: message the owner with
the count, and stop. Do not delete your container's ~/owwt-sim folder until the owner has merged (the full logs are needed). No add-sim-replays, no commits: the owner does that.

## Keep the container alive (added 13:25 UTC)

Containers restart while the session sits idle and the run dies with them. After starting the detached run, ALSO start this watcher
with the Bash tool's run_in_background (timeout 7200000), so your session stays busy and you are woken when the run stops:

    until [ -f /mnt/project-files/honest-chances-h2h-2026-11-17/<folder>/done ] || ! pgrep -f simulate-local >/dev/null; do sleep 30; done; tail -3 ~/hc-part.log

When it wakes you: if `done` is missing, run the detached line again and start the watcher again.

## 14:22 UTC: the shared folder refuses new folders

`mkdir` on the mount gives "Input/output error" (files still copy). That is fine: every game is pushed to simulation-data and the
owner merges from there. If your copy fails this way, just let the run finish; report the count from ~/hc-part.log ("saved to
simulation-data" lines) and that the run ended. Do not delete anything.

## 14:30 UTC: part folders on the mount removed

All copied games were checked identical in simulation-data and the part folders were removed to save files (project file limit).
Copy errors to the mount from now on are expected and harmless. Let your run finish, check `~/hc-part.log` says 36 saved to
simulation-data, then message the owner with that count. Do not recreate folders here.
