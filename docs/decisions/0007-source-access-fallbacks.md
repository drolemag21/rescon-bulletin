# 0007. Source access fallbacks and per-source access notes

- **Date:** 2026-11-18
- **Status:** Accepted

## Context
Several sources block automated fetches, render only with JavaScript, or time out, and each run rediscovered this. One-off notes ("use RSS for NCSC UK") would be lost.

## Decision
A fixed fallback order for any source (page → feed → structured data → targeted search → tier 2–3 coverage → record the gap), plus `feed`, `access` and `checked` fields per source in `data/sources.yml`, which runs update as they learn. Reading an official statement only through coverage supports `reported`, not `confirmed`.

## Alternatives considered
- Notes in CLAUDE.md per source: mixes data with instructions; runs couldn't update them.

## Consequences
17 sources had verified feeds on this date. Updates to the notes are content (direct to `main`); changing the source list itself is policy (PR).
