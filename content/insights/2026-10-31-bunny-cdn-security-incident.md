---
title: "Bunny CDN Security Incident"
date: 2026-10-31T16:03:46.666029+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Plan"
tags: ["cdn-security", "vendor-incident", "third-party-risk"]
cves: []
source: "https://status.bunny.net/incidents/p6gf1by9kr7m"
source_name: "HN (security)"
status: "active"
---
- **Engineer — Plan:** If Bunny CDN serves your assets or sits in your delivery pipeline, review the incident report at their status page and rotate any API keys or access tokens tied to your account as a precaution until scope is confirmed.
- **SOC/IR — Skip**
- **Leader — Plan:** Confirm whether your organization uses Bunny CDN and, if so, request a customer-facing incident report from them; assess whether any customer data or content delivery was affected and whether disclosure obligations apply.
