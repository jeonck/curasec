---
title: "Teams IT-Support Vishing + AD CS Abuse Leads to Domain Compromise"
date: 2026-11-02T20:44:36.815553+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["active-directory", "social-engineering", "microsoft-teams"]
cves: []
source: "https://thehackernews.com/2026/11/attackers-pose-as-it-support-on.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Confirmed active exploitation of overly permissive AD CS certificate templates to mint privileged-account certs — no KEV/PoC signal, but real intrusions warrant a scheduled audit. Run Certify or PSPKIAudit against your AD CS deployment to identify ESC-class misconfigurations and tighten enrollment permissions on certificate templates.
- **SOC/IR — Act:** Two confirmed intrusions with actionable detection surface: hunt for anomalous AD CS certificate issuance events (Windows Event IDs 4886/4887) for privileged accounts since October, and review Microsoft Teams external-user remote-control session logs for vishing patterns. TTPs map to ATT&CK T1649 (Steal or Forge Authentication Certificates).
- **Leader — Plan:** Microsoft-confirmed intrusions via Teams impersonation plus identity-infrastructure abuse are a prompt to review external Teams access policy and schedule an AD CS configuration assessment — neither is urgent enough for a board brief today, but both belong on the Q4 identity security roadmap.
