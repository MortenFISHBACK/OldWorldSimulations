#!/bin/bash
# Lists the batch branches of this archive: branch, date of its commit, batch folder(s) it adds to main, and "DUE" when the commit is
# more than 14 days old (README rule 3). It deletes nothing: `git push origin --delete <branch>` is for whoever may.
#   scripts/batch-branches.sh [days]     default 14
set -euo pipefail
days=${1:-14}
git fetch -q --prune origin
now=$(date +%s)
for b in $(git for-each-ref --format='%(refname:short)' refs/remotes/origin | grep -v -E '^origin/(main|HEAD)$'); do
  ahead=$(git rev-list --count origin/main.."$b")
  [ "$ahead" -gt 0 ] || continue
  when=$(git log -1 --format=%ct "$b")
  batches=$(git diff --name-only origin/main..."$b" | sed -n 's|^batches/\([^/]*\)/.*|\1|p' | sort -u | tr '\n' ' ')
  due=""; [ $(( (now - when) / 86400 )) -ge "$days" ] && due="DUE"
  printf '%s\t%s\t%s\t%s\n' "${b#origin/}" "$(date -u -d "@$when" +%F)" "${batches:-(no batch folder)}" "$due"
done | sort -k2
