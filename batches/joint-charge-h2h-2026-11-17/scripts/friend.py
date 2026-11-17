# FRIEND IN REACH rows per brain (adds ON / OFF): alone v with best friend, and what the friend did.
import glob,json,re,collections,os,sys
A=os.path.expanduser('~/jc/an')
R=re.compile(r'^FRIEND IN REACH: ([+-][\d.]+) VP: alone ~([\d.-]+) VP \(reach (\d+)%, win (\d+)%\); (.*)$')
W=re.compile(r'with #(\d+) .*? ~([\d.-]+) VP \(its reach (\d+)%, together win (\d+)%\); the friend: (.*)$')
S=collections.defaultdict(lambda: collections.defaultdict(float)); why=collections.defaultdict(collections.Counter)
for arm in ('mine','opp'):
  on='Mine' if arm=='mine' else 'Opponent'
  for f in glob.glob(f'{A}/{arm}-*/game-*.log.jsonl'):
    for l in open(f):
      if 'FRIEND IN REACH' not in l: continue
      x=json.loads(l); s=x.get('summary','')
      m=R.match(s)
      if not m: continue
      b='on' if x['side']==on else 'off'; d=S[b]
      d['n']+=1; d['alone']+=float(m[2])
      w=W.search(m[5])
      if w:
        d['withf']+=1; d['tog']+=float(w[2]); d['alone_w']+=float(m[2]); d['gain']+=float(m[1])
        fr=w[5]
        k=('charges with it / too' if ('charges with it' in fr or 'charges it too' in fr) else 'below zero alone' if 'below zero' in fr else 'not among its best / unseen' if 'not among' in fr else 'on its list, not taken' if 'on its list at' in fr else 'other')
        why[b][k]+=1
      else: d['nofriend']+=1
G=144*2
for b in ('on','off'):
  d=S[b]; print(b,'charges picked/game %.2f'%(d['n']/G),'friend in reach %.0f%%'%(100*d['withf']/d['n']),
   'alone~%.0f with~%.0f (+%.0f) when friend'%(d['alone_w']/d['withf'],d['tog']/d['withf'],d['gain']/d['withf']))
  t=sum(why[b].values()); print('  ', {k:'%.0f%%'%(100*v/t) for k,v in why[b].most_common(8)})
