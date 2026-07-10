<meta name="robots" content="noindex">

# tnbc-brca1-oligomet-liver-r7p3

<!-- libby:case-output:begin -->

## Case output

- [Target validation paths (PDF)](tnbc-brca1-oligomet-liver-r7p3-target-validation.pdf?v=2f74caa0) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table (HTML)](tnbc-brca1-oligomet-liver-r7p3-recommendations.html?v=1af2c40c) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide (HTML)](accessibility.md?v=86c8e87a) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, sortable in-browser
- [Access guide (offline HTML)](tnbc-brca1-oligomet-liver-r7p3-accessibility.html?v=0176b3dc) — same access-guide content as the in-browser page, packaged as a self-contained HTML that opens offline
- [Master manuscripts table (HTML)](manuscripts.md?v=d98229d6) — every paper considered — n, effect, variance, toxicities, sortable in-browser
- [Master manuscripts table (offline HTML)](tnbc-brca1-oligomet-liver-r7p3-manuscripts.html?v=e78c434d) — same manuscripts inventory as the in-browser page, packaged as a self-contained HTML that opens offline
- [Patient/caregiver PDF](tnbc-brca1-oligomet-liver-r7p3-plain-language.pdf?v=b51fb4ae) — plain-language summary

<!-- libby:case-output:end -->
## Research question

In treatment-naive de novo metastatic triple-negative breast cancer — BRCA1-mutant, basal-like, TIL-rich, with a solitary liver oligometastasis and a curative-intent goal — what interventions could target the BRCA1 mutation and the basal/immune-favorable phenotype in the first line, and which recruiting on-axis trials deliver those options on-protocol?

## Patient profile (scrubbed)

- Woman, age band 40-49, ECOG 1.
- Right breast invasive ductal carcinoma, no special type, triple-negative; basal-like by intrinsic-subtype call.
- Stage cT2-3 cN1 cM1 — newly diagnosed de novo M1, with ipsilateral axillary nodal involvement and a solitary 1.5 cm hepatic lesion (liver-only, single-site oligometastatic).
- **BRCA1 mutated** on tumor NGS — **germline vs somatic not yet specified.** Somatic-only BRCA1 remains PARP-inhibitor-actionable, so PARP-i eligibility is not gated on this distinction; the germline call gates the *labeled* indication and the risk-reducing-surgery / cascade-testing conversation.
- TP53 mutated; MYC amplified; IRS2 amplified; PTEN copy-number loss (all confirmed).
- PIK3CA mutated — **specific hotspot codon pending** (NGS resolution needed to establish alpelisib/capivasertib actionability).
- TMB 14 mut/Mb (confirmed, ≥10 threshold); MSS; 3+ stromal TILs (ITWG, high); ER-negative, PR-negative, HER2-negative.
- **PD-L1 CPS by 22C3 — pending.** This is the gating biomarker for the 1L immunotherapy decision.
- No prior therapy; treatment-naive at presentation.

## Preferences

- Efficacy/toxicity weight: 0.7 (moderately efficacy-leaning).
- Toxicity vetoes: none stated.
- Modality constraints: none stated.
- Prefers trials: **true.**
- Free text: intake-applied defaults. The efficacy-leaning weight reflects a curative-intent framing — a young patient with a solitary liver lesion where systemic conversion followed by local ablation is plausible, so the operative goal weighs efficacy above tolerability. Trial preference is set true because the profile is strongly trial-eligible.

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

The refreshed dossier holds 38 trial rows, 22 clinical-evidence rows, and a preclinical set anchoring the BRCA1/PARP synthetic-lethality mechanism, plus accessibility and target-validation tracks. Nine ranked recommendations survive to this page, spanning agreement scores from 1.0 (unanimous) down to −0.2. All five personas converged on the KEYNOTE-355 backbone at rank 1 and on talazoparib as a PARP option; olaparib carries a four-persona endorsement with one preference-flavored dissent. The disagreement concentrates lower down: two personas dissented on the TROPION-Breast05 trial at rank 5, the PARP1-selective class split three-to-two at rank 7, and the DDR-combination and consolidation slots each carry a single standing objection. No persona issued a veto anywhere in the case.

## Cross-cutting caveat (read first)

**Two pending biomarkers gate the top of this ranking, and neither branches it — they decide on-label versus off-label and which lane the patient enters, not whether an option exists.** The 1L conversation cannot be finalized until the 22C3 PD-L1 CPS on the breast primary and the germline-vs-somatic BRCA1 determination return. These are the first actions, ahead of any prescription. What they change:

- **PD-L1 CPS ≥10 by 22C3** unlocks the rank-1 KEYNOTE-355 backbone (and TROPION-Breast05 enrollment) on label. CPS <10 removes the labeled ICI benefit — the favorable TMB-14 and 3+ TIL phenotype does not rescue it, because the label tracks CPS, not those surrogates — and the on-protocol route shifts to the CPS-low TROP2-ADC trials (TROPION-Breast02, TroFuse-011). Score the breast primary: primary-vs-liver-met PD-L1 discordance runs 20-30%.
- **Germline BRCA1** keeps olaparib and talazoparib category 1 and on label. A somatic-only call moves both off-label for the breast indication; the axis stays PARP-actionable, and the enrollable route becomes the Stanford somatic-BRCA talazoparib trial (NCT03990896). PARP-i actionability itself does not disappear on a somatic call — the label does.
- **Local therapy for the liver oligometastasis is trial-only, not a standalone recommendation.** Both randomized trials point against consolidation for unselected patients (NRG-BR002 phase IIR PFS HR ~1.31; E2108 OS HR 1.11). The curative-intent goal is honored through the MSK SABR trial slot (NCT05534438) layered on the systemic backbone after a documented response, not through off-protocol ablation.
- **The PIK3CA/AKT axis is out of the ranking on evidence, not on gating.** CAPItello-290 read out negative in 1L mTNBC including the PIK3CA/AKT1/PTEN-altered stratum this patient sits in, and EPIK-B3 (alpelisib) terminated early. Resolving the PIK3CA hotspot clarifies the pathway biology but does not open an active recommendation here.

## Intervention grouping

- 1L ICI + chemotherapy backbone: pembrolizumab + gem/carbo, KEYNOTE-355 ([33278935](https://pubmed.ncbi.nlm.nih.gov/33278935), [35857659](https://pubmed.ncbi.nlm.nih.gov/35857659), [NCT02819518](https://clinicaltrials.gov/study/NCT02819518)).
- BRCA1-directed PARP monotherapy: olaparib OlympiAD ([28578601](https://pubmed.ncbi.nlm.nih.gov/28578601)), talazoparib EMBRACA ([30110579](https://pubmed.ncbi.nlm.nih.gov/30110579)); somatic-BRCA route [NCT03990896](https://clinicaltrials.gov/study/NCT03990896).
- BRCA1 platinum backbone / induction: carboplatin per TNT BRCA-mut subset ([29713086](https://pubmed.ncbi.nlm.nih.gov/29713086), [35093516](https://pubmed.ncbi.nlm.nih.gov/35093516)).
- Recruiting 1L TROP2-ADC + ICI on-protocol route: TROPION-Breast05 ([40297626](https://pubmed.ncbi.nlm.nih.gov/40297626), [NCT06103864](https://clinicaltrials.gov/study/NCT06103864)).
- Chemo-free PARP + IO and PARP1-selective trial options: TOPACIO/MEDIOLA ([31194225](https://pubmed.ncbi.nlm.nih.gov/31194225), [32771088](https://pubmed.ncbi.nlm.nih.gov/32771088)); HS-10502 / saruparib class ([NCT05740956](https://clinicaltrials.gov/study/NCT05740956)).
- DDR-combination and oligomet consolidation trials: olaparib + ceralasertib ([37773077](https://pubmed.ncbi.nlm.nih.gov/37773077), [NCT04090567](https://clinicaltrials.gov/study/NCT04090567)); MSK SABR ([NCT05534438](https://clinicaltrials.gov/study/NCT05534438), [33885704](https://pubmed.ncbi.nlm.nih.gov/33885704), [34995128](https://pubmed.ncbi.nlm.nih.gov/34995128)).

## Workup considerations

Order the two gating biomarkers before any prescription, and run the rest of the panel in parallel off the same archival block:

- **PD-L1 CPS by 22C3 pharmDx on the breast primary** (essential, gates pembrolizumab). Turnaround 5-7 business days. Score the primary rather than the liver met; note discordance if only the M1 block is available.
- **Germline BRCA1/2 sequencing plus del/dup on a hereditary panel** (essential, gates the labeled olaparib/talazoparib indication and the risk-reducing-surgery / cascade-testing decisions). Blood or saliva; 2-3 weeks. NCCN mandates germline testing for TNBC at any age. Pair with a cancer-genetics counseling visit so cascade testing can trigger the same week.
- **TMB locked to FoundationOne CDx** (essential for any future TMB-agnostic pembrolizumab use). Same-day chart review if the 14 mut/Mb call already came from F1CDx; otherwise re-run before that value gates therapy.
- Lower-priority, non-gating, run when the block is already out: PTEN IHC protein confirmation, HRD genomic-scar score, PIK3CA hotspot resolution, ITWG stromal-TIL re-score, baseline ctDNA for BRCA1-reversion surveillance, and B2M/HLA class I IHC (ICI primary-resistance check in this MSS tumor). None of these gates a rank on this page; each hardens a rationale or seeds later-line interpretation.

## Top interventions

## Rank 1. Pembrolizumab + carboplatin/gemcitabine (KEYNOTE-355 backbone)

*The maturest 1L survival evidence in metastatic TNBC — but the entire labeled benefit lives in the CPS ≥10 stratum, and CPS is pending.*

### Evidence base

KEYNOTE-355 ([33278935](https://pubmed.ncbi.nlm.nih.gov/33278935), n=847, [NCT02819518](https://clinicaltrials.gov/study/NCT02819518)) randomized treatment-naive mTNBC to pembrolizumab plus investigator-choice chemotherapy versus chemotherapy alone. In the pre-specified PD-L1 CPS ≥10 stratum the primary PFS hit HR 0.65 (95% CI 0.49-0.86, p=0.0012; mPFS 9.7 vs 5.6 mo), and the final OS analysis at 44-month follow-up confirmed a durable gain: HR 0.73 (95% CI 0.55-0.95; mOS 23.0 vs 16.1 mo, [35857659](https://pubmed.ncbi.nlm.nih.gov/35857659)). RoB 2 is low across domains. Choosing the gemcitabine/carboplatin flavor of the backbone folds in the platinum this BRCA1 tumor is doubly sensitive to — TNT put the BRCA-mut carboplatin ORR at 68% vs 33% for docetaxel ([29713086](https://pubmed.ncbi.nlm.nih.gov/29713086)).

### Likelihood of desired effect

High, conditional on the biomarker. In the CPS ≥10 population this is the one 1L regimen with a proven survival benefit, and the patient's TIL-3+ / TMB-14 phenotype sits in the subgroup that pulls the largest effect in the KEYNOTE analyses. The catch is binary: below CPS 10 the labeled benefit evaporates, and neither TMB nor TILs substitutes for CPS in the label. Everything above hinges on the pending 22C3 result.

### Toxicity profile

- Grade 3+ treatment-related AEs 68.1% (vs 66.9% for chemo alone) — the increment over the backbone the patient would receive anyway is small.
- Grade 3+ neutropenia ~41%, driven by the gem/carbo backbone.
- Grade 3+ immune-mediated AEs 5.3% — hypothyroidism, hepatitis, pneumonitis; the standard irAE algorithm applies.
- Treatment-related deaths 0.4%.
- No stated toxicity veto is breached (the preference file sets none).

### Counter-productive mechanisms / dissent

No persona dissented or vetoed. The conservative and concensusite both flagged one mechanism-level watch item rather than an objection: in an MSS tumor a B2M or HLA class I-loss subclone would blunt the checkpoint arm despite the favorable TMB/TIL signal, which is why the B2M/HLA IHC sits on the workup list as cheap insurance. The critic's note was about ordering, not the regimen — the PARP axis carries two registered phase-3 hits against KEYNOTE-355's one, so if germline BRCA1 resolves before CPS returns, replication count argues the PARP monotherapy could lead.

### Practical considerations

Off-trial standard of care when CPS ≥10; routine Medicare and commercial coverage once the 22C3 result is documented. The trials-first preference is met by enrolling on TROPION-Breast05 (rank 5), whose control arm is this exact regimen — the advocate and concensusite both made this point. NCCN Breast v4.2025 category 1 / preferred, ESMO class I. If CPS <10, this drops out and the CPS-low lanes take over.

### Why this rank

The only unanimous endorsement in the case (agreement 1.0) and the maturest survival evidence for a treatment-naive patient. It sits above the PARP options because it carries an OS readout in the front-line setting that single-agent PARP-i does not, and because it serves the BRCA1 axis through its carboplatin partner at the same time.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Pembrolizumab + chemo (CPS ≥10, primary PFS) | PFS HR 0.65; mPFS 9.7 vs 5.6 mo | G3+ TRAE 68.1%; irAE G3+ 5.3% | [33278935](https://pubmed.ncbi.nlm.nih.gov/33278935) |
| Pembrolizumab + chemo (CPS ≥10, final OS) | OS HR 0.73; mOS 23.0 vs 16.1 mo | Treatment-related death 0.4% | [35857659](https://pubmed.ncbi.nlm.nih.gov/35857659) |
| Carboplatin (TNT BRCA-mut subset) | ORR 68% vs 33%; PFS HR 0.44 | G3+ neutropenia 12% (single-agent) | [29713086](https://pubmed.ncbi.nlm.nih.gov/29713086) |

## Rank 2. Olaparib 300 mg PO BID (OlympiAD)

*Conditional on germline BRCA1. A somatic-only call moves it off-label — the axis stays PARP-actionable, but the labeled indication does not.*

### Evidence base

OlympiAD ([28578601](https://pubmed.ncbi.nlm.nih.gov/28578601), n=302, [NCT02000622](https://clinicaltrials.gov/study/NCT02000622)) randomized germline-BRCA HER2-negative mBC to olaparib versus physician's-choice chemotherapy: PFS HR 0.58 (95% CI 0.43-0.80, p<0.001; mPFS 7.0 vs 4.2 mo), ORR 59.9% vs 28.8%, BICR-adjudicated, low RoB 2. EMBRACA replicates the direction and magnitude with talazoparib (HR 0.54). The OlympiA adjuvant dataset ([34081848](https://pubmed.ncbi.nlm.nih.gov/34081848), n=1836) extends the safety window to a curative setting with no MDS/AML excess at 300 mg BID — reassurance for a patient who may live years on or after the drug.

### Likelihood of desired effect

High in germline BRCA1 disease. Two independent registrational RCTs converge on PFS HR ~0.55 in exactly this biomarker-defined population, which is the evidence bar the critic and concensusite weight above every abstract-level DDR agent in the dossier. If the variant reads somatic-only, the predictive biology holds but the labeled confidence does not, and the estimate should be read down to the single-arm somatic cohort.

### Toxicity profile

- Grade 3+ anemia 16.1% — the dominant AE; set a transfusion/hold threshold and baseline CBC before starting.
- Grade 3+ AE rate 36.6% overall, below the 50.5% comparator chemo.
- Treatment discontinuation for AE 4.9% — the lowest among single-agent options on this ranking.
- Cumulative MDS/AML ~1-2% across the pooled PARP dataset over a 12-18 month horizon; serial CBC monitoring.

### Counter-productive mechanisms / dissent

No dissent, no veto. The advocate's only reservation was preference-flavored: with prefers_trials true and a curative-intent framing, she would foreground the enrollable options first, not a dissent on the drug itself. The one mechanism-level note is a resistance route rather than a counter-productive vector — BRCA1 reversion is the dominant acquired-resistance mechanism, which is why a baseline ctDNA draw before any PARP exposure is worth having.

### Practical considerations

Oral, single-agent, chemo-free — fits a young patient with a lower visit burden than chair-time regimens. On-label and routinely covered when germline BRCA is documented; a somatic-only call makes the identical script off-label, workable through an NCCN Compendium medical-exception request. Between the two labeled PARP inhibitors, the conservative, concensusite and advocate all favor olaparib on the hematologic margin. NCCN Breast v4.2025 category 1, ESMO class I.

### Why this rank

It sits behind the KEYNOTE-355 backbone because single-agent PARP-i carries no front-line OS readout, and ahead of talazoparib because it delivers the same replicated efficacy with a materially gentler hematologic profile (G3+ anemia 16.1% vs 39%). The agreement gap to rank 1 (0.8 vs 1.0) is the advocate's preference-fit reservation, not an evidence dispute.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Olaparib (OlympiAD, gBRCA mBC) | PFS HR 0.58; ORR 59.9% vs 28.8% | G3+ anemia 16.1%; discontinuation 4.9% | [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601) |
| Olaparib (OlympiA adjuvant) | iDFS HR 0.58; OS HR 0.68 | No MDS/AML excess at 300 mg BID | [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848) |

## Rank 3. Talazoparib 1 mg PO daily (EMBRACA)

*Conditional on germline BRCA1, same as olaparib. Somatic-only routes through the Stanford trial (NCT03990896).*

### Evidence base

EMBRACA ([30110579](https://pubmed.ncbi.nlm.nih.gov/30110579), n=431, [NCT01945775](https://clinicaltrials.gov/study/NCT01945775)) is the second registrational PARP RCT in germline-BRCA HER2-negative mBC: PFS HR 0.54 (95% CI 0.41-0.71, p<0.001; mPFS 8.6 vs 5.6 mo), ORR 62.6% vs 27.2% — the deepest single-agent response rate on the BRCA1 axis. OS was not significantly improved (HR 0.76, p=0.11). If BRCA1 reads somatic-only, the Stanford/TBCRC talazoparib cohort ([NCT03990896](https://clinicaltrials.gov/study/NCT03990896)) reported ~38% ORR in interim analysis.

### Likelihood of desired effect

High in germline BRCA1 disease, at parity with olaparib on PFS and edging it on ORR depth. The risktaker's specific bet is that the deepest single-agent response is the most plausible route to shrinking the solitary hepatic lesion to a resectable target — a conversion hypothesis, testable on-protocol at rank 9, not a settled endpoint. As with olaparib, a somatic-only call reads the labeled confidence down.

### Toxicity profile

- Grade 3+ anemia ~39% — substantially heavier than olaparib; expect dose holds or transfusion support.
- Grade 3+ neutropenia ~21%, thrombocytopenia ~15%.
- Same germline-restricted label as olaparib.

### Counter-productive mechanisms / dissent

Endorsed by all five personas with no dissent. The split was on ordering, not mechanism: the risktaker put talazoparib first for the highest PARP-trapping potency and deepest ORR, while the conservative, critic and advocate placed it a notch below olaparib purely on the hematologic-tolerability delta. There is no mechanism-level counter-productive vector.

### Practical considerations

Interchangeable with olaparib for the on-label germline case and facing the same somatic-only question. Most teams default to olaparib unless once-daily dosing is preferred or the anemia profile is acceptable. The heavier marrow cost matters specifically because the patient may need myelosuppressive chemo before or after. NCCN category 1, ESMO class I.

### Why this rank

The efficacy is not what separates rank 3 from rank 2 — EMBRACA and OlympiAD are at parity. Talazoparib sits one rank lower because it spends more marrow reserve for the same PFS, which is the deciding factor for a patient who may also need platinum-containing chemo. The risktaker's conversion argument keeps it a genuine co-lead rather than dropping it further.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Talazoparib (EMBRACA, gBRCA mBC) | PFS HR 0.54; ORR 62.6% vs 27.2% | G3+ anemia ~39%; neutropenia ~21% | [30110579](https://pubmed.ncbi.nlm.nih.gov/30110579) |
| Talazoparib (somatic-BRCA cohort) | ORR ~38% (interim) | Early-phase; single-arm | [NCT03990896](https://clinicaltrials.gov/study/NCT03990896) |

## Rank 4. Carboplatin AUC2 + gemcitabine d1,8 q21d

*The germline- and CPS-agnostic BRCA1 backbone — the one option no pending test can foreclose.*

### Evidence base

TNT ([29713086](https://pubmed.ncbi.nlm.nih.gov/29713086), n=376) found no overall PFS difference between carboplatin and docetaxel, but the pre-specified BRCA-mut subgroup (n=43) favored carboplatin: ORR 68.0% vs 33.3%, PFS HR 0.44, interaction p=0.01. BrighTNess and CALGB 40603 ([35093516](https://pubmed.ncbi.nlm.nih.gov/35093516)) both show the platinum, not an added PARP, drives depth of response. This is class evidence plus decades of post-marketing experience, not a registrational 1L anchor — a point the critic and conservative both made plainly.

### Likelihood of desired effect

Moderate-to-high in BRCA1-mut disease, with the honest caveat that the headline 68% comes from an n=43 subgroup with a wide CI. It is the one 1L option that works no matter how the CPS and germline questions resolve, and it doubles as the induction platform for a later olaparib or PARP+IO maintenance strategy.

### Toxicity profile

- Additive myelosuppression from the doublet — G3+ neutropenia 30-40%, thrombocytopenia ~15%; day-8 counts drive dose modification.
- Well-characterized and dose-modifiable; standard supportive-care algorithms apply.
- Trading down from the pembrolizumab arm gives up the OS advantage that regimen carries if CPS ≥10 returns.

### Counter-productive mechanisms / dissent

Three-persona endorsement (conservative rank 3, critic rank 5, concensusite rank 3), no dissent, no veto. No counter-productive mechanism — the tradeoff is a forgone OS benefit versus the CPS-gated ICI arm, not a mechanistic vector.

### Practical considerations

NCCN Breast v4.2025 category 1 / preferred with explicit BRCA-mut support; NCCN Compendium covers the indication, so no prior-auth friction. Off-trial. Its practical value is as the biomarker-agnostic hold and as the platinum induction that a PARP or PARP+IO maintenance can build on (DORA / KEYLYNK-009 template).

### Why this rank

It ranks below the PARP options because it forgoes their chemo-free footprint and replicated RCT tier, and below pembro+chemo because it forgoes the OS advantage in a CPS-high patient. It earns rank 4 rather than lower because it is the option that cannot be gated out from under the patient — the defensible floor if both biomarker gates close.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Carboplatin (TNT BRCA-mut subset) | ORR 68% vs 33%; PFS HR 0.44 | G3+ neutropenia 12%; thrombocytopenia 7% | [29713086](https://pubmed.ncbi.nlm.nih.gov/29713086) |
| Carboplatin add-on (BrighTNess EFS) | 4-yr EFS HR 0.63 (carbo arm vs pacli alone) | G3+ neutropenia 56%; anemia 29% (combo) | [35093516](https://pubmed.ncbi.nlm.nih.gov/35093516) |

## Rank 5. Datopotamab deruxtecan +/- durvalumab on TROPION-Breast05 (NCT06103864)

*The recruiting 1L on-protocol route if CPS ≥10 — the control arm reproduces standard of care, but the experimental TROP2 mechanism sits off the BRCA1 axis and is untested.*

### Evidence base

TROPION-Breast05 ([NCT06103864](https://clinicaltrials.gov/study/NCT06103864), [40297626](https://pubmed.ncbi.nlm.nih.gov/40297626), n=1075) is the actively-recruiting 1L pivotal that randomizes Dato-DXd ± durvalumab against the KEYNOTE-355 backbone in PD-L1 CPS ≥10 mTNBC. The readout is pending, so there is no efficacy estimate for the experimental arms yet; what is knowable is that the control arm is the rank-1 regimen ([33278935](https://pubmed.ncbi.nlm.nih.gov/33278935)), which bounds the downside at standard of care.

### Likelihood of desired effect

Unquantified. The control arm reproduces the KEYNOTE-355 floor; the experimental-arm benefit — a TROP2-ADC against the basal feature plus a durvalumab arm leveraging the TMB-H / TIL-rich phenotype — is a bet, not a measured effect. A 1:1 randomization means the patient may never touch the experimental arm. CPS <10 removes eligibility entirely and shifts the on-protocol route to TROPION-Breast02 or TroFuse-011.

### Toxicity profile

- Class Dato-DXd AEs: stomatitis, ocular events, and ILD/pneumonitis (~3% any-grade, the characteristic deruxtecan-payload signal).
- Fewer hematologic events than the chemo arm.
- No stated toxicity veto is breached.

### Counter-productive mechanisms / dissent

Two dissents, which is what lands this at considered_with_caveats. The risktaker's is mechanistic: Dato-DXd carries no BRCA1 synthetic-lethal mechanism, so the experimental arm spends the curative-intent window on TROP2 rather than the DDR axis that could actually shrink the liver lesion, and the randomization risks assignment to the control arm she could get off-trial. The concensusite's is on guideline fit: an investigational ADC does not outrank the category-1 CPS ≥10 standard, so the trial belongs on the ranking as an enrollment vehicle, not as evidence Dato-DXd beats KEYNOTE-355.

### Practical considerations

Recruiting; AstraZeneca Clinical Study Information Center handles site screening. Investigational in 1L mTNBC with no NCCN category. The honest framing, which both dissenting personas insisted on, is that this is the on-protocol way to receive the rank-1 floor plus a shot at an experimental ceiling — the trials-first preference is served by enrollment, not by a claim that the drug outranks standard of care.

### Why this rank

It sits below the biomarker-agnostic backbone because its own arm is unproven and its mechanism is off the BRCA1 axis the case revolves around, yet it earns a place on the ranking because prefers_trials is true and this is the cleanest recruiting 1L on-axis slot — the advocate ranked it first for exactly that reason. The negative agreement score (−0.2) reflects the two standing dissents against a single endorsement.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Dato-DXd ± durvalumab (TROPION-Breast05) | Readout pending; control arm = KEYNOTE-355 | Stomatitis, ocular, ILD/pneumonitis ~3% | [NCT06103864](https://clinicaltrials.gov/study/NCT06103864) |
| Control arm (pembro + chemo) | OS HR 0.73 in CPS ≥10 (KEYNOTE-355) | G3+ TRAE 68.1% | [33278935](https://pubmed.ncbi.nlm.nih.gov/33278935) |

## Rank 6. Niraparib + pembrolizumab (TOPACIO)

*A mechanistically clean chemo-free PARP+IO bet for this exact phenotype — but the headline 47% is an n=15 subgroup and niraparib is off-label.*

### Evidence base

TOPACIO ([31194225](https://pubmed.ncbi.nlm.nih.gov/31194225), n=55, single-arm) reported cohort-level ORR 21% (95% CI 12-33, n=42); the 47% the pick leans on is the BRCA-mut TNBC subgroup, n=15. MEDIOLA ([32771088](https://pubmed.ncbi.nlm.nih.gov/32771088), olaparib+durvalumab, n=34) points the same direction with ORR 63% and DCR 80%. Both are single-arm with no comparator to apportion credit between the PARP inhibitor, the checkpoint, and BRCA1 selection.

### Likelihood of desired effect

Moderate but genuinely uncertain. The biology is a reasonable prior for this BRCA1 + TMB-14 + 3+ TIL patient — a neoantigen-generating PARP inhibitor stacked on a checkpoint that exploits them. But a response rate from 15 patients has a confidence interval wide enough to swallow much of the enthusiasm, and a larger cohort would likely regress toward the published 21%. Framed for the front line, this overstates the evidence weight; it reads best as a later-line maintenance question.

### Toxicity profile

- Overlapping hematologic burden: G3+ anemia 18%, thrombocytopenia 15%.
- Immune-related AEs 15% any-grade, 4% G3+.
- No dedicated combination safety readout in TNBC — the AE algorithm for the doublet does not exist the way it does for labeled PARP monotherapy.

### Counter-productive mechanisms / dissent

The risktaker ranked it third; the critic dissented on evidence quality and the conservative attached a heavy toxicity qualifier, leaving it at neutral agreement (0.0). In an MSS tumor a B2M/HLA-loss subclone would blunt the checkpoint half, the same watch item as at rank 1. The critic's dissent is the load-bearing one: an n=15 subgroup ORR does not compete with the front-line RCT anchors.

### Practical considerations

Niraparib is off-label in breast cancer with no NCCN Compendium support, so payer denial is likely versus labeled olaparib/talazoparib. TOPACIO itself is completed; the enrollable analog of the chemo-free PARP+IO concept is a maintenance design after platinum induction (DORA / KEYLYNK-009), not this exact regimen.

### Why this rank

It sits below the labeled PARP monotherapy and the trial-vehicle rank 5 because its evidence is a single-arm subgroup and its access path is the hardest of the PARP options. It stays on the list because the biology genuinely matches this phenotype and the ceiling is high — a later-line maintenance question worth carrying, not a 1L move.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Niraparib + pembrolizumab (TOPACIO) | ORR 21% (n=42); 47% BRCA-mut (n=15) | G3+ anemia 18%; thrombocytopenia 15%; irAE G3+ 4% | [31194225](https://pubmed.ncbi.nlm.nih.gov/31194225) |
| Olaparib + durvalumab (MEDIOLA) | ORR 63%; DCR 80%; mPFS 8.2 mo | G3+ AEs 32%; anemia 12% | [32771088](https://pubmed.ncbi.nlm.nih.gov/32771088) |

## Rank 7. PARP1-selective inhibitor trial — HS-10502 (NCT05740956), saruparib/PETRA as class precedent

*The enrollable toxicity-sparing PARP bet for a young patient facing years on the DDR axis — but the efficacy is cross-subtype abstract-level, and the enrollable agent has no readout of its own.*

### Evidence base

The class signal is saruparib in the PETRA breast subset: ORR 48.4% (95% CI 35.7-61.3, n=31 at 60 mg), mPFS 9.1 mo, with less hematologic toxicity than approved PARP1/2 inhibitors. That is a single-arm AACR abstract with a mixed HR+/TNBC subset, a null PMID, and no per-term grade-3+ table. HS-10502 ([NCT05740956](https://clinicaltrials.gov/study/NCT05740956)) has a dedicated HRR-mutant HER2-negative breast cohort the patient's BRCA1 status matches directly, but no published efficacy or safety readout of its own — it must not inherit saruparib's number.

### Likelihood of desired effect

Uncertain. PARP1-selectivity is designed to spare the anemia and thrombocytopenia that cap olaparib and talazoparib, which is the real appeal for a 42-year-old facing years of DDR-axis therapy. But without a per-term grade-3+ table you cannot show the toxicity-sparing, only argue it, and the TNBC-specific PARP1-selective ORR is unknown. Framed for the positive branch of enrollment, this is a mechanistic bet, not a measured effect.

### Toxicity profile

- Not characterized — no per-term grade-3+ table released for either agent.
- The mechanism predicts less anemia than olaparib/talazoparib; that prediction is the whole point and is untested.

### Counter-productive mechanisms / dissent

The board split three-to-two. The risktaker, concensusite and advocate surfaced the class as a preference-aligned trial option; the conservative and critic dissented on evidence quality, and their dissents persist regardless of biomarker status — the published-evidence base does not change with any test result. The toxicity-sparing claim is a hypothesis a trial is meant to test, which is exactly why enrollment with prospective AE capture is the only honest route.

### Practical considerations

Recruiting, on-axis, 2L+ with a prior-therapy expectation — so a treatment-naive patient needs a first line before qualifying. Investigational; no NCCN category. Every persona who surfaced it agreed it does not outrank the replicated category-1 PARP RCTs.

### Why this rank

It ranks below the chemo-free PARP+IO slot because its enrollable agent has no data of its own and the class evidence is cross-subtype, and it is 2L+ rather than front-line. It stays ranked (agreement 0.2) because the enrollable form is a legitimate on-protocol route for the toxicity-sparing bet the preference file cares about, not because the efficacy is established.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| HS-10502 (HRR-mut breast cohort) | No readout of its own | Not reported | [NCT05740956](https://clinicaltrials.gov/study/NCT05740956) |
| Saruparib (PETRA breast subset, class precedent) | ORR 48.4%; mPFS 9.1 mo (abstract) | No per-term G3+ table | [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601) |

## Rank 8. Olaparib + ceralasertib (ATR-i) on the recruiting germline-BRCA arm (NCT04090567)

*The best-evidenced DDR-combination entry and a recruiting home for the BRCA1+TP53 ATR rationale — but VIOLETTE was negative over olaparib alone, and it is 2L+ only.*

### Evidence base

plasmaMATCH Cohort E ([37773077](https://pubmed.ncbi.nlm.nih.gov/37773077), n=70) is a published, TNBC-specific cohort — ORR 17.1% (95% CI 10.4-25.5), with responses in HRR-wildtype and functional-HRD tumors that fit her BRCA1 + TP53 replication-stress phenotype. That maturity is what distinguishes it from the abstract-only POLθ/PARG rows. But it is single-arm with a surrogate endpoint, and VIOLETTE ([NCT03330847](https://clinicaltrials.gov/study/NCT03330847)), the dedicated randomized test, failed to beat olaparib monotherapy (PFS HR ~0.81, NS). The MD Anderson trial ([NCT04090567](https://clinicaltrials.gov/study/NCT04090567)) gives the ATR combination a recruiting germline-BRCA home.

### Likelihood of desired effect

Low-to-moderate. A 17% ORR in a 2L+ pretreated cohort does not transfer to 1L treatment-naive disease, and the one randomized trial built to prove the combination adds value over PARP monotherapy could not show it. Framed for enrollment, this is a later-line trial slot, not a front-line efficacy play.

### Toxicity profile

- Adds anemia and hypertension over single-agent olaparib.
- Requires a documented anemia/hypertension monitoring plan.

### Counter-productive mechanisms / dissent

The critic and advocate both surfaced it as the best-evidenced new DDR entry; the conservative's qualifier reads as a dissent on incremental value — the added ATR toxicity buys efficacy the randomized trial could not demonstrate over the PARP monotherapy the patient is already eligible for. Both the setting mismatch and the washout requirement make it non-enrollable now.

### Practical considerations

Recruiting; accepts germline-BRCA. Investigational, no NCCN category. It ranks here as a later-line slot with a monitoring plan, not a 1L move and not a substitute for the labeled PARP monotherapy above it.

### Why this rank

It sits below the PARP1-selective slot on the strength of the negative randomized readout that specifically tests its premise, and below all the front-line options because it is 2L+ and washout-gated. Its agreement (0.2) reflects two endorsements against one incremental-value dissent.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Olaparib + ceralasertib (plasmaMATCH Cohort E) | ORR 17.1%; mPFS ~4.3 mo | Anemia, hypertension added | [37773077](https://pubmed.ncbi.nlm.nih.gov/37773077) |
| Olaparib + ceralasertib (VIOLETTE) | PFS HR ~0.81 (NS) vs olaparib alone | Additive myelosuppression | [NCT03330847](https://clinicaltrials.gov/study/NCT03330847) |

## Rank 9. SBRT to the solitary liver lesion on the MSK SABR trial (NCT05534438)

*The on-protocol route to the curative-intent framing the patient asked for — tempered by two negative randomized consolidation trials. A trial-only layer on the systemic backbone, never a standalone.*

### Evidence base

The MSK randomized phase 2 ([NCT05534438](https://clinicaltrials.gov/study/NCT05534438)) enrolls de novo oligometastatic breast disease and delivers SBRT on-protocol once a 12-week scan confirms the breast and axilla are controlled. The counter-evidence travels with it: NRG-BR002 ([33885704](https://pubmed.ncbi.nlm.nih.gov/33885704)) phase IIR PFS favored systemic therapy alone (HR ~1.31), and E2108 ([34995128](https://pubmed.ncbi.nlm.nih.gov/34995128)) found no OS benefit from local therapy of the intact primary (OS HR 1.11).

### Likelihood of desired effect

Low for a durable benefit off-protocol. The curative-intent rationale rests on biology selection of a single small lesion, not on a positive randomized signal — both randomized trials point the other way for unselected patients. Whether biology-selected single-lesion consolidation escapes that negative signal is precisely the open trial question, which is why the MSK slot rather than off-protocol ablation.

### Toxicity profile

- Radiation modality; lesion-specific, with no systemic AE profile.

### Counter-productive mechanisms / dissent

The advocate ranked it fifth and carried the counter-evidence herself; the conservative and critic both flagged that off-protocol local therapy is unsupported. No persona dissented against the trial framing, and the advocate conceded the NRG-BR002 and E2108 points to the critic in round 2 — which is exactly why the recommendation points at the trial slot, not off-protocol ablation. No mechanism blunts the systemic goal; the risk is null benefit from consolidation.

### Practical considerations

Recruiting at MSK network sites; requires a documented systemic response first, so timing is downstream of the rank 1-4 decision. Not guideline-endorsed as routine practice — a case-by-case tumor-board decision framed here as trial-only, layered on top of the systemic backbone.

### Why this rank

It sits at the bottom because it neither targets the tumor biology directly nor rests on a positive randomized signal — it is consolidation, not systemic therapy. It earns a place on a 1L ranking at all only because the patient's curative-intent free text and a solitary 1.5 cm lesion make it the most consolidatable disease she will ever present with, and the trials-first preference points at the MSK slot as the honest route.

### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| SBRT consolidation (MSK SABR trial) | Ongoing; layered on systemic therapy | Radiation modality; lesion-specific | [NCT05534438](https://clinicaltrials.gov/study/NCT05534438) |
| SBRT/resection (NRG-BR002 phase IIR) | PFS HR ~1.31 (favors systemic alone) | Consolidation not supported off-protocol | [33885704](https://pubmed.ncbi.nlm.nih.gov/33885704) |
| Primary local therapy (E2108) | OS HR 1.11 (no benefit) | — | [34995128](https://pubmed.ncbi.nlm.nih.gov/34995128) |

## Classes examined but not ranked

- **PI3Kα / AKT inhibitors (alpelisib, inavolisib, capivasertib).** Excluded on direct RCT evidence, not on gating: CAPItello-290 read out negative in 1L mTNBC including the PIK3CA/AKT1/PTEN-altered stratum this patient sits in, and EPIK-B3 (alpelisib) terminated early. The PIK3CA hotspot resolution clarifies pathway biology but opens no active recommendation here.
- **WEE1 inhibitors (adavosertib, azenosertib).** Adavosertib is discontinued with no supply path; the VIOLETTE WEE1 arm closed for toxicity, and no TNBC azenosertib trial is open. Mechanistically plausible for the TP53 replication-stress phenotype, but there is nothing enrollable today.
- **POLθ and PARG inhibitors (ART6043, novobiocin, SYN818, DAT-2645).** On-axis for the BRCA1 HRD vulnerability but phase 1 with no per-term safety tables, and all washout-gated, so incompatible with a treatment-naive 1L position.
- **CX-5461 (G-quadruplex stabilizer).** Touches both BRCA1 and MYC, but the IND.231 responders clustered in BRCA2/PALB2 carriers (BRCA1 benefit inferred), ORR was 14%, and a published mutagenicity flag plus G3-4 phototoxicity make it disqualifying for any curative-intent framing — the conservative said as much explicitly.
- **IGF-1R / IRS-axis agents (xentuzumab class).** The IRS2 amplification is real biology, but the entire class has wound down across sponsors with no accessible agent.
- **Niraparib monotherapy (BRAVO), veliparib (BROCADE3/BrighTNess).** BRAVO was halted for futility on central review; veliparib is functionally unavailable after AbbVie discontinued the program, and BrighTNess showed the platinum, not the PARP, drove the benefit.

## Ranked prioritization

| Rank | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
|---|---|---|---|---|---|
| 1 | **Pembrolizumab + carbo/gem (KEYNOTE-355)**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | High in the CPS ≥10 subset: OS HR 0.73 / mOS 23.0 vs 16.1 mo (pmid:35857659); zero labeled benefit if CPS <10, and CPS is pending. | High (neutropenia ~41%, immune-mediated events, treatment-related death 0.4%) | **Low** (In an MSS tumor a B2M/HLA class I-loss subclone would blunt the checkpoint arm, but no persona vetoed on mechanism.) | **The maturest 1L survival evidence in mTNBC and the board's only unanimous endorsement, though the entire labeled benefit is gated on a pending CPS ≥10 result.** |
| 2 | **Olaparib (OlympiAD)**<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | High in gBRCA1 disease: PFS HR 0.58, ORR 60% (pmid:28578601), replicated by EMBRACA; off-label and weaker-supported if BRCA1 is somatic-only. | Low (anemia 16.1%; nausea/fatigue mostly low-grade) | **Low** (No mechanism blunts the therapeutic goal; later BRCA1 reversion is a resistance route, not a counter-productive vector.) | **Category-1, replicated, oral single-agent efficacy directly on the BRCA1 axis with the gentlest hematologic profile of the PARP options — conditional on the germline call.** |
| 3 | **Talazoparib (EMBRACA)**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small> | High in gBRCA1 disease: PFS HR 0.54, ORR 62.6% (pmid:30110579) — deepest single-agent response; OS gain not significant. | Moderate (anemia ~39%, neutropenia ~21%, thrombocytopenia ~15%) | **Low** (No mechanism-level counter-productive vector; the risktaker/critic split was on tolerability and ORR depth, not mechanism.) | **Equal-labeled PARP alternative with the deepest ORR on the BRCA1 axis; ranks below olaparib only on a heavier hematologic burden, not on evidence.** |
| 4 | **Carboplatin + gemcitabine**<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small> | Moderate-to-high in BRCA1-mut disease: ORR 68% vs 33% for carboplatin over taxane (pmid:29713086), from an n=43 subgroup with a wide CI. | Moderate (neutropenia 30-40%, thrombocytopenia ~15%) | **Low** (No counter-productive mechanism; the tradeoff is forgone OS benefit versus the CPS-gated ICI arm, not a mechanistic vector.) | **The biomarker-agnostic BRCA1 platinum backbone that no pending test can foreclose; a floor and an induction platform rather than the efficacy ceiling.** |
| 5 | **Dato-DXd ± durvalumab (TROPION-Breast05)**<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-concensusite">concensusite</span></small> | Unquantified: 1L pivotal readout pending (nct:NCT06103864); the control arm reproduces the KEYNOTE-355 floor, the experimental-arm benefit is untested. | Moderate (stomatitis, ocular events, ILD/pneumonitis; fewer hematologic events than chemo) | **Moderate** (TROP2-ADC has no DDR mechanism, so the experimental arm may spend the curative-intent window off the BRCA1 axis.) | **The recruiting 1L on-protocol route whose control arm reproduces standard of care, honoring the trials-first preference; the experimental arm's TROP2 mechanism sits off the BRCA1 axis and is untested.** |
| 6 | **Niraparib + pembrolizumab (TOPACIO)**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span></small><br><small><em>dissent:</em> <span class="persona persona-critic">critic</span></small> | Moderate but uncertain: BRCA-mut subgroup ORR 47% (n=15) vs published cohort 21% (n=42, pmid:31194225); single-arm, no comparator. | Moderate (anemia, thrombocytopenia, immune-related AEs stacked) | **Moderate** (In an MSS tumor a B2M/HLA-loss subclone would blunt the checkpoint half; critic dissented on the thin single-arm evidence base.) | **A mechanistically clean chemo-free PARP+IO bet for this exact BRCA1/TMB/TIL phenotype, but the 47% is an n=15 subgroup and niraparib is off-label — a later-line maintenance question, not a 1L move.** |
| 7 | **PARP1-selective trial — HS-10502 (saruparib class)**<br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span></small> | Uncertain: class-precedent ORR 48.4% (saruparib PETRA, abstract, mixed HR+/TNBC); HS-10502's own activity unpublished. | Not characterized (per-term G3+ table not released; mechanism predicts less anemia) | **Moderate** (Critic and conservative dissented on the unproven toxicity-sparing claim; no per-term safety data to confirm PARP1-selectivity spares marrow.) | **The enrollable toxicity-sparing PARP bet for a young patient facing years on the DDR axis, but the efficacy is cross-subtype abstract-level and the enrollable agent has no readout of its own.** |
| 8 | **Olaparib + ceralasertib (NCT04090567)**<br><small><em>endorse:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span></small> | Low-to-moderate: TNBC ORR 17.1% (pmid:37773077), single-arm 2L+; the randomized VIOLETTE test did not beat olaparib alone. | Moderate (anemia and hypertension added over single-agent olaparib) | **Moderate** (Conservative flagged that the added ATR toxicity buys efficacy the randomized trial could not demonstrate over PARP monotherapy.) | **The best-evidenced DDR-combination entry and a recruiting home for the BRCA1+TP53 ATR rationale, but VIOLETTE was negative over olaparib alone and it is 2L+ only.** |
| 9 | **SBRT liver consolidation (MSK SABR, NCT05534438)**<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span></small> | Low for durable benefit off-protocol: randomized consolidation was negative in unselected patients (NRG-BR002 HR 1.31, pmid:33885704); trial-only, biology-selected. | Low (radiation modality; lesion-specific, no systemic AE profile) | **Low** (No mechanism blunts the systemic goal; the risk is null benefit from consolidation, per the negative randomized readouts.) | **The on-protocol route to the curative-intent framing the patient asked for, honestly tempered by two negative randomized consolidation trials — a trial-only layer on the systemic backbone, never a standalone.** |

!!! note "How to read this table"
    **Toxicity burden** is patient-level adverse-event severity (the side effects the patient feels). **Counter-productive MoA** is a separate axis — the mechanism-level risk that a therapy could blunt its own goal (a checkpoint that fails in an antigen-presentation-deficient tumor, an ADC that spends the window off the driver axis). The persona pills under each intervention are the at-a-glance board signal; the full per-persona rationale lives on the [board page](board.md).

## Caveats

- **Evidence-base caveats.** Ranks 1-4 rest on registrational phase-3 RCTs. Everything from rank 5 down leans on pending readouts (TROPION-Breast05), single-arm subgroups (TOPACIO n=15), conference abstracts with null PMIDs (saruparib PETRA), or negative randomized comparisons (VIOLETTE, NRG-BR002, E2108). The TNT BRCA-mut carboplatin advantage that anchors rank 4 comes from an n=43 pre-specified subgroup with a wide CI. Read the lower ranks as trial-enrollment options, not as efficacy claims at parity with the top four.
- **Biomarker dependencies.** The ranking assumes the two pending gates resolve favorably. A CPS <10 result forecloses ranks 1 and 5 as written and shifts the on-protocol route to the CPS-low TROP2-ADC lanes. A somatic-only BRCA1 call moves ranks 2 and 3 off-label — the axis stays PARP-actionable through the Stanford trial (NCT03990896), but the labeled category-1 status does not survive.
- **What would change the ranking.** A germline BRCA1 result returning before 22C3 would strengthen the critic's argument that the replicated PARP monotherapy could lead over the single-trial KEYNOTE-355 backbone. A CPS <10 result moves rank 1 to non-applicable and promotes the platinum backbone and the CPS-low trials. A peer-reviewed TNBC-specific PARP1-selective safety readout would move rank 7 from mechanistic bet toward measured option.
- **Re-scoping caveat.** This ranking is built for a treatment-naive, curative-intent, trials-preferring 1L position. If the patient declines trials, ranks 5, 7, 8, and 9 lose their footing and the off-trial standards at ranks 1-4 carry the plan. If the clinical state moves to established incurable disease, the curative-intent consolidation slot (rank 9) drops off entirely.

## Sources

**PubMed (PMID):**

- [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601)
- [29713086](https://pubmed.ncbi.nlm.nih.gov/29713086)
- [30110579](https://pubmed.ncbi.nlm.nih.gov/30110579)
- [31194225](https://pubmed.ncbi.nlm.nih.gov/31194225)
- [32771088](https://pubmed.ncbi.nlm.nih.gov/32771088)
- [33278935](https://pubmed.ncbi.nlm.nih.gov/33278935)
- [33885704](https://pubmed.ncbi.nlm.nih.gov/33885704)
- [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848)
- [34995128](https://pubmed.ncbi.nlm.nih.gov/34995128)
- [35093516](https://pubmed.ncbi.nlm.nih.gov/35093516)
- [35857659](https://pubmed.ncbi.nlm.nih.gov/35857659)
- [37773077](https://pubmed.ncbi.nlm.nih.gov/37773077)
- [40297626](https://pubmed.ncbi.nlm.nih.gov/40297626)

**ClinicalTrials.gov (NCT):**

- [NCT01945775](https://clinicaltrials.gov/study/NCT01945775)
- [NCT02000622](https://clinicaltrials.gov/study/NCT02000622)
- [NCT02819518](https://clinicaltrials.gov/study/NCT02819518)
- [NCT03330847](https://clinicaltrials.gov/study/NCT03330847)
- [NCT03990896](https://clinicaltrials.gov/study/NCT03990896)
- [NCT04090567](https://clinicaltrials.gov/study/NCT04090567)
- [NCT05534438](https://clinicaltrials.gov/study/NCT05534438)
- [NCT05740956](https://clinicaltrials.gov/study/NCT05740956)
- [NCT06103864](https://clinicaltrials.gov/study/NCT06103864)

## Transparency artifacts

- [Trial table](trials.md) — every screened trial row, all columns.
- [Clinical evidence](evidence.md) — clinical-evidence rows with effect sizes and toxicity tables.
- [Manuscripts](manuscripts.md) — master flat inventory of every paper considered (clinical + preclinical), with sample size, effect size, variance, and toxicity columns.
- [Board](board.md) — full agreement matrix and per-persona rationale for all five positions and cross-critiques.
- [Recommendations](recommendations.md) — the forwardable ranked table.
- [Plain language](plain_language.md) — the patient-facing translation.

## Run log

Authored 2026-07-09 by the PI agent, synthesizing fresh from the just-completed re-deliberated board (5 round-1 positions, 27 round-2 cross-critiques, all 2026-07 re-run) plus the refreshed dossier (38 trial rows, 22 clinical-evidence rows, preclinical set, accessibility and target-validation tracks) and the scrubbed profile/preferences. Scenario kept null throughout: BRCA1 is confirmed on tumor NGS and remains PARP-actionable whether germline or somatic, so the germline gate decides on-label versus off-label rather than branching the targetable-feature ranking; the two pending gates (22C3 CPS, germline-vs-somatic) are surfaced in Workup considerations and the cross-cutting caveat rather than as a rank-1 workup row. The PIK3CA/AKT axis was excluded on direct negative RCT evidence (CAPItello-290, EPIK-B3), not on gating, and named in Classes examined but not ranked. Reference check: 22 identifiers carried into recommendations.jsonl and index.md; all PMIDs and NCTs resolved on PubMed / ClinicalTrials.gov and matched their claimed context (title and effect); zero corrected, zero nulled, clean.

<!-- libby:downloads:begin -->

## Downloads

### HTML

- [Target validation paths](target_validation.md?v=a6d3ace3) — per-feature biomarker-workup table with providers and references, sortable in-browser
- [Recommendations table](tnbc-brca1-oligomet-liver-r7p3-recommendations.html?v=1af2c40c) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide](accessibility.md?v=86c8e87a) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Access guide (offline)](tnbc-brca1-oligomet-liver-r7p3-accessibility.html?v=0176b3dc) — same access-guide content packaged as a self-contained HTML that opens offline
- [Master manuscripts table](manuscripts.md?v=d98229d6) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Master manuscripts table (offline)](tnbc-brca1-oligomet-liver-r7p3-manuscripts.html?v=e78c434d) — same manuscripts inventory packaged as a self-contained HTML that opens offline

### PDF

- [Target validation paths](tnbc-brca1-oligomet-liver-r7p3-target-validation.pdf?v=2f74caa0) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table](tnbc-brca1-oligomet-liver-r7p3-recommendations.pdf?v=61be3230) — ranked options + pipeline context + evidence in detail, in a print-friendly PDF
- [Access guide](tnbc-brca1-oligomet-liver-r7p3-accessibility.pdf?v=d53466f3) — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF
- [Master manuscripts table](tnbc-brca1-oligomet-liver-r7p3-manuscripts.pdf?v=0c145605) — every paper considered — n, effect, variance, toxicities, in a print-friendly PDF
- [Patient/caregiver PDF](tnbc-brca1-oligomet-liver-r7p3-plain-language.pdf?v=b51fb4ae) — plain-language summary

<!-- libby:downloads:end -->

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
