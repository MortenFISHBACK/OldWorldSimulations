#!/usr/bin/env python3
"""Joint charges batch A (2026-11-18): ON (joint-charge-now + aftermath-with-friends) v OFF, claimed v happened.
    python3 -I joint.py <root holding <arm>-N/<batch>/game-*.log.jsonl> <charges.pkl from build.py>
A charge is ALONE when it is the only charge declared on that target in that player turn, else LEAD (first declared) or SECOND (later).
Ready pair: two or more units of a side had a charge on the same target among their weighed options (JOB SPLIT / CANDIDATES JOB) that turn.
"""
import collections, glob, json, os, pickle, re, sys
ROOT, PKL = sys.argv[1], sys.argv[2]
R = pickle.load(open(PKL, 'rb'))
m = lambda v: sum(v) / len(v) if v else float('nan')
JROW = re.compile(r"^JOINT CHARGE NOW: ([+-][\d.]+) VP: charge #(\d+) .*?\| (brings|joins) (.*?) on #\d+ .*?all in (\d+)%, first round won (\d+)% together \(alone (\d+)%\), kills ~(-?[\d.]+), own losses ~(-?[\d.]+)")
OPT = re.compile(r"\d+\. charge #(\d+)")
games = 0
ready = {'ON': collections.Counter(), 'OFF': collections.Counter()}
jrows = {'ON': [], 'OFF': []}
for f in sorted(glob.glob(ROOT + '/**/game-*.log.jsonl', recursive=True)):
    arm = os.path.relpath(f, ROOT).split('/')[0].split('-')[0]
    on = 'Mine' if arm == 'mine' else 'Opponent'
    br = lambda s: 'ON' if s == on else 'OFF'
    games += 1
    offers = collections.defaultdict(set)   # (turn, side, target) -> units
    decl = collections.defaultdict(set)
    for line in open(f, encoding='utf-8'):
        if not line.startswith('{'): continue
        x = json.loads(line)
        if x.get('kind') != 'action': continue
        s = x.get('summary') or ''; t = x.get('type')
        if t == 'JobSplit' and s.startswith('JOB SPLIT') or t == 'Candidates' and s.startswith('CANDIDATES JOB'):
            for T in OPT.findall(s): offers[(x['turn'], x['side'], int(T))].add(x['actor_id'])
        elif t == 'Computer' and ' does not charge #' in s:
            for T in re.findall(r"#(\d+)", s): offers[(x['turn'], x['side'], int(T))].add(x['actor_id'])
        elif t == 'Charge' and 'declares a charge' in s:
            decl[(x['turn'], x['side'], x['target_id'])].add(x['actor_id'])
        elif t == 'OpponentRule' and s.startswith('JOINT CHARGE NOW'):
            mm = JROW.match(s)
            if mm: jrows[br(x['side'])].append(dict(file=(os.path.basename(os.path.dirname(f)), os.path.basename(f)), turn=x['turn'], side=x['side'], A=x['actor_id'], T=int(mm.group(2)), kind=mm.group(3),
                partner=mm.group(4), allin=int(mm.group(5)) / 100, win=int(mm.group(6)) / 100, alone=int(mm.group(7)) / 100, kills=float(mm.group(8)), losses=float(mm.group(9))))
    for k, us in offers.items():
        if len(us) < 2: continue
        b = br(k[1]); ready[b]['ready'] += 1
        d = decl.get(k, set()) & us
        ready[b]['both' if len(d) >= 2 else 'one' if d else 'none'] += 1
G = games
# charges: group by set
sets = collections.defaultdict(list)
for c in R: sets[((c['batch'], c['file']), c['side'], c['turn'], c['T0'])].append(c)
role = {}
for k, cs in sets.items():
    cs.sort(key=lambda c: c['i'])
    for n, c in enumerate(cs): c['role'] = 'alone' if len(cs) == 1 else 'lead' if n == 0 else 'second'
br2 = lambda c: 'OFF' if c['simpler'] else 'ON'
cnt = {'ON': collections.Counter(), 'OFF': collections.Counter()}
for c in R: cnt[br2(c)][c['role']] += 1
print(f"GAMES {G}\n## Charges a game (declared)\n| | ON | OFF |\n|---|---|---|")
for r in ('alone', 'lead', 'second'): print(f"| {r} | {cnt['ON'][r]/G:.2f} | {cnt['OFF'][r]/G:.2f} |")
print(f"| all | {sum(cnt['ON'].values())/G:.2f} | {sum(cnt['OFF'].values())/G:.2f} |")
# first round won + net per fight, alone v joint (per set)
print("\n## Fights (contact made): first round won claimed v happened; net points over 2 turns (target lost - all chargers lost)")
print("| | n ON | won claimed v happened ON | net ON | n OFF | won claimed v happened OFF | net OFF |\n|---|---|---|---|---|---|---|")
jidx = {}
for b in ('ON', 'OFF'):
    for j in jrows[b]: jidx.setdefault((j['file'], j['side'], j['turn'], j['T']), []).append(j)
out = {}
for b in ('ON', 'OFF'):
    for kind in ('alone', 'joint'):
        cl, hp, net, n = [], [], [], 0
        for k, cs in sets.items():
            if br2(cs[0]) != b: continue
            if (kind == 'alone') != (len(cs) == 1): continue
            ct = [c for c in cs if c['res'] == 'contact']
            if not ct or ct[0].get('r1') not in ('win', 'loss', 'draw'): continue
            n += 1
            hp.append(ct[0]['r1'] == 'win')
            if kind == 'alone': w = ct[0].get('win')
            else:
                js = jidx.get(k)
                w = js[0]['win'] if js else (max(c.get('win') or 0 for c in cs) or None)
            if w is not None: cl.append(w)
            net.append(max(c['t_2t'] for c in ct) - sum(c['a_2t'] for c in ct))
        out[(b, kind)] = (n, f"{100*m(cl):.0f} v {100*m(hp):.0f}", f"{m(net):+.0f}")
for kind in ('alone', 'joint'):
    a, o = out[('ON', kind)], out[('OFF', kind)]
    print(f"| {kind} | {a[0]} | {a[1]} | {a[2]} | {o[0]} | {o[1]} | {o[2]} |")
print("(joint claim ON = the JOINT CHARGE NOW set figure where a row exists; OFF = best single unit's own figure)")
# JOINT CHARGE NOW rows
print("\n## JOINT CHARGE NOW rows")
for b in ('ON', 'OFF'):
    rows = jrows[b]; claims = {}
    for j in rows: claims.setdefault((j['file'], j['side'], j['turn'], j['T']), []).append(j)
    both = made = 0; cw, hw = [], []
    for k, js in claims.items():
        cs = sets.get(k, [])
        units = {j['A'] for j in js}
        dec = {c['A'] for c in cs}
        con = {c['A'] for c in cs if c['res'] == 'contact'}
        if len(dec & units) >= 2 or len(dec) >= 2: made += 1
        if len(con) >= 2: both += 1
        ct = [c for c in cs if c['res'] == 'contact' and c.get('r1') in ('win', 'loss', 'draw')]
        if len(con) >= 2 and ct: cw.append(js[0]['win']); hw.append(ct[0]['r1'] == 'win')
    print(f"{b}: rows {len(rows)} ({len(rows)/G:.2f} a game), sets claimed {len(claims)}, two+ declared {made}, two+ made contact {both}"
          + (f"; all in claimed {100*m([js[0]['allin'] for js in claims.values()]):.0f}% v both in {100*both/len(claims):.0f}%" if claims else '')
          + (f"; first round won (both in) claimed {100*m(cw):.0f} v {100*m(hw):.0f} (n {len(cw)})" if cw else ''))
print("\n## Ready pairs (2+ units with a charge on the same target in their weighed options, that turn)")
print("| | ON | OFF |\n|---|---|---|")
for k in ('ready', 'both', 'one', 'none'):
    print(f"| {k} | {ready['ON'][k]} ({ready['ON'][k]/G:.2f}/game) | {ready['OFF'][k]} ({ready['OFF'][k]/G:.2f}/game) |")
print("\n## Net points per charged fight, claimed v happened (mean)")
for b in ('ON', 'OFF'):
    al = [(c.get('gain'), c['t_2t'] - c['a_2t']) for k, cs in sets.items() if len(cs) == 1 for c in cs if br2(c) == b and c['res'] == 'contact' and c.get('gain') is not None]
    print(f"{b} alone: pick gain claimed {m([a for a,_ in al]):+.0f} VP v net {m([h for _,h in al]):+.0f} (n {len(al)})")
    js = []
    for k, rows in {(j['file'], j['side'], j['turn'], j['T']): j for j in jrows[b]}.items():
        cs = [c for c in sets.get(k, []) if c['res'] == 'contact']
        if cs: js.append((rows['kills'] - rows['losses'], max(c['t_2t'] for c in cs) - sum(c['a_2t'] for c in cs)))
    if js: print(f"{b} joint (JOINT CHARGE NOW sets): kills - own losses claimed {m([a for a,_ in js]):+.0f} v net {m([h for _,h in js]):+.0f} (n {len(js)})")
