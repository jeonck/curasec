---
title: "Attackers Hijack Three ccTLD Registries to Forge Google HTTPS Certs"
date: 2026-10-08T17:51:36.071186+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["certificate-hijacking", "pki", "cctld"]
cves: []
source: "https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Audit Certificate Transparency logs (crt.sh) for unauthorized certificates issued against any domains your organization owns in .gh, .sl, or .as TLDs; if hits found, treat as active compromise and revoke/reissue. Broader takeaway: review certificate pinning posture for critical services.
- **SOC/IR — Learn:** Registry-level compromise enabling HTTPS certificate fraud is a novel MITM vector worth understanding, but the summary provides no IOCs, TTPs, or detection signatures to act on today.
- **Leader — Plan:** Determine whether your organization operates services or depends on vendors using .gh, .sl, or .as domains; if so, commission a CT log audit this quarter and confirm no traffic was intercepted. No immediate board action needed unless exposure is confirmed.
