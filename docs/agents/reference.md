# Shared reference

Rules used by more than one role (runs and maintainer work sessions). Root `CLAUDE.md` rules apply on top.

## Labels: the highest label a source supports on its own

- `confirmed`: tier 1 official source, or a statement from the victim or operator. Nothing else.
- `reported`: tier 2–3, or an established tier 4a researcher.
- `unverified`: single-source or eyewitness (tier 4a), not corroborated.
- `claimed`: a threat actor's assertion, reported via tier 2–3 coverage.

Label by what you actually read: an official statement you only read through press coverage supports `reported`, not `confirmed`. A staff submission gets the same label it would get from any other source. "Staff Submitted" shows where an item came from, not that it's verified.

## Significant incidents (get their own forum post)

- A confirmed attack or disruption affecting in-scope critical infrastructure.
- A new joint advisory from US and/or allied agencies.
- Disclosure of a major nation-state campaign or a pre-positioning campaign.
- An actively exploited vulnerability in widely deployed infrastructure or OT technology, with an official advisory.

An entry is only significant if its own label supports the criterion: an attack or disruption needs `confirmed`.

**Possibly significant but only press coverage?** Read the victim's or agency's own statement (the source access order in `run.md`). If you can't reach it (e.g. the host isn't allowlisted), publish the entry as `reported` with `significant: false`, and add an inbox item naming the host so the maintainer can allow it. A later run that confirms the item sets `significant: true` and posts the incident then.

Set `significant: true` on qualifying entries. Don't post incidents for routine items. Flooding the forum makes members stop reading. If you're unsure whether an item qualifies, decide, and add an inbox item explaining the call.

## Entry format

Path: `content/entries/YYYY/MM/DD/<short-kebab-slug>.md`, dated by the UTC day it was first seen.

```yaml
---
title: "Plain, factual headline"
date: 2026-11-18T14:05:00Z         # first seen by RESCON (UTC, never future)
lastmod: 2026-11-18T14:05:00Z      # bump on every change
label: reported                    # confirmed | reported | unverified | claimed
label_history:
  - { at: 2026-11-18T14:05:00Z, label: reported }
sectors: [energy]                  # keys from data/sectors.yml; first = primary
countries: [us]                    # keys from data/countries.yml (add a key there if needed)
sources:
  - { name: "The Record", url: "https://…", tier: "3" }
  - { name: "WSJ", url: "https://…", tier: "3", paywalled: true }
guidance: { name: "CISA AA26-xxx", url: "https://…" }   # optional, official guidance only
submitted_by: rescon               # rescon | staff
significant: false
correction: null                   # { at: …, note: "Ruled out — …" }
discord_thread_id: null            # set by `incident`
---
What
: What happened, to whom, when. Who reported or confirmed it.

Who
: Who is behind it and who says so, or "Unknown" / "Not attributed".

Status
: What's still unclear, denials, deadlines, or what happens next.
```

The summary is a Markdown definition list with exactly these three terms, in this order (a term line, then a line starting with `: `, then a blank line). The site shows it as a labeled grid and Discord as bold lead-ins.

- **At most 75 words in total, and no sentence over 30 words.** Split long sentences; don't chain clauses with semicolons. Each line is one or two sentences.
- **Who** is always present. Use "Unknown" when nobody has attributed it, and keep attribution hedged as the source hedges it (`claimed` items: "Claimed by X; not verified").
- Leave out detail that doesn't fit. Long lists (e.g. a batch of CVEs) keep the most important item and summarize the rest ("and three others"); the source link has the full list.
- When updating an older entry whose summary is a plain paragraph, leave the paragraph as it is unless the update changes the summary anyway; then rewrite it in this format.

When updating an entry, bump `lastmod`, append to `label_history` if the label changed, and add new sources. A correction goes in `correction` and the entry stays.

## RESCON state (`data/state/rescon.json`)

```json
{ "level": 3, "set_at": "…Z", "expires_at": null, "interval": null, "stack": [] }
```

- **Untimed `RESCON n`:** set the level and `set_at`, set `expires_at` to null, clear `stack`, delete the `RESCON scheduled runs` task if it exists, then do one run.
- **Timed `RESCON n for D [every I]`:** push the current state onto `stack`, set the new level with `expires_at` and `interval` (the default from `data/levels.yml`, minimum 1h). Create or update the `RESCON scheduled runs` task (see "Scheduled tasks") at that interval. Then do the first run now.
- **Expiry (checked at step 2 of every run):** if `expires_at` has passed, pop the `stack` until you reach an entry whose `expires_at` is null or still in the future, and restore it. If the restored level is timed, set `RESCON scheduled runs` to its interval; if it's untimed, delete that task. Announce it with `publish --note "⏱️ RESCON 2 window ended → returning to RESCON 4"`.

## Scheduled tasks

Scheduled work goes through the long-lived **dispatcher session** (the session tagged `rescon:dispatcher`; find it with `list_sessions` and its tags), which starts a fresh session per job. See `docs/decisions/` for why.

- `RESCON scheduled runs` exists only during timed windows (cron = the interval, e.g. `0 */6 * * *`). `RESCON weekly source report` is permanent (Mondays 15:00 UTC): never delete or change it when a level changes or a window expires, and never count it as a duplicate. Both are created with `create_trigger`, `persistent_session_id` = the dispatcher. Never use `create_new_session_on_fire`. Use `list_triggers` before creating one; never leave duplicates.
- Task prompts can only be edited from inside the dispatcher, so they stay generic. Canonical prompts when creating them:
  - Runs: *"Scheduled RESCON run (set up by the maintainer). git pull, then follow CLAUDE.md for your role."*
  - Report: *"Weekly RESCON source report (set up by the maintainer). git pull, then follow CLAUDE.md for your role."*
- **Changing a window:** try `update_trigger` with only `cron_expression` (and `enabled`); if refused, delete the task and create it again with the canonical prompt. When no timed window is active, delete `RESCON scheduled runs`.

## Local build

```bash
H=/tmp/hugo && mkdir -p $H && cd $H && \
curl -sSfLO https://github.com/gohugoio/hugo/releases/download/v0.169.0/hugo_0.169.0_linux-amd64.tar.gz && \
echo "2d2f0bfe357d8cb4cec02f6bb28a3bff34978c8dda44b618029c5eb9d66765a7  hugo_0.169.0_linux-amd64.tar.gz" | sha256sum -c - && \
tar -xzf hugo_0.169.0_linux-amd64.tar.gz hugo && cd - && /tmp/hugo/hugo --minify -d /tmp/hugo/out
```

Keep the version and checksum in sync with `.github/workflows/pages.yml` and `.github/workflows/check.yml`.
