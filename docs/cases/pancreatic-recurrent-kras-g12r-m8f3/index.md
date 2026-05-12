<meta name="robots" content="noindex">

# `pancreatic-recurrent-kras-g12r-m8f3`

<!-- libby:downloads:begin -->

## Downloads

### HTML

- [Target validation paths](target_validation.md?v=dc34379c) — per-feature biomarker-workup table with providers and references, sortable in-browser
- [Recommendations table](pancreatic-recurrent-kras-g12r-m8f3-recommendations.html?v=8eeb26f9) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide](accessibility.md?v=2958eb74) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Master manuscripts table](manuscripts.md?v=9ea36b70) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table

### PDF

- [Target validation paths](pancreatic-recurrent-kras-g12r-m8f3-target-validation.pdf?v=65dd4d18) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table](pancreatic-recurrent-kras-g12r-m8f3-recommendations.pdf?v=1e114511) — ranked options + pipeline context + evidence in detail, in a print-friendly PDF
- [Access guide](pancreatic-recurrent-kras-g12r-m8f3-accessibility.pdf?v=24ea5db6) — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF
- [Master manuscripts table](pancreatic-recurrent-kras-g12r-m8f3-manuscripts.pdf?v=f6dd2111) — every paper considered — n, effect, variance, toxicities, in a print-friendly PDF
- [Patient/caregiver PDF](pancreatic-recurrent-kras-g12r-m8f3-plain-language.pdf?v=4ab72e3e) — plain-language summary

<!-- libby:downloads:end -->
## Research question

In recurrent pancreatic adenocarcinoma after adjuvant FOLFIRI, what interventions can target KRAS G12R, CDKN2A loss, and CCND3 alteration in an MSS / sub-threshold-TMB background?

## Patient profile (scrubbed)

- **Primary site / histology:** pancreas — pancreatic adenocarcinoma
- **Stage:** recurrent
- **Performance status:** ECOG 1
- **Age band:** 50-59
- **Sex:** unknown
- **Biomarkers (all confirmed):**
    - **KRAS G12R** by NGS — RAS-GTP-binding-deficient allele; pan-KRAS / RAS(ON) class is the relevant lane, not G12C / G12D-selective agents
    - **TP53** inactivating mutation by NGS — variant class (LOF vs dominant-negative vs GOF) not yet annotated; informs co-mutation context
    - **CDKN2A** loss by NGS / IHC — derepresses CDK4/6; supports CDK4/6 inhibitor rationale; MTAP co-deletion likely (~80-90% co-deletion on 9p21) and reflex-testable
    - **CCND3** alteration by NGS — class refinement pending (amplification vs activating mutation); reinforces CDK4/6 axis
    - **MSI status:** MSS — biomarker-excluded from tumor-agnostic pembrolizumab
    - **TMB:** 4.1 mut/Mb — below the 10 mut/Mb tumor-agnostic pembrolizumab threshold
- **Prior therapy:** FOLFIRI adjuvant; best response PD. Patient is oxaliplatin-naive and platinum-naive.
- **Current therapy:** none

## Preferences

- **Efficacy/toxicity weight:** 0.80 (strong efficacy lean)
- **Toxicity vetoes:** none
- **Modality constraints:** none
- **Free text:** "Treat to remission as the primary goal. Accepts high-risk-high-reward options. Minimize toxicity where possible, but no hard toxicity vetoes."
- **Trials preferred:** yes

<!-- libby:target-validation:begin -->

## Target validation paths

All six biomarkers in this case read as confirmed on the local report, so the workup here hardens the calls rather than gates a fresh diagnosis. The single essential row is orthogonal KRAS G12R confirmation by plasma ctDNA plus a second-platform tissue NGS: pan-RAS and RAS(ON) sponsors re-test the variant on plasma at screening regardless of the local report, and the same draw seeds the baseline VAF used for on-treatment monitoring at cycle 2 and cycle 4. This re-test gates trial entry for daraxonrasib (RMC-6236, NCT05379985), the daraxonrasib + chemo combination platform (NCT06445062), and the zoldonrasib (RMC-7977) + ivonescimab program (NCT07397338). Five high-priority workups run in parallel: a comprehensive germline panel, p16 IHC on the CDKN2A call, CCND3 alteration-class refinement, KRAS co-mutation NGS (SMAD4 / KEAP1 / STK11 / GNAS / ARID1A), and MTAP reflex testing on the 9p21 locus. Six medium-priority workups round out the dossier.

### KRAS G12R

Essential: orthogonal NGS plus baseline ctDNA. Pan-RAS / RAS(ON) trial central labs re-test KRAS G12X on plasma at screening; the orthogonal call locks eligibility for daraxonrasib monotherapy (NCT05379985), daraxonrasib + chemo (NCT06445062), and the RMC-7977 + ivonescimab combination (NCT07397338). Reference platforms are Guardant360 CDx, FoundationOne Liquid CDx, Tempus xF+, Natera Signatera, and Caris Assure; the FDA-approved CDx platforms are the safest choice for trial-entry documentation. G12R is biologically distinct from G12C and G12D (RAS-GTP-binding-deficient per Hobbs 2020), so G12C-specific covalent agents are not the relevant class. Turnaround is one to two weeks.

Three high-priority companions ride on the same NGS order. Co-mutation profiling for SMAD4, KEAP1, STK11, GNAS, and ARID1A frames prognosis and weights any ICI-combination decision: SMAD4 loss in PDAC is the strongest single co-alteration linked to wider metastatic spread, and KEAP1 / STK11 predict diminished ICI benefit on KRAS-mutant backgrounds. A germline hereditary-cancer panel (BRCA1, BRCA2, PALB2, ATM, MLH1, MSH2, MSH6, PMS2, EPCAM, CDKN2A, TP53, STK11) is NCCN-recommended for every PDAC patient regardless of family history. A pathogenic BRCA1 / BRCA2 or PALB2 result opens olaparib maintenance via NCT02184195 plus rucaparib as the platinum-induction-gated PARP follow-on. Germline turnaround is three to six weeks; order in parallel with a genetic-counseling referral.

Two medium-priority resistance reads sit alongside: KRAS copy-number annotation (baseline KRAS amplification and acquired wildtype-KRAS amplification are documented escape mechanisms on the pan-RAS class), and serial KRAS G12R ddPCR or tumor-informed MRD at cycle 2 and cycle 4 of any KRAS-directed therapy, which flags VAF rebound weeks ahead of RECIST imaging.

### TP53

The local report annotates an inactivating mutation, but the functional class matters: pure loss-of-function (truncations, splice) reads differently from dominant-negative missense hotspots (R175H, R248W, R273H) and from gain-of-function variants, and any TP53-restoration or MDM2-axis strategy gates on the precise call. The workup is a same-day re-read of the existing NGS report against the IARC TP53 database for variant annotation in HGVS notation. Does not gate the KRAS axis; refines any downstream cell-cycle / DDR conversation.

### CDKN2A

Two confirmatory reads. p16 IHC (clone E6H4 on archival FFPE, one to two week turnaround) is the orthogonal protein-level check on the NGS copy-number call; CDK4/6-inhibitor trial central labs prefer p16-negative status or biallelic CDKN2A loss for enrollment in CDKN2A-loss-enriched arms. A discordance (NGS-loss but IHC-retained) suggests subclonal or assay-driven calls and tempers expectations for CDK4/6 monotherapy.

Multi-region p16 IHC on a second tumor block (primary plus metastatic site if available) reads PDAC clonal heterogeneity at the next tier. A patchy result does not gate enrollment, but it changes how a CDK4/6-inhibitor response is interpreted and may push the board toward combination strategies.

The 9p21 MTAP reflex (callable from the same NGS panel) is the other operational read: CDKN2A and MTAP are co-deleted in roughly 80 to 90 percent of CDKN2A homozygous deletions, and MTAP co-deletion is the eligibility threshold for the MTA-cooperative PRMT5 class (anvumetostat on NCT06360354, BMS-986504 on NCT07492680). Decisive for any decision on whether the dual-feature daraxonrasib + anvumetostat regimen is on the table.

### CCND3

The local NGS report names a CCND3 alteration without specifying class. An amplification or activating mutation supports cyclin-D-axis dependency and CDK4/6 sensitivity; a passenger missense without copy gain carries weaker mechanistic weight. Cyclin-D-degrader and selective CDK4 programs (PF-07220060, fadraciclib, INCB123667) gate on copy-number gain or known activating mutations, so the class call frames whether these axes belong on the page at all. Usually returnable as an annotation re-read of the existing NGS panel; ask the molecular pathologist for the alteration class explicitly. Turnaround is two to three weeks if a fresh order is required.

### MSS

Two reads to confirm the negative ICI finding. MMR IHC (MLH1, MSH2, MSH6, PMS2 on archival FFPE, one to two week turnaround) is the orthogonal protein-level confirmation on the NGS call. NGS-derived MSI calls have known false negatives at low tumor purity, and most ICI-trial central labs accept MMR IHC on its own. A confirmed MSS by both NGS and IHC closes the door cleanly on the tumor-agnostic pembrolizumab pathway.

The tumor microenvironment workup (PD-L1 22C3, CD3 / CD8 TIL density, alpha-SMA or H and E stromal density) frames any ICI-combination strategy. PDAC is the textbook immune-cold, stromally dense tumor, and the dominant interpretive question is usually T-cell exclusion rather than PD-L1 score. Returnable on a multiplex IHC panel (NeoGenomics MultiOmyx covers PD-L1, CD3, CD8, and stromal markers on a single section).

### TMB

Documentation review rather than a new order. TMB values are sensitive to panel size, mutation-call filters, and whether synonymous variants are included; 4.1 mut/Mb on a 500-gene panel may map differently against the FDA-approved tumor-agnostic pembrolizumab threshold than a whole-exome-derived value (Friends of Cancer Research TMB Project harmonization study). If the existing report is from FoundationOne CDx, this is a same-day documentation check on the bioinformatics methods section. Below the 10 mut/Mb threshold the tumor-agnostic pembrolizumab route is foreclosed; the read confirms that foreclosure cleanly.

### Where to order these assays

| Assay | Provider | Decision gated | Contact |
|---|---|---|---|
| **Orthogonal NGS panel plus ctDNA (KRAS G12R-specific ddPCR or comprehensive plasma NGS)** | **Guardant Health *(preferred)* (Guardant360 CDx)** | **Pan-RAS / RAS(ON) inhibitor trials (RMC-6236 NCT05379985, RMC-7977 NCT06445062); G12C-specific agents are not the relevant class.** | **[test info](https://guardanthealth.com/products/guardant360-cdx/) · 505 Penobscot Drive, Redwood City, CA 94063 · 1-855-698-8887** |
| Orthogonal NGS panel plus ctDNA | Foundation Medicine *(FoundationOne Liquid CDx)* | Pan-RAS / RAS(ON) inhibitor trials (RMC-6236 NCT05379985, RMC-7977 NCT06445062); G12C-specific agents are not the relevant class. | [test info](https://www.foundationmedicine.com/test/foundationone-liquid-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| Orthogonal NGS panel plus ctDNA | Tempus *(Tempus xF+ (plasma) / xT (tissue))* | Pan-RAS / RAS(ON) inhibitor trials (RMC-6236 NCT05379985, RMC-7977 NCT06445062); G12C-specific agents are not the relevant class. | [test info](https://www.tempus.com/oncology/diagnostics/) · 600 West Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| Orthogonal NGS panel plus ctDNA | Natera *(Signatera (tumor-informed MRD))* | Pan-RAS / RAS(ON) inhibitor trials (RMC-6236 NCT05379985, RMC-7977 NCT06445062); G12C-specific agents are not the relevant class. | [test info](https://www.natera.com/oncology/signatera-advanced-cancer-detection/) · 13011 McCallen Pass, Austin, TX 78753 · 1-650-249-9090 |
| Orthogonal NGS panel plus ctDNA | Caris Life Sciences *(Caris Assure)* | Pan-RAS / RAS(ON) inhibitor trials (RMC-6236 NCT05379985, RMC-7977 NCT06445062); G12C-specific agents are not the relevant class. | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| **p16 IHC (clone E6H4 or equivalent)** | **Mayo Clinic Laboratories *(preferred)*** | **CDK4/6-inhibitor eligibility (palbociclib, ribociclib, abemaciclib) and CDKN2A-loss-enriched trial arms.** | **[test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710** |
| p16 IHC (clone E6H4 or equivalent) | ARUP Laboratories | CDK4/6-inhibitor eligibility (palbociclib, ribociclib, abemaciclib) and CDKN2A-loss-enriched trial arms. | [test info](https://www.aruplab.com/) · 500 Chipeta Way, Salt Lake City, UT 84108 · 1-800-242-2787 |
| p16 IHC (clone E6H4 or equivalent) | NeoGenomics Laboratories | CDK4/6-inhibitor eligibility (palbociclib, ribociclib, abemaciclib) and CDKN2A-loss-enriched trial arms. | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| p16 IHC (clone E6H4 or equivalent) | LabCorp / Esoterix Oncology | CDK4/6-inhibitor eligibility (palbociclib, ribociclib, abemaciclib) and CDKN2A-loss-enriched trial arms. | [test info](https://www.labcorp.com/oncology) · 358 South Main Street, Burlington, NC 27215 · 1-800-345-4363 |
| p16 IHC (clone E6H4 or equivalent) | Quest Diagnostics | CDK4/6-inhibitor eligibility (palbociclib, ribociclib, abemaciclib) and CDKN2A-loss-enriched trial arms. | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| **CCND3 alteration-class refinement (amplification vs activating mutation vs fusion) via NGS plus FISH or copy-number array as needed** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **CDK4/6-inhibitor and cyclin-D-degrader trial enrichment (PF-07220060, fadraciclib, INCB123667).** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| CCND3 alteration-class refinement | Caris Life Sciences *(Caris Molecular Intelligence)* | CDK4/6-inhibitor and cyclin-D-degrader trial enrichment (PF-07220060, fadraciclib, INCB123667). | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| CCND3 alteration-class refinement | Tempus *(Tempus xT)* | CDK4/6-inhibitor and cyclin-D-degrader trial enrichment (PF-07220060, fadraciclib, INCB123667). | [test info](https://www.tempus.com/oncology/diagnostics/) · 600 West Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| CCND3 alteration-class refinement | Memorial Sloan Kettering Diagnostic Molecular Pathology *(MSK-IMPACT)* | CDK4/6-inhibitor and cyclin-D-degrader trial enrichment (PF-07220060, fadraciclib, INCB123667). | [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |
| CCND3 alteration-class refinement | NeoGenomics Laboratories *(NeoTYPE Comprehensive Panel)* | CDK4/6-inhibitor and cyclin-D-degrader trial enrichment (PF-07220060, fadraciclib, INCB123667). | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| **Comprehensive tumor NGS including SMAD4, KEAP1, STK11, GNAS, ARID1A** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Frames prognosis under multi-agent therapy and weights any ICI-combo strategy on the KRAS axis.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| Comprehensive tumor NGS | Caris Life Sciences *(Caris Molecular Intelligence)* | Frames prognosis under multi-agent therapy and weights any ICI-combo strategy on the KRAS axis. | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| Comprehensive tumor NGS | Tempus *(Tempus xT)* | Frames prognosis under multi-agent therapy and weights any ICI-combo strategy on the KRAS axis. | [test info](https://www.tempus.com/oncology/diagnostics/) · 600 West Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| Comprehensive tumor NGS | NeoGenomics Laboratories *(NeoTYPE Comprehensive Panel)* | Frames prognosis under multi-agent therapy and weights any ICI-combo strategy on the KRAS axis. | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| Comprehensive tumor NGS | Memorial Sloan Kettering Diagnostic Molecular Pathology *(MSK-IMPACT)* | Frames prognosis under multi-agent therapy and weights any ICI-combo strategy on the KRAS axis. | [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |
| **Germline hereditary-cancer panel covering BRCA1, BRCA2, PALB2, ATM, MLH1, MSH2, MSH6, PMS2, EPCAM, CDKN2A, TP53, STK11** | **Invitae *(preferred)* (Invitae Multi-Cancer Panel)** | **Olaparib maintenance after platinum for germline BRCA-mutant PDAC; family cascade testing; FAMMM-CDKN2A screening.** | **[test info](https://www.invitae.com/en/providers/test-catalog) · 1400 16th Street, San Francisco, CA 94103 · 1-800-436-3037** |
| Germline hereditary-cancer panel | GeneDx *(GeneDx OncoGeneDx)* | Olaparib maintenance after platinum for germline BRCA-mutant PDAC; family cascade testing; FAMMM-CDKN2A screening. | [test info](https://www.genedx.com/tests) · 207 Perry Parkway, Gaithersburg, MD 20877 · 1-888-729-1206 |
| Germline hereditary-cancer panel | Ambry Genetics *(CancerNext)* | Olaparib maintenance after platinum for germline BRCA-mutant PDAC; family cascade testing; FAMMM-CDKN2A screening. | [test info](https://www.ambrygen.com/providers/test-menu) · 1 Enterprise, Aliso Viejo, CA 92656 · 1-866-262-7943 |
| Germline hereditary-cancer panel | Myriad Genetics *(MyRisk Hereditary Cancer)* | Olaparib maintenance after platinum for germline BRCA-mutant PDAC; family cascade testing; FAMMM-CDKN2A screening. | [test info](https://myriad.com/genetic-tests/myrisk-hereditary-cancer/) · 320 Wakara Way, Salt Lake City, UT 84108 · 1-800-469-7423 |
| Germline hereditary-cancer panel | Color Health | Olaparib maintenance after platinum for germline BRCA-mutant PDAC; family cascade testing; FAMMM-CDKN2A screening. | [test info](https://www.color.com/) · 831 Mitten Road, Burlingame, CA 94010 · 1-844-352-6567 |
| **MMR IHC panel (MLH1, MSH2, MSH6, PMS2)** | **Mayo Clinic Laboratories *(preferred)*** | **Confirms the MSS call; closes the door on tumor-agnostic pembrolizumab.** | **[test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710** |
| MMR IHC panel | ARUP Laboratories | Confirms the MSS call; closes the door on tumor-agnostic pembrolizumab. | [test info](https://www.aruplab.com/) · 500 Chipeta Way, Salt Lake City, UT 84108 · 1-800-242-2787 |
| MMR IHC panel | LabCorp / Esoterix Oncology | Confirms the MSS call; closes the door on tumor-agnostic pembrolizumab. | [test info](https://www.labcorp.com/oncology) · 358 South Main Street, Burlington, NC 27215 · 1-800-345-4363 |
| MMR IHC panel | Quest Diagnostics | Confirms the MSS call; closes the door on tumor-agnostic pembrolizumab. | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| MMR IHC panel | NeoGenomics Laboratories | Confirms the MSS call; closes the door on tumor-agnostic pembrolizumab. | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| **TMB assay platform and calling-pipeline confirmation (panel size, filters, harmonization with FDA-approved 10 mut/Mb threshold)** | **Foundation Medicine *(preferred)* (FoundationOne CDx (TMB-harmonized))** | **Confirms sub-threshold TMB and the foreclosure of tumor-agnostic pembrolizumab eligibility.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| TMB assay platform confirmation | Caris Life Sciences *(Caris Molecular Intelligence)* | Confirms sub-threshold TMB and the foreclosure of tumor-agnostic pembrolizumab eligibility. | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| TMB assay platform confirmation | Tempus *(Tempus xT)* | Confirms sub-threshold TMB and the foreclosure of tumor-agnostic pembrolizumab eligibility. | [test info](https://www.tempus.com/oncology/diagnostics/) · 600 West Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| TMB assay platform confirmation | NeoGenomics Laboratories *(NeoTYPE Comprehensive Panel)* | Confirms sub-threshold TMB and the foreclosure of tumor-agnostic pembrolizumab eligibility. | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| TMB assay platform confirmation | Memorial Sloan Kettering Diagnostic Molecular Pathology *(MSK-IMPACT)* | Confirms sub-threshold TMB and the foreclosure of tumor-agnostic pembrolizumab eligibility. | [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |
| **TP53 variant annotation (LOF vs dominant-negative vs gain-of-function) with reference to IARC TP53 database** | **Memorial Sloan Kettering Diagnostic Molecular Pathology *(preferred)* (MSK-IMPACT (with variant annotation))** | **Frames any TP53-restoration or MDM2-inhibitor strategy; does not gate the KRAS axis.** | **[test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000** |
| TP53 variant annotation | Foundation Medicine *(FoundationOne CDx)* | Frames any TP53-restoration or MDM2-inhibitor strategy; does not gate the KRAS axis. | [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| TP53 variant annotation | Tempus *(Tempus xT)* | Frames any TP53-restoration or MDM2-inhibitor strategy; does not gate the KRAS axis. | [test info](https://www.tempus.com/oncology/diagnostics/) · 600 West Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| TP53 variant annotation | Caris Life Sciences *(Caris Molecular Intelligence)* | Frames any TP53-restoration or MDM2-inhibitor strategy; does not gate the KRAS axis. | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| TP53 variant annotation | IARC TP53 Database (annotation reference) | Frames any TP53-restoration or MDM2-inhibitor strategy; does not gate the KRAS axis. | [test info](https://tp53.isb-cgc.org/) · 150 Cours Albert Thomas, 69372 Lyon CEDEX 08, France |
| **p16 IHC across multiple tumor regions (primary site vs metastatic biopsy if available)** | **Mayo Clinic Laboratories *(preferred)*** | **Refines confidence in the CDKN2A loss call for CDK4/6-inhibitor strategy; does not gate enrollment.** | **[test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710** |
| p16 IHC multi-region | ARUP Laboratories | Refines confidence in the CDKN2A loss call for CDK4/6-inhibitor strategy; does not gate enrollment. | [test info](https://www.aruplab.com/) · 500 Chipeta Way, Salt Lake City, UT 84108 · 1-800-242-2787 |
| p16 IHC multi-region | NeoGenomics Laboratories | Refines confidence in the CDKN2A loss call for CDK4/6-inhibitor strategy; does not gate enrollment. | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| p16 IHC multi-region | Memorial Sloan Kettering Diagnostic Molecular Pathology | Refines confidence in the CDKN2A loss call for CDK4/6-inhibitor strategy; does not gate enrollment. | [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |
| p16 IHC multi-region | LabCorp / Esoterix Oncology | Refines confidence in the CDKN2A loss call for CDK4/6-inhibitor strategy; does not gate enrollment. | [test info](https://www.labcorp.com/oncology) · 358 South Main Street, Burlington, NC 27215 · 1-800-345-4363 |
| **Serial KRAS G12R ctDNA quantitation (ddPCR or tumor-informed MRD) at baseline and at cycle 2 / cycle 4 of KRAS-directed therapy** | **Natera *(preferred)* (Signatera (tumor-informed MRD))** | **Early-response and emerging-resistance surveillance on pan-RAS / RAS(ON) inhibitor therapy.** | **[test info](https://www.natera.com/oncology/signatera-advanced-cancer-detection/) · 13011 McCallen Pass, Austin, TX 78753 · 1-650-249-9090** |
| Serial KRAS G12R ctDNA quantitation | Guardant Health *(Guardant Reveal / Guardant360 Response)* | Early-response and emerging-resistance surveillance on pan-RAS / RAS(ON) inhibitor therapy. | [test info](https://guardanthealth.com/) · 505 Penobscot Drive, Redwood City, CA 94063 · 1-855-698-8887 |
| Serial KRAS G12R ctDNA quantitation | Bio-Rad / academic ddPCR core | Early-response and emerging-resistance surveillance on pan-RAS / RAS(ON) inhibitor therapy. | [test info](https://www.bio-rad.com/en-us/category/digital-pcr) · 1000 Alfred Nobel Drive, Hercules, CA 94547 · 1-510-724-7000 |
| Serial KRAS G12R ctDNA quantitation | Tempus *(Tempus xM)* | Early-response and emerging-resistance surveillance on pan-RAS / RAS(ON) inhibitor therapy. | [test info](https://www.tempus.com/oncology/diagnostics/) · 600 West Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| Serial KRAS G12R ctDNA quantitation | Foundation Medicine *(FoundationOne Tracker)* | Early-response and emerging-resistance surveillance on pan-RAS / RAS(ON) inhibitor therapy. | [test info](https://www.foundationmedicine.com/test/foundationone-tracker) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| **Tumor NGS for KRAS copy-number (KRAS amplification, wildtype KRAS amplification, secondary KRAS mutations)** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Frames durability and next-line planning for pan-RAS / RAS(ON) inhibitor therapy; does not gate enrollment.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| Tumor NGS for KRAS copy-number | Caris Life Sciences *(Caris Molecular Intelligence)* | Frames durability and next-line planning for pan-RAS / RAS(ON) inhibitor therapy; does not gate enrollment. | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| Tumor NGS for KRAS copy-number | Tempus *(Tempus xT)* | Frames durability and next-line planning for pan-RAS / RAS(ON) inhibitor therapy; does not gate enrollment. | [test info](https://www.tempus.com/oncology/diagnostics/) · 600 West Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| Tumor NGS for KRAS copy-number | Memorial Sloan Kettering Diagnostic Molecular Pathology *(MSK-IMPACT)* | Frames durability and next-line planning for pan-RAS / RAS(ON) inhibitor therapy; does not gate enrollment. | [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |
| Tumor NGS for KRAS copy-number | NeoGenomics Laboratories *(NeoTYPE Comprehensive Panel)* | Frames durability and next-line planning for pan-RAS / RAS(ON) inhibitor therapy; does not gate enrollment. | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| **Tumor microenvironment workup: PD-L1 IHC (22C3), CD3 / CD8 TIL density, and stromal density (alpha-SMA or H and E review)** | **NeoGenomics Laboratories *(preferred)* (MultiOmyx multiplex IHC)** | **Frames ICI-combination strategy (KRAS-inhibitor plus PD-1, CXCR4 antagonist plus PD-1, vaccine plus PD-1); does not gate enrollment.** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| Tumor microenvironment workup | Caris Life Sciences *(Caris Molecular Intelligence)* | Frames ICI-combination strategy (KRAS-inhibitor plus PD-1, CXCR4 antagonist plus PD-1, vaccine plus PD-1); does not gate enrollment. | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| Tumor microenvironment workup | Foundation Medicine *(FoundationOne CDx (with PD-L1 IHC reflex))* | Frames ICI-combination strategy (KRAS-inhibitor plus PD-1, CXCR4 antagonist plus PD-1, vaccine plus PD-1); does not gate enrollment. | [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| Tumor microenvironment workup | Mayo Clinic Laboratories | Frames ICI-combination strategy (KRAS-inhibitor plus PD-1, CXCR4 antagonist plus PD-1, vaccine plus PD-1); does not gate enrollment. | [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 |
| Tumor microenvironment workup | Memorial Sloan Kettering Diagnostic Molecular Pathology | Frames ICI-combination strategy (KRAS-inhibitor plus PD-1, CXCR4 antagonist plus PD-1, vaccine plus PD-1); does not gate enrollment. | [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |

### Biomarker plan

| Recommended assay | Rationale | Suggested assay provider | Tissue requirements |
|---|---|---|---|
| Orthogonal NGS panel plus ctDNA (KRAS G12R-specific ddPCR or comprehensive plasma NGS) | Pan-RAS and RAS(ON) multi-selective programs (RMC-6236, RMC-7977 and the divarasib-class follow-ons) require allele-resolved KRAS G12X status at trial entry, and most central labs re-test the variant on plasma at screening regardless of the local report. G12R is biologically distinct from G12C and G12D: it is RAS-GTP-binding-deficient, so G12C-specific inhibitors (sotorasib, adagrasib) are not the relevant class. A second-platform call plus a baseline ctDNA reading anchors both eligibility and on-treatment monitoring. | Guardant Health *(Guardant360 CDx)* · [test info](https://guardanthealth.com/products/guardant360-cdx/) · 505 Penobscot Drive, Redwood City, CA 94063 · 1-855-698-8887 | 10-20 mL Streck whole blood for ctDNA; archival FFPE or matched tissue NGS for the orthogonal call |
| p16 IHC (clone E6H4 or equivalent) | NGS copy-number calls for CDKN2A homozygous deletion can be unreliable at low tumor purity, and p16 IHC is the orthogonal protein-level readout that confirms loss of function. Most CDK4/6-inhibitor trials in CDKN2A-altered tumors require p16-negative status or biallelic CDKN2A loss at enrollment, and the IHC is the assay the central labs run. A confirmed loss reads cleanly; a discordance (NGS-loss but IHC-retained) is a meaningful signal that the call may be subclonal or assay-driven. | Mayo Clinic Laboratories · [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 | archival FFPE; same block as the tumor NGS |
| CCND3 alteration-class refinement (amplification vs activating mutation vs fusion) via NGS plus FISH or copy-number array as needed | The user-supplied report says CCND3 alteration without specifying class, and that distinction matters: an amplification or activating mutation supports cyclin-D-axis dependency and CDK4/6 sensitivity, whereas a single passenger missense without copy gain has weaker mechanistic weight. Cyclin-D-degrader and selective CDK4 programs (PF-07220060, fadraciclib, INCB123667) typically gate on copy-number gain or known activating mutations. Refine the class before the board ranks CDK4/6-inhibitor strategy alongside CDKN2A loss. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | archival FFPE; usually returnable from the same NGS panel as the KRAS / co-mutation row |
| Comprehensive tumor NGS including SMAD4, KEAP1, STK11, GNAS, ARID1A | SMAD4 loss in PDAC is the strongest single co-alteration linked to wider metastatic spread and shorter survival, and it changes how the board weights aggressive multi-agent regimens against trial enrollment. KEAP1 and STK11 are imported from the NSCLC literature for a reason: they predict diminished ICI benefit on KRAS-mutant backgrounds and would tilt any decision to layer pembrolizumab onto a pan-RAS inhibitor. GNAS and ARID1A refine the differential against IPMN-origin disease and ARID1A-defined synthetic-lethal pathways. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | archival FFPE; ctDNA as a backup if tissue is exhausted |
| Germline hereditary-cancer panel covering BRCA1, BRCA2, PALB2, ATM, MLH1, MSH2, MSH6, PMS2, EPCAM, CDKN2A, TP53, STK11 | NCCN guidance is that every patient with pancreatic adenocarcinoma should be offered germline testing regardless of family history. A pathogenic BRCA1/2 or PALB2 variant opens the platinum-plus-PARP-inhibitor pathway (olaparib maintenance is FDA-approved for germline BRCA-mutant metastatic PDAC after platinum). Lynch and Li-Fraumeni hits would change family screening and would not be excluded by a somatic-only tumor panel; CDKN2A germline is non-trivial in PDAC with melanoma family history (FAMMM). | Invitae *(Invitae Multi-Cancer Panel)* · [test info](https://www.invitae.com/en/providers/test-catalog) · 1400 16th Street, San Francisco, CA 94103 · 1-800-436-3037 | 5-10 mL EDTA whole blood; saliva kits available from most providers |
| MMR IHC panel (MLH1, MSH2, MSH6, PMS2) | NGS-derived MSI calls have known false-negative cases at low tumor purity or when the panel uses fewer microsatellite loci. MMR IHC is the orthogonal protein-level confirmation and is the assay most ICI-trial central labs accept on its own. A confirmed MSS by both NGS and IHC closes the door cleanly on the tumor-agnostic pembrolizumab pathway and frees the board to focus the ICI discussion on combination strategies. | Mayo Clinic Laboratories · [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 | archival FFPE; same block as the tumor NGS |
| TMB assay platform and calling-pipeline confirmation (panel size, filters, harmonization with FDA-approved 10 mut/Mb threshold) | TMB values are sensitive to the panel size, the mutation-call filters, and whether synonymous variants are included. A 4.1 mut/Mb on a 500-gene panel may map differently against the FDA-approved tumor-agnostic pembrolizumab threshold than a whole-exome-derived value, and the harmonization study (Friends of Cancer Research TMB Project) shows non-trivial cross-platform spread. Confirming the platform and call pipeline locks in the sub-threshold call and forecloses the biomarker-agnostic pembrolizumab pathway cleanly. Below 10 mut/Mb, that route is off the table. | Foundation Medicine *(FoundationOne CDx (TMB-harmonized))* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | no new tissue required |
| TP53 variant annotation (LOF vs dominant-negative vs gain-of-function) with reference to IARC TP53 database | The user report says inactivating mutation, but TP53 alterations split functionally into pure loss-of-function (truncations, splice), dominant-negative missense (hotspot R175H, R248W, R273H), and gain-of-function variants. Any TP53-restoration or mutant-p53 reactivation strategy (eprenetapopt / APR-246-class agents, MDM2 inhibitors in TP53-wildtype residual context) gates on the precise variant class. Annotate against IARC TP53 to make this explicit rather than re-litigating it at the trial-screening step. | Memorial Sloan Kettering Diagnostic Molecular Pathology *(MSK-IMPACT (with variant annotation))* · [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 | no new tissue required; re-read the existing NGS report |
| p16 IHC across multiple tumor regions (primary site vs metastatic biopsy if available) | PDAC biology often shows clonal heterogeneity between primary and metastatic sites, and CDKN2A loss is not always uniform. A patchy p16 result on multi-region IHC tempers expectations for CDK4/6-inhibitor monotherapy and may push the board toward combination strategies. Lower priority than the orthogonal IHC because the gating decision rides on the dominant block, but the heterogeneity read changes how the response is interpreted. | Mayo Clinic Laboratories · [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 | archival FFPE from a second site if available |
| Serial KRAS G12R ctDNA quantitation (ddPCR or tumor-informed MRD) at baseline and at cycle 2 / cycle 4 of KRAS-directed therapy | On KRAS-directed therapy, the rate of KRAS variant-allele-fraction decline by cycle 2 to cycle 4 is one of the earliest readouts of biological response and tracks ahead of RECIST imaging by weeks. A rising VAF on therapy is a sentinel for emerging resistance and prompts an earlier re-biopsy or re-staging conversation. Does not gate enrollment; informs how the team sequences imaging, re-biopsy, and switch decisions while on a pan-RAS inhibitor. | Natera *(Signatera (tumor-informed MRD))* · [test info](https://www.natera.com/oncology/signatera-advanced-cancer-detection/) · 13011 McCallen Pass, Austin, TX 78753 · 1-650-249-9090 | 10 mL Streck whole blood per draw; serial sampling protocol |
| Tumor NGS for KRAS copy-number (KRAS amplification, wildtype KRAS amplification, secondary KRAS mutations) | Baseline KRAS amplification and acquired wildtype-KRAS amplification are documented resistance mechanisms to KRAS-directed therapy, including the pan-RAS class. Detecting a baseline amplicon shifts the durability expectation; detecting an emerging wildtype-allele amplification on progression reframes whether the next move is intra-class (different RAS-directed agent) or a switch to chemo or to a downstream pathway. The same NGS panel that returns the co-mutation profile should annotate these copy-number calls. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | archival FFPE at baseline; ctDNA at progression |
| Tumor microenvironment workup: PD-L1 IHC (22C3), CD3 / CD8 TIL density, and stromal density (alpha-SMA or H and E review) | PDAC is the textbook immune-cold, stromally dense tumor, and the MSS / sub-threshold-TMB combination forecloses the easy ICI route. The microenvironment workup informs whether an ICI-combination strategy (CXCR4 antagonist plus PD-1, KRAS-inhibitor plus PD-1, vaccine plus PD-1) is biologically rational for this case or whether the dominant problem is exclusion of T cells from the tumor bed. A PD-L1 CPS read also feeds any ICI-combination trial that uses a soft enrichment threshold rather than a hard cutoff. | NeoGenomics Laboratories *(MultiOmyx multiplex IHC)* · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | archival FFPE; same block as the tumor NGS |
---

*Decision support, not medical advice. Confirm assay availability and current standards with the treating team and the local pathology service.*

<!-- libby:target-validation:end -->

## Scope summary

26 trials surfaced, 16 clinical-evidence rows (11 included + 5 standard-of-care chemo rows logged as `considered_excluded` per the targetable-feature scope rule), 22 preclinical rows, and 12 target-validation rows (1 essential `gates_intervention`, 5 high-priority, 6 medium-priority workups). The ranked list contains 11 rows spanning agreement scores from 1.0 (rank 1 workup; rank 2 daraxonrasib monotherapy) down to -0.2 (rank 7 RMC-7977 + ivonescimab). All five personas converged on daraxonrasib monotherapy as the lead therapeutic option. The remaining ranks split across pan-KRAS-class backup, dual-feature trials, gated PARP / vaccine pathways, and informational-context entries (palbociclib, RAMP-205) carrying explicit caveats.

## Cross-cutting caveat (read first)

**All six biomarkers are confirmed. The load-bearing decisions for this case sit elsewhere — in three places the user should hold in mind before reading the ranks.**

- **Workup hardening is not optional even though biomarkers read as confirmed.** Pan-RAS and RAS(ON) sponsors re-test KRAS G12R on plasma at screening regardless of the local report, and a baseline ctDNA VAF is the on-treatment-monitoring anchor that flags resistance weeks ahead of imaging. Rank 1 is the orthogonal NGS + ctDNA confirmation; it gates trial entry on the lead recommendation, not the patient's eligibility in principle.
- **PDAC carries a meaningful germline prior. Order the germline panel.** BRCA1, BRCA2, PALB2, ATM, MLH1/MSH2/MSH6/PMS2, EPCAM, CDKN2A, TP53, and STK11 are all worth knowing in PDAC regardless of family history (NCCN Pancreatic Adenocarcinoma v2.2026 recommends germline testing for every patient with the diagnosis). A pathogenic BRCA1/2 or PALB2 result moves olaparib (rank 5) and rucaparib (rank 10) from "off-table without these gates" to "decision-relevant after a platinum induction." A Lynch hit changes family cascade testing. A CDKN2A germline variant in PDAC with melanoma family history (FAMMM) changes screening. None of this is on file yet; the germline panel turnaround is 3-6 weeks.
- **MSS + TMB 4.1 forecloses biomarker-agnostic ICI cleanly.** KEYNOTE-158 (Marabelle 2020) requires MSI-H for the tumor-agnostic pembrolizumab indication; this patient is MSS by both NGS and (recommended) MMR IHC. TMB 4.1 mut/Mb is well below the 10 mut/Mb threshold for the TMB-based tumor-agnostic indication. CCTG PA.7 (Renouf 2022, RoB2:Low, p=0.72) is the load-bearing negative RCT for adding biomarker-agnostic ICI to chemo in unselected metastatic PDAC. The implication: rank 7 (RMC-7977 + ivonescimab) is the only entry on the page that touches the immune axis at all, and it does so under three persona dissents because the published clinical PDAC data are zero.

The case ranking is targetable-feature-scoped. Standard-of-care chemotherapy for recurrent PDAC (FOLFIRINOX, NALIRIFOX, gem/nab-paclitaxel, nal-IRI/5FU) is NCCN cat-1 / 2A and is the treating team's call; it does not target the patient's listed features and is logged as `considered_excluded` rather than ranked. The page enumerates what Libby has to say about KRAS G12R, CDKN2A loss, and CCND3, not what the medical oncologist already knows.

## Intervention grouping

- **Pan-RAS / RAS(ON) class targeting KRAS G12R:** daraxonrasib (RMC-6236) monotherapy and chemo-combo, zoldonrasib (RMC-7977) with PD-1xVEGF bispecific. Anchor evidence: Wolpin NEJM 2026 ([PMID 42090791](https://pubmed.ncbi.nlm.nih.gov/42090791)); Holderfield Nature 2024 ([PMID 38589574](https://pubmed.ncbi.nlm.nih.gov/38589574)); Jiang Cancer Discovery 2024 ([PMID 38593348](https://pubmed.ncbi.nlm.nih.gov/38593348)); Wasko Nature 2024 ([PMID 38588697](https://pubmed.ncbi.nlm.nih.gov/38588697)); Hobbs Cancer Discovery 2020 ([PMID 31649109](https://pubmed.ncbi.nlm.nih.gov/31649109)) for the G12R-specific biology.
- **Pan-KRAS small-molecule and IV programs (G12R explicit in eligibility):** PF-07934040 ([NCT06447662](https://clinicaltrials.gov/study/NCT06447662)), ASP5834 ([NCT07094204](https://clinicaltrials.gov/study/NCT07094204)).
- **MTA-cooperative PRMT5 class hitting CDKN2A / MTAP co-deletion:** anvumetostat (AMG 193, [NCT06360354](https://clinicaltrials.gov/study/NCT06360354)) with a daraxonrasib combination arm; BMS-986504 ([NCT07492680](https://clinicaltrials.gov/study/NCT07492680) — not yet recruiting). Anchor evidence: Mavrakis Science 2016 ([PMID 26912361](https://pubmed.ncbi.nlm.nih.gov/26912361)); Kryukov Science 2016 ([PMID 26912360](https://pubmed.ncbi.nlm.nih.gov/26912360)); Smith Cancer Discovery 2023 ([PMID 37552839](https://pubmed.ncbi.nlm.nih.gov/37552839)).
- **PARP-class maintenance (gated on germline BRCA / PALB2 + platinum induction):** olaparib (POLO, [PMID 31157963](https://pubmed.ncbi.nlm.nih.gov/31157963)); rucaparib (Reiss JCO 2021, [PMID 33970687](https://pubmed.ncbi.nlm.nih.gov/33970687)).
- **KRAS-peptide vaccine targeting G12R (MRD-positive enrollment window):** ELI-002 7P ([NCT05726864](https://clinicaltrials.gov/study/NCT05726864)). Anchor evidence: AMPLIFY-201 (Pant Nat Med 2024 [PMID 38195752](https://pubmed.ncbi.nlm.nih.gov/38195752); Wainberg Nat Med 2025 [PMID 40790272](https://pubmed.ncbi.nlm.nih.gov/40790272)).
- **MAPK + autophagy / RAF-MEK + FAK combinations:** avutometinib + defactinib + gem/nab (RAMP-205, [NCT05669482](https://clinicaltrials.gov/study/NCT05669482)) — informational, abstract-only PDAC efficacy at n=6.
- **CDK4/6 axis combinations:** palbociclib + MEK or IGF1R or chemo via ADOPT ([NCT06813079](https://clinicaltrials.gov/study/NCT06813079)) or off-label — Z1C basket monotherapy precedent is negative (O'Hara CCR 2025, [PMID 39437014](https://pubmed.ncbi.nlm.nih.gov/39437014)).

## Top interventions

### Rank 1. KRAS G12R orthogonal NGS + ctDNA confirmation

*Workup hardening. The user reported KRAS G12R as confirmed; this row is the orthogonal second-platform check that pan-RAS / RAS(ON) sponsors require at screening, plus a baseline ctDNA VAF for monitoring.*

#### Evidence base

Pan-RAS and RAS(ON) trial programs re-test KRAS G12X variants on plasma at screening regardless of the local report (target-validation row `kras-g12r-orthogonal-ngs-ctdna`, priority: essential, decision_relevance: gates_intervention). A second-platform call plus baseline ctDNA anchors both eligibility for [NCT05379985](https://clinicaltrials.gov/study/NCT05379985) (RMC-6236-001) and [NCT06445062](https://clinicaltrials.gov/study/NCT06445062) (RMC-GI-102) and seeds the serial-monitoring protocol for cycle 2 and cycle 4 VAF reads. Reference platforms: Guardant360 CDx, FoundationOne Liquid CDx, Tempus xF+, Natera Signatera, Caris Assure. The same draw returns SMAD4 / KEAP1 / STK11 co-mutations ([PMID 30019789](https://pubmed.ncbi.nlm.nih.gov/30019789), [PMID 30100704](https://pubmed.ncbi.nlm.nih.gov/30100704), [PMID 29773717](https://pubmed.ncbi.nlm.nih.gov/29773717)) and the KRAS copy-number read ([PMID 36952657](https://pubmed.ncbi.nlm.nih.gov/36952657), [PMID 34471132](https://pubmed.ncbi.nlm.nih.gov/34471132)) that frame durability on pan-RAS therapy.

#### Likelihood of desired effect

Diagnostic certainty. Locks the G12R call for trial entry and seeds the on-treatment monitoring baseline. No therapeutic claim on its own.

#### Toxicity profile

- None. Blood draw plus archival FFPE retest.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. No persona dissented or vetoed.

#### Practical considerations

Order in parallel with the germline panel (3-6 week turnaround), MMR IHC (1-2 weeks), p16 IHC (1-2 weeks), MTAP reflex (often returnable on the same NGS request), and the TMB platform / pipeline documentation review. Most academic centers can run all of this on a single archival block plus a single blood draw. Ask the molecular pathologist to annotate KRAS copy-number, SMAD4 status, and MTAP explicitly rather than burying them in a 500-gene appendix. The target-validator surfaced this row as essential / gates_intervention; the user-reported G12R confirmation means this is hardening rather than pre-enrollment gating.

#### Why this rank

Rank 1 because every downstream pan-RAS / RAS(ON) lane requires central-lab orthogonal confirmation regardless of the local report. The serial ctDNA dynamics (cycle 2, cycle 4) are the early-response readout that tracks ahead of imaging.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Orthogonal KRAS G12R NGS + baseline ctDNA (Guardant360 CDx / FoundationOne CDx / Tempus xF+ / Natera Signatera / Caris Assure) | Gates pan-RAS / RAS(ON) trial entry; seeds monitoring baseline | None — diagnostic | [NCT05379985](https://clinicaltrials.gov/study/NCT05379985), [NCT06445062](https://clinicaltrials.gov/study/NCT06445062), [PMID 36952657](https://pubmed.ncbi.nlm.nih.gov/36952657) |

---

### Rank 2. daraxonrasib (RMC-6236) 300 mg PO daily monotherapy on NCT05379985

*Lead therapeutic option. All five personas put this at rank 1.*

#### Evidence base

The Wolpin NEJM 2026 publication ([PMID 42090791](https://pubmed.ncbi.nlm.nih.gov/42090791)) is the load-bearing efficacy anchor: 168 PDAC patients dosed at 300 mg or below in the RMC-6236-001 phase 1/2; the 2L RAS G12 subgroup at 300 mg (n=26) returned ORR 35%, mDoR 8.2 mo, mPFS 8.5 mo, mOS 13.1 mo. G12X variants enrolled include G12D, G12V, G12R, and Q61H — the patient's G12R sits inside the pooled estimand. Preclinical activity is replicated across G12R-bearing PDAC lines (Holderfield Nature 2024 [PMID 38589574](https://pubmed.ncbi.nlm.nih.gov/38589574); Jiang Cancer Discovery 2024 [PMID 38593348](https://pubmed.ncbi.nlm.nih.gov/38593348)), and the G12R-specific biology (Hobbs Cancer Discovery 2020 [PMID 31649109](https://pubmed.ncbi.nlm.nih.gov/31649109)) puts this allele squarely in the RAS(ON) tri-complex window rather than the GDP-state covalent G12C window. RASolute-302 ([NCT06625320](https://clinicaltrials.gov/study/NCT06625320)) is the registrational phase 3; status is active not recruiting and the OS readout has not landed.

#### Likelihood of desired effect

High in 2L RAS G12 PDAC at the 300 mg dose. The ORR 35% / mPFS 8.5 mo / mOS 13.1 mo in n=26 is the best published efficacy on this allele anywhere, and G12R sits inside the pooled G12X estimand on biology that Hobbs 2020 explains. The open question is allele resolution: the G12R-specific subgroup ORR has not been broken out from the pooled estimand, and the field reads G12X as a single number pending the RASolute-302 phase 3 readout. The Singhi 2025 finding that G12R PDAC carries a relatively lower baseline ERK flux and an immune-enriched microenvironment is consistent with a wider therapeutic window for active-state RAS blockade in this allele than in G12D, but that hypothesis has not been tested clinically at allele resolution.

#### Toxicity profile

The AE distribution is fully mapped in the 168-patient PDAC cohort:

- Any-grade treatment-related AE 96%; G3+ TRAE 30%; no grade-5 events
- Rash any-grade 91% / G3+ 8% — EGFR-inhibitor management playbook applies (topical steroids plus low-dose doxycycline)
- Diarrhea any-grade 48% / G3+ 2% — loperamide ladder
- Stomatitis any-grade 31% / G3+ 3% — dexamethasone mouthwash
- Nausea any-grade 43%, vomiting 31%, fatigue 20%

The user has no toxicity vetoes and the rash / GI / stomatitis profile fits inside the consent envelope. Visit burden for rash management is real but not dose-limiting at 300 mg.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous in round 1. The critic's evidence caveat (ROBINS-I:Moderate, n=26, no allele-resolved G12R subgroup, RASolute-302 not yet read out) persists and is acknowledged. The concensusite reframed this in round 2 as a trial-enrollment-principle pick rather than a guideline-listed regimen — pan-RAS is not yet listed in any NCCN evidence category for PDAC. The risktaker and advocate filed round-2 qualified critiques arguing for the chemo-combo lane (NCT06445062) above monotherapy given the patient's oxaliplatin-naive status and treat-to-remission goal; that argument is captured separately at rank 6. No persona dissented or vetoed monotherapy.

#### Practical considerations

- Trial open at [NCT05379985](https://clinicaltrials.gov/study/NCT05379985) (recruiting) — the registrational RASolute-302 trial is active not recruiting, so access most likely runs through RMC-6236-001 or RMC-GI-102.
- Eligibility requires orthogonal G12R confirmation (rank 1).
- FDA Breakthrough Therapy designation is a regulatory process status, not a guideline category. NCCN Pancreatic Adenocarcinoma v2.2026 lists the trial-enrollment principle for recurrent disease with an actionable alteration, which is the framing for this pick.
- 5-year safety follow-up for the pan-RAS class is not yet available; longest-followed patients are at roughly 2 years.

#### Why this rank

Rank 2 only because rank 1 is the workup that gates everything. On therapeutic merit this is rank 1 with a unanimous board: only published meaningful effect size on KRAS G12R PDAC, recruiting trial, fully mapped AE distribution, matched mechanism. The agreement score (1.0) is the maximum for any therapeutic row.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| daraxonrasib (RMC-6236) 300 mg PO daily monotherapy — RMC-6236-001 ([NCT05379985](https://clinicaltrials.gov/study/NCT05379985)) 2L+ PDAC | ORR 35% (n=26); mPFS 8.5 mo; mOS 13.1 mo; mDoR 8.2 mo | G3+ TRAE 30%; rash G3+ 8%; diarrhea G3+ 2%; stomatitis G3+ 3%; no G5 | [PMID 42090791](https://pubmed.ncbi.nlm.nih.gov/42090791) |
| daraxonrasib monotherapy — RASolute-302 phase 3 vs investigator's choice SoC ([NCT06625320](https://clinicaltrials.gov/study/NCT06625320)) | OS, PFS, ORR — registrational readout pending | Per RMC-6236-001 profile | [NCT06625320](https://clinicaltrials.gov/study/NCT06625320) |
| RMC-6236 + RMC-7977 translational PDAC efficacy across G12X alleles including G12R | Strong preclinical activity across G12 variants; ERK pathway suppression at sub-100 nM | n/a | [PMID 38589574](https://pubmed.ncbi.nlm.nih.gov/38589574), [PMID 38593348](https://pubmed.ncbi.nlm.nih.gov/38593348) |

---

### Rank 3. PF-07934040 pan-KRAS small-molecule on NCT06447662

*Backup pan-KRAS class with explicit G12R inclusion in eligibility. Endorsed by critic, concensusite, and advocate.*

#### Evidence base

Pfizer's first-in-human pan-KRAS phase 1 ([NCT06447662](https://clinicaltrials.gov/study/NCT06447662)) is one of the few programs that names G12R explicitly in the inclusion criteria rather than burying it in pan-codon-12 language. Eligibility covers G12C, G12D, G12V, G12R, G12S, G13D, and Q61H across NSCLC, CRC, and PDAC. Two cohorts fit: Part 2a Cohort A1 is 2L+ PDAC monotherapy and matches the patient's recurrent post-FOLFIRI status; Part 2b Cohort A2 is the 1L gem/nab combination arm. No published efficacy data exist; the rank is class-extrapolation from the daraxonrasib precedent (PMID 42090791) under the assumption that small-molecule pan-KRAS chemistry can deliver similar effects as the RAS(ON) tri-complex class. Astellas's ASP5834 ([NCT07094204](https://clinicaltrials.gov/study/NCT07094204)) is the IV-dosed parallel option also naming G12R explicitly; PDAC is in the expansion cohorts.

#### Likelihood of desired effect

Moderate — class extrapolation rather than direct evidence. No PF-07934040 efficacy readout has been published; the rank stands on the daraxonrasib precedent and the G12R-explicit eligibility. Useful access-positioning if a daraxonrasib slot is unavailable.

#### Toxicity profile

- No published AE-grade distribution — phase 1 dose-finding still in progress
- Class-effect rash and GI toxicity expected per pan-KRAS mechanism
- Grade 2+ sensory neuropathy is an enrollment exclusion — watch-item given prior FOLFIRI, though irinotecan-based regimens are usually neuropathy-sparing

User has no toxicity vetoes; the rash / GI watch-items are not pre-flagged.

#### Counter-productive mechanisms / dissent

No round-2 dissent critiques were filed against this row. The critic, concensusite, and advocate all flagged it on roughly the same logic: G12R is in eligibility, no efficacy yet, useful as a backup if RMC-6236 access is blocked.

#### Practical considerations

- Trial open at [NCT06447662](https://clinicaltrials.gov/study/NCT06447662) (recruiting)
- Confirm residual neuropathy from prior FOLFIRI clears the grade-2 exclusion threshold before screening
- Decision between Part 2a (2L+ monotherapy) and Part 2b (1L gem/nab combo) depends on whether the protocol counts adjuvant FOLFIRI as prior systemic
- Not an NCCN-listed or ESMO-scored regimen for PDAC; the framing is the NCCN trial-enrollment principle

#### Why this rank

Rank 3 because the class case is plausible and the G12R-explicit eligibility is operationally distinctive, but no clinical efficacy is published and the dossier has no PF-07934040 AE-grade distribution. Tied with rank 4 on agreement score (0.6); broken on stage of development (PF-07934040 has no biomarker reflex requirement; rank 4 is gated on MTAP).

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| PF-07934040 oral pan-KRAS — Part 2a Cohort A1 2L+ PDAC monotherapy ([NCT06447662](https://clinicaltrials.gov/study/NCT06447662)) | Safety, RP2D, ORR primary; no efficacy readout yet | Not yet published; G2+ neuropathy excluded | [NCT06447662](https://clinicaltrials.gov/study/NCT06447662) |
| ASP5834 IV pan-KRAS — parallel program also naming G12R ([NCT07094204](https://clinicaltrials.gov/study/NCT07094204)) | Safety, RP2D, ORR primary; PDAC in expansion | Not yet published | [NCT07094204](https://clinicaltrials.gov/study/NCT07094204) |

---

### Rank 4. anvumetostat (AMG 193) + daraxonrasib on NCT06360354 — gated on MTAP co-deletion

*Two-feature trial covering KRAS G12R and CDKN2A / MTAP loss on a single regimen. Endorsed by risktaker, advocate, and concensusite.*

#### Evidence base

CDKN2A and MTAP are adjacent on the 9p21 locus and co-deleted in roughly 80-90% of CDKN2A homozygous deletions. The MTA-cooperative PRMT5 class is one of the cleanest synthetic-lethal axes in preclinical oncology: Mavrakis Science 2016 ([PMID 26912361](https://pubmed.ncbi.nlm.nih.gov/26912361)) and Kryukov Science 2016 ([PMID 26912360](https://pubmed.ncbi.nlm.nih.gov/26912360)) established the underlying biology back-to-back, and Smith Cancer Discovery 2023 ([PMID 37552839](https://pubmed.ncbi.nlm.nih.gov/37552839)) showed MRTX1719 with greater than 70-fold MTAP-deleted selectivity in xenografts, sparing the bone-marrow toxicity that killed first-generation PRMT5 inhibitors. [NCT06360354](https://clinicaltrials.gov/study/NCT06360354) (MTAPESTRY-103) carries an anvumetostat + daraxonrasib combination arm — a single trial that targets the patient's KRAS G12R feature and the CDKN2A-loss / MTAP-deletion axis simultaneously. PDAC-cohort efficacy is not yet published; the bulk of in-vivo data is in NSCLC and mesothelioma.

#### Likelihood of desired effect

Moderate if MTAP is co-deleted. The preclinical foundation is unusually clean and the cooperative MTA chemistry is designed to spare MTAP-proficient tissue. The clinical signal in PDAC specifically is not yet public; the trial is still in phase 1b combination dose-finding.

#### Toxicity profile

- No published clinical AE distribution for anvumetostat + daraxonrasib in PDAC
- MTA-cooperative chemistry designed to spare hematologic toxicity (the dose-limiting feature of first-generation PRMT5 inhibitors)
- Daraxonrasib class effects (rash, GI, stomatitis) layer in the combination arm

#### Counter-productive mechanisms / dissent

No round-2 dissent critiques filed against this row. The risktaker placed it at rank 4 as a high-mechanism-stack pick, advocate at rank 5 for dual-feature targeting consistent with treat-to-remission, and concensusite at rank 5 under the trial-enrollment principle.

#### Practical considerations

- Trial open at [NCT06360354](https://clinicaltrials.gov/study/NCT06360354) (recruiting)
- **Order the MTAP IHC or NGS copy-number reflex on the existing tumor block before banking on this row** — cheap to order, decisive to read, the entire row collapses if MTAP is retained
- Most comprehensive NGS panels already return MTAP copy-number; ask the molecular pathologist to call it explicitly
- BMS-986504 ([NCT07492680](https://clinicaltrials.gov/study/NCT07492680)) MountainTAP-5 is the parallel option but not yet recruiting (July 2026 start)

#### Why this rank

Rank 4 on the dual-feature mechanism stack and clean preclinical foundation. Tied with rank 3 on agreement score (0.6); breaks below because of the MTAP reflex gate. If MTAP confirms, this row rises operationally — particularly under the treat-to-remission preference, because the daraxonrasib combination arm hits both targetable features on a single regimen.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| anvumetostat (AMG 193) + daraxonrasib — MTAPESTRY-103 ([NCT06360354](https://clinicaltrials.gov/study/NCT06360354)) GI tumors with homozygous MTAP deletion | Safety, RP2D, ORR primary; no PDAC efficacy yet | Not yet published; class-cooperative design spares MTAP-proficient tissue | [NCT06360354](https://clinicaltrials.gov/study/NCT06360354) |
| MRTX1719 (MTA-cooperative PRMT5i) preclinical translational anchor | >70-fold MTAP-deleted vs MTAP-WT selectivity; xenograft regression | Hematologic and bone-marrow effects not observed at efficacious doses | [PMID 37552839](https://pubmed.ncbi.nlm.nih.gov/37552839) |
| BMS-986504 (navlimetostat) ± daraxonrasib — MountainTAP-5 platform | TBD; not yet recruiting | TBD | [NCT07492680](https://clinicaltrials.gov/study/NCT07492680) |

---

### Rank 5. olaparib maintenance after platinum induction — POLO regimen

*Considered with caveats. Two locked gates: germline BRCA1/2 / PALB2 status, and a 16-plus-week platinum induction the patient has not had.*

#### Evidence base

POLO (Golan NEJM 2019, [PMID 31157963](https://pubmed.ncbi.nlm.nih.gov/31157963), [NCT02184195](https://clinicaltrials.gov/study/NCT02184195)) is the only RoB2:Low phase 3 RCT in this dossier and the only PARP-class regimen with seven years of post-marketing PDAC surveillance. PFS HR 0.53 (95% CI 0.35-0.82, p=0.004), mPFS 7.4 vs 3.8 mo on placebo. The PFS hit is unambiguous; the interim OS HR was 0.91 with no separation, which is the relevant ceiling. Reiss 2021 JCO ([PMID 33970687](https://pubmed.ncbi.nlm.nih.gov/33970687)) extends the PARP signal to somatic BRCA and PALB2 in a phase 2 single-arm (n=46) — useful for net-widening but not RCT-grade.

#### Likelihood of desired effect

High in PFS, conditional on both locked gates opening. The germline panel has not returned (target-validation row `germline-pdac-hboc-lynch-lfs-panel` is the workup) and the patient is platinum-naive after irinotecan-only adjuvant FOLFIRI. POLO requires at least 16 weeks of first-line platinum without progression as the entry condition — that is a NALIRIFOX or FOLFIRINOX induction (treating team's call, outside Libby's scope) before the maintenance pathway opens. The OS ceiling is the binding interpretation: PFS HR 0.53 has not converted to an OS hit at the registrational analysis.

#### Toxicity profile

- G3+ AEs in 40% of olaparib patients vs 23% on placebo
- AE-driven discontinuation 5% vs 2%
- PARP-class MDS / AML risk at roughly 1.5% on prolonged exposure — the long-tail signal to monitor at year 2 and beyond
- Class effects: anemia, fatigue, nausea (NCCN-published management algorithms)

User has no toxicity vetoes.

#### Counter-productive mechanisms / dissent

Critic ranked olaparib at 2 (only RCT-grade option in the dossier), conservative at 2 (most mature safety dataset), concensusite at 2 (only NCCN category 1 listing in the case). Risktaker filed a round-2 dissent on preference-fit grounds: two sequential locked gates stack against a tumor that is already recurrent, and the POLO interim OS HR of 0.91 means even when the gates open the payoff is PFS, not OS. Advocate filed a qualified-on-preference round-2 critique on the same logic and parked it as a deferred option pending germline reflex. The evidence-quality case is unambiguous; the preference-fit case is the disagreement.

Status: `considered_with_caveats` per Hard Rule 3 — two dissents (risktaker, advocate) on a non-veto option.

#### Practical considerations

- Trial / regimen is FDA-approved, not a recruiting trial — this is a standard-of-care option after the gates open
- Germline BRCA1/2 / PALB2 panel: 3-6 week turnaround; order alongside the orthogonal NGS in rank 1
- Platinum induction is the treating team's decision; Libby's scope does not include SoC chemo selection
- Rucaparib (rank 10) is the somatic-BRCA / PALB2 backup if germline is negative but somatic HRD is positive

#### Why this rank

Rank 5 because the gating timeline (germline panel + platinum induction + 16-week disease control) puts this option weeks-to-months behind the pan-KRAS lanes for a tumor that is already recurrent. Higher than rank 6 because the underlying evidence is RoB2:Low RCT rather than ASCO-abstract n=6; lower than rank 4 because it requires two sequential bets on a tumor with active progression.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| olaparib 300 mg PO BID maintenance — POLO ([NCT02184195](https://clinicaltrials.gov/study/NCT02184195)) gBRCA1/2 metastatic PDAC after >=16 wk platinum | PFS HR 0.53 (95% CI 0.35-0.82, p=0.004); mPFS 7.4 vs 3.8 mo; interim OS HR 0.91 NS | G3+ AEs 40% olaparib vs 23% placebo; AE discontinuation 5% | [PMID 31157963](https://pubmed.ncbi.nlm.nih.gov/31157963) |
| rucaparib 600 mg PO BID — Reiss 2021 single-arm phase 2 (somatic BRCA + PALB2 extension) | mPFS 13.1 mo; mOS 23.5 mo; ORR 41.7% | PARP-class effects per olaparib | [PMID 33970687](https://pubmed.ncbi.nlm.nih.gov/33970687) |

---

### Rank 6. daraxonrasib + mFOLFIRINOX or gem/nab-paclitaxel on NCT06445062 (RMC-GI-102)

*Considered with caveats. Preference-aligned escalation lane; two persona dissents on missing combination-safety data.*

#### Evidence base

[NCT06445062](https://clinicaltrials.gov/study/NCT06445062) is the open-label multi-arm RAS(ON) platform combining daraxonrasib with mFOLFIRINOX or gemcitabine/nab-paclitaxel in 1L and 2L+ RAS-mutant GI tumors. PDAC arms cover G12X variants including G12R. The Wolpin NEJM 2026 ([PMID 42090791](https://pubmed.ncbi.nlm.nih.gov/42090791)) monotherapy data are the floor; the combination ceiling has not been publicly characterized in PDAC yet. The closest precedent is RAMP-205 dose-level-1 (avutometinib + defactinib + gem/nab; ASCO 2024 abstract, [doi:10.1200/JCO.2024.42.16_suppl.4140](https://doi.org/10.1200/JCO.2024.42.16_suppl.4140)) reporting 5/6 confirmed PRs in 1L KRAS-mutant metastatic PDAC at n=6 — an exact binomial 95% CI on 5/6 runs roughly 36-100%, and a single non-responder collapses the point estimate. The patient is oxaliplatin-naive (adjuvant FOLFIRI only), so an mFOLFIRINOX combination arm is biologically available rather than just nominally on protocol.

#### Likelihood of desired effect

Moderate-to-high in principle; uncharacterized in published evidence. Combination intensification is the route the treat-to-remission preference points at, and the RAMP-205 precedent suggests pan-RAS-class plus chemo backbones can produce deeper responses than monotherapy in PDAC. The honest read: no published daraxonrasib + chemo PDAC efficacy data exist as of this run.

#### Toxicity profile

- Pan-RAS class toxicity (rash 91% any-grade, diarrhea 48%) layered on chemo-class toxicity (cytopenias, neuropathy)
- No published dedicated combination-safety readout for daraxonrasib + chemo in PDAC
- Residual neuropathy from prior FOLFIRI may push the chemo backbone choice toward gem/nab rather than mFOLFIRINOX
- Cumulative GI toxicity is the load-bearing watch-item

User has no toxicity vetoes; high-risk-high-reward is explicit in the free-text preference.

#### Counter-productive mechanisms / dissent

Advocate ranked this at 2 (treat to remission, efficacy weight 0.80, oxaliplatin-naive backbone available) and risktaker pushed it to rank 1 in round-2 qualified critiques on the monotherapy lane. Conservative did not rank and filed a round-2 qualified critique noting no published dedicated combination-safety table; concensusite filed a round-2 qualified critique on guideline-fit (stacks an unlisted pan-RAS agent onto an NCCN cat-1 chemo backbone — a step further off the guideline than monotherapy). Critic did not rank.

Status: `considered_with_caveats` per Hard Rule 3 (advocate flagged as preference-aligned; conservative and concensusite dissented in round 2).

#### Practical considerations

- Trial open at [NCT06445062](https://clinicaltrials.gov/study/NCT06445062) (recruiting)
- Sponsor confirmation of PDAC subprotocol openness at the referral site is the operational gate
- Whether prior adjuvant FOLFIRI counts as prior systemic therapy is protocol-dependent
- Treat as a contingent escalation pending public release of the RMC-GI-102 PDAC-cohort AE distribution

#### Why this rank

Rank 6 — preference-aligned with the highest user-side ceiling on the page, but the load-bearing combination-safety publication is missing. Higher than ranks 7-11 on agreement-score and on the unambiguous preference-fit; lower than ranks 1-5 because the AE-distribution gap is real and the conservative + concensusite dissents are calibrated to that gap rather than to the mechanism.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| daraxonrasib + mFOLFIRINOX or gem/nab — RMC-GI-102 ([NCT06445062](https://clinicaltrials.gov/study/NCT06445062)) GI tumors with RAS mutation | Safety, RP2D, ORR, PFS — PDAC efficacy not yet published | Not yet published; pan-RAS + chemo overlap expected | [NCT06445062](https://clinicaltrials.gov/study/NCT06445062) |
| avutometinib + defactinib + gem/nab — RAMP-205 dose-level-1 (closest precedent) | 5/6 confirmed PRs (ORR 83%, n=6); 95% CI 36-100% | Not yet published in full | [doi:10.1200/JCO.2024.42.16_suppl.4140](https://doi.org/10.1200/JCO.2024.42.16_suppl.4140) |
| daraxonrasib monotherapy floor | ORR 35% (n=26); mPFS 8.5 mo | G3+ TRAE 30% | [PMID 42090791](https://pubmed.ncbi.nlm.nih.gov/42090791) |

---

### Rank 7. zoldonrasib (RMC-7977) + ivonescimab (PD-1xVEGF bispecific) on NCT07397338

*Considered with caveats. Highest-ceiling preclinical option the patient could touch; three persona dissents on evidence, toxicity, and guideline-fit. Only entry on the page that touches the immune axis.*

#### Evidence base

[NCT07397338](https://clinicaltrials.gov/study/NCT07397338) is the open-label dose-exploration combining RAS(ON) inhibitors with ivonescimab (AK112, PD-1xVEGF bispecific). Primary listed indications are NSCLC and CRC; PDAC enrollment depends on cohort schedule. The preclinical case for the RAS(ON) class in PDAC is the strongest in the dossier: Wasko Nature 2024 ([PMID 38588697](https://pubmed.ncbi.nlm.nih.gov/38588697)) showed RMC-7977 in the autochthonous KPC GEMM produced the longest survival extension recorded for that model with complete radiologic responses in a subset, and Holderfield Nature 2024 ([PMID 38589574](https://pubmed.ncbi.nlm.nih.gov/38589574)) anchors the pharmacology across G12 alleles. The Singhi 2025 finding that G12R PDAC carries a relatively lower-ERK and immune-enriched microenvironment relative to G12D suggests the ICI layer may behave differently in G12R than in G12D, though that hypothesis is unproven clinically. Zero published clinical PDAC data exist for this combination.

#### Likelihood of desired effect

Low in the published-evidence sense. The preclinical ceiling is the highest on the page; the clinical floor is unmeasured because no PDAC patient has been reported on this combination. KPC GEMM data are G12D-allele rather than G12R-matched.

#### Toxicity profile

- No published PDAC clinical AE distribution
- Pan-RAS class toxicity (rash 91% any-grade, diarrhea 48%) stacked on PD-1xVEGF class immune-mediated AEs
- Diagnostic ambiguity between class rash and immune-rash is the load-bearing toxicity-attribution watch-item
- No management algorithm published for overlapping AE profiles

User has no toxicity vetoes.

#### Counter-productive mechanisms / dissent

Risktaker ranked this at 2, advocate at 3. Conservative filed a round-2 dissent on toxicity grounds (no published PDAC combination-safety data; rash-vs-immune-rash diagnostic ambiguity). Critic filed a round-2 qualified critique on evidence-quality grounds (zero published clinical PDAC efficacy; preclinical KPC is G12D not G12R; layering pan-RAS class toxicity onto PD-1xVEGF without combination-safety publication is the specific gap). Concensusite filed a round-2 dissent on guideline-fit grounds (two pre-approval layers off the NCCN menu; PD-1xVEGF has no NCCN, ESMO, or ASCO PDAC line).

Status: `considered_with_caveats` per the three round-2 dissents.

#### Practical considerations

- Trial open at [NCT07397338](https://clinicaltrials.gov/study/NCT07397338) (recruiting) — confirm PDAC cohort openness with the sponsor before screening labs
- MSS + TMB 4.1 forecloses every standard ICI lane; this trial is the only route that touches the immune axis at all
- Off every guideline; the case for keeping this on the page is the patient's accept-high-risk-high-reward stance plus the preclinical KPC data

#### Why this rank

Rank 7 because the preclinical ceiling justifies surfacing it but the clinical floor is unmeasured and three persona dissents are calibrated to that gap. Higher than ranks 8-11 on the mechanism stack and the unique route to an immune axis; lower than ranks 1-6 because the published clinical PDAC effect size is zero.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| zoldonrasib (RMC-7977) + ivonescimab — open-label dose-exploration ([NCT07397338](https://clinicaltrials.gov/study/NCT07397338)) RAS-mutant solid tumors | Safety, RP2D, ORR primary; no PDAC efficacy yet | Not yet published; pan-RAS + PD-1xVEGF overlap unmapped | [NCT07397338](https://clinicaltrials.gov/study/NCT07397338) |
| RMC-7977 preclinical KPC GEMM anchor (Wasko Nature 2024) | Longest survival extension recorded for KPC; complete radiologic responses in subset | n/a | [PMID 38588697](https://pubmed.ncbi.nlm.nih.gov/38588697) |
| Pan-RAS pharmacology cross-allele (Holderfield Nature 2024) | Strong activity across G12 alleles including G12R | n/a | [PMID 38589574](https://pubmed.ncbi.nlm.nih.gov/38589574) |

---

### Rank 8. ELI-002 7P amphiphile mKRAS peptide vaccine on NCT05726864 (AMPLIFY-7P)

*Considered with caveats. Cleanest safety profile in the dossier and G12R-explicit mechanism, but the MRD-positive enrollment window forecloses this patient's overt-recurrent state.*

#### Evidence base

[NCT05726864](https://clinicaltrials.gov/study/NCT05726864) (AMPLIFY-7P) is the phase 1/2 successor to AMPLIFY-201, enrolling resected PDAC and other KRAS / NRAS-mutant solid tumors in the adjuvant minimal-residual-disease setting. The 7-peptide panel covers G12D, G12R, G12V, G12A, G12C, G12S, and G13D — the patient's G12R is explicitly in scope. AMPLIFY-201 (Pant Nat Med 2024 [PMID 38195752](https://pubmed.ncbi.nlm.nih.gov/38195752); Wainberg Nat Med 2025 [PMID 40790272](https://pubmed.ncbi.nlm.nih.gov/40790272)) reported ctDNA reduction in 21/25 MRD-positive resected PDAC and CRC patients, mKRAS-specific T-cell responses in 84%, mRFS not reached vs 3.02 mo in high- vs low-T-cell-responders. The preclinical foundation (Rakhra JITC 2021 [PMID 34376552](https://pubmed.ncbi.nlm.nih.gov/34376552)) is the amphiphile-peptide platform with greater than 10-fold T-cell expansion vs soluble peptide.

#### Likelihood of desired effect

Low for this patient's clinical state. The mechanism is purpose-built for MRD-positive resected disease, not overt recurrence. AMPLIFY-7P enrolls the MRD window; the patient is past it. AMPLIFY-201's striking immunogenicity does not transpose to bulk overt disease.

#### Toxicity profile

- Zero dose-limiting toxicities across the AMPLIFY-201 dose-escalation
- No grade 3+ vaccine-attributed events across n=25
- Injection-site reactions are the dominant AE class
- Cleanest safety profile in the entire dossier

#### Counter-productive mechanisms / dissent

Conservative ranked at 3 (cleanest safety in dossier), concensusite at 4 (clean G12R mechanism-fit). In round 2 the concensusite filed a guideline-fit dissent on the conservative's placement — patient is overt-recurrent while AMPLIFY-7P enrolls MRD-positive resected; the indication is off, not just borderline. Conservative qualified-on-guideline-fit response acknowledged the enrollment-window issue is the binding constraint. The mechanism-fit case is unusually clean; the operational case has closed.

Status: `considered_with_caveats`.

#### Practical considerations

- Trial active not recruiting per registry — access is binding even if eligibility were open
- Vaccine requires immune competence and a 2-3 month T-cell expansion window; not a bridge for rapidly progressing disease
- Logged on the page so the reader can see this was considered and rejected on indication grounds, not mechanism — if a curative-intent salvage resection ever becomes feasible, this row would re-enter scope

#### Why this rank

Rank 8 because the mechanism-fit is unusually clean for G12R specifically, but the eligibility window does not match the patient's clinical state. Higher than ranks 9-11 on mechanism quality and safety profile; lower than ranks 1-7 because the operational route is closed for this patient.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| ELI-002 7P — AMPLIFY-7P ([NCT05726864](https://clinicaltrials.gov/study/NCT05726864)) resected PDAC + KRAS-mutant solid tumors, MRD-positive | RFS, ctDNA reduction, immunogenicity — pending | Class-clean per AMPLIFY-201 | [NCT05726864](https://clinicaltrials.gov/study/NCT05726864) |
| ELI-002 2P — AMPLIFY-201 (Wainberg Nat Med 2025) | ctDNA reduction 21/25; T-cell response 84%; mRFS NR vs 3.02 mo by responder stratification | Zero DLTs; no G3+ vaccine-attributed events | [PMID 40790272](https://pubmed.ncbi.nlm.nih.gov/40790272), [PMID 38195752](https://pubmed.ncbi.nlm.nih.gov/38195752) |
| Amphiphile-peptide preclinical platform (Rakhra JITC 2021) | >10-fold T-cell expansion vs soluble peptide; durable cures in fraction of KRAS-mutant syngeneic models | Class-clean | [PMID 34376552](https://pubmed.ncbi.nlm.nih.gov/34376552) |

---

### Rank 9. avutometinib (RAF/MEK clamp) + defactinib (FAKi) + gem/nab-paclitaxel on NCT05669482 (RAMP-205)

*Considered with caveats. Striking abstract-only n=6 signal in 1L PDAC; trial active not recruiting; one round-2 critic dissent on evidence quality.*

#### Evidence base

[NCT05669482](https://clinicaltrials.gov/study/NCT05669482) (RAMP-205) is the phase 1b/2 of the avutometinib + defactinib + gem/nab combination in treatment-naive metastatic PDAC. The Krebs ASCO 2024 abstract ([doi:10.1200/JCO.2024.42.16_suppl.4140](https://doi.org/10.1200/JCO.2024.42.16_suppl.4140)) reported 5/6 confirmed PRs at dose level 1 (ORR 83%, n=6) — a striking early signal at a small N; an exact binomial 95% CI on 5/6 runs roughly 36-100%. Cross-tumor LGSOC validation (Banerjee JCO 2025 [PMID 40644648](https://pubmed.ncbi.nlm.nih.gov/40644648)) gave 44% ORR with mPFS 22 mo and mDoR 31.1 mo in KRAS-mutant subset — FDA-accelerated approval for that indication. Preclinical Jiang Nat Med 2016 ([PMID 27376576](https://pubmed.ncbi.nlm.nih.gov/27376576)) is the KPC FAK-stroma anchor.

#### Likelihood of desired effect

Moderate-to-high in cross-tumor KRAS-mutant disease (LGSOC). PDAC signal at n=6 is hypothesis-generating; the exact 95% CI is wide enough that a single non-responder collapses the point estimate.

#### Toxicity profile

- Four-agent stack: RAF/MEK class rash, edema, CK elevation, reversible ocular events; FAKi GI; chemo cytopenias and neuropathy
- No published dedicated PDAC combination AE table
- Residual neuropathy from prior FOLFIRI is the watch-item with the gem/nab backbone

#### Counter-productive mechanisms / dissent

Risktaker ranked at 3. Critic filed a round-2 dissent on evidence-quality grounds (ASCO 2024 abstract with no peer-reviewed publication, ROBINS-I:Serious, n=6 with wide CI, four-agent stack with no published PDAC combination characterization). Conservative did not rank and noted the missing dedicated four-agent PDAC combination-safety publication. Status `considered_with_caveats` because the load-bearing efficacy datum is an unpeer-reviewed abstract at n=6 and the trial is active not recruiting.

#### Practical considerations

- Trial active not recruiting — access is the gating issue
- Line mismatch: trial is 1L untreated metastatic, patient is recurrent post-adjuvant FOLFIRI; some protocols count adjuvant chemo as prior systemic
- FDA orphan drug designation granted on the back of the dose-level-1 signal — formal accelerated approval in PDAC is contingent on the full RAMP-205 readout

#### Why this rank

Rank 9 because the published evidence is one unpeer-reviewed abstract at n=6 and the trial is access-gated. Higher than ranks 10-11 because the signal is on a KRAS-mutant PDAC cohort directly rather than a basket precedent that read negative. Lower than ranks 1-8 because the evidence base is genuinely thin.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| avutometinib + defactinib + gem/nab — RAMP-205 ([NCT05669482](https://clinicaltrials.gov/study/NCT05669482)) 1L metastatic PDAC | 5/6 confirmed PRs at dose level 1 (n=6); full publication pending | Not yet published in full | [doi:10.1200/JCO.2024.42.16_suppl.4140](https://doi.org/10.1200/JCO.2024.42.16_suppl.4140) |
| avutometinib + defactinib — RAMP-201 cross-tumor LGSOC (Banerjee JCO 2025) | 44% ORR KRAS-mutant LGSOC; mPFS 22 mo; mDoR 31.1 mo | Manageable AE profile; class effects rash, edema, CK, reversible ocular | [PMID 40644648](https://pubmed.ncbi.nlm.nih.gov/40644648) |
| FAK + ICI preclinical KPC anchor (Jiang Nat Med 2016) | KPC survival doubled with FAK monotherapy; sustained regression with ICI add-on | n/a | [PMID 27376576](https://pubmed.ncbi.nlm.nih.gov/27376576) |

---

### Rank 10. rucaparib maintenance — gated on germline or somatic BRCA / PALB2 + platinum induction

*Considered with caveats. PARP-class backup to olaparib that widens the biomarker net to somatic BRCA / PALB2.*

#### Evidence base

Reiss JCO 2021 ([PMID 33970687](https://pubmed.ncbi.nlm.nih.gov/33970687)) is the single-arm phase 2 (n=46) supporting rucaparib maintenance in platinum-sensitive advanced PDAC with germline or somatic BRCA1/2 or PALB2. Primary endpoint was PFS rate at 6 months. Secondary readouts: mPFS 13.1 mo, mOS 23.5 mo, ORR 41.7% (15/36 with measurable disease), mDoR 17.3 mo. The cohort enriched for platinum-sensitive disease; the population breakdown was germline BRCA1 n=7, BRCA2 n=27, PALB2 n=6, somatic BRCA2 n=2.

#### Likelihood of desired effect

Moderate when both gates open. The somatic-BRCA / PALB2 extension is the value proposition vs olaparib — wider biomarker net at a phase 2 single-arm evidence floor.

#### Toxicity profile

Same PARP class as olaparib: fatigue, anemia, nausea at expected rates; MDS / AML class risk on prolonged exposure.

#### Counter-productive mechanisms / dissent

Conservative ranked at 4. Critic filed a round-2 qualified critique on evidence-quality — the mPFS and mOS figures are secondary readouts in a single-arm design, not registrational. No round-2 dissents.

Status: `considered_with_caveats` — same locked gates as olaparib (germline / somatic HRD + platinum induction) with weaker evidence base.

#### Practical considerations

- FDA-approved for the maintenance setting; not a recruiting trial
- Revisit if germline panel returns BRCA1/2 or PALB2 (or if somatic NGS already returned a hit) and an olaparib slot is unavailable

#### Why this rank

Rank 10 below olaparib (rank 5) on evidence floor (phase 2 single-arm vs phase 3 RCT) and above palbociclib (rank 11) because the PARP class has a registrational PDAC precedent while CDK4/6i in CDKN2A-altered tumors has a registrational basket negative readout.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| rucaparib 600 mg PO BID maintenance — Reiss 2021 single-arm phase 2 (germline / somatic BRCA + PALB2) | mPFS 13.1 mo; mOS 23.5 mo; ORR 41.7%; mDoR 17.3 mo | Class effects per PARP; no new safety signals | [PMID 33970687](https://pubmed.ncbi.nlm.nih.gov/33970687) |

---

### Rank 11. palbociclib + MEK/ERK or IGF1R combination via ADOPT or off-label

*Considered with caveats. Mechanism-fit on CDKN2A / CCND3 axis but Z1C basket monotherapy precedent (ORR 4%) is actively negative.*

#### Evidence base

CDKN2A loss derepresses CDK4/6 and CCND3 alteration reinforces the cyclin-D axis dependency — the textbook biomarker setup for CDK4/6 inhibitor strategy. Preclinical Knudsen Cancer Research 2023 ([PMID 36346366](https://pubmed.ncbi.nlm.nih.gov/36346366)) showed synergistic suppression in all six PDAC organoid models when palbociclib was combined with trametinib or ulixertinib. Earlier work (Franco/Knudsen Oncotarget 2014 [PMID 25156567](https://pubmed.ncbi.nlm.nih.gov/25156567); Heilmann/Knudsen Cancer Res 2014 [PMID 24986516](https://pubmed.ncbi.nlm.nih.gov/24986516)) showed palbociclib + IGF1R / mTOR converts cytostasis into regression in p16-deficient PDAC PDX. The NCI-MATCH Z1C basket (O'Hara CCR 2025 [PMID 39437014](https://pubmed.ncbi.nlm.nih.gov/39437014)) is the load-bearing negative clinical precedent — palbociclib monotherapy in CDK4/6-amplified solid tumors gave ORR 4% with mPFS 2.0 mo. [NCT06813079](https://clinicaltrials.gov/study/NCT06813079) (ADOPT) is the PDO-guided platform that could route a PDAC patient onto abemaciclib based on organoid sensitivity; not yet recruiting.

#### Likelihood of desired effect

Low for monotherapy (Z1C confirmed). Preclinical combination synergy in PDAC organoids (Knudsen 2023) has no PDAC clinical translation yet, and the G12R-specific lower-ERK phenotype (Singhi 2025) is an open variable for the MEK + CDK4/6 synergy logic.

#### Toxicity profile

- G3+ neutropenia is the class-defining AE
- Cumulative cytopenia risk when stacking with chemo or MEKi

#### Counter-productive mechanisms / dissent

Risktaker ranked at 5 on the mechanism stack. Critic and conservative both excluded with explicit rationale (Z1C negative precedent in basket; ADOPT not yet recruiting; off-label combination requires institutional pharmacy support). No formal round-2 dissents were filed but the exclusion rationales are calibrated in the positions.

Status: `considered_with_caveats` — informational context for the CDKN2A / CCND3 axis rather than a recommended action.

#### Practical considerations

- ADOPT not yet recruiting; off-label combination requires institutional pharmacy support and is not a registered trial
- Watch the MTAP reflex on rank 1 — if MTAP is co-deleted, rank 4 (PRMT5 + RAS axis) is the cleaner mechanism-stack lane for the CDKN2A-loss feature than CDK4/6i

#### Why this rank

Rank 11 because the closest published basket precedent (Z1C ORR 4%) is actively negative, the combination logic is preclinical-only in PDAC, and the operational route (ADOPT PDO-guided or off-label) is structurally weaker than every trial-enrollment lane above it. The row appears so the reader can see the CDKN2A / CCND3 axis was considered and the negative basket readout is the load-bearing reason it does not rise higher.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| palbociclib monotherapy — NCI-MATCH Z1C CDK4/6-amplified solid tumors (load-bearing negative precedent) | ORR 4%; mPFS 2.0 mo; mOS 8.8 mo | Class-defining neutropenia | [PMID 39437014](https://pubmed.ncbi.nlm.nih.gov/39437014) |
| palbociclib + trametinib or ulixertinib — Knudsen 2023 PDAC organoid synergy | All 6 PDOs synergistic; xenograft regression where monotherapy was cytostatic | n/a (preclinical) | [PMID 36346366](https://pubmed.ncbi.nlm.nih.gov/36346366) |
| abemaciclib via ADOPT PDO-guided platform ([NCT06813079](https://clinicaltrials.gov/study/NCT06813079)) | PDO-guided ORR, PFS, organoid-clinical concordance | TBD | [NCT06813079](https://clinicaltrials.gov/study/NCT06813079) |

## Classes examined but not ranked

- **G12C-selective inhibitors (sotorasib, adagrasib):** off-target at the molecular level for KRAS G12R. Sotorasib in PDAC (Strickler NEJM 2023 [PMID 36546651](https://pubmed.ncbi.nlm.nih.gov/36546651), ORR 21%, n=38 G12C-only) and adagrasib in PDAC (Bekaii-Saab JCO 2023 [PMID 37099736](https://pubmed.ncbi.nlm.nih.gov/37099736), PDAC subset ORR 33%, n=21 G12C-only) anchor the allele-selective KRAS class precedent that the pan-RAS programs are extending to G12R, but G12R is GTP-loaded and structurally distinct (Hobbs 2020 [PMID 31649109](https://pubmed.ncbi.nlm.nih.gov/31649109)) — these drugs do not bind G12R. Reviewed and rejected on allele grounds.
- **G12D-selective inhibitors (INCB161734, ASP3082 / setidegrasib, MRTX1133):** off-target by allele design. DAWN-303 ([NCT07522073](https://clinicaltrials.gov/study/NCT07522073)) and the ASP3082 phase 3 ([NCT07409272](https://clinicaltrials.gov/study/NCT07409272)) are registrational programs in G12D PDAC; MRTX1133 ([NCT05737706](https://clinicaltrials.gov/study/NCT05737706)) was terminated for formulation issues. Anchor the parallel class precedent for allele-selective pan-RAS programs the patient is eligible for; not actionable for G12R.
- **MEK + autophagy combinations (trametinib + hydroxychloroquine):** PaTcH ([NCT05518110](https://clinicaltrials.gov/study/NCT05518110)) closed for futility in March 2026. Preclinical Bryant / Kinsey 2019 back-to-back Nat Med ([PMID 30833752](https://pubmed.ncbi.nlm.nih.gov/30833752); [PMID 30833748](https://pubmed.ncbi.nlm.nih.gov/30833748)) showed the synthetic-lethal axis preclinically; the clinical translate did not deliver. NTO-RAS basket ([NCT06229340](https://clinicaltrials.gov/study/NCT06229340)) is the next iteration but inherits the PaTcH cloud. Reviewed and rejected on negative clinical readout.
- **TP53 reactivators (eprenetapopt / APR-246):** mechanism is selective for missense / dominant-negative variants (R175H, R248W, R273H). The patient's TP53 variant class is annotated as inactivating without missense specification; target-validation row `tp53-lof-classification` is the workup. APROC ([NCT02999893](https://clinicaltrials.gov/study/NCT02999893)) was terminated. Off-target for this case until the variant class resolves.
- **Single-agent CDK4/6 inhibition for CDKN2A loss (CAPTUR Group 8 [NCT03297606](https://clinicaltrials.gov/study/NCT03297606), NCI rare-tumor platform [NCT04423185](https://clinicaltrials.gov/study/NCT04423185)):** mechanism is on-axis for CDKN2A loss + CCND3 alteration, but the load-bearing Z1C readout (O'Hara 2025 [PMID 39437014](https://pubmed.ncbi.nlm.nih.gov/39437014), ORR 4%) reads as a negative basket precedent. CAPTUR Group 8 palbociclib arm is listed closed. The CDK4/6 axis appears as rank 11 (considered_with_caveats) on the combination-strategy rationale rather than as a standalone class.

## Ranked prioritization

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Intervention</th><th>Likelihood of effect</th><th>Toxicity burden</th><th>Counter-productive MoA</th><th>Overall</th></tr></thead>
      <tbody>
        <tr>
          <td>1</td>
          <td><strong>KRAS G12R orthogonal NGS + ctDNA confirmation</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Diagnostic certainty — locks the G12R call for trial entry and anchors a baseline ctDNA VAF for monitoring on pan-RAS therapy.</td>
          <td>Low (none — orthogonal NGS / ctDNA on blood draw plus optional archival FFPE)</td>
          <td><strong>N/A</strong> <span class="cpm-desc">(diagnostic, not therapeutic — no mechanism-level risk to the therapeutic goal)</span></td>
          <td><strong>Non-therapeutic workup that hardens the KRAS G12R call before pan-RAS trial entry and seeds the ctDNA baseline for on-treatment monitoring.</strong></td>
        </tr>
        <tr>
          <td>2</td>
          <td><strong>daraxonrasib (RMC-6236) 300 mg PO monotherapy on NCT05379985</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>High in 2L RAS G12 PDAC at 300 mg — ORR 35%, mPFS 8.5 mo, mOS 13.1 mo (Wolpin NEJM 2026, n=26). G12R is inside the pooled estimand.</td>
          <td>Moderate (rash 91% any-grade / G3+ 8%; diarrhea 48% / G3+ 2%; stomatitis 31% / G3+ 3%; G3+ TRAE 30% overall)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(Residual wild-type-RAS pharmacology window is tight in some tissues; KPC-model relapse linked to MYC amplification)</span></td>
          <td><strong>Only published meaningful effect size on KRAS G12R PDAC; recruiting trial with fully mapped AE distribution and matched mechanism. Phase 3 confirmation pending.</strong></td>
        </tr>
        <tr>
          <td>3</td>
          <td><strong>PF-07934040 pan-KRAS small-molecule on NCT06447662</strong><br><small><em>endorse:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Moderate — class extrapolation from daraxonrasib (PMID 42090791); no PF-07934040 efficacy readout yet. G12R explicit in eligibility.</td>
          <td>Low (no published AE data yet; class-effect rash + GI expected from pan-KRAS chemistry; G2+ neuropathy is an enrollment exclusion)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(Same pan-KRAS class window as daraxonrasib; no persona dissent on mechanism for this row)</span></td>
          <td><strong>Backup-class pan-KRAS lane with explicit G12R eligibility; useful if the daraxonrasib slot is unavailable, but no published efficacy yet anchors the rank.</strong></td>
        </tr>
        <tr>
          <td>4</td>
          <td><strong>anvumetostat (AMG 193) + daraxonrasib on NCT06360354</strong> (gated on MTAP co-deletion reflex)<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Moderate if MTAP is co-deleted — preclinical foundation strong (>70-fold selectivity, Smith 2023). No PDAC clinical readout yet; combination arm covers two features on one trial.</td>
          <td>Low (no published clinical AE data for the combination; MTA-cooperative class designed to spare the hematologic toxicity of first-generation PRMT5 inhibitors)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(Synthetic-lethal mechanism is clean; cooperative MTA chemistry limits exposure to MTAP-proficient tissue)</span></td>
          <td><strong>Dual-feature trial covering KRAS G12R and CDKN2A / MTAP loss on a single regimen — gated on MTAP co-deletion reflex testing.</strong></td>
        </tr>
        <tr>
          <td>5</td>
          <td><strong>olaparib maintenance after platinum induction — POLO regimen</strong> (gated on germline BRCA1/2 / PALB2 + platinum induction)<br><small><em>endorse:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>dissent:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>High when both gates open — PFS HR 0.53 (Golan 2019 NEJM POLO). Interim OS HR 0.91 means OS benefit not yet demonstrated.</td>
          <td>Moderate (G3+ AEs 40% olaparib vs 23% placebo; AE discontinuation 5%; MDS / AML class risk ~1.5% on prolonged exposure)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(Synthetic-lethal mechanism well-characterized; reversion mutations restoring BRCA function are the documented resistance route)</span></td>
          <td><strong>Only RCT-grade option in the dossier — high-confidence when germline BRCA/PALB2 confirms and platinum induction succeeds, but two sequential gates remain locked.</strong></td>
        </tr>
        <tr>
          <td>6</td>
          <td><strong>daraxonrasib + mFOLFIRINOX or gem/nab on NCT06445062 (RMC-GI-102)</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span></small></td>
          <td>Moderate-to-high if RAMP-205 dose-level-1 (5/6 PR, ORR 83%, n=6) survives N — exact 95% CI on 5/6 runs 36-100%. Daraxonrasib + chemo PDAC-cohort efficacy not yet public.</td>
          <td>High (rash + GI from pan-RAS stacked with chemo cytopenias and neuropathy; no published dedicated combination-safety table)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(Cumulative on-target wild-type-RAS exposure plus chemo myelosuppression — conservative dissented on the missing combination-safety publication)</span></td>
          <td><strong>Higher-ceiling combination lane that matches the treat-to-remission preference, but no published dedicated PDAC combination-safety data yet — contingent on sponsor cohort openness and an AE-distribution readout.</strong></td>
        </tr>
        <tr>
          <td>7</td>
          <td><strong>zoldonrasib (RMC-7977) + ivonescimab on NCT07397338</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small></td>
          <td>Low for clinical effect at present — zero published PDAC clinical data; preclinical KPC ceiling is high (Wasko Nature 2024) but allele-mismatched (G12D not G12R).</td>
          <td>Moderate (pan-RAS rash + GI stacked with PD-1xVEGF immune-mediated AEs; no published PDAC combination safety table)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(Diagnostic ambiguity between class rash and immune-rash complicates AE attribution; conservative dissented on this mechanism-level overlap)</span></td>
          <td><strong>Highest-ceiling preclinical option the patient could touch, but zero published clinical PDAC data and three persona dissents on evidence, toxicity, and guideline-fit.</strong></td>
        </tr>
        <tr>
          <td>8</td>
          <td><strong>ELI-002 7P amphiphile mKRAS peptide vaccine on NCT05726864 (AMPLIFY-7P)</strong><br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>dissent:</em> <span class="persona persona-concensusite">concensusite</span></small></td>
          <td>Low for this clinical state — designed for MRD-positive resected disease, not overt recurrence; AMPLIFY-201 read in the MRD window (Wainberg Nat Med 2025).</td>
          <td>Low (zero DLTs; no G3+ vaccine-attributed events across AMPLIFY-201 n=25; injection-site reactions dominate)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(T-cell exhaustion / antigen-loss escape on overt-disease bulk are the theoretical concerns; mechanism designed for MRD setting)</span></td>
          <td><strong>Cleanest safety in the dossier with G12R-explicit mechanism fit, but the MRD-positive enrollment window forecloses this patient's clinical state.</strong></td>
        </tr>
        <tr>
          <td>9</td>
          <td><strong>avutometinib + defactinib + gem/nab on NCT05669482 (RAMP-205)</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span></small><br><small><em>dissent:</em> <span class="persona persona-critic">critic</span></small></td>
          <td>Moderate-to-high in cross-tumor KRAS-mutant disease (LGSOC ORR 44% Banerjee 2025); PDAC signal is abstract-only at n=6 with 95% CI 36-100%.</td>
          <td>Moderate (four-agent stack: RAF/MEK class rash, edema, CK / FAKi GI / chemo cytopenias and neuropathy; no published dedicated PDAC combination AE table)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(Critic dissented on evidence-quality; cumulative MAPK + stromal + cytotoxic toxicity overlap is the mechanism-level risk to dose intensity)</span></td>
          <td><strong>Striking n=6 PDAC abstract signal and KRAS-mutant LGSOC cross-tumor validation, but trial is active not recruiting and the evidence base is one unpeer-reviewed abstract.</strong></td>
        </tr>
        <tr>
          <td>10</td>
          <td><strong>rucaparib maintenance — gated on germline / somatic BRCA / PALB2</strong><br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span></small></td>
          <td>Moderate when gates open — Reiss 2021 single-arm n=46 mPFS 13.1 / mOS 23.5 in platinum-sensitive BRCA / PALB2 PDAC; not RCT-grade.</td>
          <td>Moderate (PARP class effects mirroring olaparib; MDS / AML class risk on prolonged exposure)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(Same synthetic-lethal mechanism as olaparib; reversion mutations restoring BRCA function are the documented resistance route)</span></td>
          <td><strong>PARP-class backup that widens the biomarker net beyond germline BRCA to include somatic BRCA / PALB2; same two locked gates as olaparib, phase 2 single-arm evidence.</strong></td>
        </tr>
        <tr>
          <td>11</td>
          <td><strong>palbociclib + MEK/ERK or IGF1R via ADOPT or off-label</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span></small></td>
          <td>Low for monotherapy (Z1C ORR 4%, O'Hara 2025); preclinical combination synergy in PDAC organoids (Knudsen 2023) has no PDAC clinical translation yet.</td>
          <td>Moderate (G3+ neutropenia is the class-defining AE; cumulative cytopenia risk when combined with chemo or MEKi)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(Single-agent CDK4/6i triggers RB-bypass compensation via cyclin D, MYC, and mTOR — the documented monotherapy escape route that Z1C confirmed)</span></td>
          <td><strong>Mechanism-fit on the CDKN2A / CCND3 axis but the closest published basket precedent (Z1C ORR 4%) is actively negative and PDAC combination data are preclinical-only.</strong></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

!!! note "Reading the columns"
    **Toxicity burden** is patient-level G3+ AE severity (Low / Moderate / High) summarized from the trial publications. **Counter-productive MoA** is the mechanism-level risk that the intervention's own pathway could blunt the therapeutic goal — distinct from patient AEs. The board's endorse / dissent / veto state appears as pills under each intervention; full per-persona rationale lives on the [board page](board.md).

## Caveats

- **Evidence-base caveats.** The load-bearing efficacy datum on the lead recommendation (Wolpin NEJM 2026 [PMID 42090791](https://pubmed.ncbi.nlm.nih.gov/42090791)) is ROBINS-I:Moderate, single-arm open-label, n=26 in the 2L RAS G12 PDAC 300-mg subgroup with no separately published G12R-allele-resolved ORR. RASolute-302 ([NCT06625320](https://clinicaltrials.gov/study/NCT06625320)) phase 3 confirmation has not landed. The combination ranks (6, 7, 9) rest variously on ASCO abstracts (RAMP-205 at n=6) or zero published PDAC clinical data (RMC-7977 + ivonescimab). The only RoB2:Low RCT in the dossier (POLO) is gated on a germline result and a platinum induction the patient has not had.
- **Compartment / biomarker dependencies.** Rank 4 (PRMT5 + RAS) is contingent on MTAP co-deletion confirmation — order the reflex on the existing tumor block. Ranks 5 and 10 (olaparib, rucaparib) are contingent on germline BRCA1/2 / PALB2 status AND a platinum induction the patient has not had. MSS + TMB 4.1 forecloses biomarker-agnostic ICI cleanly (KEYNOTE-158 [PMID 31682550](https://pubmed.ncbi.nlm.nih.gov/31682550); CCTG PA.7 [PMID 36028483](https://pubmed.ncbi.nlm.nih.gov/36028483)); rank 7 is the only entry that touches the immune axis at all, under three persona dissents. The TP53 variant class (LOF vs dominant-negative vs GOF) is not yet annotated — closes the eprenetapopt door pending workup.
- **What would change the ranking.**
    - A G12R-resolved subgroup ORR within the Wolpin 2026 cohort, or the RASolute-302 OS readout landing, would tighten rank 2's confidence interval and possibly upgrade the chemo-combo lane (rank 6) on the strength of a chemo-arm signal.
    - A positive MTAP co-deletion reflex would move rank 4 above ranks 5-6 on dual-feature mechanism grounds.
    - A positive germline BRCA1/2 or PALB2 result plus a successful platinum induction would move rank 5 to the top of the gated lanes — but the induction is the treating team's decision and outside Libby's scope.
    - A published RMC-GI-102 PDAC-cohort AE distribution that fits inside the user's consent envelope would move rank 6 above rank 2 on the risktaker / advocate's preferred reading of the preferences.
    - A negative SMAD4 status on co-mutation reflex would weight aggressive multi-agent regimens; positive SMAD4 loss tilts toward enrollment-first framing because of the wider metastatic spread signal.
- **Re-scoping caveat.** If the user's preferences shift toward toxicity vetoes (e.g. veto on rash-class AEs, veto on inpatient cycle-1 monitoring) or hard modality constraints (e.g. oral-only), the ranking changes — daraxonrasib monotherapy's any-grade rash at 91% and the combination lanes' chemo backbones become disqualifying rather than tradeable. The current ranking assumes the preference set as supplied (efficacy 0.80, no vetoes, accept high-risk-high-reward, prefers trials).

## Sources

**PubMed (PMID):**

- [24986516](https://pubmed.ncbi.nlm.nih.gov/24986516) — Heilmann / Knudsen, palbociclib + IGF1R in p16-deficient PDAC, *Cancer Research* 2014
- [25156567](https://pubmed.ncbi.nlm.nih.gov/25156567) — Franco / Knudsen, palbociclib in PDAC primary explants, *Oncotarget* 2014
- [26912360](https://pubmed.ncbi.nlm.nih.gov/26912360) — Kryukov / Stegmeier, PRMT5 dependence in MTAP-deleted cancers, *Science* 2016
- [26912361](https://pubmed.ncbi.nlm.nih.gov/26912361) — Mavrakis / Sellers, PRMT5 / MTA cooperative mechanism, *Science* 2016
- [27376576](https://pubmed.ncbi.nlm.nih.gov/27376576) — Jiang / DeNardo, FAK inhibition + ICI in KPC, *Nature Medicine* 2016
- [29773717](https://pubmed.ncbi.nlm.nih.gov/29773717) — KEAP1 / STK11 co-mutation in KRAS-mutant disease
- [30019789](https://pubmed.ncbi.nlm.nih.gov/30019789) — SMAD4 prognostic signal in PDAC
- [30100704](https://pubmed.ncbi.nlm.nih.gov/30100704) — KRAS co-mutation landscape
- [30833748](https://pubmed.ncbi.nlm.nih.gov/30833748) — Kinsey / McMahon, MEK + autophagy in KRAS-mutant cancers, *Nature Medicine* 2019
- [30833752](https://pubmed.ncbi.nlm.nih.gov/30833752) — Bryant / Der, ERK + autophagy in PDAC, *Nature Medicine* 2019
- [31157963](https://pubmed.ncbi.nlm.nih.gov/31157963) — Golan / Kindler, POLO, olaparib maintenance in gBRCA PDAC, *NEJM* 2019
- [31649109](https://pubmed.ncbi.nlm.nih.gov/31649109) — Hobbs / Der, KRAS G12R signaling biology, *Cancer Discovery* 2020
- [31682550](https://pubmed.ncbi.nlm.nih.gov/31682550) — Marabelle / Diaz, KEYNOTE-158 MSI-H pembrolizumab, *JCO* 2020
- [33970687](https://pubmed.ncbi.nlm.nih.gov/33970687) — Reiss / Domchek, rucaparib in BRCA / PALB2 PDAC, *JCO* 2021
- [34376552](https://pubmed.ncbi.nlm.nih.gov/34376552) — Rakhra / Irvine, amphiphile mKRAS peptide vaccine preclinical platform, *JITC* 2021
- [34471132](https://pubmed.ncbi.nlm.nih.gov/34471132) — KRAS copy-number resistance mechanism
- [36028483](https://pubmed.ncbi.nlm.nih.gov/36028483) — Renouf / O'Callaghan, CCTG PA.7 dual ICI + chemo PDAC, *Nature Communications* 2022
- [36346366](https://pubmed.ncbi.nlm.nih.gov/36346366) — Knudsen / Witkiewicz, CDK4/6 + MEK in PDAC organoids, *Cancer Research* 2023
- [36546651](https://pubmed.ncbi.nlm.nih.gov/36546651) — Strickler / Hong, sotorasib in G12C PDAC (CodeBreaK 100), *NEJM* 2023
- [36952657](https://pubmed.ncbi.nlm.nih.gov/36952657) — KRAS ctDNA dynamics on KRAS-directed therapy
- [37099736](https://pubmed.ncbi.nlm.nih.gov/37099736) — Bekaii-Saab / Pant, adagrasib in G12C PDAC (KRYSTAL-1), *JCO* 2023
- [37552839](https://pubmed.ncbi.nlm.nih.gov/37552839) — Smith / Christensen, MRTX1719 MTA-cooperative PRMT5 inhibitor, *Cancer Discovery* 2023
- [38195752](https://pubmed.ncbi.nlm.nih.gov/38195752) — Pant / O'Reilly, ELI-002 2P AMPLIFY-201 first report, *Nature Medicine* 2024
- [38588697](https://pubmed.ncbi.nlm.nih.gov/38588697) — Wasko / Olive, RMC-7977 RAS(ON) in PDAC translational suite, *Nature* 2024
- [38589574](https://pubmed.ncbi.nlm.nih.gov/38589574) — Holderfield / Singh, RMC-6236 / RMC-7977 pan-RAS pharmacology, *Nature* 2024
- [38593348](https://pubmed.ncbi.nlm.nih.gov/38593348) — Jiang / Singh, RMC-6236 translational PDAC across G12 alleles, *Cancer Discovery* 2024
- [39437014](https://pubmed.ncbi.nlm.nih.gov/39437014) — O'Hara / Flaherty, NCI-MATCH Z1C palbociclib in CDK4/6-amplified solid tumors, *Clinical Cancer Research* 2025
- [40644648](https://pubmed.ncbi.nlm.nih.gov/40644648) — Banerjee, avutometinib + defactinib RAMP-201 LGSOC, *JCO* 2025
- [40790272](https://pubmed.ncbi.nlm.nih.gov/40790272) — Wainberg / O'Reilly, AMPLIFY-201 final report ELI-002 2P, *Nature Medicine* 2025
- [42090791](https://pubmed.ncbi.nlm.nih.gov/42090791) — Wolpin / Hong, daraxonrasib (RMC-6236) in 2L RAS G12 PDAC, *NEJM* 2026

**ClinicalTrials.gov (NCT):**

- [NCT02184195](https://clinicaltrials.gov/study/NCT02184195) — POLO (olaparib maintenance in gBRCA metastatic PDAC)
- [NCT05379985](https://clinicaltrials.gov/study/NCT05379985) — RMC-6236-001 (daraxonrasib FIH RAS G12X solid tumors)
- [NCT05669482](https://clinicaltrials.gov/study/NCT05669482) — RAMP-205 (avutometinib + defactinib + gem/nab in 1L PDAC)
- [NCT05726864](https://clinicaltrials.gov/study/NCT05726864) — AMPLIFY-7P (ELI-002 7P in resected KRAS-mutant solid tumors)
- [NCT06360354](https://clinicaltrials.gov/study/NCT06360354) — MTAPESTRY-103 (anvumetostat ± daraxonrasib in MTAP-deleted GI tumors)
- [NCT06445062](https://clinicaltrials.gov/study/NCT06445062) — RMC-GI-102 (daraxonrasib + chemo in RAS-mutant GI tumors)
- [NCT06447662](https://clinicaltrials.gov/study/NCT06447662) — PF-07934040 pan-KRAS phase 1 with G12R explicit
- [NCT06625320](https://clinicaltrials.gov/study/NCT06625320) — RASolute-302 (daraxonrasib phase 3 in 2L+ PDAC)
- [NCT06813079](https://clinicaltrials.gov/study/NCT06813079) — ADOPT (PDO-guided PDAC platform)
- [NCT07094204](https://clinicaltrials.gov/study/NCT07094204) — ASP5834 IV pan-KRAS phase 1 with G12R explicit
- [NCT07397338](https://clinicaltrials.gov/study/NCT07397338) — zoldonrasib (RMC-7977) + ivonescimab combination
- [NCT07492680](https://clinicaltrials.gov/study/NCT07492680) — MountainTAP-5 (BMS-986504 PRMT5i platform)

## Transparency artifacts

- [Trial table](trials.md) — 26 rows, all columns
- [Evidence list](evidence.md) — 16 clinical-evidence rows (11 included, 5 considered_excluded SoC chemo) + 22 preclinical rows
- [Manuscripts master table](manuscripts.md) — every paper considered with structured n, effect, variance, toxicity columns
- [Tumor-board transcript](board.md) — 5 positions, 20 cross-critiques
- [Recommendations table](recommendations.md) — full ranked detail
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Authored May 2026. Inputs: 26 trials, 16 clinical-evidence rows, 22 preclinical rows, 12 target-validation rows, 5 board positions with 20 cross-critiques. The case slug carries six confirmed biomarkers — KRAS G12R, TP53 inactivating, CDKN2A loss, CCND3 alteration, MSS, TMB 4.1 — so this is a non-gated case with `scenario: null` on every recommendation row. The user's report of KRAS G12R as confirmed turned the orthogonal NGS / ctDNA target-validator row from a pre-enrollment gate into workup hardening; it ranks first because pan-RAS / RAS(ON) sponsors re-test at screening regardless. The germline panel, MSS + TMB foreclosure, and TP53 variant-class workup are surfaced in the cross-cutting caveat rather than as ranked rows because they reframe the option set rather than gate a single trial. Humanizer pass applied to all prose sections per `.claude/skills/humanizer/SKILL.md`.

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
