<meta name="robots" content="noindex">

# `hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq`

<!-- libby:case-output:begin -->

## Case output

- [Target validation paths (PDF)](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-target-validation.pdf?v=7a9f3ba4) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table (HTML)](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-recommendations.html?v=83b565ec) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Preclinical recommendations (HTML)](preclinical_recommendations.md?v=6e4babf2) — forward-looking horizon scan of earlier-than-clinical candidate drugs, compounds, and strategies, sortable in-browser
- [Access guide (HTML)](accessibility.md?v=c675a486) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, sortable in-browser
- [Access guide (offline HTML)](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-accessibility.html?v=4bcd4526) — same access-guide content as the in-browser page, packaged as a self-contained HTML that opens offline
- [Master manuscripts table (HTML)](manuscripts.md?v=4c89f134) — every paper considered — n, effect, variance, toxicities, sortable in-browser
- [Master manuscripts table (offline HTML)](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-manuscripts.html?v=bb3a11c6) — same manuscripts inventory as the in-browser page, packaged as a self-contained HTML that opens offline
- [Patient/caregiver PDF](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-plain-language.pdf?v=81b64e34) — plain-language summary

<!-- libby:case-output:end -->

## Research question

In R0-resected stage IIIc high-grade serous tubo-ovarian carcinoma after first-line carboplatin/paclitaxel/bevacizumab with on-study GEN-1, and with tumor NGS confirming a BRCA-wild-type but genomically-unstable, ER-positive, HER2-low (IHC 1+) tumor, which maintenance interventions could target the homologous-recombination/genomic-instability, VEGF, ER, on-study IL-12, and HER2-low axes?

## Patient profile (scrubbed)

- Age band 70-79, female; primary site ovary.
- High-grade serous carcinoma (tubo-ovarian / primary peritoneal; WT1+, PAX8+, SOX17+, CK7+).
- Stage IIIc, ECOG 1 (estimated). Status-post interval radical cytoreduction (TAH/BSO + omentectomy + bilateral ureterolysis) with R0 resection.
- Prior/current therapy: neoadjuvant carboplatin + paclitaxel + bevacizumab with GEN-1 (IMNN-001, investigational IL-12 immunogene) x4, best response PR; now post-debulking carboplatin + paclitaxel + GEN-1.
- **TP53 V157G (somatic)** — confirmed; defines HGSC biology, not a direct drug gate.
- **BRCA1/2 germline AND somatic — wild-type** — confirmed (74-gene germline panel + Altera tumor/normal exome). Forecloses BRCA-mutation-gated olaparib monotherapy (SOLO1).
- **HRD / genomic instability** — confirmed PRESENT but **qualitative only** (multiple chromosomal imbalances / frequent LOH); BRCA-proficient; **no validated quantitative GIS/HRD score** reported by Altera.
- **MSI/MMR** — MSS (confirmed); **TMB** — low, 1 mut/Mb (confirmed). Both foreclose tumor-agnostic checkpoint-inhibitor eligibility.
- **PIK3CA amplification (somatic, focal)** and **MAP2K4 deletion (somatic, focal)** — confirmed; investigational-only, no approved matched therapy in HGSC.
- **ER positive** (~80% nuclei, weak-moderate), **PR negative** — confirmed.
- **HER2-low (IHC 1+)** — confirmed; the surgical report scored 1+ as "negative" under gastric/pan-tumor scoring, but the case-level tier is HER2-low. **Altera could not evaluate HER2 (insufficient material), so the 1+ rests on a single specimen.** Below the IHC 3+ tumor-agnostic T-DXd threshold, so HER2-directed ADCs are investigational here.
- **FOLR1** negative (<75% PS2+) — confirmed; forecloses mirvetuximab on the current specimen.
- **CA-125** normalized on therapy (940 -> 11.6 U/mL); **Signatera ctDNA (MRD)** cleared to Not Detected.
- Organ function: eGFR 98, creatinine 0.49, AST 27, ALT 16, bilirubin 1.5, WBC 3.5.

## Preferences

- Efficacy/toxicity weight: 0.7 (efficacy-leaning, tolerability-aware given the age band).
- Toxicity vetoes: additional peripheral neuropathy; severe myelosuppression / febrile neutropenia.
- Modality constraints: oral or low-infusion-burden preferred; caution with thrombotic/bleeding-risk agents (high VTE history, prior IVC filter).
- Free text: efficacy-leaning overall but tolerability-aware; ECOG estimated at 1; the previously pending HRD / somatic-BRCA result was the highest-value open question.
- Trial preference: prefers trials.

<!-- libby:target-validation:begin -->

## Target validation paths

Every biomarker in this case has resulted, but two workups are still worth ordering before acting on the tumor's most contingent options. A validated genomic-instability score decides whether olaparib plus bevacizumab (PAOLA-1, NCT02477644) is available: a Myriad MyChoice CDx GIS of at least 42 opens that combination, and below 42 the tumor reads HRD-negative and it is foreclosed. A confirmatory HER2 IHC re-stain decides whether a HER2-directed ADC such as trastuzumab deruxtecan is on the table: the IHC 1+ call rests on a single specimen Altera could not stain, and a re-stain reading HER2 0 takes the option away. Neither workup disturbs the all-comer PARP, anti-angiogenic, endocrine, or on-study choices. The remaining rows below record assays that have already resulted, kept here so the workup picture is complete.

### HRD / genomic instability

The Altera tumor NGS calls genomic instability qualitatively, reporting chromosomal imbalances and frequent LOH, but it gives no validated quantitative score, and a qualitative call does not meet the companion-diagnostic definition of HRD-positive. This matters because the PAOLA-1 olaparib-plus-bevacizumab indication defines HRD-positive as either a deleterious BRCA mutation or a Myriad MyChoice CDx GIS of at least 42. The tumor is BRCA-wild-type, so eligibility rests entirely on the GIS. This is the one essential, decision-gating workup left: it runs on archival FFPE, with the surgical resection block preferred for tumor content, turnaround 2 to 3 weeks. The MyChoice CDx is the only assay whose threshold maps directly to the olaparib-plus-bevacizumab label. FoundationOne CDx and Caris report LOH-based HRD surrogates, so confirm the score maps to the at-least-42 threshold before relying on either for eligibility. Germline 74-gene panel and tumor BRCA1/2 sequencing have both resulted as wild-type, which forecloses BRCA-gated olaparib monotherapy (SOLO1) and routes the PARP decision onto this score; no further BRCA testing is outstanding.

### HER2

The tumor scored HER2 IHC 1+ on a single surgical-pathology stain, which Libby reads as HER2-low. That call gates whether a HER2-directed ADC such as trastuzumab deruxtecan is worth discussing, because the tumor-agnostic trastuzumab-deruxtecan approval keys on IHC 3+. At IHC 1+ in ovarian cancer the drug is trial-eligibility and cross-tumor extrapolation only, never on-label. The 0-versus-1+ boundary has the poorest interrater concordance of any HER2 tier, and the Altera platform could not evaluate HER2 at all for lack of material, so no orthogonal read currently backs the stain. Two steps come first and are both high priority. Check specimen sufficiency on the surgical resection block (macrodissect if tumor content is low) before ordering anything, since an exhausted block forces a fresh-biopsy decision. Then run a confirmatory re-stain on the FDA-approved Ventana Pathway HER2 (clone 4B5) assay, scored to ASCO-CAP criteria, and ask for a discrete-tier report (0 / ultralow / 1+ / 2+ with reflex ISH / 3+) rather than a binary positive or negative call, because the tiers open different option sets: IHC 3+ or 2+/ISH-amplified puts the tumor-agnostic label in range, HER2-low keeps it at trial-eligibility, and HER2-ultralow is a still-lower tier defined only in breast. Reflex HER2 ISH/FISH (ERBB2 dual-probe) is conditional, triggered only if the re-stain reads 2+; do not order it up front on the current 1+. ERBB2 copy-number on a comprehensive NGS panel is a low-priority orthogonal cross-check, since HER2-low protein is expression-driven and a normal copy number neither confirms nor refutes the 1+ IHC; protein IHC stays the decision-driving assay. The IHC work runs on archival FFPE, turnaround 1 to 2 weeks, low cost.

### ER

ER is positive in roughly 80 percent of nuclei at weak-to-moderate intensity with PR negative, which supports a low-toxicity aromatase-inhibitor option such as letrozole. PR-negativity predicts a more modest endocrine response, so the semiquantitative ER/PR readout sets expectations rather than gating a drug. The values are already reported; no additional staining is needed unless a later specimen is obtained.

### PIK3CA / MAP2K4

The Altera panel reported focal PIK3CA amplification and focal MAP2K4 deletion, both investigational-only in HGSC with no approved matched therapy. They matter only as potential early-phase trial-matching tags on the PI3K/AKT/mTOR axis or MAP2K4-listed studies. No confirmatory or orthogonal assay is warranted; the findings are recorded for trial-screening completeness.

### Signatera ctDNA (MRD)

Tumor-informed ctDNA has cleared to Not Detected after cytoreduction and chemoimmunotherapy, marking a favorable molecular-residual-disease state that informs how intensively to pursue maintenance. Serial monitoring can flag biochemical relapse ahead of CA-125 or imaging. It does not select a target or gate a drug, so this is surveillance rather than a one-time gating assay; continuity favors keeping draws on the platform that designed the patient-specific panel.

### Where to order these assays

| Assay | Provider | Decision gated | Contact |
|---|---|---|---|
| **Validated genomic-instability score (Myriad MyChoice CDx GIS, or FDA-approved equivalent companion diagnostic)** | **Myriad Genetics *(preferred)* (MyChoice CDx)** | **Olaparib plus bevacizumab maintenance (PAOLA-1) eligibility in BRCA-wild-type HGSC, which is gated on a validated GIS of at least 42.** | **[test info](https://myriad.com/precision-medicine/mychoice-cdx/) · 320 Wakara Way, Salt Lake City, UT 84108 · 1-800-469-7423** |
| Validated genomic-instability score (Myriad MyChoice CDx GIS, or FDA-approved equivalent companion diagnostic) | Foundation Medicine *(FoundationOne CDx (LOH-based HRD))* | Olaparib plus bevacizumab maintenance (PAOLA-1) eligibility in BRCA-wild-type HGSC, which is gated on a validated GIS of at least 42. | [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| Validated genomic-instability score (Myriad MyChoice CDx GIS, or FDA-approved equivalent companion diagnostic) | Caris Life Sciences *(Caris HRD / genomic LOH)* | Olaparib plus bevacizumab maintenance (PAOLA-1) eligibility in BRCA-wild-type HGSC, which is gated on a validated GIS of at least 42. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| **HER2 IHC re-stain (Ventana Pathway HER2 clone 4B5), scored to ASCO-CAP criteria** | **NeoGenomics Laboratories *(preferred)* (HER2 (4B5) IHC)** | **Whether a HER2-directed ADC (e.g. trastuzumab deruxtecan) is on the table; tumor-agnostic T-DXd needs IHC 3+, so a confirmed HER2-low 1+ is trial-eligibility only in ovarian cancer.** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| HER2 IHC re-stain (Ventana Pathway HER2 clone 4B5), scored to ASCO-CAP criteria | Labcorp Oncology *(HER2 IHC (4B5))* | Whether a HER2-directed ADC (e.g. trastuzumab deruxtecan) is on the table; tumor-agnostic T-DXd needs IHC 3+, so a confirmed HER2-low 1+ is trial-eligibility only in ovarian cancer. | [test info](https://www.labcorp.com/) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| HER2 IHC re-stain (Ventana Pathway HER2 clone 4B5), scored to ASCO-CAP criteria | Quest Diagnostics *(HER2 IHC)* | Whether a HER2-directed ADC (e.g. trastuzumab deruxtecan) is on the table; tumor-agnostic T-DXd needs IHC 3+, so a confirmed HER2-low 1+ is trial-eligibility only in ovarian cancer. | [test info](https://www.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| HER2 IHC re-stain (Ventana Pathway HER2 clone 4B5), scored to ASCO-CAP criteria | Caris Life Sciences *(Caris MI Profile (IHC + WTS))* | Whether a HER2-directed ADC (e.g. trastuzumab deruxtecan) is on the table; tumor-agnostic T-DXd needs IHC 3+, so a confirmed HER2-low 1+ is trial-eligibility only in ovarian cancer. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| HER2 IHC re-stain (Ventana Pathway HER2 clone 4B5), scored to ASCO-CAP criteria | Tempus *(Tempus xT / IHC)* | Whether a HER2-directed ADC (e.g. trastuzumab deruxtecan) is on the table; tumor-agnostic T-DXd needs IHC 3+, so a confirmed HER2-low 1+ is trial-eligibility only in ovarian cancer. | [test info](https://www.tempus.com/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 · 1-800-739-4137 |
| **Specimen-sufficiency / tissue-adequacy check on the surgical resection block** | **NeoGenomics Laboratories *(preferred)* (Tissue QC / macrodissection)** | **Enables the confirmatory HER2 IHC, reflex ISH, and ERBB2 NGS reads; gates whether any HER2-directed ADC workup can proceed.** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| Specimen-sufficiency / tissue-adequacy check on the surgical resection block | Caris Life Sciences *(Tissue QC / molecular profiling)* | Enables the confirmatory HER2 IHC, reflex ISH, and ERBB2 NGS reads; gates whether any HER2-directed ADC workup can proceed. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| **Full HER2-tier classification (3+ vs 2+/ISH vs HER2-low vs HER2-ultralow)** | **NeoGenomics Laboratories *(preferred)* (HER2 (4B5) IHC, full-tier reporting)** | **Which HER2 stratum applies: 3+ (on-label tumor-agnostic T-DXd), HER2-low (trial-eligibility ADC), or ultralow; each opens a different option set.** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| Full HER2-tier classification (3+ vs 2+/ISH vs HER2-low vs HER2-ultralow) | Labcorp Oncology *(HER2 IHC (4B5))* | Which HER2 stratum applies: 3+ (on-label tumor-agnostic T-DXd), HER2-low (trial-eligibility ADC), or ultralow; each opens a different option set. | [test info](https://www.labcorp.com/) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| Full HER2-tier classification (3+ vs 2+/ISH vs HER2-low vs HER2-ultralow) | Quest Diagnostics *(HER2 IHC)* | Which HER2 stratum applies: 3+ (on-label tumor-agnostic T-DXd), HER2-low (trial-eligibility ADC), or ultralow; each opens a different option set. | [test info](https://www.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| **Reflex HER2 ISH/FISH (ERBB2 dual-probe), triggered only on a 2+ stain** | **NeoGenomics Laboratories *(preferred)* (HER2 (ERBB2) FISH)** | **Separates HER2-low (2+/ISH-negative) from HER2-amplified (2+/ISH-positive); conditional on a 2+ re-stain.** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| Reflex HER2 ISH/FISH (ERBB2 dual-probe), triggered only on a 2+ stain | Labcorp Oncology *(HER2 FISH)* | Separates HER2-low (2+/ISH-negative) from HER2-amplified (2+/ISH-positive); conditional on a 2+ re-stain. | [test info](https://www.labcorp.com/) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| Reflex HER2 ISH/FISH (ERBB2 dual-probe), triggered only on a 2+ stain | Quest Diagnostics *(HER2 FISH)* | Separates HER2-low (2+/ISH-negative) from HER2-amplified (2+/ISH-positive); conditional on a 2+ re-stain. | [test info](https://www.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| **ERBB2 copy-number / expression on a comprehensive NGS panel** | **Foundation Medicine *(preferred)* (FoundationOne CDx (ERBB2 copy number))** | **Orthogonal ERBB2 amplification check; does not gate ADC eligibility, which is set by protein IHC.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| ERBB2 copy-number / expression on a comprehensive NGS panel | Tempus *(Tempus xT (ERBB2 copy number))* | Orthogonal ERBB2 amplification check; does not gate ADC eligibility, which is set by protein IHC. | [test info](https://www.tempus.com/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 · 1-800-739-4137 |
| ERBB2 copy-number / expression on a comprehensive NGS panel | Caris Life Sciences *(Caris MI Profile (ERBB2 copy number))* | Orthogonal ERBB2 amplification check; does not gate ADC eligibility, which is set by protein IHC. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| **Serial tumor-informed ctDNA MRD (Signatera, already cleared to Not Detected)** | **Natera *(preferred)* (Signatera)** | **Maintenance intensity and relapse surveillance; does not gate a specific drug.** | **[test info](https://www.natera.com/oncology/signatera-advanced-cancer-detection/) · 13011 McCallen Pass, Building A, Austin, TX 78753 · 1-650-980-9190** |

### Biomarker plan

| Recommended assay | Rationale | Suggested assay provider | Tissue requirements |
|---|---|---|---|
| Validated genomic-instability score (Myriad MyChoice CDx GIS, or FDA-approved equivalent companion diagnostic) | The Altera tumor NGS calls genomic instability qualitatively (chromosomal imbalances and frequent LOH) but reports no validated quantitative score, and a qualitative call does not satisfy the companion-diagnostic definition of HRD-positive. The PAOLA-1 olaparib-plus-bevacizumab maintenance indication requires HRD-positive status defined as a deleterious BRCA mutation or a Myriad MyChoice CDx GIS of at least 42; this tumor is BRCA wild-type, so eligibility rests entirely on the GIS. Without a validated score the patient defaults to all-comer niraparib maintenance (PRIMA) and the higher-benefit olaparib-plus-bevacizumab option in HRD-positive disease cannot be offered. | Myriad Genetics *(MyChoice CDx)* · [test info](https://myriad.com/precision-medicine/mychoice-cdx/) · 320 Wakara Way, Salt Lake City, UT 84108 · 1-800-469-7423 | archival FFPE acceptable (surgical resection block preferred for tumor content) |
| Germline 74-gene panel plus tumor BRCA1/2 sequencing (already performed) | Both germline (74-gene panel) and somatic (Altera tumor/normal exome) BRCA1/2 testing have resulted as wild-type, which is the resolution that previously gated the case. This forecloses the BRCA-mutation-gated indications (olaparib monotherapy maintenance, SOLO1) and shifts the PARP question onto the genomic-instability score. No further BRCA testing is needed; the row records the resolved state so downstream agents do not re-flag it as pending. | Resolved on germline blood and tumor block already tested; no additional provider order required | none additional; germline blood and tumor block already tested |
| ER and PR semiquantitative IHC (Allred or percentage plus intensity, already reported) | ER is positive in roughly 80 percent of nuclei at weak-to-moderate intensity with PR negative, which supports a low-toxicity aromatase-inhibitor option (for example letrozole) as maintenance or later-line therapy that fits the patient's age and oral-preference. PR-negativity predicts a more modest endocrine response, so the quantitative ER/PR readout sets expectations rather than gating a drug. The values are already reported; no additional staining is required unless a later specimen is obtained. | Reported on the diagnostic IHC panel; no additional provider order required | archival FFPE acceptable |
| Comprehensive tumor NGS reporting PIK3CA amplification and MAP2K4 deletion (already performed, Altera) | The Altera panel reported focal PIK3CA amplification and focal MAP2K4 deletion, both investigational-only in HGSC with no approved matched therapy. They are relevant only as potential early-phase trial-matching tags (PI3K/AKT/mTOR-axis or MAP2K4-listed studies). No confirmatory or orthogonal assay is warranted; the findings are recorded for trial-screening completeness. | Reported on the Altera tumor NGS panel; no additional provider order required | archival FFPE acceptable |
| Serial tumor-informed ctDNA MRD (Signatera, already cleared to Not Detected) | Signatera tumor-informed ctDNA has cleared to Not Detected after cytoreduction and chemoimmunotherapy, which marks a favorable molecular-residual-disease state and informs how intensively to pursue maintenance. Serial monitoring can detect biochemical relapse ahead of CA-125 or imaging and help time maintenance decisions. It does not select a target or gate any specific drug, so priority is medium and surveillance, not a one-time gating assay. | Natera *(Signatera)* · [test info](https://www.natera.com/oncology/signatera-advanced-cancer-detection/) · 13011 McCallen Pass, Building A, Austin, TX 78753 · 1-650-980-9190 | serial whole-blood draws; tumor block already used for assay design |
| HER2 IHC re-stain (Ventana Pathway HER2 clone 4B5), scored to ASCO-CAP criteria | The 1+ call rests on a single surgical-pathology stain, and the 0-versus-1+ boundary has the poorest interrater concordance of any HER2 IHC tier. A confirmatory re-stain on the FDA-approved Ventana Pathway HER2 (4B5) assay, scored against ASCO-CAP criteria, hardens whether the tumor is genuinely HER2-low; the surgical report used ASCO-CAP gastric / DESTINY-PanTumor scoring, which labels 1+ as 'negative' even though the case-level tier is HER2-low. Skipping it leaves any HER2-directed ADC discussion resting on an unconfirmed, low-concordance score. | NeoGenomics Laboratories *(HER2 (4B5) IHC)* · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | archival FFPE acceptable (additional unstained slides from the surgical resection block) |
| Specimen-sufficiency / tissue-adequacy check on the surgical resection block | The Altera tumor NGS could not evaluate HER2 because of insufficient material, so no orthogonal molecular read currently backs the single IHC. Confirm the surgical resection block has enough residual tumor for added unstained sections (macrodissect if tumor content is low) before ordering the 4B5 re-stain and any ERBB2 copy-number read; if the block is exhausted, weigh a fresh biopsy against the modest yield of repeat HER2 testing. Without adequate tissue the HER2-low call cannot be confirmed or extended to ISH or NGS. | NeoGenomics Laboratories *(Tissue QC / macrodissection)* · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | archival FFPE block (assess residual tumor; fresh biopsy only if block exhausted) |
| Full HER2-tier classification (3+ vs 2+/ISH vs HER2-low vs HER2-ultralow) | A binary positive/negative HER2 call does not tell the board which option applies, because the tiers diverge sharply. IHC 3+ (or 2+/ISH-amplified) would put the tumor-agnostic trastuzumab-deruxtecan label in range; HER2-low (1+ or 2+/ISH-negative) keeps T-DXd at trial-eligibility and cross-tumor extrapolation from breast (DESTINY-Breast04); HER2-ultralow (IHC 0 with faint incomplete staining, per DESTINY-Breast06) is a lower tier defined only in breast. Reporting the discrete tier rather than a label is what lets the trial_screener match the correct HER2 stratum. | NeoGenomics Laboratories *(HER2 (4B5) IHC, full-tier reporting)* · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | archival FFPE acceptable (same sections as the confirmatory stain) |
| Reflex HER2 ISH/FISH (ERBB2 dual-probe), triggered only on a 2+ stain | Reflex ISH/FISH is indicated only when a stain scores 2+, to separate HER2-low (2+/ISH-negative) from gene-amplified disease (2+/ISH-positive). The current 1+ does not trigger ISH, so this row is conditional on the confirmatory re-stain coming back 2+. The tumor-agnostic trastuzumab-deruxtecan label keys on IHC 3+ rather than ISH in non-breast tumors, so amplification status here informs the biological call and trial stratification more than a direct drug gate. | NeoGenomics Laboratories *(HER2 (ERBB2) FISH)* · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | archival FFPE acceptable (reflex on the same block; no new specimen) |
| ERBB2 copy-number / expression on a comprehensive NGS panel | ERBB2 copy number and expression on a comprehensive NGS panel gives the orthogonal molecular read the Altera run could not produce on this tumor. In HER2-low disease the protein is driven by expression rather than gene amplification, so a normal ERBB2 copy number neither confirms nor refutes the 1+ IHC; an unexpected amplification would prompt slide re-review. Protein IHC stays the decision-driving assay for ADC eligibility, so this is a low-priority cross-check, not a substitute. | Foundation Medicine *(FoundationOne CDx (ERBB2 copy number))* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | archival FFPE acceptable (depends on the specimen-sufficiency check clearing) |

---

*Decision support, not medical advice. Confirm assay availability and current standards with the treating team and the local pathology service.*

<!-- libby:target-validation:end -->

## Scope summary

This case draws on 21 screened trials, 14 clinical-evidence rows, and 17 preclinical-evidence rows. Seven feature-targeting interventions made the ranked list and an eighth, disitamab vedotin, is kept as a board-vetoed not-recommended row. Agreement scores span 0.8 down to -0.4 across the ranked options, with disitamab vedotin sitting at -2 on a unanimous veto. The board did not converge on a single lead: the two registered all-comer PARP options (rucaparib, niraparib) carry the strongest evidence but both press the myelosuppression veto; bevacizumab is the only option clearing both vetoes outright, but it is PFS-only; the highest-magnitude regimen, olaparib + bevacizumab, sits sixth under a toxicity veto and an open eligibility gate; and the two HER2-directed ADCs split sharply, with trastuzumab deruxtecan landing seventh as an investigational relapse option that clears both vetoes while disitamab vedotin is rejected by all five personas because its MMAE payload triggers both.

## Cross-cutting caveat (read first)

**Every biomarker has resulted, so nothing gates the ranking outright — but two confirm-before-acting questions shape its tail.** The tumor is BRCA-wild-type on both germline and somatic testing yet genomically unstable on a qualitative Altera call, and a qualitative call is not the same thing as a companion-diagnostic HRD-positive result. That distinction splits the PARP question in two:

- The all-comer PARP options (rucaparib via ATHENA-MONO, niraparib via PRIMA) need neither a BRCA mutation nor a validated score, so they are available to this tumor today.
- The highest-magnitude option, olaparib + bevacizumab (PAOLA-1), is gated on HRD-positive status defined as a deleterious tumor BRCA mutation **or** a Myriad MyChoice CDx GIS of at least 42. This tumor is BRCA-wild-type, so eligibility rests entirely on a GIS the patient does not yet have. The Altera qualitative instability call does not clear that bar.

The second question is HER2. The tumor scored IHC 1+, which Libby reads as HER2-low rather than HER2-negative even though the surgical-pathology report labelled 1+ "negative" under gastric/pan-tumor scoring. HER2-low is an actionable expression tier, but the tumor-agnostic trastuzumab deruxtecan approval requires IHC 3+, so for an IHC 1+ ovarian tumor any HER2-directed ADC is investigational, supported by cross-tumor extrapolation from HER2-low breast rather than by ovarian data. The 1+ also rests on a single specimen Altera could not stain, so a confirmatory re-stain comes before acting on the HER2 axis.

Neither question moves the lead:

- A validated GIS gates only rank 6. The all-comer PARP, bevacizumab, endocrine, and on-study options stand regardless. A MyChoice GIS at least 42 promotes olaparib + bevacizumab, provided the conservative's toxicity veto is also addressed; below 42 the tumor reads HRD-negative and that combination is foreclosed.
- The HER2-directed option (trastuzumab deruxtecan, rank 7) is an investigational relapse consideration, not a current maintenance pick. A confirmatory HER2 re-stain hardens it before it is on the table, and if the re-stain reads HER2 0 the option falls away.
- Because all biomarkers have resulted, both the GIS and the HER2 re-stain are surfaced below under Workup considerations rather than as ranked diagnostic rows.

## Workup considerations

- **Validated genomic-instability score (Myriad MyChoice CDx GIS >=42, or FDA-approved equivalent) — essential, gates olaparib + bevacizumab only.** Runs on archival FFPE (surgical resection block preferred for tumor content), turnaround 2-3 weeks, moderate cost. A result at or above 42 makes the patient PAOLA-1-eligible and promotes olaparib + bevacizumab; below 42 she is HRD-negative and defaults to all-comer niraparib or rucaparib. The MyChoice CDx is the only assay whose threshold maps directly to the olaparib + bevacizumab label; FoundationOne CDx and Caris report LOH-based HRD surrogates that are not the label-recognized companion diagnostic, so confirm the score maps to the >=42 threshold before relying on it (validation row `gis-hrd-validated-score`, [PMID 31851799](https://pubmed.ncbi.nlm.nih.gov/31851799), [NCT02477644](https://clinicaltrials.gov/study/NCT02477644)).
- **Confirmatory HER2 IHC re-stain (Ventana Pathway HER2 4B5, scored to ASCO-CAP) — high priority, hardens the HER2-low call.** The IHC 1+ rests on a single surgical-path specimen, and the 0-versus-1+ boundary has the poorest interrater concordance of any HER2 tier; Altera could not evaluate HER2 at all (insufficient material), so no orthogonal read currently backs the stain. Confirm the resection block has enough residual tumor first (macrodissect if low), then run the 4B5 re-stain on archival FFPE, turnaround 1-2 weeks, low cost. Ask for a discrete-tier report (0 / ultralow / 1+ / 2+ with reflex ISH / 3+) so any HER2 ADC discussion rests on a confirmed score; reflex ISH triggers only on a 2+ result (validation rows `her2-ihc-confirmatory`, `her2-specimen-sufficiency`, [PMID 35665782](https://pubmed.ncbi.nlm.nih.gov/35665782)).
- BRCA germline (74-gene panel) and somatic (Altera) are both resolved as wild-type; no further BRCA testing is outstanding, and the germline result also covers family-counseling needs.
- ER/PR semiquantitative IHC, the PIK3CA/MAP2K4 NGS findings, and serial Signatera MRD are all already reported; none requires a new assay. Signatera continuity favors keeping serial draws on the platform that designed the patient-specific panel.

## Intervention grouping

- All-comer PARP maintenance for a BRCA-wild-type, genomically-unstable tumor — rucaparib (ATHENA-MONO, [NCT03522246](https://clinicaltrials.gov/study/NCT03522246), [PMID 35658487](https://pubmed.ncbi.nlm.nih.gov/35658487)) and niraparib (PRIMA, [NCT02655016](https://clinicaltrials.gov/study/NCT02655016), [PMID 31562799](https://pubmed.ncbi.nlm.nih.gov/31562799); BRCA-wild-type PDX pharmacology [PMID 30647846](https://pubmed.ncbi.nlm.nih.gov/30647846)).
- VEGF / angiogenesis maintenance — bevacizumab (GOG-218 [NCT00262847](https://clinicaltrials.gov/study/NCT00262847) / [PMID 22204724](https://pubmed.ncbi.nlm.nih.gov/22204724); ICON7 [PMID 22204725](https://pubmed.ncbi.nlm.nih.gov/22204725)).
- HRD-gated PARP + anti-angiogenic combination — olaparib + bevacizumab (PAOLA-1, [NCT02477644](https://clinicaltrials.gov/study/NCT02477644), [PMID 31851799](https://pubmed.ncbi.nlm.nih.gov/31851799)).
- ER-directed endocrine maintenance — letrozole ([PMID 29157627](https://pubmed.ncbi.nlm.nih.gov/29157627)).
- IL-12 immunogene / tumor immune microenvironment — GEN-1 / IMNN-001 (OVATION 2, [NCT03393884](https://clinicaltrials.gov/study/NCT03393884); IL-12 TME mechanism [PMID 20033066](https://pubmed.ncbi.nlm.nih.gov/20033066)).
- HER2-directed ADCs for HER2-low (IHC 1+) disease, investigational in ovarian cancer — trastuzumab deruxtecan (DESTINY-Breast04 [PMID 35665782](https://pubmed.ncbi.nlm.nih.gov/35665782); DESTINY-PanTumor02 ovarian cohort [PMID 37870536](https://pubmed.ncbi.nlm.nih.gov/37870536); DESTINY-Breast06 [PMID 39282896](https://pubmed.ncbi.nlm.nih.gov/39282896)). Disitamab vedotin (NCT06003231) was rejected on MMAE toxicity; see Classes examined but not ranked.

## Rank 1. Rucaparib (1L maintenance)

*All-comer PARP maintenance that qualifies a BRCA-wild-type tumor with no GIS gate. Replicated phase 3 evidence, but the same myelosuppression veto as niraparib.*

### Evidence base

ATHENA-MONO is a registered, double-blind, placebo-controlled phase 3 (n=538, 4:1 randomization) of 1L rucaparib maintenance after a platinum response ([PMID 35658487](https://pubmed.ncbi.nlm.nih.gov/35658487), [NCT03522246](https://clinicaltrials.gov/study/NCT03522246)). The intent-to-treat result was mPFS 20.2 vs 9.2 months, HR 0.52 (95% CI 0.40-0.68, p<0.0001), and the benefit held in the HRD-negative stratum (HR 0.47), so a BRCA-wild-type, HRD-unquantified tumor qualifies on the ITT footing rather than on a nested BRCA-mutant subgroup. RoB2 reads low. The effect estimate quoted throughout is the ITT HR 0.52 from the primary JCO publication (Monk et al, J Clin Oncol 2022).

### Likelihood of desired effect

For progression-free survival this is a strong fit: the all-comer enrolment is the eligibility match itself, and the ITT effect is the larger of the two registered all-comer PARP options. The honest ceiling is that the evidence is PFS-grade, and rucaparib carries no tumor-specific preclinical pharmacology pointing it at this particular BRCA-proficient biology, unlike niraparib, which does.

### Toxicity profile

- Grade 3+ anemia 28.7% — **this presses the patient's named severe-myelosuppression / febrile-neutropenia veto.**
- Grade 3+ neutropenia 14.6%.
- Grade 3+ ALT/AST elevation 10.6% (usually transient; baseline LFTs are normal here).
- AE-related discontinuation 11.8%, which matters for a maintenance commitment in the 70-79 band.

### Counter-productive mechanisms / dissent

No persona vetoed or dissented against rucaparib. The critic ranked it second on evidence quality, reading the all-comer ITT footing as the right basis for a BRCA-wild-type tumor, and the concensusite, conservative, and advocate all carry it as an oral maintenance option. The myelosuppression here is a patient-AE burden, not a mechanism that blunts PARP maintenance in a genomically-unstable tumor.

### Practical considerations

Oral 600 mg twice daily for up to 24 months; NCCN Ovarian v1.2025 lists single-agent PARP maintenance as category 2A for all-comers. The oral route matches the patient's preference. The anemia signal sits on her veto, so the same hematology support and cytopenia-management planning that niraparib needs applies here.

### Why this rank

Rucaparib takes rank 1 on board signal, not on a clinical-superiority claim: it carries no veto and no dissent (agreement_score 0.8) where niraparib accrued a conditional veto and a persistent dissent (0.2). The two are near-interchangeable all-comer PARP options; the risktaker, who ranks niraparib first, would break the tie toward niraparib on its BRCA-wild-type PDX pharmacology, which is the one reason niraparib is not simply redundant with rucaparib.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Rucaparib maintenance (ATHENA-MONO) | ITT mPFS 20.2 vs 9.2 mo, HR 0.52 (0.40-0.68) | G3+ anemia 28.7%, neutropenia 14.6%, ALT/AST 10.6% | [35658487](https://pubmed.ncbi.nlm.nih.gov/35658487) · [NCT03522246](https://clinicaltrials.gov/study/NCT03522246) |

## Rank 2. Niraparib (1L maintenance)

*Cleanest all-comer guideline and evidence fit with the only tumor-specific pharmacology on the board, but its grade 3+ thrombocytopenia/anemia hit the patient's named veto.*

### Evidence base

PRIMA/ENGOT-OV26 is a registered, double-blind, placebo-controlled phase 3 (n=733, 2:1) of 1L niraparib maintenance ([PMID 31562799](https://pubmed.ncbi.nlm.nih.gov/31562799), [NCT02655016](https://clinicaltrials.gov/study/NCT02655016)). It enrolled all-comers with no BRCA mutation and no validated HRD score required, and hit its primary PFS endpoint at mPFS 13.8 vs 8.2 months, HR 0.62 (95% CI 0.50-0.76, p<0.001); RoB2 low. For a BRCA-wild-type tumor with only a qualitative instability call, that all-comer enrolment is the eligibility match, not a cross-stratum extrapolation. The risktaker adds the one tumor-specific argument the board surfaced: in a BRCA-wild-type PDX, niraparib partitioned into tumor at 3.3x plasma and cut growth 58% where olaparib barely moved ([PMID 30647846](https://pubmed.ncbi.nlm.nih.gov/30647846)). That preclinical signal is thin, but it argues the upside here may run above the registration-population number rather than at it.

### Likelihood of desired effect

As an evidence fit this is high for PFS: the all-comer estimate applies directly, and the PDX pharmacology nudges expectations upward. Two things temper it. The larger HRD-positive effect (HR 0.43) does not apply without a validated score, so expectations should be set off the all-comer HR 0.62; and OS was immature at the primary report (HR 0.70, 95% CI 0.44-1.11), so the demonstrated benefit is PFS, not survival.

### Toxicity profile

- Grade 3+ thrombocytopenia 28.7% — **direct hit on the patient's named severe-myelosuppression / febrile-neutropenia veto.**
- Grade 3+ anemia 31%.
- Grade 3+ neutropenia 12.8%.
- Baseline WBC is already 3.5, a thin marrow reserve in the 70-79 band before any drug-related cytopenia. Individualized starting dose by body weight and baseline platelet count blunts this but does not erase it.

### Counter-productive mechanisms / dissent

This is where niraparib loses its rank. The conservative issued a conditional veto, against ranking niraparib at rank 1 on the patient's own myelosuppression veto, and stated it would withdraw the veto once a hematology-supported, platelet-based starting-dose plan and a written cytopenia-management pathway are documented. The advocate dissented for the same reason, holding that the veto is the patient's to lift, not the board's to rank past on evidence grounds. We override the veto to keep niraparib ranked and visible, because the all-comer benefit is real and the objection is a deliverability condition rather than a claim that the drug is wrong for the tumor. The risktaker and critic both endorsed it; the critic rated it high-confidence on evidence, flagging only that the cost is toxicity, not bias.

### Practical considerations

Oral 200-300 mg once daily; NCCN Ovarian v1.2025 category 2A all-comer, ESMO-endorsed. The oral route fits the patient's preference. Deliverability at her marrow reserve is the open item: a documented dose plan converts the conservative's conditional veto into an endorsement.

### Why this rank

Niraparib sits one rank below rucaparib because of where the board signal landed, not because of an efficacy gap — the two are the matched all-comer PARP pair. The agreement_score gap (0.8 vs 0.2) is entirely the conditional veto plus the advocate dissent. If a hematology dose plan is documented, that gap closes and niraparib's tumor-specific pharmacology arguably makes it the lead PARP for this BRCA-proficient tumor.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Niraparib maintenance (PRIMA) | Overall mPFS 13.8 vs 8.2 mo, HR 0.62 (0.50-0.76) | G3+ thrombocytopenia 28.7%, anemia 31%, neutropenia 12.8% | [31562799](https://pubmed.ncbi.nlm.nih.gov/31562799) · [NCT02655016](https://clinicaltrials.gov/study/NCT02655016) |

## Rank 3. Bevacizumab (continued maintenance)

*The only maintenance that clears both named vetoes on a backbone she already tolerates — but PFS-only, with a live VTE/bleeding caution against her IVC-filter history.*

### Evidence base

GOG-218 is a three-arm, double-blind, placebo-controlled phase 3 (n=1873) anchoring bevacizumab maintenance, with bevacizumab-throughout mPFS 14.1 vs 10.3 months, HR 0.717 (95% CI 0.625-0.824, p<0.001), RoB2 low ([PMID 22204724](https://pubmed.ncbi.nlm.nih.gov/22204724), [NCT00262847](https://clinicaltrials.gov/study/NCT00262847)). ICON7 (n=1528, open-label, HR 0.81) reinforces the axis, with the OS gain confined to the high-risk subset ([PMID 22204725](https://pubmed.ncbi.nlm.nih.gov/22204725)). Both are PFS-only: neither showed an overall-population OS benefit, and the critic insists this be labelled a PFS hold rather than a survival argument. A stage IIIc R0 patient sits adjacent to, not inside, ICON7's high-risk OS subset.

### Likelihood of desired effect

Moderate, and PFS-only. The effect size is the smallest of the maintenance options on the board, and there is no overall-population survival signal to lean on. What it offers instead is predictability: a drug she is already on and tolerating, with a decade of post-marketing characterization.

### Toxicity profile

- Grade 2+ hypertension 22.9% (vs 7.2% control) requiring medical therapy, with a well-worn management algorithm.
- GI perforation / bowel-wall disruption 2.6% (vs 1.2%).
- VTE and bleeding class risk — the operative caution given the patient's high VTE history and prior IVC filter. **Neither named veto (neuropathy, myelosuppression) is triggered**, so this is a managed caution, not a stop.

### Counter-productive mechanisms / dissent

The conservative, advocate, and concensusite all endorse bevacizumab on patient-side grounds: it is the one maintenance axis whose toxicity is predictable and that clears both vetoes. The critic ranks it third but insists it be read as a PFS hold, not a survival argument. The risktaker dissents on magnitude — seating the smallest effect on the board at the top of an efficacy-leaning (0.7) patient's list forfeits the larger PARP signal and banks a curve she is already riding. The advocate's own round-2 dissent is narrower and is about sequencing: the patient asked for the confirmatory workup to rank first, so leading with bevacizumab over that ordering is the quarrel, not the drug. The anti-angiogenic VTE/bleeding risk is a patient-AE caution to monitor, not a mechanism that blunts the maintenance benefit.

### Practical considerations

IV q3w, continuing to roughly 15 months total — she is already on it, so this costs nothing in new decision-making. NCCN Ovarian v1.2025 category 2A all-comer. The VTE/bleeding caution is handled with established BP and bleeding monitoring kept running rather than escalated. The open question is whether to continue bevacizumab alone or layer a PARP on once the GIS resolves, given the cleared Signatera MRD state.

### Why this rank

Bevacizumab outscores GEN-1 (0.6 vs 0.4) and ranks above it on evidence quality and deliverability: a RoB2-low phase 3 backbone she already tolerates beats an immature sponsor-topline regimen. It ranks below the two PARP options because, for an efficacy-leaning patient, a PFS-only HR 0.717 is a smaller bet than the replicated all-comer PARP curves — even though those trip a veto and this one does not.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Bevacizumab-throughout (GOG-218) | mPFS 14.1 vs 10.3 mo, HR 0.717 (0.625-0.824); no OS gain | G2+ hypertension 22.9%, GI-wall disruption 2.6% | [22204724](https://pubmed.ncbi.nlm.nih.gov/22204724) · [NCT00262847](https://clinicaltrials.gov/study/NCT00262847) |
| Bevacizumab (ICON7) | mPFS 21.8 vs 20.3 mo, HR 0.81 (0.70-0.94); OS gain in high-risk subset | G2+ hypertension 18% vs 2% | [22204725](https://pubmed.ncbi.nlm.nih.gov/22204725) |

## Rank 4. GEN-1 / IMNN-001 (IL-12 immunogene, OVATION 2)

*On-study IL-12 continuation that sidesteps the foreclosed checkpoint axis and carries a real OS signal. The efficacy is sponsor-topline-immature, though, and the route is intraperitoneal.*

### Evidence base

OVATION 2 is a randomized phase 1/2 (n=110) adding intraperitoneal IMNN-001 (GEN-1) to neoadjuvant carboplatin/paclitaxel ([NCT03393884](https://clinicaltrials.gov/study/NCT03393884)). The reported ITT result is mPFS 14.9 vs 11.9 months, HR 0.79, with OS HR 0.69 (a roughly 13-month median OS improvement, immature). These come from a sponsor topline and a 2025 Gynecologic Oncology abstract; CIs are not reported and there is no peer-reviewed per-term grade 3+ safety table. The regimen is matched to this patient, who received GEN-1 with neoadjuvant carbo/paclitaxel and reached R0. Mechanistically it acts through the peritoneal immune microenvironment ([PMID 20033066](https://pubmed.ncbi.nlm.nih.gov/20033066)) rather than the MSI/TMB checkpoint axis her MSS, TMB-low tumor forecloses, so the usual single-agent-immunotherapy disqualifier does not apply.

### Likelihood of desired effect

Moderate but immature. The OS signal (HR 0.69) is large enough that the risktaker would not dismiss it, but the PFS magnitude trails the PARP options and the estimates rest on topline data with unreported CIs. The continuation argument is partly that this is the regimen that carried her to R0.

### Toxicity profile

- No per-term grade 3+ AE table in the public topline or abstract; IP delivery is reported as generally well tolerated with no new safety signal.
- Intraperitoneal route — not the oral, low-burden modality the patient prefers.
- Investigational status: access and continuity outside the trial structure are not guaranteed.
- No named patient veto is triggered to date.

### Counter-productive mechanisms / dissent

No persona vetoed it. The risktaker and advocate endorse continuing it; in round 2 the risktaker pushed back at the critic for leaving it off the list, arguing that holding out for peer-reviewed CIs before continuing a working IL-12 immunogene is the kind of inaction that costs in advanced disease. The mechanism — IL-12-driven immune activation in the peritoneal compartment — carries no plausible counter-productive vector that the board flagged.

### Practical considerations

The patient prefers trials and is already on this one, so continuity is the argument. The cost is the route (intraperitoneal, not oral) and the immaturity of the efficacy and safety data. It keeps a credible OS hypothesis alive while the GIS result decides the PARP question.

### Why this rank

GEN-1 ranks just below bevacizumab (0.4 vs 0.6) because bevacizumab's evidence is a RoB2-low phase 3 and GEN-1's is a sponsor topline with no peer-reviewed safety table. It ranks above letrozole despite a lower nominal endorsement count because its OS signal and regimen-match outweigh letrozole's retrospective evidence base.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| IMNN-001 (GEN-1) + neoadjuvant chemo (OVATION 2) | ITT mPFS 14.9 vs 11.9 mo, HR 0.79; OS HR 0.69 (immature) | IP delivery well tolerated; no per-term G3+ table published | [NCT03393884](https://clinicaltrials.gov/study/NCT03393884) |

## Rank 5. Letrozole (endocrine maintenance)

*The lowest-toxicity oral option that clears every veto and fits the age band. The evidence is a single retrospective ROBINS-I-serious series, though, and PR-negativity tempers the expected magnitude.*

### Evidence base

The supporting data are a non-randomized retrospective letrozole-maintenance comparison nested in a translational ER-expression study ([PMID 29157627](https://pubmed.ncbi.nlm.nih.gov/29157627)): 60% vs 38.5% recurrence-free at 24 months (p=0.035), control mRFS roughly 13.2 months, ROBINS-I serious, n=80, evidence tier 4. The critic insists the ROBINS-I Serious tag sit next to the rank so a reader does not take the 60% for a trial result. The clinician also flagged a design mismatch — the trials row described a single-arm phase 2, but the source is a retrospective translational series. The patient is ER-positive (~80% nuclei) but PR-negative, which predicts a more modest response than the ER reading alone suggests.

### Likelihood of desired effect

Low, and weakly evidenced. There is no randomized letrozole-maintenance data in HGSC to anchor the estimate, and PR-negativity tempers even the retrospective signal. This is a tolerability floor, not an efficacy bet.

### Toxicity profile

- Arthralgia on prolonged aromatase inhibition.
- Bone-density loss with extended use.
- No per-term toxicity table in the source; **none of the patient's named vetoes apply.**

### Counter-productive mechanisms / dissent

No persona vetoed or dissented outright. The critic and concensusite both filed qualified critiques on evidence quality and guideline tier, asking that letrozole be framed as the low-toxicity later-line or adjunct fallback rather than a maintenance option carrying the same guideline weight as the PARP and bevacizumab choices. Endocrine blockade has no plausible counter-productive vector in ER-positive HGSC.

### Practical considerations

Oral 2.5 mg once daily, no infusion burden — the best fit on the board for the age band and the oral preference. NCCN Ovarian v1.2025 includes aromatase inhibitors among hormone-therapy options, at a softer tier than the category 2A PARP and bevacizumab recommendations. The natural role is a later-line or adjunct fallback, particularly if a GIS returns HRD-negative and the patient wants to stay off cytopenia-inducing maintenance.

### Why this rank

Letrozole's agreement_score ties rucaparib's at 0.6 because nobody objected to it — but that score reflects the absence of dissent on a low-stakes, low-toxicity option, not evidence strength. It ranks fifth, below options with weaker board signal but materially stronger evidence, because the efficacy-toxicity-weighted preference fit (efficacy weight 0.7) pulls a tier-4 retrospective series down past the registered phase 3 and the regimen-matched on-study options.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Letrozole maintenance (retrospective series) | 60% vs 38.5% RFS at 24 mo (p=0.035); ROBINS-I serious | Arthralgia, bone-density loss; no per-term table | [29157627](https://pubmed.ncbi.nlm.nih.gov/29157627) |

## Rank 6. Olaparib + bevacizumab (PAOLA-1 maintenance, contingent on validated HRD-positive)

*Highest-magnitude maintenance if HRD-positive is confirmed — but contingent on a GIS she lacks, and held back by a toxicity veto plus a subgroup-only evidence dissent.*

### Evidence base

PAOLA-1 is a registered, double-blind, placebo-controlled phase 3 (n=806) adding olaparib to a bevacizumab backbone ([PMID 31851799](https://pubmed.ncbi.nlm.nih.gov/31851799), [NCT02477644](https://clinicaltrials.gov/study/NCT02477644)). The load-bearing number — HRD-positive mPFS 37.2 vs 17.7 months, HR 0.33 (95% CI 0.25-0.45) — is a pre-specified subgroup, and the BRCA-non-mutated HRD-positive analogue closest to this patient is a further-nested subgroup at HR 0.43. The pre-specified ITT was a materially smaller HR 0.59 (95% CI 0.49-0.72), mPFS 22.1 vs 16.6 months, and ITT OS was not significant. The trial design is RoB2 low; the problem is eligibility. PAOLA-1 defines HRD-positive by MyChoice GIS at least 42 or tumor BRCA, and this BRCA-wild-type tumor with only a qualitative Altera call does not clear that companion-diagnostic bar.

### Likelihood of desired effect

High only if a validated GIS confirms HRD-positive. Frame this conditionally: if MyChoice returns at least 42, the subgroup HR 0.33 applies and this is the strongest maintenance on the board, and the patient is already on the bevacizumab half. If it returns below 42 she is HRD-negative and this rec is foreclosed entirely. Without the score, the conservative read is the ITT HR 0.59, not the subgroup 0.33.

### Toxicity profile

- Combination-arm grade 3+ AE near 57%.
- Grade 3+ hypertension 19% — **compounds the patient's VTE/bleeding caution against her high VTE history and prior IVC filter.**
- Grade 3+ anemia 17% — **presses the PARP myelosuppression veto.**
- Up to 20% discontinued olaparib for AEs. This regimen stacks two of the patient's concerns at once.

### Counter-productive mechanisms / dissent

This rec carries one veto and two dissents, for distinct and all-live reasons. The conservative vetoed it on toxicity: a roughly 57% grade 3+ rate with 19% grade 3+ hypertension, stacked onto a VTE history and prior IVC filter, with no compensating mitigation evidence in the record — the veto lifts only with a documented anticoagulation/BP plan and a confirmed GIS at least 42. The critic dissented on evidence quality: the HR 0.33 is a subgroup estimate (ITT HR 0.59), and the patient does not clear the companion-diagnostic gate that defines that subgroup, so reading her against a subgroup readout she is not eligible for is the case the dissent exists for. The advocate dissented on the stacked PARP-plus-anti-angiogenic toxicity against the IVC-filter history. We override the conservative veto and keep the row visible at considered_with_caveats rather than dropping it, because the risktaker and concensusite hold it as a contingent high-upside option: a GIS at least 42 opens the gate and makes the toxicity veto addressable.

### Practical considerations

Oral olaparib 300 mg twice daily plus IV bevacizumab — she is already on the bevacizumab half, which makes the add-on operationally clean. NCCN Ovarian v1.2025 ranks it category 1, but only for the HRD-positive population she is not yet in. The actionable next step is the GIS, surfaced above under Workup considerations; the regimen reorders upward if the score confirms HRD-positive and an anticoagulation/BP plan addresses the conservative's toxicity veto.

### Why this rank

This is the only ranked rec carrying a veto, which is why it sits last (agreement_score -0.4) despite the largest effect size on the board. The gap to letrozole and the rest is the standing toxicity veto plus two dissents and the open eligibility gate. Its rank is the most conditional on the page: a confirmed GIS at least 42 plus a documented anticoagulation/BP plan could move it from last toward first.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Olaparib + bevacizumab (PAOLA-1) | HRD+ mPFS 37.2 vs 17.7 mo, HR 0.33 (0.25-0.45); ITT HR 0.59 | G3+ AE ~57%; hypertension 19%, anemia 17% | [31851799](https://pubmed.ncbi.nlm.nih.gov/31851799) · [NCT02477644](https://clinicaltrials.gov/study/NCT02477644) |

## Rank 7. Trastuzumab deruxtecan (T-DXd), HER2-low (IHC 1+), investigational

*The one HER2-directed option that clears both named vetoes, but investigational at IHC 1+ ovarian on breast-only extrapolation — a relapse consideration, not a current maintenance pick.*

### Evidence base

There is no ovarian HER2-low IHC 1+ efficacy data, and that absence is the whole story. The closest tumor-type read, DESTINY-PanTumor02's ovarian cohort, posted a 45% ORR (n=40) but enrolled at IHC 2+/3+ ([PMID 37870536](https://pubmed.ncbi.nlm.nih.gov/37870536)), and the tumor-agnostic approval that came out of it is IHC 3+ only. The IHC 1+ evidence is all breast: DESTINY-Breast04 enrolled HER2-low (IHC 1+ or 2+/ISH-) and the hormone-receptor-positive subgroup that mirrors her ER-positive biology had a PFS HR of 0.51 ([PMID 35665782](https://pubmed.ncbi.nlm.nih.gov/35665782)), and DESTINY-Breast06 pushed the signal down to ultralow at PFS HR 0.62 ([PMID 39282896](https://pubmed.ncbi.nlm.nih.gov/39282896)). She cannot enrol on a breast trial, so for her ovarian tumor this is cross-tumor extrapolation plus the DXd bystander mechanism standing in for indication data.

### Likelihood of desired effect

Low-to-moderate, and entirely borrowed. If the HER2-low signal travels from breast to ovary the way the DXd bystander biology suggests it might, the effect could be real — but no ovarian IHC 1+ patient has been treated and reported, and at 1+ antigen density the sparse HER2-positive cells may not seed enough payload to reach their neighbors. Treat this as a hypothesis with mechanistic support, not a demonstrated benefit.

### Toxicity profile

- ILD/pneumonitis 10-12% adjudicated drug-related, including fatal cases — the defining long-tail risk, requiring baseline and serial chest imaging.
- Grade 3+ AE 52.6% in DESTINY-Breast04; near-universal nausea; grade 3+ anemia and neutropenia.
- IV q3w, against the patient's low-infusion preference.
- **Neither named veto is triggered**: the headline toxicities are ILD and nausea, not peripheral neuropathy or febrile neutropenia. That is the single reason it survives where disitamab vedotin does not.

### Counter-productive mechanisms / dissent

The advocate, critic, and risktaker all carry T-DXd, but only as a relapse option. The advocate carries it because its toxicity profile clears both vetoes, unlike the MMAE alternative. The concensusite dissented on guideline fit: no NCCN, ESMO, or SGO text endorses HER2-directed therapy in HER2-low ovarian, and seating it above an all-comer PARP would invert the consensus order. The critic dissented on the risktaker ranking it as high as third, on the grounds that a preclinical bystander mechanism cannot stand in for an ovarian efficacy estimand that does not exist. No persona vetoed it; the reservation is about evidence and route, not harm.

### Practical considerations

Off-label use of an approved drug is the only T-DXd route — no T-DXd trial is currently enrolling this tumor type, and a payer denial is likely since the tumor-agnostic approval is IHC 3+. Order the confirmatory HER2 re-stain first; the 1+ rests on a single specimen Altera could not evaluate. Best positioned as a documented later-line option for relapse, after the re-stain, with baseline and serial ILD monitoring.

### Why this rank

T-DXd sits seventh, below every active maintenance option and below the contingent olaparib + bevacizumab, because it is investigational off cross-tumor data and is a relapse consideration rather than a current-line pick — not because of a veto. Its agreement_score (0.4) matches GEN-1's, but the efficacy-toxicity-weighted preference fit pushes an off-label, IV, ILD-risk, single-specimen option below the regimen-matched on-study choice and the contingent high-magnitude combination.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| T-DXd, HER2-low breast (DESTINY-Breast04) | HR+ PFS HR 0.51 (mPFS 10.1 vs 5.4 mo) | ILD 12.1% incl. G5 0.8%; G3+ AE 52.6% | [35665782](https://pubmed.ncbi.nlm.nih.gov/35665782) |
| T-DXd, ovarian cohort (DESTINY-PanTumor02) | ORR 45% at IHC 2+/3+ (above this tumor's tier) | ILD 10.5% (3 fatal); G3+ TRAE 40.8% | [37870536](https://pubmed.ncbi.nlm.nih.gov/37870536) |
| T-DXd, HER2-low/ultralow breast (DESTINY-Breast06) | HER2-low PFS HR 0.62 (mPFS 13.2 vs 8.1 mo) | ILD 11.3% incl. 3 G5; G3+ AE 52.8% | [39282896](https://pubmed.ncbi.nlm.nih.gov/39282896) |

## Classes examined but not ranked

- **Disitamab vedotin (RC48) — not recommended, board-vetoed unanimously.** The open solid-tumor basket (NCT06003231) does accept HER2 IHC 1+ ovarian, so on biomarker and tumor type it is the most directly enrollable HER2 option — yet all five personas rejected it, because its MMAE payload runs peripheral sensory neuropathy at 68% any-grade / 18.7% grade 3+ and neutropenia at 12.1% grade 3+ ([PMID 37988648](https://pubmed.ncbi.nlm.nih.gov/37988648)), hitting both of the patient's named vetoes head-on. Its only HER2-low efficacy read is an abstract-only PAM-pathway-selected breast series, and the accessibility pass flags that the US basket is now active-not-recruiting and the only recruiting trial is China-only. Kept as a not-recommended row so the rejection is visible, not silent.
- **Trastuzumab duocarmazine (SYD985) — unavailable.** A second HER2 ADC with documented IHC 1+ breast activity, but the program is discontinued after the FDA complete response letter and it never enrolled ovarian patients; mechanism context only, with no access route.
- **Olaparib monotherapy (SOLO1) — not recommended, foreclosed.** BRCA-mutation-gated; both germline and somatic BRCA resulted as wild-type, so this indication does not apply to this tumor.
- **PI3K/AKT-pathway inhibitors (PIK3CA-directed) — investigational only.** The tumor carries a focal somatic PIK3CA amplification, but amplification is a poorly-validated predictive marker versus an activating hotspot mutation, there is no approved PI3K-directed therapy in HGSC, and the only options are phase 1 trial-matching tags with no efficacy estimand (NCT05216432, NCT05683418).
- **MAP2K4-directed agents — investigational only.** The focal somatic MAP2K4 deletion is a phase 1 trial-matching tag with no validated preclinical target and no approved matched therapy (NCT05557045, NCT05691504, NCT03340506, NCT03454035).

## Ranked prioritization

| Rank | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
|---|---|---|---|---|---|
| 1 | **Rucaparib (1L maintenance)**<br><small><em>endorse:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-advocate">advocate</span></small> | Moderate-to-high for PFS: replicated all-comer phase 3 (ATHENA-MONO ITT HR 0.52, 20.2 vs 9.2 mo) qualifying a BRCA-wild-type tumor without a BRCA or GIS gate. | Moderate (grade 3+ anemia 28.7%, neutropenia 14.6%, transaminase rise 10.6%) | **Low** (PARP myelosuppression is a patient-AE burden, not a mechanism that blunts the maintenance goal in genomically-unstable HGSC.) | **Replicated all-comer PARP maintenance that qualifies a BRCA-wild-type tumor with no GIS gate; near-interchangeable with niraparib but lacks its tumor-specific pharmacology, and carries the same myelosuppression veto.** |
| 2 | **Niraparib (1L maintenance)**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>dissent:</em> <span class="persona persona-advocate">advocate</span></small><br><small><em>veto:</em> <span class="persona persona-conservative">conservative</span></small> | High for PFS as an evidence fit: all-comer PRIMA phase 3 (HR 0.62, 13.8 vs 8.2 mo) plus BRCA-wild-type PDX pharmacology (pmid:30647846); deliverability gated by marrow reserve. | Moderate (grade 3+ thrombocytopenia 28.7%, anemia 31%, neutropenia 12.8%) | **Moderate** (Cytopenia-driven dose interruption on thin baseline marrow reserve can erode maintenance dose intensity; the advocate and conservative dissented on this toxicity-as-deliverability axis.) | **Cleanest all-comer guideline and evidence fit with the only tumor-specific BRCA-wild-type pharmacology, but its grade 3+ thrombocytopenia/anemia hit the patient's named veto; deliverable only behind a documented hematology dose plan.** |
| 3 | **Bevacizumab (continued maintenance)**<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-advocate">advocate</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-critic">critic</span></small><br><small><em>dissent:</em> <span class="persona persona-risktaker">risktaker</span></small> | Moderate for PFS only: GOG-218 HR 0.717 (14.1 vs 10.3 mo), RoB2-low but no overall-population OS gain; smallest maintenance effect on the board. | Low (grade 2+ hypertension 22.9%, GI-wall disruption 2.6%; VTE/bleeding class caution) | **Low** (Anti-angiogenic wound-healing and VTE/bleeding risk is a patient-AE caution here, not a mechanism that blunts maintenance benefit; risktaker dissent was magnitude/preference-flavored.) | **The only maintenance that clears both named vetoes on a backbone she already tolerates, but PFS-only with no OS gain and a live VTE/bleeding caution against her IVC-filter history.** |
| 4 | **GEN-1 / IMNN-001 (IL-12 immunogene)**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small> | Moderate but immature: OVATION 2 ITT PFS HR 0.79 (14.9 vs 11.9 mo) and OS HR 0.69 from sponsor topline; CIs unreported, regimen-matched to this patient. | Low (IP delivery reported well tolerated; no per-term grade 3+ table published) | **Low** (IL-12 immunogene acts via the peritoneal TME, sidestepping the foreclosed MSS/TMB-low checkpoint axis; no plausible counter-productive vector flagged.) | **On-study IL-12 continuation that sidesteps the foreclosed checkpoint axis and carries a real OS signal, but efficacy is sponsor-topline-immature and delivery is intraperitoneal, not oral.** |
| 5 | **Letrozole (endocrine maintenance)**<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | Low and weakly evidenced: only a retrospective ROBINS-I-serious series (60% vs 38.5% RFS at 24 mo, pmid:29157627); PR-negativity tempers the ER-driven signal. | Low (arthralgia, bone-density loss on prolonged aromatase inhibition; no named veto triggered) | **Low** (Endocrine blockade has no plausible counter-productive vector in ER-positive HGSC; the dissent here is evidence-quality, not mechanism.) | **The lowest-toxicity oral option that clears every veto and fits the age band, but the evidence is a single retrospective ROBINS-I-serious series and PR-negativity tempers the expected magnitude.** |
| 6 | **Olaparib + bevacizumab (PAOLA-1, contingent on validated HRD-positive)**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>dissent:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>veto:</em> <span class="persona persona-conservative">conservative</span></small> | High ONLY if GIS >=42 confirms HRD-positive: PAOLA-1 subgroup HR 0.33 (37.2 vs 17.7 mo); contingent and foreclosed below 42, ITT effect is a smaller HR 0.59. | High (combination grade 3+ AE ~57%; hypertension 19%, anemia 17%, up to 20% olaparib discontinuation) | **High** (Anti-angiogenic VTE/bleeding stacked on PARP myelosuppression against an IVC-filter history; the conservative's toxicity veto stood on this mechanism.) | **Highest-magnitude maintenance if HRD-positive is confirmed, but contingent on a GIS she lacks and held back by a toxicity veto and an evidence-quality dissent on a subgroup-only effect estimate.** |
| 7 | **Trastuzumab deruxtecan (HER2-low IHC 1+, investigational)**<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-critic">critic</span> <span class="persona persona-risktaker">risktaker</span></small><br><small><em>dissent:</em> <span class="persona persona-concensusite">concensusite</span></small> | Low-to-moderate, cross-tumor only: no ovarian IHC 1+ data; rests on HER2-low breast extrapolation (DESTINY-Breast04 PFS HR 0.51) plus the DXd bystander mechanism. | High (ILD/pneumonitis 10-12% incl. fatal cases; grade 3+ AE 52.6%; nausea; anemia) | **Moderate** (Bystander DXd reach is unproven at IHC 1+ antigen density; sparse HER2-positive cells may not seed enough payload to kill neighbors.) | **The one HER2-directed option that clears both named vetoes, but investigational at IHC 1+ ovarian on breast-only extrapolation — a relapse consideration after a confirmatory re-stain, not a maintenance pick.** |

!!! note "How to read this table"
    **Toxicity burden** is patient-level adverse-event severity — the cytopenias, hypertension, ILD, and bleeding a patient would actually experience. **Counter-productive MoA** is a different axis: the mechanism-level risk that a treatment could blunt its own therapeutic goal. The persona pills under each intervention are the at-a-glance board signal; the full per-persona rationale lives on the [board page](board.md). Disitamab vedotin is omitted from this table as a not-recommended, board-vetoed row; it is documented under Classes examined but not ranked.

## Caveats

- **Evidence-base caveats.** The two PARP options and bevacizumab rest on RoB2-low registered phase 3 trials, but bevacizumab is PFS-only with no overall-population OS gain, and ICON7 was open-label. PAOLA-1's load-bearing HR 0.33 is a pre-specified subgroup, not the ITT (HR 0.59). GEN-1's efficacy comes from a sponsor topline and a 2025 abstract with no peer-reviewed safety table. Letrozole rests on a single non-randomized retrospective series (ROBINS-I serious, n=80), and its design source is flagged for screener reconciliation. T-DXd at IHC 1+ ovarian has no indication data at all — the case is cross-tumor extrapolation from HER2-low breast plus a preclinical bystander mechanism, with a 10-12% ILD rate that has been fatal — and disitamab vedotin's only HER2-low read is an abstract-only PAM-selected breast series.
- **Compartment / biomarker dependencies.** The maintenance ranking is stable across the GIS result except for rank 6: olaparib + bevacizumab is foreclosed unless a validated MyChoice CDx GIS returns at least 42, and the Altera qualitative instability call does not satisfy the companion-diagnostic definition. The HER2-directed option depends on the confirmatory re-stain: the IHC 1+ rests on a single specimen Altera could not evaluate, and a re-stain reading HER2 0 would take T-DXd off the table. SOLO1 olaparib monotherapy is foreclosed by confirmed BRCA-wild-type status, and the MSS/TMB-low profile forecloses tumor-agnostic checkpoint inhibition.
- **What would change the ranking.** A MyChoice GIS at least 42, paired with a documented anticoagulation/BP-management plan, would move olaparib + bevacizumab from last toward first. A documented hematology-supported dose plan would lift the conservative's conditional veto on niraparib and close its gap with rucaparib. A confirmatory HER2 re-stain that holds at 1+ keeps T-DXd as a documented relapse option; a re-stain of HER2 0 forecloses it, while a 2+/3+ result would move it toward (or onto) the tumor-agnostic label.
- **Re-scoping caveat.** If the patient's preference shifts to accept myelosuppression risk with hematology support, the PARP options strengthen at the top; if tolerability concerns deepen, bevacizumab or letrozole rise as the veto-clearing, lower-burden choices, and T-DXd stays a relapse-only HER2 option regardless.

## Sources

**PMIDs**

- [20033066](https://pubmed.ncbi.nlm.nih.gov/20033066)
- [22204724](https://pubmed.ncbi.nlm.nih.gov/22204724)
- [22204725](https://pubmed.ncbi.nlm.nih.gov/22204725)
- [29157627](https://pubmed.ncbi.nlm.nih.gov/29157627)
- [30647846](https://pubmed.ncbi.nlm.nih.gov/30647846)
- [31562799](https://pubmed.ncbi.nlm.nih.gov/31562799)
- [31851799](https://pubmed.ncbi.nlm.nih.gov/31851799)
- [35658487](https://pubmed.ncbi.nlm.nih.gov/35658487)
- [35665782](https://pubmed.ncbi.nlm.nih.gov/35665782)
- [37870536](https://pubmed.ncbi.nlm.nih.gov/37870536)
- [37988648](https://pubmed.ncbi.nlm.nih.gov/37988648)
- [39282896](https://pubmed.ncbi.nlm.nih.gov/39282896)

**NCTs**

- [NCT00262847](https://clinicaltrials.gov/study/NCT00262847)
- [NCT02477644](https://clinicaltrials.gov/study/NCT02477644)
- [NCT02655016](https://clinicaltrials.gov/study/NCT02655016)
- [NCT03393884](https://clinicaltrials.gov/study/NCT03393884)
- [NCT03522246](https://clinicaltrials.gov/study/NCT03522246)
- [NCT06003231](https://clinicaltrials.gov/study/NCT06003231)

## Transparency artifacts

- [Trial table](trials.md) — 21 screened trials, all columns.
- [Evidence table](evidence.md) — 14 clinical-evidence rows with effect sizes, variance, and toxicity.
- [Manuscripts inventory](manuscripts.md) — master flat list of every paper considered (clinical + preclinical).
- [Board proceedings](board.md) — 5 positions and 20 cross-critiques with the full agreement matrix.
- [Recommendations table](recommendations.md) — the forwardable ranked-options table.
- [Plain-language summary](plain_language.md) — the patient-facing translation.

## Run log

Authored 2026-06-26 by the PI agent on the re-run after a HER2-low (IHC 1+) targetable feature was added and the full dossier and board were refreshed. Supplied: a scrubbed profile (now seven targetable features), preferences, the target-validation file (with five HER2 workup rows), 21 trials, 14 clinical-evidence and 17 preclinical-evidence rows, and a fresh board record (5 positions, 20 critiques regenerated with HER2 in the mix). Every biomarker reads `confirmed`, including HER2-low, so the ranking stays a single unbranched list with `scenario: null` on each row; the GIS and the HER2 re-stain are surfaced under Workup considerations rather than as ranked diagnostic rows. The HER2-low ADCs were integrated per Hard Rule 6: trastuzumab deruxtecan is ranked seventh as a real but investigational, relapse-context option (status considered_with_caveats, target her2_low), never as approved standard care, and disitamab vedotin is kept as a rank-8 not-recommended row on a unanimous MMAE-toxicity veto. Two departures from the prior six-feature synthesis are recomputed from the refreshed board and worth flagging: rucaparib rose to agreement_score 0.8 (the refreshed board added conservative and advocate endorsements and dropped risktaker, who now ranks niraparib first), and olaparib + bevacizumab now carries a single conservative toxicity veto plus critic and advocate dissents (refreshed critic ranked it fourth rather than vetoing, so it is scored as a dissent), landing at -0.4. The clinical order of the six prior options is preserved. Agreement scores, ranks, vetoes, and dissents were computed from the board files; the DESTINY-Breast06 PFS HR is reported as the published 0.62 (the screener row's 0.64 was reconciled to the publication). All eight recommendation rows validate against the schema. The letrozole design-source mismatch is inherited from the dossier and logged for a screener re-run.

<!-- libby:downloads:begin -->

## Downloads

### HTML

- [Target validation paths](target_validation.md?v=9923877e) — per-feature biomarker-workup table with providers and references, sortable in-browser
- [Recommendations table](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-recommendations.html?v=83b565ec) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Preclinical recommendations](preclinical_recommendations.md?v=6e4babf2) — forward-looking horizon scan of earlier-than-clinical candidate drugs, compounds, and strategies, in a sortable in-browser table
- [Preclinical recommendations (offline)](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-preclinical.html?v=de5f8378) — same preclinical horizon scan packaged as a self-contained HTML that opens offline
- [Access guide](accessibility.md?v=c675a486) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Access guide (offline)](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-accessibility.html?v=4bcd4526) — same access-guide content packaged as a self-contained HTML that opens offline
- [Master manuscripts table](manuscripts.md?v=4c89f134) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Master manuscripts table (offline)](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-manuscripts.html?v=bb3a11c6) — same manuscripts inventory packaged as a self-contained HTML that opens offline

### PDF

- [Target validation paths](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-target-validation.pdf?v=7a9f3ba4) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-recommendations.pdf?v=57631e33) — ranked options + pipeline context + evidence in detail, in a print-friendly PDF
- [Preclinical recommendations](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-preclinical.pdf?v=d6f1a1e8) — forward-looking horizon scan of earlier-than-clinical candidates, one deep section per candidate, in a print-friendly PDF
- [Access guide](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-accessibility.pdf?v=38e69e61) — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF
- [Master manuscripts table](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-manuscripts.pdf?v=1483d570) — every paper considered — n, effect, variance, toxicities, in a print-friendly PDF
- [Patient/caregiver PDF](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-plain-language.pdf?v=81b64e34) — plain-language summary

<!-- libby:downloads:end -->

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
