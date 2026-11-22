---
title: "Rackspace Spot breach gave attackers access to customer Kubernetes secrets"
date: 2026-11-22T14:41:00Z
lastmod: 2026-11-22T14:41:00Z
label: reported
label_history:
  - { at: 2026-11-22T14:41:00Z, label: reported }
sectors: [it]
countries: [us]
sources:
  - { name: "BleepingComputer", url: "https://www.bleepingcomputer.com/news/security/rackspace-spot-breach-let-hackers-access-customer-kubernetes-secrets/", tier: "3" }
submitted_by: rescon
significant: false
correction: null
discord_thread_id: null
---
What
: Rackspace told customers that an intruder used leaked credentials to access its Spot Kubernetes platform on November 17. The attacker could create pods and read secrets in some customer clusters.

Who
: Unknown. Rackspace has not attributed the intrusion.

Status
: Rackspace revoked tokens and rotated keys. It told customers to rotate any credentials stored in cluster secrets and check logs back to November 17.
