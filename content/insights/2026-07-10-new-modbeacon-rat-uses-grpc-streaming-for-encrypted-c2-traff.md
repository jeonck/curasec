---
title: "MODBEACON RAT Uses gRPC C2; Linked to China's Silver Fox Group"
date: 2026-07-10T09:49:54.653216-05:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["rat", "threat-actor", "c2"]
cves: []
source: "https://thehackernews.com/2026/07/new-modbeacon-rat-uses-grpc-streaming.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Learn:** gRPC-based C2 may evade TLS inspection tuned for HTTP/2 REST traffic; review whether your egress controls decode and inspect gRPC streams.
- **SOC/IR — Plan:** Build or tune detections for outbound gRPC streaming to novel external endpoints; Silver Fox distributes via SEO-poisoned counterfeit installers, so hunt for unexpected Rust-compiled binaries in user-facing application paths.
- **Leader — Learn:** Adds to the picture of China-linked actors targeting enterprise software supply chains via SEO poisoning; useful context for board-level threat landscape briefings but no immediate action required.
