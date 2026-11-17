# Standing still by numbers against simpler pricing, head-to-head (2026-11-17) - one part

Both sides play the same build (simpler pricing + split log + standing still by numbers). In every game ONE side has
`standing-by-numbers` ON (falls-short, time-on-our-side, cheapest-holder, nearer-not-needed, no-forced-advance, hard-stay-dropped),
the other has it OFF (= simpler pricing). 144 DKTC pairs (static-static, seed 1, scenarios mix), the same pairs as the five-action and
joint-charge batches, played both ways = 288 games. 8 parts of 36 games. No Haiku.

| Part thread | Arm + N (the two words after run-part.sh) | Folder here | Pairs file | Standing still ON for |
| --- | --- | --- | --- | --- |
| part 1 | `mine 1` | mine-1 | pairs-1.txt | Mine |
| part 2 | `mine 2` | mine-2 | pairs-2.txt | Mine |
| part 3 | `mine 3` | mine-3 | pairs-3.txt | Mine |
| part 4 | `mine 4` | mine-4 | pairs-4.txt | Mine |
| part 5 | `opp 1` | opp-1 | pairs-1.txt | Opponent |
| part 6 | `opp 2` | opp-2 | pairs-2.txt | Opponent |
| part 7 | `opp 3` | opp-3 | pairs-3.txt | Opponent |
| part 8 | `opp 4` | opp-4 | pairs-4.txt | Opponent |

Build: branch `claude/project-thread-3c34nw` at `06f55ceb`. Do NOT use any other head. Touch no other folder here (another batch,
joint-charge-h2h, runs at the same time in its own folder); delete nothing.

## GATE: wait for the file `go`

Set up and build now; start the games only when `/mnt/project-files/standing-still-h2h-2026-11-17/go` exists. If `STOP` exists
instead, read it. Check every few minutes (end your turn between checks, no sleep loops).

## Set-up (now)

    cd ~ && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd WarhammerOldWorldSimulator && git fetch origin claude/project-thread-3c34nw && git checkout -B ss 06f55ceb
    git log --oneline -1          # must start 06f55ceb

.NET 10: `ci.dot.net` is blocked here, so scripts/cloud-setup.sh fails on `--channel`. Install a fixed version instead:

    /usr/local/share/dotnet/dotnet --list-sdks | grep -q '^10\.' || { curl -sSL https://dot.net/v1/dotnet-install.sh -o /tmp/di.sh && bash /tmp/di.sh --version 10.0.100 --install-dir /usr/local/share/dotnet; }
    export DOTNET_ROOT=/usr/local/share/dotnet PATH=/usr/local/share/dotnet:$PATH
    dotnet build OldWorldWarTable.sln -c Release --nologo -v q

(If your repo is not at ~/WarhammerOldWorldSimulator, put `REPO=<path>` in front of the run line below.)

## Run (after `go`) - CHANGED 13:20 UTC: Bash tool run_in_background, NOT setsid

Detached (setsid/nohup) runs die when your session goes idle between turns (every part and the owner saw it). Run it with the
Bash tool's `run_in_background: true` and `timeout: 7200000`, which keeps your session alive while it runs:

    bash /mnt/project-files/standing-still-h2h-2026-11-17/run-part.sh <arm> <N> > ~/ss-part.log 2>&1 < /dev/null

Use your row's two words (e.g. part 6: `opp 2`). When the background task ends before `<folder>/done` exists (2-hour limit,
restart), start the same line the same way again.
The script makes a sparse simulation-data clone (a full one is 12 GB and fills the disk), runs your 36 games 3 at a time, pushes
each finished game to simulation-data, and copies finished games to `<folder>/` here every 3 minutes (`<folder>/count.txt` = count).
At the end it appends your count to counts.log and creates `<folder>/done` when all 36 are in.

**Resumable**: after a stop, a container restart or "No space left on device", run the SAME line again; finished games are skipped.
Check it is alive with `pgrep -af simulate-local` and `tail ~/ss-part.log`.
**"Another simulation is running in this container"** with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`, run again.

## Check after the first 2-3 games

`~/owwt-sim/ss-<arm>-06f55ce-p<N>/data/measurements/<batch>/rules-off.txt` names STANDING BY NUMBERS (or its six parts) @Opponent
(parts 1-4) or @Mine (parts 5-8), and nothing else. The ON side's game logs show rows such as "TIME ON OUR SIDE", "NEARER NOT NEEDED",
"CHEAPEST HOLDER", "FALLS SHORT" or "NO FORCED ADVANCE"; the OFF side's do not. If the rules-off file is wrong, stop
(`pkill -f simulate-local`) and tell the owner thread with the game id.

## Report

Message the owner thread ("Test standing still against simpler", cmsg_01UAkEmFCZaVyiEY4rv4XRKjDcKv8P9Zxw525wrcKC3idW) with your count
after the first ~5 games and about every 45 minutes, and append `<UTC hh:mm> part N <done>/36` to counts.log here. Name any game that
crashed or hit the time limit (the log says "FAILED" or the game report says so). When `done` exists: message the owner with the
count, and stop. No add-sim-replays, no commits: the owner does that.

## CHANGED 14:30 UTC: shared folder near its file limit - stop copying games to it

simulation-data (git) is the only copy the owner uses. Stop your copier now (the run goes on):

    for p in $(pgrep -f "sleep 180"); do kill $(ps -o ppid= -p $p) $p; done

At the end the script still copies once; that is fine, the owner clears it after checking simulation-data. Make sure all 36 games
are pushed to simulation-data (re-push any failed push with fetch + rebase, never force).
