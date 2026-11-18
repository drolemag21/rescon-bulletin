# 0003. Dispatcher session starts a fresh session per job

- **Date:** 2026-11-18
- **Status:** Accepted

## Context
The persistent runner (0002) grew by ~100k tokens per run and paid a full cache re-write each run. Sessions created with `create_session` (unlike sessions started by a scheduled task) do get the repository.

## Decision
The long-lived session becomes a **dispatcher**: scheduled tasks wake it, and it starts a fresh session (repo attached) for each run or source report, archives finished ones after 24h, and flags a previous run that failed. Task prompts can only be edited from inside the dispatcher, so they stay generic and the behaviour lives in `docs/agents/dispatcher.md`.

## Alternatives considered
- `New runner` rotations or `/clear` in the runner: manual, and only reset the growth now and then.
- A sub-agent inside the dispatcher: a *fork* sub-agent inherits the parent's whole context (the original problem); a fresh one might work but can't be relied on to start its own sub-agents, which RESCON 2 and 1 need.

## Consequences
Tested: the dispatcher started a run session in ~30s; the run cost $1.39 vs $2.20–2.77 in the runner, and its usage is exact per session. Each run still carries a fixed ~87k-token session overhead (tools, system prompt, CLAUDE.md), so run frequency is the main cost lever. One session per run appears in the session list until archived.
