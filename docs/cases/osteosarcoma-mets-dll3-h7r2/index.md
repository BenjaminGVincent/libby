<meta name="robots" content="noindex">

# `osteosarcoma-mets-dll3-h7r2`

<!-- libby:case-output:begin -->

## Case output

- [Target validation paths (PDF)](osteosarcoma-mets-dll3-h7r2-target-validation.pdf?v=d1506bbb) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table (HTML)](osteosarcoma-mets-dll3-h7r2-recommendations.html?v=9fef7fe9) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide (HTML)](accessibility.md?v=42cdc41d) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, sortable in-browser
- [Access guide (offline HTML)](osteosarcoma-mets-dll3-h7r2-accessibility.html?v=d0bcf270) — same access-guide content as the in-browser page, packaged as a self-contained HTML that opens offline
- [Master manuscripts table (HTML)](manuscripts.md?v=00f2085a) — every paper considered — n, effect, variance, toxicities, sortable in-browser
- [Master manuscripts table (offline HTML)](osteosarcoma-mets-dll3-h7r2-manuscripts.html?v=cf6908cb) — same manuscripts inventory as the in-browser page, packaged as a self-contained HTML that opens offline
- [Patient/caregiver PDF](osteosarcoma-mets-dll3-h7r2-plain-language.pdf?v=54c73344) — plain-language summary

<!-- libby:case-output:end -->
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

The case has two RNA-only targetable features, each with its own protein-level confirmation step. **DLL3 IHC (clone SP347)** gates the DLL3-directed pathway: tarlatamab via NCT06788938, and the tarlatamab-plus-radiation combination via NCT06814496. **PRAME IHC plus HLA-A*02:01 typing** together gate the PRAME-directed pathway: IMA203 via NCT03686124 (Immatics ACTengine), plus the PRAME ImmTAC class, brenetafusp via NCT04262466 and its successor IMC-P115C via NCT07156136. The two pathways are independent. The patient may have neither, either, or both. All three workup tests can run in parallel on archival tissue and a single blood draw. If both workups return negative, this report has no within-scope recommendations, and the next conversation about standard 2L+ care is the treating team's, not Libby's.

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

The dossier surfaces 41 trials on the DLL3 and PRAME axes, 7 clinical-evidence rows (6 included, 1 excluded for sponsor discontinuation), and 6 preclinical rows. Seven rows are ranked: a shared biomarker-workup gate at rank 1, then six antigen-directed therapeutics — three on the DLL3 axis (tarlatamab; tarlatamab + RT) and four on the PRAME axis (IMA203; brenetafusp; IMC-P115C; NW-101C). Agreement scores span 1.0 down to −0.2. All five personas placed their entire ranking behind the workup and none issued a veto. The board split on which drug leads: the critic and conservative rank tarlatamab first on RCT-tier evidence and managed safety, while the risktaker and advocate lead IMA203 on the 0.85 efficacy weight — a genuine efficacy-versus-safety disagreement, not a consensus. The case scopes to the DLL3/PRAME features the user nominated; the guideline TKIs regorafenib and cabozantinib sit off that axis and are named as scope in the caveat below, not ranked.

## Cross-cutting caveat (read first)

**Both nominated features are RNA-only, and RNA is not a target.** DLL3 RNA does not put DLL3 protein on the cell membrane where a BiTE can engage it; PRAME RNA does not establish that the PRAME peptide is presented on HLA-A*02:01 at a density a TCR or ImmTAC can see. The decision resolution is protein-level: DLL3 IHC SP347 at ≥1% (≥25% preferred for stage-1 entry) for the BiTE class, and PRAME IHC plus HLA-A*02:01 typing for the entire PRAME class. Until those return, the ranking below is provisional — which is why the workup is rank 1 and every therapeutic rec is tagged conditional.

- **The ranking is scoped to the nominated antigen axis.** Only the workup and the DLL3/PRAME-directed therapeutics appear. The DLL3 IHC gate opens the tarlatamab options; PRAME IHC plus HLA-A*02:01 together open the PRAME class. The two axes are independent — the patient may have neither, either, or both.
- **Standard care is outside this ranking, on purpose.** NCCN Bone Cancer v2.2025 lists regorafenib as category 1 for relapsed osteosarcoma (SARC024, REGOBONE) and cabozantinib as a listed option (CABONE). Neither acts on DLL3 or PRAME, so neither is a Libby recommendation here — Libby scoped to the features the user supplied, not to the full 2L+ guideline. The concensusite ranked both and the board flagged the tension explicitly; they are named here as the guideline-endorsed path the treating team owns, not because Libby ignored them.
- **If DLL3 is negative, this case has no within-scope DLL3 recommendation; if PRAME IHC or HLA-A*02:01 is negative, no within-scope PRAME recommendation. If all three are negative, this case has no within-scope recommendations; standard-of-care for relapsed osteosarcoma lies outside Libby's targetable-feature ranking and should be pursued through the treating team's normal care channel.**
- **Workup logistics.** All three tests are non-toxic and batch on archival FFPE plus one blood tube for HLA typing, one to three weeks turnaround, trivial cost against a treatment cycle. Run them in parallel on day one rather than sequencing. Confirm the SP347 clone is stocked at the treating institution — not every reference lab carries it. HLA-A*02:01 is genetic and lifetime-stable, so a single typing is sufficient; its ~40–50% population prevalence means roughly half of patients are foreclosed from the whole PRAME class regardless of PRAME status.

## Intervention grouping

- **DLL3 × CD3 BiTEs (biomarker-conditional, actionable via [NCT06788938](https://clinicaltrials.gov/study/NCT06788938)):** tarlatamab, alone and combined with radiation ([NCT06814496](https://clinicaltrials.gov/study/NCT06814496)). Anchor evidence: DeLLphi-301 ([PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218)) and the confirmatory DeLLphi-304 phase 3 ([PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646)) — both SCLC.
- **PRAME TCR-T (biomarker-conditional, actionable via [NCT03686124](https://clinicaltrials.gov/study/NCT03686124), sarcoma cohort named):** IMA203, plus the registry-only successor NW-101C ([NCT07266298](https://clinicaltrials.gov/study/NCT07266298)). Anchor: Wermke et al., *Nat Med* 2025 ([PMID 40205198](https://pubmed.ncbi.nlm.nih.gov/40205198); ORR 54% in a PRAME+ HLA-A*02:01+ pan-solid basket).
- **PRAME × CD3 ImmTAC bispecifics (biomarker-conditional):** brenetafusp / IMC-F106C ([NCT04262466](https://clinicaltrials.gov/study/NCT04262466), sarcoma cohort active-not-recruiting) and its next-generation successor IMC-P115C ([NCT07156136](https://clinicaltrials.gov/study/NCT07156136), recruiting). Class-validated by tebentafusp. Anchor: brenetafusp ASCO 2024 abstract 9507 ([DOI 10.1200/JCO.2024.42.16_suppl.9507](https://doi.org/10.1200/JCO.2024.42.16_suppl.9507)).
- **Guideline TKIs for relapsed osteosarcoma (off the nominated axis — scope context, not ranked):** regorafenib (NCCN category 1) and cabozantinib. Named in the cross-cutting caveat as the treating team's standard path; neither targets DLL3 or PRAME.

## Top interventions

### Rank 1. DLL3 IHC (SP347) + PRAME IHC + HLA-A*02:01 typing — diagnostic gate

*Resolves which antigen axes are open. Batch all three tests day one; the RNA signal opens no trial on its own.*

#### Evidence base

Two RNA-only features, two protein-level gates. DLL3 IHC (SP347) at ≥1%, with ≥25% preferred for stage-1 entry, gates the tarlatamab options; [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) enforces that threshold, and every approved DLL3-directed therapy gates on protein, not transcript ([PMID 35983951](https://pubmed.ncbi.nlm.nih.gov/35983951)). PRAME IHC plus HLA-A*02:01 typing together gate the entire PRAME class ([NCT03686124](https://clinicaltrials.gov/study/NCT03686124)): the PRAME peptide is presented on HLA-A*02:01, so a patient without the allele cannot present the target no matter how strongly PRAME stains. PRAME IHC runs positive in roughly half of osteosarcoma; HLA-A*02:01 sits at ~40–50% population prevalence.

#### Likelihood of desired effect

Not a therapy — a gate. It determines whether any downstream antigen-directed rec applies at all. The PRAME axis is more likely than not to survive the IHC given the ~56% osteosarcoma positivity, but HLA-A*02:01 is a coin-flip, and DLL3 protein status in bone is genuinely unknown because RNA says nothing about membrane localization. A negative result on either axis forecloses that half of the ranking outright.

#### Toxicity profile

- None. IHC on archival FFPE plus one blood tube for HLA typing.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. The workup is non-toxic and gates everything, so no persona dissented or vetoed. The one preference genuinely in tension — flagged by the advocate — is the one-to-three-week delay before any antigen-directed therapy can start; the board judged it clearly worth paying, because skipping the workup forecloses the entire preferred option set.

#### Practical considerations

Batch all three on day one rather than sequencing. DLL3 IHC and PRAME IHC run on the same archival block; HLA-A*02:01 needs one EDTA tube and is genetic, so a single lifetime test suffices. Confirm the SP347 clone is stocked at the treating institution — the Roche Tissue Diagnostics clone used in the tarlatamab program is not universally carried. The risktaker would run the HLA typing first-in-line to fail fast on the PRAME half if resources force a sequence.

#### Why this rank

The board placed its whole ranking behind this step. It is a gate, not a therapy, and skipping it would put the drug before the biomarker that qualifies it.

#### Per-trial detail

| Test / trial | Efficacy context | Toxicity | Reference |
|---|---|---|---|
| DLL3 IHC SP347 (assay) | Gates enrollment in the DLL3-directed BiTE trials | None — diagnostic | [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) |
| PRAME IHC + HLA-A*02:01 typing (assay pair) | Gates enrollment in the PRAME ImmTAC and TCR-T trials | None — diagnostic | [NCT03686124](https://clinicaltrials.gov/study/NCT03686124) |

---

### Rank 2. Tarlatamab (DLL3 × CD3 BiTE) via NCT06788938

*Conditional on `dll3_ihc:positive`. Foreclosed if the IHC is negative.*

#### Evidence base

The mechanistic case rests entirely on SCLC. DeLLphi-304 is a randomized phase 3 with a pre-specified OS primary that hit: HR 0.60 (95% CI 0.47–0.77), median OS 13.6 vs 8.3 months, RoB2 Low ([PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646)), pointed the same direction by the DeLLphi-301 phase-2 ORR of 40% (95% CI 29–52) ([PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218)). [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) is a single-arm phase-2 basket that accepts non-SCLC tumors clearing the DLL3 IHC gate. No published osteosarcoma efficacy — or even osteosarcoma DLL3-protein — data exist with this drug; the IHC gate carries the whole extrapolation.

#### Likelihood of desired effect

Moderate, assuming the IHC confirms. This is the best-validated mechanism on the board, but "best-validated" describes SCLC, not bone. Whether the SCLC OS curve transfers to osteosarcoma is the open question the basket exists to answer, and DLL3 in osteosarcoma may sit intracellularly or below the membrane density a BiTE needs to kill — RNA elevation gives no read on that. **A negative IHC forecloses this rec entirely.**

#### Toxicity profile

- CRS any-grade ~56%, grade ≥3 ~1% (DeLLphi-304); inpatient cycle-1 step-up dosing required
- ICANS-like neurologic events ~10–12%
- Grade ≥3 treatment-related AEs 24%, against 53% on the chemo comparator arm
- Step-up dosing: 1 mg D1, 10 mg D8/D15, then 10 mg q2w

The user set no toxicity vetoes, so the CRS/ICANS burden violates no stated constraint. The offsetting point is that this toxicity has a written management algorithm — step-up dosing, inpatient cycle-1 monitoring, tocilizumab — which is exactly what the conservative wanted before treating a young patient.

#### Counter-productive mechanisms / dissent

No persona dissented on the drug, but the board split on where it ranks. The critic and conservative put it first among the enrollable options precisely because it is the only RCT-grade mechanism in the set and its safety is characterized. The risktaker pushed back on that ordering — ranking tarlatamab over IMA203 rewards RCT tier while ignoring that every tarlatamab efficacy row is SCLC and IMA203's higher-ceiling number comes from a basket that names a sarcoma cohort. That is a ranking argument, not a dissent on tarlatamab, which stayed on all five lists. The mechanism-level risk is on-target CNS/neuro bystander activation and antigen-density-dependent escape if DLL3 expression is low or heterogeneous.

#### Practical considerations

- Trial recruiting; confirm osteosarcoma is on the NCT06788938 per-protocol enrolling list before counting on the slot.
- Inpatient cycle-1 monitoring for CRS step-up is required — deliverable but not trivial at every center.
- No consensus category in bone sarcoma; endorsed only under the NCCN Bone Cancer v2.2025 clinical-trial pathway, not as a listed regimen.
- Off-the-shelf, no manufacturing wait — the practical contrast with the TCR-T route below.

#### Why this rank

It ties IMA203 nowhere and beats it on agreement: five personas back tarlatamab, none dissent on the drug, and its toxicity is managed. IMA203 outscores it on raw ORR but carries three dissents and a fatality, which is why the RCT-tier BiTE leads the therapeutics and the high-ceiling TCR-T follows.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Tarlatamab — NCT06788938 DLL3-IHC-selected basket (osteosarcoma admissible), n=29 planned | ORR at 18 mo (primary); no osteosarcoma data yet | Per class: CRS ~50%, ICANS ~10%, inpatient C1 | [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) |
| Tarlatamab — DeLLphi-301 SCLC (cross-tumor mechanism), n=220 | ORR 40% (95% CI 29–52); mPFS 4.9 mo | CRS ~51% (G3+ ~1%); ICANS ~10%; G3+ TRAEs 30% | [PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218) |
| Tarlatamab — DeLLphi-304 SCLC (cross-tumor confirmatory), n=509 | OS HR 0.60 (95% CI 0.47–0.77), p<0.001; median OS 13.6 vs 8.3 mo | G3+ TRAEs 24% vs 53% chemo | [PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646) |

---

### Rank 3. IMA203 (PRAME TCR-T) via NCT03686124 — ACTengine pan-solid basket

*Conditional on `prame_hla:positive` (PRAME IHC AND HLA-A*02:01 both positive). Foreclosed if either is negative.*

#### Evidence base

This is the pick that lands squarely on the PRAME axis with the biggest number in the dossier. The Wermke phase-1 trial reports ORR 54% (95% CI 34–73) in 28 evaluable PRAME+ HLA-A*02:01+ patients across solid-tumor types, median duration of response not reached at 9 months, mPFS 5.1 months ([PMID 40205198](https://pubmed.ncbi.nlm.nih.gov/40205198), *Nat Med* 2025). [NCT03686124](https://clinicaltrials.gov/study/NCT03686124) names a sarcoma cohort outright, so an osteosarcoma patient is admissible in principle rather than by cross-tumor argument. The honest limit: n=28, single-arm, no comparator, and the responders skewed melanoma — no osteosarcoma-specific response is reported.

#### Likelihood of desired effect

A high ceiling if both biomarkers confirm, but from an unstable base. A 95% CI of 34–73 on 28 patients is a signal, not a rate you can quote to a patient, and no osteosarcoma patient contributed to it. The sarcoma-cohort activity so far leans on synovial histology, so osteosarcoma-specific benefit stays a hypothesis. Durability could also be blunted by tumor HLA-LOH, B2M loss, or a CD8-cold microenvironment even with PRAME and HLA both positive. A negative PRAME IHC or absent HLA-A*02:01 forecloses this rec entirely.

#### Toxicity profile

- **One treatment-related death from septic shock (1/28, 4%)** — the single data point most responsible for its dissents
- CRS ~100% (grade ≥3 ~11%), ICANS-like neurotoxicity ~25%
- Universal grade ≥3 cytopenias after Cy/Flu lymphodepletion — a real immunosuppression window in a metastatic patient
- Autologous manufacturing: leukapheresis, a ~4–6-week vein-to-vein window, and CAR-T-style infusion infrastructure

No toxicity veto is on file, so this profile violates no stated constraint — but it is the heaviest tail in the dossier, and a death in a 28-person series is not a footnote to rank past.

#### Counter-productive mechanisms / dissent

The efficacy-first personas lead it and three others dissent on ranking it high — honestly, on different grounds. The risktaker and advocate read the patient's 0.85 efficacy weight and explicit high-risk appetite as pointing here: the biggest response number on the nominated antigen with a named sarcoma cohort. The conservative and critic dissent on the safety tail — the septic death, uniform CRS, ~25% ICANS, universal post-lymphodepletion cytopenias — with the critic adding the imprecision of a wide CI on 28 patients. The concensusite dissents on guideline fit: no consensus category, trial-enrollment pathway only. The mechanism-level risk is antigen-loss / HLA-LOH escape plus the lymphodepletion immunosuppression window.

#### Practical considerations

- Trial recruiting; confirm the sarcoma-cohort slot directly with Immatics.
- The treating institution needs full cell-therapy infrastructure — leukapheresis, Cy/Flu, inpatient CRS monitoring, tocilizumab, ICU step-up — and bridging-therapy planning for the manufacturing window.
- No consensus category; guideline-consonant only under the NCCN clinical-trial recommendation.
- The workup at rank 1 should include the CD8-TIL and HLA-LOH/B2M reads to frame durability before infusion.

#### Why this rank

Ranked below tarlatamab because the underlying evidence is single-arm phase 1/2 against a randomized OS readout, and because three personas dissented on ranking it higher — the mechanical agreement score lands at −0.2. Ranked above the ImmTAC and the registry-only options because it carries the strongest efficacy signal on the patient's own antigen and the only explicitly named sarcoma cohort; the efficacy-first case for placing it first is real and is preserved here, not buried.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| IMA203 — NCT03686124 ACTengine pan-solid PRAME+ HLA-A*02:01+ basket (sarcoma cohort named) | ORR 54% (95% CI 34–73); mDoR not reached at 9 mo; mPFS 5.1 mo | CRS ~100% (G3+ ~11%); ICANS ~25%; universal post-Cy/Flu cytopenia; 1 TRAE death | [NCT03686124](https://clinicaltrials.gov/study/NCT03686124), [PMID 40205198](https://pubmed.ncbi.nlm.nih.gov/40205198) |

---

### Rank 4. Brenetafusp (IMC-F106C, PRAME × CD3 ImmTAC) via NCT04262466 / successor IMC-P115C

*Conditional on `prame_hla:positive`. Foreclosed if PRAME IHC or HLA-A*02:01 is negative.*

#### Evidence base

The evidence is cross-tumor melanoma and modest. The ASCO 2024 readout shows ORR 9–11% (4 partial responses of 36 at active doses), with the durable benefit concentrated in the PRAME-positive subset: mPFS 4.5 vs 2.1 months and 6-month OS 94% vs 40% ([DOI 10.1200/JCO.2024.42.16_suppl.9507](https://doi.org/10.1200/JCO.2024.42.16_suppl.9507)). The osteosarcoma-accepting basket cohort ([NCT04262466](https://clinicaltrials.gov/study/NCT04262466)) is active-not-recruiting, and the NCI's dedicated sarcoma trial ([NCT07686367](https://clinicaltrials.gov/study/NCT07686367)) enrolls synovial and myxoid/round-cell liposarcoma, not bone. The subset OS separation is an unadjusted post-hoc split on an open-label phase-1 abstract — hypothesis-generating, not a survival claim to carry across drugs and tumor types.

#### Likelihood of desired effect

Low-to-moderate, and honestly stated. The 9–11% overall ORR is a genuine but thin single-agent signal; the meaningful benefit lives in a PRAME-positive responder subset that may or may not include bone. It sits below IMA203 on efficacy by a wide margin — the conservative ranks it above IMA203 anyway, trading response rate for tolerability, not efficacy.

#### Toxicity profile

- CRS ~85% any-grade but predominantly grade 1–2; no grade ≥3 CRS reported in the melanoma cohort
- Rash ~70% (on-target/off-tumor ImmTAC signal), transient hypotension ~35%
- Grade ≥3 TRAEs ~30%; managed with dexamethasone pre-medication
- Off-the-shelf, no lymphodepletion, no marrow wipeout — the safety-for-access trade that earns it this rank

#### Counter-productive mechanisms / dissent

No dissent — the pushback here is enrollability, not mechanism. The conservative ranks it the best-tolerated agent in the PRAME class and places it above IMA203 on that basis; the risktaker and critic keep it on the list as a defensible pathway. The critic's qualifier is specific: the 6-month OS separation is an unadjusted subgroup split on an open-label phase-1 abstract, and should not be deployed as a survival claim. The on-mechanism risk is limited to on-target/off-tumor rash and antigen-density dependence, with no plausible counter-productive vector against the therapeutic goal.

#### Practical considerations

- The osteosarcoma-relevant slot is not open today: the basket sarcoma cohort is active-not-recruiting and the NCI trial excludes bone.
- Enrollability hinges on the cohort re-opening or the IMC-P115C successor (rank 5) accepting osteosarcoma.
- Weekly IV infusion, outpatient after step-up — a lower-burden route onto the PRAME axis than TCR-T.
- No consensus category; trial-enrollment pathway only.

#### Why this rank

It draws no dissent, which lifts it above IMA203 on agreement score despite far weaker numbers. It sits below tarlatamab because the ImmTAC efficacy is thin and cross-tumor while tarlatamab carries RCT-grade mechanism evidence. And it edges out the tarlatamab+RT combination at the same score because it has real phase-1 efficacy data where the combination has none.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Brenetafusp — NCT04262466 melanoma cohort (cross-tumor; sarcoma slot active-not-recruiting) | ORR 9–11%; PRAME+ subset mPFS 4.5 vs 2.1 mo; 6-mo OS 94% vs 40% | CRS predominantly G1-2, no G3+ CRS; rash ~70%; G3+ TRAE ~30% | [NCT04262466](https://clinicaltrials.gov/study/NCT04262466), [DOI 10.1200/JCO.2024.42.16_suppl.9507](https://doi.org/10.1200/JCO.2024.42.16_suppl.9507) |
| Brenetafusp — NCT07686367 NCI sarcoma phase 2 (synovial + myxoid/round-cell lipo; osteosarcoma not on list) | ORR endpoint; not-yet-recruiting, no data | Per ImmTAC class | [NCT07686367](https://clinicaltrials.gov/study/NCT07686367) |

---

### Rank 5. IMC-P115C (next-gen PRAME × CD3 ImmTAC) via NCT07156136

*Conditional on `prame_hla:positive` AND sponsor confirms osteosarcoma is on the per-protocol list. Foreclosed if PRAME IHC or HLA-A*02:01 is negative.*

#### Evidence base

There is no IMC-P115C efficacy readout — it is a recruiting first-in-human dose-escalation ([NCT07156136](https://clinicaltrials.gov/study/NCT07156136)). The rank buys the ImmTAC class and the PRAME target off brenetafusp's data, since IMC-P115C is Immunocore's next-generation successor engineered from it ([DOI 10.1200/JCO.2024.42.16_suppl.9507](https://doi.org/10.1200/JCO.2024.42.16_suppl.9507)). The eligibility is written pan-tumor for PRAME-positive HLA-A*02:01-positive disease, so non-melanoma histologies are admissible in principle once the sponsor confirms sarcoma is on the list.

#### Likelihood of desired effect

Unknown for the molecule itself. The class read suggests the ImmTAC platform produces durable but lower-frequency responses than TCR-T. What earns it a rank over the registry-only options is that it is actually recruiting where brenetafusp's sarcoma slot is closed — for a patient who wants the gentler PRAME route and an open door today, this is the one to call about. A negative PRAME IHC or absent HLA-A*02:01 forecloses it.

#### Toxicity profile

- No drug-specific data yet; class expectation is the brenetafusp profile — CRS predominantly grade 1–2, rash, transient hypotension
- Dexamethasone pre-medication manages CRS in the ImmTAC class
- Weekly IV infusion, outpatient cycle-1 monitoring after step-up

#### Counter-productive mechanisms / dissent

No dissent. The risktaker and advocate rank it as the open-door version of brenetafusp. The critic's qualifier lands here too: the borrowed brenetafusp OS figures are an unadjusted phase-1 melanoma subset and should not be deployed as an IMC-P115C survival expectation. Same on-target/off-tumor and antigen-density dependence as the ImmTAC class; no drug-specific counter-productive signal exists yet.

#### Practical considerations

- Trial recruiting. First action: contact Immunocore medical affairs to confirm sarcoma is on the per-protocol list and what the PRAME IHC threshold is.
- Concurrent enrollment with IMA203 is unlikely to be permitted; if both biomarkers confirm, the choice is ImmTAC weekly outpatient infusion versus TCR-T autologous manufacturing.
- No consensus category; investigational.

#### Why this rank

Below brenetafusp because it is a pure platform-and-target bet with no data of its own, and above the registry-only options because it is genuinely recruiting today. It is the ImmTAC a patient could enter now if brenetafusp's slot stays shut.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| IMC-P115C — NCT07156136 pan-tumor PRAME+ HLA-A*02:01+ (sarcoma fit pending sponsor confirmation) | DLT, MTD primary; no efficacy data yet | ImmTAC class: CRS predominantly G1-2; rash; transient hypotension | [NCT07156136](https://clinicaltrials.gov/study/NCT07156136) |

---

*Ranks 6 (tarlatamab + radiation, `dll3_ihc:positive`) and 7 (NW-101C PRAME TCR-T, `prame_hla:positive`) are carried in `recommendations.jsonl` and the ranked-prioritization table below with `status: considered_with_caveats`. Both are tier-5 registry-only — the critic and conservative declined to rank the tarlatamab+RT combination and the critic dissented on NW-101C — so their narratives are deliberately thin: tarlatamab+RT layers an untested abscopal RT arm on the rank-2 backbone with zero combination data, and NW-101C is a second PRAME TCR-T fallback with no clinical data under its own name, borrowing its entire efficacy expectation from IMA203. Neither carries enough substantiation for a deep narrative; both are named as verify-first fallback slots.*

## Classes examined but not ranked

- **Tarlatamab + radiation (NCT06814496) and NW-101C (NCT07266298):** both feature-targeting but tier-5 registry-only, carried at ranks 6–7 with caveats rather than given deep narratives. Tarlatamab+RT has no published combination AE profile — the conservative and critic decline to rank an uncharacterized RT-on-BiTE combination — and NW-101C has no clinical data under its name, so its efficacy is borrowed from IMA203.
- **Other DLL3- and PRAME-targeting pipeline agents (SCLC/NEC- or melanoma-only enrollment):** the DLL3 BiTE/ADC/radioligand/CAR-T constructs (ZL-1310, ²²⁵Ac agents, LB2102, DLL3-CAR-NK and similar) and the PRAME TCER/mRNA-combination rows carry no osteosarcoma-axis data that beats the basket-eligible picks and, in most cases, no osteosarcoma eligibility. They remain in the dossier as evidence-base context for the mechanism classes; none is enrollable for a bone-sarcoma patient absent a basket that explicitly accepts the histology.

## Ranked prioritization

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Intervention</th><th>Likelihood of effect</th><th>Toxicity burden</th><th>Counter-productive MoA</th><th>Overall</th></tr></thead>
      <tbody>
        <tr>
          <td>1</td>
          <td><strong>DLL3 IHC (SP347) + PRAME IHC + HLA-A*02:01 typing — diagnostic gate</strong> <span class="scenario-conditional">(shared workup)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>N/A — diagnostic gate. Determines whether any downstream antigen-directed rec applies; PRAME axis more likely than not to hold, DLL3 protein status unknown.</td>
          <td>Low (none — diagnostic test on tissue and blood)</td>
          <td><strong>N/A</strong> <span class="cpm-desc">(diagnostic gate, no mechanism of action)</span></td>
          <td><strong>The one move that unlocks the whole antigen list — cheap, archival, non-toxic; a negative result on either axis forecloses that half of the ranking.</strong></td>
        </tr>
        <tr>
          <td>2</td>
          <td><strong>tarlatamab (DLL3 × CD3 BiTE) via NCT06788938</strong> <span class="scenario-conditional">(conditional on dll3_ihc positive)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Moderate if DLL3 IHC confirms — best-validated mechanism (DeLLphi-304 OS HR 0.60) but efficacy is entirely SCLC-derived; no osteosarcoma data.</td>
          <td>Moderate (CRS ~56% mostly G1-2, ICANS-like ~12%, G3+ TRAE 24%)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(On-mechanism CNS/neuro bystander activation and antigen-density-dependent escape if DLL3 membrane expression is low or heterogeneous)</span></td>
          <td><strong>The best-validated mechanism on the board and the lighter-toxicity DLL3 route — but every efficacy row is SCLC; osteosarcoma activity is a hypothesis until the IHC confirms surface target.</strong></td>
        </tr>
        <tr>
          <td>3</td>
          <td><strong>IMA203 (PRAME TCR-T) via NCT03686124</strong> <span class="scenario-conditional">(conditional on prame_hla positive)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small></td>
          <td>High ceiling if both biomarkers confirm (ORR 54%, Nat Med 2025) but from n=28 with a wide CI and no osteosarcoma-specific responder; unstable point estimate.</td>
          <td>High (1 treatment-related septic death; CRS ~100%/G3+ 11%, ICANS ~25%, universal G3+ cytopenias post-Cy/Flu)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(Antigen-loss / HLA-LOH escape and post-lymphodepletion immunosuppression window; durability unproven, responders melanoma-skewed)</span></td>
          <td><strong>The highest-response on-axis option with a named sarcoma cohort, and the one with a fatality on the board — efficacy-first personas lead it, three dissent on the safety tail and n=28 imprecision.</strong></td>
        </tr>
        <tr>
          <td>4</td>
          <td><strong>brenetafusp (IMC-F106C, PRAME × CD3 ImmTAC) via NCT04262466 / successor IMC-P115C</strong> <span class="scenario-conditional">(conditional on prame_hla positive)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span></small></td>
          <td>Low-to-moderate: overall ORR 9-11%, benefit concentrated in a PRAME-positive subset (mPFS 4.5 vs 2.1 mo); melanoma-derived, cross-tumor.</td>
          <td>Low (CRS predominantly G1-2, no G3+ CRS in cohort; rash ~70%, G3+ TRAE ~30%)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(On-target/off-tumor rash and antigen-density dependence; dissent is enrollability-flavored, no mechanism-level counter-productive vector)</span></td>
          <td><strong>The best-tolerated PRAME route with an off-the-shelf, no-lymphodepletion trade — but modest single-agent efficacy and a sarcoma enrollment slot that is currently closed.</strong></td>
        </tr>
        <tr>
          <td>5</td>
          <td><strong>IMC-P115C (next-gen PRAME × CD3 ImmTAC) via NCT07156136</strong> <span class="scenario-conditional">(conditional on prame_hla positive)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Unknown — first-in-human, no efficacy data; class bet on the ImmTAC platform and PRAME target, inferred from brenetafusp.</td>
          <td>Low (no drug-specific data; class expectation predominantly G1-2 CRS and rash)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(Same on-target/off-tumor and antigen-density dependence as the ImmTAC class; no drug-specific counter-productive signal yet)</span></td>
          <td><strong>The recruiting-today PRAME ImmTAC when brenetafusp's sarcoma slot is closed — a platform-and-target bet with no efficacy readout of its own yet.</strong></td>
        </tr>
        <tr>
          <td>6</td>
          <td><strong>tarlatamab + radiation therapy via NCT06814496</strong> <span class="scenario-conditional">(conditional on dll3_ihc positive)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Unknown — no combination data; abscopal benefit over tarlatamab monotherapy is a hypothesis the phase-1 is still measuring.</td>
          <td>Moderate (uncharacterized combination; BiTE CRS ~50% mostly G1-2, ICANS-like ~10%, plus site-specific RT toxicity)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(Uncharacterized RT-on-BiTE synergistic toxicity; potential on-mechanism CNS/neuro bystander activation compounded by radiation)</span></td>
          <td><strong>A parallel DLL3 slot with an abscopal rationale — but zero combination data, and the monotherapy basket delivers the same backbone with a written safety algorithm.</strong></td>
        </tr>
        <tr>
          <td>7</td>
          <td><strong>NW-101C (PRAME TCR-T) via NCT07266298</strong> <span class="scenario-conditional">(conditional on prame_hla positive)</span><br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-critic">critic</span></small></td>
          <td>Unknown — no NW-101C data exist; efficacy inferred entirely from the IMA203 PRAME TCR-T class precedent.</td>
          <td>High (no drug-specific data; class expectation is the IMA203 TCR-T profile — CRS, ICANS, post-lymphodepletion cytopenias)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(Same antigen-loss / HLA-LOH escape and lymphodepletion immunosuppression risk as the PRAME TCR-T class; no drug-specific data)</span></td>
          <td><strong>A redundant PRAME TCR-T fallback if the IMA203 slot is inaccessible — but zero data under this name; the efficacy expectation is entirely borrowed.</strong></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

!!! note "Reading the columns"
    **Toxicity burden** is patient-level G3+ AE severity (Low / Moderate / High) summarized from the trial publications. **Counter-productive MoA** is the mechanism-level risk that the intervention's own pathway could blunt the therapeutic goal — distinct from patient AEs. The board's endorse / dissent / veto state appears as pills under each intervention; full per-persona rationale lives on the [board page](board.md).

## Caveats

- **Evidence base.** The therapeutic ranks rest on thin, mostly cross-tumor data. Tarlatamab's OS signal is a randomized phase 3 but entirely in SCLC. IMA203's 54% ORR is single-arm, n=28, one treatment-related death, with responders skewed to melanoma. Brenetafusp's PRAME-positive subset separation is an unadjusted split on an open-label phase-1 ASCO abstract. IMC-P115C, tarlatamab+RT, and NW-101C have no efficacy readouts of their own. None of these has published osteosarcoma-specific response data.
- **Biomarker dependencies.** The whole ranking assumes protein-level confirmation. Tarlatamab and tarlatamab+RT (ranks 2, 6) assume DLL3 IHC ≥1% (≥25% for stage-1 entry); without it they are foreclosed. IMA203, brenetafusp, IMC-P115C, and NW-101C (ranks 3, 4, 5, 7) assume both PRAME IHC positivity and HLA-A*02:01 typing; either negative forecloses the entire PRAME class. The two axes are independent — a negative DLL3 IHC does not foreclose the PRAME ranks, and vice versa.
- **What would change the ranking.**
    - An independent replication of PRAME TCR-T or DLL3 BiTE activity in a bone-sarcoma cohort — as opposed to the current cross-tumor extrapolation — would tighten the confidence on rank 2 or rank 3.
    - A negative DLL3 IHC moves ranks 2 and 6 to non-applicable; a negative PRAME IHC or absent HLA-A*02:01 moves ranks 3, 4, 5, and 7 to non-applicable.
    - If the user declared a toxicity veto on CRS, ICANS, or lymphodepletion — none is on file — IMA203 and NW-101C would drop sharply, since the septic-death and cytopenia burden is their load-bearing dissent.
- **Re-scoping.** If the user's stated preference shifts away from high-risk/high-reward toward tolerability, or the clinical state changes, the guideline TKIs regorafenib and cabozantinib — named as scope context, not ranked here — become the more relevant conversation with the treating team.

## Sources

**PubMed (PMID):**

- [35983951](https://pubmed.ncbi.nlm.nih.gov/35983951) — Yao et al., DLL3 as an emerging target for neuroendocrine neoplasms, *The Oncologist* 2022 (workup-row target reference)
- [37861218](https://pubmed.ncbi.nlm.nih.gov/37861218) — Ahn et al., DeLLphi-301 tarlatamab SCLC phase 2, *NEJM* 2023
- [40205198](https://pubmed.ncbi.nlm.nih.gov/40205198) — Wermke et al., IMA203 PRAME TCR-T phase 1, *Nat Med* 2025
- [40454646](https://pubmed.ncbi.nlm.nih.gov/40454646) — Mountzios et al., DeLLphi-304 tarlatamab SCLC phase 3, *NEJM* 2025

**DOI (abstract, no PMID):**

- [10.1200/JCO.2024.42.16_suppl.9507](https://doi.org/10.1200/JCO.2024.42.16_suppl.9507) — Hamid et al., brenetafusp (IMC-F106C) PRAME ImmTAC melanoma phase 1, ASCO 2024 abstract 9507

**ClinicalTrials.gov (NCT):**

- [NCT03686124](https://clinicaltrials.gov/study/NCT03686124) — IMA203 ACTengine pan-solid PRAME/HLA-A*02:01 basket (sarcoma cohort named)
- [NCT04262466](https://clinicaltrials.gov/study/NCT04262466) — brenetafusp PRAME ImmTAC basket (sarcoma cohort active-not-recruiting)
- [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) — tarlatamab DLL3-IHC-gated solid-tumor basket
- [NCT06814496](https://clinicaltrials.gov/study/NCT06814496) — tarlatamab + radiation, pan-tumor DLL3-IHC basket
- [NCT07156136](https://clinicaltrials.gov/study/NCT07156136) — IMC-P115C next-gen PRAME ImmTAC pan-tumor
- [NCT07266298](https://clinicaltrials.gov/study/NCT07266298) — NW-101C PRAME TCR-T pan-solid basket

## Transparency artifacts

- [Trial table](trials.md) — full DLL3/PRAME trial inventory, all columns
- [Evidence list](evidence.md) — clinical-evidence + preclinical rows not rising to a ranked rec
- [Master manuscripts table](manuscripts.md) — every paper considered, with n, effect size, variance, and toxicity columns
- [Tumor-board transcript](board.md) — 5 positions, 31 cross-critiques with the full agreement matrix
- [Recommendations table](recommendations.md) — full ranked detail with the biomarker-conditional scenario flags
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Re-run 2026-07-09 for a full board re-deliberation after the trial screen added the DLL3 + PRAME/HLA-A*02:01 pipeline. Inputs: profile (two RNA-only features, DLL3 and PRAME), preferences (efficacy weight 0.85, accepts high-risk/high-reward, prefers trials, no toxicity veto), 5 board positions, 31 critiques, and the refreshed dossier. Synthesis: one shared workup gate plus six antigen-directed therapeutics, no vetoes issued. Ranking follows agreement score, with the efficacy-toxicity tiebreak keeping IMA203 above the tier-5 registry-only options despite its −0.2 score, since all five personas listed it and two led it. Scope: regorafenib and cabozantinib (concensusite ranks 1–2) are off the nominated DLL3/PRAME axis and are named as scope context, not ranked — the board flagged this tension explicitly. Reference check corrected the IMA203 citation from the dossier's PMID 38821093 (which resolves to an unrelated Lancet Oncol letter) to the verified Wermke *Nat Med* 2025 primary publication, PMID 40205198; the dossier's PMID 28315425 for the Iura PRAME-osteosarcoma prevalence figure resolves to an unrelated hepatocellular paper and no single PubMed record cleanly supports the "56%, n=82" claim, so that figure is carried as free text without a promoted identifier and the case should be re-screened to repair the source row. Humanizer pass applied over all prose sections.

<!-- libby:downloads:begin -->

## Downloads

### HTML

- [Target validation paths](target_validation.md?v=98962654) — per-feature biomarker-workup table with providers and references, sortable in-browser
- [Recommendations table](osteosarcoma-mets-dll3-h7r2-recommendations.html?v=9fef7fe9) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide](accessibility.md?v=42cdc41d) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Access guide (offline)](osteosarcoma-mets-dll3-h7r2-accessibility.html?v=d0bcf270) — same access-guide content packaged as a self-contained HTML that opens offline
- [Master manuscripts table](manuscripts.md?v=00f2085a) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Master manuscripts table (offline)](osteosarcoma-mets-dll3-h7r2-manuscripts.html?v=cf6908cb) — same manuscripts inventory packaged as a self-contained HTML that opens offline

### PDF

- [Target validation paths](osteosarcoma-mets-dll3-h7r2-target-validation.pdf?v=d1506bbb) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table](osteosarcoma-mets-dll3-h7r2-recommendations.pdf?v=49aeec93) — ranked options + pipeline context + evidence in detail, in a print-friendly PDF
- [Access guide](osteosarcoma-mets-dll3-h7r2-accessibility.pdf?v=4dc4a899) — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF
- [Master manuscripts table](osteosarcoma-mets-dll3-h7r2-manuscripts.pdf?v=ae2b09e6) — every paper considered — n, effect, variance, toxicities, in a print-friendly PDF
- [Patient/caregiver PDF](osteosarcoma-mets-dll3-h7r2-plain-language.pdf?v=54c73344) — plain-language summary

<!-- libby:downloads:end -->

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
