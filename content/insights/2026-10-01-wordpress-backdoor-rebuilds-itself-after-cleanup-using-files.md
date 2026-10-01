---
title: "WordPress 'SC' Backdoor Uses Files, DB, and Shared Memory to Persist"
date: 2026-10-01T17:21:52.102295+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["wordpress", "malware-persistence", "backdoor"]
cves: []
source: "https://thehackernews.com/2026/10/wordpress-backdoor-rebuilds-itself.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** WordPress is pervasive in enterprise estates and this multi-vector persistence (filesystem + database + shared memory segments) means standard file-only cleanup leaves the site re-infected; audit WordPress deployments for SC_ markers in files and the database, and inspect PHP shared memory usage via shmop-based process inspection.
- **SOC/IR — Plan:** The shared-memory component creates a blind spot for file-integrity and AV-based scans; build or tune detections for PHP processes writing to shared memory segments (shmop_open/write syscalls) and add a correlation rule requiring simultaneous sweep of filesystem, database content, and memory when a WordPress compromise is suspected.
- **Leader — Skip**
