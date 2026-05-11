# Trial-screener search spec — pancreatic-recurrent-kras-g12r-m8f3

## Case anchor
- Recurrent PDAC, post-resection + adjuvant FOLFIRI (PD).
- ECOG 1, age band 50-59.
- Confirmed biomarkers: KRAS G12R, TP53 inactivating, CDKN2A loss, CCND3 alteration, MSS, TMB 4.1 mut/Mb.
- No germline data yet on file (gating for PARP-inhibitor rows).
- User prefers trials; no toxicity vetoes; treat-to-remission goal; accepts high-risk/high-reward.

## Targetable features in scope
1. KRAS G12R (highest-EV axis) — pan-KRAS / pan-RAS(ON) / G12X-pan / G12R-selective inhibitors.
2. CDKN2A loss + CCND3 alteration — CDK4/6 inhibitors (palbo / ribo / abema), selective CDK4 (PF-07220060), cyclin-D-degraders, fadraciclib, INCB123667.
3. KRAS-directed combinations — KRASi + SHP2i / SOS1i, KRASi + ICI, KRASi + chemo, KRASi + CDK4/6i, KRASi + FAK / autophagy.
4. TP53 inactivating — APR-246 (eprenetapopt) / analogues; MDM2 inhibitors are off-mechanism for inactivating mutations and are excluded.
5. MSS + TMB 4.1 (cross-tumor IO with non-PD-1 mechanism only — flag biomarker-non-fit).

## Search axes
A. ClinicalTrials.gov v2 — drug-name alias-expanded:
   - RMC-6236 / daraxonrasib
   - RMC-7977 / zoldonrasib
   - BI-3706674
   - ASP3082 / ASP-3082
   - INCB161734
   - MRTX1133 (KRAS G12D, off-target for G12R, only include if basket / pan-G12X)
   - divarasib (GDC-6036) — G12C, but allied program family; check for pan-KRAS variant
   - olomorasib / LY3537982 (G12C, allied family)
   - palbociclib, ribociclib, abemaciclib in PDAC with CDKN2A loss
   - PF-07220060, fadraciclib, INCB123667 (cyclin / CDK selective)
   - eprenetapopt / APR-246 (only TP53 LOF basket trials)
B. PubMed — pivotal publications for each agent above.
C. Biomarker-basket searches: "KRAS G12X solid tumor", "CDKN2A loss CDK4/6 inhibitor solid tumor".

## Decision rules
- `primary_indication_match`: trial enrolls PDAC cohort as primary.
- `basket_or_biomarker_match`: KRAS-mutant or G12X solid-tumor basket.
- `cross_tumor_extrapolation`: non-PDAC trial of a feature-targeting drug, informational.
- `fit_to_case`: strong if biomarker + indication + line + ECOG all align; partial if one axis is gating (e.g. germline-BRCA pending, p16-IHC pending); weak if biomarker-adjacent only; none if clearly excluded.
- `toxicity_flags`: empty per preferences (no vetoes), but populate with mechanistic flags where standard (e.g. neutropenia for CDK4/6i, GI tox for KRASi).

## Result cap
Lift the 30-row cap given >10 pipeline agents in scope. Run to pipeline-roster exhaustion.
