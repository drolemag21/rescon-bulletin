---
title: "F5 patches five NGINX flaws allowing unauthenticated code execution; CERT-EU urges fast updates"
date: 2026-11-18T19:03:19Z
lastmod: 2026-11-18T19:03:19Z
label: confirmed
label_history:
  - { at: 2026-11-18T19:03:19Z, label: confirmed }
sectors: [it]
countries: [eu, ca, us]
sources:
  - { name: "CERT-EU Security Advisory 2026-022", url: "https://cert.europa.eu/publications/security-advisories/2026-022/", tier: "1" }
  - { name: "Canadian Centre for Cyber Security AV26-1174", url: "https://www.cyber.gc.ca/en/alerts-advisories/f5-security-advisory-av26-1174", tier: "1" }
  - { name: "CyberScoop", url: "https://cyberscoop.com/nginx-critical-vulnerabilities-exploits/", tier: "3" }
guidance: { name: "CERT-EU Security Advisory 2026-022", url: "https://cert.europa.eu/publications/security-advisories/2026-022/" }
submitted_by: rescon
significant: false
correction: null
discord_thread_id: null
---
F5 has released fixes for five memory-safety bugs in NGINX Open Source and NGINX Plus that can let an unauthenticated remote attacker run code with the privileges of the NGINX worker process; the most serious, CVE-2026-123007, needs only HTTP/2 enabled on a listening port, while the others depend on specific HTTP/2, HTTP/3, resolver or mail-proxy setups. CERT-EU says researchers have demonstrated exploitation but no attacks in the wild have been reported, and recommends patching internet-facing servers first or disabling HTTP/2 as a stopgap. CyberScoop reports that the researchers published working exploits, that the HTTP/2 attack needs very high traffic volumes to succeed, and that F5 says BIG-IP and F5OS are not affected.
