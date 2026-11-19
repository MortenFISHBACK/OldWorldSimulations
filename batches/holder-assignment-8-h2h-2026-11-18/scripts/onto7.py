#!/usr/bin/env python3
"""Batch 7: ON-side CANDIDATES MOVE rows with ONTO: is the best spot onto the given objective taken? By walk claim (near/far) or hold."""
import json,glob,os,html,re,collections,sys
R=sys.argv[1]; C=collections.Counter(); EX=collections.defaultdict(list); GAP=collections.defaultdict(list)
ONTO=re.compile(r'ONTO (.+?): (?:rank (\d+) of (\d+), ([+-][\d.]+) VP|no spot in its range weighed)')
for j in sorted(glob.glob(os.path.join(R,'**/game-*.log.jsonl'),recursive=True)):
  new='Opponent' if '/opp-' in j else 'Mine'; g=os.path.basename(j)[5:-11]
  acts=[json.loads(l) for l in open(j) if l.startswith('{"kind":"action"')]
  walk={}
  for r in acts:
    if r.get('type')=='OpponentRule' and r.get('side')==new:
      s=html.unescape(r['summary'] or '')
      for m in re.finditer(r'HOLD ODDS: (Marker \d+[^-\]]*?) - arrives in (\d+)',s): walk[(r['turn'],r['actor_id'])]=(m.group(1).strip(),int(m.group(2)))
  for r in acts:
    if r.get('type')!='Candidates' or r.get('phase')!='Movement' or r.get('side')!=new: continue
    s=html.unescape(r['summary'] or ''); m=ONTO.search(s)
    if not m: continue
    obj=m.group(1); kind='marker' if obj.startswith('Marker') else obj.split()[1] if obj.startswith('The ') else obj[:20]
    w=walk.get((r['turn'],r['actor_id']))
    cls=('walk far' if w[1]>=2 else 'walk near') if w and w[0].split(' (')[0]==obj.split(' (')[0] else ('hold/other '+kind)
    taken=re.search(r'(\d+)\. ([+-][\d.]+) VP: [^|]*\[TAKEN\]',s)
    C[cls,'n']+=1
    if not m.group(2): C[cls,'no spot weighed']+=1; EX[cls,'none'].append((g,r['turn'],r['actor'])); continue
    rk=int(m.group(2))
    if taken and rk==int(taken.group(1)): C[cls,'took the ONTO spot']+=1
    else:
      C[cls,'took another']+=1
      if taken: GAP[cls].append(float(taken.group(2))-float(m.group(4)))
      EX[cls,'other'].append((g,r['turn'],r['actor'],rk))
    if rk==1: C[cls,'ONTO rank 1']+=1
for cls in sorted({k[0] for k in C}):
  gp=sorted(GAP[cls]); med=gp[len(gp)//2] if gp else 0
  print(f"{cls}: rows {C[cls,'n']}, took the best ONTO spot {C[cls,'took the ONTO spot']}, took another {C[cls,'took another']} (median VP gap {med:.1f}), no spot in range weighed {C[cls,'no spot weighed']}")
for k,v in EX.items():
  if k[0].startswith('walk'): print(k, v[:6])
