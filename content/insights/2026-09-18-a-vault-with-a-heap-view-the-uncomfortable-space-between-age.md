---
title: "AWS AgentCore Harness default configs enable prompt-injection credential theft"
date: 2026-09-18T14:58:07.079452+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["aws-agentcore", "prompt-injection", "ai-agents"]
cves: []
source: "https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Plan:** If you run AWS AgentCore Harness for AI agent workloads, audit your default IAM role assignments and trust boundaries this quarter — the research identifies specific misconfigurations that allow injected prompts to reach credential storage. No active exploitation or PoC noted, but the hardening steps are concrete and low-effort.
- **SOC/IR — Learn:** The prompt-injection-to-credential-exfiltration path in AI agent runtimes is a maturing attack class worth understanding for future detection coverage, but no IOCs, active campaigns, or ATT&CK mappings are surfaced here to act on today.
- **Leader — Learn:** This illustrates the emerging risk of AI agent frameworks inheriting over-privileged identities — useful context for shaping an AI/LLM agent governance policy before the attack surface grows, but no immediate leadership action is required.
