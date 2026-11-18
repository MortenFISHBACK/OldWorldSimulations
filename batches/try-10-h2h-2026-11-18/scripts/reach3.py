import pickle,collections
R=pickle.load(open('reach2.pkl','rb'))
P=[c for c in R if c['claim'] is not None]
held=[c for c in P if c['cause'] in('contact','dice short','halted (way blocked)','none')]
def line(lab,rows):
    if not rows: return
    n=len(rows); cl=sum(c['claim'] for c in rows)/n; ct=sum(c['cause']=='contact' for c in rows)/n
    sh=sum(c['cause']=='dice short' for c in rows)/n; ha=sum(c['cause'].startswith('halted') for c in rows)/n
    print(f"| {lab} | {n} | {cl:.0%} | {ct:.0%} | {sh:.0%} | {ha:.0%} |")
print('HELD targets: claim v contact'); print('| | n | claimed | contact | dice short | halted |')
line('all',held); line('new',[c for c in held if c['new']]); line('simpler',[c for c in held if not c['new']])
def band(g):
    if g is None: return '?'
    for l in (3,6,9,12,15): 
        if g<l: return f'<{l}'
    return '15+'
for b in ['<3','<6','<9','<12','<15','15+','?']: line('gap '+b,[c for c in held if band(c.get('gap'))==b])
for lo,hi in ((0,.5),(.5,.75),(.75,.9),(.9,.995),(.995,1.01)): line(f'claim {lo}-{hi}',[c for c in held if lo<=c['claim']<hi])
tt=collections.Counter(c['Att'] for c in held)
for t,_ in tt.most_common(): line(str(t),[c for c in held if c['Att']==t])
print('\nALL with claim: reaction share by target'); 
def fl(lab,rows):
    if not rows: return
    n=len(rows); f=sum('fled' in c['cause'] for c in rows); ct=sum(c['cause'] in('contact','fled, redirected: contact','fled as reaction: caught') for c in rows)
    print(f"| {lab} | {n} | {sum(c['claim'] for c in rows)/n:.0%} | {f/n:.0%} | {ct/n:.0%} |")
fl('all',P); fl('new',[c for c in P if c['new']]); fl('simpler',[c for c in P if not c['new']])
for a in ('front','flank','rear'): fl('arc '+a,[c for c in P if c['arc']==a])
for lo,hi in ((0,.5),(.5,.8),(.8,.95),(.95,1.01)): fl(f'win {lo}-{hi}',[c for c in P if c['win'] is not None and lo<=c['win']<hi])
tn=collections.Counter()
for c in P:
    tn[c['Tn'].rstrip(' 0123456789')]+=1
print('\nfleeing targets by name:')
ff=collections.Counter(c['Tn'].rstrip(' 0123456789') for c in P if 'fled' in c['cause'])
for k,n in ff.most_common(25): print(n,'/',tn[k],k)
print('\nhalted and none:')
for c in R:
    if c['cause'].startswith('halted') or c['cause']=='none': print(c['file'],c['arm'],c['turn'],c['An'],'->',c['Tn'],c['claim'],round(c.get('gap') or -1,1),c['Att'],c['ev'][:2])
