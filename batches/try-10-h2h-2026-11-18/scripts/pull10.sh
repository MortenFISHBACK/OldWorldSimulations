#!/bin/bash
# copy every part's batch.tgz from the mount to ~/t10/<arm>-N and unpack
D=/mnt/project-files/try-10-h2h-2026-11-18; rm -rf ~/t10; mkdir -p ~/t10
for p in mine-1 mine-2 mine-3 mine-4 opp-1 opp-2 opp-3 opp-4; do [ -f $D/$p/batch.tgz ] || continue; mkdir -p ~/t10/$p; cp $D/$p/batch.tgz /tmp/b.tgz && tar xzf /tmp/b.tgz -C ~/t10/$p; done
find ~/t10 -name 'game-*.log.jsonl' | wc -l
