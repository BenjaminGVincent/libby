<meta name="robots" content="noindex">

# `gist-sdh-multifocal-resected-m1-k4n8`

<!-- libby:case-output:begin -->

## Case output

- [Target validation paths (PDF)](gist-sdh-multifocal-resected-m1-k4n8-target-validation.pdf?v=161ca509) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table (HTML)](gist-sdh-multifocal-resected-m1-k4n8-recommendations.html?v=019e36df) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Preclinical recommendations (HTML)](preclinical_recommendations.md?v=755fab5a) — forward-looking horizon scan of earlier-than-clinical candidate drugs, compounds, and strategies, sortable in-browser
- [Access guide (HTML)](accessibility.md?v=888bc293) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, sortable in-browser
- [Access guide (offline HTML)](gist-sdh-multifocal-resected-m1-k4n8-accessibility.html?v=4790bbb0) — same access-guide content as the in-browser page, packaged as a self-contained HTML that opens offline
- [Master manuscripts table (HTML)](manuscripts.md?v=803f8425) — every paper considered — n, effect, variance, toxicities, sortable in-browser
- [Master manuscripts table (offline HTML)](gist-sdh-multifocal-resected-m1-k4n8-manuscripts.html?v=07f726fd) — same manuscripts inventory as the in-browser page, packaged as a self-contained HTML that opens offline
- [Patient/caregiver PDF](gist-sdh-multifocal-resected-m1-k4n8-plain-language.pdf?v=cdfcacd3) — plain-language summary

<!-- libby:case-output:end -->
## Research question

In multifocal SDH-deficient (KIT/PDGFRA wild-type) gastric GIST status post R0 distal gastrectomy + Roux-en-Y plus complete resection of a single M1 deposit at the ligament of Treitz — currently NED — what is the right adjuvant and surveillance strategy, and what contingency belongs on file for the first measurable recurrence, gated on the SDHA germline + SDHA/SDHB IHC + tissue-NGS bundle that locks in the dSDH-GIST phenotype?

## Patient profile (scrubbed)

- **Primary site / histology:** stomach — gastrointestinal stromal tumor, SDH-deficient subtype (KIT/PDGFRA wild-type)
- **Stage:** ypT3(m)N0M1 — multifocal gastric GIST with a single M1 deposit in the ligament of Treitz; R0 distal gastrectomy + Roux-en-Y; 0/7 nodes; largest mass 7.5 cm; M1 deposit completely resected
- **Performance status:** ECOG 1
- **Age band:** 40-49
- **Sex:** unknown
- **Current state:** NED
- **Biomarkers:**
    - **SDHA L306P** (tumor NGS, VAF 44%) — **ngs_pending** germline-vs-somatic; SDHA full-gene sequencing on blood/saliva pending
    - **SDHA Y408N** (tumor NGS, VAF 41%, somatic) — confirmed
    - **SDHA E350fs** (ctDNA only) — **ngs_pending** tissue confirmation
    - **PIK3CA R93W** (ctDNA only) — **ngs_pending** tissue confirmation; non-canonical ABD-domain variant outside alpelisib companion-diagnostic hotspots
    - **MAP2K1 P124S** (ctDNA only) — **ngs_pending** tissue confirmation; recognized αC-helix activating site
    - **POLE R1679C** (germline) — confirmed; outside canonical proofreading hotspots; most likely VUS at TMB <1 / MSS
    - **SDHB protein** (IHC) — intact; **interpretive caveat** that retained SDHB IHC alongside biallelic SDHA inactivation (~85% combined VAF) is paradoxical and demands a re-cut with positive internal control plus paired SDHA IHC arbitration
    - **CD117 (KIT) protein** (IHC) — positive (supports GIST diagnosis, does NOT imply KIT-mutant GIST given KIT-WT genotype)
    - **DOG1** (IHC) — positive
    - **Desmin** (IHC) — negative
    - **KIT** (tumor NGS) — wild-type
    - **PDGFRA** (tumor NGS) — wild-type
    - **TMB:** <1 mut/Mb — below the 10 mut/Mb tumor-agnostic pembrolizumab threshold
    - **MSI status:** MSS — biomarker-excluded from tumor-agnostic pembrolizumab
    - **NTRK / RET / BRAF:** no actionable alteration
- **Prior therapy:** R0 distal gastrectomy with Roux-en-Y reconstruction; complete resection of multifocal primary + M1 deposit at ligament of Treitz; 0/7 nodes involved. Best response: NE (definitive surgery).
- **Current therapy:** none

## Preferences

- **Efficacy/toxicity weight:** 0.65 (mildly efficacy-leaning) — defaulted, no explicit user input
- **Toxicity vetoes:** none stated — defaulted
- **Modality constraints:** none stated — defaulted
- **Free text:** No explicit user preferences. Defaults assumed: post-R0 resection with no measurable disease at present, so the operative question is adjuvant / surveillance strategy and a contingency plan for first recurrence. Efficacy/toxicity weight set to 0.65 because (a) M1 disease that has been completely resected still carries a high recurrence risk and (b) SDH-deficient GIST is indolent, which raises the bar for committing to chronic-toxicity adjuvant therapy.
- **Trials preferred:** yes — defaulted to true because targeted options (HIF-2α, hypomethylating agents, FGFR inhibitors) sit predominantly in trial territory

<!-- libby:target-validation:begin -->

## Target validation paths

The case hinges on whether the SDH-deficient GIST phenotype actually holds. Biallelic SDHA inactivation at ~85% combined VAF should destabilize the SDH complex and abolish SDHB staining, and SDHB IHC reads as intact. That paradox is the gate. Resolving it via a paired SDHB re-cut with positive internal control, an orthogonal SDHA IHC, and a germline SDHA panel locks in (or refutes) the driver call that controls enrollment on belzutifan via NCT04924075 and on the temozolomide trials NCT03556384 and NCT05661643. If both the IHC arbitration and the germline workup come back unsupportive, the trial-route options foreclose and the conversation about KIT/PDGFRA-WT systemic care for first recurrence belongs with the treating team rather than this report.

### SDHA

Five workup steps stack on one tissue pull. Essential: SDHB IHC re-cut (clone 21A11 or BSB-131) with an explicit positive internal control vessel in the field, reviewed by a soft-tissue or GI pathologist who routinely sees SDH-deficient tumors; paired SDHA IHC (clone 2E3 or D6J9M) on the same block, which is specifically lost in SDHA-driven cases and arbitrates the SDHB-intact paradox more directly than re-staining SDHB alone; germline SDHA full-gene sequencing with del/dup analysis as part of a hereditary paraganglioma-pheochromocytoma panel covering all 10 PGL/PCC genes, which resolves whether SDHA L306P (VAF 44%) is germline or fully somatic and triggers cascade testing of first-degree relatives if germline; baseline paraganglioma surveillance with plasma free metanephrines by LC-MS/MS plus rapid-sequence whole-body MRI from skull base to pelvis, which is the patient-safety floor for any SDHx carrier going to anesthesia for any reason; and tumor tissue NGS on a comprehensive FDA-cleared panel (FoundationOne CDx or equivalent) to confirm or refute the ctDNA-only SDHA E350fs, PIK3CA R93W, and MAP2K1 P124S calls. High-priority: Signatera tumor-informed ctDNA MRD using an FFPE-derived bespoke panel as a recurrence-surveillance adjunct to imaging (informative, not therapy-triggering). Medium-priority: SDHC promoter methylation analysis as the fallback driver-call assay if the SDHA workup collapses, ordered through the NIH Pediatric and wild-type GIST Clinic since clinically-available testing is limited to academic referral labs; MGMT promoter methylation on archival FFPE, deferred until recurrence is anticipated or temozolomide enters the active discussion. Bundling the IHC re-cut, SDHA IHC, tumor NGS, and Signatera baseline build on a single archival block keeps the operational sequence to one tissue pull.

### PIK3CA R93W

Tissue NGS confirmation on a comprehensive FDA-cleared panel (FoundationOne CDx, Tempus xT CDx, or equivalent) of the ctDNA-only call. R93W sits outside the validated alpelisib companion-diagnostic hotspots (E542K, E545K/A/D/G, H1047R/Y/L, C420R) and the variant has not been corroborated on tumor tissue, so any PI3Kα-inhibitor discussion or trial enrollment is gated on this step. Same comprehensive panel resolves the MAP2K1 and SDHA E350fs questions on one requisition.

### MAP2K1 P124S

Same tissue NGS panel as PIK3CA. P124 is a recognized MEK1 activating site (P124L/Q/S) with documented but heterogeneous MEK-inhibitor response, but the ctDNA-only call cannot anchor MEK-inhibitor consideration until clonality in tumor is established. Without that, MEK monotherapy in MAP2K1-mutant disease is a stretch outside histiocytosis and melanoma even at the best of times.

### POLE R1679C

Cancer-predisposition genetic counseling referral with R1679C variant reclassification review. R1679 sits outside the canonical POLE proofreading hotspots (P286R, V411L, S459F) and the tumor is TMB-low and MSS, so the polymerase-proofreading-associated polyposis phenotype is not supported. Counseling resolves the variant on the right side of the ledger (most likely VUS, no current ICI rationale, no polyposis surveillance trigger) and folds the SDHA germline result into the same family-risk conversation rather than scheduling two staggered ones.

### Where to order these assays

| Assay | Provider | Decision gated | Contact |
|---|---|---|---|
| **Germline SDHA full-gene sequencing + del/dup (hereditary PGL/PCC panel)** | **Labcorp Genetics *(preferred)* (Invitae Hereditary Paraganglioma-Pheochromocytoma Panel)** | **Confirms SDH-deficient driver call for belzutifan (NCT04924075) and temozolomide (NCT03556384 / NCT05661643); triggers cascade testing of first-degree relatives.** | **[test info](https://www.invitae.com/providers/test-catalog/test-01302) · 1400 16th Street, San Francisco, CA 94103 · 1-800-436-3037** |
| Germline SDHA full-gene sequencing + del/dup (hereditary PGL/PCC panel) | GeneDx *(GeneDx Pheochromocytoma/Paraganglioma Panel)* | Confirms SDH-deficient driver call for belzutifan (NCT04924075) and temozolomide (NCT03556384 / NCT05661643); triggers cascade testing of first-degree relatives. | [test info](https://www.genedx.com/tests/detail/pheochromocytoma-and-paraganglioma-pgl-pcc-panel-857) · 207 Perry Parkway, Gaithersburg, MD 20877 · 1-888-729-1206 |
| Germline SDHA full-gene sequencing + del/dup (hereditary PGL/PCC panel) | Ambry Genetics *(PGLNext)* | Confirms SDH-deficient driver call for belzutifan (NCT04924075) and temozolomide (NCT03556384 / NCT05661643); triggers cascade testing of first-degree relatives. | [test info](https://www.ambrygen.com/clinician/genetic-testing/panel/pgl-pcc-panel) · 15 Argonaut, Aliso Viejo, CA 92656 · 1-866-262-7943 |
| Germline SDHA full-gene sequencing + del/dup (hereditary PGL/PCC panel) | Mayo Clinic Laboratories *(PGLPN / Hereditary Paraganglioma-Pheochromocytoma Gene Panel)* | Confirms SDH-deficient driver call for belzutifan (NCT04924075) and temozolomide (NCT03556384 / NCT05661643); triggers cascade testing of first-degree relatives. | [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 |
| **Tumor tissue NGS confirmation of PIK3CA R93W** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **PI3Kα-inhibitor consideration (alpelisib, inavolisib); enrollment in PI3K-inhibitor trials.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| Tumor tissue NGS confirmation of PIK3CA R93W | Tempus Labs *(Tempus xT CDx)* | PI3Kα-inhibitor consideration (alpelisib, inavolisib); enrollment in PI3K-inhibitor trials. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| Tumor tissue NGS confirmation of PIK3CA R93W | Caris Life Sciences *(MI Cancer Seek / MI Tumor Seek Hybrid)* | PI3Kα-inhibitor consideration (alpelisib, inavolisib); enrollment in PI3K-inhibitor trials. | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 1-888-979-8669 |
| Tumor tissue NGS confirmation of PIK3CA R93W | NeoGenomics Laboratories *(NeoTYPE Comprehensive Tumor Profile)* | PI3Kα-inhibitor consideration (alpelisib, inavolisib); enrollment in PI3K-inhibitor trials. | [test info](https://neogenomics.com/) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| **Tumor tissue NGS confirmation of MAP2K1 P124S** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **MEK-inhibitor consideration (trametinib, binimetinib) if the variant is clonal in tumor.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| Tumor tissue NGS confirmation of MAP2K1 P124S | Tempus Labs *(Tempus xT CDx)* | MEK-inhibitor consideration (trametinib, binimetinib) if the variant is clonal in tumor. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| Tumor tissue NGS confirmation of MAP2K1 P124S | Memorial Sloan Kettering Diagnostic Molecular Pathology *(MSK-IMPACT)* | MEK-inhibitor consideration (trametinib, binimetinib) if the variant is clonal in tumor. | [test info](https://www.mskcc.org/clinical-services/pathology/molecular-diagnostics) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |
| Tumor tissue NGS confirmation of MAP2K1 P124S | Caris Life Sciences *(MI Cancer Seek)* | MEK-inhibitor consideration (trametinib, binimetinib) if the variant is clonal in tumor. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 1-888-979-8669 |
| **SDHB IHC re-cut with positive internal control** | **Mayo Clinic Laboratories *(preferred)* (SDHB Immunostain test code SDHB / 70550, technical component only)** | **Confirms dSDH-GIST phenotype that gates belzutifan (NCT04924075) and the temozolomide trials; resolves the SDHB-intact / SDHA-biallelic paradox before referral.** | **[test info](https://www.mayocliniclabs.com/test-catalog/Overview/70550) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710** |
| SDHB IHC re-cut with positive internal control | Memorial Sloan Kettering Pathology Consultation Service | Confirms dSDH-GIST phenotype that gates belzutifan (NCT04924075) and the temozolomide trials; resolves the SDHB-intact / SDHA-biallelic paradox before referral. | [test info](https://www.mskcc.org/clinical-services/pathology/consultation-services) · 1275 York Avenue, New York, NY 10065 · 1-212-639-5511 |
| SDHB IHC re-cut with positive internal control | Brigham and Women's Hospital Department of Pathology (Dana-Farber / BWH GIST referral) | Confirms dSDH-GIST phenotype that gates belzutifan (NCT04924075) and the temozolomide trials; resolves the SDHB-intact / SDHA-biallelic paradox before referral. | [test info](https://www.brighamandwomens.org/pathology) · 75 Francis Street, Boston, MA 02115 · 1-617-732-7510 |
| SDHB IHC re-cut with positive internal control | NeoGenomics Laboratories *(SDHB IHC)* | Confirms dSDH-GIST phenotype that gates belzutifan (NCT04924075) and the temozolomide trials; resolves the SDHB-intact / SDHA-biallelic paradox before referral. | [test info](https://neogenomics.com/test-menu/sdhb-stain) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| **SDHA IHC (clone 2E3 or D6J9M)** | **Mayo Clinic Laboratories *(preferred)* (SDHA Immunostain)** | **Arbitrates SDHA-vs-other-SDHx driver call; if SDHA IHC is lost it locks in dSDH-GIST regardless of SDHB result.** | **[test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710** |
| SDHA IHC (clone 2E3 or D6J9M) | Memorial Sloan Kettering Pathology Consultation Service | Arbitrates SDHA-vs-other-SDHx driver call; if SDHA IHC is lost it locks in dSDH-GIST regardless of SDHB result. | [test info](https://www.mskcc.org/clinical-services/pathology/consultation-services) · 1275 York Avenue, New York, NY 10065 · 1-212-639-5511 |
| SDHA IHC (clone 2E3 or D6J9M) | Brigham and Women's Hospital Department of Pathology | Arbitrates SDHA-vs-other-SDHx driver call; if SDHA IHC is lost it locks in dSDH-GIST regardless of SDHB result. | [test info](https://www.brighamandwomens.org/pathology) · 75 Francis Street, Boston, MA 02115 · 1-617-732-7510 |
| SDHA IHC (clone 2E3 or D6J9M) | NeoGenomics Laboratories *(SDHA IHC)* | Arbitrates SDHA-vs-other-SDHx driver call; if SDHA IHC is lost it locks in dSDH-GIST regardless of SDHB result. | [test info](https://neogenomics.com/) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| **Baseline PGL / PCC surveillance: whole-body MRI + Ga-68 DOTATATE PET/CT** | **Treating-center academic radiology *(preferred)* (NCI-designated center with a NET program)** | **Paraganglioma / pheochromocytoma surveillance frequency and modality choice for an SDHx-deficient patient.** | **varies by region** |
| Baseline PGL / PCC surveillance: whole-body MRI + Ga-68 DOTATATE PET/CT | RadNet (national imaging network) | Paraganglioma / pheochromocytoma surveillance frequency and modality choice for an SDHx-deficient patient. | [test info](https://www.radnet.com/) · 1510 Cotner Avenue, Los Angeles, CA 90025 · 1-310-478-7808 |
| Baseline PGL / PCC surveillance: whole-body MRI + Ga-68 DOTATATE PET/CT | NIH Clinical Center (Pacak laboratory) | Paraganglioma / pheochromocytoma surveillance frequency and modality choice for an SDHx-deficient patient. | [test info](https://www.cc.nih.gov/) · 10 Center Drive, Bethesda, MD 20892 · 1-800-411-1222 |
| **Plasma free metanephrines + normetanephrines (LC-MS/MS) and / or 24-hour urine fractionated metanephrines** | **Mayo Clinic Laboratories *(preferred)* (PMETF / Metanephrines, Fractionated, Free, Plasma)** | **Functional paraganglioma / pheochromocytoma screen; informs anesthesia-safety planning and surveillance interval.** | **[test info](https://www.mayocliniclabs.com/test-catalog/Overview/8859) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710** |
| Plasma free metanephrines + normetanephrines (LC-MS/MS) and / or 24-hour urine fractionated metanephrines | Quest Diagnostics *(Metanephrines, Free, Plasma (LC-MS/MS))* | Functional paraganglioma / pheochromocytoma screen; informs anesthesia-safety planning and surveillance interval. | [test info](https://testdirectory.questdiagnostics.com/test/test-detail/37562/metanephrines-free-plasma) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| Plasma free metanephrines + normetanephrines (LC-MS/MS) and / or 24-hour urine fractionated metanephrines | Labcorp *(Metanephrines, Fractionated, Plasma Free)* | Functional paraganglioma / pheochromocytoma screen; informs anesthesia-safety planning and surveillance interval. | [test info](https://www.labcorp.com/tests/123059/metanephrines-fractionated-plasma-free) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| Plasma free metanephrines + normetanephrines (LC-MS/MS) and / or 24-hour urine fractionated metanephrines | ARUP Laboratories *(Metanephrines, Fractionated, Free, Plasma by LC-MS/MS)* | Functional paraganglioma / pheochromocytoma screen; informs anesthesia-safety planning and surveillance interval. | [test info](https://ltd.aruplab.com/Tests/Pub/2007006) · 500 Chipeta Way, Salt Lake City, UT 84108 · 1-800-522-2787 |
| **Cancer-predisposition genetic counseling referral (POLE R1679C reclassification + SDHA cascade testing)** | **NSGC Find-a-Genetic-Counselor Directory *(preferred)*** | **Polyposis surveillance decision (almost certainly no for R1679C VUS at TMB <1 / MSS) and family cascade-testing decision.** | **[test info](https://findageneticcounselor.nsgc.org/) · 330 N Wabash Ave, Suite 2000, Chicago, IL 60611 · 1-312-321-6834** |
| Cancer-predisposition genetic counseling referral (POLE R1679C reclassification + SDHA cascade testing) | Dana-Farber Cancer Genetics and Prevention Program | Polyposis surveillance decision (almost certainly no for R1679C VUS at TMB <1 / MSS) and family cascade-testing decision. | [test info](https://www.dana-farber.org/cancer-genetics-and-prevention) · 450 Brookline Avenue, Boston, MA 02215 · 1-617-632-2178 |
| Cancer-predisposition genetic counseling referral (POLE R1679C reclassification + SDHA cascade testing) | MD Anderson Clinical Cancer Genetics Program | Polyposis surveillance decision (almost certainly no for R1679C VUS at TMB <1 / MSS) and family cascade-testing decision. | [test info](https://www.mdanderson.org/patients-family/diagnosis-treatment/care-centers-clinics/clinical-cancer-genetics-program.html) · 1515 Holcombe Boulevard, Houston, TX 77030 · 1-877-632-6789 |
| Cancer-predisposition genetic counseling referral (POLE R1679C reclassification + SDHA cascade testing) | Memorial Sloan Kettering Clinical Genetics Service | Polyposis surveillance decision (almost certainly no for R1679C VUS at TMB <1 / MSS) and family cascade-testing decision. | [test info](https://www.mskcc.org/cancer-care/diagnosis-treatment/cancer-screening-prevention/hereditary/clinical-genetics) · 1275 York Avenue, New York, NY 10065 · 1-646-888-4050 |
| **Tumor tissue NGS for SDHA E350fs (same comprehensive panel as PIK3CA / MAP2K1)** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Clonal-architecture mapping; no direct intervention gating since biallelic SDHA inactivation already established.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| Tumor tissue NGS for SDHA E350fs (same comprehensive panel as PIK3CA / MAP2K1) | Tempus Labs *(Tempus xT CDx)* | Clonal-architecture mapping; no direct intervention gating since biallelic SDHA inactivation already established. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| **Tumor-informed ctDNA MRD (Signatera) or tumor-naive comprehensive ctDNA panel** | **Natera *(preferred)* (Signatera tumor-informed ctDNA MRD)** | **Recurrence-surveillance signal; complements imaging but does not by itself trigger therapy initiation in dSDH-GIST.** | **[test info](https://www.natera.com/oncology/signatera-advanced-cancer-detection/) · 13011 McCallen Pass, Building A, Austin, TX 78753 · 1-650-249-9090** |
| Tumor-informed ctDNA MRD (Signatera) or tumor-naive comprehensive ctDNA panel | Guardant Health *(Guardant360 (tumor-naive comprehensive ctDNA))* | Recurrence-surveillance signal; complements imaging but does not by itself trigger therapy initiation in dSDH-GIST. | [test info](https://guardanthealth.com/products/guardant360/) · 505 Penobscot Drive, Redwood City, CA 94063 · 1-855-698-8887 |
| Tumor-informed ctDNA MRD (Signatera) or tumor-naive comprehensive ctDNA panel | Foundation Medicine *(FoundationOne Liquid CDx)* | Recurrence-surveillance signal; complements imaging but does not by itself trigger therapy initiation in dSDH-GIST. | [test info](https://www.foundationmedicine.com/test/foundationone-liquid-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| Tumor-informed ctDNA MRD (Signatera) or tumor-naive comprehensive ctDNA panel | Tempus Labs *(Tempus xF / xF+)* | Recurrence-surveillance signal; complements imaging but does not by itself trigger therapy initiation in dSDH-GIST. | [test info](https://www.tempus.com/oncology/genomic-profiling/xf/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| **SDHC promoter methylation analysis (pyrosequencing or methylation-specific PCR)** | **NIH Pediatric and Wild-Type GIST Clinic *(preferred)*** | **dSDH-GIST sub-driver call if SDHA inactivation is not confirmed; does not gate therapy by itself.** | **[test info](https://ccr.cancer.gov/pediatric-oncology-branch/pediatric-and-wild-type-gist-clinic) · 10 Center Drive, Bethesda, MD 20892 · 1-240-760-6000** |
| SDHC promoter methylation analysis (pyrosequencing or methylation-specific PCR) | University Hospital Mannheim (Wegert / Hofmann group) | dSDH-GIST sub-driver call if SDHA inactivation is not confirmed; does not gate therapy by itself. | Theodor-Kutzer-Ufer 1-3, 68167 Mannheim, Germany |
| **MGMT promoter methylation (pyrosequencing or methylation-specific PCR)** | **Mayo Clinic Laboratories *(preferred)* (MGMTM / MGMT Promoter Methylation, Tumor)** | **Temozolomide-response prediction at recurrence (NCT03556384, NCT05661643).** | **[test info](https://www.mayocliniclabs.com/test-catalog/Overview/89033) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710** |
| MGMT promoter methylation (pyrosequencing or methylation-specific PCR) | Quest Diagnostics *(MGMT Methylation Analysis)* | Temozolomide-response prediction at recurrence (NCT03556384, NCT05661643). | [test info](https://testdirectory.questdiagnostics.com/test/test-detail/91720/mgmt-methylation-analysis) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| MGMT promoter methylation (pyrosequencing or methylation-specific PCR) | Labcorp *(MGMT Promoter Methylation)* | Temozolomide-response prediction at recurrence (NCT03556384, NCT05661643). | [test info](https://www.labcorp.com/) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| MGMT promoter methylation (pyrosequencing or methylation-specific PCR) | NeoGenomics Laboratories *(MGMT Methylation by PCR)* | Temozolomide-response prediction at recurrence (NCT03556384, NCT05661643). | [test info](https://neogenomics.com/) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |

### Biomarker plan

| Recommended assay | Rationale | Suggested assay provider | Tissue requirements |
|---|---|---|---|
| Germline SDHA full-gene sequencing + del/dup (hereditary paraganglioma-pheochromocytoma panel) | Resolves whether SDHA L306P (VAF 44%) is germline (single-hit carrier with a second somatic event) or fully somatic. Locks in the SDH-deficient driver call gating the temozolomide and belzutifan trials and triggers first-degree-relative cascade testing per the 2025 Florou review. | Labcorp Genetics *(Invitae Hereditary Paraganglioma-Pheochromocytoma Panel)* · [test info](https://www.invitae.com/providers/test-catalog/test-01302) · 1400 16th Street, San Francisco, CA 94103 · 1-800-436-3037 | 5-10 mL whole blood (EDTA) or saliva kit |
| Tumor tissue NGS confirmation of PIK3CA R93W (FoundationOne CDx, Tempus xT, or equivalent) | R93W sits outside the validated alpelisib companion-diagnostic hotspots and the ctDNA-only call has not been corroborated on tumor tissue. Confirms whether the variant is a real subclonal alteration or a ctDNA artifact and frames any PI3Kα-inhibitor discussion. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | 1 FFPE block or 10-20 unstained slides; archival acceptable |
| Tumor tissue NGS confirmation of MAP2K1 P124S (comprehensive panel) | P124 is a recognized MEK1 activating site with documented but heterogeneous MEK-inhibitor response. The variant is currently ctDNA-only; tissue confirmation establishes whether it is clonal in the resected tumor or low-allele-fraction subclonal / artifactual. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | 1 FFPE block or 10-20 unstained slides; archival acceptable |
| SDHB IHC re-cut with positive internal control (clone 21A11 or BSB-131) | Biallelic SDHA inactivation at ~85% combined VAF should destabilize the SDH complex and abolish SDHB staining; retained SDHB in this case conflicts with the molecular call. A re-cut with explicit positive internal control resolves the most likely technical false-negative before the dSDH-GIST diagnosis anchors trial enrollment. | Mayo Clinic Laboratories *(SDHB Immunostain test code SDHB / 70550)* · [test info](https://www.mayocliniclabs.com/test-catalog/Overview/70550) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 | 1 unstained slide from archival FFPE (block returns to pathology) |
| SDHA IHC (clone 2E3 or D6J9M) on archival FFPE | SDHA IHC is specifically lost in tumors with biallelic SDHA inactivation while retained in SDHB/C/D or SDHC-methylation-driven cases. Arbitrates the SDHB-intact / SDHA-biallelic conflict more directly than re-staining SDHB alone. | Mayo Clinic Laboratories *(SDHA Immunostain)* · [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 | 1 unstained slide from archival FFPE |
| Baseline PGL / PCC surveillance: rapid-sequence whole-body MRI plus Ga-68 DOTATATE PET/CT | SDHx carriers carry a lifetime paraganglioma / pheochromocytoma risk warranting imaging surveillance even when the index tumor is a GIST. Current Endocrine Society 2014 / ENS@T consensus recommends biennial whole-body MRI from skull base to pelvis with Ga-68 DOTATATE as the most sensitive functional tracer. Clean baseline now also serves as the recurrence-monitoring comparator. | Treating-center academic radiology at an NCI-designated center with an established NET / PGL program · varies by region | no specimen; imaging only |
| Plasma free metanephrines + normetanephrines (LC-MS/MS) plus 24-hour urine fractionated metanephrines | An undetected functional paraganglioma in an SDHx carrier going to surgery or anesthesia is a hypertensive-crisis hazard. Biochemical screening pairs with imaging as the standard SDHx workup per the Endocrine Society 2014 guideline; plasma free metanephrines by LC-MS/MS is the most sensitive single test. | Mayo Clinic Laboratories *(PMETF / Metanephrines, Fractionated, Free, Plasma)* · [test info](https://www.mayocliniclabs.com/test-catalog/Overview/8859) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 | 10 mL plasma (EDTA) and / or 24-hour urine collection in acid-preservative container |
| Cancer-predisposition genetic counseling referral with POLE R1679C reclassification review | R1679 sits outside the canonical POLE proofreading hotspots and the tumor is TMB-low / MSS, so the polymerase-proofreading-associated polyposis phenotype is not supported. Counseling resolves the variant on the right side of the ledger and folds the SDHA germline result into one coherent family-risk discussion. | NSGC Find-a-Genetic-Counselor Directory · [test info](https://findageneticcounselor.nsgc.org/) · 330 N Wabash Ave, Suite 2000, Chicago, IL 60611 · 1-312-321-6834 | no specimen required; counselor reviews the existing germline report |
| Tumor tissue NGS for SDHA E350fs (same comprehensive panel as PIK3CA / MAP2K1) | E350fs was called from ctDNA but not seen in the tumor NGS that already reported L306P and Y408N. Confirming or refuting clarifies whether this is a true third SDHA hit, a subclonal event in unsampled tissue, or a ctDNA artifact. Incremental rather than gating since biallelic inactivation is already established. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | shared with PIK3CA / MAP2K1 block |
| Tumor-informed ctDNA MRD assay (Signatera) or tumor-naive comprehensive ctDNA panel | Post-R0 with no measurable disease and the existing ctDNA call surface already informative (SDHA E350fs, PIK3CA R93W, MAP2K1 P124S). Serial ctDNA gives a lead-time signal for recurrence ahead of imaging. GIST has weaker prospective MRD validation than colorectal or lung; frame as informative rather than gating. | Natera *(Signatera tumor-informed ctDNA MRD)* · [test info](https://www.natera.com/oncology/signatera-advanced-cancer-detection/) · 13011 McCallen Pass, Building A, Austin, TX 78753 · 1-650-249-9090 | 5-10 mL plasma (Streck tube); Signatera baseline also needs an FFPE block |
| SDHC promoter methylation analysis (pyrosequencing or methylation-specific PCR) | Fallback driver-call assay if the SDHA story collapses on the SDHA IHC / germline / E350fs workup. SDHC promoter epimutation is the next-most-likely Carney-triad-pattern driver and most dSDH-GIST trials accept methylation-driven cases as SDH-deficient. Clinically-available testing is limited to academic referral labs. | NIH Pediatric and Wild-Type GIST Clinic · [test info](https://ccr.cancer.gov/pediatric-oncology-branch/pediatric-and-wild-type-gist-clinic) · 10 Center Drive, Bethesda, MD 20892 · 1-240-760-6000 | FFPE block or 10 unstained slides |
| MGMT promoter methylation (pyrosequencing or methylation-specific PCR) | Recent data show preferential MGMT promoter hypermethylation in SDH-deficient wild-type GIST and a corresponding rationale for temozolomide activity. If the temozolomide trials become the leading systemic option at recurrence, MGMT status helps predict response. Does not gate enrollment but adds depth once disease becomes measurable. | Mayo Clinic Laboratories *(MGMTM / MGMT Promoter Methylation, Tumor)* · [test info](https://www.mayocliniclabs.com/test-catalog/Overview/89033) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 | FFPE block or 10 unstained slides; bundle with SDHC methylation order if both are needed |

---

*Decision support, not medical advice. Confirm assay availability and current standards with the treating team and the local pathology service.*

<!-- libby:target-validation:end -->

## Scope summary

15 trials surfaced, 22 clinical-evidence rows (13 included plus 9 logged as `considered_excluded` per the molecular-subset transport rules — adjuvant-imatinib RCTs and PI3Kα / PARP-class extrapolation candidates), 22 preclinical rows (14 included), and 12 target-validation rows (8 essential + 2 high-priority + 2 medium-priority). The ranked list contains 12 rows spanning agreement scores from +1.0 (rank 1 shared workup; rank 3 NCI registry — both unanimous) down to -0.8 (rank 12 adjuvant imatinib — vetoed by every persona in concept). All five personas converged on the rank-1 workup bundle and on the rank-2 active-surveillance call; one preference-fit dissent on the rank-6 sunitinib contingency from the risktaker (preferring trial-route at recurrence); two formal dissents on the rank-9 pemigatinib trial pick (advocate on preferences, critic on evidence pyramid); one conservative veto on the rank-11 olaparib + temozolomide combination, overridden to a bounded late-line trial-route framing; unanimous veto on rank-12 adjuvant imatinib.

## Cross-cutting caveat (read first)

**The dSDH-GIST phenotype itself is not fully locked in. Retained SDHB IHC alongside biallelic SDHA inactivation at combined VAF ~85% is paradoxical — biallelic SDHA loss should destabilize the SDH complex and abolish SDHB staining (Hornick 2013, Miettinen 2013). Every dSDH-GIST trial in this dossier (NCT04924075 belzutifan, NCT03556384 / NCT05661643 temozolomide, NCT07434843 pemigatinib) uses SDHB-IHC loss as the entry phenotype. Until the SDHA IHC + SDHB re-cut + germline SDHA panel close the discrepancy, the dSDH-GIST label is provisional and the trial-route contingency stack is gated on that resolution. The case sits in NED post-R0 disease, so the immediate decision is NOT a therapeutic one — it is a workup decision and an adjuvant-vs-surveillance decision.**

- **The ranking is targetable-feature-scoped to dSDH-GIST (and the KIT/PDGFRA-WT systemic backbone in that subset).** Standard-of-care chemotherapy for KIT-mutant GIST (adjuvant imatinib in particular) does not target the patient's stated targetable feature and is logged as NOT RECOMMENDED rather than off-the-page so the no-imatinib decision is documented and not re-litigated. The PI3Kα and MEK paths gated on ctDNA-only PIK3CA R93W and MAP2K1 P124S are not ranked — R93W sits outside the validated alpelisib hotspots and Burke 2012 biochemistry classifies the ABD-domain class as weakly activating; both variants are ctDNA-only and tissue NGS confirmation is a prerequisite that has not happened yet. Linsitinib (IGF-1R) and guadecitabine (DNA hypomethylating agent) are mechanism-matched programs that read out negative (0/20 and 0/9 respectively) and are off the table.
- **If the SDHA workup collapses (SDHB intact + SDHA intact on clean re-stain, or germline SDHA panel finds no constitutional variant and the L306P proves tumor-only artifact), the trial-route contingency picks at ranks 7, 8, and 9 (belzutifan, temozolomide, pemigatinib) are foreclosed.** In that scenario this case has no within-scope trial-route recommendations targeting the gating feature; the systemic backbone for KIT/PDGFRA-WT non-dSDH GIST at recurrence (sunitinib, then regorafenib) lies outside Libby's targetable-feature ranking and should be pursued through the treating team's normal care channel, and the SDHC promoter methylation fallback assay (medium-priority on the validation paths report) becomes decision-relevant.
- **Workup logistics are unusually load-bearing here because rank 1 is the workup row itself.** Operational discipline: one tissue pull, three answers — pull the archival FFPE once, run the SDHB IHC re-cut with positive internal control + SDHA IHC + comprehensive tumor NGS for the PIK3CA / MAP2K1 / SDHA E350fs confirmation on the same panel. Order germline SDHA on whole blood (or saliva) in parallel. Turnaround is 2-4 weeks for the IHC/tissue NGS and 2-3 weeks for the germline panel. Reference labs: Mayo Clinic Laboratories for SDHB/SDHA IHC with a validated protocol (the most defensible reference for an equivocal stain); Labcorp Genetics (formerly Invitae) Hereditary Paraganglioma-Pheochromocytoma Panel for germline SDHA; Foundation Medicine FoundationOne CDx for tissue NGS confirmation of the ctDNA-only variants. The same archival block can carry all the IHC + tissue NGS + Signatera baseline-build work.
- **Preferences are defaulted. The strength of the surveillance recommendation rests on the user not having stated a preference for 'doing something' over 'doing the right thing,' and that gap has to be closed before the recommendation hardens.** Geography is also unspecified, and at recurrence the travel question becomes load-bearing — NCT05661643 is Asan Medical Center in Seoul, PEMIGIST (NCT07434843) is DFCI single-site in Boston, LITESPARK-015 (NCT04924075) has 14 US sites. A real preferences elicitation should happen before any of these contingencies are committed to.

## Intervention grouping

- **Diagnostic / workup gating:** SDHA germline panel (Labcorp Genetics PGL/PCC panel), SDHA + SDHB IHC re-cut (Mayo Clinic Laboratories), tumor-tissue NGS confirmation of PIK3CA R93W / MAP2K1 P124S / SDHA E350fs (FoundationOne CDx) — pmid:[39927693](https://pubmed.ncbi.nlm.nih.gov/39927693), pmid:[35546442](https://pubmed.ncbi.nlm.nih.gov/35546442), pmid:[23023976](https://pubmed.ncbi.nlm.nih.gov/23023976).
- **Active management today (NED state):** structured imaging surveillance (NCCN GIST v1.2025 + ESMO-EURACAN-GENTURIS 2022), NCI Rare Tumor Natural History Study enrollment ([NCT03739827](https://clinicaltrials.gov/study/NCT03739827)), paraganglioma/pheochromocytoma baseline workup (Endocrine Society 2014 guideline), Signatera tumor-informed MRD as imaging adjunct (pmid:[34754095](https://pubmed.ncbi.nlm.nih.gov/34754095)).
- **dSDH-GIST trial-route therapeutics for first recurrence (gated on dSDH phenotype confirmation):** belzutifan on LITESPARK-015 wt-GIST cohort ([NCT04924075](https://clinicaltrials.gov/study/NCT04924075)) — pmid:[15652751](https://pubmed.ncbi.nlm.nih.gov/15652751), pmid:[35324464](https://pubmed.ncbi.nlm.nih.gov/35324464); temozolomide on the Asan trial ([NCT05661643](https://clinicaltrials.gov/study/NCT05661643)) or the UCSD trial ([NCT03556384](https://clinicaltrials.gov/study/NCT03556384), active-not-recruiting, watch-for-readout) — pmid:[34426440](https://pubmed.ncbi.nlm.nih.gov/34426440), pmid:[38132569](https://pubmed.ncbi.nlm.nih.gov/38132569); pemigatinib on PEMIGIST ([NCT07434843](https://clinicaltrials.gov/study/NCT07434843)) — Flynn 2025 AACR abstract CT215.
- **KIT/PDGFRA-WT systemic backbone TKIs (contingency at recurrence; not dSDH-specific):** sunitinib at 2L (Demetri 2006, pmid:[17046465](https://pubmed.ncbi.nlm.nih.gov/17046465); Boikos 2016, pmid:[27011036](https://pubmed.ncbi.nlm.nih.gov/27011036)); regorafenib at 3L (Demetri 2013 GRID, pmid:[23177515](https://pubmed.ncbi.nlm.nih.gov/23177515); Dedousis 2025, pmid:[40045030](https://pubmed.ncbi.nlm.nih.gov/40045030)).
- **PARP-plus-alkylator synthetic-lethal late-line contingency:** olaparib + temozolomide on the Sulkowski synthetic-lethal mechanism (pmid:[30013182](https://pubmed.ncbi.nlm.nih.gov/30013182), pmid:[32494005](https://pubmed.ncbi.nlm.nih.gov/32494005), pmid:[36151992](https://pubmed.ncbi.nlm.nih.gov/36151992)) — bounded use only.
- **Adjuvant imatinib — explicitly NOT RECOMMENDED:** logged for the record so the reflex 'GIST equals imatinib' reach is documented and rejected (Boikos 2016 pmid:[27011036](https://pubmed.ncbi.nlm.nih.gov/27011036); ESMO-EURACAN-GENTURIS 2022; PERSIST-5 pmid:[30383140](https://pubmed.ncbi.nlm.nih.gov/30383140)).

## Top interventions

### Rank 1. SDHA germline panel + SDHA/SDHB IHC re-cut + tumor-tissue NGS bundle (one-tissue-pull, three-answers diagnostic gate)

*Shared workup. Resolves the SDHB-intact / SDHA-biallelic paradox, locks in the germline-vs-somatic call for SDHA L306P, and confirms or refutes the ctDNA-only PIK3CA / MAP2K1 / SDHA E350fs variants before any trial-route contingency is reached for.*

#### Evidence base

The SDHB-IHC pitfall literature (Hornick 2013 [PMID 23046294](https://pubmed.ncbi.nlm.nih.gov/23046294); Miettinen 2013 [PMID 23023976](https://pubmed.ncbi.nlm.nih.gov/23023976); Wagner 2013 [PMID 23459398](https://pubmed.ncbi.nlm.nih.gov/23459398); Pantaleo 2022 [PMID 35546442](https://pubmed.ncbi.nlm.nih.gov/35546442)) anchors the technical case: biallelic SDHA inactivation should destabilize the SDH complex and abolish SDHB staining, and SDHA IHC (clone 2E3 or D6J9M) is specifically lost in SDHA-driven dSDH-GIST while retained in SDHB/C/D or SDHC-methylation-driven cases. The 2025 Florou review ([PMID 39927693](https://pubmed.ncbi.nlm.nih.gov/39927693)) is the contemporary reference for the germline-SDHA workup. Burke 2012 ([PMID 22949673](https://pubmed.ncbi.nlm.nih.gov/22949673)) is the biochemistry paper that classifies the ABD-domain PIK3CA class (R88Q, R93W, G106V) as weakly activating relative to the canonical helical-domain (E545K) and kinase-domain (H1047R) hotspots — the structural reason the PIK3CA R93W call is at best a partial driver even if it confirms in tissue.

#### Likelihood of desired effect

Diagnostic certainty — not a therapeutic effect. The germline SDHA result resolves cascade testing and the lifetime PGL-surveillance cadence; the SDHA IHC arbitrates the SDHB-intact paradox; the comprehensive tumor NGS panel locks in or rejects the ctDNA-only variants. All three answers come from one archival block plus one blood draw. The dSDH phenotype confirmation gates the three downstream trial-route therapeutics at recurrence (ranks 7, 8, 9).

#### Toxicity profile

- None — germline blood draw, IHC re-cut on existing FFPE, comprehensive tumor NGS panel on the same FFPE.
- Operational cost is 2-4 weeks of turnaround before the trial-route contingencies can move and the cascade-testing conversation can begin.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. The critic's round-2 push was to elevate the SDHB-intact / SDHA-biallelic discrepancy from "loose end" to "structural threat" — every dSDH-GIST trial entry phenotype runs through SDHB-IHC loss, and an unresolved IHC discordance gets the patient bounced at trial screening. The advocate framed the operational discipline (one tissue pull, three answers); the conservative endorsed the diagnostic gating and added that every dollar of chronic-toxicity exposure averted by NOT anchoring a PI3Kα or MEK inhibitor on an unconfirmed ctDNA-only call is a clean win.

#### Practical considerations

- **Germline SDHA panel:** Labcorp Genetics (formerly Invitae) Hereditary Paraganglioma-Pheochromocytoma Panel covers all 10 PGL/PCC genes including SDHA full-gene sequencing plus del/dup by NGS — the most widely-ordered hereditary PGL panel in the US and explicitly named in the 2025 Florou review as adequate for SDHA carriers. Order on whole blood (EDTA) or saliva.
- **SDHB IHC re-cut + SDHA IHC:** Mayo Clinic Laboratories runs a validated SDHB protocol (test code SDHB/70550) and a paired SDHA stain — the most defensible reference for resolving an equivocal SDHB read. Send the FFPE block plus the original SDHB-stained slide for side-by-side review. Brigham (Jason Hornick's group) and MSKCC are the academic alternatives.
- **Tumor NGS confirmation:** FoundationOne CDx is the FDA-approved comprehensive panel that covers PIK3CA, MAP2K1, and SDHA on a single requisition. Tempus xT CDx is the equivalent if the center has an existing Tempus relationship.
- **SDHC promoter methylation** sits in reserve at medium priority — order through the NIH Pediatric & wt-GIST Clinic only if the SDHA workup collapses (clinically-available testing is limited to academic referral labs).

#### Why this rank

The workup gates every downstream trial-route contingency and resolves the load-bearing diagnostic flag in the case (SDHB IHC paradox). Agreement score 1.0 with no dissent. Cost is two-to-four weeks of turnaround and effectively no toxicity. There is no rank-2 below this that earns priority over locking in the diagnosis.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Germline SDHA full-gene sequencing + del/dup (Hereditary PGL/PCC panel) | Resolves germline-vs-somatic for SDHA L306P; cascade testing trigger | None (blood / saliva) | [PMID 39927693](https://pubmed.ncbi.nlm.nih.gov/39927693) |
| SDHA IHC (clone 2E3 / D6J9M) on archival FFPE | Arbitrates SDHB-intact paradox; locks in SDHA-driven dSDH if lost | None (IHC on existing FFPE) | [PMID 23023976](https://pubmed.ncbi.nlm.nih.gov/23023976), [PMID 23459398](https://pubmed.ncbi.nlm.nih.gov/23459398) |
| SDHB IHC re-cut with positive internal control | Resolves technical false-negative if present; confirms dSDH-GIST if SDHB now reads as lost | None | [PMID 35546442](https://pubmed.ncbi.nlm.nih.gov/35546442), [PMID 23046294](https://pubmed.ncbi.nlm.nih.gov/23046294) |
| FoundationOne CDx tumor NGS (PIK3CA / MAP2K1 / SDHA E350fs confirmation) | Locks in or refutes the three ctDNA-only variants in tissue | None (archival FFPE) | [PMID 22949673](https://pubmed.ncbi.nlm.nih.gov/22949673) |

### Rank 2. Active surveillance — structured imaging q3-6 mo for 2-3 years then space out, no adjuvant systemic therapy

*The cross-society guideline call and the empirical no on adjuvant imatinib in this molecular subset. Cross-cutting decision today.*

#### Evidence base

Three RCTs of adjuvant imatinib anchor the cross-society convergence against it in dSDH-GIST: Z9001 (DeMatteo 2009 [PMID 19303137](https://pubmed.ncbi.nlm.nih.gov/19303137), RFS HR 0.35), SSGXVIII (Joensuu 2012 [PMID 22453568](https://pubmed.ncbi.nlm.nih.gov/22453568); 10-year follow-up [PMID 32469385](https://pubmed.ncbi.nlm.nih.gov/32469385)), and PERSIST-5 (Raut 2018 [PMID 30383140](https://pubmed.ncbi.nlm.nih.gov/30383140)). All three sit at RoB2:Low for the populations they enrolled, and all three structurally excluded the SDH-deficient subset — dSDH-GIST was not a recognized molecular entity at accrual. The empirical counter-anchor is Boikos 2016 ([PMID 27011036](https://pubmed.ncbi.nlm.nih.gov/27011036), NIH Pediatric & wt-GIST Clinic, ROBINS-I:Moderate): 1/49 (2%) PR in dSDH-GIST on imatinib versus 7/38 (18%) on sunitinib. The natural-history anchor is the Mei/Boikos 2018 review ([PMID 29413424](https://pubmed.ncbi.nlm.nih.gov/29413424)) citing the NIH 76-patient surgical cohort: median EFS ~2.5 years post-R0 with ~71% eventual recurrence — indolent enough that imaging surveillance picks up disease at a treatable window.

#### Likelihood of desired effect

Effect is option preservation. ESMO-EURACAN-GENTURIS 2022 is explicit that adjuvant imatinib should be avoided in dSDH-GIST; NCCN GIST v1.2025 lists imatinib as standard adjuvant only for KIT-mutant high-risk GIST and flags KIT/PDGFRA-WT subtypes (including dSDH-GIST) as imatinib-insensitive. The empirical 2% PR rate against the imatinib 3-year AE profile (G2+ edema ~30%, fatigue ~50%, hepatic and cardiac monitoring burden) is not a defensible toxicity tradeoff at any reasonable efficacy/toxicity weighting. Surveillance preserves every downstream contingency: belzutifan, temozolomide, pemigatinib, sunitinib at recurrence — none of which is reachable later if a year of TKI toxicity gets burned now on a regimen the molecular evidence rejects.

#### Toxicity profile

- None — imaging surveillance has no characterized AE profile.
- Soft cost is scan anxiety and the burden of indefinite follow-up — not captured in any toxicity table and not a preference axis the defaulted preferences elicited.
- PGL imaging carries cumulative radiation if CT-based; the MRI-first protocol (rank 4) mitigates.

#### Counter-productive mechanisms / dissent

Four of five personas put this at rank 1 (conservative, critic, concensusite, advocate); the risktaker did not rank surveillance separately but stated explicitly in their notes that the patient gets no adjuvant systemic therapy — the same call by another name. The advocate's round-2 critique on the conservative rank-1 framing was a discipline note rather than a dissent: surveillance reads too passively if the registry + PGL screen + Signatera + imaging cadence are listed as separate adjuncts, so bundle them as one active-surveillance package. The conservative endorsed the advocate's pick on the same grounds, citing the option-preservation argument: starting an adjuvant TKI burns screening eligibility for several recurrence-contingency trials (most require measurable disease and deprioritize prior-systemic-therapy patients). Preferences are defaulted — a real elicitation should happen before this hardens, but the toxicity math gets to the same answer under any plausible weight when there is no efficacy signal to lean on for an adjuvant regimen.

#### Practical considerations

- **Imaging cadence:** cross-sectional CT or whole-body MRI every 3-6 months for the first 2-3 years post-resection, then space out per response. Cadence is consensus-derived rather than RCT-supported in dSDH-GIST specifically.
- **Chart-note discipline:** cite ESMO-EURACAN-GENTURIS 2022 and Boikos 2016 (1/49 PR) in the post-op note so the no-imatinib decision is documented and does not get re-litigated downstream. The most likely failure mode is a community oncologist reaching for adjuvant imatinib on the 'GIST equals imatinib' reflex — a clearly documented dissent in the chart is the cheapest insurance.
- **Multifocal primary + resected M1 puts this patient outside the cleanest natural-history cohorts** (mostly localized primaries). The 2.5-year mEFS estimate is a floor, not a ceiling — keep the cadence on the tighter end of the q3-6 mo range early.
- **Geography is unspecified.** If the patient is not near an NCI-designated center with a sarcoma program, imaging cadence stays local and the registry visit (rank 3) is the specialist touchpoint.

#### Why this rank

The workup at rank 1 has to happen first to lock in the trial-route contingency stack, but the surveillance decision is the immediate management call and is what the patient leaves clinic with this week. Cross-society guideline convergence + empirical 2% imatinib PR rate make this the cleanest decision in the dossier.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Active surveillance with imaging q3-6 mo + PGL screen | EFS ~2.5 yr post-R0 in NIH 76-pt cohort; ~71% eventual recurrence | None (imaging only) | [PMID 29413424](https://pubmed.ncbi.nlm.nih.gov/29413424) |
| Adjuvant imatinib (excluded — comparator anchor) | 1/49 (2%) PR in dSDH-GIST on imatinib (Boikos 2016) | G2+ edema ~30%, fatigue ~50% on 3-yr exposure | [PMID 27011036](https://pubmed.ncbi.nlm.nih.gov/27011036) |
| Adjuvant imatinib in KIT-mutant high-risk GIST (population-mismatched anchor) | Z9001: RFS HR 0.35; SSGXVIII: RFS HR 0.46, OS HR 0.45; PERSIST-5: 5-yr RFS 90% | RoB2:Low for the populations enrolled; dSDH-GIST not represented | [PMID 19303137](https://pubmed.ncbi.nlm.nih.gov/19303137), [PMID 22453568](https://pubmed.ncbi.nlm.nih.gov/22453568), [PMID 32469385](https://pubmed.ncbi.nlm.nih.gov/32469385), [PMID 30383140](https://pubmed.ncbi.nlm.nih.gov/30383140) |

### Rank 3. NCI Rare Tumor Natural History Study (NCT03739827) + cancer-genetics counseling

*Zero-toxicity, highest-yield-per-cost move on the page. The only trial the patient can join today.*

#### Evidence base

Janeway 2011 ([PMID 21173220](https://pubmed.ncbi.nlm.nih.gov/21173220)) is the prospective NIH/DFCI cohort that established SDH-deficient GIST as a real molecular entity beyond Carney-Stratakis syndrome (4/34 sporadic wt-GIST carried germline SDH defects). The 2025 Florou review ([PMID 39927693](https://pubmed.ncbi.nlm.nih.gov/39927693)) frames the contemporary workup. The POLE counseling case rests on Bourdais 2017 + Domingo 2016-class data on canonical proofreading hotspots ([PMID 32424176](https://pubmed.ncbi.nlm.nih.gov/32424176), [PMID 32058550](https://pubmed.ncbi.nlm.nih.gov/32058550)): R1679C sits outside that domain, the patient is TMB <1 / MSS, and the standard hypermutator-ICI rationale does not transport — counseling resolves the variant as a likely VUS without a polyposis surveillance trigger.

#### Likelihood of desired effect

Infrastructure-level effect. Registry enrollment is open regardless of disease status, so the NED-post-R0 state is not a blocker. Pairs naturally with cancer-genetics counseling once the germline SDHA panel returns (2-3 weeks); folds the POLE R1679C VUS framing into the same family-risk conversation. Three structural payoffs: (1) longitudinal specialty follow-up at the NIH Pediatric & wt-GIST Clinic for a tumor too rare for community oncology to maintain expertise on; (2) access to SDHC promoter methylation testing if the SDHA workup collapses (clinically-available testing is otherwise limited to academic referral labs); (3) biospecimen banking that pays forward if a slot on PEMIGIST or LITESPARK-015 opens at recurrence.

#### Toxicity profile

- None — registry enrollment plus a counseling visit.
- One in-person baseline visit at NIH Bethesda (or OHSU / Texas Children's as alternative arms) — travel is the operational cost.

#### Counter-productive mechanisms / dissent

All five personas surfaced the registry as the highest-yield zero-toxicity move. Conservative and concensusite at rank 2, advocate at rank 2, risktaker at rank 5, critic endorsed in round 2 on the conservative pick. The critic's round-2 push was to elevate the SDHB-intact / SDHA-biallelic discrepancy more sharply than the conservative's framing did — it is the load-bearing diagnostic threat to every trial-route contingency, and the registry is the operational vehicle that unlocks the SDHC methylation fallback if the SDHA story collapses. No dissent on the call itself.

#### Practical considerations

- **Operational sequencing:** order the germline SDHA panel and the SDHA/SDHB IHC re-cut now (rank 1); the registry visit can run either before or after the germline result returns. Most NIH counselors prefer to discuss both findings (SDHA + POLE R1679C) together, which favors scheduling the visit after the germline result.
- **Geography:** registry baseline requires US travel to NIH Bethesda (or OHSU, or Texas Children's). The patient's geography and time-off-work are not specified in preferences.json — flag this for the care team.
- **POLE counseling will most likely land on VUS** at TMB <1 / MSS for a non-proofreading-domain variant. Tell the patient upfront so the result is not over-interpreted.
- **Reference centers for dSDH-GIST:** NIH Pediatric & wt-GIST Clinic (Bethesda), DFCI (Suzanne George), MSKCC (Ping Chi), Royal Marsden (Robin Jones), Lyon Centre Léon Bérard (Jean-Yves Blay). NIH is the primary registry door; the others are referral pathways the registry itself routes patients toward.

#### Why this rank

Rank 3 sits behind surveillance (the active management decision today) and the workup (the diagnostic gate). The registry is the operational scaffolding that everything else attaches to — it is not the management decision, but it is the highest-yield move with zero toxicity. Agreement score 1.0.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| NCI Rare Tumor Natural History Study (NCT03739827) | Specialty follow-up + biospecimen banking + SDHC methylation access | None (registry + biospecimen) | [NCT03739827](https://clinicaltrials.gov/study/NCT03739827) |
| Cancer-genetics counseling (SDHA + POLE) | Cascade testing decisions; POLE R1679C reclassification | None (counseling visit) | [PMID 32424176](https://pubmed.ncbi.nlm.nih.gov/32424176), [PMID 32058550](https://pubmed.ncbi.nlm.nih.gov/32058550) |

### Rank 4. Paraganglioma / pheochromocytoma baseline surveillance — plasma free metanephrines + rapid-sequence whole-body MRI

*Patient-safety floor for an SDHx carrier. One-time setup; cadence depends on the germline SDHA result.*

#### Evidence base

The Endocrine Society 2014 PPGL guideline (endorsed by ESMO and ENS@T) recommends biochemical screening plus baseline whole-body MRI in SDHx carriers, with Ga-68 DOTATATE PET/CT as the most sensitive functional tracer for SDHx-driven paraganglioma ([PMID 31369093](https://pubmed.ncbi.nlm.nih.gov/31369093), [PMID 23934599](https://pubmed.ncbi.nlm.nih.gov/23934599)). Plasma free metanephrines by LC-MS/MS is the reference-standard biochemical screen ([PMID 24893135](https://pubmed.ncbi.nlm.nih.gov/24893135)).

#### Likelihood of desired effect

Patient-safety floor. An unscreened functional paraganglioma in an SDHx carrier going to anesthesia for any reason is a hypertensive-crisis hazard — directly relevant given the possibility of future re-operation if the patient recurs. The baseline also establishes a clean comparator for the recurrence-monitoring strategy: the question at any later point becomes 'what has changed' rather than 'do we have a baseline.'

#### Toxicity profile

- None — non-invasive imaging + one blood draw.
- Ga-68 DOTATATE adds radiation; deferred to baseline + change-flagging to limit cumulative dose.
- Whole-body MRI sometimes requires prior auth even with documented SDHx-carrier indication.

#### Counter-productive mechanisms / dissent

Advocate ranked the PGL screen explicitly at rank 4; concensusite folded it into the rank-2 registry+screening package; conservative built it into the rank-1 surveillance plan; critic anchored it on Endocrine Society 2014. All four named-endorse personas converge on the same workup; the risktaker did not rank it separately. The cadence decision (biennial vs annual, MRI-only vs DOTATATE-augmented) ties to the SDHA germline result — a confirmed germline carrier triggers the lifelong biennial-imaging cadence; a fully somatic case has lower extra-GIST cancer risk and the schedule shifts.

#### Practical considerations

- **Default to MRI as the repeatable backbone** and reserve Ga-68 DOTATATE for baseline + change-flagging. Ga-68 coverage varies by site and is not uniformly available at community imaging centers.
- **Bundle the metanephrines draw with the germline SDHA blood draw** for operational efficiency (separate result paths, same venipuncture).
- **Reference labs for plasma free metanephrines by LC-MS/MS:** Mayo Clinic Laboratories PMETF assay, Quest Diagnostics, Labcorp, ARUP — broad insurance acceptance.
- **Strong preference for an NCI-designated center with an established NET / PGL program** for the imaging (MD Anderson, MSK, Mayo, NIH, UCLA, Dana-Farber/BWH, UPenn). Ga-68 DOTATATE requires on-site generator or supply arrangement.

#### Why this rank

Patient-safety floor that pairs naturally with the registry visit at rank 3 and the surveillance plan at rank 2. Cadence locks in once the germline SDHA result returns. The workup itself is essentially zero-toxicity and unambiguously guideline-aligned for SDHx carriers.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Plasma free metanephrines (LC-MS/MS) | Functional PGL screen — anesthesia-safety floor | None (blood draw) | [PMID 24893135](https://pubmed.ncbi.nlm.nih.gov/24893135) |
| Rapid-sequence whole-body MRI (skull base to pelvis) | Anatomic PGL screen; repeatable imaging backbone | None (no radiation) | [PMID 31369093](https://pubmed.ncbi.nlm.nih.gov/31369093) |
| Ga-68 DOTATATE PET/CT | Most sensitive functional tracer for SDHx-driven PGL; baseline + change-flagging only | Cumulative radiation; defer routine use | [PMID 23934599](https://pubmed.ncbi.nlm.nih.gov/23934599) |

### Rank 5. Signatera tumor-informed ctDNA MRD as recurrence-surveillance adjunct (informative, not therapy-triggering)

*Lead-time signal ahead of imaging — with an explicit guardrail.*

#### Evidence base

The colorectal and lung tumor-informed MRD literature establishes prognostic informativeness and lead-time signal ahead of cross-sectional imaging ([PMID 34754095](https://pubmed.ncbi.nlm.nih.gov/34754095), [PMID 34380780](https://pubmed.ncbi.nlm.nih.gov/34380780)). GIST-specific prospective MRD validation is thinner. The patient already has ctDNA-detectable SDHA E350fs plus PIK3CA and MAP2K1 variants pre-resection, so plasma is informative in this individual — Signatera can build a bespoke panel from those variants for serial tracking.

#### Likelihood of desired effect

Lead-time signal that flags recurrence weeks ahead of CT. NOT a trigger for systemic-therapy initiation. The right operational use is: a positive Signatera result prompts shortened-interval imaging (CT or MRI at 6-8 weeks instead of the next q3-6-month slot), and only an imaging-confirmed recurrence triggers the contingency stack at ranks 6-11.

#### Toxicity profile

- None — venipuncture only. FFPE block re-use for the baseline panel build (shares tissue with the rank-1 workup).

#### Counter-productive mechanisms / dissent

Conservative ranked the MRD at 4, risktaker at 5, advocate at 3 (bundled with the SDHA workup). The critic did not formally rank but discussed in critique. Conservative's round-2 critique on the risktaker's framing was the binding guardrail: the risktaker's rationale described the goal as "compress lead time to action" so the contingency picks can be "triggered at first molecular relapse rather than waiting for RECIST-measurable disease." That framing is exactly the use case the prospective validation data do not yet support in GIST. The same conservative critique flagged the advocate's similar framing: ctDNA "could legitimately move the conversation from surveillance to sunitinib before the patient is symptomatic" is the actionable read that the validation does not support. With the imaging-gating guardrail explicit in the chart, the modality earns ranking; without it, the assay becomes an anxiety amplifier with a TKI-initiation footgun attached.

#### Practical considerations

- **Modality:** Signatera (Natera) for tumor-informed MRD — bespoke panel built from this patient's known variants, baseline build 4-6 weeks, subsequent draws ~2 weeks. Tumor-naive panels (Guardant360, FoundationOne Liquid CDx) at the recurrence-genotyping moment if needed.
- **Cadence:** q3 months alongside imaging on stable baseline; tighter if a baseline draw is detectable.
- **Tissue triage:** the Signatera baseline-build FFPE block is the same archival block carrying the SDHB IHC re-stain and the FoundationOne CDx tissue NGS confirmation. Order the tissue pull once.
- **Chart language:** the guardrail wording goes in the chart note. "A positive Signatera result prompts shortened-interval imaging; it does not trigger systemic therapy initiation in NED dSDH-GIST."

#### Why this rank

Rank 5 sits behind the active management actions (surveillance, registry, PGL screen) and the workup gate. The assay is genuinely useful but the framing discipline matters more than the modality — with the imaging-gating guardrail it earns the rank, without it the row would belong below the standard-care contingencies.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Signatera tumor-informed ctDNA MRD (Natera) | Lead-time signal ahead of imaging in CRC/lung; GIST validation thinner | None (venipuncture; FFPE block for baseline build) | [PMID 34754095](https://pubmed.ncbi.nlm.nih.gov/34754095), [PMID 34380780](https://pubmed.ncbi.nlm.nih.gov/34380780) |

### Rank 6. Sunitinib 50 mg PO 4-on/2-off (or 37.5 mg continuous) — first systemic line at measurable recurrence; NOT adjuvant

*Best-characterized 2L TKI for KIT/PDGFRA-WT GIST. Contingency-only.*

#### Evidence base

Demetri 2006 ([PMID 17046465](https://pubmed.ncbi.nlm.nih.gov/17046465), Lancet, RoB2:Low, n=312, 2:1 randomization) is the pivotal phase 3 for 2L GIST: time-to-progression HR 0.33 (p<0.0001), mTTP 27.3 weeks vs 6.4 weeks on placebo. The dSDH-GIST subset was minimally represented in the registration cohort, so the activity claim in this molecular subtype runs through Boikos 2016 ([PMID 27011036](https://pubmed.ncbi.nlm.nih.gov/27011036), NIH wt-GIST clinic, ROBINS-I:Moderate, n=38 retrospective subgroup): 7/38 (18%) objective response on sunitinib vs 1/49 (2%) on imatinib. The 18% number has no confidence interval reported; it is the directional anchor that every published sequencing recommendation in dSDH-GIST cites for choosing sunitinib over imatinib at 2L. The Dedousis 2025 review ([PMID 40045030](https://pubmed.ncbi.nlm.nih.gov/40045030)) and Mavroeidis 2025 ([PMID 40156874](https://pubmed.ncbi.nlm.nih.gov/40156874)) summarize the contemporary practice and note that dSDH-GIST patients typically need dose modification to 37.5 mg continuous within 2-3 cycles.

#### Likelihood of desired effect

Moderate at first measurable recurrence in this subset. The 18% ORR is directional, not a precise estimate; it sits well above the imatinib 2% floor but is mediocre against the trial-route ceiling some personas cited (rogaratinib NCT04595747 41.7% ORR, LITESPARK-015 PPGL adjacency at 26%). Useful for the chart note: this is not a primary play. It is the best-characterized fallback at recurrence when the dSDH-trial options either close, fill, or read negative.

#### Toxicity profile

- **Hand-foot skin reaction, hypothyroidism, fatigue, hypertension, skin discoloration** dominate the class AE picture — well-characterized with published management algorithms.
- **TSH q-cycle, BP optimization pre-start, dermatology baseline, dose-modification ladders to 37.5 mg continuous** are routine.
- **Hypothyroidism cumulative incidence rises with exposure duration** — chronic monitoring needed, not difficult.
- **Most dSDH-GIST patients need dose modification within 2-3 cycles** — plan for this as the rule rather than the exception.
- **Cumulative chronic AE burden on the natural-history timescale** (often multi-year if responsive) is the underweighted concern in the round-1 rationale. Younger dSDH-GIST patients accumulate years of exposure.

#### Counter-productive mechanisms / dissent

Conservative, critic, concensusite all ranked sunitinib at 3 with explicit 'NOT adjuvant today' framing; advocate placed it at 5 to formalize the contingency-only positioning. The risktaker dissented in their position notes: at 18% ORR in dSDH-GIST, sunitinib is a fallback after the high-effect-size trial picks fail or close, not a primary play. The advocate's round-2 critique on the conservative and critic rank-3 placements raised the same preference-fit tension: prefers_trials defaults to true, and at recurrence the sunitinib path should be presented alongside the trial route (PEMIGIST, LITESPARK-015 wt-GIST, NCT05661643 temozolomide) rather than ahead of it. The critic's round-2 push was a directional caveat — the Boikos 18% has no confidence interval and the dSDH subset in the pivotal phase 3 is minimally represented, so the chart note should say so. Conservative's round-2 operational note: build 37.5 mg continuous into the contingency plan as the anticipated trajectory.

#### Practical considerations

- **Initiation trigger:** RECIST 1.1 measurable disease on imaging, NOT rising ctDNA alone. The board consensus on this is explicit and goes in the chart note.
- **Schedule choice:** start at 50 mg 4-on/2-off per label; dose-modify to 37.5 mg continuous within the first 2-3 cycles in most dSDH-GIST patients.
- **Sequencing at recurrence:** with prefers_trials defaulted to true, the trial-route options (belzutifan / TMZ / pemigatinib at ranks 7, 8, 9) should be evaluated as co-equal conversations rather than sequenced after sunitinib by reflex.
- **Monitoring:** TSH q-cycle, BP at every visit, derm review at baseline + at HFSR onset, LVEF surveillance per label.

#### Why this rank

Sunitinib is the best-characterized 2L systemic option for KIT/PDGFRA-WT GIST at recurrence, and Boikos 2016 puts it well above imatinib in this subset. The rank-6 placement reflects two things: (1) it is contingency-only — the patient is NED today, so sunitinib does not run today; and (2) with prefers_trials defaulted to true, the trial-route contingencies should be a co-equal conversation at the moment of recurrence rather than a downstream fallback. The risktaker's preference-fit dissent on this row pulls the agreement score down to 0.6.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Sunitinib (Demetri 2006 pivotal RCT in 2L GIST) | TTP HR 0.33 (p<0.0001); mTTP 27.3 vs 6.4 wks | Fatigue, diarrhea, skin discoloration, nausea; HFSR | [PMID 17046465](https://pubmed.ncbi.nlm.nih.gov/17046465) |
| Sunitinib in dSDH-GIST (Boikos 2016 NIH wt-GIST cohort) | 7/38 (18%) ORR in dSDH-GIST; 1/49 (2%) on imatinib comparator | Not the focus of the cohort report; class AEs as expected | [PMID 27011036](https://pubmed.ncbi.nlm.nih.gov/27011036) |
| Sunitinib sequencing review (Dedousis 2025) | dSDH-GIST 2L → 3L → 4L TKI backbone | Cumulative class AE burden on multi-year exposure | [PMID 40045030](https://pubmed.ncbi.nlm.nih.gov/40045030) |

### Rank 7. Belzutifan 120 mg PO daily on LITESPARK-015 wt-GIST cohort (NCT04924075) — contingency at first measurable recurrence

*Conditional on `sdh_confirmed:positive`. Foreclosed if SDHB IHC stays intact after a clean re-stain and SDHA IHC also reads as retained.*

#### Evidence base

Selak 2005 ([PMID 15652751](https://pubmed.ncbi.nlm.nih.gov/15652751), Cancer Cell) is the foundational biology: SDH inhibition raises intracellular succinate to mM concentrations, succinate competitively inhibits the α-KG-dependent prolyl hydroxylases that tag HIF-1α/2α for VHL-mediated degradation, and HIF-2α stabilizes in normoxic cells (pseudohypoxia). The drug-mechanism story runs through Chen 2016 (PMID 27595394, Nature — PT2399 in VHL-null ccRCC PDX, 56% growth suppression) and Wehn 2019 (PMID 31062976, J Med Chem — PT2977/belzutifan medicinal chemistry from PT2385). Bayley 2022 ([PMID 35324464](https://pubmed.ncbi.nlm.nih.gov/35324464), Endocrine-Related Cancer) is the closest mechanism-matched in-vivo readout: belzutifan reduced tumor growth in an Sdhb-knockout pheochromocytoma allograft. LITESPARK-015 PPGL cohort returned ORR 26%, DCR 85%, mPFS 22 mo — the closest human adjacency. The wt-GIST cohort has no published readout yet.

#### Likelihood of desired effect

Frame the likelihood assuming the positive branch — SDHB IHC loss confirmed (or SDHA IHC loss locking in the SDHA-driven dSDH-GIST phenotype). PPGL ORR 26% is a fair adjacency on the succinate-HIF-2 biology but does not transport quantitatively to GIST. The wt-GIST cohort interim readout (most likely at ASCO 2026 / WCGIC) is the live question. A negative test forecloses this rec entirely — most dSDH-GIST trials use SDHB-IHC loss as the entry phenotype.

#### Toxicity profile

- **Anemia and hypoxia at the EPO-suppression target are dose-limiting in roughly 25-30%** of treated patients in the broader belzutifan dataset.
- **Roux-en-Y reconstruction compounds the anemia management problem** — iron and B12 absorption are already compromised post-gastrectomy, and EPO suppression on top of that is a stacked hit. Baseline Hgb / iron / B12 documented before enrollment, and a Hgb floor for dose-hold written into the protocol-deviation conversation.
- **Post-marketing surveillance is in the ~5-year window** since the August 2021 VHL approval — at the low end of long-tail safety follow-up for a chronic oral.

#### Counter-productive mechanisms / dissent

Risktaker rank 2, critic rank 5 (trial-watch), concensusite rank 5 (bundled with TMZ and pemigatinib in the trial-route tier), advocate implicit endorsement via 'preserves every future option.' Three round-2 qualifications stack but no formal dissent: conservative on toxicity (anemia/hypoxia compounded by Roux-en-Y is the stacked hit), advocate on preference fit (preferences are defaulted; the AE counseling gestured at in the rationale needs to be on the consent form), critic on evidence quality (PPGL ORR 26% does not transport to GIST as a quantitative effect estimate; single-arm open-label phase-2 with ORR endpoint will not generate OS data). With DFF332 ([NCT04895748](https://clinicaltrials.gov/study/NCT04895748)) terminated February 2026 and NKT-2152 discontinued, belzutifan is the sole active HIF-2α option — a negative wt-GIST readout would close the modality entirely with no successor.

#### Practical considerations

- **Geography:** 14 US sites recruiting. Better operational footprint than PEMIGIST (DFCI single-site) or NCT05661643 (Asan).
- **Eligibility:** requires measurable disease at recurrence (RECIST 1.1) AND pathologist-confirmed dSDH phenotype. The IHC re-cut + SDHA arbitration from the rank-1 workup is the gating step.
- **Baseline workup before enrollment:** Hgb, iron studies, B12, ferritin documented. Pre-emptive iron / B12 replacement plan if Roux-en-Y absorption is borderline.
- **Watch-for-data:** ASCO 2026 / WCGIC for the wt-GIST cohort interim cut. A positive readout shifts this rec higher; a negative readout drops the row entirely.

#### Why this rank

Belzutifan ranks above the temozolomide and pemigatinib trial-route options because the mechanism case is the cleanest in the dossier (Selak 2005 → Bayley 2022 → LITESPARK-015 PPGL adjacency) and the geography (14 US sites) is the most accessible. Below sunitinib because sunitinib has registration-grade RCT evidence and does not require dSDH phenotype confirmation; belzutifan's GIST signal is pre-readout. Three qualified critiques (not formal dissents) keep this honest about the cross-tumor transport uncertainty and the Roux-en-Y anemia complication.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Belzutifan LITESPARK-015 wt-GIST cohort (NCT04924075) | Pre-readout for wt-GIST; PPGL cohort ORR 26%, DCR 85%, mPFS 22 mo as adjacency | Anemia / hypoxia dose-limiting in 25-30% on broader dataset | [NCT04924075](https://clinicaltrials.gov/study/NCT04924075), [PMID 15652751](https://pubmed.ncbi.nlm.nih.gov/15652751), [PMID 35324464](https://pubmed.ncbi.nlm.nih.gov/35324464), [PMID 27595394](https://pubmed.ncbi.nlm.nih.gov/27595394) |

### Rank 8. Temozolomide on NCT05661643 (Asan) or NCT03556384 (UCSD, watch-for-readout); off-label generic TMZ with MGMT methylation as enrichment lever — contingency at first measurable recurrence

*Conditional on `sdh_confirmed:positive`. Foreclosed if SDHB IHC stays intact and SDHA IHC reads as retained.*

#### Evidence base

Yebra 2022 ([PMID 34426440](https://pubmed.ncbi.nlm.nih.gov/34426440), Clin Cancer Res, Sicklick lab at UCSD) is the load-bearing clinical readout in this subset: 5 SDH-mutant GIST patients on low-dose continuous TMZ (85 mg/m² d1-21 q28d), 2/5 PR, 100% disease control rate, mOS 1.9 years from TMZ start. Exact binomial 95% CI on 2/5 PR runs roughly 5-85%, so the point estimate is uninformative at that sample size; the load-bearing claim is mechanism coherence — patient-derived dSDH-GIST PDX models recapitulated parent-tumor biology and showed on-target alkylator damage while imatinib / sunitinib / regorafenib arms produced no growth inhibition. Flego 2024 ([PMID 38132569](https://pubmed.ncbi.nlm.nih.gov/38132569)) and Giger 2022 ([PMID 36198483](https://pubmed.ncbi.nlm.nih.gov/36198483)) identify MGMT promoter methylation as a candidate response biomarker enriched in ~24% of dSDH-GIST tumors. The cautionary mechanism-coherent precedent is Ligon 2023 guadecitabine ([PMID 36302175](https://pubmed.ncbi.nlm.nih.gov/36302175)) which returned 0/9 across the wt-GIST + PPGL + HLRCC cohorts — global hypomethylator on a hypermethylator phenotype, hard negative.

#### Likelihood of desired effect

Framed for the positive branch (dSDH phenotype confirmed). Low-to-moderate. The Yebra 2022 2/5 PR is uninformative at n=5; the mechanism rationale is the load-bearing argument and the Ligon 2023 negative readout in a closely-related mechanism-coherent design is the disconfirming precedent. NCT03556384 (UCSD, active-not-recruiting, primary completion June 2025) is the readout that will reframe the case-series 2/5 from anecdote to phase-2 data. MGMT-methylated status enriches the response-probability case but is not gating.

#### Toxicity profile

- **MDS / AML long-tail at ~1% with cumulative TMZ exposure beyond 6-12 months** — chronic safety signal that accrues on the natural-history timescale of dSDH-GIST. If the patient responds and stays on for years, the signal compounds.
- **Myelosuppression, nausea, fatigue** dominate the AE picture — class-known with published management algorithms.
- **TMZ PK after Roux-en-Y has not been formally studied** — raises a tolerability question for low-dose continuous dosing.
- **Pre-specified cumulative-exposure re-evaluation at 9-12 months** on therapy goes in the plan.

#### Counter-productive mechanisms / dissent

Conservative rank 5, risktaker rank 3 (highest enthusiasm), critic rank 7 (trial-watch with explicit CI framing), concensusite rank 5 (bundled). The critic's round-2 dissent on the risktaker's framing was sharp: 2/5 PR with no CI is not a 40% ORR estimate, and the rationale invoking 100% DCR at n=5 in an indolent natural-history setting brushes past the Ligon 2023 cautionary readout. Conservative's round-2 qualification on the concensusite pick added the MDS / AML chronic-exposure conversation. Advocate's round-2 critique on the concensusite bundling of three trials into one rank was that Asan-only TMZ, DFCI-only pemigatinib, and 14-US-site belzutifan are three different feasibility stories that should not share a rank.

#### Practical considerations

- **Geography:** NCT05661643 is Korea-only (Asan Medical Center, Seoul). Travel feasibility is the operational gate.
- **NCT03556384 (UCSD)** is active-not-recruiting — not an enrollment path, but the readout (primary completion June 2025) will reframe the case-series 2/5 from anecdote to phase-2 data.
- **Off-label US route:** order MGMT methylation on archival FFPE now (Mayo Clinic Laboratories MGMTM assay, or Quest / Labcorp / NeoGenomics equivalents) so the prior-auth packet is ready at recurrence. MGMT-methylated status is the response-probability lever and the prior-auth lever.
- **Schedule choice:** Yebra 2022 used 85 mg/m² d1-21 q28d (low-dose continuous); Asan uses 200 mg/m² d1-5 q28d (high-dose intermittent). Cytopenia and MDS risk profile differs by schedule.
- **Documentation:** baseline CBC and marrow reserve before initiation. Pre-specified cumulative-exposure re-evaluation point (9-12 months).

#### Why this rank

Temozolomide ranks below belzutifan because the human evidence base is n=5 with a wide CI and the Ligon 2023 negative precedent (closely-related mechanism-coherent design) is the disconfirming anchor. Above pemigatinib because the parent-drug safety profile is mature (20 years of post-marketing surveillance in glioblastoma) and the MGMT-methylation enrichment biomarker is the operational lever neither belzutifan nor pemigatinib has. NCT03556384 readout (June 2025 primary completion) is the inflection that could move this row up.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| TMZ in dSDH-GIST (Yebra 2022 mini-cohort) | 2/5 PR (40%, 95% CI ~5-85%); 100% DCR; mOS 1.9 yr from TMZ start | Per-AE table not published; cytopenia / fatigue / nausea presumed | [PMID 34426440](https://pubmed.ncbi.nlm.nih.gov/34426440) |
| TMZ trial NCT05661643 (Asan, recruiting) | Pre-readout | Schedule: 200 mg/m² d1-5 q28d | [NCT05661643](https://clinicaltrials.gov/study/NCT05661643) |
| TMZ trial NCT03556384 (UCSD, active-not-recruiting, watch-for-readout) | Primary completion June 2025; readout not yet public | Schedule: 85 mg/m² d1-21 q28d | [NCT03556384](https://clinicaltrials.gov/study/NCT03556384) |
| MGMT methylation enrichment (Flego 2024, Giger 2022) | Hypermethylation in ~24% of dSDH-GIST; predictive biomarker rationale | n/a — descriptive biomarker | [PMID 38132569](https://pubmed.ncbi.nlm.nih.gov/38132569), [PMID 36198483](https://pubmed.ncbi.nlm.nih.gov/36198483) |
| Guadecitabine (Ligon 2023, cautionary mechanism-coherent precedent) | 0/9 across cohorts; trial closed for low accrual | G3+ neutropenia treatment-limiting in 2/9 | [PMID 36302175](https://pubmed.ncbi.nlm.nih.gov/36302175) |

### Rank 9. Pemigatinib on PEMIGIST (NCT07434843, DFCI single-site, Suzanne George) — contingency at first measurable recurrence

*Conditional on `sdh_confirmed:positive`. Foreclosed if dSDH phenotype not pathologist-confirmed at trial screening.*

#### Evidence base

Flynn 2025 AACR abstract CT215 (doi:[10.1158/1538-7445.AM2025-CT215](https://doi.org/10.1158/1538-7445.AM2025-CT215)) showed tumor regression in an SDH-deficient GIST PDX where sunitinib and regorafenib were essentially ineffective. The mechanism: genome-wide DNA hypermethylation in dSDH-GIST (Killian 2013 [PMID 23550148](https://pubmed.ncbi.nlm.nih.gov/23550148); Killian 2014 [PMID 25540324](https://pubmed.ncbi.nlm.nih.gov/25540324)) disrupts CTCF-bound chromatin insulators, leading to aberrant FGF3 / FGF4 transcription that signals through FGFR1 (and FGFR4) as an autocrine driver. The cited human bridge is rogaratinib (NCT04595747, n=24) at ORR 41.7% with 31-month median PFS — exact binomial 95% CI on 10/24 runs roughly 22-63%. NCT07434843 itself is n=24 single-arm phase 2 and will hit the same statistical wall.

#### Likelihood of desired effect

Framed for the positive branch. Low-to-moderate. The rogaratinib bridge is the strongest preclinical-to-clinic translation signal in dSDH-GIST so far but n=24 with wide binomial CI is not a stable point estimate. The pemigatinib trial design will not resolve that wall on its own.

#### Toxicity profile

- **Serous retinal detachment in roughly 25% of treated patients** on the FGFR-inhibitor class (pemigatinib FIGHT-202 cholangiocarcinoma program plus infigratinib bladder data) — requires baseline OCT + monthly OCT through the first 6 months.
- **Hyperphosphatemia approaching 60% all-grade** — requires weekly phosphate during titration and a phosphate-binder management plan.
- **Nail and mucosal toxicity** drive dose holds; dermatology partner is part of the order set.

#### Counter-productive mechanisms / dissent

Risktaker rank 1 (their highest-conviction trial-route bet); critic rank 6 (trial-watch); concensusite rank 5 (bundled in trial-route tier). **Two formal round-2 dissents stack on the rank-1 framing:** advocate dissent on preference-fit grounds (DFCI single-site is a logistics burden for a patient whose geography hasn't been elicited; AE counseling on serous retinal detachment and hyperphosphatemia is missing from the rationale) and critic dissent on evidence-quality grounds (one PDX in an AACR abstract plus a rogaratinib sister-drug readout at n=24 with wide binomial CI does not anchor a rank-1 pick — the rationale calls it the strongest preclinical-to-clinic translation and overstates what the evidence supports). Conservative's round-2 qualification added a chronic-toxicity conditional ask: OCT baseline + monthly OCT through first 6 months and weekly phosphate during titration in the order set. Status is considered_with_caveats per the two formal dissents.

#### Practical considerations

- **Geography:** DFCI single-site is a hard operational constraint. Suzanne George (DFCI Sarcoma Center) is the contact and the logical referral path; for non-Boston-area patients, this is travel-dependent.
- **Trial design:** n=24 single-arm phase 2 won't generate a long-tail safety dataset on the timescale a non-trial off-label decision would need.
- **Monitoring order set:** baseline OCT, monthly OCT through first 6 months, weekly phosphate during titration, phosphate-binder management plan, dermatology partner.
- **Off-label pemigatinib is hard to justify outside the trial:** the patient has no canonical FGFR fusion or rearrangement, and the FGF3/4 overexpression rationale is not a companion-diagnostic finding any payer accepts on first pass.

#### Why this rank

Below belzutifan and TMZ because the evidence pyramid is the shallowest (one PDX abstract + one sister-drug n=24 trial), the AE class is the most monitoring-intensive, and two formal dissents stack on rank-1 framing. Above regorafenib because the preclinical signal is more direct (dSDH-GIST PDX, not by extrapolation) and the trial is recruiting in a feature-targeting setting that regorafenib does not address.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Pemigatinib PEMIGIST (NCT07434843, DFCI) | Pre-readout; n=24 single-arm phase 2; opened April 2026 | FGFR class: serous retinal detachment ~25%, hyperphosphatemia ~60% | [NCT07434843](https://clinicaltrials.gov/study/NCT07434843) |
| Rogaratinib bridge (NCT04595747, sister FGFR program) | ORR 41.7% at n=24 (95% CI ~22-63%); mPFS 31 mo | Same FGFR class profile | doi:[10.1158/1538-7445.AM2025-CT215](https://doi.org/10.1158/1538-7445.AM2025-CT215) |
| Pemigatinib dSDH-GIST PDX (Flynn 2025 AACR abstract) | Tumor regression where sunitinib / regorafenib failed; FGF3/4-FGFR1 axis | n/a (preclinical) | doi:[10.1158/1538-7445.AM2025-CT215](https://doi.org/10.1158/1538-7445.AM2025-CT215) |

### Rank 10. Regorafenib 160 mg PO 3-on/1-off — 3L contingency at sunitinib progression

*Standard-of-care anchor for advanced GIST 3L. dSDH-GIST activity by extrapolation.*

#### Evidence base

Demetri 2013 GRID ([PMID 23177515](https://pubmed.ncbi.nlm.nih.gov/23177515), Lancet, RoB2:Low, n=199, 2:1 randomization): BICR median PFS 4.8 vs 0.9 mo, PFS HR 0.27 (95% CI 0.19-0.39, p<0.0001). Registration-grade 3L GIST. The dSDH-GIST subset was minimally represented; activity in this subtype runs through the Dedousis 2025 review ([PMID 40045030](https://pubmed.ncbi.nlm.nih.gov/40045030)) qualitative narrative ('modest, similar to KIT-mutant 3L'), not a published subset analysis with a confidence interval.

#### Likelihood of desired effect

Low-to-moderate in dSDH-GIST. GRID PFS HR 0.27 is registration-grade in the overall (predominantly KIT-mutant) population; transport to dSDH-GIST is by extrapolation rather than subset evidence.

#### Toxicity profile

- **G3+ hypertension 23%** (31/132) — pre-treatment BP optimization saves cycles 1-2.
- **G3+ hand-foot skin reaction 20%** (26/132) — pre-treatment dermatology baseline.
- **G3+ diarrhea 5%** (7/132).
- **Dose modifications are the rule rather than the exception** in real-world use.

#### Counter-productive mechanisms / dissent

Critic rank 4, concensusite rank 4. **Advocate filed a round-2 dissent on preference-fit grounds:** prefers_trials defaults to true, and putting regorafenib ahead of the trial-route options sequences a registration-grade TKI ahead of the patient's defaulted trial preference. By the time the patient progresses on sunitinib, the dSDH-GIST trial landscape will likely have moved (concensusite's own rationale notes this), and the right move at 3L should be a fresh trial-landscape review rather than a reflex rotation to regorafenib. Critic's round-2 qualification noted that the Dedousis 2025 review's 'modest activity' claim is qualitative narrative, not a published subset analysis with a confidence interval — the evidence pyramid for regorafenib in this molecular subtype is RCT-in-different-population plus expert-narrative, not RCT-in-population. Status is considered_with_caveats per the advocate's formal dissent.

#### Practical considerations

- **Sequencing:** standard contingency stack reads sunitinib → regorafenib → trial or ripretinib. At 3L, the dSDH-GIST trial portfolio (PEMIGIST / LITESPARK-015 / NCT05661643) should be re-evaluated as the live alternative to regorafenib.
- **Initiation workup:** baseline BP, dermatology baseline, LFTs, TSH, ECG.
- **Dose modifications:** plan for 120 mg or 80 mg as routine de-escalation steps; published management algorithms apply.
- **Ripretinib at 4L** (Mavroeidis 2025 [PMID 40156874](https://pubmed.ncbi.nlm.nih.gov/40156874)) carries the weakest dSDH-GIST evidence base of the three post-imatinib TKIs because INVICTUS enrolled vanishingly few wt-GIST patients — by the time it gets reached for, the trial landscape will have shifted again.

#### Why this rank

Regorafenib ranks below the dSDH-specific trial options because the dSDH-GIST evidence base is by extrapolation rather than subset evidence and prefers_trials defaults to true. Above the late-line PARP combination at rank 11 because the registration-grade RCT anchor is real even with the subset transport caveat. The advocate's preference-fit dissent pulls the agreement score to 0.2.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Regorafenib (GRID pivotal RCT, 3L GIST) | mPFS 4.8 vs 0.9 mo; PFS HR 0.27 (95% CI 0.19-0.39); p<0.0001 | G3+ hypertension 23%, G3+ HFSR 20%, G3+ diarrhea 5% | [PMID 23177515](https://pubmed.ncbi.nlm.nih.gov/23177515) |
| Regorafenib sequencing in dSDH-GIST (Dedousis 2025 review) | 'Modest activity, similar to KIT-mutant 3L' (narrative, no CI) | Same class profile | [PMID 40045030](https://pubmed.ncbi.nlm.nih.gov/40045030) |
| Ripretinib INVICTUS pivotal (4L+ GIST anchor; weakest dSDH evidence) | mPFS 6.3 vs 1.0 mo; PFS HR 0.15; mOS 15.1 vs 6.6 mo | G3+ lipase 5%, G3+ hypertension 4%, fatigue 2% | [PMID 32511981](https://pubmed.ncbi.nlm.nih.gov/32511981), [PMID 40156874](https://pubmed.ncbi.nlm.nih.gov/40156874) |

### Rank 11. Olaparib 300 mg PO BID + temozolomide — late-line / post-trial-exhaustion contingency; trial-route only with hematology co-management

*Conditional on `sdh_confirmed:positive` AND on prior contingencies being exhausted. Conservative veto stands on off-label cash-pay default; overridden to a bounded trial-route framing.*

#### Evidence base

Sulkowski 2018 ([PMID 30013182](https://pubmed.ncbi.nlm.nih.gov/30013182), Nat Genet) and Sulkowski 2020 ([PMID 32494005](https://pubmed.ncbi.nlm.nih.gov/32494005), Nature) build the mechanism case. Succinate and fumarate competitively inhibit the α-KG-dependent KDM4A/B histone lysine demethylases. The resulting aberrant H3K9 trimethylation at DSB sites blocks recruitment of the homologous-recombination machinery (53BP1, BRCA1, RAD51). HR is locked out at chromatin even though the HR proteins themselves are intact. PARP-trapping inhibitors push the cell past the synthetic-lethal threshold — a BRCA-like phenotype without a BRCA mutation. The xenograft arm (talazoparib in SDHB-knockdown cells) showed significant tumor-growth inhibition relative to isogenic controls. Singh 2023 ([PMID 36151992](https://pubmed.ncbi.nlm.nih.gov/36151992), Pediatr Blood Cancer) is one patient — multiply-relapsed dSDH-GIST + paraganglioma — with a durable clinical response on the combination. n=1 published case plus a tight mechanism stack is the entire clinical evidence base.

#### Likelihood of desired effect

Low at the population level. Singh 2023 is n=1; the Sulkowski work establishes the synthetic-lethal logic at chromatin but has no replicated clinical readout in dSDH-GIST. The mechanism case is the strongest reason to keep this on the page; the absence of a replicated human signal is why it sits at rank 11.

#### Toxicity profile

- **Overlapping cytopenias from PARP-trapping + alkylator** are not just additive — published OlympiA-style olaparib AML/MDS rates of ~1.2% rise sharply when the partner is itself genotoxic.
- **TMZ carries its own ~1% MDS / AML long-tail at cumulative exposure beyond 6-12 months.** The two together in a sustained-response scenario is exactly the chronic exposure where the MDS / AML signal compounds.
- **No published combination safety dataset in dSDH-GIST** to anchor a management algorithm.
- **Off-label cash-pay** PARP-plus-alkylator is ~$17K/month olaparib if appeal fails — the operational cost is meaningful even before the safety conversation.

#### Counter-productive mechanisms / dissent

Risktaker rank 4 — their own characterization: 'the weakest in this position.' **Conservative round-2 dissent + conditional veto** on toxicity and evidence-quality grounds: n=1 cannot adjudicate the combination's chronic-toxicity profile; the MDS/AML signal compounds across PARP + alkylator in sustained-response scenarios; off-label cash-pay use without baseline marrow assessment, without trial structure, and without a pre-specified cumulative-exposure stopping rule is not signable. Critic round-2 qualification: mechanism work is real and tight, but the n=1 caveat must travel forward so the row is not cited as 'durable response in dSDH-GIST' downstream. **Status is considered_with_caveats with the conservative veto OVERRIDDEN** to the bounded framing the conservative explicitly accepted: late-line, post-trial-exhaustion only, trial-route or compassionate-use only, hematology co-management with baseline marrow assessment, pre-specified 9-12 month cumulative-exposure re-evaluation. In the off-label cash-pay default framing, the conservative veto stands.

#### Practical considerations

- **Bounded framing only:** late-line, post-trial-exhaustion (sunitinib + belzutifan/TMZ/pemigatinib trials + regorafenib all exhausted), trial-route or compassionate-use, hematology co-management.
- **Baseline marrow assessment** documented before initiation; pre-specified 9-12 month cumulative-exposure re-evaluation point written into the plan.
- **No active trial of the combination in dSDH-GIST** currently registered. Natural sponsors would be the NIH wt-GIST clinic or DFCI; the row stays on file as the mechanism-supported late-line option if the trial portfolio at recurrence has been worked through.
- **Investigator-initiated route** through the NCI Pediatric & wt-GIST Clinic (registry enrollment at rank 3 is the door) is the most plausible operational path.

#### Why this rank

Mechanism-strong, evidence-thin, and chronically toxic in the sustained-response scenario. Belongs on the page because the SDH-loss / HR-defect biology is one of the cleanest synthetic-lethal stories in this subset and the Singh 2023 case is the only human readout. Belongs at rank 11 because the conservative veto in the off-label cash-pay framing is unambiguous and the override only applies to bounded use that may not be practically available.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Olaparib + TMZ in dSDH-GIST (Singh 2023 case) | Durable clinical response (n=1, multiply-relapsed) | Per-AE not reported (letter format) | [PMID 36151992](https://pubmed.ncbi.nlm.nih.gov/36151992) |
| SDH-loss HR-defect mechanism (Sulkowski 2018 / 2020) | Talazoparib growth inhibition in SDHB-knockdown xenograft | Preclinical | [PMID 30013182](https://pubmed.ncbi.nlm.nih.gov/30013182), [PMID 32494005](https://pubmed.ncbi.nlm.nih.gov/32494005) |

## Classes examined but not ranked

- **Linsitinib (IGF-1R/IR inhibitor).** Hard negative phase 2 in dSDH-GIST: von Mehren 2020 ([PMID 31792037](https://pubmed.ncbi.nlm.nih.gov/31792037)) returned 0/20 ORR in the SARC wt-GIST cohort despite the IGF1R-overexpression rationale (Belalcazar 2013 [PMID 23046288](https://pubmed.ncbi.nlm.nih.gov/23046288); Lasota 2013 88% IHC positivity). The 40% 9-month clinical-benefit rate overlaps the natural-history indolence of dSDH-GIST and is uninformative for drug activity. Closes IGF-1R inhibition as a strategy in this subset.
- **Guadecitabine (DNA hypomethylating agent).** Hard negative phase 2: Ligon 2023 ([PMID 36302175](https://pubmed.ncbi.nlm.nih.gov/36302175)) returned 0/9 objective responses across the wt-GIST + PPGL + HLRCC cohorts. Trial closed for low accrual before reaching its 70-patient target. The Killian 2013 / 2014 mechanism papers ([PMID 23550148](https://pubmed.ncbi.nlm.nih.gov/23550148), [PMID 25540324](https://pubmed.ncbi.nlm.nih.gov/25540324)) established the dSDH-GIST hypermethylator phenotype as biologically real; the clinical-vs-mechanism disconnect on global hypomethylators is the cautionary precedent that travels with temozolomide at rank 8.
- **DFF332 / NKT-2152 (next-gen HIF-2α inhibitors).** Both discontinued in 2025-2026 for business reasons; the DFF332 SDHx-mutation expansion arm 1B never opened ([NCT04895748](https://clinicaltrials.gov/study/NCT04895748) terminated February 2026). Leaves belzutifan as the sole active HIF-2α option.
- **Alpelisib / inavolisib / tersolisib (PI3Kα inhibitors).** Gated on tissue confirmation of the ctDNA-only PIK3CA R93W. R93W sits outside the validated alpelisib companion-diagnostic hotspots (E542K, E545K, H1047R, C420R) and Burke 2012 ([PMID 22949673](https://pubmed.ncbi.nlm.nih.gov/22949673)) biochemistry classifies the ABD-domain class as weakly activating. Cross-tumor extrapolation from SOLAR-1 and INAVO120 is blocked by both the histology mismatch and the non-canonical variant. The rank-1 tissue NGS reveals whether the variant confirms; even if it does, the path forward is sponsor-by-sponsor variant-eligibility check at a basket trial ([NCT05768139](https://clinicaltrials.gov/study/NCT05768139) tersolisib), not borrowing breast-cancer effect sizes.
- **Trametinib / cobimetinib / binimetinib (MEK inhibitors) on MAP2K1 P124S.** Gated on tissue confirmation of the ctDNA-only call. Gao 2018 ([PMID 36442478](https://pubmed.ncbi.nlm.nih.gov/36442478)) classifies P124 as a class-I RAF-dependent activator with retained MEK-inhibitor sensitivity in vitro, and Wagle 2014 ([PMID 24265154](https://pubmed.ncbi.nlm.nih.gov/24265154)) frames P124 as a partial-activator α-C-helix variant. Cross-tumor precedent is anecdotal (Gounder 2018 [PMID 26222557](https://pubmed.ncbi.nlm.nih.gov/26222557) histiocytic sarcoma F53L case; Andritsos 2017 hairy cell K57N — both class-I but cross-class and cross-tumor). MEGALiT cobimetinib arm ([NCT04185831](https://clinicaltrials.gov/study/NCT04185831)) is active-not-recruiting; NCT06739395 MAP2K1 arm is in a Chinese consortium with geography blockers. Stays off the ranked list pending tissue confirmation and a sponsor-by-sponsor enrollment conversation.
- **Pembrolizumab (tumor-agnostic ICI).** Foreclosed by MSS + TMB <1 mut/Mb (KEYNOTE-158 thresholds: MSI-H or TMB ≥10). The POLE R1679C germline variant does not transport the standard hypermutator-ICI rationale — it sits outside the canonical proofreading hotspots (P286R, V411L, S459F) and the patient phenotype (TMB <1, MSS) is the opposite of the ultramutated phenotype that drives the published response data.

## Ranked prioritization

### Shared workup (gates trial-route contingencies)

| Rank | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
|---|---|---|---|---|---|
| 1 | **SDHA germline panel + SDHA/SDHB IHC re-cut + tumor-tissue NGS bundle**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | Diagnostic certainty — locks the dSDH-GIST driver call, resolves the SDHB-intact paradox, and gates the three dSDH-GIST trials at recurrence. | Low (none — germline blood draw + IHC re-cut on archival FFPE + comprehensive tumor NGS panel) | **N/A** (Diagnostic, not therapeutic — no mechanism-level risk to the therapeutic goal.) | **Non-therapeutic workup that resolves the SDHB-intact / SDHA-biallelic paradox and locks in trial-screener eligibility before any contingency is reached for.** |

### Unified ranking (active management today + recurrence contingency)

| Rank | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
|---|---|---|---|---|---|
| 2 | **Active surveillance — structured imaging q3-6 mo, no adjuvant systemic therapy**<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | Effect is option preservation. Cross-society guideline convergence + Boikos 2016 (1/49 PR on imatinib) close the door on adjuvant systemic therapy in this molecular subset. | Low (none — imaging surveillance has no AE profile; soft cost is scan anxiety, not characterized in any toxicity table) | **N/A** (Non-therapeutic management pathway — no mechanism-level risk to a therapeutic goal.) | **The right answer today and the call cross-society guidelines explicitly make; every contingency below this row depends on not burning option space now.** |
| 3 | **NCI Rare Tumor Natural History Study (NCT03739827) + cancer-genetics counseling**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | High infrastructure value — unlocks SDHC methylation fallback, biospecimen banking, NIH wt-GIST clinic follow-up, and family cascade-testing path. | Low (none — registry enrollment + counseling visit; one in-person NIH baseline) | **N/A** (Infrastructure, not therapy — no mechanism-level risk to a therapeutic goal.) | **The highest yield-per-cost move on the page — zero-toxicity registry access plus genetics counseling that unlocks every downstream option.** |
| 4 | **Paraganglioma / pheochromocytoma baseline surveillance (plasma metanephrines + WB-MRI)**<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | Patient-safety floor — establishes clean PGL/PCC baseline and the anesthesia-safety screen required before any future elective surgery in an SDHx carrier. | Low (none — imaging + blood draw; minimal radiation if MRI-first, DOTATATE deferred) | **N/A** (Non-therapeutic surveillance — no mechanism-level risk to a therapeutic goal.) | **Standard SDHx-carrier surveillance — anesthesia-safety floor and a clean comparator baseline for the recurrence-monitoring strategy.** |
| 5 | **Signatera tumor-informed ctDNA MRD (imaging adjunct, not therapy-triggering)**<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small> | Lead-time signal ahead of imaging — informative for recurrence monitoring; weaker prospective GIST validation than colorectal/lung MRD data. | Low (none — venipuncture; FFPE block re-use for baseline build) | **Low** (False-positive ctDNA without imaging correlate could drive premature TKI initiation; imaging-gating guardrail is the mitigation.) | **Adjunct to imaging surveillance with a clear guardrail — a positive Signatera prompts shorter-interval imaging, not systemic therapy.** |
| 6 | **Sunitinib 50 mg PO 4-on/2-off (or 37.5 mg continuous) — at measurable recurrence, NOT adjuvant**<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-risktaker">risktaker</span></small> | Moderate at first measurable recurrence — Boikos 2016 dSDH-GIST 18% ORR (n=38 retrospective, no CI); Demetri 2006 registration-grade 2L GIST (TTP HR 0.33). | Moderate (HFSR, hypothyroidism, fatigue, hypertension — well-characterized chronic class AEs; published management algorithms apply) | **Low** (Class-effect VEGFR signaling withdrawal on chronic dosing; no mechanism-level dissent for THIS subset in the board's deliberation.) | **Best-characterized 2L TKI for KIT/PDGFRA-WT GIST; contingency-only at measurable recurrence, with the trial-route options as a co-equal conversation rather than a downstream fallback.** |
| 7 | **Belzutifan on LITESPARK-015 wt-GIST cohort (NCT04924075)** *(conditional on `sdh_confirmed:positive`)*<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | Moderate if dSDH phenotype confirms — PPGL adjacency (ORR 26%, mPFS 22 mo) does not quantitatively transport to GIST; cleanest mechanism case but no GIST efficacy readout yet. | Moderate (anemia and hypoxia dose-limiting in 25-30% on broader dataset; stacked anemia management problem in Roux-en-Y; ~5-year post-marketing surveillance) | **Low** (Cross-tumor mechanism transport from PPGL to GIST is the gating uncertainty — modality-level risk, not patient-AE risk.) | **Cleanest mechanism case for dSDH-GIST in the dossier — 14 US sites recruiting; cross-tumor transport from PPGL is the live question and Roux-en-Y anemia management is the patient-specific complication.** |
| 8 | **Temozolomide on NCT05661643 / NCT03556384 (or off-label with MGMT enrichment)** *(conditional on `sdh_confirmed:positive`)*<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small> | Low-to-moderate — Yebra 2022 2/5 PR (95% CI ~5-85%) is mechanism-coherent but uninformative at n=5; Ligon 2023 guadecitabine 0/9 is the cautionary precedent for mechanism-vs-clinic disconnect in this subset. | Moderate (myelosuppression, fatigue, nausea well-characterized; MDS/AML long-tail ~1% at cumulative exposure >6-12 months is the chronic signal) | **Moderate** (Critic dissented on the Yebra n=5 point-estimate framing; Ligon 2023 (guadecitabine 0/9) is the mechanism-coherent precedent where the hypomethylator/alkylator class disconnect already played out in this subset.) | **Mechanism-coherent contingency with mature parent-drug safety, but n=5 efficacy + the Ligon 2023 negative precedent argue for trial-route, MGMT-enriched, with a pre-specified cumulative-exposure stopping rule.** |
| 9 | **Pemigatinib on PEMIGIST (NCT07434843, DFCI single-site)** *(conditional on `sdh_confirmed:positive`)*<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>dissent:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-critic">critic</span></small> | Low-to-moderate — rogaratinib NCT04595747 41.7% ORR at n=24 (95% CI ~22-63%) is the cited bridge; pemigatinib NCT07434843 itself is n=24 single-arm phase 2 with no readout yet. | Moderate (FGFR-class: serous retinal detachment ~25%, hyperphosphatemia ~60% all-grade, nail/mucosal AEs; monitoring-intensive class) | **Moderate** (Critic and advocate dissented on evidence-pyramid narrowness and preference-fit; FGFR-class toxicity-as-monitoring-burden is the mechanism-adjacent concern.) | **Freshest mechanism story in the dossier with the strongest preclinical-to-clinic signal so far, but the evidence pyramid is shallow and two personas dissented on rank-1 framing.** |
| 10 | **Regorafenib 160 mg PO 3-on/1-off — 3L at sunitinib progression**<br><small><em>endorse:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>dissent:</em> <span class="persona persona-advocate">advocate</span></small> | Low-to-moderate in dSDH-GIST — GRID PFS HR 0.27 is registration-grade in KIT-mutant 3L; dSDH-subset activity is by extrapolation, no published subset CI. | Moderate (G3+ hypertension 23%, G3+ HFSR 20%, G3+ diarrhea 5%; dose modifications are the rule) | **Low** (Advocate dissent was preference-fit on sequencing against the trial-route, not on the mechanism.) | **Registration-grade 3L anchor with weak dSDH-GIST subset evidence; sequencing against the trial-route at 3L is the live preference question.** |
| 11 | **Olaparib + temozolomide — late-line, bounded trial-route / hematology-comanaged only** *(conditional on `sdh_confirmed:positive`)*<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span></small><br><small><em>dissent:</em> <span class="persona persona-critic">critic</span></small><br><small><em>veto:</em> <span class="persona persona-conservative">conservative</span></small> | Low for population-level effect — Singh 2023 is n=1; Sulkowski mechanism work is robust at chromatin level but no replicated clinical readout in dSDH-GIST. | High (overlapping PARP + alkylator cytopenias; cumulative MDS/AML risk on sustained exposure; no published combination safety dataset in dSDH-GIST) | **High** (Conservative veto stood on chronic-toxicity-as-mechanism: PARP + alkylator MDS/AML compounding in sustained-response scenarios is the mechanism-level risk to durable use.) | **Mechanism-strong, evidence-thin late-line contingency — acceptable only in bounded trial-route or hematology-comanaged framing; off-label cash-pay default is not signable.** |
| 12 | **Adjuvant imatinib — NOT RECOMMENDED**<br><small><em>veto:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span></small> | None in dSDH-GIST — Boikos 2016 1/49 (2%) PR on imatinib; adjuvant trials structurally excluded this subset. | High (3-year exposure: G2+ edema ~30%, fatigue ~50%, hepatic / cardiac monitoring burden) measured against a 2% PR rate — not a defensible tradeoff. | **High** (Both vetoes stood on mechanism + toxicity: imatinib insensitivity in dSDH-GIST plus chronic AE burden at the 2% PR floor; PERSIST-5 confirmed imatinib-insensitive genotypes recur regardless of treatment.) | **Logged as NOT RECOMMENDED so the reflex 'GIST equals imatinib' reach is documented and rejected on the record — every persona vetoed in concept.** |

!!! note "Reading the table"
    **Toxicity burden** is patient-level adverse-event severity. **Counter-productive MoA** is mechanism-level risk to the therapeutic goal — distinct from patient AEs and rated against board dissent on the mechanism, not on AE rates. The persona pills under each intervention are the at-a-glance board signal; per-persona rationale lives on the board page.

## Caveats

- **Evidence-base caveats.** The dSDH-GIST-specific clinical evidence base is thin across the board: Boikos 2016 (n=38 retrospective subgroup, ROBINS-I:Moderate, no CI on the 18% ORR) anchors the sunitinib call by extrapolation; Yebra 2022 (n=5 clinical cohort, ROBINS-I:Serious, exact 95% CI ~5-85% on 2/5 PR) anchors the temozolomide case; Flynn 2025 (one PDX in an AACR abstract not peer-reviewed at full-paper resolution; rogaratinib n=24 bridge with wide binomial CI) anchors the pemigatinib case; Singh 2023 (n=1 case report) anchors the olaparib + TMZ contingency. The registration-grade RCT evidence (Demetri 2006, Demetri 2013 GRID, Blay 2020 INVICTUS, Z9001 / SSGXVIII / PERSIST-5) was all built in populations where dSDH-GIST was either structurally absent or minimally represented. The LITESPARK-015 wt-GIST cohort has no published readout yet.
- **Compartment / biomarker dependencies.** Rankings assume SDHA germline panel + SDHA/SDHB IHC re-cut + tumor NGS confirmation will lock in the dSDH-GIST phenotype. If SDHB IHC reads as retained after a clean re-stain with positive internal control AND SDHA IHC also reads as retained, the dSDH-GIST label collapses and the trial-route contingencies at ranks 7, 8, 9, and 11 are foreclosed entirely. In that scenario the case has no within-scope trial-route recommendations targeting the gating feature; the systemic backbone (sunitinib then regorafenib) remains relevant for KIT/PDGFRA-WT GIST regardless of SDH status and should be pursued through the treating team's normal care channel, and the SDHC promoter methylation fallback assay (medium-priority on the validation paths report) becomes decision-relevant. The PIK3CA R93W and MAP2K1 P124S ctDNA-only calls are out-of-scope for ranking until they confirm in tissue; even if they confirm, R93W is biochemically classified as weakly activating and the alpelisib companion-diagnostic hotspots do not include it.
- **What would change the ranking.**
    - **Positive SDHA germline result** (constitutional carrier) tightens the lifetime PGL-surveillance cadence to biennial whole-body MRI and adds cascade testing for first-degree relatives. Does not change the ranking but makes the rank-4 PGL screen a lifelong commitment rather than a one-time baseline.
    - **NCT03556384 (UCSD temozolomide) readout** (primary completion June 2025) — a positive readout shifts the rank-8 temozolomide row up and could displace belzutifan at rank 7. A negative readout drops the row below the standard-care TKI contingencies.
    - **LITESPARK-015 wt-GIST cohort interim readout** (most likely ASCO 2026 / WCGIC) — positive readout shifts rank 7 up. Negative readout closes the modality entirely (DFF332 and NKT-2152 already discontinued) and the row drops to 'modality-closed' caveat.
    - **Tissue confirmation of PIK3CA R93W or MAP2K1 P124S** as clonal in tumor would reopen the PI3Kα or MEK inhibitor conversation, though R93W's non-canonical status keeps any PI3Kα consideration at a sponsor-by-sponsor variant-eligibility check rather than a label-driven option.
    - **Multifocal recurrence vs single-site oligometastatic recurrence** at first relapse — the latter may favor a re-resection conversation alongside systemic therapy that the contingency stack does not currently anticipate.
- **Re-scoping caveat.** The recommendation rests on a defaulted preferences set. If the patient signals a strong preference for "doing something" over surveillance, the registry visit and the Signatera baseline at ranks 3 and 5 are the cleanest active-but-non-toxic options; a real preferences elicitation including geography, scan-anxiety tolerance, travel willingness, and trial-route conviction should happen before any contingency is committed to. Geography in particular is load-bearing at recurrence — Asan (Korea), DFCI (Boston), and 14 LITESPARK-015 sites are three different feasibility stories.

## Sources

### PMIDs

- [PMID 15652751](https://pubmed.ncbi.nlm.nih.gov/15652751) — Selak 2005, Cancer Cell (succinate-PHD-HIF pseudohypoxia biology)
- [PMID 17046465](https://pubmed.ncbi.nlm.nih.gov/17046465) — Demetri 2006, Lancet (sunitinib pivotal 2L GIST)
- [PMID 19303137](https://pubmed.ncbi.nlm.nih.gov/19303137) — DeMatteo 2009, Lancet (ACOSOG Z9001 adjuvant imatinib)
- [PMID 21173220](https://pubmed.ncbi.nlm.nih.gov/21173220) — Janeway 2011, PNAS (SDH-deficient GIST as molecular entity)
- [PMID 22453568](https://pubmed.ncbi.nlm.nih.gov/22453568) — Joensuu 2012, JAMA (SSGXVIII adjuvant imatinib 36 vs 12 mo)
- [PMID 22949673](https://pubmed.ncbi.nlm.nih.gov/22949673) — Burke 2012, PNAS (PI3Kα ABD-domain biochemistry)
- [PMID 23023976](https://pubmed.ncbi.nlm.nih.gov/23023976) — Miettinen 2013 (SDHA IHC in SDHA-driven dSDH-GIST)
- [PMID 23046294](https://pubmed.ncbi.nlm.nih.gov/23046294) — Hornick 2013 (SDHB-IHC pitfall literature)
- [PMID 23177515](https://pubmed.ncbi.nlm.nih.gov/23177515) — Demetri 2013, Lancet (GRID regorafenib pivotal 3L GIST)
- [PMID 23459398](https://pubmed.ncbi.nlm.nih.gov/23459398) — Wagner 2013 (SDHA IHC reference)
- [PMID 23934599](https://pubmed.ncbi.nlm.nih.gov/23934599) — Endocrine Society / ENS@T PGL imaging reference
- [PMID 24265154](https://pubmed.ncbi.nlm.nih.gov/24265154) — Wagle 2014, Cancer Discov (MAP2K1 P124 αC-helix variant in melanoma resistance)
- [PMID 24893135](https://pubmed.ncbi.nlm.nih.gov/24893135) — plasma free metanephrines LC-MS/MS reference
- [PMID 26222557](https://pubmed.ncbi.nlm.nih.gov/26222557) — Gounder 2018, NEJM (trametinib in MAP2K1 F53L histiocytic sarcoma)
- [PMID 27011036](https://pubmed.ncbi.nlm.nih.gov/27011036) — Boikos 2016, JAMA Oncol (NIH wt-GIST cohort molecular subtypes)
- [PMID 27595394](https://pubmed.ncbi.nlm.nih.gov/27595394) — Chen 2016, Nature (PT2399 HIF-2α in VHL-null ccRCC PDX)
- [PMID 29413424](https://pubmed.ncbi.nlm.nih.gov/29413424) — Mei 2018, Trends Cancer (dSDH-GIST natural history)
- [PMID 30013182](https://pubmed.ncbi.nlm.nih.gov/30013182) — Sulkowski 2018, Nat Genet (SDH-loss HR-defect synthetic lethal)
- [PMID 30383140](https://pubmed.ncbi.nlm.nih.gov/30383140) — Raut 2018, JAMA Oncol (PERSIST-5 5-year adjuvant imatinib)
- [PMID 31062976](https://pubmed.ncbi.nlm.nih.gov/31062976) — Wehn 2019, J Med Chem (PT2977/belzutifan medicinal chemistry)
- [PMID 31369093](https://pubmed.ncbi.nlm.nih.gov/31369093) — Endocrine Society 2014 PGL imaging guidance
- [PMID 31792037](https://pubmed.ncbi.nlm.nih.gov/31792037) — von Mehren 2020, Clin Cancer Res (linsitinib SARC wt-GIST trial)
- [PMID 32424176](https://pubmed.ncbi.nlm.nih.gov/32424176) — POLE proofreading hotspot literature
- [PMID 32058550](https://pubmed.ncbi.nlm.nih.gov/32058550) — POLE proofreading reference
- [PMID 32469385](https://pubmed.ncbi.nlm.nih.gov/32469385) — Joensuu 2020, JAMA Oncol (SSGXVIII 10-yr follow-up)
- [PMID 32494005](https://pubmed.ncbi.nlm.nih.gov/32494005) — Sulkowski 2020, Nature (oncometabolite-chromatin axis)
- [PMID 32511981](https://pubmed.ncbi.nlm.nih.gov/32511981) — Blay 2020, Lancet Oncol (INVICTUS ripretinib 4L GIST)
- [PMID 34380780](https://pubmed.ncbi.nlm.nih.gov/34380780) — ctDNA MRD validation reference
- [PMID 34426440](https://pubmed.ncbi.nlm.nih.gov/34426440) — Yebra 2022, Clin Cancer Res (TMZ in dSDH-GIST PDX + mini-cohort)
- [PMID 34754095](https://pubmed.ncbi.nlm.nih.gov/34754095) — tumor-informed ctDNA MRD reference
- [PMID 35324464](https://pubmed.ncbi.nlm.nih.gov/35324464) — Bayley 2022, Endocrine-Related Cancer (belzutifan in Sdhb-KO PCC allograft)
- [PMID 35546442](https://pubmed.ncbi.nlm.nih.gov/35546442) — Pantaleo 2022 (SDHB-IHC pitfall literature)
- [PMID 36151992](https://pubmed.ncbi.nlm.nih.gov/36151992) — Singh 2023, Pediatr Blood Cancer (olaparib + TMZ in dSDH-GIST + PGL case)
- [PMID 36198483](https://pubmed.ncbi.nlm.nih.gov/36198483) — Giger 2022, J Clin Pathol (MGMT methylation in dSDH-GIST)
- [PMID 36302175](https://pubmed.ncbi.nlm.nih.gov/36302175) — Ligon 2023, Clin Cancer Res (guadecitabine in wt-GIST + PPGL + HLRCC)
- [PMID 36442478](https://pubmed.ncbi.nlm.nih.gov/36442478) — Gao 2018, Mol Cancer Ther (MAP2K1 variant functional survey)
- [PMID 38132569](https://pubmed.ncbi.nlm.nih.gov/38132569) — Flego 2024, J Exp Clin Cancer Res (MGMT methylation enrichment in dSDH-GIST)
- [PMID 39927693](https://pubmed.ncbi.nlm.nih.gov/39927693) — Florou 2025 (contemporary dSDH-GIST workup review)
- [PMID 40045030](https://pubmed.ncbi.nlm.nih.gov/40045030) — Dedousis 2025, Curr Treat Options Oncol (dSDH-GIST systemic therapy review)
- [PMID 40156874](https://pubmed.ncbi.nlm.nih.gov/40156874) — Mavroeidis 2025, Expert Rev (rare GIST subtypes review)

### NCTs

- [NCT03556384](https://clinicaltrials.gov/study/NCT03556384) — TMZ in advanced SDH-deficient GIST (UCSD, active-not-recruiting, primary completion June 2025)
- [NCT03739827](https://clinicaltrials.gov/study/NCT03739827) — NCI Rare Tumor Natural History Study
- [NCT04185831](https://clinicaltrials.gov/study/NCT04185831) — Cobimetinib MEGALiT NF1/MAP2K1 basket (active-not-recruiting)
- [NCT04895748](https://clinicaltrials.gov/study/NCT04895748) — DFF332 HIF-2α (terminated Feb 2026)
- [NCT04924075](https://clinicaltrials.gov/study/NCT04924075) — Belzutifan LITESPARK-015 wt-GIST cohort
- [NCT05661643](https://clinicaltrials.gov/study/NCT05661643) — TMZ in advanced SDH-deficient GIST (Asan)
- [NCT05768139](https://clinicaltrials.gov/study/NCT05768139) — Tersolisib PIK3CA-mutant solid tumors
- [NCT06739395](https://clinicaltrials.gov/study/NCT06739395) — Trametinib +/- vebreltinib MAP2K1-alteration basket
- [NCT07434843](https://clinicaltrials.gov/study/NCT07434843) — Pemigatinib PEMIGIST (DFCI)

## Transparency artifacts

- [Trial table](trials.md) — full trial dossier (15 rows), all columns including recruitment status, intervention dosing, modality, regulatory status.
- [Clinical evidence](evidence.md) — 22 rows (8 included clinical + 16 preclinical, with the included / considered_excluded calls and per-row rationale).
- [Master manuscripts inventory](manuscripts.md) — every paper considered (clinical + preclinical) with structured sample size, effect size, variance, toxicity columns.
- [Board proceedings](board.md) — 5 round-1 positions + 20 round-2 critiques, full agreement matrix, per-intervention persona transcripts.
- [Recommendations table](recommendations.md) — structured rendering of the 12 ranked rows in this page.
- [Plain-language summary](plain_language.md) — patient/caregiver framing of the same content.

## Run log

Authored 2026-05 by the Libby PI agent synthesizing `target_validation.jsonl` (12 rows, 8 essential), `trials.jsonl` (15 rows), `clinical_evidence.jsonl` (22 rows, 13 included), `preclinical_evidence.jsonl` (22 rows, 14 included), `positions.jsonl` (5 round-1 picks), and `critiques.jsonl` (5 personas × 4 round-2 critiques each = 20 rows). The PI applied the biomarker-gating logic to the SDHA + SDHB IHC + germline + tissue NGS bundle (rank 1, scenario `shared`) and tagged the three trial-route therapeutic contingencies (belzutifan, temozolomide, pemigatinib at ranks 7, 8, 9) plus the late-line olaparib + TMZ contingency at rank 11 with `scenario: "sdh_confirmed:positive"`. The KIT/PDGFRA-WT systemic backbone (sunitinib at rank 6, regorafenib at rank 10) does not strictly require formal dSDH phenotype confirmation to lift — Boikos 2016 sunitinib activity tracks the KIT-WT phenotype and is the right TKI for KIT-WT GIST regardless of formal SDH status — and is tagged scenario null. Active surveillance, NCI registry, PGL screen, and Signatera MRD are non-therapeutic management actions independent of the biomarker test and are tagged scenario null. Adjuvant imatinib is logged at rank 12 as `not_recommended` with vetoes from advocate and conservative, per Hard Rule 1 (the row is on the page so the no-imatinib decision is documented and not re-litigated). The PI3Kα and MEK inhibitor paths gated on ctDNA-only PIK3CA R93W and MAP2K1 P124S are out-of-scope until tissue NGS confirms; surfaced in the cross-cutting caveat and in 'Classes examined but not ranked.' Preferences are defaulted — flagged in the cross-cutting caveat and re-raised in the re-scoping caveat. The board converged on rank 1 (workup) and rank 2 (surveillance) unanimously; one preference-fit dissent on the rank-6 sunitinib (risktaker preferring trial-route); two formal dissents on the rank-9 pemigatinib (advocate and critic); one advocate dissent on the rank-10 regorafenib; one conservative veto on the rank-11 olaparib + TMZ overridden to a bounded framing; unanimous veto on rank-12 adjuvant imatinib.

<!-- libby:downloads:begin -->

## Downloads

### HTML

- [Target validation paths](target_validation.md?v=575ea9eb) — per-feature biomarker-workup table with providers and references, sortable in-browser
- [Recommendations table](gist-sdh-multifocal-resected-m1-k4n8-recommendations.html?v=019e36df) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Preclinical recommendations](preclinical_recommendations.md?v=755fab5a) — forward-looking horizon scan of earlier-than-clinical candidate drugs, compounds, and strategies, in a sortable in-browser table
- [Preclinical recommendations (offline)](gist-sdh-multifocal-resected-m1-k4n8-preclinical.html?v=03e08c6b) — same preclinical horizon scan packaged as a self-contained HTML that opens offline
- [Access guide](accessibility.md?v=888bc293) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Access guide (offline)](gist-sdh-multifocal-resected-m1-k4n8-accessibility.html?v=4790bbb0) — same access-guide content packaged as a self-contained HTML that opens offline
- [Master manuscripts table](manuscripts.md?v=803f8425) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Master manuscripts table (offline)](gist-sdh-multifocal-resected-m1-k4n8-manuscripts.html?v=07f726fd) — same manuscripts inventory packaged as a self-contained HTML that opens offline

### PDF

- [Target validation paths](gist-sdh-multifocal-resected-m1-k4n8-target-validation.pdf?v=161ca509) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table](gist-sdh-multifocal-resected-m1-k4n8-recommendations.pdf?v=983fdaaa) — ranked options + pipeline context + evidence in detail, in a print-friendly PDF
- [Preclinical recommendations](gist-sdh-multifocal-resected-m1-k4n8-preclinical.pdf?v=717cb09f) — forward-looking horizon scan of earlier-than-clinical candidates, one deep section per candidate, in a print-friendly PDF
- [Access guide](gist-sdh-multifocal-resected-m1-k4n8-accessibility.pdf?v=c7428d16) — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF
- [Master manuscripts table](gist-sdh-multifocal-resected-m1-k4n8-manuscripts.pdf?v=990272aa) — every paper considered — n, effect, variance, toxicities, in a print-friendly PDF
- [Patient/caregiver PDF](gist-sdh-multifocal-resected-m1-k4n8-plain-language.pdf?v=cdfcacd3) — plain-language summary

<!-- libby:downloads:end -->

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
