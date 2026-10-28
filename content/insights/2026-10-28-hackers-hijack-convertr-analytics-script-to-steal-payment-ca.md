---
title: "Hackers hijack Convertr analytics script for payment card skimming"
date: 2026-10-28T17:09:30.637292+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["supply-chain", "skimming", "e-commerce"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-hijack-convertr-analytics-script-to-steal-payment-card-data/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If you load third-party analytics scripts at checkout, audit your CSP and subresource integrity (SRI) settings; inventory any Convertr script dependencies and verify their current integrity hashes.
- **SOC/IR — Plan:** Build or tune a detection for unexpected script mutations or new external script loads on checkout pages; hunt for anomalous POST requests to unfamiliar domains from e-commerce endpoints.
- **Leader — Learn:** Third-party script supply-chain skimming is a recurring risk vector for e-commerce; useful framing for vendor risk discussions, but no immediate leadership action is indicated without confirmation of organizational exposure.
