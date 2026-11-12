---
title: "Fireworks AI breach exposes Notion and downstream customer data"
date: 2026-11-12T18:52:40.662404+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Act"
tags: ["vendor-breach", "ai-supply-chain", "third-party-risk"]
cves: []
source: "https://www.notion.com/help/security-incident-involving-a-third-party-ai-vendor"
source_name: "HN (security)"
status: "active"
---
- **Engineer — Plan:** If Fireworks AI is used in any AI pipeline or if your team uses Notion, audit what data was accessible to Fireworks AI and monitor Notion's incident disclosure page for updated scope and affected data types.
- **SOC/IR — Plan:** No IOCs are available yet, but if the organization uses Notion, begin tracking this incident for follow-on indicators; prepare a hunt query template to deploy once Fireworks AI or Notion publish technical details.
- **Leader — Act:** Notion is widely used across enterprises — confirm whether your organization uses it, request Notion's incident report and attestation on what customer data was exposed to Fireworks AI, and brief leadership before they encounter this in the news.
