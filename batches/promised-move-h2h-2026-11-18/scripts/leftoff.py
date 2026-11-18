#!/usr/bin/env python3
"""Charges left off by LEGAL CHARGES ONLY, by reason, and for "its way or its sight is blocked" what lies on the straight line from the
charger to the target at that moment (worked-out-chances batch, 2026-11-17; Morten: "make batch include charge lines and paths").

This is the measuring script's own geometry, not the game's: a straight corridor as wide as the charger's front, from the charger's middle
to the nearest model of the target. A unit any of whose models sits in that corridor is "on the path" (friend or enemy); an impassable
feature the line crosses is "terrain"; else "nothing on the straight line" (sight, a wheel, the front arc corner). A friend on the path
that declared a charge on the same target that turn = "friend charging the same target" (the second unit of a joint charge).

    python3 leftoff.py <game-*.log.jsonl> ...   -> prints tables; also writes leftoff.jsonl next to this script's cwd
"""
import collections, json, math, re, sys

LINE = re.compile(r"^(.+?) is offered no charge on #(\d+) (.+?) this turn: (.+?) \(the estimate alone said reach (\d+)%\) - LEGAL CHARGES ONLY")


def reason(why):
    if why.startswith("its way or its sight"): return "way or sight blocked"
    if why.startswith("it is outside its front arc"): return "outside its front arc"
    m = re.search(r"\(([^()]+)\)$", why)
    return "rule bars it: " + (m.group(1) if m else why[:40])


def seg_dist(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy or 1e-9
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / L2))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy)), t


def crosses(poly, ax, ay, bx, by):
    def inside(x, y):
        c = False
        for k in range(len(poly)):
            (x1, y1), (x2, y2) = poly[k], poly[k - 1]
            if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / ((y2 - y1) or 1e-9) + x1: c = not c
        return c
    return any(inside(ax + (bx - ax) * s / 40, ay + (by - ay) * s / 40) for s in range(2, 39))


def game(path):
    side, name, state, rows, charges, imp, sight = {}, {}, {}, [], [], [], []
    acts = []
    for line in open(path, encoding="utf-8"):
        try: x = json.loads(line)
        except ValueError: continue
        k = x.get("kind")
        if k == "board":
            for u in x.get("units", []): side[u["id"]] = u["s"]; name[u["id"]] = u.get("n")
            imp = [t["p"] for t in x.get("terrain", []) if t.get("k") == "Impassable" and t.get("p")]
            sight = [(t["k"], t["p"]) for t in x.get("terrain", []) if t.get("k") in ("Wood", "Hill") and t.get("p")]
        elif k == "frame": acts.append((x["after"], 0, x))
        elif k == "action": acts.append((x["id"], 1, x))
    acts.sort(key=lambda a: (a[0], a[1]))
    turn_of = {}
    for _, kind, x in acts:
        if kind == 0:
            for u in x["units"]: state[u["id"]] = u
            continue
        if x.get("type") == "Charge" and "declares a charge" in (x.get("summary") or ""):
            charges.append((x["turn"], x["side"], x.get("actor_id"), x.get("target_id")))
        m = LINE.match(x.get("summary") or "") if x.get("type") == "Computer" else None
        if not m: continue
        cname, tid, why, reach = m.group(1), int(m.group(2)), m.group(4), int(m.group(5))
        s = x["side"]
        cid = next((i for i, n in name.items() if n == cname and side[i] == s), None)
        r = {"file": path.split("/")[-1], "turn": x["turn"], "side": s, "charger": cname, "target": m.group(3), "reach": reach,
             "reason": reason(why), "cid": cid, "tid": tid, "on_path": []}
        if r["reason"] == "way or sight blocked" and cid in state and tid in state:
            C, T = state[cid], state[tid]
            cm, tm = C.get("m") or [], T.get("m") or []
            if cm and tm:
                ax = sum(p[0] for p in cm) / len(cm); ay = sum(p[1] for p in cm) / len(cm)
                bx, by = min(tm, key=lambda p: math.hypot(p[0] - ax, p[1] - ay))[:2]
                L = math.hypot(bx - ax, by - ay) or 1e-9
                nx, ny = -(by - ay) / L, (bx - ax) / L
                across = [p[0] * nx + p[1] * ny for p in cm]
                half = (max(across) - min(across) + (C.get("bw") or 1)) / 2
                for uid, u in state.items():
                    if uid in (cid, tid) or not u.get("on") or uid not in side: continue
                    for p in u.get("m") or []:
                        d, t = seg_dist(p[0], p[1], ax, ay, bx, by)
                        if 0.02 < t < 0.98 and d < half + (u.get("bw") or 1) / 2:
                            r["on_path"].append({"id": uid, "name": name.get(uid), "friend": side[uid] == s}); break
                r["terrain"] = any(crosses(p, ax, ay, bx, by) for p in imp)
                r["sight"] = sorted({k for k, p in sight if crosses(p, ax, ay, bx, by)})
        rows.append(r)
    for r in rows:
        for b in r["on_path"]:
            b["charges_same_target"] = any(c[0] == r["turn"] and c[1] == r["side"] and c[2] == b["id"] and c[3] == r["tid"] for c in charges)
            b["charges_any"] = any(c[0] == r["turn"] and c[1] == r["side"] and c[2] == b["id"] for c in charges)
    return rows


def blocker(r):
    if r["reason"] != "way or sight blocked": return None
    f = [b for b in r["on_path"] if b["friend"]]; e = [b for b in r["on_path"] if not b["friend"]]
    if any(b["charges_same_target"] for b in f): return "friend on the path, charging the same target (joint charge)"
    if any(b["charges_any"] for b in f): return "friend on the path, charging another enemy"
    if f: return "friend on the path, not charging"
    if e: return "another enemy on the path"
    if r.get("terrain"): return "impassable terrain on the line"
    if "Wood" in r.get("sight", []): return "a wood on the line (blocks sight)"
    if "Hill" in r.get("sight", []): return "a hill on the line (may block sight)"
    return "nothing on the straight line (the game's own check: half the models' arcs, wheel room)"


if __name__ == "__main__":
    rows = [r for f in sys.argv[1:] for r in game(f)]
    with open("leftoff.jsonl", "w") as o:
        for r in rows: o.write(json.dumps(r) + "\n")
    n = len(sys.argv[1:])
    print(f"{len(rows)} charges left off in {n} games ({len(rows)/max(1,n):.1f} a game); reach the estimate gave them: mean {sum(r['reach'] for r in rows)/max(1,len(rows)):.0f}%\n")
    print("| Why | Left off | Share | Of them reach 50%+ |\n| --- | --- | --- | --- |")
    for k, v in collections.Counter(r["reason"] for r in rows).most_common():
        print(f"| {k} | {v} | {v/len(rows):.0%} | {sum(1 for r in rows if r['reason']==k and r['reach']>=50)} |")
    bl = [blocker(r) for r in rows if blocker(r)]
    print("\n| Way or sight blocked: what lies on the straight line | Left off | Share |\n| --- | --- | --- |")
    for k, v in collections.Counter(bl).most_common():
        print(f"| {k} | {v} | {v/len(bl):.0%} |")
