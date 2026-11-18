# 0012. Labeled summaries with a word limit; compact Weekly list

- **Date:** 2026-11-18
- **Status:** Accepted

## Context
Entries read as dense paragraphs. The 3-sentence limit capped sentences, not words, so runs packed detail into long sentences: one KEV summary opened with a 78-word sentence of semicolon clauses. The home page also rendered every recent entry twice in full, once under Daily and again under Weekly.

## Decision
- The summary is a Markdown definition list with three fixed terms: **What**, **Who** (attribution, or "Unknown") and **Status**. At most 75 words in total, no sentence over 30 words.
- The site renders the list as a labeled grid. Entries written as a single paragraph render as before; the body's shape decides the layout, so there is no cutoff date or flag. Old entries are not rewritten.
- The Weekly panel shows one row per entry (label dot, headline, countries, last activity) linking to the full card. Daily keeps full cards.
- `rescon_discord.py incident` turns the list into `**What:** …` lines for Discord.

## Alternatives considered
- **Bottom line first, rest folded behind "More".** Fastest to skim, but hides denials and attribution caveats by default.
- **Structured front-matter fields (actor, status, deadline, CVE table).** Better for filtering, but a schema change with more for runs to get wrong; not needed for readability. Can be revisited.
- **Rewriting existing entries in the new format.** Changes published text without a correction; the old entries leave the Daily and Weekly windows within a week anyway.

## Consequences
- Attribution always has the same place in every entry.
- Runs must write the exact definition-list syntax; a malformed list renders as plain paragraphs, which is readable but loses the labels.
- RSS descriptions use the plain text, so labels and text run together on separate lines without colons.
