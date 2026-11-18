# 0001. Allowlist source hosts; read pages with curl when WebFetch fails

- **Date:** 2026-11-18
- **Status:** Accepted

## Context
The first run couldn't open any source page: the cloud environment's network policy only allowed package registries. Search results alone weren't enough to verify items, and CLAUDE.md forbids citing what wasn't read. After hosts were added, `curl` picked up the change immediately but WebFetch in that session kept failing.

## Decision
Add each source's host to the "Anthropic Cloud" environment allowlist (27 hosts as of this date), maintained by the maintainer. Runs may read pages with plain `curl` and extract text, as well as WebFetch.

## Alternatives considered
- Unrestricted network access: broader than needed.
- Search-only research: can't verify content or dates; risks citing summaries rather than sources.

## Consequences
New sources need a host added by the maintainer (only they can approve it). The environment service refused Reuters and/or AP for unknown reasons. Some allowed hosts (ACSC, CERT-FR) still time out. See 0007 for the fallback order.
