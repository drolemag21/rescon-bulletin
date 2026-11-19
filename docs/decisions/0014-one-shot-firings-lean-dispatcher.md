# 0014. One-shot firings for timed windows; leaner dispatcher

- **Date:** 2026-11-19
- **Status:** Accepted

## Context
The first window expiry (RESCON 3, 2026-11-19) restored RESCON 5 correctly, but the run could not remove the recurring `RESCON scheduled runs` task: the unattended session's auto-mode permission check refused `update_trigger` (disable) as a destructive action, and the run declined to delete it. The task kept firing every 6h until the maintainer paused it and a work session deleted it. Separately, the dispatcher grew ~20–25k tokens per firing, not the few thousand expected: it re-read `CLAUDE.md`, received full session listings, and carried notification text each time.

## Decision
- Timed windows are scheduled as **one-shot firings** (`run_once_at`), created by the maintainer work session for the whole timeline the stack implies, including a stand-down firing just after each expiry. One-shots disable themselves after firing, so nothing needs removing. Runs never create, change or delete scheduled tasks. Cancelling or replacing a window deletes the pending one-shots, in a maintainer session.
- The dispatcher reads only `dispatcher.md` after a quiet `git pull`, lists at most 10 sessions, and never touches scheduled tasks.

## Alternatives considered
- Keep the recurring task and have runs disable it: blocked by the permission check.
- Have the dispatcher skip runs when the level is 5: leaves a task firing forever at ~$0.65 a firing.
- Ask the maintainer to delete the task at every expiry: manual step on every window.

## Consequences
A 24h window at 6h makes about 5 one-shots; RESCON 1 for 24h every 2h about 13. Pending one-shots show in the scheduled-tasks list until they fire. Deleting a task does not delete the dispatcher it delivers to (seen 2026-11-18 and 2026-11-19), contrary to the run's worry. Untested until the next timed window.
