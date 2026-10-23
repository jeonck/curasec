---
title: "PHP 5.4–8.1 EOL RCE patches released (CVE-2026-109618/109619)"
date: 2026-10-23T15:44:28.729261+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["php", "rce", "end-of-life"]
cves: ["CVE-2026-109618", "CVE-2026-109619"]
source: "https://github.com/Anton-Barinov/php2shell-patches"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Plan:** Public PoCs exist for two RCE flaws in EOL PHP affecting WordPress, OpenCart, and similar stacks, but EPSS scores (0.12 / 0.06) and no KEV listing mean immediate emergency patching isn't warranted. Audit your fleet for EOL PHP 5.4–8.1; prioritize upgrading to a supported PHP release, or apply these community backport patches as a temporary stopgap for systems that can't migrate quickly.
- **SOC/IR — Learn:** No active exploitation campaign or IOCs are reported, so there's no hunt to run today. The published PoCs document how PHP file-upload progress-bar handling can be abused for RCE, which is worth reviewing to inform or validate any existing detection rules for web shell drops via file upload on PHP applications.
- **Leader — Skip**
- **Signals:** CVE-2026-109618 — CISA KEV: not listed, EPSS 0.12, public PoC on GitHub, reported by 5 collected sources · CVE-2026-109619 — CISA KEV: not listed, EPSS 0.06, public PoC on GitHub, reported by 5 collected sources
