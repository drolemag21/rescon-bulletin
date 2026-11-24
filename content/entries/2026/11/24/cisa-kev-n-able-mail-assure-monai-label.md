---
title: "CISA adds exploited N-able Mail Assure and MONAI Label flaws to KEV catalog"
date: 2026-11-24T02:42:00Z
lastmod: 2026-11-24T02:42:00Z
label: confirmed
label_history:
  - { at: 2026-11-24T02:42:00Z, label: confirmed }
sectors: [it]
countries: [us]
sources:
  - { name: "CISA KEV alert (23 Nov)", url: "https://www.cisa.gov/news-events/alerts/2026/11/23/cisa-adds-two-known-exploited-vulnerabilities-catalog", tier: "1" }
  - { name: "SecurityWeek (N-able)", url: "https://www.securityweek.com/n-able-patches-critical-flaw-disclosed-after-mail-assure-cyberattack/", tier: "3" }
guidance: { name: "CISA KEV alert (23 Nov)", url: "https://www.cisa.gov/news-events/alerts/2026/11/23/cisa-adds-two-known-exploited-vulnerabilities-catalog" }
submitted_by: rescon
significant: false
correction: null
discord_thread_id: null
---
What
: On November 23 CISA listed two exploited flaws: CVE-2026-134624 in N-able's Mail Assure email security service and a path traversal in MONAI Label. N-able found its flaw while investigating a breach of its hosted service.

Who
: Not attributed for N-able. Amazon tied MONAI Label exploitation to a China-nexus actor.

Status
: N-able says exploitation was confined to one hosted server and has patched it. A root cause report is due within two weeks.
