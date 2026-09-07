---
title: "ASCII smuggling via invisible Unicode evades email security filters"
date: 2026-09-07T16:27:04.378719+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["phishing", "email-security", "evasion"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/attackers-conceal-phishing-lures-using-invisible-unicode-characters/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** ASCII smuggling with invisible Unicode is a useful technique to understand when evaluating email security tooling or building internal phishing-resistant workflows; no patch or configuration change required today.
- **SOC/IR — Plan:** Add detection coverage for invisible Unicode characters in email bodies and subject lines — tune existing email security filters to flag or quarantine messages containing high-density non-printing Unicode codepoints, and build a hunt query against recent inbound mail logs for this pattern.
- **Leader — Skip**
