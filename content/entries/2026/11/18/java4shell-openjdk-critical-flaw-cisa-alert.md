---
title: "CISA urges immediate patching of critical 'Java4Shell' flaw in Java's Base64 decoder"
date: 2026-11-18T07:02:00Z
lastmod: 2026-11-18T07:02:00Z
label: confirmed
label_history:
  - { at: 2026-11-18T07:02:00Z, label: confirmed }
sectors: [it]
countries: [us, ca]
sources:
  - { name: "CISA alert", url: "https://www.cisa.gov/news-events/alerts/2026/11/17/critical-java-vulnerability-requires-immediate-patching", tier: "1" }
  - { name: "Cisco Talos", url: "https://blog.talosintelligence.com/java4shell/", tier: "2" }
  - { name: "CyberScoop", url: "https://cyberscoop.com/java4shell-critical-java-flaw-openjdk/", tier: "3" }
guidance: { name: "CISA: Critical Java Vulnerability Requires Immediate Patching", url: "https://www.cisa.gov/news-events/alerts/2026/11/17/critical-java-vulnerability-requires-immediate-patching" }
submitted_by: rescon
significant: false
correction: null
discord_thread_id: null
---
On November 17 CISA, with input from Canada's Cyber Centre, told organizations to patch CVE-2026-114938 ("Java4Shell") immediately: a memory-corruption bug in the HotSpot JVM's Base64 decoder that can allow unauthenticated remote code execution on x86-64 systems with AVX-512 enabled. Oracle and OpenJDK released fixes the same day, and Talos describes disabling AVX-512 at JVM start-up as an interim mitigation. As of publication, neither CISA nor Talos reported exploitation in the wild, but Java's presence in appliances and bundled runtimes across every sector makes finding affected systems the main challenge.
