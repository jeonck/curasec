---
title: "JadePuffer ransomware uses agentic AI to attack and destroy Azure tenants"
date: 2026-09-28T18:35:17.473670+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["ransomware", "azure", "agentic-ai"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/jadepuffer-agentic-ai-attacks-target-azure-destroy-cloud-resources/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Azure tenants are directly in scope for this destructive ransomware campaign, but no KEV listing, PoC, or EPSS data is present to justify emergency action. Audit Azure service principal permissions and activity logs for anomalous automation, and verify that critical resource deletion requires additional approval controls.
- **SOC/IR — Act:** JadePuffer is an active operator running agent-driven Azure attacks involving credential theft and resource destruction — hunt Azure audit logs for unusual service principal activity and bulk resource operations, and tune detections for abnormal automation patterns consistent with agentic reconnaissance since this campaign surfaced.
- **Leader — Plan:** A named ransomware operator using AI agents to destroy Azure infrastructure represents a meaningful shift in cloud ransomware capability; confirm your Azure tenant's blast-radius controls (resource locks, backup isolation) are in place and add this actor profile to the risk register this quarter.
