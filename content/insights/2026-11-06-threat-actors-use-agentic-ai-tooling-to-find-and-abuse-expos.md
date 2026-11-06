---
title: "Threat actors use AI agent framework ARTEX to harvest GitHub OAuth secrets"
date: 2026-11-06T17:55:59.437458+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["oauth", "exposed-secrets", "agentic-ai"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Act:** Active exploitation observed: run GitHub secret scanning across all repos (public and private) to identify exposed OAuth application secrets, then rotate any found credentials and audit the associated OAuth apps for unauthorized actions.
- **SOC/IR — Act:** Active campaign with traceable TTPs: hunt for anomalous OAuth application authentication events and unusual API calls in Entra/M365 audit logs, focusing on OAuth apps that have recently authenticated from unexpected sources or granted new delegated permissions.
- **Leader — Act:** Microsoft Threat Intelligence documents an active, AI-augmented campaign capable of systematically targeting any organization with OAuth secrets in GitHub; task your security team this week to confirm exposure and audit OAuth application activity before this surfaces as a customer or board question.
