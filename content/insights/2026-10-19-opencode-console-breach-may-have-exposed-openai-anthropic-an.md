---
title: "OpenCode Console Breach May Have Exposed AI Provider API Keys"
date: 2026-10-19T17:27:24.131557+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["vendor-breach", "api-key-exposure", "ai-provider"]
cves: []
source: "https://thehackernews.com/2026/10/opencode-console-breach-may-have.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** If your team stored OpenAI, Anthropic, or Google API keys in OpenCode Console, treat them as compromised: revoke and reissue those keys immediately, then audit provider dashboards for unauthorized calls since October 16.
- **SOC/IR — Act:** For any org using OpenCode Console, hunt for anomalous AI provider API usage (unexpected spikes in calls, unfamiliar IP origins, unexpected cost) in OpenAI/Anthropic/Google dashboards and SIEM from October 16 onward, assuming keys may be in adversary hands.
- **Leader — Act:** Confirm whether your organization uses OpenCode Console; if so, request an incident report from OpenCode and have engineering rotate all affected AI provider keys this week — exposure of these keys can result in significant unauthorized spend or data access via AI APIs.
