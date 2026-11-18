"""Try 7: the shot claim on new-side picks v points lost to shots + magic in the enemy turn after, split by whether the picked option
carries HE SHOOTS OR CHARGES, and by the claimed share of wounds (SHOT RISK POINTS)."""
import collections, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'risk.py')).read().split("ROOT = sys.argv[1]")[0])
ROOT=sys.argv[1]
JR = re.compile(r"^JOB RISK: (.+?): gain ([+-]?[\d.]+) VP, risk (-?[\d.]+) VP")
SR = re.compile(r"shots ([\d.]+) \(SHOT RISK POINTS: ([\d.]+) of its (\d+) wounds")
SHOT = {'Shooting', 'WarMachineShot', 'BreathWeapon', 'ColumnOfFire', 'Zzzzap', 'StandAndShoot'}; MAG = {'SpellCast', 'SpellEffect'}; MEL={'Charge','CombatAttack','ImpactHits','StompAttacks'}
A=collections.defaultdict(lambda: [0,0.0,0.0,0]); NG=0; EX=[]
for f in sorted(glob.glob(ROOT + '/*/*/game-*.log.jsonl')):
    on = 'Mine' if os.path.relpath(f, ROOT).startswith('mine') else 'Opponent'; NG+=1; g = jc.read_game(f)
    acts = [x for x in (json.loads(l) for l in open(f) if l.strip()) if x.get('kind') == 'action']
    risk={}; hs=set()
    for x in acts:
        s=(x.get('summary') or '')
        if x.get('side')!=on: continue
        if x.get('type')=='JobRisk' and (m:=JR.match(s)):
            sr=SR.search(s); risk[(x['turn'],x.get('actor'),m.group(1))]=(float(sr.group(1)),float(sr.group(2)),int(sr.group(3))) if sr else None
        if x.get('type')=='JobSplit':
            t=next((q for q in s.split(' | ')[1:] if '[TAKEN]' in q),'')
            if 'HE SHOOTS OR CHARGES' in t: hs.add((x['turn'],x.get('actor')))
    for p in g['picks']:
        if p['side']!=on: continue
        me=g['byname'].get((p['side'],p['unit']))
        if me is None: continue
        body=next((x['summary'] for x in acts if x['id']==p['i']),'')
        job=re.sub(r'^Objective for .+?: ','',body).split(': ')[0]
        rk=risk.get((p['turn'],p['unit'],job)); we=jc._window(g,p['i'],p['side'],'enemy')
        if not rk or not we: continue
        lost=jc._lost(g,me,we[0],we[1]); hit={x.get('type') for x in acts if we[0]<=x['id']<we[1] and x.get('target_id')==me['id']}
        shotlost = lost if (hit & (SHOT|MAG)) and not hit & MEL else 0
        k1='HE SHOOTS OR CHARGES on the pick' if (p['turn'],p['unit']) in hs else 'without it'
        share=rk[1]/max(1,rk[2]); band='wound share claimed <5%' if share<.05 else '5-20%' if share<.2 else '20%+'
        for k in (k1,band,'ALL'):
            a=A[k]; a[0]+=1; a[1]+=rk[0]; a[2]+=shotlost; a[3]+= shotlost>0
        if rk[0]>40 and shotlost==0 and len(EX)<8: EX.append((os.path.basename(f),p['turn'],p['unit'],job[:40],rk,round(me['points'] if 'points' in me else 0)))
print(NG,'games; new side: shot claim v lost to shots+magic (no melee), a game')
for k,a in A.items(): print(f"{k:35s} picks {a[0]:5d}  claimed {a[1]/NG:6.0f}  lost {a[2]/NG:6.0f}  hit {a[3]}")
for e in EX: print(e)
