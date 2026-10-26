---
title: "KnotScryer: Detecting Insecure AI Agent Skill Composition via Flow Graphs"
date: 2026-10-26T18:39:19.902923+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Learn"
tags: ["ai-agents", "skill-composition", "capability-flow"]
cves: []
source: "https://arxiv.org/abs/2610.32155"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** Novel finding that combining individually benign AI agent skills can create security-violation chains at runtime, a gap current malicious-skill scanners miss. No immediate patch exists; architects building agent platforms with third-party skill ecosystems should review orchestration trust boundaries in their design.
- **SOC/IR — Skip**
- **Leader — Learn:** Academic research revealing a design-time risk in AI agent skill marketplaces — relevant context if your organization is evaluating or deploying agentic AI platforms, as vetting individual skills may be insufficient without compositional analysis.
