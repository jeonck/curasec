---
title: "Spring Boot /actuator/heapdump endpoint exposes secrets in memory"
date: 2026-07-27T13:44:31.918240+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["spring-boot", "secrets-exposure", "misconfiguration"]
cves: []
source: "https://isc.sans.edu/diary/rss/33188"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Act:** Audit all Spring Boot deployments for exposed /actuator/heapdump endpoints — this endpoint leaks in-memory secrets including API keys and DB credentials. Disable or restrict actuator endpoints via Spring Security configuration if not required.
- **SOC/IR — Plan:** Build a detection for inbound GET requests to /actuator/heapdump in web/proxy logs; active scanning activity means attackers are already probing for this endpoint in your estate.
- **Leader — Skip**
