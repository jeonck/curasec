---
title: "LiteLLM Supply Chain Compromise Pushes Credential Stealer to PyPI and Docker Hub"
date: 2026-10-22T15:52:23.930402+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "python-package", "ai-gateway"]
cves: []
source: "https://thehackernews.com/2026/10/litellm-suspects-github-token-leak-in.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active supply chain compromise: if you run litellm, check immediately for version 1.107.0 in pip environments and Docker images, remove it, rotate any credentials and LLM API keys that may have been exposed through the credential stealer.
- **SOC/IR — Act:** Sweep all systems for litellm==1.107.0 installations deployed on or after October 21, 2026; hunt for outbound connections or credential exfiltration from hosts where that version ran, and treat any match as a potential backdoor compromise.
- **Leader — Act:** LiteLLM is widely used as an AI gateway routing LLM API keys — confirm whether any teams use it, check exposure to the malicious 1.107.0 release, and request LiteLLM's incident report to assess scope before this surfaces in board-level AI security discussions.
