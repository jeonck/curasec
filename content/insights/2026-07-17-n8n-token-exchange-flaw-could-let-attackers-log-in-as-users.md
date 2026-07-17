---
title: "n8n JWT Cross-Issuer Flaw Enables Account Takeover on Enterprise"
date: 2026-07-17T12:06:10.948288+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["authentication-bypass", "jwt", "workflow-automation"]
cves: []
source: "https://thehackernews.com/2026/07/n8n-token-exchange-flaw-could-let.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Any n8n Enterprise deployment trusting multiple external JWT issuers is exposed to cross-tenant account takeover via `iss` claim bypass; patch n8n to the fixed version and audit multi-issuer OIDC/JWT configurations now.
- **SOC/IR — Skip**
- **Leader — Skip**
