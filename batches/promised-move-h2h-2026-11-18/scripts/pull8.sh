#!/bin/bash
# copy every part's batch.tgz from the mount to ~/t8/<arm>-N and unpack
D=/mnt/project-files/promised-move-h2h-2026-11-18; rm -rf ~/t8; mkdir -p ~/t8
for p in mine-1 mine-2 mine-3 mine-4 opp-1 opp-2 opp-3 opp-4; do [ -f $D/$p/batch.tgz ] || continue; mkdir -p ~/t8/$p; cp $D/$p/batch.tgz /tmp/b.tgz && tar xzf /tmp/b.tgz -C ~/t8/$p; done
find ~/t8 -name 'game-*.log.jsonl' | wc -l
