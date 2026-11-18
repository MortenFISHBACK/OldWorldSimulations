#!/usr/bin/env python3
"""Claimed against happened, per brain (ON = worked-out chances, OFF = simpler pricing), for the worked-out-chances batch 2026-11-17.
Morten 2026-11-17: odds first, VP second. Turn windows from the corrected job_claims.py (branch 6skrm4).
    python3 odds.py <root holding <arm>-N/<batch>/game-*.log.jsonl> <charges.pkl from build.py>
"""
import collections, glob, json, os, pickle, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import job_claims as jc

def _lost(g, u, start, end):
    if jc._gone(g, u["id"], start): return 0.0
    if jc._gone(g, u["id"], end): return float(u["vp"])
    m0, m1 = jc._models(g, u["id"], start), jc._models(g, u["id"], end)
    if m0 is None or m1 is None: return 0.0
    return max(0, m0 - m1) * u["points"] / max(1, u["mc"])
jc._lost = getattr(jc, "_lost", _lost)

ROOT, PKL = sys.argv[1], sys.argv[2]
JR = re.compile(r"^JOB RISK: (.+?): gain ([+-]?[\d.]+) VP, risk (-?[\d.]+) VP, worth ([+-]?[\d.]+) VP")
SH = {'SpellCast', 'SpellEffect', 'Shooting', 'WarMachineShot', 'BreathWeapon', 'ColumnOfFire', 'Zzzzap'}
m = lambda v: sum(v) / len(v) if v else float('nan')
R = collections.defaultdict(lambda: collections.defaultdict(list))
NG = 0
for f in sorted(glob.glob(ROOT + '/**/game-*.log.jsonl', recursive=True)):
    arm = os.path.relpath(f, ROOT).split('/')[0].split('-')[0]
    on_side = 'Mine' if arm == 'mine' else 'Opponent'
    br = lambda s: 'ON' if s == on_side else 'OFF'
    NG += 1
    g = jc.read_game(f)
    acts = [x for x in (json.loads(l) for l in open(f, encoding='utf-8') if l.strip()) if x.get('kind') == 'action']
    risk = {}
    for x in acts:
        if x.get('type') == 'JobRisk' and (mm := JR.match(x.get('summary') or '')):
            risk[(x['turn'], x['side'], x.get('actor'), mm.group(1))] = (float(mm.group(2)), float(mm.group(3)))
    for p in g['picks']:
        me = g['byname'].get((p['side'], p['unit']))
        if me is None: continue
        b = br(p['side'])
        body = next((x['summary'] for x in acts if x['id'] == p['i']), '')
        job = re.sub(r'^Objective for .+?: ', '', body).split(': ')[0]
        h = jc.happened(g, p)
        k = p['kind']
        if p['worth'] is not None: R[b][k + ' claimed'].append(p['worth'])
        if k == 'charge':
            if 'declared' in h: R[b]['charge declared'].append(h['declared'])
            if 'net' in h: R[b]['charge net'].append(h['net'])
        elif k == 'shoot':
            w = jc._window(g, p['i'], p['side'], 'this')
            T = next((i for i in p['ids'] if i in g['units'] and g['units'][i]['side'] != p['side']), None)
            if w and T:
                R[b]['shoot fired at target'].append(any(w[0] <= x['id'] < w[1] and x.get('actor_id') == me['id'] and x.get('type') in SH and x.get('target_id') == T for x in acts))
            if 'vp' in h: R[b]['shoot vp'].append(h['vp'])
        elif k in ('close-in', 'advance', 'turn') and 'followed' in h:
            R[b][k + ' followed'].append(h['followed'])
        elif k == 'hold' and 'vp' in h:
            R[b]['hold vp'].append(h['vp'])
        rk = risk.get((p['turn'], p['side'], p['unit'], job))
        if rk is not None:
            we = jc._window(g, p['i'], p['side'], 'enemy')
            if we:
                R[b]['risk claimed'].append(rk[1])
                R[b]['risk lost'].append(jc._lost(g, me, we[0], we[1]))
C = pickle.load(open(PKL, 'rb'))
for c in C:
    b = 'OFF' if c['simpler'] else 'ON'
    R[b]['declared charges'].append(1)
    R[b]['contact'].append(c['res'] == 'contact')
    if c['res'] == 'contact' and c.get('win') is not None and c.get('r1') in ('win', 'loss', 'draw'):
        R[b]['win claimed'].append(c['win']); R[b]['win happened'].append(c['r1'] == 'win')
    if c['res'] == 'contact': R[b]['net per fight'].append(c['t_2t'] - c['a_2t'])


def row(label, f):
    print(f"| {label} | {f('ON')} | {f('OFF')} |")


ng = NG  # each brain plays every game once
print(f"{NG} games, each brain on one side of every game.\n")
print("| Odds: claimed v happened | Worked-out chances (ON) | Simpler (OFF) |\n| --- | --- | --- |")
row('Charge picks a game', lambda b: f"{len(R[b]['charge declared'])/ng:.1f}")
row('Charge picks declared that turn', lambda b: f"{m(R[b]['charge declared']):.0%}")
row('Charges declared a game', lambda b: f"{len(R[b]['declared charges'])/ng:.1f}")
row('Declared charges that made contact', lambda b: f"{m(R[b]['contact']):.0%}")
row('Win first round: claimed v happened', lambda b: f"{m(R[b]['win claimed']):.0%} v {m(R[b]['win happened']):.0%}")
row('Charge pick: claimed VP v net points 2 turns', lambda b: f"{m(R[b]['charge claimed']):.0f} v {m(R[b]['charge net']):+.0f}")
row('Net points per charged fight (contact)', lambda b: f"{m(R[b]['net per fight']):+.0f}")
row('Shoot picks a game', lambda b: f"{len(R[b]['shoot fired at target'])/ng:.1f}")
row('Shoot picks that fire at their target', lambda b: f"{m(R[b]['shoot fired at target']):.0%}")
row('Shoot pick: claimed VP v VP of wounds done', lambda b: f"{m(R[b]['shoot claimed']):.0f} v {m(R[b]['shoot vp']):.0f}")
row('Close in: claimed VP; charged that target next turn', lambda b: f"{m(R[b]['close-in claimed']):.0f}; {m(R[b]['close-in followed']):.0%}")
row('Advance: claimed VP; charged that target next turn', lambda b: f"{m(R[b]['advance claimed']):.0f}; {m(R[b]['advance followed']):.0%}")
row('Hold: claimed VP v scored', lambda b: f"{m(R[b]['hold claimed']):.0f} v {m(R[b]['hold vp']):.0f}")
row('Risk of picked jobs a game: claimed v points lost next enemy turn', lambda b: f"{sum(R[b]['risk claimed'])/ng:.0f} v {sum(R[b]['risk lost'])/ng:.0f}")
