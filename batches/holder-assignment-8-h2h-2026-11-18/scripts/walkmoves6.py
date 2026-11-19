#!/usr/bin/env python3
"""Every ON-side HOLD ODDS walk claim to a marker: what the unit did in the move phase that turn, and which move row it took.
python3 -I walkmoves6.py <root>"""
import json,glob,os,html,re,collections,sys,math
R=sys.argv[1]; C=collections.Counter(); ROWS=collections.Counter(); EX={}
def kind(t, mkr):
    if f'onto Marker {mkr}' in t or f'next to Marker {mkr}' in t: return 'onto that marker'
    if re.search(r'onto |next to ', t): return 'onto another objective'
    if re.search(r'nearest enemy|go at|close in on|charge|shoot|stopping \d+" short', t): return 'toward or against an enemy'
    if 'wider search' in t: return 'a spot the wider search found'
    if re.search(r'stays|stand', t): return 'stays where it is'
    return 'other'
for j in sorted(glob.glob(os.path.join(R,'**/game-*.log.jsonl'),recursive=True)):
  new='Opponent' if '/opp-' in j else 'Mine'
  acts=[json.loads(l) for l in open(j) if l.startswith('{"kind":"action"')]
  for r in acts:
    if r.get('type')!='OpponentRule' or r.get('side')!=new: continue
    s=html.unescape(r['summary']); m=re.search(r'HOLD ODDS: Marker (\d+)[^-]*- arrives in (\d+)',s)
    if not m: continue
    mkr=m.group(1); far='far (2+ more turns)' if int(m.group(2))>=2 else 'near (1 more turn)'
    mine=[q for q in acts if q.get('actor_id')==r['actor_id'] and q.get('turn')==r['turn'] and q.get('phase') in ('Strategy','Movement')]
    job=next((html.unescape(q['summary']) for q in mine if q['type']=='Candidates' and q['phase']=='Strategy'),'')
    jt=re.search(r'(\d+)\. [+-][\d.]+ VP: ([^|]*?) \[TAKEN\]',job)
    sp=next((html.unescape(q['summary']) for q in mine if q['type']=='JobSplit' and q['phase']=='Movement'),None)
    cm=next((html.unescape(q['summary']) for q in mine if q['type']=='Candidates' and q['phase']=='Movement'),'')
    if not sp: k='no move row (did not move)'; rank='-'
    else:
        t=sp.split('[TAKEN]')[0]; k=kind(t,mkr)
        n=re.search(r'MOVE: (\d+) weighed',cm); rank=None
        for mm in re.finditer(r'(\d+)\. [+-][\d.]+ VP: ([^|]*)',cm):
            if '[TAKEN]' in mm.group(2): rank=mm.group(1)
        # rank of the best row going onto that marker
        onto=[mm.group(1) for mm in re.finditer(r'(\d+)\. ([+-][\d.]+) VP: ([^|]*)',cm) if f'Marker {mkr}' in mm.group(3)]
        C[far,'a row onto that marker was weighed']+=bool(onto)
    C[far,k]+=1; C[far,'n']+=1; C['job',jt.group(2).strip()[:40] if jt else '?']+=1
    ROWS[far,k,'taken row '+(str(rank) if rank else '?')]+=1
    EX.setdefault((far,k),(os.path.basename(j),r['turn'],r['actor'],(sp or '')[:300]))
for f in ('near (1 more turn)','far (2+ more turns)'):
    print(f"\n## {f}: {C[f,'n']} walk claims; a move row onto that marker was among the rows weighed: {C[f,'a row onto that marker was weighed']}")
    for k in ('onto that marker','onto another objective','toward or against an enemy','a spot the wider search found','stays where it is','other','no move row (did not move)'):
        if C[f,k]:
            rk=', '.join(f"{x[2].split()[-1]}:{ROWS[x]}" for x in sorted(ROWS) if x[0]==f and x[1]==k)
            print(f"  {k}: {C[f,k]}  (rank of the taken row in CANDIDATES MOVE: {rk})")
print("\njob picked at the strategy phase (top): "+'; '.join(f"{k[1]} {v}" for k,v in C.most_common() if k[0]=='job'))
print("\nexamples:")
for k,v in EX.items(): print(' ',k,v)
