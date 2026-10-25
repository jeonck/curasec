---
title: "Public RCE toolkit targets all PHP versions via CVE-2026-109619/109618"
date: 2026-10-25T14:56:19.493230+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["php-rce", "exploit-toolkit", "cve"]
cves: ["CVE-2026-109619"]
source: "https://github.com/aarsaputra/php2shell"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Act:** EPSS 1.00 plus a public, actively maintained exploit toolkit covering PHP 5.4–8.4.26 means exploitation pressure is immediate. Patch PHP to the latest release beyond 8.4.26 and audit any internet-exposed PHP applications for successful exploitation attempts.
- **SOC/IR — Act:** The toolkit's JA3 impersonation capability specifically evades TLS fingerprint-based detections, requiring tuning beyond standard signatures. Hunt for unauthenticated HTTP sequences matching this RCE chain against PHP endpoints dating back to the toolkit's first appearance on GitHub.
- **Leader — Act:** A public exploit kit with EPSS 1.00 covering the entire PHP version tree is a systemic exposure on par with Log4Shell in breadth. Confirm this week whether PHP is present across your estate and that engineering has emergency-patched it; be prepared to brief leadership if a breach follows.
- **Signals:** CVE-2026-109619 — CISA KEV: not listed, EPSS 1.00, public PoC on GitHub, reported by 2 collected sources
