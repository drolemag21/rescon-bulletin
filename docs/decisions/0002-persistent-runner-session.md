# 0002. Scheduled runs in one persistent runner session

- **Date:** 2026-11-18
- **Status:** Superseded by 0003

## Context
Scheduled tasks that start a fresh session on each firing give that session no repository, and it can't attach one (tested: the `add_repo` tool isn't available there). Tasks created in the claude.ai UI can have a repository but can't be edited by agents, so every RESCON command would have needed manual edits.

## Decision
One long-lived "runner" session with the repo attached; an agent-created scheduled task wakes it for each run.

## Alternatives considered
- UI-created task with the repo: works, but not manageable by commands.
- Fresh sessions attaching the repo themselves: not possible (tool unavailable).
- Running in the maintainer's own work session: mixes runs with conversation.

## Consequences
Worked, but each run added ~100k tokens to the runner's conversation, and because the prompt cache expires after about an hour, every 6-hourly run re-wrote the whole conversation to cache (12:58 run: $2.77 with no new entries). Replaced by 0003 the same day.
