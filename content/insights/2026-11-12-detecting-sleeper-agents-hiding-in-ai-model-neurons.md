---
title: "Microsoft Research: Sleeper agents injectable via <10 neuron edits in AI models"
date: 2026-11-12T18:52:40.662404+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["ai-security", "supply-chain", "research"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/11/10/detecting-sleeper-agents-hiding-in-ai-model-neurons/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Learn:** Novel attack class showing AI model weights can be covertly backdoored at the neuron level; no immediate patch action exists, but engineers deploying or fine-tuning models should track emerging model-integrity verification tooling as this matures.
- **SOC/IR — Learn:** No IOCs, no active exploitation, and no detection rules are available yet; the research notes frontier agents can spot anomalous weight edits, but no operationalizable detection surface exists today.
- **Leader — Plan:** This demonstrates a credible supply-chain attack vector against AI agent models — relevant to any org deploying third-party or fine-tuned LLMs; add model-integrity and provenance attestation requirements to AI vendor assessments this quarter before AI agents proliferate further.
