---
title: "North Korea Contagious Interview Campaign: 30K Devices, $10.71M Stolen"
date: 2026-09-22T15:30:54.753130+00:00
verdict: "Act"
verdict_engineer: "Learn"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["threat-intel", "supply-chain", "north-korea"]
cves: []
source: "https://thehackernews.com/2026/09/contagious-interview-campaign.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No KEV listing or PoC signals; the campaign targets individuals via fake job interviews delivering malware, so engineering teams should be aware of the social-engineering vector but no immediate patch or config action is required today.
- **SOC/IR — Act:** Joint advisory indicates active, widespread campaign — hunt for Contagious Interview TTPs (fake recruiter lures, malicious npm/Python packages, BeaverTail/InvisibleFerret malware) in endpoint and email telemetry, and sweep for IOCs from the advisory across devices belonging to engineering and crypto-adjacent staff.
- **Leader — Plan:** A confirmed North Korean campaign at this scale targeting engineers and crypto wallets warrants a policy review of how staff handle unsolicited recruiting outreach and code from unknown sources; brief security awareness owners to update training for engineering and finance teams this quarter.
