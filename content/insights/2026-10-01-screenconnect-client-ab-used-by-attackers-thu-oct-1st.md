---
title: "ScreenConnect RMM Tool Abused as Attack Vector"
date: 2026-10-01T17:21:52.102295+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["rmm-abuse", "remote-access", "living-off-the-land"]
cves: []
source: "https://isc.sans.edu/diary/rss/33388"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** No patch or configuration change required; this is a technique highlight showing attackers deploy legitimate RMM clients to blend in. Worth auditing your estate for unauthorized ScreenConnect installations and confirming it appears only where IT-sanctioned.
- **SOC/IR — Plan:** Build or tune detections for ScreenConnect client processes spawning in unexpected contexts (non-IT endpoints, unusual parent processes, new installs outside change windows); review your SIEM for ScreenConnect relay connections to external infrastructure.
- **Leader — Skip**
