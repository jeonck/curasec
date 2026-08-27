---
title: "Auditing Admin Rights in Microsoft Entra ID"
date: 2026-08-27T21:01:55.123618+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["entra-id", "identity", "least-privilege"]
cves: []
source: "https://isc.sans.edu/diary/rss/33284"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Plan:** Run an Entra ID privileged role audit this quarter: export current role assignments, flag stale accounts from departed staff, and scope down over-provisioned roles (e.g. helpdesk accounts holding Global Admin) to least-privilege equivalents.
- **SOC/IR — Learn:** Useful framing for why excessive Entra admin roles expand blast radius during identity-based intrusions, but no new TTPs, IOCs, or detection content here.
- **Leader — Plan:** Excess admin accounts are a recurring audit finding (CIS Control 4); scheduling a formal privileged-access review and documenting results strengthens posture for SOC 2 / ISO 27001 auditors asking exactly this question.
