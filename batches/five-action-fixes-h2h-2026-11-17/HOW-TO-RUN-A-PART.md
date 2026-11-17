# Fixed five actions against simpler pricing head-to-head (2026-11-17) - one part

Does the FIXED five-action computer stay level with simpler pricing (keep if not worse than about -30 VP a game)? Both sides play the
same build. In every game ONE side has five-action ON (with all its parts and the four new switches next-charge-by-list,
next-objective-nearer, no-double-rounds, scaled-chance); the other side has five-action OFF = simpler pricing. `likely-charge` is off
for both sides. The VP margin of the five-action side decides.

144 DKTC games (Hero v Hero = static-static, seed 1, scenarios mix), the SAME pairs and seeds as last night's five-action batch,
played twice so side and first-turn effects cancel. 8 parts of 36 games, one per thread. No Haiku.

| Part thread | Folder | Pairs file | Five-action ON for | `--rules-off` file | Batch name |
| --- | --- | --- | --- | --- | --- |
| part 1 | mine-1 | pairs-1.txt | Mine | off-for-opponent.txt | fafix-mine-5e477c5-p1 |
| part 2 | mine-2 | pairs-2.txt | Mine | off-for-opponent.txt | fafix-mine-5e477c5-p2 |
| part 3 | mine-3 | pairs-3.txt | Mine | off-for-opponent.txt | fafix-mine-5e477c5-p3 |
| part 4 | mine-4 | pairs-4.txt | Mine | off-for-opponent.txt | fafix-mine-5e477c5-p4 |
| part 5 | opp-1 | pairs-1.txt | Opponent | off-for-mine.txt | fafix-opp-5e477c5-p1 |
| part 6 | opp-2 | pairs-2.txt | Opponent | off-for-mine.txt | fafix-opp-5e477c5-p2 |
| part 7 | opp-3 | pairs-3.txt | Opponent | off-for-mine.txt | fafix-opp-5e477c5-p3 |
| part 8 | opp-4 | pairs-4.txt | Opponent | off-for-mine.txt | fafix-opp-5e477c5-p4 |

Build: branch `claude/project-thread-1nluyr` at `5e477c59`. Do NOT use any other head.

Do NOT touch other batch folders on the shared folder. Delete nothing there.

## GATE: wait for the file `go`

Set up and build now, but start the games only when the file `$D/go` exists (the owner creates it after a smoke game proved the
switches are ON). If `$D/STOP` exists instead, do not start and read it. Check every few minutes (end your turn between checks,
no sleep loops).

## Commands

    cd <repo> && git fetch origin claude/project-thread-1nluyr && git checkout -B fafix 5e477c59
    git log --oneline -1   # must start 5e477c59
    dotnet --version     # if it is not 10.x: bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"; export DOTNET_ROOT="$HOME/.dotnet"
    dotnet build OldWorldWarTable.sln -c Release --nologo -v q   # build while you wait for `go`
    D=/mnt/project-files/five-action-fixes-h2h-2026-11-17

  Parts 1-4 (folder mine-N, five-action ON for Mine):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-opponent.txt)" --keep-as measurement --batch fafix-mine-5e477c5-pN \
      --look-for $D/look-for.md > ~/fafix-mine-N.log 2>&1

  Parts 5-8 (folder opp-N, five-action ON for Opponent):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-mine.txt)" --keep-as measurement --batch fafix-opp-5e477c5-pN \
      --look-for $D/look-for.md > ~/fafix-opp-N.log 2>&1

N is the pairs number from the table (part 5 uses pairs-1, part 6 pairs-2, ...). Run it with the Bash tool's run_in_background
(timeout 7200000), and re-run the same command when it stops before 36 games.

**Resumable**: a part that stops (the 2-hour run limit, a container restart, "No space left on device") resumes with exactly the same
command - games with a `done` marker in the batch folder are skipped. Out of disk: delete old ~/owwt-sim/<batch> folders and the test
bin/obj folders first (in your own container only).

**"Another simulation is running in this container"** with nothing running: a leftover MSBuild node still holds the lock.
Run `dotnet build-server shutdown; pkill -f MSBuild.dll` and the same command again.

**Report early**: message the owner thread ("Test fixed five-action against simpler pricing", cmsg_01UAkEmFCZaVyiEY4rv4XRKjEWCWQmsvgAHY7mkwzRtyRH)
with your game count after the first ~5 games and about every 45 minutes after. Also append one line to
$D/counts.log: `<UTC time> part N <games done>/36`. Say if any game hit the Movement phase time limit, or crashed (the log or game report says so).

**Check after the first 2-3 games**: the batch's rules-off.txt names FIVE ACTION and its parts plus LIKELY CHARGE, each @Opponent
(parts 1-4) or @Mine (parts 5-8), and NOT advance worth / idle cost / risk once / one sum. The five-action side's game logs show
"FIVE ACTION" rows and "; FIVE:" and "SPLIT:" in its JOB RISK rows; the other side's JOB RISK rows have no "; FIVE:".
If not, stop and tell the owner thread with the game id.

**Keep it small**: the shared folder is near its limit (10 GB / 50,000 files). Copy only the batch folder and the log, nothing else
(no build output, no databases).

**Shared folder**: copy ONLY when the part is done, then check the copy: `du -sb` of source and copy must match and every game-*.txt must
be non-empty. A refused write looks saved but is not kept - if sizes differ, tell the owner thread at once.

**When done**: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<mine|opp>-N/,
create an empty file $D/<mine|opp>-N/done, and message the owner thread with your game count and any findings the log names.
No add-sim-replays, no commits: the owner does that.
