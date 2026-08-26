---
title: "SSRF bypass: IP addresses obfuscated as hostnames evade blocklists"
date: 2026-08-26T11:42:13.540622+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["ssrf", "appsec", "evasion"]
cves: []
source: "https://isc.sans.edu/diary/rss/33280"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** Highlights that string-matching or IP blocklists for SSRF protection (e.g. blocking '169.254.169.254') can be bypassed via hostname equivalents — review your SSRF defenses to ensure they resolve hostnames before comparing, not just match raw strings.
- **SOC/IR — Learn:** Useful context for tuning SSRF-related detections: logs showing hostname variants of link-local or metadata addresses in outbound requests may indicate bypass attempts worth adding to hunt queries.
- **Leader — Skip**
