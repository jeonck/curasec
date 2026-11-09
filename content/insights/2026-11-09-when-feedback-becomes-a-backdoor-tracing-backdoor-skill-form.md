---
title: "Reference-Feedback Poisoning Can Implant Backdoors in LLM Skill Agents"
date: 2026-11-09T22:16:08.330867+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Learn"
tags: ["llm-security", "supply-chain", "ai-agents"]
cves: []
source: "https://arxiv.org/abs/2611.09348"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** Novel attack class showing that poisoning reference answers in SkillOpt-style pipelines can inject persistent trigger-conditioned backdoors with no model or optimizer access; teams building LLM agents with feedback-driven skill learning should evaluate whether reference-answer inputs are treated as untrusted data with validation controls.
- **SOC/IR — Skip**
- **Leader — Learn:** Academic research demonstrating a new supply-chain-style risk in AI agent feedback loops; organizations deploying LLM agents that ingest external reference answers for skill training should add this attack class to their AI risk register ahead of policy work on agentic systems.
