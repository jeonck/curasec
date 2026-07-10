# Persona: Cloud/AppSec Engineer

## Who this is
A hands-on engineer responsible for the security of cloud infrastructure and
application code. Typical titles: Security Engineer, AppSec Engineer, Platform
Engineer with security duties, DevSecOps. They ship and patch systems directly —
they have root/admin on something that matters.

## Environment assumptions
- Runs workloads on at least one major cloud (AWS/Azure/GCP), often Kubernetes.
- Owns a dependency tree: language package managers (npm/pip/Go/Maven),
  container base images, IaC (Terraform), CI/CD pipelines.
- Uses common edge/infra software that is frequently exploited: reverse proxies,
  VPN appliances, CI runners, artifact registries, identity providers (OIDC/SAML).
- Has a patch window measured in days for critical issues, weeks for routine.

## What they must decide from each item
"Does this touch software or configuration I run, and do I need to patch,
reconfigure, or audit something — and how fast?"

## Verdict criteria
- **Act** — a vulnerability or misconfiguration in software this persona
  plausibly runs, where exploitation is practical now. Signals: CISA KEV listed,
  public PoC exists, EPSS high (≥ ~0.5), actively exploited per multiple sources,
  or a supply-chain compromise in a popular package/registry. The verdict must
  name the concrete action: "patch X to version Y", "rotate these credentials",
  "audit for this IOC in build logs".
- **Plan** — real exposure but no exploitation pressure: patch available and no
  PoC/KEV; a deprecation or breaking security change with a deadline (e.g. cloud
  provider disabling a legacy auth method); a new hardening feature worth
  adopting this quarter.
- **Learn** — new attack technique or research that changes how they should
  design systems, but requires no change to running systems today. Novel
  vulnerability classes, interesting post-mortems, new tooling to evaluate.
- **Skip** — vendor marketing, vulnerabilities in niche/regional software they
  almost certainly don't run, re-announcements of old news, compliance/policy
  items with no engineering surface.

## What they do NOT care about (do not inflate verdicts for these)
- Pure policy/regulation news with no technical control to implement.
- Threat-actor attribution drama without IOCs or affected-software specifics.
- Consumer-security or end-user scam stories.
