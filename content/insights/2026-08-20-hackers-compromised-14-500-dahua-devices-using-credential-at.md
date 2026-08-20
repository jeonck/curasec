---
title: "Operation CameraSwarm: 14,500+ Dahua Devices Compromised via Auth Bypasses"
date: 2026-08-20T11:39:11.237527+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["iot-security", "credential-attack", "camera-exploitation"]
cves: []
source: "https://thehackernews.com/2026/08/hackers-compromised-14500-dahua-devices.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** If your environment includes Dahua cameras or NVRs, audit for these two auth-bypass CVEs and enforce credential rotation immediately; also review whether P2P relay features are exposed to the internet and disable if not required.
- **SOC/IR — Plan:** Build detections for unusual outbound P2P relay traffic from camera subnets and sweep network logs for connections to Dahua cloud relay infrastructure since June 17, 2026; full IOC set not confirmed in enrichment signals but Hunt.io research may provide indicators.
- **Leader — Learn:** Large-scale IoT compromise campaign is worth noting for vendor risk assessments if Dahua devices are deployed in physical security infrastructure, but no immediate leadership action is required absent confirmed breach at your organization.
