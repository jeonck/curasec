---
title: "Open VSX Removes 77 Malicious Evil Twin Extensions Exfiltrating Dev Data"
date: 2026-08-05T13:01:27.566949+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["supply-chain", "malicious-extensions", "developer-tools"]
cves: []
source: "https://thehackernews.com/2026/08/open-vsx-removes-77-malicious-evil-twin.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** If your team uses Open VSX-sourced extensions (common in Theia, Gitpod, or VS Code OSS environments), audit installed extensions against the 77 removed packages and remove any installed between July 26–August 1, 2026; check build/dev environments for unexpected outbound connections during that window.
- **SOC/IR — Act:** Hunt for anomalous outbound traffic from developer workstations and CI runners between July 26 and August 1, 2026 that may indicate data exfiltration from compromised extensions; correlate against Open VSX extension install events in endpoint logs.
- **Leader — Plan:** This incident illustrates supply-chain risk in developer tooling marketplaces; work with engineering leads this quarter to establish an approved-extension policy and inventory for IDE plugins used across the org.
