#!/bin/bash
# One part of the charge-outcomes head-to-head. Usage (detached, see HOW-TO-RUN-A-PART.md):
#   setsid nohup bash /mnt/project-files/charge-outcomes-h2h-2026-11-17/run-part.sh <mine|opp> <N> > ~/co-part.log 2>&1 < /dev/null &
# Resumable: run the same line again after a stop or container restart.
set -uo pipefail
ARM="$1"; N="$2"
D=/mnt/project-files/charge-outcomes-h2h-2026-11-17
REPO="${REPO:-$HOME/WarhammerOldWorldSimulator}"; [ -d "$REPO" ] || REPO=/home/user/WarhammerOldWorldSimulator
export DOTNET_ROOT=/usr/local/share/dotnet PATH=/usr/local/share/dotnet:$PATH
case "$ARM" in mine) OFF="$D/off-for-opponent.txt" ;; opp) OFF="$D/off-for-mine.txt" ;; *) echo "arm must be mine or opp"; exit 2 ;; esac
B="${BATCH:-co-$ARM-a57fba0-p$N}"; OUT="$D/$ARM-$N"; W="$HOME/owwt-sim/$B"; BD="$W/data/measurements/$B"
mkdir -p "$OUT" "$W"
# Sparse clone of simulation-data (a full clone is 12 GB and fills the disk): the lessons, unit records and this batch only.
if [ ! -d "$W/data/.git" ]; then
  git clone -q --filter=blob:none --no-checkout --depth 1 --branch simulation-data "$(git -C "$REPO" remote get-url origin)" "$W/data" || exit 5
  git -C "$W/data" sparse-checkout set --no-cone '/README.md' '/batches/*/lessons.jsonl' '/batches/*/units.jsonl' "/measurements/$B/"
  git -C "$W/data" checkout -q simulation-data
fi
# Copier: every 3 minutes, finished games go to the shared folder (containers restart; the push to simulation-data is the other copy).
( while sleep 180; do [ -d "$BD" ] && cp -ru "$BD/." "$OUT/" 2>/dev/null; cp "$HOME/co-part.log" "$OUT/run.log" 2>/dev/null;
    n=$(ls -d "$BD"/parts/*/done 2>/dev/null | wc -l); echo "$(date -u +%H:%M) part $ARM-$N $n/36" > "$OUT/count.txt"; done ) &
COPIER=$!
cd "$REPO" && scripts/simulate-local.sh --opponent static-static --pairs "${PAIRS:-$(cat $D/pairs-$N.txt)}" --seeds 1 --scenarios mix \
  --rules-off "$(cat $OFF)" --keep-as measurement --batch "$B" --look-for "$D/look-for.md"
kill $COPIER 2>/dev/null
cp -ru "$BD/." "$OUT/"; cp "$HOME/co-part.log" "$OUT/run.log" 2>/dev/null
n=$(ls -d "$BD"/parts/*/done 2>/dev/null | wc -l)
echo "$(date -u +%H:%M) part $ARM-$N $n/36" > "$OUT/count.txt"; echo "$(date -u +%H:%M) part $ARM-$N $n/36" >> "$D/counts.log"
if [ "$n" -ge 36 ] && [ "$(du -sb "$BD" | cut -f1)" -le "$(du -sb "$OUT" | cut -f1)" ]; then touch "$OUT/done"; echo "PART DONE"; else echo "PART NOT COMPLETE ($n/36): run the same line again"; fi
