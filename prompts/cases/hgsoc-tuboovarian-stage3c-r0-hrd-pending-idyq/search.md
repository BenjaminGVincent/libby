# Search spec — hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq

Patient: 70-79F, high-grade serous tubo-ovarian/primary-peritoneal carcinoma, FIGO IIIc,
ECOG 1, R0 after neoadjuvant carbo/paclitaxel/bevacizumab + GEN-1 (IMNN-01) and interval
debulking. Germline BRCA wild-type. Tumor HRD / somatic BRCA / genomic-instability score
PENDING. ER-positive (~80%, weak-moderate) / PR-negative. HER2 IHC 1+ (negative). FOLR1
below threshold (negative). Signatera MRD cleared to Not Detected.

## Targetable features (drive every keep decision)
1. HRD / homologous-recombination status (somatic BRCA + GIS) — gates PARP-inhibitor maintenance. RANK 1.
2. VEGF / angiogenesis — already on bevacizumab; anti-angiogenic maintenance axis.
3. ER expression (ER+/PR-) — endocrine option (aromatase inhibition).
4. IL-12 / tumor immune microenvironment — on-study GEN-1/IMNN-01; immunotherapy-combo context.

## Out of scope (mechanism-scope rule)
- Trastuzumab-deruxtecan / HER2-directed ADCs — HER2 IHC 1+, below threshold. DROP as fit.
- Mirvetuximab soravtansine / FRalpha ADCs — FOLR1 below PS2+ threshold. DROP as fit.
- Standard-of-care drugs whose mechanism does NOT target a listed feature.

## Search axes
(a) Tumor + line + biomarker: newly-diagnosed / 1L-maintenance advanced HGSOC PARP-inhibitor
    maintenance; HRD-positive and all-comers; +/- bevacizumab.
(b) Biomarker / target alone: PARP inhibitor maintenance ovarian; VEGF/anti-angiogenic
    maintenance ovarian; endocrine therapy (aromatase inhibitor / letrozole / anastrozole /
    fulvestrant) ER+ ovarian; IL-12 immunogene / immunotherapy combos ovarian.
(c) Drug / mechanism anchors:
    - PARP inhibitors: olaparib, niraparib, rucaparib, veliparib (+ bev combos).
    - Anti-angiogenic maintenance: bevacizumab; cediranib (+olaparib); pazopanib.
    - PARP+anti-angiogenic combos: olaparib+bevacizumab (PAOLA-1), olaparib+cediranib.
    - Endocrine: letrozole, anastrozole, fulvestrant, tamoxifen in ovarian.
    - IL-12: GEN-1 / IMNN-01 (Imunon), other IL-12 immunotherapy ovarian.

## Sources
1. ClinicalTrials.gov v2 API (primary discovery).
2. PubMed E-utilities (pivotal trial publications).
3. Europe PMC fallback.

## Fit / toxicity computation
- efficacy_toxicity_weight 0.7 (efficacy-leaning, tolerability-aware, age 70-79, ECOG 1).
- Vetoes: additional peripheral neuropathy; severe myelosuppression / febrile neutropenia.
- Modality: oral / low-infusion-burden preferred; caution with thrombotic / bleeding risk
  (high VTE history, prior IVC filter) — flag bevacizumab/anti-angiogenic VTE+bleeding.
- HRD result PENDING -> PARP-maintenance fit capped at "partial" pending the gating assay.
