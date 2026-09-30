---
title: "Zimbra CVE-2026-73570: Unauthenticated Command Injection Under Active Exploit"
date: 2026-09-30T16:48:49.184501+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["zimbra", "rce", "cisa-kev"]
cves: ["CVE-2026-73570"]
source: "https://www.microsoft.com/en-us/security/blog/2026/09/30/unauthenticated-command-injection-on-internet-facing-mail-servers-tracking-cve-2026-73570/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Act:** CISA KEV listing plus a public GitHub PoC confirms active exploitation of this unauthenticated RCE on Zimbra mail servers. Apply the available Zimbra patch immediately; if the instance is internet-facing and patching will be delayed, consider taking it offline or blocking external access as a temporary control.
- **SOC/IR — Act:** Microsoft's analysis includes attack paths and detection opportunities for an actively exploited, unauthenticated command injection on a common enterprise mail platform. Run a targeted hunt across Zimbra hosts for compromise indicators using the TTPs outlined in the post, and tune SIEM/EDR detections against the described exploitation behavior — assume any unpatched internet-facing Zimbra instance may already be compromised.
- **Leader — Plan:** This is a KEV-listed RCE on internet-facing mail servers, meaning exploitation is confirmed in the wild; confirm whether Zimbra is in your inventory and verify the engineering team has an emergency patch timeline in place this week. Not yet at Log4Shell systemic scope, but email server compromise carries credential and data-exfiltration risk worth validating before it becomes an incident.
- **Signals:** CVE-2026-73570 — CISA KEV: listed, EPSS 0.12, public PoC on GitHub
