---
title: "FBI: North Korea Stole $400M Crypto via Deepfake Video Call Social Engineering"
date: 2026-11-14T17:01:43.117086+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["dprk", "social-engineering", "cryptocurrency"]
cves: []
source: "https://thehackernews.com/2026/11/fbi-says-north-korean-hackers-stole.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No software vulnerability or patch action here — this is a social engineering campaign exploiting deepfake video calls. Worth understanding as it invalidates the common 'verify via video' out-of-band confirmation pattern used in some CI/CD and privileged-access workflows.
- **SOC/IR — Learn:** DPRK FaceStealer campaign TTPs (deepfake-assisted impersonation in video calls) are worth filing for actor profiling, but the summary provides no IOCs or ATT&CK-mappable specifics to hunt or detect against.
- **Leader — Plan:** A $400M theft attributed to DPRK and backed by a coordinated FBI action signals a mature, scalable social engineering capability that defeats video-call identity verification — review whether employee and vendor onboarding processes rely on that control, and schedule an update to social engineering awareness training.
