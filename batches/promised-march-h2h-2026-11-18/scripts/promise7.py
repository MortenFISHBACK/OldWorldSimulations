"""Try 7: kept promises whose charge was on offer next turn and not taken. Promised VP v the charge's own worth when on offer, what was
picked instead (kind, again 'next turn' on the same target?), the gap and the picked option's split (A this turn / B next charge / C friends)."""
import json,glob,re,sys,collections,os,statistics as st
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import job_claims as jc
ROOT=sys.argv[1]
K=re.compile(r"PROMISE KEPT: charge #(\d+) .*? next turn, ~(-?[\d.]+) VP at (\d+)%")
SP=re.compile(r"SPLIT: A objectives (-?[\d.]+) shoots (-?[\d.]+) missiles (-?[\d.]+) feature (-?[\d.]+) \| B (\S+) (-?[\d.]+) x (\d+)%(?: on #(\d+))?.*?\| C support (-?[\d.]+) carries (-?[\d.]+) chaff (-?[\d.]+) mask (-?[\d.]+) \| D (-?[\d.]+)")
R=[]; kinds=collections.Counter(); ex=[]
for f in glob.glob(f"{ROOT}/*/*/game-*.log.jsonl"):
    new='Mine' if f.split('/')[-3].startswith('mine') else 'Opponent'
    g=jc.read_game(f)
    ev=[json.loads(l) for l in open(f)]; ev=[d for d in ev if d.get('kind')=='action']
    for d in ev:
        if d.get('side')!=new: continue
        m=K.search(d.get('summary','')); 
        if not m: continue
        u=d['actor_id']; T=int(m.group(1)); pv=float(m.group(2)); pp=int(m.group(3))
        ow=jc._window(g,d['id'],new,'own')
        if not ow: continue
        win=[e for e in ev if ow[0]<=e['id']<ow[1]]
        if any(e.get('type')=='Charge' and 'declares a charge' in e.get('summary','') and e.get('actor_id')==u for e in win): continue
        js=[e for e in win if e.get('type')=='JobSplit' and e.get('actor_id')==u and e['summary'].startswith('JOB SPLIT')]
        if not js: continue
        e=js[0]; chw=None; taken=None
        for p in e['summary'].split(' | ')[1:]:
            mm=re.match(r'\d+\. ([a-z]+)(.*?): worth ([+\-]?[\d.]+)',p)
            if not mm: continue
            if mm.group(1)=='charge' and re.match(r' #%d\b'%T,mm.group(2)): chw=float(mm.group(3))
            if '[TAKEN]' in p: taken=(mm.group(1),p,float(mm.group(3)))
        if chw is None or not taken or taken[0]=='charge': continue
        nt=re.search(r'next turn: #(\d+)',taken[1]); same=bool(nt and int(nt.group(1))==T)
        rk=[x for x in win if x.get('type')=='JobRisk' and x.get('actor_id')==u]
        s=SP.search(rk[0]['summary']) if rk else None
        row=dict(pv=pv,pp=pp,chw=chw,tw=taken[2],kind=taken[0],same=same,other=bool(nt and not same))
        if s:
            v=s.groups(); row.update(A=sum(float(v[i]) for i in range(4)),obj=float(v[0]),B=float(v[5])*int(v[6])/100,C=float(v[8])+float(v[9])+float(v[10])-float(v[11]),D=float(v[12]))
        R.append(row)
        if len(ex)<8: ex.append((f.split('/')[-1],e['turn'],e['actor'],T,row))
print('kept promises on offer next turn, not taken:',len(R))
print('picked:',collections.Counter(r['kind'] for r in R),' again SAME target next turn:',sum(r['same'] for r in R),' another target:',sum(r['other'] for r in R))
print('promised VP median %.0f; the charge on offer then worth median %.0f; picked median %.0f'%(st.median(r['pv'] for r in R),st.median(r['chw'] for r in R),st.median(r['tw'] for r in R)))
print('charge worth < promised in %d of %d; charge worth <= 0 in %d'%(sum(r['chw']<r['pv'] for r in R),len(R),sum(r['chw']<=0 for r in R)))
print('mean promised minus charge-on-offer worth %.0f'%st.mean(r['pv']-r['chw'] for r in R))
S=[r for r in R if 'A' in r]
for lab,sub in (('again same',[r for r in S if r['same']]),('other',[r for r in S if not r['same']])):
    if sub: print(lab,len(sub),'mean: picked-charge %.0f = A %.0f (obj %.0f) + B %.0f + C %.0f - D %.0f ; charge worth %.0f'%(st.mean(r['tw']-r['chw'] for r in sub),st.mean(r['A'] for r in sub),st.mean(r['obj'] for r in sub),st.mean(r['B'] for r in sub),st.mean(r['C'] for r in sub),st.mean(r['D'] for r in sub),st.mean(r['chw'] for r in sub)))
for x in ex: print(x)
