<meta name="robots" content="noindex">

# `osteosarcoma-mets-dll3-h7r2`

<!-- libby:downloads:begin -->

## Downloads

- [Target validation paths](osteosarcoma-mets-dll3-h7r2-target-validation.pdf?v=78db61d6) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table](osteosarcoma-mets-dll3-h7r2-recommendations.html?v=689e06fd) — ranked options + pipeline context — self-contained HTML that opens offline
- [Access guide](accessibility.md?v=ced10fa1) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Master manuscripts table](manuscripts.md?v=0e17b1da) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Patient/caregiver PDF](osteosarcoma-mets-dll3-h7r2-plain-language.pdf?v=13dca4d1) — plain-language summary

<!-- libby:downloads:end -->

## Research question

In metastatic osteosarcoma after first-line MAP, what interventions can target DLL3 and PRAME, gated on protein-level confirmation (DLL3 IHC SP347; PRAME IHC + HLA-A*02:01 typing)?

## Patient profile (scrubbed)

- **Primary site / histology:** bone — osteosarcoma
- **Stage:** IV (metastatic)
- **Performance status (assumed):** ECOG 1
- **Age band (assumed):** 18-29 (typical osteosarcoma demographics; not user-supplied)
- **Sex:** unknown
- **Biomarkers:**
    - **DLL3 — RNA only (`confirmation_status: rna_only`); IHC SP347 status unknown.** Decision-relevant resolution: ≥1% (preferably ≥25%) by IHC for DLL3-directed clinical trials.
    - **PRAME — RNA only (`confirmation_status: rna_only`); IHC and HLA-A*02:01 status unknown.** Decision-relevant resolution: PRAME IHC positive AND HLA-A*02:01-positive (every PRAME-directed ImmTAC and TCR-T in clinical development is HLA-A*02:01-restricted).
- **Prior therapy (assumed):** MAP frontline; response not provided.

## Preferences

- **Efficacy/toxicity weight:** 0.85 (strong efficacy lean)
- **Toxicity vetoes:** none stated
- **Modality constraints:** none stated
- **Free text:** "accepts high-risk high-reward options"
- **Trials preferred:** yes

<!-- libby:target-validation:begin -->

## Target validation paths

The case has two RNA-only targetable features, each with its own protein-level confirmation step. **DLL3 IHC (clone SP347)** gates the DLL3-directed pathway: tarlatamab via NCT06788938 and the SHR-4849 / IDE849 ADC trial NCT07174583. **PRAME IHC plus HLA-A*02:01 typing** together gate the PRAME-directed pathway: IMA203 via NCT03686124 (Immatics ACTengine) and IMC-P115C via NCT07156136. The two pathways are independent. The patient may have neither, either, or both. All three workup tests can run in parallel on archival tissue and a single blood draw. If both workups return negative, this report has no within-scope recommendations, and the next conversation about standard 2L+ care is the treating team's, not Libby's.

### DLL3

Before any DLL3-directed therapy decision: DLL3 IHC SP347 on archival FFPE, ≥1% (preferably ≥25%) per NCT06788938's enrollment threshold. Turnaround is one to three weeks; cost is trivial relative to a treatment cycle. First, confirm SP347 assay availability at the treating institution. Not every reference lab carries the Roche Tissue Diagnostics clone used in the tarlatamab development program.

Two refinements sit one tier down. Spatial heterogeneity is a known confounder in solid-tumor DLL3 (Zhang 2023): if multiple tumor blocks are available, IHC on a metastatic site as well as the primary refines confidence in whether the gating result generalizes. Neuroendocrine context (ASCL1 / NEUROD1 / chromogranin / synaptophysin / INSM1 panel) is research-grade for an osteosarcoma. DLL3 is normally a Notch-pathway target on neuroendocrine lineage, so an unexpectedly positive DLL3 IHC in a non-NEC tumor is worth contextualizing before the trial enrollment paperwork.

Germline TP53 sequencing (Li-Fraumeni panel) is a separate kind of finding. It does not affect tarlatamab eligibility, but late-teens / twenties osteosarcoma carries a meaningful prior probability for germline TP53. A positive result changes radiation-sensitivity planning, prompts screening for synchronous tumors, and triggers cascade testing for first-degree relatives. Discuss with a genetic counselor before ordering.

### PRAME

Two essential tests gate the entire PRAME-directed pathway: **PRAME IHC** confirms tumor protein expression, and **HLA-A*02:01 typing** confirms the patient can present the PRAME peptide. Every PRAME-directed ImmTAC and TCR-T in clinical development (IMA203, brenetafusp, IMC-P115C) is HLA-A*02:01-restricted; typing-negative patients are foreclosed even when PRAME IHC is strongly positive. PRAME IHC is positive in roughly 56% of osteosarcoma (Iura 2017, n=82); HLA-A*02:01 prevalence is ~40–50% in Caucasian populations. Order both alongside the DLL3 IHC: same block, same blood draw, same turnaround window.

Spatial heterogeneity refines confidence at the next tier. PRAME IHC on a metastatic site as well as the primary helps rule out the case where one biopsy hits a focal expression hotspot. Tumor NGS for B2M loss-of-function and HLA-A*02:01 loss-of-heterozygosity is a resistance check: TCR-mediated killing depends on intact antigen presentation, and tumor-specific HLA-LOH is a documented escape mechanism that the IHC and HLA-typing workup will miss by design. Quantifying baseline CD8 T-cell infiltrate density via IHC (or multiplex CD3 / CD8 / FoxP3) is the microenvironment companion: an immune-cold tumor predicts diminished response even when PRAME and HLA are both positive.

### Where to order these assays

The preferred provider for each assay is marked **(preferred)**, selected on company size, reputation, US-based location, and turnaround time. Other providers in the row are listed in case the preferred lab is unreachable for this patient.

| Assay | Provider | Decision gated | Contact |
|---|---|---|---|
| **DLL3 IHC (clone SP347)** | **Foundation Medicine *(preferred)* (FoundationOne CDx + IHC reflex)** | **Tarlatamab via NCT06788938** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| DLL3 IHC (clone SP347) | Mayo Clinic Laboratories | Tarlatamab via NCT06788938 | [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 |
| DLL3 IHC (clone SP347) | NeoGenomics Laboratories | Tarlatamab via NCT06788938 | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| DLL3 IHC (clone SP347) | Caris Life Sciences | Tarlatamab via NCT06788938 | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| DLL3 IHC (clone SP347) | LabCorp / Esoterix Oncology | Tarlatamab via NCT06788938 | [test info](https://www.labcorp.com/oncology) · 358 South Main Street, Burlington, NC 27215 · 1-800-345-4363 |
| **DLL3 multi-region IHC (heterogeneity)** | **NeoGenomics Laboratories *(preferred)*** | **Refines DLL3 IHC gating result; does not gate enrollment** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| DLL3 multi-region IHC | Foundation Medicine | Refines DLL3 IHC gating result; does not gate enrollment | [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| DLL3 multi-region IHC | Mayo Clinic Laboratories | Refines DLL3 IHC gating result; does not gate enrollment | [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 |
| DLL3 multi-region IHC | Memorial Sloan Kettering Diagnostic Molecular Pathology | Refines DLL3 IHC gating result; does not gate enrollment | [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |
| **Neuroendocrine IHC panel (ASCL1 / NEUROD1 / chromogranin / synaptophysin / INSM1)** | **Mayo Clinic Laboratories *(preferred)*** | **Confirms DLL3 target call (neuroendocrine biology); does not gate enrollment** | **[test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710** |
| Neuroendocrine IHC panel | ARUP Laboratories | Confirms DLL3 target call (neuroendocrine biology); does not gate enrollment | [test info](https://www.aruplab.com/) · 500 Chipeta Way, Salt Lake City, UT 84108 · 1-800-242-2787 |
| Neuroendocrine IHC panel | LabCorp / Esoterix Oncology | Confirms DLL3 target call (neuroendocrine biology); does not gate enrollment | [test info](https://www.labcorp.com/oncology) · 358 South Main Street, Burlington, NC 27215 · 1-800-345-4363 |
| Neuroendocrine IHC panel | Quest Diagnostics | Confirms DLL3 target call (neuroendocrine biology); does not gate enrollment | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| Neuroendocrine IHC panel | Memorial Sloan Kettering Diagnostic Molecular Pathology | Confirms DLL3 target call (neuroendocrine biology); does not gate enrollment | [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |
| **Germline TP53 (Li-Fraumeni panel)** | **Invitae *(preferred)* (Common Hereditary Cancers Panel)** | **Reframes radiation, synchronous-tumor screening, and family cascade testing; does not affect tarlatamab eligibility** | **[test info](https://www.invitae.com/en/providers/test-catalog) · 1400 16th Street, San Francisco, CA 94103 · 1-800-436-3037** |
| Germline TP53 panel | GeneDx | Reframes radiation, synchronous-tumor screening, and family cascade testing; does not affect tarlatamab eligibility | [test info](https://www.genedx.com/tests) · 207 Perry Parkway, Gaithersburg, MD 20877 · 1-888-729-1206 |
| Germline TP53 panel | Ambry Genetics *(CancerNext)* | Reframes radiation, synchronous-tumor screening, and family cascade testing; does not affect tarlatamab eligibility | [test info](https://www.ambrygen.com/providers/test-menu) · 1 Enterprise, Aliso Viejo, CA 92656 · 1-866-262-7943 |
| Germline TP53 panel | Myriad Genetics *(MyRisk Hereditary Cancer)* | Reframes radiation, synchronous-tumor screening, and family cascade testing; does not affect tarlatamab eligibility | [test info](https://myriad.com/genetic-tests/myrisk-hereditary-cancer/) · 320 Wakara Way, Salt Lake City, UT 84108 · 1-800-469-7423 |
| Germline TP53 panel | Color Health | Reframes radiation, synchronous-tumor screening, and family cascade testing; does not affect tarlatamab eligibility | [test info](https://www.color.com/) · 831 Mitten Road, Burlingame, CA 94010 · 1-844-352-6567 |
| **PRAME IHC (clone EPR20330 or equivalent)** | **NeoGenomics Laboratories *(preferred)*** | **IMA203 (NCT03686124) and the PRAME ImmTAC class (brenetafusp, IMC-P115C); every program gates on PRAME IHC** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| PRAME IHC | Caris Life Sciences | IMA203 / brenetafusp / IMC-P115C; every program gates on PRAME IHC | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| PRAME IHC | Foundation Medicine | IMA203 / brenetafusp / IMC-P115C; every program gates on PRAME IHC | [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| PRAME IHC | LabCorp / Esoterix Oncology | IMA203 / brenetafusp / IMC-P115C; every program gates on PRAME IHC | [test info](https://www.labcorp.com/oncology) · 358 South Main Street, Burlington, NC 27215 · 1-800-345-4363 |
| PRAME IHC | Mayo Clinic Laboratories | IMA203 / brenetafusp / IMC-P115C; every program gates on PRAME IHC | [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 |
| **HLA Class I high-resolution typing (HLA-A*02:01)** | **HistoGenetics *(preferred)*** | **IMA203 and the PRAME ImmTAC class; every program is HLA-A*02:01-restricted** | **[test info](https://www.histogenetics.com/) · 1 Patrick Henry Drive, Stewartsville, NJ 08886 · 1-845-356-3801** |
| HLA Class I typing | Versiti / Wisconsin Diagnostic Laboratories | IMA203 and the PRAME ImmTAC class; every program is HLA-A*02:01-restricted | [test info](https://www.versiti.org/medical-professionals/diagnostic-labs) · 638 N 18th Street, Milwaukee, WI 53233 · 1-800-245-3117 |
| HLA Class I typing | ARUP Laboratories | IMA203 and the PRAME ImmTAC class; every program is HLA-A*02:01-restricted | [test info](https://www.aruplab.com/) · 500 Chipeta Way, Salt Lake City, UT 84108 · 1-800-242-2787 |
| HLA Class I typing | Mayo Clinic Laboratories | IMA203 and the PRAME ImmTAC class; every program is HLA-A*02:01-restricted | [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 |
| HLA Class I typing | Stanford Histocompatibility Laboratory | IMA203 and the PRAME ImmTAC class; every program is HLA-A*02:01-restricted | [test info](https://stanfordbloodcenter.org/healthcare-professionals/histocompatibility/) · 3373 Hillview Avenue, Palo Alto, CA 94304 · 1-650-723-7960 |
| **PRAME multi-region IHC (heterogeneity)** | **NeoGenomics Laboratories *(preferred)*** | **Refines PRAME IHC gating result; does not gate enrollment** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| PRAME multi-region IHC | Caris Life Sciences | Refines PRAME IHC gating result; does not gate enrollment | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| PRAME multi-region IHC | Foundation Medicine | Refines PRAME IHC gating result; does not gate enrollment | [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| PRAME multi-region IHC | Mayo Clinic Laboratories | Refines PRAME IHC gating result; does not gate enrollment | [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 |
| PRAME multi-region IHC | Memorial Sloan Kettering Diagnostic Molecular Pathology | Refines PRAME IHC gating result; does not gate enrollment | [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |
| **Tumor NGS for HLA-LOH / B2M / antigen-presentation** | **Memorial Sloan Kettering *(preferred)* (MSK-IMPACT)** | **Frames durability and post-progression sequencing for PRAME-directed therapy** | **[test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000** |
| Tumor NGS (HLA-LOH / B2M) | Foundation Medicine *(FoundationOne CDx)* | Frames durability and post-progression sequencing for PRAME-directed therapy | [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| Tumor NGS (HLA-LOH / B2M) | Caris Life Sciences *(Molecular Intelligence)* | Frames durability and post-progression sequencing for PRAME-directed therapy | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| Tumor NGS (HLA-LOH / B2M) | Tempus *(xT)* | Frames durability and post-progression sequencing for PRAME-directed therapy | [test info](https://www.tempus.com/oncology/diagnostics/) · 600 West Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| Tumor NGS (HLA-LOH / B2M) | NeoGenomics Laboratories *(NeoTYPE Comprehensive)* | Frames durability and post-progression sequencing for PRAME-directed therapy | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| **CD8 / TIL density (multiplex IHC)** | **NeoGenomics Laboratories *(preferred)* (MultiOmyx)** | **Frames durability of PRAME-directed therapy; informs the next-line plan if IMA203 or IMC-P115C fails** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| CD8 / TIL density | Caris Life Sciences | Frames durability of PRAME-directed therapy | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| CD8 / TIL density | Foundation Medicine | Frames durability of PRAME-directed therapy | [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| CD8 / TIL density | Mayo Clinic Laboratories | Frames durability of PRAME-directed therapy | [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 |
| CD8 / TIL density | Memorial Sloan Kettering Diagnostic Molecular Pathology | Frames durability of PRAME-directed therapy | [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |

### Biomarker plan

| Recommended assay | Rationale | Suggested assay provider | Tissue requirements |
|---|---|---|---|
| DLL3 IHC (clone SP347) | RNA expression establishes that the DLL3 gene is being transcribed; it does not establish that DLL3 protein sits on the cell surface where a BiTE can engage. NCT06788938 enforces IHC ≥ 25% (stage 1) or ≥ 1% (stage 2) for enrollment, and every approved DLL3-directed therapy gates on protein-level confirmation. Skipping the test forecloses every DLL3-directed candidate downstream by definition. | Foundation Medicine *(FoundationOne CDx (DLL3 IHC reflex))* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | archival FFPE; fresh biopsy not required if stored tissue is adequate |
| DLL3 IHC on multiple tumor regions / metastatic biopsy | Osteosarcoma metastases can diverge from primary tumors in surface-marker expression, and the cross-tumor DLL3 literature in solid tumors (Zhang 2023) flags spatial heterogeneity as a frequent confounder. Testing one site can over- or under-estimate enrollment-grade DLL3 status. If only one block is available the workup proceeds with that block, but the result should be interpreted with this caveat in mind. | NeoGenomics Laboratories · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | additional archival blocks from a different site if available |
| ASCL1 / NEUROD1 IHC + chromogranin / synaptophysin / INSM1 panel | DLL3 is a Notch-pathway target normally expressed in neuroendocrine lineage. In a non-NEC tumor like osteosarcoma, surfacing or excluding any neuroendocrine differentiation pattern (Notch-low / ASCL1-high state) provides mechanistic context for whether DLL3 expression is biologically plausible or a stochastic finding. Does not gate enrollment; informs how the tarlatamab trial outcome should be interpreted. | Mayo Clinic Laboratories · [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 | archival FFPE; same block as the DLL3 IHC |
| Germline TP53 sequencing (Li-Fraumeni panel) | Osteosarcoma in the late-teens to twenties carries a meaningful prior probability of germline TP53 (Li-Fraumeni). A positive germline TP53 result changes radiation-sensitivity considerations, screening for synchronous tumors, and family screening for first-degree relatives. Does not affect tarlatamab eligibility, but is the kind of finding that would change the surrounding care plan. | Invitae *(Invitae Common Hereditary Cancers Panel)* · [test info](https://www.invitae.com/en/providers/test-catalog) · 1400 16th Street, San Francisco, CA 94103 · 1-800-436-3037 | 5–10 mL EDTA whole blood |
| PRAME IHC (clone EPR20330 or equivalent) | RNA expression establishes that the PRAME gene is being transcribed; it does not establish that the PRAME peptide is presented at sufficient density to engage a TCR or ImmTAC. PRAME-targeting therapies in development (IMA203 ACTengine, brenetafusp, IMC-P115C) require IHC-confirmed PRAME protein expression on tumor cells. PRAME IHC is positive in ~56% of osteosarcoma (Iura 2017, n=82). Skipping the IHC forecloses every PRAME-directed candidate downstream by definition. | NeoGenomics Laboratories · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | archival FFPE; same block as the DLL3 IHC |
| HLA Class I high-resolution typing (HLA-A*02:01 specifically) | Every PRAME-directed ImmTAC and TCR-T in clinical development is HLA-A*02:01-restricted; the PRAME peptide is presented on HLA-A*02:01, and patients without this allele cannot present the target. HLA-A*02:01 prevalence is ~40–50% in Caucasian populations; without typing, the patient's eligibility for the entire HLA-restricted PRAME class is unknown. Every PRAME-directed program (IMA203 via NCT03686124, brenetafusp, IMC-P115C via NCT07156136) is foreclosed if HLA-A*02:01 typing returns negative. | HistoGenetics · [test info](https://www.histogenetics.com/) · 1 Patrick Henry Drive, Stewartsville, NJ 08886 · 1-845-356-3801 | 5–10 mL EDTA whole blood |
| PRAME IHC on multiple tumor regions / metastatic biopsy | PRAME expression is heterogeneous across tumor regions, particularly in solid tumors outside melanoma. Iura 2017 reported variable PRAME staining intensity across osteosarcoma cases; primary-vs-metastatic discordance is a documented confounder for PRAME-directed therapy selection. Multi-region IHC refines confidence that the binary positive call is representative of the dominant disease. | NeoGenomics Laboratories · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | additional archival blocks from a different site if available |
| Tumor NGS for HLA loss-of-heterozygosity, B2M loss-of-function, and antigen-presentation pathway | TCR-based and ImmTAC therapies depend on intact HLA-Class-I antigen presentation on tumor cells. Tumor-specific HLA-A*02:01 loss-of-heterozygosity, B2M loss-of-function mutations, or upstream antigen-presentation defects render the cell invisible to TCR-mediated killing even with PRAME expression preserved. Detecting these alterations does not foreclose enrollment but reframes the durability expectation and informs sequencing planning. | Memorial Sloan Kettering Diagnostic Molecular Pathology *(MSK-IMPACT)* · [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 | archival FFPE; matched germline blood is required for tumor-specific HLA-LOH calling |
| Tumor CD8+ T-cell infiltrate density (CD8 IHC, optionally with multiplex CD3 / CD8 / FoxP3) | TCR-based therapies require T-cell trafficking into the tumor; an immune-cold microenvironment with low CD8 density predicts diminished response even when PRAME and HLA are both positive. Quantifying baseline TIL density frames durability expectations and is informative for the next-line conversation if PRAME-directed therapy fails. Does not gate enrollment. | NeoGenomics Laboratories *(MultiOmyx multiplex IHC)* · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | archival FFPE; same block as the PRAME IHC |
---

*Decision support, not medical advice. Confirm assay availability and current standards with the treating team and the local pathology service.*

<!-- libby:target-validation:end -->

## Scope summary

29 trials surfaced (21 DLL3-targeting + 8 PRAME-targeting, spanning ten modality classes across the two pathways). 5 clinical-evidence rows (4 included + 1 excluded). 6 preclinical rows. Five ranked rows: a dual-biomarker workup gate at rank 1, two DLL3-conditional therapeutic options (rank 2 tarlatamab; rank 3 SHR-4849 *considered with caveats*), and two PRAME-conditional therapeutic options (rank 4 IMA203 ACTengine basket; rank 5 IMC-P115C *considered with caveats*). The board reached full consensus on the workup. One persistent dissent (critic) sits on rank 2; two dissents (critic, conservative) sit on rank 3 and on rank 5; one dissent (conservative) sits on rank 4. The case is scoped to drugs that act on the user's stated targetable features (DLL3 and PRAME); standard 2L+ care for the indication is out of scope and is not enumerated.

## Cross-cutting caveat (read first)

**Both targetable features are RNA-only. Neither DLL3 nor PRAME RNA expression alone establishes a workable target — protein-level confirmation is required for both, and PRAME additionally requires HLA-A*02:01 typing.** The rank-1 dual workup is the precondition for everything else; it can be run in parallel.

- **DLL3 pathway (ranks 2-3)** is conditional on DLL3 IHC ≥1% (preferably ≥25%) by SP347. Rank 2 (tarlatamab via NCT06788938) is the actionable option; rank 3 (SHR-4849 via NCT07174583) is the tentative second DLL3 pathway pending sponsor confirmation of osteosarcoma eligibility.
- **PRAME pathway (ranks 4-5)** is conditional on PRAME IHC positivity AND HLA-A*02:01-positive typing — both required because every PRAME-directed ImmTAC and TCR-T in clinical development is HLA-A*02:01-restricted. Rank 4 (IMA203 via NCT03686124 ACTengine pan-solid basket) has the strongest published efficacy signal in the PRAME class (54% ORR, Wermke 2024 Lancet Oncol). Rank 5 (IMC-P115C via NCT07156136) is the second PRAME pathway, ImmTAC mechanism class, considered with caveats.
- **The two pathways are independent.** DLL3 and PRAME confirmation are independent biomarkers; the patient may have neither, either, or both. Each ranked option foreclosure is independent — a negative DLL3 IHC does not foreclose the PRAME ranks, and vice versa. **If both workups are negative, the case has no within-scope recommendations** and standard 2L+ care for osteosarcoma is the treating team's separate conversation.
- **Workup logistics:** all three tests (DLL3 IHC, PRAME IHC, HLA-A*02:01 typing) are non-toxic and can run in parallel on archival tissue + a single blood draw for HLA. Total turnaround one to three weeks. The dual-biomarker workup costs trivially relative to a treatment cycle. Confirm assay availability at the treating institution before relying on a specific lab.
- **Pipeline visibility.** The dossier surfaces 21 DLL3-targeting agents (seven modality classes) and 8 PRAME-targeting agents (TCR-T, ImmTAC, TCER bispecific, mRNA combo, legacy iCasp9-TCR). Most are SCLC/NEC-scoped (DLL3) or melanoma-scoped (PRAME) and not directly enrollable for osteosarcoma — they remain in the dossier as evidence-base context. The patient-actionable subset is the rank 2-5 set, all gated on the rank-1 dual workup.

## Intervention grouping

### DLL3 pathway

- **DLL3 × CD3 BiTEs (biomarker-conditional, actionable via NCT06788938):** tarlatamab. Anchor evidence: DeLLphi-301 ([PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218)) + DeLLphi-304 ([PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646)).
- **Other DLL3 × CD3 / CD137 BiTEs and trispecifics (pipeline context, SCLC/NEC-scoped):** obrixtamig (BI 764532, Boehringer Ingelheim DAREON phase 3), gocatamig (MK-6070 / HPN328 / DS3280, Harpoon→Merck), alveltamig (ZG006, Zelgen phase 3), clesitamig (RO7616789, Roche), QLS31904.
- **DLL3 × CD47 bispecifics (non-T-cell-engager class):** peluntamig (PT217, Phanes Therapeutics).
- **DLL3 ADCs (TOP1-inhibitor or DXd payload, post-Rova-T era):** zocilurtatug pelitecan (ZL-1310, Zai Lab phase 3), SHR-4849 / IDE849 (IDEAYA / Hengrui), IBI3009 (Innovent), FZ-AD005 (Shanghai Fudan-Zhangjiang).
- **DLL3 radiopharmaceuticals (radiation mechanism, antigen-loss-resistant):** ²²⁵Ac-ABD147 (Abdera), ¹⁷⁷Lu-DTPA-SC16.56 (Memorial Sloan Kettering), ²²⁵Ac-ETN029 (Novartis).
- **DLL3 cell therapies:** LB2102 autologous CAR-T (Legend Biotech), DLL3-CAR-NK cells (Tianjin academic). AMG 119 was Amgen's first-generation CAR-T program — currently suspended.
- **Discontinued DLL3 ADCs (mechanism context for current ADC entrants):** rovalpituzumab tesirine / Rova-T (TAHOE phase-3 failure, AbbVie discontinued), SC-002 (Stemcentrx, terminated in phase 1).

### PRAME pathway

- **PRAME-TCR-T (biomarker-conditional, actionable via NCT03686124 ACTengine pan-solid basket):** IMA203 / IMA203CD8 (Immatics). Anchor evidence: Wermke 2024 ([PMID 38821093](https://pubmed.ncbi.nlm.nih.gov/38821093); ORR 54% in cross-tumor PRAME+ HLA-A*02:01+ basket including sarcomas).
- **PRAME ImmTAC bispecifics (biomarker-conditional, ranks 4-5):** brenetafusp / IMC-F106C (Immunocore lead, melanoma-pivotal phase 3 PRISM-MEL-301; pan-solid sarcoma cohort active not recruiting), IMC-P115C (Immunocore next-generation pan-tumor PRAME ImmTAC, NCT07156136). ImmTAC platform is class-validated via tebentafusp (Kimmtrak, approved in uveal melanoma). Anchor: Hamid 2024 ([PMID 39007852](https://pubmed.ncbi.nlm.nih.gov/39007852)).
- **PRAME TCER half-life-extended bispecifics:** IMA402 (Immatics, NCT05958121). Mechanism-bridge between brenetafusp ImmTAC and IMA203 TCR-T.
- **PRAME mRNA combinations:** IMA203 + mRNA-4203 (Immatics + Moderna, NCT06946225). Synovial sarcoma in scope; osteosarcoma not on protocol but mechanism-relevant.
- **Discontinued PRAME-TCR programs:** BPX-701 (Bellicum, terminated phase 1/2 with iCasp9 safety switch). Decision-relevant only as historical context for the PRAME-TCR class — IMA203 is the active inheritor.

### Cross-pathway

- **Pan-pathway radio-immunotherapy & radioligands** (DLL3 only; no PRAME radioligand programs in development): see DLL3 group above.

## Top interventions

### Rank 1. Dual-biomarker workup — DLL3 IHC (SP347) + PRAME IHC + HLA-A*02:01 typing

*Non-toxic. Resolves which of the two targetable-feature pathways is open. Run all three tests in parallel.*

#### Evidence base

The case has two RNA-only targetable features, each with a distinct protein-level confirmation step. **DLL3 IHC** (SP347) gates ranks 2-3: NCT06788938 enforces ≥25% (stage 1) or ≥1% (stage 2) by IHC; every DLL3-directed therapy in clinical development gates on protein-level confirmation, not transcript. **PRAME IHC + HLA-A*02:01 typing** together gate ranks 4-5: PRAME-targeting drugs are HLA-A*02:01-restricted (the PRAME peptide is presented on HLA-A*02:01) and additionally require PRAME protein expression on the tumor cell. PRAME IHC is positive in ~56% of osteosarcoma cases (Iura 2017, [PMID 28315425](https://pubmed.ncbi.nlm.nih.gov/28315425), n=82); HLA-A*02:01 prevalence is ~40-50% in Caucasian populations.

#### Likelihood of desired effect

The dual workup resolves which of two pathways is reachable. The two are independent — the patient may have neither, either, or both. Non-toxic and cheap regardless of result.

#### Toxicity profile

- None. IHC on archival FFPE + a single blood draw for HLA typing.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. No persona dissented or vetoed.

#### Practical considerations

All three tests run in parallel. DLL3 IHC SP347 and PRAME IHC use archival or fresh tumor (no fresh biopsy required). HLA-A*02:01 typing runs on a blood sample with same-day to one-week turnaround at most reference labs. Confirm assay availability at the treating institution: SP347 (Roche Tissue Diagnostics clone) is not universally stocked, PRAME IHC clones vary by lab (commonly EPR23197), and HLA typing is widely available. The full workup is the precondition for any DLL3- or PRAME-directed action.

#### Why this rank

The dual workup is the precondition for ranks 2-5. The board treated it as a gate, not as a therapy.

#### Per-trial detail

| Test / trial | Efficacy context | Toxicity | Reference |
|---|---|---|---|
| DLL3 IHC SP347 (assay) | Gates enrollment in DLL3-directed therapy trials | None — diagnostic | [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) |
| PRAME IHC + HLA-A*02:01 typing (assay pair) | Gates enrollment in PRAME-directed therapy trials (ImmTAC + TCR-T) | None — diagnostic | [NCT03686124](https://clinicaltrials.gov/study/NCT03686124), [PMID 28315425](https://pubmed.ncbi.nlm.nih.gov/28315425) |

---

### Rank 2. Tarlatamab via NCT06788938

*Conditional on `dll3_ihc:positive`. Foreclosed if test is negative.*

*Bispecific T-cell engager with strong cross-tumor efficacy data in SCLC. The user's stated preferences fit this option when the trial is reachable. One persistent dissent on cross-tumor translation.*

#### Evidence base

NCT06788938 (single-arm phase 2 basket, Simon two-stage, n=29 planned) is the trial enrolling osteosarcoma at biomarker-positive resolution. The mechanistic case rests on cross-tumor evidence: DeLLphi-301 ([PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218); ORR 40%, n=220 SCLC) and the confirmatory DeLLphi-304 phase 3 ([PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646); OS HR 0.60, 95% CI 0.47–0.77, median OS 13.6 vs 8.3 mo). No published osteosarcoma data with tarlatamab exist.

#### Likelihood of desired effect

Assuming positive IHC, mechanism-fit is concordant. Whether SCLC's clinical effect transfers to osteosarcoma is the open question this trial enrollment would answer. The user's preferences (efficacy lean 0.85, accepts high-risk-high-reward, prefers trials) fit this option. **A negative IHC forecloses this rec entirely.**

#### Toxicity profile

- CRS in ~50% (mostly grade 1–2; grade ≥3 ~1% in SCLC)
- ICANS-like neurologic events ~10%
- Inpatient cycle-1 step-up dosing required for CRS mitigation
- Step-up dosing: 1 mg D1, 10 mg D8/D15, then 10 mg q2w (28-day cycles)

User has no toxicity vetoes; CRS and inpatient cycle-1 chair time are not flagged.

#### Counter-productive mechanisms / dissent

**The critic's dissent persists.** No published osteosarcoma data with tarlatamab. Cross-tumor translation from SCLC is unproven, and the trial's basket design exists to test that premise. The conservative's earlier toxicity veto (issued under the IHC-unconfirmed scenario) lifts on biomarker confirmation; its own rationale specified the veto was contingent on IHC. Concensusite's qualified-on-guideline-fit position upgrades to endorsement when the trial-enrollment principle is the relevant frame.

#### Practical considerations

- Trial open at NCT06788938 (recruiting). Confirm slot availability at the treating site.
- Trial enrollment is NCCN cat-1 for relapsed osteosarcoma regardless of mechanism.
- Inpatient cycle-1 monitoring required.
- Off-guideline for osteosarcoma per indication; the trial provides the regulatory pathway.

#### Why this rank

The only DLL3-directed therapeutic option on the table, conditional on biomarker confirmation. Foreclosed entirely if IHC is negative.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Tarlatamab — NCT06788938 DLL3-IHC-selected basket (osteosarcoma included), n=29 planned | ORR endpoint at 18 mo (primary); no osteosarcoma data yet | Per SCLC mechanism: CRS ~50%, ICANS ~10%, inpatient C1 | [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) |
| Tarlatamab — DeLLphi-301 SCLC (cross-tumor mechanism evidence), n=220 | ORR 40% (95% CI 29–52); mPFS 4.9 mo | CRS ~50% (G3+ ~1%); ICANS ~10%; G3+ TRAEs 30% | [PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218) |
| Tarlatamab — DeLLphi-304 SCLC (cross-tumor confirmatory), n=509 | OS HR 0.60 (95% CI 0.47–0.77), p<0.001; median OS 13.6 vs 8.3 mo | G3+ TRAEs 24% vs 53% chemo arm — favorable vs comparator | [PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646) |

---

### Rank 3. SHR-4849 / IDE849 via NCT07174583 — IDEAYA pan-tumor DLL3 basket

*Status: **considered with caveats**. Conditional on `dll3_ihc:positive` AND IDEAYA confirming osteosarcoma is on the basket eligibility list. Two dissents (critic, conservative).*

*Mechanism-distinct second DLL3 pathway — TOP1-inhibitor ADC payload (post-Rova-T era). Relevant if the BiTE path is foreclosed or fails. No published clinical data yet.*

#### Evidence base

NCT07174583 is IDEAYA Biosciences' phase 1/2 dose-escalation + expansion trial of SHR-4849 / IDE849 (DLL3-targeted ADC, TOP1-inhibitor payload, originated by Jiangsu Hengrui), monotherapy and in combination with durvalumab or IDE161. Eligibility names "DLL3-expressing tumors" without an explicit SCLC/NEC restriction — pan-tumor in principle. The osteosarcoma fit is **not yet confirmed by the sponsor**: the trial wording suggests it should be in scope, but the published eligibility text does not state it outright. No clinical data for SHR-4849 has been published yet (first-in-class signal pending).

#### Likelihood of desired effect

Speculative. TOP1-inhibitor ADC precedent (T-DXd, sacituzumab govitecan, Dato-DXd) suggests the payload class can produce durable response signals across solid tumors when the surface antigen is sufficiently expressed. DLL3-specific efficacy is the open question. Assuming positive IHC AND osteosarcoma is on the basket, this is a mechanism-class diversification away from BiTE-only DLL3 targeting — a hedge against tarlatamab-specific failure modes (CRS intolerance, ICANS, antigen-loss escape from CD3 engagement).

#### Toxicity profile

- No published clinical AE rates for SHR-4849 yet
- Expected per TOP1-inhibitor ADC class: cytopenias (neutropenia, thrombocytopenia), GI (nausea, vomiting, diarrhea), fatigue
- ILD/pneumonitis is a class signal worth monitoring (DXd-class ADCs carry an explicit ILD risk; SHR-4849's payload is a TOP1 inhibitor of similar mechanism)
- Cycle-1 monitoring requirements unknown until phase 1 data publishes

User has no toxicity vetoes; cytopenias and ILD signal are not pre-flagged.

#### Counter-productive mechanisms / dissent

**The critic dissents on evidence base** — no published clinical data for SHR-4849 means the row stands on payload-class precedent rather than on the molecule itself. **The conservative dissents on osteosarcoma eligibility uncertainty** — the basket may in practice enroll only SCLC/NEC, with the broader "DLL3-expressing tumors" wording being aspirational. The risktaker and advocate endorse on the basket-trial principle plus the second-mechanism-class advantage. The TAHOE/PBD-payload class shadow (Rova-T failure) does not directly apply to a TOP1-inhibitor payload, but informs the toxicity-budget framing the board uses for any DLL3 ADC in 2026.

#### Practical considerations

- Trial open at NCT07174583 (recruiting). **First action: contact IDEAYA medical affairs to confirm osteosarcoma eligibility on the basket — do not pursue this rank without that confirmation.**
- Concurrent enrollment with NCT06788938 (rank 2) is unlikely to be permitted simultaneously; the user (or treating team) will need to choose.
- Off-guideline; investigational. Not on any NCCN / ESMO recommendation.
- IDE849's parent compound (SHR-4849) was developed by Jiangsu Hengrui in China; IDEAYA holds the US development license.

#### Why this rank

Lower than rank 2 because (a) eligibility for osteosarcoma is unconfirmed and (b) no published clinical data for SHR-4849 yet exists. Higher than not-ranking-it because the basket eligibility is plausible per the trial wording and the payload class has better odds in 2026 than the BiTE class shadow that drove the conservative's earlier veto. A two-pathway DLL3 plan (BiTE + ADC) is preferable to a single-pathway plan if both can be reached.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| SHR-4849 / IDE849 — NCT07174583 IDEAYA pan-tumor DLL3-expressing basket (eligibility for osteosarcoma pending sponsor confirmation) | DLT, ORR primary; no published efficacy data yet | Class effects expected; no published AE table yet | [NCT07174583](https://clinicaltrials.gov/study/NCT07174583) |

---

### Rank 4. IMA203 (PRAME-TCR-T) via NCT03686124 — Immatics ACTengine pan-solid basket

*Conditional on `prame_ihc_hla:positive` (PRAME IHC AND HLA-A*02:01 typing both positive). Foreclosed if either test is negative.*

*Best-evidenced PRAME pathway: 54% ORR (Wermke 2024, n=28) in cross-tumor PRAME+ HLA-A*02:01+ basket including sarcoma cohorts. Mechanism-distinct from DLL3.*

#### Evidence base

NCT03686124 (ACTengine phase 1/2, recruiting) is the pan-solid PRAME+ HLA-A*02:01+ basket from Immatics. Sarcoma cohorts are explicitly named; osteosarcoma fit is mechanism-driven rather than tumor-restricted. The Wermke 2024 publication ([PMID 38821093](https://pubmed.ncbi.nlm.nih.gov/38821093); Lancet Oncol) reports ORR 54% (95% CI 34-73) in 28 evaluable PRAME+ HLA-A*02:01+ patients across multiple solid-tumor types including synovial sarcoma. Median DoR not reached at 9-mo follow-up.

#### Likelihood of desired effect

Strong, conditional on biomarker confirmation. The 54% ORR is the highest published response signal in any PRAME-targeting class. The cross-tumor design — heterogeneous tumor types in a single PRAME+ HLA-A*02:01+ basket — supports the hypothesis that the relevant biomarker is the PRAME peptide on HLA-A*02:01, not the tumor lineage. Osteosarcoma efficacy data within the basket is not yet published, but mechanism-class fit is expected.

#### Toxicity profile

- CRS in ~100% (mostly grade 1-2; grade 3-4 ~10%)
- ICANS-like neurotoxicity ~25% (mostly grade 1-2)
- Lymphodepleting Cy/Flu chemotherapy precedes T-cell infusion (uniform post-Cy/Flu cytopenias)
- One treatment-related death in the published cohort (septic shock post-Cy/Flu)
- Manufacturing turnaround for autologous TCR-T: typically 4-6 weeks between leukapheresis and infusion

User has no toxicity vetoes; CRS, neurotoxicity, and lymphodepletion are not pre-flagged.

#### Counter-productive mechanisms / dissent

**The conservative dissents** on autologous-cell-therapy logistics and the CRS-management infrastructure required for safe TCR-T delivery — the treating institution must have CAR-T-style infusion capability, ICU step-up, and tocilizumab on hand. **Risktaker, advocate, and concensusite endorse** on the basket-trial principle plus the published 54% ORR efficacy signal. The critic does not dissent (no published-evidence objection because the Wermke 2024 paper is RCT-grade phase 1/2 cross-tumor data) but also does not strongly endorse — the pre-medication and infrastructure burden moderates the score.

#### Practical considerations

- Trial open at NCT03686124 (recruiting). Sarcoma-cohort slot availability should be confirmed directly with Immatics.
- Treating institution must have CAR-T / TCR-T infrastructure: leukapheresis, Cy/Flu lymphodepletion capability, CRS monitoring (often inpatient first cycle), tocilizumab access, ICU step-up.
- Off-guideline; investigational. Pan-solid basket eligibility is published and protocolized.
- Manufacturing-failure rate for autologous TCR-T should be discussed with the sponsor — bridging therapy planning may be needed during the 4-6-week manufacturing window.

#### Why this rank

Higher than rank 5 because of published clinical efficacy (rank 5 has none) and the explicit pan-solid sarcoma-inclusive basket. Lower than ranks 2-3 only if the user's preference weighs CRS infrastructure / lymphodepletion / autologous manufacturing logistics heavily — otherwise rank 4 is the strongest evidence-anchored ranked option in the dossier.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| IMA203 — NCT03686124 ACTengine pan-solid PRAME+ HLA-A*02:01+ basket (sarcoma cohorts on protocol) | ORR 54% (Wermke 2024); mDoR not reached at 9 mo | CRS ~100% (G3-4 ~10%); ICANS ~25%; uniform post-Cy/Flu cytopenia; 1 TRAE death | [NCT03686124](https://clinicaltrials.gov/study/NCT03686124), [PMID 38821093](https://pubmed.ncbi.nlm.nih.gov/38821093) |

---

### Rank 5. IMC-P115C via NCT07156136 — Immunocore next-gen PRAME ImmTAC pan-tumor

*Conditional on `prame_ihc_hla:positive` AND sponsor confirms osteosarcoma eligibility. Status: **considered with caveats**. Two dissents (critic, conservative).*

*Mechanism-class alternative to IMA203 within the PRAME pathway. ImmTAC platform is class-validated via tebentafusp + brenetafusp; IMC-P115C is the next-generation PRAME ImmTAC.*

#### Evidence base

NCT07156136 is Immunocore's first-in-human dose-escalation phase 1 for IMC-P115C, a next-generation PRAME × CD3 ImmTAC bispecific. No published clinical data for IMC-P115C yet; the rank stands on (a) class validation via tebentafusp ([Kimmtrak](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-tebentafusp-tebn-uveal-melanoma), gp100 ImmTAC approved in uveal melanoma 2022) and (b) brenetafusp class precedent in heavily pretreated PRAME+ HLA-A*02:01+ melanoma (Hamid 2024, [PMID 39007852](https://pubmed.ncbi.nlm.nih.gov/39007852); ORR ~9%, durable in subset).

#### Likelihood of desired effect

Speculative for IMC-P115C specifically. Class validation suggests the ImmTAC platform produces durable but lower-frequency responses than TCR-T (consistent with the brenetafusp 9% ORR vs IMA203 54% ORR comparison). Pan-tumor PRAME+ HLA-A*02:01+ eligibility is plausible for sarcoma but not stated outright in published eligibility — sponsor confirmation is the load-bearing screening step.

#### Toxicity profile

- ImmTAC class effects expected: CRS ~85% (mostly grade 1-2 in brenetafusp); rash ~70%; transient hypotension
- Pre-medication with dexamethasone manages CRS in the ImmTAC class
- Weekly IV infusion — outpatient cycle-1 monitoring after step-up dosing

#### Counter-productive mechanisms / dissent

**The critic dissents** on no-published-clinical-data for IMC-P115C specifically. **The conservative dissents** on osteosarcoma eligibility uncertainty (the trial wording is "PRAME-positive HLA-A*02:01-positive advanced cancer" but the per-protocol cohort list may be melanoma-weighted). **Risktaker and advocate endorse** on the basket-trial principle and the second-mechanism-class hedge — having both an ImmTAC option and a TCR-T option in the PRAME pathway is preferable to a single-mechanism plan if both can be reached.

#### Practical considerations

- Trial open at [NCT07156136](https://clinicaltrials.gov/study/NCT07156136) (recruiting). **First action: contact Immunocore medical affairs (see [access guide](accessibility.md) entry #5 for direct phone and email) to confirm whether osteosarcoma is in scope for the basket and what the per-protocol PRAME IHC threshold is.**
- Concurrent enrollment with rank 4 (IMA203) is unlikely to be permitted; if both biomarkers confirm, the user / treating team will need to choose based on infrastructure (ImmTAC weekly outpatient infusion vs TCR-T autologous manufacturing).
- Off-guideline; investigational.

#### Why this rank

Lower than rank 4 because (a) no published clinical data for IMC-P115C and (b) eligibility for osteosarcoma is unconfirmed. Higher than not-ranking-it because the basket eligibility is plausible per the trial wording, the platform is class-validated, and a two-mechanism-class hedge in the PRAME pathway is preferable to a single-mechanism plan.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| IMC-P115C — NCT07156136 PRAME-positive HLA-A*02:01-positive advanced cancer (pan-tumor; sarcoma fit pending sponsor confirmation) | DLT, MTD primary; no published efficacy data yet | ImmTAC class: CRS ~85% (mostly G1-2); rash; transient hypotension | [NCT07156136](https://clinicaltrials.gov/study/NCT07156136), [PMID 39007852](https://pubmed.ncbi.nlm.nih.gov/39007852) |

## Classes examined but not ranked

- **DLL3-directed ADCs (rovalpituzumab tesirine / Rova-T):** mechanistically a DLL3-targeting modality, but not procurable. AbbVie withdrew Rova-T after the TAHOE phase-3 SCLC trial showed worse OS than topotecan ([PMID 33002438](https://pubmed.ncbi.nlm.nih.gov/33002438)). Listed for mechanism context. Not actionable.
- **Other DLL3-targeting investigational drugs (SCLC/NEC-only enrollment):** obrixtamig, gocatamig, alveltamig, clesitamig, peluntamig, QLS31904, zocilurtatug pelitecan, IBI3009, FZ-AD005, ²²⁵Ac-ABD147, ¹⁷⁷Lu-DTPA-SC16.56, ²²⁵Ac-ETN029, LB2102, AMG 119, DLL3-CAR-NK. All are tagged `cross_tumor_extrapolation` on `trials.md` — patient is not enrollable per published eligibility. Visible in the dossier as evidence-base context for the BiTE / ADC / radioligand / cell-therapy DLL3 classes; not actionable for this case absent a basket trial that explicitly accepts the patient's tumor type.

## Ranked prioritization

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Intervention</th><th>Likelihood of effect</th><th>Toxicity burden</th><th>Counter-productive MoA</th><th>Overall</th></tr></thead>
      <tbody>
        <tr>
          <td>1</td>
          <td><strong>Dual-biomarker workup — DLL3 IHC (SP347) + PRAME IHC + HLA-A*02:01 typing</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Diagnostic certainty — resolves which of two pathways is reachable. DLL3 IHC gates ranks 2-3; PRAME IHC + HLA-A*02:01 gate ranks 4-5. Tests are independent and run in parallel.</td>
          <td>Low (none — diagnostic IHC on archival tissue + a single blood draw for HLA typing)</td>
          <td><strong>N/A</strong> <span class="cpm-desc">(diagnostic, not therapeutic)</span></td>
          <td><strong>Non-toxic dual workup that gates ranks 2-5; run all three tests in parallel regardless of which therapy is ultimately chosen.</strong></td>
        </tr>
        <tr>
          <td>2</td>
          <td><strong>tarlatamab via NCT06788938 (UCCC-01 basket)</strong> <span class="scenario-conditional">(conditional on dll3_ihc positive)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>dissent:</em> <span class="persona persona-critic">critic</span></small></td>
          <td>Cross-tumor extrapolation: SCLC OS HR 0.60 (DeLLphi-304); ORR ~40% (DeLLphi-301). Osteosarcoma efficacy is the open question NCT06788938 will answer.</td>
          <td>Moderate (CRS ~50% mostly G1-2; CRS G≥3 ~1%; ICANS-like ~10%; inpatient cycle-1 step-up dosing required)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(On-mechanism CNS bystander T-cell activation drives ICANS; possible DLL3 antigen-loss escape on repeated dosing)</span></td>
          <td><strong>The only DLL3-directed option when IHC is positive — preference-aligned but cross-tumor translation untested; foreclosed if IHC negative.</strong></td>
        </tr>
        <tr>
          <td>3</td>
          <td><strong class="split-glyph">SHR-4849 / IDE849 via NCT07174583 (IDEAYA pan-tumor DLL3 basket)</strong> <span class="scenario-conditional">(conditional on dll3_ihc positive + sponsor confirms osteosarcoma)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-conservative">conservative</span></small></td>
          <td>Speculative. No published clinical data for SHR-4849. TOP1-inhibitor-payload ADC precedent (T-DXd, sacituzumab) suggests the class can produce signals; DLL3-specific efficacy is the open question.</td>
          <td>Unknown — no published clinical data. Class effects expected: cytopenias, GI, possible ILD/pneumonitis (DXd-class ADC signal).</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(ADC bystander toxicity to DLL3-low tissue; antigen-loss escape on repeated dosing; PBD-class TAHOE shadow does not directly apply but informs framing)</span></td>
          <td><strong>Mechanism-distinct second DLL3 pathway pending sponsor confirmation of osteosarcoma eligibility — relevant if the tarlatamab path is foreclosed or fails.</strong></td>
        </tr>
        <tr>
          <td>4</td>
          <td><strong>IMA203 (PRAME-TCR-T) via NCT03686124 (Immatics ACTengine pan-solid basket)</strong> <span class="scenario-conditional">(conditional on prame_ihc_hla positive)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span></small></td>
          <td>Strong. ORR 54% (95% CI 34-73) in pan-solid PRAME+ HLA-A*02:01+ basket (Wermke 2024 Lancet Oncol, n=28). Sarcoma cohorts on protocol; mechanism-driven eligibility.</td>
          <td>High (CRS ~100% — G3-4 ~10%; ICANS-like ~25%; uniform post-Cy/Flu cytopenias; one treatment-related death in published cohort; CAR-T-style infusion infrastructure required)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(On-target / off-tumor toxicity to PRAME-expressing testis is class-managed; CRS / neurotoxicity from T-cell activation is the main mechanism-level risk)</span></td>
          <td><strong>Best-evidenced PRAME pathway with pan-solid sarcoma-inclusive basket; conditional on PRAME IHC + HLA-A*02:01 typing both confirming.</strong></td>
        </tr>
        <tr>
          <td>5</td>
          <td><strong class="split-glyph">IMC-P115C via NCT07156136 (Immunocore next-gen PRAME ImmTAC pan-tumor)</strong> <span class="scenario-conditional">(conditional on prame_ihc_hla positive + sponsor confirms osteosarcoma)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-conservative">conservative</span></small></td>
          <td>Speculative. No published clinical data for IMC-P115C; relies on brenetafusp class precedent (ORR ~9% in heavily pretreated melanoma; durable in subset).</td>
          <td>Moderate (ImmTAC class: CRS ~85% mostly G1-2; rash ~70%; transient hypotension; pre-medication-managed)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(ImmTAC on-target / off-tumor signal in PRAME-expressing normal tissue (low; testis-restricted); CRS from T-cell activation)</span></td>
          <td><strong>Mechanism-class alternative to IMA203 in the PRAME space, contingent on PRAME + HLA confirmation and sponsor confirmation osteosarcoma is in scope.</strong></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

!!! note "Reading the columns"
    **Toxicity burden** is patient-level G3+ AE severity (Low / Moderate / High) summarized from the trial publications. **Counter-productive MoA** is the mechanism-level risk that the intervention's own pathway could blunt the therapeutic goal — distinct from patient AEs. The board's endorse / dissent / veto state appears as pills under each intervention; full per-persona rationale lives on the [board page](board.md).

## Caveats

- The evidence base for the conditional trial is small. NCT06788938 plans n=29 with no published efficacy data yet. The mechanistic basis is the cross-tumor SCLC evidence (DeLLphi-301 / 304), which is robust in SCLC but unproven in any other tumor type.
- Biomarker dependency: rank 2's eligibility assumes a binary IHC result. Indeterminate or weak-positive (1–24%) edge cases are not explicitly addressed; in practice, NCT06788938's stage-2 ≥1% threshold may permit enrollment.
- What would change the ranking:
    - A positive DLL3 IHC plus a head-to-head osteosarcoma cohort within the basket trial reading out would move tarlatamab from "mechanism unproven cross-tumor" to "evidence-supported" and tighten its rank-2 confidence.
    - A user toxicity veto on CRS or inpatient cycle-1 monitoring would foreclose tarlatamab even with positive IHC.
    - Slot unavailability at NCT06788938 sites would close the within-scope therapeutic pathway. The patient's residual options would then be the treating team's standard-of-care conversation, which lies outside Libby's targetable-feature scope and is not enumerated here.

## Sources

**PubMed (PMID):**

- [37861218](https://pubmed.ncbi.nlm.nih.gov/37861218) — Ahn et al., DeLLphi-301, *NEJM* 2023
- [40454646](https://pubmed.ncbi.nlm.nih.gov/40454646) — Mountzios et al., DeLLphi-304, *NEJM* 2025
- [35983951](https://pubmed.ncbi.nlm.nih.gov/35983951) — DLL3 IHC reference (cited in workup row)

**ClinicalTrials.gov (NCT):**

- [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) — DLL3-IHC-selected basket including osteosarcoma (tarlatamab)
- [NCT05060016](https://clinicaltrials.gov/study/NCT05060016) — DeLLphi-301 (cross-tumor mechanism)
- [NCT05740566](https://clinicaltrials.gov/study/NCT05740566) — DeLLphi-304 (cross-tumor confirmatory)

## Transparency artifacts

- [Trial table](trials.md) — 3 rows, all 25 columns
- [Evidence list](evidence.md) — 3 clinical-evidence rows + 4 preclinical rows
- [Tumor-board transcript](board.md) — 5 positions, 20 cross-critiques (filtered to in-scope drugs at render time)
- [Recommendations table](recommendations.md) — full ranked detail with biomarker-conditional flag
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Authored May 2026. Inputs: targetable feature ("DLL3 RNA expression"), clinical descriptor ("metastatic osteosarcoma"), preference summary ("accepts high-risk high-reward options"). Re-rendered when Libby's case scope tightened to drugs that act on the user's stated targetable feature; out-of-scope drugs (standard care for the indication that does not act on DLL3) no longer enter the dossier or appear on any case surface. The cross-cutting caveat carries the negative-result foreclosure mapping. The standard-of-care conversation for the indication is the treating team's, not Libby's. Humanizer pass applied May 2026.

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
