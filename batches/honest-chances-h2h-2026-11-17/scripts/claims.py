# Claimed v happened from the split log. Usage: python3 claims.py <merged root with mine/ and opp/>
import sys,os,glob,json,re,collections,statistics as st
M=sys.argv[1]; ON={'mine':'Mine','opp':'Opponent'}
PCT=lambda k,s:(lambda m:float(m.group(1))/100 if m else None)(re.search(k+r' (\d+(?:\.\d+)?)%',s))
def opts(s):
  for o in s.split(' | ')[1:]:
    m=re.match(r'^(\d+)\. (.*)$',o,re.S)
    if m: yield m.group(2)
C=collections.defaultdict(list)   # (brain, measure) -> list of (claimed, happened)
NX=collections.defaultdict(list)
for arm in ('mine','opp'):
  for f in sorted(glob.glob(f'{M}/{arm}/game-*.log.jsonl')):
    A=[];U={}
    for l in open(f):
      try: d=json.loads(l)
      except ValueError: continue
      if d.get('kind')=='action': A.append(d)
      elif d.get('kind')=='board': U={u['id']:u['n'] for u in d['units']}
    for i,a in enumerate(A):
      if a.get('type')!='JobSplit': continue
      side=a.get('side'); brain='honest' if side==ON[arm] else 'simpler'; turn=a.get('turn'); me=a.get('actor_id')
      for o in opts(a.get('summary') or ''):
        if '[TAKEN]' not in o: continue
        m=re.match(r'^charge #(\d+) ',o)
        if m:
          T=int(m.group(1)); name=U.get(T,'?')
          later=[b for b in A[i+1:] if b.get('turn')==turn]
          seg=[]; fought=False
          for b in later:
            if b.get('phase')=='Combat': fought=True
            elif fought: break
            seg.append(b)
          dec=next((b for b in seg if b.get('type')=='Charge' and b.get('actor_id')==me and 'declares a charge' in (b.get('summary') or '')),None)
          if not dec or dec.get('target_id')!=T: C[(brain,'declared as picked')].append((1,0)); continue
          C[(brain,'declared as picked')].append((1,1))
          con=next((b for b in seg if b.get('type')=='Charge' and b.get('actor_id')==me and 'made contact' in (b.get('summary') or '')),None)
          C[(brain,'reach')].append((PCT('reach',o),1 if con else 0))
          ss=sum(int(x) for b in seg if b.get('type')=='Shooting' and b.get('actor_id')==T and b.get('target_id')==me and (not con or b['id']<con['id']) for x in re.findall(r'(\d+) wound\(s\)',b.get('summary') or ''))
          sm=re.search(r'stand & shoot ~(\d+(?:\.\d+)?) wounds',o)
          if sm: C[(brain,'stand & shoot wounds (number)')].append((float(sm.group(1)),ss))
          short=next((b for b in seg if b.get('type')=='Charge' and b.get('actor_id')==me and 'fell short' in (b.get('summary') or '')),None)
          if con or short: C[(brain,'reach (charges not fled from)')].append((PCT('reach',o),1 if con else 0))
          if not con: continue
          cs=[b for b in seg if b['id']>con['id'] and b.get('phase')=='Combat']
          bt=next((b for b in cs if b.get('type')=='BreakTest' and b.get('actor_id') in (T,me)),None)
          wiped=next((b for b in cs if b.get('type')=='CombatResult' and (b.get('summary') or '').startswith(name+' wiped out')),None)
          btm=next((b for b in cs if b.get('type')=='BreakTestMove' and b.get('actor_id')==T),None)
          s=(btm or {}).get('summary') or ''
          fi=next((k for k,b in enumerate(cs) if b.get('type')=='Computer' and (b.get('summary') or '').startswith('Fights the combat: ') and U.get(me,'#') in b['summary']),None)
          res=next((b for b in cs[fi:] if b.get('type')=='CombatResult'),None) if fi is not None else None
          rs=(res or {}).get('summary') or ''
          if 'wiped out' in rs: won = rs.split(' wiped out')[0]!=U.get(me) and side in rs.split('- ')[-1]
          elif ' wins' in rs: won = rs.rstrip().endswith(side+' wins')
          elif 'drawn' in rs: won=False
          else: won=None
          if won is not None: C[(brain,'win (first round)')].append((PCT('win',o),1 if won else 0))
          oc=re.search(r'outcomes: (.*?)counted',o)
          if not oc or won is None: continue
          oc=oc.group(1)
          flee=' breaks and flees' in s
          C[(brain,'slain')].append((PCT('slain',oc),1 if wiped else 0))
          C[(brain,'flees')].append((PCT('flees',oc),1 if flee else 0))
          C[(brain,'falls back')].append((PCT('falls back',oc),1 if 'falls back in good order' in s else 0))
          C[(brain,'gives ground')].append((PCT('gives ground',oc),1 if 'gives ground' in s else 0))
          C[(brain,'any of the four (target loses)')].append((sum(PCT(k,oc) or 0 for k in ('slain','flees','falls back','gives ground')),1 if (wiped or flee or 'falls back in good order' in s or 'gives ground' in s) else 0))
          if flee:
            rest=A[A.index(btm):]
            pts=any((b.get('actor_id')==T and 'destroyed' in (b.get('summary') or '')) or ('catches and destroys '+name) in (b.get('summary') or '') or (b.get('summary') or '').startswith(name+' wiped out') for b in rest)
            C[(brain,'a flee ends as points (of flees)')].append((PCT('a flee ends as points',oc),1 if pts else 0))
          continue
        m=re.match(r'^close in to charge #(\d+) .*?next turn',o)
        if m:
          T=int(m.group(1)); reach=PCT('reach',o); share=PCT('share',o)
          if reach is None: continue
          claim=reach*(0.22 if brain=='honest' else (share or 0.5))
          nxt=[b for b in A[i+1:] if b.get('turn')==turn+1 and b.get('side')==side and b.get('type')=='Charge' and b.get('actor_id')==me]
          decl=any('declares a charge' in (b.get('summary') or '') and b.get('target_id')==T for b in nxt)
          cont=any('made contact' in (b.get('summary') or '') and b.get('target_id')==T for b in nxt)
          NX[(brain,'close-in job: charges that target next turn')].append((claim,1 if decl else 0))
          NX[(brain,'close-in job: contact with it next turn')].append((claim,1 if cont else 0))
          NX[(brain,'close-in job: reach claimed v contact')].append((reach,1 if cont else 0))
    # measured move spots (honest side only, the row names the target by name)
    for i,a in enumerate(A):
      s=a.get('summary') or ''
      if a.get('type')=='OpponentRule' and s.startswith('MEASURED NEXT CHARGE') and 'counted' in s:
        m=re.search(r': charge (.+?) next turn \(MEASURED NEXT CHARGE: reach (\d+)%, counted (\d+)%',s)
        if not m: continue
        me=a.get('actor_id'); side=a.get('side'); turn=a.get('turn')
        nxt=[b for b in A[i+1:] if b.get('turn')==turn+1 and b.get('side')==side and b.get('type')=='Charge' and b.get('actor_id')==me and 'made contact' in (b.get('summary') or '')]
        hit=any((b.get('summary') or '').startswith(f"{b.get('actor')} charges {m.group(1)}:") for b in nxt)
        NX[('honest','move spot (measured): contact next turn')].append((int(m.group(3))/100,1 if hit else 0))
def show(D,title):
  print(f'\n### {title}\n\n| Measure | Side | Picks | Claimed | Happened |\n| --- | --- | --- | --- | --- |')
  for k in sorted(D,key=lambda k:(k[1],k[0])):
    xs=[x for x in D[k] if x[0] is not None]
    if not xs: continue
    num='number' in k[1]
    cl=st.mean(x[0] for x in xs); hp=st.mean(x[1] for x in xs)
    f=(lambda v:f'{v:.2f}') if num else (lambda v:f'{100*v:.0f}%')
    print(f'| {k[1]} | {k[0]} | {len(xs)} | {f(cl)} | {f(hp)} |')
show(C,'Charge picks: the chance the computer logged v what happened (charges declared as picked)')
show(NX,"Next turn's charge: the counted chance v what happened")

