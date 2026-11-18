#!/usr/bin/env python3
"""Count holder rows per side in game logs: python3 -I sides.py <game.log.jsonl or folder/tgz>..."""
import sys, json, glob, os, tarfile, collections, re
TAGS = ("HOLDER ASSIGNMENT", "HOLDER AT DEPLOYMENT", "CHEAPEST HOLDER")
def scan(name, lines):
    c = collections.Counter()
    for l in lines:
        if b'"OpponentRule"' not in l and b'HOLDER' not in l: continue
        try: r = json.loads(l)
        except Exception: continue
        s = r.get('summary') or ''
        for t in TAGS:
            if s.startswith(t) or (t in s and r.get('type') == 'OpponentRule'): c[(r.get('side'), t)] += 1
    print(os.path.basename(name), ' '.join(f"{t}:{c[('Mine',t)]}/{c[('Opponent',t)]}" for t in TAGS), '(Mine/Opponent)')
for a in sys.argv[1:]:
    if a.endswith('.tgz') or a.endswith('.tar.gz'):
        t = tarfile.open(a)
        for m in t:
            if m.name.endswith('.log.jsonl'): scan(m.name, t.extractfile(m))
    else:
        for f in (sorted(glob.glob(os.path.join(a, '**/*.log.jsonl'), recursive=True)) if os.path.isdir(a) else [a]):
            scan(f, open(f, 'rb'))
