---
title: "keyv/cacheable npm Worm: Revoking Token Arms the Payload"
date: 2026-08-06T13:03:19.955458+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["supply-chain", "npm", "incident-response"]
cves: []
source: "https://isc.sans.edu/diary/rss/33218"
source_name: "SANS ISC"
status: "archived"
---
- **Engineer — Act:** Active supply-chain compromise in the npm keyv/cacheable packages — audit all build hosts for execution of these packages immediately and preserve forensic state before touching credentials, because revoking the stolen token is what triggers the malicious payload; follow a forensics-first sequence before any rotation.
- **SOC/IR — Act:** Ongoing supply-chain worm with a novel IR wrinkle: token revocation activates the payload, which inverts standard response playbooks — sweep CI/CD build logs for keyv/cacheable execution since Aug 4, and update incident runbooks to gate credential rotation on payload-trigger analysis.
- **Leader — Plan:** Active npm supply-chain compromise affecting keyv/cacheable; confirm whether internal engineering teams depend on these packages and brief engineering leadership on the non-standard response sequence before teams instinctively rotate credentials and worsen the incident.
