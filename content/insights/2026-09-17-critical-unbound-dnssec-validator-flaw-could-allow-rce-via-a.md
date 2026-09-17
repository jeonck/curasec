---
title: "Critical Unbound DNS RCE via Malicious DNSSEC Zone (CVE-2026-81642)"
date: 2026-09-17T15:32:45.721902+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["dns", "rce", "dnssec"]
cves: ["CVE-2026-81642"]
source: "https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC exists for this critical heap overflow enabling RCE against any Unbound resolver that validates DNSSEC; patch to Unbound 1.26.1 immediately and verify all resolver deployments (containers, host-based, service mesh sidecars) are updated.
- **SOC/IR — Learn:** No active exploitation or IOCs reported, and EPSS is 0.01; the attack path (attacker-controlled zone triggers RCE in resolver) is worth noting for future hunt hypotheses, but no detection work is warranted until exploitation evidence emerges.
- **Leader — Skip**
- **Signals:** CVE-2026-81642 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub
