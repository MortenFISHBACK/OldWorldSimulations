import json,glob,os,html,re,collections,sys
R=sys.argv[1]; C=collections.Counter()
for j in glob.glob(os.path.join(R,'**/game-*.log.jsonl'),recursive=True):
  new='Opponent' if '/opp-' in j else 'Mine'
  acts=[json.loads(l) for l in open(j) if l.startswith('{"kind":"action"')]
  claim={}
  for r in acts:
    if r['side']==new and r['type']=='OpponentRule':
      m=re.search(r'HOLD ODDS: (Marker \d+)[^-\]]*- arrives in (\d+)',html.unescape(r['summary'] or ''))
      if m: claim[(r['turn'],r['actor_id'])]=(m.group(1),int(m.group(2)))
  for r in acts:
    if r['side']!=new or r['phase']!='Movement' or r['type']!='JobSplit': continue
    c=claim.get((r['turn'],r['actor_id']))
    if not c or c[1]<2: continue
    s=html.unescape(r['summary']); rows=s.split(' | ')
    for x in rows:
      if '[TAKEN]' not in x: continue
      onto=f'onto {c[0]}' in x
      cr=re.search(re.escape(c[0])+r' \([^)]*\) in (\d+) more turns?|'+re.escape(c[0])+r' in (\d+) more turns?',x)
      C['far walk taken rows']+=1
      if onto: C['taken = onto that marker']+=1
      elif cr: C['taken elsewhere, still credits the walk']+=1
      else: C['taken elsewhere, no walk credit']+=1
    others=[x for x in rows if '[TAKEN]' not in x and 'more turn' in x and c[0] in x]
    C['other rows weighed crediting the walk']+=len(others)
print(dict(C))
