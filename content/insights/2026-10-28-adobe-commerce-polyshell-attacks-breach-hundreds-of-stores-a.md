---
title: "Adobe Commerce PolyShell attacks exploiting KEV-listed RCE flaw"
date: 2026-10-28T17:09:30.637292+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["adobe-commerce", "active-exploitation", "supply-chain"]
cves: ["CVE-2026-111497"]
source: "https://thehackernews.com/2026/10/adobe-commerce-polyshell-attacks-breach.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** CVE-2026-111497 is CISA KEV-listed with EPSS 0.88 and a public PoC — patch Adobe Commerce/Magento to the latest vendor-released version immediately, and audit web server logs for PolyShell indicators and anomalous Brotli-encoded traffic.
- **SOC/IR — Act:** Hundreds of stores are actively compromised; hunt for PolyShell webshell artifacts and Brotli-encoded C2 traffic in web access logs since KEV listing date, and tune WAF/SIEM rules to flag unusual POST patterns on Commerce endpoints.
- **Leader — Plan:** If your org runs Adobe Commerce or Magento storefronts — or relies on a third-party e-commerce vendor that does — confirm patching status and request a written attestation; breach of payment pages may trigger PCI DSS incident-notification obligations.
- **Signals:** CVE-2026-111497 — CISA KEV: listed, EPSS 0.88, public PoC on GitHub
