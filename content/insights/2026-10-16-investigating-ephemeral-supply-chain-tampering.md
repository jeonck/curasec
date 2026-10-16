---
title: "UNC7017 Uses Ephemeral Update Tampering in AOMEI Supply Chain Attack"
date: 2026-10-16T15:21:49.798528+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "malware", "threat-intel"]
cves: []
source: "https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering/"
source_name: "Google Threat Intelligence"
status: "active"
---
- **Engineer — Act:** If AOMEI backup/disk utilities are deployed in your environment, audit endpoints and build systems for CROSSROAD downloader or SHINYROAD backdoor indicators; the 5–10 minute tampering windows mean file-integrity scans at rest may have missed the delivery.
- **SOC/IR — Act:** Hunt for CROSSROAD and SHINYROAD IOCs on hosts that could have fetched AOMEI updates between April and July 2026; standard hash-based detection likely missed the ephemeral delivery window, so focus on behavioral indicators (unusual parent-child process chains post-update, unexpected staging domain connections).
- **Leader — Act:** Confirm whether AOMEI software is in use anywhere in your environment and request Mandiant's full IOC set to verify exposure; the novel evasion technique (auto-reverting tampering windows) is a systemic supply chain risk worth briefing leadership on as evidence that static compliance checks alone are insufficient.
