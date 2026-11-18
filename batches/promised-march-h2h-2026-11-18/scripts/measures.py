#!/usr/bin/env python3
"""Worked-out chances batch (2026-11-17): per brain (ON = worked-out chances, OFF = simpler pricing)
- picked charges never declared that turn (gain-risk finding: 13%),
- shoot picks that never fire at the picked target that turn (finding: 32%), split: shot another enemy / no shot,
- shoot picks whose target a friend charged that turn (what SHOT OR CHARGE prices),
- CHARGE NOT DECLARED rows (always on) and SHOT OR CHARGE rows (ON side only).
Uses the corrected job_claims.py (turn-boundary fix, branch 6skrm4).
    python3 measures.py <root holding <arm>-N/<batch>/game-*.log.jsonl>
"""
import collections, glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import job_claims as jc

SH = {'SpellCast', 'SpellEffect', 'Shooting', 'WarMachineShot', 'BreathWeapon', 'ColumnOfFire', 'Zzzzap'}
ROOT = sys.argv[1]
C = collections.defaultdict(collections.Counter)
games = collections.Counter()
for f in sorted(glob.glob(ROOT + '/**/game-*.log.jsonl', recursive=True)):
    arm = os.path.relpath(f, ROOT).split('/')[0].split('-')[0]
    on_side = 'Mine' if arm == 'mine' else 'Opponent'
    br = lambda s: 'ON' if s == on_side else 'OFF'
    g = jc.read_game(f)
    games['ON'] += 1; games['OFF'] += 1
    acts = []
    for line in open(f, encoding='utf-8'):
        try: x = json.loads(line)
        except ValueError: continue
        if x.get('kind') == 'action': acts.append(x)
    for x in acts:
        s = x.get('summary') or ''
        if x.get('type') == 'OpponentRule':
            for tag in ('CHARGE NOT DECLARED', 'SHOT OR CHARGE', 'LEGAL CHARGES ONLY'):
                if s.startswith(tag + ':'): C[br(x['side'])]['row ' + tag] += 1
    for p in g['picks']:
        me = g['byname'].get((p['side'], p['unit']))
        enemy = [i for i in p['ids'] if i in g['units'] and g['units'][i]['side'] != p['side']]
        if me is None or not enemy: continue
        w = jc._window(g, p['i'], p['side'], 'this')
        if not w: continue
        b = br(p['side']); T = enemy[0]
        if p['kind'] == 'charge':
            C[b]['charge picks'] += 1
            if not any(w[0] <= c[0] < w[1] and c[2] == me['id'] and c[3] == T for c in g['charges']):
                C[b]['charge picks never declared'] += 1
        elif p['kind'] == 'shoot':
            C[b]['shoot picks'] += 1
            mine = [x for x in acts if w[0] <= x['id'] < w[1] and x.get('actor_id') == me['id'] and x.get('type') in SH]
            friend_charged = any(w[0] <= c[0] < w[1] and c[3] == T and c[2] != me['id'] for c in g['charges'])
            if friend_charged: C[b]['shoot picks: a friend charged the target'] += 1
            if any(x.get('target_id') == T for x in mine): continue
            C[b]['shoot picks never at their target'] += 1
            C[b]['  of them shot another enemy' if mine else '  of them did not shoot'] += 1
            if friend_charged: C[b]['  of them a friend charged the target'] += 1

keys = ['charge picks', 'charge picks never declared', 'shoot picks', 'shoot picks never at their target', '  of them shot another enemy',
        '  of them did not shoot', '  of them a friend charged the target', 'shoot picks: a friend charged the target',
        'row CHARGE NOT DECLARED', 'row LEGAL CHARGES ONLY', 'row SHOT OR CHARGE']
print(f"{games['ON']} games\n\n| Count | ON | OFF |\n| --- | --- | --- |")
for k in keys:
    def cell(b):
        v = C[b][k]
        base = C[b]['charge picks'] if 'charge picks never' in k else C[b]['shoot picks'] if k.startswith(('shoot picks never', 'shoot picks:')) else C[b]['shoot picks never at their target'] if k.startswith('  ') else None
        return f"{v}" + (f" ({v / base:.0%})" if base else "")
    print(f"| {k.strip()} | {cell('ON')} | {cell('OFF')} |")
