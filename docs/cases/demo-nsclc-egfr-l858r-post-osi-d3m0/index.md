<meta name="robots" content="noindex">

# `demo-nsclc-egfr-l858r-post-osi-d3m0`

<!-- libby:downloads:begin -->

## Downloads

- [Target validation paths](demo-nsclc-egfr-l858r-post-osi-d3m0-target-validation.pdf?v=26ec21ae) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table](demo-nsclc-egfr-l858r-post-osi-d3m0-recommendations.html?v=f497c9ba) — ranked options + pipeline context — self-contained HTML that opens offline
- [Access guide](accessibility.md?v=a9b23b43) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Master manuscripts table](manuscripts.md?v=ccc49de6) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Patient/caregiver PDF](demo-nsclc-egfr-l858r-post-osi-d3m0-plain-language.pdf?v=473effa2) — plain-language summary

<!-- libby:downloads:end -->

## Research question

A working artist in her 60s has stage IV EGFR L858R lung adenocarcinoma. She got 22 months out of first-line osimertinib (PR), and now she is progressing. The tumor is T790M-negative but MET-amplified at GCN 8.2 by FISH. What should the next line of therapy target, given that she needs her hands, prefers oral therapy, and is open to trials?

## Patient profile (scrubbed)

- **Primary site / histology:** lung adenocarcinoma
- **Stage:** IV
- **Performance status:** ECOG 1
- **Age band:** 60-69
- **Biomarkers:** EGFR L858R (present); EGFR T790M (absent); MET amplification (GCN 8.2 by FISH); PD-L1 TPS 10%
- **Prior therapy:** 1L osimertinib, PR x 22 months — now progressed
- **Targetable features:** EGFR L858R (sensitizing); MET amplification (likely on-target resistance)

## Preferences

- **Efficacy/toxicity weight:** 0.55 (slight efficacy lean)
- **Toxicity vetoes:** severe neuropathy, cardiotoxicity, alopecia
- **Modality constraints:** oral preferred; no inpatient infusion; minimize IV chair time
- **Free text:** *"working artist — manual dexterity in hands matters more than typical"*
- **Trials preferred:** yes

<!-- libby:target-validation:begin -->

## Target validation paths

EGFR L858R, MET amplification (GCN 8.2), and T790M-absent are all confirmed at decision-relevant resolution, so no diagnostic test gates the savolitinib + osimertinib trial enrollment (SAFFRON / SACHI). The validation work here is about resistance characterization at progression, not target confirmation. The goal is to make sure the case really is MET-amplified bypass resistance and not something more complicated wearing the same imaging signature.

### EGFR L858R

The most consequential miss right now would be SCLC histologic transformation, which is the highest-PPV resistance pattern that no liquid biopsy can confirm. Tumor NGS including TP53 and RB1 status is the screen: co-loss is the strongest predictor of transformation, with reported rates of 3–14% across post-osimertinib cohorts. If imaging morphology shifts or co-loss is detected, fresh re-biopsy with a neuroendocrine IHC panel (chromogranin, synaptophysin, INSM1, Ki-67) is the only way to confirm. ctDNA covering EGFR C797S and exon-20 inserts is the parallel on-target resistance check; a positive C797S result reframes the next-line conversation toward fourth-generation EGFR-TKIs or combination strategies.

### MET amplification

The FISH GCN 8.2 result clears SAFFRON's enrollment threshold (≥ 6) cleanly, but MET amplification can be focal, and primary-vs-metastatic discordance is a documented confounder in this setting. A second-site FISH (or a matched archival block) refines confidence that the dominant disease, not just the biopsied site, is the amplified one. MET IHC (clone SP44) is the orthogonal-modality complement to the SAFFRON eligibility profile. A comprehensive NGS panel that picks up HER2 / BRAF / FGFR co-alterations frames durability expectations and the next-line plan.

### Where to order these assays

The preferred provider for each assay is marked **(preferred)**, selected on company size, reputation, US-based location, and turnaround time. Other providers in the row are listed in case the preferred lab is unreachable for this patient.

| Assay | Provider | Decision gated | Contact |
|---|---|---|---|
| **ctDNA panel (EGFR C797S / T790M / exon-20)** | **Guardant Health *(preferred)* (Guardant360 CDx)** | **Distinguishes on-target (C797S, exon-20) vs bypass post-osimertinib resistance; informs fourth-gen TKI vs combination strategy** | **[test info](https://guardanthealth.com/products/guardant360-cdx/) · 505 Penobscot Drive, Redwood City, CA 94063 · 1-855-698-8887** |
| ctDNA panel | Foundation Medicine *(FoundationOne Liquid CDx)* | Distinguishes on-target vs bypass post-osimertinib resistance | [test info](https://www.foundationmedicine.com/test/foundationone-liquid-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| ctDNA panel | Tempus *(xF+)* | Distinguishes on-target vs bypass post-osimertinib resistance | [test info](https://www.tempus.com/oncology/diagnostics/) · 600 West Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| ctDNA panel | Caris Life Sciences *(Caris Assure)* | Distinguishes on-target vs bypass post-osimertinib resistance | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| ctDNA panel | NeoGenomics Laboratories *(NeoLAB Liquid)* | Distinguishes on-target vs bypass post-osimertinib resistance | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| **Tumor NGS for TP53 / RB1 + bypass alterations** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Predicts SCLC histologic transformation; informs whether next-line stays adenocarcinoma-targeted or pivots to chemo** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| Tumor NGS | Caris Life Sciences *(Molecular Intelligence)* | Predicts SCLC histologic transformation | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| Tumor NGS | Tempus *(xT)* | Predicts SCLC histologic transformation | [test info](https://www.tempus.com/oncology/diagnostics/) · 600 West Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| Tumor NGS | NeoGenomics Laboratories *(NeoTYPE Comprehensive)* | Predicts SCLC histologic transformation | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| Tumor NGS | Memorial Sloan Kettering *(MSK-IMPACT)* | Predicts SCLC histologic transformation | [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |
| **Re-biopsy + neuroendocrine IHC panel** | **Mayo Clinic Laboratories *(preferred)*** | **Confirms SCLC transformation when imaging shifts or TP53/RB1 co-loss is detected; pivots therapy entirely** | **[test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710** |
| Re-biopsy + neuroendocrine IHC | ARUP Laboratories | Confirms SCLC transformation when imaging shifts or TP53/RB1 co-loss is detected | [test info](https://www.aruplab.com/) · 500 Chipeta Way, Salt Lake City, UT 84108 · 1-800-242-2787 |
| Re-biopsy + neuroendocrine IHC | LabCorp / Esoterix Oncology | Confirms SCLC transformation when imaging shifts or TP53/RB1 co-loss is detected | [test info](https://www.labcorp.com/oncology) · 358 South Main Street, Burlington, NC 27215 · 1-800-345-4363 |
| Re-biopsy + neuroendocrine IHC | Quest Diagnostics | Confirms SCLC transformation when imaging shifts or TP53/RB1 co-loss is detected | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| Re-biopsy + neuroendocrine IHC | Memorial Sloan Kettering Diagnostic Molecular Pathology | Confirms SCLC transformation when imaging shifts or TP53/RB1 co-loss is detected | [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |
| **MET FISH (gene/CEP7 ratio)** | **NeoGenomics Laboratories *(preferred)*** | **Refines confidence in MET amp gating result for SAFFRON enrollment; does not gate eligibility** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| MET FISH | Foundation Medicine | Refines MET amp gating result; does not gate eligibility | [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| MET FISH | Mayo Clinic Laboratories | Refines MET amp gating result; does not gate eligibility | [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 |
| MET FISH | LabCorp / Esoterix Oncology | Refines MET amp gating result; does not gate eligibility | [test info](https://www.labcorp.com/oncology) · 358 South Main Street, Burlington, NC 27215 · 1-800-345-4363 |
| MET FISH | Quest Diagnostics | Refines MET amp gating result; does not gate eligibility | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| **MET IHC (clone SP44)** | **Mayo Clinic Laboratories *(preferred)*** | **Confirms MET protein-level expression; orthogonal complement to FISH but does not change SAFFRON eligibility** | **[test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710** |
| MET IHC | ARUP Laboratories | Confirms MET protein-level expression | [test info](https://www.aruplab.com/) · 500 Chipeta Way, Salt Lake City, UT 84108 · 1-800-242-2787 |
| MET IHC | NeoGenomics Laboratories | Confirms MET protein-level expression | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| MET IHC | LabCorp / Esoterix Oncology | Confirms MET protein-level expression | [test info](https://www.labcorp.com/oncology) · 358 South Main Street, Burlington, NC 27215 · 1-800-345-4363 |
| MET IHC | Quest Diagnostics | Confirms MET protein-level expression | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| **Comprehensive bypass NGS (HER2 / BRAF / KRAS / FGFR)** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Frames durability expectations and the next-line plan for MET-directed therapy; does not gate SAFFRON** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| Comprehensive bypass NGS | Caris Life Sciences *(Molecular Intelligence)* | Frames durability and next-line plan for MET-directed therapy | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 1-888-979-8669 |
| Comprehensive bypass NGS | Tempus *(xT)* | Frames durability and next-line plan for MET-directed therapy | [test info](https://www.tempus.com/oncology/diagnostics/) · 600 West Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| Comprehensive bypass NGS | NeoGenomics Laboratories *(NeoTYPE Comprehensive)* | Frames durability and next-line plan for MET-directed therapy | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| Comprehensive bypass NGS | Memorial Sloan Kettering *(MSK-IMPACT)* | Frames durability and next-line plan for MET-directed therapy | [test info](https://www.mskcc.org/clinical-services/diagnostic-laboratory) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |

### Biomarker plan

| Recommended assay | Rationale | Suggested assay provider | Tissue requirements |
|---|---|---|---|
| ctDNA panel including EGFR C797S, T790M, and exon 20 insertions | After osimertinib progression, the resistance landscape divides cleanly between on-target EGFR mutations (C797S, exon-20 inserts, less commonly T790M) and bypass mechanisms. Detecting C797S in cis vs trans changes whether a fourth-generation EGFR-TKI or a combination strategy is the rational next move. Skipping ctDNA at progression risks treating the case as bypass-resistance-only when the biology is mixed. | Guardant Health *(Guardant360 CDx)* · [test info](https://guardanthealth.com/products/guardant360-cdx/) · 505 Penobscot Drive, Redwood City, CA 94063 · 1-855-698-8887 | 10–20 mL whole blood; archival tissue not required |
| Tumor NGS including TP53 and RB1 status | TP53 + RB1 co-loss is the strongest predictor of small-cell histologic transformation as a resistance mechanism in EGFR-mutant NSCLC progressing on osimertinib. The probability of transformation is non-trivial (3–14% across cohorts), and missing it changes the next-line conversation entirely; chemotherapy backbones and platinum-etoposide enter the picture. Pair this with re-biopsy guidance below. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | archival FFPE; if exhausted, ctDNA broad panel |
| Re-biopsy with neuroendocrine IHC panel (chromogranin, synaptophysin, INSM1, Ki-67) if imaging morphology shifts | Histologic small-cell transformation is the most consequential resistance pattern that no liquid biopsy can confirm. When TP53/RB1 are co-lost or imaging shows new visceral / explosive growth atypical for adenocarcinoma, fresh tissue with a neuroendocrine IHC panel is the only way to confirm. Without this, a transformed case can be treated as adenocarcinoma indefinitely. | Mayo Clinic Laboratories · [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 | fresh biopsy of the most-active site |
| MET FISH on a second site (metastatic biopsy or matched archival block) | MET amplification can be focal and discordant between primary and metastatic sites in EGFR-resistant NSCLC. The patient's GCN 8.2 from a single block clears SAFFRON's threshold, but a second-site test rules out the scenario where one biopsy hits a focal amplicon and the dominant disease is unaffected. Without it, a positive trial enrollment can rest on a non-representative result. | NeoGenomics Laboratories · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | second-site archival FFPE if available; not gating |
| MET IHC (clone SP44) for orthogonal expression confirmation | FISH-confirmed MET amplification at GCN 8.2 is the load-bearing finding, and SAFFRON enrollment accepts FISH or IHC 3+. IHC adds an orthogonal modality and surfaces protein-level MET expression; concordance increases confidence that the FISH result reflects active MET signaling. Discordance (FISH-amp without IHC overexpression) is a soft signal worth flagging but does not foreclose the trial. | Mayo Clinic Laboratories · [test info](https://www.mayocliniclabs.com/test-catalog) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 | archival FFPE; same block as prior testing |
| Comprehensive NGS for HER2 amp, BRAF, KRAS, FGFR1-3, and bypass-pathway alterations | Bypass amplifications co-occur with MET amp in roughly 10–20% of post-osimertinib cases and modify expected response to MET-directed therapy. Detecting co-bypass alterations doesn't foreclose savolitinib + osimertinib but reframes the durability expectation and informs subsequent-line planning. Pair this with the TP53 / RB1 panel if running comprehensive NGS; same blood draw / block. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | archival FFPE; ctDNA as backup |
---

*Decision support, not medical advice. Confirm assay availability and current standards with the treating team and the local pathology service.*

<!-- libby:target-validation:end -->

## Scope summary

The dossier behind this page contains 4 trials, 5 clinical-evidence rows, and 4 preclinical rows. Three interventions get ranked. There is no scenario branching because every biomarker on this patient is `confirmed`. Board agreement scores run from +0.8 at rank 1 down to -0.4 at rank 2, where there is an active veto, so the gap between the top two picks is wide and does real work in the ranking.

## Cross-cutting caveat (read first)

MET amplification at GCN 8.2 with T790M absent points cleanly at MET-directed combination therapy. The patient's modality and toxicity preferences then close off the most-cited alternative. That is the story behind every rank below.

- T790M-negative status takes second-generation osimertinib re-challenge off the table as a sequencing move. The resistance is not gatekeeper-mutation-driven.
- MET amplification accounts for roughly 15–30% of post-osimertinib resistance at this GCN range. Savolitinib + osimertinib is the mechanism-matched combination with replicated evidence in this exact subset.
- The patient's manual-dexterity-driven veto on **severe neuropathy** plus **minimize IV chair time** rules out amivantamab + lazertinib at rank 1 even though the regimen carries NCCN cat-2A status. The conservative's toxicity veto on this rec is the load-bearing dissent.
- The **alopecia veto** alone forecloses patritumab deruxtecan independent of efficacy. The dossier keeps it on the page for transparency, not as a live option.

## Intervention grouping

Three buckets, sorted by how cleanly each one matches the resistance biology.

- MET-targeted EGFR-TKI combinations (mechanism-matched, all-oral): savolitinib + osimertinib via the SAFFRON / SACHI phase-3 program. The mechanistic anchor is the TATTON expansion ([PMID 32679432](https://pubmed.ncbi.nlm.nih.gov/32679432)).
- EGFR + MET bispecific paired with a 3G TKI (broader-spectrum, IV-anchored): amivantamab + lazertinib via CHRYSALIS-2 ([PMID 36720074](https://pubmed.ncbi.nlm.nih.gov/36720074)).
- HER3-directed antibody-drug conjugate (mechanism-agnostic post-TKI option): patritumab deruxtecan via HERTHENA-Lung01 ([PMID 37563559](https://pubmed.ncbi.nlm.nih.gov/37563559)).

## Top interventions

### Rank 1. Savolitinib + osimertinib (preferably on SAFFRON / SACHI)

*Mechanism-matched, all-oral, clears every preference axis. Four of five personas endorsed. Concensusite's qualified guideline-fit concern resolves on trial enrollment.*

#### Evidence base

The mechanistic and clinical anchor is the TATTON expansion ([PMID 32679432](https://pubmed.ncbi.nlm.nih.gov/32679432); n=69; ORR 30%, 95% CI 19–42 in the EGFR-mut + MET-amp post-EGFR-TKI subset). The phase-3 confirmatory study ([NCT05261399](https://clinicaltrials.gov/study/NCT05261399); SAFFRON; n=324; savo + osi vs platinum + pemetrexed; PFS endpoint) is recruiting and reads out into the same biomarker-defined population. The patient's MET-amp GCN 8.2 by FISH clears the GCN ≥6 / IHC 3+ enrollment threshold without needing a borderline call.

#### Likelihood of desired effect

Mechanism concordance is high. MET amplification IS the on-target resistance mechanism this combination targets, and the patient's biomarker fits the studied stratum exactly. The TATTON ORR (~30%) is real, replicated within the program, and pre-specified to this subset. The phase-3 readout will quantify durability and PFS gain over chemotherapy.

#### Toxicity profile

- LFT elevation, manageable with dose reduction
- Peripheral edema
- Fatigue
- All-oral, with no inpatient component
- No severe-neuropathy signal in either TATTON or the broader SAFFRON program

User vetoes (severe neuropathy, cardiotoxicity, alopecia) all clear. Modality constraints (oral, no inpatient, minimize IV) all clear.

#### Counter-productive mechanisms / dissent

Endorsed by risktaker, conservative, critic, and advocate. Concensusite raised a *qualified guideline-fit* concern: the combination is not currently NCCN-listed as a recommended regimen, so off-trial use is off-label. The resolution is trial enrollment, which the patient already prefers. No persona dissented or vetoed.

#### Practical considerations

- All-oral: savolitinib 300 mg PO BID + osimertinib 80 mg PO daily
- Trial enrollment is the guideline-aligned route
- Off-trial use is off-label, so flag it with the treating team
- LFT monitoring at baseline plus every 2–4 weeks early in therapy

#### Why this rank

Strong combined evidence-and-preference fit. Every preference axis clears, the mechanism matches the biomarker, and the agreement_score (+0.8) is the highest in the dossier. The rank-1/rank-2 gap is +1.2 (vs amivantamab + lazertinib at -0.4), driven both by the active veto on rank 2 and by the better preference fit here.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Savolitinib + osimertinib — TATTON expansion (single-arm phase 1b, n=69 EGFR-mut + MET-amp post-TKI) | ORR 30% (95% CI 19–42) | LFT elevation, peripheral edema, fatigue (all manageable) | [PMID 32679432](https://pubmed.ncbi.nlm.nih.gov/32679432) |
| Savolitinib + osimertinib — SAFFRON (phase 3 RCT, recruiting, n=324) | PFS endpoint; outcome pending | Per TATTON safety profile + comparator chemo arm | [NCT05261399](https://clinicaltrials.gov/study/NCT05261399) |

---

### Rank 2. Amivantamab + lazertinib

*Real efficacy signal, NCCN cat-2A, but **conservative vetoed on neuropathy + IV-burden grounds**. Considered with caveats; override not recommended absent rank-1 failure.*

#### Evidence base

CHRYSALIS-2 ([PMID 36720074](https://pubmed.ncbi.nlm.nih.gov/36720074); single-arm phase 1/2; n=162; post-osimertinib EGFR-mutant biomarker subset including MET-amp): ORR 36% (95% CI 28–45). NCCN NSCLC v3.2025 category 2A. ESMO MCBS B.

#### Likelihood of desired effect

Effect size is real and slightly larger than rank 1's ORR. Biomarker fit is acceptable (EGFR L858R + MET-amp permitted), but the trial is not enriched specifically for MET-amplified post-osimertinib progressors at this GCN range, so the subset estimate is less granular than TATTON's.

#### Toxicity profile

- **Severe neuropathy** in combination data, which triggers the user veto
- IRR grade 3+ ~7%
- Rash
- Inpatient or extended chair-time IV cycle 1, which conflicts with both modality preferences (no inpatient infusion; minimize IV chair time)

For a working artist whose manual dexterity matters more than typical, the neuropathy risk is decision-relevant beyond the categorical veto.

#### Counter-productive mechanisms / dissent

**Conservative issued a toxicity veto on stated severe-neuropathy and IV-burden grounds.** Advocate dissented on preference fit. Critic dissented on evidence-quality grounds (single-arm phase 1/2, no randomized comparator in the post-osimertinib subset). Risktaker endorsed on effect size; concensusite endorsed on NCCN guideline alignment.

The veto is honored, not silently dropped. Per PI synthesis rules this row stays on the page as `considered_with_caveats` so the user sees what was considered. Override of the conservative's veto is **not** recommended absent failure of the rank-1 option.

#### Practical considerations

- Amivantamab 1050 mg IV weekly cycle 1 then q2w + lazertinib 240 mg PO daily
- Subcutaneous amivantamab is in development; AE re-profiling pending
- NCCN-recommended; off-label considerations are weaker than for rank 1

#### Why this rank

Below savolitinib + osimertinib because of the active toxicity veto plus the modality conflict, even though the ORR is slightly larger. Above patritumab deruxtecan because two personas affirmatively endorsed and the alopecia veto on rank 3 is unconditional.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Amivantamab + lazertinib — CHRYSALIS-2 (single-arm phase 1/2, n=162 post-osimertinib) | ORR 36% (95% CI 28–45) | Severe neuropathy (combination); IRR G3+ ~7%; rash | [PMID 36720074](https://pubmed.ncbi.nlm.nih.gov/36720074) |

---

### Rank 3. Patritumab deruxtecan (HER3-DXd)

*Real efficacy, but **the alopecia veto forecloses it.** Surfaced only so the user can re-weight the veto with her oncologist if she chooses.*

#### Evidence base

HERTHENA-Lung01 ([PMID 37563559](https://pubmed.ncbi.nlm.nih.gov/37563559); single-arm phase 2; n=225; EGFR-mutant NSCLC after EGFR-TKI): ORR 29.8% (95% CI 23.9–36.2). Effect size is comparable to ranks 1 and 2.

#### Likelihood of desired effect

The mechanism (HER3-targeted antibody-drug conjugate) is mechanism-agnostic relative to the patient's MET-amp resistance. It targets HER3 expression rather than the resistance pathway. The effect is real, but the mechanism fit is weaker than at rank 1.

#### Toxicity profile

- ILD grade 3+ ~5%
- **Alopecia**, which triggers the user veto
- Thrombocytopenia
- IV q3w

#### Counter-productive mechanisms / dissent

Only the risktaker advanced this rec. Advocate did not advance it because the alopecia veto was already on the table. No formal veto was issued because the dossier surfaced the rec only after ranks 1 and 2 were established.

#### Practical considerations

- 5.6 mg/kg IV q3w
- Not currently NCCN-endorsed as standard for this setting
- ILD risk requires baseline pulmonary function plus ongoing monitoring

#### Why this rank

Below ranks 1 and 2 because the alopecia veto is unconditional. The rec is on the page for transparency: the user can ask her oncologist whether re-weighting the alopecia veto changes the calculus. That is a conversation, not a recommendation.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Patritumab deruxtecan — HERTHENA-Lung01 (single-arm phase 2, n=225 post-EGFR-TKI) | ORR 29.8% (95% CI 23.9–36.2) | ILD G3+ ~5%; alopecia; thrombocytopenia | [PMID 37563559](https://pubmed.ncbi.nlm.nih.gov/37563559) |

## Classes examined but not ranked

- Osimertinib re-challenge or dose escalation: T790M is absent, so the gatekeeper-mutation pathway is not the resistance mechanism, and re-challenge has no biomarker rationale.
- MET-targeted monotherapy (capmatinib, tepotinib): the mechanism overlaps with the rank-1 savolitinib + osimertinib combo, but the approved indications cover METex14 rather than amplification, so the biomarker subset does not match.

## Ranked prioritization

| Rank | Status | Intervention | Endorsed by | Dissent | Veto | Likelihood | Toxicity burden | Why this rank |
|---|---|---|---|---|---|---|---|---|
| 1 | recommended | Savolitinib + osimertinib (preferably on SAFFRON / SACHI) | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-advocate">advocate</span> | — | — | High mechanism fit; ORR ~30% replicated | LFT, edema, fatigue | Mechanism + preferences both clean |
| 2 | considered_with_caveats | Amivantamab + lazertinib | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-concensusite">concensusite</span> | <span class="persona persona-critic">critic</span> <span class="persona persona-advocate">advocate</span> | <span class="persona persona-conservative">conservative</span> | ORR 36% in subset | Severe neuropathy, IV burden | Active veto + modality conflict |
| 3 | considered_with_caveats | Patritumab deruxtecan (HER3-DXd) | <span class="persona persona-risktaker">risktaker</span> | — | — | ORR 29.8% post-TKI | ILD ~5%; alopecia | Triggers alopecia veto outright |

## Caveats

- The evidence base is modest in size. Rank 1's anchor is a 69-patient TATTON expansion plus a recruiting phase 3. Rank 2's anchor is a 162-patient single-arm. Rank 3's anchor is a 225-patient single-arm. None has a randomized comparator in this patient's exact biomarker stratum yet.
- No OS data exist for any of the three ranked interventions in the post-osimertinib MET-amp setting specifically. Effect estimates are ORR-based, and durability is the open question for all three.
- Two of the three rec-ranks turn on user vetoes (neuropathy, alopecia) tied to the working-artist context. The board treated those as load-bearing, not disposable.
- What would change the ranking:
    - A SAFFRON OS readout that confirms a meaningful PFS / OS benefit would tighten rank 1's confidence and could push it from "preferred" to "guideline-fit."
    - A MET-amp-stratified amivantamab + lazertinib randomized readout that mitigates neuropathy (for example with the SC formulation) could narrow the rank-1 / rank-2 gap, but the modality preference would still anchor rank 1 above it.
    - If the user re-weighted the alopecia veto, patritumab deruxtecan would move from rank 3 (`considered_with_caveats`) to rank 2.
    - Failure of the rank-1 option (intolerance, progression, slot unavailability) is the explicit precondition for revisiting rank 2 with the conservative's veto on the table.
- Re-scoping caveat. If the patient's clinical state changes (CNS progression, declining ECOG) or if the modality preference relaxes, the ranking shifts. The current page assumes the stated profile and preferences hold.

## Sources

**PubMed (PMID):**

- [32679432](https://pubmed.ncbi.nlm.nih.gov/32679432) — Sequist et al., TATTON expansion, *Lancet Oncol* 2020
- [36720074](https://pubmed.ncbi.nlm.nih.gov/36720074) — Cho et al., CHRYSALIS-2, *JCO* 2023
- [37563559](https://pubmed.ncbi.nlm.nih.gov/37563559) — Yu et al., HERTHENA-Lung01, *JCO* 2023

**ClinicalTrials.gov (NCT):**

- [NCT05261399](https://clinicaltrials.gov/study/NCT05261399) — SAFFRON (savolitinib + osimertinib phase 3)
- [NCT04077463](https://clinicaltrials.gov/study/NCT04077463) — CHRYSALIS-2 (amivantamab + lazertinib)
- [NCT04619004](https://clinicaltrials.gov/study/NCT04619004) — HERTHENA-Lung01 (patritumab deruxtecan)
- [NCT02143466](https://clinicaltrials.gov/study/NCT02143466) — TATTON

## Transparency artifacts

- [Trial table](trials.md) — 4 trials in the dossier
- [Evidence list](evidence.md) — 5 clinical-evidence rows + 4 preclinical rows
- [Tumor-board transcript](board.md) — 5 positions, 20 cross-critiques
- [Recommendations table](recommendations.md) — full ranked detail
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

This is a demo case authored in May 2026 with synthetic data so the pipeline can be smoke-tested. No real patient is represented. The page was re-rendered into the shieldbreak-flavored layout the same month after Libby's PI authoring contract was updated to mirror `pirl-unc/io-shieldbreak`, then re-run with the humanizer pass once that was added to the contract.

!!! danger disclaimer "Decision support, not medical advice"
    Libby is experimental. The recommendations on this page have **not** been
    reviewed by a clinician treating this patient. Do not act on this page
    without consulting a qualified oncologist. This is a synthetic
    demonstration case; the patient profile is fictional.
