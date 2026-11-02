---
title: "Google Dismantles XCPE Botnet Built Into Videostrong Set-Top Boxes"
date: 2026-11-02T20:44:36.815553+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["botnet", "supply-chain", "iot-security"]
cves: []
source: "https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet/"
source_name: "Google Threat Intelligence"
status: "active"
---
- **Engineer — Learn:** A firmware-level backdoor shipped pre-installed across multiple device models over years is a concrete supply-chain integrity case study; informs hardware procurement standards and secure boot requirements, but no action needed on typical cloud/app infrastructure.
- **SOC/IR — Learn:** The campaign enrolled 10M+ devices into residential proxy networks used to obscure malicious traffic origins — useful context for tuning detections that rely on residential IP reputation signals, though the C2 infrastructure has already been disrupted with no specific IOCs released.
- **Leader — Learn:** A manufacturer intentionally shipping backdoored devices at scale illustrates hardware supply-chain risk at the vendor relationship level; useful material for board discussions on device procurement controls and vendor integrity assurance programs, but unlikely to require immediate action unless the organization directly procures Videostrong hardware.
