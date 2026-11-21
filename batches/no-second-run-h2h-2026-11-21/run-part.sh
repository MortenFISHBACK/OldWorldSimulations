#!/bin/bash
# One part of the no second run head-to-head (2026-11-21, one of cut C's three cuts alone): 3 pairs of the danger head-to-head (danger-h2h-2026-11-20), the
# same scenario mix and seed 1, both sides with every rule on except no-second-run off on one side (parts.txt), build in build.txt.
# Usage, DETACHED:  setsid nohup bash /mnt/project-files/no-second-run-h2h-2026-11-21/run-part.sh <N> >> ~/cnsr-part.log 2>&1 < /dev/null &
# Resumable: run the same line again after a stop or container restart (finished games are skipped).
set -uo pipefail
net() { local i; for i in 1 2 3 4 5; do "$@" && return 0; echo "network step failed (try $i): $*"; sleep $((i*20)); done; return 1; }
N="$1"
D=${PM_DIR:-/mnt/project-files/no-second-run-h2h-2026-11-21}
[ -f "$D/go" ] || { echo "no go file yet: wait"; exit 4; }
PAIRS=$(awk -v n="$N" '$1==n {print $2; exit}' "$D/parts.txt"); OFF=$(awk -v n="$N" '$1==n {print $3; exit}' "$D/parts.txt"); [ -n "$PAIRS" ] || { echo "part $N not in parts.txt"; exit 2; }
SHA=$(awk '{print $1; exit}' "$D/build.txt"); S8=${SHA:0:8}; S7=${SHA:0:7}
REPO="${REPO:-$HOME/WarhammerOldWorldSimulator}"; [ -d "$REPO" ] || REPO=/home/user/WarhammerOldWorldSimulator
OUT="$D/part-$N"; mkdir -p "$OUT"; rm -f "$OUT/error.txt"
/usr/local/share/dotnet/dotnet --list-sdks 2>/dev/null | grep -q '^10\.' || { net curl -sSL https://dot.net/v1/dotnet-install.sh -o /tmp/di.sh && net bash /tmp/di.sh --version 10.0.100 --install-dir /usr/local/share/dotnet > /tmp/di.log 2>&1; }
export DOTNET_ROOT=/usr/local/share/dotnet PATH=/usr/local/share/dotnet:$PATH
dotnet --list-sdks | grep -q '^10\.' || { echo ".NET 10 SDK not installed (see /tmp/di.log)" | tee "$OUT/error.txt"; exit 1; }
if [ "$(git -C "$REPO" rev-parse --short=8 HEAD)" != "$S8" ]; then
  git -C "$REPO" cat-file -e "$SHA^{commit}" 2>/dev/null || net git -C "$REPO" fetch -q origin claude/project-thread-rjmkp1
  git -C "$REPO" checkout -q --detach "$SHA" || { echo "cannot check out $SHA" | tee "$OUT/error.txt"; exit 3; }
fi
[ "$(git -C "$REPO" rev-parse --short=8 HEAD)" = "$S8" ] || { echo "repo is not at $S8" | tee "$OUT/error.txt"; exit 3; }
B="${PM_BATCH:-cnsr-$S7-p$N}"; W="$HOME/owwt-sim/$B"; BD="$W/data/measurements/$B"
mkdir -p "$W"
pack() { [ -d "$BD" ] || return; tar czf "$W/batch.tgz.tmp" -C "$W/data/measurements" "$B" 2>/dev/null && cp "$W/batch.tgz.tmp" "$OUT/batch.tgz.tmp" && mv -f "$OUT/batch.tgz.tmp" "$OUT/batch.tgz"
  n=$(ls -d "$BD"/parts/*/done 2>/dev/null | wc -l); echo "$(date -u +%H:%M) part $N $n/3" > "$OUT/count.txt"; }
if [ ! -d "$W/data/.git" ]; then
  net sh -c 'rm -rf "$1"; git clone -q --filter=blob:none --no-checkout --depth 1 --branch simulation-data "$2" "$1"' _ "$W/data" "$(git -C "$REPO" remote get-url origin)" || { echo "clone of simulation-data failed 5 times (network/proxy): this container cannot reach GitHub; restart the part in a new thread" | tee "$OUT/error.txt"; exit 5; }
  git -C "$W/data" sparse-checkout set --no-cone '/README.md' '/batches/*/lessons.jsonl' '/batches/*/units.jsonl' "/measurements/$B/"
  net git -C "$W/data" checkout -q simulation-data || { echo "simulation-data checkout failed 5 times (network/proxy): restart the part in a new thread" | tee "$OUT/error.txt"; exit 5; }
fi
( while sleep 180; do pack; done ) &
COPIER=$!
if pgrep -f simulate-local >/dev/null; then
  echo "$(date -u +%H:%M) simulate-local already running: packing only until it ends"
  while pgrep -f simulate-local >/dev/null; do sleep 30; done
else
  cd "$REPO" && scripts/simulate-local.sh --opponent static-static --pairs "$PAIRS" --seeds 1 --scenarios mix \
    --rules-off "$OFF" --keep-as measurement --batch "$B" --look-for "$D/look-for.md"
fi
kill $COPIER 2>/dev/null
pack
n=$(ls -d "$BD"/parts/*/done 2>/dev/null | wc -l)
echo "$(date -u +%H:%M) part $N $n/3" >> "$D/counts.log"
if [ "$n" -ge 3 ] && tar tzf "$OUT/batch.tgz" | grep -c 'game-.*\.log\.jsonl' | grep -qx 3 && [ "$(tar tzf "$OUT/batch.tgz" | grep -c 'records\.db$')" -ge 3 ]; then touch "$OUT/done"; echo "PART DONE"; else echo "PART NOT COMPLETE ($n/3): run the same line again"; fi
