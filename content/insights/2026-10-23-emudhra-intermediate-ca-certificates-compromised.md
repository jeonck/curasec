---
title: "eMudhra Intermediate CA Private Keys Compromised, MitM Risk"
date: 2026-10-23T15:44:28.729261+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Act"
tags: ["pki-compromise", "certificate-authority", "mitm"]
cves: []
source: "https://unit42.paloaltonetworks.com/emudhra-certificate-compromise/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Act:** Audit your certificate inventory now for any eMudhra-issued TLS certs; any certificate signed by one of the eight compromised intermediates must be replaced and the intermediates should be distrusted in your trust stores.
- **SOC/IR — Plan:** No IOCs are published yet, but build or tune detections for certificate validation failures and unexpected CA chain presentations that could indicate MitM use of fraudulently issued eMudhra certs; add eMudhra intermediate serial numbers to watchlists once revocation details are public.
- **Leader — Act:** Confirm with your security team whether any customer-facing or internal services rely on eMudhra-issued certificates; if so, request remediation status and prepare to notify affected parties given the MitM interception risk this poses to encrypted communications.
