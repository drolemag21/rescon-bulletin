---
title: "CISA adds actively exploited Perforce Puppet remote code execution flaw to KEV catalog"
date: 2026-11-18T14:33:00Z
lastmod: 2026-11-18T14:33:00Z
label: confirmed
label_history:
  - { at: 2026-11-18T14:33:00Z, label: confirmed }
sectors: [it]
countries: [us]
sources:
  - { name: "CISA KEV catalog", url: "https://www.cisa.gov/known-exploited-vulnerabilities-catalog", tier: "1" }
  - { name: "SecurityWeek", url: "https://www.securityweek.com/critical-perforce-puppet-rce-exploited-in-attacks/", tier: "3" }
guidance: { name: "CISA KEV: CVE-2026-115731", url: "https://www.cisa.gov/known-exploited-vulnerabilities-catalog" }
submitted_by: rescon
significant: false
correction: null
discord_thread_id: null
---
CISA added CVE-2026-115731, a critical deserialization flaw in Puppet Enterprise and Puppet Core (also affecting OpenVox), to its Known Exploited Vulnerabilities catalog on November 17, giving federal agencies two weeks to patch. A client holding a Puppet-signed agent certificate can send a crafted report that runs code on the Puppet server, which Perforce warns could expose the server's certificate-signing key; servers that auto-sign certificate requests are especially exposed. Patches have been available since November 3, and no attacker has been publicly identified.
