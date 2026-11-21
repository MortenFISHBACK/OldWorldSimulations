import tarfile, csv, io, os, statistics as st, sys
def load(folder):
    out = {}
    for n in range(1, 49):
        p = f'{folder}/part-{n}/batch.tgz'
        if not os.path.exists(p) or not os.path.exists(f'{folder}/part-{n}/done'): continue
        try:
            t = tarfile.open(p)
            g = [m for m in t.getmembers() if m.name.count('/') == 1 and m.name.endswith('/games.csv')]
            rows = list(csv.DictReader(io.TextIOWrapper(t.extractfile(g[0]))))
        except Exception as e: print('bad', n, e); continue
        for r in rows: out[(r['pair'], n)] = r
    return out
new = load(sys.argv[1]); old = load(sys.argv[2])
same = diff = 0; mn = []; d = []
for k, r in sorted(new.items(), key=lambda x: (x[0][1], x[0][0])):
    o = old.get(k)
    if not o: continue
    if (r['vp_mine_opponent'], r['ended'], r['round']) == (o['vp_mine_opponent'], o['ended'], o['round']): same += 1
    else: diff += 1; d.append((k, o['vp_mine_opponent'], o['ended'], o['round'], '->', r['vp_mine_opponent'], r['ended'], r['round']))
    if r['ended'] == 'yes' and o['ended'] == 'yes': mn.append((float(r['minutes']), float(o['minutes'])))
print('games', len(new), 'same result', same, 'different', diff)
print('minutes new %.1f old %.1f (%.0f%%), median ratio %.2f, n %d' % (st.mean(a for a, b in mn), st.mean(b for a, b in mn), 100 * (st.mean(a for a, b in mn) / st.mean(b for a, b in mn) - 1), st.median(a / b for a, b in mn), len(mn)))
for x in d[:60]: print(x)
