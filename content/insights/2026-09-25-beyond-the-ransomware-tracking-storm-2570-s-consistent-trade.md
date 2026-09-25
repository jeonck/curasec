---
title: "Storm-2570 ransomware affiliate: consistent tradecraft across Qilin, DragonForce, Anubis, BERT"
date: 2026-09-25T15:49:12.385738+00:00
verdict: "Act"
verdict_engineer: "Learn"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["ransomware", "threat-intel", "ttp-analysis"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Learn:** No exploitable vulnerability or patchable component here — this is post-compromise TTP analysis. Worth reviewing to understand how Storm-2570 stages before detonation, which could inform detection-oriented hardening of endpoint configs or logging.
- **SOC/IR — Act:** Microsoft documents Storm-2570's reusable pre-ransomware toolchain across four active ransomware families with defender detection guidance — review the full blog post, map identified TTPs to ATT&CK, and tune or create SIEM/EDR rules against the common tradecraft patterns before the next deployment hits.
- **Leader — Learn:** A single-source threat-actor profile with no confirmed incident or sector-specific targeting disclosed; useful background for briefing on ransomware affiliate sophistication and the multi-group risk model, but no same-week action needed.
