---
title: "CISA adds exploited Drupal core RCE and two other flaws to KEV catalog"
date: 2026-11-25T02:44:00Z
lastmod: 2026-11-28T02:41:00Z
label: confirmed
label_history:
  - { at: 2026-11-25T02:44:00Z, label: confirmed }
sectors: [it]
countries: [us]
sources:
  - { name: "CISA KEV alert (24 Nov)", url: "https://www.cisa.gov/news-events/alerts/2026/11/24/cisa-adds-three-known-exploited-vulnerabilities-catalog", tier: "1" }
  - { name: "CISA KEV alert (27 Nov)", url: "https://www.cisa.gov/news-events/alerts/2026/11/27/cisa-adds-three-known-exploited-vulnerabilities-catalog", tier: "1" }
  - { name: "SecurityWeek (Drupal follow-up flaw)", url: "https://www.securityweek.com/drupal-installer-patch-left-a-gap-attackers-are-already-exploiting/", tier: "3" }
guidance: { name: "CISA KEV alert (24 Nov)", url: "https://www.cisa.gov/news-events/alerts/2026/11/24/cisa-adds-three-known-exploited-vulnerabilities-catalog" }
submitted_by: rescon
significant: false
correction: null
discord_thread_id: null
---
What
: On November 24 CISA listed three flaws as exploited. The most notable is CVE-2026-132165, a remote code execution bug in Drupal core. The others affect Optimizely Web Experimentation and the Idunno AntiCsrf library.

Who
: Not attributed. CISA's alert does not say who is exploiting the flaws.

Status
: Drupal then disclosed CVE-2026-136716, a gap in the first fix. CISA listed it as exploited on November 27. Sites must upgrade and run an update hook.
