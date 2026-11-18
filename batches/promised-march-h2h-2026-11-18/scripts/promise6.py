import json,glob,re,sys,collections,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import job_claims as jc
ROOT=sys.argv[1]; c=collections.Counter(); why=collections.Counter(); reasons=collections.Counter(); prom=[]; legal=collections.Counter()
K=re.compile(r"PROMISE KEPT: charge #(\d+) .*? next turn, ~(-?[\d.]+) VP at (\d+)%")
W=re.compile(r"PROMISE WITHDRAWN: .*?(?:VP|facing \d+)[;,] (?:worth ~-?[\d.]+ VP; )?(.*)")
for f in glob.glob(f"{ROOT}/*/*/game-*.log.jsonl"):
    new='Mine' if f.split('/')[-3].startswith('mine') else 'Opponent'
    g=jc.read_game(f)
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
        hw=jc._window(g,d['id'],new,'enemy'); ow=jc._window(g,d['id'],new,'own')
        if not ow: continue
        enemyturn=[e for e in ev if hw and hw[0]<=e['id']<hw[1]]
        win=[e for e in ev if ow[0]<=e['id']<ow[1]]
        c['kept']+=1; c['claimed p']+=p
        decl=[e for e in win if e.get('type')=='Charge' and 'declares a charge' in e.get('summary','') and e.get('actor_id')==u]
        if any(e.get('target_id')==T for e in decl): why['charged it']+=1; continue
        if decl: why['charged another']+=1; continue
        cand=[e for e in win if e.get('type')=='JobSplit' and e.get('actor_id')==u]
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
        else:
            why['target stood?, not on offer']+=1
        if not decl and not onoff and cand:
            again=any(f'(next turn: #{T})' in e['summary'] for e in cand)
            c['not on offer: promised again next turn']+=again; c['not on offer total']+=1
            ch=any(x in (d.get('actor') or '') for x in ('King','General','Lord','Hero','Wargor','Beastlord','Shaman','Captain','Prince','Noble','Thane','Boss','Herald','Priest','Wizard','Necro','Vampire','Wight','Exalted','Chieftain','Warlord','Hag','Sorcer','Champion','Bray','Great','Seer'))
            c['not on offer: name looks like a character']+=ch
            lr=[re.sub(r'[\d.]+','N',x.group(1))[:110] for e in win if e.get('actor_id')==u for x in re.finditer(r'LEGAL CHARGES ONLY: [^:]*: no charge job on #%d [^:]*: ([^|]*)'%T, e.get('summary',''))]
            legal[lr[0] if lr else '(no LEGAL CHARGES ONLY row for this pair)']+=1
print('--- why not on own list next turn'); [print(v,k) for k,v in legal.most_common(10)]
print(c, 'mean promised', c['claimed p']/max(1,c['kept']))
for k,v in why.most_common(): print(v,k)
print('--- withdrawn reasons'); [print(v,k) for k,v in reasons.most_common(12)]
