<meta name="robots" content="noindex">

# `mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4`

<!-- libby:case-output:begin -->

## Case output

- [Target validation paths (PDF)](mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4-target-validation.pdf?v=a3e93fd8) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table (HTML)](mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4-recommendations.html?v=9deeb66c) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide (HTML)](accessibility.md?v=5c99e682) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, sortable in-browser
- [Access guide (offline HTML)](mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4-accessibility.html?v=6133b7ca) — same access-guide content as the in-browser page, packaged as a self-contained HTML that opens offline
- [Master manuscripts table (HTML)](manuscripts.md?v=d90da807) — every paper considered — n, effect, variance, toxicities, sortable in-browser
- [Master manuscripts table (offline HTML)](mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4-manuscripts.html?v=a3a786ce) — same manuscripts inventory as the in-browser page, packaged as a self-contained HTML that opens offline
- [Patient/caregiver PDF](mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4-plain-language.pdf?v=0010a141) — plain-language summary

<!-- libby:case-output:end -->
## Research question

In metastatic colon adenocarcinoma with KRAS A59T (atypical switch-II) plus PIK3CA M1043I in a 37-year-old on 1L FOLFIRI + bevacizumab with resected liver metastases and active peritoneal disease entering a planned CRS-HIPEC window, what interventions target the atypical RAS allele, the PI3K-alpha activation, and the peritoneal compartment, gated on comprehensive NGS confirmation (KRAS A59T VAF, full extended RAS, BRAF V600, ERBB2 amplification, PIK3CA M1043I clonality, TP53 R273 substitution), HER2 IHC/FISH per HERACLES, MMR IHC orthogonal to NGS-MSI, DPYD + UGT1A1 germline pharmacogenomics, and a Signatera baseline draw before surgery?

## Patient profile (scrubbed)

- **Primary site / histology:** colon adenocarcinoma (histologic subtype not specified at intake)
- **Stage:** IV — metastatic; liver metastases status post-resection, active peritoneal involvement
- **Performance status:** ECOG 1 (assumed from current FOLFIRI tolerance; intake flagged for confirmation)
- **Age band:** 30–39 (37)
- **Sex:** not specified at intake — downstream sex-specific dosing or contraindications would need to be re-checked when known
- **Biomarkers (intake state):**
    - **KRAS A59T** mutated by tumor NGS — *ngs_pending* for VAF / clonality and full extended-RAS clearance; the dominant uncertainty axis on the case
    - **PIK3CA M1043I** mutated by tumor NGS — *ngs_pending* for somatic vs germline + clonal-VAF confirmation; kinase-domain activating allele, ALASCCA Group A by exon-20 position
    - **APC E1295** mutated by tumor NGS — *ngs_pending* for exact substitution (E1295* vs E1295fs vs missense) and second-allele status; mutation cluster region position
    - **TP53 R273** hotspot — *ngs_pending* for exact substitution (R273H vs C vs L vs S vs P); gain-of-function alleles have distinct pharmacology
    - **SMAD4 R361H** MH2-domain hotspot — *ngs_pending*; loss-of-function consistent with peritoneal-spread biology
    - **20q11 amplification (BCL2L1 / TOP1 co-amplified)** — *ngs_pending* for segment boundary
    - **MSI status:** MSS — *confirmed*
    - **TMB:** low — *confirmed* (exact mut/Mb value and panel-definition needed for the ≥10 mut/Mb pembrolizumab label gate)
    - **PD-L1:** negative — *confirmed* (IHC clone + CPS value needed for combination-trial stratification)
    - **HER2 (ERBB2) amplification:** *not performed / not reported* — the single most-actionable target check not yet done
    - **BRAF V600E:** *not explicitly reported* — must be excluded to scope BEACON and the encorafenib-cetuximab door
    - **NRAS / HRAS:** *not explicitly reported* — full extended-RAS clearance is a parallel anti-EGFR gate
    - **CMS / CDX2:** *not reported* — SMAD4 loss + peritoneal phenotype raises the prior for CMS4 (mesenchymal)
    - **Germline hereditary cancer panel:** negative — confirmed; POLE / POLD1 proofreading-domain coverage worth verifying given the 37yo early-onset bracket
- **Prior therapy:** liver metastasectomy; 1L FOLFIRI + bevacizumab in progress
- **Current therapy:** FOLFIRI + bevacizumab; planned cytoreductive surgery + HIPEC after systemic-therapy completion

## Preferences

- **Efficacy/toxicity weight:** 0.70 (moderate efficacy lean)
- **Toxicity vetoes:** none
- **Modality constraints:** none
- **Free text:** *"Auto-mode intake: surface the full option space — standard of care, off-label rational combinations, clinical trials, and compassionate-use pathways. No modality vetoes and no hard toxicity vetoes beyond standard clinical reasonableness. Treat the planned cytoreductive-surgery-plus-HIPEC window as a sequencing constraint. Sex not specified at intake; downstream agents should flag if their recommendation depends on sex-specific dosing or contraindications. Primary tumor resection status not specified — flag as a gap. ECOG 1 is an assumption from current FOLFIRI tolerance and should be confirmed."*
- **Trials preferred:** yes

<!-- libby:target-validation:begin -->

## Target validation paths

Seven essential gates and four high-priority workups have to land before the rest of the ranking moves from biomarker-conditional to actionable: comprehensive tissue NGS (FoundationOne CDx or equivalent) returns KRAS A59T variant allele fraction plus full extended-RAS clearance, BRAF V600, ERBB2 amplification, PIK3CA M1043I clonality, TP53 R273 substitution, SMAD4, and the 20q segment boundary; HER2 IHC/FISH per HERACLES is the most-actionable target check not yet done and gates trastuzumab deruxtecan via NCT04744831 (RAS-mutant-allowed) plus the RAS-WT-restricted tucatinib + trastuzumab door via MOUNTAINEER-03 (NCT05253651); MMR IHC orthogonal to NGS-MSI closes the ICI door definitively rather than presumptively; TMB in mut/Mb with the panel definition documented locks the tumor-agnostic pembrolizumab gate; PD-L1 IHC with clone + CPS covers combination-trial stratification; DPYD and UGT1A1 germline genotyping land the March 2024 FDA fluoropyrimidine label update and the 2026 NCCN recommendation; Signatera tumor-informed baseline before CRS gives the lead-time signal for peritoneal recurrence after surgery. None of this requires a new biopsy. All seven essential gates can run in parallel off the archival FFPE block plus a peripheral blood draw plus a pre-CRS Signatera tube.

### KRAS A59T

Essential: comprehensive tissue NGS (FoundationOne CDx, Tempus xT CDx, Caris MI Cancer Seek, or MSK-IMPACT) with explicit KRAS A59T variant allele fraction, full extended RAS coverage (KRAS / NRAS exons 2/3/4, HRAS), and an explicit BRAF V600 call. A59 substitutions are recognized RAS-pathway activating alterations and current NCCN consensus treats them as resistance variants for anti-EGFR therapy, but Lochhead 2018 reported a -36% target-lesion change on panitumumab + FOLFIRI in a single A59T tumor and Arena 2021 characterized A59 alleles as showing weaker MAPK signaling than canonical G12 mutants. A clean VAF, a fully resolved extended RAS, and a documented BRAF V600 status are the only way to scope cetuximab / panitumumab and BEACON (encorafenib + cetuximab) eligibility for this patient. The same panel returns ERBB2 amplification, MSI by NGS, TMB in mut/Mb, and the PIK3CA / APC / TP53 / SMAD4 confirmations every downstream row depends on. Turnaround 2-3 weeks; archival FFPE from the resected liver metastasis or the primary is sufficient.

Essential: HER2 IHC (clone 4B5 or HercepTest) with reflex dual-probe FISH per MOUNTAINEER / HERACLES scoring (IHC 3+ in >50% of cells, or IHC 2+ with HER2:CEP17 ratio ≥2.0). HER2 amplification covers another 3-5% of mCRC and is the single most-actionable target check not yet done on this case. A positive return routes trastuzumab deruxtecan via DESTINY-CRC02 (NCT04744831, ORR ~38% including RAS-mutant under the 2024 pan-tumor accelerated approval); the MOUNTAINEER tucatinib + trastuzumab door is RAS-WT-restricted by label and the A59T patient is closed out regardless of HER2 status. Order the IHC first; FISH only runs if the IHC reads 2+ equivocal. Turnaround 5-10 business days.

Low priority: documentation review of the existing negative multi-gene germline panel to confirm POLE / POLD1 proofreading-domain coverage (POLE P286R / V411L hotspots). A 37-year-old sits in the early-onset bracket where polymerase-proofreading deficiency is on the differential even at TMB-low; if the prior panel did not specifically cover the proofreading exonuclease domain, a focused add-on is warranted. Otherwise this is a chart-review row.

### TP53 R273

Essential: explicit TP53 R273 substitution call (R273H vs R273C vs R273L vs R273S vs R273P) from the comprehensive NGS report. R273H and R273C have the strongest preclinical APR-246 / eprenetapopt and arsenic-trioxide reactivation data, R273L is intermediate, and R273S is a less-studied DNA-contact variant. The eprenetapopt solid-tumor program is effectively closed after Park 2022 posted 2 PRs / 24 evaluable, and PYNNACLE rezatapopt is Y220C-binding-pocket-restricted and additionally KRAS-WT-only by protocol so this patient is structurally ineligible regardless of the R273 sub-call. Resolving the substitution is still load-bearing because it sharpens any future ATR / WEE1 / HSP90 synthetic-lethal trial discussion at recurrence. Comes off the master NGS report; the action is to request the lab to call the substitution explicitly rather than abbreviating to a generic 'p.R273'.

Low priority: confirmation that no co-occurring TP53 Y220C variant is present on the existing NGS report. Most TP53-mutant CRC tumors carry a single dominant alteration; PYNNACLE requires Y220C plus KRAS wild-type, and the case fails the KRAS-WT gate regardless, but the rule-out is documented so the trial screener does not waste time on it.

### MSS / TMB-low / PD-L1-negative

Essential: MMR protein IHC four-antibody panel (MLH1, MSH2, MSH6, PMS2) on archival FFPE, paired with the NGS-derived MSIsensor or MANTIS score from the master panel. MSS by a single method misses the rare but real discordant case where NGS-MSI or IHC alone calls a tumor MSS that the orthogonal method calls MSI-H (concordance ~95%, discordance ~5%). Confirming MSS by both methods closes the ICI door definitively rather than presumptively, which matters because MSI-H mCRC has a 44% ORR with pembrolizumab and would reorder the entire decision tree. Turnaround 5-7 business days; the IHC is a low-cost defensive call that the comprehensive NGS does not substitute for.

Essential: explicit TMB value in mutations per megabase from the comprehensive NGS report, with the panel definition and threshold documented. The intake says 'TMB-low' without the numeric value, and 8-9 mut/Mb closes the door while 10-12 opens the tumor-agnostic pembrolizumab label. Each panel uses a slightly different bait region and counting rule (FoundationOne CDx 0.8 Mb of CDS; Tempus xT 2.4 Mb reportable; MSK-IMPACT 1.06 Mb), so the panel name and threshold travel with the number. Bundled with the master NGS.

Essential: PD-L1 IHC with explicit clone (22C3, SP263, or 28-8) and explicit scoring system (CPS for mCRC). 'Negative' without a clone or scoring system is not interpretable for trial eligibility because different ICI labels and combination studies use different cutoffs and antibodies. Several MSS-mCRC combination ICI trials use PD-L1 CPS thresholds for stratification rather than for hard exclusion, so the exact CPS value still matters even when the headline result is negative. Default to 22C3 with CPS scoring for CRC context.

Medium priority: high-resolution HLA-A typing (4-digit) plus full class-I and class-II profile on peripheral blood. MSS / TMB-low mCRC is the population where HLA-restricted TCR-T (afami-cel, lete-cel, IMA203) and ImmTAC (brenetafusp) trials are most often considered; HLA-A*02:01 is the dominant restriction. Bank the result before the HIPEC procedure even if no TCR-T trial is in immediate play; the result lasts for life and removes friction from any future referral.

### Peritoneal carcinomatosis

Essential: DPYD genotyping for the four CPIC-recommended variants (c.1905+1G>A / *2A, c.1679T>G / *13, c.2846A>T, c.1236G>A / HapB3) on peripheral whole blood. The March 2024 FDA fluoropyrimidine label update and the 2026 NCCN colon guideline both advise pre-treatment testing. The patient is already on FOLFIRI and has tolerated cycles, which lowers but does not eliminate the value: heterozygous carriers of c.2846A>T or HapB3 can show progressive cumulative toxicity, and the HIPEC-window dose decision plus any future capecitabine maintenance both benefit from a documented genotype.

High priority: UGT1A1 *6 and *28 genotyping bundled with DPYD on a single pharmacogenomic order. *28/*28 (and *6/*28 in Asian ancestry) confers a 3-4x increased risk of severe irinotecan-related neutropenia and diarrhea, and the FDA irinotecan label recommends a starting-dose reduction in homozygotes. Pre-resolves the irinotecan-HIPEC question if that perfusate route enters discussion.

High priority: Signatera tumor-informed serial ctDNA MRD at three peri-HIPEC timepoints (pre-CRS baseline, post-operative day 30-60, then every 8-12 weeks). Peritoneal-spread CRC is one of the settings where ctDNA MRD is most predictive: pre-CRS ctDNA detection correlates with shorter PFS and identifies patients who may benefit more from extended systemic therapy than from upfront cytoreduction. Signatera carries Medicare coverage for stage II-IV CRC MRD surveillance and the tumor-informed bespoke design (16 patient-specific variants from WES) gives the best low-tumor-fraction sensitivity; Guardant Reveal is the tumor-naive alternative if faster start outweighs sensitivity. The bespoke build runs 4-6 weeks, so the order has to land BEFORE CRS for the baseline draw to be interpretable.

Medium priority: serum CEA, CA 19-9, and CA 125 at baseline and at each peri-HIPEC interval. CA 125 elevation correlates with peritoneal carcinomatosis burden and tracks response and recurrence independently of CEA. Together they give a low-cost peri-HIPEC response signal that complements ctDNA and imaging. Pull all three at every routine draw rather than CEA alone; the marginal cost is negligible.

### BCL2L1 / TOP1 (20q11)

High priority: 20q amplification segment definition (20q11.21 BCL2L1 / TOP1 vs extended 20q13 ZNF217 / MYBL2 / AURKA) from the existing NGS copy-number plot, with optional confirmatory FISH or OncoScan if the NGS boundaries are ambiguous. 20q11.21-restricted amplification centered on BCL2L1 (BCL-xL) and TOP1 is biologically distinct from broad 20q gain: the BCL2L1 subset supports BH3-mimetic / BCL-xL-degrader rationale (navitoclax solid-tumor program discontinued; DT2216 pediatric-only trial) and the TOP1 amplification correlates with irinotecan sensitivity, while the broader 20q gain raises AURKA-class trial questions instead. No new sample needed in most cases; the action is on interpreting the existing CNV plot. If the report flags 20q amplification without segment boundaries, request a CNV-segment annotation from the lab or reflex to OncoScan.

### SMAD4 R361H

High priority: consensus molecular subtype (CMS1-4) by transcriptomic classifier (CRCassigner / CMScaller from RNA-seq) plus CDX2 IHC and the ZEB1 / HTR2B / FRMD6 / pan-cytokeratin IHC surrogate panel when RNA-seq is not available. Peritoneal-dominant disease with SMAD4 loss raises the prior for CMS4 (mesenchymal) classification, which has a worse prognosis but identifies patients with a TGF-beta-mediated immune-excluded phenotype and a different combination-therapy landscape than CMS2 / CMS3. The IHC surrogate panel achieves 87% concordance with transcriptomic CMS and is the practical clinical-lab path when full RNA-seq is unavailable. Best value if Caris MI Cancer Seek is already used as the master comprehensive panel since CMS comes off the whole-transcriptome data.

Medium priority: SMAD4 (DPC4) IHC (clone B-8 or EP618Y) on archival FFPE. R361H sits in the MH2 DNA-binding domain and is a known loss-of-function hotspot; SMAD4 IHC loss is the protein-level orthogonal confirmation that the molecular call translates to absent nuclear SMAD4. Cheap defensive call rather than a gating one; pair on a single block release with the MMR IHC.

Low priority: spatial multiplex immune profile of TIL density, CD3 / CD8 distribution, FAP+ stromal CAF density, and pSMAD2/3 in the peritumoral stroma (Akoya PhenoCycler / Lunaphore platform). SMAD4 loss plus a CMS4 phenotype is the canonical TGF-beta-driven immune-excluded state where CD8+ T cells are stuck at the invasive margin behind a FAP+ CAF stromal collar. A multiplex profile separates 'cold' from 'excluded' cases and sharpens any anti-TGF-beta + ICI combination-trial discussion. Research-grade; reserve for the moment a TGF-beta-axis or stromal-targeting protocol enters serious discussion.

### APC E1295

Medium priority: exact APC codon-1295 variant type (E1295* nonsense vs E1295fs frameshift vs missense) and position relative to the mutation cluster region (MCR, codons 1250-1500), with second-allele status (LOH vs second truncating event) from the existing NGS report. Codon 1295 sits within the MCR; truncating events in the MCR retain partial beta-catenin binding but lose the SAMP repeats needed for downregulation, and bi-allelic MCR truncation is the typical 'just right' Wnt-pathway state most studied for Wnt-axis drug rationale. The variant call and second-allele status decide whether this case is a strong candidate for Wnt-pathway investigational trials (PORCN inhibitors, tankyrase inhibitors, frizzled antibodies) or a weak one. No new sample; request the lab to explicitly call the variant type and the second-allele state, both of which sit in the raw VCF but are sometimes summarized.

### Where to order these assays

| Assay | Provider | Decision gated | Contact |
|---|---|---|---|
| **Comprehensive tissue NGS (KRAS A59T VAF + extended RAS + BRAF V600 + ERBB2 + PIK3CA + TP53 R273 + SMAD4 + 20q + TMB)** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Anti-EGFR (cetuximab, panitumumab) and BEACON (encorafenib + cetuximab) eligibility; resolves the dominant first-question gate on systemic-therapy options.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| Comprehensive tissue NGS | Tempus Labs *(Tempus xT CDx)* | Anti-EGFR (cetuximab, panitumumab) and BEACON (encorafenib + cetuximab) eligibility; resolves the dominant first-question gate on systemic-therapy options. | [test info](https://www.tempus.com/oncology/genomic-profiling/xt-xr/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| Comprehensive tissue NGS | Caris Life Sciences *(MI Cancer Seek)* | Anti-EGFR (cetuximab, panitumumab) and BEACON (encorafenib + cetuximab) eligibility; resolves the dominant first-question gate on systemic-therapy options. | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 1-888-979-8669 |
| Comprehensive tissue NGS | NeoGenomics Laboratories *(NeoTYPE Comprehensive Tumor Profile)* | Anti-EGFR (cetuximab, panitumumab) and BEACON (encorafenib + cetuximab) eligibility; resolves the dominant first-question gate on systemic-therapy options. | [test info](https://neogenomics.com/test-menu/comprehensive-genomic-profiling) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| Comprehensive tissue NGS | Memorial Sloan Kettering Diagnostic Molecular Pathology *(MSK-IMPACT)* | Anti-EGFR (cetuximab, panitumumab) and BEACON (encorafenib + cetuximab) eligibility; resolves the dominant first-question gate on systemic-therapy options. | [test info](https://www.mskcc.org/clinical-services/pathology/molecular-diagnostics) · 1275 York Avenue, New York, NY 10065 · 1-212-639-2000 |
| **HER2 (ERBB2) IHC clone 4B5 / HercepTest with reflex dual-probe FISH per HERACLES** | **NeoGenomics Laboratories *(preferred)* (HER2 IHC + FISH (HERACLES/MOUNTAINEER scoring available))** | **Tucatinib + trastuzumab (MOUNTAINEER label, RAS-WT only), trastuzumab deruxtecan off-label, HERACLES regimens, and MOUNTAINEER-03 first-line study (NCT05253651).** | **[test info](https://neogenomics.com/test-menu/her2-erbb2-ihc-and-fish) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| HER2 IHC + reflex FISH | Mayo Clinic Laboratories *(HER2 IHC + Dual-Probe FISH)* | Tucatinib + trastuzumab (MOUNTAINEER label, RAS-WT only), trastuzumab deruxtecan off-label, HERACLES regimens, and MOUNTAINEER-03 first-line study (NCT05253651). | [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 |
| HER2 IHC + reflex FISH | Labcorp *(HER2/ERBB2 IHC with Reflex FISH)* | Tucatinib + trastuzumab (MOUNTAINEER label, RAS-WT only), trastuzumab deruxtecan off-label, HERACLES regimens, and MOUNTAINEER-03 first-line study (NCT05253651). | [test info](https://www.labcorp.com/tests/480080/her2-erbb2-immunohistochemistry-and-fish-reflex) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| HER2 IHC + reflex FISH | Quest Diagnostics *(HER2 IHC + FISH)* | Tucatinib + trastuzumab (MOUNTAINEER label, RAS-WT only), trastuzumab deruxtecan off-label, HERACLES regimens, and MOUNTAINEER-03 first-line study (NCT05253651). | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| **MMR protein IHC four-antibody panel (MLH1, MSH2, MSH6, PMS2) plus NGS-MSI orthogonal** | **NeoGenomics Laboratories *(preferred)* (MMR IHC Panel (MLH1/MSH2/MSH6/PMS2))** | **Single-agent and dual-agent ICI (pembrolizumab, dostarlimab, nivolumab + ipilimumab); reverses entire treatment paradigm if MSI-H by either method.** | **[test info](https://neogenomics.com/test-menu/mismatch-repair-mmr-ihc-panel) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| MMR protein IHC | Mayo Clinic Laboratories *(MMR Protein IHC)* | Single-agent and dual-agent ICI (pembrolizumab, dostarlimab, nivolumab + ipilimumab); reverses entire treatment paradigm if MSI-H by either method. | [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 |
| MMR protein IHC | Labcorp *(MMR Protein IHC)* | Single-agent and dual-agent ICI (pembrolizumab, dostarlimab, nivolumab + ipilimumab); reverses entire treatment paradigm if MSI-H by either method. | [test info](https://www.labcorp.com/tests/480039/mismatch-repair-protein-ihc-mlh1-msh2-msh6-pms2) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| MMR protein IHC | Quest Diagnostics *(MMR Protein IHC Panel)* | Single-agent and dual-agent ICI (pembrolizumab, dostarlimab, nivolumab + ipilimumab); reverses entire treatment paradigm if MSI-H by either method. | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| **TMB explicit mut/Mb value with panel + threshold documented** | **Foundation Medicine *(preferred)* (FoundationOne CDx (FDA-labeled TMB-H companion diagnostic))** | **Tumor-agnostic pembrolizumab eligibility (TMB-H ≥10 mut/Mb label).** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| TMB explicit mut/Mb | Tempus Labs *(Tempus xT CDx)* | Tumor-agnostic pembrolizumab eligibility (TMB-H ≥10 mut/Mb label). | [test info](https://www.tempus.com/oncology/genomic-profiling/xt-xr/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| TMB explicit mut/Mb | Caris Life Sciences *(MI Cancer Seek)* | Tumor-agnostic pembrolizumab eligibility (TMB-H ≥10 mut/Mb label). | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 1-888-979-8669 |
| **PD-L1 IHC with explicit clone (22C3 / SP263 / 28-8) and explicit scoring (CPS for CRC)** | **NeoGenomics Laboratories *(preferred)* (PD-L1 22C3 pharmDx (CPS) and SP263 (TPS))** | **ICI combination trial stratification and any PD-L1-conditioned MSS-CRC ICI regimen.** | **[test info](https://neogenomics.com/test-menu/pd-l1-22c3-pharmdx) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| PD-L1 IHC | Mayo Clinic Laboratories *(PD-L1 22C3 / SP263 / 28-8 IHC)* | ICI combination trial stratification and any PD-L1-conditioned MSS-CRC ICI regimen. | [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 |
| PD-L1 IHC | Labcorp *(PD-L1 22C3 IHC)* | ICI combination trial stratification and any PD-L1-conditioned MSS-CRC ICI regimen. | [test info](https://www.labcorp.com/tests/483675/pd-l1-22c3-immunohistochemistry) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| PD-L1 IHC | Quest Diagnostics *(PD-L1 IHC)* | ICI combination trial stratification and any PD-L1-conditioned MSS-CRC ICI regimen. | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| **DPYD four-variant CPIC genotyping (*2A, *13, c.2846A>T, HapB3)** | **Mayo Clinic Laboratories *(preferred)* (DPYD Genotype (test code DPYDZ))** | **Fluoropyrimidine dose adjustment for ongoing FOLFIRI and any future capecitabine maintenance.** | **[test info](https://www.mayocliniclabs.com/test-catalog/Overview/65167) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710** |
| DPYD genotyping | Labcorp *(DPYD Genotyping)* | Fluoropyrimidine dose adjustment for ongoing FOLFIRI and any future capecitabine maintenance. | [test info](https://www.labcorp.com/tests/451850/dihydropyrimidine-dehydrogenase-dpyd-genotyping) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| DPYD genotyping | Quest Diagnostics *(DPYD Genotype)* | Fluoropyrimidine dose adjustment for ongoing FOLFIRI and any future capecitabine maintenance. | [test info](https://testdirectory.questdiagnostics.com/test/test-detail/93408/dpyd-genotype) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| DPYD genotyping | ARUP Laboratories *(DPYD Genotyping, 5 Variants)* | Fluoropyrimidine dose adjustment for ongoing FOLFIRI and any future capecitabine maintenance. | [test info](https://ltd.aruplab.com/Tests/Pub/2013661) · 500 Chipeta Way, Salt Lake City, UT 84108 · 1-800-522-2787 |
| **UGT1A1 *6 / *28 genotyping (TA repeat polymorphism)** | **Mayo Clinic Laboratories *(preferred)* (UGT1A1 Genotyping (test code UGTGT))** | **Irinotecan dose adjustment in FOLFIRI and any irinotecan-based HIPEC protocol.** | **[test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710** |
| UGT1A1 genotyping | Labcorp *(UGT1A1 Genotype)* | Irinotecan dose adjustment in FOLFIRI and any irinotecan-based HIPEC protocol. | [test info](https://www.labcorp.com/tests/511135/ugt1a1-genotype) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| UGT1A1 genotyping | Quest Diagnostics *(UGT1A1 Genotype)* | Irinotecan dose adjustment in FOLFIRI and any irinotecan-based HIPEC protocol. | [test info](https://testdirectory.questdiagnostics.com/test/test-detail/14618/ugt1a1-genotype) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 |
| UGT1A1 genotyping | ARUP Laboratories *(UGT1A1 (TA)n Repeat)* | Irinotecan dose adjustment in FOLFIRI and any irinotecan-based HIPEC protocol. | [test info](https://ltd.aruplab.com/Tests/Pub/0051450) · 500 Chipeta Way, Salt Lake City, UT 84108 · 1-800-522-2787 |
| **Tumor-informed serial ctDNA MRD bracketing CRS-HIPEC** | **Natera *(preferred)* (Signatera (tumor-informed ctDNA MRD))** | **Peri-HIPEC recurrence surveillance; informs adjuvant-therapy duration after cytoreductive surgery + HIPEC.** | **[test info](https://www.natera.com/oncology/signatera-advanced-cancer-detection/) · 13011 McCallen Pass, Building A, Austin, TX 78753 · 1-650-249-9090** |
| Tumor-informed ctDNA MRD | Guardant Health *(Guardant Reveal (tumor-naive MRD))* | Peri-HIPEC recurrence surveillance; informs adjuvant-therapy duration after cytoreductive surgery + HIPEC. | [test info](https://guardanthealth.com/products/guardant-reveal/) · 505 Penobscot Drive, Redwood City, CA 94063 · 1-855-698-8887 |
| Tumor-informed ctDNA MRD | Foundation Medicine *(FoundationOne Tracker)* | Peri-HIPEC recurrence surveillance; informs adjuvant-therapy duration after cytoreductive surgery + HIPEC. | [test info](https://www.foundationmedicine.com/test/foundationone-tracker) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 |
| Tumor-informed ctDNA MRD | Tempus Labs *(Tempus xM)* | Peri-HIPEC recurrence surveillance; informs adjuvant-therapy duration after cytoreductive surgery + HIPEC. | [test info](https://www.tempus.com/oncology/genomic-profiling/xm/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| **CMS transcriptomic classifier (or IHC surrogate panel)** | **Caris Life Sciences *(preferred)* (MI Cancer Seek (WES + WTS, CMS classification on whole-transcriptome RNA))** | **TGF-beta-axis / mesenchymal-targeting trial selection; CMS4 prognostic stratification; CDX2-negative HR-poor subgroup identification.** | **[test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 1-888-979-8669** |
| CMS classifier | Tempus Labs *(Tempus xR (RNA sequencing))* | TGF-beta-axis / mesenchymal-targeting trial selection; CMS4 prognostic stratification; CDX2-negative HR-poor subgroup identification. | [test info](https://www.tempus.com/oncology/genomic-profiling/xr/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| CMS classifier | NeoGenomics Laboratories *(CDX2 IHC (plus ZEB1, HTR2B, FRMD6, pan-cytokeratin for the IHC-CMS surrogate))* | TGF-beta-axis / mesenchymal-targeting trial selection; CMS4 prognostic stratification; CDX2-negative HR-poor subgroup identification. | [test info](https://neogenomics.com/test-menu/cdx2-stain) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| **SMAD4 (DPC4) IHC** | **NeoGenomics Laboratories *(preferred)* (SMAD4 (DPC4) IHC)** | **Confirms SMAD4-loss phenotype underpinning CMS4 / mesenchymal interpretation and TGF-beta-axis trial discussion.** | **[test info](https://neogenomics.com/test-menu/smad4-dpc4-stain) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907** |
| SMAD4 IHC | Mayo Clinic Laboratories *(SMAD4 IHC)* | Confirms SMAD4-loss phenotype underpinning CMS4 / mesenchymal interpretation and TGF-beta-axis trial discussion. | [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 |
| SMAD4 IHC | Labcorp *(SMAD4 IHC)* | Confirms SMAD4-loss phenotype underpinning CMS4 / mesenchymal interpretation and TGF-beta-axis trial discussion. | [test info](https://www.labcorp.com/) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| **20q amplification segment definition (20q11.21 BCL2L1 / TOP1 vs extended 20q13)** | **Foundation Medicine *(preferred)* (FoundationOne CDx (copy-number plot))** | **BCL-xL-directed strategy framing (navitoclax, DT2216) and 20q13-driven AURKA-class trial framing; refines the irinotecan-sensitivity rationale on top of TOP1.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| 20q segment definition | Tempus Labs *(Tempus xT (segment-level CNV))* | BCL-xL-directed strategy framing (navitoclax, DT2216) and 20q13-driven AURKA-class trial framing; refines the irinotecan-sensitivity rationale on top of TOP1. | [test info](https://www.tempus.com/oncology/genomic-profiling/xt-xr/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| 20q segment definition | NeoGenomics Laboratories *(OncoScan CNV Plus)* | BCL-xL-directed strategy framing (navitoclax, DT2216) and 20q13-driven AURKA-class trial framing; refines the irinotecan-sensitivity rationale on top of TOP1. | [test info](https://neogenomics.com/test-menu/oncoscan-cnv-plus-assay) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| **High-resolution HLA-A typing (4-digit) plus full class-I / class-II profile** | **Labcorp *(preferred)* (HLA A, B, C, DRB1 Profile (High Resolution))** | **HLA-restricted TCR-T (afami-cel, lete-cel, IMA203) and ImmTAC / soluble-TCR (brenetafusp, IMC-P115C) trial eligibility.** | **[test info](https://www.labcorp.com/tests/176076/hla-a-b-c-drb1-profile-high-resolution) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167** |
| HLA-A typing | Histogenetics *(HLA Class I/II High-Resolution Sanger / NGS Typing)* | HLA-restricted TCR-T (afami-cel, lete-cel, IMA203) and ImmTAC / soluble-TCR (brenetafusp, IMC-P115C) trial eligibility. | [test info](https://www.histogenetics.com/) · 300 Executive Boulevard, Ossining, NY 10562 · 1-914-762-1600 |
| HLA-A typing | Discovery Life Sciences *(Clinical Trial HLA Typing)* | HLA-restricted TCR-T (afami-cel, lete-cel, IMA203) and ImmTAC / soluble-TCR (brenetafusp, IMC-P115C) trial eligibility. | [test info](https://dls.com/clinical-trial-hla-typing-services/) · 2904 Beech Court NW, Huntsville, AL 35805 · 1-256-705-4060 |
| **Serum CEA, CA 19-9, and CA 125 baseline + serial** | **Quest Diagnostics *(preferred)* (CEA / CA 19-9 / CA 125 Serum Panels)** | **Peri-HIPEC biochemical surveillance; CA 125 specifically tracks peritoneal-disease burden.** | **[test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378** |
| Tumor markers | Labcorp *(CEA / CA 19-9 / CA 125 Serum Markers)* | Peri-HIPEC biochemical surveillance; CA 125 specifically tracks peritoneal-disease burden. | [test info](https://www.labcorp.com/) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 |
| Tumor markers | Mayo Clinic Laboratories *(CEA / CA 19-9 / CA 125)* | Peri-HIPEC biochemical surveillance; CA 125 specifically tracks peritoneal-disease burden. | [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 |
| **APC E1295 variant resolution + second-allele status** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Wnt-axis investigational trial fit (PORCN, tankyrase, frizzled / WNT974 / LGK974-class).** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639** |
| APC E1295 variant resolution | Tempus Labs *(Tempus xT CDx)* | Wnt-axis investigational trial fit (PORCN, tankyrase, frizzled / WNT974 / LGK974-class). | [test info](https://www.tempus.com/oncology/genomic-profiling/xt-xr/) · 600 W Chicago Avenue, Chicago, IL 60654 · 1-800-739-4137 |
| APC E1295 variant resolution | Caris Life Sciences *(MI Cancer Seek)* | Wnt-axis investigational trial fit (PORCN, tankyrase, frizzled / WNT974 / LGK974-class). | [test info](https://www.carislifesciences.com/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 1-888-979-8669 |
| **Spatial multiplex immune profile (TIL, CD3/CD8, FAP CAF, pSMAD2/3)** | **Akoya Biosciences *(preferred)* (PhenoCycler-Fusion / Phenoptics multiplex IHC)** | **Anti-TGF-beta + ICI combination trial selection (bintrafusp alfa-class, NIS793, BCA101).** | **[test info](https://www.akoyabio.com/services/) · 100 Campus Drive, 6th Floor, Marlborough, MA 01752 · 1-855-896-8401** |
| Spatial multiplex immune profile | NeoGenomics Laboratories *(MultiOmyx Multiplex IHC)* | Anti-TGF-beta + ICI combination trial selection (bintrafusp alfa-class, NIS793, BCA101). | [test info](https://neogenomics.com/test-menu/multiomyx) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 |
| **Hereditary cancer panel POLE / POLD1 proofreading-domain coverage review** | **Labcorp Genetics (formerly Invitae) *(preferred)* (Invitae Common Hereditary Cancers Panel (POLE/POLD1 included))** | **Polymerase-proofreading polyposis surveillance and family cascade decisions; downstream tumor-agnostic ICI rationale if POLE proofreading deficiency is uncovered.** | **[test info](https://www.invitae.com/providers/test-catalog/test-01101) · 1400 16th Street, San Francisco, CA 94103 · 1-800-436-3037** |
| Hereditary cancer panel review | GeneDx *(GeneDx Comprehensive Common Cancer Panel)* | Polymerase-proofreading polyposis surveillance and family cascade decisions; downstream tumor-agnostic ICI rationale if POLE proofreading deficiency is uncovered. | [test info](https://www.genedx.com/tests/detail/comprehensive-common-cancer-panel-883) · 207 Perry Parkway, Gaithersburg, MD 20877 · 1-888-729-1206 |
| Hereditary cancer panel review | Ambry Genetics *(CancerNext-Expanded)* | Polymerase-proofreading polyposis surveillance and family cascade decisions; downstream tumor-agnostic ICI rationale if POLE proofreading deficiency is uncovered. | [test info](https://www.ambrygen.com/) · 15 Argonaut, Aliso Viejo, CA 92656 · 1-866-262-7943 |

### Biomarker plan

| Recommended assay | Rationale | Suggested assay provider | Tissue requirements |
|---|---|---|---|
| Comprehensive tissue NGS (KRAS A59T VAF + extended RAS + BRAF V600 + ERBB2 + PIK3CA + TP53 R273 + SMAD4 + 20q + TMB mut/Mb) | A59 substitutions are recognized RAS-pathway activating alterations and current NCCN consensus treats them as resistance variants for anti-EGFR therapy; a clean VAF and a fully resolved extended RAS plus BRAF V600 are the only way to scope cetuximab / panitumumab and BEACON eligibility. The same panel returns ERBB2 amplification, MSI by NGS, TMB in mut/Mb, and the PIK3CA / APC / TP53 / SMAD4 confirmations the downstream rows depend on. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | 1 FFPE block or 15-20 unstained slides; archival acceptable from resected liver met or primary |
| HER2 (ERBB2) IHC clone 4B5 with reflex dual-probe FISH per HERACLES | HER2 amplification covers another 3-5% of mCRC and is the single most-actionable target check not yet done; a positive return routes trastuzumab deruxtecan via DESTINY-CRC02 (NCT04744831, ORR ~38% including RAS-mutant under the 2024 pan-tumor accelerated approval). MOUNTAINEER tucatinib + trastuzumab is RAS-WT-restricted by label so the A59T patient is closed out regardless of HER2 status. Order IHC first; FISH reflexes if 2+ equivocal. | NeoGenomics Laboratories *(HER2 IHC + FISH HERACLES/MOUNTAINEER scoring)* · [test info](https://neogenomics.com/test-menu/her2-erbb2-ihc-and-fish) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | 2-3 unstained slides from archival FFPE |
| TP53 R273 specific amino acid substitution call | R273H and R273C have the strongest preclinical APR-246 reactivation data; R273L is intermediate; R273S is less-studied. PYNNACLE rezatapopt is Y220C-restricted and KRAS-WT-only so the patient is structurally ineligible regardless, but the substitution call sharpens any future ATR / WEE1 / HSP90 synthetic-lethal trial discussion at recurrence. | Foundation Medicine *(FoundationOne CDx TP53 codon 273 amino acid call)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | shared with master NGS block |
| MMR protein IHC four-antibody panel (MLH1 / MSH2 / MSH6 / PMS2) | MSS by a single method misses the rare but real discordant case where NGS-MSI or IHC alone calls a tumor MSS that the orthogonal method calls MSI-H (concordance ~95%, discordance ~5%). Confirming MSS by both methods closes the ICI door definitively rather than presumptively; a discordant MSI-H call reverses the entire decision tree. | NeoGenomics Laboratories *(MMR IHC Panel)* · [test info](https://neogenomics.com/test-menu/mismatch-repair-mmr-ihc-panel) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | 1-2 unstained slides from archival FFPE |
| TMB explicit value in mutations per megabase with panel and threshold documented | Intake says 'TMB-low' without a number, and 8-9 mut/Mb closes the tumor-agnostic pembrolizumab door while 10-12 opens it. Each panel uses a slightly different bait region and counting rule so the panel name and threshold travel with the number. The FDA label cites FoundationOne CDx specifically for the TMB-H call. | Foundation Medicine *(FoundationOne CDx FDA-labeled TMB-H companion diagnostic)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | shared with master NGS block |
| PD-L1 IHC with explicit clone (22C3, SP263, or 28-8) and explicit scoring system (CPS for CRC) | 'Negative' without a clone or scoring system is not interpretable for trial eligibility; different ICI labels use different cutoffs and antibodies. Several MSS-mCRC combination ICI trials use PD-L1 CPS thresholds for stratification rather than hard exclusion, so the exact CPS value still matters even when the headline is negative. Default to 22C3 with CPS scoring for CRC context. | NeoGenomics Laboratories *(PD-L1 22C3 pharmDx CPS + SP263 TPS)* · [test info](https://neogenomics.com/test-menu/pd-l1-22c3-pharmdx) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | 1-2 unstained slides |
| DPYD four-variant CPIC genotyping (c.1905+1G>A / *2A, c.1679T>G / *13, c.2846A>T, c.1236G>A / HapB3) | March 2024 FDA fluoropyrimidine label update and 2026 NCCN colon guideline both advise pre-treatment testing. The patient is tolerating FOLFIRI now, but heterozygous c.2846A>T or HapB3 carriers can show progressive cumulative toxicity, and the HIPEC-window dose decision plus any future capecitabine maintenance both benefit from a documented genotype. | Mayo Clinic Laboratories *(DPYD Genotype DPYDZ)* · [test info](https://www.mayocliniclabs.com/test-catalog/Overview/65167) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 | 5 mL whole blood (EDTA) or buccal swab |
| UGT1A1 *6 / *28 genotyping | *28/*28 (and *6/*28 in Asian ancestry) confers a 3-4x increased risk of severe irinotecan-related neutropenia and diarrhea; the FDA irinotecan label recommends a starting-dose reduction in homozygotes. Bundle with DPYD on a single pharmacogenomic order. Pre-resolves the irinotecan-HIPEC question if that perfusate route enters discussion. | Mayo Clinic Laboratories *(UGT1A1 Genotyping UGTGT)* · [test info](https://www.mayocliniclabs.com/test-catalog/) · 3050 Superior Drive NW, Rochester, MN 55901 · 1-800-533-1710 | 5 mL whole blood (EDTA) or shared with DPYD order |
| 20q amplification segment definition (20q11.21 BCL2L1 / TOP1 vs extended 20q13) | 20q11.21-restricted amplification centered on BCL2L1 (BCL-xL) and TOP1 is biologically distinct from broad 20q gain that sweeps in 20q13. The BCL2L1 subset supports BH3-mimetic / BCL-xL-degrader rationale; TOP1 amplification correlates with irinotecan sensitivity; the broader 20q13 gain raises AURKA-class trial questions instead. Action is on interpreting the existing CNV plot; reflex to OncoScan only if segment boundaries are ambiguous. | Foundation Medicine *(FoundationOne CDx copy-number plot)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | shared with master NGS block |
| Tumor-informed serial ctDNA MRD bracketing CRS-HIPEC | Peritoneal-spread CRC is one of the settings where ctDNA MRD is most predictive; pre-CRS detection correlates with shorter PFS and identifies patients who may benefit more from extended systemic therapy than from upfront cytoreduction. Signatera has Medicare coverage in stage II-IV CRC and the tumor-informed bespoke design (16 patient-specific variants from WES) gives the best low-tumor-fraction sensitivity. Bespoke build runs 4-6 weeks; the order has to land BEFORE CRS for the baseline draw to be interpretable. | Natera *(Signatera tumor-informed ctDNA MRD)* · [test info](https://www.natera.com/oncology/signatera-advanced-cancer-detection/) · 13011 McCallen Pass, Building A, Austin, TX 78753 · 1-650-249-9090 | 5-10 mL plasma per draw; Signatera baseline also needs an FFPE block (can share the master NGS block) |
| CMS transcriptomic classifier (CRCassigner / CMScaller) or IHC surrogate panel (CDX2 + ZEB1 + HTR2B + FRMD6 + pan-cytokeratin) | Peritoneal-dominant disease with SMAD4 loss raises the prior for CMS4 (mesenchymal), which identifies patients with a TGF-beta-mediated immune-excluded phenotype and a different combination-therapy landscape than CMS2 / CMS3. The IHC surrogate achieves 87% concordance with transcriptomic CMS when full RNA-seq is unavailable. Best value if Caris MI Cancer Seek is the master panel since CMS comes off the whole-transcriptome data. | Caris Life Sciences *(MI Cancer Seek WES + WTS, CMS on whole-transcriptome RNA)* · [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Suite 100, Phoenix, AZ 85040 · 1-888-979-8669 | archival FFPE; 5-10 unstained slides for IHC surrogate |
| SMAD4 (DPC4) IHC (clone B-8 or EP618Y) | R361H is a known loss-of-function MH2-domain hotspot; SMAD4 IHC loss is the protein-level orthogonal confirmation that the molecular call translates to absent nuclear SMAD4. Cheap defensive call; pair on a single block release with the MMR IHC. | NeoGenomics Laboratories *(SMAD4 DPC4 IHC)* · [test info](https://neogenomics.com/test-menu/smad4-dpc4-stain) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 1-866-776-5907 | 1-2 unstained slides |
| High-resolution HLA-A typing (4-digit) plus full class-I / class-II profile | MSS / TMB-low mCRC is the population where HLA-restricted TCR-T (afami-cel, lete-cel, IMA203) and ImmTAC (brenetafusp) trials are most often considered; HLA-A*02:01 is the dominant restriction. Bank the result before HIPEC even if no TCR-T trial is in immediate play; the result lasts for life and removes friction from any future referral. | Labcorp *(HLA A B C DRB1 Profile High Resolution)* · [test info](https://www.labcorp.com/tests/176076/hla-a-b-c-drb1-profile-high-resolution) · 358 South Main Street, Burlington, NC 27215 · 1-800-845-6167 | 5-10 mL whole blood (EDTA) |
| Serum CEA, CA 19-9, and CA 125 baseline + serial | CA 125 elevation correlates with peritoneal carcinomatosis burden and tracks response and recurrence independently of CEA. Together with CA 19-9 they give a low-cost peri-HIPEC response signal that complements ctDNA and imaging. Pull all three at every routine draw rather than CEA alone; the marginal cost is negligible. | Quest Diagnostics *(CEA / CA 19-9 / CA 125 Serum Panels)* · [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 1-866-697-8378 | 3-5 mL serum per marker |
| APC E1295 variant resolution + second-allele status | Codon 1295 sits within the APC mutation cluster region (codons 1250-1500); truncating events in the MCR retain partial beta-catenin binding but lose the SAMP repeats needed for downregulation, and bi-allelic MCR truncation is the typical 'just right' Wnt-pathway state most studied for Wnt-axis drug rationale. Request the lab to explicitly call the variant type (nonsense / frameshift / missense) and the second-allele state. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | shared with master NGS block |
| Hereditary cancer panel POLE / POLD1 proofreading-domain coverage review | A 37-year-old with mCRC sits in the early-onset bracket where polymerase-proofreading deficiency (germline POLE / POLD1) is on the differential even at TMB-low. If the prior multi-gene panel did not specifically cover the POLE proofreading exonuclease domain and POLD1, a focused add-on is warranted; if it did, this is a documentation row. | Labcorp Genetics (formerly Invitae) *(Invitae Common Hereditary Cancers Panel POLE/POLD1 included)* · [test info](https://www.invitae.com/providers/test-catalog/test-01101) · 1400 16th Street, San Francisco, CA 94103 · 1-800-436-3037 | no new specimen unless add-on testing needed |
| TP53 Y220C co-mutation rule-out | Most TP53-mutant CRC tumors carry a single dominant alteration; the intake reports R273 only. PYNNACLE rezatapopt requires Y220C plus KRAS wild-type; the case fails the KRAS-WT gate regardless. Cheap to confirm there is no second hit at Y220C from the existing NGS report so the trial screener does not waste time on it. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 1-888-988-3639 | shared with master NGS block |
| Spatial multiplex immune profile (TIL, CD3 / CD8, FAP CAF, pSMAD2/3) | SMAD4 loss plus a CMS4 phenotype is the canonical TGF-beta-driven immune-excluded state where CD8+ T cells are stuck at the invasive margin behind a FAP+ CAF stromal collar. A multiplex profile separates 'cold' from 'excluded' cases and sharpens any anti-TGF-beta + ICI combination-trial discussion. Research-grade; reserve for the moment a TGF-beta-axis protocol enters serious discussion. | Akoya Biosciences *(PhenoCycler-Fusion multiplex IHC)* · [test info](https://www.akoyabio.com/services/) · 100 Campus Drive, 6th Floor, Marlborough, MA 01752 · 1-855-896-8401 | 1 FFPE block or 5-10 unstained slides |

---

*Decision support, not medical advice. Confirm assay availability and current standards with the treating team and the local pathology service.*

<!-- libby:target-validation:end -->

## Scope summary

59 trials surfaced, 61 clinical-evidence rows, 39 preclinical rows, and 18 target-validation rows (7 essential `gates_intervention`: KRAS A59T VAF + RAS/BRAF panel, HER2 IHC/FISH, TP53 R273 substitution, MMR IHC orthogonal, TMB mut/Mb, PD-L1 clone + CPS, DPYD genotype; 4 high-priority: UGT1A1, 20q segment boundary, ctDNA MRD, CMS subtyping). The ranked list contains 14 rows spanning agreement scores from 1.0 (rank 1 shared workup; rank 2 FOLFIRI-bev backbone; rank 3 aspirin; rank 7 T-DXd HER2-conditional) down to -2.0 (three Hard-Rule-1 documented vetoes at ranks 11-14). All five personas converged on the rank-1 workup, the rank-2 backbone continuation, and the rank-3 aspirin adjunct. The critic vetoed the rank-8 RMC-6236 sponsor-inquiry route on evidence-quality grounds; the conservative and concensusite dissented on the rank-5 inavolisib 2L positioning and on the rank-10 anti-EGFR research-framework lane.

## Cross-cutting caveat (read first)

**The rank-1 workup is itself the load-bearing intervention. Seven essential diagnostic gates have to land before the rest of the ranking moves from biomarker-conditional to actionable.** The single comprehensive NGS send-out (FoundationOne CDx or equivalent) returns KRAS A59T VAF + clonality, full extended RAS, BRAF V600, ERBB2 amplification, PIK3CA M1043I clonality, TP53 R273 substitution, SMAD4, and the 20q segment boundaries; HERACLES-graded HER2 IHC/FISH covers the single most-actionable target check not yet done; MMR IHC orthogonal closes the ICI door definitively rather than presumptively; DPYD + UGT1A1 genotyping is mandated by the March 2024 FDA fluoropyrimidine label update; Signatera baseline before CRS gives the lead-time signal for peritoneal recurrence. None of this requires a new biopsy.

- **Sponsor confirmation on KRAS A59T eligibility is the single highest-yield phone call on the case.** RMC-6236 (RASolve-GI NCT06445062; medinfo@revmed.com / 1-844-2-REVMED), JAB-23E73 (NCT06973564, Jacobio; codon-agnostic by public protocol text and excludes prior KRAS-inhibitor exposure which the patient has none of), and S241656 (NCT05786924, Servier ERK inhibitor; codon-agnostic) are all gated by sponsor judgment on whether A59T qualifies under the protocol's RAS-mutant criterion. The flagship RMC-6236 monotherapy basket NCT05379985 restricts to codons 12/13/61 by published protocol text, so basket-level access is closed; the GI platform may or may not be open. Make the call before scheduling screening visits anywhere.

- **PRODIGE 7 is the load-bearing surgical-evidence caveat the family needs to hear honestly.** CRS retains the OS spine (NCCN-endorsed mOS 30-40 mo in selected patients at experienced centers). Oxaliplatin HIPEC does not (PRODIGE 7 OS 41.7 vs 41.2 mo, HR ~1.00, with higher 60-day morbidity in the HIPEC arm). COLOPEC and PROPHYLOCHIP complete the negative trifecta. Mitomycin C HIPEC at a high-volume center is the lower-bad choice if HIPEC is performed at all (Van der Speeten's MMC peritoneal:plasma AUC ~20-25× pharmacokinetic argument carries even though no positive randomized OS readout exists for the MMC agent either). Surgeon volume drives 60-day morbidity more than perfusate choice.

- **The bevacizumab peri-operative hold is non-negotiable.** 4-6 weeks pre-CRS and 4-6 weeks post-CRS, with documented wound closure before resumption. Skipping this is the single highest-yield way to harm the patient before any KRAS or PIK3CA question matters.

- **HER2 amplification is the wildcard.** If the rank-1 HER2 IHC returns 3+ (or 2+ with FISH ratio ≥2.0), trastuzumab deruxtecan (DESTINY-CRC02 ORR ~38% including RAS-mutant per the 2024 pan-tumor accelerated approval) jumps the post-1L queue. MOUNTAINEER tucatinib + trastuzumab is RAS-WT-restricted by label and the A59T patient is closed out of that door even with HER2 amp; T-DXd is the RAS-allowed substitute. Prior probability of HER2 amp in mCRC is 3-5%; the test costs nothing relative to the upside.

- **The TP53 R273 reactivator question is foreclosed.** Eprenetapopt's solid-tumor program is effectively closed after the Park 2022 ORR 8% phase 1b readout. Rezatapopt (PYNNACLE) is Y220C-binding-pocket-restricted by structural design AND requires KRAS wild-type — A59T fails both gates. The rank-1 NGS R273-substitution call still sharpens any future ATR / WEE1 / HSP90 synthetic-lethal trial discussion at recurrence, but there is no current drug accessible to this patient.

## Intervention grouping

- **PI3K-alpha-selective targeting PIK3CA M1043I:** inavolisib + bevacizumab on INTRINSIC ([NCT04929223](https://clinicaltrials.gov/study/NCT04929223), [PMID 39476340](https://pubmed.ncbi.nlm.nih.gov/39476340), [PMID 29401002](https://pubmed.ncbi.nlm.nih.gov/29401002)).
- **PIK3CA-mutant adjuvant aspirin (ALASCCA-derived) targeting PIK3CA M1043I:** [PMID 40979555](https://pubmed.ncbi.nlm.nih.gov/40979555), [PMID 38889377](https://pubmed.ncbi.nlm.nih.gov/38889377), [PMID 23094721](https://pubmed.ncbi.nlm.nih.gov/23094721).
- **Pan-RAS(ON) and ERK targeting KRAS A59T (atypical switch-II):** RMC-6236 on RASolve-GI ([NCT06445062](https://clinicaltrials.gov/study/NCT06445062), [PMID 38778097](https://pubmed.ncbi.nlm.nih.gov/38778097), [PMID 38778099](https://pubmed.ncbi.nlm.nih.gov/38778099)); JAB-23E73 ([NCT06973564](https://clinicaltrials.gov/study/NCT06973564)); S241656 ([NCT05786924](https://clinicaltrials.gov/study/NCT05786924)); Arena 2021 functional characterization [PMID 34031055](https://pubmed.ncbi.nlm.nih.gov/34031055).
- **Fc-enhanced anti-CTLA-4 + PD-1 targeting MSS / peritoneal-dominant phenotype:** botensilimab + balstilimab USC NCT06336902, BATTMAN [NCT07152821](https://clinicaltrials.gov/study/NCT07152821), Agenus EAP [NCT06751524](https://clinicaltrials.gov/study/NCT06751524); Bullock 2024 [PMID 38871975](https://pubmed.ncbi.nlm.nih.gov/38871975).
- **HER2-directed ADC targeting HER2 amplification (conditional):** trastuzumab deruxtecan DESTINY-CRC02 [NCT04744831](https://clinicaltrials.gov/study/NCT04744831), [PMID 39058319](https://pubmed.ncbi.nlm.nih.gov/39058319); HERACLES scoring [PMID 27108243](https://pubmed.ncbi.nlm.nih.gov/27108243).
- **mCRC chemotherapy + anti-angiogenic backbones (SoC floor):** FOLFIRI + bev ([PMID 15175435](https://pubmed.ncbi.nlm.nih.gov/15175435), [PMID 17947725](https://pubmed.ncbi.nlm.nih.gov/17947725)); FOLFOXIRI + bev TRIBE / TRIBE2 ([PMID 25337750](https://pubmed.ncbi.nlm.nih.gov/25337750), [PMID 32007158](https://pubmed.ncbi.nlm.nih.gov/32007158)); CAIRO6 perioperative chemo + CRS-HIPEC [PMID 39550351](https://pubmed.ncbi.nlm.nih.gov/39550351); 2L+ aflibercept / ramucirumab / TAS-102+bev / fruquintinib / regorafenib bench.
- **Peritoneal loco-regional control:** CRS at high-volume center per NCCN; HIPEC framed honestly per PRODIGE 7 ([PMID 33417845](https://pubmed.ncbi.nlm.nih.gov/33417845)) + COLOPEC ([PMID 31272834](https://pubmed.ncbi.nlm.nih.gov/31272834)) + PROPHYLOCHIP ([PMID 32717181](https://pubmed.ncbi.nlm.nih.gov/32717181)); EFFIPEC trial route [NCT04861558](https://clinicaltrials.gov/study/NCT04861558).
- **Anti-EGFR research-framework lane (default avoid, not welded shut):** Sorich 2015 anti-EGFR meta-analysis [PMID 25115304](https://pubmed.ncbi.nlm.nih.gov/25115304); Schirripa 2015 [PMID 24806288](https://pubmed.ncbi.nlm.nih.gov/24806288); Arena 2021 functional [PMID 34031055](https://pubmed.ncbi.nlm.nih.gov/34031055); Lochhead 2018 single-patient PR [PMID 30538852](https://pubmed.ncbi.nlm.nih.gov/30538852); ASCEND-CRC platform NCT07318389.

## Top interventions

### Rank 1. Diagnostic gates: comprehensive NGS + HER2 IHC/FISH + MMR IHC + TMB + PD-L1 + DPYD/UGT1A1 + Signatera baseline

*The rank-1 row is the precondition for everything below — workup, not therapy. None of it requires a new biopsy. All seven essential gates can run in parallel off the archival FFPE block plus a peripheral blood draw plus a pre-CRS Signatera tube.*

#### Evidence base

Seven confirmatory tests, each anchored to a specific decision. **Comprehensive tumor NGS** (FoundationOne CDx, Tempus xT CDx, Caris MI Cancer Seek, or MSK-IMPACT — [PMID 30538852](https://pubmed.ncbi.nlm.nih.gov/30538852), [PMID 27959278](https://pubmed.ncbi.nlm.nih.gov/27959278), [PMID 34754095](https://pubmed.ncbi.nlm.nih.gov/34754095), NCCN Colon v1.2026) returns KRAS A59T VAF + clonality, full extended RAS (KRAS / NRAS / HRAS exons 2/3/4), BRAF V600, ERBB2 amplification, PIK3CA M1043I somatic call, TP53 R273 substitution, SMAD4 R361H, the 20q segment boundaries, and TMB in mut/Mb with panel-definition documented for the ≥10 mut/Mb tumor-agnostic pembrolizumab cutoff. **HER2 IHC/FISH per HERACLES scoring** (clone 4B5 or HercepTest with reflex dual-probe FISH — [PMID 39058319](https://pubmed.ncbi.nlm.nih.gov/39058319), [PMID 27108243](https://pubmed.ncbi.nlm.nih.gov/27108243)) is the most-actionable target check not yet done; MOUNTAINEER ORR 38.1% with 12.4 mo median DOR if positive ([NCT03043313](https://clinicaltrials.gov/study/NCT03043313)), and the T-DXd 2024 pan-tumor accelerated approval makes the call RAS-allele-agnostic at the label level. **MMR IHC orthogonal** (four-antibody MLH1 / MSH2 / MSH6 / PMS2 — [PMID 31416808](https://pubmed.ncbi.nlm.nih.gov/31416808)) closes the ICI door definitively rather than presumptively; the ~5% MSS-vs-MSI-H discordance rate is the reason this stays a real defensive call. **PD-L1 IHC with documented clone + CPS** ([PMID 30604034](https://pubmed.ncbi.nlm.nih.gov/30604034)) covers combination-trial stratification even when the headline value is negative. **DPYD genotyping** for the four CPIC variants and **UGT1A1 *6 / *28** ([PMID 40958923](https://pubmed.ncbi.nlm.nih.gov/40958923), [PMID 21570278](https://pubmed.ncbi.nlm.nih.gov/21570278), CPIC + March 2024 FDA fluoropyrimidine label update) close the pharmacogenomic safety gap before the next FOLFIRI cycle and any future capecitabine maintenance. **Signatera baseline + serial ctDNA** ([PMID 32576704](https://pubmed.ncbi.nlm.nih.gov/32576704), [PMID 34754095](https://pubmed.ncbi.nlm.nih.gov/34754095)) brackets the CRS-HIPEC window for the lead-time signal on peritoneal recurrence — Medicare-covered in stage II-IV CRC.

#### Likelihood of desired effect

Diagnostic certainty across seven dimensions. The result branching:

- **HER2 IHC 3+ or ISH ratio ≥2.0 (3-5% prior) → rank 7 T-DXd jumps the post-1L queue.**
- **MMR IHC discordant dMMR (~5% prior) → reverses the entire ranking; single-agent pembrolizumab leaps to 1L consideration.**
- **TMB on F1CDx ≥10 mut/Mb (low prior given intake "low" call) → tumor-agnostic pembrolizumab label unlocks at later lines.**
- **PIK3CA M1043I confirmed somatic + clonal → rank 5 inavolisib trial slot enabled.**
- **DPYD *2A / HapB3 / c.2846A>T carrier (3-5% prior) → FOLFIRI dose-rationalize for the remaining cycles per CPIC.**
- **UGT1A1 *28/*28 (~10% prior in European-ancestry; *6/*28 in Asian-ancestry) → starting-dose reduction on irinotecan; impacts irinotecan HIPEC if elected.**
- **Signatera positive at day 30-60 post-CRS → escalates the adjuvant-therapy duration conversation toward extended systemic exposure rather than observation.**

#### Toxicity profile

- Archival FFPE block release + EDTA peripheral blood draw + a pre-op Signatera tube
- No patient-facing toxicity
- The only operational risk is Signatera bespoke-build delay (4-6 weeks for the first sample); start the order before CRS scheduling

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. The workup row carries no mechanism-level counter-productive vector.

#### Practical considerations

Bundle the comprehensive NGS, HERACLES HER2 IHC + reflex FISH, MMR IHC, PD-L1 22C3 with CPS scoring, and the SMAD4 + 20q-segment requisitions on one block release to avoid multiple FFPE pulls. Order DPYD + UGT1A1 on a single pharmacogenomic blood draw at the next infusion visit. Initiate the Signatera bespoke build at the same time as the master NGS — the tumor-informed assay needs an FFPE block for the 16-variant WES design, and the baseline plasma draw has to land BEFORE CRS for the perioperative kinetic to stay interpretable. The PIK3CA M1043I clonality + somatic confirmation and the TP53 R273-substitution call (R273H vs R273C vs R273L vs R273S vs R273P) come off the same comprehensive NGS report — request the lab to explicitly call the substitution rather than abbreviating to a generic 'p.R273'.

#### Why this rank

Rank 1 because seven downstream decisions hang from it (anti-EGFR eligibility, HER2-directed options, ICI doors, PIK3CA confirmation, fluoropyrimidine safety, post-CRS surveillance) and all five personas endorsed the workup without reservation. Ranks 2-9 are biomarker-conditional in narrow ways and the gates resolve in 2-3 weeks of turnaround.

#### Per-trial detail

| Diagnostic gate | Decision unlocked | Provider | Reference |
|---|---|---|---|
| Comprehensive tumor NGS (FoundationOne CDx preferred) | KRAS A59T VAF + extended RAS + BRAF V600 + ERBB2 amp + PIK3CA M1043I clonality + TP53 R273 substitution + SMAD4 + 20q + TMB mut/Mb | Foundation Medicine — 1-888-988-3639 | [PMID 30538852](https://pubmed.ncbi.nlm.nih.gov/30538852) |
| HER2 IHC (4B5 or HercepTest) + reflex dual-probe FISH per HERACLES | Tucatinib + trastuzumab (RAS-WT only, A59T-excluded) and T-DXd (RAS-allowed) | NeoGenomics — 1-866-776-5907 | [PMID 39058319](https://pubmed.ncbi.nlm.nih.gov/39058319) |
| MMR IHC four-antibody panel | Orthogonal MSI-H vs MSS confirmation (~5% NGS-vs-IHC discordance) | NeoGenomics — 1-866-776-5907 | [PMID 31416808](https://pubmed.ncbi.nlm.nih.gov/31416808) |
| DPYD 4-variant CPIC panel + UGT1A1 *6 / *28 | Fluoropyrimidine + irinotecan dose adjustment per CPIC + 2024 FDA label | Mayo Clinic Labs — 1-800-533-1710 | [PMID 40958923](https://pubmed.ncbi.nlm.nih.gov/40958923) |
| Signatera tumor-informed bespoke ctDNA | Peri-CRS recurrence surveillance (Medicare-covered in stage II-IV CRC) | Natera — 1-650-249-9090 | [PMID 32576704](https://pubmed.ncbi.nlm.nih.gov/32576704) |

### Rank 2. FOLFIRI + bevacizumab through the peri-operative window (FOLFOXIRI + bev intensification permitted)

*The SoC backbone the patient is already tolerating, with the bev peri-op hold as the binding safety thread and FOLFOXIRI intensification as a permitted upgrade per TRIBE/TRIBE2.*

#### Evidence base

FOLFIRI + bev is NCCN category 1 for 1L mCRC. AVF2107g (Hurwitz 2004, [PMID 15175435](https://pubmed.ncbi.nlm.nih.gov/15175435)) anchored the IFL backbone at mOS 20.3 vs 15.6 mo, HR 0.66, p<0.001; BICC-C (Fuchs 2007, [PMID 17947725](https://pubmed.ncbi.nlm.nih.gov/17947725)) established FOLFIRI as the favored irinotecan schedule at mOS 23.1 mo; MAVERICC ([PMID 30224341](https://pubmed.ncbi.nlm.nih.gov/30224341)) supports FOLFIRI-bev = FOLFOX-bev in 1L. FOLFOXIRI + bev intensification is NCCN category 2A preferred for fit patients and ESMO MCBS 3: TRIBE (Loupakis 2014, [PMID 25337750](https://pubmed.ncbi.nlm.nih.gov/25337750), mPFS 12.1 vs 9.7 mo, HR 0.75) and TRIBE2 (Cremolini 2020, [PMID 32007158](https://pubmed.ncbi.nlm.nih.gov/32007158), mOS 27.4 vs 22.5 mo, HR 0.82) are the registrational anchors.

#### Likelihood of desired effect

High — replicated phase 3 OS signal across AVF2107g, BICC-C, MAVERICC, and TRIBE2 in a 37-year-old ECOG 1 patient who is exactly the TRIBE-eligible population. The realistic question is whether the team intensifies to triplet + bev before CRS-HIPEC or holds the regimen the patient is already tolerating; both are guideline-supported and the right framing is permitted preferred upgrade rather than mandatory switch.

#### Toxicity profile

- FOLFIRI: G3+ neutropenia ~25-30%, G3+ diarrhea ~14%; UGT1A1 *28/*28 carriers warrant dose reduction
- Bevacizumab: wound-healing impairment in the peri-op window — 4-6 weeks pre-CRS and 4-6 weeks post-CRS, documented wound closure before resumption is the binding safety thread
- FOLFOXIRI intensification: cumulative oxaliplatin neuropathy is rate-limiting for a 37yo with a long runway — bake OPTIMOX stop-and-go in if pursued
- DPYD *2A / HapB3 carriers can compensate early and decompensate later on 5-FU; the rank-1 genotyping closes that surveillance gap

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous on the rank. The single mechanism-flavored caveat is bevacizumab wound-healing impairment in the peri-op window, managed by the hold rather than by drug avoidance. No persona dissented on the backbone choice.

#### Practical considerations

Coordinate the systemic-to-surgical handoff so the last irinotecan dose lands at least 3 weeks before CRS to limit perioperative neutropenia. CAIRO6 ([NCT02758951](https://clinicaltrials.gov/study/NCT02758951)) is the perioperative-chemo + CRS-HIPEC protocol template even though new enrollment is closed; the team can mirror the schedule off-trial. If switching to FOLFOXIRI + bev, confirm oxaliplatin-naive status (the prior-therapy list shows FOLFIRI only) and lay in an OPTIMOX-style stop-and-go from the start. Pharmacy access is universal; no payer obstacles.

#### Why this rank

Rank 2 because no other intervention has comparable replicated OS signal and the patient is already tolerating it. Rank 3 (aspirin) sits below this on agreement-score grounds only because aspirin is a layered adjunct rather than a systemic backbone; rank 5 (inavolisib) and rank 6 (bot/bal) are sequenced for progression / 2L+ slots rather than 1L displacement.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| FOLFIRI + bevacizumab (BICC-C / MAVERICC) | mOS 23.1 mo BICC-C; 1L category 1 | G3+ neutropenia 25-30%, G3+ diarrhea ~14%, bev wound-healing/perforation | [PMID 17947725](https://pubmed.ncbi.nlm.nih.gov/17947725), [PMID 30224341](https://pubmed.ncbi.nlm.nih.gov/30224341) |
| FOLFOXIRI + bevacizumab (TRIBE / TRIBE2) | mPFS 12.1 vs 9.7 mo HR 0.75 (TRIBE); mOS 27.4 vs 22.5 mo HR 0.82 (TRIBE2) | G3+ neutropenia 50%, G3+ diarrhea 19%, cumulative oxaliplatin neuropathy | [PMID 25337750](https://pubmed.ncbi.nlm.nih.gov/25337750), [PMID 32007158](https://pubmed.ncbi.nlm.nih.gov/32007158) |
| Bevacizumab + irinotecan / 5-FU (AVF2107g) | mOS 20.3 vs 15.6 mo, HR 0.66 | bev class AEs: hypertension, proteinuria, wound healing | [PMID 15175435](https://pubmed.ncbi.nlm.nih.gov/15175435) |
| CAIRO6 (perioperative chemo + CRS-HIPEC) | PFS / DFS improved; OS unchanged in interim | Compounded chemo + surgical morbidity | [PMID 39550351](https://pubmed.ncbi.nlm.nih.gov/39550351), [NCT02758951](https://clinicaltrials.gov/study/NCT02758951) |

### Rank 3. Low-dose aspirin 160 mg PO QD (PIK3CA-pathway-altered adjunct, ALASCCA-derived)

*The only RoB2:Low phase 3 RCT in the dossier with a biomarker match to the patient. Cheap layered adjunct that stacks on top of whichever systemic backbone the team runs.*

#### Evidence base

ALASCCA (Frödin / Martling 2025 NEJM, [PMID 40979555](https://pubmed.ncbi.nlm.nih.gov/40979555), n=626) randomized resected stage I-III rectal or stage II-III colon cancer with somatic PI3K-pathway alteration to aspirin 160 mg daily for 3 years vs placebo. Group A (PIK3CA exon 9/20 mutated, M1043I qualifies via exon 20 kinase-domain position): 3-year time-to-recurrence HR 0.49 (95% CI 0.24-0.98, p=0.044). Group B (other PI3K-pathway alterations): HR 0.42 (95% CI 0.21-0.83, p=0.013). Direction is independently supported by Liao 2012 NHS/HPFS observational signal ([PMID 23094721](https://pubmed.ncbi.nlm.nih.gov/23094721), HR 0.18 CRC-specific mortality in PIK3CA-mut, n=964) and the CALGB/SWOG 80702 celecoxib PIK3CA-activating subset (Yang/Meyerhardt 2024, [PMID 38889377](https://pubmed.ncbi.nlm.nih.gov/38889377), DFS HR 0.56 (95% CI 0.35-0.88), OS HR 0.41 (95% CI 0.21-0.79)). Three concordant biomarker-stratified datasets, two RCT-grade; COX-2 / PGE2 / PI3K mechanism coherent.

#### Likelihood of desired effect

Moderate. The mechanism direction is the cleanest in the dossier and three independent biomarker-stratified studies agree on it. The honest qualifier the whole board co-signed: ALASCCA enrolled resected stage I-III, not stage IV with active peritoneal disease. The post-CRS-HIPEC state is adjuvant-equivalent and the class safety profile transfers, but the metastatic-setting efficacy claim is biology-driven extrapolation rather than endpoint-validated. The Group A 95% CI upper bound at 0.98 also means magnitude is fragile even within the adjuvant indication; direction is robust.

#### Toxicity profile

- G3+ GI bleeding ~3% on the ALASCCA aspirin arm vs ~2% placebo
- Compounded bleeding risk with bevacizumab co-administration is real; coordinate aspirin hold with the bev cycle
- Peri-operative hold 5-7 days pre-CRS, resume post-op once surgical hemostasis allows
- No user toxicity vetoes apply

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. The critic flagged the indication gap (adjuvant vs metastatic) honestly; the concensusite noted NCCN v4.2025 adopted the recommendation despite the same Group A CI fragility, treating it as collective expert calibration of the evidence rather than a separate problem. No mechanism-level counter-productive vector.

#### Practical considerations

OTC product, ~$0.05/pill at any pharmacy, no payer involvement. NCCN Colon Cancer v4.2025 adopted the ALASCCA recommendation: consider PIK3CA testing in stage II-III colon cancer and offer low-dose aspirin 100-162 mg PO daily for 3 years in PIK3CA-mutated patients. Discuss baseline GI history and any reflux or NSAID intolerance; consider PPI co-administration. Document the peri-operative hold plan explicitly with the CRS-HIPEC surgical team.

#### Why this rank

Rank 3 because aspirin is a layered adjunct that stacks on top of the systemic backbone rather than competing for the lead slot — it does not substitute for systemic targeted therapy and the rank-1 + rank-2 picks own the precondition + the chemotherapy floor. Above the rank-4 CRS-HIPEC row because the evidence quality (phase 3 RCT with biomarker match) is higher than the surgical row's negative-randomized-HIPEC component, even though the surgical question carries higher decision urgency.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Aspirin 160 mg QD (ALASCCA) | PIK3CA exon 9/20 (Group A): 3-yr TTR HR 0.49 (95% CI 0.24-0.98); Group B (other PI3K-path): HR 0.42 (0.21-0.83) | G3+ GI bleeding ~3% vs ~2% placebo | [PMID 40979555](https://pubmed.ncbi.nlm.nih.gov/40979555) |
| Celecoxib (CALGB/SWOG 80702 PIK3CA subset) | DFS HR 0.56 (0.35-0.88); OS HR 0.41 (0.21-0.79) in PIK3CA-activated subset | COX-2 class AEs; CV risk | [PMID 38889377](https://pubmed.ncbi.nlm.nih.gov/38889377) |
| Aspirin observational (Liao 2012 NHS/HPFS) | CRC-specific mortality HR 0.18 (0.06-0.61) in PIK3CA-mut | Observational; baseline GI bleed | [PMID 23094721](https://pubmed.ncbi.nlm.nih.gov/23094721) |

### Rank 4. CRS at a high-volume center; mitomycin C HIPEC if elected (PRODIGE 7 framing)

*The surgical autonomy lane. CRS retains the OS signal per NCCN; HIPEC does not under the randomized-evidence read.*

#### Evidence base

NCCN Colon Cancer v1.2026 endorses cytoreductive surgery at category 2A for selected patients with limited resectable peritoneal disease (PCI < 20) at experienced centers. The HIPEC question is unsettled by randomized OS data. PRODIGE 7 (Quenet 2021 Lancet Oncol, [PMID 33417845](https://pubmed.ncbi.nlm.nih.gov/33417845), n=265, RoB2:Low): oxaliplatin HIPEC vs no HIPEC after CRS — OS 41.7 vs 41.2 mo, HR ~1.00, RFS 13.1 vs 11.1 mo, with higher 60-day morbidity in the HIPEC arm. COLOPEC (Klaver 2019, [PMID 31272834](https://pubmed.ncbi.nlm.nih.gov/31272834)) and PROPHYLOCHIP-PRODIGE 15 (Goere 2020, [PMID 32717181](https://pubmed.ncbi.nlm.nih.gov/32717181)) complete the negative trifecta. Mitomycin C HIPEC was not the agent PRODIGE 7 eliminated; Van der Speeten ([PMID 20689948](https://pubmed.ncbi.nlm.nih.gov/20689948)) gives MMC a peritoneal:plasma AUC of ~20-25× — the pharmacokinetic argument PRODIGE 7 did not test, though no positive randomized OS signal exists for MMC either. CAIRO6 (Rovers 2024, [PMID 39550351](https://pubmed.ncbi.nlm.nih.gov/39550351)) supports the perioperative-chemo + CRS-HIPEC structure for PFS even where OS is unchanged.

#### Likelihood of desired effect

Moderate for CRS (NCCN-endorsed selected-patient mOS 30-40 mo). Low for the HIPEC component specifically — the only randomized OS readout in CRC peritoneal disease is negative for the oxaliplatin agent, and the mitomycin C lane has no positive randomized OS signal either. The right framing for the family conversation is that the survival math runs through the cytoreduction, not the perfusate.

#### Toxicity profile

- 60-day G3+ morbidity 25-40% at high-volume centers, higher at lower-volume
- Treatment-related mortality 1-3% at high-volume centers
- Surgeon volume drives morbidity more than HIPEC agent choice
- Bleeding, anastomotic leak, infection, prolonged ileus; recovery delays systemic therapy 4-8 weeks
- **Oxaliplatin HIPEC**: PRODIGE 7 added 60-day morbidity without OS benefit; closed for CRC at the agent level

#### Counter-productive mechanisms / dissent

The critic dissented honestly. The strict-evidence read is that no randomized OS signal exists for mitomycin C HIPEC either, and the negative trifecta closes the HIPEC OS claim at the class level. Four-of-five endorsement on the surgical row depends on the user's free-text framing ("treat the planned CRS-HIPEC window as a sequencing constraint") and the explicit honoring of patient autonomy with the treating surgical team. The risktaker qualified rather than vetoed because the Van der Speeten MMC pharmacokinetic argument was about mitomycin C, not oxaliplatin. The synthesis: CRS = survival spine; HIPEC = patient-autonomy + surgeon-judgment call with the family hearing the PRODIGE 7 result plainly.

#### Practical considerations

Confirm the CRS-HIPEC center is high-volume (>20 cases/yr). Major US peritoneal-surface-malignancy centers include MSK, MD Anderson, Mayo (Rochester, Phoenix, Jacksonville), City of Hope, Wake Forest, UPMC (Pittsburgh Sugarbaker network), Cleveland Clinic, Moffitt. Document PCI and CC-0/CC-1 cytoreduction probability at the surgical consult. Bracket with Signatera (rank-1 row): baseline pre-op, day 30-60 post-op, then every 8-12 weeks. Hold bevacizumab 4-6 weeks pre-op and resume 4-6 weeks post-op once the wound is healed. Mitomycin C HIPEC is the post-PRODIGE 7 default at most US centers. Trial routes: EFFIPEC ([NCT04861558](https://clinicaltrials.gov/study/NCT04861558)) is Sweden + India only (not US-accessible); University of Kentucky flat-dose vs weight-based MMC dosing trial ([NCT04779554](https://clinicaltrials.gov/study/NCT04779554), Prakash Pandalai, 859-323-8920) is US-accessible; Yale MRT-guided HIPEC selection ([NCT07291180](https://clinicaltrials.gov/study/NCT07291180)) personalizes the agent choice on resected tissue.

#### Why this rank

Rank 4 because the CRS half is OS-validated and the patient already has surgery planned, but the HIPEC component drops the row below the rank-3 aspirin adjunct on evidence quality. Above rank 5 (inavolisib) and rank 6 (bot/bal) because the surgical window is now-or-never for a peritoneal-dominant patient with resected liver mets; the trial slots wait, the operative window does not.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| CRS + oxaliplatin HIPEC (PRODIGE 7) | OS 41.7 vs 41.2 mo (CRS alone), HR ~1.00; RFS 13.1 vs 11.1 mo | 60-day morbidity ~25-40% G3+; higher than CRS-alone arm | [PMID 33417845](https://pubmed.ncbi.nlm.nih.gov/33417845) |
| Adjuvant oxaliplatin HIPEC T4/perforated (COLOPEC) | 18-mo peritoneal DFS 80.9 vs 76.2%, NS | Compounded surgical + chemo AEs | [PMID 31272834](https://pubmed.ncbi.nlm.nih.gov/31272834) |
| Second-look + HIPEC (PROPHYLOCHIP) | 3-yr DFS 44 vs 53%, HR 0.97, p=0.82 | Compounded surgical morbidity | [PMID 32717181](https://pubmed.ncbi.nlm.nih.gov/32717181) |
| Perioperative chemo + CRS-HIPEC (CAIRO6) | PFS / DFS improved; OS unchanged | Compounded chemo + surgical AEs | [PMID 39550351](https://pubmed.ncbi.nlm.nih.gov/39550351) |
| Flat-dose vs weight-based MMC HIPEC ([NCT04779554](https://clinicaltrials.gov/study/NCT04779554)) | PK + clearance endpoint | Mitomycin C myelosuppression | University of Kentucky / Pandalai |

### Rank 5. Inavolisib + bevacizumab on INTRINSIC (NCT04929223)

*Conditional on PIK3CA M1043I somatic + clonal confirmation from the rank-1 NGS. Sequenced at progression past FOLFIRI-bev or post-CRS-HIPEC, not 1L displacement.*

#### Evidence base

INAVO120 (Jhaveri 2024 NEJM, [PMID 39476340](https://pubmed.ncbi.nlm.nih.gov/39476340), n=325, RoB2:Low) in HR+/HER2- PIK3CA-mutant breast: PFS HR 0.43 (95% CI 0.32-0.59), mPFS 15.0 vs 7.3 mo — the registrational anchor that drove the Oct 2024 FDA breast approval. INTRINSIC ([NCT04929223](https://clinicaltrials.gov/study/NCT04929223)) is the Roche-Genentech umbrella mCRC platform with multiple biomarker-defined arms; the PIK3CA-mut arm routes inavolisib + bev directly. CRC fallback is Juric 2018 alpelisib phase 1a ([PMID 29401002](https://pubmed.ncbi.nlm.nih.gov/29401002)): 2 PRs across the n=134 CRC subset of a PI3K-altered solid-tumor basket — anecdote-grade. Vasan 2019 ([PMID 31699932](https://pubmed.ncbi.nlm.nih.gov/31699932)) tagged M1043 as a kinase-domain activating allele sensitizing to PI3K-alpha-selective inhibition.

#### Likelihood of desired effect

Moderate assuming M1043I confirms somatic + clonal. The cross-tumor breast PFS HR 0.43 is the strongest cross-tumor anchor in the case, but the CRC efficacy translation is hypothesis-grade: Juric 2018's 2 PRs / 134 CRC subset and an unpublished INTRINSIC arm-specific readout are the available data. M1043I is also non-canonical relative to the H1047R / E545K / E542K hotspots INAVO120 powered on. The realistic upside is depth-of-response augmentation and PFS extension, not a single-agent home run; KRAS A59T co-activation may blunt single-pathway PI3K-alpha response by routing escape through RAS-MAPK signaling.

#### Toxicity profile

- Any-grade hyperglycemia 58.6%, G3+ hyperglycemia 5.6% — fasting glucose + HbA1c baseline; preemptive metformin / SGLT2-inhibitor plan if HbA1c ≥7%
- G3+ stomatitis 5.6%, G3+ diarrhea 3.7%
- Treatment discontinuation rate 6.5%
- Bevacizumab continuation tracks the patient's current regimen; peri-op hold logic from rank 2 applies

#### Counter-productive mechanisms / dissent

Three personas dissented for separate but coherent reasons. The conservative reserved for 2L on cross-tumor evidence grounds (INAVO120 is breast; CRC efficacy lives in 2 PRs from a phase 1a basket). The critic dissented on cross-tumor extrapolation generally and on M1043I non-canonical positioning specifically. The concensusite dissented on guideline-fit (1L displacement of category-1 chemo+bev backbone is outside NCCN endorsement). Synthesis: position as INTRINSIC trial enrollment at progression past FOLFIRI-bev or post-CRS-HIPEC, with the cross-tumor caveat carried forward in the consent conversation. The trial slot is real and the mechanism match is the cleanest PIK3CA play in the dossier; the off-label use case outside a trial is not.

#### Practical considerations

Off-label outside the trial has no compendium support and payer access is unlikely. INTRINSIC is the cleanest route because Genentech covers the drug under protocol. Contact global-roche-genentech-trials@gene.com or 888-662-6728 with the PIK3CA M1043I + KRAS A59T molecular profile to ask which INTRINSIC arm fits and whether M1043I is treated as kinase-domain-activating without a sponsor exception. If INTRINSIC is not accessible, do not pursue inavolisib off-label outside a trial — alpelisib has more mCRC-relevant trial signal. The KRAS A59T arm question may be parallel-tractable; INTRINSIC has multiple biomarker-defined cohorts including a divarasib-containing RAS arm worth surfacing in the same sponsor inquiry.

#### Why this rank

Rank 5 because the mechanism match is clean but the CRC evidence is hypothesis-grade and three personas dissented on positioning. Above rank 6 (bot/bal) because the biomarker-targeting biology is direct (M1043I → PI3K-alpha-selective inhibitor) whereas bot/bal targets the patient's MSS / peritoneal phenotype rather than a stated targetable feature. Below rank 4 (CRS) because the operative window is now-or-never and inavolisib waits.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Inavolisib + palbociclib + fulvestrant (INAVO120, breast) | PFS HR 0.43 (0.32-0.59); mPFS 15.0 vs 7.3 mo | G3+ hyperglycemia 5.6% (any-grade 58.6%); G3+ stomatitis 5.6%; G3+ diarrhea 3.7% | [PMID 39476340](https://pubmed.ncbi.nlm.nih.gov/39476340) |
| INTRINSIC umbrella mCRC ([NCT04929223](https://clinicaltrials.gov/study/NCT04929223)) | PIK3CA-mut + RAS-mut arms; arm-specific PFS unpublished | Per backbone (bev / cetuximab / divarasib / FOLFOX / FOLFIRI / atezolizumab) | Sponsor: Roche-Genentech |
| Alpelisib phase 1a PIK3CA-altered basket (Juric 2018) | 2 PRs / 134 CRC subset; ~6% all-comer ORR | G3+ hyperglycemia ~20%; G3+ rash; G3+ diarrhea | [PMID 29401002](https://pubmed.ncbi.nlm.nih.gov/29401002) |

### Rank 6. Botensilimab + balstilimab at 2L+ (USC NCT06336902 / Agenus EAP NCT06751524 / BATTMAN NCT07152821)

*The post-1L MSS-mCRC immunotherapy slot. The patient's NLM peritoneal-dominant phenotype matches the Bullock 2024 responder subset; the trial route activates at progression past FOLFIRI-bev.*

#### Evidence base

Bullock 2024 Nat Med ([PMID 38871975](https://pubmed.ncbi.nlm.nih.gov/38871975), n=101 phase 1b in refractory MSS mCRC): all-comer ORR 17% (95% CI 10-26); no-liver-metastases (NLM) subset ORR 22% with mOS 20.9 mo; active-liver-mets subset ORR 5%. Randomized phase 2 update (Bullock 2024 ASCO GI / ESMO GI, n=123 NLM): BOT+BAL ORR 19% with mOS approaching 21 mo, peritoneal-site responses called out specifically. The CCTG BATTMAN phase 3 ([NCT07152821](https://clinicaltrials.gov/study/NCT07152821), Chris O'Callaghan, cocallaghan@ctg.queensu.ca) is the registrational confirmation vs BSC. USC's BOT/BAL + fasting-mimicking diet + IV vitamin C ([NCT06336902](https://clinicaltrials.gov/study/NCT06336902), Charlean Ketchens, 323-865-0451) explicitly enrolls KRAS-mutant MSS mCRC. The Agenus EAP ([NCT06751524](https://clinicaltrials.gov/study/NCT06751524), med.info@agenusbio.com, 781-202-1614) is FDA-authorized for chemo-refractory patients across multiple cancers including CRC.

#### Likelihood of desired effect

Moderate in the NLM peritoneal-dominant subset. ORR 22%, mOS 20.9 mo is the strongest MSS-CRC ICI signal of the decade and the patient's resected-liver + active-peritoneal profile maps onto the responder phenotype. The honest qualifiers: NLM was selected post-hoc as the responder subset in the Bullock expansion, not pre-specified as a primary stratum; the randomized phase 2 compared BOT+BAL to BOT monotherapy rather than to BSC or chemo; BATTMAN OS readout is 2027-2028. The liver-mets contingency matters — if recurrence appears at the liver after CRS, the response probability drops to the ~5% LM-subset rate.

#### Toxicity profile

- G3+ irAE 35-38% across phase 1 and phase 2
- G3+ colitis 12%, G3+ hepatitis 8%, pyrexia 38% any-grade
- No treatment-related deaths in the dossier
- Baseline thyroid / hepatic / endocrine panel mandatory before initiation
- irAE management algorithm per SITC / ASCO / NCCN; high-dose steroids → infliximab → vedolizumab for refractory colitis

#### Counter-productive mechanisms / dissent

The critic dissented on RoB2 / evidence-quality grounds: single-arm phase 1b plus randomized phase 2 vs monotherapy, no BSC comparator until BATTMAN; the NLM phenotype was post-hoc-defined. The conservative dissented on stacking research-only adjuncts (the USC FMD + IV vitamin C layer) on top of an investigational ICI signal in a patient recovering from CRS-HIPEC. Both dissents are honest and load-bearing. Synthesis: position as the 2L+ pivot once FOLFIRI-bev has progressed and the peritoneal-only phenotype persists; consider asking the USC PI whether the FMD + IV-C adjuncts can be modified or whether the EAP route bypasses them.

#### Practical considerations

Most actionable today: USC NCT06336902 (KRAS-mutant MSS mCRC cohort, ~15 patients across southern California sites; travel logistics matter — contact Charlean Ketchens, Charlean.Ketchens@med.usc.edu, 323-865-0451). Bank the Agenus EAP request packet at med.info@agenusbio.com for the moment the patient progresses past 1L FOLFIRI-bev; the EAP requires standard-line exhaustion. The MGH SBRT + BOT/BAL combination ([NCT07128355](https://clinicaltrials.gov/study/NCT07128355), Aparna Parikh, aparna.parikh@mgh.harvard.edu) is a parallel option if a peritoneal or recurrent hepatic SBRT target can be defined. BATTMAN is Canadian-primary and chemo-refractory-restricted; useful as the registrational readout to track, not currently enrollable for a 1L patient.

#### Why this rank

Rank 6 because the trial slot activates only on progression past 1L (the patient is currently on FOLFIRI-bev) and two personas dissented on evidence-quality grounds. Below rank 5 (inavolisib) on biomarker-targeting strictness — bot/bal targets the patient's MSS / peritoneal phenotype rather than a stated single targetable feature — and the rank-5 PIK3CA mechanism match is more direct. Above ranks 8-10 because the Bullock 2024 NLM signal is the strongest modern MSS-CRC ICI readout the dossier contains.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| BOT+BAL phase 1b refractory MSS mCRC (Bullock 2024) | All-comer ORR 17% (10-26); NLM ORR 22%, mOS 20.9 mo; LM ORR 5% | G3+ irAE 35%; G3+ colitis 12%; G3+ hepatitis 8% | [PMID 38871975](https://pubmed.ncbi.nlm.nih.gov/38871975) |
| BOT+BAL randomized phase 2 vs BOT mono (Bullock 2024) | BOT+BAL ORR 19%, mOS ~21 mo; peritoneal-site responses | G3+ irAE 38% | Bullock ASCO GI / ESMO GI 2024 |
| BOT+BAL + FMD + IV vitamin C ([NCT06336902](https://clinicaltrials.gov/study/NCT06336902)) | KRAS-mutant MSS mCRC; ongoing | Per ICI + dietary intervention | USC / Ketchens |
| BATTMAN phase 3 vs BSC ([NCT07152821](https://clinicaltrials.gov/study/NCT07152821)) | OS endpoint pending 2027-2028 | TBD | CCTG / O'Callaghan |
| BOT/BAL EAP ([NCT06751524](https://clinicaltrials.gov/study/NCT06751524)) | Treating-physician-initiated; case-by-case | Per ICI class | Agenus |

### Rank 7. Trastuzumab deruxtecan (T-DXd) on DESTINY-CRC02 — CONDITIONAL on HER2 IHC 3+ from rank-1 workup

*The HER2 wildcard. RAS-mutant-allowed under the April 2024 T-DXd pan-tumor accelerated approval, distinct from MOUNTAINEER tucatinib + trastuzumab which the RAS-WT label excludes for this A59T patient.*

#### Evidence base

DESTINY-CRC02 (Raghav 2024, [PMID 39058319](https://pubmed.ncbi.nlm.nih.gov/39058319), [NCT04744831](https://clinicaltrials.gov/study/NCT04744831)): T-DXd 5.4 mg/kg in HER2-positive mCRC, ORR ~38% including the RAS-mutant subset (the trial specifically enrolled RAS-mutant patients in parallel to RAS-WT). The April 2024 FDA pan-tumor accelerated approval for HER2-positive (IHC 3+) unresectable / metastatic solid tumors removed the RAS-WT restriction at the label level. HERACLES scoring ([PMID 27108243](https://pubmed.ncbi.nlm.nih.gov/27108243)) is the historically defensible IHC + FISH call: IHC 3+ in >50% of cells, or IHC 2+ with HER2:CEP17 ratio ≥2.0 by FISH. The TOP1 deruxtecan payload rationale aligns with the patient's 20q11 TOP1 co-amplification on existing NGS.

#### Likelihood of desired effect

High in the HER2 IHC 3+ subset (~3-5% prior probability of HER2 amp in mCRC). Foreclosed if HER2 returns negative. RAS-mutant subset within DESTINY-CRC02 carries lower absolute response than RAS-WT (mid-30% range vs RAS-WT) and A59T-specific data are not reported; the realistic positive-branch expectation is ORR in the 30-38% range with DOR comparable to the breast experience.

#### Toxicity profile

- G3+ ILD / pneumonitis 5-10% across DESTINY trials; treatment-related ILD deaths reported
- Baseline + Q3W chest imaging surveillance; PFTs at baseline
- G3+ neutropenia ~30%, G3+ nausea/vomiting 10-15%, G3+ fatigue 10%
- ILD monitoring infrastructure at the treating center is the operational gate

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous on the conditional. The risktaker named T-DXd as the wildcard upside; the concensusite called out that the pan-tumor approval is RAS-mutant-allowed; the conservative agreed HER2 status is the binding pre-2L decision; the advocate framed T-DXd as the cleanest HER2-pathway option for an A59T patient; the critic flagged DESTINY-CRC02 ORR ~38% without dissent. No mechanism-level counter-productive vector identified beyond on-target ILD.

#### Practical considerations

If HER2 returns 3+ or 2+ with FISH ratio ≥2.0, T-DXd jumps the post-1L queue and ranks 5 (inavolisib) and 6 (bot/bal) get re-prioritized against it. The 2024 pan-tumor accelerated approval means access is on-label after prior systemic therapy; payer support is generally available with the HER2 amp documentation. NCT04744831 is the DESTINY-CRC02 trial slot if expansion-cohort enrollment is preferred; NCT07407465 is a follow-up arm. ILD surveillance at the treating center is the operational gate. Coordinate with the rank-1 workup so the HER2 IHC reflexes to FISH before the post-CRS decision point.

#### Why this rank

Rank 7 because the entire row is contingent on the rank-1 HER2 IHC result returning positive (3-5% prior probability). If positive, the conditional likelihood of effect is the highest in the dossier and the row jumps ahead of inavolisib and bot/bal in the post-1L sequence. If negative, the row is foreclosed and the rank-5 / rank-6 ordering stands. Listed at rank 7 in the unified table rather than higher because the prior probability of a positive test is 3-5%; the expected value across the prior conditions the placement.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Trastuzumab deruxtecan 5.4 mg/kg (DESTINY-CRC02) | HER2+ mCRC ORR ~38% including RAS-mutant; pan-tumor accelerated approval | G3+ ILD 5-10% with treatment-related deaths; G3+ neutropenia ~30%; G3+ nausea/vomiting 10-15% | [PMID 39058319](https://pubmed.ncbi.nlm.nih.gov/39058319), [NCT04744831](https://clinicaltrials.gov/study/NCT04744831) |
| HERACLES IHC + FISH scoring | IHC 3+ in >50% cells OR IHC 2+ with FISH ratio ≥2.0 | Diagnostic only | [PMID 27108243](https://pubmed.ncbi.nlm.nih.gov/27108243) |

### Rank 8. Daraxonrasib (RMC-6236) on RASolve-GI (NCT06445062) — GATED on sponsor confirming KRAS A59T eligibility

*The asymmetric-upside single phone call for the atypical KRAS A59T allele. Critic-vetoed on evidence-quality grounds; carried per Hard Rule 1 so the user sees what was considered and what the dissent rests on.*

#### Evidence base

RMC-6236 is the first pan-RAS(ON) tri-complex inhibitor with documented regression across G12/G13/Q61 PDXs at 25-50 mg/kg (Knox / Jiang Nature 2024, [PMID 38778097](https://pubmed.ncbi.nlm.nih.gov/38778097), [PMID 38778099](https://pubmed.ncbi.nlm.nih.gov/38778099)). A59T sits in switch-II in a way that preserves the binding interface so the mechanism plausibly carries, but the published RMC-6236 / RMC-7977 package contains zero A59T in-vivo regression data. RASolve-GI ([NCT06445062](https://clinicaltrials.gov/study/NCT06445062)) protocol text reads "RAS-mutated CRC" without an explicit codon gate; sponsor-level operational definition usually narrows to codons 12/13/61. The flagship RMC-6236 monotherapy basket ([NCT05379985](https://clinicaltrials.gov/study/NCT05379985)) restricts to codons 12/13/61 by published protocol text, so basket-level access is explicitly closed. JAB-23E73 ([NCT06973564](https://clinicaltrials.gov/study/NCT06973564), Jacobio) reads codon-agnostic in the public protocol and excludes only patients with prior G12C/G12D/pan-KRAS-inhibitor exposure (the patient has none). S241656 ([NCT05786924](https://clinicaltrials.gov/study/NCT05786924), Servier ERK inhibitor) lists KRAS / HRAS / NRAS / BRAF / CRAF alterations without codon restriction. Arena 2021 ([PMID 34031055](https://pubmed.ncbi.nlm.nih.gov/34031055)) functionally characterized A59 alleles as showing partial residual MAPK activity with weaker output than canonical G12 mutants — hypothesis-generating only.

#### Likelihood of desired effect

Low. Zero published A59T clinical efficacy in any RAS(ON) or pan-RAS program. Mechanism plausibility from preclinical PDX work only. If RevMed confirms A59T eligibility, the realistic upside is a phase 1/2 expansion-cohort slot with a class-typical response rate (RMC-6236 in G12X PDAC ORR ~20-30% in the breakthrough-designation readout) attenuated by the atypical allele's lower MAPK output. If sponsor declines, the pick collapses to JAB-23E73 (Jacobio, codon-agnostic) or S241656 (Servier, codon-agnostic) as fallback inquiries.

#### Toxicity profile

- Class-typical RAS(ON) toxicity: acneiform rash (any-grade 30-40%), GI nausea / diarrhea, hepatic transaminitis
- Cumulative CRC-population AE profile still maturing; the breakthrough-designation PDAC dataset is the closest neighbor
- Pause around CRS-HIPEC required; eats into PFS clock

#### Counter-productive mechanisms / dissent

This is the dissent-heavy row of the case. **The critic vetoed on evidence-quality grounds** — ranking a sponsor-confirmation-gated n=0 A59T pick above replicated category-1 backbones inverts the evidence hierarchy. The conservative dissented ("hypothetical until sponsor confirms" framing — accurate but ranks the pick low rather than vetoing it). The concensusite dissented on guideline-fit (no NCCN / ESMO endorsement for atypical-KRAS off-protocol use; 1L displacement is outside the consensus stack). The advocate and risktaker endorsed on the asymmetric-upside argument: A59T is the single allele in the case dossier that the G12C-selective programs cannot touch, the preference file authorizes "surface all options" with efficacy-weight 0.7, and the load-bearing single phone call is the highest-leverage move on the file.

Synthesis per Hard Rule 1: the row stays in the table with status considered_with_caveats and the veto + dissents documented. The honest framing is that the highest-yield single action on the case is the **medinfo@revmed.com / 1-844-2-REVMED inquiry for A59T eligibility on NCT06445062** — if RevMed confirms, this becomes a real 2L+ contingent pick; if declines, **medical-affairs@jacobiopharma** for JAB-23E73 is the structural fallback (the codon-agnostic protocol text + no-prior-KRAS-inhibitor exclusion both fit), and S241656 is the secondary fallback. If all three sponsor inquiries return no, this rec collapses.

#### Practical considerations

Email medinfo@revmed.com or call 1-844-2-REVMED with the KRAS A59T VAF and clinical summary; ask explicitly whether atypical codon 59 mutations are accepted into the CRC arms of RMC-GI-102 (NCT06445062). If accepted, ask which arm fits (monotherapy / + cetuximab / + chemo combo). Note that the cetuximab arm runs into the A59T anti-EGFR question (rank 10) and the chemo-combo arm may interact with the peri-CRS-HIPEC window. Geographic scope: US + select EU + Australia sites for RASolve-GI. Sponsor covers the drug under protocol. Standard-of-care procedures bill the patient's insurance.

#### Why this rank

Rank 8 because the critic veto and two persona dissents bring the agreement score to -0.2, but the asymmetric-upside argument and the preference-file alignment keep the row in the considered_with_caveats column. Above rank 9 (post-HIPEC 2L+ SoC bench) on biomarker-targeting strictness — this row targets the user's stated targetable feature (KRAS A59T) where the SoC bench does not — but below rank 6 (bot/bal) because bot/bal has a published n=101 phase 1b signal in the patient's phenotype where this row has n=0 A59T clinical data.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| RMC-6236 RASolve-GI ([NCT06445062](https://clinicaltrials.gov/study/NCT06445062)) | n=0 A59T; sponsor confirmation gates eligibility | Class: rash 30-40%, GI nausea/diarrhea, hepatic | Sponsor: Revolution Medicines; medinfo@revmed.com / 1-844-2-REVMED |
| RMC-6236 monotherapy basket ([NCT05379985](https://clinicaltrials.gov/study/NCT05379985)) | Codon 12/13/61 only by protocol — A59T excluded | Class same as above | Sponsor: Revolution Medicines |
| JAB-23E73 ([NCT06973564](https://clinicaltrials.gov/study/NCT06973564)) | Codon-agnostic by protocol; A59T plausibly eligible | Phase 1/2; AE profile maturing | Sponsor: Jacobio |
| S241656 ERK inhibitor ([NCT05786924](https://clinicaltrials.gov/study/NCT05786924)) | KRAS/HRAS/NRAS/BRAF/CRAF codon-agnostic; CRC arms with FOLFOX/FOLFIRI ± anti-EGFR | Class: rash, GI, hepatic; AE profile maturing | Sponsor: Servier |
| Knox / Jiang RAS(ON) preclinical | PDX regression across G12/G13/Q61 at 25-50 mg/kg | n/a (preclinical) | [PMID 38778097](https://pubmed.ncbi.nlm.nih.gov/38778097), [PMID 38778099](https://pubmed.ncbi.nlm.nih.gov/38778099) |

### Rank 9. Post-CRS-HIPEC 2L+ SoC bench (FOLFOX-bev → aflibercept-FOLFIRI / ramucirumab-FOLFIRI → SUNLIGHT TAS-102+bev → FRESCO-2 fruquintinib → regorafenib)

*The replicated phase 3 OS floor the experimental picks have to beat. Sequenced post-CRS-HIPEC, around the bev peri-op hold, and modulated by rank-1 DPYD/UGT1A1 results.*

#### Evidence base

NCCN category 1 at each line. NO16966 (Saltz 2008, [PMID 18421054](https://pubmed.ncbi.nlm.nih.gov/18421054)) anchored FOLFOX/XELOX + bev at mPFS 9.4 vs 8.0 mo (HR 0.83). VELOUR (Van Cutsem 2012) aflibercept-FOLFIRI mOS 13.5 vs 12.1 (HR 0.82). RAISE (Tabernero 2015, [PMID 25862517](https://pubmed.ncbi.nlm.nih.gov/25862517)) ramucirumab-FOLFIRI mOS 13.3 vs 11.7 (HR 0.84). SUNLIGHT TAS-102 + bev mOS 10.8 vs 7.5 (HR 0.61). FRESCO-2 fruquintinib HR_OS 0.66. CORRECT regorafenib HR 0.77; CONCUR HR 0.55. Stacked, the field reaches 28-32 mo mOS for fit patients on optimal sequencing — that is the bar the experimental picks need to beat.

#### Likelihood of desired effect

Moderate-High at each line individually; stacked sequencing through the full bench achieves the 28-32 mo mOS the critic anchored on. No biomarker enrichment — the bench targets the patient's mCRC backbone phenotype rather than a specific targetable feature.

#### Toxicity profile

- Cumulative oxaliplatin neuropathy is rate-limiting for a 37yo with a long runway — bake OPTIMOX stop-and-go in
- Anti-angiogenic continuation past 2L compounds wound-healing / bleeding / hypertension
- TAS-102 G3+ neutropenia ~40%; fruquintinib hypertension and hand-foot syndrome
- DPYD + UGT1A1 results (rank 1) modulate dose calibration at each line

#### Counter-productive mechanisms / dissent

Endorsed by the three guideline / evidence-anchored seats (conservative, critic, concensusite); the advocate and risktaker did not formally rank this row but did not dissent on it either — both noted the SoC bench as the floor their experimental picks layered on or replaced. No mechanism-level counter-productive vector. The critic's notes section specifically named this as "the interventions with replicated RCT evidence the patient should actually receive."

#### Practical considerations

Whether the team runs FOLFOX or FOLFOXIRI pre-CRS (rank 2 intensification path) changes the 2L drug choice: FOLFOX-exposed patients have less to gain from aflibercept-FOLFIRI vs ramucirumab-FOLFIRI vs continuing bev. The oxaliplatin-naive lane is preserved by continuing FOLFIRI + bev pre-CRS, saving the cleaner 2L drug for after the surgical window. NRG-GI008 CIRCULATE-US ([NCT05174169](https://clinicaltrials.gov/study/NCT05174169)) is the ctDNA-guided adjuvant-duration trial the concensusite flagged for the post-CRS surveillance question.

#### Why this rank

Rank 9 because Libby's primary deliverable is the feature-targeted ranking and this row is the SoC reference frame rather than a feature-targeting pick. Surfaced explicitly to honor the user's "surface all options" framing and to anchor the experimental picks above against the replicated-RCT floor below. The critic's evidence-pyramid argument that the field reaches 28-32 mo mOS through this bench (not 21 mo through a single experimental pick) is the load-bearing reason this row sits in the ranking rather than under "classes examined but not ranked."

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| FOLFOX + bev (NO16966) | mPFS 9.4 vs 8.0 mo, HR 0.83 | G3+ neutropenia, cumulative neuropathy, bev class | [PMID 18421054](https://pubmed.ncbi.nlm.nih.gov/18421054) |
| Aflibercept-FOLFIRI (VELOUR) | mOS 13.5 vs 12.1 mo, HR 0.82 | Hypertension, proteinuria, hemorrhage | NCCN cat 1 2L |
| Ramucirumab-FOLFIRI (RAISE) | mOS 13.3 vs 11.7 mo, HR 0.84 | Anti-angiogenic class | [PMID 25862517](https://pubmed.ncbi.nlm.nih.gov/25862517) |
| TAS-102 + bev (SUNLIGHT) | mOS 10.8 vs 7.5 mo, HR 0.61 | G3+ neutropenia ~40%; nausea | NCCN cat 1 3L |
| Fruquintinib (FRESCO-2) | mOS HR 0.66 | Hypertension, hand-foot syndrome | NCCN cat 1 4L |
| Regorafenib (CORRECT / CONCUR) | HR_OS 0.77 / 0.55 | Hand-foot skin reaction; hepatic | NCCN cat 1 4L |

### Rank 10. Anti-EGFR (cetuximab / panitumumab) — default AVOID at 1L; structured research-framework lane only at later lines

*The atypical-KRAS anti-EGFR question. Default avoid per Sorich 2015 population-level meta-analytic data; not welded shut for later lines under a documented A59T functional argument.*

#### Evidence base

Sorich 2015 ([PMID 25115304](https://pubmed.ncbi.nlm.nih.gov/25115304), n=5,948 across 9 RCTs, RoB2:Low): in the any-new-RAS-mutant subset, OS HR 1.08 (95% CI 0.91-1.28) and PFS HR 1.03 (95% CI 0.78-1.36) — no anti-EGFR benefit. Schirripa 2015 ([PMID 24806288](https://pubmed.ncbi.nlm.nih.gov/24806288), n=786 retrospective): 0/9 responders among NRAS-mutant anti-EGFR-treated patients. Arena 2021 ([PMID 34031055](https://pubmed.ncbi.nlm.nih.gov/34031055), n=169, ROBINS-I:Moderate): A59 / A146 / K117 alleles show "occasional responders" with weaker MAPK signaling than canonical G12 mutants — hypothesis-generating only. Lochhead 2018 ([PMID 30538852](https://pubmed.ncbi.nlm.nih.gov/30538852)): single-patient case report of -36% target-lesion change on panitumumab + FOLFIRI in a KRAS A59T tumor — anecdote, not population-level evidence.

#### Likelihood of desired effect

Low at 1L. The population-level evidence (n=5,948 RoB2:Low meta-analytic OS HR 1.08) wins against the Lochhead n=1 PR by a wide margin. The Arena 2021 functional data are the strongest argument that A59 alleles should be assessed individually rather than as a flat anti-EGFR contraindication, but that argument carries cleaner at later lines under a research framework than at 1L displacement of the chemo + bev backbone. Uncharacterized at later lines under ASCEND-CRC NCT07318389 with a documented A59T-specific functional argument.

#### Toxicity profile

- Anti-EGFR-class acneiform rash G3+ 10-20%, hypomagnesemia, paronychia, infusion reactions
- Compounded wound-healing risk if administered around CRS-HIPEC

#### Counter-productive mechanisms / dissent

The concensusite and conservative seats vetoed on guideline-fit and population-evidence grounds. The advocate and risktaker dissented on the population-level closure: the preference file's "surface all options" framing with efficacy-weight 0.7 authorizes outside-guideline thinking when biology supports it, and the Arena 2021 functional data are the strongest atypical-KRAS anti-EGFR-rechallenge argument in the field. The conservative seat itself softened on cross-critique to "default AVOID pending functional characterization, with anti-EGFR rechallenge under a research framework (ASCEND-CRC NCT07318389) defensible at later lines if a specific A59T functional argument is made." Synthesis per Hard Rule 1: carried as considered_with_caveats with the structured research-framework path explicitly named; default AVOID at 1L; not welded shut for later lines.

#### Practical considerations

Cetuximab off-label use in KRAS-mutant mCRC has no compendium support and payer access is unlikely. The defensible path at later lines is a research framework (ASCEND-CRC platform [NCT07318389] or the RMC-6236 + cetuximab arm of RASolve-GI if RevMed accepts A59T per rank 8) where the A59T-specific functional argument can be made and tracked. Lilly medical information: 1-800-545-5979 for Erbitux specific questions; Amgen for Vectibix.

#### Why this rank

Rank 10 because two personas vetoed and two dissented — the conservative softened on cross-critique but did not endorse, the concensusite stood on the population-evidence veto. The structured research-framework lane at later lines keeps the door open per the dissenters' argument while honoring the veto-grade objections to 1L use.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Anti-EGFR + chemo (Sorich 2015 meta-analysis) | New-RAS-mutant: OS HR 1.08 (0.91-1.28), PFS HR 1.03 (0.78-1.36) — no benefit | Acneiform rash G3+ 10-20%, hypomagnesemia | [PMID 25115304](https://pubmed.ncbi.nlm.nih.gov/25115304) |
| Anti-EGFR in NRAS-mut CRC (Schirripa 2015) | 0/9 ORR in NRAS-mutant cohort | Class as above | [PMID 24806288](https://pubmed.ncbi.nlm.nih.gov/24806288) |
| A59 / A146 / K117 functional + anti-EGFR (Arena 2021) | "Occasional responders" with weaker MAPK signaling | n/a (functional study) | [PMID 34031055](https://pubmed.ncbi.nlm.nih.gov/34031055) |
| Panitumumab + FOLFIRI A59T case report (Lochhead 2018) | -36% target-lesion change, n=1 | Anecdotal | [PMID 30538852](https://pubmed.ncbi.nlm.nih.gov/30538852) |

## Classes examined but not ranked

- **BCL-xL-directed (navitoclax, DT2216, AZD0466, pelcitoclax) for 20q11 BCL2L1 + TOP1 co-amplification** — navitoclax solid-tumor program discontinued; DT2216 has no CRC trial slot (pediatric COG + irinotecan trial NCT06620302 is the closest precedent and accepts pediatric patients only); AZD0466 / pelcitoclax abstract-only. Surface as a recurrence pre-position for compassionate-use conversation if the 20q segment boundary confirms BCL2L1-restricted amplification; not currently enrollable for this patient.
- **ATR / WEE1 / HSP90 synthetic-lethal-with-mutant-p53 (ceralasertib, camonsertib, elimusertib) for TP53 R273** — thin mCRC evidence; surface as a 3L+ trial-slot watch list. The rank-1 NGS R273-substitution call (R273H vs C vs L vs S) sharpens any future trial discussion.
- **Wnt-axis (PORCN inhibitors LGK974/WNT974, tankyrase inhibitors, ST316, frizzled antibodies) for APC E1295** — Rodon 2021 WNT974 0% RECIST responses across 94 patients; ST316 ASCO GI 2025 abstract-only with prolonged SD but no ORRs; porcupine class faces APC-loss bypass biology (Liu / Cong 2013 PMID 23258887). Not currently enrollable on an actionable axis for this patient.
- **TGF-beta-axis (galunisertib + nivolumab, bintrafusp alfa-class, NIS793, BCA101) for SMAD4 R361H** — galunisertib + nivolumab Yamazaki 2023 ORR 5% with no CRC subset responses; Lilly wound the program down. Surface as a 3L+ trial-slot watch list if CMS4 + immune-excluded phenotype confirms on the rank-1 transcriptomic add-on.
- **KRAS peptide vaccines (ELI-002, JHU NCT06411691)** — vaccine peptides encode G12C/G12D/G12V/G12R/G12A/G12S/G13D; A59T is not among them. Patient is not biomarker-eligible.
- **TCR-T / ImmTAC (afami-cel, lete-cel, IMA203, brenetafusp)** — currently not approved for CRC; flagged on the rank-1 workup as a low-priority HLA-A typing bank for future trial readiness.
- **MOUNTAINEER tucatinib + trastuzumab** — RAS-WT label restriction; A59T fails the gate regardless of HER2 status. T-DXd (rank 7) is the RAS-allowed HER2-directed substitute.
- **PIPAC oxaliplatin or 5-FU (NCT04329494 City of Hope, NCT06367270 Hong Kong)** — relevant only if upfront CRS-HIPEC is deferred or peritoneal recurrence develops post-CRS; flagged as recurrence pre-position.

## Ranked prioritization

### Workup (rank 1 — precondition)

| Rank | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
|---|---|---|---|---|---|
| 1 | **Diagnostic gates: comprehensive NGS + HER2 IHC/FISH + MMR IHC + TMB + PD-L1 + DPYD/UGT1A1 + Signatera baseline**<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small> | High — diagnostic certainty across seven decision gates; precondition for every therapeutic call below. | Low (none — diagnostic test on archival tissue + peripheral blood draw) | <strong>N/A</strong> (Diagnostic workup; no mechanism-level risk to a therapeutic goal.) | **Unblocks anti-EGFR eligibility, HER2-directed options, ICI doors, PIK3CA confirmation, fluoropyrimidine safety, and post-CRS surveillance from a single archival-block send-out plus blood draws.** |

### Unified ranked options (ranks 2-14)

| Rank | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
|---|---|---|---|---|---|
| 2 | **Continue FOLFIRI + bevacizumab (FOLFOXIRI + bev intensification permitted)**<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-critic">critic</span> <span class="persona persona-advocate">advocate</span> <span class="persona persona-risktaker">risktaker</span></small> | High — replicated phase 3 OS signal across AVF2107g, BICC-C, MAVERICC, TRIBE2; ESMO MCBS 3. | Moderate (G3+ neutropenia ~25-30%, G3+ diarrhea ~14% on FOLFIRI; cumulative neuropathy and bev wound-healing constraints with intensification) | <strong>Low</strong> (Bevacizumab wound-healing impairment in the peri-operative window — managed by the 4-6 week hold; not a mechanism-level blunting of the cytotoxic backbone.) | **The replicated 1L OS backbone with the longest safety dossier in the case; the bev peri-op hold is the load-bearing safety thread, and FOLFOXIRI intensification is a permitted upgrade for a fit 37-year-old.** |
| 3 | **Low-dose aspirin 160 mg PO QD (PIK3CA-pathway adjunct, ALASCCA-derived)**<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small> | Moderate — three concordant biomarker-stratified signals (ALASCCA HR 0.49, 80702 celecoxib OS HR 0.41, Liao 2012 HR 0.18) but indication gap from resected adjuvant to metastatic-equivalent post-HIPEC. | Low (G3+ GI bleed ~3% vs 2% on ALASCCA; manageable with PPI + perioperative hold) | <strong>Low</strong> (Aspirin hold required around bev cycles and CRS-HIPEC to avoid additive bleeding; mechanism direction itself is supportive, not counter-productive.) | **The only RoB2:Low phase 3 RCT in the dossier with a biomarker match — a cheap, layered, guideline-adopted adjunct that almost any other pick stacks on top of.** |
| 4 | **CRS at high-volume center; mitomycin C HIPEC if elected (PRODIGE 7 framing)**<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-risktaker">risktaker</span><br><em>dissent:</em> <span class="persona persona-critic">critic</span></small> | Moderate for CRS (NCCN-endorsed selected-patient mOS 30-40 mo); Low for the HIPEC component specifically (PRODIGE 7 negative for oxaliplatin; no positive randomized signal for mitomycin C). | High (CRS-HIPEC 60-day morbidity ~25-40% G3+; bleeding, anastomotic leak, infection, prolonged ileus; treatment-related mortality 1-3% at high-volume centers, higher at lower-volume) | <strong>Moderate</strong> (Critic dissent stands on mechanism grounds: oxaliplatin HIPEC negative randomized OS readout; mitomycin C HIPEC has no positive randomized OS readout either — the procedure window itself delays systemic therapy.) | **CRS retains the OS spine for resectable peritoneal CRC; HIPEC sits outside randomized OS validation — mitomycin C is the defensible perfusate at a high-volume center if HIPEC is elected.** |
| 5 | **Inavolisib + bevacizumab on INTRINSIC ([NCT04929223](https://clinicaltrials.gov/study/NCT04929223))** (conditional on PIK3CA M1043I somatic + clonal confirmation)<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-critic">critic</span><br><em>dissent:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span></small> | Moderate ASSUMING M1043I confirmed — INAVO120 PFS HR 0.43 is cross-tumor breast; CRC efficacy is hypothesis-grade (Juric 2018 2 PRs / 134 CRC subset; INTRINSIC arm-specific PFS unpublished). | Moderate (G3+ hyperglycemia 5.6%, any-grade 58.6%; G3+ stomatitis 5.6%; G3+ diarrhea 3.7%; discontinuation 6.5%) | <strong>Moderate</strong> (Critic and concensusite dissented on mechanism grounds: KRAS A59T co-activation may blunt single-pathway PI3K-alpha inhibition; cross-tumor breast extrapolation does not address CRC's downstream-RAS escape biology.) | **The cleanest PIK3CA M1043I mechanism match in the dossier, gated by cross-tumor extrapolation and KRAS A59T co-activation — trial-route only, sequenced at progression rather than 1L displacement.** |
| 6 | **Botensilimab + balstilimab at 2L+ (USC NCT06336902 / EAP NCT06751524 / BATTMAN NCT07152821)**<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-critic">critic</span><br><em>dissent:</em> <span class="persona persona-critic">critic</span> <span class="persona persona-conservative">conservative</span></small> | Moderate in the NLM peritoneal-dominant subset (ORR 22%, mOS 20.9 mo Bullock 2024) — strongest MSS-CRC ICI signal of the decade but selection bias + no BSC comparator until BATTMAN reads out. | Moderate (G3+ colitis 12%, G3+ hepatitis 8%, G3+ pyrexia in subset; cumulative G3+ irAE 35-38%) | <strong>Moderate</strong> (Critic dissented on evidence-quality mechanism (post-hoc NLM subgroup); conservative dissented on stacking research-only FMD + IV-C adjuncts on Fc-enhanced anti-CTLA-4 in active peritoneal disease.) | **Strongest modern MSS-CRC immunotherapy signal mapped to the patient's NLM peritoneal phenotype; 2L+ trial-route only, gated by FOLFIRI-bev progression and travel logistics.** |
| 7 | **Trastuzumab deruxtecan (T-DXd) on DESTINY-CRC02 ([NCT04744831](https://clinicaltrials.gov/study/NCT04744831))** (conditional on HER2 IHC 3+ from rank-1 workup)<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-critic">critic</span></small> | High in HER2 IHC 3+ subset (DESTINY-CRC02 ORR ~38% including RAS-mutant); contingent on HER2 status — foreclosed if HER2 negative (3-5% prior probability of positive). | Moderate (G3+ neutropenia ~30%, G3+ ILD 5-10% with treatment-related deaths reported, G3+ nausea/vomiting 10-15%) | <strong>Low</strong> (On-target ILD is the dominant counter-productive vector; RAS-mutant subset has lower absolute response than RAS-WT but A59T-specific behavior unreported.) | **The single most-actionable wildcard if HER2 amplification returns positive — RAS-mutant-allowed under the 2024 pan-tumor accelerated approval, and the cleanest HER2 path for an A59T patient.** |
| 8 | **Daraxonrasib (RMC-6236) on RASolve-GI ([NCT06445062](https://clinicaltrials.gov/study/NCT06445062))** (gated on sponsor confirming A59T eligibility)<br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-risktaker">risktaker</span><br><em>dissent:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span><br><em>veto:</em> <span class="persona persona-critic">critic</span></small> | Low — zero published A59T clinical efficacy in any RAS(ON) or pan-RAS program; mechanism plausibility from Knox/Jiang Nature 2024 preclinical PDX work only. | Moderate (class-typical RAS(ON) acneiform rash 30-40% any-grade, GI nausea/diarrhea, hepatic; cumulative CRC profile maturing) | <strong>High</strong> (Critic veto stands on evidence-quality / mechanism grounds: ranking a sponsor-confirmation-gated n=0 A59T pick above replicated category-1 backbones inverts the evidence hierarchy.) | **The asymmetric-upside single phone call for the atypical KRAS A59T allele — sponsor-confirmation-gated and critic-vetoed; document the inquiry result before any other RAS(ON) action.** |
| 9 | **Post-CRS-HIPEC 2L+ SoC bench (FOLFOX-bev → aflibercept-FOLFIRI / ramucirumab-FOLFIRI → SUNLIGHT TAS-102+bev → FRESCO-2 fruquintinib → regorafenib)**<br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small> | Moderate-High — replicated phase 3 OS signal at each line; stacked sequencing 28-32 mo mOS achievable in fit patients. | Moderate (cumulative oxaliplatin neuropathy is rate-limiting; G3+ neutropenia and diarrhea at each line; anti-angiogenic AE compound) | <strong>Low</strong> (No mechanism-level counter-productive vector; cumulative neuropathy and anti-angiogenic compound AEs are patient-level toxicity, not therapeutic-goal blunting.) | **The replicated 2L+ phase 3 OS floor the experimental picks have to beat — bake OPTIMOX in for the long young-patient runway and modulate by DPYD/UGT1A1 results.** |
| 10 | **Cetuximab / panitumumab — default AVOID at 1L; ASCEND-CRC research framework only at later lines**<br><small><em>dissent:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-risktaker">risktaker</span><br><em>veto:</em> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-conservative">conservative</span></small> | Low at 1L (Sorich 2015 OS HR 1.08 in any-new-RAS-mutant n=5,948); uncharacterized at later lines under a research framework with A59T-specific functional argument. | Moderate (G3+ acneiform rash 10-20%, hypomagnesemia, paronychia; manageable but real) | <strong>High</strong> (Conservative + concensusite veto stands on mechanism: A59T is treated as RAS-activating by NCCN consensus, so anti-EGFR is mechanism-counter-productive at the population level.) | **Default AVOID at 1L per population-level meta-analysis; structured research-framework rechallenge defensible at later lines on Arena 2021 functional grounds — not welded shut, not 1L-recommendable.** |
| 11 | **Sotorasib + panitumumab and adagrasib + cetuximab — NOT RECOMMENDED for KRAS A59T (allele-incompatible)**<br><small><em>veto:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small> | None — mechanism-incompatible at the covalent-warhead level; A59T lacks the switch-II cysteine the drugs target. | Moderate (class acneiform rash, GI nausea/diarrhea, hepatic) — but zero efficacy for A59T makes any AE counter-productive by definition. | <strong>High</strong> (Universal veto on mechanism grounds: drug binds G12C-specific cysteine; A59T lacks the warhead substrate entirely.) | **Allele-incompatible — listed so the consultation team sees the closed door explicitly; the G12C-selective drugs cannot reach A59T at the covalent-warhead level.** |
| 12 | **Single-agent pembrolizumab / dostarlimab / nivolumab-ipilimumab — NOT RECOMMENDED in MSS / TMB-low / PD-L1-negative**<br><small><em>veto:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small> | None — phenotype-incompatible (MSS / TMB-low / PD-L1-neg); unless rank-1 MMR IHC unexpectedly returns dMMR. | Moderate (G3+ irAE colitis, hepatitis, pneumonitis, endocrinopathy) — counter-productive without target engagement. | <strong>High</strong> (Universal veto on phenotype grounds: ICI biology requires MSI-H or TMB-H or PD-L1-high substrate, none of which the patient presents.) | **Phenotype-foreclosed in MSS / TMB-low / PD-L1-negative — listed so the door is explicitly closed; the rank-1 MMR IHC orthogonal is the only path that reopens it.** |
| 13 | **Eprenetapopt (APR-246) and rezatapopt (PC14586) for TP53 R273 — NOT RECOMMENDED**<br><small><em>veto:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small> | None — eprenetapopt solid-tumor program closed; rezatapopt is Y220C-restricted and KRAS-WT-only. | Low (none — drugs not accessible to this patient) | <strong>High</strong> (Universal veto on program-status + structural-design grounds: drug-allele mismatch at the binding-pocket level.) | **Closed at the program + structural-design level; documented so the TP53 R273 reactivator question is explicitly addressed and the future ATR/WEE1 watch-list framing is preserved.** |
| 14 | **Oxaliplatin HIPEC framed as OS-positive — NOT RECOMMENDED**<br><small><em>veto:</em> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small> | None over CRS alone — PRODIGE 7 negative for OS; COLOPEC and PROPHYLOCHIP reinforce the negative. | High (60-day G3+ morbidity 25-40%, treatment-related mortality 1-3%; without OS benefit) | <strong>High</strong> (Veto stands on mechanism: oxaliplatin HIPEC adds operative-window morbidity that delays systemic therapy without offsetting the patient with an OS gain.) | **Closed on randomized evidence — surgical team retains autonomy on HIPEC agent choice; oxaliplatin perfusate specifically should not be framed as OS-validated in the family conversation.** |

!!! note "Reading the table"
    **Toxicity burden** is patient-level AE severity; **Counter-productive MoA** is mechanism-level risk to the therapeutic goal (distinct from patient AEs in the toxicity column). The persona pills under each intervention are the at-a-glance board signal; the full per-persona rationale lives on the board page.

## Caveats

- **Evidence-base caveats.** Two of the experimental picks rest on cross-tumor or hypothesis-grade evidence in CRC. Inavolisib's PFS HR 0.43 anchor is HR+/HER2- breast (INAVO120); the CRC arm-specific INTRINSIC PFS / OS has not posted, and the M1043I-specific subset within Group A is unreported at scale. Bot/bal's NLM-subset ORR 22% / mOS 20.9 mo comes from a post-hoc-defined responder phenotype within a single-arm phase 1b (Bullock 2024 Nat Med); the CCTG BATTMAN phase 3 OS readout vs BSC is 2027-2028. RMC-6236 has zero published A59T clinical efficacy across any program — the sponsor-inquiry gate is the entire decision. ALASCCA's PIK3CA Group A 95% CI upper bound at 0.98 means magnitude is fragile even within the resected adjuvant indication; the post-CRS-HIPEC metastatic-equivalent state adds an extrapolation layer.
- **Compartment / biomarker dependencies.** The ranking is biomarker-conditional in narrow ways at three rank positions. Rank 5 (inavolisib) requires PIK3CA M1043I somatic + clonal confirmation from the rank-1 NGS; if M1043I is subclonal or germline, the trial slot is foreclosed. Rank 7 (T-DXd) is HER2-amp-conditional and the prior probability of a positive test is 3-5%; the row is the highest-yield wildcard if positive and foreclosed if negative. Rank 8 (RMC-6236) is sponsor-confirmation-conditional on RevMed accepting A59T; if declined, the JAB-23E73 and S241656 fallback inquiries decide whether the RAS-pathway-direct lane stays open. The rank-1 MMR IHC orthogonal closes the ICI door definitively (concordant MSS, ~95% prior) or reopens it entirely (discordant dMMR, ~5% prior).
- **What would change the ranking.**
    - **RevMed confirms A59T eligible on NCT06445062** → rank 8 jumps to a real contingent 2L+ pick with the asymmetric-upside argument intact.
    - **HER2 IHC returns 3+ or 2+ with FISH ratio ≥2.0** → rank 7 jumps to the front of the post-1L queue and ranks 5/6 get re-prioritized against it.
    - **MMR IHC unexpectedly returns dMMR** → reverses the entire ranking; single-agent pembrolizumab leaps to 1L consideration.
    - **TMB on F1CDx ≥10 mut/Mb** → tumor-agnostic pembrolizumab label unlocks at later lines.
    - **DPYD *2A / HapB3 carrier** → FOLFIRI dose-rationalize for remaining cycles per CPIC; modifies the rank-2 plan.
    - **Signatera positive at day 30-60 post-CRS** → escalates the adjuvant-therapy duration conversation toward extended systemic exposure rather than observation.
    - **POLE / POLD1 proofreading variant on germline add-on** → reopens the ICI door even with MSS / TMB-low intake calls.
- **Re-scoping caveat.** If the patient's preferences shift (toxicity vetoes introduced, trial-prefer revoked, ECOG drops to 2) or the clinical state changes (liver mets recur, peritoneal phenotype expands beyond resectable, primary tumor becomes symptomatic), the ranking is re-scoped: the bot/bal NLM responder phenotype assumption (rank 6) is the most preference-sensitive, and the FOLFOXIRI intensification path (rank 2) is the most performance-status-sensitive.

## Sources

### PubMed

- [PMID 15175435](https://pubmed.ncbi.nlm.nih.gov/15175435) — Hurwitz 2004, AVF2107g bevacizumab + IFL mCRC
- [PMID 17947725](https://pubmed.ncbi.nlm.nih.gov/17947725) — Fuchs 2007, BICC-C FOLFIRI as irinotecan reference
- [PMID 18421054](https://pubmed.ncbi.nlm.nih.gov/18421054) — Saltz 2008, NO16966 FOLFOX/XELOX + bev
- [PMID 20689948](https://pubmed.ncbi.nlm.nih.gov/20689948) — Van der Speeten mitomycin C HIPEC pharmacokinetics
- [PMID 21570278](https://pubmed.ncbi.nlm.nih.gov/21570278) — UGT1A1 *28 irinotecan safety
- [PMID 23094721](https://pubmed.ncbi.nlm.nih.gov/23094721) — Liao 2012 NEJM aspirin in PIK3CA-mutant CRC
- [PMID 24806288](https://pubmed.ncbi.nlm.nih.gov/24806288) — Schirripa 2015 NRAS-mut anti-EGFR
- [PMID 25115304](https://pubmed.ncbi.nlm.nih.gov/25115304) — Sorich 2015 anti-EGFR meta-analysis n=5,948
- [PMID 25337750](https://pubmed.ncbi.nlm.nih.gov/25337750) — Loupakis 2014 TRIBE FOLFOXIRI + bev
- [PMID 25862517](https://pubmed.ncbi.nlm.nih.gov/25862517) — Tabernero 2015 RAISE ramucirumab-FOLFIRI
- [PMID 26028255](https://pubmed.ncbi.nlm.nih.gov/26028255) — Le 2015 NEJM dMMR pembrolizumab selectivity
- [PMID 27108243](https://pubmed.ncbi.nlm.nih.gov/27108243) — HERACLES HER2 IHC + FISH scoring
- [PMID 27959278](https://pubmed.ncbi.nlm.nih.gov/27959278) — comprehensive NGS in mCRC reference
- [PMID 29355075](https://pubmed.ncbi.nlm.nih.gov/29355075) — Overman 2018 CheckMate 142 nivo-ipi MSI-H
- [PMID 29401002](https://pubmed.ncbi.nlm.nih.gov/29401002) — Juric 2018 alpelisib phase 1a PI3K-altered solid tumors
- [PMID 30224341](https://pubmed.ncbi.nlm.nih.gov/30224341) — MAVERICC FOLFOX-bev vs FOLFIRI-bev 1L
- [PMID 30538852](https://pubmed.ncbi.nlm.nih.gov/30538852) — Lochhead 2018 KRAS A59T panitumumab PR case report
- [PMID 30604034](https://pubmed.ncbi.nlm.nih.gov/30604034) — PD-L1 clone / CPS / TPS scoring reference
- [PMID 31272834](https://pubmed.ncbi.nlm.nih.gov/31272834) — Klaver 2019 COLOPEC adjuvant HIPEC T4/perforated
- [PMID 31416808](https://pubmed.ncbi.nlm.nih.gov/31416808) — NGS-MSI vs MMR-IHC concordance
- [PMID 31699932](https://pubmed.ncbi.nlm.nih.gov/31699932) — Vasan 2019 M1043 kinase-domain PI3K-alpha sensitization
- [PMID 32007158](https://pubmed.ncbi.nlm.nih.gov/32007158) — Cremolini 2020 TRIBE2 FOLFOXIRI + bev
- [PMID 32576704](https://pubmed.ncbi.nlm.nih.gov/32576704) — peritoneal CRC ctDNA prognostic
- [PMID 32717181](https://pubmed.ncbi.nlm.nih.gov/32717181) — Goere 2020 PROPHYLOCHIP-PRODIGE 15 second-look + HIPEC
- [PMID 33417845](https://pubmed.ncbi.nlm.nih.gov/33417845) — Quenet 2021 PRODIGE 7 oxaliplatin HIPEC negative OS
- [PMID 34031055](https://pubmed.ncbi.nlm.nih.gov/34031055) — Arena 2021 atypical KRAS functional characterization
- [PMID 34754095](https://pubmed.ncbi.nlm.nih.gov/34754095) — Signatera tumor-informed ctDNA / GALAXY MRD
- [PMID 36546659](https://pubmed.ncbi.nlm.nih.gov/36546659) — Yaeger 2023 KRYSTAL-1 adagrasib G12C
- [PMID 37870968](https://pubmed.ncbi.nlm.nih.gov/37870968) — Fakih 2023 CodeBreaK 300 sotorasib + panitumumab G12C
- [PMID 38778097](https://pubmed.ncbi.nlm.nih.gov/38778097) — Knox 2024 Nature RAS(ON) preclinical
- [PMID 38778099](https://pubmed.ncbi.nlm.nih.gov/38778099) — Jiang 2024 Nature RAS(ON) preclinical
- [PMID 38871975](https://pubmed.ncbi.nlm.nih.gov/38871975) — Bullock 2024 Nat Med BOT/BAL MSS mCRC NLM ORR 22%
- [PMID 38889377](https://pubmed.ncbi.nlm.nih.gov/38889377) — Yang/Meyerhardt 2024 CALGB/SWOG 80702 celecoxib PIK3CA subset
- [PMID 39058319](https://pubmed.ncbi.nlm.nih.gov/39058319) — Raghav 2024 DESTINY-CRC02 T-DXd ORR ~38%
- [PMID 39476340](https://pubmed.ncbi.nlm.nih.gov/39476340) — Jhaveri 2024 NEJM INAVO120 PFS HR 0.43
- [PMID 39550351](https://pubmed.ncbi.nlm.nih.gov/39550351) — Rovers 2024 CAIRO6 perioperative chemo + CRS-HIPEC
- [PMID 40932470](https://pubmed.ncbi.nlm.nih.gov/40932470) — rezatapopt Y220C structural restriction
- [PMID 40958923](https://pubmed.ncbi.nlm.nih.gov/40958923) — DPYD genotyping NCCN v1.2026 + FDA label update
- [PMID 40979555](https://pubmed.ncbi.nlm.nih.gov/40979555) — Frödin/Martling 2025 NEJM ALASCCA aspirin PIK3CA exon 9/20

### ClinicalTrials.gov

- [NCT02758951](https://clinicaltrials.gov/study/NCT02758951) — CAIRO6 perioperative chemo + CRS-HIPEC
- [NCT04585750](https://clinicaltrials.gov/study/NCT04585750) — PYNNACLE rezatapopt Y220C-restricted (rule-out)
- [NCT04744831](https://clinicaltrials.gov/study/NCT04744831) — DESTINY-CRC02 T-DXd
- [NCT04779554](https://clinicaltrials.gov/study/NCT04779554) — Flat-dose vs weight-based mitomycin C HIPEC (Kentucky)
- [NCT04861558](https://clinicaltrials.gov/study/NCT04861558) — EFFIPEC CRS vs CRS + HIPEC (Sweden/India)
- [NCT04929223](https://clinicaltrials.gov/study/NCT04929223) — INTRINSIC inavolisib + bev mCRC platform
- [NCT05379985](https://clinicaltrials.gov/study/NCT05379985) — RMC-6236 monotherapy basket (codon 12/13/61 only — A59T excluded)
- [NCT05786924](https://clinicaltrials.gov/study/NCT05786924) — S241656 Servier ERK inhibitor RAS/MAPK basket
- [NCT06336902](https://clinicaltrials.gov/study/NCT06336902) — USC BOT/BAL + FMD + IV vitamin C in KRAS-mutant MSS mCRC
- [NCT06445062](https://clinicaltrials.gov/study/NCT06445062) — RASolve-GI RMC-6236 (A59T sponsor-inquiry gate)
- [NCT06751524](https://clinicaltrials.gov/study/NCT06751524) — Agenus BOT/BAL Expanded Access Protocol
- [NCT06973564](https://clinicaltrials.gov/study/NCT06973564) — JAB-23E73 Jacobio (codon-agnostic atypical-KRAS fallback)
- [NCT07152821](https://clinicaltrials.gov/study/NCT07152821) — CCTG BATTMAN BOT/BAL vs BSC (registrational)
- [NCT07291180](https://clinicaltrials.gov/study/NCT07291180) — Yale MRT-guided HIPEC selection

## Transparency artifacts

- [Trial table](trials.md) — 59 rows, all columns
- [Clinical evidence table](evidence.md) — 61 rows
- [Manuscripts inventory](manuscripts.md) — flat master table with sample size, effect size, variance, toxicity columns
- [Board page](board.md) — 5 persona positions, 20 cross-critiques, full agreement matrix
- [Recommendations table](recommendations.md) — ranked rec rows with full evidence anchors
- [Plain-language summary](plain_language.md) — patient / caregiver layer (downstream of this page)

## Run log

Authored 2026-05-29 by the PI agent on the standard Libby pipeline. Inputs supplied: `profile.json`, `preferences.json`, `target_validation.jsonl` (18 rows), `trials.jsonl` (59 rows), `clinical_evidence.jsonl` (61 rows), `preclinical_evidence.jsonl` (39 rows), `accessibility.jsonl` (61 rows), `board/positions.jsonl` (5 rows), `board/critiques.jsonl` (20 rows). Inferences carried forward: ECOG 1 from intake-stated FOLFIRI tolerance (flagged for confirmation per the user free text); HIPEC framing per the explicit user request to surface PRODIGE 7 honestly rather than veto the surgical plan; KRAS A59T sponsor-inquiry-gated picks ranked as considered_with_caveats per Hard Rule 1 with the critic veto and conservative / concensusite dissents documented; HER2 amplification ranked as a conditional positive-branch wildcard at rank 7 rather than splitting the table into a separate Path B because the prior probability is 3-5% and the rank-1 workup gates it. The single unified ranking covers workup (rank 1) + feature-targeting therapeutic options (ranks 2-10) + Hard-Rule-1 documented vetoes (ranks 11-14). For re-runs: the load-bearing single action is the medinfo@revmed.com inquiry on NCT06445062 A59T eligibility; the second load-bearing action is the HER2 IHC + reflex FISH result; both shape ranks 5-8 directly.

<!-- libby:downloads:begin -->

## Downloads

### HTML

- [Target validation paths](target_validation.md?v=60ae8f51) — per-feature biomarker-workup table with providers and references, sortable in-browser
- [Recommendations table](mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4-recommendations.html?v=9deeb66c) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide](accessibility.md?v=5c99e682) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Access guide (offline)](mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4-accessibility.html?v=6133b7ca) — same access-guide content packaged as a self-contained HTML that opens offline
- [Master manuscripts table](manuscripts.md?v=d90da807) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Master manuscripts table (offline)](mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4-manuscripts.html?v=a3a786ce) — same manuscripts inventory packaged as a self-contained HTML that opens offline

### PDF

- [Target validation paths](mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4-target-validation.pdf?v=a3e93fd8) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table](mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4-recommendations.pdf?v=5a893110) — ranked options + pipeline context + evidence in detail, in a print-friendly PDF
- [Access guide](mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4-accessibility.pdf?v=f8b16172) — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF
- [Master manuscripts table](mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4-manuscripts.pdf?v=eb7f2023) — every paper considered — n, effect, variance, toxicities, in a print-friendly PDF
- [Patient/caregiver PDF](mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4-plain-language.pdf?v=0010a141) — plain-language summary

<!-- libby:downloads:end -->

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
