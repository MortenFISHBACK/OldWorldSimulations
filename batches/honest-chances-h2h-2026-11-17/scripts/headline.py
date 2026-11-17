# Headline of the honest-chances h2h. Usage: python3 headline.py <shared dir> <merged root with mine/ and opp/>
import sys,os,csv,glob,statistics as st,math,collections,importlib.util,json
D,M=sys.argv[1],sys.argv[2]
R='/home/user/WarhammerOldWorldSimulator/scripts'
def mod(n,f):
  s=importlib.util.spec_from_file_location(n,f); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
cb=mod('cb',R+'/compare-batches.py'); fc=mod('fc',R+'/flank_charges.py')
ON={'mine':'Mine','opp':'Opponent'}
rows=[]
for arm in ('mine','opp'):
  for r in csv.DictReader(open(f'{M}/{arm}/games.csv')):
    if r['ended']!='yes': continue
    on=ON[arm].lower(); off='opponent' if on=='mine' else 'mine'
    a,b=map(int,r['vp_mine_opponent'].split('-')); v={'mine':a,'opponent':b}
    g=dict(arm=arm,pair=r['pair'],margin=v[on]-v[off],first=r['first_player'].lower()==on)
    for k in ('vp_kills','vp_objectives','vp_leaders','vp_other','points_lost','units_lost'):
      g[k+'_on']=float(r[f'{k}_{on}'] or 0); g[k+'_off']=float(r[f'{k}_{off}'] or 0)
    rows.append(g)
by=collections.defaultdict(dict)
for g in rows: by[g['pair']][g['arm']]=g
pairs=[p for p,v in by.items() if len(v)==2]; Mg=[g for p in pairs for g in by[p].values()]
ps=[by[p]['mine']['margin']+by[p]['opp']['margin'] for p in pairs]
band=1.96*st.stdev(ps)/math.sqrt(len(ps))/2
print(f"games ended {len(rows)}; matched pairs {len(pairs)}; ahead/behind {sum(x>0 for x in ps)}/{sum(x<0 for x in ps)}")
print(f"VP margin honest v simpler: {st.mean(g['margin'] for g in Mg):+.0f} ±{band:.0f}")
for lab,f in (('honest as Mine',lambda g:g['arm']=='mine'),('honest as Opponent',lambda g:g['arm']=='opp'),('honest first',lambda g:g['first']),('honest second',lambda g:not g['first'])):
  xs=[g['margin'] for g in Mg if f(g)]; print(f"  {lab}: {st.mean(xs):+.0f} ({len(xs)})")
for k in ('vp_objectives','vp_kills','vp_leaders','vp_other','points_lost','units_lost'):
  print(f"{k}: honest {st.mean(g[k+'_on'] for g in Mg):.0f}  simpler {st.mean(g[k+'_off'] for g in Mg):.0f}")
# charged fights
F={'on':[],'off':[]}; FL={'on':collections.Counter(),'off':collections.Counter()}; NG=0
for arm in ('mine','opp'):
  per=cb.charged_fights(f'{M}/{arm}')
  for (side,army),v in per.items():
    F['on' if side==ON[arm] else 'off']+=v['fights']
  out,games=fc.flank_charges(f'{M}/{arm}'); NG+=games
  for side,c in out.items(): FL['on' if side==ON[arm] else 'off']+=c
for k in ('on','off'):
  fs=F[k]; fr=[f for f in fs if f[4] is not None]
  print(f"{k}: fights {len(fs)} ({len(fs)/len(rows):.1f}/game); first round won {100*sum(1 for f in fr if f[4])/len(fr):.0f}% of {len(fr)}; net/fight (gone) {st.mean(f[1]-f[2] for f in fs):+.0f}; net/fight (damage) {st.mean(f[7]-f[8] for f in fs):+.0f}")
  c=FL[k]; print(f"   own free units caught in flank/rear per game {c['free_flank']/NG:.2f} (flank {c['flank']} of {c['charged']} charged)")
