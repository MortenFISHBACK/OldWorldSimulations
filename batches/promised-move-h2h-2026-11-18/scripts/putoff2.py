import json,glob,re,sys,collections,statistics as st
ROOT=sys.argv[1]
tagc=collections.defaultdict(list); tagd=collections.defaultdict(list); ex=[]
for f in glob.glob(f"{ROOT}/*/*/game-*.log.jsonl"):
    new='Mine' if f.split('/')[-3].startswith('mine') else 'Opponent'
    for l in open(f):
        d=json.loads(l)
        if d.get('type')!='JobSplit' or d.get('side')!=new: continue
        parts=d['summary'].split(' | ')[1:]; ch={}; tk=None
        for p in parts:
            m=re.match(r'\d+\. ([a-z]+)(.*?): worth ([+\-]?[\d.]+)',p)
            if not m: continue
            if m.group(1)=='charge':
                t=re.match(r' #(\d+)',m.group(2))
                if t: ch[int(t.group(1))]=p
            if '[TAKEN]' in p: tk=(m.group(1),p)
        if not ch or not tk or tk[0]=='charge': continue
        m=re.search(r'next turn: #(\d+)',tk[1])
        if not m or int(m.group(1)) not in ch: continue
        c=ch[int(m.group(1))]
        def tags(p):
            b=p[p.rfind('{')+1:p.rfind('}')]
            return {k.strip():float(v) for k,v in re.findall(r'([A-Z][A-Z \'\-]+) ([+\-][\d.]+)',b)}
        for k,v in tags(c).items(): tagc[k].append(v)
        for k,v in tags(tk[1]).items(): tagd[k].append(v)
        ex.append((f.split('/')[-1],d['turn'],d['actor_id'],c[:700],tk[1][:500]))
n=len(ex); print(n,'cases')
print('charge now: tag mean (sum/n)'); 
for k,v in sorted(tagc.items(),key=lambda x:sum(x[1])): print(f'  {k} {sum(v)/n:+.1f} ({len(v)})')
print('delay picked: tag mean')
for k,v in sorted(tagd.items(),key=lambda x:sum(x[1])): print(f'  {k} {sum(v)/n:+.1f} ({len(v)})')
for e in ex[:4]: print('\n',e[0],e[1],e[2],'\nNOW:',e[3],'\nDELAY:',e[4])
