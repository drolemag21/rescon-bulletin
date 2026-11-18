# Role: maintainer work session

The maintainer is talking to you directly. Also read `docs/agents/reference.md`, and `docs/agents/run.md` whenever they ask for a run. Root `CLAUDE.md` rules apply. `docs/COMMANDS.md` lists the commands in plain words; this file says how to carry them out.

## At the start of a session

Check `docs/INBOX.md` and mention how many open items there are (don't list them unless asked).

## Making changes

- **Content** (see `CLAUDE.md` for the list): commit straight to `main`, message starting `content:` (or `run:` when doing a run).
- **System files:** never commit them to `main` directly.
  1. Work on a branch (the session's assigned branch if it has one, otherwise `change/<short-name>`), created from the latest `main`.
  2. Run the build check (`reference.md`) if anything that affects the site changed.
  3. If the change is a decision someone would later ask "why?" about (a new mechanism, a rule change, a trade-off), add or update a record in `docs/decisions/` (format in its `README.md`). Small fixes don't need one.
  4. Add a line to `CHANGELOG.md` under "Unreleased".
  5. Push the branch and, when the maintainer asks, open a pull request into `main` with a description: what changed, why, how it was checked, and any follow-up. Don't merge it yourself; the maintainer merges.
  6. Remember that runs read `CLAUDE.md` and `docs/agents/` from `main`: a change takes effect at the first run after the merge.
- When a PR is merged, move its `CHANGELOG.md` lines from "Unreleased" under the merge date.

## Commands

| Command | How |
|---|---|
| `RESCON n` / `RESCON n for D [every I]` | Change `data/state/rescon.json` and the scheduled task as in `reference.md` ("RESCON state", "Scheduled tasks"), then do one run (`run.md`). |
| `What's the current RESCON?` | Read `data/state/rescon.json`: level, expiry, stack. |
| `Update the bulletin` | One run at the current level (`run.md`). |
| `Post these: <links>` | A run limited to those items: check and label them like any other, then publish (`run.md` steps 5–12). |
| `Mark <entry> <label>` | Change `label`, append to `label_history`, bump `lastmod`; commit as content. |
| `Rule out <entry>: <reason>` | Set `correction` with the date and note, bump `lastmod`; the entry stays. Commit as content. |
| `Make <entry> an incident post` | Set `significant: true`, run `rescon_discord.py incident`, commit as content. |
| `Add source` / `Remove source` / `Exclude <source>` | Source policy: a system change (PR). Log the decision in `docs/sources-log.md`. |
| `Source report` | Follow `report.md` in this session. |
| `Approve` / `Reject <held item or source>` | Publish or drop the held item; for sources, add or log as not added (PR for additions). |
| `Usage report [for N days]` | `python3 scripts/rescon_usage.py report [--days N]`. Relay it; remind them `cost_usd` is an API-price estimate including each session's fixed overhead, and plan limits are under claude.ai → Settings → Usage. |
| `Inbox` | Show open items in `docs/INBOX.md`, numbered, each with a recommendation. Resolve as they decide: do the work (via the right path above), mark `[x]` with the date and resolution, move to Resolved, commit as content. |
| `New dispatcher` | See below. |
| `Turn the update line off` / `on` | A system change to `rescon_discord.py` behaviour (PR). |

## New dispatcher

Swaps in a fresh dispatcher session if the current one is gone or has grown large (it should grow only a few thousand tokens per firing).

1. Don't do it within 10 minutes of a task firing.
2. `create_session` with `https://github.com/drolemag21/rescon-bulletin` as `source_url`, title "RESCON dispatcher (scheduled tasks)", tag `rescon:dispatcher`, and a setup-check prompt (on `main`; `list_sessions`/`create_session`/`archive_session` available; no run). Read the result with `list_events`; if it fails, stop.
3. Delete each RESCON task and create it again with the same name and cron, the canonical prompt (`reference.md`), and `persistent_session_id` = the new session.
4. Replace the dispatcher session id in the root `CLAUDE.md` role table. That's a system change: branch and PR, and ask the maintainer to merge promptly, because until then the new dispatcher won't recognise itself. Note this in the PR.
5. After the merge, `archive_session` the old dispatcher. Report the new session id and task ids.

## Pending decisions

- **Dispatcher growth:** check the dispatcher's `context_usage` after a week; if it grows much faster than a few thousand tokens per firing, tighten `dispatcher.md`.
