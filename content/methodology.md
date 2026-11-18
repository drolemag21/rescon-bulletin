---
title: Methodology
description: What RESCON Bulletin is, what it covers, how items are verified and labeled, and which sources it uses.
---

RESCON Bulletin is an open-source, public awareness and preparedness tool. It collects **public reporting** (OSINT) on nation-state cyber activity and threats to critical infrastructure in the **United States and allied countries**, then summarizes and labels each item so readers can tell at a glance how well it's corroborated.

It is **not intelligence**, not an official source, and implies nothing beyond what's publicly reported.

## Scope

- **Critical infrastructure:** attacks on and threats to the 16 CISA critical infrastructure sectors and their allied equivalents (energy, water, telecom, healthcare, finance, government, transportation and so on).
- **Nation-state cyber activity:** APT campaigns, espionage and pre-positioning in infrastructure networks, even when no disruption has happened yet. These are often the earliest public signals.
- **Geography:** the US and allies (Five Eyes, NATO, EU, Japan, South Korea and similar partners).
- **Geopolitics** appears only where it directly relates to an in-scope cyber item.

## RESCON levels {#rescon}

**RESCON (Research Condition)** shows how intensively RESCON is currently researching. **It is not a threat level.** A higher research level means more sources are being swept and cross-checked, not that something bad is happening. Only the project maintainer sets the level, and research runs only when the maintainer triggers them.

{{< levels >}}

A level can be set for a limited time (e.g. "RESCON 2 for 12 hours"). When that window ends, the level returns to whatever was set before.

## Verification labels

Every entry has exactly one label. It describes **how well the item is corroborated**, not how severe it is. Labels change as evidence develops, and each entry page shows its label history.

{{< labels >}}

**Corrections, not silent edits.** When an item is retracted, debunked or ruled out (e.g. an outage turns out to be an equipment failure), the entry is marked with a correction and stays in the archive.

**Staff Submitted** means the item was flagged by a RESCON staff member. It shows where the item came from, not that it's verified. Staff items go through the same checks and labeling as everything else.

## Entries

Each entry has a headline, a short summary in our own words (what happened, who is behind it, and its status), links to the original reporting (🔒 marks paywalled sources), sectors, countries, and when it was first seen and last updated. Where official mitigation guidance exists, the entry links to it. We don't write guidance of our own.

The **Daily** and **Weekly** sections cover the 24 hours and 7 days before the most recent update. Updates happen when research runs, not continuously, so each section shows the time it is "as of".

## Sources

Sources are grouped into tiers, and a tier limits which label a source can support on its own. Only an official source (tier 1), or a statement from the victim or operator, can make an item **Confirmed**.

- **Threat-actor channels** (hacktivist Telegram channels, ransomware leak sites, actor-run accounts) are **never linked or quoted directly**. Claims from those channels appear only when reported by credible tier 2–3 coverage, labeled **Claimed**. Linking them would point readers at stolen data and amplify claims made specifically to get attention.
- **Social media** posts from named researchers, journalists and on-the-ground accounts (tier 4a) may be linked directly. Eyewitness reports are labeled **Unverified** until corroborated.

{{< sources >}}

Source additions and removals are logged in [`docs/sources-log.md`](https://github.com/drolemag21/rescon-bulletin/blob/main/docs/sources-log.md).

## How it's made

Research runs are carried out by Claude (an AI model by Anthropic), directed by the project maintainer, using the source policy above. The full design is public in [`docs/DESIGN.md`](https://github.com/drolemag21/rescon-bulletin/blob/main/docs/DESIGN.md). Every change to every entry is visible in the repository's git history.

## Licensing

Code: [MIT](https://github.com/drolemag21/rescon-bulletin/blob/main/LICENSE). Summaries and site content: [CC BY 4.0](https://github.com/drolemag21/rescon-bulletin/blob/main/LICENSE-content). Linked articles belong to their publishers. We link and summarize, never copy.
