---
title: "Cisco ISE CVSS 10.0 Auth Bypass Zero-Day Actively Exploited"
date: 2026-09-17T15:32:45.721902+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["cisco", "zero-day", "authentication-bypass"]
cves: ["CVE-2026-76460"]
source: "https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Cisco ISE is widely deployed as network access control in enterprise environments; unauthenticated API auth bypass at CVSS 10.0 with CISA KEV listing and public PoC demands immediate action — apply Cisco's posted mitigation or patch for CVE-2026-76460 and restrict ISE API endpoint exposure at the network layer until patched.
- **SOC/IR — Act:** Active exploitation of an ISE auth bypass means attackers may already have bypassed NAC controls; hunt for anomalous unauthenticated API calls against ISE endpoints in your perimeter logs and assume-breach sweep network access audit trails since at least the PoC publication date.
- **Leader — Act:** A CVSS 10.0 actively exploited zero-day in Cisco ISE — a core identity and network access control product in most enterprise stacks — warrants same-week action: confirm whether ISE is in use, verify your team is executing Cisco's mitigations, and prepare a brief for leadership given the likelihood of press coverage and customer security questions.
- **Signals:** CVE-2026-76460 — CISA KEV: listed, EPSS n/a, public PoC on GitHub
