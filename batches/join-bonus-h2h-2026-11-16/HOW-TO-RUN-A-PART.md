# Join bonus head-to-head (2026-11-16) - one part

Does the computer with the bonus for joining a friend's charge (switch `joins-a-friend`) beat the same computer without it?
In every game ONE side plays with the bonus and the other side plays as main (bonus switched off). Everything else stays ON for both
sides. The VP margin of the bonus side decides.

144 DKTC games (Hero v Hero = static-static, seed 1, scenarios mix), the SAME pairs and seeds as today's charge worth and set-up
head-to-heads, played twice so side and first-turn effects cancel. 8 parts of 36 games, one per thread. No Haiku.

| Part thread | Folder | Pairs file | Bonus ON for | `--rules-off` file | Batch name |
| --- | --- | --- | --- | --- | --- |
| part 1 | opp-1 | pairs-1.txt | Opponent | off-for-mine.txt | jb-h2h-opp-b54c226-p1 |
| part 2 | opp-2 | pairs-2.txt | Opponent | off-for-mine.txt | jb-h2h-opp-b54c226-p2 |
| part 3 | opp-3 | pairs-3.txt | Opponent | off-for-mine.txt | jb-h2h-opp-b54c226-p3 |
| part 4 | opp-4 | pairs-4.txt | Opponent | off-for-mine.txt | jb-h2h-opp-b54c226-p4 |
| part 5 | mine-1 | pairs-1.txt | Mine | off-for-opponent.txt | jb-h2h-mine-b54c226-p1 |
| part 6 | mine-2 | pairs-2.txt | Mine | off-for-opponent.txt | jb-h2h-mine-b54c226-p2 |
| part 7 | mine-3 | pairs-3.txt | Mine | off-for-opponent.txt | jb-h2h-mine-b54c226-p3 |
| part 8 | mine-4 | pairs-4.txt | Mine | off-for-opponent.txt | jb-h2h-mine-b54c226-p4 |

(Parts 1-4 switch the bonus off for Mine; parts 5-8 switch it off for Opponent.)

Build: branch `claude/project-thread-u9nplz` at `b54c22600` (built on main c7c800290; repo note
docs/claude-memory/project_joins_a_friend_2026-11-16.md).

Do NOT touch other batch folders on the shared folder. Delete nothing there.

## Commands

    cd <repo> && git fetch origin claude/project-thread-u9nplz && git checkout -B jb-h2h b54c22600
    git log --oneline -1   # must start b54c2260
    dotnet --version     # if it is not 10.x: bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"; export DOTNET_ROOT="$HOME/.dotnet"
    D=/mnt/project-files/join-bonus-h2h-2026-11-16

  Parts 1-4 (folder opp-N, bonus ON for Opponent):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-mine.txt)" --keep-as measurement --batch jb-h2h-opp-b54c226-pN \
      --look-for $D/look-for.md > ~/jb-h2h-opp-N.log 2>&1

  Parts 5-8 (folder mine-N, bonus ON for Mine):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-opponent.txt)" --keep-as measurement --batch jb-h2h-mine-b54c226-pN \
      --look-for $D/look-for.md > ~/jb-h2h-mine-N.log 2>&1

N is the pairs number from the table (part 5 uses pairs-1, part 6 pairs-2, ...). Run it with the Bash tool's run_in_background.

**Resumable**: a part that stops (the 2-hour run limit, a container restart, "No space left on device") resumes with exactly the same
command - games with a `done` marker in the batch folder are skipped. Out of disk: delete old ~/owwt-sim/<batch> folders and the test
bin/obj folders first (in your own container only).

**"Another simulation is running in this container"** with nothing running: a leftover MSBuild node still holds the lock.
Run `dotnet build-server shutdown; pkill -f MSBuild.dll` and the same command again.

**Report early**: message the owner thread ("Run join bonus head-to-head", cmsg_01UAkEmFCZaVyiEY4rv4XRKjJtvbTGNtaPYbSSRHQSxasT)
with your game count after the first ~5 games and about every 30-45 minutes after. Also say if any game hit the Movement phase time
limit (the log or game report says so).

**Check after the first 2-3 games**: the log's first lines say `Rules off: joins-a-friend@mine` (or `@opponent`); the game logs'
"Rules off" line and the batch's rules-off.txt name the tag as `JOINS A FRIEND@Mine` (or `@Opponent`). A game that stops with "is
switched off for one side only, but this check does not say for which side" is a check the port missed: stop and tell the owner thread
with the game id and the last log lines.

**Keep it small**: the shared folder is near its limit (10 GB / 50,000 files). Copy only the batch folder and the log, nothing else
(no build output, no databases).

**Shared folder**: copy ONLY when the part is done, then check the copy: `du -sb` of source and copy must match and every game-*.txt must
be non-empty. A refused write looks saved but is not kept - if sizes differ, tell the owner thread at once.

**When done**: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<opp|mine>-N/,
create an empty file $D/<opp|mine>-N/done, and message the owner thread with your game count and any findings the log names.
No add-sim-replays, no commits: the owner does that.
