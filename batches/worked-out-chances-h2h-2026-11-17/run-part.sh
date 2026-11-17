#!/bin/bash
# One part of the worked-out-chances head-to-head (2026-11-17). The mount gets ONE packed file per part (<folder>/batch.tgz,
# rewritten every 3 minutes). Usage, DETACHED:  setsid nohup bash /mnt/project-files/worked-out-chances-h2h-2026-11-17/run-part.sh <mine|opp> <N> >> ~/wc-part.log 2>&1 < /dev/null &
# If simulate-local is already running in this container, it does not start another: it only packs until that run ends.
# Resumable: run the same line again after a stop or container restart.
set -uo pipefail
ARM="$1"; N="$2"
D=/mnt/project-files/worked-out-chances-h2h-2026-11-17
REPO="${REPO:-$HOME/WarhammerOldWorldSimulator}"; [ -d "$REPO" ] || REPO=/home/user/WarhammerOldWorldSimulator
export DOTNET_ROOT=/usr/local/share/dotnet PATH=/usr/local/share/dotnet:$PATH
[ "$(git -C "$REPO" rev-parse --short=8 HEAD)" = b0077eed ] || { echo "repo is not at b0077eed: git checkout -B wc b0077eed4 first"; exit 3; }
case "$ARM" in mine) OFF="$D/off-for-opponent.txt" ;; opp) OFF="$D/off-for-mine.txt" ;; *) echo "arm must be mine or opp"; exit 2 ;; esac
B="wc-$ARM-b0077ee-p$N"; OUT="$D/$ARM-$N"; W="$HOME/owwt-sim/$B"; BD="$W/data/measurements/$B"
mkdir -p "$OUT" "$W"
pack() { [ -d "$BD" ] || return; tar czf "$W/batch.tgz.tmp" -C "$W/data/measurements" "$B" 2>/dev/null && cp "$W/batch.tgz.tmp" "$OUT/batch.tgz.tmp" && mv -f "$OUT/batch.tgz.tmp" "$OUT/batch.tgz"
  n=$(ls -d "$BD"/parts/*/done 2>/dev/null | wc -l); echo "$(date -u +%H:%M) part $ARM-$N $n/36" > "$OUT/count.txt"; }
if [ ! -d "$W/data/.git" ]; then
  git clone -q --filter=blob:none --no-checkout --depth 1 --branch simulation-data "$(git -C "$REPO" remote get-url origin)" "$W/data" || exit 5
  git -C "$W/data" sparse-checkout set --no-cone '/README.md' '/batches/*/lessons.jsonl' '/batches/*/units.jsonl' "/measurements/$B/"
  git -C "$W/data" checkout -q simulation-data
fi
( while sleep 180; do pack; done ) &
COPIER=$!
if pgrep -f simulate-local >/dev/null; then
  echo "$(date -u +%H:%M) simulate-local already running: packing only until it ends"
  while pgrep -f simulate-local >/dev/null; do sleep 30; done
else
  cd "$REPO" && scripts/simulate-local.sh --opponent static-static --pairs "$(cat $D/pairs-$N.txt)" --seeds 1 --scenarios mix \
    --rules-off "$(cat $OFF)" --keep-as measurement --batch "$B" --look-for "$D/look-for.md"
fi
kill $COPIER 2>/dev/null
pack
n=$(ls -d "$BD"/parts/*/done 2>/dev/null | wc -l)
echo "$(date -u +%H:%M) part $ARM-$N $n/36" >> "$D/counts.log"
if [ "$n" -ge 36 ] && tar tzf "$OUT/batch.tgz" | grep -c 'game-.*\.log\.jsonl$' | grep -qx 36; then touch "$OUT/done"; echo "PART DONE"; else echo "PART NOT COMPLETE ($n/36): run the same line again"; fi
