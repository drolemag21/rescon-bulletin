---
title: "Google details Russian FSB-linked group using one US victim's identity to breach another"
date: 2026-11-18T14:33:00Z
lastmod: 2026-11-18T16:14:08Z
label: reported
label_history:
  - { at: 2026-11-18T14:33:00Z, label: reported }
sectors: [other]
countries: [us]
sources:
  - { name: "Google Threat Intelligence Group", url: "https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise", tier: "2" }
  - { name: "SecurityWeek", url: "https://www.securityweek.com/russian-apt-poses-as-employee-of-hacked-firm-to-breach-another-us-organization/", tier: "3" }
  - { name: "The Record", url: "https://therecord.media/russia-cyber-espionage-google", tier: "3" }
submitted_by: rescon
significant: false
correction: null
discord_thread_id: null
---
Google's threat intelligence group published a case study of COLD RELIC (also known as COLDRIVER and Star Blizzard), an espionage group the US links to Russia's FSB, which kept access to an unnamed US organization for months from late 2025 using stolen administrator credentials, MFA fatigue and rogue passkeys. After being removed, the group impersonated that organization's staff over encrypted messaging to phish a second US organization and steal its cloud files. Google says it saw new phishing activity from the group this month and recommends phishing-resistant MFA and auditing registered devices; the victims' sectors were not disclosed.
