# Search spec — ulms-highgrade-pulm-mets-tp53-smarcb1-hla-a2-w9t4

Run 2026-08. Re-run of `ulms-highgrade-pulm-mets-er-pr-neg-qqvt` with plasma
ctDNA (Guardant) and allele-level HLA class I typing added. The launching brief
enumerated the axes and is treated as the agreed spec; no interactive
confirmation round was held. Every row re-derived against this slug's profile —
the source case's `trials.jsonl` was read for coverage comparison only and is
not modified.

## Patient anchors
- High-grade uterine leiomyosarcoma, spindle-cell; bilateral pulmonary mets with
  an infiltrative / possibly inflammatory radiologic read. Stage IV.
- **Systemic-therapy naive.** LMS-04 (doxorubicin + trabectedin -> trabectedin
  maintenance) planned, NOT started. A first-line window is open now and closes
  when induction starts. Screen 1L-eligible seats separately from
  post-anthracycline seats.
- ER <1% / PR <1% by IHC — endocrine foreclosure.
- SMARCB1 G344Afs*13, plasma ctDNA only, no tissue, tumour fraction unsupplied.
  Hard prior against it: 170 consecutive uterine smooth-muscle tumours all
  retained SMARCB1 (pmid:34271067). Every EZH2/SWI-SNF seat is conditional on
  INI1 IHC.
- TP53 Q52*, plasma only, CHIP caveat, prognostic — not a targeting axis.
- Four VUS at 0.09-1.1% VAF. ERBB3 G914E is explicitly NOT a HER-family
  rationale; no HER-directed row is logged on it.
- HLA-A*02:01 confirmed (also A*03:01; B*39:01, B*44:02; C*05:01, C*12:03).
  Allele gate cleared; antigen expression (MAGE-A4, NY-ESO-1, PRAME) unmeasured.
  Typing is not eligibility.
- Unmeasured: MSI/MMR, TMB, NTRK, RET, BRAF, HRD/BRCA, RB1, ATRX, MED12, PD-L1,
  B7-H3, HER2. Plasma negatives are not exclusionary at unsupplied tumour
  fraction.
- ECOG 1 is an intake ASSUMPTION, not measured. Flag every protocol with an
  ECOG 0-1 ceiling.
- Baseline LVEF undocumented; residence ~8,500 ft (oximetry / pulmonary
  criteria); infiltrative pattern may complicate RECIST measurability.
- Preferences are all assumed defaults: prefers_trials true, no toxicity vetoes,
  no modality constraints, US geography band.

## Eligibility scope = the validator's essential `gates_intervention` rows
tazemetostat / NCT02601950; pembrolizumab, dostarlimab / NCT02628067,
NCT02715284; larotrectinib, entrectinib, repotrectinib / NCT02576431,
NCT02568267, NCT03093116; olaparib + temozolomide / NCT03880019; doxorubicin,
trabectedin; afamitresgene autoleucel, uzatresgene autoleucel / NCT04044768;
IMA203, brenetafusp / NCT03686124, NCT04262466; ifinatamab deruxtecan,
enoblituzumab, vobramitamab duocarmazine; letetresgene autoleucel / NCT03967223.

## Axes
1. **uLMS / STS systemic therapy, first line.** LMS-04, GeDDiS, PALETTE, eribulin
   ph3, trabectedin ph3; current 1L registry protocols (lurbinectedin +
   doxorubicin, ivonescimab, unesbulin, zanzalintinib, anlotinib). Tagged 1L.
2. **Post-anthracycline seats.** Kept separately; she is ineligible today and
   eligible after LMS-04 induction/progression.
3. **EZH2 / SWI-SNF-directed.** tazemetostat (NCT02601950 SWI/SNF basket,
   INI1-negative non-epithelioid cohort ~9% ORR, pmid:41882006), tulmimetostat
   (CPI-0209), valemetostat, SNDX-5613-adjacent SWI/SNF programs, BRM/BRG1
   (SMARCA2/4) degraders and ATPase inhibitors, EZH2 x other. All conditional on
   INI1 IHC.
4. **HLA-A*02:01 restriction / platform sweep (Step 1.75).** Registry queried by
   the eligibility gate, not the drug: `HLA-A*02:01`, `HLA-A2`, `A*02:01`,
   `A2-restricted` x {sarcoma, leiomyosarcoma, solid tumor}. TCR-T, ImmTAC /
   TCR-mimetic engagers, peptide vaccines. Verified facts respected: Tecelra is
   synovial-sarcoma-only on label; SPEARHEAD-1 uses >=1+ in >=10% by central IHC;
   IMA203 screens PRAME by RT-qPCR not IHC; IGNYTE-ESO restricts to synovial and
   myxoid/round-cell liposarcoma.
5. **Tumour-agnostic baskets** gated on NTRK, RET, MSI-H/dMMR, TMB-H, BRAF,
   HER2 IHC — untested here, logged as gated-on-missing-assay, not excluded.
   No row is logged on ERBB3 G914E.
6. **ADCs, incl. B7-H3/CD276** — ifinatamab deruxtecan, HS-20093/GSK5764227,
   MGC026, YL201, MHB088C, enoblituzumab, vobramitamab duocarmazine
   (discontinued). Plus non-B7-H3 sarcoma ADCs.
7. **Checkpoint and combination immunotherapy** in sarcoma / uLMS.
8. **Anti-angiogenics and TKIs.**
9. **PARP-based combinations** — olaparib + temozolomide (NCI 10250 /
   NCT03880019) and successors; PARP + other in sarcoma.
10. **HDAC, CDK and cell-cycle** — abemaciclib combinations, CDK7 (REC-617),
    WEE1, RB1-directed.
11. **Isotope sweep, run explicitly to completion.** {leiomyosarcoma, sarcoma,
    solid tumor} x {177Lu, lutetium, 225Ac, actinium, 131I, iodine-131, 90Y,
    211At, 212Pb, 227Th, 161Tb} plus target-anchored (FAP-2286, B7-H3/omburtamab).
    Therapeutic intent decides; imaging-only drops, and the drop is named in the
    run log rather than left silent.
12. **Locoregional options for bilateral pulmonary disease** — metastasectomy,
    SBRT, isolated lung perfusion / pulmonary suffusion, inhaled therapy.

## Per-row eligibility axes
Prior-therapy requirement (anthracycline-naive today); ECOG ceiling vs
undocumented ECOG; LVEF requirement; RECIST measurability against the
infiltrative pattern; oximetry / pulmonary criteria vs altitude; biomarker gate
where the named assay has not been run.

## Sources
ClinicalTrials.gov v2 API (primary), PubMed E-utilities, PMC / Europe PMC,
DailyMed for label status, Inxight for alias resolution. Web search budget for
this session is assumed exhausted; primary APIs used directly.
