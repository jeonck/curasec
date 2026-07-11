---
title: "Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers"
date: 2026-07-11T11:49:48.413664+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["sharefile", "active-incident", "enterprise-file-sharing"]
cves: []
source: "https://thehackernews.com/2026/07/urgent-progress-tells-sharefile.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Progress has confirmed a credible active threat against on-prem ShareFile Storage Zone Controllers and is directing customers to shut them down immediately. If you run Storage Zone Controllers on Windows, take them offline now and await Progress's remediation guidance before bringing them back up.
- **SOC/IR — Act:** A vendor-confirmed active compromise campaign against enterprise file-sharing infrastructure warrants an assume-breach review if ShareFile is in your environment — check for lateral movement or data staging activity originating from Storage Zone Controller hosts since at least the past 30 days, and watch Progress and threat intel feeds for IOC release.
- **Leader — Act:** Progress's directive to shut down an enterprise product mid-operation signals a serious active incident; confirm this week whether your organization runs ShareFile Storage Zone Controllers, request a formal incident statement from Progress, and assess whether any stored data exposure triggers disclosure obligations.
