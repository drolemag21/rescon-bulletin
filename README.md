# 📡 RESCON Bulletin

Open-source aggregation of **public reporting** on nation-state cyber activity and threats to critical infrastructure in the **US and allied countries**. Each item is summarized in three sentences or fewer, linked to its sources, and labeled by how well it's corroborated.

**Site:** https://drolemag21.github.io/rescon-bulletin/

> RESCON Bulletin is aggregated public reporting. It is **not intelligence** and not an official source. **RESCON** (Research Condition) shows how intensively we're researching, **not a threat level**.

## How it works

- **Entries** are Markdown files in `content/entries/YYYY/MM/DD/`, one per item, each carrying a verification label: Confirmed, Reported, Unverified or Claimed.
- **Corrections** are marked on the entry, never silently deleted. Git history is the audit trail.
- **Sources** and their tiers live in [`data/sources.yml`](data/sources.yml). Decisions are logged in [`docs/sources-log.md`](docs/sources-log.md).
- **State** (current RESCON level, last update, Daily/Weekly syntheses) lives in `data/state/`.
- The site is built with [Hugo](https://gohugo.io/) (pinned and checksum-verified, no package dependencies) and deployed to GitHub Pages by `.github/workflows/pages.yml`.

The full design is in [`docs/DESIGN.md`](docs/DESIGN.md), and the [Methodology page](https://drolemag21.github.io/rescon-bulletin/methodology/) explains the labels and source policy.

## Local preview

Install Hugo 0.169.0 or later, then:

```bash
hugo server
```

## License

- Code: [MIT](LICENSE)
- Summaries and site content: [CC BY 4.0](LICENSE-content)
- Linked articles belong to their publishers. We link and summarize, never copy.
