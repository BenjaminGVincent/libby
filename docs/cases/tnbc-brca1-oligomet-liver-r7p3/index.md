<meta name="robots" content="noindex">

# `tnbc-brca1-oligomet-liver-r7p3`

<!-- libby:case-output:begin -->

## Case output

- [Target validation paths (PDF)](tnbc-brca1-oligomet-liver-r7p3-target-validation.pdf?v=608875ca) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table (HTML)](tnbc-brca1-oligomet-liver-r7p3-recommendations.html?v=dcf5cfc9) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide (HTML)](accessibility.md?v=86c8e87a) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, sortable in-browser
- [Access guide (offline HTML)](tnbc-brca1-oligomet-liver-r7p3-accessibility.html?v=14fff67a) — same access-guide content as the in-browser page, packaged as a self-contained HTML that opens offline
- [Master manuscripts table (HTML)](manuscripts.md?v=cd8be571) — every paper considered — n, effect, variance, toxicities, sortable in-browser
- [Master manuscripts table (offline HTML)](tnbc-brca1-oligomet-liver-r7p3-manuscripts.html?v=3df6d0d1) — same manuscripts inventory as the in-browser page, packaged as a self-contained HTML that opens offline
- [Patient/caregiver PDF](tnbc-brca1-oligomet-liver-r7p3-plain-language.pdf?v=32c31c9c) — plain-language summary

<!-- libby:case-output:end -->
## Research question

In newly diagnosed de novo M1 triple-negative breast cancer with BRCA1 mutation, basal-like subtype, TMB-high / TIL-rich phenotype, and a single 1.5 cm hepatic oligometastasis, what 1L interventions target the patient's biomarker axes — gated on germline-vs-somatic BRCA1 resolution, PD-L1 CPS by 22C3, and TMB platform confirmation?

## Patient profile (scrubbed)

- **Primary site / histology:** breast — invasive ductal carcinoma NST, triple-negative, basal-like by molecular subtyping
- **Stage:** cT2-3 cN1 cM1 — newly diagnosed; right breast primary with ipsilateral axillary nodal involvement and a solitary 1.5 cm hepatic lesion consistent with oligometastatic de novo M1 disease (liver-only single-site)
- **Performance status:** ECOG 1
- **Age band:** 40–49 (42)
- **Sex:** female
- **Biomarkers:**
    - **BRCA1** mutated by tumor NGS — *germline vs somatic not specified*; germline status gates olaparib / talazoparib on the FDA breast label
    - **TP53** mutated by tumor NGS — confirmed; functionally informative for replication-stress phenotype, not directly drug-gating
    - **PIK3CA** mutated by tumor NGS — *ngs_pending* for specific hotspot resolution; PI3K/AKT-axis options read negative in TNBC (CAPItello-290, EPIK-B3) so this gate is informational rather than actionable
    - **MYC amplification** by tumor NGS / copy-number — confirmed
    - **IRS2 amplification** by tumor NGS / copy-number — confirmed
    - **PTEN loss** by tumor NGS / copy-number — confirmed
    - **Intrinsic molecular subtype** basal-like (PAM50 or equivalent) — confirmed
    - **TMB** 14 mut/Mb by tumor NGS panel — *assay-platform confirmation on F1CDx pending* for KEYNOTE-158 label use
    - **MSI status:** MSS — confirmed; closes the tumor-agnostic MSI-H pembrolizumab door
    - **Stromal TILs:** 3+ stromal TILs (TILs-WG criteria, high) — confirmed; ITWG re-score recommended
    - **ER:** negative; **PR:** negative; **HER2:** negative (HER2 0 vs HER2-low not specified — gates T-DXd / Dato-DXd off-label questions)
- **PD-L1 CPS by 22C3:** *not on file — ngs_pending per target_validation*; gates KEYNOTE-355, ASCENT-04, and TROPION-Breast05 enrollment
- **Prior therapy:** none — treatment-naive
- **Current therapy:** none

## Preferences

- **Efficacy/toxicity weight:** 0.70 (moderate efficacy lean)
- **Toxicity vetoes:** none
- **Modality constraints:** none
- **Free text:** *"Defaults applied by intake agent — user did not explicitly state preferences. Rationale for moderately efficacy-leaning weight (0.7): newly diagnosed de novo M1 TNBC in a 42-year-old with high disease burden plus an oligometastatic single liver lesion — curative-intent strategy plausible (resection/ablation of solitary liver lesion after systemic conversion), so the operative goal weighs efficacy higher than tolerability. Trial preference set to true because the profile (BRCA1, PIK3CA, MYC/IRS2/PTEN, TMB-H, TIL-rich, basal-like, young, oligometastatic) is strongly trial-eligible and several of the best options sit in trial territory."*
- **Trials preferred:** yes

<!-- libby:target-validation:begin -->

## Target validation paths

Six gating workups load the 1L conversation in parallel: germline BRCA1 / hereditary breast-ovarian panel (gates olaparib via NCT02000622 and talazoparib via NCT01945775 on FDA label; the somatic-only contingency routes to NCT03990896), PD-L1 22C3 CPS on the breast primary block (gates pembrolizumab + chemo via KEYNOTE-355 / NCT02819518, sacituzumab govitecan + pembrolizumab via ASCENT-04 / NCT05382299, and datopotamab deruxtecan ± durvalumab via TROPION-Breast05 / NCT06103864), TMB on F1CDx (gates tumor-agnostic pembrolizumab under KEYNOTE-158 / NCT02628067 for later lines), PIK3CA hotspot resolution (gates alpelisib, inavolisib, and capivasertib eligibility, even though the PI3K/AKT-axis evidence in TNBC reads negative or terminated), PTEN IHC (gates capivasertib at the protein-level call), and HER2 IHC 0 vs 1+ / 2+ FISH-negative (gates trastuzumab deruxtecan for later lines if HER2-low reflexes positive). None of these involves a fresh biopsy. They run on archival FFPE plus a peripheral blood draw, in parallel, with turnaround between five business days and three weeks.

### BRCA1

Essential: germline BRCA1/2 sequencing plus del/dup on a hereditary breast-ovarian panel that also covers PALB2, ATM, CHEK2, BARD1, RAD51C/D, BRIP1, TP53, PTEN, CDH1, and STK11. The tumor NGS call does not say whether the BRCA1 variant is germline or somatic, and the answer changes a 42-year-old's life: germline carriers face bilateral mastectomy and risk-reducing salpingo-oophorectomy decisions and trigger cascade testing of first-degree relatives, while somatic-only BRCA1 still supports PARP-inhibitor and platinum sensitivity but does not drive surgical or family-screening choices. NCCN BINV and genetic-familial breast guidelines mandate this for any patient diagnosed under 50 or with TNBC. Pair the order with a cancer-genetics counseling visit so cascade testing can be triggered the same week the variant is classified. Turnaround is two to three weeks.

High priority: an HRD genomic-scar score (Myriad MyChoice CDx GIS, or the LOH-based signal on FoundationOne CDx) as orthogonal proof that the BRCA1 variant is producing a functional HR-deficient phenotype rather than sitting at a permissive VAF. Does not gate PARP-inhibitor eligibility in BRCA1-mutated TNBC, but it strengthens the platinum / PARP rationale and gives any future HR-targeted trial discussion a baseline scar reference.

High priority: a baseline ctDNA draw before any PARP-inhibitor or platinum exposure (Guardant360, FoundationOne Liquid CDx, or Natera Signatera tumor-informed). BRCA1/2 reversion mutations are detectable in roughly 60% of patients who progress on PARP inhibitors and are the dominant acquired-resistance mechanism in BRCA-mutated breast cancer. Without a clean baseline, the reversion call at later progression becomes ambiguous and the team cannot cleanly distinguish on-pathway resistance from off-pathway escape.

### PD-L1 / TILs

Essential: PD-L1 IHC 22C3 pharmDx on the breast primary FFPE block (CPS scoring for pembrolizumab; SP142 IC for atezolizumab if needed). The pembrolizumab + chemotherapy label for metastatic TNBC requires CPS ≥10 by the 22C3 companion diagnostic, and PD-L1 expression in TNBC is discordant between primary breast and liver metastasis in roughly 20-30% of paired samples. Run on the breast primary; if only liver M1 is available, run on both and document the discordance rate. Turnaround is five to seven business days.

Medium priority: ITWG stromal-TIL re-scoring on H and E by a dedicated breast pathologist using the Salgado 2014 methodology on a 0-100% scale. The 3+ stromal-TIL label sits cleanly with ITWG only if the scoring was done as a continuous percentage on a single tumor-bearing section; ad-hoc 1+/2+/3+ grading inflates inter-observer variability. The re-score does not gate ICI eligibility (TIL-rich status is informative, not labeled) but it makes the TIL signal defensible at tumor board.

### TMB

Essential: TMB measurement on an FDA-cleared comprehensive genomic panel sized ≥0.8 Mb, with the panel and threshold documented in the report. The tumor-agnostic pembrolizumab approval under KEYNOTE-158 is anchored on FoundationOne CDx as the companion diagnostic at a ≥10 mut/Mb cutoff, and TMB values are not interchangeable across panels. Smaller or differently-bioinformatic panels can over- or under-call TMB by 3-5 mut/Mb at the clinically relevant threshold. A 14 mut/Mb value from a non-FDA-cleared assay near the 10 mut/Mb cutoff is exactly the situation where the call should be locked to a panel the FDA label recognizes. If the original 14 mut/Mb already came from F1CDx, this row collapses to a chart-review check. Otherwise, re-run on F1CDx before using the value to gate pembrolizumab.

Medium priority: baseline B2M and HLA class I IHC (B2M EP2978Y, HLA-ABC EMR8-5) plus a re-read of B2M / HLA-A/B/C variant calls on the existing tumor NGS panel. B2M loss and HLA class I antigen-presentation defects are well-characterized primary-resistance mechanisms for ICI in TMB-high and MSI-H tumors. Cheap to add at the same time as the PD-L1 stain; refines the ICI rationale without gating it.

### PIK3CA / PTEN

Essential: PIK3CA variant resolution to the specific codon (therascreen PIK3CA RGQ PCR Kit or FoundationOne CDx) covering C420R, E542K, E545A/D/G/K, Q546E/R, H1047L/R/Y. The FDA companion diagnostics for alpelisib and capivasertib only call a tumor PIK3CA-altered for this 11-variant hotspot set. A non-hotspot helical or kinase-domain variant does not get a patient onto an alpelisib-labeled regimen. If the existing NGS already names the codon, this collapses to a chart-review check; if it does not, a hotspot-aware confirmation is the rate-limiting step before any PI3K-axis discussion. Even though the TNBC PI3K/AKT-axis evidence reads negative (CAPItello-290 was negative overall and in the AKT-pathway-altered stratum; EPIK-B3 was terminated for slow recruitment), the gate clarifies pathway biology rather than unlocking an active recommendation here.

Essential: PTEN IHC (clone 138G6 or SP218) with a positive internal control, scored as deficient if less than 10% of tumor cells stain at any intensity. Copy-number loss on NGS does not always translate to PTEN protein loss: PTEN is frequently inactivated by promoter methylation, frameshift, or LOH that panel-level copy-number resolution can miss. The IHC re-stain is the orthogonal protein-level confirmation that pathologists and tumor boards expect before AKT-inhibitor discussion. Turnaround is five to seven business days.

### Basal-like subtype

High priority: PAM50 intrinsic-subtype assay (NanoString Prosigna or Agendia BluePrint) with concurrent Lehmann TNBCtype-4 (BL1, BL2, M, LAR) classification on RNA-seq data. Roughly 25% of TNBCs do not classify as PAM50 basal-like, and within basal-like the Lehmann TNBCtype-4 subdivision carries divergent neoadjuvant pCR rates: BL1 about 52%, BL2 about 0%, LAR about 10%, M about 23% under anthracycline-taxane backbones. The current basal-like call should be locked to the assay that made it. The Lehmann layer adds therapeutic resolution that the basal-vs-non-basal binary cannot: LAR enrichment shifts the conversation toward AR-directed agents, M or MSL shifts it away from KEYNOTE-style ICI + taxane, and BL1 reinforces the platinum / PARP backbone already supported by BRCA1.

### TP53 / MYC / IRS2 (context)

Medium priority: a comprehensive NGS review for replication-stress and DDR co-alterations (ATM, ATR, CHK1/2, CDK12, CCNE1 amplification) and TP53 variant-functional classification. TP53 mutation is near-universal in basal-like TNBC and not directly drug-gating, but the co-alteration profile anchors the WEE1-inhibitor and ATR-inhibitor trial rationale. Shared block with the PIK3CA, PTEN, and TMB orders.

Medium priority: MYC FISH (8q24 break-apart / amplification probe set) or MYC IHC (clone Y69) on archival FFPE. MYC amplification by NGS copy-number is reasonably specific but the magnitude (low-level gain vs focal high-level amplification) varies by panel and tumor purity, and BET / CDK7 / CDK9 trial enrollment favors high-level amplification rather than borderline gain. Does not gate any approved therapy; refines MYC-pathway trial eligibility.

Low priority: IRS2 RNA expression on tumor RNA-seq with reference to the TCGA TNBC distribution. Copy-number amplification only matters clinically if it translates to elevated IRS2 transcript and a functional IGF-1R / IRS signaling readout. Deferrable until an IGF-1R-axis protocol is on the table. Bundle on the same RNA-seq order as PAM50 and Lehmann to share cost.

### Where to order these assays

| Assay | Provider | Decision gated | Contact |
|---|---|---|---|
| **Germline BRCA1/2 + hereditary breast-ovarian panel** | **Labcorp Genetics (formerly Invitae) *(preferred)* (Invitae Hereditary Breast and Gyn Cancers Panel)** | **Olaparib via NCT02000622 and talazoparib via NCT01945775 FDA-label eligibility; risk-reducing surgery (bilateral mastectomy, RRSO); cascade testing of first-degree relatives.** | **[test info](https://www.invitae.com/providers/test-catalog/test-01202) · 1400 16th Street, San Francisco, CA 94103 · 1-800-436-3037** |
| Germline BRCA1/2 + hereditary breast-ovarian panel | Myriad Genetics *(MyRisk Hereditary Cancer Panel)* | Olaparib via NCT02000622 and talazoparib via NCT01945775 FDA-label eligibility; risk-reducing surgery (bilateral mastectomy, RRSO); cascade testing of first-degree relatives. | [test info](https://myriad.com/oncology/myrisk/) · 320 Wakara Way, Salt Lake City, UT 84108 · 1-800-469-7423 |
| Germline BRCA1/2 + hereditary breast-ovarian panel | GeneDx *(GeneDx Comprehensive Common Cancer Panel)* | Olaparib via NCT02000622 and talazoparib via NCT01945775 FDA-label eligibility; risk-reducing surgery (bilateral mastectomy, RRSO); cascade testing of first-degree relatives. | [test info](https://www.genedx.com/tests/detail/comprehensive-common-cancer-panel-925) · 207 Perry Parkway, Gaithersburg, MD 20877 · 1-888-729-1206 |
| Germline BRCA1/2 + hereditary breast-ovarian panel | Ambry Genetics *(CancerNext)* | Olaparib via NCT02000622 and talazoparib via NCT01945775 FDA-label eligibility; risk-reducing surgery (bilateral mastectomy, RRSO); cascade testing of first-degree relatives. | [test info](https://www.ambrygen.com/clinician/genetic-testing/panel/cancernext) · 15 Argonaut, Aliso Viejo, CA 92656 · 1-866-262-7943 |
| **PD-L1 IHC 22C3 pharmDx on breast primary FFPE** | **Labcorp Oncology *(preferred)* (PD-L1 IHC 22C3 pharmDx (Dako/Agilent))** | **Pembrolizumab + chemotherapy via KEYNOTE-355 (NCT02819518) at CPS ≥10; sacituzumab govitecan + pembrolizumab via ASCENT-04 (NCT05382299); datopotamab deruxtecan ± durvalumab via TROPION-Breast05 (NCT06103864).** | **[test info](https://oncology.labcorp.com/) · 358 South Main Street, Burlington, NC 27215 · 1-800-345-4363** |
| PD-L1 IHC 22C3 pharmDx on breast primary FFPE | Quest Diagnostics *(PD-L1 22C3 pharmDx)* | Pembrolizumab + chemotherapy via KEYNOTE-355 (NCT02819518) at CPS ≥10; sacituzumab govitecan + pembrolizumab via ASCENT-04 (NCT05382299); datopotamab deruxtecan ± durvalumab via TROPION-Breast05 (NCT06103864). | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| PD-L1 IHC 22C3 pharmDx on breast primary FFPE | NeoGenomics Laboratories *(PD-L1 22C3 pharmDx)* | Pembrolizumab + chemotherapy via KEYNOTE-355 (NCT02819518) at CPS ≥10; sacituzumab govitecan + pembrolizumab via ASCENT-04 (NCT05382299); datopotamab deruxtecan ± durvalumab via TROPION-Breast05 (NCT06103864). | [test info](https://neogenomics.com/test-menu/pd-l1-22c3-pharmdx) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| PD-L1 IHC 22C3 pharmDx on breast primary FFPE | Mayo Clinic Laboratories *(PD-L1 22C3 pharmDx)* | Pembrolizumab + chemotherapy via KEYNOTE-355 (NCT02819518) at CPS ≥10; sacituzumab govitecan + pembrolizumab via ASCENT-04 (NCT05382299); datopotamab deruxtecan ± durvalumab via TROPION-Breast05 (NCT06103864). | [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 |
| **TMB on FDA-cleared comprehensive genomic panel ≥0.8 Mb (FoundationOne CDx, MSK-IMPACT, or Tempus xT CDx)** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Tumor-agnostic pembrolizumab under KEYNOTE-158 (NCT02628067) at ≥10 mut/Mb; TMB-restricted trial enrollment.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| TMB on FDA-cleared comprehensive genomic panel ≥0.8 Mb | Tempus Labs *(Tempus xT CDx)* | Tumor-agnostic pembrolizumab under KEYNOTE-158 (NCT02628067) at ≥10 mut/Mb; TMB-restricted trial enrollment. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| TMB on FDA-cleared comprehensive genomic panel ≥0.8 Mb | Memorial Sloan Kettering Diagnostic Molecular Pathology *(MSK-IMPACT)* | Tumor-agnostic pembrolizumab under KEYNOTE-158 (NCT02628067) at ≥10 mut/Mb; TMB-restricted trial enrollment. | [test info](https://www.mskcc.org/clinical-services/pathology/molecular-diagnostics) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |
| TMB on FDA-cleared comprehensive genomic panel ≥0.8 Mb | Caris Life Sciences *(MI Cancer Seek)* | Tumor-agnostic pembrolizumab under KEYNOTE-158 (NCT02628067) at ≥10 mut/Mb; TMB-restricted trial enrollment. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 1-888-979-8669 |
| **PIK3CA variant resolution to specific codon (11-variant hotspot set)** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Alpelisib, inavolisib, and capivasertib eligibility; trial enrollment for PI3K/AKT-axis studies requiring a hotspot-defined PIK3CA call.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| PIK3CA variant resolution to specific codon | Labcorp Oncology *(therascreen PIK3CA RGQ PCR Kit (FDA-approved))* | Alpelisib, inavolisib, and capivasertib eligibility; trial enrollment for PI3K/AKT-axis studies requiring a hotspot-defined PIK3CA call. | [test info](https://oncology.labcorp.com/tests/485113/pik3ca-mutation-analysis-therascreen-qiagen-fda-approved) · 358 South Main Street, Burlington, NC 27215 · 1-800-345-4363 |
| PIK3CA variant resolution to specific codon | Tempus Labs *(Tempus xT CDx)* | Alpelisib, inavolisib, and capivasertib eligibility; trial enrollment for PI3K/AKT-axis studies requiring a hotspot-defined PIK3CA call. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| PIK3CA variant resolution to specific codon | Caris Life Sciences *(MI Cancer Seek)* | Alpelisib, inavolisib, and capivasertib eligibility; trial enrollment for PI3K/AKT-axis studies requiring a hotspot-defined PIK3CA call. | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 1-888-979-8669 |
| PIK3CA variant resolution to specific codon | Guardant Health *(Guardant360 CDx)* | Alpelisib, inavolisib, and capivasertib eligibility; trial enrollment for PI3K/AKT-axis studies requiring a hotspot-defined PIK3CA call. | [test info](https://guardanthealth.com/products/guardant360-cdx/) · 505 Penobscot Drive, Redwood City, CA 94063 · 1-855-698-8887 |
| **PTEN IHC (clone 138G6 or SP218) with internal control, deficient if less than 10% tumor staining** | **Mayo Clinic Laboratories *(preferred)* (PTEN Immunostain)** | **Capivasertib + fulvestrant (HR+/HER2-) decision; trial enrollment for AKT-inhibitor protocols in TNBC requiring PTEN-deficient status by IHC.** | **[test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710** |
| PTEN IHC | NeoGenomics Laboratories *(PTEN IHC)* | Capivasertib + fulvestrant (HR+/HER2-) decision; trial enrollment for AKT-inhibitor protocols in TNBC requiring PTEN-deficient status by IHC. | [test info](https://neogenomics.com/test-menu/pten-stain) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| PTEN IHC | Memorial Sloan Kettering Pathology Consultation Service | Capivasertib + fulvestrant (HR+/HER2-) decision; trial enrollment for AKT-inhibitor protocols in TNBC requiring PTEN-deficient status by IHC. | [test info](https://www.mskcc.org/clinical-services/pathology/consultation-services) · 1275 York Avenue, New York, NY 10065 · 1-212-639-5511 |
| PTEN IHC | Labcorp / Esoterix *(PTEN IHC)* | Capivasertib + fulvestrant (HR+/HER2-) decision; trial enrollment for AKT-inhibitor protocols in TNBC requiring PTEN-deficient status by IHC. | [test info](https://www.labcorp.com/) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| **HRD genomic-scar score (Myriad MyChoice CDx GIS or LOH-based on FoundationOne CDx)** | **Myriad Genetics *(preferred)* (MyChoice CDx (HRD with Genomic Instability Score))** | **Orthogonal HR-deficient phenotype call; strengthens platinum / PARP rationale; does not gate PARP-inhibitor eligibility in BRCA1-mutated TNBC.** | **[test info](https://myriad.com/oncology/mychoice-cdx/) · 320 Wakara Way, Salt Lake City, UT 84108 · 1-800-469-7423** |
| HRD genomic-scar score | Foundation Medicine *(FoundationOne CDx (LOH-based HRD signal))* | Orthogonal HR-deficient phenotype call; strengthens platinum / PARP rationale; does not gate PARP-inhibitor eligibility in BRCA1-mutated TNBC. | [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| HRD genomic-scar score | Caris Life Sciences *(MI Profile HRD)* | Orthogonal HR-deficient phenotype call; strengthens platinum / PARP rationale; does not gate PARP-inhibitor eligibility in BRCA1-mutated TNBC. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 1-888-979-8669 |
| HRD genomic-scar score | Tempus Labs *(Tempus HRD)* | Orthogonal HR-deficient phenotype call; strengthens platinum / PARP rationale; does not gate PARP-inhibitor eligibility in BRCA1-mutated TNBC. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| **PAM50 intrinsic-subtype assay plus Lehmann TNBCtype-4 classification** | **Veracyte *(preferred)* (Prosigna PAM50)** | **TNBC-subtype-directed therapy bias (AR-axis vs platinum / PARP vs ICI + taxane); trial-enrollment refinement for subtype-restricted protocols.** | **[test info](https://www.veracyte.com/our-products/prosigna/) · 6000 Shoreline Court, Suite 300, South San Francisco, CA 94080 · 1-650-243-6300** |
| PAM50 intrinsic-subtype assay | Agendia *(BluePrint 80-gene molecular subtyping)* | TNBC-subtype-directed therapy bias (AR-axis vs platinum / PARP vs ICI + taxane); trial-enrollment refinement for subtype-restricted protocols. | [test info](https://agendia.com/our-tests/blueprint/) · 22 Morgan, Suite 100, Irvine, CA 92618 · 1-888-321-2732 |
| PAM50 intrinsic-subtype assay | Tempus Labs *(Tempus xR (RNA-seq))* | TNBC-subtype-directed therapy bias (AR-axis vs platinum / PARP vs ICI + taxane); trial-enrollment refinement for subtype-restricted protocols. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| PAM50 intrinsic-subtype assay | Caris Life Sciences *(MI Cancer Seek + WTS)* | TNBC-subtype-directed therapy bias (AR-axis vs platinum / PARP vs ICI + taxane); trial-enrollment refinement for subtype-restricted protocols. | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 1-888-979-8669 |
| **Baseline ctDNA for BRCA1 reversion surveillance** | **Guardant Health *(preferred)* (Guardant360 CDx)** | **Acquired PARP-inhibitor and platinum resistance surveillance; informs whether to push through resistance or switch to a non-HR-axis therapy.** | **[test info](https://guardanthealth.com/products/guardant360/) · 505 Penobscot Drive, Redwood City, CA 94063 · 1-855-698-8887** |
| Baseline ctDNA for BRCA1 reversion surveillance | Foundation Medicine *(FoundationOne Liquid CDx)* | Acquired PARP-inhibitor and platinum resistance surveillance; informs whether to push through resistance or switch to a non-HR-axis therapy. | [test info](https://www.foundationmedicine.com/test/foundationone-liquid-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| Baseline ctDNA for BRCA1 reversion surveillance | Natera *(Signatera (tumor-informed ctDNA))* | Acquired PARP-inhibitor and platinum resistance surveillance; informs whether to push through resistance or switch to a non-HR-axis therapy. | [test info](https://www.natera.com/oncology/signatera-advanced-cancer-detection/) · 13011 McCallen Pass, Building A, Austin, TX 78753 · 1-650-249-9090 |
| Baseline ctDNA for BRCA1 reversion surveillance | Tempus Labs *(Tempus xF)* | Acquired PARP-inhibitor and platinum resistance surveillance; informs whether to push through resistance or switch to a non-HR-axis therapy. | [test info](https://www.tempus.com/oncology/genomic-profiling/xf/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| **ITWG stromal-TIL re-scoring (Salgado 2014 methodology, 0-100% scale)** | **Memorial Sloan Kettering Pathology Consultation Service *(preferred)*** | **ICI-combination rationale strength (KEYNOTE-522, IMpassion-style); reinforces but does not gate enrollment.** | **[test info](https://www.mskcc.org/clinical-services/pathology/consultation-services) · 1275 York Avenue, New York, NY 10065 · 1-212-639-5511** |
| ITWG stromal-TIL re-scoring | Dana-Farber / Brigham and Women's Pathology | ICI-combination rationale strength (KEYNOTE-522, IMpassion-style); reinforces but does not gate enrollment. | [test info](https://www.brighamandwomens.org/pathology) · 75 Francis Street, Boston, MA 02115 · 1-617-732-7510 |
| ITWG stromal-TIL re-scoring | MD Anderson Department of Pathology | ICI-combination rationale strength (KEYNOTE-522, IMpassion-style); reinforces but does not gate enrollment. | [test info](https://www.mdanderson.org/departments-divisions/pathology.html) · 1515 Holcombe Boulevard, Houston, TX 77030 · 1-877-632-6789 |
| ITWG stromal-TIL re-scoring | Mayo Clinic Anatomic Pathology Consultation | ICI-combination rationale strength (KEYNOTE-522, IMpassion-style); reinforces but does not gate enrollment. | [test info](https://www.mayoclinic.org/departments-centers/laboratory-medicine-pathology) · 200 First Street SW, Rochester, MN 55905 · 1-800-533-1710 |
| **MYC FISH (8q24 break-apart / amplification probe set) or MYC IHC (clone Y69)** | **NeoGenomics Laboratories *(preferred)* (MYC FISH)** | **Refines MYC-amplification call strength for BET, CDK7, and CDK9 trial enrollment; does not gate approved therapy.** | **[test info](https://neogenomics.com/test-menu/myc-fish) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| MYC FISH or IHC | Mayo Clinic Laboratories *(MYCBA / MYC Break-Apart FISH)* | Refines MYC-amplification call strength for BET, CDK7, and CDK9 trial enrollment; does not gate approved therapy. | [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 |
| MYC FISH or IHC | Labcorp / Esoterix *(MYC FISH)* | Refines MYC-amplification call strength for BET, CDK7, and CDK9 trial enrollment; does not gate approved therapy. | [test info](https://www.labcorp.com/) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| MYC FISH or IHC | Quest Diagnostics *(MYC FISH)* | Refines MYC-amplification call strength for BET, CDK7, and CDK9 trial enrollment; does not gate approved therapy. | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| **B2M and HLA class I IHC plus variant-call review on tumor NGS** | **NeoGenomics Laboratories *(preferred)* (B2M IHC / HLA Class I IHC)** | **Primary-resistance risk for pembrolizumab and other PD-1/PD-L1 agents; refines the ICI rationale without gating it.** | **[test info](https://neogenomics.com/) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| B2M and HLA class I IHC | Mayo Clinic Laboratories *(B2M / HLA Class I IHC)* | Primary-resistance risk for pembrolizumab and other PD-1/PD-L1 agents; refines the ICI rationale without gating it. | [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 |
| B2M and HLA class I IHC | Memorial Sloan Kettering Pathology Consultation Service | Primary-resistance risk for pembrolizumab and other PD-1/PD-L1 agents; refines the ICI rationale without gating it. | [test info](https://www.mskcc.org/clinical-services/pathology/consultation-services) · 1275 York Avenue, New York, NY 10065 · 1-212-639-5511 |
| **Comprehensive NGS review for replication-stress / DDR co-alterations and TP53 variant classification** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **WEE1 / ATR-inhibitor trial enrollment rationale; not gating for any approved therapy.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| Comprehensive NGS review for DDR co-alterations | Tempus Labs *(Tempus xT CDx)* | WEE1 / ATR-inhibitor trial enrollment rationale; not gating for any approved therapy. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| Comprehensive NGS review for DDR co-alterations | Caris Life Sciences *(MI Cancer Seek)* | WEE1 / ATR-inhibitor trial enrollment rationale; not gating for any approved therapy. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 1-888-979-8669 |
| **IRS2 RNA expression on tumor RNA-seq** | **Tempus Labs *(preferred)* (Tempus xR (whole-transcriptome RNA-seq))** | **IGF-1R / IRS-axis trial enrollment; does not gate approved therapy.** | **[test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137** |
| IRS2 RNA expression | Caris Life Sciences *(MI Profile WTS)* | IGF-1R / IRS-axis trial enrollment; does not gate approved therapy. | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 1-888-979-8669 |

### Biomarker plan

| Recommended assay | Rationale | Suggested assay provider | Tissue requirements |
|---|---|---|---|
| PIK3CA variant resolution to specific codon (therascreen PIK3CA RGQ PCR Kit hotspots or FoundationOne CDx) covering C420R, E542K, E545A/D/G/K, Q546E/R, H1047L/R/Y | The profile says PIK3CA is mutated but does not specify the codon, and the FDA companion diagnostics for alpelisib (therascreen PIK3CA) and the F1CDx label for capivasertib (PIK3CA/AKT1/PTEN) only call a tumor PIK3CA-altered for the 11-variant hotspot set. A non-hotspot helical or kinase-domain variant does not get a patient onto an alpelisib-labeled regimen and may or may not be accepted by capivasertib protocols, so the resolution gates which PI3K/AKT-axis drug can be offered at all. If the existing NGS already names the codon, this row collapses to a documentation check; if it does not, a hotspot-aware confirmation is the rate-limiting step before any PI3K-axis discussion. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | 1 FFPE block or 10-20 unstained slides; archival acceptable |
| PTEN IHC (clone 138G6 or SP218) with positive internal control, scored as deficient if less than 10% tumor-cell staining at any intensity | Copy-number loss on NGS does not always translate to PTEN protein loss; PTEN is frequently inactivated by promoter methylation, frameshift, or LOH not picked up by panels with limited copy-number resolution. The FDA approval of capivasertib (CAPItello-291) and the F1CDx companion-diagnostic label define PTEN-altered on a DNA call, but the IHC re-stain with a less-than-10% cutoff is the orthogonal protein-level confirmation that pathologists and tumor boards expect before AKT-inhibitor discussion. Skipping it leaves the AKT-inhibitor rationale resting on a single copy-number signal without protein-level corroboration. | Mayo Clinic Laboratories *(PTEN Immunostain (technical component))* · [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 | 1 unstained slide from archival FFPE |
| TMB measurement on an FDA-cleared comprehensive genomic panel sized ≥0.8 Mb (FoundationOne CDx, MSK-IMPACT, or Tempus xT CDx), with the panel and threshold documented in the report | The tumor-agnostic pembrolizumab approval (KEYNOTE-158) is anchored on FoundationOne CDx as the companion diagnostic at a ≥10 mut/Mb cutoff, and TMB values are not interchangeable across panels: smaller or differently-bioinformatic panels can over- or under-call TMB by 3-5 mut/Mb at the clinically relevant threshold. A 14 mut/Mb value from a non-FDA-cleared assay near the 10 mut/Mb cutoff is exactly the situation where the call should be locked to a panel the FDA label recognizes before pembrolizumab is offered on a TMB-only basis. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | 1 FFPE block or 10-20 unstained slides; archival acceptable |
| PD-L1 IHC 22C3 pharmDx CPS on the breast primary block | In metastatic TNBC the pembrolizumab + chemotherapy label (KEYNOTE-355) requires PD-L1 CPS ≥10 by the 22C3 pharmDx companion diagnostic. PD-L1 expression in TNBC is discordant between primary breast and liver metastasis in roughly 20-30% of paired samples, so order on the breast primary; if only liver M1 is available, run on both and document the discordance rate. Skipping it means defaulting to PD-L1-agnostic backbones and missing the chance to anchor a CPS ≥10 case onto the pembrolizumab + chemo regimen. | Labcorp Oncology *(PD-L1 IHC 22C3 pharmDx (Dako/Agilent))* · [test info](https://oncology.labcorp.com/) · 358 South Main Street, Burlington, NC 27215 · 1-800-345-4363 | 1 FFPE block or 4-6 unstained slides |
| Germline BRCA1/2 sequencing plus del/dup on a hereditary breast/ovarian cancer panel covering PALB2, ATM, CHEK2, BARD1, RAD51C/D, BRIP1, TP53, PTEN, CDH1, STK11 | The tumor NGS call does not say whether the BRCA1 variant is germline or somatic, and the answer changes a 42-year-old patient's life: germline carriers face bilateral mastectomy and risk-reducing salpingo-oophorectomy decisions and trigger cascade testing of first-degree relatives, while purely somatic BRCA1 still supports PARP-inhibitor and platinum sensitivity but does not drive surgical or family-screening choices. NCCN BINV and genetic-familial breast guidelines mandate germline testing in any patient diagnosed under 50 or with TNBC regardless of age. | Labcorp Genetics (formerly Invitae) *(Invitae Hereditary Breast and Gyn Cancers Panel)* · [test info](https://www.invitae.com/providers/test-catalog/test-01202) · 1400 16th Street, San Francisco, CA 94103 · 1-800-436-3037 | 5-10 mL whole blood (EDTA) or saliva kit |
| HRD genomic-scar score (Myriad MyChoice CDx GIS or equivalent on FoundationOne CDx / Caris MI Profile) | An HRD score (LOH + telomeric allelic imbalance + large-scale state transitions) gives orthogonal proof that the BRCA1 variant is producing a functional HR-deficient phenotype, not just sitting at a permissive VAF. This matters most when the BRCA1 call sits in a domain whose functional consequence is debatable, or when later resistance lines need a baseline scar score to interpret BRCA reversion in ctDNA. The score does not gate PARP-inhibitor eligibility in BRCA1-mutated TNBC (that runs off the BRCA call itself), but it strengthens the platinum / PARPi rationale. | Myriad Genetics *(MyChoice CDx (HRD with Genomic Instability Score))* · [test info](https://myriad.com/oncology/mychoice-cdx/) · 320 Wakara Way, Salt Lake City, UT 84108 · 1-800-469-7423 | 1 FFPE block or 10-20 unstained slides |
| PAM50 intrinsic-subtype assay (NanoString Prosigna or Agendia BluePrint) with concurrent Lehmann TNBCtype-4 classification on RNA-seq | Roughly 25% of TNBCs do not classify as PAM50 basal-like, and within basal-like the Lehmann TNBCtype-4 subdivision carries divergent neoadjuvant pCR rates: BL1 about 52%, BL2 about 0%, LAR about 10%, M about 23% under anthracycline-taxane backbones. The current basal-like call should be locked to the assay that made it (PAM50 vs ad-hoc gene set), and the Lehmann layer adds therapeutic resolution that the basal-vs-non-basal binary cannot. | Veracyte *(Prosigna PAM50)* · [test info](https://www.veracyte.com/our-products/prosigna/) · 6000 Shoreline Court, Suite 300, South San Francisco, CA 94080 · 1-650-243-6300 | FFPE block or 10 unstained slides |
| Baseline ctDNA for BRCA1 reversion / secondary mutation surveillance | BRCA1/2 reversion mutations are detectable in ctDNA in roughly 60% of patients who progress on PARP inhibitors and are the single most common acquired-resistance mechanism in BRCA-mutated breast cancer. A baseline draw before any PARP-inhibitor or platinum exposure gives a clean reference for downstream resistance interpretation; serial draws after first progression let the team distinguish on-pathway resistance (reversion) from off-pathway escape. Without a baseline the reversion call becomes ambiguous when the patient later progresses on olaparib or talazoparib. | Guardant Health *(Guardant360 CDx)* · [test info](https://guardanthealth.com/products/guardant360/) · 505 Penobscot Drive, Redwood City, CA 94063 · 1-855-698-8887 | 5-10 mL plasma (Streck tube); Signatera also needs an FFPE block for assay design |
| ITWG stromal-TIL re-scoring on H and E by a dedicated breast pathologist (Salgado 2014 methodology) | The 3+ stromal-TIL label sits cleanly with the ITWG methodology only if it was scored as a continuous 0-100% percentage on a single H and E section by a pathologist trained on the Salgado 2014 guideline; ad-hoc 1+/2+/3+ grading is a known pitfall and inflates inter-observer variability. The re-score does not gate ICI eligibility but it is the reference standard the KEYNOTE-522 and ImPACT literature uses, and it makes the TIL signal defensible at tumor board. | Memorial Sloan Kettering Pathology Consultation Service · [test info](https://www.mskcc.org/clinical-services/pathology/consultation-services) · 1275 York Avenue, New York, NY 10065 · 1-212-639-5511 | 1 representative H and E slide; archival acceptable |
| MYC FISH (8q24 break-apart / amplification probe set) or MYC IHC (clone Y69) | MYC amplification by NGS copy-number is reasonably specific but the magnitude (low-level gain vs focal high-level amplification) varies by panel and tumor purity. FISH or IHC arbitrates this for the BET, CDK7, and CDK9 trial rationale, which generally favors high-level amplification or strong protein overexpression rather than borderline gain. The result refines trial eligibility for MYC-pathway protocols but does not gate any approved therapy. | NeoGenomics Laboratories *(MYC FISH)* · [test info](https://neogenomics.com/test-menu/myc-fish) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | 1 FFPE block or 4 unstained slides |
| B2M and HLA class I IHC plus B2M / HLA-A/B/C variant call review on tumor NGS | B2M loss and HLA class I antigen-presentation defects are well-characterized primary-resistance mechanisms for ICI in TMB-high and MSI-H tumors; loss of cell-surface MHC class I removes the substrate that PD-1 blockade depends on. In a TMB-14 / TIL-rich / MSS TNBC the ICI rationale is strong, but a B2M-deficient subclone would predict primary ICI failure even with the favorable TIL and TMB signals, and is detectable on the same FFPE block used for PD-L1 and TIL re-scoring. Cheap to add at the same time as the PD-L1 stain. | NeoGenomics Laboratories *(B2M IHC / HLA Class I IHC)* · [test info](https://neogenomics.com/) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | 1-2 unstained slides; can share the PD-L1 / TIL block |
| Comprehensive NGS review for replication-stress / DDR co-alterations (ATM, ATR, CHK1/2, CDK12, CCNE1 amplification) and TP53 variant-functional classification | TP53 mutation is near-universal in basal-like TNBC and not directly drug-gating, but it anchors the replication-stress phenotype that WEE1 inhibitors (adavosertib, debio-0123) and ATR inhibitors (ceralasertib, elimusertib) exploit. The actionability hinges on co-alterations: CCNE1 amplification, CDK12 loss, or ATM loss meaningfully shift the WEE1 / ATR rationale, and TP53 missense vs nonsense vs hotspot R175H / R248Q / R273H functional class also affects experimental-trial enrollment. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | shared with the PIK3CA / PTEN / TMB block |
| IRS2 RNA expression on tumor RNA-seq with reference to the TCGA TNBC distribution | IRS2 copy-number amplification only matters clinically if it translates to elevated IRS2 transcript and a functional IGF-1R / IRS signaling readout; many copy-number gains in TNBC do not. RNA-level confirmation is the cheapest way to triage whether IRS2 is worth chasing on an IGF-1R-axis trial versus parking it as a passenger event. Not gating any approved therapy; deferrable until an IGF-1R-axis protocol is on the table. | Tempus Labs *(Tempus xR (whole-transcriptome RNA-seq))* · [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 | FFPE block or 10 unstained slides; can bundle with the PAM50 / Lehmann RNA-seq order |

---

*Decision support, not medical advice. Confirm assay availability and current standards with the treating team and the local pathology service.*

<!-- libby:target-validation:end -->

## Scope summary

23 trials surfaced, 30 clinical-evidence rows (25 included + 5 logged as `considered_excluded` per the targetable-feature scope rule), 24 preclinical rows, and 13 target-validation rows (5 essential `gates_intervention`, 4 high-priority, 4 medium-priority). The ranked list contains 11 rows spanning agreement scores from 1.0 (rank 1 shared workup) down to -0.2 (rank 10 MEDIOLA-style maintenance, considered_with_caveats). All five personas converged on the workup; four of five endorsed olaparib at rank 2 (one dissent from risktaker on combination-strategy grounds); the conservative veto on rank 11 (ZEN-3694 triplet) is contingent on the absence of a published triplet safety dossier; two dissents on rank 10 (MEDIOLA) trigger `considered_with_caveats`; the rank-6 SBRT consolidation row sits at concensusite-vs-advocate/risktaker split on routine-off-trial-vs-protocol-enrollment.

## Cross-cutting caveat (read first)

**Multiple parallel biomarker gates make this a workup-first case, but the rank-2 BRCA1 anchor can start on germline confirmation alone — do not wait for CPS to begin therapy.** Three of the patient's six gating biomarkers are in flight: germline-vs-somatic BRCA1 (gates olaparib / talazoparib on the FDA breast label), PD-L1 CPS by 22C3 (gates KEYNOTE-355, ASCENT-04, TROPION-Breast05), and TMB platform confirmation on F1CDx (gates KEYNOTE-158, applicable in later lines only). NCCN v2.2026 is explicit that germline-BRCA-directed PARP-i can be initiated before PD-L1 testing resolves, so the workup gates the trial-slot conversation but not the systemic-therapy conversation entirely.

- **The ranking is targetable-feature-scoped.** Every recommendation acts on the patient's stated biomarker axes — BRCA1, basal-like subtype, TIL-rich / TMB-high, MYC amplification, oligometastatic state. Standard chemotherapy backbones that do not target a named feature (single-agent eribulin, capecitabine, vinorelbine) are NCCN-listed alternatives for 2L+ care that the treating team can pursue through normal care channels; they do not target any of this patient's stated features and are out of scope for Libby.

- **The oligometastatic-curative-intent layer (rank 6) is genuinely split among board members.** The advocate and risktaker placed SBRT on the MSK SABR protocol (NCT05534438) in their top 5 on the grounds that a solitary 1.5 cm liver lesion in a 42-year-old with BRCA1+ TNBC is the most consolidatable disease pattern she will ever present with. The concensusite ranked AGAINST routine early local therapy on the basis of E2108 (no OS benefit from intact-primary surgery in de novo M1) and NRG-BR002 phase IIR (PFS HR ~1.31 favored systemic-only). The synthesis honors that split: trial-protocol enrollment on NCT05534438 after documented systemic response is the consensus-aligned path; off-trial SBRT or hepatectomy on biology selection alone is what the negative parent trials argue against.

- **The conservative veto on rank 11 (ZEN-3694 + pembrolizumab + nab-paclitaxel triplet) is conditional and lifts on published triplet safety data.** Per Hard Rule 1, the row is carried through as `not_recommended` so the reader sees what was considered and rejected, with the explicit lift condition documented (dose-expansion safety with G-CSF primary prophylaxis and an irAE-management algorithm).

- **The PIK3CA gate is informational, not actionable in TNBC.** CAPItello-290 (capivasertib + paclitaxel, n=812) returned negative OS overall AND in the pre-specified AKT-pathway-altered stratum (HR 1.05) — exactly the subgroup this patient would have been routed to. EPIK-B3 (alpelisib + nab-paclitaxel) was terminated for slow recruitment and missed its primary ORR endpoint. Per the directive scope, the PI3K/AKT-axis drugs (alpelisib, inavolisib, capivasertib) are out of scope for this case and do not appear in the ranking.

- **Multiple co-occurring actionable features make this a strong trial-eligible profile and the patient's preference for trials is honored** — rank 5 (TROPION-Breast05) and rank 6 (NCT05534438) are the lead trial slots; the off-trial cat-1 picks at ranks 2 / 3 / 4 sit above them on board agreement, not on preference fit.

## Intervention grouping

- **PARP-class targeting BRCA1 mutation:** olaparib (OlympiAD, [PMID 28578601](https://pubmed.ncbi.nlm.nih.gov/28578601); OlympiA adjuvant, [PMID 34081848](https://pubmed.ncbi.nlm.nih.gov/34081848)); talazoparib (EMBRACA, [PMID 30110579](https://pubmed.ncbi.nlm.nih.gov/30110579)); somatic-BRCA Stanford trial ([NCT03990896](https://clinicaltrials.gov/study/NCT03990896)) for the somatic-only contingency.
- **ICI + chemo backbones targeting PD-L1 CPS / TILs / TMB axis:** pembrolizumab + carboplatin/gemcitabine (KEYNOTE-355, [PMID 33278935](https://pubmed.ncbi.nlm.nih.gov/33278935), [PMID 35857659](https://pubmed.ncbi.nlm.nih.gov/35857659)); sacituzumab govitecan + pembrolizumab (ASCENT-04 / KEYNOTE-D19, [NCT05382299](https://clinicaltrials.gov/study/NCT05382299)).
- **TROP2-ADC class targeting basal-like subtype:** sacituzumab govitecan monotherapy (ASCENT, [PMID 33882206](https://pubmed.ncbi.nlm.nih.gov/33882206), [PMID 38422473](https://pubmed.ncbi.nlm.nih.gov/38422473); ASCENT-03 1L extension); datopotamab deruxtecan ± durvalumab (TROPION-Breast05, [NCT06103864](https://clinicaltrials.gov/study/NCT06103864), [PMID 40297626](https://pubmed.ncbi.nlm.nih.gov/40297626); TROPION-Breast02 forward-cite anchor, [PMID 41937088](https://pubmed.ncbi.nlm.nih.gov/41937088)).
- **Platinum doublet targeting BRCA1 mutation:** carboplatin/gemcitabine (TNT, [PMID 29713086](https://pubmed.ncbi.nlm.nih.gov/29713086)).
- **Oligometastatic ablation targeting oligometastatic state:** SBRT on MSK SABR protocol ([NCT05534438](https://clinicaltrials.gov/study/NCT05534438), anchored against NRG-BR002 [PMID 33885704](https://pubmed.ncbi.nlm.nih.gov/33885704) and SABR-COMET [PMID 30982687](https://pubmed.ncbi.nlm.nih.gov/30982687)).
- **PARPi + ICI maintenance targeting BRCA1 + TIL-rich + TMB-high phenotype:** olaparib + durvalumab (MEDIOLA breast cohort, [PMID 32771088](https://pubmed.ncbi.nlm.nih.gov/32771088); DORA, [PMID 38236575](https://pubmed.ncbi.nlm.nih.gov/38236575); KEYLYNK-009, [PMID 41405563](https://pubmed.ncbi.nlm.nih.gov/41405563)); niraparib + pembrolizumab (TOPACIO, [PMID 31194225](https://pubmed.ncbi.nlm.nih.gov/31194225)) as the closest replication.
- **BET inhibitor + ICI + chemo triplet targeting MYC amplification:** ZEN-3694 + pembrolizumab + nab-paclitaxel ([NCT05422794](https://clinicaltrials.gov/study/NCT05422794)) — conservative veto.

## Top interventions

### Rank 1. Shared workup: germline BRCA1, PD-L1 CPS by 22C3, TMB on F1CDx, PIK3CA hotspot resolution, HER2 IHC 0 vs low, ITWG TIL re-score

*Workup gates the 1L conversation but does not block PARP-i: olaparib can start on germline confirmation before CPS returns per NCCN v2.2026.*

#### Evidence base

Six confirmatory tests, each anchored to a specific decision. **Germline BRCA1/2 panel** on a hereditary breast/ovarian panel covering PALB2, ATM, CHEK2, BARD1, RAD51C/D, BRIP1, TP53, PTEN, CDH1, STK11 ([PMID 33119881](https://pubmed.ncbi.nlm.nih.gov/33119881), NCCN v3.2025 genetic-familial breast guideline) — the result drives both the olaparib / talazoparib on-label decision (OlympiAD [PMID 28578601](https://pubmed.ncbi.nlm.nih.gov/28578601), EMBRACA [PMID 30110579](https://pubmed.ncbi.nlm.nih.gov/30110579)) and the risk-reducing surgery / cascade testing conversation for a 42-year-old. **PD-L1 22C3 pharmDx** on the breast primary block ([PMID 34626408](https://pubmed.ncbi.nlm.nih.gov/34626408), [PMID 31166680](https://pubmed.ncbi.nlm.nih.gov/31166680)) — the FDA companion diagnostic for KEYNOTE-355 CPS ≥10 and the ASCENT-04 enrollment threshold; primary-vs-liver-M1 discordance runs 20–30%, so the breast block is the right substrate. **TMB on F1CDx** ([PMID 32919526](https://pubmed.ncbi.nlm.nih.gov/32919526)) locks the 14 mut/Mb value to the panel the KEYNOTE-158 label recognizes — relevant for later lines, since the tumor-agnostic indication requires ≥1 prior line. **ITWG TIL re-score** ([PMID 25214542](https://pubmed.ncbi.nlm.nih.gov/25214542), [PMID 32195312](https://pubmed.ncbi.nlm.nih.gov/32195312)) hardens the '3+ stromal TILs' call to the percentage-scale methodology that ICI literature uses. **HER2 IHC 0 vs 1+/2+ FISH-** gates trastuzumab deruxtecan (DESTINY-Breast04/06) eligibility for later lines if reflex confirms HER2-low. **PIK3CA hotspot resolution** ([PMID 31091374](https://pubmed.ncbi.nlm.nih.gov/31091374)) is informational in TNBC — CAPItello-290 and EPIK-B3 read negative or terminated, so the hotspot call clarifies pathway biology rather than unlocking an active recommendation here.

#### Likelihood of desired effect

Diagnostic certainty across six dimensions. The result branching:
- **Germline BRCA1 positive → rank 2 olaparib / rank 9 talazoparib unlocked on FDA label.**
- **Germline BRCA1 negative (somatic-only) → rank 2 collapses to off-label use or routes the patient to the Stanford talazoparib trial NCT03990896 (n=13 interim, single-arm).**
- **22C3 CPS ≥10 → rank 3 KN-355, rank 5 TROPION-Breast05, rank 7 SG + pembro on the table.**
- **22C3 CPS <10 → rank 8 SG monotherapy (ASCENT-03 NCCN cat-1 preferred) and rank 4 carbo/gem inherit the slot; CPS-low TROPION-Breast02 and TroFuse-011 lanes also open.**

#### Toxicity profile

- None. Peripheral blood draw (germline) plus archival FFPE pulls for IHC and NGS reflexes.
- Decision-tree risk only: discordant results between assays (e.g. CPS discordance breast-vs-liver, TMB panel cross-platform) require a tie-breaker decision rather than a re-stain.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. No persona dissented or vetoed the workup itself; the workup is the precondition for the disagreements that follow at ranks 2–11.

#### Practical considerations

Order the germline panel (turnaround 2–3 weeks), 22C3 CPS (5–7 days), F1CDx TMB (chart-review check if the existing 14 mut/Mb value already came from F1CDx; new send-out 2–4 weeks otherwise), HER2 IHC reflex (5 days), ITWG TIL re-score (1–2 weeks), and PIK3CA hotspot annotation (chart-review check if the codon is already named in the NGS report). The germline panel pairs with a cancer-genetics counseling visit so cascade testing of siblings and first-degree relatives can be triggered the same week the variant is classified. The PD-L1 CPS goes on the breast primary block per 22C3 companion-diagnostic instructions; if only liver M1 is available, run both and note the discordance rate in the report.

#### Why this rank

Rank 1 because every downstream therapeutic decision branches on at least one of these results, and the workup is non-toxic, low-cost, and parallelizable. Concensusite is explicit that olaparib can start on a germline-positive result without waiting for CPS — the workup gates the trial-slot conversation, not the systemic-therapy conversation entirely. Agreement score 1.0 is the maximum on the ranking.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Germline BRCA1/2 + HBOC panel (Invitae / Myriad MyRisk / GeneDx / Ambry CancerNext) | Gates olaparib / talazoparib FDA label; informs risk-reducing surgery and cascade testing | None — peripheral blood draw | [PMID 33119881](https://pubmed.ncbi.nlm.nih.gov/33119881), [NCT02000622](https://clinicaltrials.gov/study/NCT02000622), [NCT01945775](https://clinicaltrials.gov/study/NCT01945775) |
| PD-L1 22C3 pharmDx on breast primary FFPE (Labcorp / Quest / NeoGenomics / Mayo) | Gates KEYNOTE-355 + ASCENT-04 + TROPION-Breast05 (CPS ≥10) | None — archival FFPE pull | [PMID 34626408](https://pubmed.ncbi.nlm.nih.gov/34626408), [PMID 31166680](https://pubmed.ncbi.nlm.nih.gov/31166680) |
| TMB on F1CDx (Foundation Medicine; Tempus xT CDx / MSK-IMPACT as alternates) | Confirms 14 mut/Mb on the KEYNOTE-158 label panel | None — archival FFPE pull | [PMID 32919526](https://pubmed.ncbi.nlm.nih.gov/32919526), [NCT02628067](https://clinicaltrials.gov/study/NCT02628067) |
| HER2 IHC 0 vs 1+/2+ FISH- reflex (institutional pathology) | Gates trastuzumab deruxtecan (DESTINY-Breast04/06) for later lines if HER2-low | None — archival FFPE re-stain | DESTINY-Breast04 ([PMID 35665782](https://pubmed.ncbi.nlm.nih.gov/35665782)) |
| ITWG stromal TIL re-score (MSK / DFCI / MDACC / Mayo pathology consult) | Hardens the 3+ TIL call on the ITWG percentage-scale methodology | None — H&E review | [PMID 25214542](https://pubmed.ncbi.nlm.nih.gov/25214542), [PMID 32195312](https://pubmed.ncbi.nlm.nih.gov/32195312) |
| PIK3CA hotspot annotation (chart-review of existing NGS; F1CDx reflex if not done) | Informational in TNBC — CAPItello-290 / EPIK-B3 are negative or terminated | None — chart review | [PMID 31091374](https://pubmed.ncbi.nlm.nih.gov/31091374), [PMID 35613031](https://pubmed.ncbi.nlm.nih.gov/35613031) |

---

### Rank 2. Olaparib 300 mg PO BID (OlympiAD)

*Conditional on germline_brca:positive. Foreclosed if germline BRCA1 is negative (somatic-only) — the row collapses to off-label use or routes the patient to the Stanford talazoparib trial NCT03990896.*

#### Evidence base

OlympiAD ([PMID 28578601](https://pubmed.ncbi.nlm.nih.gov/28578601), [NCT02000622](https://clinicaltrials.gov/study/NCT02000622), n=302, germline BRCA1/2 HER2-negative mBC including TNBC and HR+, up to 2 prior chemo lines) hit PFS HR 0.58 (95% CI 0.43–0.80, p<0.001) on BICR-adjudicated primary endpoint; median PFS 7.0 vs 4.2 months on physician's-choice chemo; ORR 59.9% vs 28.8%. Replicated by EMBRACA ([PMID 30110579](https://pubmed.ncbi.nlm.nih.gov/30110579), n=431, talazoparib) at PFS HR 0.54 (95% CI 0.41–0.71). OlympiA ([PMID 34081848](https://pubmed.ncbi.nlm.nih.gov/34081848), n=1836, adjuvant) extends the package into curative settings at iDFS HR 0.58 and OS HR 0.68 — the only PARP-i with a curative-setting OS hit, which strengthens the precedent for post-consolidation maintenance if the rank-6 liver-lesion ablation is pursued. RoB 2 low across all OlympiAD / EMBRACA domains; open-label trials with BICR-adjudicated PFS as the mitigation.

#### Likelihood of desired effect

High in germline BRCA1 HER2-negative mBC, conditional on the germline gate opening. The patient is treatment-naive, ECOG 1, with no prior chemo — squarely inside the OlympiAD enrolled population, and the BRCA1 status is the load-bearing predictor for which the trials were designed. Olaparib's OS HR in OlympiAD did not reach formal significance at the registrational analysis (HR 0.90, 95% CI 0.66–1.23), but the OlympiA adjuvant OS HR 0.68 extends the survival case in the curative setting. If germline BRCA1 returns negative (somatic-only), the patient falls outside the OlympiAD / EMBRACA label population and the row's expected value drops to the small-n Stanford somatic trial signal (ORR ~38% in n=13 interim, [NCT03990896](https://clinicaltrials.gov/study/NCT03990896)).

#### Toxicity profile

- G3+ anemia 16.1% (vs **39%** on talazoparib in EMBRACA — the cleanest single-agent hematologic profile on the ranking and the load-bearing reason olaparib leads talazoparib on this axis)
- G3+ neutropenia 9.3%
- All-grade nausea 58%, fatigue 28.8%
- Treatment-related AE discontinuation 4.9% — the lowest among single-agent options
- MDS/AML risk 1–2% on cumulative PARP-i exposure (pooled OlympiAD / OlympiA dataset); baseline and serial CBC monitoring per FDA label
- User has no toxicity vetoes; the hematologic and GI profile fits inside the consent envelope

#### Counter-productive mechanisms / dissent

Four-persona endorsement (advocate, conservative, critic, concensusite). The critic ranked olaparib at #1 on evidence-quality grounds: two independent registrational phase 3 trials replicating the same biomarker-defined effect, RoB 2 low across all domains, replicated synthetic-lethality preclinical anchor (Bryant 2005, Farmer 2005). The concensusite ranked it at #1 on guideline anchor: NCCN v2.2026 cat-1 preferred 1L, ESMO MCBS v1.1 score 4 [I, A], can be started without waiting for PD-L1 testing. The conservative ranked it at #2 on the cleanest tolerability margin in the dossier.

The risktaker filed three dissent critiques across round 2 (against advocate's, critic's, and concensusite's olaparib placements) on the grounds that 'single-agent PARP-i collapses BRCA1 + TP53 + PTEN-loss + MYC-amp + TIL-3+ + TMB-14 down to one axis' and pushed for a chemo-free PARP-i + ICI combination (rank 10 MEDIOLA-style maintenance) instead. That dissent is preserved on this row — the multi-hit phenotype argument has merit, but the combination evidence stack (single-arm MEDIOLA + post-hoc TOPACIO BRCA-mut subset + negative-overall KEYLYNK-009) does not displace the cat-1 monotherapy anchor.

The advocate's round-2 dissent on the critic's olaparib rank-1 was a preference-fit critique about ranking olaparib above the trial-preferred TROPION-Breast05 — that's a rank-ordering disagreement, not a drug-level dissent. The advocate themselves ranked olaparib at #3, so endorsement stands.

#### Practical considerations

- FDA-approved on-label in this indication since January 2018; immediately prescribable on germline confirmation
- Trial enrollment for the somatic-BRCA contingency: [NCT03990896](https://clinicaltrials.gov/study/NCT03990896) (Stanford / Telli lab, recruiting; interim n=13 ORR ~38%)
- Baseline ctDNA draw before olaparib start (target-validation row brca-reversion-ctdna-baseline) seeds reversion surveillance — BRCA1 reversion is the dominant acquired-resistance mechanism on PARP-i exposure ([PMID 38302062](https://pubmed.ncbi.nlm.nih.gov/38302062))
- Sequencing question: olaparib as 1L systemic backbone vs as maintenance after a platinum-containing induction (DORA / MEDIOLA template). The dossier supports either; the rank-10 row carries the combination-maintenance alternative
- HRD genomic-scar score (Myriad MyChoice CDx GIS) is a high-priority orthogonal validation step but does not gate eligibility (target-validation row hrd-genomic-scar-score)

#### Why this rank

Rank 2 only because rank 1 is the workup that gates whether the germline label applies. On therapeutic merit this is the strongest evidence-quality + guideline-fit anchor in the dossier: two registrational phase 3 replications, NCCN cat-1 preferred, OS hit in the adjuvant setting, lowest discontinuation rate on the ranking. The 0.4-point agreement-score gap above rank 5 (TROPION-Breast05) reflects four-persona convergence here vs two-persona convergence there.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Olaparib 300 mg PO BID — OlympiAD ([NCT02000622](https://clinicaltrials.gov/study/NCT02000622)) 1L–3L germline BRCA1/2 HER2- mBC | PFS HR 0.58 (CI 0.43–0.80); mPFS 7.0 vs 4.2 mo; ORR 59.9% vs 28.8% | G3+ TRAE 36.6%; G3+ anemia 16%; G3+ neutropenia 9%; AE discontinuation 4.9% | [PMID 28578601](https://pubmed.ncbi.nlm.nih.gov/28578601) |
| Olaparib 300 mg PO BID — OlympiA adjuvant ([PMID 34081848](https://pubmed.ncbi.nlm.nih.gov/34081848)) | iDFS HR 0.58 (CI 0.46–0.74); 3-yr iDFS 85.9% vs 77.1%; OS HR 0.68 (p=0.009) | G3+ TRAE 24.5%; G3+ anemia 8.7%; MDS/AML 0.2% (no excess) | [PMID 34081848](https://pubmed.ncbi.nlm.nih.gov/34081848) |
| Talazoparib 1 mg PO daily — somatic-BRCA Stanford ([NCT03990896](https://clinicaltrials.gov/study/NCT03990896)) — contingency if germline BRCA1 negative | ORR ~38% in interim n=13 (single-arm) | Hematologic per EMBRACA profile | [NCT03990896](https://clinicaltrials.gov/study/NCT03990896) |

---

### Rank 3. Pembrolizumab 200 mg q3w + carboplatin AUC2 / gemcitabine 1000 mg/m² d1,8 q21d (KEYNOTE-355)

*Conditional on 22C3 CPS ≥10. CPS <10 closes this regimen and routes the patient to rank 8 (SG monotherapy ASCENT-03) or rank 4 (carbo/gem alone).*

#### Evidence base

KEYNOTE-355 ([PMID 33278935](https://pubmed.ncbi.nlm.nih.gov/33278935), [NCT02819518](https://clinicaltrials.gov/study/NCT02819518), n=847, 1L mTNBC): PFS HR 0.65 (95% CI 0.49–0.86, p=0.0012) in the CPS ≥10 stratum at primary readout; final OS HR 0.73 (95% CI 0.55–0.95, p=0.0185) at 44-month median follow-up, median OS 23.0 vs 16.1 months ([PMID 35857659](https://pubmed.ncbi.nlm.nih.gov/35857659)) — a 7-month median OS gain. The label and the data both track CPS ≥10; the CPS <10 subset showed no benefit. KEYNOTE-522 ([PMID 32101663](https://pubmed.ncbi.nlm.nih.gov/32101663), neoadjuvant) replicates the direction of effect in early-stage TNBC. The carboplatin/gemcitabine flavor of the chemo backbone doubles as BRCA1-directed cytotoxicity per the TNT BRCA-mut subgroup signal ([PMID 29713086](https://pubmed.ncbi.nlm.nih.gov/29713086)). RoB 2 low across all KEYNOTE-355 domains. IMpassion130 atezolizumab + nab-paclitaxel was the original 1L ICI + chemo signal but the indication was withdrawn in 2021 after IMpassion131 ([PMID 34219000](https://pubmed.ncbi.nlm.nih.gov/34219000)) failed to confirm with paclitaxel solvent — pembrolizumab + chemo is the active US 1L ICI backbone.

#### Likelihood of desired effect

High in CPS ≥10 1L mTNBC. The 7-month median OS gain is the defining survival signal in the dossier. The TIL-3+ / TMB-14 phenotype is the subset that retrospectively benefits most in KEYNOTE-522 — that biomarker enrichment is consistent with KEYNOTE-355 expectations even though KN-355 was not powered on TILs or TMB. If 22C3 CPS returns <10, the regimen is closed; the critic's round-2 caveat is explicit that TILs and TMB are not substitutes for CPS in the KEYNOTE-355 label (the KEYNOTE-158 TMB-H basket requires ≥1 prior line and excluded breast cancer from the original cohorts, so it cannot bridge the 1L CPS-low gap).

#### Toxicity profile

- G3+ TRAE 68.1% (vs 66.9% on placebo + chemo — the chemo backbone drives most of the burden)
- G3+ neutropenia ~41% on the carbo/gem backbone; manageable with G-CSF per ASCO 2015 guidance
- G3+ immune-mediated AEs 5.3% (hypothyroidism, hepatitis, pneumonitis at single-digit rates each)
- Treatment-related deaths 0.4% at final analysis
- ICI-related hypothyroidism ~15% any-grade — the irAE class with the longest tail; codified ASCO/SITC management algorithm applies
- ILD / pneumonitis surveillance via baseline PFTs and HRCT recommended

#### Counter-productive mechanisms / dissent

Four-persona endorsement (advocate, conservative, critic, concensusite). Conservative ranked it at #1 on the deepest 1L safety dossier; critic at #2 on phase 3 evidence quality; advocate at #2 honoring efficacy lean and TIL-rich phenotype; concensusite at #3 after the NCCN v2.2026 elevation of SG + pembro (rank 7) to the cat-1 preferred slot — KN-355 is now the alternative cat-1 backbone.

Risktaker dissented on preference fit (round 2 critique against conservative's rank 1): off-trial KN-355 is the same regimen as the TROPION-Breast05 control arm (rank 5), so prescribing it off-trial wastes a trial-slot opportunity for a patient with prefers_trials=true. The synthesis preserves that dissent and surfaces TROPION-Breast05 at rank 5 as the trial-preferred path to access the same regimen with a 50% shot at the experimental arm. Critic's round-2 qualified critique (against conservative's rank 1) was a rank-ordering note: olaparib's two-trial replication beats KN-355's single-trial-plus-CPS-gate evidence package when both apply.

#### Practical considerations

- FDA-approved on-label since 2020 for PD-L1 CPS ≥10 1L mTNBC
- Carboplatin/gemcitabine is the preferred chemo backbone here over nab-paclitaxel for the TNT-class BRCA1 platinum sensitivity signal
- Pembrolizumab + chemo can be initiated while waiting for germline BRCA1 to resolve — if germline confirms, the team can pivot to olaparib monotherapy or layer olaparib maintenance per the KEYLYNK-009 design (overall negative; BRCA1/2-mut subgroup HR ~0.70 not powered, [PMID 41405563](https://pubmed.ncbi.nlm.nih.gov/41405563))
- B2M / HLA class I IHC baseline (target-validation row b2m-hla-ici-resistance-baseline) refines the primary-ICI-resistance risk; informative, not gating

#### Why this rank

Rank 3 because the four-persona convergence on phase 3 OS + cat-1 guideline + mature six-year irAE-management algorithm matches the rank-2 olaparib agreement-score (0.6) but the CPS-gating dependency makes it more provisional than the germline-BRCA1 anchor. The 0.4-point gap above rank 5 (TROPION-Breast05) reflects four-persona vs two-persona convergence, not effect-size difference.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Pembrolizumab 200 mg q3w + carbo/gem — KEYNOTE-355 ([NCT02819518](https://clinicaltrials.gov/study/NCT02819518)) CPS ≥10 1L mTNBC | PFS HR 0.65 (CPS ≥10); OS HR 0.73; mOS 23.0 vs 16.1 mo | G3+ TRAE 68%; G3+ neutropenia 41%; irAE G3+ 5.3%; TRAE death 0.4% | [PMID 33278935](https://pubmed.ncbi.nlm.nih.gov/33278935), [PMID 35857659](https://pubmed.ncbi.nlm.nih.gov/35857659) |
| Pembrolizumab + chemo neoadjuvant — KEYNOTE-522 ([NCT03036488](https://clinicaltrials.gov/study/NCT03036488)) | pCR 64.8% vs 51.2%; EFS HR 0.63 (TIL-rich enrichment retrospective) | G3+ TRAE 78%; irAE G3+ 14% | [PMID 32101663](https://pubmed.ncbi.nlm.nih.gov/32101663) |
| Atezolizumab + nab-paclitaxel — IMpassion130 ([PMID 30345906](https://pubmed.ncbi.nlm.nih.gov/30345906)) — historical, withdrawn in US | PFS HR 0.62 (PD-L1 IC ≥1%) — but IMpassion131 negative on paclitaxel solvent triggered withdrawal | — | [PMID 30345906](https://pubmed.ncbi.nlm.nih.gov/30345906), [PMID 34219000](https://pubmed.ncbi.nlm.nih.gov/34219000) |

---

### Rank 4. Carboplatin AUC2 + gemcitabine 1000 mg/m² d1,8 q21d

*PD-L1-agnostic BRCA1-directed backbone; the CPS-low fallback if the rank-3 / rank-5 / rank-7 ICI lanes close.*

#### Evidence base

TNT ([PMID 29713086](https://pubmed.ncbi.nlm.nih.gov/29713086), [NCT00532727], n=376) is the phase 3 platinum-vs-taxane RCT in unselected advanced TNBC. The pre-specified BRCA1/2 subgroup (n=43) returned ORR 68% on carboplatin vs 33% on docetaxel, with biomarker × treatment interaction p=0.01 and PFS HR 0.44 — the foundational platinum-sensitivity data in BRCA1-mut TNBC. CALGB 40603 ([PMID 25092775](https://pubmed.ncbi.nlm.nih.gov/25092775)) and BrighTNess long-term follow-up ([PMID 35093516](https://pubmed.ncbi.nlm.nih.gov/35093516)) confirm carboplatin drives the pCR / EFS gain in the neoadjuvant setting — not veliparib, which failed to add benefit over carboplatin alone in BrighTNess Arm A vs B. Veliparib + carbo + paclitaxel in BROCADE3 (germline BRCA mBC, [PMID 32861273](https://pubmed.ncbi.nlm.nih.gov/32861273)) hit PFS HR 0.71 but no OS benefit, and veliparib was never FDA-approved in breast cancer — the BRCA1-mut platinum effect dominates the combination signal. The critic is straight: TNT BRCA-mut PFS HR 0.59 sits in a pre-specified n=43 subgroup with wide CIs, so this is class evidence plus three decades of post-marketing carbo/gem experience, not a registrational 1L anchor.

#### Likelihood of desired effect

Moderate to High in BRCA1-mut TNBC. The TNT ORR 68% in n=43 is the strongest indication-specific platinum-sensitivity signal anywhere, and the BrighTNess long-term follow-up confirms the platinum component drives the durability gain. The CI width on the n=43 subgroup is the load-bearing caveat — this is class evidence with a small subset anchor, not a registrational primary-endpoint hit.

#### Toxicity profile

- G3+ neutropenia 30–40% (driven by gemcitabine d1,8 dosing); G-CSF and dose holds per ASCO 2015
- G3+ thrombocytopenia ~15%
- Cumulative platinum nephrotoxicity rare with carboplatin; baseline creatinine clearance documentation
- Predictable AE profile after three decades of post-marketing experience — no novel safety signals

#### Counter-productive mechanisms / dissent

Three-persona endorsement (conservative #3, critic #4, concensusite #4). Concensusite filed a round-2 qualified critique against the critic's rank-4 positioning: NCCN v2.2026 elevated SG monotherapy (rank 8) to category 1 preferred for CPS <10 / ICI-ineligible mTNBC on ASCENT-03, including BRCA-mutated patients, which now sits above platinum doublets in the CPS-low stack. Carbo/gem remains a defensible category 2A backbone but is no longer the unambiguous CPS-low lead. No persona dissented or vetoed the regimen itself.

#### Practical considerations

- Off-trial FDA-approved standard chemotherapy; immediately prescribable
- Most experienced 1L backbone with the cleanest BRCA1 mechanistic fit
- Layers cleanly with rank 6 SBRT consolidation after documented response — the longest-experience platinum doublet for a converted-disease strategy
- Sequencing: carbo/gem followed by olaparib maintenance is an off-trial regimen that parallels the DORA / MEDIOLA template (pmid:38236575, pmid:32771088) — not a labeled sequence, defensible mechanism
- If the team prefers the BROCADE3 framework, veliparib + carbo + paclitaxel is not commercially available (veliparib was never approved) so the practical regimen is carbo/gem alone or carbo + paclitaxel

#### Why this rank

Rank 4 on the same agreement-score (0.6) as ranks 2 and 3, broken on preference fit: the rank-2 olaparib row hits the BRCA1 anchor on the strongest evidence package and the rank-3 KN-355 hits the OS-curve signal in CPS ≥10. Carbo/gem is the safe-haven for the contingencies. After the Feb-2026 NCCN update elevating SG monotherapy in CPS-low, carbo/gem's CPS-low lead is no longer unambiguous; it stays in the ranking for the platinum-sensitivity argument and consolidation-pairing fit.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Carboplatin AUC2 + gemcitabine d1,8 q21d — class evidence + TNT BRCA-mut subgroup | TNT BRCA-mut ORR 68% vs 33% docetaxel; PFS HR 0.44 (n=43, p=0.01) | G3+ neutropenia 30–40%; G3+ thrombocytopenia ~15% | [PMID 29713086](https://pubmed.ncbi.nlm.nih.gov/29713086) |
| Carboplatin neoadjuvant — CALGB 40603 ([PMID 25092775](https://pubmed.ncbi.nlm.nih.gov/25092775)); BrighTNess 4-yr follow-up ([PMID 35093516](https://pubmed.ncbi.nlm.nih.gov/35093516)) | pCR 60% (carbo) vs 44%; EFS HR 0.63 (carbo+pacli vs pacli alone) | G3+ neutropenia 22%; G3+ thrombocytopenia 19% | [PMID 25092775](https://pubmed.ncbi.nlm.nih.gov/25092775), [PMID 35093516](https://pubmed.ncbi.nlm.nih.gov/35093516) |
| Veliparib + carbo + paclitaxel — BROCADE3 ([NCT02163694]) — historical, drug not commercially available | PFS HR 0.71; no OS benefit; mPFS 14.5 vs 12.6 mo | G3+ neutropenia 81%; G3+ thrombocytopenia 40% | [PMID 32861273](https://pubmed.ncbi.nlm.nih.gov/32861273) |

---

### Rank 5. Datopotamab deruxtecan ± durvalumab on TROPION-Breast05 (NCT06103864)

*Conditional on 22C3 CPS ≥10. Forward-cite anchor is TROPION-Breast02 (CPS <10) — cross-trial extrapolation, not a within-trial estimate. CPS <10 closes Breast05 and routes the patient to TROPION-Breast02 (NCT05374512) or TroFuse-011 (NCT06841354).*

#### Evidence base

[TROPION-Breast05](https://clinicaltrials.gov/study/NCT06103864) is the actively recruiting 1L phase 3 (n=1075 target) testing Dato-DXd ± durvalumab against the KEYNOTE-355 chemo + pembrolizumab backbone in PD-L1 CPS ≥10 mTNBC ([PMID 40297626](https://pubmed.ncbi.nlm.nih.gov/40297626)). The forward-cite anchor is TROPION-Breast02 ([PMID 41937088](https://pubmed.ncbi.nlm.nih.gov/41937088), n=644, CPS <10 / ICI-ineligible vs investigator's-choice chemo): PFS HR 0.57 (95% CI 0.44–0.73, p<0.0001), median PFS 10.8 vs 5.6 months. The mechanism — TROP2-directed deruxtecan payload — directly targets the basal-like subtype call. The critic's round-2 caveat is the load-bearing tension: PFS HR 0.57 from Breast02 (CPS <10 vs chemo) is being extrapolated forward to Breast05 (CPS ≥10 vs pembro + chemo), with a different population and a different comparator — no Breast05 primary readout has landed.

#### Likelihood of desired effect

Moderate, with the honest framing 'mechanistically aligned phase 3 slot with no primary readout in hand.' The cross-trial extrapolation from Breast02 PFS HR 0.57 is a forward bet, not an effect estimate. The randomization risk is symmetric: 50% probability of drawing the experimental Dato-DXd ± durvalumab arm vs 50% of drawing the KEYNOTE-355 chemo + pembrolizumab control — and the control arm is the same regimen the patient would receive at rank 3 off-trial. If she draws the control arm she gets standard of care; if she draws the experimental arm she gets the trial bet. The downside is bounded; the upside is the registrational TROP2-ADC + ICI signal.

#### Toxicity profile

- Dato-DXd G3+ stomatitis ~6%; ocular events (keratitis); G3+ TRAE ~35% — fewer hematologic events than the chemo control arm
- **ILD / pneumonitis ~3% any-grade, ~2% G3+ — characteristic deruxtecan-payload AE; baseline HRCT, PFTs, and documented ILD-management algorithm before cycle 1 per conservative's round-2 caveat**
- Durvalumab adds pneumonitis ~3–5% any-grade — overlapping pulmonary-tox stack with Dato-DXd warrants active surveillance
- No dedicated TROPION-Breast05 combination safety readout yet; the AE algorithms are inferred from cumulative Dato-DXd + ICI experience

#### Counter-productive mechanisms / dissent

Two-persona endorsement (advocate #1, risktaker #1). The critic, conservative, and concensusite each filed round-2 qualified critiques rather than endorsing or dissenting. Critic's qualified critique on evidence quality: Breast02 PFS HR 0.57 is cross-trial extrapolation, not a Breast05 readout — the honest framing matters. Conservative's qualified critique on toxicity: the overlapping pulmonary-tox stack needs baseline HRCT / PFTs and an ILD-management algorithm before cycle 1. Concensusite's qualified critique on guideline fit: TROPION-Breast05 is not a guideline-endorsed regimen, NCCN v2.2026 lists Dato-DXd + ICI nowhere as a 1L option — the trial-slot framing is fine, the 'highest expected value' framing conflates open phase 3 slot with guideline endorsement.

No persona dissented or vetoed the row outright; all three caveats are operational rather than rank-blocking.

#### Practical considerations

- Trial actively recruiting at academic centers; site logistics may demote the row if the patient is not near an enrolling site (preference file does not capture geography)
- Eligibility gated on PD-L1 CPS ≥10 by 22C3 (rank-1 workup)
- If CPS returns <10, the trial-slot routing pivots to TROPION-Breast02 ([NCT05374512](https://clinicaltrials.gov/study/NCT05374512), active not recruiting) or TroFuse-011 ([NCT06841354](https://clinicaltrials.gov/study/NCT06841354), sacituzumab tirumotecan ± pembro, recruiting)
- Pre-cycle-1 workup: baseline HRCT, PFTs, ocular surveillance plan per Dato-DXd label
- The trial enrollment slot complements rather than substitutes for the rank-2 olaparib decision — if germline BRCA1 confirms, the patient can take olaparib monotherapy as 1L, OR enroll on Breast05 and use olaparib as maintenance or 2L. Both options remain on the table

#### Why this rank

Rank 5 because the two-persona convergence (advocate, risktaker) sits below the four-persona convergence at ranks 2 / 3 / 4 — but the trial-preference fit and the curative-intent framing make this the strongest trial slot in the dossier on preference grounds. The 0.2-point agreement-score gap below rank 4 (carbo/gem) is real but the preference-weighted ordering tilts in this row's favor for any patient who prioritizes trial enrollment.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Dato-DXd 6 mg/kg q3w ± durvalumab 1120 mg q3w — TROPION-Breast05 ([NCT06103864](https://clinicaltrials.gov/study/NCT06103864)) CPS ≥10 1L mTNBC | Readout pending; forward-cite Breast02 PFS HR 0.57 (CI 0.44–0.73) | Stomatitis G3+ 6%; ILD ~3%; G3+ TRAE ~35% | [PMID 40297626](https://pubmed.ncbi.nlm.nih.gov/40297626), [NCT06103864](https://clinicaltrials.gov/study/NCT06103864) |
| Dato-DXd monotherapy — TROPION-Breast02 ([NCT05374512](https://clinicaltrials.gov/study/NCT05374512)) CPS <10 1L mTNBC — CPS-low fallback | PFS HR 0.57 (CI 0.44–0.73, p<0.0001); mPFS 10.8 vs 5.6 mo | Same Dato-DXd AE profile | [PMID 41937088](https://pubmed.ncbi.nlm.nih.gov/41937088) |
| Sacituzumab tirumotecan ± pembrolizumab — TroFuse-011 ([NCT06841354](https://clinicaltrials.gov/study/NCT06841354)) CPS <10 — alternate TROP2-ADC | Readout pending | TROP2-ADC class effects | [NCT06841354](https://clinicaltrials.gov/study/NCT06841354) |

---

### Rank 6. SBRT to the solitary 1.5 cm hepatic lesion on the MSK SABR protocol (NCT05534438)

*Conditional consolidation layer — layered on systemic response, not a substitute for systemic therapy. The board is genuinely split: trial enrollment is the consensus-aligned path; off-trial SBRT on biology selection is what the negative parent trials argue against.*

#### Evidence base

The patient has a single 1.5 cm liver lesion in de novo M1 BRCA1-mut TNBC — biologically the most consolidatable disease pattern she will ever present with. SABR-COMET ([PMID 30982687](https://pubmed.ncbi.nlm.nih.gov/30982687), n=99, mixed histologies, 18% breast) hit OS HR 0.57 (95% CI 0.30–1.10, p=0.090) with median OS 41 vs 28 months — encouraging but not statistically significant, with **3 treatment-related deaths in the SBRT arm (4.5%)** vs none in control. NRG-BR002 ([PMID 33885704](https://pubmed.ncbi.nlm.nih.gov/33885704), breast-specific n=125): phase IIR PFS HR ~1.31 favored systemic-only — the breast-specific randomized signal is against routine consolidation. E2108 ([PMID 34995128](https://pubmed.ncbi.nlm.nih.gov/34995128), n=256): no OS benefit from resecting an intact primary in de novo M1 (HR 1.11, 90% CI 0.82–1.52), and worse health-related QoL at 18 months. [NCT05534438](https://clinicaltrials.gov/study/NCT05534438) is the actively recruiting MSK SABR consolidation phase 2 for de novo oligometastatic and oligoprogressive breast / other solid tumors.

#### Likelihood of desired effect

Low to Moderate for OS in breast-specific oligometastatic disease at the population level — NRG-BR002 phase IIR PFS HR ~1.31 favors the systemic-only arm, and SABR-COMET's encouraging signal was not statistically significant. The risktaker's biology-selection argument is the counter-case: NRG-BR002 enrolled all subtypes and any-site oligomets, and a BRCA1-mutated TNBC patient with a solitary liver lesion on documented systemic response is a subset the trial was not powered to detect benefit in. That argument is post-hoc, not randomized.

#### Toxicity profile

- SBRT G≥2 AE rate 29% (SABR-COMET)
- **3 treatment-related deaths in the SBRT arm of SABR-COMET (4.5%)** — non-trivial signal for any oligometastatic ablation discussion
- Requires 12-week systemic response confirmation before SBRT; multidisciplinary IR/radiation-oncology coordination
- The MSK protocol does the SBRT under registered slot with documented response gating — the cleanest way to pursue the curative-intent layer

#### Counter-productive mechanisms / dissent

Two-persona endorsement (advocate #4, risktaker #3) with concensusite as one explicit dissent. Concensusite's rank-5 was a recommendation AGAINST routine early local therapy — but their own rationale acknowledges that NCT05534438 trial enrollment is the consensus-aligned route if consolidation is pursued ('on a trial, after systemic response, not as primary therapy'). The dissent is preserved on this row, framed as: off-trial SBRT or hepatectomy is what concensusite reads as outside the guideline-endorsed population; trial enrollment is the consensus path.

Advocate's round-2 dissent on concensusite's rank-5 ('this pick recommends against the exact intervention the preference file's free-text was written to enable') is preserved on this row. Risktaker's round-2 critique on concensusite framed similarly. The synthesis tags this row as `considered_with_caveats` because two personas (advocate, risktaker) endorse and one (concensusite) dissents on the off-trial framing — net agreement +1 on the trial-protocol path.

Critic and conservative did not surface SBRT in their picks (no endorsement, no dissent).

#### Practical considerations

- Trial open at [NCT05534438](https://clinicaltrials.gov/study/NCT05534438) (recruiting)
- Layered on top of (not instead of) the rank-2 to rank-5 systemic backbone; SBRT timing is post-12-week response assessment
- Multidisciplinary slot needed (IR or radiation oncology, medical oncology, breast surgery)
- Post-consolidation maintenance question: olaparib (OlympiA precedent, [PMID 34081848](https://pubmed.ncbi.nlm.nih.gov/34081848)) is the natural choice if the patient is on PARP-i at the time of SBRT; sequence-of-care varies by 1L choice and is a tumor-board call
- E2108 / NRG-BR002 are the consensus-against anchors for off-trial consolidation — the team should be honest with the patient that the randomized evidence on this question is negative at the population level and the case rests on biology selection

#### Why this rank

Rank 6 because the agreement-score (0.4) sits below the four-persona converges at ranks 2 / 3 / 4 and ties with rank 5 — but the curative-intent framing in the preference file makes this the load-bearing conversation for any 42-year-old with a solitary liver lesion in de novo M1 TNBC. The cross-cutting caveat preserves the honest acknowledgment that NRG-BR002 is negative; rank 6 is the trial-protocol path that honors the preference file without overriding the negative parent-trial signal.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| SBRT per lesion-specific RTOG / AAPM guidelines on systemic therapy — MSK SABR consolidation ([NCT05534438](https://clinicaltrials.gov/study/NCT05534438)) | Readout pending; phase 2 design | SBRT G≥2 AE expected ~29% | [NCT05534438](https://clinicaltrials.gov/study/NCT05534438) |
| SBRT for mixed-histology oligomets — SABR-COMET ([PMID 30982687](https://pubmed.ncbi.nlm.nih.gov/30982687)) | OS HR 0.57 (CI 0.30–1.10, p=0.090); mOS 41 vs 28 mo | G≥2 AE 29%; **TRAE deaths 4.5%** | [PMID 30982687](https://pubmed.ncbi.nlm.nih.gov/30982687) |
| SBRT or surgery for breast oligomets — NRG-BR002 ([PMID 33885704](https://pubmed.ncbi.nlm.nih.gov/33885704)) | phase IIR PFS HR ~1.31 favors systemic-only; 3-yr PFS no different | G3+ TRAE ~12%; no excess high-grade | [PMID 33885704](https://pubmed.ncbi.nlm.nih.gov/33885704) |
| Intact primary resection in de novo M1 — E2108 ([PMID 34995128](https://pubmed.ncbi.nlm.nih.gov/34995128)) | OS HR 1.11; no benefit; worse QoL at 18 mo | Surgical AE ~15% | [PMID 34995128](https://pubmed.ncbi.nlm.nih.gov/34995128) |

---

### Rank 7. Sacituzumab govitecan 10 mg/kg d1,8 q21d + pembrolizumab 200 mg q3w (ASCENT-04 / KEYNOTE-D19)

*Conditional on 22C3 CPS ≥10. NCCN v2.2026 cat-1 preferred for CPS ≥10 1L mTNBC, elevated above KEYNOTE-355 on the ASCENT-04 readout — but only one persona surfaced this in their top picks, reflecting the freshness of the elevation.*

#### Evidence base

ASCENT-04 / KEYNOTE-D19 ([NCT05382299](https://clinicaltrials.gov/study/NCT05382299), n=443, PD-L1 CPS ≥10 1L mTNBC including BRCA-mut and -WT, conference-data baseline pending peer-reviewed primary publication): PFS HR 0.65 (95% CI 0.51–0.84, p<0.001); median PFS 11.2 vs 7.8 months; median DoR 16.5 vs 9.2 months. OS still immature at the primary PFS readout. The 2L+ ASCENT backbone ([PMID 33882206](https://pubmed.ncbi.nlm.nih.gov/33882206), final analysis [PMID 38422473](https://pubmed.ncbi.nlm.nih.gov/38422473)) returned PFS HR 0.41 and final OS HR 0.51 — the most mature TROP2-ADC monotherapy efficacy in the dossier. NCCN Breast Cancer v2.2026 (Feb 27 2026 update) elevated SG + pembro to category 1 preferred 1L for CPS ≥10 mTNBC on the basis of the ASCENT-04 PFS plus quality-of-life data.

#### Likelihood of desired effect

High in CPS ≥10 1L mTNBC: the PFS HR 0.65 plus DoR gain (16.5 vs 9.2 months) is consistent with the KEYNOTE-355 effect size on PFS and durability. OS is still immature — the next decision-relevant pivot for whether SG + pembro stays above KN-355 in the consensus stack.

#### Toxicity profile

- G3+ neutropenia ~50% on the SG arm; primary G-CSF prophylaxis recommended per the SG label
- G3+ diarrhea ~10% from the SN-38 payload (loperamide algorithm)
- Pembrolizumab adds irAE pneumonitis ~3%, colitis ~2%, hypothyroidism ~15%
- G3+ febrile neutropenia ~6% in the cumulative SG dataset
- Treatment-related deaths reported in the cumulative SG dataset at 0.4%
- UGT1A1*28 genotype check recommended for febrile-neutropenia risk stratification

#### Counter-productive mechanisms / dissent

One-persona endorsement (concensusite #2). Conservative qualified on toxicity (G3+ neutropenia ~50% plus irAE stack needs explicit G-CSF + irAE-surveillance preconditions). Critic qualified on evidence quality (peer-reviewed primary publication pending, OS immature). Advocate and risktaker did not surface SG + pembro in their picks — they ranked SG-class options lower because the conservative reserved SG for 2L per the older ASCENT label and the freshness of the NCCN elevation had not propagated to the round-1 picks.

No persona dissented or vetoed. The 0.2 agreement-score reflects single-persona endorsement, not clinical dissent — the row is `recommended` on the NCCN cat-1 anchor.

#### Practical considerations

- ASCENT-04 itself is closed to enrollment; the regimen is now NCCN cat-1 preferred and immediately prescribable for CPS ≥10 1L mTNBC
- Pre-cycle-1 setup: G-CSF primary prophylaxis, UGT1A1*28 genotype check, irAE-surveillance plan
- Sequence question after SG + pembro: olaparib (germline BRCA1), Dato-DXd (TROP2 class continued), or platinum doublet are the natural 2L choices

#### Why this rank

Rank 7 only because the board did not converge on it in round 1 — the single-persona endorsement gives this row a 0.2 agreement-score even though the NCCN cat-1 elevation puts it above KEYNOTE-355 in the post-Feb-2026 sequence. The 0.4-point gap below rank 4 reflects the round-1 picks predating the NCCN update; the gap above rank 8 (SG monotherapy) reflects the same single-persona endorsement.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| SG 10 mg/kg d1,8 q21d + pembrolizumab 200 mg q3w — ASCENT-04 ([NCT05382299](https://clinicaltrials.gov/study/NCT05382299)) CPS ≥10 1L mTNBC | PFS HR 0.65; mPFS 11.2 vs 7.8 mo; DoR 16.5 vs 9.2 mo; OS immature | G3+ neutropenia ~50%; diarrhea G3+ 10%; irAE ~25% any | ASCENT-04 ([NCT05382299](https://clinicaltrials.gov/study/NCT05382299)) |
| SG monotherapy — ASCENT 2L+ ([PMID 33882206](https://pubmed.ncbi.nlm.nih.gov/33882206), [PMID 38422473](https://pubmed.ncbi.nlm.nih.gov/38422473)) — backbone effect anchor | PFS HR 0.41; final OS HR 0.51; mOS 11.8 vs 6.9 mo | G3+ neutropenia 51%; febrile neutropenia 6% | [PMID 33882206](https://pubmed.ncbi.nlm.nih.gov/33882206), [PMID 38422473](https://pubmed.ncbi.nlm.nih.gov/38422473) |

---

### Rank 8. Sacituzumab govitecan 10 mg/kg d1,8 q21d monotherapy (ASCENT-03 1L CPS-low / ICI-ineligible)

*Conditional on 22C3 CPS <10 (or ICI ineligibility). NCCN v2.2026 cat-1 preferred 1L for CPS-low mTNBC including BRCA-mutated patients — displaces carbo/gem (rank 4) as the lead CPS-low backbone in the post-Feb-2026 consensus stack.*

#### Evidence base

The 2L+ ASCENT pivotal ([PMID 33882206](https://pubmed.ncbi.nlm.nih.gov/33882206), final analysis [PMID 38422473](https://pubmed.ncbi.nlm.nih.gov/38422473), n=529): PFS HR 0.41 (95% CI 0.32–0.52, p<0.001), median PFS 5.6 vs 1.7 months; final OS HR 0.51, median OS 11.8 vs 6.9 months — the most mature TROP2-ADC monotherapy evidence base. ASCENT-03 is the 1L extension that informed the NCCN v2.2026 cat-1 preferred elevation for CPS <10 / ICI-ineligible mTNBC including BRCA-mutated patients (concensusite's round-2 critique 15 is the dossier reference; the peer-reviewed primary publication is pending). RoB 2 low across the 2L+ ASCENT domains.

#### Likelihood of desired effect

High at 2L+ on the mature ASCENT data (OS HR 0.51, 5-month median OS gain). The 1L extension via ASCENT-03 informs the NCCN cat-1 preferred elevation but the peer-reviewed primary readout is pending — the effect size at 1L is the load-bearing claim. Among CPS-low BRCA1-mut TNBC patients, ASCENT-03 enrolled BRCA-mutated patients explicitly, so the BRCA1 status does not park the patient outside the SG monotherapy population (concensusite's framing).

#### Toxicity profile

- G3+ neutropenia ~51% (primary G-CSF prophylaxis per label)
- G3+ diarrhea ~10%; G3+ febrile neutropenia ~6%
- Treatment-related death rate 0.4% in cumulative SG dataset
- UGT1A1*28 homozygotes carry higher febrile-neutropenia risk

#### Counter-productive mechanisms / dissent

One-persona endorsement (concensusite, surfaced in round 2 critique). Conservative kept SG 'in reserve for 2L per ASCENT label' at their rank 4 — they did not surface the 1L extension, so the endorsement counts at the conservative's 2L positioning rather than the 1L. Critic, advocate, and risktaker did not surface SG monotherapy in their picks. No persona dissented or vetoed. The 0.2 agreement-score reflects single-persona endorsement on the freshness of the NCCN elevation, not clinical dissent.

#### Practical considerations

- FDA-approved on-label in 2L+ mTNBC since 2020; ASCENT-03 1L NCCN cat-1 preferred elevation is the active-channel anchor
- Pre-cycle-1: G-CSF primary prophylaxis, UGT1A1*28 genotype check
- After SG monotherapy progression: PARP-i (germline BRCA1), Dato-DXd (TROP2-class continued), or platinum doublet are the natural 2L choices

#### Why this rank

Rank 8 ties with rank 7 (SG + pembro) on agreement-score and on single-persona endorsement; rank 7 sits above because it applies in the CPS ≥10 case and rank 8 applies in CPS <10. Both rest on the same NCCN cat-1 sequence; the case-by-case branching depends on the rank-1 CPS read. The 0.2 gap above rank 9 (talazoparib) reflects different patient populations (CPS-low vs germline-BRCA-confirmed); rank 8 is broader, rank 9 is more specific.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| SG monotherapy — ASCENT 2L+ pivotal ([NCT02574455](https://clinicaltrials.gov/study/NCT02574455)) | PFS HR 0.41; OS HR 0.51 (final); mOS 11.8 vs 6.9 mo | G3+ neutropenia 51%; diarrhea G3+ 10%; febrile neutropenia 6% | [PMID 33882206](https://pubmed.ncbi.nlm.nih.gov/33882206), [PMID 38422473](https://pubmed.ncbi.nlm.nih.gov/38422473) |
| SG monotherapy — ASCENT-03 1L NCCN cat-1 preferred for CPS <10 / ICI-ineligible | NCCN v2.2026 elevation; primary readout pending peer-reviewed publication | Same SG class profile | NCCN Breast Cancer v2.2026 |

---

### Rank 9. Talazoparib 1 mg PO daily (EMBRACA)

*Conditional on germline_brca:positive. Evidence-quality parity with olaparib (rank 2); hematologic compression is the binding differentiator. Foreclosed if germline BRCA1 is negative — the somatic-BRCA Stanford trial NCT03990896 is the off-label substitute.*

#### Evidence base

EMBRACA ([PMID 30110579](https://pubmed.ncbi.nlm.nih.gov/30110579), [NCT01945775](https://clinicaltrials.gov/study/NCT01945775), n=431, germline BRCA1/2 HER2-negative mBC, up to 3 prior chemo lines): PFS HR 0.54 (95% CI 0.41–0.71, p<0.001), median PFS 8.6 vs 5.6 months; ORR 62.6% vs 27.2%. OS HR 0.76 (95% CI 0.55–1.06, p=0.11) — not significantly improved at the primary OS analysis with 57% events. RoB 2 low across all domains. Open-label with BICR-adjudicated PFS as the mitigation. Evidence-quality parity with OlympiAD on the same biomarker-defined population.

#### Likelihood of desired effect

High in germline BRCA1 HER2-negative mBC, on parity with olaparib at rank 2. The differentiator is hematologic compression: EMBRACA reported dose reductions in 53% and transfusion in ~38% of patients, vs 25% and ~17% on OlympiAD per the conservative's round-2 caveat — material dose-intensity loss over the 12–18 month treatment horizon for a 42-year-old on long-haul therapy.

#### Toxicity profile

- **G3+ anemia 39% (vs 16% on olaparib — the binding differentiator)**
- G3+ neutropenia 21%; G3+ thrombocytopenia 15%
- All-grade fatigue 50.3%
- Treatment-related AE discontinuation 7.7%
- Same MDS/AML class signal as olaparib at 1–2% on cumulative PARP-i exposure
- Conservative's round-2 critique on talazoparib emphasizes the dose-intensity compression: 53% dose reductions and 38% transfusion materially affect the duration the patient can stay on therapy

#### Counter-productive mechanisms / dissent

One-persona endorsement (critic #3). Conservative qualified on toxicity (round-2 critique 6: 'keep talazoparib as the contingency if olaparib intolerance emerges, not at rank parity'). Critic's own framing in round 1 was 'evidence-quality at parity with pick 1 [olaparib]' — they ranked talazoparib below olaparib explicitly on tolerability. No persona dissented or vetoed.

#### Practical considerations

- Same germline-vs-somatic BRCA1 gate as olaparib; somatic-only routes to [NCT03990896](https://clinicaltrials.gov/study/NCT03990896) (Stanford / Telli, n=13 interim ORR ~38%)
- Hematologic optimization before starting full dose; consider starting at reduced dose for patients with marginal baseline hemoglobin
- The critic's framing is honest: this is the contingency if olaparib intolerance emerges, not the parity choice — both drugs are NCCN cat-1 preferred, the choice rests on tolerability

#### Why this rank

Rank 9 because the board's consensus is that olaparib (rank 2) leads talazoparib on hematologic tolerability while the two are at parity on efficacy. The 0.4-point agreement-score gap below rank 2 reflects single-persona endorsement here vs four-persona convergence there — the same drug class, the same biomarker-defined indication, ranked separately because the synthesis preserves the olaparib-first ordering.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Talazoparib 1 mg PO daily — EMBRACA ([NCT01945775](https://clinicaltrials.gov/study/NCT01945775)) germline BRCA1/2 HER2- mBC | PFS HR 0.54 (CI 0.41–0.71); mPFS 8.6 vs 5.6 mo; ORR 62.6% vs 27.2% | G3+ anemia 39%; neutropenia 21%; thrombocytopenia 15%; dose reductions 53% | [PMID 30110579](https://pubmed.ncbi.nlm.nih.gov/30110579) |
| Talazoparib 1 mg PO daily — Stanford somatic-BRCA ([NCT03990896](https://clinicaltrials.gov/study/NCT03990896)) — for somatic-only contingency | ORR ~38% in interim n=13 (single-arm) | Same talazoparib hematologic profile | [NCT03990896](https://clinicaltrials.gov/study/NCT03990896) |

---

### Rank 10. Olaparib 300 mg PO BID + durvalumab 1500 mg q4w as MEDIOLA-style maintenance after platinum + pembrolizumab induction

*Status: considered_with_caveats. Two dissents (critic, concensusite) on a non-veto option. The canonical-responder phenotype argument is mechanistically clean; the evidence stack is single-arm + subset, and no actively recruiting registered slot exists for this 1L US TNBC switch.*

#### Evidence base

MEDIOLA breast cohort ([PMID 32771088](https://pubmed.ncbi.nlm.nih.gov/32771088), n=34, single-arm, germline BRCA1/2 HER2-neg mBC): DCR 80% at 12 weeks (95% CI 64–91%), ORR 63%, median PFS 8.2 months. TOPACIO / KEYNOTE-162 ([PMID 31194225](https://pubmed.ncbi.nlm.nih.gov/31194225), n=55 single-arm advanced TNBC including BRCA-mut and -WT): ORR 21% all-comers, **47% in the BRCA-mut subset (n=15)**. DORA ([PMID 38236575](https://pubmed.ncbi.nlm.nih.gov/38236575), n=45 randomized phase 2 maintenance after platinum induction): 12-month PFS 35.7% (olaparib + durvalumab combo) vs 11.8% (olaparib alone). KEYLYNK-009 ([PMID 41405563](https://pubmed.ncbi.nlm.nih.gov/41405563), n=271 randomized phase 2/3 maintenance after pembro + chemo induction): overall PFS HR 0.98 (95% CI 0.72–1.33, p=0.46) — **negative on the primary endpoint**; BRCA1/2-mut subgroup PFS HR 0.70 (95% CI 0.33–1.48, crosses 1, not powered).

#### Likelihood of desired effect

Moderate in BRCA1 + ICI-favorable phenotype — and the canonical-responder argument is mechanistically real: BRCA1 + TIL-rich + TMB-high + APOBEC-flavored is the phenotype where MEDIOLA delivered ORR 63%, TOPACIO 47% in the BRCA-mut TNBC subset, and KEYLYNK-009's BRCA1/2-mut subgroup signaled PFS HR ~0.70. The critic's load-bearing dissent is that none of these are RCT-grade in this exact patient population: MEDIOLA is single-arm n=34, TOPACIO is a post-hoc subset of n=15, KEYLYNK-009 was negative overall and the BRCA-mut subgroup CI crosses 1.

#### Toxicity profile

- MEDIOLA G3+ AE rate 32% (11/34); G3+ anemia 12%, G3+ neutropenia 9%, G3+ pancreatitis 6%; 3 discontinuations for AE in n=34
- TOPACIO G3+ anemia 18%, G3+ thrombocytopenia 15%, G3 irAE 4%
- DORA: nausea, fatigue, anemia dominant; G3-4 events scattered (<5% per term) — chemo-free maintenance is well-tolerated relative to continued chemo
- KEYLYNK-009: pembro + olaparib G3+ TRAE 84% vs pembro + chemo 96% — combo regimen better tolerated than continued chemo

#### Counter-productive mechanisms / dissent

One-persona endorsement (risktaker #2). Two dissents:
- **Critic dissent (evidence quality):** 'subset-of-subset stack of single-arm signals layered on a negative randomized parent trial, not three independent replications; the rank-2 position misreads the evidence weight.'
- **Concensusite dissent (guideline fit):** 'NCCN v2.2026 plus ESMO ABC guidance both list germline-BRCA-directed PARPi monotherapy as category 1 preferred 1L for this patient, not PARPi + ICI combination. KEYLYNK-009 negative-overall with a CI-crossing-1 BRCA subgroup is exactly the data the consensus seat reads as not enough to displace the category 1 monotherapy. There is no actively recruiting registered slot for the MEDIOLA-style switch in 1L US TNBC.'

Advocate qualified on preference fit ('off-label single-arm n=34 dressed up as a registrational option, and prefers_trials=true wants an actually-enrolling slot') — not a full dissent.

Two dissents on a non-veto option triggers `considered_with_caveats` per Hard Rule 3. The row stays in the ranking because the canonical-responder phenotype argument is mechanistically clean and the post-induction maintenance template is a defensible tumor-board discussion, but it does not displace the rank-2 olaparib monotherapy anchor.

#### Practical considerations

- No actively recruiting US 1L TNBC trial for the MEDIOLA-style switch; off-label use requires payer pushback management
- Sequencing: pembrolizumab + carbo/gem induction (rank 3, 4–6 cycles) then switch to olaparib + durvalumab maintenance; the closest published template is KEYLYNK-009 (negative overall) and DORA (n=45 randomized phase 2 with combo PFS gain)
- Baseline ctDNA before olaparib start (target-validation row brca-reversion-ctdna-baseline) seeds reversion surveillance
- Alternative: olaparib monotherapy maintenance after platinum-containing induction is on better-evidenced ground than the combination — KEYLYNK-009 + DORA both inform the maintenance question but neither closes it cleanly

#### Why this rank

Rank 10 below the recommended set because two dissents (critic, concensusite) on the evidence + guideline-fit axes outweigh the single-persona endorsement, even though no veto was issued. The row is retained for tumor-board discussion of post-induction maintenance — particularly if the team pursues a platinum-containing 1L induction and wants a chemo-free maintenance layer for a young patient with curative-intent framing.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Olaparib + durvalumab — MEDIOLA breast cohort ([NCT02734004](https://clinicaltrials.gov/study/NCT02734004)) germline BRCA1/2 HER2- mBC | DCR 80%; ORR 63%; mPFS 8.2 mo (n=34 single-arm) | G3+ TRAE 32%; anemia 12%; neutropenia 9% | [PMID 32771088](https://pubmed.ncbi.nlm.nih.gov/32771088) |
| Niraparib + pembrolizumab — TOPACIO / KEYNOTE-162 ([NCT02657889](https://clinicaltrials.gov/study/NCT02657889)) advanced TNBC | ORR 21% all-comers; 47% BRCA-mut (n=15 subset, single-arm) | G3+ anemia 18%; thrombocytopenia 15%; irAE 15% any | [PMID 31194225](https://pubmed.ncbi.nlm.nih.gov/31194225) |
| Olaparib ± durvalumab maintenance — DORA ([NCT03167619]) platinum-pretreated mTNBC | 12-mo PFS 35.7% (combo) vs 11.8% (olaparib alone), n=45 randomized phase 2 | Nausea, fatigue, anemia; G3+ <5% per term | [PMID 38236575](https://pubmed.ncbi.nlm.nih.gov/38236575) |
| Pembrolizumab + olaparib maintenance after pembro + chemo — KEYLYNK-009 ([NCT04191135](https://clinicaltrials.gov/study/NCT04191135)) | Overall PFS HR 0.98 (negative); BRCA-mut subgroup PFS HR 0.70 (CI 0.33–1.48) | G3+ TRAE 84% vs 96% chemo arm; anemia 25% on olaparib arm | [PMID 41405563](https://pubmed.ncbi.nlm.nih.gov/41405563) |

---

## Classes examined but not ranked

The board surfaced several feature-targeting options that did not make the recommended list and are documented here for transparency.

- **Atezolizumab + nab-paclitaxel (IMpassion130, [PMID 30345906](https://pubmed.ncbi.nlm.nih.gov/30345906))** — original 1L ICI + chemo approval in PD-L1 SP142 IC ≥1% mTNBC, voluntarily withdrawn from the US market in 2021 after IMpassion131 ([PMID 34219000](https://pubmed.ncbi.nlm.nih.gov/34219000)) failed to confirm benefit with paclitaxel solvent. Patient cannot access this regimen in the US; the active equivalent is the rank-3 KEYNOTE-355 backbone.
- **Niraparib monotherapy (BRAVO, [PMID 34301749](https://pubmed.ncbi.nlm.nih.gov/34301749))** — halted for futility on central review (PFS HR 0.96 central vs HR 0.65 local); not FDA-approved in breast cancer; payer pushback likely vs labeled olaparib or talazoparib. Excluded from the ranking on negative-readout grounds.
- **Olaparib + ceralasertib (ATR-i) on a VIOLETTE-style protocol** — VIOLETTE ([NCT03330847](https://clinicaltrials.gov/study/NCT03330847)) was negative on the primary PFS endpoint (BRCA-mut HR ~0.81 not significant); risktaker's rank-5 pick rests on speculative successor protocols, and no active US successor trial is documented in the dossier. The mechanistic rationale (BRCA1 + TP53 + PTEN replication-stress triad, preclinical synergy [PMID 35046096](https://pubmed.ncbi.nlm.nih.gov/35046096)) is real; the operational path is not.
- **Adavosertib (WEE1 inhibitor) + cisplatin (DFCI-Tolaney, [PMID 33257427](https://pubmed.ncbi.nlm.nih.gov/33257427))** — missed the pre-specified 30% ORR threshold in mTNBC (ORR 26%, 13–44% CI); no genomic correlate including TP53 predicted response. Tempers the WEE1-inhibitor rationale for TP53-mut TNBC; remains experimental, no active US trial path for this combination.
- **Samuraciclib (CDK7 inhibitor)** — abstract-only data in TNBC; no peer-reviewed publication. The MYC-amp mechanistic rationale is hypothesis-generating only.
- **ZEN-3694 + talazoparib (NCT03901469)** — BRCA-WT-restricted enrollment; patient is BRCA1-mut so the trial does not apply. The companion BET-i triplet is at rank 11 with conservative veto.

The PI3K/AKT-axis drugs (alpelisib, inavolisib, capivasertib) are out of scope per the cross-cutting caveat and the user directive: CAPItello-290 returned negative OS overall and in the AKT-pathway-altered stratum that would have been this patient's most likely benefit subgroup ([PMID-pending, doi:10.1016/j.annonc.2025.10.025]); EPIK-B3 was terminated for slow recruitment and missed primary ORR. These drugs do not appear in the ranking.

## Ranked prioritization

**Workup (gates the ranked therapeutic options):**

| Rank | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
|---|---|---|---|---|---|
| 1 | **Shared workup: germline BRCA1, PD-L1 CPS 22C3, TMB on F1CDx, PIK3CA hotspot, HER2 IHC 0/low, ITWG TIL re-score**<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-risktaker">risktaker</span></small> | Diagnostic certainty. Gates olaparib (rank 2) on germline; gates ICI + chemo / TROP2-ADC + ICI rows on CPS ≥10; gates KEYNOTE-158 TMB-H on F1CDx. | Low (none — diagnostic test on tissue + blood) | <strong>N/A</strong> (Workup row — no therapeutic mechanism.) | **The 1L conversation depends on six results; order them in parallel and start olaparib on a germline-positive return without waiting for CPS.** |

**Ranked therapeutic options:**

| Rank | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
|---|---|---|---|---|---|
| 2 | **Olaparib 300 mg PO BID (OlympiAD)** *(conditional on germline_brca positive)*<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>dissent:</em> <span class="persona persona-risktaker">risktaker</span></small> | High in germline BRCA1 HER2-neg mBC: PFS HR 0.58 (OlympiAD) replicated by HR 0.54 (EMBRACA, talazoparib). | Low (G3+ anemia 16%, neutropenia 9%, fatigue, nausea) | <strong>Low</strong> (BRCA1 reversion / RAD51 fork-protection rescue is the dominant on-pathway escape; baseline ctDNA seeds reversion surveillance.) | **Two independent phase 3 anchors, lowest discontinuation rate on the ranking, oral single-agent — the cat-1 BRCA1 anchor that earns rank 2 in any synthesis that respects guideline fit and evidence replication.** |
| 3 | **Pembrolizumab 200 mg q3w + carboplatin/gemcitabine (KEYNOTE-355)**<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small><br><small><em>dissent:</em> <span class="persona persona-risktaker">risktaker</span></small> | High in CPS ≥10 1L mTNBC: PFS HR 0.65 (mPFS 9.7 vs 5.6 mo) plus OS HR 0.73 (mOS 23.0 vs 16.1 mo) at final analysis. | High (G3+ neutropenia 41%, irAE 5%, treatment-related death 0.4%) | <strong>Low</strong> (T-cell exhaustion / B2M-HLA antigen-presentation loss is the canonical primary-ICI-resistance route; rank-1 workup includes baseline B2M/HLA IHC.) | **The defining 1L mTNBC survival regimen at CPS ≥10 (OS HR 0.73, 7-mo median gain); now the alternative cat-1 backbone after SG + pembro took the preferred slot.** |
| 4 | **Carboplatin AUC2 + gemcitabine d1,8 q21d**<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small> | Moderate to High in BRCA1-mut TNBC: TNT BRCA-mut subgroup ORR 68% vs 33% docetaxel (n=43, p=0.01). | Moderate (G3+ neutropenia 30–40%, thrombocytopenia ~15%) | <strong>Low</strong> (BRCA1 reversion under platinum pressure mirrors the PARP-i resistance route; serial ctDNA at progression resolves intra-pathway vs off-pathway escape.) | **The PD-L1-agnostic BRCA1-directed backbone; rests on a small TNT subgroup (n=43) plus three decades of carbo/gem experience; sits below SG monotherapy in the post-Feb-2026 NCCN CPS-low stack but pairs more cleanly with later consolidation.** |
| 5 | **Datopotamab deruxtecan ± durvalumab on TROPION-Breast05 (NCT06103864)**<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-risktaker">risktaker</span></small> | Moderate (cross-trial extrapolation, not a within-trial estimate): TROPION-Breast02 PFS HR 0.57 in CPS <10 / ICI-ineligible 1L; Breast05 readout pending. | Moderate (G3+ stomatitis 6%, ILD ~3%, ocular events; G3+ TRAE 35%) | <strong>Moderate</strong> (Overlapping pulmonary toxicity from Dato-DXd payload + durvalumab pneumonitis; baseline HRCT/PFTs mitigate but no combination safety dossier yet.) | **The trial-preference-anchored 1L slot — randomized against KN-355 with a 50% shot at TROP2-ADC + ICI; effect size still a forward bet on cross-trial extrapolation.** |
| 6 | **SBRT to solitary hepatic lesion on MSK SABR protocol (NCT05534438)** *(considered_with_caveats)*<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-risktaker">risktaker</span></small><br><small><em>dissent:</em> <span class="persona persona-concensusite">concensusite</span></small> | Low to Moderate for OS in breast-specific oligometastatic disease (NRG-BR002 phase IIR PFS HR ~1.31 favors systemic-only); biology-selection argument for this patient is post-hoc. | Moderate (SBRT G≥2 AE 29%; 4.5% treatment-related deaths in SABR-COMET) | <strong>Moderate</strong> (Treatment-related deaths in SABR-COMET 4.5% and negative NRG-BR002 phase IIR PFS are the load-bearing concerns against routine off-trial consolidation.) | **The curative-intent layer the preference file was written to enable; honest about NRG-BR002 negative, anchored on NCT05534438 trial enrollment after documented systemic response.** |
| 7 | **Sacituzumab govitecan + pembrolizumab (ASCENT-04 / KEYNOTE-D19)**<br><small><em>endorse:</em> <span class="persona persona-concensusite">concensusite</span></small> | High in CPS ≥10 1L mTNBC: PFS HR 0.65 (mPFS 11.2 vs 7.8 mo); OS still immature. | High (G3+ neutropenia ~50%, diarrhea 10%, irAE ~25% any-grade) | <strong>Low</strong> (Same T-cell exhaustion / antigen-presentation loss concerns as KN-355; rank-1 B2M/HLA workup applies.) | **NCCN v2.2026 cat-1 preferred for CPS ≥10 over KN-355 on PFS HR 0.65 and DoR 16.5 mo; rank pulled down by single-persona endorsement reflecting fresh elevation and immature OS rather than clinical dissent.** |
| 8 | **Sacituzumab govitecan monotherapy (ASCENT-03 CPS-low / ICI-ineligible)**<br><small><em>endorse:</em> <span class="persona persona-concensusite">concensusite</span></small> | High in CPS <10 / ICI-ineligible 1L mTNBC (ASCENT-03 NCCN cat-1 elevation); replicated by ASCENT 2L+ OS HR 0.51. | High (G3+ neutropenia 51%, diarrhea 10%, febrile neutropenia 6%, treatment-related death 0.4%) | <strong>Low</strong> (TROP2-ADC mechanism — payload-driven cytotoxicity; no mechanism-level counter-productive vector specific to BRCA1+ TNBC.) | **NCCN v2.2026 cat-1 preferred 1L for CPS <10 / ICI-ineligible; the CPS-low fallback that displaces carbo/gem in the post-Feb-2026 consensus stack.** |
| 9 | **Talazoparib 1 mg PO daily (EMBRACA)** *(conditional on germline_brca positive)*<br><small><em>endorse:</em> <span class="persona persona-critic">critic</span></small> | High in germline BRCA1 HER2-neg mBC: PFS HR 0.54 (EMBRACA); evidence-quality parity with olaparib, tolerability is the binding differentiator. | Moderate (G3+ anemia 39%, neutropenia 21%, thrombocytopenia 15%; dose reductions 53%) | <strong>Low</strong> (Same BRCA1 reversion route as olaparib; hematologic compression more often forces dose reduction than off-pathway escape.) | **Evidence-quality parity with olaparib (PFS HR 0.54) but G3+ anemia 39% vs 16% — the contingency if olaparib intolerance emerges, not the parity choice.** |
| 10 | **Olaparib + durvalumab MEDIOLA-style maintenance after platinum + pembro induction** *(considered_with_caveats)*<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span></small><br><small><em>dissent:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small> | Moderate in BRCA1 + ICI-favorable phenotype (MEDIOLA ORR 63%, n=34); evidence is single-arm + subset, not RCT-grade. | Low (G3+ anemia 12%, neutropenia 9%, pancreatitis 6%) | <strong>Moderate</strong> (Critic dissented on the subset-of-subset evidence stack; concensusite dissented on guideline-fit — no registered 1L slot.) | **The chemo-free PARPi + ICI maintenance bet on the canonical-responder phenotype; held back by single-arm evidence stack and guideline-fit gap, retained for tumor-board discussion of post-induction maintenance.** |
| 11 | **ZEN-3694 + pembrolizumab + nab-paclitaxel (NCT05422794)** *(not_recommended — conservative veto)*<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-risktaker">risktaker</span></small><br><small><em>veto:</em> <span class="persona persona-conservative">conservative</span></small> | Low for characterized efficacy (phase 1b dose-finding, no readout); class extrapolation from MYC-amp / BET-i mechanism only. | High (BET-i thrombocytopenia 20–30%, nab-paclitaxel neutropenia 30%, pembrolizumab irAE — uncharacterized triplet) | <strong>High</strong> (Conservative veto on toxicity-as-mechanism grounds: three independent myelosuppressive mechanisms with no characterized triplet AE algorithm.) | **Conservative veto on cumulative toxicity without a triplet safety dossier; mechanism is aligned with the patient's MYC-amp / basal / TIL-rich axis but evidence is too thin to act on.** |

!!! info "Reading the table"

    **Toxicity burden** is patient-level AE severity (the G3+ rates the patient will experience). **Counter-productive MoA** is mechanism-level risk to the therapeutic goal — distinct from patient AEs. The persona pills under each intervention show the at-a-glance board signal; full per-persona rationale lives on the [board page](board.md).

## Caveats

- **Evidence-base caveats.** Three of the recommended rows rest on small-n or post-hoc subgroup evidence: rank 4 (carbo/gem) relies on the n=43 TNT BRCA-mut subgroup; rank 7 (SG + pembro) and rank 8 (SG monotherapy 1L) rest on the ASCENT-04 / ASCENT-03 NCCN cat-1 elevation pending peer-reviewed primary publications; rank 10 (MEDIOLA-style maintenance) is single-arm + subset across MEDIOLA, TOPACIO, and KEYLYNK-009 BRCA-mut subgroups. Rank 5 (TROPION-Breast05) is an actively recruiting phase 3 with no within-trial readout yet — the forward-cite anchor is TROPION-Breast02 (CPS <10 vs chemo), which is cross-trial extrapolation.

- **Biomarker dependencies.** The ranking is contingent on the rank-1 workup completing. Rank 2 and rank 9 are conditional on `germline_brca:positive` — germline-negative (somatic-only) BRCA1 routes the patient to NCT03990896 (Stanford talazoparib, n=13 interim) or to off-label use that the FDA breast label does not cover. Ranks 3, 5, 7 are conditional on PD-L1 CPS ≥10 by 22C3 — CPS <10 routes to ranks 6 (SG monotherapy) and 4 (carbo/gem) and to the CPS-low trial lanes TROPION-Breast02 / TroFuse-011. PIK3CA hotspot resolution is informational in TNBC; HER2 0 vs low gates trastuzumab deruxtecan for later lines only.

- **What would change the ranking.**
    - **Germline BRCA1 negative (somatic-only):** rank 2 and rank 9 collapse to off-label or NCT03990896; the CPS-anchored regimens move up.
    - **22C3 CPS <10:** rank 3 (KN-355), rank 5 (TROPION-Breast05), and rank 7 (SG + pembro) collapse; rank 8 (SG monotherapy ASCENT-03 NCCN cat-1) moves up to be the lead 1L systemic choice alongside rank 2 if germline confirms.
    - **ASCENT-04 OS interim positive:** the rank 7 / rank 3 ordering inverts in the NCCN consensus stack and rank 7 moves up.
    - **TROPION-Breast05 primary PFS positive:** rank 5's effect-size claim becomes a within-trial estimate rather than cross-trial extrapolation; rank 5 moves up.
    - **Published triplet safety dossier for ZEN-3694 + pembro + nab-paclitaxel:** the conservative veto on rank 11 lifts to qualified and the row may rise.
    - **Negative HER2 IHC reflex (HER2 0 confirmed):** keeps T-DXd out of scope for this case.

- **Re-scoping caveat.** If the patient's preferences shift (e.g. trial preference toggled off, modality vetoes added), or if her clinical state changes (e.g. liver lesion grows, additional sites emerge, ECOG declines), the ranking shifts. The most preference-sensitive call here is rank 5 (TROPION-Breast05) and rank 6 (SBRT NCT05534438) — both rest on the trial-preferred + curative-intent free-text framing. Toggling either preference changes their rank position materially.

## Sources

### PMIDs

- [PMID 21633166](https://pubmed.ncbi.nlm.nih.gov/21633166)
- [PMID 21945652](https://pubmed.ncbi.nlm.nih.gov/21945652)
- [PMID 25092775](https://pubmed.ncbi.nlm.nih.gov/25092775)
- [PMID 25214542](https://pubmed.ncbi.nlm.nih.gov/25214542)
- [PMID 28578601](https://pubmed.ncbi.nlm.nih.gov/28578601)
- [PMID 29070816](https://pubmed.ncbi.nlm.nih.gov/29070816)
- [PMID 29501363](https://pubmed.ncbi.nlm.nih.gov/29501363)
- [PMID 29521352](https://pubmed.ncbi.nlm.nih.gov/29521352)
- [PMID 29713086](https://pubmed.ncbi.nlm.nih.gov/29713086)
- [PMID 30110579](https://pubmed.ncbi.nlm.nih.gov/30110579)
- [PMID 30345906](https://pubmed.ncbi.nlm.nih.gov/30345906)
- [PMID 30894373](https://pubmed.ncbi.nlm.nih.gov/30894373)
- [PMID 30982687](https://pubmed.ncbi.nlm.nih.gov/30982687)
- [PMID 31091374](https://pubmed.ncbi.nlm.nih.gov/31091374)
- [PMID 31166680](https://pubmed.ncbi.nlm.nih.gov/31166680)
- [PMID 31194225](https://pubmed.ncbi.nlm.nih.gov/31194225)
- [PMID 31300473](https://pubmed.ncbi.nlm.nih.gov/31300473)
- [PMID 31754023](https://pubmed.ncbi.nlm.nih.gov/31754023)
- [PMID 31836816](https://pubmed.ncbi.nlm.nih.gov/31836816)
- [PMID 32101663](https://pubmed.ncbi.nlm.nih.gov/32101663)
- [PMID 32195312](https://pubmed.ncbi.nlm.nih.gov/32195312)
- [PMID 32499663](https://pubmed.ncbi.nlm.nih.gov/32499663)
- [PMID 32540858](https://pubmed.ncbi.nlm.nih.gov/32540858)
- [PMID 32771088](https://pubmed.ncbi.nlm.nih.gov/32771088)
- [PMID 32826325](https://pubmed.ncbi.nlm.nih.gov/32826325)
- [PMID 32861273](https://pubmed.ncbi.nlm.nih.gov/32861273)
- [PMID 32913096](https://pubmed.ncbi.nlm.nih.gov/32913096)
- [PMID 32919526](https://pubmed.ncbi.nlm.nih.gov/32919526)
- [PMID 33037126](https://pubmed.ncbi.nlm.nih.gov/33037126)
- [PMID 33119881](https://pubmed.ncbi.nlm.nih.gov/33119881)
- [PMID 33257427](https://pubmed.ncbi.nlm.nih.gov/33257427)
- [PMID 33278935](https://pubmed.ncbi.nlm.nih.gov/33278935)
- [PMID 33882206](https://pubmed.ncbi.nlm.nih.gov/33882206)
- [PMID 33885704](https://pubmed.ncbi.nlm.nih.gov/33885704)
- [PMID 34081848](https://pubmed.ncbi.nlm.nih.gov/34081848)
- [PMID 34219000](https://pubmed.ncbi.nlm.nih.gov/34219000)
- [PMID 34301749](https://pubmed.ncbi.nlm.nih.gov/34301749)
- [PMID 34607981](https://pubmed.ncbi.nlm.nih.gov/34607981)
- [PMID 34626408](https://pubmed.ncbi.nlm.nih.gov/34626408)
- [PMID 34995128](https://pubmed.ncbi.nlm.nih.gov/34995128)
- [PMID 35046096](https://pubmed.ncbi.nlm.nih.gov/35046096)
- [PMID 35093516](https://pubmed.ncbi.nlm.nih.gov/35093516)
- [PMID 35168954](https://pubmed.ncbi.nlm.nih.gov/35168954)
- [PMID 35441145](https://pubmed.ncbi.nlm.nih.gov/35441145)
- [PMID 35613031](https://pubmed.ncbi.nlm.nih.gov/35613031)
- [PMID 35665782](https://pubmed.ncbi.nlm.nih.gov/35665782)
- [PMID 35857659](https://pubmed.ncbi.nlm.nih.gov/35857659)
- [PMID 37939271](https://pubmed.ncbi.nlm.nih.gov/37939271)
- [PMID 38092534](https://pubmed.ncbi.nlm.nih.gov/38092534)
- [PMID 38236575](https://pubmed.ncbi.nlm.nih.gov/38236575)
- [PMID 38302062](https://pubmed.ncbi.nlm.nih.gov/38302062)
- [PMID 38422473](https://pubmed.ncbi.nlm.nih.gov/38422473)
- [PMID 39101942](https://pubmed.ncbi.nlm.nih.gov/39101942)
- [PMID 40297626](https://pubmed.ncbi.nlm.nih.gov/40297626)
- [PMID 40931235](https://pubmed.ncbi.nlm.nih.gov/40931235)
- [PMID 41405563](https://pubmed.ncbi.nlm.nih.gov/41405563)
- [PMID 41937088](https://pubmed.ncbi.nlm.nih.gov/41937088)

### NCT IDs

- [NCT01945775](https://clinicaltrials.gov/study/NCT01945775)
- [NCT02000622](https://clinicaltrials.gov/study/NCT02000622)
- [NCT02032823](https://clinicaltrials.gov/study/NCT02032823)
- [NCT02163694](https://clinicaltrials.gov/study/NCT02163694)
- [NCT02364557](https://clinicaltrials.gov/study/NCT02364557)
- [NCT02425891](https://clinicaltrials.gov/study/NCT02425891)
- [NCT02574455](https://clinicaltrials.gov/study/NCT02574455)
- [NCT02628067](https://clinicaltrials.gov/study/NCT02628067)
- [NCT02657889](https://clinicaltrials.gov/study/NCT02657889)
- [NCT02734004](https://clinicaltrials.gov/study/NCT02734004)
- [NCT02819518](https://clinicaltrials.gov/study/NCT02819518)
- [NCT03036488](https://clinicaltrials.gov/study/NCT03036488)
- [NCT03167619](https://clinicaltrials.gov/study/NCT03167619)
- [NCT03330847](https://clinicaltrials.gov/study/NCT03330847)
- [NCT03801369](https://clinicaltrials.gov/study/NCT03801369)
- [NCT03990896](https://clinicaltrials.gov/study/NCT03990896)
- [NCT03997123](https://clinicaltrials.gov/study/NCT03997123)
- [NCT04191135](https://clinicaltrials.gov/study/NCT04191135)
- [NCT05374512](https://clinicaltrials.gov/study/NCT05374512)
- [NCT05382299](https://clinicaltrials.gov/study/NCT05382299)
- [NCT05422794](https://clinicaltrials.gov/study/NCT05422794)
- [NCT05534438](https://clinicaltrials.gov/study/NCT05534438)
- [NCT05633654](https://clinicaltrials.gov/study/NCT05633654)
- [NCT06103864](https://clinicaltrials.gov/study/NCT06103864)
- [NCT06841354](https://clinicaltrials.gov/study/NCT06841354)
- [NCT07441512](https://clinicaltrials.gov/study/NCT07441512)

## Transparency artifacts

- [Trial table](trials.md) — 23 rows, all columns
- [Clinical evidence](evidence.md) — 30 rows (25 included + 5 considered_excluded)
- [Master manuscripts](manuscripts.md) — flat inventory of every paper considered (clinical + preclinical) with sample size, effect size, variance, and toxicity columns
- [Board deliberations](board.md) — full agreement matrix and per-intervention persona transcripts (5 positions + 20 critiques)
- [Recommendations table](recommendations.md) — ranked options + pipeline context + per-intervention evidence in detail
- [Patient / caregiver plain-language summary](plain_language.md) — translator-agent output

## Run log

Authored 2026-05-19 by the PI synthesis agent on the case dossier assembled across screener (23 trials), evidence_curator (30 clinical-evidence rows + 24 preclinical), accessibility_screener (21 interventions), target_validator (13 rows), and five board personas (5 round-1 positions + 20 round-2 critiques). Inferred elements: rank ordering across same-agreement-score rows (broken on preference fit per Hard Rule); the rank-1 shared workup row consolidates five essential / high-priority target-validation rows the user enumerated (germline BRCA1, 22C3 CPS, F1CDx TMB, PIK3CA hotspot informational, HER2 IHC 0/low, ITWG TIL re-score); the `germline_brca:positive` scenario was chosen as the single decision-relevant dimension per the cap-at-one-dimension rule, with CPS dependencies documented in `open_questions[]` for the relevant rows; SBRT NCT05534438 status set to `considered_with_caveats` reflecting the genuine board split rather than a clean recommendation; SG monotherapy 1L (rank 8) was synthesized from concensusite's round-2 critique 15 referencing the Feb 27 2026 NCCN v2.2026 elevation, since no persona surfaced it in their round-1 picks.

<!-- libby:downloads:begin -->

## Downloads

### HTML

- [Target validation paths](target_validation.md?v=a6d3ace3) — per-feature biomarker-workup table with providers and references, sortable in-browser
- [Recommendations table](tnbc-brca1-oligomet-liver-r7p3-recommendations.html?v=dcf5cfc9) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide](accessibility.md?v=86c8e87a) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Access guide (offline)](tnbc-brca1-oligomet-liver-r7p3-accessibility.html?v=14fff67a) — same access-guide content packaged as a self-contained HTML that opens offline
- [Master manuscripts table](manuscripts.md?v=cd8be571) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Master manuscripts table (offline)](tnbc-brca1-oligomet-liver-r7p3-manuscripts.html?v=3df6d0d1) — same manuscripts inventory packaged as a self-contained HTML that opens offline

### PDF

- [Target validation paths](tnbc-brca1-oligomet-liver-r7p3-target-validation.pdf?v=608875ca) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table](tnbc-brca1-oligomet-liver-r7p3-recommendations.pdf?v=cb1396bc) — ranked options + pipeline context + evidence in detail, in a print-friendly PDF
- [Access guide](tnbc-brca1-oligomet-liver-r7p3-accessibility.pdf?v=bbb27e72) — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF
- [Master manuscripts table](tnbc-brca1-oligomet-liver-r7p3-manuscripts.pdf?v=a3a1b78c) — every paper considered — n, effect, variance, toxicities, in a print-friendly PDF
- [Patient/caregiver PDF](tnbc-brca1-oligomet-liver-r7p3-plain-language.pdf?v=32c31c9c) — plain-language summary

<!-- libby:downloads:end -->

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
