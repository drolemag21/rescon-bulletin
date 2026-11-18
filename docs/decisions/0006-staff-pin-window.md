# 0006. Staff 📌: scan a 7-day window, mark handled explicitly

- **Date:** 2026-11-18
- **Status:** Accepted

## Context
`collect` only read `#osint` messages posted after a cursor, and the cursor advanced past every message fetched. A 📌 added later to an already-seen message (the usual case: a link is posted, staff flag it later) was never picked up; one was missed this way.

## Decision
`collect` scans every message from the last 7 days and skips IDs in `osint_handled`. Runs mark exactly the messages they published or held with `collect --handled <ids>`, rather than advancing past everything fetched (which could mark a 📌 added mid-run as handled unseen).

## Alternatives considered
- Keep the cursor but re-scan a short overlap: still misses pins added after the overlap.
- Discord gateway events: needs a running bot; the bot isn't running between runs.

## Consequences
A 📌 on a message older than 7 days isn't seen (configurable via `submit_lookback_days`). Each run makes one reactions call per pinned message in the window.
