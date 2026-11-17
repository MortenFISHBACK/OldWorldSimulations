#!/bin/bash
# One part of the deployment head-to-head (2026-11-17). Usage, with the Bash tool's run_in_background (timeout 7200000):
#   bash /mnt/project-files/deployment-h2h-2026-11-17/run-part.sh <mine|opp> <N> >> ~/dep-part.log 2>&1
# Games stay OFF the shared folder: every finished game is pushed to simulation-data (measurements/<batch>) by simulate-local.sh.
# The shared folder gets only status-<arm>-<N>.txt (rewritten every 3 min), one line in counts.log at the end, and done-<arm>-<N>.
# Resumable: run the same line again after a stop or container restart; games already on simulation-data are skipped.
set -uo pipefail
ARM="$1"; N="$2"
D=/mnt/project-files/deployment-h2h-2026-11-17
REPO="${REPO:-$HOME/WarhammerOldWorldSimulator}"; [ -d "$REPO" ] || REPO=/home/user/WarhammerOldWorldSimulator
export DOTNET_ROOT=/usr/local/share/dotnet PATH=/usr/local/share/dotnet:$PATH
case "$ARM" in mine) OFF="$D/off-for-opponent.txt" ;; opp) OFF="$D/off-for-mine.txt" ;; *) echo "arm must be mine or opp"; exit 2 ;; esac
[ "$(git -C "$REPO" rev-parse --short=8 HEAD)" = 13df7bd5 ] || { echo "repo is not at 13df7bd5"; exit 3; }
B="dep-$ARM-13df7bd-p$N"; W="$HOME/owwt-sim/$B"; BD="$W/data/measurements/$B"; ST="$D/status-$ARM-$N.txt"
mkdir -p "$W"
if [ ! -d "$W/data/.git" ]; then
  git clone -q --filter=blob:none --no-checkout --depth 1 --branch simulation-data "$(git -C "$REPO" remote get-url origin)" "$W/data" || exit 5
  git -C "$W/data" sparse-checkout set --no-cone '/README.md' '/batches/*/lessons.jsonl' '/batches/*/units.jsonl' "/measurements/$B/"
  git -C "$W/data" checkout -q simulation-data
fi
# Games pushed to simulation-data (the source of truth), counted on the remote branch itself.
remote_count() { git -C "$W/data" fetch -q --depth 1 origin simulation-data 2>/dev/null
  git -C "$W/data" ls-tree -r --name-only FETCH_HEAD "measurements/$B/parts/" 2>/dev/null | grep -c '/done$'; }
status() { local l p w; l=$(ls -d "$BD"/parts/*/done 2>/dev/null | wc -l); p=$(remote_count)
  w=$(grep -c "WARNING: kept in this container only" "$HOME/dep-part.log" 2>/dev/null)
  echo "$(date -u +%H:%M) part $ARM-$N played $l/36, on simulation-data $p/36, push warnings $w" > "$ST"; }
( while sleep 180; do status; done ) &
WATCH=$!
if pgrep -f "simulate-local.sh.*--batch $B" >/dev/null; then
  echo "$(date -u +%H:%M) already running: watching only"; while pgrep -f "simulate-local.sh.*--batch $B" >/dev/null; do sleep 30; done
else
  cd "$REPO" && scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-$N.txt)" --seeds 1 --scenarios mix \
    --rules-off "$(cat $OFF)" --keep-as measurement --batch "$B" --look-for "$D/look-for.md"
fi
kill $WATCH 2>/dev/null
status; p=$(remote_count)
echo "$(date -u +%H:%M) part $ARM-$N $p/36 on simulation-data" >> "$D/counts.log"
if [ "$p" -ge 36 ]; then touch "$D/done-$ARM-$N"; echo "PART DONE"; else echo "PART NOT COMPLETE ($p/36 on simulation-data): run the same line again"; fi
