---
title: "FBI Probes Service Selling 153M+ Driver's Licenses from ID Verification Breach"
date: 2026-09-02T15:05:08.783541+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Act"
tags: ["data-breach", "identity-theft", "vendor-risk"]
cves: []
source: "https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/"
source_name: "Krebs on Security"
status: "active"
---
- **Engineer — Plan:** If your platform uses a third-party identity verification or KYC service — particularly one based in Louisiana — audit that integration and check whether user-submitted ID scans are in scope; no patch action applies, but vendor contract and data-handling review is warranted this quarter.
- **SOC/IR — Learn:** 153M+ stolen driver's licenses will likely fuel account-takeover and synthetic-identity fraud campaigns; no IOCs or TTPs are published yet, but flag for future hunting context once the affected vendor is named publicly.
- **Leader — Act:** Confirm this week whether your organization uses the implicated Louisiana-based identity verification vendor and request an incident attestation; the scale of this exposure is likely to generate customer and board questions before the week is out.
