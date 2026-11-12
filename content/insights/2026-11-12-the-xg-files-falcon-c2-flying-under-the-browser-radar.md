---
title: "Falcon C2: Browser-Based Framework Targets Governments via Extensions"
date: 2026-11-12T18:52:40.662404+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["browser-security", "c2-framework", "threat-research"]
cves: []
source: "https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Learn:** Falcon C2's use of browser extensions and malicious scripts as a C2 channel is a novel technique worth factoring into enterprise browser hardening and extension allowlist policies — no patch or immediate reconfiguration required today.
- **SOC/IR — Plan:** Build or tune detections for browser extension-based C2 behaviors: unusual extension installations, extensions making anomalous outbound connections, and behavioral indicators tied to the Antino implant; no specific IOCs are published in this summary to hunt on immediately.
- **Leader — Learn:** Government-targeting browser C2 campaign is useful sector threat context, but with no named vendor breach or regulatory deadline, this is background intelligence rather than a same-week action item.
