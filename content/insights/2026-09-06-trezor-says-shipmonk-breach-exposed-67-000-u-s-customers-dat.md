---
title: "ShipMonk Breach Exposes 67K Trezor Customers' PII Vendor Said It Deleted"
date: 2026-09-06T14:08:28.650854+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Plan"
tags: ["vendor-breach", "supply-chain", "data-exposure"]
cves: []
source: "https://thehackernews.com/2026/09/trezor-says-shipmonk-breach-exposed.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No vulnerability to patch; the salient lesson is that vendor data-deletion attestations cannot be taken at face value — worth reviewing contractual data-retention obligations and requesting evidence (not just assertions) from third-party logistics or fulfillment partners holding customer PII.
- **SOC/IR — Skip**
- **Leader — Plan:** This case — a logistics vendor retaining customer data after certifying deletion — is a textbook vendor risk gap; schedule a review of fulfillment and logistics vendors' data-lifecycle practices this quarter and require documented evidence of deletion rather than self-attestation.
