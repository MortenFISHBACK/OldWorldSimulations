#!/usr/bin/env python3
"""Holders batch 6: marker walks claimed v happened (ON side).
python3 -I walks6.py <root with <arm>-N/.../game-*.log.jsonl>  (arm mine-* = Mine ON, opp-* = Opponent ON)"""
import sys, glob, os, re, json, collections, html, math, statistics as st
R = sys.argv[1]; C = collections.Counter(); L = collections.defaultdict(list)
WALK = re.compile(r"\[HOLD ODDS: Marker (\d+)[^-]*- arrives in (\d+) turns? (\d+)%([^\]]*)\]")
GOES = re.compile(r"HOLDER ASSIGNMENT: Marker (\d+)[^:]*? (?:goes to (.+?) \((holds it this turn|walks on to it)|stays empty)")
files = [f for f in glob.glob(os.path.join(R, '**/game-*.log.jsonl'), recursive=True)]
for j in files:
    arm = os.path.relpath(j, R).split('/')[0]; new = 'Opponent' if arm.startswith('opp') else 'Mine'
    rows = [json.loads(l) for l in open(j) if l.startswith('{')]
    board = next((r for r in rows if r.get('kind') == 'board'), None)
    if not board or not board.get('markers'): continue
    mk = {m['l']: (m['x'], m['y']) for m in board['markers']}
    acts = [r for r in rows if r.get('kind') == 'action']
    scored = collections.defaultdict(set)
    for r in rows:
        if r.get('kind') == 'objective' and r['objective'] == 'StrategicLocation': scored[(r['side'], r['index'])].add((r['turn'], r['unit']))
    ha = {}  # (turn, marker) -> (how, unit)
    for r in acts:
        if r.get('side') != new or r.get('phase') != 'Strategy' or r.get('type') != 'Computer': continue
        m = GOES.match(html.unescape(r.get('summary') or ''))
        if m: ha[(r['turn'], m.group(1))] = ('empty' if not m.group(2) else 'holds' if m.group(3).startswith('holds') else 'walks', html.unescape(m.group(2) or ''))
    claims = {}  # (turn, unit, marker) -> (N, p, text, actor_id)
    for r in acts:
        if r.get('side') != new or r.get('type') != 'OpponentRule': continue
        s = html.unescape(r.get('summary') or '')
        for m in WALK.finditer(s): claims[(r['turn'], html.unescape(r.get('actor') or ''), m.group(1))] = (int(m.group(2)), int(m.group(3)), m.group(4), r.get('actor_id'))
    C['games'] += 1
    for (tn, mkr), (how, unit) in ha.items():
        if how != 'walks': continue
        cl = claims.get((tn, unit, mkr))
        if not cl: C['walk rows without a claim'] += 1; continue
        N, p, rest, aid = cl
        late = 'a turn later' in rest; prom = 'WALK PROMISE' in rest
        k = 'far' if N >= 2 else 'near'
        C[k, 'n'] += 1; L[k, 'p'].append(p / 100); C[k, 'late claim'] += late; C[k, 'promise claim'] += prom
        # this turn's movement
        fr = to = None
        for q in acts:
            if q.get('turn') != tn or q.get('side') != new or q.get('actor_id') != aid or q.get('phase') != 'Movement': continue
            f, t = q.get('from'), q.get('to')
            if f and t and None not in f[:2] and None not in t[:2]:
                if fr is None: fr = f
                to = t
        if mkr in mk and fr:
            d0 = math.hypot(fr[0] - mk[mkr][0], fr[1] - mk[mkr][1]); d1 = math.hypot(to[0] - mk[mkr][0], to[1] - mk[mkr][1])
            L[k, 'closed'].append(d0 - d1); L[k, 'need'].append(max(d0 - 6, 0) / (N + 1)); C[k, 'closed the share'] += (d0 - d1) >= max(d0 - 6, 0) / (N + 1) - 0.5
        elif mkr in mk: C[k, 'did not move'] += 1; L[k, 'closed'].append(0)
        sc = scored.get((new, int(mkr) - 1), set())
        C[k, 'unit scored by claimed turn'] += any(u == unit and tn <= t2 <= tn + N for t2, u in sc)
        C[k, 'unit scored ever'] += any(u == unit and t2 >= tn for t2, u in sc)
        C[k, 'side scored by claimed turn'] += any(tn <= t2 <= tn + N for t2, u in sc)
        nx = ha.get((tn + 1, mkr))
        if nx is None: C[k, 'next: no row'] += 1
        elif nx[1] == unit: C[k, 'next: same unit ' + nx[0]] += 1
        elif nx[0] == 'empty': C[k, 'next: empty'] += 1
        else: C[k, 'next: passed to another unit'] += 1
        nc = claims.get((tn + 1, unit, mkr))
        if nc: C[k, 'next claim late'] += 'a turn later' in nc[2]; C[k, 'next claim promise'] += 'WALK PROMISE' in nc[2]; C[k, 'next claim N same or less than N-1'] += nc[0] <= N - 1
print(f"games with markers: {C['games']}; walk rows without a claim: {C['walk rows without a claim']}")
for k in ('near', 'far'):
    n = C[k, 'n']
    if not n: continue
    print(f"\n## {k} walks ({'arrives in 1 more turn' if k=='near' else 'arrives in 2+ more turns'}): {n}, claimed arrival {st.mean(L[k,'p'])*100:.0f}%; claim already late {C[k,'late claim']} (by WALK PROMISE {C[k,'promise claim']})")
    if L[k, 'closed']: print(f"  moved toward the marker this turn: median {st.median(L[k,'closed']):.1f}\" (share needed median {st.median(L[k,'need']) if L[k,'need'] else 0:.1f}\"); covered its share {C[k,'closed the share']} of {len(L[k,'closed'])}; no move {C[k,'did not move']}")
    print(f"  that unit scored it by the claimed turn {C[k,'unit scored by claimed turn']}, ever {C[k,'unit scored ever']}; the side scored it by the claimed turn {C[k,'side scored by claimed turn']}")
    print("  next turn's table row: " + ', '.join(f"{x.split(': ')[1]} {C[k,x]}" for x in sorted({kk[1] for kk in C if isinstance(kk, tuple) and kk[0]==k and kk[1].startswith('next: ')})))
    print(f"  next turn's claim by the same unit: late {C[k,'next claim late']} (WALK PROMISE {C[k,'next claim promise']}), on pace (N fell by 1+) {C[k,'next claim N same or less than N-1']}")
