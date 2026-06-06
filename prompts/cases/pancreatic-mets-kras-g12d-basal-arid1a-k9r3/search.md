# Search spec — pancreatic-mets-kras-g12d-basal-arid1a-k9r3

Patient: 79M, metastatic basal-like PDAC (large primary + multiple >1cm liver mets), ECOG 1 (assumed), treatment-naive. Plasma ctDNA profile. MSS, TMB 8.6, germline-negative, no rearrangements.

HLA class I: A*01:01, A*02:01, B*37:01, B*44:02, C*05:01, C*06:02. NOT C*08:02, NOT A*11:01.

## Targetable features in scope (mechanism gate)

1. KRAS G12D — RAS(ON) small-molecule inhibitors and KRAS-directed immunotherapy (vaccine / TCR-T / cell therapy).
2. ARID1A loss-of-function — synthetic-lethal axis: ATR inhibitors, EZH2 inhibitors.
3. MLH1 / MMR-conditional immunotherapy — decision-relevant, validation-gated (MMR IHC). Treat checkpoint monotherapy as low-yield given MSS + TMB 8.6 + germline-negative.

## Search axes

(a) Tumor type + line + biomarker: KRAS G12D metastatic PDAC, 1L and 2L+.
(b) Biomarker / target alone (basket / pan-tumor): KRAS G12D solid-tumor baskets; ARID1A-deficient solid-tumor ATR/EZH2 baskets.
(c) Drug-name / mechanism anchored on candidate interventions across tumor types: each RAS(ON) inhibitor, each KRAS vaccine/TCR program, each ATR/EZH2 agent, alias-expanded.

## HLA screening rule

Every KRAS immunotherapy is screened against the patient's class I alleles. C*08:02-restricted (NT-112) and A*11:01-restricted (AZD0240) TCR-T products are INELIGIBLE and recorded as such. Peptide/amphiphile and mRNA vaccines that are not single-allele-restricted are eligible on HLA grounds.

## Out of scope

Standard-of-care chemotherapy backbones (FOLFIRINOX, gem/nab-paclitaxel) whose mechanism does not target a listed feature. PARP/HRD maintenance (germline-negative, no HRD). Fusion-directed agents (no rearrangements).

## Sources

ClinicalTrials.gov v2 API (primary), PubMed E-utilities, ASCO GI 2026 abstracts (INCB161734).
