# Persona: SOC/IR Analyst

## Who this is
An analyst in a security operations center or incident-response team. They
triage alerts, hunt threats, and respond to intrusions. Typical titles: SOC
Analyst (T1–T3), Threat Hunter, Incident Responder, Detection Engineer.

## Environment assumptions
- Operates a SIEM (Splunk/Sentinel/Elastic) and an EDR (CrowdStrike/Defender/
  SentinelOne); writes or tunes detection rules (Sigma/KQL/SPL).
- Consumes threat intel feeds; tracks named actors and campaigns that target
  their sector.
- Defends a mixed estate: Windows-heavy endpoints, some Linux servers, M365 or
  Google Workspace, VPN/edge appliances they don't control but must watch.
- Measured on detection coverage and response time, not patching (patching is
  the Engineer's job — verdicts should not tell this persona to patch).

## What they must decide from each item
"Do I need to write/tune a detection, run a hunt, sweep for IOCs, or brief the
on-call — and is there enough technical detail here to actually do that?"

## Verdict criteria
- **Act** — active exploitation with actionable detection surface: published
  IOCs, TTPs mapped or mappable to ATT&CK, exploitation of an edge device where
  compromise precedes patching (assume-breach sweep needed), or a campaign
  targeting software common in enterprise estates. The verdict must name the
  action: "sweep for these IOCs", "hunt for this behavior since <date>",
  "enable/tune this detection".
- **Plan** — new TTPs or tooling worth building detections for this quarter:
  a new persistence/evasion technique with public analysis, a red-team tool
  gaining adoption, log sources they should start collecting.
- **Learn** — actor profiles, campaign retrospectives, or research that improves
  triage judgment but yields no immediate detection work.
- **Skip** — vulnerability announcements with no exploitation and no detection
  angle (that's Engineer territory), vendor product launches, policy news.

## What they do NOT care about (do not inflate verdicts for these)
- Patch-available-no-exploitation CVE noise — for them that is Skip or at most
  Learn, even when the Engineer verdict is Act/Plan.
- Compliance frameworks and governance news.
- Consumer-facing scams unless the lure technique is novel enough to hunt for.
