#!/usr/bin/env python3
"""FAR MARKERS, ON v OFF. python3 -I far.py <root with <arm>-N/<batch>/game-*.log.jsonl>
For each side at the start of each of its own turns: a marker is 'far' when no non-character unit of that side on the table can get
within 6" of it in one move (reach = the longest single-turn move that unit made in the game, centre to centre: an empirical march).
Counts: markers far for a side at its first turn, and whether that side ever scored it (all game); same for markers far at EVERY own turn start."""
import sys, glob, json, os, math, collections
R = sys.argv[1]; C = collections.Counter()
for f in glob.glob(os.path.join(R, '*/*/game-*.log.jsonl')):
    arm = os.path.relpath(f, R).split('/')[0]; new = 'Mine' if arm.startswith('mine') else 'Opponent'
    L = open(f).readlines(); b = json.loads(L[0]); mk = b.get('markers') or []
    if not isinstance(mk, list) or not mk: continue
    side = {u['id']: u['s'] for u in b['units']}; char = {u['id'] for u in b['units'] if (u.get('lk') or {}).get('tt') == 'Character'}
    pos = {}; turnof = {}; starts = collections.OrderedDict(); scored = collections.defaultdict(set)
    cur = None; snap = {}; reach = collections.Counter(); tstart = {}
    for l in L[1:]:
        d = json.loads(l); k = d['kind']
        if k == 'action' and d.get('turn'):
            key = (d['turn'], d['side'])
            if key != cur:
                if cur:  # close previous turn: displacement of that side's units
                    for u, p in pos.items():
                        if side.get(u) == cur[1] and u in tstart and p[2]: reach[u] = max(reach[u], math.dist(p[:2], tstart[u][:2]))
                cur = key; tstart = dict(pos); starts[key] = dict(pos)
        if k == 'action' and d.get('to') and d['to'][0] is not None and d.get('actor_id'):
            on = pos.get(d['actor_id'], (0, 0, 1))[2]; pos[d['actor_id']] = (d['to'][0], d['to'][1], on)
        elif k == 'frame':
            for u in d['units']: pos[u['id']] = (u['x'], u['y'], u['on'])
        elif k == 'objective' and d['objective'] == 'StrategicLocation': scored[d['side']].add(d['index'])
    for s in ('Mine', 'Opponent'):
        arm_ = 'on' if s == new else 'off'; own = [k for k in starts if k[1] == s]
        if not own: continue
        def far_at(k, i):
            m = mk[i]
            return all(math.dist(p[:2], (m['x'], m['y'])) - 6 > reach[u] for u, p in starts[k].items() if side.get(u) == s and u not in char and p[2])
        for i in range(len(mk)):
            C[arm_, 'markers'] += 1
            if far_at(own[0], i):
                C[arm_, 'far1'] += 1; C[arm_, 'far1_empty'] += i not in scored[s]
                if all(far_at(k, i) for k in own): C[arm_, 'farall'] += 1
            else: C[arm_, 'near1'] += 1; C[arm_, 'near1_empty'] += i not in scored[s]
    C['games'] += 1
print(f"games with markers {C['games']}")
print("| | ON side | OFF side |\n| --- | --- | --- |")
for lab, a, b_ in (("Markers far at own first turn (share of side-markers)", 'far1', 'markers'), ("  of those, never scored by that side all game", 'far1_empty', 'far1'),
                   ("  of those, far at EVERY own turn start", 'farall', 'far1'), ("Markers in reach at first turn: never scored all game", 'near1_empty', 'near1')):
    print(f"| {lab} | " + " | ".join(f"{C[x,a]/max(C[x,b_],1):.0%} ({C[x,a]}/{C[x,b_]})" for x in ('on', 'off')) + " |")
