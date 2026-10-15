---
title: "SANS ISC Guest Diary: Panchan Peer-to-Peer Cryptomining Botnet"
date: 2026-10-15T15:35:13.586755+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["botnet", "cryptomining", "linux"]
cves: []
source: "https://isc.sans.edu/diary/rss/33426"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** Panchan is a Go-based P2P botnet that spreads via SSH brute-force and drops cryptominers on Linux hosts — relevant to any team running internet-exposed Linux infrastructure, but the summary is too thin to identify new IOCs or required config changes.
- **SOC/IR — Learn:** An intern analysis of Panchan may surface behavioral indicators useful for tuning SSH brute-force and cryptominer detections, but no IOCs or ATT&CK mappings are provided in this summary to act on immediately.
- **Leader — Skip**
