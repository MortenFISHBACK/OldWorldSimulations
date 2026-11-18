import json,glob,re,sys,collections
ROOT=sys.argv[1]; c=collections.Counter(); why=collections.Counter(); reasons=collections.Counter(); prom=[]
K=re.compile(r"PROMISE KEPT: charge #(\d+) .*? next turn, ~(-?[\d.]+) VP at (\d+)%")
W=re.compile(r"PROMISE WITHDRAWN: .*?(?:VP|facing \d+)[;,] (?:worth ~-?[\d.]+ VP; )?(.*)")
for f in glob.glob(f"{ROOT}/*/*/game-*.log.jsonl"):
    new='Mine' if f.split('/')[-3].startswith('mine') else 'Opponent'
    ev=[json.loads(l) for l in open(f)]; ev=[d for d in ev if d.get('kind')=='action']
    for i,d in enumerate(ev):
        s=d.get('summary','')
        if d.get('side')!=new: continue
        for m in re.finditer(r"PROMISE WITHDRAWN[^|]*",s):
            r=m.group(0); r=re.sub(r".*facing \d+, worth ~-?[\d.]+ VP; ","",r); r=re.sub(r"[-\d.~]+","N",r); r=re.sub(r"#N [^:;()]*","#X",r)
            reasons[r[:90]]+=1
        m=K.search(s)
        if not m: continue
        u=d['actor_id']; T=int(m.group(1)); p=int(m.group(3))
        # next own turn window: skip to enemy events, then own events until enemy again after own Movement
        j=i+1
        while j<len(ev) and ev[j].get('side')==new: j+=1
        while j<len(ev) and not (ev[j].get('side')==new and ev[j].get('phase')=='Strategy'): j+=1
        win=[]
        enemyturn=ev[i+1:j]
        for e in ev[j:]:
            if e.get('side')!=new and e.get('side') and e.get('phase')=='Strategy' and win and any(x.get('phase')=='Movement' for x in win): break
            win.append(e)
        c['kept']+=1; c['claimed p']+=p
        decl=[e for e in win if e.get('type')=='Charge' and 'declares a charge' in e.get('summary','') and e.get('actor_id')==u]
        if any(e.get('target_id')==T for e in decl): why['charged it']+=1; continue
        if decl: why['charged another']+=1; continue
        cand=[e for e in win if e.get('type')=='Candidates' and e.get('actor_id')==u and 'CANDIDATES JOB' in e.get('summary','')]
        onoff=[p for e in cand for p in e['summary'].split('|') if f'#{T} ' in p and 'charge' in p.lower()]
        gone = not any(e.get('actor_id')==u for e in win)
        enemyhit = any(e.get('target_id')==u and e.get('type')=='Charge' for e in enemyturn)
        tmoved = any(e.get('actor_id')==T and e.get('phase')=='Movement' and (e.get('to') or [None])[0] is not None and e.get('from')!=e.get('to') for e in enemyturn)
        tre = any(e.get('actor_id')==T and 'reform' in (e.get('type','')+e.get('summary','')[:80]).lower() for e in enemyturn)
        c['reformed']+=tre
        if gone: why['unit gone/no action']+=1
        elif enemyhit: why['unit was charged in enemy turn']+=1
        elif onoff: why['on offer, not taken']+=1
        elif not cand: why['no job list (in combat/fleeing?)']+=1
        elif tmoved: why['target moved/charged, not on offer']+=1
        else: why['target stood?, not on offer']+=1
print(c, 'mean promised', c['claimed p']/max(1,c['kept']))
for k,v in why.most_common(): print(v,k)
print('--- withdrawn reasons'); [print(v,k) for k,v in reasons.most_common(12)]
