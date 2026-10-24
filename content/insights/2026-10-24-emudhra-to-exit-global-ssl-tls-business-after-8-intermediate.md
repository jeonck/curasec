---
title: "eMudhra Exits SSL/TLS After 8 Intermediate CA Private Keys Recovered"
date: 2026-10-24T14:29:02.695753+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Act"
tags: ["certificate-authority", "pki", "ssl-tls"]
cves: []
source: "https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Eight intermediate CA private keys were actually recovered — any certificate signed by those intermediates should be treated as potentially compromised. Audit your certificate inventory for eMudhra-issued certs and replace them now, before major browsers revoke trust and cause outages.
- **SOC/IR — Plan:** Compromised intermediate CA keys enable forged certificates for MITM attacks. Update TLS inspection rules to flag or alert on eMudhra-signed certificates in your environment, and confirm that CA distrust events are reflected in your trust stores and monitoring.
- **Leader — Act:** A CA with recovered intermediate private keys will face browser distrust, which turns unexpired certificates into outages. Confirm this quarter whether your organization holds any eMudhra-issued certificates and initiate replacement before the distrust wave hits — and check if any vendors in your supply chain rely on them.
