#!/usr/bin/env python3
"""Enrichment for CuraSec judgments.

Cross-references each item's CVEs with:
  - CISA KEV (known exploited vulnerabilities catalog)
  - EPSS score (FIRST.org exploit prediction)
  - public PoC presence (GitHub repository search)
  - cross-source corroboration (same CVE seen from multiple collected sources)

Every network call degrades to "unavailable" on failure — enrichment must
never abort the pipeline.
"""

import re
import time

import requests

KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
EPSS_URL = "https://api.first.org/data/v1/epss"
GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"
USER_AGENT = "curasec-pipeline/1.0"

CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}", re.IGNORECASE)
MAX_CVES_PER_ITEM = 3
POC_SEARCH_BUDGET = 20   # GitHub search API calls per run (rate-limit guard)
POC_SEARCH_SLEEP = 2.5   # seconds between search calls


def extract_cves(text: str) -> list:
    """Unique, normalized CVE ids found in text (capped per item)."""
    return sorted({m.upper() for m in CVE_RE.findall(text or "")})[:MAX_CVES_PER_ITEM]


class Enricher:
    def __init__(self, github_token: str | None = None, log=print):
        self.log = log
        self._github_headers = {
            "User-Agent": USER_AGENT,
            "Accept": "application/vnd.github+json",
        }
        if github_token:
            self._github_headers["Authorization"] = f"Bearer {github_token}"
        self._kev: set | None = None
        self._kev_failed = False
        self._epss: dict[str, float] = {}
        self._epss_failed = False
        self._poc: dict[str, bool] = {}
        self._poc_budget = POC_SEARCH_BUDGET

    # ------------------------------------------------------------------ KEV

    def kev_set(self) -> set:
        if self._kev is None and not self._kev_failed:
            try:
                resp = requests.get(
                    KEV_URL, headers={"User-Agent": USER_AGENT}, timeout=30
                )
                resp.raise_for_status()
                self._kev = {
                    v.get("cveID", "").upper()
                    for v in resp.json().get("vulnerabilities", [])
                }
                self.log(f"  [enrich] KEV catalog loaded: {len(self._kev)} CVEs")
            except Exception as exc:  # noqa: BLE001
                self._kev_failed = True
                self.log(f"  [enrich] KEV fetch failed ({exc}) — degrading")
        return self._kev or set()

    # ----------------------------------------------------------------- EPSS

    def prefetch_epss(self, cves: list) -> None:
        """One batch call for all CVEs in this run's queue."""
        missing = [c for c in cves if c not in self._epss]
        if not missing or self._epss_failed:
            return
        try:
            # the EPSS API accepts a comma-separated list (well under its 100 cap here)
            resp = requests.get(
                EPSS_URL,
                params={"cve": ",".join(missing[:100])},
                headers={"User-Agent": USER_AGENT},
                timeout=30,
            )
            resp.raise_for_status()
            for row in resp.json().get("data", []):
                self._epss[row["cve"].upper()] = float(row["epss"])
            self.log(f"  [enrich] EPSS scores fetched for {len(missing)} CVEs")
        except Exception as exc:  # noqa: BLE001
            self._epss_failed = True
            self.log(f"  [enrich] EPSS fetch failed ({exc}) — degrading")

    # ------------------------------------------------------------ public PoC

    def has_public_poc(self, cve: str) -> bool | None:
        """True/False from GitHub repo search; None when unavailable (budget/rate)."""
        if cve in self._poc:
            return self._poc[cve]
        if self._poc_budget <= 0:
            return None
        self._poc_budget -= 1
        try:
            resp = requests.get(
                GITHUB_SEARCH_URL,
                params={"q": f'"{cve}" in:name,description,readme', "per_page": 1},
                headers=self._github_headers,
                timeout=15,
            )
            resp.raise_for_status()
            found = resp.json().get("total_count", 0) > 0
            self._poc[cve] = found
            time.sleep(POC_SEARCH_SLEEP)
            return found
        except Exception as exc:  # noqa: BLE001
            self.log(f"  [enrich] PoC search failed for {cve} ({exc})")
            return None

    # -------------------------------------------------------------- assembly

    def signals_line(self, cves: list, cve_sources: dict) -> str:
        """Human-readable enrichment summary fed to the judge and the post."""
        if not cves:
            return ""
        kev = self.kev_set()
        parts = []
        for cve in cves:
            bits = []
            bits.append("CISA KEV: listed" if cve in kev else "CISA KEV: not listed")
            score = self._epss.get(cve)
            bits.append(f"EPSS {score:.2f}" if score is not None else "EPSS n/a")
            poc = self.has_public_poc(cve)
            if poc is True:
                bits.append("public PoC on GitHub")
            elif poc is False:
                bits.append("no public PoC found")
            sources = cve_sources.get(cve, set())
            if len(sources) > 1:
                bits.append(f"reported by {len(sources)} collected sources")
            parts.append(f"{cve} — " + ", ".join(bits))
        return " · ".join(parts)
