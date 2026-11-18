# 0010. Identify the dispatcher by tag, not session id

- **Date:** 2026-11-18
- **Status:** Accepted

## Context
The root `CLAUDE.md` recognised the dispatcher by its session id. Every `New dispatcher` therefore needed a pull request to change that id, and until it merged the new dispatcher wouldn't recognise itself and would treat a scheduled message as a run. The current dispatcher also needed replacing soon: it still carries its history as the old runner (~334k tokens), so each firing cost ~$3 in cache re-writes.

## Decision
The dispatcher is the session tagged `rescon:dispatcher`. A session whose message comes straight from a RESCON scheduled task checks its own tags with `get_session`. `New dispatcher` moves the tag from the old session to the new one; no file changes.

## Alternatives considered
- Keep the id in `CLAUDE.md`: a PR per rotation and a gap until it merges.
- Detect the role from the prompt alone: the scheduled-task prompts can only be edited from inside the dispatcher and still mention the run procedure, so the wording is ambiguous.

## Consequences
One extra `get_session` call per firing. Only one session may carry the tag; `New dispatcher` removes it from the old one. Run and report sessions are tagged `rescon:run` / `rescon:report`. Sections in the claude.ai session list don't carry over to sessions the dispatcher creates (tested), so run sessions appear outside the maintainer's "RESCON activities" section.
