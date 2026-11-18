#!/usr/bin/env python3
"""Risk gap evidence (one-figure batch, 2026-11-17). python3 -I risk.py <root with <arm>-N/<batch>/game-*.log.jsonl>
1. Picked jobs: claimed risk (JOB RISK row of the taken job; new side split D = enemy charges / shots / lost-charge) v points the unit
   actually lost in the enemy turn that follows, by job kind, and the loss split by what hit the unit in that enemy turn
   (charged = an enemy charge on it or it fought in combat; shot = shooting/war machine/breath; magic = spells; none seen).
2. Passed-over charges (new side): the split of gain (fight, wears-down, other-costs), after, and risk (charges, shots, lost-charge).
"""
import collections, glob, json, os, re, sys, statistics as stt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import job_claims as jc
if not hasattr(jc, '_lost'):
    def _lost(g, u, start, end):
        if jc._gone(g, u["id"], start): return 0.0
        if jc._gone(g, u["id"], end): return float(u["vp"])
        m0, m1 = jc._models(g, u["id"], start), jc._models(g, u["id"], end)
        if m0 is None or m1 is None: return 0.0
        return max(0, m0 - m1) * u["points"] / max(1, u["mc"])
    jc._lost = _lost
ROOT = sys.argv[1]
JR = re.compile(r"^JOB RISK: (.+?): gain ([+-]?[\d.]+) VP, risk (-?[\d.]+) VP, worth ([+-]?[\d.]+) VP")
DC = re.compile(r"\| D ([\d.]+): (?:charges ([\d.]+) .*?shots ([\d.]+) .*?lost-charge ([\d.]+))?")
SHOT = {'Shooting', 'WarMachineShot', 'BreathWeapon', 'ColumnOfFire', 'Zzzzap', 'StandAndShoot'}
MAG = {'SpellCast', 'SpellEffect'}
MEL = {'Charge', 'CombatAttack', 'ImpactHits', 'StompAttacks', 'Thunderous Impact'}
num = lambda s: float(s.replace('\\u002B', '+')) if s else 0.0
T = collections.defaultdict(lambda: collections.defaultdict(float)); N = collections.Counter(); NG = 0
PASS = []
for f in sorted(glob.glob(ROOT + '/*/*/game-*.log.jsonl')):
    arm = os.path.relpath(f, ROOT).split('/')[0].split('-')[0]; on = 'Mine' if arm == 'mine' else 'Opponent'
    NG += 1; g = jc.read_game(f)
    acts = [x for x in (json.loads(l) for l in open(f, encoding='utf-8') if l.strip()) if x.get('kind') == 'action']
    risk = {}
    for x in acts:
        s = (x.get('summary') or '').replace('\\u002B', '+')
        if x.get('type') == 'JobRisk' and (m := JR.match(s)):
            d = DC.search(s); comp = (num(d.group(2)), num(d.group(3)), num(d.group(4))) if d and d.group(2) else None
            risk[(x['turn'], x['side'], x.get('actor'), m.group(1))] = (float(m.group(3)), comp)
        if x.get('type') == 'JobSplit' and x['side'] == on:
            for p in s.split(' | ')[1:]:
                m = re.match(r'\d+\. charge #\d+ .*?: worth ([+-]?[\d.]+) = gain ([+-]?[\d.]+) \(fight ([+-]?[\d.]+), [a-z-]+ ([+-]?[\d.]+), other-costs ([+-]?[\d.]+).*?after ([+-]?[\d.]+)\) - risk ([\d.]+)(?: \(charges ([\d.]+) .*?shots ([\d.]+) .*?lost-charge ([\d.]+)\))?', p)
                if m and '[TAKEN]' not in p:
                    taken = next((q for q in s.split(' | ')[1:] if '[TAKEN]' in q), '')
                    PASS.append(dict(worth=float(m.group(1)), gain=float(m.group(2)), fight=float(m.group(3)), wears=float(m.group(4)), other=float(m.group(5)),
                                     after=float(m.group(6)), risk=float(m.group(7)), rc=num(m.group(8)), rs=num(m.group(9)), rl=num(m.group(10)),
                                     taken=(re.match(r'\d+\. ([a-z]+)', taken) or [None, '?'])[1], unit=x.get('actor'), file=os.path.basename(f), turn=x['turn']))
    for p in g['picks']:
        me = g['byname'].get((p['side'], p['unit']))
        if me is None: continue
        b = 'new' if p['side'] == on else 'simpler'
        body = next((x['summary'] for x in acts if x['id'] == p['i']), '').replace('\\u002B', '+')
        job = re.sub(r'^Objective for .+?: ', '', body).split(': ')[0]
        rk = risk.get((p['turn'], p['side'], p['unit'], job))
        we = jc._window(g, p['i'], p['side'], 'enemy')
        if rk is None or not we: continue
        lost = jc._lost(g, me, we[0], we[1])
        hit = {x.get('type') for x in acts if we[0] <= x['id'] < we[1] and x.get('target_id') == me['id']}
        cause = 'charged/fought' if hit & MEL else 'shot' if hit & SHOT else 'magic' if hit & MAG else 'other/none seen'
        if hit & SHOT and hit & MAG and not hit & MEL: cause = 'shot+magic'
        k = (b, p['kind']); N[k] += 1; T[k]['claimed'] += rk[0]; T[k]['lost'] += lost; T[k]['lost ' + cause] += lost; T[k]['n ' + cause] += 1
        if rk[1]:
            T[k]['c charges'] += rk[1][0]; T[k]['c shots'] += rk[1][1]; T[k]['c lost-charge'] += rk[1][2]
        T[k]['claimed>0'] += rk[0] > 0; T[k]['lost>0'] += lost > 0
        T[(b, 'ALL')]['claimed'] += rk[0]; T[(b, 'ALL')]['lost'] += lost; N[(b, 'ALL')] += 1; T[(b, 'ALL')]['lost ' + cause] += lost
        if rk[1]:
            for i, nm in enumerate(('charges', 'shots', 'lost-charge')): T[(b, 'ALL')]['c ' + nm] += rk[1][i]
print(f"{NG} games\n\n## 1. Risk of the picked job: claimed v points lost in the enemy turn after (per game)\n")
print("| Side | Job | picks | claimed risk | lost | claimed: enemy charges / shots / lost-charge | lost when charged-fought / shot / magic / other |")
print("| --- | --- | --- | --- | --- | --- | --- |")
for k in sorted(N, key=lambda k: (k[0], -N[k])):
    t = T[k]; pg = lambda v: f"{v/NG:.0f}"
    print(f"| {k[0]} | {k[1]} | {N[k]} | {pg(t['claimed'])} | {pg(t['lost'])} | {pg(t['c charges'])} / {pg(t['c shots'])} / {pg(t['c lost-charge'])} | "
          f"{pg(t['lost charged/fought'])} / {pg(t['lost shot']+t['lost shot+magic'])} / {pg(t['lost magic'])} / {pg(t['lost other/none seen'])} |")
print("\n(simpler side logs only the total risk, no split; 'other' = lost with no enemy action on the unit logged, e.g. panic, flee, combat it was already in)\n")
print(f"## 2. Passed-over charges, new side ({len(PASS)} options not taken)\n")
if PASS:
    md = lambda key, rows: f"{stt.median([r[key] for r in rows]):+.1f}"
    sm = lambda key, rows: f"{sum(r[key] for r in rows)/len(rows):+.1f}"
    print("| Term | median | mean |\n| --- | --- | --- |")
    for key in ('worth', 'gain', 'fight', 'wears', 'other', 'after', 'risk', 'rc', 'rs', 'rl'):
        print(f"| {dict(rc='risk: enemy charges', rs='risk: shots', rl='risk: lost-charge', wears='second term (wears-down / kills-count / together)', other='other-costs').get(key, key)} | {md(key, PASS)} | {sm(key, PASS)} |")
    pos_wo_after = sum(r['worth'] <= 0 and r['worth'] - r['after'] > 0 for r in PASS)
    pos_wo_risk = sum(r['worth'] <= 0 and r['worth'] + r['risk'] > 0 for r in PASS)
    print(f"\nAt or below zero: {sum(r['worth']<=0 for r in PASS)}; of those above zero without the 'after' term: {pos_wo_after}; above zero without the risk: {pos_wo_risk}; fight term alone above zero: {sum(r['worth']<=0 and r['fight']>0 for r in PASS)}")
    print("Picked instead:", dict(collections.Counter(r['taken'] for r in PASS).most_common()))
    import csv
    with open(os.path.join(ROOT, 'passed-over-charges.tsv'), 'w', newline='') as o:
        w = csv.DictWriter(o, fieldnames=list(PASS[0]), delimiter='\t'); w.writeheader(); w.writerows(PASS)
