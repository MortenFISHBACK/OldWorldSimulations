import json,glob,re,sys,collections
sys.path.insert(0,'.')
import job_claims as jc
ROOT=sys.argv[1]
CHR=re.compile(r"#(\d+) (\w+) (\d+)%/(\d+)% (-?[\d.]+) \(he wins (\d+)%\)")
T=collections.defaultdict(collections.Counter); N=collections.Counter()
for f in sorted(glob.glob(f"{ROOT}/*/*/game-*.log.jsonl")):
    new='Mine' if f.split('/')[-3].startswith('mine') else 'Opponent'
    g=jc.read_game(f)
    ev=[json.loads(l) for l in open(f)]; ev=[d for d in ev if d.get('kind')=='action']
    for d in ev:
        if d.get('type')!='JobRisk' or d.get('side')!=new: continue
        i=d['id']; u=d['actor_id']; hw=jc._window(g,i,new,'enemy')
        if not hw: continue
        his=[e for e in ev if hw[0]<=e['id']<hw[1]]
        for E,arc,p,full,loss,wn in CHR.findall(d['summary']):
            E=int(E); un=g['units'].get(E,{}); tt=un.get('tt') or '?'
            nm=un.get('name') or ''
            hit=any(e.get('actor_id')==E and e.get('type')=='Charge' and 'declares a charge' in e.get('summary','') and e.get('target_id')==u for e in his)
            rnd=any(e.get('actor_id')==E and 'RANDOM MOVE' in e.get('summary','') for e in ev)
            key=('random mover' if rnd else tt)+(' (joined char)' if un.get('joined') and tt=='Character' else '')
            T[key]['n']+=1; T[key]['hit']+=hit; T[key]['claim']+=int(p)
            N[nm]+=not hit
for k,v in sorted(T.items(),key=lambda x:-x[1]['n']): print(f"{k:40s} n {v['n']:4d} claimed {v['claim']/v['n']:.0f}% came {v['hit']/v['n']:.0%}")
print(N.most_common(12))
