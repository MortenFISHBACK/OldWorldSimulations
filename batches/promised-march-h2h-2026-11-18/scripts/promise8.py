"""Try 8: where promised charges go, grouped as in promised-charges-finding-2026-11-18 (try 6), on the new side.
A promise = one PROMISE KEPT / PROMISE WITHDRAWN row (move-phase row for a five-option job that promised 'charge #T next turn').
    python3 -I promise8.py <root holding <arm>-N/<batch>/game-*.log.jsonl>
"""
import json, glob, re, sys, collections, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import job_claims as jc
ROOT = sys.argv[1]
P = re.compile(r"PROMISE (KEPT|WITHDRAWN): charge #(\d+) .*? next turn, ~(-?[\d.]+) VP at (\d+)% from \((-?[\d.]+), (-?[\d.]+)\)")
TAKENNEXT = re.compile(r"\[TAKEN\][^|]*?(?:next turn: #(\d+)|on #(\d+) reach)")
grp = collections.Counter(); sub = collections.Counter(); C = collections.Counter(); claimed = []; games = 0
waits = collections.Counter(); rules = collections.Counter()
def pos(g, uid, i):
    s = jc._state(g, uid, i); return (s[3], s[4]) if s and s[3] is not None else None
for f in sorted(glob.glob(f"{ROOT}/*/*/game-*.log.jsonl")):
    new = 'Mine' if f.split('/')[-3].startswith('mine') else 'Opponent'
    games += 1
    g = jc.read_game(f)
    ev = [json.loads(l) for l in open(f) if l.strip()]; ev = [d for d in ev if d.get('kind') == 'action']
    seen = set()
    for d in ev:
        if d.get('side') != new: continue
        s = d.get('summary', '')
        if d.get('type') == 'OpponentRule':
            for tag in ('WAITS AGAIN', 'THE PROMISED MOVE', 'FRIEND CHARGES FIRST', 'FRIEND SHOOTS FIRST', 'SAME CHARGE LATER', 'WOUNDS ON THE RANKS'):
                if s.startswith(tag): rules[tag] += 1
        if d.get('type') == 'JobSplit' and TAKENNEXT.search(s): C['picks promising a charge next turn'] += 1
        for m in P.finditer(s):
            u = d.get('actor_id'); T = int(m.group(2)); key = (u, d.get('turn'), T)
            if key in seen: continue
            seen.add(key)
            kind, pv, pc = m.group(1), float(m.group(3)), int(m.group(4)); claimed.append(pc)
            C['promises'] += 1; C['claimed %'] += pc
            if kind == 'WITHDRAWN':
                g1 = 'Own move phase: promised move not made'; grp[g1] += 1
                why = ('spot not taken though worth more' if 'not taken though it is worth more' in s else
                       'charge no longer there from the spot' if 'no longer there' in s else
                       'another move worth more' if 'another move is worth more' in s else
                       'none of the spots weighed' if 'none of the spots weighed' in s else
                       'spot no longer legal' if 'no longer legal' in s else 'other')
                sub[why] += 1; continue
            C['kept'] += 1
            i = d['id']; tw = jc._window(g, i, new, 'this'); hw = jc._window(g, i, new, 'enemy'); ow = jc._window(g, i, new, 'own')
            if not ow: grp['Game over before the next turn'] += 1; continue
            rest = [e for e in ev if e['id'] > i and tw and e['id'] < tw[1]]
            enemy = [e for e in ev if hw and hw[0] <= e['id'] < hw[1]]
            win = [e for e in ev if ow[0] <= e['id'] < ow[1]]
            decl = [e for e in win if e.get('type') == 'Charge' and 'declares a charge' in e.get('summary', '') and e.get('actor_id') == u]
            if any(e.get('target_id') == T for e in decl): grp['Charged the promised target'] += 1; continue
            if decl: grp['Charged another target instead'] += 1; continue
            if jc._gone(g, u, ow[0]) or any(e.get('type') == 'Charge' and e.get('target_id') == u and 'declares' in e.get('summary', '') for e in enemy) \
               or not any(e.get('actor_id') == u for e in win):
                grp['Our unit dead, fleeing, charged or pinned'] += 1; continue
            friendhit = any(e.get('type') == 'Charge' and e.get('target_id') == T and 'declares' in e.get('summary', '') for e in rest + win)
            tcharged = any(e.get('type') == 'Charge' and e.get('actor_id') == T and 'declares' in e.get('summary', '') for e in enemy)
            if jc._gone(g, T, ow[0]) or friendhit or tcharged:
                grp['Target dead, fleeing or in a fight before our turn'] += 1; continue
            js = [e for e in win if e.get('type') == 'JobSplit' and e.get('actor_id') == u and e['summary'].startswith('JOB SPLIT')]
            nm = (g['units'].get(u) or {}).get('name') or '?'
            if any(e.get('summary', '').startswith(nm + ' does not charge') and 'no charge below zero' in e.get('summary', '') and re.search(r'#%d\b[^#]*?worth ~-' % T, e['summary']) for e in win):
                grp['Charge on the list, own figure at or below zero'] += 1; continue
            chw = None
            for e in js[:1]:
                for p in e['summary'].split(' | ')[1:]:
                    mm = re.match(r'\d+\. charge #%d\b.*?: worth ([+\-]?[\d.]+)' % T, p)
                    if mm: chw = float(mm.group(1))
            if chw is not None:
                if chw > 0:
                    grp['Charge on offer next turn, not taken'] += 1
                    if js and re.search(r'next turn: #%d\)[^|]*\[TAKEN\]' % T, js[0]['summary']): sub['on offer: same charge put off again'] += 1
                else: grp['Charge on the list, own figure at or below zero'] += 1
                continue
            p0, p1 = pos(g, T, i), pos(g, T, ow[0])
            if p0 and p1 and math.dist(p0, p1) >= 1: grp['Target moved in its turn, no charge left'] += 1; continue
            grp['Nothing moved, yet no charge listed'] += 1
n = max(1, C['promises'])
print(f"games {games}; promises {C['promises']} ({C['promises']/max(1,games):.1f} a game, {C['picks promising a charge next turn']} picks promising), "
      f"kept {C['kept']}, claimed {C['claimed %']/n:.0f}%")
print("| What happened | count | per 100 |\n| --- | --- | --- |")
for k, v in grp.most_common(): print(f"| {k} | {v} | {100*v/n:.1f} |")
print("withdrawn / sub:", dict(sub))
print("rule rows (new side):", dict(rules))
