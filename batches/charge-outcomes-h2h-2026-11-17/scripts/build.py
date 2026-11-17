import sys,os,glob,json,re,pickle,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import job_claims as jc
ROOT=sys.argv[1]
def simpler_side(batch,arm):
    if batch.startswith('one-sum'): return 'Mine' if arm=='mine' else 'Opponent'
    return 'Opponent' if arm=='mine' else 'Mine'
NOISE={'Candidates','SpellNotCast','MissileNotTried','ShotNotTaken','SpellHeldBack'}
JR=re.compile(r"^JOB RISK: (.+?): gain ([+-][\d.]+) VP, risk (-?[\d.]+) VP, worth ([+-][\d.]+) VP")
RULE=re.compile(r"^([A-Z][A-Z0-9' \-]+): ([+-][\d.]+) VP: (.*?)(?: \| (SAME|CHANGED): ([+-][\d.]+) VP v ([+-][\d.]+) VP.*)?$",re.S)
ATT={'CombatAttack','ImpactHits','StompAttacks','BreathWeapon','Thunderous Impact','NoEnemyToStrike','Unstable'}
AFTER={'BreakTest','BreakTestMove','Pursuit','PursuitDeclared','PursuitIntoFreshEnemy','PursuitIntoCombat','Overrun','FollowUp','FollowUpContact','RestrainAndReform','BreakTestBsbReroll','AftermathDeclared','FledOffWithUnit'}
def other(s): return 'Opponent' if s=='Mine' else 'Mine'
def game(batch,arm,f):
    g=jc.read_game(f)
    S=simpler_side(batch,arm)
    acts=[];board=None;FL=collections.defaultdict(list)
    for line in open(f,encoding='utf-8'):
        try:x=json.loads(line)
        except ValueError: continue
        if x.get('kind')=='board': board={k:x.get(k) for k in ('mine','opponent','sc')}
        if x.get('kind')=='action' and x['type'] not in NOISE: acts.append(x)
        if x.get('kind')=='frame':
            for u in x.get('units',[]): FL[u['id']].append((x.get('after') or 0,u.get('fl') or 0))
    acts.sort(key=lambda a:a['id'])
    U=g['units']
    def body(uid):
        u=U.get(uid)
        if not u: return {uid}
        h=u.get('host') or uid
        return {h}|{c['id'] for c in U.values() if c.get('host')==h}
    def host(uid):
        u=U.get(uid); return (u.get('host') or uid) if u else uid
    # player-turn segments by ArmyStance
    segs=[]
    for n,a in enumerate(acts):
        if a['type']!='ArmyStance': continue
        st=a['id']; m=n-1
        while m>=0 and n-m<60:
            b=acts[m]
            if b['type'] in ('CombatResult','CombatAttack','Shooting','WarMachineShot','SpellCast','RallyTest') or b['phase'] in ('Combat','Strategy') and b['type']!='Computer': break
            if b['type']=='Charge' and 'declares a charge' in b['summary']: st=b['id']
            m-=1
        segs.append(st)
    def seg(i):
        k=-1
        for j,s in enumerate(segs):
            if s<=i: k=j
            else: break
        return k
    def segend(k): return segs[k+1] if k+1<len(segs) else g['n']
    def segstart(k): return segs[k] if 0<=k<len(segs) else g['n']
    idx={a['id']:n for n,a in enumerate(acts)}
    # combat blocks
    blocks=[]  # dict(k, ids set, result action, after list)
    cur=None
    for n,a in enumerate(acts):
        if a['phase']!='Combat' and a['type'] not in AFTER: continue
        t=a['type']
        if t in ATT or t.startswith('Challenge'):
            if cur is None or cur.get('res') is not None:
                cur=dict(k=seg(a['id']),ids=set(),res=None,after=[],first=a['id']); blocks.append(cur)
            for q in (a.get('actor_id'),a.get('target_id')):
                if q: cur['ids'].add(host(q))
        elif t=='CombatResult':
            if cur is None or cur.get('res') is not None:
                cur=dict(k=seg(a['id']),ids=set(),res=None,after=[],first=a['id']); blocks.append(cur)
            cur['res']=a
        elif t in AFTER and cur is not None and cur.get('res') is not None:
            cur['after'].append(a)
            if a.get('actor_id'): cur['ids'].add(host(a['actor_id']))
    # picks: JobRisk + rules per (seg-ish turn, actor)
    jr={};rules=collections.defaultdict(list);win={}
    for a in acts:
        if a['type']=='JobRisk':
            m=JR.match(a['summary'])
            if m and m.group(1).startswith('charge #'): jr[(a['turn'],a['side'],a['actor_id'])]=(float(m.group(2)),float(m.group(3)),float(m.group(4)),a['target_id'])
        elif a['type']=='OpponentRule' and not a['summary'].startswith('PLAN RESULT'):
            m=RULE.match(a['summary'])
            if m and m.group(3).startswith('charge #'): rules[(a['turn'],a['side'],a['actor_id'])].append((m.group(1),float(m.group(2))))
        elif a['type']=='Computer':
            m=re.match(r"^Objective for (.+?): charge #(\d+) .*win first round (\d+)%",a['summary'])
            if m: win[(a['turn'],a['side'],m.group(1))]=int(m.group(3))/100
    def pts(uid):
        u=U.get(host(uid)); return u['vp'] if u else 0
    def lost(uid,a,b):
        u=U.get(host(uid))
        if not u: return 0.0
        tot=jc._lost(g,u,a,b)
        for c in U.values():
            if c.get('host')==u['id'] and not jc._gone(g,u['id'],b):
                tot+=jc._lost(g,c,a,b) if jc._gone(g,c['id'],b) and not jc._gone(g,c['id'],a) else 0
        return tot
    def objpts(name,side,k0,k1):
        return 0
    out=[]
    n=0
    while n<len(acts):
        a=acts[n]
        if a['type']=='Charge' and 'declares a charge' in a['summary']:
            A=a['actor_id'];T=a['target_id'];k=seg(a['id']);end=segend(k)
            arc=a['summary'].rsplit('in its ',1)[-1]
            c=dict(batch=batch,arm=arm,file=os.path.basename(f),simpler=(a['side']==S),side=a['side'],turn=a['turn'],i=a['id'],A=A,T0=T,T=T,arc=arc,
                   res=None,react='hold',sns_w=0,sns_shots=0,panicA=None,redirect=False,caught_chase=False,
                   army_def=board['mine' if other(a['side'])=='Mine' else 'opponent'] if board else None,
                   army_att=board['mine' if a['side']=='Mine' else 'opponent'] if board else None)
            for b in acts[n+1:]:
                if b['id']>=end or b['phase'] in ('Shooting','Combat') and b['type'] not in ('Shooting','SkirmisherFormUp') : 
                    if b['phase']=='Combat' or (b['phase']=='Shooting' and b['type']!='Shooting'): break
                t=b['type'];s=b['summary']
                if t=='Charge' and b['actor_id']==A:
                    if 'declares a charge' in s: break
                    if 'redirects its charge' in s: c['redirect']=True; c['react']='flee'; c['T']=b['target_id']; continue
                    if 'fails to redirect' in s: c['react']='flee'; continue
                    if 'made contact' in s: c['res']='contact'; c['T']=b['target_id']; c['ci']=b['id']; c['arc2']=('flank' if 'in its flank' in s else 'rear' if 'in its rear' in s else 'front'); break
                    if 'fell short' in s: c['res']='short'; break
                    if 'halted' in s: c['res']='halted'; break
                    c['res']='other:'+s[:60]; break
                elif t.startswith('Chase') and b['actor_id']==A:
                    c['react']='flee'
                    if t=='ChaseRunsDown': c['res']='chase-caught'; c['caught_chase']=True
                    elif c['res'] is None: c['res']='chase-'+t[5:]
                    if not c['redirect']: break
                elif t=='Shooting' and b['side']!=a['side'] and b.get('target_id') in body(A) and host(b.get('actor_id')) in {host(c['T'])}|body(c['T']):
                    m=re.search(r'(\d+) wound\(s\)',s)
                    if 'fires' in s:
                        c['react']='sns' if c['react']=='hold' else c['react']; c['sns_w']+=int(m.group(1)) if m else 0; c['sns_shots']+=1
                elif t=='PanicTest' and b.get('actor_id')==A and c['panicA'] is None and 'heavy casualties' in s:
                    c['panicA']='flees' if 'flee' in s else 'holds'
            # value windows
            uA=U.get(host(A)); uT=U.get(host(c['T']))
            c['Aname']=uA['name'] if uA else a.get('actor'); c['Tname']=uT['name'] if uT else a.get('target')
            c['Apts']=pts(A); c['Tpts']=pts(c['T']); c['Att']=jc.unit_type(uA); c['Ttt']=jc.unit_type(uT)
            c['Aw']=(uA['mc']*uA['w']) if uA else 1; c['Aown']=uA['points'] if uA else 0
            e1=end; e2=segstart(k+4) if k+4<len(segs) else g['n']
            c['t_r1']=lost(c['T'],a['id'],e1); c['a_r1']=lost(A,a['id'],e1)
            c['t_2t']=lost(c['T'],a['id'],e2); c['a_2t']=lost(A,a['id'],e2)
            c['a_pre']=lost(A,a['id'],c.get('ci',a['id']))
            c['turnsleft']=len(segs)-1-k
            key=(a['turn'],a['side'],A)
            if key in jr: c['gain'],c['risk'],c['worth'],c['jt']=jr[key]
            c['rules']=rules.get(key,[])
            c['win']=win.get((a['turn'],a['side'],c['Aname']))
            # round 1
            if c['res']=='contact':
                bl=[b for b in blocks if b['k']==k and b['res'] is not None and (host(A) in b['ids'] or host(c['T']) in b['ids'])]
                # wiped-out results name the unit
                if not bl:
                    bl=[b for b in blocks if b['k']==k and b['res'] is not None and 'wiped out' in b['res']['summary'] and (c['Tname'] and b['res']['summary'].startswith(c['Tname']) or c['Aname'] and b['res']['summary'].startswith(c['Aname']))]
                if bl:
                    b=bl[0]; s=b['res']['summary']
                    m=re.search(r'Mine (\d+) vs Opponent (\d+)',s)
                    if m:
                        x,y=int(m.group(1)),int(m.group(2)); mine,opp=(x,y)
                        me=mine if a['side']=='Mine' else opp; th=opp if a['side']=='Mine' else mine
                        c['r1']='win' if me>th else 'loss' if me<th else 'draw'; c['by']=me-th
                    elif 'wiped out' in s:
                        m=re.search(r'- (Mine|Opponent) wins',s)
                        c['r1']='win' if m and m.group(1)==a['side'] else 'loss'; c['wipe']=True; c['by']=None
                    else: c['r1']='?'
                    ev=[]
                    for q in b['after']:
                        ev.append((q['type'],q.get('actor_id'),host(q.get('actor_id')) if q.get('actor_id') else None,q['side'],q['summary'][:260]))
                    c['after']=ev
                    c['nunits']=len(b['ids'])
                else: c['r1']='nofight'
                # later rounds of same fight: results in later segs involving both
                later=[]
                for b in blocks:
                    if b['k']>k and b['res'] is not None and host(A) in b['ids'] and host(c['T']) in b['ids']:
                        later.append((b['k']-k,b['res']['summary'][:80],[(q['type'],host(q.get('actor_id')) if q.get('actor_id') else None,q['summary'][:160]) for q in b['after']]))
                c['later']=later
            c['hA']=host(A); c['hT']=host(c['T'])
            def flat(uid,i):
                last=0
                for (aa,fl) in sorted(FL.get(uid,[])):
                    if aa<i: last=fl
                    else: break
                return bool(last)
            c['T0_fleeing']=flat(host(c['T0']),a['id'])
            c['T_gone_r1']=jc._gone(g,host(c['T']),e1); c['A_gone_r1']=jc._gone(g,host(A),e1)
            c['T_gone_2t']=jc._gone(g,host(c['T']),e2); c['A_gone_2t']=jc._gone(g,host(A),e2)
            fr=None
            for q in c.get('after',[]):
                if q[2]!=host(A): continue
                m=re.search(r'pursues into contact with (.+?) - locked',q[4]) or re.search(r'it stops against (.+?) after',q[4])
                if m and 'impassable' not in m.group(1): fr=m.group(1)
            if fr:
                fu=g['byname'].get((other(a['side']),fr))
                if fu:
                    c['fresh']=fr; c['fresh_pts']=pts(fu['id']); c['fresh_lost']=lost(fu['id'],a['id'],e2); c['fresh_gone']=jc._gone(g,host(fu['id']),e2)
            c['obj_after']=sum(p for (t,ts,sd,un,p) in g['obj'] if sd==a['side'] and un==c['Aname'] and c['turn']<t<=c['turn']+2)
            c['obj_T_before']=sum(p for (t,ts,sd,un,p) in g['obj'] if sd!=a['side'] and un==c['Tname'] and c['turn']-1<=t<=c['turn'] )
            c['obj_T_after']=sum(p for (t,ts,sd,un,p) in g['obj'] if sd!=a['side'] and un==c['Tname'] and c['turn']<t<=c['turn']+2)
            out.append(c)
        n+=1
    return out
res=[]
fs=sorted(glob.glob(ROOT+'/**/game-*.log.jsonl',recursive=True))
for f in fs:
    rel=os.path.relpath(f,ROOT).split('/')
    batch=rel[0]; arm=rel[1].split('-')[0]
    try: res+=game(batch,arm,f)
    except Exception as e: print('ERR',f,repr(e))
pickle.dump(res,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'charges.pkl'),'wb'))
print(len(fs),'games',len(res),'charges')
