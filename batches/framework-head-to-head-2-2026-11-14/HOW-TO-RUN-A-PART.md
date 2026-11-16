# Job framework head-to-head 2 (with the five charge fixes) - one part

Batch 2 (2026-11-14): same as batch 1 but on the build with the five charge fixes (options 1-5 of
/mnt/project-files/framework-waits-2026-11-13/report.md) and the deployment/Orion fix c6fc19ce. Switch `job-framework` also switches
the five fixes off, so off-for-*.txt still give the old brain on the off side.

The question (Morten 2026-11-13): does the computer with the job framework beat the same computer without it? So in every game ONE side
plays with the framework and the other side plays with it switched off. The VP margin of the framework side decides.

144 DKTC games (Hero v Hero = static-static, seed 1, scenarios mix), the same pairs and seeds as the on/off batch in
/mnt/project-files/framework-batch-2026-11-13/, played twice so side and first-turn effects cancel:

- **fwmine-1..4**: framework ON for Mine, OFF for Opponent (`--rules-off` from `off-for-opponent.txt`);
- **fwopp-1..4**: framework ON for Opponent, OFF for Mine (`--rules-off` from `off-for-mine.txt`).

8 parts of 36 games (pairs-1..4.txt = the on/off batch's on-N/off-N pairs). One part per thread. No Haiku. Flank fixes stay ON for both sides.

Build: branch `claude/project-thread-281ndx` at `1eea44e9` (framework + per-side switch + deployment/Orion fix + five charge fixes; 16,629 green).

## Commands

    cd <repo> && git fetch origin claude/project-thread-281ndx && git checkout -B fw-h2h2 1eea44e9
    bash scripts/cloud-setup.sh; export PATH="$HOME/.dotnet:$PATH"     # if dotnet --version is not 10
    D=/mnt/project-files/framework-head-to-head-2-2026-11-14

  fwmine-N (framework side = Mine):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-opponent.txt)" --keep-as measurement --batch fw-h2h2-mine-1eea44e-pN \
      --look-for $D/look-for.md > ~/fw-h2h2-mine-N.log 2>&1

  fwopp-N (framework side = Opponent):

    scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-N.txt)" --seeds 1 --scenarios mix \
      --rules-off "$(cat $D/off-for-mine.txt)" --keep-as measurement --batch fw-h2h2-opp-1eea44e-pN \
      --look-for $D/look-for.md > ~/fw-h2h2-opp-N.log 2>&1

Replace N with your part number (pairs file, batch name, log name). Run it with the Bash tool's run_in_background.

**Resumable**: a part that stops (the 2-hour run limit, a container restart, "No space left on device") resumes with exactly the same
command - games with a `done` marker in the batch folder are skipped. Out of disk: delete old ~/owwt-sim/<batch> folders and the test
bin/obj folders first.

**"Another simulation is running in this container"** with nothing running: a leftover MSBuild node from the build still holds the lock.
Run `dotnet build-server shutdown; pkill -f MSBuild.dll` and the same command again.

**Report early**: message the owner thread with your game count after the first ~5 games and about every 30-45 minutes after.

**Check after the first 2-3 games**: the log's first lines say `Rules off: ...@opponent` (or `@mine`); the game logs' "Rules off" line and
the batch's rules-off.txt list every rule as `TAG@Opponent` (or `@Mine`). A game that stops with "is switched off for one side only, but
this check does not say for which side" is a check the port missed: stop and tell the owner thread with the game id and the last log lines.

**When done**: copy the whole batch folder (~/owwt-sim/<batch>/data/measurements/<batch>/ plus the log) to $D/<fwmine|fwopp>-N/, create an
empty file $D/<fwmine|fwopp>-N/done, and message the owner thread ("Run head-to-head on charge fixes", cmsg_01UAkEmFCZaVyiEY4rv4XRKjRoA13XXAVW7DfmBFP1eFTr) with your game count and any findings the log names.
No add-sim-replays, no commits: the owner does that.

## Reading the result (owner)

- Framework side: Mine in fwmine-*, Opponent in fwopp-*. Its VP margin = (framework side's VP - other side's VP), summed over all 288 games.
  Each pair of armies is played with the framework on each side once, so army, side and first-turn effects cancel.
- compare-batches.py KPI tables and job_claims.py now print a "Rules off - Opponent only: ..." (or "Mine only") line under the heading, and
  the ARMY STANCE row says "(defensive army switched off)" only for the off side. Mine/Opponent columns therefore read as framework/off in
  fwmine and off/framework in fwopp.
