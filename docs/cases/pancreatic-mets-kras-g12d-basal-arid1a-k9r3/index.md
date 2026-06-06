<meta name="robots" content="noindex">

# `pancreatic-mets-kras-g12d-basal-arid1a-k9r3`

<!-- libby:case-output:begin -->

## Case output

- [Target validation paths (PDF)](pancreatic-mets-kras-g12d-basal-arid1a-k9r3-target-validation.pdf?v=8ea0ad75) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table (HTML)](pancreatic-mets-kras-g12d-basal-arid1a-k9r3-recommendations.html?v=28af508b) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide (HTML)](accessibility.md?v=81963249) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, sortable in-browser
- [Access guide (offline HTML)](pancreatic-mets-kras-g12d-basal-arid1a-k9r3-accessibility.html?v=4a04da67) — same access-guide content as the in-browser page, packaged as a self-contained HTML that opens offline
- [Master manuscripts table (HTML)](manuscripts.md?v=3f80e7af) — every paper considered — n, effect, variance, toxicities, sortable in-browser
- [Master manuscripts table (offline HTML)](pancreatic-mets-kras-g12d-basal-arid1a-k9r3-manuscripts.html?v=054c3258) — same manuscripts inventory as the in-browser page, packaged as a self-contained HTML that opens offline
- [Patient/caregiver PDF](pancreatic-mets-kras-g12d-basal-arid1a-k9r3-plain-language.pdf?v=539bfeef) — plain-language summary

<!-- libby:case-output:end -->
## Research question

In newly diagnosed metastatic basal-like pancreatic adenocarcinoma (large primary plus multiple >1 cm liver metastases, treatment-naive), what interventions could target KRAS G12D or the ARID1A loss-of-function synthetic-lethal axis?

## Patient profile (scrubbed)

- **Primary site / histology:** pancreas — pancreatic ductal adenocarcinoma; PurIST RNA signature classifies it as the basal-like subtype
- **Stage:** IV (metastatic) — large primary pancreatic mass with multiple liver metastases each >1 cm
- **Performance status:** ECOG 1 (assumed — not supplied, decision-critical at 79)
- **Age band:** 70-79
- **Sex:** male
- **Biomarkers (all confirmed on Tempus plasma/germline/RNA profiling):**
    - **KRAS G12D** — mutated, Tempus xF (plasma ctDNA). The lead driver.
    - **MLH1** — somatic mutation reported; single MMR-gene variant in an MSS, TMB-8.6, germline-negative tumor. Most likely MMR-proficient biology (see cross-cutting caveat).
    - **SMAD4** — E520* stop-gain (predicted loss of function); poor-prognosis, metastasis-associated co-alteration.
    - **TP53** — Y126S and A138V missense; near-universal PDAC co-mutation context.
    - **ARID1A** — frameshift (predicted loss of function); the secondary synthetic-lethal axis.
    - **TMB** — 8.6 mut/Mb, below the >=10 threshold for the tumor-agnostic pembrolizumab TMB-high label.
    - **Microsatellite status** — MSS.
    - **PurIST subtype** — basal-like.
    - **Germline** — no variants detected (Tempus xG); no BRCA1/2, PALB2, ATM, or Lynch germline finding.
    - **Rearrangements** — none (Tempus xR); no NRG1, NTRK, ALK, ROS1, RET, FGFR, or BRAF fusion.
    - **HLA class I** — A*01:01, A*02:01, B*37:01, B*44:02, C*05:01, C*06:02. Not C*08:02.
    - **Incidental xR variants** — ABCC3, ASXL1 (frameshift), BCL7A, BCLAF1, LRP1B. ASXL1 flagged for CHIP adjudication.
- **Prior therapy:** none (treatment-naive assumed from a newly diagnosed presentation)
- **Current therapy:** none

## Preferences

- **Efficacy/toxicity weight:** 0.50 (neutral)
- **Toxicity vetoes:** none
- **Modality constraints:** none
- **Free text:** rich molecular profile but no stated patient preferences or goals-of-care. ECOG 1, US geography, and treatment-naive status all assumed and flagged to the treating team; the author notes a neutral 0.5 weight probably understates how toxicity-averse a 79-year-old would be, which would tilt the ranking if a real preference were captured.
- **Trials preferred:** yes

<!-- libby:target-validation:begin -->

## Target validation paths

This case turns on tissue. The molecular profile came from plasma, and two assays carry the most weight before any feature-targeting therapy is chosen: MMR protein IHC, which settles whether the immunotherapy door is open or closed, and a tissue NGS confirmation of the plasma KRAS G12D call, which the RAS(ON) inhibitor trials require to enroll. Two more assays harden the secondary axis and the trial paperwork: ARID1A/BAF250a IHC and high-resolution HLA class I typing. If MMR IHC shows retained protein, the dMMR/MSI-H checkpoint route stays closed and that low-yield option drops off the table without a wasted treatment course.

### MLH1 / mismatch-repair status

Order MMR protein IHC for MLH1, PMS2, MSH2, and MSH6 on tumor tissue first. This is the gate on the whole immunotherapy question. The plasma call is a single somatic MLH1 variant in an MSS, TMB-8.6, germline-negative tumor, which usually means MMR is still proficient. Protein IHC settles it directly by showing retained versus lost nuclear staining, and retained expression argues against single-agent checkpoint blockade and closes the dMMR/MSI-H pembrolizumab and dostarlimab door. Read MLH1 and PMS2 together, since PMS2 is unstable without MLH1, and use the four-antibody panel rather than a PMS2/MSH6-only screen because the variant of interest sits in MLH1. IHC and MSI can disagree: a missense variant can leave a functional protein, and roughly 6% of MSI-H tumors retain MMR protein (pmid:32152268). Turnaround is 3 to 7 days once a block is in hand.

### KRAS G12D

A tissue comprehensive genomic profile confirming KRAS G12D, with SMAD4, TP53, ARID1A, and MLH1 co-calls, is the second essential test. The driver came from plasma ctDNA, but the RAS(ON) inhibitor protocols want the mutation pathologically documented on tissue, so this confirmation hardens eligibility for daraxonrasib via NCT06625320, zoldonrasib, and MRTX1133, and rules out a ctDNA artifact before a trial slot is committed. The same report re-confirms the SMAD4, TP53, and ARID1A co-alterations that drive the rest of this workup, and the SMAD4 loss and TP53 status ride along for free as prognostic context. If no archival block exists, this row drives the decision about a liver-met core; weigh that against any biopsy reluctance with the treating team. Turnaround is 2 to 3 weeks from block receipt.

### ARID1A

ARID1A/BAF250a IHC is high priority because the synthetic-lethal trials define ARID1A deficiency by loss of BAF250a protein, not by the DNA frameshift. In the ceralasertib study, only 67% (28/42) of ARID1A-mutant tumors showed BAF250a loss, so the frameshift call alone does not predict protein loss (pmid:41686845). This is the test that actually gates ATR-inhibitor entry on NCT03682289 and the EZH2 baskets such as NCT05023655. It runs off the same block as the MMR IHC with a 3 to 7 day turnaround. Many ARID1A baskets accept either a pathogenic mutation or BAF250a loss, but IHC loss is the stronger eligibility token where a protocol requires protein-level deficiency.

### HLA-restricted KRAS immunotherapy

High-resolution HLA class I typing (A, B, C) by sequence-based typing documents the decision-relevant negative already in the file: the patient is HLA-C*05:01/C*06:02, not C*08:02, so the published C*08:02-restricted anti-KRAS-G12D TCR-T (NT-112 via NCT06218914; NCI NCT06690281) does not apply and should not be pursued. A clinical-grade, ASHI-accredited type satisfies trial enrollment paperwork and lets the screener match A*02:01- and A*01:01-restricted KRAS programs cleanly rather than relying on the research call alone. No tumor is needed: 5 to 10 mL of whole blood in EDTA or a buccal swab, with a 1 to 2 week turnaround.

### SMAD4 and TP53 co-mutations

Two lower-priority blood-based steps round out the picture. Paired peripheral-blood-cell (buffy coat) sequencing adjudicates the plasma ASXL1 frameshift as clonal hematopoiesis versus tumor. ASXL1 is one of the top three CHIP genes, and a frameshift seen only in plasma cannot be assigned to tumor versus blood by VAF alone (pmid:32814631). If it is CHIP, drop it from the target list and the TMB accounting; this bundles with the whole-blood draw for HLA typing. The SMAD4 E520* loss and TP53 status come for free on the tissue NGS report already ordered for the KRAS confirmation, so order no separate assay for them. SMAD4 loss tracks with a metastasis-dominant, poorer-prognosis pattern and sharpens prognosis and DDR/cell-cycle trial stratification rather than naming a drug.

### Where to order these assays

| Assay | Provider | Decision gated | Contact |
|---|---|---|---|
| **Mismatch-repair protein IHC (MLH1, PMS2, MSH2, MSH6) on tumor tissue** | **Tempus *(preferred)* (MMR IHC reflex on xT/xF profiling)** | **Pembrolizumab/dostarlimab on the dMMR/MSI-H tumor-agnostic label; retained MMR expression argues against single-agent checkpoint blockade here.** | **[test info](https://www.tempus.com/oncology/) · 600 W Chicago Ave, Suite 510, Chicago, IL 60654 · +1-800-739-4137** |
| Mismatch-repair protein IHC (MLH1, PMS2, MSH2, MSH6) on tumor tissue | Caris Life Sciences *(MI Profile (MMR IHC))* | Pembrolizumab/dostarlimab on the dMMR/MSI-H tumor-agnostic label; retained MMR expression argues against single-agent checkpoint blockade here. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Phoenix, AZ 85040 · +1-888-979-8669 |
| Mismatch-repair protein IHC (MLH1, PMS2, MSH2, MSH6) on tumor tissue | NeoGenomics Laboratories *(MMR/MSI by IHC)* | Pembrolizumab/dostarlimab on the dMMR/MSI-H tumor-agnostic label; retained MMR expression argues against single-agent checkpoint blockade here. | [test info](https://neogenomics.com/) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · +1-866-776-5907 |
| Mismatch-repair protein IHC (MLH1, PMS2, MSH2, MSH6) on tumor tissue | Labcorp / Labcorp Oncology *(MMR protein IHC panel)* | Pembrolizumab/dostarlimab on the dMMR/MSI-H tumor-agnostic label; retained MMR expression argues against single-agent checkpoint blockade here. | [test info](https://www.labcorp.com/) · 358 South Main St, Burlington, NC 27215 · +1-800-845-6167 |
| **Tissue comprehensive genomic profiling (DNA NGS) confirming KRAS G12D, with SMAD4, TP53, ARID1A, MLH1 co-calls** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **RAS(ON) inhibitor trial entry (daraxonrasib/RMC-6236, RMC-9805, MRTX1133) requiring a pathologically documented KRAS G12D.** | **[test info](https://www.foundationmedicine.com/) · 150 Second St, Cambridge, MA 02141 · +1-888-988-3639** |
| Tissue comprehensive genomic profiling (DNA NGS) confirming KRAS G12D, with SMAD4, TP53, ARID1A, MLH1 co-calls | Tempus *(Tempus xT (tissue DNA/RNA))* | RAS(ON) inhibitor trial entry (daraxonrasib/RMC-6236, RMC-9805, MRTX1133) requiring a pathologically documented KRAS G12D. | [test info](https://www.tempus.com/oncology/) · 600 W Chicago Ave, Suite 510, Chicago, IL 60654 · +1-800-739-4137 |
| Tissue comprehensive genomic profiling (DNA NGS) confirming KRAS G12D, with SMAD4, TP53, ARID1A, MLH1 co-calls | Caris Life Sciences *(MI Cancer Seek / WES+WTS)* | RAS(ON) inhibitor trial entry (daraxonrasib/RMC-6236, RMC-9805, MRTX1133) requiring a pathologically documented KRAS G12D. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Phoenix, AZ 85040 · +1-888-979-8669 |
| Tissue comprehensive genomic profiling (DNA NGS) confirming KRAS G12D, with SMAD4, TP53, ARID1A, MLH1 co-calls | MSK-IMPACT (Memorial Sloan Kettering) *(MSK-IMPACT)* | RAS(ON) inhibitor trial entry (daraxonrasib/RMC-6236, RMC-9805, MRTX1133) requiring a pathologically documented KRAS G12D. | [test info](https://www.mskcc.org/) · 1275 York Ave, New York, NY 10065 · +1-833-675-5437 |
| **ARID1A/BAF250a IHC (loss of nuclear expression)** | **NeoGenomics Laboratories *(preferred)* (ARID1A (BAF250a) IHC)** | **ATR inhibitor (ceralasertib) and EZH2 inhibitor (tazemetostat) trials that require BAF250a loss by IHC.** | **[test info](https://neogenomics.com/) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · +1-866-776-5907** |
| ARID1A/BAF250a IHC (loss of nuclear expression) | Tempus *(ARID1A IHC)* | ATR inhibitor (ceralasertib) and EZH2 inhibitor (tazemetostat) trials that require BAF250a loss by IHC. | [test info](https://www.tempus.com/oncology/) · 600 W Chicago Ave, Suite 510, Chicago, IL 60654 · +1-800-739-4137 |
| ARID1A/BAF250a IHC (loss of nuclear expression) | Caris Life Sciences *(ARID1A IHC)* | ATR inhibitor (ceralasertib) and EZH2 inhibitor (tazemetostat) trials that require BAF250a loss by IHC. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Phoenix, AZ 85040 · +1-888-979-8669 |
| ARID1A/BAF250a IHC (loss of nuclear expression) | Labcorp / Labcorp Oncology *(BAF250a (ARID1A) IHC)* | ATR inhibitor (ceralasertib) and EZH2 inhibitor (tazemetostat) trials that require BAF250a loss by IHC. | [test info](https://www.labcorp.com/) · 358 South Main St, Burlington, NC 27215 · +1-800-845-6167 |
| **High-resolution HLA class I genotyping (A, B, C) by sequence-based typing** | **Labcorp / Labcorp Transplant Diagnostics *(preferred)* (HLA class I high-resolution typing)** | **HLA-restricted KRAS G12D TCR-T / cell therapy (e.g. NT-112 via NCT06218914); confirms the patient is not C*08:02 and so is ineligible for the C*08:02-restricted products.** | **[test info](https://www.labcorp.com/) · 358 South Main St, Burlington, NC 27215 · +1-800-845-6167** |
| High-resolution HLA class I genotyping (A, B, C) by sequence-based typing | American Red Cross HLA Laboratory *(High-resolution HLA class I typing)* | HLA-restricted KRAS G12D TCR-T / cell therapy (e.g. NT-112 via NCT06218914); confirms the patient is not C*08:02 and so is ineligible for the C*08:02-restricted products. | [test info](https://www.redcrossblood.org/biomedical-services/immunohematology-reference-laboratories.html) · 100 Edgewood Ave NE, Atlanta, GA 30303 · +1-800-733-2767 |
| High-resolution HLA class I genotyping (A, B, C) by sequence-based typing | Versiti Diagnostic Laboratories *(HLA high-resolution typing)* | HLA-restricted KRAS G12D TCR-T / cell therapy (e.g. NT-112 via NCT06218914); confirms the patient is not C*08:02 and so is ineligible for the C*08:02-restricted products. | [test info](https://www.versiti.org/) · 638 N 18th St, Milwaukee, WI 53233 · +1-800-245-3117 |
| High-resolution HLA class I genotyping (A, B, C) by sequence-based typing | NMDP / Histogenetics (reference HLA) *(SBT high-resolution HLA)* | HLA-restricted KRAS G12D TCR-T / cell therapy (e.g. NT-112 via NCT06218914); confirms the patient is not C*08:02 and so is ineligible for the C*08:02-restricted products. | [test info](https://www.histogenetics.com/) · 300 Collins St, Ossining, NY 10562 · +1-914-682-4020 |
| **Paired peripheral-blood-cell (buffy coat) sequencing to adjudicate the plasma ASXL1 frameshift as CHIP vs tumor** | **Tempus *(preferred)* (Paired tumor/normal (tissue + buffy coat))** | **Whether the plasma ASXL1 frameshift counts as a tumor alteration; CHIP origin removes it from target and biomarker accounting.** | **[test info](https://www.tempus.com/oncology/) · 600 W Chicago Ave, Suite 510, Chicago, IL 60654 · +1-800-739-4137** |
| Paired peripheral-blood-cell (buffy coat) sequencing to adjudicate the plasma ASXL1 frameshift as CHIP vs tumor | Foundation Medicine *(FoundationOne (germline/CHIP filtering))* | Whether the plasma ASXL1 frameshift counts as a tumor alteration; CHIP origin removes it from target and biomarker accounting. | [test info](https://www.foundationmedicine.com/) · 150 Second St, Cambridge, MA 02141 · +1-888-988-3639 |
| Paired peripheral-blood-cell (buffy coat) sequencing to adjudicate the plasma ASXL1 frameshift as CHIP vs tumor | Guardant Health *(Guardant360 (CH annotation))* | Whether the plasma ASXL1 frameshift counts as a tumor alteration; CHIP origin removes it from target and biomarker accounting. | [test info](https://www.guardanthealth.com/) · 3100 Hanover St, Palo Alto, CA 94304 · +1-855-698-8887 |
| **Tissue confirmation of SMAD4 loss and TP53 status (read off the same tissue NGS report)** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Prognostic weighting and DDR/cell-cycle trial stratification; no standalone drug gate.** | **[test info](https://www.foundationmedicine.com/) · 150 Second St, Cambridge, MA 02141 · +1-888-988-3639** |

### Biomarker plan

| Recommended assay | Rationale | Suggested assay provider | Tissue requirements |
|---|---|---|---|
| Mismatch-repair protein IHC (MLH1, PMS2, MSH2, MSH6) on tumor tissue | This is the gate on the whole immunotherapy question. The plasma call is a single somatic MLH1 variant in an MSS, TMB-8.6, germline-negative tumor, which usually means MMR is still proficient; protein IHC on tissue settles it directly by showing retained vs lost MLH1/PMS2 nuclear staining. Skip it and the team is guessing whether the dMMR/MSI-H pembrolizumab label even applies, when retained expression would close that door and spare a low-yield checkpoint course. Roughly 6% of MSI-H tumors retain MMR protein and a missense variant can leave a functional protein, so IHC and MSI can disagree (pmid:32152268). | Tempus *(MMR IHC (reflex on xT/xF profiling))* · [test info](https://www.tempus.com/oncology/) · 600 W Chicago Ave, Suite 510, Chicago, IL 60654 · +1-800-739-4137 | archival FFPE block or unstained slides; no fresh biopsy needed |
| Tissue comprehensive genomic profiling (DNA NGS) confirming KRAS G12D, with SMAD4, TP53, ARID1A, MLH1 co-calls | The KRAS G12D driver came from plasma ctDNA, but the RAS(ON) inhibitor trials want the mutation pathologically documented on tissue, so a tissue NGS confirmation hardens eligibility and rules out a ctDNA artifact before committing to a trial slot. The RMC-9805 and daraxonrasib protocols specify a pathologically documented KRAS mutation, and tissue profiling simultaneously re-confirms the SMAD4, TP53, ARID1A, and MLH1 co-calls that drive the rest of this workup. Without it, a borderline-VAF plasma case risks a screen-fail or a wrong target call at the most decision-heavy step. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/) · 150 Second St, Cambridge, MA 02141 · +1-888-988-3639 | FFPE block or ~10-15 unstained slides; a liver-met core is acceptable if the primary block is unavailable |
| ARID1A/BAF250a IHC (loss of nuclear expression) | The synthetic-lethal trials in ARID1A-deficient tumors define deficiency by loss of BAF250a protein on IHC, not by the DNA frameshift alone, so this is the test that actually gates ATR- and EZH2-inhibitor enrollment. In the ceralasertib study only 67% (28/42) of ARID1A-mutant tumors showed BAF250a loss, so the frameshift call does not reliably predict protein loss (pmid:41686845). Order it and the ATR/EZH2 axis becomes a concrete trial option; skip it and the patient could screen-fail or be enrolled on an unconfirmed target. | NeoGenomics Laboratories *(ARID1A (BAF250a) IHC)* · [test info](https://neogenomics.com/) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · +1-866-776-5907 | archival FFPE block or unstained slides; same block as the MMR IHC can be used |
| High-resolution HLA class I genotyping (A, B, C) by sequence-based typing | The HLA genotype decides which KRAS G12D cell and TCR products can present the epitope, so a clinical-grade, high-resolution A/B/C type is the enrollment token for these programs. It confirms the decision-relevant negative already in the file: the patient is HLA-C*05:01/C*06:02, not C*08:02, so the published C*08:02-restricted anti-KRAS-G12D TCR-T (NT-112, NCT06218914; NCI NCT06690281) does not apply and should not be pursued. A confirmed type also lets the screener match A*02:01- and A*01:01-restricted KRAS programs cleanly instead of relying on the research HLA call alone. | Labcorp / Labcorp Transplant Diagnostics *(HLA class I high-resolution typing)* · [test info](https://www.labcorp.com/) · 358 South Main St, Burlington, NC 27215 · +1-800-845-6167 | 5-10 mL whole blood in EDTA, or a buccal swab; no tumor tissue needed |
| Paired peripheral-blood-cell (buffy coat) sequencing to adjudicate the plasma ASXL1 frameshift as CHIP vs tumor | ASXL1 is one of the top three CHIP genes, and a frameshift seen only in plasma cannot be assigned to tumor versus blood by VAF alone, so paired white-blood-cell sequencing is what separates clonal hematopoiesis from a true tumor variant (pmid:32814631). If the ASXL1 call is CHIP, it should be dropped as a tumor target and not counted toward TMB or trial stratification; if it is also present in tumor tissue, it stays in the co-alteration picture. The same paired analysis flags any other plasma calls that are really hematopoietic in origin. | Tempus *(Paired tumor/normal (tissue + buffy coat))* · [test info](https://www.tempus.com/oncology/) · 600 W Chicago Ave, Suite 510, Chicago, IL 60654 · +1-800-739-4137 | 5-10 mL whole blood for buffy-coat DNA; pairs with the tissue NGS draw |
| Tissue confirmation of SMAD4 loss and TP53 status (read off the same tissue NGS report) | SMAD4 loss tracks with a metastasis-dominant, poorer-prognosis pattern and TP53 inactivation is near-universal in PDAC, so confirming both on tissue mainly sharpens prognosis and DDR/cell-cycle trial stratification rather than naming a drug. These calls come for free on the tissue NGS panel already ordered for KRAS confirmation, so no separate specimen or cost is involved. The value is making sure the prognostic weighting and any combination rationale rest on tissue rather than plasma alone. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/) · 150 Second St, Cambridge, MA 02141 · +1-888-988-3639 | none beyond the tissue NGS block already submitted |

---

*Decision support, not medical advice. Confirm assay availability and current standards with the treating team and the local pathology service.*

<!-- libby:target-validation:end -->

## Scope summary

16 trials surfaced, 13 clinical-evidence rows (4 included as ranked anchors, 9 logged `considered_excluded` as mechanism history or out-of-setting), 8 preclinical rows, and 6 target-validation rows (2 essential `gates_intervention`, 2 high-priority, 2 lower-priority). The ranked list holds 4 therapeutic rows, all `scenario: null` since every biomarker is confirmed, spanning agreement scores from 0.6 to 1.0. All five personas endorsed all four interventions; the disagreement is about order, not membership. Four of five put daraxonrasib at rank 1; the risktaker and advocate would lead with the gentler allele-matched zoldonrasib, and the critic and concensusite dissented on ranking an n=40 phase 1 abstract above the one randomized phase 3. Nobody issued a veto.

## Cross-cutting caveat (read first)

**The immunotherapy axis here is a mirage, and the ranking is scoped to two molecular targets, not the whole first-line conversation.** Three reads shape everything below, and the user should hold them before reading the ranks.

- **The somatic MLH1 variant most likely reflects MMR-proficient biology, so checkpoint-inhibitor monotherapy is low-yield.** A single somatic MLH1 mutation sits alongside MSS status, TMB 8.6 mut/Mb (below the >=10 tumor-agnostic threshold), and a negative germline panel. Pembrolizumab on the dMMR/MSI-H label requires IHC protein loss or an MSI-H call, and neither is present. MMR protein IHC (MLH1/PMS2/MSH2/MSH6) on tissue is the gate that settles it; until it shows loss, do not treat the dMMR/MSI-H label as established here. The relevant immunotherapy biology in this MSS tumor is KRAS-inhibitor-driven FAS/CD8 restoration ([PMID 37625401](https://pubmed.ncbi.nlm.nih.gov/37625401)), which is a reason to favor the small molecules, not a standalone option.
- **The published anti-KRAS-G12D TCR-T does not apply to this patient.** That product is HLA-C*08:02-restricted ([PMID 35648703](https://pubmed.ncbi.nlm.nih.gov/35648703)); this man is C*05:01/C*06:02 (and A*01:01/A*02:01), so it cannot present his mutant epitope. The NT-112 arm of [NCT06218914](https://clinicaltrials.gov/study/NCT06218914) carries the same C*08:02 gate, and the terminated Merck/Moderna mRNA KRAS vaccine required A*11:01 and/or C*08:02 — both screen him out. Every KRAS immunotherapy was matched against his actual class I alleles; only the HLA-agnostic peptide vaccines survive the genotype, and they fail on setting instead.
- **The ASXL1 frameshift may be clonal hematopoiesis, not tumor.** ASXL1 is one of the top three CHIP genes, and a frameshift seen only in plasma cannot be assigned to tumor versus blood by VAF alone. Send paired peripheral-blood-cell (buffy-coat) sequencing before counting it as a tumor target or toward TMB; if it is CHIP, drop it from the target list.
- **The ranking is targetable-feature-scoped.** Only KRAS-G12D-directed agents and the ARID1A synthetic-lethal axis appear below. Standard first-line chemotherapy for metastatic PDAC (mFOLFIRINOX, NALIRIFOX, gem/nab-paclitaxel) carries the NCCN category 1 / 2A endorsement here and is the treating team's call — it does not target the patient's listed molecular features and is out of scope, so it is named only as the backbone the trials build on, not ranked. The basal-like PurIST signal (a debated chemo-backbone consideration) belongs to that same out-of-scope conversation.

## Workup considerations

These steps harden the targetable-feature calls but are diagnostic, not therapeutic, so they sit here rather than in the ranked list. The full per-assay table with providers lives on the Target Validation paths report.

- **MMR protein IHC (MLH1/PMS2/MSH2/MSH6) on tumor tissue — essential.** This is the gate on the whole immunotherapy question. Retained nuclear staining argues against single-agent checkpoint blockade and closes the dMMR/MSI-H pembrolizumab door; IHC and MSI can disagree because a missense variant can leave a functional protein and ~6% of MSI-H tumors retain MMR protein ([PMID 32152268](https://pubmed.ncbi.nlm.nih.gov/32152268)). Read MLH1 and PMS2 together, since PMS2 is unstable without MLH1. Turnaround 3-7 days once a block is in hand.
- **Tissue NGS confirming KRAS G12D (with SMAD4 / TP53 / ARID1A / MLH1 co-calls) — essential.** The driver came from plasma; the RAS(ON) inhibitor trials want the mutation pathologically documented on tissue, which also re-confirms the co-alterations and rules out a ctDNA artifact before a trial slot. If no archival block exists, this drives the decision about a liver-met core.
- **ARID1A/BAF250a IHC — high priority.** The ATR/EZH2 baskets define ARID1A deficiency by BAF250a protein loss, not the frameshift; only ~67% of ARID1A-mutant tumors lose the protein ([PMID 41686845](https://pubmed.ncbi.nlm.nih.gov/41686845)), so this is what actually gates rank 4. Runs off the same block as the MMR IHC.
- **High-resolution HLA class I typing — high priority.** Documents the C*08:02-negative status for trial paperwork and lets the screener match A*02:01- and A*01:01-restricted KRAS programs cleanly. Whole blood or buccal swab; no tumor needed.
- **Paired buffy-coat sequencing for the ASXL1 call — medium priority.** Separates CHIP from a true tumor variant; bundles with the whole-blood draw for HLA typing.

## Intervention grouping

- **Pan-RAS / RAS(ON) class targeting KRAS G12D:** daraxonrasib (RMC-6236) front-line via RASolute 303 ([NCT07491445](https://clinicaltrials.gov/study/NCT07491445)). Anchor evidence: RASolute 302 ([PMID 42223072](https://pubmed.ncbi.nlm.nih.gov/42223072)); Jiang *Cancer Discovery* 2024 ([PMID 38593348](https://pubmed.ncbi.nlm.nih.gov/38593348)).
- **KRAS G12D(ON)-selective inhibitors at the patient's exact allele:** zoldonrasib (RMC-9805) via RASolute 305 ([NCT07621718](https://clinicaltrials.gov/study/NCT07621718)) and the RMC-GI-102 platform ([NCT06445062](https://clinicaltrials.gov/study/NCT06445062)); INCB161734 via DAWN-303 ([NCT07522073](https://clinicaltrials.gov/study/NCT07522073)) and its phase 1 parent ([NCT06179160](https://clinicaltrials.gov/study/NCT06179160)). The discontinued tool compound MRTX1133 ([PMID 36216931](https://pubmed.ncbi.nlm.nih.gov/36216931), [PMID 37625401](https://pubmed.ncbi.nlm.nih.gov/37625401)) anchors the target biology and the FAS/CD8 immune mechanism.
- **ARID1A synthetic-lethal axis (ATR):** ceralasertib (AZD6738) via [NCT03682289](https://clinicaltrials.gov/study/NCT03682289). Mechanism: Williamson *Nat Commun* 2016 ([PMID 27958275](https://pubmed.ncbi.nlm.nih.gov/27958275)).
- **HLA-agnostic KRAS peptide vaccines (mechanism only — adjuvant/MRD setting):** ELI-002 ([PMID 40790272](https://pubmed.ncbi.nlm.nih.gov/40790272), [NCT05726864](https://clinicaltrials.gov/study/NCT05726864)) and the Hopkins pooled vaccine + nivolumab/ipilimumab ([PMID 41667470](https://pubmed.ncbi.nlm.nih.gov/41667470)).

## Top interventions

### Rank 1. daraxonrasib (RMC-6236), pan-RAS(ON) inhibitor — front-line via RASolute 303 (NCT07491445)

*Lead option. Four of five personas put it at rank 1; all five endorsed it. It is the one feature-targeting agent with randomized phase 3 evidence.*

#### Evidence base

RASolute 302 ([PMID 42223072](https://pubmed.ncbi.nlm.nih.gov/42223072), [NCT06625320](https://clinicaltrials.gov/study/NCT06625320)) is the load-bearing anchor: a randomized open-label phase 3 (n=500) in previously treated metastatic RAS-mutant PDAC that hit its registered OS endpoint, HR 0.40 (95% CI 0.30-0.53, p=4.6e-11), with median OS 13.2 vs 6.7 months, mPFS 7.2 vs 3.6 months, and ORR 31.6% vs 11.2%. The patient's KRAS G12D sits inside the RAS G12 subgroup (HR 0.40, 95% CI 0.30-0.54), which makes up ~92% of the trial — but that is a stratum estimate, not a pre-specified per-allele analysis. Two limits matter: the trial reads out at second line while this man is treatment-naive, so the first-line claim rests on the unread RASolute 303 ([NCT07491445](https://clinicaltrials.gov/study/NCT07491445)); and RoB2 rates the open-label design "Some," so the PFS and ORR signals carry performance and treatment-switch bias even where OS as a hard endpoint is largely insulated. Preclinical regression is replicated across 22 PDAC mouse-clinical-trial models (64% objective response, [PMID 38593348](https://pubmed.ncbi.nlm.nih.gov/38593348)).

#### Likelihood of desired effect

High in the 2L RAS G12 population that produced the HR. The 0.40 hazard ratio with a hard OS endpoint at p=4.6e-11 is the strongest efficacy signal on the KRAS axis anywhere in this dossier, and the pan-RAS mechanism covers any subclonal RAS escape his ctDNA has not yet surfaced. The open question is whether that benefit holds at first line in a treatment-naive 79-year-old, which is exactly what RASolute 303 will measure and has not yet reported. The allele-specific estimate is borrowed from the G12 stratum rather than measured directly for G12D.

#### Toxicity profile

- Grade >=3 treatment-related AEs 43.6%, below chemotherapy's 57.5% in the same trial
- Grade >=3 rash 14% — the most frequent grade >=3 event; EGFR-inhibitor management playbook applies
- Grade >=3 stomatitis 12%
- TRAE-driven discontinuation 1.2% (chemo arm 11.2%)
- The grade >=3 profile was measured in pretreated patients; a treatment-naive 79-year-old on a longer front-line course has not been characterized, and mucocutaneous toxicity drives dose reductions in an older patient even with a good algorithm. The user logged no toxicity vetoes, so nothing here is disqualifying on stated preferences.

#### Counter-productive mechanisms / dissent

The risktaker dissented on preference-fit in round 2: their own notes concede the neutral 0.5 weight understates a 79-year-old's likely toxicity aversion, and prefers_trials does not separate daraxonrasib from the gentler allele-matched zoldonrasib since both recruit front-line. The conservative, critic, and concensusite all qualified rather than dissented — they share the rank-1 placement but press the same gap: the safety and efficacy data that earn this pick its grade were measured at 2L, not in the population the patient is actually in. The concensusite added that proximity-to-future-listing and the FDA Breakthrough Therapy Designation are a regulatory flag, not evidence, and the rank should rest on the trial result. No mechanism-level antagonism of the therapeutic goal was raised, and no veto.

#### Practical considerations

RASolute 303 is recruiting, enrolls treatment-naive metastatic PDAC, and accepts KRAS G12D under its RAS-mutant criterion — a three-arm design (daraxonrasib mono vs daraxonrasib + gem/nab-paclitaxel vs gem/nab-paclitaxel). The agent is oral and continuous, which is worth flagging at 79 even though the modality field is silent. No NCCN category applies yet (NCCN Pancreatic Adenocarcinoma v2.2025 lists no KRAS G12D agent), so the treating team should frame consent around proximity-to-guideline and trial enrollment, the route NCCN names as preferred for an actionable finding. Tissue NGS confirmation of the ctDNA call strengthens the eligibility token.

#### Why this rank

Rank 1 because it is the only feature-targeting option carrying a positive randomized phase 3, and four of five personas placed it there. The gap to rank 2 is real but narrow: zoldonrasib matches the exact allele and is gentler, but its evidence is a single-arm n=40 abstract, so the randomized survival result outweighs the tolerability edge on a neutral preference weight. If a toxicity-averse preference were captured for this 79-year-old, the risktaker and advocate would flip these two.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| daraxonrasib (RMC-6236) front-line, 3-arm | OS readout pending; enrolls treatment-naive PDAC at the patient's line | Pan-RAS rash/GI; chemo-combo arm adds cytopenias | [NCT07491445](https://clinicaltrials.gov/study/NCT07491445) |
| daraxonrasib vs chemo, 2L (RASolute 302) | OS HR 0.40 (95% CI 0.30-0.53); mOS 13.2 vs 6.7 mo; ORR 31.6% | G3+ rash 14%, stomatitis 12%; G3+ TRAE 43.6% | [PMID 42223072](https://pubmed.ncbi.nlm.nih.gov/42223072) |
| RMC-GI-102 platform (RMC-6236 ± RMC-9805, ± chemo) | Safety / ORR; G12D PDAC subprotocols | Cohort-defined | [NCT06445062](https://clinicaltrials.gov/study/NCT06445062) |

---

### Rank 2. zoldonrasib (RMC-9805), KRAS G12D(ON)-selective inhibitor — front-line via RASolute 305 (NCT07621718)

*The allele-matched, gentlest agent in the set. All five endorsed it; the critic and concensusite dissented on ranking it above the randomized daraxonrasib evidence.*

#### Evidence base

The clinical read is a phase 1 dose-escalation/expansion ([NCT06040541](https://clinicaltrials.gov/study/NCT06040541)), single-arm, n=40, reported as an ASCO GI 2025 abstract ([DOI 10.1200/JCO.2025.43.4_suppl.724](https://doi.org/10.1200/JCO.2025.43.4_suppl.724)): ORR 30% with 80% disease control in KRAS G12D PDAC at the patient's exact allele. The abstract gives no 95% CI on that response rate and no mature PFS or DoR, so durability is unmeasured. This is the G12D(ON)-selective tri-complex agent, distinct from pan-RAS daraxonrasib; the covalent chemistry that buys G12D selectivity is described in Knox *Science* 2025 ([DOI 10.1126/science.ads0239](https://doi.org/10.1126/science.ads0239)). The front-line phase 3 RASolute 305 ([NCT07621718](https://clinicaltrials.gov/study/NCT07621718), n=670) builds on it, randomizing zoldonrasib + investigator's-choice chemo against placebo + chemo.

#### Likelihood of desired effect

Moderate, and allele-matched in a way daraxonrasib's pooled estimate is not. The 30% ORR was measured directly in G12D PDAC, but an uncontrolled n=40 cannot separate drug effect from selection, and without a time-to-event readout the durability is unknown. RASolute 305 is the randomized double-blind trial that could convert this signal into real evidence; today it is a promising abstract. A negative read on durability when PFS matures is the live downside.

#### Toxicity profile

- No grade 4 or 5 treatment-related events at 1200 mg/day — the cleanest profile in the dossier
- Low-grade GI: nausea 27%, diarrhea 20%, vomiting 15%, rash 10%, almost all grade 1-2
- ALT/AST elevations rare and mostly grade 1
- The RASolute 305 chemo combination has no published dedicated combination-toxicity table, so additive myelosuppression at 79 is unquantified

#### Counter-productive mechanisms / dissent

The advocate endorsed this as the pick to put in front of the patient, reading the free_text's age-79 note as pointing straight at the gentlest agent. The critic and concensusite dissented on the rank: putting an n=40 single-arm abstract at the top inverts the one consensus signal (the randomized daraxonrasib OS result), and a response rate without a time-to-event anchor is the surrogate the critic discounts. Both dissents are about position over the randomized evidence, not about using the drug — the concensusite explicitly said the guideline gives this an endorsed trial pathway and it should sit second, not be discounted toward the floor. The conservative qualified: no veto, the profile is genuinely clean, but they will not co-sign ranking an n=40 phase 1 first on safety when durability is unmeasured.

#### Practical considerations

RASolute 305 is recruiting, requires KRAS G12D specifically, and enrolls treatment-naive metastatic PDAC, so it matches on allele, tumor type, and line. Oral tablets daily. No NCCN category. The first-in-human basket ([NCT06040541](https://clinicaltrials.gov/study/NCT06040541)) enrolls after progression on or intolerance to standard therapy, so it becomes relevant only if the patient is post-first-line or chemo-intolerant. A documented tissue G12D call is the enrollment token. One open biology question: whether the G12D-selective agent reproduces the preclinical FAS/CD8 immune reprogramming seen with the tool compound MRTX1133 ([PMID 37625401](https://pubmed.ncbi.nlm.nih.gov/37625401)) at clinical exposures is untested.

#### Why this rank

Rank 2 because the allele match and tolerability are real advantages, but the evidence base is a single-arm abstract against daraxonrasib's randomized phase 3. On a neutral 0.5 preference weight, the survival result outranks the tolerability edge. Above rank 3 (INCB161734) because both are n~40 phase 1 abstracts at the same evidence level, and the critic reads the 30% vs 37% gap as within-noise — so the tie-break falls to zoldonrasib's cleaner monotherapy profile and the fact that its front-line trial does not bundle the ~40% grade >=3 neutropenia that INCB161734's combination cohort carries.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| zoldonrasib (RMC-9805) phase 1, G12D PDAC | ORR 30%, DCR 80% (n=40; no CI, PFS/DoR immature) | No G4/5; nausea 27%, diarrhea 20%, rash 10% | [DOI 10.1200/JCO.2025.43.4_suppl.724](https://doi.org/10.1200/JCO.2025.43.4_suppl.724) |
| zoldonrasib + chemo vs placebo + chemo, front-line (RASolute 305) | OS readout pending; requires KRAS G12D | Combination toxicity not yet published | [NCT07621718](https://clinicaltrials.gov/study/NCT07621718) |
| RMC-9805 ± RMC-6236 basket, 2L+ | Safety / RP2D / ORR | Cohort-defined | [NCT06040541](https://clinicaltrials.gov/study/NCT06040541) |

---

### Rank 3. INCB161734, KRAS G12D-selective inhibitor — front-line + chemo via DAWN-303 (NCT07522073)

*The strongest single-agent response number on the board, but the enrollable front-line construct bundles chemotherapy. All five endorsed it; the conservative dissented on the combination's marrow toxicity.*

#### Evidence base

A phase 1 monotherapy and chemo-combination study ([NCT06179160](https://clinicaltrials.gov/study/NCT06179160)), single-arm, n=41, reported at ASCO GI 2026 ([DOI 10.1200/JCO.2026.44.2_suppl.654](https://doi.org/10.1200/JCO.2026.44.2_suppl.654)): ORR 37% with 78% disease control in heavily pretreated KRAS G12D PDAC, all with two or more prior lines, with mPFS and mDoR not reached at ~5 months of follow-up. That is the highest single-agent response rate surfaced in G12D PDAC, but ~5 months is too short to call durability either way. The front-line construct the patient would enter, DAWN-303 ([NCT07522073](https://clinicaltrials.gov/study/NCT07522073)), stacks the inhibitor on mFOLFIRINOX or gem/nab-paclitaxel against placebo + chemo.

#### Likelihood of desired effect

Moderate to high as a single agent on response rate, but read it carefully. The 37% ORR comes from a tiny uncontrolled cohort, and the critic reads the numeric gap over zoldonrasib's 30% as within-noise rather than as evidence one agent beats the other. First-line durability is unproven; the signal is from late-line disease, and the bet DAWN-303 makes is that front-line does better. A negative durability readout when PFS matures is the same risk that hangs over zoldonrasib.

#### Toxicity profile

- Grade >=3 neutropenia ~40% in the chemo-combination cohort — the construct the patient would actually enter
- Monotherapy GI toxicity 50-60%, but grade 1-2, with rash and stomatitis notably absent
- No treatment-related deaths
- The combination went onto full-dose chemo without cutting dose intensity, but the ~40% neutropenia is synergistic marrow toxicity with no dedicated combination-safety characterization

#### Counter-productive mechanisms / dissent

The conservative dissented in round 2, setting aside the shared daraxonrasib rank-1 to press the agent their prior flags at 79: the enrollable construct is the chemo combination, and ~40% grade >=3 neutropenia is synergistic marrow toxicity that a neutral 0.5 weight does not shield an older patient from. The critic and concensusite hold it at the same level as zoldonrasib on evidence grade — a single-sponsor phase 1 abstract with immature PFS — and decline to reorder on the response number alone. The favorable monotherapy profile is real, but the front-line arm carries an uncharacterized marrow burden.

#### Practical considerations

DAWN-303 is recruiting, requires KRAS G12D, and enrolls previously untreated metastatic PDAC, so it matches on allele, tumor type, and line; the phase 1 parent ([NCT06179160](https://clinicaltrials.gov/study/NCT06179160)) also takes him front-line and includes combination cohorts with cetuximab, retifanlimab, and gem/nab-paclitaxel. Oral daily plus chemotherapy. A second sponsor's G12D-selective agent broadens the front-line options beyond Revolution Medicines. No NCCN category; enrollable only through the trial, not as standard care.

#### Why this rank

Rank 3, not rank 2, because it sits at the same evidence grade as zoldonrasib (both n~40 phase 1 abstracts) but the enrollable front-line construct bundles chemotherapy with ~40% grade >=3 neutropenia, while zoldonrasib's front-line trial does not carry that documented marrow hit. On a neutral weight the cleaner-route allele-matched agent edges ahead. Above rank 4 by a wide margin: this targets the lead driver directly, while ceralasertib is a cross-tumor extrapolation on the secondary axis.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| INCB161734 monotherapy, pretreated G12D PDAC | ORR 37%, DCR 78% (n=41; PFS not reached at ~5 mo) | GI 50-60% grade 1-2; rash/stomatitis absent | [DOI 10.1200/JCO.2026.44.2_suppl.654](https://doi.org/10.1200/JCO.2026.44.2_suppl.654) |
| INCB161734 + chemo vs placebo + chemo, front-line (DAWN-303) | OS readout pending; requires KRAS G12D | Combination-cohort G3+ neutropenia ~40% | [NCT07522073](https://clinicaltrials.gov/study/NCT07522073) |
| INCB161734 phase 1 parent (mono + combinations) | Safety / ORR / DCR | Cohort-defined | [NCT06179160](https://clinicaltrials.gov/study/NCT06179160) |

---

### Rank 4. ceralasertib (AZD6738), ATR inhibitor (ARID1A synthetic-lethal axis) — via NCT03682289, gated on BAF250a IHC loss

*A mechanistically independent banked second axis off the ARID1A frameshift. Every persona ranked it last; it is the thinnest evidence on the board for this patient.*

#### Evidence base

The clinical read is a phase 2 Simon two-stage monotherapy study ([NCT03682289](https://clinicaltrials.gov/study/NCT03682289), n=29) requiring ARID1A loss by IHC ([PMID 41686845](https://pubmed.ncbi.nlm.nih.gov/41686845)): confirmed ORR 14% (4/29) across all ARID1A-deficient tumors. The 31% figure people quote is a gynecologic-histology subset (endometrioid endometrial, ovarian clear cell), with no pancreatic responder shown. Reading that subset across to basal-like PDAC is cross-tumor extrapolation, and the preclinical ATR-ARID1A work ([PMID 27958275](https://pubmed.ncbi.nlm.nih.gov/27958275)) was done in colorectal and ovarian models with no PDAC line tested. The synthetic-lethal logic is sound — ARID1A loss strands topoisomerase 2A and ATR inhibition forces premature mitotic entry onto the unresolved tangles — but it has not engaged a pancreatic tumor in the clinic.

#### Likelihood of desired effect

Low for this patient. No pancreatic responder exists in the ARID1A clinical data, and the activity concentrates in gynecologic histologies, so the PDAC rationale is inference rather than evidence. The personas keep it on the list as a banked, mechanistically independent shot if the KRAS routes fail, not because the current PDAC signal is strong. It is genuinely a second axis, which is why a treatment-naive man deserves to have it documented; it is not a present recommendation.

#### Toxicity profile

- ATR-class cytopenias — anemia, thrombocytopenia, neutropenia — are the class signature; class anemia is the dose-limiting effect (grade 3 anemia ~26-36% in related agents camonsertib and tuvusertib)
- Per-term grade >=3 rates were not broken out in the abstract; the only number in the toxicity table is zero treatment-related deaths
- The unquantified ATR-class anemia burden is the specific safety gap in a 79-year-old

#### Counter-productive mechanisms / dissent

No persona issued a round-2 dissent or veto on this row, but that silence is not endorsement — the board spent its critiques on the top-tier disagreement among the KRAS agents, and all five ranked ceralasertib last in round 1. The concensusite's round-2 note (directed at the conservative) names the load-bearing problem as guideline fit: no society endorses ATR inhibition for PDAC, and the only positive read is a gynecologic subset with zero pancreatic responders. The mechanism-level risk is that cross-tumor extrapolation may simply not translate to basal-like PDAC, and class anemia limits exposure at 79.

#### Practical considerations

NCT03682289 takes pancreatic tumors stratified by ARID1A status, so it directly targets the secondary axis, but it is active-not-recruiting, so the open door a trials-leaning patient wants is not currently available. Entry is gated on BAF250a IHC loss, and only ~67% of ARID1A-mutant tumors lose the protein, so the ctDNA/tissue frameshift call alone does not confirm eligibility — order the BAF250a IHC before treating this as concrete. The EZH2 arm of this axis lost its lead agent when tazemetostat was withdrawn in March 2026 on an unfavorable benefit-risk read, leaving ATR as the live route. Oral, intermittent schedule.

#### Why this rank

Rank 4 by unanimous round-1 consensus, even though the synthesis formula scores it 1.0 (it drew no round-2 critiques because the personas argued about the KRAS agents instead). That score is an artifact, not a signal that ceralasertib outranks the RAS-directed options — every persona placed it below all three. It is last on evidence grade: cross-tumor extrapolation with no PDAC responder, not-confirmed enrollable, and the enrollable door is closed. It stays on the page because the ARID1A frameshift is a real, independent target worth banking if the KRAS axis fails.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| ceralasertib monotherapy, ARID1A-deficient (phase 2) | ORR 14% (4/29) overall; 31% gynecologic subset; no PDAC responder | ATR-class cytopenias (per-term G3+ unreported); 0 treatment-related deaths | [PMID 41686845](https://pubmed.ncbi.nlm.nih.gov/41686845) |
| ceralasertib ± olaparib or durvalumab, ARID1A-stratified basket | ORR / disease control; takes PDAC | Oral, intermittent | [NCT03682289](https://clinicaltrials.gov/study/NCT03682289) |

---

## Classes examined but not ranked

- **HLA-agnostic KRAS peptide vaccines (ELI-002; Hopkins pooled vaccine + nivolumab/ipilimumab).** These clear the HLA gate the C*08:02-restricted TCR-T fails, and ELI-002's safety is the cleanest in the case (no grade >=3 events across 25 patients, [PMID 40790272](https://pubmed.ncbi.nlm.nih.gov/40790272)). But the data come from resected, minimal-residual-disease PDAC, and this man has a large primary and liver metastases, so the efficacy read does not transfer to bulky metastatic disease. The ELI-002 hazard ratios (RFS HR 0.12, OS HR 0.23) split patients by on-treatment T-cell response, not randomization, so they anchor the vaccine mechanism rather than a metastatic benefit estimate. Excluded on setting, not on biology.
- **HLA-C*08:02-restricted anti-KRAS-G12D TCR-T (NT-112, NCT06218914) and the C*08:02/A*11:01-restricted mRNA KRAS vaccine.** Excluded on HLA mismatch: the patient is C*05:01/C*06:02 and A*01:01/A*02:01, so these products cannot present his mutant epitope ([PMID 35648703](https://pubmed.ncbi.nlm.nih.gov/35648703)). This is the concrete negative behind the case's second judgment call.
- **EZH2 inhibition for the ARID1A axis (tazemetostat).** On-axis mechanism, but the lead agent was withdrawn from all trials in March 2026 after the negative NRG-GY014 read, so the EZH2 route lost both its supporting efficacy signal and its drug. ATR inhibition (rank 4) is the surviving route.
- **MRTX1133, first-generation KRAS G12D-selective inhibitor.** Validated the target and the FAS/CD8 immune mechanism preclinically ([PMID 36216931](https://pubmed.ncbi.nlm.nih.gov/36216931), [PMID 37625401](https://pubmed.ncbi.nlm.nih.gov/37625401)), but the clinical program was terminated for formulation problems, not loss of target validity. Carried forward as mechanism history by zoldonrasib and INCB161734.
- **Single-agent checkpoint blockade (pembrolizumab on the dMMR/MSI-H or TMB-high label).** Foreclosed: MSS, TMB 8.6 (below the >=10 threshold), and a somatic MLH1 variant that most likely reflects MMR-proficient biology. MMR IHC is the gate before any dMMR/MSI-H claim. Not recommended on that label here.

## Ranked prioritization

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Intervention</th><th>Likelihood of effect</th><th>Toxicity burden</th><th>Counter-productive MoA</th><th>Overall</th></tr></thead>
      <tbody>
        <tr>
          <td>1</td>
          <td><strong>daraxonrasib (RMC-6236) pan-RAS(ON) front-line on NCT07491445</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-risktaker">risktaker</span></small></td>
          <td>High in 2L RAS G12 PDAC — OS HR 0.40 (95% CI 0.30-0.53) in RASolute 302 (n=500); first-line benefit inferred from the unread RASolute 303.</td>
          <td>Moderate (rash G3+ 14%, stomatitis G3+ 12%; G3+ TRAE 43.6% overall, below chemo)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(Mucocutaneous toxicity can force dose reductions that erode the exposure the survival signal depends on; no mechanism-level antagonism)</span></td>
          <td><strong>The only feature-targeting option with randomized phase 3 survival evidence; first-line benefit inferred from an unread trial and the allele estimate borrowed from a RAS G12 subgroup.</strong></td>
        </tr>
        <tr>
          <td>2</td>
          <td><strong>zoldonrasib (RMC-9805) G12D-selective front-line on NCT07621718</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small></td>
          <td>Moderate, allele-matched — ORR 30% / DCR 80% in G12D PDAC (phase 1, n=40, no CI; PFS/DoR immature). RASolute 305 will test it front-line.</td>
          <td>Low (nausea 27%, diarrhea 20%, rash 10%; no G4/5 events at monotherapy dose)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(Critic and concensusite dissented on the thin single-arm base; durability unmeasured, so on-target activity may not translate to a durable effect)</span></td>
          <td><strong>The allele-matched, gentlest agent in the set — best tolerability for a 79-year-old, but the evidence is a single-arm n=40 abstract with no durability readout.</strong></td>
        </tr>
        <tr>
          <td>3</td>
          <td><strong>INCB161734 G12D-selective + chemo front-line on NCT07522073 (DAWN-303)</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span></small></td>
          <td>Moderate to high single-agent — ORR 37% / DCR 78% in pretreated G12D PDAC (phase 1, n=41, no CI; PFS not reached at ~5 mo). DAWN-303 tests it front-line.</td>
          <td>High (combination-cohort G3+ neutropenia ~40%; monotherapy GI 50-60% grade 1-2)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(Conservative dissented on additive marrow toxicity: chemo-combination neutropenia can force dose reductions that erode delivered intensity at 79)</span></td>
          <td><strong>Strongest single-agent response number in the dossier, but the enrollable front-line construct bundles chemotherapy with ~40% grade >=3 neutropenia and no dedicated combination-safety data.</strong></td>
        </tr>
        <tr>
          <td>4</td>
          <td><strong>ceralasertib (AZD6738) ATR inhibitor on NCT03682289</strong> (ARID1A axis; gated on BAF250a IHC loss)<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Low for PDAC — confirmed ORR 14% across ARID1A-deficient tumors (PMID 41686845), activity concentrated in gynecologic histologies with zero pancreatic responders shown.</td>
          <td>Moderate (ATR-class anemia / thrombocytopenia / neutropenia; per-term G3+ rates unreported, zero treatment-related deaths)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(Cross-tumor extrapolation with no PDAC responder; the synthetic-lethal effect may not engage in basal-like PDAC, and class anemia limits exposure at 79)</span></td>
          <td><strong>A mechanistically independent banked second axis off the ARID1A frameshift, but no PDAC responder exists, entry is BAF250a-IHC-gated, and the lead basket is not recruiting.</strong></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

!!! note "Reading the columns"
    **Toxicity burden** is patient-level G3+ AE severity (Low / Moderate / High) summarized from the trial publications. **Counter-productive MoA** is the mechanism-level risk that the intervention's own pathway could blunt the therapeutic goal — distinct from patient AEs. The board's endorse / dissent / veto state appears as pills under each intervention; full per-persona rationale lives on the [board page](board.md).

## Caveats

- **Evidence-base caveats.** Only one ranked option carries randomized evidence: daraxonrasib's RASolute 302 ([PMID 42223072](https://pubmed.ncbi.nlm.nih.gov/42223072), n=500, RoB2:Some, open-label, 2L). The other three rest on thinner ground — zoldonrasib and INCB161734 are uncontrolled n=40/n=41 phase 1 conference abstracts with no CI on ORR and immature PFS/DoR, and ceralasertib's only positive read is a post-hoc gynecologic subgroup with zero pancreatic responders. The RoB judgments on the three abstract-stage agents are provisional until full-text publication.
- **Compartment / biomarker dependencies.** Rank 4 (ceralasertib) is contingent on BAF250a IHC loss — the frameshift call alone does not confirm it, and only ~67% of ARID1A-mutant tumors lose the protein. All four ranks assume tissue NGS confirmation of the ctDNA KRAS G12D call, which the RAS(ON) trials require at screening. The immunotherapy axis is foreclosed pending MMR IHC: MSS plus TMB 8.6 plus a somatic MLH1 variant most likely reflects MMR-proficient biology, and the dMMR/MSI-H pembrolizumab label is not established until IHC shows protein loss.
- **What would change the ranking.**
    - The RASolute 303 first-line OS readout landing would convert rank 1's inferred first-line benefit into measured benefit and tighten its confidence.
    - A captured toxicity-averse preference for this 79-year-old would flip ranks 1 and 2 — the risktaker and advocate already read the gentler allele-matched zoldonrasib as the patient-facing lead.
    - A BAF250a IHC showing retained protein would foreclose rank 4 (ceralasertib) entirely, since entry requires protein loss.
    - An MMR IHC showing protein loss would re-open the dMMR/MSI-H immunotherapy axis that is currently foreclosed — a change to the option set, not just the order.
- **Re-scoping caveat.** If performance status proves worse than the assumed ECOG 1, the chemo-combination option (INCB161734 on DAWN-303, with ~40% grade >=3 neutropenia) drops on additive-toxicity grounds, and the willingness to surface aggressive trial-only options narrows; re-run intake if PS, goals-of-care, or a preferred efficacy/toxicity balance become available.

## Sources

**PubMed (PMID):**

- [27958275](https://pubmed.ncbi.nlm.nih.gov/27958275) — Williamson / Lord, ATR inhibition in ARID1A-deficient tumors, *Nat Commun* 2016
- [32152268](https://pubmed.ncbi.nlm.nih.gov/32152268) — MMR IHC vs MSI concordance reference (workup)
- [35648703](https://pubmed.ncbi.nlm.nih.gov/35648703) — Leidner / Tran, HLA-C*08:02-restricted anti-KRAS-G12D TCR-T, *NEJM* 2022
- [36216931](https://pubmed.ncbi.nlm.nih.gov/36216931) — Hallin / Christensen, MRTX1133 target validation, *Nat Med* 2022
- [37625401](https://pubmed.ncbi.nlm.nih.gov/37625401) — Mahadevan / Kalluri, KRAS G12D shutoff restores FAS/CD8 killing, *Cancer Cell* 2023
- [38593348](https://pubmed.ncbi.nlm.nih.gov/38593348) — Jiang / Singh, RMC-6236 translational PDAC across G12 alleles, *Cancer Discovery* 2024
- [40790272](https://pubmed.ncbi.nlm.nih.gov/40790272) — Wainberg / O'Reilly, AMPLIFY-201 final report ELI-002, *Nat Med* 2025
- [41667470](https://pubmed.ncbi.nlm.nih.gov/41667470) — Huff / Zaidi, pooled mKRAS vaccine + nivolumab/ipilimumab, *Nat Commun* 2026
- [41686845](https://pubmed.ncbi.nlm.nih.gov/41686845) — Zhu / Aggarwal, ceralasertib in ARID1A-deficient tumors, *Clin Cancer Res* 2026
- [42223072](https://pubmed.ncbi.nlm.nih.gov/42223072) — O'Reilly / Wolpin, daraxonrasib RASolute 302 in 2L RAS-mutant PDAC, *NEJM* 2026

**ClinicalTrials.gov (NCT):**

- [NCT03682289](https://clinicaltrials.gov/study/NCT03682289) — ceralasertib ARID1A-stratified basket (ATR axis)
- [NCT05726864](https://clinicaltrials.gov/study/NCT05726864) — AMPLIFY-7P (ELI-002 in resected KRAS-mutant solid tumors)
- [NCT06040541](https://clinicaltrials.gov/study/NCT06040541) — zoldonrasib (RMC-9805) first-in-human G12D basket
- [NCT06179160](https://clinicaltrials.gov/study/NCT06179160) — INCB161734 phase 1 parent (mono + combinations)
- [NCT06445062](https://clinicaltrials.gov/study/NCT06445062) — RMC-GI-102 platform (RMC-6236 / RMC-9805 ± chemo)
- [NCT06625320](https://clinicaltrials.gov/study/NCT06625320) — RASolute 302 (daraxonrasib phase 3, 2L+)
- [NCT07491445](https://clinicaltrials.gov/study/NCT07491445) — RASolute 303 (daraxonrasib front-line, 3-arm)
- [NCT07522073](https://clinicaltrials.gov/study/NCT07522073) — DAWN-303 (INCB161734 + chemo front-line)
- [NCT07621718](https://clinicaltrials.gov/study/NCT07621718) — RASolute 305 (zoldonrasib + chemo front-line)

## Transparency artifacts

- [Trial table](trials.md) — 16 rows, all columns
- [Evidence list](evidence.md) — 13 clinical-evidence rows (4 ranked anchors, 9 considered_excluded) + 8 preclinical rows
- [Manuscripts master table](manuscripts.md) — every paper considered with structured n, effect, variance, toxicity columns
- [Tumor-board transcript](board.md) — 5 positions, 20 cross-critiques
- [Recommendations table](recommendations.md) — full ranked detail
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Authored June 2026. Inputs: 16 trials, 13 clinical-evidence rows, 8 preclinical rows, 6 target-validation rows, 5 board positions with 20 cross-critiques. Every biomarker reads as confirmed on the Tempus plasma/germline/RNA profiling, so this is a non-gated case with `scenario: null` on all four recommendation rows and a single unbranched ranking scoped to KRAS-G12D-directed and ARID1A-directed interventions. No workup-hardening row appears in the ranking; the MMR IHC, tissue NGS, BAF250a IHC, HLA typing, and ASXL1 CHIP adjudication are surfaced under Workup considerations and on the Target Validation paths report instead. Three clinical judgment calls are honored throughout: the somatic MLH1 variant most likely reflects MMR-proficient biology (checkpoint monotherapy low-yield, MMR IHC the gate); the patient is HLA-C*05:01/C*06:02, not C*08:02, so the published anti-KRAS-G12D TCR-T does not apply; and the ASXL1 plasma frameshift may be CHIP. ECOG 1, US geography, treatment-naive status, and the neutral 0.5 efficacy/toxicity weight are all assumed and flagged; re-run intake if performance status or goals-of-care become available. Humanizer pass applied to all prose sections per `.claude/skills/humanizer/SKILL.md`.

<!-- libby:downloads:begin -->

## Downloads

### HTML

- [Target validation paths](target_validation.md?v=a767f75d) — per-feature biomarker-workup table with providers and references, sortable in-browser
- [Recommendations table](pancreatic-mets-kras-g12d-basal-arid1a-k9r3-recommendations.html?v=28af508b) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide](accessibility.md?v=81963249) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Access guide (offline)](pancreatic-mets-kras-g12d-basal-arid1a-k9r3-accessibility.html?v=4a04da67) — same access-guide content packaged as a self-contained HTML that opens offline
- [Master manuscripts table](manuscripts.md?v=3f80e7af) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Master manuscripts table (offline)](pancreatic-mets-kras-g12d-basal-arid1a-k9r3-manuscripts.html?v=054c3258) — same manuscripts inventory packaged as a self-contained HTML that opens offline

### PDF

- [Target validation paths](pancreatic-mets-kras-g12d-basal-arid1a-k9r3-target-validation.pdf?v=8ea0ad75) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table](pancreatic-mets-kras-g12d-basal-arid1a-k9r3-recommendations.pdf?v=a47c02a8) — ranked options + pipeline context + evidence in detail, in a print-friendly PDF
- [Access guide](pancreatic-mets-kras-g12d-basal-arid1a-k9r3-accessibility.pdf?v=cc90e1b8) — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF
- [Master manuscripts table](pancreatic-mets-kras-g12d-basal-arid1a-k9r3-manuscripts.pdf?v=7399aa08) — every paper considered — n, effect, variance, toxicities, in a print-friendly PDF
- [Patient/caregiver PDF](pancreatic-mets-kras-g12d-basal-arid1a-k9r3-plain-language.pdf?v=539bfeef) — plain-language summary

<!-- libby:downloads:end -->

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
