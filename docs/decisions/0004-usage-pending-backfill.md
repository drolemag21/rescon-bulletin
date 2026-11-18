# 0004. Usage: record pending, backfill from the next run

- **Date:** 2026-11-18
- **Status:** Accepted

## Context
`get_session` returned no usage during a session's first turn, so the original start/end snapshots logged zeros. A turn's usage is only published when the turn ends, which is after the run has committed its log row.

## Decision
Each run writes its row as pending with `usage_start` (the session's cumulative usage when the run began). The next run fills it in from a fresh `get_session` of that session (the delta), falling back to summing the session's `result` events. Costs include the session's fixed overhead; they are API-price estimates.

## Alternatives considered
- Event-log backfill only: works, but result events are large and add thousands of tokens to the backfilling run's context.
- Separate "overhead" and "work" figures: only an estimate; the total is what a run really costs.

## Consequences
The newest run's cost is always pending until the next run. With one session per run (0003) the delta is exact. Effort level is logged as null for dispatched sessions.
