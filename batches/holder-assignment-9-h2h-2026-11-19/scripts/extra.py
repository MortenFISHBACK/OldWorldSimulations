#!/usr/bin/env python3
"""Holders batch 2 extras. python3 -I extra.py <root with <arm>-N/<batch>/game-*.log.jsonl>
1) turn-table 'goes to' rows (Strategy): did the named unit score that objective that round, split holds-it-this-turn / walks-on.
2) units ending their own player turn within 6" of their OWN baggage train (nearest model base edge to the train's rectangle), per game, ON v OFF.
"""
import sys, glob, json, os, re, collections, html, math
R = sys.argv[1]
rx = re.compile(r'HOLDER ASSIGNMENT: (.+?) goes to (.+?) \((holds it this turn|walks on to it)')
hit = collections.Counter(); bag = collections.Counter(); games = collections.Counter(); bag_r = collections.Counter()
def rect_dist(px, py, f):
    hw, hd = f['w']/2, f['d']/2
    if f.get('r'):
        a = -math.radians(f['r']); dx, dy = px-f['x'], py-f['y']; px, py = f['x']+dx*math.cos(a)-dy*math.sin(a), f['y']+dx*math.sin(a)+dy*math.cos(a)
    dx = max(abs(px-f['x'])-hw, 0); dy = max(abs(py-f['y'])-hd, 0); return math.hypot(dx, dy)
for f in glob.glob(os.path.join(R, '*/*/game-*.log.jsonl')):
    arm = os.path.relpath(f, R).split('/')[0]; new = 'Mine' if arm.startswith('mine') else 'Opponent'
    L = open(f).readlines(); b = json.loads(L[0])
    side_of = {u['id']: u['s'] for u in b['units']}; char = {u['id'] for u in b['units'] if (u.get('lk') or {}).get('tt') == 'Character'}
    trains = {t['f']['bag']: t['f'] for t in b['terrain'] if t['f'].get('bag')}
    obj = collections.defaultdict(set); acts = []; frames = []; pend = []
    for l in L[1:]:
        if l.startswith('{"kind":"objective"'):
            d = json.loads(l); obj[(d['turn'], d['side'], d['unit'])].add((d['objective'], d['index']))
        elif l.startswith('{"kind":"frame"'): frames.append(json.loads(l))
        elif l.startswith('{"kind":"action"'):
            d = json.loads(l); acts.append((d['id'], d['turn'], d['side']))
            if 'goes to' in l and 'HOLDER ASSIGNMENT' in l and d['phase'] == 'Strategy':
                m = rx.search(d['summary'])
                if not m: continue
                t = html.unescape(m.group(1)); mm = re.match(r'Marker (\d+)', t)
                if mm: want = ('StrategicLocation', int(mm.group(1))-1); k = 'marker'
                elif 'hill' in t.lower(): want = ('Hill', None); k = 'hill'
                else: continue
                how = 'holds' if m.group(3).startswith('holds') else 'walks on'
                pend.append((k, how, want, d['turn'], d['side'], html.unescape(m.group(2))))
    for k, how, want, t, sd, un in pend:
        got = obj.get((t, sd, un), set())
        h = any(o == want[0] and (want[1] is None or i == want[1]) for o, i in got)
        hit[(k, how, 'n')] += 1; hit[(k, how, 'hit')] += h
        g2 = obj.get((t+1, sd, un), set())
        hit[(k, how, 'next')] += any(o == want[0] and (want[1] is None or i == want[1]) for o, i in g2)
    games['all'] += 1
    if not trains: continue
    games['bag'] += 1
    # last action id of each own player turn
    last = {}
    for i, t, s in acts:
        if t and t >= 1: last[(t, s)] = max(last.get((t, s), 0), i)
    frames.sort(key=lambda x: x['after'])
    for (t, s), aid in last.items():
        if s not in trains: continue
        state = {}
        for x in frames:
            if x['after'] > aid: break
            for u in x['units']: state[u['id']] = u
        k = 'new' if s == new else 'old'
        for u in state.values():
            if side_of.get(u['id']) != s or not u.get('on') or u['id'] in char: continue
            d = min(rect_dist(p[0], p[1], trains[s]) for p in u['m']) - min(u['bw'], u['bd'])/2
            if d <= 6: bag[k] += 1; bag_r[(k, 'r1-4' if t <= 4 else 'r5+')] += 1
print("| Assigned to | How | Rows | Scored it that round | Scored it the next round |\n| --- | --- | --- | --- | --- |")
for k in ('marker', 'hill'):
    for how in ('holds', 'walks on'):
        n = hit[(k, how, 'n')]
        if n: print(f"| {k} | {how} | {n} | {hit[(k,how,'hit')]/n:.0%} | {hit[(k,how,'next')]/n:.0%} |")
g = games['bag']
print(f"games {games['all']}, with baggage trains {g}")
if g: print(f"units (not characters) ending own turn within 6\" of own baggage train, a game: ON {bag['new']/g:.1f}  OFF {bag['old']/g:.1f}  (rounds 1-4: {bag_r[('new','r1-4')]/g:.1f} v {bag_r[('old','r1-4')]/g:.1f})")
