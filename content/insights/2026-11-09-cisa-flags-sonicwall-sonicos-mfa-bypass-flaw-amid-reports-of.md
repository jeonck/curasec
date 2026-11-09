---
title: "CISA KEV: SonicWall SonicOS MFA Bypass CVE-2026-19868 Actively Exploited"
date: 2026-11-09T21:25:24.006803+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["sonicwall", "cisa-kev", "mfa-bypass"]
cves: ["CVE-2026-19868"]
source: "https://thehackernews.com/2026/11/cisa-flags-sonicwall-sonicos-mfa-bypass.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** KEV-listed with a public GitHub PoC and exploitation reports makes this urgent for any org running SonicWall edge appliances; patch SonicOS to the vendor-specified fixed version immediately and audit recent authentication logs for unexpected successful logins.
- **SOC/IR — Act:** MFA bypass on a perimeter device means attackers may have authenticated silently before patching; sweep VPN/firewall auth logs for anomalous successful authentications since the disclosure date and tune detections for lateral movement originating from SonicWall management IPs.
- **Leader — Plan:** Confirm whether SonicWall SonicOS is in the environment and verify the engineering team has this on an emergency patch track; if SonicWall is used, assess whether the MFA bypass window requires any breach-notification review under SEC or applicable disclosure rules.
- **Signals:** CVE-2026-19868 — CISA KEV: listed, EPSS 0.01, public PoC on GitHub
