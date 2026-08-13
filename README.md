# Suboot

A federated clinical-evidence network that lets global pharma companies buy real-world patient evidence from South Asian hospitals — while no patient data ever leaves the hospital.

## Problem

Global regulators (FDA Diversity Action Plans under FDORA, EMA guidance) now require pharma to include diverse populations in clinical trials. South Asia carries roughly a quarter of the world's disease burden but supplies under 5% of trial participants. The data exists in Pakistani hospitals; what's missing is a way to prove it is real, consented, and computed on genuine patients — without moving protected health information (PHI).

## Solution

Suboot is a federated evidence platform:

- **Federated compute:** pharma uploads an analysis query, not data. The query runs inside each hospital's environment.
- **Local-language structuration:** an LLM pipeline converts unstructured Urdu / Roman-Urdu / English clinical notes into standard OMOP data structures on-site.
- **Privacy:** only differentially-private aggregate statistics leave the hospital.
- **Provenance:** every query, consent, and result is written to an append-only audit ledger with zero-knowledge verification, producing a tamper-evident "evidence receipt" the buyer pays for.

No PHI ever moves — that is the legal and trust unlock.

## Documents

- `NIC_Cohort6_Suboot_Application.md` — full application draft (problem, solution, competition, market, risks)

## Status

Idea stage (pre-revenue). Concept, architecture, and market research complete. MVP prototype build in progress.
