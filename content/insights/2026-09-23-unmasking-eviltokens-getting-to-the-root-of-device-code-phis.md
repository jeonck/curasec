---
title: "EvilTokens PhaaS disrupted after enabling AI-assisted device code phishing"
date: 2026-09-23T15:27:03.663698+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["device-code-phishing", "token-theft", "phaas"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Plan:** Device code phishing industrialization is a signal to audit whether OAuth device code flow is enabled in your Entra ID / identity provider — restrict it to only necessary clients and enforce conditional access policies that block token reuse from unexpected locations.
- **SOC/IR — Act:** EvilTokens was actively stealing tokens at scale via device code flow; hunt for anomalous device code authentication requests in your identity logs (Entra Sign-in logs, unified audit log) since at least early 2026, and tune detections for device code grants issued to unfamiliar device types or followed by token use from new geographies.
- **Leader — Learn:** The Microsoft DCU-led disruption illustrates how AI-assisted PhaaS platforms are lowering the bar for credential and token theft campaigns; useful context for the next board or risk-committee briefing on evolving phishing sophistication.
