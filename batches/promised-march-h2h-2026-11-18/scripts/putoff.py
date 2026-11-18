"""Try 6: charges on offer (new side) not taken; how many picked a move/march/stand 'next turn: #T' on the SAME target as an offered charge,
split by target kind (shooter/wizard = wizard level or fired in the game; mobile = cavalry/chariot/monster/flier-ish troop types; plain block = rest).
Also: did the delayed charge come next turn."""
import json,glob,re,sys,collections,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import job_claims as jc
ROOT=sys.argv[1]
SHOTT={'Shooting','WarMachineShot','SpellCast','BreathWeapon'}
c=collections.Counter(); kind=collections.Counter(); came=collections.Counter(); wnow=[]; wlat=[]
def k_of(u,shooters):
    if not u: return '?'
    if u.get('wz') or u['id'] in shooters: return 'shooter/wizard'
    t=((u.get('tt') or '')+' '+(u.get('rt') or '')).lower()
    if any(x in t for x in ('cavalry','chariot','monster','beast','swarm','war beast','flier','fly')): return 'mobile'
    return 'plain block'
for f in glob.glob(f"{ROOT}/*/*/game-*.log.jsonl"):
    new='Mine' if f.split('/')[-3].startswith('mine') else 'Opponent'
    g=jc.read_game(f)
    ev=[json.loads(l) for l in open(f) if l.strip()]
    shooters={d.get('actor_id') for d in ev if d.get('type') in SHOTT}
    decl=set()
    for d in ev:
        if d.get('type')=='Charge' and 'declares a charge' in d.get('summary',''): decl.add((d['actor_id'],d['target_id'],d['turn']))
    for d in ev:
        if d.get('type')!='JobSplit' or d.get('side')!=new: continue
        parts=d['summary'].split(' | ')[1:]
        ch={}; taken=None
        for p in parts:
            m=re.match(r'\d+\. ([a-z]+)(.*?): worth ([+\-]?[\d.]+)',p)
            if not m: continue
            if m.group(1)=='charge':
                t=re.match(r' #(\d+)',m.group(2))
                if t: ch[int(t.group(1))]=float(m.group(3))
            if '[TAKEN]' in p: taken=(m.group(1),p,float(m.group(3)))
        if not ch or not taken or taken[0]=='charge': continue
        c['offered, not taken']+=1
        m=re.search(r'next turn: #(\d+)',taken[1])
        if not m: c['no next-turn target']+=1; continue
        T=int(m.group(1))
        if T in ch:
            c['same target next turn']+=1; kk=k_of(g['units'].get(T),shooters); kind[kk]+=1
            wnow.append(ch[T]); wlat.append(taken[2])
            came[(kk,(d['actor_id'],T,d['turn']+1) in decl)]+=1
        else: c['another target next turn']+=1
print(dict(c)); print('by target kind',dict(kind)); print('came next turn',dict(came))
import statistics as st
if wnow: print('median worth: charge now',round(st.median(wnow),1),'picked (delay)',round(st.median(wlat),1))
