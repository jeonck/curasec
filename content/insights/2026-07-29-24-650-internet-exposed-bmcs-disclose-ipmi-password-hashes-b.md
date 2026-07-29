---
title: "24,650 Internet-Exposed BMCs Leak IPMI Password Hashes Pre-Auth"
date: 2026-07-29T13:07:14.832066+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["bmc-ipmi", "credential-exposure", "infrastructure-security"]
cves: []
source: "https://thehackernews.com/2026/07/24650-internet-exposed-bmcs-disclose.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** The IPMI RAKP pre-auth hash disclosure flaw is a known long-standing weakness, but this research quantifies how many organizations still expose BMC interfaces directly to the internet. Audit all BMC/IPMI management interfaces for internet reachability and enforce firewall or out-of-band network isolation; rotate IPMI credentials on any system that may have been exposed.
- **SOC/IR — Learn:** No active exploitation campaign, IOCs, or ATT&CK-mappable TTPs are provided; this is a research enumeration finding. File as context for what attackers can target on internet-facing server management planes, but there is nothing actionable to hunt or detect today.
- **Leader — Learn:** A research finding showing widespread internet exposure of server management interfaces — useful benchmark data for a future board deck on infrastructure hygiene, but no breach, vendor incident, or regulatory trigger requires leadership action now.
