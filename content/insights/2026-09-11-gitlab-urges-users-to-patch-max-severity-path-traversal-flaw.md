---
title: "GitLab max-severity path traversal flaw has public PoC on GitHub"
date: 2026-09-11T14:58:57.702490+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["gitlab", "path-traversal", "critical-cve"]
cves: ["CVE-2026-85706"]
source: "https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Max-severity path traversal in GitLab with a public PoC significantly raises exploitation risk even absent a KEV listing — patch all self-hosted GitLab instances to the fixed version immediately and verify no unauthorized file access occurred before the patch window.
- **SOC/IR — Act:** A public PoC for a max-severity GitLab flaw means opportunistic exploitation attempts are likely imminent; hunt for anomalous file-read patterns and path traversal sequences (e.g., ../ chains) in GitLab access logs since the disclosure date.
- **Leader — Plan:** Confirm whether self-hosted GitLab instances exist in the environment and verify engineering teams have prioritized patching within days given the public PoC; no board-level brief warranted yet unless active breach evidence emerges.
- **Signals:** CVE-2026-85706 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
