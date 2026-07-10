---
title: "About CuraSec"
---
## What this is

CuraSec is a daily, AI-curated security intelligence channel. Most security
news tells you *what happened*; CuraSec tells you **who should do what, now** —
every item gets three independent verdicts, one per practitioner persona:

| Persona | Judged on |
|---|---|
| **Engineer** (Cloud/AppSec) | patching, configuration changes, dependency impact |
| **SOC/IR** (Analyst/Hunter) | detections, IOC sweeps, hunting priorities |
| **Leader** (CISO/Security Director) | policy, vendor risk, board/customer communication |

## The verdicts

| Verdict | Meaning |
|---|---|
| **Act** | do or check something now (KEV-listed, actively exploited, urgent) |
| **Plan** | review within the quarter (patch cycles, policy shifts, new techniques) |
| **Learn** | worth knowing, no action required |
| **Skip** | not published — marketing, duplicates, irrelevant items |

Items judged Skip for *all three* personas are never published.

## How verdicts are made

1. **Collection** — RSS (CISA, Google TI, Microsoft, CrowdStrike, Unit 42,
   Krebs, The Hacker News, BleepingComputer, SANS ISC and more), Hacker News,
   Reddit, and GitHub, daily at 11:00 UTC. A weekly batch adds arXiv cs.CR.
2. **Enrichment** — every CVE is cross-referenced against the CISA KEV catalog,
   its EPSS score, public PoC presence on GitHub, and whether multiple
   independent sources reported it in the same window.
3. **Judgment** — Claude (Anthropic) judges each item against
   [context.md](https://github.com/jeonck/curasec/blob/main/context.md) and the
   [persona definitions](https://github.com/jeonck/curasec/tree/main/personas),
   producing a verdict and a 1–2 sentence evidence-based note per persona.

## Trust principles

- **AI disclosure** — every post and page states that curation and verdicts are
  automated. There is no human editor writing these judgments.
- **Evidence required** — every non-Skip verdict carries its reasoning and the
  enrichment signals it was based on.
- **Corrections log** — confirmed misjudgments are recorded on the
  [corrections page](../corrections/), not silently edited.
- **Human review period** — during the channel's first 30 days, a human reviews
  published verdicts daily and corrects errors.

Verdicts are starting points, not authoritative guidance — always verify
against the original source before acting.

## Feedback

Bad verdict? Broken source? Open an issue on
[GitHub](https://github.com/jeonck/curasec/issues).
