# Requirements & Scope Document

**Project:** Internal Policy Knowledge Assistant
**Client:** Nilachala Textiles Pvt. Ltd., Bhubaneswar
**Client Sponsor:** Sri Jagannadha, Head of Operations
**Prepared by:** Ratha Yatra Das, AI/ML Consultant
**Version:** 1.0 — for client sign-off
**Date:** 8 August 2026

---

## 1. Project Objective

Nilachala Textiles' HR team currently spends a significant portion of each working day answering employee questions that are already documented in internal policy files. This project delivers an internal web application where employees ask questions in plain English and receive answers drawn **only** from the company's own policy documents, with a citation naming the exact source document and page.

The system will run entirely inside Nilachala's own network. No company document or employee question will be transmitted to any external service.

**Business outcome targeted:** reduce repetitive policy questions reaching the HR team by roughly 60%, and eliminate policy disputes caused by employees referring to outdated or unverifiable document versions.

---

## 2. In Scope

1. **Document ingestion pipeline** for 68 supplied documents (~900 pages), covering digital PDFs and Word files.
2. **Optical Character Recognition (OCR)** for the 12 scanned legacy documents, so their text becomes searchable. See §4 Assumptions and §8 Risks for the accuracy caveat.
3. **Question answering in English**, returning an answer grounded in the source documents.
4. **Source citation** on every answer — document name and page number.
5. **Explicit "not found" behaviour.** Where the documents do not contain an answer, the system will say so and direct the employee to the HR helpdesk rather than guessing.
6. **Department-based access control.** Employees see answers only from documents their department is permitted to view.
7. **Document-to-department access mapping file**, drafted by the consultant and confirmed in writing by the client (see §5).
8. **Web interface** accessible on the company intranet, supporting up to 10 concurrent users.
9. **Administrator re-ingestion process** allowing updated documents to be loaded without code changes.
10. **Query audit log** capturing question, answer, cited sources, and timestamp — for dispute resolution and quality review.
11. **Handover package:** deployment guide, administrator runbook, architecture documentation.
12. **Post-delivery support for 3 months**, including one training session for the nominated IT staff member.

---

## 3. Out of Scope

The following are explicitly excluded from this engagement. Each can be quoted separately as a future phase.

1. **Salary slips, PF balances, and any per-employee financial data.**
   This is a fundamentally different system from the one described here. The present project reads static policy documents that are identical for every employee. Salary and PF queries require live integration with the payroll system, per-employee identity verification, and handling of personally identifiable financial information — each carrying its own security and compliance obligations. Attempting to combine the two would put the 4-week demo deadline at risk and would weaken the security posture of both. **Recommendation:** deliver the policy assistant first, prove it in production, then scope a Payroll Query module as a separate Phase 2 engagement. The architecture built here is designed so that module can be added later without rework.

2. **Questions or answers in Odia, Hindi, or any language other than English.** Deferred to Phase 2.

3. **WhatsApp or Microsoft Teams integration.** Confirmed by client as Phase 2.

4. **Interpretation of images, floor plans, and safety diagrams.** Text within these documents is indexed; the visual content is not interpreted. Confirmed with client that no questions are asked against these diagrams.

5. **Determining which version of a duplicated document is current.** The consultant will *report* suspected duplicates; the client decides which version is authoritative. See §5.3.

6. **Mobile application.** The web interface is mobile-viewable but no native app is delivered.

7. **Migration or reorganisation of the existing shared drive.**

---

## 4. Assumptions

If any of these prove untrue, scope, timeline, and cost are subject to renegotiation.

1. Deployment target is a single Dell PowerEdge server, 32 GB RAM, **CPU only, no GPU**. All model selection is constrained accordingly.
2. Document corpus is approximately 68 documents / 900 pages, and will not grow materially during the engagement.
3. All documents are in English.
4. Documents change 4–5 times per year; near-real-time synchronisation is not required.
5. The 12 scanned documents are of sufficient scan quality for OCR to reach usable accuracy. This is verified in Week 1 — see §8.
6. Peak concurrency is 10 users; total user base 120–150 office staff.
7. The server is reachable on the company intranet and the client's IT team provides network access, deployment permissions, and a service account.
8. Employee department information can be supplied by the client in any structured form (spreadsheet is acceptable).

---

## 5. Client Responsibilities

Delivery in 4 weeks depends on these items arriving on time. **Each day of delay to a Week 1 item moves the final delivery date by one day.**

| # | Item | Owner | Due |
|---|---|---|---|
| 5.1 | All 68 documents delivered in a single folder | Sri Jagannadha | **End of Week 1, Day 2** |
| 5.2 | 20–30 real employee questions from HR executives, to form the acceptance test set | HR team, via Sri | **End of Week 1** |
| 5.3 | Confirmation of which version of each duplicated document is authoritative; superseded versions removed from the supplied folder | HR team, via Sri | **End of Week 2** |
| 5.4 | Written sign-off on the document-to-department access mapping drafted by consultant | Sri Jagannadha | **End of Week 2** |
| 5.5 | Server access, credentials, and network clearance | Pramod, IT | **End of Week 2** |
| 5.6 | Nominated IT staff member identified for handover training | Sri Jagannadha | **Week 4** |
| 5.7 | Decision-making availability. Where Sri is travelling, Pramod (IT) is the delegated approver. Items awaiting approval for more than 2 working days will be escalated and the timeline adjusted. | — | Ongoing |

---

## 6. Constraints

| Constraint | Source | Design implication |
|---|---|---|
| No data may leave the company network | MD directive, firm | All models run locally. No commercial AI APIs. |
| No GPU available this quarter | IT | Small local language model on CPU. Response times will be seconds, not milliseconds — see §7. |
| 32 GB RAM, single server | IT | Model size and index size budgeted within this envelope. |
| 12 documents are scanned images | Existing corpus | OCR stage required before indexing. |
| Working demo required for MD | Client | Week 4 is a hard date. |
| Documents contain tables (salary grades, leave entitlement) | Existing corpus | Table structure must survive text extraction or answers will be wrong. |

---

## 7. Definition of Done

The project is complete and payable when **all** of the following are demonstrated:

1. **Accuracy.** Against the client-supplied test set of 20–30 real questions: **at least 90% (18/20) judged correct by the client's HR team.** "Correct" means the answer matches the policy and cites the right source document.
2. **Grounding.** For 5 deliberately out-of-scope questions, the system returns its "not found" response in **5 out of 5** cases. Zero fabricated answers is a hard pass/fail gate.
3. **Citations.** 100% of answers display a source document name and page number.
4. **Access control.** A test user from one department is verifiably unable to retrieve content from a document restricted to another.
5. **Performance.** Median response time **under 15 seconds** on the supplied CPU-only hardware, with 10 concurrent users.
6. **Operability.** The nominated IT staff member successfully re-ingests an updated document without consultant assistance, following the written runbook.
7. **Handover.** Deployment guide, runbook, and architecture document delivered and walked through.

Items 1 and 2 are assessed jointly with the client in a single sign-off session in Week 4.

---

## 8. Risks & Mitigations

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R1 | **Scanned documents OCR poorly.** The Safety Manual is among them. A wrong safety answer is a physical-harm risk, not just a quality issue. | Medium | **High** | OCR quality assessed in Week 1 as the first technical task. Any document scoring below the agreed quality bar is flagged to the client, and the system is configured to answer safety questions with a mandatory "verify with the printed Safety Manual" notice. Client to be informed in writing before Week 2. |
| R2 | **Duplicate policy versions cause the system to cite an outdated policy** — recreating the very disputes this project exists to end. | **High** | **High** | Consultant runs an automated duplicate-detection pass in Week 1 and delivers a list. Client confirms authoritative versions (§5.3). System indexes only confirmed-current documents. Until confirmed, affected topics are excluded from the demo. |
| R3 | **CPU-only inference too slow for acceptable user experience.** | Medium | Medium | Model size and retrieval depth benchmarked in Week 1 before committing to architecture. Response streaming used so the user sees output beginning immediately. Performance target set explicitly in §7.5. |
| R4 | **Client-supplied test questions arrive late**, compressing evaluation into the final days. | Medium | High | Consultant drafts a provisional test set in Week 1 from the document corpus, so evaluation tooling is ready and only the questions need substituting. |
| R5 | **Scope expansion** — Finance requesting salary/PF, or Phase 2 items pulled forward. | **High** | High | Handled by this document. Any addition is quoted as a change request with an explicit timeline impact before work begins. |
| R6 | **Client approvals delayed while sponsor travels.** | Medium | Medium | Pramod (IT) named as delegated approver in §5.7, with a 2-working-day escalation rule. |
| R7 | **Tables in policy documents lose structure during extraction**, producing wrong entitlement figures. | Medium | High | Table-aware extraction used; leave and salary-grade tables added explicitly to the Week 3 test set as a targeted check. |

---

## 9. Timeline — 4 Weeks

| Week | Milestone | Deliverable to client |
|---|---|---|
| **Week 1** | **Discovery & Feasibility.** Corpus received and inventoried. OCR quality assessed on the 12 scanned documents. Duplicate documents detected and reported. Model benchmarked on CPU for speed. Architecture finalised. | Corpus inventory report, duplicate list, OCR feasibility note, architecture document |
| **Week 2** | **Core Pipeline.** Ingestion, chunking, and indexing of confirmed documents. Retrieval working end to end. Access mapping drafted for client sign-off. | Working retrieval demonstration (internal), draft access mapping |
| **Week 3** | **Application & Grounding.** Question answering with citations. "Not found" behaviour implemented and tuned. Access control enforced. Audit logging. Web interface built. Evaluation run against test set; accuracy tuned. | Internal demo, first evaluation report |
| **Week 4** | **Hardening, Evaluation & Demo.** Deployment to company server. Formal acceptance test against §7. MD demonstration. Documentation and handover training. | Deployed system, signed acceptance test, deployment guide, runbook, architecture document |

**Post-delivery:** 3 months support, followed by handover to nominated IT staff.

---

## 10. Commercial Summary

- **Payment milestones:** 30% on signature of this document · 40% on successful MD demonstration (Week 4) · 30% on completion of handover and documentation.
- **Change requests:** any item listed in §3 Out of Scope, or any new requirement, is quoted separately before work commences.
- **Support period:** 3 months from acceptance, covering defect resolution and document re-ingestion assistance. Does not include new features.

---

## 11. Sign-off

By signing below, the client confirms the scope, assumptions, responsibilities, and definition of done recorded in this document.

| | Client | Consultant |
|---|---|---|
| Name | Sri Jagannadha | Ratha Yatra Das |
| Role | Head of Operations | AI/ML Consultant |
| Signature | | |
| Date | | |
