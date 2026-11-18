"""Try 5: enemies priced NO risk by HIS SHOT LIST ('in reach would not have it on their list') or HIS CHARGE LIST ('no charge risk from #X'):
did that enemy then shoot / charge the unit in its next turn? By reason."""
import json,glob,re,sys,collections
ROOT=sys.argv[1]
HS=re.compile(r"HIS SHOT LIST: \d+ in reach would not have it on their list \((.*?)\), [\d.]+ VP no risk")
HS1=re.compile(r"#(\d+) ([^,#]*?)(?=, #|$)")
HC=re.compile(r"HIS CHARGE LIST: no charge risk from #(\d+) [^(]*\(([^)]*)\)")
c=collections.Counter(); byr=collections.defaultdict(collections.Counter); ex=[]
for f in glob.glob(f"{ROOT}/*/*/game-*.log.jsonl"):
    new='Mine' if f.split('/')[-3].startswith('mine') else 'Opponent'
    ev=[json.loads(l) for l in open(f)]; ev=[d for d in ev if d.get('kind')=='action']
    for i,d in enumerate(ev):
        if d.get('type')!='JobRisk' or d.get('side')!=new: continue
        u=d['actor_id']; s=d['summary']
        win=[]; seen=False
        for e in ev[i+1:]:
            if e.get('side')!=new and e.get('side'): seen=True
            if seen and e.get('side')==new and e.get('phase')=='Strategy': break
            if e.get('side')!=new: win.append(e)
        def acts(E,T):
            out=set()
            for e in win:
                if e.get('actor_id')!=E or e.get('target_id')!=T: continue
                t=e.get('type'); sm=e.get('summary','')
                if t=='Charge' and 'declares a charge' in sm: out.add('charge')
                elif t in ('Shooting','SpellCast') or (e.get('phase')=='Shooting' and t not in ('Candidates','MissileNotTried','ShotNotTaken','SpellNotCast','JobSplit','OpponentRule')): out.add('shot')
            return out
        seenE=set()
        for m in HS.finditer(s):
            for E,why in HS1.findall(m.group(1)):
                E=int(E)
                if ('s',E) in seenE: continue
                seenE.add(('s',E)); r=why.split(',')[0].strip(); a=acts(E,u)
                c['shot pairs']+=1; byr[r]['pairs']+=1
                if 'shot' in a: c['shot then shot here']+=1; byr[r]['shot here']+=1; ex.append((f.split('/')[-1],d['turn'],u,E,r))
                if 'charge' in a: c['shot then charged here']+=1
        for E,why in HC.findall(s):
            E=int(E)
            if ('c',E) in seenE: continue
            seenE.add(('c',E)); r=why.split(',')[0].strip(); a=acts(E,u)
            c['charge pairs']+=1; byr['CH '+r]['pairs']+=1
            if 'charge' in a: c['charge then charged here']+=1; byr['CH '+r]['charged here']+=1; ex.append((f.split('/')[-1],d['turn'],u,E,'CH '+r))
for k,v in sorted(c.items()): print(k,v)
for r,v in sorted(byr.items(),key=lambda x:-x[1]['pairs'])[:15]: print(r,dict(v))
for x in ex[:12]: print(x)
