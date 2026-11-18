#!/usr/bin/env python3
"""Try 10 extra measures: joint on the table, pair below the better unit alone, table/order rows, blocked landings, minutes.
python3 -I m10.py <root with <arm>-N/<batch>/game-*.log.jsonl>"""
import collections, glob, json, os, re, sys, csv
ROOT = sys.argv[1]
c = collections.Counter(); games = 0
JCN = re.compile(r"joint ~(-?[\d.]+) VP against ~(-?[\d.]+) without it")
JOT = re.compile(r"JOINT ON THE TABLE: #(\d+) (.*?) behind it has the charge on #(\d+)")
mins = []
for g in glob.glob(ROOT + '/**/games.csv', recursive=True):
    if '/parts/' in g: continue
    for r in csv.DictReader(open(g)):
        try: mins.append(float(r['minutes']))
        except: pass
for f in sorted(glob.glob(ROOT + '/**/game-*.log.jsonl', recursive=True)):
    arm = os.path.relpath(f, ROOT).split('/')[0].split('-')[0]
    on = 'Mine' if arm == 'mine' else 'Opponent'
    games += 1
    acts = []
    for line in open(f, encoding='utf-8'):
        if not line.startswith('{'): continue
        x = json.loads(line)
        if x.get('kind') != 'action': continue
        acts.append(x)
    decl = collections.defaultdict(set)
    for x in acts:
        if x.get('type') == 'Charge' and 'declares a charge' in (x.get('summary') or ''):
            decl[(x['turn'], x['side'], str(x.get('target_id')))].add(str(x.get('actor_id')))
    for x in acts:
        sm = x.get('summary') or ''
        if x.get('type') == 'Charge' and 'blocked short of contact' in sm:
            b = 'ON' if x['side'] == on else 'OFF'
            n = len(decl[(x['turn'], x['side'], str(x.get('target_id')))])
            c[b, 'charge halted: blocked short of contact'] += 1
            if n >= 2: c[b, 'charge halted: blocked short, in a set of 2+ chargers on that target'] += 1
    for x in acts:
        if x.get('type') != 'OpponentRule': continue
        s = x.get('summary') or ''; b = 'ON' if x['side'] == on else 'OFF'
        tag = s.split(':')[0]
        if tag == 'JOINT CHARGE NOW':
            c[b, 'jcn rows'] += 1
            m = JCN.search(s)
            if m:
                c[b, 'jcn with figure'] += 1
                if float(m.group(1)) < float(m.group(2)): c[b, 'jcn joint below lead alone'] += 1
            if 'CHANGED' in s:
                mm = re.search(r"CHANGED: ([+-][\d.]+) VP v ([+-][\d.]+) VP instead of its own fight alone", s)
                if mm and float(mm.group(1)) < float(mm.group(2)): c[b, 'jcn row: joiner below its own fight alone'] += 1
        elif tag == 'JOINT ON THE TABLE':
            c[b, 'jot rows'] += 1
            m = JOT.search(s)
            if m and m.group(1) in decl[(x['turn'], x['side'], m.group(3))]: c[b, 'jot friend behind charged the same target'] += 1
        elif tag == 'MOVE ORDER':
            c[b, 'move order rows'] += 1
            if 'crosses the ground' in s: c[b, 'move order: crossing paths'] += 1
            if 'ends in the path' in s: c[b, 'move order: ends in a path'] += 1
        elif tag == 'THE DEARER SUM KEEPS ITS PLAN':
            c[b, 'dearer sum rows'] += 1
            if 'gives way' in s: c[b, 'dearer: a friend gives way (same ground)'] += 1
            if 'line of fire' in s: c[b, 'dearer: in a line of fire'] += 1
        elif tag == 'BLOCKED CHARGE SKIPPED':
            c[b, 'blocked charge skipped (friend in the way of landing)'] += 1
        elif tag == 'BLOCKED CHARGE HANDED OVER':
            c[b, 'blocked charge handed over'] += 1
        elif tag in ('ARMY TABLE', 'HOLDER ASSIGNMENT', 'CHARGE LIST READ AGAIN', 'SET FIGHT', 'JOINT KNOWS CHALLENGE', 'AFTERMATH WITH FRIENDS'):
            c[b, tag.lower() + ' rows'] += 1
print(f"GAMES {games}; minutes a game (whole game, both sides) mean {sum(mins)/len(mins):.1f} (n {len(mins)})")
keys = sorted({k for _, k in c})
print('| | ON a game | OFF a game | ON count | OFF count |\n|---|---|---|---|---|')
for k in keys: print(f"| {k} | {c['ON',k]/games:.2f} | {c['OFF',k]/games:.2f} | {c['ON',k]} | {c['OFF',k]} |")
