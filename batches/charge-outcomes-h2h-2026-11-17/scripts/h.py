import csv,glob,statistics as st,math,collections,json,os
D='/mnt/project-files/charge-outcomes-h2h-2026-11-17'
rows=[]
for arm in ('mine','opp'):
  for f in sorted(set(glob.glob(f'{D}/{arm}-*/games.csv')+glob.glob(f'{D}/{arm}-*/*/games.csv'))):
    if '/parts/' in f: continue
    for r in csv.DictReader(open(f)):
      if r['ended']!='yes': continue
      fw,off=('mine','opponent') if arm=='mine' else ('opponent','mine')
      m,o=map(int,r['vp_mine_opponent'].split('-')); v={'mine':m,'opponent':o}
      win=r['winner'].lower()
      res='D' if win=='draw' else ('W' if win==fw else 'L')
      g=dict(arm=arm,pair=r['pair'],sc=r['scenario'],margin=v[fw]-v[off],res=res,fwfirst=r['first_player'].lower()==fw,
        fwarmy=r.get(f'army_{fw}') ,)
      for k in ('vp_kills','vp_objectives','vp_leaders','vp_other','units_lost','points_lost'):
        g[k+'_fw']=float(r[f'{k}_{fw}'] or 0); g[k+'_off']=float(r[f'{k}_{off}'] or 0)
      rows.append(g)
by=collections.defaultdict(dict)
for g in rows: by[g['pair']][g['arm']]=g
matched=[p for p,v in by.items() if len(v)==2]
M=[g for p in matched for g in by[p].values()]
print('games',len(rows),'matched pairs',len(matched))
def band(xs): return 1.96*st.stdev(xs)/math.sqrt(len(xs))
pairsum=[by[p]['mine']['margin']+by[p]['opp']['margin'] for p in matched]
print(f"ALL matched: {st.mean(g['margin'] for g in M):+.0f} paired ±{band(pairsum)/2:.0f}; pairs ahead/behind {sum(x>0 for x in pairsum)}/{sum(x<0 for x in pairsum)}")
def line(lab,rs):
  c=collections.Counter(g['res'] for g in rs); ms=[g['margin'] for g in rs]
  print(f"| {lab} | {len(rs)} | {st.mean(ms):+.0f} | ±{band(ms):.0f} | {c['W']} / {c['D']} / {c['L']} |")
line('All matched',M)
line('fw Mine',[g for g in M if g['arm']=='mine']); line('fw Opp',[g for g in M if g['arm']=='opp'])
line('fw first',[g for g in M if g['fwfirst']]); line('fw second',[g for g in M if not g['fwfirst']])
for k in ('vp_kills','vp_objectives','vp_leaders','vp_other','units_lost','points_lost'):
  print(k, f"{st.mean(g[k+'_fw'] for g in M):.1f}", f"{st.mean(g[k+'_off'] for g in M):.1f}")
