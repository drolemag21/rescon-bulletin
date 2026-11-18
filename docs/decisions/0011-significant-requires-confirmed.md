# 0011. Incident posts only for confirmed attacks; read the primary statement first

- **Date:** 2026-11-18
- **Status:** Accepted

## Context
The Equinor attack got its own forum post while labelled `reported`: Equinor's statement had only been read via The Record, because equinor.com wasn't allowlisted. The criterion says "a confirmed attack or disruption", so the post and the label disagreed.

## Decision
An attack or disruption is significant only when the entry is `confirmed`. When a possibly significant incident is only in the press, the run reads the victim's or agency's own statement; if it can't reach it, it publishes the entry as `reported` without a post and adds an inbox item asking for the host. A later run sets `significant: true` once confirmed.

## Alternatives considered
- Allow posts on `reported` coverage of a victim statement: faster, but forum posts would carry weaker labels than members expect.
- A "developing incident" post type for big unconfirmed incidents: open idea, tracked in the inbox.

## Consequences
A major incident may wait one run (or a host approval) before getting its own post; it still appears in the bulletin and Daily/Weekly replies immediately. Incident posts aren't edited after creation, so a label change after posting isn't reflected in the post's tags (Equinor: posted as Reported, now Confirmed).
