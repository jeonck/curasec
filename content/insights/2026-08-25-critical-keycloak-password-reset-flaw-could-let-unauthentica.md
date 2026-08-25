---
title: "Critical Keycloak Password Reset Flaw Enables Unauthenticated Account Takeover"
date: 2026-08-25T11:39:54.623847+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["keycloak", "account-takeover", "identity-management"]
cves: ["CVE-2026-18963"]
source: "https://thehackernews.com/2026/08/critical-keycloak-password-reset-flaw.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Keycloak is a common IAM component in Kubernetes and cloud stacks; a public PoC for unauthenticated account takeover makes exploitation practical regardless of the low EPSS. Patch Keycloak to the fixed release immediately and audit authentication logs for anomalous password-reset activity since disclosure.
- **SOC/IR — Plan:** No active exploitation or IOCs yet, but a public PoC raises the likelihood of opportunistic abuse soon. Build or tune a detection for high-volume or cross-account password-reset requests against Keycloak endpoints so you are ready to alert when attempts begin.
- **Leader — Plan:** An unauthenticated takeover flaw in an IAM server is high-blast-radius if exploited — it could affect all accounts in the realm. Confirm your engineering team has scheduled the Keycloak patch and verify whether any customer-facing SSO flows depend on it.
- **Signals:** CVE-2026-18963 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub
