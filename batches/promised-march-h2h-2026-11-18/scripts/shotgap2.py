"""Shot risk claimed (picked job, new side) v what the enemy's shooters and wizards did with the unit in their next turn."""
import json,glob,re,sys,collections
ROOT=sys.argv[1]
SR=re.compile(r"\] shots (-?[\d.]+) \(SHOT RISK POINTS: ([\d.]+) of its (\d+) wounds")
HERE=re.compile(r"ONE TARGET A SHOOTER: (\d+) of (\d+) that reach it")
agg=collections.defaultdict(lambda:[0,0.0,0.0]); games=set()
SHT={'Shooting','SpellCast','SpellEffect','WarMachineShot','BreathWeapon'}
for f in glob.glob(f"{ROOT}/*/*/game-*.log.jsonl"):
    games.add(f)
    new='Mine' if f.split('/')[-3].startswith('mine') else 'Opponent'
    ev=[json.loads(l) for l in open(f)]; ev=[d for d in ev if d.get('kind')=='action']
    for i,d in enumerate(ev):
        if d.get('type')!='JobRisk' or d.get('side')!=new: continue
        m=SR.search(d['summary'])
        if not m: continue
        vp=float(m.group(1)); u=d['actor_id']
        if vp<=0: continue
        h=HERE.search(d['summary']); away=int(h.group(1)) if h else 0; reach=int(h.group(2)) if h else None
        win=[]; seen=False
        for e in ev[i+1:]:
            if e.get('side') and e.get('side')!=new: seen=True
            if seen and e.get('side')==new and e.get('phase')=='Strategy': break
            if e.get('side')!=new: win.append(e)
        tag=f"#{u} "
        listed=[e for e in win if e.get('type')=='Candidates' and ('CANDIDATES SHOT' in e['summary'] or 'CANDIDATES MISSILE' in e['summary']) and tag in e['summary']]
        took=any(p for e in listed for p in e['summary'].split('|') if tag in p and '[TAKEN]' in p)
        hit=any(e.get('target_id')==u and e.get('type') in SHT for e in win)
        charged=any(e.get('target_id')==u and e.get('type')=='Charge' and 'declares' in e.get('summary','') for e in win)
        # lost: models before/after not available simply; use count only
        if charged: k='charged instead (shots x (1-charged) still counted)'
        elif hit: k='shot or cast at'
        elif took: k='taken on a list but no hit logged'
        elif listed: k='on a shooter/wizard list, other target picked'
        else:
            nl=sum(1 for e in win if e.get('type')=='Candidates' and ('CANDIDATES SHOT' in e['summary'] or 'CANDIDATES MISSILE' in e['summary']))
            k='on nobody\'s list: enemy made no shot/spell lists at all' if nl==0 else 'on nobody\'s list: enemy shot/cast at others'
            mm=re.search(r"shot ([\d.]+), charged ([\d.]+)\)", d['summary'])
            if mm: agg[('nobody: claimed shot chance band', f"{min(9,int(float(mm.group(1))*10))/10:.1f}")][0]+=1; agg[('nobody: claimed shot chance band', f"{min(9,int(float(mm.group(1))*10))/10:.1f}")][1]+=vp
        nh=(reach-away) if reach is not None else -1
        for key in (('why',k),('shooters counted here',min(nh,4) if nh>=0 else 'n/a')):
            a=agg[key]; a[0]+=1; a[1]+=vp
n=len(games)
for key,(c,v,_) in sorted(agg.items(),key=lambda x:(x[0][0],-x[1][1])):
    print(key[0],'|',key[1],'|',c,'|',round(v/n,1),'VP a game')
