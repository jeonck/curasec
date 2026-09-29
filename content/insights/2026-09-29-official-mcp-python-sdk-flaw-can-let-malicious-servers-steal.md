---
title: "MCP Python SDK OAuth Credential Theft Flaw Fixed in v1.30.0"
date: 2026-09-29T16:53:02.010350+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["supply-chain", "oauth", "ai-agents"]
cves: []
source: "https://thehackernews.com/2026/09/official-mcp-python-sdk-flaw-can-let.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Any application built on the MCP Python SDK before 1.30.0 could expose OAuth client secrets, authorization codes, and PKCE keys to a malicious MCP server; upgrade to 1.30.0 and audit all MCP server endpoints your app trusts. No active exploitation signals yet, but the credential theft path is direct.
- **SOC/IR — Learn:** No IOCs, no exploitation activity, and no useful detection surface today, but understanding that MCP servers are a potential OAuth credential harvesting vector is worth noting as AI-agent tooling proliferates in enterprise environments.
- **Leader — Learn:** This is an early signal about supply-chain risk in AI-agent SDK infrastructure; no breach or active exploitation reported, but worth factoring into any AI-agent adoption policy before MCP-based tooling is widely deployed internally.
