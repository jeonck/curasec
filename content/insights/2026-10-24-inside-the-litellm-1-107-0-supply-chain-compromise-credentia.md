---
title: "LiteLLM 1.107.0 supply chain compromise: Python startup hooks steal creds"
date: 2026-10-24T14:29:02.695753+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "python", "credential-theft"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Act:** LiteLLM is widely used in AI/ML workloads; a confirmed supply-chain compromise with credential theft and remote code loading is an immediate Act trigger. Audit all dependency trees and container images for version 1.107.0, rotate any API keys or cloud credentials accessible from affected environments, and review the Microsoft post's IOCs against build/runtime logs.
- **SOC/IR — Act:** Microsoft published TTPs and detections for this compromise; hunt for abuse of Python startup hooks (usercustomize/sitecustomize) across Python-capable hosts since the 1.107.0 release window, and sweep for the remote code-loading IOCs detailed in the post.
- **Leader — Act:** A confirmed supply-chain compromise of a widely-adopted AI/LLM proxy library with credential theft impact; direct engineering this week to assess whether LiteLLM 1.107.0 is in use and report on any exposed credentials, and be prepared to brief leadership on scope if exposure is confirmed.
