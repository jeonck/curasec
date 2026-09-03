---
title: "Teams IT-support impersonation campaign deploys Node.js implant"
date: 2026-09-03T14:58:44.181043+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["social-engineering", "teams-abuse", "lateral-movement"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Plan:** Audit and tighten Microsoft Teams external access policies to block or restrict unsolicited external chat from unknown tenants; review which remote-access tools are permitted and ensure Node.js execution from user-writable paths is monitored or blocked.
- **SOC/IR — Act:** Active human-operated campaign with clear TTPs: external Teams chat impersonating IT support → remote session → Node.js implant → lateral movement via living-off-the-land tools. Hunt for Node.js spawning unusual child processes, remote-access tool sessions initiated from external Teams contacts, and abnormal lateral movement patterns since early September 2026; tune EDR rules on Teams-initiated process chains.
- **Leader — Plan:** This campaign exploits enterprise collaboration tools (Teams) rather than unpatched software, meaning technical controls alone are insufficient — review whether external Teams federation policies are hardened and ensure current security-awareness training explicitly covers IT-support impersonation via chat platforms.
