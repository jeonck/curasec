---
title: "IETF Publishes HTTP QUERY Method (RFC 10008): First New Verb Since PATCH"
date: 2026-09-18T14:58:07.079452+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["http-protocol", "web-security", "rfc"]
cves: []
source: "https://isc.sans.edu/diary/rss/33352"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** The new QUERY method sits between GET and POST semantics, meaning existing WAF rules, reverse proxies, and security controls may handle it inconsistently or not at all — worth understanding before adopting it in APIs or encountering it in the wild.
- **SOC/IR — Learn:** A new HTTP verb with ambiguous semantics may appear in traffic without triggering existing method-based detection rules; no active exploitation context, but analysts should know to expect it in logs and WAF telemetry.
- **Leader — Skip**
