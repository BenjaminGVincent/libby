<meta name="robots" content="noindex">

# `urothelial-mets-her2-discordant-kndl`

<!-- libby:case-output:begin -->

## Case output

- [Target validation paths (PDF)](urothelial-mets-her2-discordant-kndl-target-validation.pdf?v=a9705d7e) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Selected general biomarker report (HTML)](biomarker_survey.md?v=6e2ecaae) — which panel biomarkers this patient has and has not been tested for, including the tumor-agnostic ones, sortable in-browser
- [Recommendations table (HTML)](urothelial-mets-her2-discordant-kndl-recommendations.html?v=44760f25) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Standard of care options (HTML)](standard_of_care.md?v=89266e1c) — approved and guideline-endorsed strategies for this patient's situation, assessed for eligibility and for how they sequence against the targeted options, sortable in-browser
- [Access guide (HTML)](accessibility.md?v=9eddab30) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, sortable in-browser
- [Access guide (offline HTML)](urothelial-mets-her2-discordant-kndl-accessibility.html?v=ce9dd538) — same access-guide content as the in-browser page, packaged as a self-contained HTML that opens offline
- [Master manuscripts table (HTML)](manuscripts.md?v=afc5eb72) — every paper considered — n, effect, variance, toxicities, sortable in-browser
- [Master manuscripts table (offline HTML)](urothelial-mets-her2-discordant-kndl-manuscripts.html?v=e4d61678) — same manuscripts inventory as the in-browser page, packaged as a self-contained HTML that opens offline
- [Patient/caregiver PDF](urothelial-mets-her2-discordant-kndl-plain-language.pdf?v=bd10bcdc) — plain-language summary

<!-- libby:case-output:end -->
## Research question

In metastatic urothelial carcinoma progressing on pembrolizumab maintenance after a 25-month first-line complete response to enfortumab vedotin plus pembrolizumab, what investigational interventions could target HER2, Nectin-4, TROP2, TP53 R175H with HLA-A\*02:01, FGFR3 (unread), or the mesothelin / MUC1 / PRAME / FAP / ARID1A research leads, gated on validated HER2 IHC reconciliation of the current tumor?

## Patient profile (scrubbed)

- **Primary site / histology:** bladder, high-grade muscle-invasive urothelial carcinoma, poorly differentiated (focal plasmacytoid areas at diagnosis; pleomorphic giant cells in the 2025 recurrence). Separate prostate primary treated 2020, no evidence of disease.
- **Stage:** IVB at diagnosis 2023-11 with liver metastases; CR on 1L therapy 2024-08; current disease oligometastatic nodal (biopsy-proven left para-aortic node plus probable perivesical node), treated with SBRT 2026-06.
- **ECOG:** 1
- **Biomarkers (confirmation status as recorded):**
    - **HER2 — `ihc_pending`, DISCORDANT.** Three concordant validated IHC 3+ results (primary 2023-11, liver met 2023-11, recurrence 2025-03) against a weak HER2 signal on research-grade MXIF of 2026-08 nodal tissue. Repeat validated IHC drawn 2026-08; tier not yet in the record. Decision resolution: validated IHC (4B5 or equivalent) with reflex ISH if 2+, on contemporary tissue.
    - **Nectin-4 — confirmed historically** (95-100% membranous, 2023/2025); current expression after ~25 months of EV unknown; 2026-06 Nectin-4 imaging read not in the record.
    - **TROP2 — `ihc_pending`,** low positive (weak) on 2026-08 research MXIF; validated IHC drawn, tier unretrieved.
    - **Mesothelin, MUC1 — `ihc_pending`,** strong on 2026-08 research MXIF only; no validated stain.
    - **PRAME — unknown;** 2026-08 PRAME-directed imaging result not in the record. HLA-A\*02:01 confirmed.
    - **FAP (stromal) — unknown;** the one FAPi PET on record (2025-09) showed no FAP-avid urothelial carcinoma.
    - **TMB 12.4 mut/Mb** (institutional panel; cross-assay hedge vs the FoundationOne-validated threshold). **MSS.** **MAGE-A4 negative.**
    - **Somatic mutations:** ARID1A, TERT promoter, TP53 (R175H seen in plasma ctDNA at 0.09% VAF, 2025-06). The tissue report counts exactly one OncoKB-actionable alteration and never names it; FGFR3 status is absent from the derived record.
    - **ctDNA:** chronically positive on two tumor-informed platforms, rising into 2026-06, then two zero Signatera draws after SBRT (minor internal conflict in the ops summary).
- **Prior therapy:** EV + pembrolizumab 1L (CR, ~25 months; EV stopped 2025-12 for neuropathy), pembrolizumab maintenance (PD 2026), intravesical BCG, TURBT x3, two personalized neoantigen vaccine programs (peptide + mRNA, ongoing), SBRT 2026-06.
- **Current therapy:** T-DXd (2 doses, severe nausea/bloating after dose 2; continuation under review), mRNA vaccine series, pembrolizumab on hold, metformin, amylase/lipase surveillance q3-4wk.
- **Organ function flags:** unresolved 2026-03 vs 2026-06 chest CT discrepancy (outside read suggestive of fibrosis/ILD vs no pneumonitis); recovered 2025 pancreatitis (lipase peak 384 U/L); chronic CIPN from EV; creatinine/eGFR not in the available record.

## Preferences

- **Efficacy/toxicity weight:** 0.7 (efficacy-leaning; all preferences INFERRED from the record, to confirm)
- **Toxicity vetoes (inferred):** severe peripheral neuropathy (MMAE payloads, platinum/taxane backbones); severe GI toxicity / highly emetogenic regimens; ILD/pneumonitis-high-risk agents without tight monitoring; pancreatitis-risk agents
- **Modality constraints:** no geographic/logistical constraints evident; intensive experimental modalities acceptable, including cell therapy (apheresis banked)
- **Free text:** strongly experimental-leaning; surface trials prominently; tumor tissue is scarce (prefer blood/imaging screening); three near-term decision gates — reconcile HER2, T-DXd stop/continue on ctDNA and tolerability, retrieve the full NGS report
- **Trials preferred:** yes

<!-- libby:target-validation:begin -->

## Target validation paths

Two orders decide most of this case and neither is a new test. A validated HER2 IHC was drawn in 2026-08 and only its tier is missing from the record; that tier governs whether trastuzumab deruxtecan continues on the tumor-agnostic footing written for IHC 3+, and whether the HER2 ADCs gated at 2+ or 3+ (the disitamab vedotin class) are reachable at all. The second is a records request for sequencing already performed between 2023 and 2025, which carries the FGFR3 and FGFR2 status behind erdafitinib (THOR, NCT03390504), the identity of the single OncoKB-actionable alteration the 2023 report counts without naming, and the ERBB2 copy number. If the tier comes back low and the sequencing returns nothing actionable, both of those branches close, and what remains are research-grade stains that have to be validated before anything can be screened against them.

### HER2

Ask for the validated HER2 IHC (clone 4B5 or equivalent, reflex ISH at 2+) reported as a tier with tumor content stated. Retrieval of the 2026-08 report comes before any re-stain, because the stain already exists. Three IHC 3+ results describe 2023 and 2025 tumor, while the only read of the current tumor is a weak research-grade multiplex immunofluorescence signal, which is not a validated HER2 assay and settles nothing in either direction. The 2026-08 nodal core carries 5-10% tumor content and can under-read a membrane stain, so run the 2025-03 recurrence block alongside it with tumor content reported for each. That pairing is what separates real antigen loss from a tumor-poor specimen. ERBB2 copy number sits unnamed among the 12 and 13 copy-number alterations counted in the 2023 reports and refines the tier call; it rides on the same retrieval and on the next plasma draw. Serial tumor-informed ctDNA on both existing platforms (Signatera, NeXT Personal) is the other half of the continue-or-stop question on trastuzumab deruxtecan, and the conflicting 2026-06 and 2026-07 zero draws need reconciling against the source reports before the kinetics mean anything.

### ARID1A / TERT promoter / TP53

The retrieval of the full sequencing reports is the highest-yield order in this workup and costs no tissue. Roughly 15-20% of metastatic urothelial carcinoma carries an FGFR3 alteration, and that status gates erdafitinib (NCT03390504); the derived record does not contain it. The same request closes the NTRK, RET and BRAF codon 600 questions behind larotrectinib, entrectinib, repotrectinib, selpercatinib and dabrafenib plus trametinib, returns somatic homologous-recombination status next to the ARID1A synthetic-lethality hypothesis, and supplies the exome data for the TMB recomputation and the HLA analysis below. Expect most of those to read negative. That is the normal result for rare alterations in this disease, and the case for reading them is that the answers already exist. Two practical caveats: an FGFR3 alteration found on a laboratory-developed panel may still need confirmation on the approved companion assay before treatment, and a DNA-only panel reporting no structural variants does not close NTRK, whose breakpoints sit in large introns. If the reports cannot be released, a comprehensive plasma panel answers the FGFR3 question without touching tissue, though fusion coverage has to be checked before a negative is trusted.

### Nectin-4

Both stains, 95-100% membranous, predate 25 months of enfortumab vedotin, and antigen downregulation is a recognized route to enfortumab resistance, so the historical result cannot carry a re-targeting decision now. The 2026-06 Nectin-4-directed imaging study has already been performed, and retrieving that read answers most of the question without spending tissue; a contemporary IHC on post-enfortumab tissue is the fallback. Retained expression keeps next-generation non-MMAE Nectin-4 agents live, and loss closes the axis cleanly rather than leaving it open as a standing maybe. Even with retained expression, MMAE re-exposure runs against the established neuropathy, so the practical question is whether a non-MMAE agent is reachable, and prior enfortumab is an exclusion in several Nectin-4 protocols regardless of expression.

### TROP2

The validated TROP2 IHC was also performed in 2026-08 and, again, only the tier is missing, so retrieval comes first. Ask for it as a tier (percent membranous staining times intensity, or an H-score) rather than as positive or negative. The weak multiplex signal is a low positive and not a negative, and low expression predicts TROP2-directed ADC benefit less reliably than strong expression does. That is what the number changes: it sets the confidence on the datopotamab deruxtecan and sacituzumab tirumotecan class rather than opening or closing it, since TROP2-ADC development in urothelial carcinoma has not been strictly expression-gated.

### PRAME and HLA-A\*02:01

HLA-A\*02:01 is confirmed, so expression is the only gate left on the PRAME ImmTAC and TCR-T class, and those protocols screen on validated IHC (clone EPR20330) or RT-PCR at a stated threshold rather than on the research imaging performed in 2026-08. RT-PCR tolerates the 5-10% tumor content of the nodal cores better than IHC scoring does. This is the gate on IMA203 via NCT03686124, the solid-tumor study, and on brenetafusp via NCT04262466. The other registered IMA203 study is restricted to cutaneous melanoma and does not apply here. NY-ESO-1 (CTAG1B) is the second A\*02:01-restricted antigen with an open TCR-T bench and should be run off the same block in the same order. Separately, tumor HLA class I loss of heterozygosity can be computed from the existing tumor and normal exome data; somatic loss of A\*02:01 would blunt every HLA-restricted approach here, the neoantigen vaccine programs included. That computation is research-grade and would not satisfy protocol eligibility on its own.

### Mesothelin

Strong mesothelin in urothelial carcinoma is unusual enough that it either opens a serious cell-therapy option or turns out to be an artifact of an unvalidated research assay, and only a validated clinical stain (clone 5B2 or the candidate protocol's own assay, tumor content stated) separates those. Most mesothelin cell-therapy protocols run their own central assay at screening, so a local positive opens the door rather than satisfying it, and pleural and pericardial normal expression is the on-target risk a sponsor will weigh next. A serum soluble mesothelin-related peptide level is a low-priority add-on that rides a routine draw and flags a soluble-antigen sink before a CAR-T or engager protocol. Renal impairment raises that level independently of tumor, and creatinine and eGFR are absent from the record, so read any elevation against a current renal panel.

### MUC1

MUC1 sits behind mesothelin: the same research assay, the same missing validation, a thinner therapeutic bench. Normal epithelium carries wild-type MUC1, so a strong signal only means something once the assay resolves the tumor-associated glycoform the candidate agent targets, Tn-MUC1 where that is the epitope, using the clone the protocol names. One slide on the block already being cut answers it. Until then the signal is a lead and not a result.

### B7-H3

B7-H3 (CD276) has never been assessed in this patient, and it is the pan-cancer surface target with the deepest current trial bench. One extra slide on the cut already planned for HER2 and TROP2 is the only reason it earns tissue in a case this tissue-poor. Expression would open solid-tumor ADC and bispecific cohorts of the ifinatamab deruxtecan class, though sponsors differ on B7-H3 IHC standardization and a protocol may still require its own assay at screening, and a deruxtecan-payload agent would have to be weighed against the unresolved pulmonary findings.

### TMB

The 12.4 mut/Mb figure came off an institutional 468-gene laboratory-developed panel, while the tumor-agnostic indication reads TMB-H by an FDA-approved test. Recomputing from the whole-exome data already generated costs no tissue and settles whether the number survives a cross-assay comparison; report the caller and the filtering rather than the bare number, because panel-derived and exome-derived values differ systematically. PD-L1 by a companion clone (22C3 pharmDx or equivalent) is worth repeating only once a specific protocol names a clone and a cutoff: the two results on file, CPS 5 on the primary against CPS 0 in the liver metastasis, are discordance rather than a number. Immune-infiltrate density (CD3, CD8, macrophages) can be re-queried from the 2026-08 multiplex run already performed, if that panel carried T-cell and myeloid markers, with post-SBRT inflammation stated as a caveat.

### Personalized neoantigens

An IFN-gamma EliSpot on post-mRNA-series PBMCs against the 24 predicted neoepitope pools, with CD4 and CD8 deconvolution against a matched pre-vaccine timepoint, is the next readout on this axis. The only immunogenicity data so far is 2 of 14 evaluable pools at 4 months, CD4-skewed, with several pools not evaluable, which is too thin to say whether the vaccine axis is doing anything. Banked serial PBMCs mean no new collection. Pool-level results cannot name the peptide that drove a response, so plan deconvolution for any positive pool if the result is meant to guide an expansion product, and read it against the HLA loss-of-heterozygosity analysis: presentation loss would explain a flat result better than a failed vaccine would.

### FAP

The one FAPI PET on record found no FAP-avid urothelial disease and lit up granulomatous prostate tissue instead, a classic false positive, so stromal positivity on an unvalidated multiplex assay does not make this a treatment lead. The 2026-06 repeat study has already been performed and its read costs nothing to retrieve. Recent SBRT to the nodal disease adds treatment-related fibroblast activation, which makes new uptake harder to attribute to tumor stroma. FAPI PET is not FDA approved and is available in the US mainly on research protocols, so a repeat study means an enrolling site rather than a clinical order.

### Biomarkers measured, but not to decision resolution

Nine markers on this list have a result on file that cannot carry a treatment decision as it stands. The target call is not what is in doubt for these; the resolution of the existing result is. A reader who conflates the two will think a biomarker is unproven when it is only under-measured. Each one has a matching order in the tables below, so none of them was dropped.

- **HER2.** Three validated IHC 3+ results, all on 2023 and 2025 tissue; the current tumor has only a weak research-grade multiplex read. The validated 2026-08 IHC tier, reported with tumor content, closes it.
- **TROP2.** A weak multiplex signal recorded as low expression, not as a negative. The validated 2026-08 IHC reported as a tier closes it.
- **Nectin-4.** 95-100% membranous on two specimens, both predating 25 months of enfortumab vedotin. The 2026-06 imaging read, or a contemporary IHC on post-enfortumab tissue, closes it.
- **Mesothelin.** Strong on research-grade multiplex immunofluorescence only. A validated clinical mesothelin IHC with tumor content stated closes it.
- **MUC1.** Strong on the same research assay, with no validated tier and no glycoform resolution. A validated MUC1 IHC using the clone and threshold a candidate protocol names closes it.
- **PRAME.** Imaging was performed in 2026-08 and the read is not in the record; imaging is not what a PRAME protocol screens on. Validated PRAME IHC (EPR20330) or RT-PCR at the protocol's threshold closes it.
- **TMB.** 12.4 mut/Mb from a laboratory-developed panel against a label written for an FDA-approved test. TMB recomputed from the existing whole-exome data, or a companion-diagnostic-grade report, closes it.
- **PD-L1.** CPS 5 on the primary against CPS 0 in the liver metastasis, both from 2023, on a laboratory clone validated as comparable to 22C3 rather than the companion assay itself. A companion-assay read on contemporary tissue closes it, and only when a protocol names a clone and a cutoff.
- **FAP.** Stromal positivity on an unvalidated multiplex assay against a FAPI PET that showed no avid urothelial lesion. Quantitative FAPI uptake in the known nodal disease, read with the post-SBRT caveat, closes it.

### Where to order these assays

| Assay | Provider | Decision gated | Contact |
|---|---|---|---|
| **Validated HER2 IHC (clone 4B5 or equivalent) with reflex ISH if 2+, on contemporary tumor tissue, reported as an expression tier (3+ / 2+ / 1+ / 0) with tumor content stated** | **NeoGenomics Laboratories *(preferred)* (HER2 IHC clone 4B5 (APH-HERX-01AX) with HER2 FISH reflex)** | **Continue versus stop trastuzumab deruxtecan, and eligibility for HER2 ADCs gated on IHC 2+/3+ (disitamab vedotin class).** | **[test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3** |
| Validated HER2 IHC (clone 4B5 or equivalent) with reflex ISH if 2+, on contemporary tumor tissue, reported as an expression tier (3+ / 2+ / 1+ / 0) with tumor content stated | Labcorp Oncology *(HER2 IHC with reflex FISH (test 483289))* | Continue versus stop trastuzumab deruxtecan, and eligibility for HER2 ADCs gated on IHC 2+/3+ (disitamab vedotin class). | [test info](https://www.labcorp.com/oncology/contact) · 531 South Spring Street, Burlington, NC 27215 · 800-447-5816 |
| Validated HER2 IHC (clone 4B5 or equivalent) with reflex ISH if 2+, on contemporary tumor tissue, reported as an expression tier (3+ / 2+ / 1+ / 0) with tumor content stated | Quest Diagnostics *(HER2 IHC (test 30316); IHC with FISH reflex (test 15547))* | Continue versus stop trastuzumab deruxtecan, and eligibility for HER2 ADCs gated on IHC 2+/3+ (disitamab vedotin class). | [test info](https://www.questdiagnostics.com/contact-us/customer-service) · 500 Plaza Drive, Secaucus, NJ 07094 · 866-697-8378 |
| Validated HER2 IHC (clone 4B5 or equivalent) with reflex ISH if 2+, on contemporary tumor tissue, reported as an expression tier (3+ / 2+ / 1+ / 0) with tumor content stated | Yale Pathology Labs | Continue versus stop trastuzumab deruxtecan, and eligibility for HER2 ADCs gated on IHC 2+/3+ (disitamab vedotin class). | [test info](https://medicine.yale.edu/pathology/ypl/contact/) · 310 Cedar Street LH 108, PO Box 208023, New Haven, CT 06520-8023 · 877-925-3522 |
| **Retrieval of the full existing sequencing reports (institutional 468-gene tumor/normal panel 2023-11, two commercial WES/WTS platforms, WGS 2025-03), read for FGFR3 and FGFR2 status and for the identity of the single OncoKB-actionable alteration** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Erdafitinib eligibility via FGFR3/FGFR2 status (THOR, NCT03390504), plus the identity of the one OncoKB-actionable alteration in the tissue reports.** | **[test info](https://www.foundationmedicine.com/order-a-test) · 400 Summer Street, Boston, MA 02210 · 888-988-3639** |
| Retrieval of the full existing sequencing reports (institutional 468-gene tumor/normal panel 2023-11, two commercial WES/WTS platforms, WGS 2025-03), read for FGFR3 and FGFR2 status and for the identity of the single OncoKB-actionable alteration | Caris Life Sciences *(MI Cancer Seek (whole exome plus whole transcriptome))* | Erdafitinib eligibility via FGFR3/FGFR2 status (THOR, NCT03390504), plus the identity of the one OncoKB-actionable alteration in the tissue reports. | [test info](https://www.carislifesciences.com/order/) · 4610 South 44th Place, Phoenix, AZ 85040 (specimen receiving) · 888-979-8669 |
| Retrieval of the full existing sequencing reports (institutional 468-gene tumor/normal panel 2023-11, two commercial WES/WTS platforms, WGS 2025-03), read for FGFR3 and FGFR2 status and for the identity of the single OncoKB-actionable alteration | Tempus AI *(Tempus xT / xR)* | Erdafitinib eligibility via FGFR3/FGFR2 status (THOR, NCT03390504), plus the identity of the one OncoKB-actionable alteration in the tissue reports. | [test info](https://www.tempus.com/contact-us/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 |
| **Serial tumor-informed ctDNA on the existing two platforms (Signatera, NeXT Personal), with the conflicting 2026-06 and 2026-07 zero-draw results reconciled against the source reports** | **Natera *(preferred)* (Signatera)** | **Continue versus stop trastuzumab deruxtecan, read together with the HER2 tier.** | **[test info](https://www.natera.com/oncology/signatera-advanced-cancer-detection/) · 13011 McCallen Pass, Building A Suite 100, Austin, TX 78753 · 650-489-9050** |
| Serial tumor-informed ctDNA on the existing two platforms (Signatera, NeXT Personal), with the conflicting 2026-06 and 2026-07 zero-draw results reconciled against the source reports | Personalis *(NeXT Personal Dx)* | Continue versus stop trastuzumab deruxtecan, read together with the HER2 tier. | [test info](https://www.personalis.com/contact-us/) · 6600 Dumbarton Circle, Fremont, CA 94555 · 855-373-7978 |
| **Comprehensive plasma ctDNA panel covering FGFR3 and FGFR2 alterations, ERBB2 copy number, and variants acquired under prior therapy** | **Guardant Health *(preferred)* (Guardant360 CDx)** | **Erdafitinib eligibility when the archival reports cannot be retrieved; the same draw returns ERBB2 copy number.** | **[test info](https://guardanthealth.com/contact/) · 505 Penobscot Drive, Redwood City, CA 94063 (laboratory) · 855-698-8887** |
| Comprehensive plasma ctDNA panel covering FGFR3 and FGFR2 alterations, ERBB2 copy number, and variants acquired under prior therapy | Foundation Medicine *(FoundationOne Liquid CDx)* | Erdafitinib eligibility when the archival reports cannot be retrieved; the same draw returns ERBB2 copy number. | [test info](https://www.foundationmedicine.com/order-a-test) · 400 Summer Street, Boston, MA 02210 · 888-988-3639 |
| Comprehensive plasma ctDNA panel covering FGFR3 and FGFR2 alterations, ERBB2 copy number, and variants acquired under prior therapy | Tempus AI *(Tempus xF)* | Erdafitinib eligibility when the archival reports cannot be retrieved; the same draw returns ERBB2 copy number. | [test info](https://www.tempus.com/contact-us/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 |
| **PRAME expression by validated IHC (clone EPR20330) or RT-PCR, scored at the threshold the candidate protocol names** | **NeoGenomics Laboratories *(preferred)* (PRAME IHC clone EPR20330 (APT-PRAX-01AX))** | **PRAME-directed ImmTAC / TCR-T entry (IMA203 via NCT06743126 or NCT03686124; brenetafusp via NCT04262466).** | **[test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3** |
| PRAME expression by validated IHC (clone EPR20330) or RT-PCR, scored at the threshold the candidate protocol names | Mayo Clinic Laboratories *(PRAME immunostain (test 615794))* | PRAME-directed ImmTAC / TCR-T entry (IMA203 via NCT06743126 or NCT03686124; brenetafusp via NCT04262466). | [test info](https://www.mayocliniclabs.com/customer-service/contacts) · 3050 Superior Drive NW, Rochester, MN 55901 · 800-533-1710 |
| PRAME expression by validated IHC (clone EPR20330) or RT-PCR, scored at the threshold the candidate protocol names | Discovery Life Sciences | PRAME-directed ImmTAC / TCR-T entry (IMA203 via NCT06743126 or NCT03686124; brenetafusp via NCT04262466). | [test info](https://dls.com/contact-us/) · 900 Hudson Way, Huntsville, AL 35806 · 866-838-2798 |
| **Contemporary Nectin-4 IHC on post-enfortumab-vedotin tissue, or retrieval of the 2026-06 Nectin-4-directed imaging read** | **Discovery Life Sciences *(preferred)*** | **Whether any Nectin-4 re-targeting stays on the table after 25 months of enfortumab vedotin.** | **[test info](https://dls.com/contact-us/) · 900 Hudson Way, Huntsville, AL 35806 · 866-838-2798** |
| Contemporary Nectin-4 IHC on post-enfortumab-vedotin tissue, or retrieval of the 2026-06 Nectin-4-directed imaging read | NeoGenomics Laboratories | Whether any Nectin-4 re-targeting stays on the table after 25 months of enfortumab vedotin. | [test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3 |
| Contemporary Nectin-4 IHC on post-enfortumab-vedotin tissue, or retrieval of the 2026-06 Nectin-4-directed imaging read | Yale Pathology Labs | Whether any Nectin-4 re-targeting stays on the table after 25 months of enfortumab vedotin. | [test info](https://medicine.yale.edu/pathology/ypl/contact/) · 310 Cedar Street LH 108, PO Box 208023, New Haven, CT 06520-8023 · 877-925-3522 |
| **Validated clinical mesothelin IHC (clone 5B2 or the candidate protocol's own assay), scored with tumor content stated** | **NeoGenomics Laboratories *(preferred)* (Mesothelin IHC)** | **Entry to mesothelin-directed CAR-T, T-cell engager and ADC protocols.** | **[test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3** |
| Validated clinical mesothelin IHC (clone 5B2 or the candidate protocol's own assay), scored with tumor content stated | Labcorp Oncology *(Mesothelin IHC (test zzIO-228))* | Entry to mesothelin-directed CAR-T, T-cell engager and ADC protocols. | [test info](https://www.labcorp.com/oncology/contact) · 531 South Spring Street, Burlington, NC 27215 · 800-447-5816 |
| Validated clinical mesothelin IHC (clone 5B2 or the candidate protocol's own assay), scored with tumor content stated | Discovery Life Sciences | Entry to mesothelin-directed CAR-T, T-cell engager and ADC protocols. | [test info](https://dls.com/contact-us/) · 900 Hudson Way, Huntsville, AL 35806 · 866-838-2798 |
| Validated clinical mesothelin IHC (clone 5B2 or the candidate protocol's own assay), scored with tumor content stated | Yale Pathology Labs | Entry to mesothelin-directed CAR-T, T-cell engager and ADC protocols. | [test info](https://medicine.yale.edu/pathology/ypl/contact/) · 310 Cedar Street LH 108, PO Box 208023, New Haven, CT 06520-8023 · 877-925-3522 |
| **TMB recomputed from the whole-exome data already generated, using a validated caller, or read from a companion-diagnostic-grade panel report** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **TMB-H eligibility for trials that name an assay, and the strength of the neoantigen argument behind checkpoint re-intensification.** | **[test info](https://www.foundationmedicine.com/order-a-test) · 400 Summer Street, Boston, MA 02210 · 888-988-3639** |
| TMB recomputed from the whole-exome data already generated, using a validated caller, or read from a companion-diagnostic-grade panel report | Caris Life Sciences *(MI Cancer Seek)* | TMB-H eligibility for trials that name an assay, and the strength of the neoantigen argument behind checkpoint re-intensification. | [test info](https://www.carislifesciences.com/order/) · 4610 South 44th Place, Phoenix, AZ 85040 (specimen receiving) · 888-979-8669 |
| TMB recomputed from the whole-exome data already generated, using a validated caller, or read from a companion-diagnostic-grade panel report | Tempus AI *(Tempus xT)* | TMB-H eligibility for trials that name an assay, and the strength of the neoantigen argument behind checkpoint re-intensification. | [test info](https://www.tempus.com/contact-us/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 |
| **ERBB2 copy number read from the existing tissue NGS reports (12 and 13 copy-number alterations were counted and never itemized), with plasma ERBB2 copy number on the next ctDNA draw** | **Guardant Health *(preferred)* (Guardant360 CDx)** | **Refines the HER2 tier call ahead of the continue-versus-stop decision on T-DXd; not an independent gate.** | **[test info](https://guardanthealth.com/contact/) · 505 Penobscot Drive, Redwood City, CA 94063 (laboratory) · 855-698-8887** |
| ERBB2 copy number read from the existing tissue NGS reports (12 and 13 copy-number alterations were counted and never itemized), with plasma ERBB2 copy number on the next ctDNA draw | Foundation Medicine *(FoundationOne Liquid CDx)* | Refines the HER2 tier call ahead of the continue-versus-stop decision on T-DXd; not an independent gate. | [test info](https://www.foundationmedicine.com/order-a-test) · 400 Summer Street, Boston, MA 02210 · 888-988-3639 |
| **HER2 IHC on a second site (2025-03 bladder recurrence block) read alongside the 2026-08 nodal core, with tumor content reported for each** | **NeoGenomics Laboratories *(preferred)* (HER2 IHC clone 4B5 (APH-HERX-01AX) with HER2 FISH reflex)** | **Whether a low HER2 read on the node reflects antigen loss or a tumor-poor specimen.** | **[test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3** |
| HER2 IHC on a second site (2025-03 bladder recurrence block) read alongside the 2026-08 nodal core, with tumor content reported for each | Yale Pathology Labs | Whether a low HER2 read on the node reflects antigen loss or a tumor-poor specimen. | [test info](https://medicine.yale.edu/pathology/ypl/contact/) · 310 Cedar Street LH 108, PO Box 208023, New Haven, CT 06520-8023 · 877-925-3522 |
| **Validated TROP2 IHC reported as a tier (percent membranous staining times intensity, or H-score) rather than as positive or negative** | **Discovery Life Sciences *(preferred)*** | **How much weight the TROP2-ADC trial axis carries (datopotamab deruxtecan class, sacituzumab tirumotecan).** | **[test info](https://dls.com/contact-us/) · 900 Hudson Way, Huntsville, AL 35806 · 866-838-2798** |
| Validated TROP2 IHC reported as a tier (percent membranous staining times intensity, or H-score) rather than as positive or negative | NeoGenomics Laboratories | How much weight the TROP2-ADC trial axis carries (datopotamab deruxtecan class, sacituzumab tirumotecan). | [test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3 |
| Validated TROP2 IHC reported as a tier (percent membranous staining times intensity, or H-score) rather than as positive or negative | Yale Pathology Labs | How much weight the TROP2-ADC trial axis carries (datopotamab deruxtecan class, sacituzumab tirumotecan). | [test info](https://medicine.yale.edu/pathology/ypl/contact/) · 310 Cedar Street LH 108, PO Box 208023, New Haven, CT 06520-8023 · 877-925-3522 |
| **Somatic homologous-recombination gene status (BRCA1, BRCA2, ATM, PALB2, RAD51 paralogs) read off the retrieved tissue NGS report; an HRD score only if a protocol asks for one** | **Myriad Genetics *(preferred)* (myChoice CDx (BRCA1/2 plus genomic instability score))** | **DNA-damage-response trial eligibility (ATR and PARP inhibitor protocols) alongside the ARID1A hypothesis.** | **[test info](https://myriad.com/mychoicecdx-astrazeneca/) · 322 North 2200 West, Salt Lake City, UT 84116 · 800-469-7423** |
| **Validated MUC1 IHC using the clone and threshold the candidate protocol names, glycoform-specific (Tn-MUC1) where the agent targets that epitope** | **Yale Pathology Labs *(preferred)*** | **Screening for MUC1-directed CAR-T, T-cell engager or vaccine protocols.** | **[test info](https://medicine.yale.edu/pathology/ypl/contact/) · 310 Cedar Street LH 108, PO Box 208023, New Haven, CT 06520-8023 · 877-925-3522** |
| Validated MUC1 IHC using the clone and threshold the candidate protocol names, glycoform-specific (Tn-MUC1) where the agent targets that epitope | NeoGenomics Laboratories | Screening for MUC1-directed CAR-T, T-cell engager or vaccine protocols. | [test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3 |
| Validated MUC1 IHC using the clone and threshold the candidate protocol names, glycoform-specific (Tn-MUC1) where the agent targets that epitope | Discovery Life Sciences | Screening for MUC1-directed CAR-T, T-cell engager or vaccine protocols. | [test info](https://dls.com/contact-us/) · 900 Hudson Way, Huntsville, AL 35806 · 866-838-2798 |
| **B7-H3 (CD276) IHC on tumor tissue** | **Discovery Life Sciences *(preferred)*** | **Screening for B7-H3-directed ADC and bispecific solid-tumor cohorts (ifinatamab deruxtecan class).** | **[test info](https://dls.com/contact-us/) · 900 Hudson Way, Huntsville, AL 35806 · 866-838-2798** |
| B7-H3 (CD276) IHC on tumor tissue | NeoGenomics Laboratories | Screening for B7-H3-directed ADC and bispecific solid-tumor cohorts (ifinatamab deruxtecan class). | [test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3 |
| B7-H3 (CD276) IHC on tumor tissue | Yale Pathology Labs | Screening for B7-H3-directed ADC and bispecific solid-tumor cohorts (ifinatamab deruxtecan class). | [test info](https://medicine.yale.edu/pathology/ypl/contact/) · 310 Cedar Street LH 108, PO Box 208023, New Haven, CT 06520-8023 · 877-925-3522 |
| **NY-ESO-1 (CTAG1B) expression by IHC or RT-PCR, run on the same block as PRAME** | **Discovery Life Sciences *(preferred)*** | **NY-ESO-1-directed TCR-T screening (letetresgene autoleucel class), ordered alongside PRAME.** | **[test info](https://dls.com/contact-us/) · 900 Hudson Way, Huntsville, AL 35806 · 866-838-2798** |
| NY-ESO-1 (CTAG1B) expression by IHC or RT-PCR, run on the same block as PRAME | NeoGenomics Laboratories | NY-ESO-1-directed TCR-T screening (letetresgene autoleucel class), ordered alongside PRAME. | [test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3 |
| **PD-L1 IHC by the companion clone a candidate protocol names (22C3 pharmDx or equivalent), on contemporary tissue** | **Labcorp Oncology *(preferred)* (PD-L1 IHC 22C3 pharmDx (test 451852))** | **Entry to trials that specify a PD-L1 clone and cutoff; not a gate on checkpoint use itself.** | **[test info](https://www.labcorp.com/oncology/contact) · 531 South Spring Street, Burlington, NC 27215 · 800-447-5816** |
| PD-L1 IHC by the companion clone a candidate protocol names (22C3 pharmDx or equivalent), on contemporary tissue | NeoGenomics Laboratories *(PD-L1 IHC 22C3)* | Entry to trials that specify a PD-L1 clone and cutoff; not a gate on checkpoint use itself. | [test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3 |
| PD-L1 IHC by the companion clone a candidate protocol names (22C3 pharmDx or equivalent), on contemporary tissue | Quest Diagnostics *(PD-L1 22C3 (test 93279 lung, 36260 non-lung))* | Entry to trials that specify a PD-L1 clone and cutoff; not a gate on checkpoint use itself. | [test info](https://www.questdiagnostics.com/contact-us/customer-service) · 500 Plaza Drive, Secaucus, NJ 07094 · 866-697-8378 |
| **Serum soluble mesothelin-related peptide (SMRP) immunoassay** | **ARUP Laboratories *(preferred)* (Soluble mesothelin-related peptides, MESOMARK (test 0081284))** | **Refines the mesothelin target call and flags soluble-antigen sink before a mesothelin cell-therapy protocol.** | **[test info](https://www.aruplab.com/contact) · 500 Chipeta Way, Salt Lake City, UT 84108-1221 · 800-522-2787** |
| Serum soluble mesothelin-related peptide (SMRP) immunoassay | Fujirebio Diagnostics | Refines the mesothelin target call and flags soluble-antigen sink before a mesothelin cell-therapy protocol. | [test info](https://www.fujirebio.com/en-us) · 201 Great Valley Parkway, Malvern, PA 19355 · 877-861-7246 |
| **Retrieval of the 2026-06 FAP-directed imaging read, with quantitative FAPI PET uptake in the known nodal disease only if that read is uninformative** | **UCLA Health, Ahmanson Translational Theranostics Division *(preferred)*** | **Whether FAP-directed radioligand concepts stay on the list; currently an imaging-research lead rather than a treatment lead.** | **[test info](https://www.uclahealth.org/) · 855-731-6040** |
| Retrieval of the 2026-06 FAP-directed imaging read, with quantitative FAPI PET uptake in the known nodal disease only if that read is uninformative | Stanford Nuclear Medicine and Molecular Imaging | Whether FAP-directed radioligand concepts stay on the list; currently an imaging-research lead rather than a treatment lead. | [test info](https://clinicaltrials.stanford.edu/) · 650-723-6855 |

### Biomarker plan

| Recommended assay | Rationale | Suggested assay provider | Tissue requirements |
|---|---|---|---|
| Validated HER2 IHC (clone 4B5 or equivalent) with reflex ISH if 2+, on contemporary tumor tissue, reported as an expression tier (3+ / 2+ / 1+ / 0) with tumor content stated | The validated stain was already drawn in 2026-08 and only its tier is missing from the record, so the first move is retrieving that report rather than cutting a new slide. Three IHC 3+ results describe 2023 and 2025 tumor; the only read of the current tumor is a weak research-grade multiplex immunofluorescence signal, which is not a validated HER2 assay and cannot settle the question either way. Without the tier, a poorly tolerated T-DXd course continues on three-year-old tissue, and a genuine drop to HER2-low moves the drug off its tumor-agnostic label, which is written for IHC 3+, and onto a bystander-payload argument. | NeoGenomics Laboratories *(HER2 IHC clone 4B5 (APH-HERX-01AX) with HER2 FISH reflex)* · [test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3 | Archival FFPE acceptable; already-cut 2026-08 material preferred, otherwise one block cut (2026-08 nodal core or 2025-03 recurrence) with tumor content stated on the report |
| Retrieval of the full existing sequencing reports (institutional 468-gene tumor/normal panel 2023-11, two commercial WES/WTS platforms, WGS 2025-03), read for FGFR3 and FGFR2 status and for the identity of the single OncoKB-actionable alteration | The record counts exactly one alteration with an OncoKB treatment interpretation and never names it, and FGFR3 status, which gates erdafitinib in roughly 15-20% of metastatic urothelial carcinoma, appears nowhere in the derived profile. Both answers already sit in reports that were generated and never retrieved, so this costs a records request and no tissue. Leaving it unretrieved risks missing the strongest genomic option in the case while scarce tissue is spent on stains for weaker ones. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/order-a-test) · 400 Summer Street, Boston, MA 02210 · 888-988-3639 | No specimen; records retrieval only |
| Serial tumor-informed ctDNA on the existing two platforms (Signatera, NeXT Personal), with the conflicting 2026-06 and 2026-07 zero-draw results reconciled against the source reports | The stop-versus-continue decision on T-DXd rests on ctDNA kinetics alongside the HER2 tier, and the record carries an internal conflict: two 2026-06 and 2026-07 draws read 0 MTM/mL in one table and are listed as pending in another. The two platforms also point in different directions, with NeXT Personal describing a decrease after a transient post-therapy rise while Signatera reads zero. Reconciling the source reports and taking the next scheduled draws separates a real molecular response after SBRT and two T-DXd doses from assay noise, using blood rather than the scarce tissue. | Natera *(Signatera)* · [test info](https://www.natera.com/oncology/signatera-advanced-cancer-detection/) · 13011 McCallen Pass, Building A Suite 100, Austin, TX 78753 · 650-489-9050 | 10-20 mL whole blood per draw; no tumor tissue |
| Comprehensive plasma ctDNA panel covering FGFR3 and FGFR2 alterations, ERBB2 copy number, and variants acquired under prior therapy | If the archived reports cannot be released or turn out not to cover FGFR3, a plasma panel answers the erdafitinib question without touching tissue, and detectable ctDNA on two MRD platforms says shed is adequate for it. The same draw returns ERBB2 copy number and anything acquired across 25 months of enfortumab vedotin and pembrolizumab. A negative plasma result is weaker than a negative tissue result, so it argues for tissue testing rather than closing the question. | Guardant Health *(Guardant360 CDx)* · [test info](https://guardanthealth.com/contact/) · 505 Penobscot Drive, Redwood City, CA 94063 (laboratory) · 855-698-8887 | Two Streck tubes of whole blood (about 20 mL) |
| PRAME expression by validated IHC (clone EPR20330) or RT-PCR, scored at the threshold the candidate protocol names | HLA-A*02:01 is confirmed, so expression is the only remaining gate on the PRAME ImmTAC and TCR-T class, and those protocols screen on validated IHC or RT-PCR rather than on the research imaging performed in 2026-08. PRAME in urothelial carcinoma is a subset finding rather than the rule, so a negative is a realistic and useful result. The MAGE-A4 sequence is the precedent: HLA matched, expression negative, option closed by a test rather than by assumption. | NeoGenomics Laboratories *(PRAME IHC clone EPR20330 (APT-PRAX-01AX))* · [test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3 | Archival FFPE block or 5-10 unstained slides; RT-PCR tolerates the 5-10% tumor content of the nodal cores better than IHC scoring |
| Contemporary Nectin-4 IHC on post-enfortumab-vedotin tissue, or retrieval of the 2026-06 Nectin-4-directed imaging read | Both stains predate 25 months of enfortumab vedotin, and antigen downregulation is a recognized route to EV resistance, so a 95-100% membranous result from 2023 and 2025 cannot carry a re-targeting decision now. The 2026-06 Nectin-4 imaging study has already been performed and its read would answer most of this without touching tissue. Retained expression keeps next-generation non-MMAE Nectin-4 agents on the table; loss closes the axis cleanly instead of leaving it open as a standing maybe. | Discovery Life Sciences · [test info](https://dls.com/contact-us/) · 900 Hudson Way, Huntsville, AL 35806 · 866-838-2798 | Archival FFPE acceptable (one slide on the shared block cut); zero tissue if the 2026-06 imaging read is informative |
| Validated clinical mesothelin IHC (clone 5B2 or the candidate protocol's own assay), scored with tumor content stated | Strong mesothelin in urothelial carcinoma is unusual enough that it either opens a serious cell-therapy option or turns out to be an artifact of an unvalidated research assay, and only a validated stain separates those. Apheresis product and PBMCs are already banked, so a confirmed result would be immediately usable at screening. Screening on the multiplex result alone risks consenting to a protocol the tumor cannot support. | NeoGenomics Laboratories *(Mesothelin IHC)* · [test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3 | Archival FFPE acceptable; one slide from the shared block cut, preferably the 2025-03 recurrence |
| TMB recomputed from the whole-exome data already generated, using a validated caller, or read from a companion-diagnostic-grade panel report | The 12.4 mut/Mb value sits above the TMB-H bar but comes from an institutional 468-gene laboratory-developed panel, while the tumor-agnostic indication reads TMB-H by an FDA-approved test, and FoundationOne CDx remains the only approved TMB companion diagnostic. Recomputing from the whole-exome sequencing already performed costs no tissue and settles whether the number survives a cross-assay comparison. It matters less for pembrolizumab, which this patient has already progressed through, than for trials that gate on a named assay and for the neoantigen argument behind the vaccine and ipilimumab-addition strategies. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/order-a-test) · 400 Summer Street, Boston, MA 02210 · 888-988-3639 | No specimen if recomputed from existing exome data; archival FFPE if a companion-diagnostic panel is ordered instead |
| ERBB2 copy number read from the existing tissue NGS reports (12 and 13 copy-number alterations were counted and never itemized), with plasma ERBB2 copy number on the next ctDNA draw | The 2023 panel reported 12 copy-number alterations in the primary and 13 in the liver metastasis without naming them, so whether ERBB2 was amplified is already answered inside a report nobody has retrieved. Amplification underneath the 3+ stain makes true antigen loss less likely and helps interpret a discordant weak multiplex signal; its absence pushes the other way. This rides on the records retrieval and the plasma draw already planned and uses no tissue. | Guardant Health *(Guardant360 CDx)* · [test info](https://guardanthealth.com/contact/) · 505 Penobscot Drive, Redwood City, CA 94063 (laboratory) · 855-698-8887 | No specimen for the retrieval; the plasma read shares the ctDNA draw already scheduled |
| HER2 IHC on a second site (2025-03 bladder recurrence block) read alongside the 2026-08 nodal core, with tumor content reported for each | A single nodal core at 5-10% tumor content is a thin basis for calling antigen loss, and this case already shows site-to-site discordance in another marker, with CPS 5 on the primary against CPS 0 in the liver metastasis. Staining two sites separates a real drop in HER2 from a sampling artifact of a tumor-poor node. If both sites read low, the antigen-loss interpretation becomes much harder to argue away, which is what the T-DXd decision turns on. | NeoGenomics Laboratories *(HER2 IHC clone 4B5 (APH-HERX-01AX) with HER2 FISH reflex)* · [test info](https://neogenomics.com/contact-us) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 option 3 | Archival FFPE acceptable; one additional slide from each of the 2025-03 recurrence block and the 2026-08 nodal core, cut in the same batch |
| IFN-gamma EliSpot on post-mRNA-series PBMCs against the 24 predicted neoepitope pools, with CD4 and CD8 deconvolution and a matched pre-vaccine timepoint | The only immunogenicity readout so far is 2 of 14 evaluable pools at 4 months, CD4-skewed, with several pools not evaluable, which is too thin to say whether the vaccine axis is doing anything. Serial pre- and post-vaccine PBMCs are already banked, so the assay needs no new collection and no tumor tissue. Deconvoluting CD4 from CD8 responses also tells the TIL and adoptive-cell-therapy groups which epitopes are worth expanding against. | No external provider listed; reads off records or data already generated. | Banked PBMCs, or one 30-50 mL blood draw if fresh cells are preferred; no tumor tissue |
| Validated TROP2 IHC reported as a tier (percent membranous staining times intensity, or H-score) rather than as positive or negative | The validated stain was performed in 2026-08 and only the tier is missing, so retrieval comes before any re-stain. A weak multiplex signal is a low positive and not a negative, and low expression predicts TROP2-ADC benefit less reliably than strong expression, which is exactly what the number changes about how much weight this axis carries. TROP2-ADC development in urothelial cancer has not been strictly expression-gated, so a low tier sets the confidence rather than closing the option. | Discovery Life Sciences · [test info](https://dls.com/contact-us/) · 900 Hudson Way, Huntsville, AL 35806 · 866-838-2798 | Archival FFPE acceptable; no new tissue if the 2026-08 report is retrieved |
| NTRK1/2/3 fusion status read off the retrieved whole-transcriptome and NGS reports; an RNA fusion panel only if none of them covered NTRK | This is a records problem and not a testing problem: whole-transcriptome sequencing that would show an NTRK fusion has already been run on two platforms and the reports are not in hand. NTRK fusions are rare in urothelial carcinoma so a negative is the expected answer, and a DNA-only panel reporting no structural variants does not close the question, because NTRK breakpoints sit in large introns. It rides free on the retrieval this case needs anyway. | No external provider listed; reads off records or data already generated. | No specimen for the readout; archival FFPE if an RNA fusion panel is ordered |
| RET fusion status read off the retrieved whole-transcriptome or NGS report; an RNA fusion panel only if RET was not covered | RET fusions are rare in urothelial carcinoma and nothing in this record suggests one, so the expected result is negative. It costs nothing beyond the retrieval already needed, and leaving it unread means an approved oral agent stays formally unassessed rather than excluded. A DNA panel without RET intronic coverage would not settle it on its own. | No external provider listed; reads off records or data already generated. | No specimen for the readout; archival FFPE if an RNA fusion panel is ordered |
| BRAF codon 600 status read off the retrieved full tissue NGS report | BRAF V600E is uncommon in urothelial carcinoma and the honest expectation is that it is absent. It stays on the list because the record counts one OncoKB-actionable alteration without naming it, so the identity of that variant is unknown and BRAF is among the few candidates that would arrive with an approved tumor-agnostic option. Reading it off the existing report costs a records request. | No external provider listed; reads off records or data already generated. | No specimen; readout from the existing report |
| Somatic homologous-recombination gene status (BRCA1, BRCA2, ATM, PALB2, RAD51 paralogs) read off the retrieved tissue NGS report; an HRD score only if a protocol asks for one | Germline testing was negative in 2023-12, which leaves somatic homologous-recombination status as the unanswered half, and it sits in a panel report that covers those genes and has never been retrieved. Urothelial carcinoma is not a PARP-inhibitor indication, so the realistic payoff is trial eligibility next to the ARID1A synthetic-lethality hypothesis rather than an approved drug. No new specimen is involved. | Myriad Genetics *(myChoice CDx (BRCA1/2 plus genomic instability score))* · [test info](https://myriad.com/mychoicecdx-astrazeneca/) · 322 North 2200 West, Salt Lake City, UT 84116 · 800-469-7423 | No specimen for the readout; archival FFPE if an HRD score is later required |
| Validated MUC1 IHC using the clone and threshold the candidate protocol names, glycoform-specific (Tn-MUC1) where the agent targets that epitope | MUC1 sits behind mesothelin here: the same research assay, the same missing validation, a thinner therapeutic bench. Normal epithelium carries wild-type MUC1, so a strong signal only means something when the assay resolves the tumor-associated glycoform the candidate agent targets. One slide on the block already being cut answers it; until then the signal is a lead and not a result. | Yale Pathology Labs · [test info](https://medicine.yale.edu/pathology/ypl/contact/) · 310 Cedar Street LH 108, PO Box 208023, New Haven, CT 06520-8023 · 877-925-3522 | Archival FFPE acceptable; one slide on the shared block cut |
| B7-H3 (CD276) IHC on tumor tissue | B7-H3 has never been looked at in this patient and it is the pan-cancer surface target with the deepest current trial bench. One extra slide from the block already being cut for HER2 and TROP2 answers it, which is the only reason it earns tissue in a case this tissue-poor. Expression would open solid-tumor ADC and bispecific cohorts, though a deruxtecan-payload agent would still have to be weighed against the unresolved pulmonary findings. | Discovery Life Sciences · [test info](https://dls.com/contact-us/) · 900 Hudson Way, Huntsville, AL 35806 · 866-838-2798 | Archival FFPE acceptable; one slide on the shared block cut |
| NY-ESO-1 (CTAG1B) expression by IHC or RT-PCR, run on the same block as PRAME | The HLA gate is already satisfied, and NY-ESO-1 is the second A*02:01-restricted antigen with an open TCR-T bench, so it costs one assay run next to the PRAME order. Expression in urothelial carcinoma is a minority finding, so a negative is the likely and still useful outcome. MAGE-A4 already showed how quickly an expression assay closes one of these axes. | Discovery Life Sciences · [test info](https://dls.com/contact-us/) · 900 Hudson Way, Huntsville, AL 35806 · 866-838-2798 | Archival FFPE acceptable; RT-PCR is the more forgiving option at 5-10% tumor content |
| PD-L1 IHC by the companion clone a candidate protocol names (22C3 pharmDx or equivalent), on contemporary tissue | The two results on file are CPS 5 on the primary and CPS 0 in the liver metastasis, which is discordance rather than a number, and both date from 2023 on a laboratory clone validated as comparable to 22C3 rather than the companion assay itself. Checkpoint use in metastatic urothelial carcinoma is not PD-L1 gated, and this patient has already had both a deep response and progression on PD-1 blockade, so the practical weight is low. Repeat it when a specific protocol names a clone and a cutoff, not before. | Labcorp Oncology *(PD-L1 IHC 22C3 pharmDx (test 451852))* · [test info](https://www.labcorp.com/oncology/contact) · 531 South Spring Street, Burlington, NC 27215 · 800-447-5816 | Archival FFPE acceptable; one slide on the shared block cut when a protocol requires it |
| Tumor HLA class I loss of heterozygosity computed from the existing tumor/normal exome data (LOHHLA or equivalent) | Germline typing is on file and positive for A*02:01, but somatic loss of that allele in the tumor would blunt every HLA-restricted approach in play here, from PRAME ImmTAC and TCR-T to the personalized neoantigen vaccines. The tumor and normal exome data needed for the calculation already exists, so this is an analysis rather than a specimen request. Skipping it leaves a class-wide escape mechanism unexamined while several A*02:01-dependent programs are being pursued. | No external provider listed; reads off records or data already generated. | No specimen; computed from existing tumor and normal exome data |
| CD3, CD8 and macrophage density re-queried from the 2026-08 multiplex immunofluorescence run already performed on the nodal tissue | The multiplex panel has already been run on the 2026-08 node, so immune-infiltrate density can be read from the existing image data at no tissue cost. An inflamed node supports adding CTLA-4 blockade or an IL-15 superagonist after progression on PD-1 maintenance, while an immune-desert pattern argues the problem is priming rather than checkpoint restraint. This is a research-grade readout that informs how the immune-intensification axis is ranked, not protocol eligibility. | No external provider listed; reads off records or data already generated. | No specimen; re-analysis of the 2026-08 multiplex images already acquired |
| Serum soluble mesothelin-related peptide (SMRP) immunoassay | Shed mesothelin acts as a sink that blunts mesothelin-directed agents, so a soluble level is worth having before a CAR-T or engager protocol, and it needs blood rather than tissue. The assay is cleared for mesothelioma monitoring rather than for urothelial carcinoma, so a level here corroborates or undercuts the tissue call without replacing it. Low value on its own; it earns a line because it rides on a routine draw. | ARUP Laboratories *(Soluble mesothelin-related peptides, MESOMARK (test 0081284))* · [test info](https://www.aruplab.com/contact) · 500 Chipeta Way, Salt Lake City, UT 84108-1221 · 800-522-2787 | 3-5 mL serum on a routine draw; no tumor tissue |
| Retrieval of the 2026-06 FAP-directed imaging read, with quantitative FAPI PET uptake in the known nodal disease only if that read is uninformative | The one FAPI PET on record found no FAP-avid urothelial disease and lit up granulomatous prostate tissue instead, a classic false positive, so stromal positivity on an unvalidated multiplex assay does not make this a treatment lead. The 2026-06 repeat study has already been performed and its read costs nothing to retrieve. Recent SBRT to the nodal disease adds treatment-related fibroblast activation, which makes any new uptake harder to attribute to tumor stroma. | UCLA Health, Ahmanson Translational Theranostics Division · [test info](https://www.uclahealth.org/) · 855-731-6040 | No specimen; imaging only |

---

*Decision support, not medical advice. Confirm assay availability and current standards with the treating team and the local pathology service.*

<!-- libby:target-validation:end -->

## Scope summary

The dossier holds 40 trials, 48 clinical-evidence rows (38 included), and 41 preclinical rows (34 included), argued over by five board personas across 5 positions and 20 cross-critiques. The Experimental table below carries 54 rows: one shared workup, 14 assessed therapeutic rows, and 39 non-top-tier options flagged with a surfaced reason. Board agreement spans -0.6 to 1.0. All five personas stand behind the rank-1 workup; no therapeutic row drew more than three endorsements; three vetoes were recorded against two interventions (both handled below, neither dropped). Four of five personas ranked T-DXd continuation first, but that option is approved and guideline-carried for this patient and so belongs to the standard-of-care table, not this ranking.

## Cross-cutting caveat (read first)

**The HER2 result that everything leans on describes a tumor that may no longer exist.** Three validated IHC 3+ results span 2023-2025 tissue; the only read of the current tumor is a weak HER2 signal on 2026-08 research-grade multiplex immunofluorescence, which is not a validated HER2 assay and can neither overturn nor confirm the 3+ calls. The decision resolution is a validated IHC tier (4B5 or equivalent, reflex ISH if 2+) on contemporary tissue — and that stain was already drawn in 2026-08. Its tier is sitting in a report nobody has retrieved.

- This ranking is scoped to the stated targetable features and to *investigational* options. Approved or guideline-carried feature-targeting drugs — T-DXd continuation (the tumor-agnostic IHC 3+ label), enfortumab vedotin, pembrolizumab, and erdafitinib should FGFR3 confirm — are routed to the standard-of-care table, which is a separate, co-equal surface. The T-DXd stop/continue decision is that table's question; this table's HER2 rows are what remain if it stops.
- If contemporary HER2 IHC reads negative or low without amplification, the `her2_ihc:positive` rows (ranks 2, 6, 8) are foreclosed and T-DXd continuation loses its on-label footing. The non-HER2 rows (ranks 3-5, 7, 9-12) survive on their own gates. If those gates also close — no retained Nectin-4, no tissue-confirmed R175H, no FGFR3 alteration, validated stains negative on the research-lead antigens — this case has no within-scope recommendations; standard of care for metastatic urothelial carcinoma lies outside Libby's targetable-feature ranking and should be pursued through the treating team's normal care channel.
- Workup logistics: retrieving the 2026-08 report beats recutting a block (days vs 3-7 days plus release paperwork). The nodal core carries 5-10% tumor content and can under-read a membrane stain, so tumor content belongs on the report, and a second-site read on the 2025-03 recurrence block hedges the sampling problem. Any new stains (TROP2, mesothelin, MUC1, PD-L1 re-stain) should ride the same block cut — the tissue gets opened once.
- Three screening gates recur across nearly every ranked trial and are worth settling once, centrally: whether measurable RECIST disease exists after SBRT to the only known nodal sites; the unresolved 2026-03 vs 2026-06 chest CT discrepancy (it blocks AVZO-103 outright and prices every deruxtecan-class payload); and the T-DXd washout, which forces a stop decision before most enrollments can even be discussed.

## Intervention grouping

- **HER2-directed, payload-free or cellular** (conditional on the re-stain): zanidatamab ([36400106](https://pubmed.ncbi.nlm.nih.gov/36400106), [NCT06695845](https://clinicaltrials.gov/study/NCT06695845)); pertuzumab + trastuzumab via TAPUR ([37793085](https://pubmed.ncbi.nlm.nih.gov/37793085), [NCT02693535](https://clinicaltrials.gov/study/NCT02693535)); FT825 CAR-T ([NCT06241456](https://clinicaltrials.gov/study/NCT06241456))
- **Nectin-4 re-targeting after EV:** LY4052031 ([NCT06465069](https://clinicaltrials.gov/study/NCT06465069)); [225Ac]Ac-AKY-1189 ([NCT07020117](https://clinicaltrials.gov/study/NCT07020117)); resistance biology favoring retained antigen ([42167230](https://pubmed.ncbi.nlm.nih.gov/42167230), [41173324](https://pubmed.ncbi.nlm.nih.gov/41173324))
- **Mutation-directed T-cell engagement:** CLSP-1025 against TP53 R175H x HLA-A\*02:01 ([NCT06778863](https://clinicaltrials.gov/study/NCT06778863), [33649166](https://pubmed.ncbi.nlm.nih.gov/33649166))
- **TROP2 axis, low-positive hedged:** ASP2998 ([NCT07287995](https://clinicaltrials.gov/study/NCT07287995)); class context [39086310](https://pubmed.ncbi.nlm.nih.gov/39086310), [39934055](https://pubmed.ncbi.nlm.nih.gov/39934055)
- **FGFR3, conditional on the records retrieval:** vepugratinib / FORAGER-1 ([NCT05614739](https://clinicaltrials.gov/study/NCT05614739)); the approved default (erdafitinib, [NCT03390504](https://clinicaltrials.gov/study/NCT03390504)) routes to standard of care
- **Checkpoint re-intensification:** nivolumab + ipilimumab ([36868252](https://pubmed.ncbi.nlm.nih.gov/36868252), [31100038](https://pubmed.ncbi.nlm.nih.gov/31100038)); registered variant-histology route [NCT03866382](https://clinicaltrials.gov/study/NCT03866382)
- **Personalized neoantigen vaccine / ACT axis (ongoing):** [40346292](https://pubmed.ncbi.nlm.nih.gov/40346292), [37165196](https://pubmed.ncbi.nlm.nih.gov/37165196)

## Top interventions

### Rank 1. HER2 reconciliation + sequencing-report retrieval — decision gate

*Resolves the two questions the whole case hangs on: the contemporary HER2 tier, and the FGFR3 / OncoKB-actionable readout already sitting in unretrieved reports.*

#### Evidence base

The tumor-agnostic T-DXd label and its NCCN listing are written for validated IHC 3+, and the tier dependence is quantified across two independent datasets: DESTINY-PanTumor02 responded at 61.3% in the central IHC 3+ population against 37.1% overall ([37870536](https://pubmed.ncbi.nlm.nih.gov/37870536), [NCT04482309](https://clinicaltrials.gov/study/NCT04482309)), and MyPathway's gradient runs 41% at amplified 3+ to 8.3% at 1+ to zero at IHC 0 ([37793085](https://pubmed.ncbi.nlm.nih.gov/37793085)). On the genomic side, roughly 15-20% of metastatic urothelial carcinoma carries an FGFR3 alteration that both NCCN and ESMO treat as actionable in exactly this line ([NCT03390504](https://clinicaltrials.gov/study/NCT03390504)). The 2023 tissue report counts one OncoKB-actionable alteration without naming it.

#### Likelihood of desired effect

Certain to inform. The stain was drawn in 2026-08; only its tier is missing. The sequencing retrieval closes the FGFR3, ERBB2 copy number, NTRK/RET/BRAF, somatic-HR and HLA-LOH questions in one records request, with no tissue spent.

#### Toxicity profile

- None. Records retrieval plus IHC on existing tissue.
- The real risk is interpretive: a 5-10% tumor-content nodal core can under-read a membrane stain. Tumor content must be stated on the report; a second-site read on the 2025-03 recurrence block is the hedge.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. Four personas made T-DXd continuation contingent on the tier; the critic went further and called the unretrieved reports the cheapest evidence upgrade in the case, with none of his four picks surviving unchanged if the reads come back adverse.

#### Practical considerations

First call goes to the tertiary center that stained the 2026-08 specimen — retrieval beats recutting. NeoGenomics (4B5 with FISH reflex) is the preferred commercial fallback; Labcorp, Quest and Yale Pathology are alternates, with Yale the second-opinion option for a tumor-poor core. The sequencing request covers the institutional 468-gene panel, two commercial WES/WTS platforms, and the 2025 WGS. An FGFR3 alteration found on a laboratory-developed panel may still need companion-assay confirmation before erdafitinib.

#### Why this rank

Nothing below it can be weighted correctly until it lands, it costs almost nothing, and it is the only row all five personas endorse without qualification.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| T-DXd (gate consumer; SoC table) | ORR 61.3% central IHC 3+ vs 37.1% overall | ILD 10.5%, 3 deaths in pivotal cohort | [NCT04482309](https://clinicaltrials.gov/study/NCT04482309), [37870536](https://pubmed.ncbi.nlm.nih.gov/37870536) |
| Vepugratinib (gate consumer; rank 7) | Conditional on FGFR3 readout | FGFR-class effects | [NCT05614739](https://clinicaltrials.gov/study/NCT05614739) |

### Rank 2. Zanidatamab (payload-free HER2 bispecific)

*Conditional on `her2_ihc:positive`. Foreclosed if the contemporary stain reads low.*

#### Evidence base

The phase 1 in HER2-expressing solid tumors reported ORR 37.0% (95% CI 27.0-48.7) in 132 patients, weighted toward biliary tract cancer, with six grade-3 treatment-related events in 4 of 132 and no treatment-related deaths ([36400106](https://pubmed.ncbi.nlm.nih.gov/36400106), [NCT02892123](https://clinicaltrials.gov/study/NCT02892123)). A phase 2 IHC 3+ pan-tumor basket names urothelial carcinoma ([NCT06695845](https://clinicaltrials.gov/study/NCT06695845)). Single-arm, first-in-human evidence; urothelial durability is unknown.

#### Likelihood of desired effect

Moderate if 3+ holds, and only then: the 37% figure comes from mixed histologies, and activity after T-DXd exposure has never been measured. A negative or low re-stain forecloses this row entirely.

#### Toxicity profile

- Benign phase-1 file: grade-3 treatment-related events in 4/132, no deaths.
- Standard LVEF monitoring; infusion reactions.
- Touches none of the four stated vetoes — no cytotoxic payload, so the neuropathy, GI, ILD and pancreatitis concerns do not bite. That is the point of the row.

#### Counter-productive mechanisms / dissent

No recorded dissent, but the endorsement base is narrow: conservative and concensusite ranked it, both as a fallback and both at low confidence. The unmeasured mechanism risk is ADC-selected HER2 downregulation gutting a payload-free binder.

#### Practical considerations

The registered basket cohort for this histology bars prior HER2-directed therapy, which the current T-DXd course triggers — so the realistic route is off-label, and the payer case stands or falls with the IHC tier. Post-approval safety follow-up is under two years.

#### Why this rank

It leads the conditional tier because it pairs actual clinical response data with the cleanest safety file on the board; the two rows tied with it at 0.4 carry no clinical data at all, and the 0.7 efficacy weight breaks the tie in favor of measured activity.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Zanidatamab | ORR 37.0% (95% CI 27.0-48.7), phase 1, biliary-weighted | Grade-3 TRAEs 4/132; no TRDs | [NCT06695845](https://clinicaltrials.gov/study/NCT06695845), [36400106](https://pubmed.ncbi.nlm.nih.gov/36400106) |

### Rank 3. [225Ac]Ac-AKY-1189 (Nectin-4 actinium-225 radioligand)

*A pure mechanism bet with an imaging step that answers the current-expression question without spending tissue.*

#### Evidence base

First-in-human dose escalation, no efficacy data of any kind ([NCT07020117](https://clinicaltrials.gov/study/NCT07020117)). The supporting argument is biology: NECTIN4 amplification marks 18% of urothelial carcinomas ([41173324](https://pubmed.ncbi.nlm.nih.gov/41173324)), an alpha emitter kills by crossfire rather than by antigen engagement on every cell, and the [64Cu] imaging step reads current Nectin-4 status during screening. Prior enfortumab vedotin is explicitly permitted, which almost no other Nectin-4 protocol allows.

#### Likelihood of desired effect

Unknown. There is no number to quote and both endorsing personas said so; the bet is that crossfire physics survives partial antigen loss after 25 months of EV. Dose escalation adds the risk of treatment at a level nobody expects to work.

#### Toxicity profile

- No human safety data. Class concerns: marrow suppression (2025 iron-deficiency anemia history, platelets 170) and renal exposure.
- Creatinine/eGFR is absent from the available record, with a history of obstructive uropathy — that gap needs closing before any radioligand conversation.
- No MMAE, no deruxtecan payload: no stated veto is touched.

#### Counter-productive mechanisms / dissent

Risktaker and advocate endorsed; conservative's blanket position against first-in-human radioligands (no post-marketing safety file at all) stands as the unrecorded counterweight, and the critic did not engage the row. The endorsement base is the board's two most aggressive voices, which is worth naming.

#### Practical considerations

Mount Sinai is enrolling; sites span New York, Pennsylvania and Maryland. Measurable RECIST disease after SBRT is a real screening gate, and the ~3-week washout from T-DXd forces the sequencing decision early. Retrieving the 2026-06 Nectin-4 imaging read first could make the screening visit unnecessary or much more attractive.

#### Why this rank

It edges CLSP-1025 on the strength of its target: Nectin-4 delivered this patient's 25-month complete response and is historically 95-100% positive, while the R175H call below rests on a single 0.09% VAF plasma read.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| [225Ac]Ac-AKY-1189 | None (first-in-human) | No human data; marrow/renal class risks | [NCT07020117](https://clinicaltrials.gov/study/NCT07020117) |

### Rank 4. CLSP-1025 (TP53 R175H x HLA-A\*02:01 T-cell engager)

*Both eligibility gates already answered on paper; the R175H call itself is the weak link.*

#### Evidence base

No clinical data exist for CLSP-1025 or its class ([NCT06778863](https://clinicaltrials.gov/study/NCT06778863)). The preclinical package is unusually deep — structure-resolved specificity for the mutant peptide-HLA complex ([33649166](https://pubmed.ncbi.nlm.nih.gov/33649166)) and affinity-optimized formats that outperform CAR designs at this antigen density ([41542775](https://pubmed.ncbi.nlm.nih.gov/41542775)) — and the only human precedent on the axis is one TCR-T patient with a 55% regression lasting 6 months ([35749374](https://pubmed.ncbi.nlm.nih.gov/35749374)).

#### Likelihood of desired effect

Unknown, and gated twice. The class has no clinical results, and the R175H call rests on a single plasma read at 0.09% VAF — a low-positive result that is a weaker, less reliable predictor than a tissue-confirmed truncal call would be. It could be subclonal, or fail the sponsor's central confirmation outright.

#### Toxicity profile

- Cytokine release syndrome expected; inpatient step-up dosing. No stated veto is touched.
- Off-tumor behavior in humans unknown; dose escalation may enroll at a subtherapeutic level.

#### Counter-productive mechanisms / dissent

Risktaker and advocate endorsed. The critic's round-1 notes declined the class for having no published clinical results and called the 0.09% VAF a weak basis for an eligibility case — an objection that persists and that the endorsers themselves partly conceded. The mechanism-level worry is very low peptide-HLA copy number per cell, plus unmeasured tumor HLA-A\*02 loss of heterozygosity; if that allele is lost, this row and the PRAME axis fail together.

#### Practical considerations

Off-the-shelf: no apheresis slot, no manufacturing wait, histology open, four sites in the usual care orbit. Before any screening visit: pull tissue-level confirmation of R175H from the existing 2023 NGS report (free, fast), and compute HLA-LOH from the existing exome.

#### Why this rank

Same board arithmetic as rank 3, ordered below it because the target call is one plasma read at 0.09% VAF against Nectin-4's years of validated high expression.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| CLSP-1025 | None (first-in-human) | Expected CRS; inpatient step-up | [NCT06778863](https://clinicaltrials.gov/study/NCT06778863) |

### Rank 5. LY4052031 (Nectin-4 ADC, camptothecin payload) — NEXUS-01 cohort B2

*The trial written for this exact history; the number attached to it is not yet evidence.*

#### Evidence base

Cohort B2 requires prior enfortumab vedotin rather than excluding it ([NCT06465069](https://clinicaltrials.gov/study/NCT06465069)). The reported post-EV response rate is 47% at 3.6 mg/kg — an ASCO 2026 abstract figure from the sponsor's ongoing dose escalation, unpublished, no confidence interval, and the critic priced it accordingly. The target's validation is a different matter: Nectin-4-directed therapy holds two randomized phase 3 OS wins in this disease (EV-301 HR 0.70, p=0.001, [33577729](https://pubmed.ncbi.nlm.nih.gov/33577729); EV-302 HR 0.47, p<0.001, [38446675](https://pubmed.ncbi.nlm.nih.gov/38446675)), and post-EV resistance biology favors retained antigen — endocytic and efflux defects rather than antigen loss ([42167230](https://pubmed.ncbi.nlm.nih.gov/42167230)).

#### Likelihood of desired effect

Moderate but unstable. If the 47% holds anywhere near its face value in the expansion, this is the best expected-value therapeutic on the board; regression toward something smaller is likely, and both Nectin-4 stains predate the 25 months of EV that could have thinned the target (primary-to-node IHC agreement in this disease runs kappa 0.41).

#### Toxicity profile

- No published safety table. Camptothecin-class GI toxicity (diarrhea, nausea, neutropenia) lands on an active severe-nausea problem — the GI veto is engaged as a monitoring concern, not cleared.
- The payload avoids MMAE entirely, which is what clears the neuropathy veto.
- Back-to-back topoisomerase-I payloads after T-DXd are unstudied.

#### Counter-productive mechanisms / dissent

Three personas ranked it (advocate 1st, risktaker 2nd, critic 3rd). Conservative dissented: rank-1 weight exceeds what an unpublished dose-escalation figure with no safety table can carry against an active GI problem. Concensusite dissented on placement above the guideline-listed option. The critic, while ranking it, insisted the 47% is a screening lead and not an estimate. The synthesis keeps it as the strongest live trial lead, screened in parallel with the workup rather than as a reason to stop anything.

#### Practical considerations

Six Northeast sites including MSK and MGH; screening runs on histology and prior therapy, not fresh tissue. Measurable disease is required and the only known nodal sites were irradiated in 2026-06. Enrollment cannot be discussed until the T-DXd stop decision is made, and the deruxtecan-to-camptothecin cross-resistance question should be put to the investigator directly.

#### Why this rank

The formula, not the enthusiasm: two placement dissents pull its agreement score below the 0.4 tier, and the synthesis respects that arithmetic while noting that every persona who engaged the row deeply wanted it screened.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| LY4052031 (cohort B2) | 47% post-EV ORR, unpublished dose-escalation readout | No published safety table; camptothecin-class GI, cytopenias | [NCT06465069](https://clinicaltrials.gov/study/NCT06465069) |

### Rank 6. Pertuzumab + trastuzumab (TAPUR HER2 arm)

*Conditional on `her2_ihc:positive` (3+, or 2+ with ERBB2 amplification on the retrieved report). Foreclosed if the stain reads low without amplification.*

#### Evidence base

MyPathway quantifies the tier gradient this whole case turns on: ORR 41.0% in HER2-amplified IHC 3+ tumors, 25.9% overall, 8.3% at 1+, zero at IHC 0, with two of the five complete responses in urothelial tumors ([37793085](https://pubmed.ncbi.nlm.nih.gov/37793085)). Non-randomized basket, ORR surrogate, KRAS-confounded (28.1% wild-type vs 7.1% mutant) — the critic grades it ROBINS-I serious and ranked it anyway, because the evidence is internally consistent and fully disclosed.

#### Likelihood of desired effect

Moderate at amplified 3+; collapses along the tier gradient below that. Naked-antibody activity after progression on a HER2 ADC is undocumented in this tumor type, and ADC-resistant tumors may have already selected against the target.

#### Toxicity profile

- Diarrhea 36.1%, fatigue 29.4%, nausea 22.4% any-grade; no single serious term above 1.7%. Standard LVEF algorithm.
- The only HER2 option in the dossier touching none of the four stated vetoes, with 13+ years of post-marketing data behind both antibodies.

#### Counter-productive mechanisms / dissent

Conservative (rank 2) and critic (rank 4) endorsed. Risktaker dissented on preference fit: a 25.9% pooled ORR with no post-T-DXd data ranked above the Nectin-4 axis presses the safety counterweight past what a 0.7 efficacy weight and `prefers_trials: true` will bear. The synthesis absorbs the objection by seating it below the trial leads.

#### Practical considerations

TAPUR ([NCT02693535](https://clinicaltrials.gov/study/NCT02693535)) is the protocolized route: ECOG 0-2, broad sites including Connecticut, biosimilar supply. The arm turns on ERBB2 amplification or overexpression documented in the still-unretrieved NGS report — the same rank-1 retrieval, again.

#### Why this rank

It trades rank 5's unstable 47% for a published, tier-stratified estimate and a veto-clean profile, and gives up the trial-novelty fit the preference file asks for; at 0.7 efficacy weight that nets out just below the Nectin-4 trial.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Pertuzumab + trastuzumab (TAPUR) | ORR 41.0% amplified 3+ / 25.9% overall / 8.3% at 1+ | Diarrhea 36.1% any-grade; no serious term >1.7% | [NCT02693535](https://clinicaltrials.gov/study/NCT02693535), [37793085](https://pubmed.ncbi.nlm.nih.gov/37793085) |

### Rank 7. FGFR3 axis — vepugratinib (FORAGER-1), conditional on the sequencing retrieval

*Wholly conditional on a records request. If an alteration is found, the approved default (erdafitinib) lives on the standard-of-care table and this trial is the escalation.*

#### Evidence base

No agent evidence is quotable yet because the gate is unread: FGFR3 status appears nowhere in the derived record, and roughly 15-20% of metastatic urothelial carcinoma qualifies. Both major guideline bodies carry erdafitinib for susceptible FGFR3 alterations after EV + pembrolizumab, which makes FGFR the only non-HER2 route with consensus standing in this line. FORAGER-1 ([NCT05614739](https://clinicaltrials.gov/study/NCT05614739)) is the investigational arm; cohort B7, which pairs a qualifying FGFR3 alteration with HER2 expression, is the one registry slot where this patient's two axes meet.

#### Likelihood of desired effect

Conditional arithmetic: ~15-20% probability the alteration exists at all. If it does, the axis instantly becomes the strongest non-HER2 genomic branch on the board — risktaker and advocate both said the retrieval could reorder their entire lists.

#### Toxicity profile

- FGFR-inhibitor class effects: hyperphosphatemia, stomatitis, nail and eye toxicity. No vepugratinib-specific table in the dossier.
- No stated veto is touched.

#### Counter-productive mechanisms / dissent

Concensusite ranked it; nobody dissented, and every other persona's notes point at the same retrieval. The only recorded reservation is concensusite's own: the expected yield is modest, and the consensus standing belongs to erdafitinib rather than to this phase 1.

#### Practical considerations

The gate costs a records request. An alteration found on a laboratory-developed panel may need confirmation on the FDA-approved companion assay before erdafitinib; trial screening is typically more flexible.

#### Why this rank

The highest-consensus conditional row: it loses to rank 6 only on the probability that its gate opens at all.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Vepugratinib (FORAGER-1) | Conditional; no dossier estimate | FGFR-class effects | [NCT05614739](https://clinicaltrials.gov/study/NCT05614739) |

### Rank 8. FT825 / ONO-8250 (off-the-shelf HER2 CAR-T)

*Conditional on `her2_ihc:positive` at the protocol's tier. Foreclosed if the stain reads below it.*

#### Evidence base

Phase 1 dose escalation in HER2-expressing solid tumors with no urothelial efficacy signal to quote ([NCT06241456](https://clinicaltrials.gov/study/NCT06241456)). The expectation that benefit tracks the stain rests on the class data: 61.3% at central 3+ in DESTINY-PanTumor02 ([37870536](https://pubmed.ncbi.nlm.nih.gov/37870536)), 41% falling to 8.3% by tier in MyPathway ([37793085](https://pubmed.ncbi.nlm.nih.gov/37793085)).

#### Likelihood of desired effect

Unknown. Nothing has been measured in this histology; the row exists because it is the HER2 modality that survives the file's constraints if the axis continues at all.

#### Toxicity profile

- Lymphodepleting conditioning with its cytopenia window, and CRS. High burden by construction.
- No deruxtecan payload, so the unresolved chest CT does not price it; no MMAE, so the neuropathy veto is clear.

#### Counter-productive mechanisms / dissent

Advocate alone ranked it; conservative's blanket decline of phase-1 cell therapy stands opposite. A quieter mechanism concern: lymphodepletion could blunt the vaccine-primed T-cell compartment the patient has spent a year building.

#### Practical considerations

Allogeneic — no apheresis, no manufacturing wait. Yale, MSK and Jefferson are enrolling, and prior HER2-directed therapy is not an exclusion, which separates it from every HER2 antibody protocol in the registry. The prior cell-or-gene-therapy exclusion must be cleared against the ongoing mRNA vaccine series before a screening slot is booked.

#### Why this rank

Single-persona endorsement, no efficacy data, and conditioning toxicity put it below the payload-free HER2 rows that share its gate.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| FT825 / ONO-8250 | None (phase 1, no urothelial signal) | Lymphodepletion cytopenias, CRS | [NCT06241456](https://clinicaltrials.gov/study/NCT06241456) |

### Rank 9. ASP2998 (TROP2-directed STING agonist conjugate)

*The TROP2 door that stays open after T-DXd — with the low-positive hedge doing real work.*

#### Evidence base

Phase 1, no efficacy data ([NCT07287995](https://clinicaltrials.gov/study/NCT07287995)). Urothelial carcinoma is a named escalation and expansion histology with no cap on prior regimens, and prior TROP2- or topoisomerase-I-directed therapy is explicitly permitted. The class context cuts both ways: TROPHY-U-01's biomarker analysis found benefit across TROP2 expression levels ([39086310](https://pubmed.ncbi.nlm.nih.gov/39086310)), but nearly everyone in that analysis sat well above this patient's weak signal, and the class's confirmatory phase 3 missed OS ([39934055](https://pubmed.ncbi.nlm.nih.gov/39934055)).

#### Likelihood of desired effect

Low-to-unknown. Expression-agnostic entry is not the same as expression-agnostic benefit: a low-positive TROP2 result is a weaker, less reliable predictor than a strong one, and the validated 2026-08 tier should be retrieved before this axis gets weight.

#### Toxicity profile

- No human safety data. An immune-agonist payload in a patient with 2025 checkpoint-associated pancreatitis engages the pancreatitis veto as a monitoring condition: q3-4wk lipase surveillance belongs in the plan.
- Assignment to an enfortumab vedotin combination arm would violate the neuropathy veto — the arm preference has to be settled with the site, in writing, before consent.

#### Counter-productive mechanisms / dissent

Advocate alone ranked it. The critic's class-level caution (TROP2 response rates that never moved survival) and the conservative's phase-1 decline both apply unrecorded.

#### Practical considerations

New York and New Jersey sites. Monotherapy or the pembrolizumab arm are the acceptable assignments; the EV arms are not.

#### Why this rank

Bottom of the live-trial tier: single endorsement, no data, and a target the patient may barely express.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| ASP2998 | None (phase 1) | No human data; immune-agonist class, pancreatitis watch | [NCT07287995](https://clinicaltrials.gov/study/NCT07287995) |

### Rank 10. Nivolumab + ipilimumab re-intensification — lower-ipilimumab schedule only

*Two vetoes on record against the nivo1/ipi3 boost; the ranked form is the schedule both vetoing personas named as the acceptable one.*

#### Evidence base

TITAN-TCC tested the exact maneuver in question — an ipilimumab boost after PD-1 failure in urothelial carcinoma — and met its registered endpoint: ITT ORR 33% (90% CI 24-42, p=0.0049 against a prespecified 20% bar), at the cost of 11% grade 3-4 immune enterocolitis and both treatment-related deaths (2/83) ([36868252](https://pubmed.ncbi.nlm.nih.gov/36868252)). CheckMate 032 supplies the dose-response: 38.0% at nivo1/ipi3, 26.9% at nivo3/ipi1, 25.6% for nivolumab alone ([31100038](https://pubmed.ncbi.nlm.nih.gov/31100038)). Both trials enrolled post-platinum patients; this patient skipped that line, and progression here was on pembrolizumab maintenance, not nivolumab.

#### Likelihood of desired effect

Uncertain, with an honest asymmetry: the 33% belongs to the vetoed high-dose schedule in a population this patient does not match, and the tolerable schedule never beat monotherapy anywhere in the class. TMB 12.4 mut/Mb and a deep prior IO response argue the biology is receptive; the maintenance progression argues the easy gains are taken.

#### Toxicity profile

- **Two stated vetoes are engaged by the boost schedule:** grade 3-4 enterocolitis 11% with both trial deaths sits on the severe-GI veto, and the 2025 immune-mediated pancreatitis (lipase peak 384 U/L) sits on the pancreatitis veto.
- Grade 3-4 treatment-related AEs 39.1% at nivo1/ipi3.
- The ranked lower-ipilimumab form requires protocolized q3-4wk amylase/lipase surveillance and written stopping rules as formal conditions, not habits.

#### Counter-productive mechanisms / dissent

The most contested row on the board. Conservative vetoed the nivo1/ipi3 boost, lifted only for a lower-ipilimumab schedule with protocolized surveillance and stopping rules; advocate vetoed the same schedule for engaging two vetoes at once and named the identical modified form as the only acceptable one. This row is that form — the override is the modification the vetoing personas themselves specified, and the boost stays off the table. The critic's counter-dissent persists: every response signal in the class came from ipilimumab 3 mg/kg, so cutting the dose deletes the only arm that ever beat monotherapy while keeping added irAE exposure. Concensusite's dissent also persists: no NCCN listing in any line, and prescribing the doublet off-protocol buys TITAN-TCC's toxicity without its monitoring scaffold.

#### Practical considerations

Both drugs are prescribable today with no screening assay, manufacturing slot, or washout beyond clinical judgment — the only row with that property, and why three personas ranked it. The registered route is [NCT03866382](https://clinicaltrials.gov/study/NCT03866382) (cabozantinib + nivolumab + ipilimumab, variant-histology cohorts), but its cohorts require roughly 50% variant morphology and this pathology shows focal plasmacytoid and giant-cell areas only. Payer friction off-label is part of the safety picture.

#### Why this rank

Two vetoes at double weight put its agreement score at -0.4, below every single-endorsement trial row; it stays ranked rather than rejected because the vetoing personas themselves specified the conditions under which they would allow it.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Nivo + ipi boost (TITAN-TCC schema) | ITT ORR 33% (90% CI 24-42) post-PD-1 | Enterocolitis 11% G3-4; 2/83 TR deaths | [36868252](https://pubmed.ncbi.nlm.nih.gov/36868252) |
| Nivo1/ipi3 (CheckMate 032) | ORR 38.0% vs 25.6% mono | G3-4 TRAEs 39.1% | [31100038](https://pubmed.ncbi.nlm.nih.gov/31100038) |
| Cabozantinib + nivo/ipi (registered route) | Variant-histology cohorts | Requires ~50% variant morphology | [NCT03866382](https://clinicaltrials.gov/study/NCT03866382) |

### Rank 12. Personalized neoantigen vaccine programs (ongoing) — continuation, not initiation

*Already running; the post-mRNA EliSpot is the branch point, and the honest framing is hypothesis-stage.*

#### Evidence base

The class evidence is real but belongs to other settings: vaccine-induced neoantigen-specific immunity in urothelial cancer ([40346292](https://pubmed.ncbi.nlm.nih.gov/40346292)), the Rojas pancreatic responder-nonresponder split ([37165196](https://pubmed.ncbi.nlm.nih.gov/37165196)), and randomized adjuvant-melanoma support with durable 5-year RFS benefit ([42223134](https://pubmed.ncbi.nlm.nih.gov/42223134)). This patient's own readout so far: CD4+ responses in 2 of 14 evaluable pools at 4 months, CD4-skewed, with ctDNA rising through most of the vaccine period.

#### Likelihood of desired effect

Low for objective response, on the record as it stands — no response evidence is attributable to vaccination, and the patient's EliSpot sits at the weak end of the published distribution. The value of the axis is optionality: it feeds the vaccine-primed TIL/ACT programs the patient is actively pursuing with banked material.

#### Toxicity profile

- Injection-site and constitutional reactions; the mildest profile on the board.

#### Counter-productive mechanisms / dissent

No persona ranked continuation as a therapeutic recommendation; the board treated it as running background and the critic's appraisal stands in full. CD4-skewed responses without CD8 expansion may simply not translate to tumor killing.

#### Practical considerations

Continues under the programs' own protocols; blood-based monitoring fits the tissue-scarcity constraint. One interaction to manage deliberately: continued vaccine dosing may trip prior-gene-therapy exclusions on cell-therapy protocols (the FT825 and NT-175 rows both carry that question).

#### Why this rank

Below every board-ranked row because nobody endorsed it as a rec; above the rejected rows because it is already underway, preference-aligned, and produces the next decision-relevant readout in the case.

#### Per-trial detail

No registered trial row in this dossier — administered under the two programs' own protocols, with serial EliSpot monitoring.

## Also considered — not ranked (feature-targeting investigational)

Thirty-nine feature-targeting investigational options were surfaced but not ranked as live top-tier choices. Ranks 11 and 13-15 (sacituzumab tirumotecan, trastuzumab + paclitaxel, sacituzumab govitecan, datopotamab deruxtecan) were assessed and rejected on their own records and appear in the ranked table as `not_recommended` — sac-TMT carries the board's third veto (risktaker: randomization can assign a taxane against established CIPN; also ineligible, no prior platinum).

**Blocked from enrollment (`not_enrollable`):**

- **AVZO-103 (Nectin-4 x TROP2 bispecific ADC, NCT07193511)** — the dual-target agent two personas wanted to rank; blocked solely by a drug-induced-ILD exclusion against the unresolved 2026-03 chest CT read. Converts to a live candidate if pulmonology adjudicates the CT clean.
- **Disitamab vedotin (NCT04879329)** — best HER2 ORR in the disease (50.5%), but MMAE neuropathy (68.2% any-grade) hits the CIPN veto and every US cohort excludes prior HER2 therapy and prior MMAE ADC.
- **Neoantigen-selected TIL (NCT01174121)** — requires a resectable lesion; the only known disease is a post-SBRT node.
- **Brenetafusp (NCT04262466)** — no enrollable solid-tumor slot; active registration work is melanoma/sarcoma-restricted.
- **SynKIR-110 (NCT05568680)** — histology list closed; urothelial excluded regardless of stain.
- **NEOK002 (NCT07612189)** — excluded while the most recent systemic therapy is a topoisomerase-I-payload ADC.
- **XYA02 (NCT07670312)** — not yet open; Australia.
- **EB-DT-NK-UC101 (NCT07492628)** — the most permissive eligibility on the list (prior EV and prior HER2 both allowed), from a program a US patient cannot currently reach.
- **Ceralasertib** — class clinical signal (14% ORR) confined to gynecologic histologies; informational for the ARID1A axis.
- **Tuvusertib + avelumab (NCT06518564)** — the one ARID1A-selected trial, restricted to endometrial cancer.

**Consolidated into a ranked approach (`consolidated`):**

- **NT-175 TCR-T (NCT05877599)** — same R175H x A\*02:01 axis as rank 4, with lymphodepletion, a manufacturing wait, and a gene-therapy exclusion the vaccine series may trip.
- **CRB-701 (NCT06265727)** — Nectin-4 ADC that keeps the MMAE payload the ranked agent replaced.
- **E303 (NCT07524348)** — backup Nectin-4 ADC door if NEXUS-01 screening fails.

**No peer-reviewed clinical efficacy / double-gated (`thin_evidence`):**

- **IMA203 PRAME TCR-T (NCT03686124)** — HLA gate met, PRAME expression unread; published ORR 28.9% with mDOR 4.4 months is melanoma/sarcoma only. The MAGE-A4 lesson applies: expression first.
- **IMC-P115C (NCT07156136)** — successor PRAME ImmTAC, open phase 1, same unread gate.
- **CT-95, TNhYP218, A2B694 (mesothelin bispecific and CAR-T trials)** — all wait on a validated mesothelin stain; the class record is a negative expression-selected RCT and a 0/20 CAR-T series.
- **DS-3939a (NCT05875168)** — the one active MUC1 ADC; confirmation-first, and its DXd-class payload re-runs the current drug's problems.
- **CT-202 (NCT07545122)** — payload-free Nectin-4 bispecific, nothing measured yet.
- **LCB84 (NCT05941507)** — backup TROP2 door, permissive entry, no data.
- **CAdVEC + HER2 CAR-VST (NCT03740256)** — tolerates a 2+ tier, but needs an injectable lesion and a single Texas site.
- **N-803 / IL-15 superagonist (NCT03228667)** — the immune-intensification adjunct already under single-patient-IND discussion; no metastatic efficacy base in the dossier.
- **FAP radioligand therapy (NCT04939610)** — an imaging question wearing a therapy costume: no FAP-avid urothelial disease has ever been shown in this patient, and the prior FAPi PET signal was granulomatous inflammation.
- **ART0380 (NCT04657068), PARP + temozolomide, tazemetostat** — the ARID1A synthetic-lethality shelf, all hypothesis-grade; the somatic-HR readout in the rank-1 retrieval is the cheap test of whether any of it applies.

**Program not available (`unavailable`):** gavo-cel (deprioritized post-merger), huCART-meso (0/20 ORR, no recruiting protocol), anetumab ravtansine (discontinued after the negative ARCS-M RCT), gatipotuzumab, the MUC1-CD40L vaccine, GO-203-class MUC1-C inhibition, berzosertib, and five preclinical-only constructs (Nectin-4 CAR-T, ETx-22, Nectin-4 NIR-PIT, R7059-DXd, mesothelin DARPin-MMAE conjugates).

## Ranked prioritization

**Shared first step**

| Rank | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
|---|---|---|---|---|---|
| 1 | **HER2 reconciliation + sequencing-report retrieval — decision gate**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | Certain to inform: the tier decides on-label versus cross-tumor footing for every HER2 row, and the FGFR3 readout could open the strongest genomic branch (NCT05614739). | Low (none — records retrieval and IHC on existing tissue) | **N/A** (Workup, not a therapy.) | **Both gating answers already exist in a drawn stain and unretrieved reports; retrieving them beats spending scarce tissue or a trial slot on any branch below.** |

**Ranked options**

| Rank | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
|---|---|---|---|---|---|
| 2 | **Zanidatamab** (conditional on her2_ihc positive)<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span></small> | Moderate if 3+ holds: ORR 37.0% (95% CI 27.0-48.7) in phase 1 (pmid:36400106), biliary-weighted; untested after T-DXd. | Low (grade-3 TRAEs in 4/132, no treatment-related deaths; LVEF monitoring) | **Low** (ADC-selected HER2 downregulation would blunt a payload-free bispecific; untested after T-DXd.) | **The payload-free way to stay on a confirmed HER2 3+ axis when T-DXd stops for tolerability — clean safety file, thin urothelial evidence, trial door closed by prior T-DXd.** |
| 3 | **[225Ac]Ac-AKY-1189 (Nectin-4 radioligand)**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small> | Unknown — first-in-human with zero efficacy data; a mechanism bet that alpha crossfire survives partial Nectin-4 loss after 25 months of EV (pmid:41173324). | Moderate (no human safety table; alpha-radioligand class marrow suppression and renal exposure, with eGFR unmeasured) | **Low** (Subtherapeutic dose-escalation assignment could spend the post-T-DXd window without benefit.) | **The one Nectin-4 route insulated from both MMAE neuropathy and antigen heterogeneity, with an imaging step that answers the expression question tissue-free — and no efficacy data at all.** |
| 4 | **CLSP-1025 (TP53 R175H x HLA-A\*02:01 engager)**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small> | Unknown, and gated twice: no clinical data for the class, and the R175H call is one 0.09% VAF plasma read pending tissue confirmation. | Moderate (expected CRS with inpatient step-up dosing; no human safety table yet) | **Moderate** (Very low peptide-HLA density and unmeasured HLA-A\*02 LOH could cap engager potency.) | **A truncal-driver bet with both eligibility gates already on file — but the R175H call is a single 0.09% VAF plasma read and the class has no clinical results yet.** |
| 5 | **LY4052031 (Nectin-4 ADC, NEXUS-01 B2)**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span></small> | Moderate but unstable: 47% post-EV ORR is unpublished dose-escalation data (NCT06465069); target validation is RCT-grade, the agent estimate is not. | Moderate (camptothecin-class diarrhea, nausea, neutropenia; no published safety table yet) | **Moderate** (Sequential topoisomerase-I payloads after T-DXd risk cross-resistance; current Nectin-4 expression unverified.) | **The trial written for his exact post-EV history with a payload that clears the neuropathy veto — carried by RCT-grade target validation, not by published data on this drug.** |
| 6 | **Pertuzumab + trastuzumab (TAPUR)** (conditional on her2_ihc positive)<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span></small><br><small><em>dissent:</em> <span class="persona persona-risktaker">risktaker</span></small> | Moderate at amplified 3+ (ORR 41.0%, MyPathway pmid:37793085); collapses to 8.3% at 1+; untested after a HER2 ADC. | Low (diarrhea 36.1% mostly low-grade; no serious term above 1.7%; LVEF monitoring) | **Low** (ADC-selected HER2 loss would gut a naked-antibody doublet; the tier gradient is steep.) | **The one HER2 route that touches none of the four vetoes, with a protocolized TAPUR path — its floor set by the pending tier and the unread ERBB2 copy number.** |
| 7 | **FGFR3 axis — vepugratinib (FORAGER-1)**<br><small><em>endorse:</em> <span class="persona persona-concensusite">concensusite</span></small> | Conditional: ~15-20% chance a qualifying FGFR3 alteration exists; if found, both guideline bodies endorse the axis in exactly this line (NCT05614739). | Moderate (FGFR-class hyperphosphatemia, stomatitis, nail and eye toxicity; no agent-specific table in the dossier) | **Low** (None plausible before the gate; expected yield is the limiter.) | **A records request away from being real: FGFR3 status is simply unread, and the FGFR axis is the only non-HER2 route both major guidelines endorse in this line.** |
| 8 | **FT825 (off-the-shelf HER2 CAR-T)** (conditional on her2_ihc positive)<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span></small> | Unknown — phase 1 with no urothelial signal; benefit is expected to track the pending HER2 tier (pmid:37870536). | High (lymphodepletion cytopenias and CRS; no mature safety table) | **Low** (Lymphodepletion could blunt the concurrently primed vaccine T-cell axis.) | **The HER2 cell-therapy route that survives the file's constraints — no apheresis, no deruxtecan payload — and nothing measured in urothelial cancer yet.** |
| 9 | **ASP2998 (TROP2 STING conjugate)**<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span></small> | Low-to-unknown: no clinical data, and low-positive TROP2 is a weaker predictor even where entry is expression-agnostic (pmid:39086310). | Moderate (no human data; immune-agonist class inflammatory events with a pancreatitis-history watch) | **Low** (Weak TROP2 may limit conjugate delivery regardless of payload class.) | **The TROP2 door that stays open after T-DXd — expression-agnostic entry, with the low-positive hedge stated and the MMAE combination arms declined in writing.** |
| 10 | **Nivolumab + ipilimumab (lower-ipi schedule)**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span></small><br><small><em>dissent:</em> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>veto:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-advocate">advocate</span></small> | Uncertain: the 33% ORR (pmid:36868252) belongs to the vetoed ipi-3 boost in post-platinum, post-nivolumab patients; the tolerable schedule never beat monotherapy. | High (immune enterocolitis 11% grade 3-4 with 2/83 treatment-related deaths at ipi-3; pancreatitis rechallenge risk) | **Moderate** (Dose-reducing ipilimumab may delete the CTLA-4 contribution that ever beat PD-1 monotherapy.) | **Prescribable now with no screening gate, but the efficacy evidence and both vetoes attach to the same high-dose schedule; the tolerable version is the unproven one.** |
| 11 | **Sacituzumab tirumotecan phase 3 (NCT07419295)** — not recommended<br><small><em>endorse:</em> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>veto:</em> <span class="persona persona-risktaker">risktaker</span></small> | Not applicable as ranked: ineligible (no prior platinum) and the randomization veto stands; class OS evidence is negative (pmid:39934055). | High (potential taxane-arm CIPN on randomization; class grade-5 TEAEs 7% in TROPiCS-04) | **High** (Taxane-arm assignment would inflict the vetoed neuropathy and could end all ADC options after.) | **Randomized entry is the guideline-clean route to TROP2, but this trial can assign a taxane he cannot take and requires platinum he never had.** |
| 12 | **Personalized neoantigen vaccine programs (ongoing)** | Low for objective response: no response evidence attributable to vaccination; the patient's own EliSpot sits at the weak end of the published distribution (pmid:37165196). | Low (injection-site and constitutional reactions in the trials on record) | **Low** (CD4-skewed responses without CD8 expansion may not translate to tumor killing.) | **Already underway and preference-aligned; honest framing is hypothesis-stage, with the post-mRNA EliSpot as the branch point for any TIL/ACT escalation.** |
| 13 | **Trastuzumab + paclitaxel** — not recommended | Moderate response plausible at 3+ but irrelevant: the taxane backbone lands on the stated neuropathy veto (pmid:37385153). | Moderate (any-grade neuropathy 88.9% from the taxane backbone — the vetoed toxicity class) | **Low** (None mechanism-level; the disqualifier is the taxane-neuropathy collision.) | **An accessible HER2 doublet disqualified by its backbone: 88.9% any-grade neuropathy against established CIPN.** |
| 14 | **Sacituzumab govitecan** — not recommended | Low: the confirmatory phase 3 missed OS (HR 0.86, p=0.087) and the urothelial approval was withdrawn (pmid:39934055). | High (grade-5 TEAEs 7% in TROPiCS-04, mostly neutropenic infection; diarrhea, neutropenia) | **Moderate** (Response without survival — the surrogate trap; low TROP2 weakens the predictor further.) | **The TROP2 class's own confirmatory test came back negative in this disease; a slot spent here competes with better-fitted doors.** |
| 15 | **Datopotamab deruxtecan** — not recommended | Unknown in urothelial carcinoma; low-positive TROP2 and back-to-back deruxtecan payloads argue against prioritizing it. | Moderate (deruxtecan-class nausea, stomatitis and ILD risk — the toxicities already limiting T-DXd) | **Low** (Sequential deruxtecan payloads invite cross-resistance and cumulative ILD exposure.) | **Reaches the TROP2 axis only by re-running the exact payload toxicities that are already dose-limiting on the current drug.** |

**Also considered — not ranked** (flagged rows; full detail in the recommendations table)

| Rank | Intervention | Flag | Overall |
|---|---|---|---|
| 16 | **AVZO-103 (Nectin-4 x TROP2 ADC)** | not_enrollable | The dual-target ADC two personas wanted to rank — blocked solely by an ILD exclusion against an unresolved CT read. |
| 17 | **Disitamab vedotin** | not_enrollable | The strongest HER2 number in the disease, foreclosed twice over: MMAE against established CIPN, and US exclusions for prior HER2 and MMAE therapy. |
| 18 | **Neoantigen-selected TIL** | not_enrollable | The ACT route the banked material points at, waiting on a lesion that no longer exists to resect. |
| 19 | **Brenetafusp** | not_enrollable | The PRAME ImmTAC the field is actually developing — with no door open to a urothelial patient today. |
| 20 | **NT-175 (TP53 R175H TCR-T)** | consolidated | The autologous fallback for the rank-4 axis — same gates, more toxicity, longer runway. |
| 21 | **CRB-701** | consolidated | A tidier linker on the payload the file vetoes; the ranked Nectin-4 ADC changed the payload instead. |
| 22 | **E303** | consolidated | The backup sponsor for the rank-5 approach if NEXUS-01 screening fails. |
| 23 | **IMA203 (PRAME TCR-T)** | thin_evidence | A real PRAME door once expression reads positive — today it is double-gated with cross-tumor-only evidence. |
| 24 | **IMC-P115C** | thin_evidence | The open-door PRAME option if expression ever confirms — nothing measured yet. |
| 25 | **CT-95 (mesothelin x CD3)** | thin_evidence | A mesothelin door that opens only after a validated stain — and the class record so far is negative. |
| 26 | **TNhYP218** | thin_evidence | A next-generation construct aimed at a target whose urothelial case is still a research-grade stain. |
| 27 | **A2B694** | thin_evidence | The most conditional mesothelin row: stain, screening protocol, and tumor genetics all unverified. |
| 28 | **DS-3939a (TA-MUC1 ADC)** | thin_evidence | The only active MUC1 ADC — confirmation-first, and its payload re-runs the current drug's problems. |
| 29 | **CT-202** | thin_evidence | The gentlest Nectin-4 concept on paper, with nothing measured behind it yet. |
| 30 | **LCB84** | thin_evidence | A backup TROP2 door with permissive entry and no data. |
| 31 | **CAdVEC + HER2 CAR-VST** | thin_evidence | The one HER2 row that tolerates a 2+ tier — behind an injectable-lesion gate and a single Texas site. |
| 32 | **N-803 / IL-15 superagonist** | thin_evidence | The immune-intensification adjunct the team is already exploring — no metastatic evidence base to rank it on. |
| 33 | **FAP radioligand therapy** | thin_evidence | An imaging question wearing a therapy costume: no FAP-avid urothelial disease has ever been shown in this patient. |
| 34 | **ART0380** | thin_evidence | A hypothesis-grade door that does not require its own hypothesis to enter. |
| 35 | **Tuvusertib + avelumab** | not_enrollable | The ARID1A trial that actually selects for ARID1A — closed to this histology. |
| 36 | **PARP inhibition (ARID1A rationale)** | thin_evidence | A borrowed synthetic-lethality argument waiting on a somatic HR readout that already exists in an unretrieved report. |
| 37 | **Tazemetostat (ARID1A rationale)** | thin_evidence | The mildest drug on the weakest rationale in the case. |
| 38 | **SynKIR-110** | not_enrollable | A closed door regardless of the stain. |
| 39 | **NEOK002** | not_enrollable | Closed by the current drug's payload class, not by the target. |
| 40 | **XYA02** | not_enrollable | A door that has not opened, on another continent. |
| 41 | **EB-DT-NK-UC101** | not_enrollable | The most permissive eligibility on the list, attached to a program he cannot reach. |
| 42 | **Ceralasertib** | not_enrollable | Cross-tumor evidence for someone else's tumor type. |
| 43-54 | **gavo-cel, huCART-meso, anetumab ravtansine, mesothelin DARPin conjugates, gatipotuzumab, MUC1-CD40L vaccine, MUC1-C inhibition, berzosertib, Nectin-4 CAR-T, ETx-22, Nectin-4 NIR-PIT, R7059-DXd** | unavailable | Not reachable by any enrollment or access route on record. |

!!! note "Reading the columns"
    **Toxicity burden** is patient-level adverse-event severity from the cited evidence; **Counter-productive MoA** is mechanism-level risk to the therapeutic goal (antigen loss, cross-resistance, immune blunting), which is a different axis. The persona pills under each intervention are the at-a-glance board signal; full per-persona rationale lives on the [board page](board.md).

## Caveats

- **Evidence-base caveats.** The strongest ranked efficacy figure (47%, rank 5) is an unpublished conference abstract from a sponsor-run dose escalation with no confidence interval. The HER2 tier-response data are single-arm baskets (DESTINY-PanTumor02, MyPathway) with ORR surrogates; the bladder IHC 3+ estimate behind the whole HER2 branch rests on 16 patients (95% CI 29.9-80.2). Ranks 3, 4, 8 and 9 carry no clinical efficacy data at all. The checkpoint-boost data come from post-platinum, post-nivolumab populations this patient does not match.
- **Compartment / biomarker dependencies.** Ranks 2, 6 and 8 assume contemporary HER2 confirmation; ranks 3 and 5 assume retained Nectin-4 after 25 months of EV (unverified — both stains predate exposure); rank 4 assumes R175H is real and truncal on the strength of one 0.09% VAF plasma read; rank 7 assumes an FGFR3 alteration that has an ~15-20% prior; rank 9 assumes a low-positive TROP2 signal means something. The mesothelin, MUC1, PRAME and FAP leads are research-assay-only and confirmation-first by construction.
- **What would change the ranking.** (1) The 2026-08 HER2 tier: a confirmed 3+ hardens ranks 2/6/8 and the standard-of-care T-DXd question; a downgrade forecloses them and shifts weight to the Nectin-4 and R175H rows. (2) The sequencing retrieval: a qualifying FGFR3 alteration would vault the FGFR axis over most of this list, per three personas' own notes. (3) A published NEXUS-01 expansion with a safety table would move rank 5 up and could make it the lead therapeutic. (4) A clean pulmonology adjudication of the chest CT converts AVZO-103 from flagged to rankable.
- **Re-scoping caveat.** All preferences are inferred, not stated; if the patient confirms different toxicity priorities (for instance accepts taxane risk, or rejects CRS-bearing trials), the veto structure that ordered ranks 10-13 changes and the case should be re-run.

## Sources

**PMIDs:** [27958275](https://pubmed.ncbi.nlm.nih.gov/27958275), [31100038](https://pubmed.ncbi.nlm.nih.gov/31100038), [31996390](https://pubmed.ncbi.nlm.nih.gov/31996390), [32506298](https://pubmed.ncbi.nlm.nih.gov/32506298), [32568634](https://pubmed.ncbi.nlm.nih.gov/32568634), [33577729](https://pubmed.ncbi.nlm.nih.gov/33577729), [33649166](https://pubmed.ncbi.nlm.nih.gov/33649166), [33929895](https://pubmed.ncbi.nlm.nih.gov/33929895), [34385340](https://pubmed.ncbi.nlm.nih.gov/34385340), [35358455](https://pubmed.ncbi.nlm.nih.gov/35358455), [35397434](https://pubmed.ncbi.nlm.nih.gov/35397434), [35749374](https://pubmed.ncbi.nlm.nih.gov/35749374), [36307410](https://pubmed.ncbi.nlm.nih.gov/36307410), [36400106](https://pubmed.ncbi.nlm.nih.gov/36400106), [36868252](https://pubmed.ncbi.nlm.nih.gov/36868252), [37165196](https://pubmed.ncbi.nlm.nih.gov/37165196), [37306706](https://pubmed.ncbi.nlm.nih.gov/37306706), [37385153](https://pubmed.ncbi.nlm.nih.gov/37385153), [37501016](https://pubmed.ncbi.nlm.nih.gov/37501016), [37793085](https://pubmed.ncbi.nlm.nih.gov/37793085), [37870536](https://pubmed.ncbi.nlm.nih.gov/37870536), [37988648](https://pubmed.ncbi.nlm.nih.gov/37988648), [38446675](https://pubmed.ncbi.nlm.nih.gov/38446675), [39086310](https://pubmed.ncbi.nlm.nih.gov/39086310), [39440991](https://pubmed.ncbi.nlm.nih.gov/39440991), [39934055](https://pubmed.ncbi.nlm.nih.gov/39934055), [40081946](https://pubmed.ncbi.nlm.nih.gov/40081946), [40169866](https://pubmed.ncbi.nlm.nih.gov/40169866), [40205198](https://pubmed.ncbi.nlm.nih.gov/40205198), [40346292](https://pubmed.ncbi.nlm.nih.gov/40346292), [40635151](https://pubmed.ncbi.nlm.nih.gov/40635151), [40849430](https://pubmed.ncbi.nlm.nih.gov/40849430), [40862536](https://pubmed.ncbi.nlm.nih.gov/40862536), [40931013](https://pubmed.ncbi.nlm.nih.gov/40931013), [41101697](https://pubmed.ncbi.nlm.nih.gov/41101697), [41173324](https://pubmed.ncbi.nlm.nih.gov/41173324), [41542775](https://pubmed.ncbi.nlm.nih.gov/41542775), [41566776](https://pubmed.ncbi.nlm.nih.gov/41566776), [41686845](https://pubmed.ncbi.nlm.nih.gov/41686845), [42167230](https://pubmed.ncbi.nlm.nih.gov/42167230), [42223134](https://pubmed.ncbi.nlm.nih.gov/42223134)

**NCTs:** [NCT01174121](https://clinicaltrials.gov/study/NCT01174121), [NCT02693535](https://clinicaltrials.gov/study/NCT02693535), [NCT02892123](https://clinicaltrials.gov/study/NCT02892123), [NCT03228667](https://clinicaltrials.gov/study/NCT03228667), [NCT03390504](https://clinicaltrials.gov/study/NCT03390504), [NCT03547973](https://clinicaltrials.gov/study/NCT03547973), [NCT03686124](https://clinicaltrials.gov/study/NCT03686124), [NCT03740256](https://clinicaltrials.gov/study/NCT03740256), [NCT03866382](https://clinicaltrials.gov/study/NCT03866382), [NCT04262466](https://clinicaltrials.gov/study/NCT04262466), [NCT04482309](https://clinicaltrials.gov/study/NCT04482309), [NCT04657068](https://clinicaltrials.gov/study/NCT04657068), [NCT04879329](https://clinicaltrials.gov/study/NCT04879329), [NCT04939610](https://clinicaltrials.gov/study/NCT04939610), [NCT05489211](https://clinicaltrials.gov/study/NCT05489211), [NCT05568680](https://clinicaltrials.gov/study/NCT05568680), [NCT05614739](https://clinicaltrials.gov/study/NCT05614739), [NCT05875168](https://clinicaltrials.gov/study/NCT05875168), [NCT05877599](https://clinicaltrials.gov/study/NCT05877599), [NCT05941507](https://clinicaltrials.gov/study/NCT05941507), [NCT06051695](https://clinicaltrials.gov/study/NCT06051695), [NCT06241456](https://clinicaltrials.gov/study/NCT06241456), [NCT06265727](https://clinicaltrials.gov/study/NCT06265727), [NCT06465069](https://clinicaltrials.gov/study/NCT06465069), [NCT06518564](https://clinicaltrials.gov/study/NCT06518564), [NCT06695845](https://clinicaltrials.gov/study/NCT06695845), [NCT06756035](https://clinicaltrials.gov/study/NCT06756035), [NCT06778863](https://clinicaltrials.gov/study/NCT06778863), [NCT06885697](https://clinicaltrials.gov/study/NCT06885697), [NCT07020117](https://clinicaltrials.gov/study/NCT07020117), [NCT07156136](https://clinicaltrials.gov/study/NCT07156136), [NCT07193511](https://clinicaltrials.gov/study/NCT07193511), [NCT07287995](https://clinicaltrials.gov/study/NCT07287995), [NCT07419295](https://clinicaltrials.gov/study/NCT07419295), [NCT07492628](https://clinicaltrials.gov/study/NCT07492628), [NCT07524348](https://clinicaltrials.gov/study/NCT07524348), [NCT07545122](https://clinicaltrials.gov/study/NCT07545122), [NCT07612189](https://clinicaltrials.gov/study/NCT07612189), [NCT07670312](https://clinicaltrials.gov/study/NCT07670312), [NCT07686367](https://clinicaltrials.gov/study/NCT07686367)

## Transparency artifacts

- [Trial table](trials.md) — 40 rows, all columns
- [Evidence dossier](evidence.md) — 48 clinical + 41 preclinical rows
- [Master manuscripts table](manuscripts.md) — every paper considered, with n, effect, variance and toxicity columns
- [Board proceedings](board.md) — 5 positions, 20 cross-critiques, full agreement matrix
- [Recommendations table](recommendations.md) — this ranking in sortable form
- [Biomarker survey](biomarker_survey.md) — the measured-vs-unmeasured biomarker inventory
- [Target validation paths](target_validation.md) — the diagnostic workup report behind rank 1
- [Access guide](accessibility.md) — 56 access rows with contacts
- Plain language (plain_language.md) — produced by the translator on its run

## Run log

Authored 2026-08-20 by the PI agent from the full dossier (profile, preferences, 24 target-validation rows, 40 trials, 48 clinical and 41 preclinical evidence rows, 56 access rows, 5 board positions, 20 critiques). Biomarker gating: HER2 (`ihc_pending`, discordant) chosen as the single branched dimension; TROP2, mesothelin, MUC1, PRAME, FAP and current Nectin-4 status carried as open questions on their rows. Routed to the standard-of-care table per the two-table contract: trastuzumab deruxtecan (tumor-agnostic IHC 3+ approval, NCCN-carried — every persona's continuation pick), enfortumab vedotin (including rechallenge), pembrolizumab (TMB-H and urothelial listings), and erdafitinib conditional on FGFR3. No non-targeting scope leaks found in the dossier. Vetoes handled: conservative and advocate vetoes on the nivo1/ipi3 boost overridden only by adopting the vetoing personas' own named conditions (lower-ipilimumab schedule, protocolized surveillance, written stopping rules) at rank 10; risktaker's veto on sac-TMT randomization stands at rank 11 as not_recommended. Picked rows ranked by the agreement formula with preference-fit tie-breaks; unpicked documentation rows follow at ranks 12-15; 39 flagged rows carry stable rank integers 16-54. Reference check: 45 PMIDs and 40 NCTs verified against PubMed and ClinicalTrials.gov (existence + identity); one claim-drift corrected (NCT06518564 is endometrial-restricted — row reflagged not_enrollable); zero unresolved identifiers.

<!-- libby:downloads:begin -->

## Downloads

### HTML

- [Target validation paths](target_validation.md?v=5a947ddc) — per-feature biomarker-workup table with providers and references, sortable in-browser
- [Selected general biomarker report](biomarker_survey.md?v=6e2ecaae) — which panel biomarkers this patient has and has not been tested for, including the tumor-agnostic ones, in a sortable in-browser table
- [Selected general biomarker report (offline)](urothelial-mets-her2-discordant-kndl-biomarker-survey.html?v=61a61361) — same biomarker survey packaged as a self-contained HTML that opens offline
- [Recommendations table](urothelial-mets-her2-discordant-kndl-recommendations.html?v=44760f25) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Standard of care options](standard_of_care.md?v=89266e1c) — approved and guideline-endorsed strategies for this patient's situation, assessed for eligibility and sequencing, in a sortable in-browser table
- [Standard of care options (offline)](urothelial-mets-her2-discordant-kndl-standard-of-care.html?v=01289c4b) — same standard-of-care assessment packaged as a self-contained HTML that opens offline
- [Access guide](accessibility.md?v=9eddab30) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Access guide (offline)](urothelial-mets-her2-discordant-kndl-accessibility.html?v=ce9dd538) — same access-guide content packaged as a self-contained HTML that opens offline
- [Master manuscripts table](manuscripts.md?v=afc5eb72) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Master manuscripts table (offline)](urothelial-mets-her2-discordant-kndl-manuscripts.html?v=e4d61678) — same manuscripts inventory packaged as a self-contained HTML that opens offline

### PDF

- [Target validation paths](urothelial-mets-her2-discordant-kndl-target-validation.pdf?v=a9705d7e) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Selected general biomarker report](urothelial-mets-her2-discordant-kndl-biomarker-survey.pdf?v=1bc5dac4) — biomarker screening coverage and the gaps it leaves, in a print-friendly PDF
- [Recommendations table](urothelial-mets-her2-discordant-kndl-recommendations.pdf?v=2b334063) — ranked options + pipeline context + evidence in detail, in a print-friendly PDF
- [Standard of care options](urothelial-mets-her2-discordant-kndl-standard-of-care.pdf?v=8232d41c) — approved and guideline-endorsed strategies, their eligibility fit, and how they sequence against the targeted options, in a print-friendly PDF
- [Access guide](urothelial-mets-her2-discordant-kndl-accessibility.pdf?v=5bd75ed2) — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF
- [Master manuscripts table](urothelial-mets-her2-discordant-kndl-manuscripts.pdf?v=c4f9c1b0) — every paper considered — n, effect, variance, toxicities, in a print-friendly PDF
- [Patient/caregiver PDF](urothelial-mets-her2-discordant-kndl-plain-language.pdf?v=bd10bcdc) — plain-language summary

<!-- libby:downloads:end -->

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
