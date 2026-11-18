import json,glob,re,csv,collections,statistics as st,sys,os
os.chdir(sys.argv[1])
def ci(x): return 1.96*st.stdev(x)/len(x)**.5
# headline
G=[]
for f in glob.glob("*/*/parts/*/games.csv"):
    new='mine' if f.startswith('mine') else 'opponent'; old='opponent' if new=='mine' else 'mine'
    for r in csv.DictReader(open(f)):
        a,b=map(int,r['vp_mine_opponent'].split('-')); vn,vo=(a,b) if new=='mine' else (b,a)
        g=dict(m=vn-vo,w=r['winner'].lower()==new,l=r['winner'].lower()==old)
        for k in ['objectives','kills','leaders','other']: g[k]=int(r[f'vp_{k}_{new}'] or 0)-int(r[f'vp_{k}_{old}'] or 0)
        g['pln']=int(r['points_lost_'+new]); g['plo']=int(r['points_lost_'+old]); G.append(g)
n=len(G); print(f"GAMES {n}; margin {st.mean(g['m'] for g in G):+.0f} ±{ci([g['m'] for g in G]):.0f}; won {sum(g['w'] for g in G)} lost {sum(g['l'] for g in G)} drawn {n-sum(g['w'] for g in G)-sum(g['l'] for g in G)}")
print("points lost a game new/old", round(st.mean(g['pln'] for g in G)), round(st.mean(g['plo'] for g in G)))
for k in ['objectives','kills','leaders','other']: print(" VP by source",k,f"{st.mean(g[k] for g in G):+.0f}")
take={'new':collections.Counter(),'old':collections.Counter()}; off={'new':collections.Counter(),'old':collections.Counter()}
passed=collections.Counter(); wc=[];wt=[]; chargeclaim={'new':[],'old':[]}
mtc=[]  # (claimed mtc, charged next turn)
decl={'new':0,'old':0}; contact={'new':0,'old':0}
for f in glob.glob("*/*/game-*.log.jsonl"):
    newside='Mine' if f.startswith('mine') else 'Opponent'
    ev=[json.loads(l) for l in open(f)]
    charges=set()
    for d in ev:
        if d.get('type')=='Charge' and 'declares a charge' in d['summary']:
            k='new' if d['side']==newside else 'old'; decl[k]+=1; charges.add((d['actor_id'],d['target_id'],d['turn']))
        if d.get('type')=='Charge' and 'made contact' in d['summary']:
            contact['new' if d['side']==newside else 'old']+=1
    for d in ev:
        if d.get('type')!='JobSplit': continue
        k='new' if d['side']==newside else 'old'; s=d['summary']
        os_=[]
        for p in s.split(' | ')[1:]:
            m=re.match(r'(\d+)\. ([a-z]+)(.*?): worth ([+\-]?[\d.]+)',p.replace('\\u002B','+'))
            if m: os_.append((m.group(2),float(m.group(4)),'[TAKEN]' in p,p))
        t=[o for o in os_ if o[2]]
        if not t: continue
        t=t[0]; take[k][t[0]]+=1
        ch=[o for o in os_ if o[0]=='charge']
        if ch: off[k]['offered']+=1
        if t[0]=='charge': off[k]['taken']+=1; chargeclaim[k].append(t[1])
        if k=='new' and ch and t[0]!='charge':
            passed[t[0]]+=1; wt.append(t[1]); wc.append(max(o[1] for o in ch))
        if k=='new' and t[0] in('move','march','stand'):
            m=re.search(r'next turn: #(\d+)',t[3]); v=re.search(r'MOVE TO CHARGE COMPUTED ([+\-]?[\d.]+)',t[3])
            if m and v: mtc.append((float(v.group(1)),(d['actor_id'],int(m.group(1)),d['turn']+1) in charges))
print("\nDECISIONS taken (share)")
for k in take:
    T=sum(take[k].values()); print(k,T,", ".join(f"{a} {100*b/T:.0f}%" for a,b in take[k].most_common(8)))
print("\nCHARGE offered/taken", {k:dict(v) for k,v in off.items()}, "declared", decl, "contact", contact)
print("passed over ->",passed.most_common(), "median picked",st.median(wt),"median best charge",st.median(wc),"charge<=0",f"{100*sum(c<=0 for c in wc)/len(wc):.0f}%")
print("claimed worth of charges taken: new median",st.median(chargeclaim['new']),"old median",st.median(chargeclaim['old']))
print("\nMOVE TO CHARGE picks (new):",len(mtc),"median claimed",st.median(a for a,b in mtc),"charged that target next turn",sum(b for a,b in mtc), f"{100*sum(b for a,b in mtc)/len(mtc):.0f}%")
big=[x for x in mtc if x[0]>=50]; print(" claimed >=50:",len(big),"came",sum(b for a,b in big))
