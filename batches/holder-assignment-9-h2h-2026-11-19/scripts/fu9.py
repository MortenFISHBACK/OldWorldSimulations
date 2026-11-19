import json,glob,os,re,collections,html,sys
R=sys.argv[1];C=collections.Counter();WHY=collections.Counter();AL=[];WC=collections.Counter();OR=0
for j in glob.glob(os.path.join(R,'**/game-*.log.jsonl'),recursive=True):
  new='Opponent' if '/opp-' in j else 'Mine'
  for l in open(j):
    if not l.startswith('{"kind":"action"'): continue
    r=json.loads(l); s=html.unescape(r.get('summary') or '')
    if r.get('side')!=new: continue
    OR+=s.count('ONE ROUTE')
    for m in re.finditer(r'WALK FOLLOW-UP: (.+?) walked on to (.+?) last turn.*?; now: (.*?); \2 (stays empty|stays .*?\'s|goes to )',s):
      now=m.group(3); g=m.group(4)
      k='kept (same unit)' if g.startswith('stays') and 'empty' not in g else 'empty' if 'empty' in g else 'to another unit'
      C[k]+=1
      if now.startswith('no row'):
        C['now: no row']+=1; w=re.sub(r'#\d+','#N',now[len('no row: '):]); w=re.sub(r'[\d.]+"','X"',w); WHY[w[:110]]+=1
      elif now.startswith('it is gone'): C['now: gone']+=1
      elif now.startswith('it holds it'): C['now: holds it, in a fight']+=1
      else: C['now: has a row']+=1
    for m in re.finditer(r'WALK CHECK: .*?\(([\d.]+)" away now\).*?the spot nearest it: (.*?) - rank (\d+) of (\d+)',s):
      WC['walk checks']+=1; WC['nearest spot ranked 1st' if m.group(3)=='1' else 'nearest spot not 1st']+=1
      WC['taken: that spot' if '| taken: that spot' in s else 'taken elsewhere']+=1
print('FOLLOW-UP',dict(C)); print('WALK CHECK',dict(WC)); print('ONE ROUTE mentions',OR)
print('NO ROW reasons:'); [print(f'  {n:4d}  {w}') for w,n in WHY.most_common(15)]
