---
title: "Ivanti Connect Secure: Three Flaws Chained for Unauthenticated Root Access"
date: 2026-10-31T16:03:46.666029+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["ivanti-connect-secure", "cisa-kev", "exploit-chain"]
cves: ["CVE-2026-111357"]
source: "https://thehackernews.com/2026/10/attackers-chain-three-ivanti-connect.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Ivanti Connect Secure is a common enterprise VPN appliance; CISA KEV listing plus active exploitation plus a public GitHub PoC makes this urgent — patch ICS immediately and audit appliance logs and filesystem integrity for signs of pre-patch compromise.
- **SOC/IR — Act:** Active exploitation of an edge VPN device means assume-breach posture is warranted — hunt for anomalous outbound connections and lateral movement from ICS appliance IPs since the KEV listing date, and check for Ivanti-specific persistence IOCs from prior campaigns (SPAWN/BUSHWALK malware families).
- **Leader — Act:** Ivanti Connect Secure has systemic enterprise reach; confirm with your network/infra team whether ICS is in use, obtain a patch-status attestation this week, and brief leadership — this class of Ivanti exploitation has previously generated board-level headlines.
- **Signals:** CVE-2026-111357 — CISA KEV: listed, EPSS 0.01, public PoC on GitHub
