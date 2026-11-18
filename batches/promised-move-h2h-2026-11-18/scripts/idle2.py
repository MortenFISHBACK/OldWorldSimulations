"""Try 5 check: (a) charge risk counted on a picked job (#E arc p%/full% loss) and (b) units priced NO risk by HIS SHOT LIST / HIS CHARGE LIST,
with the turn windows of job_claims (own turn rest, then the enemy's next turn)."""
import json,glob,re,sys,collections,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import job_claims as jc
ROOT=sys.argv[1]
CHR=re.compile(r"#(\d+) (\w+) (\d+)%/(\d+)% (-?[\d.]+) \(he wins (\d+)%\)")
HS=re.compile(r"HIS SHOT LIST: \d+ in reach would not have it on their list \((.*?)\), [\d.]+ VP no risk")
HS1=re.compile(r"#(\d+) ([^,#]*?)(?=, #|$)")
HC=re.compile(r"HIS CHARGE LIST: no charge risk from #(\d+) [^(]*\(([^)]*)\)")
c=collections.Counter(); w=collections.Counter(); nr=collections.Counter(); nrb=collections.defaultdict(collections.Counter)
for f in glob.glob(f"{ROOT}/*/*/game-*.log.jsonl"):
    new='Mine' if f.split('/')[-3].startswith('mine') else 'Opponent'
    g=jc.read_game(f)
    ev=[json.loads(l) for l in open(f)]; ev=[d for d in ev if d.get('kind')=='action']
    for d in ev:
        if d.get('type')!='JobRisk' or d.get('side')!=new: continue
        i=d['id']; u=d['actor_id']; s=d['summary']
        ow=jc._window(g,i,new,'this'); hw=jc._window(g,i,new,'enemy')
        if not hw: continue
        ours=[e for e in ev if i<e['id']<hw[0]]; his=[e for e in ev if hw[0]<=e['id']<hw[1]]
        def acts(E,T):
            out=set()
            for e in his:
                if e.get('actor_id')!=E or e.get('target_id')!=T: continue
                t=e.get('type'); sm=e.get('summary','')
                if t=='Charge' and 'declares a charge' in sm: out.add('charge')
                elif t in ('Shooting','SpellCast') or (e.get('phase')=='Shooting' and t not in ('Candidates','MissileNotTried','ShotNotTaken','SpellNotCast','JobSplit','OpponentRule','JobRisk')): out.add('shot')
            return out
        for E,arc,p,full,loss,wn in CHR.findall(s):
            E=int(E); p=int(p)
            if 'charge' in acts(E,u): k='charged this unit'
            elif jc._gone(g,E,hw[0]): k='dead before his turn'
            elif any(e.get('type')=='Charge' and 'declares a charge' in e.get('summary','') and e.get('target_id')==E for e in ours): k='we charged it first'
            elif any(e.get('actor_id')==E and e.get('type')=='Charge' and 'declares a charge' in e.get('summary','') for e in his): k='charged another unit'
            elif jc._gone(g,u,hw[0]): k='our unit dead before his turn'
            else:
                off=any(e.get('actor_id')==E and e.get('type')=='Candidates' and f'charge #{u} ' in e.get('summary','') for e in his)
                anyc=any(e.get('actor_id')==E and e.get('type')=='Candidates' and 'CANDIDATES JOB' in e.get('summary','') for e in his)
                cut=any(e.get('actor_id')==E and e.get('type')=='Candidates' and 'CANDIDATES JOB' in e.get('summary','') and re.search(r'\| \d+ more', e.get('summary','')) for e in his)
                k='on his list, not taken' if off else (('not in his weighed list (list cut short in log)' if cut else 'not on his list') if anyc else 'no job list (in combat/fleeing)')
            c[k]+=1; w[k]+=p
        seen=set()
        for m in HS.finditer(s):
            for E,why in HS1.findall(m.group(1)):
                E=int(E)
                if ('s',E) in seen: continue
                seen.add(('s',E)); r=why.split(',')[0].strip(); a=acts(E,u)
                nr['shot pairs']+=1; nrb[r]['pairs']+=1
                if a: nr['shot: then shot/charged here']+=1; nrb[r]['hit here']+=1
        for E,why in HC.findall(s):
            E=int(E)
            if ('c',E) in seen: continue
            seen.add(('c',E)); a=acts(E,u); nr['charge pairs']+=1; nr['charge: then charged here']+='charge' in a
n=sum(c.values())
print("CHARGE RISK COUNTED", n, "mean claimed", round(sum(w.values())/n))
for k,v in c.most_common(): print(f"  {k:34s} {v:4d} {v/n:5.0%} mean claimed {w[k]/v:.0f}%")
print("NO RISK", dict(nr))
for r,v in sorted(nrb.items(),key=lambda x:-x[1]['pairs'])[:6]: print("  ",r,dict(v))
