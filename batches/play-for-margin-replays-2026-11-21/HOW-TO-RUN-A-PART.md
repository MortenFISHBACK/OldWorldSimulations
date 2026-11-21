# How to run a part: play-for-margin replays (2026-11-21)

Owner: the thread "Measure goals-first on 144 replays". 48 parts, numbers 1 to 48, three games each (one round: the three play side by
side in your container). The games are the 144 pairs of the danger head-to-head of 2026-11-20, played one way (overhaul on Opponent,
true simpler on Mine), scenario mix, seed 1, on main 617b6ccd (`build.txt`). Your part's three pairs are the line of `parts.txt` that
starts with your number. Touch only your own `part-<N>` folder. No commits, no add-sim-replays: the owner does that.

## GATE: wait for the file `go`

Do the set-up now; start the games only when `/mnt/project-files/play-for-margin-replays-2026-11-21/go` exists. If `STOP` exists
instead, read it. A Bash `run_in_background` waiter (timeout 7200000) is fine:

    while [ ! -f /mnt/project-files/play-for-margin-replays-2026-11-21/go ]; do [ -f /mnt/project-files/play-for-margin-replays-2026-11-21/STOP ] && { echo STOP; exit 1; }; sleep 30; done; echo GO

## Set-up (now)

    cd /home/user && [ -d WarhammerOldWorldSimulator ] || git clone https://github.com/MortenFISHBACK/WarhammerOldWorldSimulator.git
    cd /home/user/WarhammerOldWorldSimulator && git fetch -q origin main

## Run (after `go`) - DETACHED, so it survives your shell

    setsid nohup bash /mnt/project-files/play-for-margin-replays-2026-11-21/run-part.sh <N> >> ~/pm-part.log 2>&1 < /dev/null &

`<N>` is your part number only (e.g. part 7: `run-part.sh 7`). The script installs .NET 10 if needed, checks out 617b6ccd, builds, makes a
sparse simulation-data clone, plays your 3 games side by side, and every 3 minutes writes ONE packed file `part-<N>/batch.tgz` here (plus
`part-<N>/count.txt`). At the end it appends a line to counts.log and creates `part-<N>/done` when all 3 games (logs and records) are in,
printing PART DONE (or PART NOT COMPLETE: run the line again). On a set-up fault it writes `part-<N>/error.txt`: say so and stop, fix nothing.

## KEEP YOUR CONTAINER AWAKE

Right after starting (or restarting) the run, ALSO start this waiter with the Bash tool's `run_in_background` (timeout 7200000):

    P=/mnt/project-files/play-for-margin-replays-2026-11-21/part-<N>; while [ ! -f $P/done ]; do [ -f $P/error.txt ] && { cat $P/error.txt; exit 2; }; pgrep -f simulate-local >/dev/null || pgrep -f run-part.sh >/dev/null || { echo DIED; exit 1; }; sleep 60; done; echo DONE

When it ends: DIED = run the run line again (it resumes; finished games are skipped) and a new waiter; DONE = report; timeout = start
the waiter again. "Another simulation is running in this container" with nothing running: `dotnet build-server shutdown; pkill -f MSBuild.dll`,
run again. Check it is alive with `pgrep -af simulate-local` and `tail ~/pm-part.log`.

## Check after the first game

`~/owwt-sim/pm-opp-617b6cc-p<N>/data/measurements/pm-opp-617b6cc-p<N>/rules-off.txt` (or the `out` folder's) must name
`worked-out-chances`, `five-action` and `standing-by-numbers` for `@Mine` only. Put one line with what you saw in your thread.

## Report

The owner cannot read your thread and goes by the `done` files. When `part-<N>/done` exists: reply in your thread with the last line of
`~/pm-part.log` and the count, then stop. Do not delete ~/owwt-sim. A game that crashed or hit the time limit: name it in your reply.

| Part | Pairs |
| --- | --- |
| 1 | L0102,L0118,L0135 |
| 2 | L0218,L0235,L0319 |
| 3 | L0405,L0421,L0508 |
| 4 | L0524,L0612,L0628 |
| 5 | L0717,L0733,L0823 |
| 6 | L0913,L0930,L1021 |
| 7 | L1114,L1131,L1224 |
| 8 | L1319,L1335,L1431 |
| 9 | L1527,L1625,L1723 |
| 10 | L1823,L1923,L2025 |
| 11 | L2127,L2231,L2335 |
| 12 | L2531,L2730,L2934 |
| 13 | L0106,L0122,L0206 |
| 14 | L0222,L0307,L0323 |
| 15 | L0409,L0425,L0512 |
| 16 | L0528,L0616,L0632 |
| 17 | L0721,L0810,L0827 |
| 18 | L0918,L0934,L1026 |
| 19 | L1118,L1135,L1228 |
| 20 | L1323,L1418,L1435 |
| 21 | L1531,L1629,L1727 |
| 22 | L1827,L1927,L2029 |
| 23 | L2131,L2235,L2429 |
| 24 | L2535,L2735,L3033 |
| 25 | L0110,L0126,L0210 |
| 26 | L0226,L0311,L0327 |
| 27 | L0413,L0429,L0516 |
| 28 | L0533,L0620,L0709 |
| 29 | L0725,L0815,L0831 |
| 30 | L0922,L1013,L1030 |
| 31 | L1122,L1216,L1232 |
| 32 | L1327,L1422,L1519 |
| 33 | L1535,L1633,L1731 |
| 34 | L1831,L1932,L2033 |
| 35 | L2223,L2327,L2433 |
| 36 | L2630,L2832,L3133 |
| 37 | L0114,L0130,L0214 |
| 38 | L0230,L0315,L0332 |
| 39 | L0417,L0434,L0520 |
| 40 | L0608,L0624,L0713 |
| 41 | L0729,L0819,L0835 |
| 42 | L0926,L1017,L1034 |
| 43 | L1126,L1220,L1314 |
| 44 | L1331,L1427,L1523 |
| 45 | L1621,L1719,L1819 |
| 46 | L1835,L2021,L2123 |
| 47 | L2227,L2331,L2527 |
| 48 | L2634,L2930,L3234 |
