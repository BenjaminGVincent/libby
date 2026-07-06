# Search spec — aml-mds-related-rr-tp53-aberrant-hla-pending-x7q2

Patient: AML-MR (transformed from MDS/RCMD), relapsed/refractory, ~6 y after
matched-sibling PBSC allo-HCT, refractory to FLAG-IDA + venetoclax, right-thigh
extramedullary myeloid sarcoma. Female, 50-59, ECOG 1. Curative intent,
efficacy-leaning (0.75), no toxicity vetoes, trials acceptable including travel.

The primary reason for the run is the HLA-restricted cellular-therapy axis.

## Axes

### A. Tumor + line + biomarker
R/R AML-MR, post allo-HCT, second-transplant / salvage cellular platforms.

### B. Biomarker / target alone (basket + pan-myeloid)
- HLA-A*02:01 / A*24:02 restriction (master switch, currently pending)
- HA-1 / HA-2 minor histocompatibility antigen mismatch (recipient+/donor-)
- WT1, PRAME antigen expression
- CD123-positive blasts (qualitative +; quant density pending)
- CD33-positive blasts (qualitative +; quant density pending)
- TP53 aberration, Y220C-contingent (Y220C unknown; TP53 status itself pending)
- KMT2A amplification (menin-inhibitor rationale — weak; amplification ≠ rearrangement)

### C. Drug / mechanism searches (across tumor types where needed)
- HA-1/HA-2 TCR-T: TSC-100, TSC-101 (ALLOHA NCT05473910), Bleakley HA-1 TCR-T
  (NCT03326921), BSB-1001 (NCT06704152)
- WT1 TCR-T: FH-WT1-E50 (NCT07645469), Chapuis WT1-TCRc4, A*24:02 WT1-siTCR (Tawara),
  NTLA-5001
- PRAME TCR-T: BPX-701
- CD123: tagraxofusp, pivekimab sunirine (IMGN632), flotetuzumab, vibecotamab,
  CD123 CAR-T / CAR-NK, dual CD33xCD123 (CD123-CD33 cCAR, CLL-1/CD33/CD123 CAR)
- CD33: gemtuzumab ozogamicin; dual CD33xCD123
- TP53 Y220C: rezatapopt / PC14586 (PYNNACLE NCT04585750; myeloid NCT06616636);
  eprenetapopt / APR-246 (low-yield, note the failed phase 3)
- Allograft platform: Iomab-B / 131I-apamistamab (SIERRA NCT02665065; successor
  NCT07157514), FLAMSA-RIC HCT2, sibling DLI
- Menin inhibitors (KMT2A-amplification, weak rationale): revumenib (AUGMENT-101
  NCT04065399), ziftomenib (COMET-001 NCT04067336)

## Scope gate
Every kept row's drug mechanism must trace to a nominated targetable feature
(HLA-restricted mHAg/WT1/PRAME, CD123, CD33, TP53-Y220C, allograft platform, or
KMT2A). Biomarker-gated cellular rows are tagged with their pending HLA/HA/Y220C
prerequisites. Menin rows carry the amplification-vs-rearrangement caveat.

## Sources
ClinicalTrials.gov v2 API (primary), PubMed E-utilities, target-specific reviews.
