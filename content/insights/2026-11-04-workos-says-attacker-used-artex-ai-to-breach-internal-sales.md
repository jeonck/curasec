---
title: "WorkOS breached via ARTEX AI tool; sales app contact data exposed"
date: 2026-11-04T18:40:06.241551+00:00
verdict: "Act"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Act"
tags: ["vendor-breach", "ai-attack-vector", "identity-platform"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/workos-says-attacker-used-artex-ai-to-breach-internal-sales-app/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** No patch or configuration action — the breach was in WorkOS's internal sales tooling, not their auth platform. The AI-assisted intrusion technique is worth noting for teams evaluating third-party AI tooling access to internal systems.
- **SOC/IR — Learn:** No IOCs or ATT&CK-mappable TTPs are published yet; insufficient detail to write detections or run a meaningful hunt. Monitor for follow-up disclosure with technical indicators.
- **Leader — Act:** WorkOS is widely used for enterprise SSO/auth; confirm whether your organization is a customer and request a scope statement from WorkOS clarifying what customer data was accessed and whether your records were included.
