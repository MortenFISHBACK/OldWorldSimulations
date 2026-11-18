#!/bin/bash
D=/mnt/project-files/joint-charge-now-h2h-2026-11-18; rm -rf ~/ja; mkdir -p ~/ja
for p in mine-1 mine-2 mine-3 mine-4 opp-1 opp-2 opp-3 opp-4; do [ -f $D/$p/batch.tgz ] || continue; mkdir -p ~/ja/$p; cp $D/$p/batch.tgz /tmp/b.tgz && tar xzf /tmp/b.tgz -C ~/ja/$p; done
find ~/ja -name 'game-*.log.jsonl' | wc -l
