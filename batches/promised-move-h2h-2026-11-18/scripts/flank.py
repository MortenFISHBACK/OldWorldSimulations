"""Own units caught in flank/rear (contact made there by an enemy charge), a game, per brain; from charges.pkl."""
import pickle,sys,collections
R=pickle.load(open(sys.argv[1],'rb')); G=int(sys.argv[2])
c=collections.Counter()
for r in R:
    if r.get('res')=='contact' and r.get('arc2') in ('flank','rear'):
        c['simpler units caught' if not r['simpler'] else 'new units caught']+=1
for k,v in c.items(): print(k, round(v/G,2), 'a game', v)
