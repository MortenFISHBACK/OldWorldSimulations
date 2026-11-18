"""Switch side check per part: rules-off.txt and which side writes the new-only rows."""
import json,glob,sys,collections,os
ROOT=sys.argv[1]
TAGS=('FIVE ACTION','STANDS STILL','LEGAL CHARGES ONLY','FRIEND CHARGES FIRST','FRIEND SHOOTS FIRST','WAITS AGAIN','WOUNDS ON THE RANKS','THE PROMISED MOVE')
for part in sorted(glob.glob(f"{ROOT}/*")):
    new='Mine' if os.path.basename(part).startswith('mine') else 'Opponent'
    ro=open(glob.glob(f"{part}/*/rules-off.txt")[0]).read().split() if glob.glob(f"{part}/*/rules-off.txt") else ['?']
    c=collections.Counter(); bad=[]; n=0
    for f in glob.glob(f"{part}/*/game-*.log.jsonl"):
        n+=1
        for l in open(f):
            d=json.loads(l)
            if d.get('type')=='OpponentRule':
                for t in TAGS:
                    if d['summary'].startswith(t):
                        c[(t,d.get('side'))]+=1
                        if d.get('side')!=new: bad.append(os.path.basename(f))
    print(os.path.basename(part),'new',new,'games',n,'rules-off sides',sorted(set(x.split('@')[-1] for x in ro if '@' in x)),'| WRONG SIDE in',sorted(set(bad)) if bad else 'none')
    print('   ',', '.join(f"{t} {s} {v}" for (t,s),v in sorted(c.items())))
