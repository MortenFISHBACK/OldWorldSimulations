#!/usr/bin/env python3
"""Holders batch 4 reading. python3 -I a4.py <root with <arm>-N/<batch>/game-*>"""
import sys, glob, os, re, json, collections, statistics as st, csv
R = sys.argv[1]
def side_new(arm): return 'Mine' if arm.startswith('mine') else 'Opponent'
games = []; mins = []
for g in glob.glob(os.path.join(R, '*/*/games.csv')):
    arm = os.path.relpath(g, R).split('/')[0]; new = side_new(arm)
    for r in csv.DictReader(open(g)):
        if r['ended'] != 'True' and r['ended'] != 'true' and not r['vp_mine_opponent']: continue
        try: m, o = [int(x) for x in r['vp_mine_opponent'].split('-')] if '-' in r['vp_mine_opponent'] else [int(x) for x in r['vp_mine_opponent'].split('/')]
        except Exception: continue
        d = m - o if new == 'Mine' else o - m
        games.append((arm, r['pair'], d)); mins.append(float(r['minutes'] or 0))
n = len(games); ds = [d for *_, d in games]
if n:
    se = st.pstdev(ds) / n ** .5
    print(f"games {n}: VP margin new-old {st.mean(ds):+.0f} ±{1.96*se:.0f} (won {sum(d>0 for d in ds)}, lost {sum(d<0 for d in ds)}, drawn {sum(d==0 for d in ds)})")
    print(f"minutes a game {st.mean(mins):.1f}, longest {max(mins):.1f}")
# switch side check + rows
TAGS = ('HOLDER ASSIGNMENT', 'HOLD ODDS', 'QUARTER ODDS')
bad = []; rows = collections.Counter()
QA = re.compile(r'QUARTER ODDS: \\u002B([\d.]+) VP|QUARTER ODDS: ([\-\d.]+) VP')
def quad(x, y):
    return ('Top' if y < 24 else 'Bottom') + '-' + ('left' if x < 36 else 'right')
qc = collections.Counter(); out = collections.Counter(); qg = 0
bag = collections.Counter(); bagclaim = collections.defaultdict(list)
BAGRX = re.compile(r"HOLDER ASSIGNMENT: (Mine|Opponent)\\u0027s baggage train goes to (.+?) \(holds it this turn: gives up ~[\d.\-]+ VP of its other options for the ~([\d.]+) VP")
for f in glob.glob(os.path.join(R, '*/*/game-*.log.jsonl')):
    arm = os.path.relpath(f, R).split('/')[0]; new = side_new(arm); old = 'Opponent' if new == 'Mine' else 'Mine'
    t = f[:-len('.log.jsonl')] + '.txt'
    if not os.path.exists(t): continue
    head = open(t).read().split('\n')[:12]
    if not any('result:' in x for x in head): continue
    c = collections.Counter(); pos = {}; qrows = []; brows = []
    for l in open(f):
        if '"to":[' in l and '"actor_id"' in l:
            try: d = json.loads(l)
            except Exception: continue
            to = d.get('to') or [None]
            if to and to[0] is not None and d.get('actor_id'): pos[d['actor_id']] = (to[0], to[1])
            s = d.get('summary') or ''
            for tg in TAGS:
                if s.startswith(tg + ':'): c[(tg, d['side'])] += 1
            if s.startswith('QUARTER ODDS:'):
                m = re.match(r'QUARTER ODDS: \+?([\-\d.]+) VP', s)
                if m and d.get('turn', 0) >= 5: qrows.append((d['side'], d['actor_id'], float(m.group(1)), d.get('turn')))
            if 'baggage train goes to' in s and d.get('turn', 0) >= 5:
                for mm in re.finditer(r"(Mine|Opponent)'s baggage train goes to (.+?) \(holds it this turn: gives up ~[\d.\-]+ VP of its other options for the ~([\d.]+) VP", s):
                    brows.append((d['side'], mm.group(1), float(mm.group(3)), d.get('turn')))
    for (tg, sd), k in c.items():
        rows[(tg, 'new' if sd == new else 'old')] += k
        if sd != new: bad.append((f, tg, sd, k))
    # end outcomes per side
    res = {}
    for x in head:
        m = re.match(r'\s+(Mine|Opponent): [\d,]+ VP = (.*)', x)
        if m: res[m.group(1)] = m.group(2)
    dom = 'domination True' in head[2]
    if dom:
        qg += 1
        for sd in ('Mine', 'Opponent'):
            k = 'new' if sd == new else 'old'
            for it in re.finditer(r'(\w+-\w+) quarter Domination: controlled at the end of the battle, Unit Strength (\d+) to (\d+)([^;]*?) (\d+)(?:;|$)', res.get(sd, '')):
                out[(k, 'controlled')] += 1
                if 'more than twice' in it.group(4): out[(k, 'more than twice')] += 1
                if 'uncontested' in it.group(4): out[(k, 'uncontested')] += 1
                out[(k, 'VP')] += int(it.group(5))
        # claim proxy: last QUARTER ODDS row per unit (round 5+, positive), unit's final spot quarter, outcome for its side
        last = {}
        for sd, uid, vp, tn in qrows: last[uid] = (sd, vp, tn)
        for uid, (sd, vp, tn) in last.items():
            if vp <= 0 or uid not in pos: continue
            q = quad(*pos[uid]); txt = res.get(sd, '')
            m = re.search(re.escape(q) + r' quarter Domination: controlled at the end of the battle, Unit Strength \d+ to \d+([^;]*)', txt)
            qc['claims'] += 1; qc['claimed VP'] += vp
            if m:
                qc['controlled'] += 1
                if 'more than twice' in m.group(1): qc['more than twice'] += 1
                if 'uncontested' in m.group(1): qc['uncontested'] += 1
    # baggage claim v scored (last round-5+ assignment per side)
    lastb = {}
    for sd, owner, vp, tn in brows: lastb[(sd, owner)] = vp
    for (sd, owner), vp in lastb.items():
        k = 'new' if sd == new else 'old'
        held = re.search(owner + r"'s baggage train Baggage Trains: controlled at the end of the battle by [^;]*? (\d+)(?:;|$)", res.get(sd, ''))
        bag[(k, 'claims')] += 1; bag[(k, 'claimed')] += vp; bag[(k, 'scored')] += int(held.group(1)) if held else 0
print('rule rows (new / old side):', {tg: (rows[(tg, 'new')], rows[(tg, 'old')]) for tg in TAGS})
print('wrong-side rows:', len(bad), bad[:5])
print(f'Domination games {qg}: quarters a game  new: controlled {out[("new","controlled")]/max(qg,1):.2f}, more than twice {out[("new","more than twice")]/max(qg,1):.2f}, uncontested {out[("new","uncontested")]/max(qg,1):.2f}, VP {out[("new","VP")]/max(qg,1):.0f}'
      f' | old: controlled {out[("old","controlled")]/max(qg,1):.2f}, more than twice {out[("old","more than twice")]/max(qg,1):.2f}, uncontested {out[("old","uncontested")]/max(qg,1):.2f}, VP {out[("old","VP")]/max(qg,1):.0f}')
k = max(qc['claims'], 1)
print(f"quarter claims (unit's last QUARTER ODDS row round 5+, gain>0; its final spot's quarter): {qc['claims']} units, avg claimed +{qc['claimed VP']/k:.0f} VP; quarter ended controlled {qc['controlled']/k:.0%}, more than twice {qc['more than twice']/k:.0%}, uncontested {qc['uncontested']/k:.0%}")
for kk in ('new', 'old'):
    b = max(bag[(kk, 'claims')], 1)
    print(f"baggage {kk}: {bag[(kk,'claims')]} last-round-5+ holds, claimed avg {bag[(kk,'claimed')]/b:.0f}, scored avg {bag[(kk,'scored')]/b:.0f}")
