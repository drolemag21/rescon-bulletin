# Changelog

System changes only: instructions, specs, scripts, templates, workflows and policy. Content (entries, state, usage, inbox) isn't listed; see the run commits (`run:`, `content:`) for that. Reasons for larger changes are in `docs/decisions/`.

## Unreleased

- Sources: CNN added as a tier 3 source (`www.cnn.com` allowlisted). Politico approved but not added: the environment service refused its hosts.

## 2026-11-19

- Timed windows use one-shot firings created up front (with a stand-down firing after expiry); runs never touch scheduled tasks. Dispatcher reads only its own file and lists at most 10 sessions per firing (#7, decision 0014).
- Exploited-vulnerability incident posts need KEV or official exploitation, a dedicated official advisory, and an infrastructure/OT product; a KEV entry alone isn't enough (#5, decision 0013).

## 2026-11-18

- Readability: entry summaries are three labeled lines (What / Who / Status), at most 75 words with no sentence over 30; older paragraph summaries render unchanged. The home page's Weekly panel lists entries as one-line rows instead of repeating full cards. Discord incident posts show the labels as bold lead-ins (#4, decision 0012).
- Significance: an attack or disruption needs a `confirmed` entry; runs read the primary statement first and raise an inbox item if its host is blocked (#3, decision 0011).
- The dispatcher is identified by the `rescon:dispatcher` session tag instead of a session id in `CLAUDE.md`; `New dispatcher` no longer needs a pull request (#2, decision 0010).
- Role-based instructions (#1): short root `CLAUDE.md` with a role table; `docs/agents/` for dispatcher, run, source report, maintainer and shared reference (decision 0008).
- Change control: content straight to `main`, system files by pull request; `run:`/`content:` commit prefixes; build check on pull requests (decision 0009).
- Decision records (`docs/decisions/`, backfilled for 2026-11-18) and this changelog.
- `DESIGN.md` updated for the dispatcher, inbox, source access, usage backfill and change control.

- Dispatcher session starts a fresh session per scheduled job; replaces the persistent runner and `New runner` with `New dispatcher` (`5b5a5c0`, `b7b91d0`; decision 0003, superseding 0002 from `1c723a7`).
- Maintainer inbox (`docs/INBOX.md`) and `Inbox` command (`7c76b08`; decision 0005).
- Staff 📌 submissions: scan a 7-day window and mark handled explicitly; fixes missed pins (`8721486`; decision 0006).
- Source access fallback order; `feed`/`access`/`checked` notes per source (`94eae97`, `5bfc9e6`; decision 0007).
- Usage logging: rows recorded pending and backfilled by the next run, from session snapshots or result events (`21ead78`, `94eae97`; decision 0004).
- Weekly source report scheduled task and procedure (`21ead78`).
- Fix internal links dropping the `/rescon-bulletin/` base path (`eaf98fc`).
- Stop tracking the Python bytecode cache (`aa409d8`).
- Per-run usage log with model and effort tracking (`b4ef0df`).
- `CLAUDE.md` run playbook (`ee5de58`).
- Discord helper script, command reference and `staff-post --pin` (`581ab5a`, `899b7f9`).
- Hugo site, licenses, source list and GitHub Pages deploy (`506592c`).
- Spec: choose Hugo, add freshness labels and the no-commands rule (`c5d1420`).

## 2026-11-17

- Draft design spec (`abbdb6a`).
