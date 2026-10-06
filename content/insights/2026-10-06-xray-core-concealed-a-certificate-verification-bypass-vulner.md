---
title: "Xray-core concealed TLS certificate verification bypass flaw"
date: 2026-10-06T17:10:43.586006+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["certificate-bypass", "proxy-security", "supply-chain"]
cves: []
source: "https://github.com/net4people/bbs/issues/672"
source_name: "HN (vulnerability)"
status: "active"
---
- **Engineer — Learn:** Xray-core is a niche censorship-circumvention proxy used by some as a tunneling layer; if it is in your stack, audit for MITM exposure and check for a patched release. The deliberate concealment of this flaw is a useful signal when evaluating trust in open-source proxy tooling.
- **SOC/IR — Skip**
- **Leader — Skip**
