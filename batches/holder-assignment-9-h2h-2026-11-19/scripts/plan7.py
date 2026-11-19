#!/usr/bin/env python3
"""Lead check: planned spot ('move to (x, y)' on the unit's rule rows, the taken move) v where the unit stood at the end of its Movement phase."""
import json,glob,os,html,re,collections,sys,math
R=sys.argv[1]; C=collections.Counter(); OUT=[]; BYK=collections.defaultdict(list)
for j in sorted(glob.glob(os.path.join(R,'**/game-*.log.jsonl'),recursive=True)):
  new='Opponent' if '/opp-' in j else 'Mine'; g=os.path.basename(j)[5:-11]
  rows=[json.loads(l) for l in open(j) if l.startswith('{')]
  acts=[r for r in rows if r['kind']=='action']; frames=[r for r in rows if r['kind']=='frame']
  pos={}  # unit -> list of (after, x, y)
  for fr in frames:
    for u in fr['units']: pos.setdefault(u['id'],[]).append((fr['after'],u['x'],u['y'],u.get('f')))
  # movement phase action id ranges per (turn, side)
  rng={}
  for r in acts:
    if r['phase']=='Movement': k=(r['turn'],r['side']); lo,hi=rng.get(k,(1e18,0)); rng[k]=(min(lo,r['id']),max(hi,r['id']))
  done=set()
  for r in acts:
    if r['side']!=new or r['phase']!='Movement' or r['type']!='JobSplit': continue
    s=html.unescape(r['summary'] or ''); key=(r['turn'],r['actor_id'])
    if key in done or '[TAKEN]' not in s: continue
    taken=s.split('[TAKEN]')[0].split('SPLIT: ',1)[-1]
    pr=[html.unescape(q['summary']) for q in acts if q.get('actor_id')==r['actor_id'] and q['turn']==r['turn'] and q['type']=='OpponentRule']
    m=next((re.search(r': move to \(([\d.-]+), ([\d.-]+)\)',p) for p in pr if re.search(r': move to \(',p)),None)
    if not m: continue
    done.add(key); px,py=float(m.group(1)),float(m.group(2))
    lo,hi=rng[(r['turn'],r['side'])]; P=pos.get(r['actor_id'],[])
    st=[p for p in P if p[0]<lo]; en=[p for p in P if p[0]<=hi]
    if not st or not en: continue
    s0,e=st[-1],en[-1]
    plan=math.hypot(px-s0[1],py-s0[2]); miss=math.hypot(px-e[1],py-e[2]); moved=math.hypot(e[1]-s0[1],e[2]-s0[2])
    kind='wider search' if 'wider search' in taken else 'promised spot' if 'priced from' in taken or 'PROMISED' in taken else 'onto objective' if re.search(r'onto |next to ',taken) else 'enemy' if re.search(r'go at|charge|shoot|cast|close in',taken) else 'other'
    C[kind,'n']+=1; BYK[kind].append(miss)
    mt=[q for q in acts if q.get('actor_id')==r['actor_id'] and q['turn']==r['turn'] and q['phase']=='Movement' and q['type'] in ('MarchTest','PanicTest','DangerousTerrain','RandomMovement','Charge','ContinuedFlee','FleeCarriedOn')]
    if miss>1:
      why='march test' if any(q['type']=='MarchTest' for q in mt) else 'charge/flee/random' if mt else 'short' if moved<plan-1 else 'elsewhere'
      C[kind,'why '+why]+=1
    if miss>1: C[kind,'missed 1"+']+=1; OUT.append((miss,why if miss>1 else "",g,r['turn'],r['actor'],kind,round(plan,1),round(moved,1),taken[:110]))
for k in sorted({k[0] for k in C}):
  v=sorted(BYK[k]); print(f"{k}: {C[k,'n']} moves, ended more than 1\" from the planned spot {C[k,'missed 1\"+']}, median miss {v[len(v)//2]:.1f}\" | "+', '.join(f"{w[1][4:]} {C[w]}" for w in sorted(C) if w[0]==k and w[1].startswith('why')))
OUT.sort(reverse=True)
for o in OUT[:20]: print(round(o[0],1),o[1:])
