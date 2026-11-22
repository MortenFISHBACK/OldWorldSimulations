#!/bin/bash
# One part of the Walk 2 head-to-head of 2026-11-22: 144 games = 48 parts x 3, the same 72 pairs both ways.
# Parts 1-24: Walk 2 OFF for side "mine" (near-walks-only@mine); parts 25-48: the same pairs with it OFF for "opponent".
# Usage, in the FOREGROUND (Bash tool, run_in_background, timeout 7200000):
#   bash /mnt/project-files/near-walks-h2h-2026-11-22/run-part.sh <N> >> ~/nw-part.log 2>&1; tail -3 ~/nw-part.log
# Resumable: run the same line again after a stop (a finished part is skipped).
set -uo pipefail
net() { local i; for i in 1 2 3 4 5; do "$@" && return 0; echo "network step failed (try $i): $*"; sleep $((i*20)); done; return 1; }
N="$1"
D=/mnt/project-files/near-walks-h2h-2026-11-22
[ -f "$D/STOP" ] && { cat "$D/STOP"; exit 7; }
[ -f "$D/go" ] || { echo "no go file yet: wait"; exit 4; }
case "$N" in ''|*[!0-9]*) echo "N must be 1-48"; exit 2 ;; esac
[ "$N" -ge 1 ] && [ "$N" -le 48 ] || { echo "N must be 1-48"; exit 2; }
PAIRS=$(awk -v n="$N" '$1==n {print $2; exit}' "$D/parts.txt"); OFF=$(awk -v n="$N" '$1==n {print $3; exit}' "$D/parts.txt")
SHA=$(awk '{print $1; exit}' "$D/build.txt"); BR=$(awk '{print $2; exit}' "$D/build.txt"); S8=${SHA:0:8}; S7=${SHA:0:7}
REPO="${REPO:-$HOME/WarhammerOldWorldSimulator}"; [ -d "$REPO" ] || REPO=/home/user/WarhammerOldWorldSimulator
P="$D/part-$N"; OUT="$P"; mkdir -p "$P"; rm -f "$P/error.txt"
[ -f "$P/done" ] && { echo "part $N already done"; echo "PART DONE"; exit 0; }
/usr/local/share/dotnet/dotnet --list-sdks 2>/dev/null | grep -q '^10\.' || { net curl -sSL https://dot.net/v1/dotnet-install.sh -o /tmp/di.sh && net bash /tmp/di.sh --version 10.0.100 --install-dir /usr/local/share/dotnet > /tmp/di.log 2>&1; }
export DOTNET_ROOT=/usr/local/share/dotnet PATH=/usr/local/share/dotnet:$PATH
dotnet --list-sdks | grep -q '^10\.' || { echo ".NET 10 SDK not installed (see /tmp/di.log)" | tee "$P/error.txt"; exit 1; }
if [ "$(git -C "$REPO" rev-parse --short=8 HEAD)" != "$S8" ]; then
  git -C "$REPO" cat-file -e "$SHA^{commit}" 2>/dev/null || net git -C "$REPO" fetch -q origin "$BR"
  # discard every changed tracked file (scripts/__pycache__ and the like) so the checkout cannot be blocked
  git -C "$REPO" checkout -q -- . 2>/dev/null; git -C "$REPO" checkout -q -f --detach "$SHA" || { echo "cannot check out $SHA" | tee "$P/error.txt"; exit 3; }
fi
[ "$(git -C "$REPO" rev-parse --short=8 HEAD)" = "$S8" ] || { echo "repo is not at $S8" | tee "$P/error.txt"; exit 3; }
B="nw22-$S7-p$N"; W="$HOME/owwt-sim/$B"; BD="$W/data/measurements/$B"; mkdir -p "$W"
echo "$(date -u +%H:%M) part $N ($PAIRS, off: $OFF) begins"
if [ ! -d "$W/data/.git" ]; then
  net sh -c 'rm -rf "$1"; git clone -q --filter=blob:none --no-checkout --depth 1 --branch simulation-data "$2" "$1"' _ "$W/data" "$(git -C "$REPO" remote get-url origin)" || { echo "clone of simulation-data failed 5 times (network/proxy): say so in your thread" | tee "$P/error.txt"; exit 5; }
  git -C "$W/data" sparse-checkout set --no-cone '/README.md' '/batches/*/lessons.jsonl' '/batches/*/units.jsonl' "/measurements/$B/"
  net git -C "$W/data" checkout -q simulation-data || { echo "simulation-data checkout failed 5 times (network/proxy): say so in your thread" | tee "$P/error.txt"; exit 5; }
fi
pack() { [ -d "$BD" ] || return; tar czf "$W/batch.tgz.tmp" -C "$W/data/measurements" "$B" 2>/dev/null && cp "$W/batch.tgz.tmp" "$OUT/batch.tgz.tmp" && mv -f "$OUT/batch.tgz.tmp" "$OUT/batch.tgz"
  n=$(ls -d "$BD"/parts/*/done 2>/dev/null | wc -l); echo "$(date -u +%H:%M) part $N $n/3" > "$OUT/count.txt"; }
( while sleep 180; do pack; done ) &
COPIER=$!
if pgrep -f "[s]imulate-local.sh --opponent" >/dev/null; then
  echo "$(date -u +%H:%M) simulate-local already running: packing only until it ends"
  while pgrep -f "[s]imulate-local.sh --opponent" >/dev/null; do sleep 30; done
else
  ( cd "$REPO" && scripts/simulate-local.sh --opponent static-static --pairs "$PAIRS" --seeds 1 --scenarios mix \
      --rules-off "$OFF" --keep-as measurement --batch "$B" --look-for "$D/look-for.md" )
fi
kill $COPIER 2>/dev/null
pack
n=$(ls -d "$BD"/parts/*/done 2>/dev/null | wc -l)
logs=$(tar tzf "$OUT/batch.tgz" 2>/dev/null | grep -c 'game-.*\.log\.jsonl'); dbs=$(tar tzf "$OUT/batch.tgz" 2>/dev/null | grep -c 'records\.db$')
echo "$(date -u +%H:%M) part $N $n/3 ended, $logs logs, $dbs records" >> "$D/counts.log"
# A game that is saved (log + records) counts even if it did not end (time limit, crash): the owner scores what is there.
if [ "$logs" -ge 3 ] && [ "$dbs" -ge 3 ]; then touch "$P/done"; echo "PART DONE ($n/3 ended)"
else echo "PART NOT COMPLETE ($logs of 3 games saved): run the same line again"; fi
