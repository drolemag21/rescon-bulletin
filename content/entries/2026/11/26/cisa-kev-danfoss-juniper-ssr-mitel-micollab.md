---
title: "CISA adds exploited Danfoss refrigeration controller, Juniper SSR and Mitel MiCollab flaws to KEV"
date: 2026-11-26T02:42:00Z
lastmod: 2026-11-26T14:42:00Z
label: confirmed
label_history:
  - { at: 2026-11-26T02:42:00Z, label: confirmed }
sectors: [food, telecom, it]
countries: [us]
sources:
  - { name: "CISA KEV alert (25 Nov)", url: "https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog", tier: "1" }
  - { name: "CISA KEV catalog (JSON)", url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json", tier: "1" }
  - { name: "CISA ICSA-26-328-03 (Danfoss AK-SM 8xxA)", url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-03", tier: "1" }
  - { name: "BleepingComputer", url: "https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-unpatched-flaw-in-danfoss-refrigeration-controllers/", tier: "3" }
  - { name: "SecurityWeek (Mitel MiCollab)", url: "https://www.securityweek.com/mitel-micollab-zero-days-exploited-in-suspected-ai-assisted-attacks/", tier: "3" }
  - { name: "SecurityWeek (Juniper SSR)", url: "https://www.securityweek.com/critical-juniper-session-smart-conductor-flaw-exploited-in-attacks/", tier: "3" }
guidance: { name: "CISA ICSA-26-328-03", url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-03" }
submitted_by: rescon
significant: false
correction: null
discord_thread_id: null
---
What
: On November 25 CISA listed ten flaws as exploited. Three affect Danfoss AK-SM 800A supermarket refrigeration controllers. The others hit Juniper Session Smart Router, Xen Orchestra and five in Mitel MiCollab.

Who
: Not attributed by CISA. BleepingComputer links recent Danfoss controller attacks on European food retailers to an IRGC-linked unit.

Status
: Per SecurityWeek, Accenture says the Mitel flaws were exploited as zero-days, likely for extortion. Juniper reports exploitation of CVE-2026-103406. A separate Danfoss flaw, CVE-2026-129713, remains unpatched.
