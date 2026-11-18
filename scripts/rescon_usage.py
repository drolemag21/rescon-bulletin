#!/usr/bin/env python3
"""RESCON usage log: one JSON line per run in usage/runs.jsonl (public, not shown on the site).

Session usage counters are cumulative for the whole session, so each run records
the DELTA between a snapshot taken at the start of the run and one at the end.
Snapshots are the `get_session` result (or just its `external_metadata.usage`
object) saved to a file by the agent.

  record   --start FILE --end FILE --level N --trigger manual|scheduled
           [--searches N --fetches N --subagents N --new N --updated N --staff N --held N --note TEXT]
  report   [--days N]      Averages per level and per model/effort, daily totals, 7-day projection.
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import pathlib
import statistics
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOG = ROOT / "usage/runs.jsonl"
FIELDS = ("input_tokens", "output_tokens", "cache_read_tokens", "cache_write_tokens", "cost_usd")


def load_snapshot(path: str) -> dict:
    d = json.loads(pathlib.Path(path).read_text())
    meta = d.get("ccr", d).get("external_metadata", d) if isinstance(d, dict) else {}
    usage = meta.get("usage", d.get("usage", d))
    ctx = d.get("ccr", d).get("session_context", {})
    return {
        "usage": {k: usage.get(k, 0) or 0 for k in FIELDS},
        "model": meta.get("last_served_model") or ctx.get("model"),
        "effort": ctx.get("effort_level"),
        "session_id": d.get("ccr", d).get("id"),
    }


def cmd_record(a):
    s, e = load_snapshot(a.start), load_snapshot(a.end)
    delta = {k: round(e["usage"][k] - s["usage"][k], 4) for k in FIELDS}
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    started = dt.datetime.fromisoformat(a.started.replace("Z", "+00:00")) if a.started else None
    row = {
        "ended_at": now.isoformat().replace("+00:00", "Z"),
        "minutes": round((now - started).total_seconds() / 60, 1) if started else None,
        "level": a.level,
        "trigger": a.trigger,
        "model": e["model"],
        "effort": e["effort"],
        **delta,
        "searches": a.searches, "fetches": a.fetches, "subagents": a.subagents,
        "new": a.new, "updated": a.updated, "staff_items": a.staff, "held": a.held,
        "session_id": e["session_id"],
    }
    if a.note:
        row["note"] = a.note
    LOG.parent.mkdir(exist_ok=True)
    with LOG.open("a") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(json.dumps(row, indent=2))


def fmt_tokens(n: float) -> str:
    return f"{n/1e6:.2f}M" if n >= 1e6 else f"{n/1e3:.1f}k"


def summarize(rows: list[dict]) -> str:
    cost = [r["cost_usd"] for r in rows]
    out = [r["output_tokens"] for r in rows]
    mins = [r["minutes"] for r in rows if r.get("minutes") is not None]
    return (f"{len(rows)} runs · avg ${statistics.mean(cost):.2f} (max ${max(cost):.2f}) · "
            f"avg out {fmt_tokens(statistics.mean(out))}"
            + (f" · avg {statistics.mean(mins):.0f} min" if mins else ""))


def cmd_report(a):
    if not LOG.exists():
        sys.exit("No runs logged yet.")
    rows = [json.loads(l) for l in LOG.read_text().splitlines() if l.strip()]
    if a.days:
        cut = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=a.days)
        rows = [r for r in rows if dt.datetime.fromisoformat(r["ended_at"].replace("Z", "+00:00")) >= cut]
    if not rows:
        sys.exit("No runs in that window.")
    lines = [f"# RESCON usage report ({'last %d days' % a.days if a.days else 'all time'})", "",
             f"**Total:** {summarize(rows)} · total ${sum(r['cost_usd'] for r in rows):.2f}", ""]

    lines.append("## By level")
    by_level = collections.defaultdict(list)
    for r in rows:
        by_level[r["level"]].append(r)
    intervals = {"4": 12, "3": 6, "2": 3, "1": 2}
    for lvl in sorted(by_level, key=str):
        rs = by_level[lvl]
        avg = statistics.mean(r["cost_usd"] for r in rs)
        per_day = 24 / intervals.get(str(lvl), 24)
        lines.append(f"- **RESCON {lvl}:** {summarize(rs)} · timed-window projection ≈ ${avg*per_day:.2f}/day, ${avg*per_day*7:.2f}/week")
    lines.append("")

    lines.append("## By model / effort")
    by_me = collections.defaultdict(list)
    for r in rows:
        by_me[(r.get("model"), r.get("effort"))].append(r)
    for (m, eff), rs in sorted(by_me.items(), key=lambda kv: str(kv[0])):
        lines.append(f"- **{m} / {eff}:** {summarize(rs)}")
    lines.append("")

    lines.append("## Per day (UTC)")
    by_day = collections.defaultdict(list)
    for r in rows:
        by_day[r["ended_at"][:10]].append(r)
    for day in sorted(by_day):
        rs = by_day[day]
        lines.append(f"- {day}: {len(rs)} runs · ${sum(r['cost_usd'] for r in rs):.2f}")
    lines.append("")

    lines.append("## Biggest runs")
    for r in sorted(rows, key=lambda r: r["cost_usd"], reverse=True)[:3]:
        lines.append(f"- {r['ended_at']} · RESCON {r['level']} · {r.get('model')}/{r.get('effort')} · ${r['cost_usd']:.2f} · "
                     f"{r.get('new', 0)} new, {r.get('updated', 0)} updated")
    lines += ["", "_cost_usd is an API-price estimate. On a subscription, check claude.ai → Settings → Usage for plan limits._"]
    print("\n".join(lines))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("record")
    r.add_argument("--start", required=True); r.add_argument("--end", required=True)
    r.add_argument("--started", help="run start time, ISO UTC")
    r.add_argument("--level", required=True); r.add_argument("--trigger", choices=["manual", "scheduled"], required=True)
    for k in ("searches", "fetches", "subagents", "new", "updated", "staff", "held"):
        r.add_argument(f"--{k}", type=int, default=0)
    r.add_argument("--note")
    r.set_defaults(fn=cmd_record)
    s = sub.add_parser("report"); s.add_argument("--days", type=int); s.set_defaults(fn=cmd_report)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
