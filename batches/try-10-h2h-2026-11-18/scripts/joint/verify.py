import glob,json,os,sys,collections
R=sys.argv[1]
for p in sorted(os.listdir(R)):
    for b in glob.glob(f'{R}/{p}/*/'):
        ro=open(b+'rules-off.txt').read().split()
        c=collections.Counter()
        for f in glob.glob(b+'game-*.log.jsonl'):
            for l in open(f):
                if '"OpponentRule"' not in l: continue
                d=json.loads(l); s=d['summary']
                for t in ('JOINT CHARGE NOW','AFTERMATH WITH FRIENDS','HIS FIGHT TOGETHER','SET UP BY THE SET'):
                    if s.startswith(t): c[(t.split()[0],d['side'])]+=1
        print(p,len(glob.glob(b+'game-*.log.jsonl')),'games |',' '.join(ro),'|',dict(c))
