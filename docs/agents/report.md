# Role: source report

Triggered by the weekly task (via the dispatcher) or by the maintainer's `Source report`. It is not a research run: no entries, no `bulletin.json` change, no usage row, no commits other than an inbox item, and no changes to the RESCON level or scheduled tasks. Root `CLAUDE.md` rules apply.

1. `git pull`. Collect the last 7 days of source decisions: `docs/sources-log.md` rows in that window, plus `git log --since="7 days ago" -p -- data/sources.yml docs/sources-log.md` for what changed and the commit messages.
2. Write the report: each decision (added, not added, held for the maintainer, removed, excluded) with its full reasoning, any source requests still held for the maintainer, and source counts per tier. If nothing changed, say so in one line.
3. Post it with `python3 scripts/rescon_discord.py staff-post -` (stdin). `#rescon-staff` is private, so reasoning can be fuller than the public log, but still no staff names or quotes in anything committed.
4. If something needs the maintainer (a broken step, a source problem), add an item to `docs/INBOX.md` (format at the top of that file, origin `report <your session id>`) and commit only that file with a message starting `content:`. Don't fix anything else here.
