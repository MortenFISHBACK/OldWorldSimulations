#!/usr/bin/env python3
"""Claimed against happened, per job (job figures report option 12, Morten 2026-11-13: "12 yes please").

For every job the computer picks ("Objective for <unit>: <job> ...: its best option, worth ~N VP"), per side: picks a game, the average VP
the pick claimed, and what happened after it, so a figure that drifts shows up in the next batch report:

- charge: the target's VP gone and the charger's VP lost by the start of the side's own turn after next (net over two game turns, the same
  span the charge figure's kills count over); and the share of picks that declared that charge in the same turn.
- shoot: the VP of the wounds the unit's shooting did that turn (wounds x the target's points per wound).
- hold (markers, the hill, special features, baggage): the VP the unit scored on objectives this turn and in the enemy's turn after.
- close in / turn to face / advance: the share followed by a charge on that target in the side's next turn.
- screen: the wounds the guarded unit lost in the enemy's next turn before combat, against the wounds a turn the line said.
- redirect / lure: the share where the enemy named charged the guarded friend, and where it charged the chaff, in its next turn.
- join and the rest: picks and claims only.

Risk (Morten 2026-11-16, "7. please log risks"): every pick also writes a hidden JobRisk row ("JOB RISK: <job>: gain +G VP, risk R VP, worth
+W VP", src/.../Services/Opponent/JobRisk.cs) - the VP the pick took off for the enemy's next turn. The table puts that risk claimed against the
unit's own points lost in the enemy's next player turn (destroyed or fled off: all its points with joined characters; else the models lost as a
share of its points). Games from before 2026-11-16 carry no JobRisk rows: those columns read "-".

A second table gives the same per unit type (rank troop type; characters apart) for the jobs that have a "happened" number.
The game logs' frames are a block at the top of the file keyed by `after` (an action id), not in line order. A joined character's points go to
the nearest unit of its side with the name it joined when the battle starts (the analysis thread's pitfalls, 2026-11-13).

    python3 scripts/job_claims.py <batch folder> [...]   (several folders: their games add up)
"""
import collections
import glob
import json
import os
import re
import sys

PICK = re.compile(r"^Objective for (.+?): (.*)$")
# HOLDER ASSIGNMENT (2026-11-18): the army-wide table's line and the row a holder's pick writes. A five-option pick reads "march by the
# five-action sum", so the job is told from these: in range = hold (claimed: what the table says the objective is worth there), walking
# on to it = advance toward an objective.
TABLE = re.compile(r"^HOLDER ASSIGNMENT: (.+?) goes to (.+?) \((holds it this turn|walks on to it): gives up ~-?[\d.]+ VP of its other options for the ~(-?[\d.]+) VP")
TAKES = "the assigned holder takes it"
RISK = re.compile(r"^JOB RISK: .*: gain [+-][\d.]+ VP, risk (-?[\d.]+) VP, worth [+-][\d.]+ VP(?:; FIVE: .*)?$")
SIDES = ("Mine", "Opponent")

JOBS = [  # (key, label) in the table's order
    ("charge", "Charge"), ("shoot", "Shoot"), ("hold", "Hold a marker, the hill, a feature"), ("hold-end", "Hold an end-of-battle objective (holder table)"), ("close-in", "Close in to charge next turn"),
    ("turn", "Turn to face"), ("advance", "Advance on an enemy"), ("advance-spot", "Advance toward an objective"), ("screen", "Screen"),
    ("redirect", "Redirect"), ("lure", "Lure"), ("join", "Join a unit"), ("cast", "Cast"), ("raid-next", "Close in to raid the baggage"),
    ("support-other", "Other support"), ("back-up", "Back up a friend"), ("other", "Other"),
]
LABEL = dict(JOBS)


def kind_of(body):
    # The replay page names jobs the same way (src/.../Services/Replay/ReplayJobs.cs, Morten 2026-11-13): change both together.
    b = body.lower()
    for prefix, k in (("support: screen", "screen"), ("support: redirect", "redirect"), ("support: lure", "lure"), ("support:", "support-other"),
                      ("charge ", "charge"), ("close in to charge", "close-in"), ("close in to raid", "raid-next"), ("advance on", "advance"),
                      ("advance toward", "advance-spot"), ("shoot ", "shoot"), ("cast", "cast"), ("stay in range and cast", "cast"),
                      ("move into casting", "cast"), ("hold or contest", "hold"), ("keep holding", "hold"), ("take", "hold"), ("contest", "hold"),
                      ("join", "join"), ("turn", "turn"), ("back up", "back-up")):
        if b.startswith(prefix):
            return k
    return "other"


def _worth(body):
    tail = body.split(": its ")[-1] if ": its " in body else body
    m = re.search(r"worth ~(-?[\d.]+) VP", tail)
    return float(m.group(1)) if m else None


def _num(pattern, text):
    m = re.search(pattern, text)
    return float(m.group(1)) if m else None


def read_game(path):
    """One game log: its units (by board id), the picks, charges, shots, objective scores, unit states and turn starts."""
    d = os.path.dirname(path)
    pair = os.path.basename(path).split("-")[1]
    parts = sorted(glob.glob(os.path.join(d, "parts", pair + "-*", "units.jsonl")))
    urows = []
    if parts:
        with open(parts[0], encoding="utf-8") as f:
            urows = [json.loads(line) for line in f if line.strip()]
    g = {"units": {}, "picks": [], "charges": [], "shots": [], "obj": [], "turnstart": {}, "hist": collections.defaultdict(list), "n": 0, "combat": [],
         "risk": {}}
    table, takes = {}, set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            try:
                x = json.loads(line)
            except ValueError:
                continue
            k = x.get("kind")
            if k == "board":
                for side in SIDES:
                    b = [u for u in x.get("units", []) if u.get("s") == side]
                    r = [q for q in urows if q.get("side") == side]
                    for j, u in enumerate(b):
                        rr = r[j] if len(b) == len(r) else None
                        lk = u.get("lk") or {}
                        g["units"][u["id"]] = {"id": u["id"], "side": side, "name": u.get("n"), "tt": lk.get("tt"), "rt": lk.get("rt"),
                                               "mc": lk.get("mc") or 1, "w": lk.get("w") or 1, "wz": lk.get("wz"),
                                               "points": (rr or {}).get("points") or 0, "joined": (rr or {}).get("joinedTo"), "cn": (rr or {}).get("unit")}
            elif k == "frame":
                i = x.get("after") or 0
                g["n"] = max(g["n"], i)
                for u in x.get("units", []):
                    g["hist"][u["id"]].append((i, u.get("on"), len(u.get("m") or []), u.get("x"), u.get("y")))
            elif k == "objective":
                g["obj"].append((x.get("turn"), x.get("turn_side"), x.get("side"), x.get("unit"), x.get("points") or 0))
            elif k == "action":
                i = x.get("id") or 0
                g["n"] = max(g["n"], i)
                if x.get("phase") == "Strategy":
                    g["turnstart"].setdefault((x.get("turn"), x.get("side")), i)
                elif x.get("phase") == "Combat":
                    g["combat"].append(i)
                t, s = x.get("type"), x.get("summary") or ""
                if t == "Computer" and (m := PICK.match(s)):
                    body = m.group(2)
                    g["picks"].append({"i": i, "turn": x.get("turn"), "side": x.get("side"), "unit": m.group(1), "kind": kind_of(body),
                                       "worth": _worth(body), "ids": [int(q) for q in re.findall(r"#(\d+)", body)],
                                       "wounds": _num(r"takes about ([\d.]+) wounds a turn", body)})
                elif t == "Computer" and (m := TABLE.match(s)):
                    table[(x.get("turn"), x.get("side"), m.group(2), m.group(1))] = (m.group(3) == "holds it this turn", float(m.group(4)))
                elif t == "OpponentRule" and x.get("phase") == "Strategy" and TAKES in s and s.startswith("HOLDER ASSIGNMENT"):
                    takes.add((x.get("turn"), x.get("side"), x.get("actor"), x.get("target")))
                elif t == "JobRisk" and (m := RISK.match(s)):
                    g["risk"][(x.get("turn"), x.get("side"), x.get("actor_id"))] = float(m.group(1))
                elif t == "Charge" and "declares a charge" in s:
                    g["charges"].append((i, x.get("side"), x.get("actor_id"), x.get("target_id")))
                elif t == "Shooting":
                    g["shots"].append((i, x.get("side"), x.get("actor_id"), x.get("target_id"), _num(r"(\d+) wound\(s\)", s) or 0))
    g["n"] += 1
    for (turn, side, unit, spot) in takes:
        if (turn, side, unit, spot) not in table:
            continue
        holds, worth = table[(turn, side, unit, spot)]
        for p in g["picks"]:
            if p["turn"] == turn and p["side"] == side and p["unit"] == unit and p["kind"] not in ("charge",):
                scores_each_turn = spot.startswith("Marker") or "hill" in spot.lower()
                p["kind"], p["worth"] = ("advance-spot" if not holds else "hold" if scores_each_turn else "hold-end", worth)
    for v in g["hist"].values():
        v.sort()
    g["starts"] = sorted((i, t, s) for (t, s), i in g["turnstart"].items())
    # Joined characters: their points go to the nearest unit of their side with the name they joined, where they stood when the battle started.
    t0 = g["starts"][0][0] if g["starts"] else 0

    def pos(uid):
        last = None
        for r in g["hist"].get(uid, []):
            if r[0] <= t0 and r[1]:
                last = r
        return (last[3], last[4]) if last else None
    for u in g["units"].values():
        u["host"] = None
        if u["joined"] and u["tt"] == "Character":
            hosts = [h for h in g["units"].values() if h["side"] == u["side"] and h["cn"] == u["joined"] and h["tt"] != "Character"]
            pu = pos(u["id"])
            if len(hosts) > 1 and pu:
                hosts.sort(key=lambda h: (lambda p: (p[0] - pu[0]) ** 2 + (p[1] - pu[1]) ** 2 if p else 1e9)(pos(h["id"])))
            u["host"] = hosts[0]["id"] if hosts else None
    for u in g["units"].values():
        u["vp"] = u["points"] + sum(c["points"] for c in g["units"].values() if c.get("host") == u["id"])
    g["byname"] = {(u["side"], u["name"]): u for u in g["units"].values()}
    return g


def _window(g, i, side, which):
    """(first action id, end) of this player turn, the side's own next one or the enemy's next one; None when there is none."""
    S = g["starts"]
    if which == "this":
        ks = [k for k, (a, _, _) in enumerate(S) if a <= i]
        if not ks:
            return None
        k = ks[-1]
    else:
        want = side if which == "own" else ("Opponent" if side == "Mine" else "Mine")
        ks = [k for k, (a, _, s) in enumerate(S) if a > i and s == want]
        if not ks:
            return None
        k = ks[0]
    return S[k][0], (S[k + 1][0] if k + 1 < len(S) else g["n"])


def _state(g, uid, i):
    last = None
    for r in g["hist"].get(uid) or []:
        if r[0] <= i:
            last = r
        else:
            break
    return last


def _gone(g, uid, i):
    s = _state(g, uid, i)
    return s is not None and not s[1]


def _models(g, uid, i):
    s = _state(g, uid, i)
    return None if s is None else (s[2] if s[1] else 0)


def _lost(g, u, start, end):
    """The unit's own points lost between two action ids: all of them (joined characters too) when it is gone by the end, else the models
    lost as a share of its points."""
    if _gone(g, u["id"], start):
        return 0.0
    if _gone(g, u["id"], end):
        return float(u["vp"])
    m0, m1 = _models(g, u["id"], start), _models(g, u["id"], end)
    if m0 is None or m1 is None:
        return 0.0
    return max(0, m0 - m1) * u["points"] / max(1, u["mc"])


def unit_type(u):
    if u is None:
        return "?"
    if u["tt"] == "Character":
        return "Character (wizard)" if u["wz"] else "Character"
    return u["rt"] or u["tt"] or "?"


def happened(g, p):
    """{measure: value} for one pick (empty when nothing can be said)."""
    me = g["byname"].get((p["side"], p["unit"]))
    if me is None:
        return {}
    own = [g["units"][i] for i in p["ids"] if i in g["units"] and g["units"][i]["side"] == p["side"]]
    enemy = [g["units"][i] for i in p["ids"] if i in g["units"] and g["units"][i]["side"] != p["side"]]
    k = p["kind"]
    out = {}
    risk = g["risk"].get((p["turn"], p["side"], me["id"]))
    if risk is not None:
        w = _window(g, p["i"], p["side"], "enemy")
        if w:
            out["risk"] = risk
            out["lost"] = _lost(g, me, w[0], w[1])
    if k == "charge" and enemy:
        tg = enemy[0]
        this = _window(g, p["i"], p["side"], "this")
        if this:
            out["declared"] = any(this[0] <= c[0] < this[1] and c[2] == me["id"] and c[3] == tg["id"] for c in g["charges"])
        w1 = _window(g, p["i"], p["side"], "own")
        w2 = _window(g, w1[0], p["side"], "own") if w1 else None
        h = w2[0] if w2 else g["n"]
        out["net"] = _gone(g, tg["id"], h) * tg["vp"] - _gone(g, me["id"], h) * me["vp"]
    elif k == "shoot":
        this = _window(g, p["i"], p["side"], "this")
        if this:
            vp = 0.0
            for (i, _, actor, target, wounds) in g["shots"]:
                if this[0] <= i < this[1] and actor == me["id"] and target in g["units"]:
                    t = g["units"][target]
                    vp += wounds * t["points"] / max(1, t["mc"] * t["w"])
            out["vp"] = vp
    elif k == "hold":
        t, other = p["turn"], ("Opponent" if p["side"] == "Mine" else "Mine")
        first = next((s for (_, tt, s) in g["starts"] if tt == t), p["side"])
        out["vp"] = sum(o[4] for o in g["obj"] if o[2] == p["side"] and o[3] == p["unit"] and (
            (o[0] == t and o[1] == p["side"]) or (o[1] == other and o[0] == (t if first == p["side"] else t + 1))))
        out["vp3"] = out["vp"] + sum(o[4] for o in g["obj"] if o[2] == p["side"] and o[3] == p["unit"] and o[0] == t + 1 and o[1] == p["side"])
    elif k in ("close-in", "turn", "advance") and enemy:
        w = _window(g, p["i"], p["side"], "own")
        if w:
            out["followed"] = any(w[0] <= c[0] < w[1] and c[2] == me["id"] and c[3] == enemy[0]["id"] for c in g["charges"])
    elif k == "screen" and own:
        w = _window(g, p["i"], p["side"], "enemy")
        if w:
            end = min([c for c in g["combat"] if w[0] <= c < w[1]], default=w[1])  # before combat: what shooting and magic took
            m0, m1 = _models(g, own[0]["id"], w[0]), _models(g, own[0]["id"], end)
            if m0 is not None and m1 is not None:
                out["wounds"] = max(0, m0 - m1) * own[0]["w"]
                out["said"] = p["wounds"] if p["wounds"] is not None else None
    elif k in ("redirect", "lure") and enemy:
        w = _window(g, p["i"], p["side"], "enemy")
        if w:
            ch = [c for c in g["charges"] if w[0] <= c[0] < w[1] and c[2] == enemy[0]["id"]]
            out["guarded"] = bool(own) and any(c[3] == own[0]["id"] for c in ch)
            out["chaff"] = any(c[3] == me["id"] for c in ch)
    return out


def collect(batch_dirs):
    """(games, rows): rows are (side, unit type, kind, claimed or None, happened dict)."""
    rows, games = [], 0
    for d in batch_dirs:
        for path in sorted(glob.glob(os.path.join(d, "game-*.log.jsonl"))):
            try:
                g = read_game(path)
            except (OSError, ValueError, KeyError, IndexError):
                continue
            games += 1
            for p in g["picks"]:
                rows.append((p["side"], unit_type(g["byname"].get((p["side"], p["unit"]))), p["kind"], p["worth"], happened(g, p)))
    return games, rows


def _mean(v):
    v = [x for x in v if x is not None]
    return sum(v) / len(v) if v else None


def _f(x, digits=0, pct=False):
    if x is None:
        return "-"
    return f"{x:.0%}" if pct else f"{x:.{digits}f}"


def _happened_text(kind, hs):
    if kind == "charge":
        return f"net {_f(_mean([h.get('net') for h in hs]))} VP in 2 turns; declared {_f(_mean([h.get('declared') for h in hs]), pct=True)}"
    if kind == "shoot":
        return f"{_f(_mean([h.get('vp') for h in hs]), 1)} VP of wounds that turn"
    if kind == "hold":
        return f"{_f(_mean([h.get('vp3') for h in hs]), 1)} VP scored over the claim's three moments (this turn, the enemy's next, own next); {_f(_mean([h.get('vp') for h in hs]), 1)} over the first two"
    if kind in ("close-in", "turn", "advance"):
        return f"charged that target next turn {_f(_mean([h.get('followed') for h in hs]), pct=True)}"
    if kind == "screen":
        return f"guarded unit lost {_f(_mean([h.get('wounds') for h in hs]), 2)} wounds (line said {_f(_mean([h.get('said') for h in hs]), 2)} a turn)"
    if kind in ("redirect", "lure"):
        return f"enemy charged the guarded friend {_f(_mean([h.get('guarded') for h in hs]), pct=True)}, the chaff {_f(_mean([h.get('chaff') for h in hs]), pct=True)}"
    return "-"


def claims_table(batch_dirs, label):
    """The two tables as Markdown lines (empty when no game has picks)."""
    games, rows = collect(batch_dirs if isinstance(batch_dirs, (list, tuple)) else [batch_dirs])
    if not rows:
        return []
    off = [o for o in dict.fromkeys(rules_off_line(d) for d in (batch_dirs if isinstance(batch_dirs, (list, tuple)) else [batch_dirs])) if o]
    out = [f"### Claimed against happened, per job: {label}", "", *([" ".join(off), ""] if off else []),
           f"{games} game{'' if games == 1 else 's'}. Claimed = the VP the pick's line said (the charge figure counts two turns: read it against the two-turn net). "
           "Happened = what came after the pick (job figures report option 12, Morten 2026-11-13).", "",
           "Risk claimed = the VP the pick took off for the enemy's next turn (JOB RISK rows, 2026-11-16); Lost = the unit's own points lost in that "
           "enemy turn.", "",
           "| Job | Side | Picks a game | Claimed (mean VP) | Happened | Risk claimed (mean VP) | Lost, enemy's next turn (mean VP) |",
           "| --- | --- | --- | --- | --- | --- | --- |"]
    by = collections.defaultdict(list)
    for side, _, kind, worth, h in rows:
        by[(kind, side)].append((worth, h))
    for kind, label_ in JOBS:
        for side in SIDES:
            v = by.get((kind, side))
            if not v:
                continue
            out.append(f"| {label_} | {side} | {len(v) / max(1, games):.1f} | {_f(_mean([w for w, _ in v]), 1)} | {_happened_text(kind, [h for _, h in v if h])} "
                       f"| {_f(_mean([h.get('risk') for _, h in v]), 1)} | {_f(_mean([h.get('lost') for _, h in v if 'risk' in h]), 1)} |")
    measured = ("charge", "shoot", "hold", "close-in", "advance", "screen", "redirect")
    out += ["", f"#### By unit type: {label}", "", "Both sides together; picks a game, claimed mean VP and what happened.", "",
            "| Unit type | Job | Picks a game | Claimed | Happened |", "| --- | --- | --- | --- | --- |"]
    bt = collections.defaultdict(list)
    for _, typ, kind, worth, h in rows:
        if kind in measured:
            bt[(typ, kind)].append((worth, h))
    counts = collections.Counter(typ for _, typ, kind, _, _ in rows)
    for typ, _ in counts.most_common():
        for kind in measured:
            v = bt.get((typ, kind))
            if v:
                out.append(f"| {typ} | {LABEL[kind]} | {len(v) / max(1, games):.2f} | {_f(_mean([w for w, _ in v]), 1)} | {_happened_text(kind, [h for _, h in v if h])} |")
    return out


def rules_off_line(batch_dir):
    """Which rules each side played without (<batch>/rules-off.txt, SimRulesOff.Now): "TAG" is off for both sides, "TAG@Mine" or
    "TAG@Opponent" for that side's computer only (a head-to-head batch, Morten 2026-11-13). "" when every rule was on."""
    try:
        with open(os.path.join(batch_dir, "rules-off.txt"), encoding="utf-8") as f:
            tags = [t.strip() for t in f if t.strip()]
    except OSError:
        return ""
    if not tags:
        return ""
    sides = {s: [t.rsplit("@", 1)[0] for t in tags if t.endswith("@" + s)] for s in ("Mine", "Opponent")}
    both = [t for t in tags if "@" not in t]
    parts = [f"{s} only: {', '.join(v)}" for s, v in sides.items() if v] + ([f"both sides: {', '.join(both)}"] if both else [])
    return "Rules off - " + "; ".join(parts) + "."


def self_test():
    """A two-unit game: a charge that destroyed its target within two turns, and a close-in followed by that charge. [] when all is well."""
    import tempfile
    problems = []
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(os.path.join(tmp, "parts", "X1-1"))
        with open(os.path.join(tmp, "parts", "X1-1", "units.jsonl"), "w") as f:
            f.write(json.dumps({"side": "Mine", "points": 200, "unit": "Knights", "joinedTo": None}) + "\n")
            f.write(json.dumps({"side": "Opponent", "points": 100, "unit": "Goblins", "joinedTo": None}) + "\n")

        def act(i, turn, side, phase, typ, summary, actor=None, target=None):
            return {"kind": "action", "id": i, "turn": turn, "side": side, "phase": phase, "type": typ, "summary": summary, "actor_id": actor, "target_id": target}

        def frame(after, goblins_on, knights=5):
            return {"kind": "frame", "after": after, "units": [{"id": 1, "on": True, "m": [1] * knights}, {"id": 2, "on": goblins_on, "m": [1] * 20 if goblins_on else []}]}
        lines = [{"kind": "board", "units": [{"id": 1, "s": "Mine", "n": "Knights", "lk": {"tt": "Cavalry", "rt": "Heavy Cavalry", "mc": 5, "w": 1}},
                                             {"id": 2, "s": "Opponent", "n": "Goblins", "lk": {"tt": "Infantry", "rt": "Regular Infantry", "mc": 20, "w": 1}}]},
                 frame(0, True), frame(5, False), frame(5.5, False, 4),
                 act(1, 1, "Mine", "Strategy", "Computer", "Objective for Knights: charge #2 Goblins (100 pts): its best option, worth ~80 VP"),
                 act(2, 1, "Mine", "Movement", "Charge", "Knights declares a charge against Goblins", 1, 2),
                 act(3, 1, "Opponent", "Strategy", "Computer", "Objective for Goblins: advance on #1 Knights: its best option, worth ~5 VP"),
                 act(4, 2, "Mine", "Strategy", "Computer", "Objective for Knights: close in to charge #2 Goblins next turn: its best option, worth ~30 VP"),
                 {**act(4, 2, "Mine", "Strategy", "JobRisk", "JOB RISK: close in to charge #2 Goblins next turn: gain +42.0 VP, risk 12.0 VP, worth +30.0 VP"), "actor_id": 1},
                 act(5, 2, "Opponent", "Strategy", "Other", "Opponent's turn"),
                 act(6, 3, "Mine", "Strategy", "Other", "Mine's turn"),
                 act(7, 3, "Mine", "Movement", "Charge", "Knights declares a charge against Goblins", 1, 2)]
        with open(os.path.join(tmp, "game-X1-1-1.log.jsonl"), "w") as f:
            f.write("\n".join(json.dumps(x) for x in lines) + "\n")
        text = "\n".join(claims_table([tmp], "t"))
        for want in ("| Charge | Mine | 1.0 | 80.0 | net 100 VP in 2 turns; declared 100% | - | - |",
                     "| Close in to charge next turn | Mine | 1.0 | 30.0 | charged that target next turn 100% | 12.0 | 40.0 |",
                     "| Advance on an enemy | Opponent | 1.0 | 5.0 | charged that target next turn 0% | - | - |",
                     "| Heavy Cavalry | Charge | 1.00 | 80.0 | net 100 VP in 2 turns; declared 100% |"):
            if want not in text:
                problems.append(f"job claims: {want}")
        if problems:
            problems.append(text)
    return problems


def main(argv):
    if "--self-test" in argv:
        problems = self_test()
        print("\n".join(problems) if problems else "self-test passed")
        return 1 if problems else 0
    dirs = [a for a in argv if not a.startswith("--")]
    if not dirs:
        print(__doc__)
        return 2
    lines = claims_table(dirs, ", ".join(os.path.basename(os.path.normpath(d)) for d in dirs))
    sys.stdout.write("\n".join(lines or ["No game with job picks in these folders."]) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
