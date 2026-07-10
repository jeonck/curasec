# Persona: Security Leader

## Who this is
The person accountable for security posture and risk, not hands-on-keyboard.
Typical titles: CISO, Head of Security, Security Director, or the engineering
manager who owns security at a smaller company. They allocate budget and
people, report risk upward, and answer to auditors, customers, and the board.

## Environment assumptions
- Accountable to at least one framework: SOC 2, ISO 27001, PCI DSS, HIPAA,
  or FedRAMP; fields security questionnaires from enterprise customers.
- Manages vendor risk — a breach at a SaaS vendor their company uses is their
  problem even with zero technical involvement.
- Subject to disclosure regimes (SEC 4-day material-incident rule, GDPR 72-hour
  notification) and watching regulatory movement (EU CRA, state privacy laws).
- Their scarce resources are headcount, budget, and board attention.

## What they must decide from each item
"Does this change my risk register, require a statement to leadership/customers,
affect a vendor we depend on, or shift where I should spend budget?"

## Verdict criteria
- **Act** — events demanding same-week leadership action: breach or compromise
  at a widely-used vendor (check exposure, ask vendor for attestations), a
  regulation taking effect with a near deadline, an incident in their sector
  likely to trigger board or customer questions, or a systemic event (major
  supply-chain compromise) requiring an internal exposure assessment. Name the
  action: "confirm whether we use X and request their incident report",
  "brief leadership before they read it in the news".
- **Plan** — quarter-horizon strategy inputs: proposed regulation moving toward
  adoption, insurance/audit requirement shifts, a technology trend (e.g. AI
  agents in the enterprise) that needs a policy before it needs a control,
  budget-relevant market moves (vendor acquisitions, EOL announcements).
- **Learn** — industry reports, breach post-mortems with governance lessons,
  benchmarking data useful for future board decks.
- **Skip** — individual CVEs (their teams handle those — a CVE only reaches
  this persona as Act when it is a named, systemic, board-question-level event
  like Log4Shell), deep technical exploit analysis, tool release notes.

## What they do NOT care about (do not inflate verdicts for these)
- Technical detail below the "what do I tell the board / auditor / customer"
  altitude.
- Routine patch cycles and detection engineering minutiae.
- Vendor marketing dressed as threat research, unless the underlying data is
  independently corroborated.
