#!/usr/bin/env python3
"""Fixed five options v simpler (2026-11-17, second try): the odds Morten asked for at the 50-game check.
- decisions per side (JobSplit rows): charge offered / taken, what was picked (stand share), STANDS STILL reasons (new side)
- move to charge (MOVE TO CHARGE COMPUTED on the new side, MOVE TO CHARGE on the simpler side): promised chance v charge on that target
  in the side's next own turn, by the distance from the unit to the target at the start of that next turn (centre to centre)
- charge now (new side, JobRisk SPLIT of a taken charge): claimed reach / win / target destroyed / charger lost v what happened
  (declared, contact, target gone and charger gone by the end of the side's next own turn = about 3 rounds of combat)
    python3 -I fixed.py <root holding <arm>-N/<batch>/game-*.log.jsonl>
"""
import collections, glob, json, math, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import job_claims as jc

ROOT = sys.argv[1]
OPT = re.compile(r'(\d+)\. ([a-z]+)')
SPLIT = re.compile(r'SPLIT: charge #(\d+) reach (\d+)% win (\d+)%')
DEST = re.compile(r'destroyed ([\d.]+) we-are-lost ([\d.]+)')
MTC = re.compile(r'^MOVE TO CHARGE(?: COMPUTED)?: ([+-]?[\d.]+) VP: ([a-z]+).*?\(next turn: #(\d+)\)')
PCT = re.compile(r'(\d+)%')
pct = lambda v: f"{100*sum(v)/len(v):.0f}%" if v else "-"
avg = lambda v: sum(v) / len(v) if v else float('nan')

D = collections.defaultdict(collections.Counter)      # decisions
STAND = collections.defaultdict(collections.Counter)  # stand reasons
MV = collections.defaultdict(list)                    # (band, promised or None, happened, any charge)
CH = []                                               # new-side charge-now claims
NG = 0


def dist(g, a, b, i):
    sa, sb = jc._state(g, a, i), jc._state(g, b, i)
    if not sa or not sb or sa[3] is None or sb[3] is None: return None
    return math.hypot(sa[3] - sb[3], sa[4] - sb[4])


def band(d):
    if d is None: return 'unknown'
    for lim in (6, 12, 18, 24):
        if d < lim: return f"<{lim}\""
    return '24"+'


for f in sorted(glob.glob(ROOT + '/**/game-*.log.jsonl', recursive=True)):
    if '/parts/' in f: continue
    arm = os.path.relpath(f, ROOT).split('/')[0].split('-')[0]
    newside = 'Mine' if arm == 'mine' else 'Opponent'
    side = lambda s: 'new' if s == newside else 'simpler'
    NG += 1
    g = jc.read_game(f)
    acts = [x for x in (json.loads(l) for l in open(f, encoding='utf-8') if l.strip()) if x.get('kind') == 'action']
    decl = [(x['id'], x['side'], x['actor_id'], x['target_id']) for x in acts if x['type'] == 'Charge' and 'declares a charge' in x['summary']]
    contact = {(x['actor_id'], x['target_id'], x['turn']) for x in acts if x['type'] == 'Charge' and 'made contact' in x['summary']}
    taken_charge = set()
    for x in acts:
        if x['type'] != 'JobSplit': continue
        k = side(x['side']); s = x['summary']; parts = s.split(' | ')[1:]
        opts = [(OPT.match(p).group(2), '[TAKEN]' in p) for p in parts if OPT.match(p)]
        t = [o for o, tk in opts if tk]
        if not t: continue
        D[k]['decisions'] += 1; D[k]['picked ' + t[0]] += 1
        if any(o == 'charge' for o, _ in opts): D[k]['charge offered'] += 1
        if t[0] == 'charge':
            D[k]['charge taken'] += 1; taken_charge.add((x['turn'], x['actor_id']))
    for x in acts:
        s = x.get('summary') or ''
        if x['type'] == 'OpponentRule' and s.startswith('STANDS STILL'):
            r = s.split(' | ')[0]
            r = 'next turn charge' if '(next turn:' in r else ('stand by the sum' if 'five-action sum' in r else r[14:60])
            STAND[side(x['side'])][r] += 1
        if x['type'] == 'OpponentRule' and (m := MTC.match(s)):
            k = side(x['side']); act, tid = m.group(2), int(m.group(3))
            w = jc._window(g, x['id'], x['side'], 'own')
            if not w: continue
            d = dist(g, x['actor_id'], tid, w[0])
            hap = any(w[0] <= i < w[1] and a == x['actor_id'] and t == tid for i, sd, a, t in decl)
            anyc = any(w[0] <= i < w[1] and a == x['actor_id'] for i, sd, a, t in decl)
            gone = jc._gone(g, tid, w[0]) or jc._gone(g, x['actor_id'], w[0])
            pr = None
            for y in acts:
                ys = y.get('summary') or ''
                if y['type'] == 'JobRisk' and y['actor_id'] == x['actor_id'] and y['turn'] == x['turn'] and ys.startswith('JOB RISK: ' + act) \
                        and (mm := re.search(r'next turn [+-]?[\d.]+ VP on #%d at (\d+)%%' % tid, ys.replace('\u002B', '+'))):
                    pr = int(mm.group(1)) / 100
            MV[k].append((band(d), act, hap, anyc, gone, pr))
        if x['type'] == 'JobRisk' and x['side'] == newside and (m := SPLIT.search(s)) and (x['turn'], x['actor_id']) in taken_charge \
                and s.startswith('JOB RISK: charge'):
            tid = int(m.group(1)); dm = DEST.search(s)
            w = jc._window(g, x['id'], x['side'], 'this'); w2 = jc._window(g, x['id'], x['side'], 'own')
            end = w2[1] if w2 else g['n']
            dec = any(w and w[0] <= i < w[1] and a == x['actor_id'] and t == tid for i, sd, a, t in decl)
            CH.append(dict(reach=int(m.group(2)) / 100, win=int(m.group(3)) / 100,
                           dest=float(dm.group(1)) if dm else None, lost=float(dm.group(2)) if dm else None,
                           decl=dec, contact=(x['actor_id'], tid, x['turn']) in contact,
                           tgone=jc._gone(g, tid, end), cgone=jc._gone(g, x['actor_id'], end)))

print(f"{NG} games\n")
print("| Per unit decision | New | Simpler |\n| --- | --- | --- |")
for k in ('decisions',):
    print(f"| decisions | {D['new'][k]} | {D['simpler'][k]} |")
for lab, key in (('charge on offer', 'charge offered'), ('charge picked', 'charge taken')):
    print(f"| {lab} | {D['new'][key]/max(1,D['new']['decisions']):.0%} | {D['simpler'][key]/max(1,D['simpler']['decisions']):.0%} |")
print(f"| charge picked when on offer | {D['new']['charge taken']/max(1,D['new']['charge offered']):.0%} | {D['simpler']['charge taken']/max(1,D['simpler']['charge offered']):.0%} |")
kinds = sorted({k[7:] for s in D.values() for k in s if k.startswith('picked ')})
for kd in kinds:
    print(f"| picked {kd} | {D['new']['picked '+kd]/max(1,D['new']['decisions']):.0%} | {D['simpler']['picked '+kd]/max(1,D['simpler']['decisions']):.0%} |")
print("\nSTANDS STILL rows (new side):", dict(STAND['new']), " simpler:", dict(STAND['simpler']))
print("\n| Move to charge (new side), by distance at the start of the next own turn | Rows | Promised chance (mean) | Charged that target |\n| --- | --- | --- | --- |")
for b in ['<6"', '<12"', '<18"', '<24"', '24"+', 'unknown', 'all']:
    r = [v for v in MV['new'] if b == 'all' or v[0] == b]
    pp = [v[5] for v in r if v[5] is not None]
    print(f"| {b} | {len(r)} | {avg(pp):.0%} ({len(pp)}) | {pct([v[2] for v in r])} |")
for k in ('new', 'simpler'):
    print(f"{k}: move-to-charge rows by picked action {dict(collections.Counter(v[1] for v in MV[k]))}; any charge next turn {pct([v[3] for v in MV[k]])}; unit or target gone by then {pct([v[4] for v in MV[k]])}")
print(f"\nCharge now (new side, taken charges with the played-out split): {len(CH)}")
if CH:
    c = [x for x in CH if x['decl']]; ct = [x for x in c if x['contact']]
    print("| | claimed | happened |\n| --- | --- | --- |")
    print(f"| reach (declared -> contact) | {avg([x['reach'] for x in c]):.0%} | {pct([x['contact'] for x in c])} |")
    print(f"| target destroyed (contact, by end of next own turn) | {avg([x['dest'] for x in ct if x['dest'] is not None]):.0%} | {pct([x['tgone'] for x in ct])} |")
    print(f"| charger lost (contact, by end of next own turn) | {avg([x['lost'] for x in ct if x['lost'] is not None]):.0%} | {pct([x['cgone'] for x in ct])} |")
    print(f"| win (claimed, for build.py's first-round check) | {avg([x['win'] for x in ct]):.0%} | see build/odds |")
    print(f"taken charges declared that turn {pct([x['decl'] for x in CH])}")
