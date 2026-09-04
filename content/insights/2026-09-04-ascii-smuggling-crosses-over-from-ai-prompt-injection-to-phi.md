---
title: "ASCII smuggling technique migrates from AI prompt injection to phishing evasion"
date: 2026-09-04T14:56:27.274495+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["phishing", "evasion-technique", "email-security"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Plan:** Audit email security gateway and content-inspection rules to detect invisible Unicode characters used to bypass filters; evaluate whether your email platform has updated signatures for this evasion class.
- **SOC/IR — Act:** Build or tune detection rules to flag emails containing invisible/tag Unicode codepoints (U+E0000 range); hunt for recent phishing lures that may have bypassed filters using this technique since the evasion method is now publicly documented.
- **Leader — Learn:** A novel phishing evasion technique is gaining traction; no board-level action needed now, but awareness is useful context for the next email security or AI-risk discussion.
