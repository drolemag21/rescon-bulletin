#!/usr/bin/env python3
"""RESCON usage log: one JSON line per run in usage/runs.jsonl (public, not shown on the site).

A run's token/cost usage is only published when the session's turn ends (in its
`result` event), which is after the run has committed. So:

  record    at the end of a run: writes the row with usage pending.
            --snapshot FILE (a get_session result) gives model, effort and session id.
  backfill  at the start of the NEXT run: fills in a pending row from that session's
            `result` events (list_events kinds ["result"]). Either pass --events FILE
            (a saved list_events result) or the summed numbers directly:
            --cost --input --output --cache-read --cache-write [--web-searches].
  pending   lists rows still waiting for usage (session id and time window).
  report    [--days N]  averages per level and per model/effort, daily totals, projection.
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


def iso(ts: str) -> dt.datetime:
    return dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_rows() -> list[dict]:
    return [json.loads(l) for l in LOG.read_text().splitlines() if l.strip()] if LOG.exists() else []


def save_rows(rows: list[dict]) -> None:
    LOG.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))


def load_snapshot(path: str) -> dict:
    d = json.loads(pathlib.Path(path).read_text())
    c = d.get("ccr", d)
    meta, ctx = c.get("external_metadata", {}), c.get("session_context", {})
    return {"model": meta.get("last_served_model") or ctx.get("model"),
            "effort": ctx.get("effort_level"), "session_id": c.get("id")}


def cmd_record(a):
    snap = load_snapshot(a.snapshot) if a.snapshot else {}
    ended = now_iso()
    row = {
        "started_at": a.started, "ended_at": ended,
        "minutes": round((iso(ended) - iso(a.started)).total_seconds() / 60, 1),
        "level": a.level, "trigger": a.trigger,
        "model": snap.get("model"), "effort": snap.get("effort"),
        **{k: None for k in FIELDS}, "usage_pending": True,
        "searches": a.searches, "fetches": a.fetches, "subagents": a.subagents,
        "new": a.new, "updated": a.updated, "staff_items": a.staff, "held": a.held,
        "session_id": snap.get("session_id"),
    }
    if a.note:
        row["note"] = a.note
    LOG.parent.mkdir(exist_ok=True)
    with LOG.open("a") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(json.dumps(row, indent=2))


def sum_results(events_file: str, start: dt.datetime, end: dt.datetime) -> dict:
    """Sum model_usage_since_last_result over result events from `start` up to and
    including the first result at or after `end` (the turn the run finished in)."""
    text = pathlib.Path(events_file).read_text()
    d = json.loads(text[text.index("{"):text.rindex("}") + 1])
    evs = sorted((e for e in d.get("ccr", d)["data"] if "result" in e), key=lambda e: e["created_at"])
    tot = {k: 0 for k in FIELDS}; tot["web_searches"] = 0; used = 0
    for e in evs:
        at = iso(e["created_at"])
        if at < start:
            continue
        for m in e["result"]["internal_anthropic_catchall"].get("model_usage_since_last_result", {}).values():
            tot["input_tokens"] += m.get("inputTokens", 0)
            tot["output_tokens"] += m.get("outputTokens", 0)
            tot["cache_read_tokens"] += m.get("cacheReadInputTokens", 0)
            tot["cache_write_tokens"] += m.get("cacheCreationInputTokens", 0)
            tot["cost_usd"] += m.get("costUSD", 0)
            tot["web_searches"] += m.get("webSearchRequests", 0)
        used += 1
        if at >= end:
            break
    else:
        sys.exit("No result event at or after the run's end in this file: fetch the right page, or retry next run.")
    return tot


def cmd_backfill(a):
    rows = load_rows()
    pend = [r for r in rows if r.get("usage_pending") and r.get("session_id") == a.session
            and (not a.ended_at or r["ended_at"] == a.ended_at)]
    if not pend:
        sys.exit("No pending row for that session.")
    r = pend[0]
    start = iso(r["started_at"]) if r.get("started_at") else iso(r["ended_at"]) - dt.timedelta(minutes=r.get("minutes") or 0)
    if a.events:
        tot = sum_results(a.events, start, iso(r["ended_at"]))
    else:
        tot = {"input_tokens": a.input, "output_tokens": a.output, "cache_read_tokens": a.cache_read,
               "cache_write_tokens": a.cache_write, "cost_usd": a.cost, "web_searches": a.web_searches}
    tot["cost_usd"] = round(tot["cost_usd"], 4)
    r.update({k: tot[k] for k in FIELDS}); r["usage_pending"] = False
    if tot.get("web_searches") is not None:
        r["web_searches_billed"] = tot["web_searches"]
    save_rows(rows)
    print(json.dumps(r, indent=2))


def cmd_pending(a):
    for r in load_rows():
        if r.get("usage_pending"):
            print(json.dumps({k: r.get(k) for k in ("session_id", "started_at", "ended_at", "level", "trigger")}))


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
    rows = load_rows()
    pending = [r for r in rows if r.get("usage_pending") or r.get("cost_usd") is None]
    rows = [r for r in rows if r not in pending]
    if a.days:
        cut = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=a.days)
        rows = [r for r in rows if dt.datetime.fromisoformat(r["ended_at"].replace("Z", "+00:00")) >= cut]
    if not rows:
        sys.exit("No runs in that window.")
    lines = [f"# RESCON usage report ({'last %d days' % a.days if a.days else 'all time'})", "",
             f"**Total:** {summarize(rows)} · total ${sum(r['cost_usd'] for r in rows):.2f}"
             + (f" · {len(pending)} run(s) still waiting for usage backfill" if pending else ""), ""]

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
    r.add_argument("--snapshot", help="get_session result saved to a file")
    r.add_argument("--started", required=True, help="run start time, ISO UTC")
    r.add_argument("--level", required=True); r.add_argument("--trigger", choices=["manual", "scheduled"], required=True)
    for k in ("searches", "fetches", "subagents", "new", "updated", "staff", "held"):
        r.add_argument(f"--{k}", type=int, default=0)
    r.add_argument("--note")
    r.set_defaults(fn=cmd_record)
    b = sub.add_parser("backfill")
    b.add_argument("--session", required=True); b.add_argument("--ended-at", help="pick a specific pending row")
    b.add_argument("--events", help="saved list_events result (kinds result)")
    b.add_argument("--cost", type=float, default=0.0)
    for k in ("input", "output", "cache-read", "cache-write"):
        b.add_argument(f"--{k}", type=int, default=0)
    b.add_argument("--web-searches", type=int)
    b.set_defaults(fn=cmd_backfill)
    q = sub.add_parser("pending"); q.set_defaults(fn=cmd_pending)
    s = sub.add_parser("report"); s.add_argument("--days", type=int); s.set_defaults(fn=cmd_report)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
