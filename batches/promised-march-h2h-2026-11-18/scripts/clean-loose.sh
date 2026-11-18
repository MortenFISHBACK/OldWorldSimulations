#!/bin/bash
# Removes loose game files from a part folder once its batch.tgz holds every game log found loose. Usage: clean-loose.sh <folder>
F="$1"; [ -f "$F/batch.tgz" ] || { echo "$F: no batch.tgz"; exit 1; }
inT=$(tar tzf "$F/batch.tgz" | grep -o 'game-[^/]*\.log\.jsonl$' | sort -u)
loose=$(cd "$F" && ls game-*.log.jsonl 2>/dev/null | sort -u)
miss=$(comm -13 <(echo "$inT") <(echo "$loose") | grep . )
[ -n "$miss" ] && { echo "$F: tgz lacks $miss"; exit 1; }
rm -rf "$F/parts"; find "$F" -mindepth 1 -maxdepth 1 ! -name batch.tgz ! -name count.txt ! -name done ! -name run.log -exec rm -rf {} +
echo "$F: cleaned, tgz has $(echo "$inT" | grep -c .) games, files left $(find "$F" -type f | wc -l)"
