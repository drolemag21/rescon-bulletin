---
title: "CISA adds four actively exploited flaws to KEV, including REDCap research platform and LiteLLM"
date: 2026-11-18T20:13:32Z
lastmod: 2026-11-18T20:13:32Z
label: confirmed
label_history:
  - { at: 2026-11-18T20:13:32Z, label: confirmed }
sectors: [it, healthcare]
countries: [us]
sources:
  - { name: "CISA KEV catalog", url: "https://www.cisa.gov/known-exploited-vulnerabilities-catalog", tier: "1" }
guidance: { name: "CISA KEV catalog", url: "https://www.cisa.gov/known-exploited-vulnerabilities-catalog" }
submitted_by: rescon
significant: false
correction: null
discord_thread_id: null
---
On November 18 CISA added four vulnerabilities to its Known Exploited Vulnerabilities catalog: a code-injection flaw in Vanderbilt's REDCap research data platform (CVE-2026-90817), widely used by hospitals and universities, that lets an unauthenticated attacker who knows a public survey link run code on the server; a code-execution flaw in the LiteLLM AI gateway (CVE-2026-40217); a 2024 Synology DiskStation Manager flaw (CVE-2024-10441); and an unsafe-reflection bug in the end-of-life Apache Axis SOAP library (CVE-2026-90436). Federal agencies must fix three of them by November 21, and LiteLLM by December 2, with forensic triage required for the REDCap, Synology and Axis cases. CISA has not said who is exploiting the flaws or against whom, and no ransomware use is recorded.
