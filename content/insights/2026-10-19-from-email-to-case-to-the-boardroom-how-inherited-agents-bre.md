---
title: "Salesforce Agentforce Email-to-Case Creates Prompt Injection Path"
date: 2026-10-19T17:27:24.131557+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["prompt-injection", "salesforce-agentforce", "ai-agents"]
cves: []
source: "https://thehackernews.com/2026/10/from-email-to-case-to-boardroom-how.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Organizations running Salesforce Agentforce with Email-to-Case or Web-to-Case should audit their Flow configurations to identify where untrusted customer input reaches agent prompts without sanitization; no exploitation signals present but the attack surface is as-designed and non-obvious.
- **SOC/IR — Learn:** This outlines how standard Salesforce workflow chaining can route external user-controlled content into AI agent prompts — a useful mental model for the indirect prompt injection attack class, but no IOCs, TTPs, or detection signatures are provided for immediate action.
- **Leader — Plan:** If your organization uses Salesforce Agentforce for customer support intake, commission a review of which agentic workflows ingest customer-controlled data; this is the 'AI agents need policy before controls' gap and warrants a governance check before broader Agentforce rollout.
