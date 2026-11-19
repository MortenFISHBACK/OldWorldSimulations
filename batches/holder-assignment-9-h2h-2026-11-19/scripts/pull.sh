#!/bin/bash
# copy each part's batch.tgz to ~/h9/<arm-N>/ and unpack
D=/mnt/project-files/holder-assignment-9-h2h-2026-11-19
for a in mine-1 mine-2 mine-3 mine-4 opp-1 opp-2 opp-3 opp-4; do
  [ -f $D/$a/batch.tgz ] || continue
  mkdir -p ~/h9/$a; cp $D/$a/batch.tgz ~/h9/$a.tgz && tar xzf ~/h9/$a.tgz -C ~/h9/$a 2>/dev/null
  echo "$a $(cat $D/$a/count.txt 2>/dev/null)"
done
