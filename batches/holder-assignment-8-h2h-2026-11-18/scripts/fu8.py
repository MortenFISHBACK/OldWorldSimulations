import json,glob,os,re,collections,html,sys
R=sys.argv[1];C=collections.Counter();AL=[];WC=collections.Counter()
for j in glob.glob(os.path.join(R,'**/game-*.log.jsonl'),recursive=True):
  new='Opponent' if '/opp-' in j else 'Mine'
  for l in open(j):
    if not l.startswith('{"kind":"action"'): continue
    r=json.loads(l); s=html.unescape(r.get('summary') or '')
    if r.get('side')!=new: continue
    for m in re.finditer(r'WALK FOLLOW-UP: (.+?) walked on to (.+?) last turn.*?now: (.*?); \2 (stays empty|stays .*?\'s|goes to [^;]*)',s):
      now=m.group(3); g=m.group(4)
      k='kept (same unit)' if g.startswith('stays') and 'empty' not in g else 'empty' if 'empty' in g else 'to another unit'
      C[k]+=1; C['now: no row' if now.startswith('no row') else 'now: has a row']+=1
    for m in re.finditer(r'not charged off on the way (\d+)%: RISK ON THE WAY',s): AL.append(int(m.group(1)))
    for m in re.finditer(r'WALK CHECK: .*?\(([\d.]+)" away now\); the spot nearest it: (.*?) - rank (\d+) of (\d+)',s):
      WC['walk checks']+=1; WC['nearest spot ranked 1st' if m.group(3)=='1' else 'nearest spot not 1st']+=1
print('FOLLOW-UP',dict(C)); print('WALK CHECK',dict(WC))
import statistics as st
print('risk-on-the-way claims',len(AL),'median alive',st.median(AL) if AL else '-', 'under 80%',sum(a<80 for a in AL))
