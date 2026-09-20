---
title: "OpenAI Codex sandbox escapes patched after researcher disclosure"
date: 2026-09-20T14:41:12.964217+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["ai-security", "sandbox-escape", "supply-chain"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If your team uses OpenAI Codex CLI or the Codex environment, verify you're running the patched version — one escape vector ran arbitrary commands on the developer's host machine. No active exploitation reported, but the attack surface is every developer workstation running Codex.
- **SOC/IR — Learn:** The sandbox escape technique (achieving host code execution from a locked-down AI coding sandbox) is worth understanding as a new attack class against AI developer tooling, but no IOCs or in-the-wild exploitation are reported, leaving no immediate detection action to take.
- **Leader — Learn:** Useful data point on AI coding assistant risk: sandbox escapes in tools running on developer machines represent a developer-workstation compromise vector worth acknowledging in AI tool policies, but the issues are patched and no exploitation was reported, so no immediate escalation is warranted.
