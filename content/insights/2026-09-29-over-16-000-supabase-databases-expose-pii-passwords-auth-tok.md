---
title: "16,000+ Supabase databases expose PII, passwords, auth tokens"
date: 2026-09-29T16:53:02.010350+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["misconfiguration", "data-exposure", "supabase"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/misconfigured-supabase-apps-expose-data-in-over-16-000-databases/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** If you use Supabase, audit your project's Row Level Security (RLS) settings immediately and verify that no tables with PII, credentials, or tokens are publicly readable; enable RLS on all sensitive tables and rotate any exposed tokens.
- **SOC/IR — Plan:** No active exploitation signals yet, but bulk exposed auth tokens are high-value targets — plan to add monitoring for anomalous API access patterns against Supabase-backed services and check whether any internal apps use Supabase with public table access.
- **Leader — Plan:** If your organization builds on Supabase, task engineering to audit RLS configurations this quarter; the scale (16,000+ databases) suggests broad industry exposure and may generate customer or auditor questions about your own posture.
