# 0008. Role-based instruction files

- **Date:** 2026-11-18
- **Status:** Accepted

## Context
One CLAUDE.md (~3,400 words) served four roles: dispatcher, run, source report and maintainer work session. Each session loaded all of it; the dispatcher's scheduled prompt said "follow the run procedure" and relied on a note to override it; a long-lived session only sees CLAUDE.md edits if it re-reads the file.

## Decision
A short root `CLAUDE.md` (what RESCON is, who can direct you, the Never list, change control, and a role table) pointing to `docs/agents/{dispatcher,run,report,maintainer}.md`, plus `docs/agents/reference.md` for rules shared by runs and work sessions. Safety rules stay in the root so they apply even if a role file isn't read. Each rule lives in exactly one file.

## Alternatives considered
- Keep one file: works, but roles see instructions not meant for them.
- Sub-folder CLAUDE.md files: only load when the session touches that folder, which doesn't map to roles.
- `@` imports: always load, so no saving.

## Consequences
The context saving is small (the fixed session overhead is ~87k tokens; CLAUDE.md was ~5k). The main gains are clarity, fewer conflicting instructions, and roles that can't stray (e.g. runs can't edit system files). Role detection depends on the prompt and session id.
