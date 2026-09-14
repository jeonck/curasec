---
title: "Research: AI Agent Skill Registries Miss Runtime Permission Gaps"
date: 2026-09-14T18:03:45.849563+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["ai-agents", "skill-registry", "runtime-governance"]
cves: []
source: "https://arxiv.org/abs/2609.12001"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** Academic research finding that skill scanners answer 'is this malicious?' but not 'is this action permitted right now?' — 34.7% of sandbox-executed commands carried consequences absent from documentation. Worth reviewing if your team is building or consuming agent skill registries, but no patch or config action today.
- **SOC/IR — Learn:** No IOCs or ATT&CK-mapped TTPs, but the finding that 34.7% of agent-executed commands have undocumented consequence classes could inform future monitoring strategy for AI agent activity logging in your environment.
- **Leader — Learn:** Reproducible measurement shows skills passing all scanners can still violate CIS Control 2.7 and NIST CM-11 — a governance gap relevant to AI agent policy discussions, but no vendor breach or regulatory deadline demands action this week.
