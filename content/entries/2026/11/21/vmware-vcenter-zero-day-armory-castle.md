---
title: "China-linked group exploited a VMware vCenter zero-day for two months before a patch"
date: 2026-11-21T17:19:00Z
lastmod: 2026-11-21T17:19:00Z
label: confirmed
label_history:
  - { at: 2026-11-21T17:19:00Z, label: confirmed }
sectors: [it]
countries: [us, ca]
sources:
  - { name: "Google Threat Intelligence (Mandiant)", url: "https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-vsphere", tier: "2" }
  - { name: "CISA KEV alert (20 Nov)", url: "https://www.cisa.gov/news-events/alerts/2026/11/20/cisa-adds-four-known-exploited-vulnerabilities-catalog", tier: "1" }
  - { name: "Canadian Centre for Cyber Security AV26-1185", url: "https://www.cyber.gc.ca/en/alerts-advisories/vmware-security-advisory-av26-1185", tier: "1" }
  - { name: "SecurityWeek", url: "https://www.securityweek.com/newly-patched-vmware-vcenter-flaw-exploited-as-zero-day-by-chinese-apt/", tier: "3" }
guidance: { name: "Canadian Centre for Cyber Security AV26-1185", url: "https://www.cyber.gc.ca/en/alerts-advisories/vmware-security-advisory-av26-1185" }
submitted_by: rescon
significant: false
correction: null
discord_thread_id: null
---
What
: Broadcom patched CVE-2026-123890, a critical vCenter authentication bypass, on November 19. CISA listed it as exploited on November 20. Mandiant says attackers used it from early September to gain administrator access.

Who
: Mandiant attributes it to Armory Castle (formerly UNC5221), a suspected China-nexus espionage group. Initial access came through a BeyondTrust Remote Support zero-day.

Status
: Fixes cover vCenter 8.0 and 9.x. SecurityWeek says end-of-life version 7.0 has no public patch. Mandiant urges patching and checking for compromise.
