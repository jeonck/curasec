---
title: "PAN-OS PHP RCE Flaws Actively Exploited, Both CISA KEV Listed"
date: 2026-11-20T19:04:41.748130+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["pan-os", "rce", "actively-exploited"]
cves: ["CVE-2026-109618", "CVE-2026-109619"]
source: "https://thehackernews.com/2026/11/everything-is-web-application-including.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** CVE-2026-109618 and CVE-2026-109619 are unauthenticated RCE flaws in PAN-OS management interfaces, both CISA KEV listed with EPSS 1.00 and public PoCs. Immediately patch PAN-OS to the latest fixed release and, if patching is not instant, block all internet access to the management interface.
- **SOC/IR — Act:** Active exploitation of internet-exposed PAN-OS management interfaces means assume-breach posture is warranted for any estate running them. Hunt for PHP2Shell execution artifacts, unexpected outbound connections, and lateral movement originating from firewall management IPs since October 28.
- **Leader — Act:** Unauthenticated RCE on perimeter firewalls with confirmed active exploitation is a board-level risk event. Confirm whether PAN-OS is in use, verify engineering has patched or isolated management interfaces, and prepare to brief leadership given the high likelihood of press coverage and customer inquiries.
- **Signals:** CVE-2026-109618 — CISA KEV: listed, EPSS 1.00, public PoC on GitHub · CVE-2026-109619 — CISA KEV: listed, EPSS 1.00, public PoC on GitHub
