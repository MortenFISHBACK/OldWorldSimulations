#!/usr/bin/env python3
"""Lead check: taken 'wider search' spots (A ahead, B to the side, keeping its facing) v the unit's real move that turn; and REAL GROUND claims."""
import json,glob,os,html,re,collections,sys,math
R=sys.argv[1]; C=collections.Counter(); D=[]; EX=[]
for j in sorted(glob.glob(os.path.join(R,'**/game-*.log.jsonl'),recursive=True)):
  new='Opponent' if '/opp-' in j else 'Mine'; g=os.path.basename(j)[5:-11]
  acts=[json.loads(l) for l in open(j) if l.startswith('{"kind":"action"')]
  for r in acts:
    if r.get('side')==new and r.get('type')=='OpponentRule' and 'REAL GROUND:' in (r.get('summary') or ''):
      C['real ground claims']+=1
      m=re.search(r'make it (\d+) turns?, (\d+) by the straight line',html.unescape(r['summary']))
      if m: C['rg diff %+d'%(int(m.group(1))-int(m.group(2)))]+=1
    if r.get('phase')!='Movement' or r.get('type')!='JobSplit': continue
    s=html.unescape(r.get('summary') or '')
    t=s.split('[TAKEN]')[0]
    m=re.search(r'wider search found: ([\d.]+)" ahead and ([\d.]+)" to the side, keeping its facing',t)
    if not m or '[TAKEN]' not in s: continue
    plan=math.hypot(float(m.group(1)),float(m.group(2)))
    mv=[q for q in acts if q.get('actor_id')==r['actor_id'] and q.get('turn')==r['turn'] and q.get('phase')=='Movement' and q.get('type') in ('Move','March','Reform','Wheel','Turn') and q.get('from') and q['from'][0] is not None and q.get('to') and q['to'][0] is not None]
    side=r.get('side'); C[side==new and 'ON' or 'OFF','taken']+=1
    if not mv: C['no move row']+=1; EX.append((g,r['turn'],r['actor'],'no move row',round(plan,1))); continue
    a,b=mv[0]['from'],mv[-1]['to']; real=math.hypot(b[0]-a[0],b[1]-a[1])
    D.append(real-plan)
    if real<plan-1: C['short by 1"+']+=1; EX.append((g,r['turn'],r['actor'],[q['type'] for q in mv],round(plan,1),round(real,1)))
    else: C['reached (within 1")']+=1
print(dict(C)); D.sort(); print('real minus planned: median %.1f, n %d'%(D[len(D)//2],len(D)) if D else '')
for e in EX[:15]: print(e)
