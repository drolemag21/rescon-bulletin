# 0009. Change control: content direct to main, system changes by PR

- **Date:** 2026-11-18
- **Status:** Accepted

## Context
Everything was committed straight to `main`. A change to CLAUDE.md or a script on `main` changes how the next scheduled run behaves, so it is effectively a production deploy; several bugs went out that way on 2026-11-18. Run commits (many per day) also buried the history of system changes.

## Decision
- **Content** (entries, state, usage log, inbox, source access notes, new taxonomy keys) goes straight to `main` with `run:` or `content:` prefixes, so publishing never waits for review.
- **System** files (instructions, specs, scripts, templates, workflows, config, source policy) change only by branch and pull request, merged by the maintainer. A build check runs on pull requests.
- Decisions get a record in `docs/decisions/`; merged changes get a line in `CHANGELOG.md`.

## Alternatives considered
- Everything by PR: every run would wait for a human merge.
- Everything direct (status quo): no review point and no readable history.

## Consequences
GitHub can't enforce the split, because runs and work sessions push with the same identity; a "require PR" rule would block runs too. It's enforced by the instructions (runs are told never to touch system files), which is a convention, not a hard control. Changes to instructions now take effect only after the maintainer merges.
