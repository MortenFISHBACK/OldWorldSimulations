import pickle,collections,re,sys,csv,glob,statistics as st,math
sys.path.insert(0,'/home/user/an')
C=pickle.load(open('/home/user/an/charges2.pkl','rb'))
NG=int(sys.argv[1]) if len(sys.argv)>1 else 288
m=lambda v:sum(v)/max(1,len(v))
TAGS=['BREAK OUTCOMES','OVERRUN ON','STAND AND SHOOT','FLEES FROM CHARGE']
def vp(c): return c['sns_w']/max(1,c['Aw'])*c['Aown'] if c['Aw'] else 0
def tagv(c,t): return [v for tt,v in c['rules'] if tt==t]
ON=[c for c in C if not c['simpler']]; OFF=[c for c in C if c['simpler']]
print('## Charges, ON v OFF (per game = per 288 games, each side plays every game)')
print('| | ON | OFF |\n|---|---|---|')
def row(lab,f): print(f'| {lab} | {f(ON)} | {f(OFF)} |')
row('Charges declared a game',lambda X:f"{len(X)/NG:.2f}")
row('Made contact',lambda X:f"{m([c['res']=='contact' for c in X]):.0%}")
row('Target fled as its reaction',lambda X:f"{m([c['react']=='flee' for c in X]):.0%}")
row('Target stood and shot',lambda X:f"{m([c['react']=='sns' for c in X if c['react']!='flee']):.0%} of stood")
row('S&S VP lost per charge where the target stood',lambda X:f"{sum(vp(c) for c in X if c['react']=='sns')/max(1,sum(1 for c in X if c['react']!='flee')):.1f}")
row('First round won (contact)',lambda X:f"{m([c.get('r1')=='win' for c in X if c['res']=='contact' and c.get('r1') in('win','loss','draw')]):.0%}")
row('Net points per contact charge, 2 turns',lambda X:f"{m([c['t_2t']-c['a_2t'] for c in X if c['res']=='contact']):+.0f}")
row('Net points per declared charge, 2 turns',lambda X:f"{m([c['t_2t']-c['a_2t'] for c in X]):+.0f}")
print()
print('### Outcome of contact charges (share, net points two turns later)')
print('| Outcome | ON share | ON net | OFF share | OFF net |\n|---|---|---|---|---|')
cl=collections.defaultdict(lambda:[[],[]])
for c in C:
    if c['res']=='contact': cl[c['cls']][0 if not c['simpler'] else 1].append(c)
non=sum(len(v[0]) for v in cl.values()); noff=sum(len(v[1]) for v in cl.values())
for k in sorted(cl,key=lambda k:-len(cl[k][0])-len(cl[k][1])):
    a,b=cl[k]; print(f"| {k} | {len(a)/non:.1%} | {m([c['t_2t']-c['a_2t'] for c in a]):+.0f} | {len(b)/noff:.1%} | {m([c['t_2t']-c['a_2t'] for c in b]):+.0f} |")
print()
print('## Per switch (ON side): how often, what it claimed, what happened')
for t in TAGS:
    X=[c for c in ON if tagv(c,t)]
    print(f'\n### {t}: on {len(X)} declared charges ({len(X)/NG:.2f} a game), claimed {m([sum(tagv(c,t)) for c in X]):+.1f} VP each')
    con=[c for c in X if c['res']=='contact']
    if t=='BREAK OUTCOMES':
        cc=collections.Counter(c['cls'] for c in con)
        print('outcomes:',', '.join(f"{k} {v/len(con):.0%}" for k,v in cc.most_common(6)),f"| net 2 turns {m([c['t_2t']-c['a_2t'] for c in con]):+.0f}")
        for lab,sel in (('claimed up (+)',lambda c:sum(tagv(c,t))>0),('claimed down (-)',lambda c:sum(tagv(c,t))<=0)):
            v=[c for c in con if sel(c)]
            print(f"- {lab}: {len(v)} contact, gives ground/falls back {m([c['cls'] in ('win-gg','win-fbigo') for c in v]):.0%}, won r1 {m([c.get('r1')=='win' for c in v]):.0%}, net {m([c['t_2t']-c['a_2t'] for c in v]):+.0f}")
    if t=='OVERRUN ON':
        print(f"contact {len(con)}; went on into a fresh enemy {m([bool(c.get('fresh')) for c in con]):.0%} (OFF side, all charges: {m([bool(c.get('fresh')) for c in OFF if c['res']=='contact']):.0%}); fresh enemy points lost when it did {m([c.get('fresh_lost',0) for c in con if c.get('fresh')]):.0f}; claimed {m([sum(tagv(c,t)) for c in con]):+.1f}")
    if t=='STAND AND SHOOT':
        print(f"target actually stood and shot {m([c['react']=='sns' for c in X]):.0%}; VP lost to the volley {m([vp(c) for c in X]):.1f} (claimed {m([-sum(tagv(c,t)) for c in X]):.1f}); zero-wound volleys {m([c['sns_w']==0 for c in X if c['react']=='sns']):.0%}")
    if t=='FLEES FROM CHARGE':
        print(f"target actually fled {m([c['react']=='flee' for c in X]):.0%} (claimed: flees); redirected {m([c['redirect'] for c in X]):.0%}; target gone within 2 turns {m([c['T_gone_2t'] for c in X if c['react']=='flee']):.0%}; net 2 turns {m([c['t_2t']-c['a_2t'] for c in X]):+.0f} (claimed {m([sum(tagv(c,t)) for c in X]):+.1f} change)")
print('\n## Stand & Shoot by defending army (charges where the target stood)')
print('| Defender | ON charges | ON S&S | ON VP lost/charge | OFF charges | OFF S&S | OFF VP lost/charge |\n|---|---|---|---|---|---|---|')
by=collections.defaultdict(lambda:[[],[]])
for c in C:
    if c['react']!='flee': by[c['army_def']][1 if c['simpler'] else 0].append(c)
for k,(a,b) in sorted(by.items(),key=lambda kv:-sum(vp(c) for c in kv[1][0]+kv[1][1])/max(1,len(kv[1][0]+kv[1][1]))):
    f=lambda X:f"{len(X)} | {m([c['react']=='sns' for c in X]):.0%} | {sum(vp(c) for c in X)/max(1,len(X)):.1f}"
    print(f"| {k} | {f(a)} | {f(b)} |")
