---
title: "FBI warns ARTEX AI framework is being used to automate intrusions across critical sectors"
date: 2026-11-18T05:28:00Z
lastmod: 2026-11-18T05:28:00Z
label: confirmed
label_history:
  - { at: 2026-11-18T05:28:00Z, label: confirmed }
sectors: [it, finance, energy, healthcare, telecom, defense]
countries: [us, kr]
sources:
  - { name: "FBI FLASH-20261113-001 (PDF)", url: "https://www.ic3.gov/CSA/2026/261113.pdf", tier: "1" }
  - { name: "Unit 42", url: "https://unit42.paloaltonetworks.com/artex-and-ai-powered-red-teaming-tools/", tier: "2" }
  - { name: "SecurityWeek", url: "https://www.securityweek.com/barracuda-hacked-amid-surge-in-artex-powered-cyberattacks/", tier: "3" }
guidance: { name: "FBI FLASH-20261113-001 mitigations", url: "https://www.ic3.gov/CSA/2026/261113.pdf" }
submitted_by: rescon
significant: false
correction: null
discord_thread_id: null
---
On November 13 the FBI issued a FLASH alert on ARTEX, an open-source, LLM-driven penetration testing framework that it says a range of malicious actors have used since August 2026 against organizations in finance, government, energy, healthcare, telecom, defense and other sectors, in some cases reaching privileged access within three hours. The alert cites data theft affecting about 67,000 people at South Korean financial institutions and a supply-chain compromise of ConnectWise Cloud Backup customers, and notes that forks and a commercial version keep the tool available after its author pulled the public repository. Unit 42 reports seeing ARTEX in intrusions it investigated, and SecurityWeek reports it has become common among Chinese threat actors; the FBI alert itself does not attribute ARTEX use to a single state.
