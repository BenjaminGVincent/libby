<meta name="robots" content="noindex">

# `hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq`

<!-- libby:case-output:begin -->

## Case output

- [Target validation paths (PDF)](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-target-validation.pdf?v=0febdbf0) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table (HTML)](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-recommendations.html?v=32e613d3) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide (HTML)](accessibility.md?v=5053f606) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, sortable in-browser
- [Access guide (offline HTML)](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-accessibility.html?v=dad5e85a) — same access-guide content as the in-browser page, packaged as a self-contained HTML that opens offline
- [Master manuscripts table (HTML)](manuscripts.md?v=1819364a) — every paper considered — n, effect, variance, toxicities, sortable in-browser
- [Master manuscripts table (offline HTML)](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-manuscripts.html?v=f6ff907f) — same manuscripts inventory as the in-browser page, packaged as a self-contained HTML that opens offline
- [Patient/caregiver PDF](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-plain-language.pdf?v=d4474f6b) — plain-language summary

<!-- libby:case-output:end -->
## Research question

In newly-diagnosed, platinum-responsive, R0-resected Stage IIIc high-grade serous tubo-ovarian carcinoma with wild-type germline BRCA, what maintenance interventions could target homologous-recombination status, the VEGF / angiogenesis axis, and ER expression, gated on the pending tumor HRD / somatic-BRCA assay?

## Patient profile (scrubbed)

- **Primary site / histology:** ovary — high-grade serous carcinoma (tubo-ovarian / primary peritoneal; WT1+, PAX8+, SOX17+, CK7+)
- **Stage:** IIIc, status-post interval radical cytoreduction (TAH/BSO + omentectomy + bilateral ureterolysis) with R0 resection
- **Performance status:** ECOG 1 (estimated; not explicitly documented)
- **Age band:** 70-79
- **Sex:** female
- **Biomarkers:**
    - **HRD / genomic instability (tumor) — `ngs_pending`; not yet resulted.** Decision resolution: genomic-instability score (e.g. Myriad MyChoice GIS ≥42) and/or somatic BRCA1/2 from tumor NGS. Gates PARP-inhibitor maintenance eligibility and magnitude.
    - **Somatic BRCA1/2 (tumor) — `ngs_pending`; not yet resulted.** From the same tumor NGS panel; refines PARP expectation independent of germline.
    - **BRCA1/2 (germline) — confirmed wild-type** (74-gene hereditary-cancer panel). Resolves hereditary status but not somatic BRCA or tumor HRD.
    - **TP53 — confirmed** abnormal (p53 IHC diffuse strong nuclear overexpression >80%), an accepted surrogate for a TP53 mutation defining HGSC biology.
    - **MSI / MMR — `ngs_pending`.** dMMR / MSI-high would open tumor-agnostic checkpoint-inhibitor eligibility; not available.
    - **ER — confirmed positive** (~80% of nuclei, weak-moderate intensity). **PR — confirmed negative.**
    - **HER2 — confirmed negative** (IHC 1+). **FOLR1 — confirmed negative** (<75%, below the mirvetuximab threshold).
    - **CA-125 — normalized on therapy** (peak 940 → 11.6 U/mL). **Signatera ctDNA (MRD) — cleared to Not Detected** (30.3 → 0 MTM/mL).
- **Prior / current therapy:** 1L neoadjuvant carboplatin + paclitaxel + bevacizumab with GEN-1 (IMNN-001, IL-12 immunogene therapy) , an investigational IL-12 immunogene therapy, x4 cycles, best response PR; status-post interval R0 cytoreduction; now on post-debulking carboplatin + paclitaxel + GEN-1.
- **Organ function:** eGFR 98, creatinine 0.49, AST 27, ALT 16, bilirubin 1.5, WBC 3.5.

## Preferences

- **Efficacy/toxicity weight:** 0.7 (efficacy-leaning, tolerability-aware given the age band)
- **Toxicity vetoes:** additional peripheral neuropathy; severe myelosuppression / febrile neutropenia
- **Modality constraints:** oral or low-infusion-burden preferred; caution with agents carrying thrombotic or bleeding risk (history of high VTE risk; prior IVC filter)
- **Free text:** efficacy-leaning overall but tolerability-aware; ECOG estimated at 1; the highest-value open question is the pending tumor HRD / somatic-BRCA result, which gates PARP-inhibitor maintenance — treat its confirmatory assay as the rank-1 shared workup.
- **Trials preferred:** yes

<!-- libby:target-validation:begin -->

## Target validation paths

One pending result decides the maintenance strategy: the tumor HRD genomic-instability score plus somatic BRCA1/2, run on archival FFPE from the interval-debulking specimen. A positive read (Myriad MyChoice GIS at or above 42, FoundationOne CDx genomic LOH-high, or a somatic BRCA1/2 mutation) qualifies olaparib plus bevacizumab via NCT02477644 and, when a somatic BRCA mutation is present, single-agent olaparib via NCT01844986. niraparib via NCT02655016 is an option regardless of the score, with larger benefit if it returns positive. If the genomic-instability score is negative and somatic BRCA is wild-type, the two HRD-positive PARP options drop out; the next conversation about standard 2L+ care belongs to the treating team, not this report. The remaining assays below sharpen context and later-line sequencing rather than gating the frontline choice.

### HRD

The essential test is the tumor HRD genomic-instability score plus somatic BRCA1/2 on archival FFPE, ordered as an FDA companion diagnostic (Myriad MyChoice CDx at the GIS at-or-above-42 cutoff, or FoundationOne CDx reporting genomic LOH). One assay returns both pending biomarkers, so a single FFPE order resolves the somatic BRCA call and the genomic-instability score together. Germline BRCA is already wild-type, so this covers the somatic and genomic-scar gap germline testing cannot reach. Two high-priority co-tests should run on the same block: MSI / MMR status (MMR IHC for MLH1, PMS2, MSH2, MSH6, or MSI by NGS or PCR), since dMMR or MSI-high would open tumor-agnostic checkpoint-inhibitor eligibility, and a comprehensive somatic NGS panel that captures non-BRCA HR-pathway genes (RAD51C, RAD51D, PALB2, BRIP1) plus other actionable drivers. As a low-priority, later option, a plasma ctDNA panel for BRCA1/2 reversion variants can monitor for acquired PARP-inhibitor resistance once maintenance is underway, but it does not gate the baseline decision.

### ER

ER is already reported positive at about 80% of nuclei with weak-to-moderate intensity, which supports a low-toxicity endocrine-maintenance rationale that fits her age and preference for oral therapy. A reference-laboratory ER / PR IHC read with standardized ASCO/CAP scoring (Allred or percent-plus-intensity) is medium priority: it confirms staining quality and quantifies intensity, which matters because PR-negativity tempers the expected endocrine benefit. This refines later-line sequencing rather than gating the frontline maintenance decision.

### IL-12

The patient is on investigational IL-12 immunogene therapy whose mechanism depends on a T-cell-inflamed microenvironment. Tumor-infiltrating lymphocyte density (CD3/CD8) and PD-L1 IHC (22C3 or SP263), with multiplex immune profiling where available, characterize that context. These are low-priority, research-grade reads for the on-study setting; they do not gate a standard-of-care decision and are best treated as supportive correlative data.

### Where to order these assays

| Assay | Provider | Decision gated | Contact |
|---|---|---|---|
| **Tumor HRD genomic-instability score plus somatic BRCA1/2 (FDA companion diagnostic; e.g. Myriad MyChoice CDx, GIS >=42, or FoundationOne CDx genomic LOH)** | **Myriad Genetics *(preferred)* (MyChoice CDx)** | **Olaparib + bevacizumab maintenance (PAOLA-1) if HRD-positive; niraparib maintenance regardless of HRD, with magnitude of benefit refined by the score.** | **[test info](https://myriad.com/genetic-tests/mychoice-cdx-hrd-test/) · 322 North 2200 West, Salt Lake City, UT 84116 · 1-800-469-7423** |
| Tumor HRD genomic-instability score plus somatic BRCA1/2 (FDA companion diagnostic; e.g. Myriad MyChoice CDx, GIS >=42, or FoundationOne CDx genomic LOH) | Foundation Medicine *(FoundationOne CDx)* | Olaparib + bevacizumab maintenance (PAOLA-1) if HRD-positive; niraparib maintenance regardless of HRD, with magnitude of benefit refined by the score. | [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| Tumor HRD genomic-instability score plus somatic BRCA1/2 (FDA companion diagnostic; e.g. Myriad MyChoice CDx, GIS >=42, or FoundationOne CDx genomic LOH) | Caris Life Sciences *(MI Cancer Seek / Genomic LOH)* | Olaparib + bevacizumab maintenance (PAOLA-1) if HRD-positive; niraparib maintenance regardless of HRD, with magnitude of benefit refined by the score. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| Tumor HRD genomic-instability score plus somatic BRCA1/2 (FDA companion diagnostic; e.g. Myriad MyChoice CDx, GIS >=42, or FoundationOne CDx genomic LOH) | Tempus *(Tempus xT / HRD)* | Olaparib + bevacizumab maintenance (PAOLA-1) if HRD-positive; niraparib maintenance regardless of HRD, with magnitude of benefit refined by the score. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 · 1-800-739-4137 |
| **MSI / MMR status (MMR IHC for MLH1, PMS2, MSH2, MSH6 and/or MSI by NGS or PCR)** | **NeoGenomics Laboratories *(preferred)* (MMR IHC panel / MSI)** | **Tumor-agnostic checkpoint inhibitor (pembrolizumab / dostarlimab) eligibility in dMMR / MSI-high disease.** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| MSI / MMR status (MMR IHC for MLH1, PMS2, MSH2, MSH6 and/or MSI by NGS or PCR) | Quest Diagnostics *(MMR IHC / MSI by PCR)* | Tumor-agnostic checkpoint inhibitor (pembrolizumab / dostarlimab) eligibility in dMMR / MSI-high disease. | [test info](https://www.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| MSI / MMR status (MMR IHC for MLH1, PMS2, MSH2, MSH6 and/or MSI by NGS or PCR) | Caris Life Sciences *(MSI by NGS)* | Tumor-agnostic checkpoint inhibitor (pembrolizumab / dostarlimab) eligibility in dMMR / MSI-high disease. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| **Comprehensive somatic NGS panel (BRCA1/2, RAD51C/D, PALB2, BRIP1, other HR-pathway genes; plus broad actionable drivers and tumor mutational burden)** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Identifies non-BRCA HR-pathway alterations supporting PARP-inhibitor use and screens for any off-pathway actionable driver.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| Comprehensive somatic NGS panel (BRCA1/2, RAD51C/D, PALB2, BRIP1, other HR-pathway genes; plus broad actionable drivers and tumor mutational burden) | Tempus *(Tempus xT)* | Identifies non-BRCA HR-pathway alterations supporting PARP-inhibitor use and screens for any off-pathway actionable driver. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 · 1-800-739-4137 |
| Comprehensive somatic NGS panel (BRCA1/2, RAD51C/D, PALB2, BRIP1, other HR-pathway genes; plus broad actionable drivers and tumor mutational burden) | Caris Life Sciences *(MI Cancer Seek)* | Identifies non-BRCA HR-pathway alterations supporting PARP-inhibitor use and screens for any off-pathway actionable driver. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| **ER / PR IHC, reference-laboratory confirmation with ASCO/CAP scoring (Allred or percent-plus-intensity)** | **NeoGenomics Laboratories *(preferred)* (ER/PR IHC)** | **Endocrine (aromatase-inhibitor) maintenance or later-line rationale in ER-positive HGSC.** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| ER / PR IHC, reference-laboratory confirmation with ASCO/CAP scoring (Allred or percent-plus-intensity) | Quest Diagnostics *(ER/PR by IHC)* | Endocrine (aromatase-inhibitor) maintenance or later-line rationale in ER-positive HGSC. | [test info](https://www.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| **Plasma ctDNA panel for BRCA1/2 reversion and HR-pathway resistance variants** | **Guardant Health *(preferred)* (Guardant360 CDx)** | **PARP-inhibitor resistance surveillance via acquired BRCA reversion; does not gate baseline maintenance selection.** | **[test info](https://guardanthealth.com/guardant360/) · 3100 Hanover Street, Palo Alto, CA 94304 · 1-855-698-8887** |
| Plasma ctDNA panel for BRCA1/2 reversion and HR-pathway resistance variants | Foundation Medicine *(FoundationOne Liquid CDx)* | PARP-inhibitor resistance surveillance via acquired BRCA reversion; does not gate baseline maintenance selection. | [test info](https://www.foundationmedicine.com/test/foundationone-liquid-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| **Tumor-infiltrating lymphocyte density and PD-L1 IHC (CD3/CD8 plus PD-L1 22C3 or SP263), with multiplex immune profiling if available** | **NeoGenomics Laboratories *(preferred)* (PD-L1 IHC / TIL profiling)** | **Correlative immune context for on-study IL-12 therapy; does not gate standard-of-care selection.** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| Tumor-infiltrating lymphocyte density and PD-L1 IHC (CD3/CD8 plus PD-L1 22C3 or SP263), with multiplex immune profiling if available | Tempus *(Tempus xT / immune profiling)* | Correlative immune context for on-study IL-12 therapy; does not gate standard-of-care selection. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 · 1-800-739-4137 |

### Biomarker plan

| Recommended assay | Rationale | Suggested assay provider | Tissue requirements |
|---|---|---|---|
| Tumor HRD genomic-instability score plus somatic BRCA1/2 (FDA companion diagnostic; e.g. Myriad MyChoice CDx, GIS >=42, or FoundationOne CDx genomic LOH) | This pending result is the primary decision point for a newly diagnosed, platinum-responsive, R0 Stage IIIc high-grade serous case with wild-type germline BRCA. A positive HRD score (Myriad MyChoice GIS >=42 or a somatic BRCA1/2 mutation) qualifies the patient for olaparib plus bevacizumab maintenance per PAOLA-1, while niraparib maintenance is an option regardless of HRD but with larger benefit when HRD-positive. Without this assay the maintenance choice cannot be made correctly; the deep platinum and ctDNA response is consistent with HRD but is not diagnostic of it. | Myriad Genetics *(MyChoice CDx)* · [test info](https://myriad.com/genetic-tests/mychoice-cdx-hrd-test/) · 322 North 2200 West, Salt Lake City, UT 84116 · 1-800-469-7423 | archival FFPE acceptable (no fresh biopsy needed) |
| MSI / MMR status (MMR IHC for MLH1, PMS2, MSH2, MSH6 and/or MSI by NGS or PCR) | MSI-high or mismatch-repair-deficient status would open tumor-agnostic checkpoint-inhibitor eligibility (pembrolizumab or dostarlimab), an option the current profile cannot rule in or out because the result is not back. dMMR is uncommon in high-grade serous ovarian cancer but is inexpensive to exclude and changes later-line strategy if present. MMR IHC and MSI usually run on the same FFPE block already submitted for the HRD panel. | NeoGenomics Laboratories *(MMR IHC panel / MSI)* · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | archival FFPE acceptable |
| Comprehensive somatic NGS panel (BRCA1/2, RAD51C/D, PALB2, BRIP1, other HR-pathway genes; plus broad actionable drivers and tumor mutational burden) | A comprehensive panel captures non-BRCA homologous-recombination genes (RAD51C, RAD51D, PALB2, BRIP1) that contribute to HRD and to PARP-inhibitor benefit beyond the genomic-instability score alone, and it flags any other actionable driver or high tumor mutational burden. Restricting tumor sequencing to BRCA1/2 would miss HR-pathway alterations and any off-pathway target. This is usually the same panel that returns the somatic BRCA and HRD score, so it adds breadth at no extra tissue cost. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | archival FFPE acceptable |
| ER / PR IHC, reference-laboratory confirmation with ASCO/CAP scoring (Allred or percent-plus-intensity) | ER is already reported positive at about 80% of nuclei with weak-to-moderate intensity, which supports a low-toxicity endocrine-maintenance rationale (aromatase inhibition) that fits the patient's age and preference for oral, low-burden therapy. A reference-laboratory ER/PR read with standardized scoring confirms the staining quality and quantifies intensity, since PR-negativity tempers the expected magnitude of endocrine benefit. This refines later-line sequencing rather than gating a frontline decision, so it is not essential. | NeoGenomics Laboratories *(ER/PR IHC)* · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | archival FFPE acceptable |
| Plasma ctDNA panel for BRCA1/2 reversion and HR-pathway resistance variants | If a somatic BRCA1/2 mutation is confirmed and PARP-inhibitor maintenance begins, plasma ctDNA can later detect secondary reversion mutations that restore homologous recombination and drive PARP-inhibitor resistance. This is a surveillance tool for the maintenance phase, not a baseline gate, so it is low priority now; the patient already has tumor-informed Signatera ctDNA that tracks residual disease. Order it only at biochemical or molecular progression on a PARP inhibitor. | Guardant Health *(Guardant360 CDx)* · [test info](https://guardanthealth.com/guardant360/) · 3100 Hanover Street, Palo Alto, CA 94304 · 1-855-698-8887 | two 10 mL Streck blood tubes |
| Tumor-infiltrating lymphocyte density and PD-L1 IHC (CD3/CD8 plus PD-L1 22C3 or SP263), with multiplex immune profiling if available | The patient is on investigational IL-12 immunogene therapy (GEN-1 / IMNN-01) on trial, whose mechanism depends on a T-cell-inflamed microenvironment. CD3/CD8 infiltrate density and PD-L1 status characterize that context and inform any immunotherapy-combination reasoning, but they are research-grade for this on-study setting and do not gate a standard-of-care decision. Treat as supportive correlative data, not part of the required workup. | NeoGenomics Laboratories *(PD-L1 IHC / TIL profiling)* · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | archival FFPE acceptable |

---

*Decision support, not medical advice. Confirm assay availability and current standards with the treating team and the local pathology service.*

<!-- libby:target-validation:end -->

## Scope summary

Twelve trial / evidence rows surfaced (the four 1L-maintenance phase-3 RCTs that anchor the decision, plus rucaparib as an HRD-stratified comparator, a recurrent-setting olaparib-cediranib doublet, two ER-positive endocrine studies, and the GEN-1 / IMNN-001 program). Nine clinical-evidence rows (all included) and nine preclinical rows (six included, three logged-excluded as mechanism duplicates). Seven ranked rows: a rank-1 HRD / somatic-BRCA workup gate, then niraparib (rank 2, *considered with caveats*) and bevacizumab (rank 3) that do not wait on the score, the HRD-positive-conditional olaparib + bevacizumab (rank 4, *considered with caveats*) and somatic-BRCA-conditional olaparib monotherapy (rank 5), letrozole (rank 6), and the GEN-1 / IMNN-001 program (rank 7, *not recommended*). Agreement scores run from 1.0 on the workup down to −0.2 on GEN-1. All five personas converged on the workup. The board split on the lead therapeutic — three personas put niraparib or a PARP-based option first, two put bevacizumab or letrozole first — one veto from the conservative on olaparib + bevacizumab (lifted in the HRD-positive branch with a monitoring plan), and one veto from the critic on GEN-1 (which stands).

## Cross-cutting caveat (read first)

**The tumor HRD / somatic-BRCA result is pending (`ngs_pending`), and it is the load-bearing input for the whole maintenance decision.** The decision resolution is a genomic-instability score (Myriad MyChoice GIS ≥42 or an equivalent LOH-high call) and/or a somatic BRCA1/2 mutation from tumor NGS. Her germline BRCA is wild-type, so germline testing has already done its work; only the somatic and genomic-scar read is outstanding, and the deep platinum response, R0 resection, and ctDNA clearance to Not Detected are consistent with HR-deficient biology without proving it.

- **The ranking spans three of her stated targetable features.** The HRD axis (PARP inhibitors), the VEGF axis (bevacizumab, which she already receives), and ER expression (letrozole) are all in scope. Two PARP options — olaparib + bevacizumab and olaparib monotherapy — are tagged `hrd_status:positive` because their guideline footing or eligibility depends on the pending result. Niraparib and bevacizumab are not tagged, because neither waits on the score: PRIMA gives niraparib an all-comers benefit, and bevacizumab targets the VEGF axis independently.
- **What the result forecloses.** If the HRD score is negative and somatic BRCA is wild-type, the two `hrd_status:positive` PARP rows (ranks 4-5) drop out: olaparib + bevacizumab loses its category-1 footing and collapses back toward bevacizumab alone, and single-agent olaparib has no eligibility without a somatic BRCA mutation. Niraparib (rank 2) and bevacizumab (rank 3) remain available regardless, so a negative result narrows the options rather than emptying them.
- **The workup is the rank-1 row because it gates the largest-magnitude options.** It runs on archival FFPE from the interval-debulking specimen — no fresh biopsy, which matters given her bleeding/VTE history and reluctance for added procedures. Turnaround is two to four weeks. The somatic BRCA call and the genomic-instability score come from the same panel, so one order resolves both pending biomarkers; MSI / MMR and the broader HR-pathway gene set (RAD51C/D, PALB2, BRIP1) can run on the same block.

## Intervention grouping

- **PARP inhibitors (HRD axis):** niraparib all-comers (PRIMA, [NCT02655016](https://clinicaltrials.gov/study/NCT02655016), [PMID 31562799](https://pubmed.ncbi.nlm.nih.gov/31562799)); olaparib + bevacizumab HRD-positive (PAOLA-1, [NCT02477644](https://clinicaltrials.gov/study/NCT02477644), [PMID 31851799](https://pubmed.ncbi.nlm.nih.gov/31851799)); olaparib monotherapy BRCA-mutated (SOLO1, [NCT01844986](https://clinicaltrials.gov/study/NCT01844986), [PMID 30345884](https://pubmed.ncbi.nlm.nih.gov/30345884)). Rucaparib (ATHENA-MONO, [PMID 35658487](https://pubmed.ncbi.nlm.nih.gov/35658487)) sits in the dossier as an HRD-stratified class comparator.
- **Anti-VEGF (angiogenesis axis):** bevacizumab concurrent + maintenance (GOG-218, [NCT00262847](https://clinicaltrials.gov/study/NCT00262847), [PMID 22204724](https://pubmed.ncbi.nlm.nih.gov/22204724); ICON7, [NCT00483782](https://clinicaltrials.gov/study/NCT00483782), [PMID 22204725](https://pubmed.ncbi.nlm.nih.gov/22204725)).
- **Endocrine (ER axis):** letrozole maintenance ([PMID 29157627](https://pubmed.ncbi.nlm.nih.gov/29157627)); anastrozole cross-tumor precedent in granulosa-cell disease ([PMID 34412908](https://pubmed.ncbi.nlm.nih.gov/34412908)).
- **IL-12 immunogene therapy (on-study microenvironment axis):** GEN-1 / IMNN-001 program — OVATION-2 ([NCT03393884](https://clinicaltrials.gov/study/NCT03393884)) and the registrational OVATION-3 ([NCT06915025](https://clinicaltrials.gov/study/NCT06915025)).

## Top interventions

### Rank 1. Tumor HRD genomic-instability score + somatic BRCA1/2

*The pending assay that decides the maintenance strategy. Runs on archival FFPE; no new procedure.*

#### Evidence base

The maintenance choice for a newly-diagnosed, platinum-responsive, R0 Stage IIIc HGSC turns on HRD / somatic-BRCA status, and four low-RoB phase-3 RCTs in her exact 1L setting attach explicit biomarker conditions to their benefit. A genomic-instability score ≥42 or a somatic BRCA1/2 mutation places her in the HRD-positive subgroup where olaparib + bevacizumab reaches a PFS HR of 0.33 (PAOLA-1, [PMID 31851799](https://pubmed.ncbi.nlm.nih.gov/31851799)); a somatic BRCA mutation specifically opens single-agent olaparib per SOLO1 (PFS HR 0.30, [PMID 30345884](https://pubmed.ncbi.nlm.nih.gov/30345884)). PRIMA carries niraparib across all-comers (HR 0.62) but sharpens to HR 0.43 in the HRD-positive subgroup ([PMID 31562799](https://pubmed.ncbi.nlm.nih.gov/31562799)). The same tumor NGS panel returns both the somatic BRCA call and the genomic-instability score.

#### Likelihood of desired effect

This is a diagnostic, not a therapy, so the relevant likelihood is decision resolution rather than tumor response. The result tells her whether the HRD-positive PARP options (ranks 4-5) are reachable. Her germline is already wild-type, so this assay covers exactly the somatic and genomic-scar gap that germline testing cannot reach.

#### Toxicity profile

- None. NGS on archival FFPE from the interval-debulking specimen.
- No fresh biopsy required, which matters given her bleeding/VTE history and prior IVC filter.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. Every persona named the pending HRD / somatic-BRCA result as the rank-1 move, and the patient's own framing put it there first. The advocate flagged that it lives in target-validation rather than the intervention files, so it could not be ranked as an intervention_id during the board rounds, but agreed it gates all four therapeutic picks.

#### Practical considerations

Archival FFPE is acceptable; turnaround is two to four weeks. Confirm which companion diagnostic the treating institution uses — Myriad MyChoice reports the GIS ≥42 cutoff used as the PAOLA-1 and PRIMA eligibility threshold, while FoundationOne CDx reports genomic LOH as its HRD signal. Run MSI / MMR and the broader HR-pathway gene set on the same block: dMMR would open checkpoint-inhibitor eligibility, and RAD51C/D, PALB2, or BRIP1 alterations support PARP benefit beyond the score alone.

#### Why this rank

It is the precondition for ranks 4-5 and refines the magnitude of rank 2. The board treated it as a gate, not a therapy, and the agreement score of 1.0 reflects that nobody disputed it.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| HRD / somatic-BRCA assay (gates PARP eligibility) | Resolves HRD-positive subgroup placement; decides ranks 4-5 reachability | None — diagnostic on archival FFPE | [NCT02477644](https://clinicaltrials.gov/study/NCT02477644), [NCT02655016](https://clinicaltrials.gov/study/NCT02655016) |

---

### Rank 2. niraparib (1L maintenance)

*The PARP option that does not wait on the HRD score. One persistent dissent on the cytopenia profile against her myelosuppression veto.*

#### Evidence base

PRIMA ([PMID 31562799](https://pubmed.ncbi.nlm.nih.gov/31562799); [NCT02655016](https://clinicaltrials.gov/study/NCT02655016)) is a low-RoB double-blind phase-3 of 733 patients with a registered ITT PFS primary endpoint that was hit at HR 0.62 (95% CI 0.50-0.76), mPFS 13.8 vs 8.2 months. The benefit holds without the pending HRD score, which is what separates it from the olaparib-based rows. The pre-specified HRD-positive subgroup reads HR 0.43 (0.31-0.59), so the pending score refines her expected magnitude rather than deciding her eligibility. The preclinical PK work ([PMID 30647846](https://pubmed.ncbi.nlm.nih.gov/30647846)) shows roughly 3.3x tumor-to-plasma exposure that drives activity in BRCA-wild-type models — relevant for a patient whose HRD status is still open.

#### Likelihood of desired effect

Moderate across all-comers, higher if she lands HRD-positive. The floor is real on a pending score, which is the reason three personas put it first or near-first. The magnitude firms up once the genomic-instability score returns, but unlike the olaparib options it does not collapse if that score is negative.

#### Toxicity profile

- Grade 3+ anemia 31% and thrombocytopenia 28.7% on the fixed 300 mg start; cumulative G3+ thrombocytopenia rose to 39.7% in the 3.5-year update.
- Grade 3+ neutropenia 12.8%.
- **This is the one ranked option that touches a stated veto.** The cytopenia profile sits directly on her severe-myelosuppression / febrile-neutropenia veto. The weight-and-platelet individualized starting dose lowers the rates (thrombocytopenia to ~21.9%) and is the prerequisite mitigation — it has to travel with the recommendation, not soften it afterward.

#### Counter-productive mechanisms / dissent

The critic ranks niraparib first at high confidence on RoB grounds; the concensusite ranks it first on guideline fit. The conservative dissents — on the confidence, not the drug — because the cytopenia rates engage her veto and the 3.5-year thrombocytopenia figure is not a footnote for a 70-79 patient on multi-year maintenance. The advocate and concensusite both qualify their support the same way: the individualized starting dose is the condition that keeps it aligned with her preferences. The critic also asked (qualified) that the warrant be cited as PRIMA rather than the NCCN category 2A tier, since a consensus tier can shift between guideline versions while the RCT result does not.

#### Practical considerations

Oral once daily, which matches her modality preference. NCCN Ovarian v3.2025 lists it as category 2A 1L maintenance for all-comers. Her age band sits at the older end of the enrolled population, so the individualized starting dose and tight CBC monitoring carry more weight here than they would in a younger patient. Mature ITT overall-survival data are weaker than the SOLO1 OS readout.

#### Why this rank

It leads the therapeutic options because it is the one PARP that does not wait on the assay, and the board's center of gravity (critic and concensusite at rank 1, risktaker at rank 2) sits here. It edges out bevacizumab at the same agreement score (0.6) on her efficacy-leaning 0.7 weight, since niraparib carries the larger effect, but the gap is narrow. The trade is real: bevacizumab clears both vetoes while niraparib touches one.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| niraparib — PRIMA, n=733, all-comers ITT | PFS HR 0.62 (0.50-0.76); mPFS 13.8 vs 8.2 mo; HRD+ HR 0.43 | G3+ anemia 31%, thrombocytopenia 28.7%, neutropenia 12.8% | [PMID 31562799](https://pubmed.ncbi.nlm.nih.gov/31562799), [NCT02655016](https://clinicaltrials.gov/study/NCT02655016) |

---

### Rank 3. bevacizumab (concurrent + maintenance)

*The lowest-regret interim while the assay is out. Clears both toxicity vetoes; one dissent that it underspends the window.*

#### Evidence base

GOG-218 ([PMID 22204724](https://pubmed.ncbi.nlm.nih.gov/22204724); [NCT00262847](https://clinicaltrials.gov/study/NCT00262847), n=1873) and ICON7 ([PMID 22204725](https://pubmed.ncbi.nlm.nih.gov/22204725); [NCT00483782](https://clinicaltrials.gov/study/NCT00483782), n=1528) establish the anti-angiogenic maintenance regimen she is already receiving in her exact 1L indication. The GOG-218 PFS gain (HR 0.717, 0.625-0.824) came only from the bevacizumab-throughout arm, matching her trajectory. ICON7's largest survival gain landed in the high-risk subgroup — stage IV or stage III with >1cm residual — which overlaps her presentation before R0 resection. Both trials are PFS-only with no ITT OS benefit on final analysis; that is the honest ceiling.

#### Likelihood of desired effect

Moderate for PFS, modest in magnitude. The survival signal is confined to the high-risk subgroup rather than the ITT, so the expected benefit is a delay in progression rather than a survival extension on the strength of these data. It is also the natural backbone if HRD reads positive and olaparib is layered on per PAOLA-1.

#### Toxicity profile

- Grade 2+ hypertension ~22.9% (GOG-218), the dominant and well-managed event.
- No significant excess of GI perforation or fistula vs control.
- Bleeding and thrombotic events are the relevant cautions given her high-VTE history and prior IVC filter — a risk already accepted in her current plan rather than a new one.
- **Clears both stated vetoes:** no myelosuppression, no neuropathy.

#### Counter-productive mechanisms / dissent

The conservative, critic, concensusite, and advocate all endorse continuing it as the interim hold; the advocate and concensusite note it asks nothing new of her and touches neither veto. The risktaker dissents — parking on the lowest-magnitude axis (GOG-218 HR 0.717, no ITT OS) underspends a curative-intent window for an R0 patient whose ctDNA cleared to Not Detected and whose biology reads HR-deficient. That dissent is preference-flavored about how aggressively to spend the window, not a mechanism objection.

#### Practical considerations

NCCN Ovarian v3.2025 keeps it category 2A in her indication. IV q3w is the one infusion burden she has already accepted, so the partial tension with her oral preference is a burden she carries rather than a new one. The IVC-filter history and bleeding/VTE caution stay on the active monitoring list.

#### Why this rank

It ties niraparib on agreement score (0.6) and clears both vetoes, but sits below it because the magnitude is lower and her preferences lean efficacy (0.7). It sits above the HRD-conditional rows because it is available now without waiting on the assay and is the axis she already tolerates.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| bevacizumab — GOG-218, n=1873 (maintenance arm) | PFS HR 0.717 (0.625-0.824); mPFS 14.1 vs 10.3 mo; no ITT OS | G2+ hypertension ~22.9%; bleeding/thrombotic caution | [PMID 22204724](https://pubmed.ncbi.nlm.nih.gov/22204724), [NCT00262847](https://clinicaltrials.gov/study/NCT00262847) |
| bevacizumab — ICON7, n=1528 (open-label) | PFS HR 0.81 (0.70-0.94); high-risk-subgroup OS 39.3 vs 34.5 mo | Hypertension, bleeding/thrombosis class effects | [PMID 22204725](https://pubmed.ncbi.nlm.nih.gov/22204725), [NCT00483782](https://clinicaltrials.gov/study/NCT00483782) |

---

### Rank 4. olaparib + bevacizumab (1L maintenance)

*Conditional on `hrd_status:positive`. Foreclosed if HRD-negative. The biggest effect on the board — and the one that drew a toxicity veto.*

#### Evidence base

PAOLA-1 ([PMID 31851799](https://pubmed.ncbi.nlm.nih.gov/31851799); [NCT02477644](https://clinicaltrials.gov/study/NCT02477644), n=806) is the closest design match in the dossier, because every patient was on bevacizumab — which she already receives — and olaparib is added on top. The ITT PFS was positive at HR 0.59 (0.49-0.72), but the benefit concentrates in the HRD-positive subgroup: PFS HR 0.33 (0.25-0.45), mPFS 37.2 vs 17.7 months, with a 5-year OS rate of 66% vs 48%. The ITT OS was not significant, so the survival headline rests on the pre-specified HRD-positive subgroup rather than a confirmed ITT result.

#### Likelihood of desired effect

High in the HRD-positive subset — the largest magnitude on the table — assuming the positive branch. A negative HRD score forecloses this rec: the add-on loses its category-1 footing and the choice collapses back toward bevacizumab alone. The deep platinum and ctDNA responses are consistent with HRD but cannot substitute for the score.

#### Toxicity profile

- Grade 3-4 anemia 17% (vs <1% on bevacizumab alone) — PARP-attributable, and it brushes her myelosuppression veto from a second direction.
- Grade 3-4 hypertension 19%, lymphopenia 7%, neutropenia 6%.
- **Compounded bleeding / VTE risk.** Stacking a PARP inhibitor onto ongoing anti-VEGF therapy in a patient with high-VTE history and a prior IVC filter is the load-bearing toxicity concern, and it is why the conservative vetoed this as a rank-1 pick.

#### Counter-productive mechanisms / dissent

The conservative issued a veto on toxicity grounds: a PARP on top of ongoing bevacizumab in a high-VTE patient with a prior IVC filter, with PAOLA-1 anemia brushing her marrow veto from a second direction. That veto was explicitly contingent — it stands *"unless and until the HRD score returns positive and a concrete bleeding/VTE and CBC monitoring plan is on the table."* In the HRD-positive branch with that monitoring plan documented, the veto lifts, which is why this row stands at *considered with caveats* rather than *not recommended*. The conservative's and advocate's dissents on the compounded bleeding and anemia load persist, because that concern does not depend on the biomarker. Risktaker (rank 1), critic (rank 3), and concensusite (rank 2, their conditional front-runner) carry it for the HRD-positive HR 0.33.

#### Practical considerations

NCCN Ovarian v3.2025 gives olaparib + bevacizumab a category 1 recommendation for HRD-positive disease (ESMO concurs), but that endorsement is written for the PAOLA-1 population, not specifically for a patient carrying her bleeding and VTE history. The conservative's qualifier from round 2 is the practical instruction: make the bleeding/VTE workup an explicit gate alongside the HRD result, not an afterthought. She is already on bevacizumab, so this adds olaparib rather than starting a new regimen.

#### Why this rank

It sits below the two no-wait options because its benefit is gated on a result that is not back, and its agreement score (0.2) reflects the two persisting dissents on the compounded bleeding/anemia load. It sits above single-agent olaparib (rank 5) despite a lower score because its gate — an HRD score — is broader and more likely to open than the somatic-BRCA mutation that olaparib monotherapy strictly requires, and it is the closest design match to her current regimen.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| olaparib + bevacizumab — PAOLA-1, n=806 | ITT PFS HR 0.59; HRD+ PFS HR 0.33, mPFS 37.2 vs 17.7 mo; HRD+ 5-yr OS 66% vs 48% | G3-4 hypertension 19%, anemia 17% (vs <1% on bev alone), lymphopenia 7% | [PMID 31851799](https://pubmed.ncbi.nlm.nih.gov/31851799), [NCT02477644](https://clinicaltrials.gov/study/NCT02477644) |

---

### Rank 5. olaparib monotherapy (1L maintenance)

*Conditional on `hrd_status:positive` (specifically a somatic BRCA1/2 mutation). Foreclosed if the somatic call is wild-type. The highest-quality evidence in the set, sitting behind the strictest gate.*

#### Evidence base

SOLO1 ([PMID 30345884](https://pubmed.ncbi.nlm.nih.gov/30345884); [NCT01844986](https://clinicaltrials.gov/study/NCT01844986), n=391) has the lowest RoB and the largest effect in the dossier: PFS HR 0.30 (0.23-0.41), mPFS 56.0 vs 13.8 months, and a mature 7-year OS benefit HR 0.55 (0.40-0.76), p=0.0004. That replicated long-term survival readout is what you want from a maintenance drug. The mechanistic floor is solid — the Bryant synthetic-lethality work ([PMID 15829966](https://pubmed.ncbi.nlm.nih.gov/15829966)) and a BRCA2-mutant ovarian PDX ([PMID 21097693](https://pubmed.ncbi.nlm.nih.gov/21097693)) both fix the response to the homologous-recombination defect. SOLO1 enrolled only BRCA-mutated tumors.

#### Likelihood of desired effect

High if a somatic BRCA1/2 mutation is confirmed, with the strongest replicated PFS and OS numbers in the dossier. The catch is the gate: her germline is wild-type, so this rec is reachable only if the tumor NGS returns a somatic variant. Foreclosed if the somatic call is wild-type.

#### Toxicity profile

- Grade 3+ anemia 22%, neutropenia 8%; AE discontinuation 11.5% vs 2.3% placebo.
- AML in 1.2% over long follow-up, all reported cases fatal — a long-term myeloid signal relevant to her marrow-toxicity veto.
- Cleaner than the olaparib + bevacizumab stack on the bleeding axis, since there is no anti-VEGF agent compounding the VTE risk.

#### Counter-productive mechanisms / dissent

No persona dissented or vetoed. Risktaker ranks it as the reserve play that activates the moment a somatic variant returns; the critic ranks it rank 2 on RoB and the mature OS; the concensusite ranks it rank 4 on the conditional guideline gate. All three keep it below the broader options precisely because its eligibility is the narrowest, not because of any objection to the drug.

#### Practical considerations

NCCN Ovarian v3.2025 carries the category 1 recommendation, but only for BRCA-mutated tumors, so the guideline gate does not currently open for her. Oral, matching her modality preference. The 1.2% AML signal across a multi-year maintenance window is worth weighing against her marrow-toxicity caution.

#### Why this rank

Its agreement score (0.6) matches niraparib's, but it sits at rank 5 because its gate is the strictest in the dossier — a somatic BRCA mutation she may not carry — whereas niraparib needs no biomarker and the olaparib + bevacizumab HRD gate is broader. The board's own ordering put it below the combination for the same reason.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| olaparib monotherapy — SOLO1, n=391 (BRCA-mutated) | PFS HR 0.30; mPFS 56.0 vs 13.8 mo; 7-yr OS HR 0.55 | G3+ anemia 22%, neutropenia 8%; AML 1.2% (fatal) | [PMID 30345884](https://pubmed.ncbi.nlm.nih.gov/30345884), [NCT01844986](https://clinicaltrials.gov/study/NCT01844986) |

---

### Rank 6. letrozole (endocrine maintenance)

*Targets her ER-positive biology with the lowest toxicity of any option. One dissent that it spends a high slot on tier-4 evidence.*

#### Evidence base

The direct maintenance evidence is a single non-randomized cohort ([PMID 29157627](https://pubmed.ncbi.nlm.nih.gov/29157627), n=80): 60% vs 38.5% recurrence-free at 24 months (p=0.035) in ER-positive high-grade serous disease, her exact biology. Preclinically the effect tracks ERalpha expression and runs partly through reduced tumor VEGF and microvessel density ([PMID 24410765](https://pubmed.ncbi.nlm.nih.gov/24410765)), with the response confined to ERalpha-positive lines. This is the weakest evidence tier of any ranked option (ROBINS-I:Serious), well below the PARP and bevacizumab RCTs.

#### Likelihood of desired effect

Low-to-moderate, and the 24-month figure comes from a non-randomized cohort, so it should not be read as RCT-grade. Her PR-negativity and the weak-to-moderate ER intensity temper the expected magnitude further. This reads as a low-toxicity holding option rather than a cytoreductive one.

#### Toxicity profile

- Class effects only: hot flushes, arthralgia, fatigue.
- No high-grade hematologic or neuropathic toxicity.
- Clears every preference axis — oral, no marrow toxicity, no neuropathy, no bleeding/VTE risk.

#### Counter-productive mechanisms / dissent

The advocate ranks it second precisely because it clears her whole preference set without a single conflict; the conservative and concensusite both carry it as a low-burden holding option. The risktaker dissents — putting a tier-4 endocrine signal above niraparib inverts her efficacy-leaning 0.7 trade-off, spending a top slot to dodge a manageable, dose-individualized cytopenia risk. The critic adds a qualified note (not a dissent) that the ROBINS-I:Serious label and non-randomized design must stay visible so the 60% figure is not mistaken for trial-grade.

#### Practical considerations

NCCN Ovarian v3.2025 lists aromatase inhibitors among hormone-therapy options for ER-positive disease, so it is not off-guideline outright, but the guideline never elevates this cohort-level evidence to frontline maintenance alongside the category 1/2A data. Anastrozole in granulosa-cell disease ([PMID 34412908](https://pubmed.ncbi.nlm.nih.gov/34412908)) is mechanism precedent in the dossier but cross-tumor only, not her histology.

#### Why this rank

It sits below the PARP and bevacizumab options because its evidence tier is a non-randomized cohort and her PR-negativity tempers the magnitude, but above GEN-1 because it targets a confirmed feature (ER) on real, if weak, clinical data and carries no veto. For a patient who wants to stay off cytopenia-prone drugs, it is the natural low-toxicity holding choice.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| letrozole — Basel cohort, n=80 (ER+ HGSC) | 60% vs 38.5% recurrence-free at 24 mo (p=0.035); non-randomized | Hot flushes, arthralgia, fatigue; no marrow/neuropathic toxicity | [PMID 29157627](https://pubmed.ncbi.nlm.nih.gov/29157627) |

---

## Classes examined but not ranked

- **GEN-1 / IMNN-001 (IL-12 immunogene therapy) — `status: not_recommended`, rank 7.** This targets her on-study IL-12 / tumor-microenvironment feature, so it is in scope, but the critic vetoed it on evidence quality: the OVATION-2 efficacy comes from SITC 2024 and ASCO 2025 toplines with no peer-reviewed primary paper, no PMID, and no structured safety table, and the BRCAm/HRD subgroup it leans on is n=34 with an OS HR confidence interval of 0.11-1.70 that crosses 1. That veto rests on the published-evidence base, not on the HRD biomarker, so it does not lift if the score returns positive. The concensusite dissents on guideline fit — no consensus guideline lists IL-12 immunogene therapy in this setting, so it belongs in her on-study context. The risktaker and advocate carry it as a trial-continuity option for a trial-preferring patient already responding on the regimen, and OVATION-3 ([NCT06915025](https://clinicaltrials.gov/study/NCT06915025)) would let her layer PARP maintenance onto the IL-12 axis — but whether a PARP arm applies still depends on the pending HRD result. It is kept as a visible not_recommended row so the reader sees what was considered and why the on-study program is the trial's and treating team's conversation rather than a Libby recommendation.
- **rucaparib (ATHENA-MONO, [PMID 35658487](https://pubmed.ncbi.nlm.nih.gov/35658487)).** An HRD-stratified 1L-maintenance PARP in her exact stage III-IV setting (ITT PFS HR 0.52), but it duplicates the PARP synthetic-lethal mechanism already represented by niraparib and the olaparib options, and its anemia (28.7%) and transaminitis engage the same myelosuppression veto. Kept in the dossier as a class comparator; not separately ranked.
- **olaparib + cediranib (NRG-GY004, [PMID 35290101](https://pubmed.ncbi.nlm.nih.gov/35290101)).** Pairs the PARP and anti-angiogenic axes she carries, but in the recurrent platinum-sensitive line rather than her 1L-maintenance setting, and the oral doublet did not beat chemotherapy on PFS overall (HR 0.86, p=0.077). It anchors a later-line option if and when she recurs, not the current decision.

## Ranked prioritization

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Intervention</th><th>Likelihood of effect</th><th>Toxicity burden</th><th>Counter-productive MoA</th><th>Overall</th></tr></thead>
      <tbody>
        <tr>
          <td>1</td>
          <td><strong>Tumor HRD genomic-instability score + somatic BRCA1/2 (workup)</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Diagnostic certainty. Resolves HRD / somatic-BRCA status and decides whether the HRD-positive PARP options (ranks 4-5) are reachable.</td>
          <td>Low (none — diagnostic NGS on archival FFPE)</td>
          <td><strong>N/A</strong> <span class="cpm-desc">(diagnostic, not therapeutic)</span></td>
          <td><strong>Non-toxic archival-tissue assay that gates the HRD-positive PARP options; order it before committing the maintenance strategy.</strong></td>
        </tr>
        <tr>
          <td>2</td>
          <td><strong>niraparib (1L maintenance)</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span></small></td>
          <td>Moderate across all-comers (PRIMA ITT PFS HR 0.62); high in the HRD-positive subset (HR 0.43). Does not wait on the pending score.</td>
          <td>High (anemia 31%, thrombocytopenia 28.7%, neutropenia 12.8%; cumulative G3+ thrombocytopenia 39.7% at 3.5 yr)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(Cytopenia-driven dose interruptions can erode maintenance dose intensity; the myelosuppression that engages her veto is itself the limiter)</span></td>
          <td><strong>The PARP option that does not wait on the HRD score; all-comers benefit is real but the cytopenia profile sits on her myelosuppression veto and requires the individualized starting dose.</strong></td>
        </tr>
        <tr>
          <td>3</td>
          <td><strong>bevacizumab (concurrent + maintenance)</strong><br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-risktaker">risktaker</span></small></td>
          <td>Moderate for PFS (GOG-218 HR 0.717; ICON7 HR 0.81); OS gain confined to the high-risk subgroup she matched pre-resection. No ITT OS benefit.</td>
          <td>Low (hypertension ~22.9% G2+; bleeding/thrombotic events on a VTE-risk patient; no marrow or neuropathic signal)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(Anti-angiogenic wound-healing impairment and the bleeding/VTE vector matter given her IVC-filter history, but the axis is already part of her tolerated regimen)</span></td>
          <td><strong>Lowest-regret guideline-aligned interim that clears both vetoes and holds the VEGF axis steady; modest PFS-only magnitude with no ITT OS gain.</strong></td>
        </tr>
        <tr>
          <td>4</td>
          <td><strong>olaparib + bevacizumab (1L maintenance)</strong> <span class="scenario-conditional">(conditional on HRD-positive)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>High in the HRD-positive subset (PAOLA-1 HR 0.33; 5-yr OS 66% vs 48%); the largest effect on the board. Foreclosed if HRD-negative.</td>
          <td>Moderate (hypertension 19%, anemia 17% vs &lt;1% on bev alone, lymphopenia 7%; compounded bleeding/VTE on a prior-IVC-filter patient)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(Anti-angiogenic plus PARP stack raises the bleeding/VTE vector that her IVC-filter history already flags; the conservative dissent rested on this mechanism)</span></td>
          <td><strong>The largest-magnitude option when HRD reads positive — but only with a documented bleeding/VTE and CBC monitoring plan, because it stacks PARP onto ongoing anti-VEGF therapy in a high-VTE patient.</strong></td>
        </tr>
        <tr>
          <td>5</td>
          <td><strong>olaparib monotherapy (1L maintenance)</strong> <span class="scenario-conditional">(conditional on somatic BRCA1/2 mutation)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small></td>
          <td>High if somatic-BRCA-mutated (SOLO1 PFS HR 0.30, mPFS 56 vs 13.8 mo; 7-yr OS HR 0.55). Foreclosed if the somatic call is wild-type.</td>
          <td>Moderate (anemia 22%, neutropenia 8%, AE discontinuation 11.5%; long-term AML 1.2%)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(Cumulative myelosuppression and the long-term myeloid (AML) risk press on her marrow veto across a multi-year maintenance window)</span></td>
          <td><strong>Highest-quality evidence and the only mature OS readout, but the strictest gate — reachable only if tumor NGS returns a somatic BRCA1/2 mutation.</strong></td>
        </tr>
        <tr>
          <td>6</td>
          <td><strong>letrozole (endocrine maintenance)</strong><br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-risktaker">risktaker</span></small></td>
          <td>Low-to-moderate (60% vs 38.5% recurrence-free at 24 mo, single non-randomized cohort, pmid:29157627); PR-negativity tempers it further.</td>
          <td>Low (class effects: hot flushes, arthralgia, fatigue; no marrow or neuropathic toxicity)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(Cytostatic / antiangiogenic rather than cytotoxic; magnitude tempered by PR-negativity, so the holding effect may be shallow)</span></td>
          <td><strong>The one option that clears every preference axis, but on tier-4 evidence in a PR-negative tumor — a low-toxicity holding strategy, not a frontline backbone.</strong></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

!!! note "Reading the columns"
    **Toxicity burden** is patient-level G3+ AE severity (Low / Moderate / High) summarized from the trial publications. **Counter-productive MoA** is the mechanism-level risk that the intervention's own pathway could blunt the therapeutic goal — distinct from patient AEs. The board's endorse / dissent / veto state appears as pills under each intervention; full per-persona rationale lives on the [board page](board.md). The GEN-1 / IMNN-001 program was considered and rated `not_recommended` (critic veto on evidence quality); it is documented in "Classes examined but not ranked" rather than in this table.

## Caveats

- **Evidence-base caveats.** The HRD-conditional ranks rest on pre-specified subgroup analyses, not ITT confirmatory results: the PAOLA-1 5-year OS gain (66% vs 48%) is from the HRD-positive subgroup, and the ITT OS was not significant. The bevacizumab trials are PFS-only with no ITT OS benefit, and ICON7 is open-label (RoB2:Some). Letrozole rests on a single non-randomized cohort (ROBINS-I:Serious, n=80). GEN-1 efficacy is conference-topline only, with no peer-reviewed primary paper and a BRCAm/HRD subgroup CI (0.11-1.70) that crosses 1.
- **Compartment / biomarker dependencies.** Ranks 4-5 assume an HRD-positive result — a genomic-instability score ≥42, LOH-high, or a somatic BRCA1/2 mutation. Without it, olaparib + bevacizumab loses its category-1 footing and single-agent olaparib has no eligibility. Niraparib and bevacizumab do not depend on the score.
- **Negative-result mapping.** If the HRD score is negative and somatic BRCA is wild-type, the two `hrd_status:positive` rows are foreclosed; the within-scope options narrow to niraparib (all-comers PARP), bevacizumab (VEGF axis), and letrozole (ER axis). This case does not empty out on a negative result, because three of the ranked options target features other than HRD-positivity.
- **What would change the ranking.**
    - An HRD-positive score would move olaparib + bevacizumab to the front-runner position for a curative-intent window (the HRD-positive HR 0.33 is the largest effect on the board), conditional on a documented bleeding/VTE and CBC monitoring plan.
    - A somatic BRCA1/2 mutation would activate single-agent olaparib with the dossier's only mature OS readout.
    - A documented bleeding/VTE and CBC monitoring plan is the condition that lifts the conservative's veto on olaparib + bevacizumab; without it, that veto stands.
    - A peer-reviewed OVATION-2 primary publication with a structured safety table would change the GEN-1 evidence read, though guideline fit would still keep it in her on-study context.
- **Re-scoping caveat.** If her tolerance for cytopenia risk falls (or the myelosuppression veto hardens), niraparib and the PARP options drop relative to bevacizumab and letrozole; if a later recurrence shifts her to a 2L+ setting, the olaparib + cediranib doublet and the endocrine options re-enter as line-appropriate choices.

## Sources

**PubMed (PMID):**

- [15829966](https://pubmed.ncbi.nlm.nih.gov/15829966) — Bryant et al., PARP synthetic lethality, *Nature* 2005
- [21097693](https://pubmed.ncbi.nlm.nih.gov/21097693) — Kortmann et al., BRCA2-mutant ovarian PDX, *Clin Cancer Res* 2011
- [22204724](https://pubmed.ncbi.nlm.nih.gov/22204724) — Burger et al., GOG-218, *NEJM* 2011
- [22204725](https://pubmed.ncbi.nlm.nih.gov/22204725) — Perren et al., ICON7, *NEJM* 2011
- [24410765](https://pubmed.ncbi.nlm.nih.gov/24410765) — Hirakawa et al., letrozole in ERalpha+ ovarian model, *J Ovarian Res* 2014
- [29157627](https://pubmed.ncbi.nlm.nih.gov/29157627) — Heinzelmann-Schwarz et al., letrozole maintenance cohort, *Gynecol Oncol* 2018
- [30345884](https://pubmed.ncbi.nlm.nih.gov/30345884) — Moore et al., SOLO1, *NEJM* 2018
- [30647846](https://pubmed.ncbi.nlm.nih.gov/30647846) — Sun et al., niraparib tumor-penetration PK, *Oncotarget* 2018
- [31562799](https://pubmed.ncbi.nlm.nih.gov/31562799) — González-Martín et al., PRIMA, *NEJM* 2019
- [31851799](https://pubmed.ncbi.nlm.nih.gov/31851799) — Ray-Coquard et al., PAOLA-1, *NEJM* 2019

**ClinicalTrials.gov (NCT):**

- [NCT00262847](https://clinicaltrials.gov/study/NCT00262847) — GOG-218 (bevacizumab)
- [NCT00483782](https://clinicaltrials.gov/study/NCT00483782) — ICON7 (bevacizumab)
- [NCT01844986](https://clinicaltrials.gov/study/NCT01844986) — SOLO1 (olaparib)
- [NCT02477644](https://clinicaltrials.gov/study/NCT02477644) — PAOLA-1 (olaparib + bevacizumab)
- [NCT02655016](https://clinicaltrials.gov/study/NCT02655016) — PRIMA (niraparib)
- [NCT03393884](https://clinicaltrials.gov/study/NCT03393884) — OVATION-2 (GEN-1 / IMNN-001)
- [NCT06915025](https://clinicaltrials.gov/study/NCT06915025) — OVATION-3 (GEN-1 / IMNN-001 ± PARP)

## Transparency artifacts

- [Trial table](trials.md) — all trial rows, all columns
- [Evidence list](evidence.md) — clinical-evidence + preclinical rows considered
- [Master manuscripts table](manuscripts.md) — every paper considered, with n, effect size, variance, and toxicity columns
- [Tumor-board transcript](board.md) — 5 positions, 20 cross-critiques
- [Recommendations table](recommendations.md) — full ranked detail with biomarker-conditional flags
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Authored June 2026 from the patient's scrubbed profile and preferences, the target-validation paths, twelve trial / evidence rows, nine clinical-evidence rows, nine preclinical rows, and the five board positions with their twenty cross-critiques. The HRD / somatic-BRCA assay was supplied as the user-named rank-1 workup and carried through as the `shared` gate. Niraparib and bevacizumab were left at `scenario: null` because neither waits on the HRD score; the olaparib options were tagged `hrd_status:positive` because their eligibility or guideline footing does. The conservative's veto on olaparib + bevacizumab was treated as biomarker-contingent and lifted in the positive branch with a documented monitoring plan; the critic's veto on GEN-1 rests on the published-evidence base, so it stands and the program is kept as a not_recommended row. Humanizer pass applied June 2026.

<!-- libby:downloads:begin -->

## Downloads

### HTML

- [Target validation paths](target_validation.md?v=7d9e937e) — per-feature biomarker-workup table with providers and references, sortable in-browser
- [Recommendations table](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-recommendations.html?v=32e613d3) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide](accessibility.md?v=5053f606) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Access guide (offline)](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-accessibility.html?v=dad5e85a) — same access-guide content packaged as a self-contained HTML that opens offline
- [Master manuscripts table](manuscripts.md?v=1819364a) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Master manuscripts table (offline)](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-manuscripts.html?v=f6ff907f) — same manuscripts inventory packaged as a self-contained HTML that opens offline

### PDF

- [Target validation paths](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-target-validation.pdf?v=0febdbf0) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-recommendations.pdf?v=d8baf3e1) — ranked options + pipeline context + evidence in detail, in a print-friendly PDF
- [Access guide](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-accessibility.pdf?v=9373877b) — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF
- [Master manuscripts table](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-manuscripts.pdf?v=5c44aba1) — every paper considered — n, effect, variance, toxicities, in a print-friendly PDF
- [Patient/caregiver PDF](hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq-plain-language.pdf?v=d4474f6b) — plain-language summary

<!-- libby:downloads:end -->

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
