#!/usr/bin/env python3
"""Turn-table HOLDER ASSIGNMENT rows (Strategy phase): did the assigned unit score that objective in that round (its own turn or the
enemy's turn after)?  python3 -I assigned.py <root with <arm>-N/...>"""
import sys, glob, json, os, re, collections, html
R = sys.argv[1]; c = collections.Counter(); claim = []; byjob = collections.Counter()
for f in glob.glob(os.path.join(R, '*/*/game-*.log.jsonl')):
    rows = []; obj = collections.defaultdict(set)
    for l in open(f):
        if '"objective"' in l[:20]:
            d = json.loads(l); obj[(d['turn'], d['side'], d['unit'])].add((d['objective'], d['index']))
        elif 'HOLDER ASSIGNMENT' in l:
            d = json.loads(l)
            if d['phase'] == 'Strategy' and 'assigned holder takes it' in d['summary']: rows.append(d)
    for d in rows:
        t = d['target'] or ''; m = re.match(r'Marker (\d+)', t)
        if m: want = ('StrategicLocation', int(m.group(1)) - 1); kind = 'marker'
        elif 'hill' in t.lower(): want = ('Hill', None); kind = 'hill'
        else: kind = 'other (' + re.sub(r"Opponent's |Mine's ", '', html.unescape(t)) + ')'; want = None
        c[kind, 'n'] += 1
        v = float(re.search(r'([+-]?[\d.]+) VP', d['summary'].replace('\\u002B', '+')).group(1)); 
        if want:
            got = obj.get((d['turn'], d['side'], d['actor']), set())
            hit = any(o == want[0] and (want[1] is None or i == want[1]) for o, i in got)
            c[kind, 'hit'] += hit; c[kind, 'claim'] += v
print("| Assigned to | Assignments | Claimed (mean VP) | Holder scored it that round |\n| --- | --- | --- | --- |")
for k in sorted({k for k, _ in c}):
    n = c[k, 'n']; print(f"| {k} | {n} | {c[k,'claim']/n:.0f} | {c[k,'hit']/n:.0%} |" if not k.startswith('other') else f"| {k} | {n} | - | not measured |")
