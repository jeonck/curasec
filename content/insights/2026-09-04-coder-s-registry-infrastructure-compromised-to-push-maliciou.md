---
title: "Coder registry infrastructure compromised via Cloudflare to deliver malicious Terraform modules"
date: 2026-09-04T14:56:27.274495+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "terraform", "credential-theft"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/coders-registry-infrastructure-compromised-to-push-malicious-modules/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** If your teams use Coder's Terraform registry, audit your module sources immediately and rotate any cloud credentials (AWS keys, GCP SAs, Azure SPNs) that Terraform may have accessed during runs while the malicious servers were active.
- **SOC/IR — Act:** Hunt CI/CD and IaC pipeline logs for module fetches from Coder's registry during the compromise window; look for anomalous outbound credential-exfiltration traffic from Terraform runner environments and trigger an assume-breach sweep if usage is confirmed.
- **Leader — Act:** Determine whether engineering teams use Coder's Terraform registry, and if so, request an incident timeline from Coder, assess credential exposure scope, and brief leadership on potential cloud environment impact before it surfaces externally.
