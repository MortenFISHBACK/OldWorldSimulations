#!/usr/bin/env python3
"""Marker (and hill) player-turns: share scored by the new side, the old side, nobody.  python3 -I markers.py <root with <arm>-N/...>"""
import sys, glob, json, os, collections
R = sys.argv[1]; tot = collections.Counter(); games = 0
for f in glob.glob(os.path.join(R, '*/*/game-*.log.jsonl')):
    arm = os.path.relpath(f, R).split('/')[0]; new = 'Mine' if arm.startswith('mine') else 'Opponent'
    fh = open(f); b = json.loads(fh.readline()); m = b.get('markers') or 0; slots = len(m) if isinstance(m, list) else m
    if b['sc'] == 'KingOfTheHill': slots = 1
    if not slots: continue
    seen = set(); maxturn = collections.Counter(); kinds = ('StrategicLocation', 'Hill')
    for l in fh:
        if not l.startswith('{"kind":"action"') and not l.startswith('{"kind":"objective"'): continue
        d = json.loads(l)
        if d['kind'] == 'action' and d.get('turn'): maxturn[(d['turn'], d['side'])] = 1
        if d['kind'] == 'objective' and d['objective'] in kinds:
            seen.add((d['turn'], d['turn_side'], d['index'])); k = 'new' if d['side'] == new else 'old'; tot[k] += 1; tot[k+'vp'] += d.get('points', 30)
    games += 1; tot['slots'] += slots * len(maxturn)
s = tot['slots']; print(f"games {games}; marker player-turns {s}; scored by new side {tot['new']/s:.0%} ({tot['newvp']/games:.0f} VP a game), old side {tot['old']/s:.0%} ({tot['oldvp']/games:.0f} VP a game), nobody {1-(tot['new']+tot['old'])/s:.0%}")
