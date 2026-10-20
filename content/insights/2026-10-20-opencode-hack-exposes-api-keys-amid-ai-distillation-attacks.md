---
title: "OpenCode breach exposes user API keys for external AI providers"
date: 2026-10-20T15:39:31.280324+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["api-key-exposure", "supply-chain", "ai-tooling"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/opencode-hack-exposes-api-keys-amid-ai-distillation-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If your team uses OpenCode, audit which external-provider API keys were configured through it and rotate any that may have been exposed; scope is described as small, but key rotation is low-cost insurance.
- **SOC/IR — Learn:** No IOCs or TTPs published; breach affects a niche open-source tool with limited enterprise footprint and no detection surface described in the report.
- **Leader — Skip**
