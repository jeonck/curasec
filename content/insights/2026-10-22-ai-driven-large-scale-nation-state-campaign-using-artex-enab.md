---
title: "Storm-0940 uses AI tool ARTEX in ConnectWise supply chain attack on M365"
date: 2026-10-22T15:52:23.930402+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "nation-state", "m365"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Act:** ConnectWise supply chain compromise explicitly triggers Act; audit your M365 tenant for unauthorized OAuth app registrations and anomalous credential grants, and verify ConnectWise installation integrity against known-good baselines.
- **SOC/IR — Act:** Active nation-state campaign with ATT&CK-mappable TTPs (supply chain compromise, application credential abuse); hunt for anomalous OAuth app registrations and unexpected delegated permission grants in M365 unified audit logs going back at least 90 days, and pull the full Microsoft post for Sentinel/Defender detection queries.
- **Leader — Act:** Nation-state supply chain compromise via a widely-used MSP tool affecting M365 tenants qualifies as a systemic event; verify whether ConnectWise is in your environment directly or via a managed service provider, request a formal exposure attestation from ConnectWise, and brief leadership given the nation-state attribution before they see it in the news.
