---
title: "SANS FOR577 Update: Forensic Scripts for AI Coding Assistant Activity"
date: 2026-10-08T17:51:36.071186+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["ai-agents", "forensics", "incident-response"]
cves: []
source: "https://isc.sans.edu/diary/rss/33410"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** Useful awareness that AI coding assistants (Claude Code, Copilot, Cursor, etc.) leave recoverable chat history and artifacts; relevant for understanding the forensic footprint of tools running in your dev environment, but no patch or config change needed.
- **SOC/IR — Plan:** New forensic scripts targeting 8 popular AI coding assistants are worth incorporating into IR playbooks — when investigating developer workstations, you can now systematically locate and review AI agent session history to reconstruct what the agent did or was instructed to do.
- **Leader — Skip**
