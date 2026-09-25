---
title: "Placeholder domain third-party[.]com now serves ClickFix malware via 1,700+ repos"
date: 2026-09-25T15:49:12.385738+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["clickfix", "supply-chain", "domain-hijacking"]
cves: []
source: "https://thehackernews.com/2026/09/placeholder-third-partycom-referenced.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Search all repos, internal docs, and README files for references to 'third-party[.]com' and replace them; any user clicking the link from documentation now risks a ClickFix social-engineering payload targeting Windows.
- **SOC/IR — Act:** Block third-party[.]com at DNS/proxy immediately, sweep web proxy and DNS logs for recent queries to that domain, and hunt for ClickFix execution indicators (mshta/PowerShell spawned from browser or Run dialog) since the domain became malicious.
- **Leader — Plan:** This demonstrates a new documentation-placeholder squatting attack class affecting thousands of open-source projects; task engineering to audit internal repos this quarter and add placeholder-domain checks to developer guidelines and repository scanning policy.
