# Decision records

One short file per significant decision about how RESCON works: what was decided, what else was considered, and why. Commit history shows *what* changed; these explain *why it's built this way*.

- File name: `NNNN-short-title.md`, numbered in order. Never renumber or delete; if a decision is replaced, set the old one's status to `Superseded by NNNN` and write a new one.
- Added or updated in the same pull request as the change it explains.
- Keep each to about a page.

```markdown
# NNNN. Title

- **Date:** YYYY-MM-DD
- **Status:** Accepted | Superseded by NNNN

## Context
What problem or question prompted this.

## Decision
What we're doing.

## Alternatives considered
What else was on the table and why it lost.

## Consequences
What this makes easier or harder; follow-ups.
```

## Index

| # | Decision | Status |
|---|---|---|
| 0001 | Allowlist source hosts; read pages with curl when WebFetch fails | Accepted |
| 0002 | Scheduled runs in one persistent runner session | Superseded by 0003 |
| 0003 | Dispatcher session starts a fresh session per job | Accepted |
| 0004 | Usage: record pending, backfill from the next run | Accepted |
| 0005 | Maintainer inbox for run feedback | Accepted |
| 0006 | Staff 📌: scan a 7-day window, mark handled explicitly | Accepted |
| 0007 | Source access fallbacks and per-source access notes | Accepted |
| 0008 | Role-based instruction files | Accepted |
| 0009 | Change control: content direct to main, system changes by PR | Accepted |
