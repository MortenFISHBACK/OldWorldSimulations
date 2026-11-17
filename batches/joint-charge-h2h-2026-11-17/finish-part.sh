#!/bin/bash
# Shared-folder file limit (14:30 UTC): games live on simulation-data only; the mount keeps count.txt and done.
# Usage: bash finish-part.sh <mine|opp> <N>   (run after simulate-local has stopped; it checks git, copies nothing)
ARM="$1"; N="$2"; D=/mnt/project-files/joint-charge-h2h-2026-11-17; B="jc-$ARM-1e5408d-p$N"; OUT="$D/$ARM-$N"
W="$HOME/owwt-sim/$B/data"; git -C "$W" fetch -q --depth 1 origin simulation-data
local_n=$(ls -d "$W/measurements/$B"/parts/*/done 2>/dev/null | wc -l)
git_n=$(git -C "$W" ls-tree -r --name-only FETCH_HEAD "measurements/$B/parts/" | grep -c '/done$')
mkdir -p "$OUT"; echo "$(date -u +%H:%M) part $ARM-$N $local_n/36 (on simulation-data $git_n)" > "$OUT/count.txt"
echo "$(date -u +%H:%M) part $ARM-$N $local_n/36 (on simulation-data $git_n)" >> "$D/counts.log"
if [ "$git_n" -ge 36 ]; then touch "$OUT/done"; echo "PART DONE"; elif [ "$local_n" -gt "$git_n" ]; then
  echo "Some games are not on simulation-data: push with: cd $W && git pull -q --rebase origin simulation-data && git push -q origin HEAD:simulation-data; then run this again"
else echo "PART NOT COMPLETE: run run-part.sh again"; fi
