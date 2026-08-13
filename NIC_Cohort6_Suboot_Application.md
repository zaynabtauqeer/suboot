# NIC Islamabad — Cohort 6 Incubation Application

**Startup:** Suboot
**Track:** Health Tech (primary) + Deep Tech (engine)
**Status:** Pre-revenue, MVP in build — submitted by a solo, technical founder

> **BEFORE YOU SUBMIT:** Verify the live deadline at https://nicislamabad.com/apply-now
> Replace every `[PLACEHOLDER]` before submitting. Do NOT submit with placeholders left in.

---

## SECTION A — APPLICATION FORM ANSWERS (copy-paste ready)

### A1. Startup Name
**Suboot** — from Urdu *ثبوت*, "proof." The company sells proof.

### A2. One-Liner Elevator Pitch
> Suboot lets the world's largest pharma companies buy real-world clinical evidence from South Asian hospitals — with cryptographic proof of authenticity — while not a single patient record ever leaves the building.

### A3. Which Vertical & Why
- **Primary: Health Tech Track** — hospital pilots, partner anonymized datasets, DRAP/medical-director mentorship, and privacy-law curriculum are exactly the infrastructure this startup needs.
- **Secondary engine: Deep Tech Track** — the product is built on **federated machine learning + a distributed consensus ledger + custom LLM routing**, three of the four Deep Tech focus areas.
- This is the only concept in this application pool that structurally requires *both* verticals.

### A4. The Problem
1. **Global pharma has a forced, unfixable shortage:** Regulators now *mandate* diversity. The FDA (under FDORA) requires Diversity Action Plans for Phase III trials; the EMA follows. But South Asia carries roughly **a quarter of the world's disease burden** and supplies **under 5% of global clinical-trial participants** — with unique genetics, diets, and drug-metabolism profiles pharma cannot source anywhere else. Recruitment failure already delays ~80% of trials (each day ≈ millions of dollars). The global real-world-evidence market is **$6B+ and growing ~13%/year**.
2. **Pakistan's hospitals sit on the supply and cannot legally sell it.** Years of real treatment outcomes — a goldmine for pharma — are locked in place. Pakistan's **Personal Data Protection Act (2025)** and DRAP rules make transferring identifiable patient data abroad effectively illegal. The manual workaround (emailing a CSV of patients) is both illegal and commercially worthless: pharma needs *auditable, protocol-ready, population-representative* evidence, which no spreadsheet can prove.

### A5. The Solution
A **verifiable clinical-evidence network**: pharma uploads an analysis *query*; NIC-partner hospitals run it on-prem against their own records; only aggregated, differentially-private statistics leave the site — signed by a cryptographic audit trail. No PHI ever moves. Pharma gets regulator-grade evidence; hospitals get a legal revenue stream; patients gain access to trials they currently never hear about.

### A6. Core Technology Architecture
- **Federated analytics core:** models/queries travel to the data, never the reverse. Only aggregated statistics return. Technically impossible to exfiltrate patient identities — this is the legal unlock.
- **Custom LLM routing layer:** a domain-tuned model converts unstructured mixed Urdu/Roman-Urdu/English clinical notes into standard **OMOP/FAIR** endpoints *at the hospital*, turning paper-era records into FDA-grade structured data locally.
- **Computer vision layer:** on-prem pathology-slide / imaging biomarker extraction, strengthening the deep-tech stack and adding a CV capability.
- **Distributed consensus ledger + zero-knowledge proofs:** every query, consent, and statistic is logged on an append-only ledger so buyers get cryptographic **data provenance** (this cohort is real, consents are valid, endpoints were computed on N genuine patients). Regulators demand ALCOA+ audit trails; Suboot ships one by default.

### A7. Why This Has Never Been Built
The components exist; the commercial convergence does not:
- **TriNetX** runs federated hospital networks — but no ledger, no cryptographic evidence provenance, no non-English/Urdu LLM extraction, and **no South Asian source hospitals**.
- **Aetion / PicnicHealth / Flatiron** — US/EU records only.
- **TensorFlow Federated / OpenFL** — open-source code, not a product, no ledger, no buyer.
No one has assembled *ledger-verified provenance + federated analytics + LLM structuration of local-language records + South Asia as the supply* into a sellable product. A US startup can't build the ground network; a Pakistani app shop can't build the crypto/federated depth. That gap is the company.

### A8. Target Market & Size
- **Primary buyer:** global pharma companies and contract research organizations (CROs) with real-world-evidence and diversity mandates — $6B+ market growing ~13%/yr.
- **Supply side:** Pakistan's top 20–30 teaching hospitals and research institutes (NIC partner hospitals included), then India, Bangladesh, Indonesia.
- **Unit of sale:** cohort-as-a-service (de-identified patient records matched to a protocol), evidence dossiers, research grants.

### A9. Business Model & Monetization
1. **Cohort-as-a-Service (core):** pharma/CROs pay per de-identified patient record matched against protocol criteria. Industry-standard, six-figure contract sizes, dollar-denominated.
2. **Evidence reports:** fees for IRB/regulatory-grade real-world evidence dossiers.
3. **Research funding:** global diversity-in-trials grants (NIH-type) co-fund pilots.
4. **Revenue profile:** no dependence on Pakistani government procurement; global buyers, recurring revenue, natural forex inflow.

### A10. Go-To-Market — first 5–10 paying pilots
- **Month 0–3:** use NIC's own Health Tech rails — partner hospital + partner anonymized dataset + medical-director mentors — to complete the first pilot: one real clinical question, one hospital, one ledger-verified report.
- **Month 3–6:** convert that report into one signed CRO/pharma agreement (target: pharma regional arms of Novartis/GSK/Gilead, or CROs like IQVIA).
- **Month 6–9:** extend to 2–3 more hospitals (Karachi/Lahore/Islamabad) + 1 more CRO.
- **Month 9–12:** close 5–10 paying pilot sites; prepare India/Bangladesh expansion LOIs.

### A11. Traction To Date (honest)
- Pre-revenue, idea-to-early-MVP stage.
- Founder has begun building the federated-query prototype.
- No signed LOIs yet — the pilot pipeline is deliberately built on NIC's partner network, which is the correct use of this program's Health Tech support.

### A12. Team
- **Founder / CTO:** [FOUNDER FULL NAME], [CITY]. Background: [e.g., software engineering / ML — one line]. Has the technical capability to build the federated + ledger stack solo.
- **Advisors to onboard in Month 1:** [PENDING] a medical director (via NIC Health Tech mentors) and a data-privacy/DRAP advisor (via NIC curriculum).
- Solo-founder risk is mitigated by a 90-day plan to recruit a technical co-founder and a clinical advisor from NIC's mentor pool (see Section D).

### A13. 12-Month Roadmap (aligned to Health Tech milestones)
| Milestone | Deliverable |
|---|---|
| **Month 3 — First pilot complete** | One federated query run against a NIC-partner hospital/partner dataset; one ledger-verified evidence report; privacy/ethics sign-off; first LOI drafted with a CRO or pharma regional office. |
| **Month 6 — First product demo** | Working product demo (live federated query + ledger receipt on screen); validation metrics vs. manual chart review; first paying pilot contract signed. |
| **Month 9 — Extended pilot run** | 3+ hospitals, 2 CRO/pharma engagements, URDU/English LLM structuration live in production; pricing proven with real payment collection. |
| **Month 12 — Final demo & graduation** | 5–10 paying pilot sites, repeatable sales motion, patent application filed on ledger-verified federated pipeline, expansion LOIs from India/Bangladesh. |

### A14. Why Us / Why Now
- **Why now:** FDA diversity mandates are live; Pakistan just enacted its data-protection law. The law created the wall, and Suboot is the only legal bridge across it.
- **Why us:** a founder who can actually build the deep-tech stack, running a concept no incumbent has assembled, inside the one country (plus India/Bangladesh) that owns the supply.

### A15. What We Need From NIC
1. Access to Health Tech partner hospitals and anonymized datasets for the Month-3 pilot.
2. DRAP / data-privacy mentors to de-risk the regulatory story early.
3. Medical-director mentorship for clinical credibility with pharma buyers.
4. R&D/IP framework to file the ledger + federated pipeline patent.

### A16. Stage / Funding Info
- Stage: idea-to-MVP. Seeking incubation (0% equity model) — not active fundraising at application time.
- [REGISTRATION STATUS: e.g., not yet registered / registered as Pvt Ltd — update]

---

## SECTION B — PITCH DECK OUTLINE (12 slides, ~5 min)

1. **Title:** Suboot — "Proof."
2. **The one-liner** (A2).
3. **The global problem:** FDA diversity mandates + South Asia supplying <5% of trial participants.
4. **The supply-side problem:** Pakistan's data-protection law locks the goldmine.
5. **The solution graphic:** query goes to hospital → local compute → ledger-signed aggregates only.
6. **The tech stack:** federated ML + custom LLM (Urdu/Roman-Urdu) + on-prem CV + ledger + ZKPs.
7. **Why never built:** TriNetX (no ledger, no South Asia) vs. us. One slide, three rows.
8. **Business model:** cohort-as-a-service pricing with $6B+ market.
9. **GTM:** NIC partner hospital pilot → one CRO/pharma deal → 3 hospitals → export.
10. **Roadmap:** the M3/M6/M9/M12 table.
11. **Team & why us:** founder builds the stack; NIC mentors close the gaps.
12. **The ask:** pilot access + DRAP/privacy mentors + IP framework.

---

## SECTION C — FIRST 90 DAYS (turns "no contacts" into a strength)

- **Week 1–2:** Build a live federated-query demo against a *synthetic* dataset (you can code this). This is your Stage-3 weapon.
- **Week 2–4:** Apply through NIC's Health Tech rails for one partner hospital / research institute. Frame it as *"we will run one clinical question on your data, and you keep the ledger receipt and the revenue."*
- **Week 4–8:** Target one clinical question with existing public data to *prove the workflow* (e.g., an NCD cohort from published/partner datasets) — produce one real ledger-verified report.
- **Week 8–12:** Use that report to open one CRO or pharma regional office conversation. The report is the sales deck.

---

## SECTION D — JUDGING-STAGES CHEAT SHEET

- **Stage 1 (paper):** Lead with the two numbers: "<5% of trial participants from South Asia" and "Pakistan's new data law." That combination reads as "founder sees the wall *and* the bridge."
- **Stage 2 (problem validation):** Bring the legal math: cost of an illegal CSV transfer (fine + zero value) vs. a ledger-verified cohort (legal + salable). Quote one DRAP/data-protection clause from memory.
- **Stage 3 (pitch):** The 2-minute live demo of the federated query + ledger receipt beats every slide. End on the pilot plan, not on "raising money."
- **Stage 4 (final interview):** Expect "why not just let TriNetX expand here?" Answer: *"TriNetX has no South Asian hospitals, no ledger, and no Urdu-record extraction. They'd have to rebuild Suboot's entire ground network — that's the moat."*

---

## SECTION E — HONEST RISK WEAKNESSES (know them before the judges do)

1. **No LOI yet (biggest risk).** Mitigation: the Month-3 pilot is designed *through NIC's partner network*, and a synthetic-data demo exists by Week 2 so judges see capability, not promises.
2. **Solo founder.** Mitigation: explicit Month-1 plan to add a technical co-founder and clinical advisor from NIC's own mentor pool.
3. **"Blockchain" skepticism.** Never say "blockchain." Say "append-only audit ledger with cryptographic evidence provenance."
4. **Long pharma sales cycles.** Mitigation: the first revenue target is a *CRO or regional pharma office*, not a global HQ procurement.
