import sys,os,json,glob,re,collections,math,pickle
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from reach import corners,gap
import job_claims as jc
P=re.compile(r'next turn [+-]?[\d.]+ VP on #(\d+) at (\d+)%')
rows=[]
for f in sorted(glob.glob('games/*/*/game-*.log.jsonl')):
    arm=f.split('/')[-3].split('-')[0]; new='Mine' if arm=='mine' else 'Opponent'
    R=[json.loads(l) for l in open(f)]
    g=jc.read_game(f)
    fr=collections.defaultdict(list); U={}
    for x in R:
        if x['kind']=='frame':
            for u in x['units']: fr[u['id']].append((x.get('after') or 0,u))
        if x['kind']=='board':
            for u in x['units']: U[u['id']]=u
    for v in fr.values(): v.sort(key=lambda t:t[0])
    def st(uid,i):
        last=None
        for a,u in fr.get(uid,[]):
            if a<i: last=u
            else: break
        return last
    def rect(s): return corners(s['x'],s['y'],s['f'],s['bw'],s['bd'])
    def G(a,b,i):
        sa,sb=st(a,i),st(b,i)
        if not sa or not sb or sa.get('x') is None or sb.get('x') is None or not sa.get('on') or not sb.get('on'): return None
        return gap(rect(sa),rect(sb))
    def pos(a,i):
        s=st(a,i); return (s['x'],s['y'],s['f']) if s and s.get('x') is not None and s.get('on') else None
    acts=[x for x in R if x['kind']=='action']; acts.sort(key=lambda a:a['id'])
    taken={}
    for x in acts:
        if x['type']=='JobSplit' and x['summary'].startswith('JOB SPLIT') and x['side']==new:
            for p in x['summary'].split(' | ')[1:]:
                if '[TAKEN]' in p: taken[(x['turn'],x['actor_id'])]=p
    for x in acts:
        if x['type']!='JobRisk' or x['side']!=new: continue
        s=x['summary'].replace('+','+')
        m=re.match(r'JOB RISK: (move|march|stand) by the five-action sum \(next turn: #(\d+)\)',s)
        if not m: continue
        tk=taken.get((x['turn'],x['actor_id']),'')
        if not re.match(r'\d+\. %s by the five-action sum \(next turn: #%s\)'%(m.group(1),m.group(2)),tk): continue
        A=x['actor_id']; T=int(m.group(2)); pm=P.search(s)
        if not pm: continue
        r=dict(f=os.path.basename(f),path=f,arm=arm,turn=x['turn'],A=A,T=T,act=m.group(1),promise=int(pm.group(2))/100,An=(U.get(A) or {}).get('n'),Tn=(U.get(T) or {}).get('n'),tt=((U.get(A) or {}).get('lk') or {}).get('tt'))
        w=jc._window(g,x['id'],x['side'],'this'); w2=jc._window(g,x['id'],x['side'],'own')
        if not w or not w2: r['k']='game ended'; rows.append(r); continue
        r['gap0']=G(A,T,x['id']); r['gap1']=G(A,T,w[1]); r['gap2']=G(A,T,w2[0]+1)
        p0,p1,p2=pos(A,x['id']),pos(A,w[1]),pos(A,w2[0]+1); t1,t2=pos(T,w[1]),pos(T,w2[0]+1)
        r['we_moved']=bool(p0 and p1 and (math.hypot(p0[0]-p1[0],p0[1]-p1[1])>0.05 or abs(p0[2]-p1[2])>0.5))
        r['we_displaced']=bool(p1 and p2 and (math.hypot(p2[0]-p1[0],p2[1]-p1[1])>0.05 or abs(p2[2]-p1[2])>0.5))
        r['t_moved']=bool(t1 and t2 and (math.hypot(t2[0]-t1[0],t2[1]-t1[1])>0.05 or abs(t2[2]-t1[2])>0.5))
        r['gone']=not p2 or not t2
        # move made this turn: MOVE SPLIT taken
        ms=[y for y in acts if w[0]<=y['id']<w[1] and y['type']=='JobSplit' and y['actor_id']==A and y['summary'].startswith('MOVE SPLIT')]
        r['movesplit']=bool(ms)
        if ms:
            first=ms[-1]['summary'].split(' | ')[0]
            mm=re.search(r'\(on #(\d+) reach (\d+)%',first)
            r['move_sets']=(int(mm.group(1)),int(mm.group(2))/100) if mm else None
            r['move_text']=first[:160]
        # next turn
        nx=[y for y in acts if w2[0]<=y['id']<w2[1]]
        r['charged']=any(y['type']=='Charge' and 'declares a charge' in y['summary'] and y['actor_id']==A and y['target_id']==T for y in nx)
        js=[y for y in nx if y['type']=='JobSplit' and y['actor_id']==A and y['summary'].startswith('JOB SPLIT')]
        r['next_offer']=None
        for y in js:
            for p in y['summary'].split(' | ')[1:]:
                mm=re.match(r'\d+\. charge #%d .*?reach (\d+)%%'%T,p)
                if mm: r['next_offer']=int(mm.group(1))/100; r['next_worth']=float(re.search(r'worth ([+-][\d.]+)',p).group(1))
        lo=[y['summary'] for y in nx if y['type']=='OpponentRule' and y['actor_id']==A and y['target_id']==T and y['summary'].startswith('LEGAL CHARGES ONLY')]
        r['leftoff']=lo[0] if lo else None
        bz=[y['summary'] for y in nx if y['type']=='Computer' and 'does not charge' in y['summary'] and '#%d '%T in y['summary'] and 'below zero' in y['summary']]
        r['below']=bool(bz)
        r['engaged_next']=False
        sa=st(A,w2[0]+1)
        if sa and sa.get('on') and sa.get('x') is not None:
            for uid,u in U.items():
                if u['s']!=U[A]['s']:
                    s2=st(uid,w2[0]+1)
                    if s2 and s2.get('on') and s2.get('x') is not None and gap(rect(sa),rect(s2))<0.2: r['engaged_next']=True
        r['fleeing_next']=bool(sa and sa.get('fl')); st2=st(T,w2[0]+1); r['t_fleeing']=bool(st2 and st2.get('fl'))
        r['k']='ok'; rows.append(r)
pickle.dump(rows,open('nextturn.pkl','wb'))
ok=[r for r in rows if r['k']=='ok']
print(len(rows),len(ok),'mean promise',sum(r['promise'] for r in ok)/len(ok),'charged',sum(r['charged'] for r in ok))
def cls(r):
    if r['charged']: return '1 charged'
    if r['gone']: return '2 unit or target gone'
    if r['fleeing_next'] or r['engaged_next']: return '3 we are in combat or fleeing'
    if r['t_fleeing']: return '3b target fleeing'
    if r['next_offer'] is not None: return '4 offered next turn, below zero' if r['below'] else '5 offered next turn, other option taken'
    if r['below']: return '4 offered next turn, below zero'
    if r['leftoff']:
        w=r['leftoff']
        return '6 game does not allow: '+('rule' if 'the game offers it no charge' in w else 'front arc' if 'front arc' in w else 'way or sight')
    return '7 not in reach by the estimate: '+('target moved' if r['t_moved'] else 'target stood')
k=collections.Counter(cls(r) for r in ok)
for a in sorted(k): 
    rr=[r for r in ok if cls(r)==a]
    print(f"{k[a]:4d} {k[a]/len(ok):4.0%} promise {sum(r['promise'] for r in rr)/len(rr):.0%}  {a}")
for r in ok: r['cls']=cls(r)
pickle.dump(rows,open('nextturn.pkl','wb'))
print('movesplit present',sum(r['movesplit'] for r in ok))
print('move sets up same target',sum(bool(r.get('move_sets')) and r['move_sets'][0]==r['T'] for r in ok),'other target',sum(bool(r.get('move_sets')) and r['move_sets'][0]!=r['T'] for r in ok),'none',sum(r['movesplit'] and not r.get('move_sets') for r in ok))
