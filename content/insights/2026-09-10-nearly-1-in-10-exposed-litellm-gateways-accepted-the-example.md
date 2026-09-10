---
title: "10% of Internet-Exposed LiteLLM Gateways Use Default \"sk-1234\" Admin Key"
date: 2026-09-10T14:58:06.811051+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["default-credentials", "ai-gateway", "misconfiguration"]
cves: []
source: "https://thehackernews.com/2026/09/nearly-1-in-10-exposed-litellm-gateways.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** If you run LiteLLM, immediately check whether your admin key is still "sk-1234" and rotate it to a strong credential; a compromised gateway exposes all upstream model API keys and full prompt/completion history to anyone who finds the instance.
- **SOC/IR — Plan:** Build a detection rule to flag any LiteLLM API requests authenticating with the literal string "sk-1234", and sweep existing gateway/proxy logs since initial deployment for unauthorized admin activity.
- **Leader — Plan:** Direct engineering to inventory all internal and vendor-managed LiteLLM deployments and confirm no default admin credentials are in use; a misconfigured AI gateway exposes both uncapped API spend and the full record of what your applications send to model providers.
