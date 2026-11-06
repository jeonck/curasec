---
title: "OpenSSH SSHole (CVE-2026-123158) Exploited Within Hours of Disclosure"
date: 2026-11-06T17:55:59.437458+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["openssh", "alpine-linux", "active-exploitation"]
cves: ["CVE-2026-123158"]
source: "https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active exploitation confirmed on honeypots plus a public PoC on GitHub — patch OpenSSH immediately on any Alpine Linux (musl libc) hosts or container images where PAM is disabled, and audit for no-password accounts that could be targeted; disable SSH exposure in containers where it isn't needed.
- **SOC/IR — Act:** With in-the-wild exploitation and a public PoC, hunt for successful SSH authentications to no-password accounts on Alpine-based hosts since the disclosure date, and check for unexpected root sessions originating from SSH on musl-libc systems.
- **Leader — Learn:** Attack surface is narrow — requires musl libc, PAM disabled, and no-password accounts — so this is not a systemic board-level event; engineering teams should handle patching without leadership escalation unless a material Alpine-heavy workload is confirmed exposed.
- **Signals:** CVE-2026-123158 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub
