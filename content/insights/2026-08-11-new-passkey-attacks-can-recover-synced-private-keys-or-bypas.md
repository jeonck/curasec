---
title: "Researchers Demonstrate Three Passkey Attack Classes That Bypass Phishing-Resistance"
date: 2026-08-11T11:54:43.298939+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["passkeys", "mfa-bypass", "authentication"]
cves: []
source: "https://thehackernews.com/2026/08/new-passkey-attacks-can-recover-synced.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** If you're deploying or have deployed cloud-synced passkeys, evaluate migrating to hardware-bound (device-local) passkeys where possible; the research shows synced passkey material can be exfiltrated by malware and Windows-issued signed auth tokens can be replayed — audit your passkey configuration to prefer non-synced, phishing-resistant authenticators.
- **SOC/IR — Learn:** These attacks require malware already present on the endpoint, making detection of credential-theft behaviors (auth token exfiltration, suspicious cloud-sync API calls) the relevant angle — no published IOCs or ATT&CK mappings yet, but worth revisiting passkey-related telemetry if new technique details emerge.
- **Leader — Learn:** Passkey rollouts sold internally as phishing-proof may need a qualification: device-bound variants maintain that property but cloud-synced ones carry residual risk if endpoints are compromised — useful context for board decks or vendor questionnaire responses that reference passkey adoption.
