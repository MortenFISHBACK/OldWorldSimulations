"""Charges picked with a claimed first-round win chance under 50%: how many, how they went (first round, net points 2 turns), and how many carry HIS CHARGE DENIED."""
import pickle,collections,sys
C=pickle.load(open(sys.argv[1],'rb'))
for simp in (False,True):
  P=[c for c in C if c['simpler']==simp and c.get('win') is not None]
  lo=[c for c in P if c['win']<0.5]
  rr=collections.Counter(c.get('r1','no contact') for c in lo)
  net=[(c.get('t_2t') or 0)-(c.get('a_2t') or 0) for c in lo]
  hcd=[c for c in lo if 'HIS CHARGE DENIED' in str(c.get('rules'))]
  print('new' if not simp else 'simpler','| with win chance',len(P),'| under 50%',len(lo),'| first round',dict(rr),'| net 2 turns mean %+.0f'%(sum(net)/max(1,len(net))),'| with HIS CHARGE DENIED',len(hcd))
allh=[c for c in C if not c['simpler'] and 'HIS CHARGE DENIED' in str(c.get('rules'))]
net=[(c.get('t_2t') or 0)-(c.get('a_2t') or 0) for c in allh]
print('new charges carrying HIS CHARGE DENIED',len(allh),dict(collections.Counter(c.get('r1','no contact') for c in allh)),'net %+.0f'%(sum(net)/max(1,len(net))),'win<50%:',sum(1 for c in allh if (c.get('win') or 1)<0.5))
