# Search spec — gist-sdh-multifocal-resected-m1-k4n8

## Patient snapshot
- 40-49, SDH-deficient GIST (KIT/PDGFRA wild-type), biallelic SDHA inactivation (L306P + Y408N, with E350fs on ctDNA pending tissue confirmation).
- ypT3(m)N0M1 → R0 distal gastrectomy + Roux-en-Y; M1 deposit at ligament of Treitz completely resected. Currently no evidence of disease.
- ECOG 1. No measurable disease right now; most phase-II trials requiring RECIST-measurable disease are off the table until first recurrence.
- ctDNA-only secondary findings: PIK3CA R93W (non-canonical), MAP2K1 P124S (activating hotspot), POLE R1679C germline (likely VUS at TMB <1, MSS).
- Decision question: (a) adjuvant systemic therapy, (b) surveillance plan, (c) contingency systemic therapy at first recurrence.

## Mechanism scope
All Keep decisions trace back to one of the patient's targetable features. Drugs whose mechanism does not engage SDH-deficient biology, MAP2K1, or PIK3CA do not enter the dossier — even if they have RCT-grade evidence in KIT-mutant GIST.

## Search axes

### Axis 1 — SDH-deficient GIST / KIT-WT GIST mechanism
- Belzutifan (NCT04924075 wt-GIST cohort) — HIF-2α inhibitor anchored on SDH→succinate→pseudohypoxia.
- Temozolomide in dSDH-GIST (NCT03556384, NCT05661643) — alkylator with MGMT-methylation-driven rationale in dSDH GIST.
- Hypomethylating agents: guadecitabine (SGI-110), decitabine, azacitidine — anchored on global DNA hypermethylation in dSDH GIST.
- HIF-2α inhibitors beyond belzutifan: PT2977 / MK-6482 (= belzutifan); next-gen HIF-2α NKT-2152 (Nikang), DFF332 (Novartis), ARO-HIF2 (Arrowhead).
- NCI Pediatric and Wild-Type GIST Clinic registry / longitudinal protocols.

### Axis 2 — TKI backbone (KIT-WT GIST)
- Sunitinib, regorafenib, ripretinib — second- and later-line in KIT-WT GIST.
- Adjuvant imatinib trials enrolling dSDH-GIST (low expected activity but enrollable).
- Cabozantinib, pazopanib, dasatinib in KIT-WT or dSDH-GIST cohorts.
- Crenolanib, ponatinib for completeness in wt-GIST.

### Axis 3 — Co-mutation / basket trials
- MAP2K1 P124 / MEK1 hotspot — MEK-inhibitor baskets (trametinib, binimetinib, selumetinib, cobimetinib) and MEK+RAF combos (NCI-MATCH arms, Rare Tumor Initiative).
- PIK3CA hotspot baskets — alpelisib, inavolisib, copanlisib, taselisib (LATTICE / SOLAR-1 / MATCH arm Z1F).
- Tumor-agnostic NCI-MATCH and NCI-COG-MATCH histiotype-neutral baskets.
- DART (S1609 dual anti-CTLA-4/anti-PD-1 in rare tumors) — historical dSDH-GIST cohort.

### Axis 4 — Off-target rule-outs (mechanism scope gate)
- Anti-PD-1 / anti-PD-L1 monotherapy in unselected GIST → drop unless biomarker-matched (TMB<1, MSS forecloses tumor-agnostic ICI).
- BRAF/MEK in BRAF V600E GIST → drop (BRAF WT here).
- NTRK / RET inhibitors → drop (no fusions / no actionable alterations).

## Registries and indices to query
1. ClinicalTrials.gov v2 API — primary discovery for active interventional studies.
2. PubMed E-utilities — trial publications and reviews on dSDH-GIST therapeutics, including the 2025 Florou and 2023–2025 NCI-PedWtGIST publications.
3. PMC — full-text OA where available.
4. ASCO / ESMO / CTOS abstracts 2023–2026 — for un-indexed pipeline updates (CTOS is the relevant sarcoma society for GIST).
5. NIH Inxight Drugs / WHO INN — for code↔INN resolution on HIF-2α next-gen agents.

## Result-cap policy
Step 1.5 pipeline roster for SDH-deficient GIST is modest (≤ 10 named investigational agents), so the default cap is fine. The cap lifts only if a single search axis returns > 10 unique pipeline agents requiring per-drug coverage.

## Triage rule
- Currently NED → trials requiring measurable disease are tagged `contingency` in `inclusion_match_notes` and `fit_to_case` defaults to `partial` rather than `none`, because they become relevant the moment ctDNA or imaging flags recurrence.
- Adjuvant trials enrolling KIT-WT / dSDH-GIST in the resected post-R0 setting are the highest-priority current-state matches.
- Surveillance / registry / observational studies (e.g. NCI wt-GIST clinic) are kept because they bridge to therapy at recurrence.
