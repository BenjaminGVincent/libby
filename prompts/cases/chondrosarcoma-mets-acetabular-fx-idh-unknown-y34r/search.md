# Trial-screen search spec — chondrosarcoma-mets-acetabular-fx-idh-unknown-y34r

Run date: 2026-08. Spec derived from the launching brief (which enumerated the
axes explicitly) plus `profile.json::targetable_features[]` and the
target_validation gating map. WebSearch budget exhausted this session: all
discovery ran through the ClinicalTrials.gov v2 API and NCBI E-utilities, Europe
PMC and WebFetch. That covers registry and literature discovery adequately but
means no Google-Scholar sweep of ASCO/ESMO/AACR meeting abstracts and no live
FDA label reads; meeting-only programs may be under-captured.

## Patient anchors
- Dedifferentiated (high-grade) chondrosarcoma, left acetabulum, pathologic
  fracture, bilateral dispersed lung mets. Treatment-naive, first line.
- ECOG 2 **assumed at intake, never measured** — flag on every row.
- IDH1/IDH2 untested (prevalence ~71% in dedifferentiated — live prior);
  HLA class I untested; PD-L1/TMB/MSI untested; no NGS yet.
- No toxicity vetoes; no modality constraints; prefers trials; geography null.
- Surgical washout risk: acetabular stabilisation may be imminent; most
  protocols exclude major surgery within 3-4 weeks.

## Axes
1. **Chondrosarcoma-specific trials** (CT.gov cond=chondrosarcoma, all phases,
   recruiting + not-yet-recruiting; per-trial check whether dedifferentiated
   histology is eligible or excluded — NCT06127407 conventional-only per
   target_validator, verify directly).
2. **Bone-sarcoma / soft-tissue-sarcoma baskets that admit chondrosarcoma** —
   cond=sarcoma with chondrosarcoma named in eligibility; first-line
   anthracycline-platform trials; gem/docetaxel-platform trials.
3. **IDH-directed agents** across tumor types: ivosidenib (AG-120), olutasidenib
   (FT-2102), vorasidenib (AG-881), enasidenib (AG-221), safusidenib (AB-218 /
   DS-1001), LY3410738, HMPL-306, BAY1436032. Chondrosarcoma cohorts first,
   then basket/other-indication context.
4. **Checkpoint blockade in sarcoma / dedifferentiated chondrosarcoma**:
   pembrolizumab, nivolumab ± ipilimumab, durvalumab/tremelimumab, atezolizumab;
   PD-L1/TMB/MSI tumor-agnostic gates.
5. **B7-H3 (CD276)-directed agents** (~96% prevalence in dedifferentiated CS):
   ifinatamab deruxtecan (DS-7300, I-DXd), vobramitamab duocarmazine (MGC018),
   HS-20093 (GSK5764227), YL201, enoblituzumab, mirzotamab?, B7-H3 CAR-T
   (e.g. Seattle Children's, Stanford), omburtamab radioconjugates.
6. **HLA-A*02:01-restricted platform (Step 1.75 eligibility-gate sweep)**:
   TCR-T and ImmTAC gated on the allele — afamitresgene autoleucel, uza-cel
   (ADP-A2M4CD8), letetresgene autoleucel, brenetafusp (IMC-F106C), IMA203;
   registry sweep on "HLA-A*02", "HLA-A*02:01", "HLA A2" tokenization variants
   crossed with sarcoma/solid tumor.
7. **Cytotoxic evidence base for dedifferentiated CS** (first-line, published):
   doxorubicin ± ifosfamide/cisplatin, MAP-type, gem/docetaxel — trial
   publications and registry rows supporting the chemo-responsive read.
8. **Local therapy for the acetabular lesion**: proton / carbon-ion trials and
   series in unresectable pelvic/axial chondrosarcoma; palliative or definitive
   particle therapy alongside systemic treatment.
9. **Isotope sweep** (radiopharmaceutical rule): chondrosarcoma × {177Lu,
   lutetium, 225Ac, actinium, 131I, 90Y, 211At, 212Pb, 227Th, 161Tb}; plus
   B7-H3 × same isotopes; all recruitment statuses. Classify by therapeutic
   intent, never by the word "radio-".

## Eligibility axes recorded per row
ECOG bar vs assumed-2; prior-therapy requirement vs treatment-naive (cuts both
ways); RECIST-measurable disease vs small dispersed nodules; surgical washout
vs planned stabilisation; archival vs contemporaneous tissue for IDH (mutant
IDH1 recurrently lost in metastatic evolution); histology inclusion wording
(conventional vs dedifferentiated).
