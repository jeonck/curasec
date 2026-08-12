---
title: "Sandworm UAC-0145 Uses Fake Recruiters to Deliver Backdoored VPN"
date: 2026-08-12T11:57:00.937865+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["sandworm", "social-engineering", "trojanized-software"]
cves: []
source: "https://thehackernews.com/2026/08/sandworm-linked-uac-0145-uses-fake-job.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Sandworm is delivering trojanized VPN clients through fake job-interview lures targeting IT professionals — a supply-chain-adjacent social engineering vector. No patch action exists, but teams should review policies on installing software provided during recruiting workflows and verify VPN client integrity via official sources only.
- **SOC/IR — Plan:** The campaign introduces a new Sandworm TTP: trojanized VPN with command-execution capability delivered via recruiter impersonation. No IOCs are currently available in this disclosure, but detection engineers should queue rules for unauthorized VPN client installs and anomalous outbound connections from VPN processes in anticipation of CERT-UA releasing indicators.
- **Leader — Learn:** Sandworm expanding its IT-targeting playbook to recruiter impersonation is notable trend intelligence, but absent evidence of Western-enterprise targeting or published IOCs, this does not require immediate leadership action; file for the next threat-landscape briefing.
