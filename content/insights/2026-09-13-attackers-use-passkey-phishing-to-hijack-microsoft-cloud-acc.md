---
title: "Passkey Phishing Campaigns Target Microsoft Cloud Accounts at Scale"
date: 2026-09-13T14:54:43.124505+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["phishing", "cloud-identity", "microsoft"]
cves: []
source: "https://thehackernews.com/2026/09/attackers-use-passkey-phishing-to.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Demonstrates that passkey-themed social engineering can bypass MFA assumptions — worth factoring into how passkey enrollment flows and conditional access policies are hardened, but no CVE or patch action follows from this disclosure.
- **SOC/IR — Plan:** The active campaign pattern — CEO-impersonation lures leading to passkey/cloud credential harvesting — is worth building detections around: hunt for anomalous passkey registration events in Entra ID and tune email-gateway rules for third-party-relayed CEO impersonation at volume.
- **Leader — Learn:** Useful context that passkey adoption does not eliminate cloud account takeover risk; informs future board or customer messaging about layered identity controls, but no vendor breach or regulatory trigger here.
