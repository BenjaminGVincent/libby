<meta name="robots" content="noindex">

# pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m

<!-- libby:case-output:begin -->

## Case output

- [Target validation paths (PDF)](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-target-validation.pdf?v=242e0eec) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Selected general biomarker report (HTML)](biomarker_survey.md?v=dab629ef) — which panel biomarkers this patient has and has not been tested for, including the tumor-agnostic ones, sortable in-browser
- [Recommendations table (HTML)](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-recommendations.html?v=adf25bf5) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Standard of care options (HTML)](standard_of_care.md?v=b014102d) — approved and guideline-endorsed strategies for this patient's situation, assessed for eligibility and for how they sequence against the targeted options, sortable in-browser
- [Preclinical recommendations (HTML)](preclinical_recommendations.md?v=7cf67438) — forward-looking horizon scan of earlier-than-clinical candidate drugs, compounds, and strategies, sortable in-browser
- [Access guide (HTML)](accessibility.md?v=bcbb9719) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, sortable in-browser
- [Access guide (offline HTML)](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-accessibility.html?v=8cfd5f67) — same access-guide content as the in-browser page, packaged as a self-contained HTML that opens offline
- [Master manuscripts table (HTML)](manuscripts.md?v=2300450f) — every paper considered — n, effect, variance, toxicities, sortable in-browser
- [Master manuscripts table (offline HTML)](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-manuscripts.html?v=d741ad30) — same manuscripts inventory as the in-browser page, packaged as a self-contained HTML that opens offline
- [Patient/caregiver PDF](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-plain-language.pdf?v=48572492) — plain-language summary

<!-- libby:case-output:end -->
## Research question

In pancreatic ductal adenocarcinoma that recurred about four months after adjuvant FOLFIRINOX, with every molecular result carried over from the December 2025 resection and the new mass never biopsied, what interventions could target CLDN18.2 at 2+/3+ in 60% of cells, KRAS G12R, TP53 Y220C, and KMT2C S2816fs, gated on biopsy and staging of that mass?

## Patient profile (scrubbed)

- Age band 50-59, sex unknown, ECOG 0.
- Pancreatic ductal adenocarcinoma. Neoadjuvant mFOLFIRINOX x6 (2025, partial response) → R0 resection December 2025 with 0/34 nodes and CAP tumor regression grade 2 → adjuvant FOLFIRINOX x4 completed per plan March 2026.
- New pancreatic body mass on imaging, July 2026, with likely vascular invasion. Roughly 4 months after finishing adjuvant therapy.
- **The recurrence has not been biopsied or re-sequenced.** Everything below comes from the resection specimen, taken before four more cycles of chemotherapy, from a lesion that is not the one now being treated.
- CLDN18.2 — positive, 2+/3+ membranous staining in 60% of tumor cells on the resected primary. Clone and assay not named in the supplied report. **CLDN18.2 on the recurrent lesion: not assessed (IHC pending).**
- KRAS p.G12R — confirmed, tumor NGS on the resection specimen.
- TP53 p.Y220C — confirmed, same specimen.
- KMT2C p.S2816fs — confirmed, same specimen.
- MSI — negative (MSS), confirmed. TMB — 0.83 mut/Mb, low, confirmed.
- **Germline: no dedicated panel has been run.** "No incidental findings" came off the tumor NGS report, not a germline test (NGS pending).
- **Somatic profile of the recurrent lesion: not assessed (NGS pending).**
- Organ function: no labs supplied at intake. Post-resection hepatobiliary and pancreatic function, residual oxaliplatin neuropathy grade after 10 total FOLFIRINOX cycles, and baseline renal, hepatic, and marrow panels are all undocumented.

## Preferences

- Efficacy/toxicity weight: **0.7**, flagged in the preferences file itself as an assumed default rather than a number the user stated.
- Toxicity vetoes: none stated.
- Modality constraints: none stated.
- Free text: trials are welcome including ones that require travel; no geographic limit was given (`geography_band` is null on purpose). Revisit the 0.7 weight once goals of care and organ function are documented. The ungraded residual oxaliplatin neuropathy could change the calculus for neurotoxic regimens.
- Trial preference: **prefers trials — yes.**

<!-- libby:target-validation:begin -->

# Target validation paths

Everything known about this tumor comes from a December 2025 resection specimen; the mass that appeared in July 2026 has never been sampled, and ten cycles of FOLFIRINOX sit between the two. So the workup here starts one step earlier than usual: before any target can be validated, the tumor itself has to be. One EUS-guided core pass supplies the histology, the CLDN18.2 re-stain, the DNA and RNA sequencing, and most tissue-gated trial screens, and the restaging read that travels with it decides access on its own: the daraxonrasib expanded-access protocol (NCT07573215) and the RASolute 303 trial (NCT07491445) both require confirmed metastatic disease, and RASolute 303 additionally requires consent within 6 weeks of that diagnosis. Two essential items need no tissue at all and should go out this week: the dedicated germline panel and a graded neuropathy examination. If the biopsy does not confirm recurrent pancreatic adenocarcinoma carrying these features, this report has no within-scope recommendations, and the next conversation about standard care is the treating team's, not Libby's.

### The recurrence itself

The biopsy is the load-bearing order. Request at least three cores so one goes to a paraffin block for IHC and the rest to molecular; the likely vascular invasion is a route question rather than a barrier, since EUS from the stomach or duodenum usually avoids the vessels a percutaneous approach cannot. If the interventional team judges the lesion unsafe to sample, plasma ctDNA is the fallback and should be ordered in parallel rather than after. Three companions are essential and independent of tissue: a graded neurologic examination for peripheral sensory neuropathy (CTCAE v5 with the EORTC QLQ-CIPN20), because ten cycles of FOLFIRINOX is a large cumulative oxaliplatin exposure, no grade appears anywhere in the record, and most protocols exclude at grade 2 or higher; baseline CBC, comprehensive metabolic panel with bilirubin and albumin, creatinine with eGFR, coagulation studies, and a CA 19-9 that will only mean something later if drawn now; and pancreas-protocol cross-sectional imaging defining vascular involvement, biopsy route, local-only versus metastatic extent, and a RECIST-measurable target lesion. A fitness screen (fecal elastase-1, fat-soluble vitamins, HbA1c, biliary anatomy and stent status) rounds this out: enzyme replacement is cheap, and the weight loss it prevents is what later costs patients trial eligibility.

### CLDN18.2

The 60% 2+/3+ result on file was produced by an assay the report does not name, on tissue from a lesion that is not the one being treated. Re-staining with the VENTANA CLDN18 (43-14A) RxDx assay puts the number on the scale every threshold conversation uses, including the sponsor assays for ASP2138 (NCT05365581) and the satri-cel program (CT041, NCT04404595). Just as essential: stain the recurrence biopsy and the December 2025 resection block side by side in one laboratory, because CLDN18.2 expression is discordant between primary and metastatic lesions in a substantial minority of gastric cases (PMID 40200874), loss under zolbetuximab treatment has been documented (PMID 41854734), and a recurrence-only stain that comes back lower cannot distinguish real antigen loss from inter-laboratory scoring drift. Ask the laboratory to report the intensity distribution at 1+, 2+, and 3+ separately rather than a single positive-or-negative call: the thresholds differ by program (>=75% at 2+/3+ for zolbetuximab in SPOTLIGHT and GLOW, >=40% at >=2+ for satri-cel, which the primary's 60% clears), and 60% sits exactly in the band where that distinction decides which door is open. Request the December 2025 block from the operating hospital early; retrieval is often the slow step.

### KRAS G12R

Comprehensive tumor NGS on recurrent-lesion tissue, DNA plus RNA, is essential. The codon-level call is what separates a pan-RAS(ON) route such as daraxonrasib (RASolute 302, NCT06625320; RASolute 303, NCT07491445) from the G12C- and G12D-selective drugs that cannot work here, and re-sequencing tests whether the driver persisted through ten cycles of FOLFIRINOX. RNA rides along so fusion status ends up established rather than unaddressed. The plasma ctDNA panel reporting KRAS codon 12 and TP53 Y220C with variant allele fractions is the second essential item: it answers in about a week, it is the only route to a current genotype if the biopsy proves unsafe, and several mutant-KRAS vaccine protocols (ELI-002 7P, NCT05726864 and NCT07671339) use ctDNA positivity as an entry criterion, so it can open a door rather than merely inform. A negative plasma result in a low-shedding pancreatic lesion does not overturn tissue findings; that is the main way this assay gets misread. Co-alteration profiling (CDKN2A, SMAD4, ARID1A, MYC, KRAS allelic imbalance) refines what to expect from RAS-pathway inhibition and reads out on the same sequencing at no extra cost.

### TP53 Y220C

PYNNACLE (NCT04585750) asks only that the tumor carry a TP53 Y220C mutation, but the companion rezatapopt protocols spell out what counts: CLIA-certified testing with a variant allele fraction above 2% (NCT06616636), tissue or liquid both acceptable (NCT07372625). The December 2025 tissue result probably satisfies this on its face; what the sponsor will want confirmed is that the variant is still present in current disease, so the cheapest version of this row is a phone call and a PDF before anything new is ordered. Two refinements are worth requesting rather than ordering: a purity-corrected variant allele fraction with TP53 copy number and LOH status on the recurrence NGS, which informs how much a Y220C reactivator can plausibly do, and, only once such a drug is actually started, serial plasma TP53 sequencing, because acquired secondary TP53 alterations arising in cis with Y220C drive on-target resistance in this class (PMID 41504628, with commentary at PMID 41918356) and show up in plasma before imaging turns.

### BRCA and homologous recombination

The "no incidental germline findings" line on file came off a tumor NGS report, which is not built for germline sensitivity, misses large rearrangements, and does not state which genes were covered. The dedicated germline multigene panel (BRCA1, BRCA2, PALB2, ATM, CDKN2A, STK11, and the mismatch-repair genes) is a blood draw NCCN recommends for every pancreatic adenocarcinoma patient, and a pathogenic BRCA1/2 or PALB2 result puts an approved PARP-inhibitor maintenance strategy on the table (POLO, PMID 31157963 and PMID 35834777) while also arguing for keeping platinum in the sequence. It needs no tissue and should not wait on the biopsy. Its high-priority companion is somatic homologous-recombination gene coverage with a genomic-instability score on the recurrence NGS, which catches the somatic-only events a germline panel will miss and costs an order line rather than a new specimen.

### MSS / TMB

Nothing here needs a standalone order. MSS and a TMB of 0.83 mut/Mb against a threshold of 10 are already at decision resolution and keep single-agent checkpoint blockade closed. The only caveat is that neither original assay platform was named, and panel-derived TMB is not interchangeable across platforms; that caveat bites near the cutoff, not an order of magnitude below it. If the recurrence is sequenced anyway, both values re-report free, and MMR IHC can ride on the same block.

### KMT2C S2816fs

To be plain about it: no assay result would make this variant actionable today. No approved or late-phase therapy selects on KMT2C status in any tumor type. What a biallelic, clonal loss-of-function call would buy is entry to an epigenetic-agent basket trial that accepts COMPASS-complex alterations, if one opens to pancreatic patients. It rides on the recurrence NGS as a reporting detail and justifies no separate order.

### Biomarkers measured, but not to decision resolution

Two results on file cannot carry the decisions that lean on them, and each is short in a different way.

- CLDN18.2. What exists is 60% of tumor cells at 2+/3+ on the December 2025 resection. Three things sit between that stain and an eligibility call: the number is below the >=75% line used in SPOTLIGHT and GLOW, the antibody clone and assay were never named so the result cannot be scored against the cutoff that assay defines, and the tissue predates ten cycles of chemotherapy and is not the lesion being treated. The 43-14A re-stain, ideally on recurrent tissue with the archival block run in the same batch, closes all three at once. The target call itself is not in doubt; the resolution of the measurement is.
- Homologous recombination / germline BRCA. What exists is "no incidental findings" from a tumor NGS report. That is not a germline test: it lacks germline sensitivity, misses large rearrangements, and does not say which genes it covered. The dedicated germline panel, plus somatic HR coverage with a genomic-instability score on the next tumor sequencing, closes the gap.

### Where to order these assays

| Assay | Provider | Decision gated | Contact |
|---|---|---|---|
| **Comprehensive tumor NGS on recurrent-lesion tissue, DNA plus RNA, reporting codon-level KRAS genotype, TP53, homologous-recombination genes, fusions, MSI and TMB** | **Caris Life Sciences *(preferred)* (MI Cancer Seek (whole exome plus whole transcriptome))** | **Pan-RAS(ON) trials for daraxonrasib (NCT06625320, NCT07491445) and rezatapopt via PYNNACLE (NCT04585750).** | **[test info](https://www.carislifesciences.com/physicians/physician-services/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 888-979-8669** |
| Comprehensive tumor NGS on recurrent-lesion tissue | Foundation Medicine *(FoundationOne CDx)* | Pan-RAS(ON) trials for daraxonrasib (NCT06625320, NCT07491445) and rezatapopt via PYNNACLE (NCT04585750). | [test info](https://www.foundationmedicine.com/providers/contact) · 400 Summer Street, Boston, MA 02210 · 888-988-3639 |
| Comprehensive tumor NGS on recurrent-lesion tissue | Tempus AI *(Tempus xT (DNA) plus xR (RNA))* | Pan-RAS(ON) trials for daraxonrasib (NCT06625320, NCT07491445) and rezatapopt via PYNNACLE (NCT04585750). | [test info](https://www.tempus.com/order/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 · 800-739-4137 |
| Comprehensive tumor NGS on recurrent-lesion tissue | NeoGenomics Laboratories *(NeoTYPE Comprehensive Tumor Profile)* | Pan-RAS(ON) trials for daraxonrasib (NCT06625320, NCT07491445) and rezatapopt via PYNNACLE (NCT04585750). | [test info](https://www.neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 (Client Services, option 3) |
| **Plasma ctDNA comprehensive panel reporting KRAS codon 12 genotype and TP53 Y220C with variant allele fractions** | **Guardant Health *(preferred)* (Guardant360 CDx)** | **Genotype for daraxonrasib and rezatapopt when tissue is not obtainable; ctDNA-positivity entry criterion for ELI-002 7P protocols.** | **[test info](https://guardanthealth.com/contact/) · 3100 Hanover Street, Palo Alto, CA 94304 · 855-698-8887** |
| Plasma ctDNA comprehensive panel | Foundation Medicine *(FoundationOne Liquid CDx)* | Genotype for daraxonrasib and rezatapopt when tissue is not obtainable; ctDNA-positivity entry criterion for ELI-002 7P protocols. | [test info](https://www.foundationmedicine.com/providers/contact) · 400 Summer Street, Boston, MA 02210 · 888-988-3639 |
| Plasma ctDNA comprehensive panel | Tempus AI *(Tempus xF+ (plasma))* | Genotype for daraxonrasib and rezatapopt when tissue is not obtainable; ctDNA-positivity entry criterion for ELI-002 7P protocols. | [test info](https://www.tempus.com/order/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 · 800-739-4137 |
| Plasma ctDNA comprehensive panel | Caris Life Sciences *(Caris Assure (blood))* | Genotype for daraxonrasib and rezatapopt when tissue is not obtainable; ctDNA-positivity entry criterion for ELI-002 7P protocols. | [test info](https://www.carislifesciences.com/physicians/physician-services/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 888-979-8669 |
| **CLDN18.2 IHC by the VENTANA CLDN18 (43-14A) RxDx assay, reporting percent of viable tumor cells with moderate-to-strong (2+/3+) membranous staining** | **NeoGenomics Laboratories *(preferred)* (Claudin 18 FDA (VYLOY), VENTANA CLDN18 (43-14A) RxDx Assay)** | **Off-label zolbetuximab and every CLDN18.2 trial that scores against the 43-14A assay (ASP2138 NCT05365581, CT041 NCT04404595).** | **[test info](https://www.neogenomics.com/providers/test/APH-CLAP-01AX/claudin-18-fda-vyloy) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 (Client Services, option 3)** |
| CLDN18.2 IHC (43-14A), including the paired recurrence-plus-archival stain and the 1+/2+/3+ tier report | Labcorp Oncology *(Claudin 18 IHC (test 452390))* | Off-label zolbetuximab and every CLDN18.2 trial that scores against the 43-14A assay (ASP2138 NCT05365581, CT041 NCT04404595). | [test info](https://oncology.labcorp.com/tests/452390/claudin-18-ihc) · 358 South Main Street, Burlington, NC 27215 · 800-845-6167 |
| CLDN18.2 IHC (43-14A), including the paired recurrence-plus-archival stain and the 1+/2+/3+ tier report | Mayo Clinic Laboratories *(CLD18: Claudin 18 (CLDN18) (43-14A), semi-quantitative IHC)* | Off-label zolbetuximab and every CLDN18.2 trial that scores against the 43-14A assay (ASP2138 NCT05365581, CT041 NCT04404595). | [test info](https://www.mayocliniclabs.com/test-catalog/overview/620665) · 3050 Superior Drive NW, Rochester, MN 55901 · 800-533-1710 |
| **Dedicated germline multigene panel on blood or saliva covering BRCA1, BRCA2, PALB2, ATM, CDKN2A, STK11 and the mismatch-repair genes** | **Myriad Genetics *(preferred)* (MyRisk Hereditary Cancer with BRACAnalysis CDx)** | **PARP-inhibitor maintenance (olaparib) eligibility, platinum re-challenge weighting, and family testing.** | **[test info](https://myriad.com/contact-us/) · 322 North 2200 West, Salt Lake City, UT 84116 · 800-469-7423** |
| Dedicated germline multigene panel | Ambry Genetics *(CustomNext-Cancer / PancNext)* | PARP-inhibitor maintenance (olaparib) eligibility, platinum re-challenge weighting, and family testing. | [test info](https://www.ambrygen.com/providers/contact-us) · One Enterprise, Aliso Viejo, CA 92656 · 866-262-7943 |
| Dedicated germline multigene panel | GeneDx | PARP-inhibitor maintenance (olaparib) eligibility, platinum re-challenge weighting, and family testing. | [test info](https://www.genedx.com/contact-us/) · 207 Perry Parkway, Gaithersburg, MD 20877 · 888-729-1206 |
| Dedicated germline multigene panel | Labcorp Genetics (formerly Invitae) *(Multi-Cancer Panel)* | PARP-inhibitor maintenance (olaparib) eligibility, platinum re-challenge weighting, and family testing. | [test info](https://www.labcorp.com/genetics) · 1400 16th Street, San Francisco, CA 94103 · 800-436-3037 |
| **TP53 p.Y220C confirmation on a CLIA-certified NGS test (tumor tissue or plasma) reporting the variant at codon level with variant allele fraction** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Rezatapopt via PYNNACLE (NCT04585750).** | **[test info](https://www.foundationmedicine.com/providers/contact) · 400 Summer Street, Boston, MA 02210 · 888-988-3639** |
| TP53 p.Y220C confirmation | Guardant Health *(Guardant360 CDx)* | Rezatapopt via PYNNACLE (NCT04585750). | [test info](https://guardanthealth.com/contact/) · 3100 Hanover Street, Palo Alto, CA 94304 · 855-698-8887 |
| TP53 p.Y220C confirmation | Tempus AI *(Tempus xT (DNA) plus xR (RNA))* | Rezatapopt via PYNNACLE (NCT04585750). | [test info](https://www.tempus.com/order/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 · 800-739-4137 |
| TP53 p.Y220C confirmation | Caris Life Sciences *(MI Cancer Seek (whole exome plus whole transcriptome))* | Rezatapopt via PYNNACLE (NCT04585750). | [test info](https://www.carislifesciences.com/physicians/physician-services/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 888-979-8669 |
| **Somatic homologous-recombination gene coverage (BRCA1, BRCA2, PALB2, ATM, RAD51 paralogs) with a genomic-instability or LOH score on the recurrence NGS** | **Caris Life Sciences *(preferred)* (MI Cancer Seek (whole exome plus whole transcriptome))** | **Somatic HRD evidence for off-label or trial PARP-inhibitor use and for keeping platinum in the sequence.** | **[test info](https://www.carislifesciences.com/physicians/physician-services/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 888-979-8669** |
| Somatic HR gene coverage with genomic-instability score | Myriad Genetics *(myChoice CDx (genomic instability score))* | Somatic HRD evidence for off-label or trial PARP-inhibitor use and for keeping platinum in the sequence. | [test info](https://myriad.com/contact-us/) · 322 North 2200 West, Salt Lake City, UT 84116 · 800-469-7423 |
| Somatic HR gene coverage with genomic-instability score | Foundation Medicine *(FoundationOne CDx)* | Somatic HRD evidence for off-label or trial PARP-inhibitor use and for keeping platinum in the sequence. | [test info](https://www.foundationmedicine.com/providers/contact) · 400 Summer Street, Boston, MA 02210 · 888-988-3639 |
| Somatic HR gene coverage with genomic-instability score | Tempus AI *(Tempus xT (DNA) plus xR (RNA))* | Somatic HRD evidence for off-label or trial PARP-inhibitor use and for keeping platinum in the sequence. | [test info](https://www.tempus.com/order/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 · 800-739-4137 |
| **Baseline CBC with differential, comprehensive metabolic panel with bilirubin and albumin, creatinine with calculated eGFR, coagulation studies, and CA 19-9** | **Labcorp *(preferred)*** | **Organ-function eligibility thresholds shared by the trials under consideration, plus a baseline CA 19-9 for response assessment.** | **[test info](https://www.labcorp.com/) · 358 South Main Street, Burlington, NC 27215 · 800-845-6167** |
| Baseline organ-function labs and CA 19-9 | Quest Diagnostics | Organ-function eligibility thresholds shared by the trials under consideration, plus a baseline CA 19-9 for response assessment. | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 866-697-8378 |
| Baseline organ-function labs and CA 19-9 | Mayo Clinic Laboratories | Organ-function eligibility thresholds shared by the trials under consideration, plus a baseline CA 19-9 for response assessment. | [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 800-533-1710 |
| **Fecal elastase-1, fat-soluble vitamin levels (A, D, E), HbA1c, and review of biliary anatomy and stent status on the restaging scan** | **Mayo Clinic Laboratories *(preferred)*** | **Nutritional and hepatobiliary fitness for systemic therapy and for trial performance-status and albumin thresholds.** | **[test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 800-533-1710** |
| Exocrine and hepatobiliary assessment | Labcorp | Nutritional and hepatobiliary fitness for systemic therapy and for trial performance-status and albumin thresholds. | [test info](https://www.labcorp.com/) · 358 South Main Street, Burlington, NC 27215 · 800-845-6167 |
| Exocrine and hepatobiliary assessment | Quest Diagnostics | Nutritional and hepatobiliary fitness for systemic therapy and for trial performance-status and albumin thresholds. | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 866-697-8378 |

The EUS-guided biopsy, the restaging imaging, the neuropathy examination, and serial on-treatment ctDNA are performed through the treating center's interventional endoscopy, radiology, and oncology services rather than a reference laboratory, so they carry no provider rows here; the serial TP53 resistance-monitoring draws, once relevant, use the same platforms as the plasma ctDNA panel above.

### Biomarker plan

| Recommended assay | Rationale | Suggested assay provider | Tissue requirements |
|---|---|---|---|
| EUS-guided core needle biopsy of the pancreatic body mass with histologic confirmation and tissue banked for downstream molecular and IHC work | Everything known about this tumor comes from a resection specimen taken before four more cycles of FOLFIRINOX, and the new mass has not been sampled, so its histology is presumed rather than established. One EUS-guided pass supplies the tissue that the CLDN18.2 re-stain, the DNA and RNA sequencing, and most tissue-gated trial screens all draw on. Skipping it means treating a radiographic diagnosis with a target call that may no longer hold. | interventional endoscopy at the treating center (no reference-lab order) | EUS-guided core biopsy; request at least three cores so one goes to a paraffin block for IHC and the rest to molecular |
| Comprehensive tumor NGS on recurrent-lesion tissue, DNA plus RNA, reporting codon-level KRAS genotype, TP53, homologous-recombination genes, fusions, MSI and TMB | G12R is not touched by the G12C-selective drugs (sotorasib, adagrasib) or by G12D-selective agents, so the codon-level call is what separates a pan-RAS(ON) route such as daraxonrasib from drugs that cannot work here; RASolute 302 (NCT06625320) asks for documented RAS status at codon 12, 13, or 61. Re-sequencing the recurrence also tests whether the driver persisted through ten cycles of FOLFIRINOX and catches anything acquired under that pressure. A DNA-only panel leaves fusion status unestablished rather than negative, which is why RNA should ride along. | Caris Life Sciences *(MI Cancer Seek (whole exome plus whole transcriptome))* · [test info](https://www.carislifesciences.com/physicians/physician-services/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 888-979-8669 | FFPE block or 10-15 unstained slides from the recurrent-lesion biopsy; archival resection block acceptable if the biopsy fails |
| Plasma ctDNA comprehensive panel reporting KRAS codon 12 genotype and TP53 Y220C with variant allele fractions | If the lesion turns out to be unsafe to biopsy, plasma is the only route to a current genotype, and it answers within about a week rather than a month. Several mutant-KRAS vaccine protocols in this space use ctDNA positivity as an entry criterion (ELI-002 7P, NCT05726864 phase 1, NCT07671339), so the result can gate access rather than merely inform it. A negative plasma result in a low-shedding pancreatic lesion does not overturn the tissue findings, which is the main way this assay is misread. | Guardant Health *(Guardant360 CDx)* · [test info](https://guardanthealth.com/contact/) · 3100 Hanover Street, Palo Alto, CA 94304 · 855-698-8887 | 10-20 mL whole blood; no tissue and no procedure |
| CLDN18.2 IHC by the VENTANA CLDN18 (43-14A) RxDx assay, reporting percent of viable tumor cells with moderate-to-strong (2+/3+) membranous staining | The existing 60% 2+/3+ result was produced by an assay the report does not name, and the >=75% cutoff that defines zolbetuximab eligibility in SPOTLIGHT and GLOW is specific to the 43-14A companion assay, so an unnamed clone cannot be scored against it. Re-staining with the FDA assay puts the number on the scale that every threshold conversation uses, including the sponsor assays for ASP2138 (NCT05365581) and CT041 (NCT04404595), which require central or protocol-specified IHC. Without it the whole CLDN18.2 strategy rests on a percentage that cannot be compared to any published threshold. | NeoGenomics Laboratories *(Claudin 18 FDA (VYLOY), VENTANA CLDN18 (43-14A) RxDx Assay)* · [test info](https://www.neogenomics.com/providers/test/APH-CLAP-01AX/claudin-18-fda-vyloy) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 (Client Services, option 3) | FFPE block, or one H&E plus 2-3 positively charged unstained slides at 4-5 microns with more than 100 viable tumor cells |
| Paired CLDN18.2 IHC on the recurrent-lesion biopsy and the December 2025 resection block, stained and scored side by side in one laboratory | CLDN18.2 expression is discordant between primary and metastatic lesions in a substantial minority of gastric cases (PMID 40200874), and loss of expression under zolbetuximab treatment has been documented in a reported case (PMID 41854734), so a stain from a pre-adjuvant resection is weak evidence about a lesion that emerged after ten cycles of chemotherapy. Running both specimens in the same laboratory in the same batch is what separates real biological change from inter-laboratory scoring drift. If only the recurrence is stained and comes back lower, there will be no way to tell which of the two explanations applies. | NeoGenomics Laboratories *(Claudin 18 FDA (VYLOY), VENTANA CLDN18 (43-14A) RxDx Assay)* · [test info](https://www.neogenomics.com/providers/test/APH-CLAP-01AX/claudin-18-fda-vyloy) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 (Client Services, option 3) | unstained slides from both blocks; request the December 2025 resection block from the operating hospital early, since retrieval is often the slow step |
| Dedicated germline multigene panel on blood or saliva covering BRCA1, BRCA2, PALB2, ATM, CDKN2A, STK11 and the mismatch-repair genes | The 'no incidental germline findings' line came off a tumor NGS report, which is not built for germline sensitivity, misses large rearrangements, and does not state which homologous-recombination genes were covered. NCCN recommends germline testing for every patient with pancreatic adenocarcinoma, and a pathogenic BRCA1/2 or PALB2 variant puts an approved PARP-inhibitor maintenance strategy on the table in this tumor type (POLO, PMID 31157963 and PMID 35834777) as well as arguing for keeping platinum in the sequence. It is a blood draw with no procedure attached, so it should go out now rather than wait on tissue. | Myriad Genetics *(MyRisk Hereditary Cancer with BRACAnalysis CDx)* · [test info](https://myriad.com/contact-us/) · 322 North 2200 West, Salt Lake City, UT 84116 · 800-469-7423 | 5-10 mL whole blood in EDTA, or a saliva kit |
| TP53 p.Y220C confirmation on a CLIA-certified NGS test (tumor tissue or plasma) reporting the variant at codon level with variant allele fraction | PYNNACLE (NCT04585750) states only that the tumor must carry a TP53 Y220C mutation, but the companion rezatapopt protocols spell out what counts: CLIA-certified local testing with variant allele fraction above 2% (NCT06616636), and tissue-based or liquid-biopsy NGS both acceptable (NCT07372625). The December 2025 tissue result probably satisfies this on its face; what the sponsor will want confirmed is that the variant is still present in current disease. Turning up at screening with only a pre-adjuvant report risks a re-test delay at best. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/providers/contact) · 400 Summer Street, Boston, MA 02210 · 888-988-3639 | no new specimen if the existing CLIA report is accepted; otherwise rides on the recurrence NGS or the plasma ctDNA draw |
| Graded neurologic examination for peripheral sensory neuropathy (CTCAE v5) with a patient-reported instrument (EORTC QLQ-CIPN20) at baseline | Ten total cycles of FOLFIRINOX is a large cumulative oxaliplatin exposure and no neuropathy grade appears anywhere in the record, yet most trial protocols exclude grade 2 or higher peripheral neuropathy and every platinum or taxane re-exposure decision turns on it. A documented baseline grade also gives the toxicity side of the 0.7 efficacy weight something real to sit on. Without it, both the ranking and the screening conversation are guessing about the one toxicity this patient is most likely to already carry. | treating oncology clinic (examination plus questionnaire; no lab order) | none; clinic examination and a questionnaire |
| Baseline CBC with differential, comprehensive metabolic panel with bilirubin and albumin, creatinine with calculated eGFR, coagulation studies, and CA 19-9 | No laboratory values were supplied at intake, so marrow, renal, and hepatic reserve after ten cycles of chemotherapy and a pancreatic resection are entirely unknown, and these thresholds appear in the eligibility criteria of essentially every trial under consideration. A baseline CA 19-9 is also needed now if it is going to mean anything as a response measure later. Screening failures on labs that were never checked are the most avoidable way to lose weeks here. | Labcorp · [test info](https://www.labcorp.com/) · 358 South Main Street, Burlington, NC 27215 · 800-845-6167 | one routine blood draw; can share the germline panel and ctDNA venipuncture |
| Pancreas-protocol CT of chest, abdomen and pelvis (or MRI abdomen) defining vascular involvement, biopsy route, and local-only versus metastatic extent, with RECIST-measurable target lesions identified | The recurrence is described as a body mass with likely vascular invasion, which leaves open both whether disease is confined to the pancreatic bed and whether a measurable target lesion exists; most trials require the latter. The same scan tells the interventional team whether an EUS or percutaneous route to the mass is safe. Local-only disease also keeps radiation and locoregional options in the conversation that widely metastatic disease would close. | radiology at the treating center (no reference-lab order) | none; imaging only |
| Somatic homologous-recombination gene coverage (BRCA1, BRCA2, PALB2, ATM, RAD51 paralogs) with a genomic-instability or LOH score on the recurrence NGS | A germline panel will miss somatic-only BRCA and PALB2 events, which occur in pancreatic adenocarcinoma and carry the same platinum-sensitivity signal even though the olaparib label is written around germline status. A genomic-instability score adds a phenotypic read when no single gene is hit. This rides on sequencing already recommended for the recurrence, so it costs an order line rather than a new specimen. | Caris Life Sciences *(MI Cancer Seek (whole exome plus whole transcriptome))* · [test info](https://www.carislifesciences.com/physicians/physician-services/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 888-979-8669 | no additional tissue beyond the recurrence NGS specimen |
| Quantified CLDN18.2 expression tier: percent of tumor cells at 1+, 2+ and 3+ membranous intensity, reported against each program's threshold | A single positive-or-negative call is useless here because the thresholds differ by program: >=75% at 2+/3+ for zolbetuximab (SPOTLIGHT, GLOW), and >=40% at >=2+ intensity for satri-cel, which the primary's 60% clears. Asking the laboratory to report the intensity distribution rather than one number lets each protocol be checked against its own criterion without re-staining. A 60% result sits in the band where this distinction decides which door is open. | NeoGenomics Laboratories *(Claudin 18 FDA (VYLOY), VENTANA CLDN18 (43-14A) RxDx Assay)* · [test info](https://www.neogenomics.com/providers/test/APH-CLAP-01AX/claudin-18-fda-vyloy) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 (Client Services, option 3) | no additional tissue; a reporting request on the CLDN18.2 re-stain |
| Fecal elastase-1, fat-soluble vitamin levels (A, D, E), HbA1c, and review of biliary anatomy and stent status on the restaging scan | Exocrine insufficiency after pancreatic resection is common, under-treated, and drives the weight loss and hypoalbuminemia that later cost patients trial eligibility and dose intensity; enzyme replacement is cheap and fixes it. New endocrine insufficiency after resection is frequent enough to check for. Biliary anatomy and any indwelling stent matter because cholangitis during systemic therapy is a common reason treatment stops. | Mayo Clinic Laboratories · [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 800-533-1710 | one stool sample plus routine blood; no procedure |
| TP53 Y220C variant allele fraction corrected for tumor purity, with TP53 copy number and LOH status, from the recurrence NGS | A Y220C reactivator only helps if the mutant protein is the dominant p53 species in most tumor cells, so a subclonal variant or a second inactivating hit on the other allele changes what the drug can plausibly do. In pancreatic adenocarcinoma TP53 alterations are typically clonal with LOH, so the expected answer supports the target rather than undercutting it. This does not gate PYNNACLE entry; it informs how much to expect. | Caris Life Sciences *(MI Cancer Seek (whole exome plus whole transcriptome))* · [test info](https://www.carislifesciences.com/physicians/physician-services/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 888-979-8669 | no additional tissue; a reporting request on the recurrence NGS |
| Serial plasma ctDNA TP53 sequencing during rezatapopt treatment to detect acquired secondary TP53 alterations in cis | Acquired secondary TP53 mutations arising in cis with Y220C drive clinical resistance to the Y220C reactivator (PMID 41504628, with accompanying commentary PMID 41918356), and they are detectable in plasma before imaging turns. Knowing that resistance is on-target rather than target-independent changes whether a next-generation p53 reactivator is worth pursuing. Only relevant once rezatapopt is actually started, which is why this sits below the eligibility rows. | Guardant Health *(Guardant360 CDx)* · [test info](https://guardanthealth.com/contact/) · 3100 Hanover Street, Palo Alto, CA 94304 · 855-698-8887 | 10-20 mL whole blood per timepoint |
| Co-alteration profiling on the recurrence NGS: CDKN2A, SMAD4, ARID1A, MYC amplification, and KRAS allelic imbalance or amplification | KRAS allelic imbalance and amplification are among the mechanisms that blunt RAS-pathway inhibition, and SMAD4 loss carries a distinct metastatic phenotype in pancreatic adenocarcinoma that bears on how aggressively to sequence therapies. None of these findings would exclude a pan-RAS(ON) trial, so this refines expectation rather than eligibility. It reads out on sequencing already ordered. | Caris Life Sciences *(MI Cancer Seek (whole exome plus whole transcriptome))* · [test info](https://www.carislifesciences.com/physicians/physician-services/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 888-979-8669 | no additional tissue; included in the recurrence NGS report |
| MMR IHC (MLH1, PMS2, MSH2, MSH6) plus MSI and TMB re-read as part of the recurrence NGS; no standalone order | MSS status and a TMB of 0.83 mut/Mb against a threshold of 10 are already at decision resolution and close the tumor-agnostic pembrolizumab routes; nothing here needs a new order. The only caveat is that neither assay platform was named, and TMB from a small panel is not interchangeable across platforms, a caveat that bites near the cutoff rather than an order of magnitude below it. If the recurrence is biopsied and sequenced anyway, both values re-report at no extra cost and MMR IHC can ride on the same block. | NeoGenomics Laboratories · [test info](https://www.neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 (Client Services, option 3) | no additional tissue; one unstained slide set if MMR IHC is added to an existing block |
| Characterization of KMT2C p.S2816fs as truncating and biallelic: variant allele fraction with tumor purity, KMT2C copy number and LOH, from the recurrence NGS | To be plain about it: no assay result would make this variant actionable today, because no approved or late-phase therapy selects patients on KMT2C status and the synthetic-lethal hypotheses remain preclinical. What a biallelic, clonal loss-of-function call would buy is entry to an epigenetic-agent basket trial that accepts COMPASS-complex alterations, if one is open and taking pancreatic patients. Nothing about this justifies a separate order or a separate specimen. | no separate order; a reporting request on the recurrence NGS | no additional tissue; a reporting detail on the recurrence NGS |

---

*Decision support, not medical advice. Confirm assay availability and current standards with the treating team and the local pathology service.*

<!-- libby:target-validation:end -->

## Scope summary

54 trial rows, 32 clinical-evidence rows, 46 preclinical rows, 18 target-validation rows, 53 accessibility rows, and 20 biomarker-survey rows feed this synthesis. This is the Experimental table, the feature-targeting investigational options only. It carries 40 rows: a rank-1 shared workup, six ranked therapeutic options, two options carried explicitly as not recommended (off-label zolbetuximab and single-agent PD-1 blockade), and thirty-one surfaced-but-not-ranked options flagged by reason. Agreement scores span 1.0, held by the workup and by daraxonrasib and IBI343 (both unanimous), down to -0.6 for satri-cel, which one persona ranked and four dissented from. **No persona issued a veto anywhere in this case.** Daraxonrasib was rank 1 on all five lists. Gemcitabine plus nab-paclitaxel, which conservative and concensusite both ranked second, targets none of the stated features and is routed to the co-equal Standard-of-care table rather than ranked here; the sequencing conflict it creates is carried in the caveat below, because that part does belong to this page.

## Cross-cutting caveat (read first)

**Nothing on this page has been measured on the tumor being treated.** The CLDN18.2 percentage, the KRAS G12R call, the TP53 Y220C call, the MSS and TMB reads: all of it comes from a December 2025 resection specimen that predates four cycles of adjuvant FOLFIRINOX, and the July 2026 mass is a radiographic diagnosis. The staging read on that biopsy is the fact everything else turns on, because metastatic versus locally recurrent flips access for the top-ranked option in the same stroke.

- The ranking is scoped to `profile.json::targetable_features[]`, and it is one of two co-equal tables. This Experimental table carries only feature-targeting *investigational* options: the workup, the recurrence-conditional therapeutic recs, and the off-label or trial-only routes against CLDN18.2, KRAS G12R, TP53 Y220C, and KMT2C. Standard second-line chemotherapy for this disease targets none of those features and lives on the Standard-of-care table, not here. That is a routing decision, not a judgment about its value; two personas ranked it second.
- If the recurrence biopsy does not confirm recurrent PDAC carrying these features, this case has no within-scope recommendations; standard-of-care for pancreatic adenocarcinoma lies outside Libby's targetable-feature ranking and should be pursued through the treating team's normal care channel.
- One qualification on how to read a negative CLDN18.2 stain. Biopsy sensitivity for CLDN18.2 runs about 54.6% against a resection standard, and primary-to-recurrence concordance is 83.3% with the losses clustering in local recurrence ([PMID 40694660](https://pubmed.ncbi.nlm.nih.gov/40694660)). A negative core is weak evidence of antigen loss. A positive one settles the question; a negative one does not.
- Practical workup logistics: one EUS-guided core pass supplies the CLDN18.2 re-stain, the DNA and RNA sequencing, and most tissue-gated trial screens, so it unlocks four of the eight other essential workup items. The vascular invasion around the mass may dictate the route, and plasma ctDNA is the fallback if the lesion cannot be sampled safely. Two items need no tissue at all and should go out this week: the dedicated germline panel and a CTCAE grade for the residual neuropathy.
- The scheduling trap the board flagged more than any other fact: RASolute 303 requires consent within 6 weeks of the metastatic diagnosis. That clock starts at staging, not at the team's convenience, so site outreach has to be teed up *before* the pathology result lands. Starting chemotherapy first silently closes the same window.

## Workup considerations

Nine target-validation rows are marked essential. Four of them ride on a single EUS-guided core pass and are folded into the rank-1 row above: histologic confirmation, comprehensive tumor NGS on recurrent tissue (DNA plus RNA, so fusion status ends up established rather than merely unaddressed), CLDN18.2 IHC by the VENTANA 43-14A companion assay, and a paired stain of the recurrence and the December 2025 block run side by side in one laboratory. That pairing matters more than it sounds: if only the recurrence is stained and comes back lower, there is no way to separate real antigen loss from inter-laboratory scoring drift.

Three essential rows are independent of the biopsy and should not wait on it. The dedicated germline multigene panel (BRCA1/2, PALB2, ATM, CDKN2A, STK11, mismatch-repair genes) is a blood draw NCCN has asked for in every pancreatic adenocarcinoma patient since 2019, and it gates the rank-5 row. A graded neurologic examination for peripheral sensory neuropathy, CTCAE v5 with a patient-reported instrument, is the item that changes a rank rather than decorates one: at documented grade 2 or higher, most trial protocols exclude and any taxane conversation ends. Baseline CBC, comprehensive metabolic panel with bilirubin and albumin, creatinine with eGFR, coagulation studies, and a CA 19-9 that will only mean something later if it is drawn now. A plasma ctDNA panel reporting KRAS codon 12 and TP53 Y220C with variant allele fractions answers in about a week and substitutes for tissue if the biopsy proves unsafe; several mutant-KRAS vaccine protocols use ctDNA positivity as an entry criterion, so it can open a door rather than merely inform.

Four high-priority rows add context without gating: pancreas-protocol cross-sectional imaging defining vascular involvement, biopsy route, and RECIST-measurable target lesions; somatic homologous-recombination gene coverage with a genomic-instability score, which a germline panel will miss and which costs an order line on sequencing already recommended; a quantified CLDN18.2 intensity distribution reported at 1+, 2+, and 3+ separately, so each program can be checked against its own threshold without re-staining; and an exocrine and endocrine insufficiency screen (fecal elastase-1, fat-soluble vitamins, HbA1c, biliary anatomy and stent status), because enzyme replacement is cheap and the weight loss it prevents is what later costs patients trial eligibility.

## Intervention grouping

- Pan-RAS and pan-KRAS inhibition against G12R: daraxonrasib ([PMID 42223072](https://pubmed.ncbi.nlm.nih.gov/42223072), [PMID 42090791](https://pubmed.ncbi.nlm.nih.gov/42090791), [NCT07573215](https://clinicaltrials.gov/study/NCT07573215), [NCT07491445](https://clinicaltrials.gov/study/NCT07491445), [NCT05379985](https://clinicaltrials.gov/study/NCT05379985)); ASP5834 ([NCT07094204](https://clinicaltrials.gov/study/NCT07094204)); KST-6051, AN9025, and five further escalations ([NCT07458347](https://clinicaltrials.gov/study/NCT07458347), [NCT07252479](https://clinicaltrials.gov/study/NCT07252479)).
- CLDN18.2 antibody-drug conjugates: IBI343 ([DOI 10.1200/JCO.2025.43.16_suppl.4017](https://doi.org/10.1200/JCO.2025.43.16_suppl.4017), [PMID 40670773](https://pubmed.ncbi.nlm.nih.gov/40670773), [NCT05458219](https://clinicaltrials.gov/study/NCT05458219)); AZD0901 ([PMID 39788133](https://pubmed.ncbi.nlm.nih.gov/39788133)); ASP546C, XNW27011, AZD4360, TORL-2-307, and the terminated EO-3021.
- CLDN18.2 T-cell engagers and bispecifics: ASP2138 ([NCT05365581](https://clinicaltrials.gov/study/NCT05365581), class mechanism [PMID 34433637](https://pubmed.ncbi.nlm.nih.gov/34433637)); AZD5863 ([PMID 40759445](https://pubmed.ncbi.nlm.nih.gov/40759445)); spevatamig (CD47), givastomig (4-1BB, [PMID 40586719](https://pubmed.ncbi.nlm.nih.gov/40586719)), QLS31905.
- CLDN18.2 cell therapy and naked antibody: satri-cel ([PMID 40460847](https://pubmed.ncbi.nlm.nih.gov/40460847), [PMID 38830992](https://pubmed.ncbi.nlm.nih.gov/38830992), [PMID 37689733](https://pubmed.ncbi.nlm.nih.gov/37689733)); LB1908 and TAC01; zolbetuximab ([PMID 37068504](https://pubmed.ncbi.nlm.nih.gov/37068504), [PMID 37524953](https://pubmed.ncbi.nlm.nih.gov/37524953), [NCT03816163](https://clinicaltrials.gov/study/NCT03816163)); FG-M108.
- CLDN18.2 radioligand therapy, the modality best matched to a patchy antigen and the one with no Western program at all: [177Lu]Lu-DOTA-SNA040 ([NCT07595237](https://clinicaltrials.gov/study/NCT07595237)) and IR199 ([NCT07707531](https://clinicaltrials.gov/study/NCT07707531)).
- p53 Y220C reactivators: rezatapopt ([PMID 41740031](https://pubmed.ncbi.nlm.nih.gov/41740031), [NCT04585750](https://clinicaltrials.gov/study/NCT04585750)); JAB-30355 ([NCT06386146](https://clinicaltrials.gov/study/NCT06386146)); NTS071, GenSci128, LG00313112; class liability in [PMID 34074758](https://pubmed.ncbi.nlm.nih.gov/34074758) and [PMID 41504628](https://pubmed.ncbi.nlm.nih.gov/41504628).
- Mutant-KRAS vaccines and cell therapy: mKRASvax with dual checkpoint blockade ([NCT06411691](https://clinicaltrials.gov/study/NCT06411691)); ELI-002 ([PMID 40790272](https://pubmed.ncbi.nlm.nih.gov/40790272), [NCT05726864](https://clinicaltrials.gov/study/NCT05726864)).
- PARP inhibition on a class-precedent axis the user did not name, carried because the germline panel that gates it has not been drawn: olaparib ([PMID 31157963](https://pubmed.ncbi.nlm.nih.gov/31157963), [PMID 35834777](https://pubmed.ncbi.nlm.nih.gov/35834777)).
- KMT2C: no clinical route in any tumor type. Two cross-tumor preclinical hypotheses only ([PMID 42118591](https://pubmed.ncbi.nlm.nih.gov/42118591)).

## Top interventions

## Rank 1. EUS-guided core biopsy of the recurrent mass, with restaging, paired CLDN18.2 IHC and NGS/ctDNA re-profiling — diagnostic and staging gate

*One procedure that resolves whether this is recurrent PDAC, whether it is metastatic or local, whether the drivers persisted, and what CLDN18.2 looks like on tissue that has actually seen chemotherapy.*

### Evidence base

This is an assay-and-staging action, so its evidence base is the eligibility criteria of the programs it unlocks plus the concordance literature that says archival tissue cannot stand in. CLDN18.2 expression is discordant between primary and recurrent specimens in a substantial minority of cases: concordance runs 83.3%, and the losses cluster in local recurrence and liver metastases, which is exactly this presentation ([PMID 40694660](https://pubmed.ncbi.nlm.nih.gov/40694660)). Kerper and colleagues found CLDN18.2 positivity less common in neoadjuvant-treated resections ([PMID 42080920](https://pubmed.ncbi.nlm.nih.gov/42080920)); the design is cross-sectional, so it cannot separate treatment-induced antigen loss from selection, and this tumor has since taken four more cycles. On the access side, RASolute 303 ([NCT07491445](https://clinicaltrials.gov/study/NCT07491445)) and the daraxonrasib expanded-access protocol both require confirmed metastatic disease, and the ASP2138 monotherapy arms exclude locally advanced unresectable patients.

### Likelihood of desired effect

As a gate it either opens the ranking or empties it. Four of the eight remaining essential workup items ride on this one specimen, and the staging call it produces controls whether the unanimously top-ranked drug is reachable at all. The one thing it cannot do cleanly is close the CLDN18.2 axis: at 54.6% biopsy sensitivity, a negative stain on a small core is not evidence of loss.

### Toxicity profile

- Procedural risk of EUS core sampling: bleeding, post-procedure pancreatitis. Modest, and the likely vascular invasion may dictate the route.
- No toxicity veto is engaged; the patient stated none.
- The real cost is time, and the schedule runs against the RASolute 303 consent clock rather than with it.

### Counter-productive mechanisms / dissent

Board endorsement was unanimous. Every persona named this workup, conservative called it cheap, fast, and the thing that opens or closes nearly every door above it, and concensusite defended it as guideline work rather than extra caution: NCCN wants suspected recurrence confirmed by imaging and/or biopsy, tumor NGS for every treatment candidate as of the March 2026 update, and tissue in hand before trial entry. No persona objected on any dimension.

### Practical considerations

Order the germline panel and the neuropathy grade now rather than bundling them with the procedure; neither needs tissue. Ask the laboratory for the CLDN18.2 intensity distribution at 1+, 2+, and 3+ separately rather than a single positive-or-negative call, since the programs in this dossier use at least four different thresholds. Run the recurrence and the archival block in the same batch in one laboratory. And make the RASolute 303 site call before the pathology comes back, because a 6-week consent window that starts at the metastatic diagnosis cannot be recovered afterwards.

### Why this rank

Every therapeutic option below is scored on a specimen from a different lesion. That is not a technicality in a tumor that has been under selective pressure for ten cycles, and it is why a procedure outranks a drug with a randomized survival win behind it.

### Per-trial detail

| Confirmatory assay | What it resolves | Turnaround / tissue | Reference |
| --- | --- | --- | --- |
| Histology + comprehensive NGS (DNA and RNA) on recurrent tissue | Is this recurrent PDAC; do KRAS G12R and TP53 Y220C persist; anything acquired | EUS core passes, banked | [NCT07491445](https://clinicaltrials.gov/study/NCT07491445), [NCT05379985](https://clinicaltrials.gov/study/NCT05379985) |
| CLDN18.2 IHC on the VENTANA 43-14A assay, paired with the December 2025 block | Where 60% 2+/3+ lands on the assay every threshold conversation uses | Same core; archival block in the same batch | [PMID 40694660](https://pubmed.ncbi.nlm.nih.gov/40694660), [PMID 42080920](https://pubmed.ncbi.nlm.nih.gov/42080920) |
| Restaging cross-sectional imaging | Metastatic vs locally recurrent; RECIST-measurable target lesion | Before the biopsy result, ideally | [NCT07491445](https://clinicaltrials.gov/study/NCT07491445), [NCT05365581](https://clinicaltrials.gov/study/NCT05365581) |
| Plasma ctDNA (KRAS codon 12, TP53 Y220C, with VAFs) | Current genotype if the lesion cannot be sampled; entry criterion for some vaccine protocols | ~1 week; blood | [NCT05726864](https://clinicaltrials.gov/study/NCT05726864), [NCT07252479](https://clinicaltrials.gov/study/NCT07252479) |

## Rank 2. Daraxonrasib (RMC-6236, oral pan-RAS(ON) multi-selective inhibitor)

*Conditional on `recurrence_profile:positive`. Foreclosed if the biopsy does not confirm recurrent PDAC carrying these features.*

### Evidence base

RASolute 302 is the only RCT-grade evidence in this dossier that is in pancreatic cancer and contains this allele ([PMID 42223072](https://pubmed.ncbi.nlm.nih.gov/42223072), n=500): median OS 13.2 vs 6.6 months against chemotherapy in the pre-specified RAS G12 population, HR 0.40, P<0.001, with PFS 7.3 vs 3.5 months, HR 0.45. The supporting phase 1/2 gave a second-line ORR of 35% (95% CI 17-56) in 26 RAS G12 patients ([PMID 42090791](https://pubmed.ncbi.nlm.nih.gov/42090791)). Two transfer problems sit under all of it and neither has been closed by anyone. G12R was inside that pooled estimand and was never studied as a population; no allele-resolved efficacy has been published, neither RMC-7977 paper carries a G12R arm, and the only G12R-specific daraxonrasib data is an un-peer-reviewed preprint. And RASolute 302 enrolled patients previously treated for metastatic disease, where this patient's only systemic exposure is perioperative and the recurrence is unstaged. The trial is also open-label, which OS survives and the PFS estimate less comfortably.

### Likelihood of desired effect

Moderate, and the qualifier is the whole point. The advocate opened at high confidence, three personas challenged it, and the advocate accepted the drop on the record. Critic and risktaker both argued that the two population mismatches widen the interval around the estimate rather than lower it, and risktaker withdrew their own G12R penetrance argument as an over-correction, since that work ([PMID 41556816](https://pubmed.ncbi.nlm.nih.gov/41556816)) describes tumor initiation rather than response to RAS(ON) inhibition. So: the direction of effect is as well established as anything in this file, and 13.2 versus 6.6 months should not be read as this patient's numbers.

### Toxicity profile

- Grade ≥3 AEs in 61.8% of the daraxonrasib arm against 69.6% on chemotherapy. Fewer, not more, than the comparator.
- Treatment-related discontinuation 1.2% versus 11.2%, which is the number that persuaded the conservative persona to put an unapproved drug first.
- Grade ≥3 treatment-related AEs in 30% of the 168-patient ≤300 mg PDAC safety set, dominated by rash and gastrointestinal events with workable management algorithms.
- The per-term grade ≥3 table lives in the NEJM full text, which the board read only at abstract level. What is priced here is the 61.8% union rate.
- No toxicity veto is engaged. Oral dosing with rash and GI as the dominant events steers around the ungraded oxaliplatin neuropathy, which is the toxicity this patient most likely already carries.
- First-in-human dosing began in 2022, so there is no follow-up beyond roughly three years and no post-marketing experience anywhere.

### Counter-productive mechanisms / dissent

No persona dissented and no persona vetoed; concensusite entered the only outright endorse of the round. The three round-2 critiques targeting this row were all *qualified*, and all three landed on the same thing: the confidence label, not the rank. Critic put it plainly, that "exactly this population" plus a high confidence label sells more than the abstract contains. On mechanism the only flag is modest, an allele-specific EGFR and RAS-wild-type rebound described in preprint, which argues for drafting the post-progression plan at the start rather than at progression.

### Practical considerations

Three routes exist and they close in different ways. RASolute 303 ([NCT07491445](https://clinicaltrials.gov/study/NCT07491445)) is recruiting and counts an adjuvant-only history as first-line, but requires confirmed metastatic disease and consent within 6 weeks of that diagnosis. The FDA-authorized expanded-access protocol ([NCT07573215](https://clinicaltrials.gov/study/NCT07573215)) is listed as available with drug supplied free of charge, physician-initiated through medinfo@revmed.com or 1-844-2-REVMED, and it is a monitored protocol rather than off-label improvisation, though its metastatic-plus-prior-line eligibility raises the same open question. The phase 1/2 ([NCT05379985](https://clinicaltrials.gov/study/NCT05379985)) stays open as the route that does not depend on a metastatic call. Guideline standing is anticipatory rather than actual: concensusite verified NCCN Pancreatic Adenocarcinoma v2.2026 (22 April 2026), which went to press before the RASolute 302 publication on 23 July 2026 and the July 2026 NDA acceptance, then found that v3.2026 has since posted and could not read it. Any claim that no guideline lists this drug is accurate as of April 2026 and is not a statement about today. One sequencing cost: taking this first closes the RAS-inhibitor-naive phase 1 doors, KST-6051 among them.

### Why this rank

It carries an agreement score of 1.0 alongside the workup and IBI343, and it sits above IBI343 because all five personas put it first on their own lists and because nothing else in the dossier has a pre-specified randomized primary endpoint in this disease. It sits below the workup because the staging call the workup produces is what decides whether two of its three access routes exist.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
| --- | --- | --- | --- |
| Daraxonrasib vs chemotherapy, previously treated mPDAC (RASolute 302) | mOS 13.2 vs 6.6 mo, HR 0.40, P<0.001; PFS 7.3 vs 3.5 mo | G≥3 AE 61.8% vs 69.6%; TRAE discontinuation 1.2% vs 11.2% | [PMID 42223072](https://pubmed.ncbi.nlm.nih.gov/42223072), [NCT06625320](https://clinicaltrials.gov/study/NCT06625320) |
| Daraxonrasib monotherapy, phase 1/2 RAS G12 PDAC | 2L ORR 35% (95% CI 17-56), n=26 | G≥3 TRAE 30% of 168 at ≤300 mg; rash, GI | [PMID 42090791](https://pubmed.ncbi.nlm.nih.gov/42090791), [NCT05379985](https://clinicaltrials.gov/study/NCT05379985) |
| Daraxonrasib ± gemcitabine/nab-paclitaxel, first-line (RASolute 303) | Pending | Pending | [NCT07491445](https://clinicaltrials.gov/study/NCT07491445) |
| Daraxonrasib expanded access, previously treated mPDAC | Not an efficacy study | Protocol-monitored; drug free of charge | [NCT07573215](https://clinicaltrials.gov/study/NCT07573215) |
| RAS(ON) inhibitors in GI solid tumors (RASolve 101) | Pending | Pending | [NCT06445062](https://clinicaltrials.gov/study/NCT06445062) |

## Rank 3. IBI343 (CLDN18.2 antibody-drug conjugate, exatecan payload)

*Conditional on `recurrence_profile:positive`. Foreclosed if the biopsy does not confirm recurrent PDAC carrying these features.*

### Evidence base

The dose-expansion cohort is the largest prospective CLDN18.2 efficacy dataset in previously treated pancreatic cancer, and it is a single-arm phase 1 reported as an ASCO 2025 abstract with no confidence interval on the 22.7% confirmed ORR and no per-term grade ≥3 table ([DOI 10.1200/JCO.2025.43.16_suppl.4017](https://doi.org/10.1200/JCO.2025.43.16_suppl.4017)). DCR was 81.8% and median OS 9.1 months in patients selected at CLDN18.2 ≥60%. The extracted evidence row records n=83 for that 6 mg/kg population while conservative and critic both read the dose-expansion cohort as 44 patients; the abstract is not detailed enough to settle which denominator carries the response rate, and that is worth knowing before anyone quotes it. The gastric phase 1 supplies the safety picture and a cross-tumor efficacy anchor: confirmed ORR 29% in the CLDN18.2-high 6 mg/kg group, n=127 ([PMID 40670773](https://pubmed.ncbi.nlm.nih.gov/40670773)). What the critic said before anyone calls 22.7% impressive still stands: 9.1 months does not separate from the 8.8 months (95% CI 6.2-9.7) that a plain gemcitabine/nab-paclitaxel class switch produced after FOLFIRINOX failure in the AGEO cohort ([PMID 26372701](https://pubmed.ncbi.nlm.nih.gov/26372701)). That is a cross-study comparison, and it is still the right comparison to make.

### Likelihood of desired effect

Moderate-to-low, with the threshold question resolved in an unexpected direction. Critic objected that the efficacy cohort pooled 1+/2+/3+ at ≥60% while this report says 2+/3+ in 60%, so the cutoff match was an assumption rather than a fact. Risktaker's arithmetic refutes the threshold half: cells scored 2+ or 3+ also count at the 1+ tier, so 60% at 2+/3+ on the same block cannot fall below a ≥1+ ≥60% line. Critic conceded that the advocate's confirm-with-the-sponsor framing is closer to right. The live risk that survives is assay and specimen concordance rather than arithmetic: an unnamed local clone on the archival slide, a sponsor central assay doing the actual calling, and a recurrence nobody has stained, with concordance at 83.3% and losses clustering in local recurrence ([PMID 40694660](https://pubmed.ncbi.nlm.nih.gov/40694660)).

### Toxicity profile

- Grade ≥3 treatment-related AEs 52.6% in the gastric phase 1 (n=116), led by neutrophil decrease 28.4% and white-cell decrease 25.9%, with anemia close behind.
- Treatment-related discontinuation 0.9%, no interstitial lung disease, and no grade ≥3 nausea or vomiting reported.
- No per-term grade ≥3 table exists for the PDAC cohort; that picture is borrowed from gastric.
- Marrow reserve after ten cycles of FOLFIRINOX is undocumented, and this is a myelosuppressive payload.
- Nothing here stacks on the neuropathy axis, which is the one advantage it holds over the chemotherapy it would displace.

### Counter-productive mechanisms / dissent

All five personas ranked it second or third; nobody dissented and nobody vetoed. The two round-2 critiques were qualified and pulled in opposite directions, which is unusual and useful: risktaker gave ground on the benchmark while refuting the threshold objection, and critic gave ground on the threshold while holding the benchmark. Mechanistically the exposure is antigen heterogeneity, since roughly 40% of cells do not stain, partly offset by bystander killing from the exatecan payload ([PMID 27166974](https://pubmed.ncbi.nlm.nih.gov/27166974) documents the class effect). The unanswered question conservative raised is a real one: an exatecan payload arrives after ten irinotecan-containing cycles, and topoisomerase-1 cross-resistance in that sequence has no published answer.

### Practical considerations

The phase 1 ([NCT05458219](https://clinicaltrials.gov/study/NCT05458219)) recruits at US and Australia sites alongside China, which makes this the CLDN18.2 route a US patient can realistically screen for. The registrational phase 3 ([NCT07066098](https://clinicaltrials.gov/study/NCT07066098)) is mainland China only, so expectations about where the definitive answer comes from should be set accordingly. Send the 43-14A re-stain result with the sponsor inquiry; expression level is the gating fact for ADC cohorts, and the live cohorts have skewed first-line. No guideline addresses CLDN18.2 in pancreatic cancer at all; NCCN's only CLDN18.2 text sits in Gastric/Esophageal v3.2026 at the ≥75% zolbetuximab cutoff, and guideline silence in this framework routes to a trial rather than forbidding the target.

### Why this rank

Same agreement score as daraxonrasib, and it ranks below it on the benchmark rather than on board signal: an option whose median survival sits inside the confidence interval of the chemotherapy floor it would displace has not yet shown that it beats that floor. It ranks above ASP2138 (0.4) because it is the only CLDN18.2 agent with a prospective efficacy readout in this disease, and because a payload that kills without needing T cells is the safer mechanism in an MSS, TMB-0.83 tumor.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
| --- | --- | --- | --- |
| IBI343 6 mg/kg, previously treated PDAC at CLDN18.2 ≥60% | Confirmed ORR 22.7%, DCR 81.8%, mOS 9.1 mo | TEAE 98.8%; anemia and neutrophil decrease most common; no per-term G≥3 table | [DOI 10.1200/JCO.2025.43.16_suppl.4017](https://doi.org/10.1200/JCO.2025.43.16_suppl.4017), [NCT05458219](https://clinicaltrials.gov/study/NCT05458219) |
| IBI343, gastric/GEJ phase 1 (CLDN18.2-high, 6 mg/kg) | Confirmed ORR 29%, n=127 | G≥3 TRAE 52.6%; neutropenia 28.4%, leukopenia 25.9%; discontinuation 0.9% | [PMID 40670773](https://pubmed.ncbi.nlm.nih.gov/40670773) |
| IBI343 vs placebo, previously treated CLDN18.2+ PDAC (phase 3) | Pending; mainland China only | Pending | [NCT07066098](https://clinicaltrials.gov/study/NCT07066098) |
| IBI343 + gemcitabine/nab-paclitaxel, advanced PDAC (phase 2) | Pending | Pending | [NCT06770439](https://clinicaltrials.gov/study/NCT06770439) |

## Rank 4. ASP2138 (CLDN18.2 x CD3 2+1 bispecific T-cell engager)

*Conditional on `recurrence_profile:positive`. Foreclosed if the biopsy does not confirm recurrent PDAC carrying these features.*

### Evidence base

There is no PDAC efficacy readout for this drug. What exists is a 12-week unconfirmed disease-control rate of 41.7% at ≥420 µg in the gastric/GEJ cohort, presented at ESMO 2025, from a congress abstract whose identifiers could not be verified against Crossref; the PDAC cohort has contributed safety only ([NCT05365581](https://clinicaltrials.gov/study/NCT05365581)). The critic called that the softest endpoint in the file and was right to. The argument for the drug is the eligibility gate rather than the number: a ≥1+ central-IHC cutoff against a tumor staining 2+/3+ in 60% of cells, a metastatic PDAC monotherapy arm with no line limit, and 46 sites across the US, Japan, Europe, and Asia. The target itself is well validated in this tissue ([PMID 23900716](https://pubmed.ncbi.nlm.nih.gov/23900716)).

### Likelihood of desired effect

Low to unknown, and the reason is biological rather than administrative. Across syngeneic models, pre-treatment intratumoral T-cell density drove bispecific engager response ([PMID 34433637](https://pubmed.ncbi.nlm.nih.gov/34433637)), and pancreatic adenocarcinoma is where that density bottoms out. The risktaker, who ranked this third, said so themselves. Engagers can produce deep responses when they connect, which is the ceiling argument for taking a phase 1 with no efficacy data in this disease, and the honest framing is that the ceiling is why it is here and the floor is why it is fourth.

### Toxicity profile

- Cytokine release syndrome in 43.2% of the gastric cohort and 23.4% of the PDAC cohort.
- No grade ≥3 nausea, vomiting, or gastritis reported on monotherapy; nausea any-grade 44.7% in the PDAC cohort.
- On-target gastric mucosal injury is the class liability, and this patient's post-resection upper-GI anatomy is nowhere in the record.
- No toxicity veto engaged, though several protocols cap peripheral neuropathy at grade 1 and that grade has never been assigned.

### Counter-productive mechanisms / dissent

Risktaker and advocate ranked it third; nobody dissented in round 2 and nobody vetoed. Both personas who ranked it labelled it honestly, the advocate writing that ranking it above better-published options would be selling hope, which is why it sits third on their list. The critic's objection lives in their notes rather than a critique row, and it is worth carrying: a 12-week unconfirmed disease-control rate is about as soft as endpoints get. The mechanism-level risk is that a T-cell-cold desmoplastic tumor starves the engager of the effector cells its response depends on, which is a Moderate rather than a theoretical concern in this disease.

### Practical considerations

Archival tissue may be able to start the screen while the biopsy is being scheduled, which is worth one call to the Astellas trial line (800-888-7704) because it saves weeks. The monotherapy arms exclude locally advanced unresectable disease, so the staging read decides which arms are open, and central CLDN18.2 IHC on submitted tissue is required regardless. No guideline standing exists; the same silence-routes-to-trial logic applies as for IBI343.

### Why this rank

Agreement score 0.4 against 1.0 for the rank above, and the gap is real rather than procedural: two personas ranked it, three did not. It sits above olaparib at the same score because the preference file says trials first and this is a live trial door, where olaparib is inert until a blood draw returns. It sits below IBI343 because a payload beats an engager in a tumor with no T cells to engage.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
| --- | --- | --- | --- |
| ASP2138 monotherapy, gastric/GEJ (≥420 µg) | 12-week unconfirmed DCR 41.7% | CRS 43.2%; TRAE any grade 77.3% | [NCT05365581](https://clinicaltrials.gov/study/NCT05365581) |
| ASP2138 monotherapy, metastatic PDAC cohort | No efficacy readout yet | CRS 23.4%; nausea 44.7%; no G≥3 gastritis on monotherapy | [NCT05365581](https://clinicaltrials.gov/study/NCT05365581) |

## Rank 5. Olaparib maintenance, gated on the germline panel that has not been drawn

*This row is about the test behind it. It sits in the Experimental table on the supplementary-key provision, because germline BRCA is not a feature the user named and the drug is off-label for this patient on two counts.*

### Evidence base

POLO is the only biomarker-directed option in this disease with a randomized base and an FDA label ([PMID 31157963](https://pubmed.ncbi.nlm.nih.gov/31157963), n=154): PFS 7.4 vs 3.8 months, HR 0.53, in germline BRCA-mutated metastatic pancreatic cancer after at least 16 weeks of first-line platinum without progression. The final overall survival analysis was null at 19.0 vs 19.2 months, P=0.3487 ([PMID 35834777](https://pubmed.ncbi.nlm.nih.gov/35834777)). The critic, who did not rank it, made the sharpest point about it: a positive germline result would put genuinely high-quality randomized evidence on the table where none of their own four picks has any. Nothing else in this file has that property.

### Likelihood of desired effect

Low, and honestly so. Roughly 5 to 7% of unselected pancreatic adenocarcinoma carries a germline BRCA1/2 variant, and recurrence four months after platinum-containing adjuvant therapy argues against the platinum sensitivity that carriers usually show, which lowers the prior further. Even with a positive panel this patient sits outside the POLO population as written, since POLO required 16 or more weeks of first-line platinum without progression. The realistic shape is off-label maintenance after a response to a new platinum-containing line, argued case by case with the payer. The honest framing even in a carrier is chemotherapy-free time, not survival gain.

### Toxicity profile

- Grade ≥3 AEs 40% versus 23% on placebo, with anemia, fatigue, and nausea the recurring events.
- Discontinuation for adverse events 5% versus 2%, and no new signals at the final analysis.
- The strategy presumes a platinum re-challenge the rest of this dossier argues against, which is a risk to the plan rather than to the patient.

### Counter-productive mechanisms / dissent

Conservative and concensusite ranked it fourth; nobody dissented and nobody vetoed, and three personas never mentioned the germline panel at all. Concensusite called that a compliance gap and the advocate called it a preference-fit failure, and both readings are right. Advocate's round-2 critique of the conservative row said the useful thing: ranking olaparib to force the germline draw was the right advocacy, better than leaving the panel in a notes field no coordinator will read. There is no mechanism-level objection; the concern is that the platinum sensitivity the whole strategy assumes is exactly what this recurrence timing argues against.

### Practical considerations

The panel is a blood draw orderable this week and it needs no tissue, so it should not wait on the biopsy. It should cover BRCA1, BRCA2, PALB2, ATM, CDKN2A, STK11, and the mismatch-repair genes; "no incidental findings" on a tumor NGS report is not a germline test, misses large rearrangements, and does not state which homologous-recombination genes were covered. A BRCA1/2-positive result should be documented with BRACAnalysis CDx; a PALB2-positive result will need an off-label prior-authorization argument, so the treating team should collect the supporting literature before submitting. Somatic-only BRCA and PALB2 events, plus a genomic-instability score, ride free on the recurrence NGS and a germline panel will miss them.

### Why this rank

Tied with ASP2138 at 0.4 and placed below it on preference fit, since the user asked for trials and this is an off-label prescription gated on an unrun test. It ranks above ASP5834 because two personas ranked it rather than one, and because the evidence behind the class is randomized rather than absent. If the panel comes back positive, this row moves up sharply.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
| --- | --- | --- | --- |
| Olaparib maintenance vs placebo, gBRCA-mutated mPDAC (POLO) | PFS 7.4 vs 3.8 mo, HR 0.53 | G≥3 AE 40% vs 23%; discontinuation 5% vs 2% | [PMID 31157963](https://pubmed.ncbi.nlm.nih.gov/31157963) |
| POLO final overall survival | 19.0 vs 19.2 mo, P=0.3487 (null) | No new safety signals | [PMID 35834777](https://pubmed.ncbi.nlm.nih.gov/35834777) |

## Rank 6. ASP5834 (intravenous pan-KRAS inhibitor), first-in-human phase 1

*Conditional on `recurrence_profile:positive`. Ranked on eligibility fit, not on evidence, and the section below says why that is defensible here and not for the Y220C tail.*

### Evidence base

There is none for this molecule. No published effect size, no toxicity table, nothing posted ([NCT07094204](https://clinicaltrials.gov/study/NCT07094204)). What the trial has instead is a set of posted criteria that match this patient's course with unusual precision: KRAS G12R is named explicitly among eligible mutations, adjuvant chemotherapy with recurrence inside 6 months counts as the prior line, and locally advanced unresectable disease is accepted alongside metastatic. The class prior is not zero, which is the difference that matters: daraxonrasib has already shown that pan-RAS inhibition produces a randomized survival benefit in this disease and this allele pool ([PMID 42223072](https://pubmed.ncbi.nlm.nih.gov/42223072)).

### Likelihood of desired effect

Unknown for this drug specifically. The reason it is on the ranked list rather than the surfaced one is narrow: it is the only KRAS-directed route that survives a locally-recurrent staging call, and that call is the largest single access risk in this case. If restaging reads local rather than metastatic, the daraxonrasib expanded-access protocol and RASolute 303 both close on the same day and this trial does not.

### Toxicity profile

- No published adverse-event table at any dose.
- Dose escalation, so early cohorts carry sub-therapeutic-dose risk as well as unknown toxicity.
- Intravenous administration sidesteps the post-resection oral-absorption question that undocumented organ function leaves open on the rank-2 option.

### Counter-productive mechanisms / dissent

Only the advocate ranked it, and they were explicit that they were ranking eligibility fit and executability rather than an effect size. Nobody dissented and nobody vetoed; four personas simply did not include it. The mechanism-level concern is the class-level one, that pan-KRAS inhibition can select RAS-wild-type escape, and the resistance map for this class is only now being drawn.

### Practical considerations

Sites are open in the US, Japan, France, and Spain, and the Astellas trial line (800-888-7704, Astellas.registration@astellas.com) can say which are enrolling and whether the PDAC expansion is open at the current dose level. Sequencing is the trap: several pan-KRAS trials exclude prior RAS-inhibitor exposure, so this class of door mostly closes after daraxonrasib. AN9025's backfill cohorts ([NCT07252479](https://clinicaltrials.gov/study/NCT07252479)) are the rare post-pan-RAS(ON) exception and are worth remembering at progression rather than now.

### Why this rank

Agreement score 0.2, one endorsement, and it stays on the ranked list rather than moving to the surfaced set for one reason: it answers the case's biggest access risk. It ranks below olaparib because a single endorsement is thinner board signal than two, and because the class behind olaparib is randomized while the drug here has nothing. Whether ranking a first-in-human escalation at all is defensible comes down to the asymmetry with the Y220C tail: the pan-KRAS class already has clinical validation in this disease, and the Y220C class has clinical evidence pointing the other way.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
| --- | --- | --- | --- |
| ASP5834, first-in-human dose finding, solid tumors incl. KRAS G12R | No published effect size | No published AE table | [NCT07094204](https://clinicaltrials.gov/study/NCT07094204) |
| Class-level validation (daraxonrasib, RASolute 302) | mOS 13.2 vs 6.6 mo, HR 0.40 | G≥3 AE 61.8% | [PMID 42223072](https://pubmed.ncbi.nlm.nih.gov/42223072) |

## Also considered — not ranked (feature-targeting investigational)

Thirty-one feature-targeting investigational options were surfaced without a live rank, plus two carried in the ranked table as explicitly not recommended. Each row in the summary table below carries a flag for why.

**Not enrollable, and the two that hurt.** [177Lu]Lu-DOTA-SNA040 ([NCT07595237](https://clinicaltrials.gov/study/NCT07595237)) is the best mechanistic match in the entire dossier and arrived after every board position was written, so no persona weighed it. Its entry threshold is ≥2+ in ≥20% of cells and this tumor clears it threefold, and beta crossfire kills antigen-negative neighbours, which makes the 40% of cells that do not stain far less disabling than they are for an antibody, an ADC, or a CAR. It is also a 12-patient investigator-initiated dose escalation at a single Shanghai center, with a companion study at Huashan ([NCT07707531](https://clinicaltrials.gov/study/NCT07707531)) that is dosimetry-only. Single-center Chinese investigator-initiated trials at this scale have no mechanism for enrolling foreign patients: consent, insurance, safety follow-up, and human-genetic-resources rules all assume local residents. Stated travel willingness does not bridge that, and a worldwide sweep found exactly three CLDN18.2 radioconjugate studies, all in China, with no Western clinical or declared preclinical program. **One event flips this row: a US IND from SmartNuclide, or any Western entrant into the class.** Satri-cel gets the same treatment for the same reason, which is where the board landed: critic ranked it third on design strength and then conceded the ranking while defending the evidence read, in their words that an option with no door occupying rank 3 above a reachable one is a category error. Risktaker and advocate refused to rank it, conservative dissented on toxicity (grade ≥3 TEAEs in 87 of 88 treated patients, CRS 95%), and concensusite dissented on the grounds that guideline silence routes you to a reachable trial rather than a closed one. It is carried as a sponsor-inquiry footnote below every reachable option.

**Thin evidence, and what that means for the tail ranks.** JAB-30355 ([NCT06386146](https://clinicaltrials.gov/study/NCT06386146)) was ranked by three personas and dissented from by two, and the critic asked that the reason be carried rather than smoothed over: the board's tail ranks measure whether a door is open, not whether evidence exists, and they must not be laundered into evidence-backed standing. Y220C fails twice in this patient. PYNNACLE's registrational rezatapopt monotherapy cohort excludes known KRAS single-nucleotide variants, which G12R is, and in the published phase 1 (n=77) every responder was KRAS wild-type, ORR 30% in that subset against 20% overall ([PMID 41740031](https://pubmed.ncbi.nlm.nih.gov/41740031)). Mechanistically, restoring p53 in a KRAS-driven tumor with low mitochondrial apoptotic priming produces arrest rather than apoptosis ([PMID 34074758](https://pubmed.ncbi.nlm.nih.gov/34074758)). JAB-30355's whole efficacy record is one sponsor phrase about a signal at high dose. The screening call is still worth making; the ranked slot is not something the evidence has bought. KST-6051 and AN9025 sit here for the same structural reason with a friendlier class prior, and both carry sequencing information worth acting on now: KST-6051 excludes prior RAS-inhibitor exposure and so closes permanently once daraxonrasib starts, while AN9025's backfill cohorts accept patients who already progressed on a pan-RAS(ON) inhibitor. Spevatamig and ASP546C are recruiting US CLDN18.2 doors with nothing published behind them.

**Consolidated under a ranked approach.** NTS071 sits under the JAB-30355 row; AZD5863 under ASP2138, though its affinity-modulated design aimed at lowering cytokine release is worth remembering; JAB-23E73, BLU-924, and BBO-11818 under the ranked pan-KRAS approach.

**Not enrollable for structural reasons.** Rezatapopt is excluded by its own registrational cohort's KRAS-SNV criterion. AZD0901's PDAC cohort requires progression at least 6 months after the last perioperative dose against this patient's roughly 4, which is two months of arithmetic closing a broadly recruiting trial. FG-M108 is the one CLDN18.2 phase 3 whose cutoff (≥40% at ≥2+) this tumor actually clears, posted at a single mainland-China site and not yet recruiting. mKRASvax is a real US door whose posted prior-therapy clause wants 4 to 6 months of first-line treatment for metastatic disease, and whose on-treatment biopsy requirement runs into the vascular invasion; risktaker's own advice was to keep the Hopkins line warm as a post-cytoreduction move. ELI-002 screens out patients whose imaging shows recurrence, which is this presentation. GenSci128, LG00313112, PF-07934040, YL-17231, JYP0015, QLS31905, givastomig, XNW27011, AZD4360, TORL-2-307, LB1908, TAC01-CLDN18.2, and the IR199 dosimetry study round out the set. EO-3021 is flagged unavailable: terminated, no successor.

**KMT2C.** The user asked that every variant stay on the table, and the honest content of that request here is a negative, which is carried as its own row rather than left implied. No approved or late-phase therapy selects patients on KMT2C status in any tumor type, no trial in this dossier enrolls on it, and the actionability hypotheses are preclinical and cross-tumor: purine-synthesis blockade in COMPASS-mutant cells, and PARP-inhibitor sensitivity through homologous-recombination disruption. The one credible mechanistic paper is gastric and uses double Kmt2c/d knockout plus Pten deletion ([PMID 42118591](https://pubmed.ncbi.nlm.nih.gov/42118591)), a long way from a single frameshift in a pancreatic tumor. Characterizing it as biallelic and clonal rides free on the recurrence NGS and would matter only for entry to an epigenetic-agent basket trial that accepts COMPASS-complex alterations, if one opens to pancreatic patients.

Three things are absent by design. Gemcitabine plus nab-paclitaxel, NALIRIFOX, and liposomal irinotecan target none of the stated features and belong to the Standard-of-care table. Zoldonrasib (KRAS G12D-selective), NT-112, and the G12V-directed TCR-T programs are target-absent for this allele and are excluded rather than surfaced. Sacituzumab tirumotecan (TROP2) and TNhYP218 (mesothelin) act on antigens that are not in this patient's stated feature set and whose expression has never been measured here; they are noted in the run log as upstream scope leaks rather than ranked.

## Ranked prioritization

**Diagnostic gate (do first):**

| Rank | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
| --- | --- | --- | --- | --- | --- |
| 1 | **EUS core biopsy of the recurrence + restaging + paired CLDN18.2 IHC + NGS/ctDNA**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | Diagnostic gate, not a therapy: unlocks four of eight remaining essential workup items and produces the staging call that controls access to rank 2. | Low (procedural only — EUS core biopsy: bleeding, post-procedure pancreatitis) | **N/A** | **Every option below is scored on a specimen from a different lesion, taken before four more cycles of chemotherapy; this is the step that makes the rest of the page about the tumor actually present.** |

**Ranked therapeutic options:**

| Rank | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
| --- | --- | --- | --- | --- | --- |
| 2 | **Daraxonrasib (RMC-6236, pan-RAS(ON))** (conditional on recurrence_profile positive)<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | Moderate: the only RCT-grade PDAC evidence containing this allele (RASolute 302, HR 0.40), read across a pooled estimand and a different line context. | High (grade ≥3 AEs 61.8%, below the 69.6% chemotherapy comparator: rash, diarrhea, nausea, stomatitis) | **Low** (pan-RAS inhibition can select RAS-wild-type escape; allele-specific EGFR rebound described in preprint only) | **The only option here with randomized survival evidence in PDAC that contains this allele; what is uncertain is the width of the interval, not the position.** |
| 3 | **IBI343 (CLDN18.2 ADC, exatecan)** (conditional on recurrence_profile positive)<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | Moderate-to-low: 22.7% confirmed ORR in expression-selected treated PDAC, but median OS 9.1 months sits inside the 8.8-month chemotherapy class-switch floor. | High (grade ≥3 TRAEs 52.6% in the gastric cohort: neutropenia 28.4%, leukopenia 25.9%, anemia, thrombocytopenia) | **Low** (roughly 40% of cells stain antigen-negative; bystander exatecan mitigates but does not erase escape) | **The best-evidenced CLDN18.2 route this patient can actually reach, and its own median survival has not yet cleared the chemotherapy floor it would displace.** |
| 4 | **ASP2138 (CLDN18.2 x CD3 engager)** (conditional on recurrence_profile positive)<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small> | Low-to-unknown in PDAC: no efficacy readout in this disease; the gastric signal is a 12-week unconfirmed DCR of 41.7%, the softest endpoint in the file. | Moderate (CRS 43.2% gastric / 23.4% PDAC cohort, largely low-grade; nausea 44.7%; on-target gastric mucosal injury) | **Moderate** (desmoplastic, T-cell-cold PDAC starves a CD3 engager of the effector density its response depends on) | **The widest-open CLDN18.2 door in the file, ranked on eligibility and site count rather than on evidence, in the tumor type where engagers historically struggle most.** |
| 5 | **Olaparib maintenance** (gated on the undrawn germline panel)<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span></small> | Low: roughly 5-7% pre-test probability of germline BRCA1/2, a POLO population fit this patient does not currently meet, and PFS-only benefit (HR 0.53). | Moderate (grade ≥3 AEs 40% vs 23% on placebo: anemia, fatigue, nausea) | **Low** (recurrence four months after platinum-containing adjuvant therapy argues against the platinum sensitivity this strategy assumes) | **Ranked chiefly to force a blood draw NCCN has asked for in every PDAC patient since 2019, which gates the one FDA-labelled biomarker route in this disease.** |
| 6 | **ASP5834 (IV pan-KRAS)** (conditional on recurrence_profile positive)<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span></small> | Unknown: zero published efficacy for this molecule. Ranked on eligibility fit, as the KRAS route that survives a locally-recurrent staging call. | Unknown (first-in-human dose escalation; no published AE table at any dose) | **Low** (pan-KRAS inhibition can select RAS-wild-type escape; the class resistance map is still being drawn) | **Insurance against the largest access risk in this case: it accepts locally advanced unresectable disease, which the daraxonrasib expanded-access protocol and RASolute 303 do not.** |
| 7 | **Zolbetuximab, off-label in PDAC** — *not recommended* | Low: the only randomized CLDN18.2 readout in PDAC was flat at 13.7 vs 13.6 months, and this tumor sits below the label-defining cutoff. | High (grade ≥3 TEAEs 87% with mFOLFOX6, 72.8% with CAPOX: nausea, vomiting, neutropenia) | **Low** (a naked antibody needs uniform surface antigen; roughly 40% of cells stain negative and there is no payload or crossfire) | **Prescribable off-label today and argued against on both counts: 60% is below the companion-diagnostic cutoff, and the randomized PDAC readout was flat.** |
| 8 | **Single-agent PD-1 blockade (pembrolizumab)** — *not recommended* | Low: MSS with TMB 0.83 mut/Mb forecloses both tumor-agnostic indications; single-agent checkpoint blockade has no route in this tumor. | Low (immune-related AE profile; academic here, since the indication is closed on biomarker) | **Low** (no target present; FAP+ CAF-driven exclusion keeps single-agent checkpoint blockade inert in MSS PDAC) | **Carried so the MSS / TMB-low result is visibly answered: it closes checkpoint monotherapy and routes immune interest to engagers, vaccines, and cell therapy instead.** |

**Also considered — not ranked (feature-targeting investigational):**

| Flag | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
| --- | --- | --- | --- | --- | --- |
| thin evidence | **JAB-30355** (p53 Y220C reactivator)<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span></small> | Unknown, and the class points the wrong way: every responder in rezatapopt's phase 1 (n=77) was KRAS wild-type, ORR 30% in that subset against 20% overall. | Unknown (no published AE table at any dose; the entire record is one sponsor sentence) | **Moderate** (restored p53 in a KRAS-driven, low-priming tumor produces arrest rather than apoptosis) | **The only Y220C door this KRAS-co-mutated patient can walk through, and Y220C fails twice here; the rank measures door-openness, not evidence.** |
| thin evidence | **KST-6051** (pan-KRAS, US phase 1) | Unknown: no published efficacy. Eligibility as posted asks only for a documented KRAS mutation, which G12R satisfies on its face. | Unknown (first-in-human dose escalation; no published AE table) | **Low** (pan-KRAS inhibition can select RAS-wild-type escape; no drug-specific mechanism data exist) | **A reachable US pan-KRAS door with an unusually simple eligibility line, and it closes permanently once daraxonrasib starts.** |
| thin evidence | **AN9025** (pan-RAS(ON), US phase 1) | Unknown: no published efficacy. Its posted criteria fit this history unusually well, including adjuvant therapy with progression inside 6 months as prior therapy. | Unknown (first-in-human dose escalation; no published AE table) | **Low** (pan-RAS(ON) inhibition can select RAS-wild-type escape; no drug-specific data exist) | **The rare pan-RAS(ON) trial with backfill cohorts that accept patients who already progressed on daraxonrasib, which makes it a post-progression asset.** |
| thin evidence | **Spevatamig** (CLDN18.2 x CD47, 11 US sites) | Unknown: no published efficacy. A straightforward US door in the CLDN18.2 class with tissue assessment built into screening. | Unknown (no published AE table; CD47 engagement carries a class anemia signal) | **Low** (CD47 blockade recruits macrophages rather than T cells, which sidesteps the T-cell-cold problem but is unproven here) | **One of the few CLDN18.2 programs recruiting at US sites for previously treated pancreatic carcinoma, with no published data behind it.** |
| thin evidence | **ASP546C** (CLDN18.2 ADC) | Unknown: no published efficacy or safety data. | Unknown (no published AE table) | **Low** (ADC class; antigen-negative cells depend on whatever bystander reach the undisclosed payload has) | **A recruiting CLDN18.2 ADC with nothing published; a screening call rather than a considered option.** |
| thin evidence | **KMT2C-directed therapy** — *not recommended* | None: no approved or late-phase therapy selects patients on KMT2C status, in any tumor type. | Not applicable (no agent to assess) | **N/A** | **The user asked that every variant stay on the table, so this one is named and its emptiness is stated rather than left implied.** |
| consolidated | **NTS071** (p53 Y220C reactivator) | Unknown: consolidated under the JAB-30355 row, which carries the class read for this patient. | Unknown (no published safety data of any kind) | **Moderate** (same class liability: restored p53 in a KRAS-driven, low-priming tumor arrests rather than kills) | **The second US Y220C door without a posted KRAS exclusion, kept as redundancy if the first one narrows.** |
| consolidated | **AZD5863** (CLDN18.2 x CD3 engager) | Consolidated under the ranked CD3-engager approach; preclinical work reports potent activity with limited cytokine release, and no clinical efficacy is published. | Unknown clinically (the affinity-modulated design is built to lower cytokine release; no human AE table) | **Moderate** (same T-cell-density dependency that handicaps every CD3 engager in desmoplastic PDAC) | **A second CLDN18.2 x CD3 engager whose affinity modulation targets the CRS problem; consolidated under the ASP2138 rank.** |
| consolidated | **JAB-23E73 / BLU-924 / BBO-11818** (pan-KRAS escalations) | Consolidated under the ranked pan-KRAS approach; no drug-specific efficacy published. | Unknown (dose escalation; no published AE table) | **Low** (pan-KRAS inhibition can select RAS-wild-type escape; no drug-specific data exist) | **Recruiting pan-KRAS escalations with no published data; the approach is already ranked at daraxonrasib and ASP5834.** |
| not enrollable | **[177Lu]Lu-DOTA-SNA040** (CLDN18.2 radioligand) | Unknown clinically, but the biomarker fit is the best in the file: it requires ≥2+ in ≥20% of cells and this tumor is 2+/3+ in 60%. | Unknown (no published clinical safety; radioligand class carries marrow and renal dose constraints) | **Low** (beta crossfire kills antigen-negative neighbours, which is the one CLDN18.2 approach heterogeneity does not disable) | **The best mechanistic match in the whole dossier and the least reachable: a 12-patient single-center trial in Shanghai with no mechanism for foreign enrollees.** |
| not enrollable | **Satri-cel** (CLDN18.2 CAR-T)<br><small><em>endorse:</em> <span class="persona persona-critic">critic</span></small><br><small><em>dissent:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | Not reachable: the strongest design in the CLDN18.2 class (mPFS 3.25 vs 1.77 months, HR 0.37) is gastric, and the absolute gain is about six weeks. | High (grade ≥3 TEAEs in 87 of 88 treated patients; CRS 95%; lymphopenia 98%; on-target gastric mucosal injury) | **Moderate** (desmoplastic, T-cell-poor PDAC is the environment CAR-T does worst in; on-target gastric injury adds a second vector) | **The closest expression match in the file and the one with no door: North American enrollment closed, the approval is dispensed only in mainland China.** |
| not enrollable | **Rezatapopt** (p53 Y220C reactivator, PYNNACLE) | Not enrollable as posted: ORR 20% overall and 30% in KRAS wild-type at ≥1150 mg (n=77), with no responder carrying a KRAS mutation. | Moderate (nausea 58%, vomiting 44%, creatinine increase 39%, fatigue 39%, largely low-grade) | **Moderate** (acquired secondary TP53 alterations in cis with Y220C drive on-target resistance in this class) | **The flagship Y220C program, closed to this patient by its own KRAS-SNV exclusion, with a phase 1 responder pattern that says the same thing.** |
| not enrollable | **AZD0901 / CMG901** (CLDN18.2 ADC) | Not enrollable as posted: the PDAC cohort is first-line and requires progression at least 6 months after the last perioperative dose; this recurrence came at about 4 months. | High (grade ≥3 TEAEs 68% in gastric: neutropenia 21%, anemia 14%, vomiting 10%) | **Low** (MMAE payload without meaningful bystander reach; antigen-negative cells are not covered) | **A broadly recruiting CLDN18.2 ADC whose PDAC cohort excludes this patient by two months of arithmetic.** |
| not enrollable | **FG-M108** (CLDN18.2 mAb + chemo, phase 3) | Unknown for this patient: the supporting phase 1b ORR of 32.4% (n=39) sits on a chemotherapy backbone that cannot isolate the antibody's contribution. | Moderate (anemia 56.2%, nausea 56.4%, vomiting 48.7% any-grade on a gemcitabine/nab-paclitaxel backbone) | **Low** (naked antibody depends on uniform antigen; ADCC enhancement does not reach antigen-negative cells) | **The one CLDN18.2 phase 3 whose cutoff this tumor actually clears, posted at a single mainland-China site and not yet recruiting.** |
| not enrollable | **mKRASvax + balstilimab + botensilimab**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span></small> | Low for bulk disease: AMPLIFY-201's HR 0.12 is a T-cell-threshold split inside a single-arm minimal-residual-disease trial with a different vaccine. | Unknown for this construct (dual checkpoint blockade brings immune-related toxicity; no organ-function labs exist) | **Moderate** (vaccines rarely shrink bulk desmoplastic tumors; the supporting data come from a minimal-residual-disease setting) | **G12R is in the peptide pool and the mandatory ECOG 0 fits, but a radiographic mass with vascular invasion is not minimal residual disease.** |
| not enrollable | **ELI-002 7P** (mKRAS amphiphile vaccine) | Not enrollable: AMPLIFY-7P screens out patients whose imaging shows recurrence, which is this patient's presentation. | Low (no dose-limiting toxicities across 25 patients in the phase 1; final abstract carries no AE table) | **Low** (minimal-residual-disease biology; no counter-productive vector, but no bulk-disease activity either) | **The vaccine platform with real G12R immunogenicity data in PDAC patients, and an entry criterion this recurrence fails on sight.** |
| not enrollable | **Givastomig** (CLDN18.2 x 4-1BB) | Cross-tumor only: ORR 16% in CLDN18.2-positive gastroesophageal cancer at ≥5 mg/kg (n=75), with no pancreatic arm. | Low (no dose-limiting toxicities through 18 mg/kg; MTD not reached; nausea and anemia the common treatment-related events) | **Moderate** (4-1BB costimulation needs T cells already present; PDAC is where that assumption fails) | **The best-tolerated agent in the CLDN18.2 file, with gastroesophageal-only efficacy and no pancreatic cohort.** |
| not enrollable | **QLS31905 / ANO31905** (CLDN18.2 x CD3, China phase 3) | Not enrollable: recruiting in China, and the phase 3 pairs the engager with a chemotherapy backbone this patient has functionally failed. | Unknown (no published AE table) | **Moderate** (same T-cell-density dependency as the class, on a chemotherapy backbone this tumor already progressed through) | **A CLDN18.2 engager that reached phase 3 in PDAC, recruiting in China only.** |
| not enrollable | **IR199** (CLDN18.2 radioconjugate, dosimetry only) | Not applicable: the primary endpoint is biodistribution and dosimetry from a single administration, so there is no treatment course to evaluate. | Not applicable (single-administration dosimetry study) | **N/A** | **Not treatment and not reachable; it matters only as proof the CLDN18.2 radioconjugate class has a second independent clinical program.** |
| not enrollable | **GenSci128 / LG00313112** (p53 Y220C reactivators) | Unknown: no published data, and no reachable site for a US patient. | Unknown (no published safety data) | **Moderate** (share the class liability of p53 reactivation in a KRAS-driven, low-priming tumor) | **Two more Y220C reactivators with no Western route; surfaced so the class inventory is complete.** |
| not enrollable | **PF-07934040 / YL-17231 / JYP0015** (pan-KRAS and pan-RAS programs) | Not enrollable for this patient (closed to enrolment, China-only, or graded not-yet-accessible); no published efficacy. | Unknown (no published AE table) | **Low** (pan-RAS inhibition can select RAS-wild-type escape; no drug-specific data exist) | **Pan-KRAS programs that match the allele and have no open door for this patient.** |
| not enrollable | **XNW27011 / AZD4360 / TORL-2-307** (CLDN18.2 ADCs) | Not enrollable: active but not recruiting; no case-relevant efficacy published. | Unknown (no published AE table) | **Low** (ADC class; antigen-negative cells depend on the payload's bystander reach) | **CLDN18.2 ADCs with no open door for this patient.** |
| not enrollable | **LB1908 / TAC01-CLDN18.2** (CLDN18.2 cell therapy) | Not enrollable: active but not recruiting; no clinical efficacy published in pancreatic cancer. | Unknown (cell-therapy class: CRS and lymphodepletion cytopenias; no published grade profile) | **Moderate** (cell therapy in desmoplastic, T-cell-poor PDAC faces the trafficking barrier that dominates this disease) | **CLDN18.2 cell-therapy programs that have stopped enrolling; carried so the cellular sweep is complete.** |
| unavailable | **EO-3021 / SYSA1801** (CLDN18.2 ADC) | Not available: the program was terminated with no successor study posted. | Not assessable (program terminated; no usable published safety readout) | **Low** (ADC class; no mechanism-level concern beyond the usual antigen-negative gap) | **A discontinued CLDN18.2 ADC, carried so its absence reads as a program decision rather than an oversight.** |

!!! note "How to read this table"
    **Toxicity burden** is patient-level adverse-event severity (Low/Moderate/High by grade-3+ rates and any treatment-related death). **Counter-productive MoA** is a different axis: the mechanism-level risk that the intervention works against the therapeutic goal, such as antigen-negative escape, T-cell starvation in a cold tumor, or p53 restoration that arrests rather than kills. The persona pills under each intervention are the at-a-glance board signal; the full per-persona rationale lives on the [board page](board.md).

## Caveats

- **Evidence-base caveats.** Of the six ranked options, one has a randomized primary endpoint (daraxonrasib), one has randomized evidence in a population this patient does not currently belong to (olaparib), one rests on a conference abstract with no confidence interval and no per-term toxicity table (IBI343), one has a 12-week unconfirmed disease-control rate in another disease (ASP2138), and one has nothing published at all (ASP5834). Eight interventions in this dossier have no indexed preclinical publication of any kind. GLEAM, the only randomized CLDN18.2 readout in pancreatic cancer, exists solely as a sponsor topline release and cannot be audited by anyone outside the company. Two comparator figures should not be repeated carelessly: the 20% one-year post-recurrence survival number comes from a cohort that excluded neoadjuvant-treated patients and used gemcitabine-era adjuvant therapy ([PMID 31082915](https://pubmed.ncbi.nlm.nih.gov/31082915)), and there is no randomized rechallenge-versus-switch trial in this window at all, with organoid work arguing that FOLFIRINOX failure should not be assumed to predict gemcitabine/nab-paclitaxel failure ([PMID 29853643](https://pubmed.ncbi.nlm.nih.gov/29853643)).
- **Compartment and biomarker dependencies.** Every therapeutic rank assumes the biopsy confirms recurrent PDAC carrying these features; the ranking is scored on a specimen from a different lesion taken before four more cycles of chemotherapy. The CLDN18.2 rows additionally assume the antigen survived, with concordance at 83.3% and losses clustering in local recurrence, and a negative core is weak evidence of loss at 54.6% biopsy sensitivity. Rank 5 is inert until the germline panel returns. Guideline currency is itself a dependency: everything guideline-related on this page is verified as of NCCN Pancreatic Adenocarcinoma v2.2026 (22 April 2026), and v3.2026 has posted and is unread behind the paywall, so no claim here should be quoted as current silence.
- **What would change the ranking.** A metastatic staging call opens the daraxonrasib expanded-access protocol and RASolute 303 and firms rank 2's deliverability; a locally-recurrent call closes both on the same day and moves ASP5834 up sharply. A positive germline BRCA1/2 or PALB2 result moves olaparib well above its current position, since it would put randomized, labelled evidence into a case that otherwise has one randomized option. A US IND from SmartNuclide, or any Western entrant into the CLDN18.2 radioligand class, would take the best mechanistic match in this dossier from unreachable to rankable. An allele-resolved G12R efficacy readout, or an independent replication that is not sponsor-shared with the phase 3, would narrow rank 2's interval rather than move its position. A documented grade 2 or higher oxaliplatin neuropathy would close several trial doors outright.
- **Re-scoping caveat.** The 0.7 efficacy/toxicity weight is an assumed default rather than the patient's number, and the preferences file says so itself. This ranking survives any plausible weighting, but if goals of care or organ function come back showing a frailer picture than an ECOG 0 chart implies, the whole page should be re-read with tolerability weighted higher and the first-in-human escalations dropped.

## Sources

**PMIDs**

- [23900716](https://pubmed.ncbi.nlm.nih.gov/23900716)
- [24277834](https://pubmed.ncbi.nlm.nih.gov/24277834)
- [26372701](https://pubmed.ncbi.nlm.nih.gov/26372701)
- [27166974](https://pubmed.ncbi.nlm.nih.gov/27166974)
- [29853643](https://pubmed.ncbi.nlm.nih.gov/29853643)
- [31082915](https://pubmed.ncbi.nlm.nih.gov/31082915)
- [31157963](https://pubmed.ncbi.nlm.nih.gov/31157963)
- [34074758](https://pubmed.ncbi.nlm.nih.gov/34074758)
- [34433637](https://pubmed.ncbi.nlm.nih.gov/34433637)
- [35834777](https://pubmed.ncbi.nlm.nih.gov/35834777)
- [37068504](https://pubmed.ncbi.nlm.nih.gov/37068504)
- [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953)
- [37689733](https://pubmed.ncbi.nlm.nih.gov/37689733)
- [38830992](https://pubmed.ncbi.nlm.nih.gov/38830992)
- [39404622](https://pubmed.ncbi.nlm.nih.gov/39404622)
- [39788133](https://pubmed.ncbi.nlm.nih.gov/39788133)
- [40460847](https://pubmed.ncbi.nlm.nih.gov/40460847)
- [40586719](https://pubmed.ncbi.nlm.nih.gov/40586719)
- [40670773](https://pubmed.ncbi.nlm.nih.gov/40670773)
- [40694660](https://pubmed.ncbi.nlm.nih.gov/40694660)
- [40759445](https://pubmed.ncbi.nlm.nih.gov/40759445)
- [40790272](https://pubmed.ncbi.nlm.nih.gov/40790272)
- [41504628](https://pubmed.ncbi.nlm.nih.gov/41504628)
- [41556816](https://pubmed.ncbi.nlm.nih.gov/41556816)
- [41740031](https://pubmed.ncbi.nlm.nih.gov/41740031)
- [42080920](https://pubmed.ncbi.nlm.nih.gov/42080920)
- [42090791](https://pubmed.ncbi.nlm.nih.gov/42090791)
- [42118591](https://pubmed.ncbi.nlm.nih.gov/42118591)
- [42223072](https://pubmed.ncbi.nlm.nih.gov/42223072)

**DOIs**

- [10.1200/JCO.2025.43.4_suppl.729](https://doi.org/10.1200/JCO.2025.43.4_suppl.729)
- [10.1200/JCO.2025.43.16_suppl.4017](https://doi.org/10.1200/JCO.2025.43.16_suppl.4017)

**NCTs**

- [NCT02628067](https://clinicaltrials.gov/study/NCT02628067)
- [NCT03816163](https://clinicaltrials.gov/study/NCT03816163)
- [NCT04585750](https://clinicaltrials.gov/study/NCT04585750)
- [NCT04900818](https://clinicaltrials.gov/study/NCT04900818)
- [NCT05156866](https://clinicaltrials.gov/study/NCT05156866)
- [NCT05365581](https://clinicaltrials.gov/study/NCT05365581)
- [NCT05379985](https://clinicaltrials.gov/study/NCT05379985)
- [NCT05458219](https://clinicaltrials.gov/study/NCT05458219)
- [NCT05482893](https://clinicaltrials.gov/study/NCT05482893)
- [NCT05539430](https://clinicaltrials.gov/study/NCT05539430)
- [NCT05726864](https://clinicaltrials.gov/study/NCT05726864)
- [NCT05862324](https://clinicaltrials.gov/study/NCT05862324)
- [NCT05980416](https://clinicaltrials.gov/study/NCT05980416)
- [NCT06005493](https://clinicaltrials.gov/study/NCT06005493)
- [NCT06096974](https://clinicaltrials.gov/study/NCT06096974)
- [NCT06219941](https://clinicaltrials.gov/study/NCT06219941)
- [NCT06386146](https://clinicaltrials.gov/study/NCT06386146)
- [NCT06411691](https://clinicaltrials.gov/study/NCT06411691)
- [NCT06445062](https://clinicaltrials.gov/study/NCT06445062)
- [NCT06447662](https://clinicaltrials.gov/study/NCT06447662)
- [NCT06625320](https://clinicaltrials.gov/study/NCT06625320)
- [NCT06770439](https://clinicaltrials.gov/study/NCT06770439)
- [NCT06792435](https://clinicaltrials.gov/study/NCT06792435)
- [NCT06895031](https://clinicaltrials.gov/study/NCT06895031)
- [NCT06908434](https://clinicaltrials.gov/study/NCT06908434)
- [NCT06917079](https://clinicaltrials.gov/study/NCT06917079)
- [NCT06921928](https://clinicaltrials.gov/study/NCT06921928)
- [NCT06973564](https://clinicaltrials.gov/study/NCT06973564)
- [NCT07060989](https://clinicaltrials.gov/study/NCT07060989)
- [NCT07066098](https://clinicaltrials.gov/study/NCT07066098)
- [NCT07079228](https://clinicaltrials.gov/study/NCT07079228)
- [NCT07094204](https://clinicaltrials.gov/study/NCT07094204)
- [NCT07252479](https://clinicaltrials.gov/study/NCT07252479)
- [NCT07383922](https://clinicaltrials.gov/study/NCT07383922)
- [NCT07444541](https://clinicaltrials.gov/study/NCT07444541)
- [NCT07458347](https://clinicaltrials.gov/study/NCT07458347)
- [NCT07488676](https://clinicaltrials.gov/study/NCT07488676)
- [NCT07491445](https://clinicaltrials.gov/study/NCT07491445)
- [NCT07573215](https://clinicaltrials.gov/study/NCT07573215)
- [NCT07595237](https://clinicaltrials.gov/study/NCT07595237)
- [NCT07629960](https://clinicaltrials.gov/study/NCT07629960)
- [NCT07671339](https://clinicaltrials.gov/study/NCT07671339)
- [NCT07707531](https://clinicaltrials.gov/study/NCT07707531)
- [NCT07752875](https://clinicaltrials.gov/study/NCT07752875)

## Transparency artifacts

- [Trial table](trials.md) — 54 rows, all columns, including the two CLDN18.2 radioligand studies that arrived after the board closed.
- [Evidence table](evidence.md) — 32 clinical and 46 preclinical rows, including the ones that did not rise to a ranked recommendation.
- [Master manuscripts table](manuscripts.md) — every paper considered, with sample size, effect size, variance, and toxicity columns.
- [Board proceedings](board.md) — 5 positions and 20 cross-critiques, with the full agreement matrix and per-persona reasoning.
- [Recommendations table](recommendations.md) — the 40 rows behind this page, sortable, with per-intervention detail.
- [Plain-language summary](plain_language.md) — the same content without the clinical vocabulary.

## Run log

Authored 12 August 2026 from the full dossier: profile, preferences, 20 biomarker-survey rows, 18 target-validation rows, 54 trials, 32 clinical-evidence rows, 46 preclinical rows, 21 preclinical-pipeline rows, 53 accessibility rows, and both board rounds. Everything ranked was supplied; nothing was inferred about the patient. Six judgments were mine rather than the board's, and each is argued in place: demoting satri-cel and the CLDN18.2 radioligand to sponsor-inquiry footnotes on the door-openness standard the board itself applied; flagging JAB-30355 as thin evidence rather than ranking it, on the critic's explicit request that tail ranks not be laundered into evidence-backed standing; keeping ASP5834 ranked despite the same absence of data, on the asymmetry that its class already has clinical validation in this disease; recording zolbetuximab and single-agent PD-1 blockade as explicitly not recommended even though no persona formally vetoed them; handling the [177Lu]Lu-DOTA-SNA040 access verdict, which arrived after every position was written and which no persona saw; and routing gemcitabine plus nab-paclitaxel out of this table to the Standard-of-care surface even though two personas ranked it second, while carrying its sequencing conflict here because that part belongs to this page. Two upstream scope leaks are noted rather than ranked: sacituzumab tirumotecan (TROP2) and TNhYP218 (mesothelin) target antigens not in this patient's stated feature set, neither of which has been measured. All PMID, DOI, and NCT identifiers carried into `recommendations.jsonl` and this page were verified against PubMed E-utilities, Crossref, and the ClinicalTrials.gov API before writing: 75 unique identifiers checked (29 PMIDs, 44 NCTs, 2 DOIs), 0 corrected, 0 nulled.

<!-- libby:downloads:begin -->

## Downloads

### HTML

- [Target validation paths](target_validation.md?v=8d5030c5) — per-feature biomarker-workup table with providers and references, sortable in-browser
- [Selected general biomarker report](biomarker_survey.md?v=dab629ef) — which panel biomarkers this patient has and has not been tested for, including the tumor-agnostic ones, in a sortable in-browser table
- [Selected general biomarker report (offline)](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-biomarker-survey.html?v=d303b999) — same biomarker survey packaged as a self-contained HTML that opens offline
- [Recommendations table](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-recommendations.html?v=adf25bf5) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Standard of care options](standard_of_care.md?v=b014102d) — approved and guideline-endorsed strategies for this patient's situation, assessed for eligibility and sequencing, in a sortable in-browser table
- [Standard of care options (offline)](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-standard-of-care.html?v=86a1f27a) — same standard-of-care assessment packaged as a self-contained HTML that opens offline
- [Preclinical recommendations](preclinical_recommendations.md?v=7cf67438) — forward-looking horizon scan of earlier-than-clinical candidate drugs, compounds, and strategies, in a sortable in-browser table
- [Preclinical recommendations (offline)](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-preclinical.html?v=78d3a6a9) — same preclinical horizon scan packaged as a self-contained HTML that opens offline
- [Access guide](accessibility.md?v=bcbb9719) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Access guide (offline)](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-accessibility.html?v=8cfd5f67) — same access-guide content packaged as a self-contained HTML that opens offline
- [Master manuscripts table](manuscripts.md?v=2300450f) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Master manuscripts table (offline)](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-manuscripts.html?v=d741ad30) — same manuscripts inventory packaged as a self-contained HTML that opens offline

### PDF

- [Target validation paths](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-target-validation.pdf?v=242e0eec) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Selected general biomarker report](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-biomarker-survey.pdf?v=54d191e4) — biomarker screening coverage and the gaps it leaves, in a print-friendly PDF
- [Recommendations table](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-recommendations.pdf?v=b5c1668e) — ranked options + pipeline context + evidence in detail, in a print-friendly PDF
- [Standard of care options](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-standard-of-care.pdf?v=5b3a2f36) — approved and guideline-endorsed strategies, their eligibility fit, and how they sequence against the targeted options, in a print-friendly PDF
- [Preclinical recommendations](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-preclinical.pdf?v=80a1aec5) — forward-looking horizon scan of earlier-than-clinical candidates, one deep section per candidate, in a print-friendly PDF
- [Access guide](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-accessibility.pdf?v=678335b2) — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF
- [Master manuscripts table](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-manuscripts.pdf?v=c285b2ba) — every paper considered — n, effect, variance, toxicities, in a print-friendly PDF
- [Patient/caregiver PDF](pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m-plain-language.pdf?v=48572492) — plain-language summary

<!-- libby:downloads:end -->

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
