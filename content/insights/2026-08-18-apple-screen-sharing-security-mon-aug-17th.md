---
title: "Apple Screen Sharing Uses Unencrypted VNC Under the Hood"
date: 2026-08-18T11:37:25.033598+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["macos", "vnc", "configuration"]
cves: []
source: "https://isc.sans.edu/diary/rss/33252"
source_name: "SANS ISC"
status: "archived"
---
- **Engineer — Learn:** Useful context on macOS screen sharing's VNC foundation — unencrypted by default with simple password auth — worth auditing whether screen sharing is enabled on any managed Mac fleet and confirming it is tunneled through SSH or restricted to VPN.
- **SOC/IR — Skip**
- **Leader — Skip**
