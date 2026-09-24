---
title: "AI agents weaponized to deploy skimmers, steal 600K credit cards"
date: 2026-09-24T15:49:46.689252+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["web-skimming", "ai-agents", "supply-chain"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/malicious-ai-agents-steal-600k-credit-cards-infect-100-plus-sites-with-skimmers/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If you operate e-commerce or payment pages, audit your site's JavaScript for unauthorized injections and review third-party script integrity; no specific CVE or PoC named in signals, but the attack vector (skimmer injection at scale via AI agents) warrants a near-term sweep of Content Security Policy and SRI enforcement.
- **SOC/IR — Act:** Active large-scale skimming campaign targeting online retailers — hunt for unauthorized script injections or outbound data exfiltration from payment pages in your estate; tune web proxy and SIEM rules for known skimmer exfil domains as IOCs become available.
- **Leader — Plan:** 600K card records stolen signals a material e-commerce threat trend; if your org runs or depends on online retail platforms, verify your payment page security posture and confirm whether any vendors in your supply chain were among the 100+ compromised sites.
