import pickle,collections,re
C=pickle.load(open('charges.pkl','rb'))
def classify(c):
    if c['res']!='contact': return None
    r=c.get('r1')
    if r in (None,'nofight','?'): return 'nofight'
    if r=='draw': return 'draw'
    ev=c.get('after',[])
    def bt(h):
        o=None;mv=None
        for t,a,ha,side,s in ev:
            if ha!=h: continue
            if t=='BreakTest':
                if 'breaks and flees' in s or 'would fall back in good order, but' in s or 'breaks' in s and 'flees' in s: o='flee'
                elif 'falls back in good order' in s: o='fbigo'
                elif 'gives ground' in s: o='gg'
                else: o=o or 'bt?'
            if t=='BreakTestMove':
                mv=s
                if o is None: o='flee' if 'breaks and flees' in s else 'fbigo' if 'falls back' in s else 'gg' if 'gives ground' in s else None
        return o,mv
    if r=='win':
        o,mv=bt(c['hT'])
        c['off']=bool(mv and 'destroyed' in mv)
        if o is None:
            return 'win-wipe' if c['T_gone_r1'] else 'win-other'
        return 'win-'+o
    else:
        o,mv=bt(c['hA'])
        c['offA']=bool(mv and 'destroyed' in mv)
        if o is None: return 'loss-wipe' if c['A_gone_r1'] else 'loss-other'
        return 'loss-'+o
def winner_moves(c):
    """what the charger did after a won round"""
    d=collections.Counter()
    for t,a,ha,side,s in c.get('after',[]):
        if ha!=c['hA']: continue
        if t=='Pursuit':
            if 'catches and destroys' in s: d['caught']+=1
            elif 're-engages' in s: d['reengage']+=1
            elif 'fresh enemy' in s: d['pursue-fresh']+=1
            elif 'off the table' in s: d['pursue-off']+=1
            else: d['pursue-nocatch']+=1
        elif t=='PursuitIntoFreshEnemy': d['fresh']+=1
        elif t=='Overrun':
            d['overrun']+=1
            if 'off the table' in s: d['overrun-off']+=1
            if 'stops against' in s and 'impassable' not in s: d['overrun-stopped']+=1
        elif t=='FollowUp': d['followup']+=1
        elif t=='RestrainAndReform':
            if 'stays and reforms' in s or 'automatically' in s: d['restrain']+=1
            else: d['restrain-failed']+=1
    return d
for c in C:
    c['cls']=classify(c); c['wm']=winner_moves(c) if c['res']=='contact' else collections.Counter()
pickle.dump(C,open('charges2.pkl','wb'))
if __name__=='__main__':
    def table(sel,label):
        X=[c for c in C if sel(c) and c['res']=='contact']
        n=len(X); print('\n==',label,'contact charges',n)
        print(f"{'class':12s} {'n':>5s} {'share':>6s} {'Tpts':>5s} {'Apts':>5s} {'t_r1':>5s} {'a_r1':>5s} {'net1':>5s} {'t_2t':>5s} {'a_2t':>5s} {'net2':>5s} {'later':>6s} {'Tgone2':>6s} {'Agone2':>6s}")
        cl=collections.defaultdict(list)
        for c in X: cl[c['cls']].append(c)
        m=lambda v:sum(v)/max(1,len(v))
        for k in sorted(cl,key=lambda k:-len(cl[k]))+['ALL']:
            v=X if k=='ALL' else cl[k]
            print(f"{k:12s} {len(v):5d} {len(v)/n:6.1%} {m([c['Tpts'] for c in v]):5.0f} {m([c['Apts'] for c in v]):5.0f} {m([c['t_r1'] for c in v]):5.0f} {m([c['a_r1'] for c in v]):5.0f} {m([c['t_r1']-c['a_r1'] for c in v]):5.0f} {m([c['t_2t'] for c in v]):5.0f} {m([c['a_2t'] for c in v]):5.0f} {m([c['t_2t']-c['a_2t'] for c in v]):5.0f} {m([(c['t_2t']-c['t_r1'])-(c['a_2t']-c['a_r1']) for c in v]):6.0f} {m([c['T_gone_2t'] for c in v]):6.0%} {m([c['A_gone_2t'] for c in v]):6.0%}")
    table(lambda c:c['simpler'],'SIMPLER side, all 3 batches')
    table(lambda c:c['simpler'] and c['batch'].startswith('one-sum'),'SIMPLER side, one-sum batch (v main)')
    table(lambda c:True,'ALL sides')
