---
title: "Sandworm & UAC-0099 Deploy Mesh Network Backdoor in Ukraine Wiper Attack"
date: 2026-10-23T15:44:28.729261+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["sandworm", "apt", "destructive-malware"]
cves: []
source: "https://thehackernews.com/2026/10/russian-linked-hackers-used-new-mesh.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Sandworm's novel mesh-network backdoor technique represents a new C2 architecture worth understanding for defensive design, but no specific software to patch is identified — initial access was spear-phishing, not a software vulnerability.
- **SOC/IR — Plan:** Review the full ESET technical report for IOCs and TTPs tied to this new backdoor, then build or tune detections for mesh-style C2 beaconing and destructive wiper staging behaviors mapped to ATT&CK; the summary is truncated so treat this as a queue item for the ESET write-up.
- **Leader — Learn:** Useful campaign retrospective illustrating Sandworm's continued evolution in destructive tooling; relevant for board-level threat-landscape awareness, particularly for organizations in logistics or critical infrastructure sectors with European operations.
