# 0005. Maintainer inbox for run feedback

- **Date:** 2026-11-18
- **Status:** Accepted

## Context
Runs end with a report (skipped items, blocked sources, label doubts), but that report lives only in the run's session, which nobody reads and which is archived after a day. Useful flags (e.g. a wrong label from an earlier run) were being found only by reading transcripts.

## Decision
`docs/INBOX.md` in the repo: runs add dated items only when something needs the maintainer's decision or action; the `Inbox` command reviews and resolves them; resolved items are marked, never deleted. Work sessions mention the open count at start.

## Alternatives considered
- Discord DM from the bot: private and notifies, but needs the maintainer's user ID in config and leaves no tracked record.
- Reading run transcripts: doesn't scale.

## Consequences
The file is public, so it must never contain held items or anything staff-related. Push notifications for new items are possible but untested.
