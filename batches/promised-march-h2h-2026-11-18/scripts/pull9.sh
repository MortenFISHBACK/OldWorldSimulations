#!/bin/bash
# copy every part's batch.tgz from the mount to ~/t9/<arm>-N and unpack
D=/mnt/project-files/promised-march-h2h-2026-11-18; rm -rf ~/t9; mkdir -p ~/t9
for p in mine-1 mine-2 mine-3 mine-4 opp-1 opp-2 opp-3 opp-4; do [ -f $D/$p/batch.tgz ] || continue; mkdir -p ~/t9/$p; cp $D/$p/batch.tgz /tmp/b.tgz && tar xzf /tmp/b.tgz -C ~/t9/$p; done
find ~/t9 -name 'game-*.log.jsonl' | wc -l
