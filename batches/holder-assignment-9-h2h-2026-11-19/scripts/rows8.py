import json,glob,os,html,sys,re
R,out=sys.argv[1],sys.argv[2]
with open(out,'w') as o:
  o.write('game\tpart\tturn\tside\tphase\tunit\tkind\ttext\n')
  for j in sorted(glob.glob(os.path.join(R,'**/game-*.log.jsonl'),recursive=True)):
    part=os.path.relpath(j,R).split('/')[0]; new='Opponent' if part.startswith('opp') else 'Mine'; g=os.path.basename(j)[5:-11]
    for l in open(j):
      if 'WALK CHECK' not in l and 'WALK FOLLOW-UP' not in l: continue
      r=json.loads(l)
      if r.get('side')!=new: continue
      s=html.unescape(r.get('summary') or '')
      for kind in ('WALK CHECK','WALK FOLLOW-UP'):
        for seg in re.split(r'(?=%s: )'%kind,s)[1:]:
          seg=re.split(r' \| (?=[A-Z][A-Z \-]+: )',seg)[0] if kind=='WALK FOLLOW-UP' else seg.split(' || ')[0]
          o.write('\t'.join([g,part,str(r.get('turn')),new,r.get('phase') or '',html.unescape(r.get('actor') or ''),kind,seg.replace('\t',' ').replace('\n',' ')])+'\n')
