import pickle,collections,sys
R=pickle.load(open('reach.pkl','rb')); C={(c['file'],c['arm'],c['i']):c for c in pickle.load(open('scripts/charges.pkl','rb'))}
def cause(c,b):
    res=b['res'] or 'none'
    if b['T0_fleeing'] or c.get('Tfl'): pre='target already fleeing: '
    else: pre=''
    if res=='contact' and not b['redirect']: return pre+'contact'
    if b['redirect']: return 'fled, redirected: '+('contact' if res=='contact' else 'no contact')
    if res.startswith('chase'): return pre+('fled as reaction: caught' if res=='chase-caught' else 'fled as reaction: got away')
    if res=='short': return pre+'dice short'
    if res=='halted': return pre+'halted (way blocked)'
    return pre+res[:30]
rows=[]
for c in R:
    b=C[(c['file'],c['arm'],c['i'])]; c['cause']=cause(c,b); c['res']=b['res']; c['react']=b['react']; c['Att']=b['Att']; rows.append(c)
pickle.dump(rows,open('reach2.pkl','wb'))
def tab(rows,title):
    print('\n##',title,len(rows))
    k=collections.Counter(c['cause'] for c in rows)
    for a,n in k.most_common(): 
        cl=[c['claim'] for c in rows if c['cause']==a and c['claim'] is not None]
        print(f"{n:4d} {n/len(rows):5.0%}  claim {sum(cl)/len(cl) if cl else float('nan'):.2f} ({len(cl)})  {a}")
tab(rows,'all declared'); tab([c for c in rows if c['new']],'new side'); tab([c for c in rows if not c['new']],'simpler side')
P=[c for c in rows if c['claim'] is not None and c['taken']]
tab(P,'planned (taken charge job on that target)'); tab([c for c in P if c['new']],'planned new'); tab([c for c in P if not c['new']],'planned simpler')
tab([c for c in rows if c['claim'] is None],'no charge option for that target in the job split')
tab([c for c in rows if c['claim'] is not None and not c['taken']],'option not taken yet declared')
for c in [c for c in rows if c['claim'] is None][:25]: print(c['file'],c['turn'],c['An'],'->',c['Tn'],c.get('why'),c['cause'])
