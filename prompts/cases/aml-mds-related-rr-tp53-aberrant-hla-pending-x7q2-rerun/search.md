# Search spec — aml-mds-related-rr-tp53-aberrant-hla-pending-x7q2-rerun

Patient: AML-MR (transformed from MDS/RCMD), relapsed/refractory, ~6 y after
matched-sibling PBSC allo-HCT, refractory to FLAG-IDA + venetoclax, right-thigh
extramedullary myeloid sarcoma. Female, 50-59, ECOG 1. Curative intent,
efficacy-leaning (0.75), no toxicity vetoes, trials acceptable including travel.

The explicit reason for the run is the HLA-restricted cellular-therapy axis. The
HLA-A*02:01 typing and HA-1/HA-2 genotypes are pending, so the primary handle is
a *restriction / platform* — every HLA-A*02:01-gated agent is in scope under the
restriction-handle rule, whatever its specific peptide.

## Axes

### A. Tumor + line + biomarker
R/R AML-MR, post allo-HCT, second-transplant / salvage cellular platforms.

### B. Biomarker / target / restriction alone (basket + pan-myeloid)
- HLA-A*02:01 / A*24:02 restriction (master switch, currently pending) — the
  eligibility gate driving the Step 1.75 sweep
- HA-1 / HA-2 minor histocompatibility antigen mismatch (recipient+/donor-)
- WT1, PRAME antigen expression
- CD123-positive blasts (qualitative +; quant density pending)
- CD33-positive blasts (qualitative +; quant density pending)
- TP53 aberration, Y220C-contingent (Y220C unknown; TP53 status itself pending)
- KMT2A amplification (menin rationale — weak; amplification != rearrangement)

### C. Drug / mechanism searches (across tumor types where needed)
- HA-1/HA-2 TCR-T: TSC-100, TSC-101 (ALLOHA NCT05473910), Bleakley HA-1 TCR-T
  (NCT03326921), BSB-1001 (NCT06704152)
- WT1 TCR-T: FH-WT1-E50 (NCT07645469), Chapuis WT1-TCRc4, A*24:02 WT1-siTCR
  (Tawara/TBI-1301), NTLA-5001
- PRAME / multi-TAA: BPX-701, TAA-T (PRAME/WT1/Survivin, NCT02203903)
- Mutant-NPM1 TCR-T (HLA-A*02:01-gated; antigen absent if NPM1-WT):
  MB-dNPM1-TCR.1 (NCT06424340), BSB-2002 (NCT07566585)
- TCR-mimetic / shared-handle engagers: CBX-250 (CG1/HLA-A*02:01, CROSSCHECK,
  NCT06994676)
- CD123: tagraxofusp, pivekimab sunirine (IMGN632), flotetuzumab, vibecotamab,
  CD123 CAR-T / CAR-NK, dual CD33xCD123 (CD123-CD33 cCAR, CLL-1/CD33/CD123 CAR)
- CD33: gemtuzumab ozogamicin; dual CD33xCD123
- TP53 Y220C: rezatapopt / PC14586 (PYNNACLE NCT04585750; myeloid NCT06616636);
  eprenetapopt / APR-246 (low-yield, failed phase 3)
- Allograft platform: Iomab-B / 131I-apamistamab (SIERRA NCT02665065; successor
  NCT07157514), FLAMSA-RIC HCT2, sibling DLI
- Menin inhibitors (KMT2A-amplification, weak rationale): revumenib (AUGMENT-101
  NCT04065399), ziftomenib (COMET-001 NCT04067336)

## Scope gate
Every kept row's drug mechanism traces to a nominated targetable feature
(HLA-restricted mHAg/WT1/PRAME, CD123, CD33, TP53-Y220C, allograft platform, or
KMT2A) OR rides the nominated HLA-A*02:01 restriction under the restriction-handle
rule. HLA-A*02:01-gated agents whose antigen the patient lacks (mutant-NPM1 TCR-T,
patient NPM1-WT) are kept for pipeline completeness but rated weak with the
target-absence caveat spelled out. Menin rows carry the amplification-vs-
rearrangement caveat.

## Step 1.75 eligibility-gate sweep
Queried ClinicalTrials.gov by the HLA-A*02:01 gate (and tokenization variants
"HLA-A2", "A*02:01", "HA-1 antigen", "PRAME", "WT1 TCR") against AML condition,
recruiting/not-yet-recruiting. Reconciled against the roster; net-new vs the prior
run: MB-dNPM1-TCR.1 (NCT06424340), BSB-2002 (NCT07566585), TAA-T (NCT02203903).

## Sources
ClinicalTrials.gov v2 API (primary), PubMed E-utilities, target-specific reviews.
