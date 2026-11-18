#!/usr/bin/env python3
"""Holders batch 5 (feature/Herdstone/far markers by the odds): claimed v happened.
python3 -I a5.py <root with <arm>-N/<batch>/game-*>   (arm mine-* = Mine ON, opp-* = Opponent ON)"""
import sys, glob, os, re, json, collections, html, statistics as st
R = sys.argv[1]
C = collections.Counter(); L = collections.defaultdict(list)
GOES = re.compile(r"HOLDER ASSIGNMENT: (.+?) (?:goes to (.+?) \((holds it this turn|walks on to it)|stays empty)")
BR = re.compile(r"\[HOLD ODDS: ([^\]]*)\]")
QBR = re.compile(r"\[QUARTER ODDS: (\S+-\S+) quarter at the end of the battle with it there \(still there then (\d+)%\): controlled (\d+)%, more than twice the enemy (\d+)%, uncontested (\d+)%; without it (\d+)%, (\d+)%, (\d+)%")
def endclaim(t):
    """claimed end VP and chance from a HOLD ODDS bracket about an end-of-battle objective, else None"""
    m = re.search(r"(\d+) VP at the end of the battle if it (?:is still played then and it holds it|still holds it then), (\d+)%", t)
    if not m: return None
    a = re.search(r"arrives in (\d+) turns? (\d+)%", t); pa = int(a.group(2))/100 if a else 1.0
    return int(m.group(1)), pa * int(m.group(2))/100, (int(a.group(1)) if a else 0)
def norm(o):
    o = html.unescape(o)
    if o.startswith('The special feature'): return 'feature'
    if o.startswith('Herdstone'): return 'herdstone'
    if 'baggage train' in o: return 'bag:' + o.split("'")[0]
    if o.startswith('Marker'): return 'marker:' + re.match(r'Marker (\d+)', o).group(1)
    if 'hill' in o.lower(): return 'hill'
    return o
for t in glob.glob(os.path.join(R, '*/*/game-*.txt')):
    arm = os.path.relpath(t, R).split('/')[0]; new = 'Mine' if arm.startswith('mine') else 'Opponent'; old = 'Opponent' if new == 'Mine' else 'Mine'
    txt = open(t, errors='ignore').read(); head = txt.split('\n')[:12]
    if not any('result:' in x for x in head): continue
    j = t[:-4] + '.log.jsonl'
    if not os.path.exists(j): continue
    vp = {}
    for s in ('Mine', 'Opponent'):
        m = re.search(r'^\s*' + s + r': \d+ VP = (.*)$', txt, re.M); vp[s] = html.unescape(m.group(1)) if m else ''
    endctl = {}  # objective -> (side, unit)
    for s in ('Mine', 'Opponent'):
        for m in re.finditer(r"(The special feature|Herdstone|Mine's baggage train|Opponent's baggage train) [A-Za-z ]+: (?:the Herdstone )?controlled at the end of the battle by (.+?) \d+(?:;|$)", vp[s]):
            endctl[norm(m.group(1))] = (s, m.group(2))
    quarters = {}  # (side, quarter) -> set of outcomes
    for s in ('Mine', 'Opponent'):
        for m in re.finditer(r"(\S+-\S+) quarter Domination: controlled at the end of the battle[^;]*", vp[s]):
            o = {'controlled'}; x = m.group(0)
            if 'uncontested' in x: o.add('uncontested')
            if 'more than twice' in x: o.add('twice')
            quarters[(s, m.group(1))] = o
    lastrow = {}; odds = {}; qlast = {}; marker_walks = []; scored = collections.defaultdict(set)
    has = set(); lastrow_at = {}
    for l in open(j):
        if l.startswith('{"kind":"objective"'):
            d = json.loads(l); scored[(d['side'], d['objective'], d['index'])].add((d['turn'], d['unit'])); continue
        if 'HOLD ODDS' not in l and 'HOLDER ASSIGNMENT' not in l and 'QUARTER ODDS' not in l: continue
        d = json.loads(l); s = d.get('summary') or ''; tn = d.get('turn') or 0
        if d.get('side') != new: continue
        if d.get('phase') == 'Strategy' and s.startswith('HOLDER ASSIGNMENT:') and d.get('type') == 'Computer':
            m = GOES.match(s)
            if m:
                o = norm(m.group(1)); has.add(o)
                how = 'empty' if not m.group(2) else ('holds' if m.group(3).startswith('holds') else 'walks')
                lastrow[o] = (tn, how, html.unescape(m.group(2) or ''))
                if o.startswith('marker') and how == 'walks': marker_walks.append((o, tn, html.unescape(m.group(2))))
                if how != 'empty': lastrow_at[(o, tn)] = html.unescape(m.group(2))
        if d.get('type') == 'OpponentRule':
            for m in BR.finditer(s): odds[(tn, html.unescape(d.get('actor') or ''))] = m.group(1)
            for m in QBR.finditer(s):
                if tn >= 5: qlast[html.unescape(d.get('actor') or '')] = (tn, m.groups())
    # end-of-battle objectives
    for o in ('feature', 'herdstone'):
        if o not in has and o not in endctl: continue
        C[o, 'games'] += 1; who = endctl.get(o, (None,))[0]
        C[o, 'ON' if who == new else 'OFF' if who == old else 'nobody'] += 1
        if o in lastrow:
            tn, how, unit = lastrow[o]; key = (o, how)
            C[key, 'n'] += 1; won = who == new; C[key, 'won'] += won
            cl = endclaim(odds.get((tn, unit), '')) if how != 'empty' else None
            if cl: L[key, 'claim'].append(cl[0] * cl[1]); L[key, 'got'].append(cl[0] if won else 0); L[key, 'p'].append(cl[1])
            if how == 'walks' and tn >= 4: C[o, 'walk4', 'n'] += 1; C[o, 'walk4', 'won'] += won
            if how == 'holds' and not won and who == old:
                C[o, 'lost', 'n'] += 1; C[o, 'lost', 'alive'] += unit not in vp[old]
    # own baggage train, last row from round 5
    o = 'bag:' + new
    if o in lastrow and lastrow[o][0] >= 5 and lastrow[o][1] != 'empty':
        tn, how, unit = lastrow[o]; cl = endclaim(odds.get((tn, unit), '')); won = endctl.get(o, (None,))[0] == new
        C['bag', how, 'n'] += 1; C['bag', how, 'won'] += won
        if cl: L['bag', 'claim'].append(cl[0] * cl[1]); L['bag', 'got'].append(cl[0] if won else 0)
    # far markers: walk rows whose HOLD ODDS says arrives in 2+ turns
    for o, tn, unit in marker_walks:
        b = odds.get((tn, unit), ''); a = re.search(r'arrives in (\d+) turns? (\d+)%', b)
        if not a or int(a.group(1)) < 2: continue
        n = int(a.group(1)); idx = int(o.split(':')[1]) - 1
        sc = scored.get((new, 'StrategicLocation', idx), set())
        C['far', 'n'] += 1; L['far', 'pa'].append(int(a.group(2)) / 100)
        C['far', 'unit scored it'] += any(u == unit and t2 >= tn for t2, u in sc)
        C['far', 'unit scored it by the claimed turn'] += any(u == unit and tn <= t2 <= tn + n for t2, u in sc)
        C['far', 'side scored it later'] += any(t2 >= tn for t2, u in sc)
        C['far', 'side scored it by the claimed turn'] += any(tn <= t2 <= tn + n for t2, u in sc)
        C['far', 'same walk next turn'] += (o, tn + 1, unit) in set(marker_walks) or lastrow_at.get((o, tn + 1)) == unit
    # quarters: unit's last claim from round 5
    for unit, (tn, g) in qlast.items():
        q = g[0]; there = int(g[1]) / 100; w = [int(x) / 100 for x in g[2:5]]; wo = [int(x) / 100 for x in g[5:8]]
        got = quarters.get((new, q), set())
        for i, k in enumerate(('controlled', 'twice', 'uncontested')):
            L['q', k, 'claim'].append(there * w[i] + (1 - there) * wo[i]); L['q', k, 'got'].append(k in got)
    C['games'] += 1
def f(k): return f"{st.mean(L[k]):.0f}" if L[k] else '-'
print(f"games read {C['games']}")
for o in ('feature', 'herdstone'):
    g = C[o, 'games']
    if not g: continue
    print(f"\n## {o} ({g} games): ends with ON {C[o,'ON']}, OFF {C[o,'OFF']}, nobody {C[o,'nobody']}")
    for how in ('holds', 'walks', 'empty'):
        k = (o, how)
        if C[k, 'n']: print(f"  last table row '{how}': {C[k,'n']} games, ON held it at the end {C[k,'won']}; claimed {f((k,'claim'))} v scored {f((k,'got'))} VP; claimed chance {st.mean(L[k,'p'])*100 if L[k,'p'] else 0:.0f}%")
    print(f"  walk rows from round 4 as last row: {C[o,'walk4','n']}, held at the end {C[o,'walk4','won']}")
    print(f"  last row 'holds' and lost to the OFF side: {C[o,'lost','n']}, holder not in the enemy's VP list {C[o,'lost','alive']}")
print(f"\n## own baggage train, last row round 5+: holds {C['bag','holds','n']} (held at end {C['bag','holds','won']}), walks {C['bag','walks','n']} (held {C['bag','walks','won']}); claimed {f(('bag','claim'))} v scored {f(('bag','got'))}")
print(f"\n## far markers (walk rows saying 'arrives in 2+ turns'): {C['far','n']}, claimed arrival {st.mean(L['far','pa'])*100 if L['far','pa'] else 0:.0f}%; that unit scored it by the claimed turn {C['far','unit scored it by the claimed turn']}, ever after {C['far','unit scored it']}; ON side scored it by the claimed turn {C['far','side scored it by the claimed turn']}, later at all {C['far','side scored it later']}; same unit still sent to it next turn {C['far','same walk next turn']}")
print("\n## quarters (each unit's last QUARTER ODDS row from round 5)")
for k in ('controlled', 'twice', 'uncontested'):
    a = L['q', k, 'claim']; b = L['q', k, 'got']
    if a: print(f"  {k}: {len(a)} claims, claimed {st.mean(a)*100:.0f}% v happened {sum(b)/len(b)*100:.0f}%")
