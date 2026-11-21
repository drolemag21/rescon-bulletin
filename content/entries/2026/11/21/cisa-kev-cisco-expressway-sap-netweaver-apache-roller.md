---
title: "CISA adds exploited Cisco Expressway, SAP NetWeaver and Apache Roller flaws to KEV catalog"
date: 2026-11-21T17:19:00Z
lastmod: 2026-11-21T17:19:00Z
label: confirmed
label_history:
  - { at: 2026-11-21T17:19:00Z, label: confirmed }
sectors: [it]
countries: [us]
sources:
  - { name: "CISA KEV alert (20 Nov)", url: "https://www.cisa.gov/news-events/alerts/2026/11/20/cisa-adds-four-known-exploited-vulnerabilities-catalog", tier: "1" }
  - { name: "SecurityWeek (Expressway)", url: "https://www.securityweek.com/hackers-exploit-cisco-expressway-vulnerability-soon-after-poc-release/", tier: "3" }
  - { name: "SecurityWeek (Roller)", url: "https://www.securityweek.com/critical-apache-roller-axis-vulnerabilities-exploited-in-attacks/", tier: "3" }
guidance: { name: "CISA KEV alert (20 Nov)", url: "https://www.cisa.gov/news-events/alerts/2026/11/20/cisa-adds-four-known-exploited-vulnerabilities-catalog" }
submitted_by: rescon
significant: false
correction: null
discord_thread_id: null
---
What
: On November 20 CISA listed four more exploited flaws, with a November 23 federal deadline. They include CVE-2026-76466, a critical root-level flaw in clustered Cisco Expressway gateways, plus SAP NetWeaver and Apache Roller bugs. The vCenter flaw has its own entry.

Who
: Unknown. Security firm F6 says the Expressway flaw was used against a Russian organization soon after a public exploit appeared.

Status
: Expressway X15.5.20 fixes it. SecurityWeek says Cisco's advisory does not yet mention exploitation.
