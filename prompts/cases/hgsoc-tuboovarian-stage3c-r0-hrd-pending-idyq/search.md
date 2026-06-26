# Search spec — hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq

Patient: 70-79F, high-grade serous tubo-ovarian/primary-peritoneal carcinoma, FIGO IIIc,
ECOG 1, R0 after neoadjuvant carbo/paclitaxel/bevacizumab + GEN-1 (IMNN-01) and interval
debulking. Germline BRCA wild-type. Tumor NGS (Altera) RESULTED: somatic BRCA wild-type
(BRCA-proficient), genomically unstable but QUALITATIVE only — no validated GIS/HRD score.
MSS, TMB-low (1 mut/Mb). ER-positive (~80%, weak-moderate) / PR-negative. HER2 IHC 1+
(negative). FOLR1 below threshold (negative). Signatera MRD cleared to Not Detected.
New low-priority investigational axes: PIK3CA amplification, MAP2K4 deletion.

## Targetable features (drive every keep decision)
1. HRD / homologous-recombination status — RESOLVED: BRCA wild-type + genomically unstable.
   PARP rationale is now genomic-instability-based, NOT BRCA-gated. niraparib (PRIMA,
   all-comers) is the cleanest fit; rucaparib (ATHENA-MONO ITT) also all-comers. olaparib
   monotherapy (SOLO1) FORECLOSED (BRCA WT). olaparib+bevacizumab (PAOLA-1) contingent on a
   validated GIS (MyChoice >=42) Altera does not provide. RANK 1.
2. VEGF / angiogenesis — already on bevacizumab; anti-angiogenic maintenance axis.
3. ER expression (ER+/PR-) — endocrine option (aromatase inhibition / letrozole).
4. IL-12 / tumor immune microenvironment — on-study GEN-1/IMNN-001; immunotherapy-combo context.
5. PIK3CA amplification (somatic) — low-priority investigational; PI3K-pathway early-phase
   baskets (NCT05216432, NCT05683418).
6. MAP2K4 deletion (somatic) — low-priority investigational; early-phase baskets
   (NCT03340506, NCT03454035, NCT05557045, NCT05691504).
7. HER2-low expression (IHC 1+) — investigational [ADDED 2026-06 re-run]. Reclassified from
   out-of-scope to in-scope under Libby HER2-low handling guidance: IHC 1+ is HER2-low, an
   actionable expression tier. Tumor-agnostic T-DXd approval is IHC 3+ ONLY, so any HER2 ADC
   in this HER2-low ovarian tumor is INVESTIGATIONAL, supported by cross-tumor extrapolation
   from breast HER2-low evidence (DESTINY-Breast04 enrolled IHC 1+). Capture each trial's HER2
   cutoff. T-DXd basket (DESTINY-PanTumor02) gates at IHC 2+/3+, so patient does NOT meet it;
   disitamab vedotin solid-tumor baskets (NCT06003231, NCT06660511) accept IHC 1+ -> actionable.

## Out of scope (mechanism-scope rule)
- olaparib monotherapy / SOLO1 — BRCA-mutation-gated, patient is BRCA WT. DROP as fit (none).
- Mirvetuximab soravtansine / FRalpha ADCs — FOLR1 below PS2+ threshold. DROP as fit.
- MSI-high / TMB-high tumor-agnostic checkpoint baskets — MSS + TMB-low. DROP as fit.
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
    - IL-12: GEN-1 / IMNN-001 (Imunon), other IL-12 immunotherapy ovarian.
    - PIK3CA / MAP2K4: biomarker-matched solid-tumor early-phase baskets (investigational, low-priority).

## Sources
1. ClinicalTrials.gov v2 API (primary discovery).
2. PubMed E-utilities (pivotal trial publications).
3. Europe PMC fallback.

## Fit / toxicity computation
- efficacy_toxicity_weight 0.7 (efficacy-leaning, tolerability-aware, age 70-79, ECOG 1).
- Vetoes: additional peripheral neuropathy; severe myelosuppression / febrile neutropenia.
- Modality: oral / low-infusion-burden preferred; caution with thrombotic / bleeding risk
  (high VTE history, prior IVC filter) — flag bevacizumab/anti-angiogenic VTE+bleeding.
- HRD RESOLVED -> niraparib/rucaparib (all-comers) score "strong"; PAOLA-1 (olaparib+bev)
  capped at "partial" pending a validated GIS; olaparib monotherapy/SOLO1 scored "none" (BRCA WT).
- PIK3CA / MAP2K4 basket rows scored "weak" (investigational, low-priority, biomarker-match only).
