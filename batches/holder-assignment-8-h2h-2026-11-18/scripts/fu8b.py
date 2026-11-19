import json,glob,os,re,collections,html,sys,statistics as st
R=sys.argv[1];C=collections.Counter();drop=[]
for j in glob.glob(os.path.join(R,'**/game-*.log.jsonl'),recursive=True):
  new='Opponent' if '/opp-' in j else 'Mine'
  for l in open(j):
    if 'WALK FOLLOW-UP' not in l: continue
    r=json.loads(l)
    if r.get('side')!=new: continue
    s=html.unescape(r.get('summary') or '')
    for seg in s.split('WALK FOLLOW-UP: ')[1:]:
      m=re.match(r'(.+?) walked on to (.+?) last turn \(~([\d.]+) VP, net ~([-\d.]+)',seg)
      if not m: continue
      was=float(m.group(4)); now=seg.split('now: ',1)[1]
      if now.startswith('no row'): C['now no row']+=1; continue
      n=re.match(r'~([\d.]+) VP there \((in range this turn|walks on)\), net ~([-\d.]+)',now)
      if not n: continue
      C['now '+n.group(2)]+=1; drop.append(float(n.group(3))-was)
print(dict(C)); print('net now-was median',st.median(drop),'fell >30:',sum(d<-30 for d in drop),'of',len(drop))
