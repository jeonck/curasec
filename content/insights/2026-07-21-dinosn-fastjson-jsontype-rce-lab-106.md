---
title: "FastJSON @JSONType RCE Lab: public exploit bypasses autoType=OFF"
date: 2026-07-21T12:43:35.631021+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["fastjson", "rce", "public-poc"]
cves: []
source: "https://github.com/dinosn/fastjson-jsontype-rce-lab"
source_name: "GitHub Trending"
status: "archived"
---
- **Engineer — Act:** A public Docker lab with a working one-payload exploit now exists for fastjson 1.2.66–1.2.83; critically, autoType=OFF and parseObject binding are not effective mitigations. Audit your dependency tree for fastjson in this range and upgrade to 1.2.84+ (or fastjson2), treating autoType-disabled deployments as unprotected.
- **SOC/IR — Plan:** The public exploit lab lowers the bar for threat actors to weaponize this Spring Boot class-loading RCE chain. Build or tune detections for unexpected outbound SSRF from Java application hosts followed by remote class loading activity; the SSRF→defineClass pattern is a distinct behavioral signal to hunt for in proxy and EDR telemetry.
- **Leader — Skip**
