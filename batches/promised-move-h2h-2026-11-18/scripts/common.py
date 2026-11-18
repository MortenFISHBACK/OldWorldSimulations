import json,glob,os,re,collections,csv
D='/mnt/project-files/worked-out-chances-h2h-2026-11-17'
ARMS=('mine','opp')
def fixed_side(arm): return 'Mine' if arm=='mine' else 'Opponent'
def part_dirs(arm):
  return sorted(set(os.path.dirname(x) for x in glob.glob(f'{D}/{arm}-*/games.csv')+glob.glob(f'{D}/{arm}-*/*/games.csv') if '/parts/' not in x))
def games():
  for arm in ARMS:
    for p in part_dirs(arm):
      for f in sorted(glob.glob(p+'/game-*.log.jsonl')):
        pair=os.path.basename(f).split('-')[1]
        yield arm,pair,f
def load(f):
  out=[]
  for l in open(f):
    try: out.append(json.loads(l))
    except ValueError: pass
  return out
def brain(arm,side): return 'fix' if side==fixed_side(arm) else 'off'
