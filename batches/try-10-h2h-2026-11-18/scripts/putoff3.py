"""Try 7: charges on offer (new side) put off for the SAME target next turn. Compares the charge-now total with the delay's total (not rule
rows), and splits what the delay earns: A = this turn (objectives, shots, missiles, feature), B = next turn's charge (raw x chance),
C = friends (support, carries, chaff, mask), D = risk, idle. Also whether the charge came next turn, and the SAME CHARGE LATER cut."""
import json,glob,re,sys,collections,statistics as st
ROOT=sys.argv[1]
SP=re.compile(r"SPLIT: A objectives (-?[\d.]+) shoots (-?[\d.]+) missiles (-?[\d.]+) feature (-?[\d.]+) \| B (\S+) (-?[\d.]+) x (\d+)%.*?\| C support (-?[\d.]+) carries (-?[\d.]+) chaff (-?[\d.]+) mask (-?[\d.]+) \| D (-?[\d.]+).*?\| idle (-?[\d.]+)")
c=collections.Counter(); rows=[]; ex=[]
for f in glob.glob(f"{ROOT}/*/*/game-*.log.jsonl"):
    new='Mine' if f.split('/')[-3].startswith('mine') else 'Opponent'
    ev=[json.loads(l) for l in open(f) if l.strip()]
    decl={(d['actor_id'],d['target_id'],d['turn']) for d in ev if d.get('type')=='Charge' and 'declares a charge' in d.get('summary','')}
    risk={}
    for d in ev:
        if d.get('type')=='JobRisk' and d.get('side')==new: risk[(d['actor_id'],d['turn'])]=d['summary']
    slc=collections.Counter()
    for d in ev:
        if d.get('type')=='OpponentRule' and d.get('side')==new and d['summary'].startswith('SAME CHARGE LATER'): slc[(d.get('actor_id'),d['turn'])]+=1
    for d in ev:
        if d.get('type')!='JobSplit' or d.get('side')!=new: continue
        ch={}; taken=None
        for p in d['summary'].split(' | ')[1:]:
            m=re.match(r'\d+\. ([a-z]+)(.*?): worth ([+\-]?[\d.]+)',p)
            if not m: continue
            if m.group(1)=='charge':
                t=re.match(r' #(\d+)',m.group(2))
                if t: ch[int(t.group(1))]=float(m.group(3))
            if '[TAKEN]' in p: taken=(m.group(1),p,float(m.group(3)))
        if not ch or not taken or taken[0]=='charge': continue
        c['charge on offer, not taken']+=1
        m=re.search(r'next turn: #(\d+)',taken[1])
        if not m or int(m.group(1)) not in ch: continue
        T=int(m.group(1)); c['put off for the SAME target']+=1
        r=risk.get((d['actor_id'],d['turn']),''); s=SP.search(r)
        came=(d['actor_id'],T,d['turn']+1) in decl
        cut='SAME CHARGE LATER' in taken[1] or slc[(d['actor_id'],d['turn'])]>0
        row=dict(now=ch[T],delay=taken[2],came=came,cut=cut,kind=taken[0])
        if s:
            g=[float(x) if i!=4 else x for i,x in enumerate(s.groups())]
            row.update(obj=g[0],shoot=g[1],miss=g[2],feat=g[3],bkind=g[4],braw=g[5],bch=g[6]/100,sup=g[7],carry=g[8],chaff=g[9],mask=g[10],D=g[11],idle=g[12])
            row['B']=g[5]*g[6]/100
        else: c['no SPLIT found']+=1
        rows.append(row)
        if len(ex)<6 and s: ex.append((f.split('/')[-1],d['turn'],d['actor'],T,row))
print(dict(c))
if rows:
    print('came next turn: %d of %d (%.0f%%)'%(sum(r['came'] for r in rows),len(rows),100*sum(r['came'] for r in rows)/len(rows)))
    print('SAME CHARGE LATER cut on the delay: %d'%sum(r['cut'] for r in rows))
    print('picked:',collections.Counter(r['kind'] for r in rows))
    print('median charge now %.1f  delay %.1f'%(st.median(r['now'] for r in rows),st.median(r['delay'] for r in rows)))
    S=[r for r in rows if 'B' in r]
    for k in ('obj','shoot','miss','feat','B','braw','bch','sup','carry','chaff','mask','D','idle'):
        v=[r[k] for r in S]; print('  %-6s mean %+.1f  median %+.1f  nonzero %d'%(k,st.mean(v),st.median(v),sum(1 for x in v if abs(x)>=0.5)))
    print('  this turn (A = obj+shoot+miss+feat) mean %+.1f; friends (C) mean %+.1f'%(st.mean(r['obj']+r['shoot']+r['miss']+r['feat'] for r in S),st.mean(r['sup']+r['carry']+r['chaff']-r['mask'] for r in S)))
    print('  B (next-turn charge) vs charge now: B > now in %d of %d'%(sum(1 for r in S if r['B']>r['now']),len(S)))
    for e in ex: print(e)
