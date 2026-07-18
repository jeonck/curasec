---
title: "OpenSSL HollowByte DoS: 11-byte TLS request leaks 131 KB per request"
date: 2026-07-18T11:51:11.203777+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["openssl", "denial-of-service", "tls"]
cves: []
source: "https://thehackernews.com/2026/07/openssl-hollowbyte-flaw-could-freeze.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** OpenSSL is near-universal; the fix shipped silently in June with no CVE, no advisory, and no changelog callout, meaning most deployments are unknowingly unpatched. Audit your OpenSSL version and upgrade to the June or later release containing the HollowByte fix — glibc-based servers are confirmed vulnerable and memory is not reclaimed until process restart.
- **SOC/IR — Plan:** No active exploitation or IOCs are currently cited, but Okta's public research lowers the bar for abuse. Build or queue a detection for abnormal memory growth trends or bursts of minimal-size TLS connections against OpenSSL-serving hosts, and flag it once exploitation attempts surface in the wild.
- **Leader — Learn:** A DoS flaw in OpenSSL is operationally significant but below board-level threshold; the more notable governance signal is that the fix was shipped with no CVE, no advisory, and no changelog pointer — a disclosure gap in a critical transitive dependency worth surfacing in your software supply chain risk review.
