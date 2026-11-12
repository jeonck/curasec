---
title: "Post-training supply chain attacks can hijack AI coding agents for RCE"
date: 2026-11-12T18:52:40.662404+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["ai-supply-chain", "model-poisoning", "coding-agents"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/11/12/trained-to-betray-how-post-training-supply-chain-attacks-hijack-coding-agents/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Learn:** Novel research on poisoned model checkpoints and datasets as an RCE vector in coding agents — no active exploitation or PoC, but engineers ingesting third-party models or using AI coding tools in CI/CD pipelines should evaluate their model provenance and sandboxing practices.
- **SOC/IR — Learn:** No IOCs, TTPs, or detection content are surfaced in this summary; useful background on AI agent attack surface for future detection design, but nothing actionable to hunt or tune today.
- **Leader — Plan:** As coding agent adoption grows, this research signals a maturing supply chain risk class for AI tooling — initiate a policy review this quarter covering approved model sources, checkpoint integrity verification, and acceptable use of AI coding agents in production pipelines.
