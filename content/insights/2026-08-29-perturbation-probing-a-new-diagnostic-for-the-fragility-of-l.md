---
title: "Research: LLM Safety Refusals Are Fragile and Easily Bypassed"
date: 2026-08-29T15:36:18.143160+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Learn"
tags: ["llm-security", "ai-safety", "research"]
cves: []
source: "https://unit42.paloaltonetworks.com/perturbation-probing-llm-safety/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Learn:** Reinforces the design principle that LLM safety filters alone are insufficient; architecture decisions should place external guardrails (input/output validation, prompt firewalls) outside the model layer rather than trusting built-in refusals.
- **SOC/IR — Skip**
- **Leader — Learn:** Supports the case for defense-in-depth policy around AI deployments: if safety refusals are fragile by design, any AI system handling sensitive data needs external controls beyond the model's built-in guardrails — useful framing for board or audit conversations about AI risk.
