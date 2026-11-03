---
title: "Google-Led Coalition Dismantles 1.3M Android TV Box Botnet"
date: 2026-11-03T18:24:39.173812+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["botnet", "iot-malware", "supply-chain"]
cves: []
source: "https://krebsonsecurity.com/2026/11/tech-firms-dismantle-botnet-that-turned-1-3m-tv-boxes-into-proxies/"
source_name: "Krebs on Security"
status: "active"
---
- **Engineer — Learn:** Devices shipped with pre-installed malware used as proxy exit nodes — a supply-chain integrity concern for any corporate IoT procurement. Botnet is dismantled, so no immediate patch action, but review device sourcing policies for Android-based IoT (TV boxes, healthcare devices) in your environment.
- **SOC/IR — Learn:** No IOCs or detection artifacts are provided, and the botnet command infrastructure has been severed, limiting immediate hunt value. Worth understanding the ad-fraud/residential-proxy TTP pattern for future investigations involving unexpected outbound proxy traffic from IoT segments.
- **Leader — Learn:** The inclusion of Android-based healthcare devices in the compromised pool is a meaningful data point for IoT and medical-device risk posture discussions. Botnet is neutralized, so no urgent vendor action needed, but useful framing for board-level conversations about supply-chain integrity in device procurement.
