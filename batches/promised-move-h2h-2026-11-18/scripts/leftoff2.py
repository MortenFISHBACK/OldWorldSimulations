import json,glob,re,collections,os,math,pickle
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from reach import corners,gap
import sys
rows=[]
for f in sorted(glob.glob('games/*/*/game-*.log.jsonl')):
    arm=f.split('/')[-3].split('-')[0]; new='Mine' if arm=='mine' else 'Opponent'
    R=[json.loads(l) for l in open(f)]
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
    for x in R:
        if x['kind']=='action' and x['type']=='OpponentRule' and x['summary'].startswith('LEGAL CHARGES ONLY') and 'way or its sight' in x['summary']:
            A,T=x['actor_id'],x['target_id']; sa,sb=st(A,x['id']),st(T,x['id'])
            if not sa or not sb or sa.get('x') is None or sb.get('x') is None or not sa.get('on') or not sb.get('on'): rows.append(dict(k='no state')); continue
            ra,rb=rect(sa),rect(sb); g=gap(ra,rb)
            # engaged: any enemy within 0.2
            side=U[A]['s']; eng=None; mind=99
            for uid,u in U.items():
                if u['s']==side or uid==A: continue
                s2=st(uid,x['id'])
                if s2 and s2.get('on') and s2.get('x') is not None:
                    d=gap(ra,rect(s2))
                    if d<mind: mind=d; eng=uid
            # bearing of target centre from charger facing
            ang=math.degrees(math.atan2(sb['y']-sa['y'],sb['x']-sa['x']))-sa['f']; ang=(ang+180)%360-180
            m=re.search(r'reach (\d+)%',x['summary'])
            rows.append(dict(k='ok',g=g,eng=mind<0.2,engT=(eng==T and mind<0.2),ang=abs(ang),reach=int(m.group(1)),tfl=sb.get('fl'),lk=(U[A].get('lk') or {}),f=os.path.basename(f),turn=x['turn'],A=x['actor'],T=x['target'],id=x['id'],tt=(U[A].get('lk') or {}).get('tt'),path=f,Aid=A,Tid=T))
pickle.dump(rows,open('leftoff.pkl','wb'))
ok=[r for r in rows if r['k']=='ok']
print(len(rows),len(ok))
print('charger engaged (an enemy within 0.2"):',sum(r['eng'] for r in ok),' of which with that target:',sum(r['engT'] for r in ok))
ne=[r for r in ok if not r['eng']]
print('not engaged',len(ne),'target fleeing',sum(bool(r['tfl']) for r in ne))
for lo,hi in((0,45),(45,60),(60,90),(90,181)): print('bearing',lo,hi,sum(lo<=r['ang']<hi for r in ne))
for lo,hi in((0,3),(3,6),(6,9),(9,12),(12,15),(15,30)): print('gap',lo,hi,sum(lo<=r['g']<hi for r in ne))
print(collections.Counter(r['tt'] for r in ne))
import random; random.seed(1)
for r in random.sample(ne,12): print(r['f'],r['turn'],r['A'],'->',r['T'],round(r['g'],1),round(r['ang']),r['reach'])
