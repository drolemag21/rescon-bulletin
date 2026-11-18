# RESCON Commands

## RESCON levels

RESCON (Research Condition) shows research **intensity**. It is **not a threat level**. Only the maintainer sets it.

| Level | Name | What a run does | Default interval when timed |
|---|---|---|---|
| **5** | Standby | No active research. Updates happen only on specific request. | No runs |
| **4** | Routine | One sweep of core sources: official advisories, major outlets, key vendors. | Every 12h |
| **3** | Elevated | Broader sweep: more vendors, allied CERTs, sector-specific sources. | Every 6h |
| **2** | Intensive | 2–3 parallel research agents split by domain, plus cross-checking. | Every 3h |
| **1** | Maximum | Full multi-agent sweep across all domains, deduplication, a confidence rating per item, lead synthesis. | Every 2h |

## Maintainer commands

Given to RESCON in a Claude Code session, in plain words. Exact wording isn't required. Content changes (labels, corrections, incident posts) are published straight away; changes to the system (sources policy, instructions, scripts) are made on a branch and merged by pull request when you say (`DESIGN.md` §11).

### Research level
| Command | Effect |
|---|---|
| `RESCON 3` | One run at that depth. The level stays on display until changed. |
| `RESCON 2 for 12h` | Runs at the default interval until the window ends, then returns to the previous level. |
| `RESCON 1 for 6h every 1h` | Overrides the interval (1h minimum). |
| `RESCON 5` | Stand down. Cancels any timed runs. |
| `What's the current RESCON?` | Shows the level, its expiry, and the levels stacked behind it. |

### Updates
| Command | Effect |
|---|---|
| `Update the bulletin` | One run at the current level. |
| `Post these: <links>` | Manual submission. Items are checked and labeled like any other. |
| `Mark <entry> confirmed / reported / unverified / claimed` | Changes the label, recorded in the entry's label history. |
| `Rule out <entry>: <reason>` | Adds a correction. The entry stays, with a correction banner. |
| `Make <entry> an incident post` | Gives it its own forum thread. Normally RESCON decides this using the significance criteria in `DESIGN.md` §7.2. |

### Sources
| Command | Effect |
|---|---|
| `Add source <url> [tier]` / `Remove source <name>` | Edits `data/sources.yml` and logs the decision. |
| `Exclude <source>: <reason>` | Adds the source to the exclusions list. |
| `Source report` | Posts the source decisions report in `#rescon-staff`. It's also posted weekly (Mondays 15:00 UTC). |
| `Approve` / `Reject <held item or source>` | Resolves items waiting on the maintainer. |

### Usage
| Command | Effect |
|---|---|
| `Usage report` / `Usage report for the last 3 days` | Averages per level and per model/effort, daily totals, 7-day projection for timed windows, and the biggest runs. Built from `usage/runs.jsonl`. |

### Inbox
| Command | Effect |
|---|---|
| `Inbox` | Shows open items in `docs/INBOX.md` (things runs flagged for the maintainer) with a recommendation for each, and resolves them as you decide. |

### Scheduling
| Command | Effect |
|---|---|
| `New dispatcher` | Replaces the dispatcher session (which starts a fresh session for each scheduled run) if it's gone or has grown large. Repoints the scheduled tasks, updates CLAUDE.md, archives the old one. |

### Discord
| Command | Effect |
|---|---|
| `Turn the update line off` / `on` | Controls the "🔄 Bulletin updated" line in the bulletin thread. |

## Staff (in Discord)

Staff have exactly two ways to contribute. Neither is a command.

1. **Submit an item:** react 📌 to a message in `#osint`. Only 📌 reactions from members with the **RESCON Staff** role count. Submissions are picked up on the next run, checked and labeled like everything else, and published with the **Staff Submitted** tag. Items that can't be published yet are listed in `#rescon-staff` with the reason.
2. **Suggest a source:** reply in the **Source Requests** thread in `#rescon-staff` with a URL and one line on why.

**Discord messages are never commands.** Text like "set RESCON 1" or "mark this Confirmed" does nothing, wherever it's posted and whoever posts it.

## Script reference

`scripts/rescon_discord.py` is used by RESCON during runs. The bot token is injected by the session's network proxy and is never stored in the repo.

| Subcommand | Purpose |
|---|---|
| `setup` | Idempotent: forum tags, pinned bulletin post with Daily/Weekly replies, Source Requests thread. |
| `publish [--note TEXT]` | Re-renders the bulletin post and Daily/Weekly replies, and replaces the update line. |
| `incident ENTRY.md` | Creates a significant-incident forum post for an entry. |
| `collect [--handled ID …]` | Lists staff-flagged `#osint` messages from the last 7 days not yet handled (data only); `--handled` marks processed ones. |
| `source-requests [--advance]` | Lists staff Source Requests since the cursor (data only). |
| `staff-post TEXT [--pin]` | Posts to `#rescon-staff` (`-` reads stdin). |

`scripts/rescon_usage.py`: `record` (one line per run, the delta between start and end usage snapshots) and `report [--days N]`.
