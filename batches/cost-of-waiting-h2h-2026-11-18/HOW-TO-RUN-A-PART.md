# Cost of waiting against simpler pricing, head-to-head (2026-11-18, sixth try) - one part

Both sides play the same build. In every game ONE side has everything ON (five options with worked-out chances, one target per enemy
shooter/charger in the risk), the other has `worked-out-chances,five-action,standing-by-numbers` OFF (= true simpler pricing). The same 144 DKTC pairs as tonight's five earlier tries (static-static, seed 1,
scenarios mix), played both ways = 288 games. 8 parts of 36 games. Other batches use their own folders on this mount: touch only this one.

| Part thread | Arm + N (the two words after run-part.sh) | Folder here | Pairs file | New side (everything ON) |
| --- | --- | --- | --- | --- |
| part 1 | `mine 1` | mine-1 | pairs-1.txt | Mine |
| part 2 | `mine 2` | mine-2 | pairs-2.txt | Mine |
| part 3 | `mine 3` | mine-3 | pairs-3.txt | Mine |
| part 4 | `mine 4` | mine-4 | pairs-4.txt | Mine |
| part 5 | `opp 1` | opp-1 | pairs-1.txt | Opponent |
| part 6 | `opp 2` | opp-2 | pairs-2.txt | Opponent |
| part 7 | `opp 3` | opp-3 | pairs-3.txt | Opponent |
| part 8 | `opp 4` | opp-4 | pairs-4.txt | Opponent |

Build: branch `claude/project-thread-60g6hv` at the sha written as the first word of the `go` file (it will be 2e2e69947...).
run-part.sh checks it out and builds it itself (Release). This is a NEW folder: do not touch the older five-options folders.
(The pairs-5..8 files are copies of pairs-1..4; the script reads pairs-<N> with N = 1-4, the second word of your row.)

## GATE: wait for the file `go`

Do the set-up now; start the games only when `/mnt/project-files/cost-of-waiting-h2h-2026-11-18/go` exists. If `STOP` exists
instead, read it. Check every few minutes (end your turn between checks, no sleep loops; a short Bash `run_in_background` waiter such as
`while [ ! -f /mnt/project-files/cost-of-waiting-h2h-2026-11-18/go ]; do sleep 60; done` with a long timeout is fine).

## Set-up (now)

    cd ~ && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd WarhammerOldWorldSimulator && git fetch origin claude/project-thread-60g6hv

.NET 10: `ci.dot.net` is blocked, so scripts/cloud-setup.sh fails. Install a fixed version instead:

    /usr/local/share/dotnet/dotnet --list-sdks | grep -q '^10\.' || { curl -sSL https://dot.net/v1/dotnet-install.sh -o /tmp/di.sh && bash /tmp/di.sh --version 10.0.100 --install-dir /usr/local/share/dotnet; }

(If your repo is not at ~/WarhammerOldWorldSimulator or /home/user/WarhammerOldWorldSimulator, put `REPO=<path>` in front of the run line.)

## Run (after `go`) - DETACHED, so it survives your shell

    setsid nohup bash /mnt/project-files/cost-of-waiting-h2h-2026-11-18/run-part.sh <arm> <N> >> ~/t6-part.log 2>&1 < /dev/null &

Use your row's two words (e.g. part 6: `opp 2`). The script checks out the go sha, builds (Release), makes a sparse simulation-data
clone, runs your 36 games 3 at a time, and every 3 minutes writes ONE packed file `<folder>/batch.tgz` here (plus `<folder>/count.txt`).
No loose files on the mount: it is near its file limit. At the end it appends your count to counts.log and creates `<folder>/done` when
all 36 are in, printing PART DONE (or PART NOT COMPLETE: run the line again).

## KEEP YOUR CONTAINER AWAKE

Your container is stopped soon after your turn ends with nothing running, and the detached run dies with it. Right after starting
(or restarting) the run, ALSO start this waiter with the Bash tool's `run_in_background` (timeout 7200000):

    D=/mnt/project-files/cost-of-waiting-h2h-2026-11-18; F=<your folder, e.g. mine-1>; while [ ! -f $D/$F/done ]; do pgrep -f simulate-local >/dev/null || pgrep -f run-part.sh >/dev/null || { echo DIED; exit 1; }; sleep 60; done; echo DONE

When it ends: DIED = run the run line again (it resumes; finished games are skipped) and a new waiter; DONE = report; timeout = start the waiter again.
**"Another simulation is running in this container"** with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`, run again.
Check it is alive with `pgrep -af simulate-local` and `tail ~/t6-part.log`.

## Check after the first 2-3 games

`~/owwt-sim/t6-<arm>-<sha7>-p<N>/data/measurements/<batch>/rules-off.txt` names worked-out-chances, five-action and standing-by-numbers
@Opponent (parts 1-4) or @Mine (parts 5-8) and nothing else. Also check the game log: in parts 1-4 the rows FIVE ACTION / STANDS STILL
/ LEGAL CHARGES ONLY (and HIS LEGAL MOVES / HIS MOVE AND SHOT / HIS TURN DENIED / THE PROMISE ADDS) appear for Mine only; in parts 5-8 for Opponent only. Put one line with what you saw in your first report. If it is wrong, stop (`pkill -f simulate-local; pkill -f run-part.sh`) and tell the
owner thread with the game id. Also tell the owner if a game takes more than 25 minutes.

## Report

Message the owner thread ("Test cost of waiting against simpler", cmsg_01UAkEmFCZaVyiEY4rv4XRKjP7N6VBcZ1vynEAhHZYqyfg) with your
count after the first ~5 games and about every 45 minutes, and append `<UTC hh:mm> part N <done>/36` to counts.log here. Name any
game that crashed or hit the time limit (the log says "FAILED" or the game report says so). When `done` exists: message the owner with
the count, and stop. Do not delete your container's ~/owwt-sim folder until the owner has merged. No add-sim-replays, no commits:
the owner does that.
