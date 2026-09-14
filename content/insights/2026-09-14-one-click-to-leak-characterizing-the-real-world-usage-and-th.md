---
title: "One-Click-to-Leak: Trust Defects in MNO-Based SSO Websites"
date: 2026-09-14T18:03:45.849563+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["single-sign-on", "identity", "authentication"]
cves: []
source: "https://arxiv.org/abs/2609.12037"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** Academic research exposing trust hijacking and credential leakage flaws in carrier-based SSO; the finding that 69.4% of MSSO sites expose developer credentials is a useful design caution for any team integrating telecom-backed identity flows, though MSSO is rare in typical US cloud stacks.
- **SOC/IR — Learn:** The One-Click-to-Leak attack class (phone number exfiltration via single page visit) is a novel auth-layer technique worth filing for threat modeling, but the paper provides no IOCs, ATT&CK mappings, or detection rules to act on today.
- **Leader — Skip**
