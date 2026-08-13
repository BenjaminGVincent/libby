# Search spec — ulms-highgrade-pulm-mets-er-pr-neg-qqvt

Run date: 2026-08. Spec taken from the launching brief (which enumerated the
axes); no interactive confirmation round was held — the brief is treated as the
agreed spec.

## Patient anchors (from profile.json / preferences.json)
- High-grade uterine leiomyosarcoma, spindle-cell; bilateral pulmonary mets,
  infiltrative / possibly inflammatory radiologic pattern. Stage IV.
- **Systemic-therapy naive.** LMS-04 (doxorubicin + trabectedin → trabectedin
  maintenance) planned and imminent, NOT started. First-line doors close in weeks.
- ER <1% / PR <1% confirmed (endocrine foreclosure; provenance check pending).
- Everything else unmeasured: NTRK, MSI/dMMR, TMB, HRD/BRCA-HRR, TP53/RB1/ATRX/
  MED12, HLA class I, PD-L1, B7-H3, HER2, PRAME/MAGE-A4/NY-ESO-1.
- ECOG 1 is an intake ASSUMPTION, never documented — flagged on every row.
- Baseline LVEF undocumented; residence ~8,500 ft (oximetry/pulmonary criteria);
  infiltrative pattern may complicate RECIST measurability.
- Preferences all assumed defaults (no user statement): prefers_trials true,
  no vetoes, no modality constraints, geography US band.

## Axes
1. **uLMS / STS systemic therapy, 1L and beyond** — doxorubicin-based
   combinations, trabectedin, gemcitabine/docetaxel, pazopanib, eribulin,
   dacarbazine, newer registrational or ph1/2 agents (unesbulin, lurbinectedin
   combos, anlotinib, etc.). Registry: cond=leiomyosarcoma recruiting; plus
   published anchors (LMS-04 PMID 35835135 — NOT 36174625, which is a letter;
   GeDDiS; PALETTE; eribulin ph3; trabectedin ph3).
2. **Maintenance / continuation phase strategies** — LMS-04-style maintenance;
   any sarcoma maintenance or switch-maintenance trial.
3. **HRD / PARP in uLMS** — olaparib + temozolomide NCI 10250 / NCT03880019 and
   successors / confirmatory studies; PARP combos in sarcoma.
4. **Tumor-agnostic baskets** gated on NTRK, MSI-H/dMMR, TMB-H, RET, BRAF,
   HER2-IHC — all untested here → rows recorded as gated-on-missing-assay, not
   excluded. Note prior-therapy requirements (TMB-H pembrolizumab requires prior
   treatment; she is naive — timing axis).
5. **Cell therapy / TCR-T in sarcoma** — HLA class I restriction is the platform
   gate (Step 1.75 sweep): PRAME (IMA203, brenetafusp), MAGE-A4 (afami-cel,
   uza-cel), NY-ESO-1 (lete-cel). HLA untyped → unassessable, not negative.
6. **B7-H3 / CD276 agents** — ADCs (ifinatamab deruxtecan, HS-20093/GSK5764227,
   YL201, MHB088C), mAbs (enoblituzumab), discontinued (vobramitamab
   duocarmazine, omburtamab RIT), CAR-T. 97% STS positive (PMID 39478506).
7. **Local / consolidative therapy for pulmonary mets** — metastasectomy, SBRT
   in sarcoma; explicitly on the table per the consulting oncologist.
8. **Isotope sweep** (radiopharmaceutical axis, run to completion):
   {leiomyosarcoma, sarcoma} × {177Lu, lutetium, 225Ac, actinium, 131I, 90Y,
   211At, 212Pb, 227Th} plus target-anchored sweeps (B7-H3/omburtamab,
   FAP-2286/FAP radioligand — FAP is on the case biomarker survey). Classify by
   therapeutic intent per the radiopharmaceutical rule; imaging-only drops.

## Eligibility axes checked on every row
- Prior-therapy requirement (anthracycline-naive TODAY — eligible 1L,
  ineligible for prior-anthracycline-required trials until LMS-04 starts/fails;
  the reverse flips within weeks).
- ECOG ceiling (undocumented ECOG — flag).
- LVEF requirement (undocumented baseline — flag on anthracycline rows).
- Measurable disease / RECIST (infiltrative pattern — flag).
- Oximetry / pulmonary criteria vs 8,500 ft residence.
- Biomarker gate: named assay not yet done → "gated on testing not done".

## Sources
ClinicalTrials.gov v2 API (primary), PubMed E-utilities, PMC/Europe PMC,
meeting abstracts (ASCO/ESMO/CTOS 2024-2026) via web search, Inxight for alias
resolution.
