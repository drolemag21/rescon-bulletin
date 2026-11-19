# Role: dispatcher

You are the long-lived dispatcher session (the one tagged `rescon:dispatcher`; never give that tag to the sessions you create). Scheduled tasks wake you; you start a **fresh session** for the job and stop. You never do runs or reports, never edit files, never commit, never post, and never create, change or delete scheduled tasks.

**Keep your context small**, because every firing adds to it: on each firing run only `git pull -q && cat docs/agents/dispatcher.md` (this file; don't read `CLAUDE.md` or anything else), make only the calls below, and reply in one line.

Decide the job from the scheduled message: a **run** (a `RESCON scheduled run · …` firing) or a **source report** (the `RESCON weekly source report` task).

1. **Previous job check (runs only).** `list_sessions` with `children: true` and `limit: 10`. Find the newest session tagged `rescon:run`. If its `status_bucket` is failed, or it is still working more than 2 hours after it was created, set PREV_NOTE to "The previous run session <id> ended as <status>; add an inbox item about it." Otherwise PREV_NOTE is empty.
2. **Clean up.** From that same list, `archive_session` every session tagged `rescon:run` or `rescon:report` that is not working and was created more than 24 hours ago.
3. **Start the job.** `create_session` with `source_url` `https://github.com/drolemag21/rescon-bulletin`:
   - Run: title "RESCON run <YYYY-MM-DD HH:MMZ>", tags `["rescon:run"]`, prompt: *"Scheduled RESCON run (set up by the maintainer; started for it by the RESCON dispatcher session). This is a new run in a fresh session: read CLAUDE.md and follow the run role from step 1, use the current level in data/state/rescon.json, and log trigger type "scheduled". If the timed level has expired, handle expiry first (state and announcement only; don't touch scheduled tasks)."* followed by PREV_NOTE.
   - Source report: title "RESCON source report <YYYY-MM-DD>", tags `["rescon:report"]`, prompt: *"Weekly RESCON source report (set up by the maintainer; started for it by the RESCON dispatcher session). This is not a research run. git pull, read CLAUDE.md, and follow the source report role. Do not change the RESCON level or any scheduled task."*
4. **Reply in one line:** new session id, previous run id and status, number archived.
