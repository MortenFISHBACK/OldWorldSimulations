import json,glob,re,collections,math,os,pickle,sys
ROOT=sys.argv[1] if len(sys.argv)>1 else None
def corners(x,y,f,w,d):
    r=math.radians(f); fx,fy=math.cos(r),math.sin(r); sx,sy=-fy,fx
    return [(x+a*fx*d/2+b*sx*w/2, y+a*fy*d/2+b*sy*w/2) for a,b in((1,1),(1,-1),(-1,-1),(-1,1))]
def segd(p,a,b):
    ax,ay=a;bx,by=b;px,py=p;dx,dy=bx-ax,by-ay;L=dx*dx+dy*dy
    t=0 if L==0 else max(0,min(1,((px-ax)*dx+(py-ay)*dy)/L))
    return math.hypot(px-ax-t*dx,py-ay-t*dy)
def gap(A,B):
    return min(min(segd(p,B[i],B[(i+1)%4]) for p in A for i in range(4)),min(segd(p,A[i],A[(i+1)%4]) for p in B for i in range(4)))
OPT=re.compile(r'(\d+)\. charge #(\d+) [^|]*?reach (\d+)%, win (\d+)%')
out=[]
if ROOT is None: FILES=[]
else: FILES=sorted(glob.glob(ROOT+"/*/*/game-*.log.jsonl"))
for f in FILES:
    arm=f.split('/')[-3].split('-')[0]; new='Mine' if arm=='mine' else 'Opponent'
    rows=[json.loads(l) for l in open(f)]
    fr=collections.defaultdict(list); U={}
    for x in rows:
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
    acts=[x for x in rows if x['kind']=='action']; acts.sort(key=lambda a:a['id'])
    claim={}; offered=collections.defaultdict(dict)
    for a in acts:
        if a['type']=='JobSplit' and a['summary'].startswith('JOB SPLIT'):
            for p in a['summary'].split(' | ')[1:]:
                m=OPT.match(p)
                if m: offered[(a['turn'],a['side'],a['actor_id'])][int(m.group(2))]=(int(m.group(3))/100,int(m.group(4))/100,'[TAKEN]' in p)
    for n,a in enumerate(acts):
        if a['type']=='Charge' and 'declares a charge' in a['summary']:
            A,T=a['actor_id'],a['target_id']
            c=dict(file=os.path.basename(f),arm=arm,new=a['side']==new,turn=a['turn'],i=a['id'],A=A,T=T,An=a['actor'],Tn=a['target'],arc=a['summary'].rsplit('in its ',1)[-1])
            o=offered.get((a['turn'],a['side'],A),{}).get(T)
            c['claim']=o[0] if o else None; c['win']=o[1] if o else None; c['taken']=o[2] if o else None
            sa,sb=st(A,a['id']),st(T,a['id'])
            if sa and sb and sa.get('x') is not None and sb.get('x') is not None:
                try: c['gap']=gap(corners(sa['x'],sa['y'],sa['f'],sa['bw'],sa['bd']),corners(sb['x'],sb['y'],sb['f'],sb['bw'],sb['bd']))
                except Exception as e: c['gap']=None
                c['Tfl']=sb.get('fl')
            lk=(U.get(A) or {}).get('lk') or {}; c['tt']=lk.get('tt'); c['rt']=lk.get('rt'); c['mt']=lk.get('mt')
            # why line just before
            for b in reversed(acts[max(0,n-4):n]):
                if b['type']=='Computer' and b['summary'].startswith(a['actor']+' charges'): c['why']=b['summary'][:200]; break
            ev=[]
            for b in acts[n+1:n+60]:
                if b['turn']!=a['turn'] or b['phase'] not in('Movement',): 
                    if b['phase'] in ('Shooting','Combat','Strategy') and b['type'] not in('Shooting','PanicTest'): break
                if b.get('actor_id')==A and (b['type']=='Charge' or b['type'].startswith('Chase')):
                    if 'declares a charge' in b['summary']: break
                    ev.append((b['type'],b['summary'],b.get('dice'),b.get('total'),b.get('target_id')))
                if b.get('actor_id')==T and b['type'] in('FleeDirection','FleeReaction','Flee','FearTest','PanicTest') : ev.append((b['type'],b['summary'][:200],None,None,None))
                if b['type']=='FearTest' and b.get('actor_id')==A: ev.append((b['type'],b['summary'][:200],None,None,None))
            c['ev']=ev
            out.append(c)
if ROOT:
    pickle.dump(out,open('reach.pkl','wb'))
    print(len(out))
    k=collections.Counter()
    for c in out:
        k[tuple(e[0] for e in c['ev'])]+=1
    for a,b in k.most_common(40): print(b,a)
