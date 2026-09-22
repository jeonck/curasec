---
title: "Fake LastPass Installer Uses Microsoft-Signed Driver to Kill EDR"
date: 2026-09-22T15:30:54.753130+00:00
verdict: "Act"
verdict_engineer: "Learn"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["byovd", "edr-evasion", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/09/fake-lastpass-authenticator-installer.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No patch or config change applies here — the attack requires a user to execute a fake installer. Worth understanding that WHCP-signed kernel drivers can be weaponized to blind EDR before a stealer runs, which has implications for defense-in-depth design (e.g., application allowlisting, restricting GitHub-sourced executables in managed environments).
- **SOC/IR — Act:** This campaign shows zero AV/EDR detections due to the signed driver kill-chain, making standard signature coverage unreliable; hunt for suspicious kernel driver loads coinciding with LastPass-themed installer execution and tune detections on processes attempting to terminate security tooling (EDR self-protection bypass behavior).
- **Leader — Plan:** If LastPass is in the enterprise toolset, issue an internal advisory directing users to install authenticator apps only from official vendor or app-store sources; this is a brand-abuse social-engineering vector that warrants a user-awareness communication this quarter rather than immediate escalation.
