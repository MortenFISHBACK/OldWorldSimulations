import json,glob,os,re,collections,html,sys
R=sys.argv[1];C=collections.Counter()
for j in glob.glob(os.path.join(R,'**/game-*.log.jsonl'),recursive=True):
  new='Opponent' if '/opp-' in j else 'Mine'
  for l in open(j):
    if 'WALK CHECK' not in l: continue
    r=json.loads(l)
    if r.get('side')!=new: continue
    s=html.unescape(r.get('summary') or ''); i=s.find('WALK CHECK'); s=s[i:]
    m=re.search(r'the spot nearest it: .*? - rank (\d+) of (\d+)',s)
    if not m: C['no nearest spot']+=1; continue
    C['checks']+=1; C['nearest ranked 1st' if m.group(1)=='1' else 'nearest not 1st']+=1
    t=re.search(r'\| taken: (.*)$',s); tk=t.group(1) if t else ''
    C['taken = nearest spot' if tk.startswith('that spot') else 'taken elsewhere']+=1
    if 'carries no walk' in s.split('| taken')[0]: C['nearest carries no walk']+=1
print(dict(C))
