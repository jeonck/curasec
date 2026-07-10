# CuraSec

**Security intelligence with actionable verdicts.** Every day at 11:00 UTC this
pipeline collects new items from RSS / Hacker News / Reddit / GitHub, enriches
each with exploitation signals (CISA KEV, EPSS, public PoC, cross-source
corroboration), and has Claude judge it **independently for three practitioner
personas** — then publishes everything that matters to
[curasec.metacog.co.kr](https://curasec.metacog.co.kr/) with an RSS feed.

## Verdict system

Each item gets one verdict *per persona*, e.g. `Engineer: Act / SOC: Plan / Leader: Skip`:

| Verdict | Meaning | Published |
|---|---|---|
| 🔥 **Act** | do or check something now (KEV-listed, active exploitation, urgent patch) | yes |
| 📌 **Plan** | review within the quarter (patch cycles, policy shifts, new techniques) | yes |
| 📚 **Learn** | worth knowing, no action needed | yes |
| **Skip** | marketing / duplicate / irrelevant | **only if Skip for all 3 personas → not published** |

The personas (the heart of judgment quality — edit these to change verdicts):

- [`personas/engineer.md`](personas/engineer.md) — Cloud/AppSec Engineer: patching, config, dependencies
- [`personas/soc.md`](personas/soc.md) — SOC/IR Analyst: detections, IOC sweeps, hunting
- [`personas/leader.md`](personas/leader.md) — Security Leader: policy, vendor risk, board communication

## Structure

```
.
├── context.md                  # channel-wide judgment rules (Skip rules, evidence discipline)
├── personas/                   # per-persona verdict criteria (fed into every judgment)
├── feeds.yaml                  # daily sources (all URLs HTTP-200 verified)
├── feeds-weekly.yaml           # weekly sources (arXiv cs.CR)
├── pipeline/
│   ├── collect.py              # collect → enrich → judge → write posts
│   ├── enrich.py               # CISA KEV / EPSS / public PoC / corroboration
│   ├── expire.py               # auto-archive: Learn >14d, others >30d
│   ├── processed.json          # judged-URL record (dedupe, 90-day retention)
│   └── done.sh                 # manual archive helper
├── content/insights/           # generated posts
├── content/about.md            # methodology + trust principles (AI disclosure)
├── content/corrections.md      # public corrections log
├── layouts/                    # self-contained Hugo layouts (no theme)
└── .github/workflows/
    ├── daily.yml               # 11:00 UTC cron: collect + judge + deploy
    ├── weekly.yml              # Monday 12:00 UTC: research sources
    └── control.yml             # pause / resume collection
```

## Setup

1. **Judge auth** — one of the two (repo Settings → Secrets and variables → Actions):
   - **Recommended: Claude subscription (Pro/Max)** — run `claude setup-token`
     locally, complete browser auth, then register the **final printed token**
     (`sk-ant-oat01-...`, *not* the browser auth code) as the
     `CLAUDE_CODE_OAUTH_TOKEN` secret. No API credits needed.
   - **Alternative: API key** — register `ANTHROPIC_API_KEY` (used only when
     the OAuth token secret is absent).
2. **Pages** — Settings → Pages → Source: **GitHub Actions**
3. **First run** — Actions tab → `Daily Curation` → Run workflow
   (manual runs deploy even with zero new items)

Then it runs daily at 11:00 UTC (06:00–07:00 US East) with no human in the loop.

## Failure handling (designed for zero-touch operation)

- **A failed judge step opens a GitHub issue automatically** (plus the normal
  Actions failure email) — the pipeline never dies silently.
- Fatal auth/credit errors abort fast; judgments completed before the abort are
  still committed and deployed. Unprocessed items retry the next day.
- Every collection source is error-isolated — one broken feed cannot kill a run.
- Zero-new-item days skip both commit and deploy (no empty publishes).
- Pause/resume: Actions tab → **Pipeline Control** (or `pipeline/pause.sh` /
  `resume.sh`) — state is a `.collect-paused` marker file in the repo.

## Local run

```bash
pip install -r pipeline/requirements.txt

# uses your local claude CLI login (subscription auth, no API key needed)
MAX_ITEMS=5 python pipeline/collect.py --dry-run

# real run + preview
python pipeline/collect.py
hugo server        # → http://localhost:1313/curasec/
```

Env knobs: `JUDGE_BACKEND` (`claude-code`|`api`), `CLAUDE_MODEL`
(default `claude-sonnet-4-6`), `MAX_ITEMS` (30), `FEEDS_FILE`, `FRESH_HOURS`,
`GITHUB_TOKEN` (search rate-limit relief).

## Operating routine

**First 30 days (trust-building period)** — skim the day's verdicts once daily
(~5 min, published 20:00 KST). Fix a bad verdict by editing the post's front
matter + note, and log confirmed errors in
[content/corrections.md](content/corrections.md). If verdicts consistently miss,
edit the persona files — not the pipeline.

**After day 30** — fully automatic. Weekly skim optional.

**Day 90 — continue/stop decision** — evaluate RSS subscribers and return
visits per PLAN.md.

## Known constraints

- **Reddit**: cloud IPs (GitHub Actions) often get 403 from the `.json` API.
  Error isolation keeps other sources healthy.
- **hnrss.org**: occasional 502 — that run collects 0 from HN, self-heals next run.
- **GitHub Search**: `created:>N days` + star filters return 0 on many days (normal).
- **Enrichment degradation**: KEV/EPSS/PoC lookups that fail degrade to
  "unavailable" in the signals — never fatal.
- **OAuth token expiry**: re-run `claude setup-token`, update the secret, close
  the auto-opened issue.

## Trust principles

Public channel, automated judgments — so: AI disclosure on every page, evidence
required on every verdict, a public corrections log, and a 30-day human review
period at launch. See [About](https://curasec.metacog.co.kr/about/).
