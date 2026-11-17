import sys,os,glob,shutil,sqlite3,csv
D,arm,out=sys.argv[1],sys.argv[2],sys.argv[3]
parts=sorted(os.path.dirname(x) for x in glob.glob(f"{D}/{arm}-[0-9]*/games.csv")+glob.glob(f"{D}/{arm}-[0-9]*/*/games.csv"))
parts=[p for p in parts if os.path.isdir(p)]
os.makedirs(out,exist_ok=True)
for f in ("games.csv","plays.csv"):
  hdr=None; rows=[]
  for p in parts:
    fp=os.path.join(p,f)
    if not os.path.exists(fp): continue
    r=list(csv.reader(open(fp))); hdr=hdr or r[0]; assert r[0]==hdr,(fp); rows+=r[1:]
  if hdr: csv.writer(open(os.path.join(out,f),"w",newline="")).writerows([hdr]+rows)
for p in parts:
  for g in glob.glob(f"{p}/game-*"):
    dst=os.path.join(out,os.path.basename(g))
    if not os.path.exists(dst): os.symlink(g,dst)
for f in ("look-for.md","rules-off.txt","commit.txt"):
  shutil.copy(os.path.join(parts[0],f),os.path.join(out,f))
db=os.path.join(out,"records.db")
if os.path.exists(db): os.remove(db)
shutil.copy(os.path.join(parts[0],"records.db"),db)
c=sqlite3.connect(db)
gcols=[r[1] for r in c.execute("pragma table_info(GameRecords)")]
ucols=[r[1] for r in c.execute("pragma table_info(GameRecordUnits)") if r[1]!="Id"]
for p in parts[1:]:
  c.execute("attach ? as o",(os.path.join(p,"records.db"),))
  off=c.execute("select coalesce(max(Id),0) from GameRecords").fetchone()[0]
  sel=",".join(f"Id+{off}" if x=="Id" else x for x in gcols)
  c.execute(f"insert into GameRecords({','.join(gcols)}) select {sel} from o.GameRecords")
  sel=",".join(f"GameRecordId+{off}" if x=="GameRecordId" else x for x in ucols)
  c.execute(f"insert into GameRecordUnits({','.join(ucols)}) select {sel} from o.GameRecordUnits")
  c.commit(); c.execute("detach o")
print(arm,len(parts),"parts",c.execute("select count(*) from GameRecords").fetchone()[0],"records")
