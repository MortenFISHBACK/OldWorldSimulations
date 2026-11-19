#!/usr/bin/env python3
"""Units that 'give way' (THE DEARER SUM KEEPS ITS PLAN): did they move that Movement phase? ON and OFF side."""
import json,glob,os,html,re,collections,sys,math
R=sys.argv[1]; C=collections.Counter(); EX=[]
for j in sorted(glob.glob(os.path.join(R,'**/game-*.log.jsonl'),recursive=True)):
  new='Opponent' if '/opp-' in j else 'Mine'; g=os.path.basename(j)[5:-11]
  rows=[json.loads(l) for l in open(j) if l.startswith('{')]
  acts=[r for r in rows if r['kind']=='action']
  pos=collections.defaultdict(list)
  for fr in rows:
    if fr['kind']=='frame':
      for u in fr['units']: pos[u['id']].append((fr['after'],u['x'],u['y']))
  rng={}
  for r in acts:
    if r['phase']=='Movement': k=(r['turn'],r['side']); lo,hi=rng.get(k,(1e18,0)); rng[k]=(min(lo,r['id']),max(hi,r['id']))
  seen=set()
  for r in acts:
    if r['phase']!='Movement' or r['type'] not in ('Computer',): continue
    for m in re.finditer(r'#(\d+) ([^(]+?) gives way',html.unescape(r['summary'] or '')):
      uid=int(m.group(1)); k=(r['turn'],r['side'],uid)
      if k in seen: continue
      seen.add(k); lo,hi=rng[(r['turn'],r['side'])]; P=pos[uid]
      st=[p for p in P if p[0]<lo]; en=[p for p in P if p[0]<=hi]
      if not st or not en: continue
      d=math.hypot(en[-1][1]-st[-1][1],en[-1][2]-st[-1][2]); sd='ON' if r['side']==new else 'OFF'
      C[sd,'gives way']+=1
      if d<0.5: C[sd,'did not move']+=1; EX.append((g,r['turn'],r['side'],m.group(2).strip()))
print(dict(C)); print(EX[:10])
