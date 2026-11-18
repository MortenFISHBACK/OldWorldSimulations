#!/bin/bash
# analyse8.sh <root with <arm>-N/<batch>/game-*.log.jsonl> <workdir>
R=$1; W=$2; S=~/s10; mkdir -p $W/scripts; cd $W
python3 -I $S/build.py $R > build.out 2>&1; mv -f $S/charges.pkl $W/charges.pkl; cp $W/charges.pkl $W/scripts/
G=$(find $R -name 'game-*.log.jsonl' | wc -l)
python3 -I $S/report.py $R > report.out 2>&1
python3 -I $S/odds.py $R charges.pkl > odds.out 2>&1
python3 -I $S/flank.py charges.pkl $G > flank.out 2>&1
python3 -I $S/risk.py $R > risk.out 2>&1
python3 -I $S/shotrisk7.py $R > shot.out 2>&1
python3 -I $S/promise8.py $R > promise.out 2>&1
python3 -I $S/reach.py $R > reach.out 2>&1; python3 -I $S/reach2.py > reach2.out 2>&1; python3 -I $S/reach3.py > reach3.out 2>&1
echo done $G games
