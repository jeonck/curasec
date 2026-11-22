---
title: "OpenRouter Drops 3 Providers After Months of Silent Prompt Data Theft"
date: 2026-11-22T16:05:35.915127+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["ai-supply-chain", "data-theft", "vendor-breach"]
cves: []
source: "https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** If your stack routes AI requests through OpenRouter or any inference aggregator, audit which providers handled your traffic and what prompts were sent; the Zero Data Retention bypass means contractual data-handling guarantees may not reflect actual behavior — review your AI API vendor contracts and enforce egress logging at the gateway.
- **SOC/IR — Act:** If your organization uses OpenRouter or similar inference gateways, treat this as a potential months-long data exfiltration event: pull AI API egress logs, identify traffic routed to the now-dropped providers, and open an exposure review — dwell time was undetected at the providers themselves, so endpoint-side logging is your only current visibility.
- **Leader — Act:** Confirm whether your organization uses OpenRouter or any third-party AI inference aggregator, then request a written incident scope statement from your providers; the Zero Data Retention breach means sensitive prompts — potentially including PII, IP, or customer data — may have been exfiltrated for months without disclosure, which could carry GDPR or contractual notification obligations.
