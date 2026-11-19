import json,sys,collections
d=json.load(open(sys.argv[1])); N=int(sys.argv[2])
fr=[f['name'] for f in d['shared']['frames']]
ow=[n.startswith('OldWorldWarTable.Web!') for n in fr]
def walk(p):
    inc=collections.Counter(); slf=collections.Counter(); game=0.0
    st=[]; last=None
    for e in p['events']:
        t=e['at']
        if last is not None and st and t>last:
            dt=t-last
            if any(ow[i] for i in st):
                game+=dt
                for n in set(fr[i] for i in st): inc[n]+=dt
                slf[fr[st[-1]]]+=dt
        last=t
        if e['type']=='O': st.append(e['frame'])
        else:
            if st and st[-1]==e['frame']: st.pop()
            elif e['frame'] in st: st.remove(e['frame'])
    return game,inc,slf
best=max((walk(p)+(p['name'],) for p in d['profiles']),key=lambda x:x[0])
game,inc,slf,name=best
print('thread',name,'game ms',round(game),'window ms',round(d['profiles'][0]['endValue']-d['profiles'][0]['startValue']))
sh=lambda n:n.split('!')[-1][:160]
k=0
for n,v in inc.most_common(3000):
    if n.startswith('OldWorldWarTable.Web!'):
        print(f'{100*v/game:5.1f}%  {sh(n)}'); k+=1
        if k>=N: break
print('--- self top')
for n,v in slf.most_common(20): print(f'{100*v/game:5.1f}%  {sh(n)}')
