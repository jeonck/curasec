---
title: "LLMJacking: Threat Actors Monetize Stolen Cloud LLM Credentials"
date: 2026-11-02T20:44:36.815553+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["llmjacking", "cloud-security", "credential-theft"]
cves: []
source: "https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models/"
source_name: "Google Threat Intelligence"
status: "active"
---
- **Engineer — Act:** Active, multi-incident campaign causing up to $100K/day in fraudulent LLM API charges. Audit IAM roles and service accounts with LLM API access, rotate any exposed keys, and enable cloud billing anomaly alerts with low thresholds for AI/ML service spend.
- **SOC/IR — Act:** Mandiant-responded incidents with a clear detection surface: sudden spikes in LLM API request volume are the primary behavioral signal. Build or tune detections for abnormal AI/ML API call rates and hunt for credential exfiltration activity in cloud IAM logs since mid-2026.
- **Leader — Plan:** Financial exposure can reach $1M before access is revoked, affecting sectors including financial services and technology. This quarter, establish a governance policy for LLM API key issuance, enforce spend caps, and confirm billing alert thresholds cover AI service abuse scenarios.
