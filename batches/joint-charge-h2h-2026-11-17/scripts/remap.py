import re,sys,csv,glob,statistics,collections,math
L=open('/root/jc/cmp-all.md').read().split('\n')
def tables():
  i=0
  while i<len(L):
    if L[i].startswith('| ') and i+1<len(L) and L[i+1].startswith('| ---'):
      j=i+2
      while j<len(L) and L[j].startswith('|'): j+=1
      # section heading
      h=next((L[k] for k in range(i,-1,-1) if L[k].startswith('#')),'')
      yield i,h,[c.strip() for c in L[i].strip('|').split('|')],[[c.strip() for c in r.strip('|').split('|')] for r in L[i+2:j]]
      i=j
    else: i+=1
OF=re.compile(r'\((\d+) of (\d+)\)')
NUM=re.compile(r'^[+-]?\d+(\.\d+)?%?')
def pool(a,b):
  if a in ('-','') : return b
  if b in ('-',''): return a
  ma,mb=OF.search(a),OF.search(b)
  if ma and mb:
    x=int(ma[1])+int(mb[1]); y=int(ma[2])+int(mb[2]); return f"{x/max(1,y):.0%} ({x} of {y})"
  na,nb=NUM.match(a),NUM.match(b)
  if na and nb:
    pa=na[0].endswith('%'); va=float(na[0].rstrip('%')); vb=float(nb[0].rstrip('%'))
    v=(va+vb)/2; d=max(len(x.rstrip('%').split('.')[1]) if '.' in x else 0 for x in (na[0],nb[0]))
    if ' declared, ' in a and ' declared, ' in b:
      ca=re.search(r'([\d.]+) contact',a); cb_=re.search(r'([\d.]+) contact',b)
      return f"{v:.2f} declared, {(float(ca[1])+float(cb_[1]))/2:.2f} contact"
    s=f"{v:.{d}f}"+('%' if pa else '')
    if na[0].startswith('+') or na[0].startswith('-') and not pa and 'net' in '': s=('+' if v>=0 else '')+s
    return s
  return f"{a} / {b}"
out=[]
for i,h,hd,rows in tables():
  if set(['A Mine','A Opponent','B Mine','B Opponent']).issubset(hd) or set(['sh Mine Mine','sh Mine Opponent','sh Opp Mine','sh Opp Opponent']).issubset(hd):
    if 'A Mine' in hd: am,ao,bm,bo=(hd.index(x) for x in ('A Mine','A Opponent','B Mine','B Opponent'))
    else: am,ao,bm,bo=(hd.index(x) for x in ('sh Mine Mine','sh Mine Opponent','sh Opp Mine','sh Opp Opponent'))
    lead=[k for k in range(len(hd)) if k<min(am,ao,bm,bo)]
    out+=[h,'',"| "+" | ".join([hd[k] for k in lead]+['**Fixes on**','**Fixes off**','on (Mine games) / (Opp games)','off (Mine games) / (Opp games)'])+" |",
          "| "+" | ".join(['---']*(len(lead)+4))+" |"]
    for r in rows:
      if len(r)<len(hd): continue
      out.append("| "+" | ".join([r[k] for k in lead]+[pool(r[am],r[bo]),pool(r[ao],r[bm]),f"{r[am]} / {r[bo]}",f"{r[ao]} / {r[bm]}"])+" |")
    out.append('')
open('/root/jc/remapped.md','w').write('\n'.join(out))
print(len(out))
