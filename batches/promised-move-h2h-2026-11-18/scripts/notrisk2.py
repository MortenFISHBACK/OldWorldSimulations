"""Units priced no risk from an enemy because it 'has a better target' (shooter) or 'charges #X instead' (charger):
did that enemy then shoot/charge the unit in its next turn, and did it go for the better target it was predicted to?"""
import json,glob,re,sys,collections
ROOT=sys.argv[1]
SH=re.compile(r"ONE TARGET A SHOOTER: \d+ of \d+ that reach it have a better target \((.*?)\), [\d.]+ VP not counted")
SH1=re.compile(r"#(\d+) at #(\d+) ~")
CH=re.compile(r"#(\d+) (\w+) [\d]+%/[\d]+% he wins (\d+)% but charges #(\d+) instead")
CHR=re.compile(r"#(\d+) (\w+) (\d+)%/(\d+)% (-?[\d.]+) \(he wins (\d+)%\)")
c=collections.Counter()
for f in glob.glob(f"{ROOT}/*/*/game-*.log.jsonl"):
    new='Mine' if f.split('/')[-3].startswith('mine') else 'Opponent'
    ev=[json.loads(l) for l in open(f)]; ev=[d for d in ev if d.get('kind')=='action']
    for i,d in enumerate(ev):
        if d.get('type')!='JobRisk' or d.get('side')!=new: continue
        u=d['actor_id']; s=d['summary']
        # window: enemy's next turn
        win=[]; seen_enemy=False
        for e in ev[i+1:]:
            if e.get('side')!=new and e.get('side'): seen_enemy=True
            if seen_enemy and e.get('side')==new and e.get('phase')=='Strategy': break
            if e.get('side')!=new: win.append(e)
        def acts(E,T):
            out=set()
            for e in win:
                if e.get('actor_id')!=E or e.get('target_id')!=T: continue
                t=e.get('type'); sm=e.get('summary','')
                if t=='Charge' and 'declares a charge' in sm: out.add('charge')
                elif t in ('Shooting','SpellCast') or (e.get('phase')=='Shooting' and t not in ('Candidates','MissileNotTried','ShotNotTaken','SpellNotCast','JobSplit','OpponentRule')): out.add('shot')
            return out
        m=SH.search(s)
        if m:
            for E,B in SH1.findall(m.group(1)):
                E,B=int(E),int(B); a=acts(E,u); b=acts(E,B)
                c['sh pairs']+=1; c['sh hit here']+= 'shot' in a or 'charge' in a; c['sh shot better']+= 'shot' in b
                c['sh shot anything']+= any(e.get('actor_id')==E and e.get('type') in ('Shooting','SpellCast') for e in win)
        for E,arc,w,B in CH.findall(s):
            E,B=int(E),int(B); a=acts(E,u); b=acts(E,B)
            c['ch pairs']+=1; c['ch charged here']+='charge' in a; c['ch charged better']+='charge' in b
            c['ch charged anything']+= any(e.get('actor_id')==E and e.get('type')=='Charge' and 'declares a charge' in e.get('summary','') for e in win)
        for E,arc,p,full,loss,w in CHR.findall(s):
            E=int(E); a=acts(E,u); c['risk pairs']+=1; c['risk claimed p']+=int(p); c['risk charged here']+='charge' in a
            ca=any(e.get('actor_id')==E and e.get('type')=='Charge' and 'declares a charge' in e.get('summary','') for e in win)
            c['risk charged anything']+=ca
            eng=any(e.get('actor_id')==E and e.get('phase')=='Combat' for e in win[:5])
            c['risk enemy had combat early']+=eng
            dead=not any(e.get('actor_id')==E for e in win)
            c['risk enemy did nothing logged']+=dead
            c['risk claimed loss']+=float(loss)
for k,v in sorted(c.items()): print(k,v)
