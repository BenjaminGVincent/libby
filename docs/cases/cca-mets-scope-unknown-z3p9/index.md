<meta name="robots" content="noindex">

# `cca-mets-scope-unknown-z3p9`

<!-- libby:case-output:begin -->

## Case output

- [Target validation paths (PDF)](cca-mets-scope-unknown-z3p9-target-validation.pdf?v=e3fd75db) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table (HTML)](cca-mets-scope-unknown-z3p9-recommendations.html?v=f0b69849) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide (HTML)](accessibility.md?v=0f1ac5cf) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, sortable in-browser
- [Access guide (offline HTML)](cca-mets-scope-unknown-z3p9-accessibility.html?v=719b462f) — same access-guide content as the in-browser page, packaged as a self-contained HTML that opens offline
- [Master manuscripts table (HTML)](manuscripts.md?v=de7b9de7) — every paper considered — n, effect, variance, toxicities, sortable in-browser
- [Master manuscripts table (offline HTML)](cca-mets-scope-unknown-z3p9-manuscripts.html?v=7fe9c969) — same manuscripts inventory as the in-browser page, packaged as a self-contained HTML that opens offline
- [Patient/caregiver PDF](cca-mets-scope-unknown-z3p9-plain-language.pdf?v=11a205bb) — plain-language summary

<!-- libby:case-output:end -->
## Research question

In metastatic cholangiocarcinoma with no molecular profiling supplied at intake, what targeted interventions could the recognized actionable biliary panel open, gated on comprehensive genomic profiling?

## Patient profile (scrubbed)

- **Primary site / histology:** biliary tract — cholangiocarcinoma (intrahepatic vs perihilar vs distal subsite not specified at intake)
- **Stage:** IV (metastatic) per the stated diagnosis; full TNM and metastatic-site inventory not supplied
- **Performance status (assumed):** ECOG 1
- **Age band (assumed):** 60-69 (near the CCA median; placeholder, not user-supplied)
- **Sex:** unknown
- **Biomarkers — every candidate `ngs_pending`, none tested:**
    - **FGFR2 fusion/rearrangement** — untested. Resolution: RNA-based fusion panel (preferred) or DNA NGS with fusion calling. Gates pemigatinib, futibatinib, infigratinib.
    - **IDH1 R132** — untested. Resolution: tumor DNA NGS hotspot. Gates ivosidenib.
    - **HER2 (ERBB2) amplification/overexpression** — untested. Resolution: HER2 IHC (4B5) with reflex ISH, not an NGS copy-number call. Gates zanidatamab, trastuzumab deruxtecan.
    - **BRAF V600E** — untested. Resolution: tumor NGS (VE1 IHC as a screen, confirmed by NGS/PCR). Gates dabrafenib + trametinib.
    - **MSI-H / dMMR and TMB-high** — untested. Resolution: MMR IHC with reflex MSI-PCR, and NGS-derived TMB. Gates pembrolizumab.
    - **NTRK1/2/3 and RET fusion** — untested. Resolution: RNA-based fusion panel. Gates larotrectinib/entrectinib (NTRK) and selpercatinib (RET).
    - **KRAS G12C** — untested. Resolution: tumor DNA NGS. Gates adagrasib/sotorasib-class inhibitors and trial enrollment.
- **Prior therapy:** none recorded (history not supplied).

## Preferences

- **Efficacy/toxicity weight:** 0.5 (balanced; stated as a neutral placeholder, not an expressed value)
- **Toxicity vetoes:** none stated
- **Modality constraints:** none stated
- **Free text:** "SCOPE-UNKNOWN CASE. Input was 'metastatic cholangiocarcinoma, no other information.'" No molecular profiling, prior-therapy history, organ-function labs, demographics, or patient preferences were supplied.
- **Trials preferred:** yes

<!-- libby:target-validation:begin -->

## Target validation paths

This case hinges on one test that has not been run: comprehensive genomic profiling. No molecular data was supplied, so every targeted option is unmeasured and a single paired DNA plus RNA panel is the gate for all of them. If that panel and the two protein assays beside it all return negative, this report has no within-scope recommendations, and the next conversation about standard care for metastatic cholangiocarcinoma belongs to the treating team rather than to Libby.

### Comprehensive genomic profiling

The essential first move is one paired DNA plus RNA panel with structural-variant and fusion calling, MSI, and TMB. It resolves seven of the eight candidate axes at once: FGFR2 fusion, IDH1 R132, BRAF V600E, KRAS G12C, NTRK1/2/3 and RET fusion, MSI and TMB. This panel gates pemigatinib, futibatinib, ivosidenib, dabrafenib plus trametinib, selpercatinib, larotrectinib, entrectinib, and pembrolizumab. The RNA arm earns its place because DNA-only calling misses a subset of FGFR2 and NTRK/RET fusions with intronic breakpoints, and the IDH1 R132 and KRAS codon-12 hotspots can fall outside a fusion-focused panel, so confirm the order covers both DNA hotspots and an RNA fusion read. Tissue turnaround is 2 to 3 weeks; ctDNA returns in 7 to 10 days as a faster parallel option when tissue is limited, at the cost of lower fusion sensitivity. Archival FFPE is the default and a fresh biopsy is not required if stored tissue is adequate.

### HER2 (ERBB2)

HER2 keys off a protein read, not the DNA panel. The essential assay is HER2 IHC on the PATHWAY 4B5 clone with reflex ISH. An NGS copy-number call does not establish protein expression, and the approved biliary HER2 agents are written against the IHC/ISH result: zanidatamab via NCT04466891 was defined by ISH amplification plus IHC 2+/3+, and trastuzumab deruxtecan is labeled for IHC 3+. The 4B5 antibody is the companion diagnostic, and this assay decides which anti-HER2 agent applies. Turnaround is 3 to 7 days.

### MSI-H / dMMR

Mismatch-repair IHC across MLH1, MSH2, MSH6, and PMS2 with reflex MSI by PCR is the high-priority orthogonal read that gates pembrolizumab. It is the fastest and cheapest way to confirm dMMR and catches low-purity cases an NGS MSI score can miss. Concordance with the NGS read is high but not perfect, so the two together harden the call before committing to checkpoint blockade. A clean negative redirects attention to the targeted axes. IHC turnaround is 3 to 5 days, with reflex MSI-PCR about a week.

### BRAF V600E

This is captured by the comprehensive panel, so it usually needs no separate order. The high-priority caveat is that a VE1 IHC screen alone is suggestive only: the dabrafenib plus trametinib label and the ROAR cohort were built on a molecularly confirmed V600E, so a positive IHC needs NGS or PCR confirmation, and a non-V600E class-2/3 BRAF alteration does not qualify for the same regimen.

### NTRK / RET, KRAS G12C, and downstream workup

The RNA arm of the comprehensive panel also resolves the rare NTRK and RET fusions that gate larotrectinib, entrectinib, and selpercatinib, and the DNA arm reports KRAS G12C. Lower-priority items round out the plan: serial ctDNA tracks acquired FGFR2 kinase-domain resistance once an FGFR inhibitor is running, and a germline referral follows only when MMR IHC shows MLH1 loss or the somatic panel flags a Lynch or BRCA finding, which carries family implications without changing immediate therapy.

### Where to order these assays

| Assay | Provider | Decision gated | Contact |
|---|---|---|---|
| **Comprehensive genomic profiling: paired DNA + RNA NGS with structural-variant/fusion calling, MSI, and TMB** | **Foundation Medicine *(preferred)* (FoundationOne CDx (tissue) / FoundationOne Liquid CDx)** | **Gates all targeted second-line therapy in metastatic CCA (FGFR, IDH1, HER2, BRAF, RET, NTRK inhibitors and pembrolizumab); shared first-step workup.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 888-988-3639** |
| Comprehensive genomic profiling: paired DNA + RNA NGS with structural-variant/fusion calling, MSI, and TMB | Tempus *(Tempus xT (DNA) + xR (RNA fusion))* | Gates all targeted second-line therapy in metastatic CCA (FGFR, IDH1, HER2, BRAF, RET, NTRK inhibitors and pembrolizumab); shared first-step workup. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 · 800-739-4137 |
| Comprehensive genomic profiling: paired DNA + RNA NGS with structural-variant/fusion calling, MSI, and TMB | Caris Life Sciences *(Caris MI Profile (whole-exome + whole-transcriptome))* | Gates all targeted second-line therapy in metastatic CCA (FGFR, IDH1, HER2, BRAF, RET, NTRK inhibitors and pembrolizumab); shared first-step workup. | [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 888-979-8669 |
| Comprehensive genomic profiling: paired DNA + RNA NGS with structural-variant/fusion calling, MSI, and TMB | Guardant Health *(Guardant360 CDx (ctDNA))* | Gates all targeted second-line therapy in metastatic CCA (FGFR, IDH1, HER2, BRAF, RET, NTRK inhibitors and pembrolizumab); shared first-step workup. | [test info](https://www.guardanthealth.com/products/guardant360-cdx/) · 3100 Hanover Street, Palo Alto, CA 94304 · 855-698-8887 |
| **HER2 IHC (PATHWAY anti-HER2/neu clone 4B5) with reflex HER2 ISH** | **NeoGenomics Laboratories *(preferred)* (HER2/neu (4B5) IHC with reflex ISH)** | **Zanidatamab (HERIZON-BTC-01) and trastuzumab deruxtecan (IHC 3+); selects which anti-HER2 agent applies.** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907** |
| HER2 IHC (PATHWAY anti-HER2/neu clone 4B5) with reflex HER2 ISH | Labcorp *(HER2 (HER-2/neu) IHC and FISH)* | Zanidatamab (HERIZON-BTC-01) and trastuzumab deruxtecan (IHC 3+); selects which anti-HER2 agent applies. | [test info](https://www.labcorp.com/tests/480020/her-2-neu-by-immunohistochemistry) · 358 South Main Street, Burlington, NC 27215 · 800-845-6167 |
| HER2 IHC (PATHWAY anti-HER2/neu clone 4B5) with reflex HER2 ISH | Quest Diagnostics *(HER2 IHC with reflex ISH)* | Zanidatamab (HERIZON-BTC-01) and trastuzumab deruxtecan (IHC 3+); selects which anti-HER2 agent applies. | [test info](https://testdirectory.questdiagnostics.com/) · 500 Plaza Drive, Secaucus, NJ 07094 · 866-697-8378 |
| **Mismatch-repair IHC (MLH1, MSH2, MSH6, PMS2) with reflex MSI by PCR** | **NeoGenomics Laboratories *(preferred)* (MMR IHC panel with reflex MSI)** | **Pembrolizumab under the MSI-H/dMMR tumor-agnostic label; orthogonal confirmation of any NGS MSI signal.** | **[test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907** |
| Mismatch-repair IHC (MLH1, MSH2, MSH6, PMS2) with reflex MSI by PCR | Labcorp *(MMR IHC / MSI by PCR)* | Pembrolizumab under the MSI-H/dMMR tumor-agnostic label; orthogonal confirmation of any NGS MSI signal. | [test info](https://www.labcorp.com/tests/481675/microsatellite-instability) · 358 South Main Street, Burlington, NC 27215 · 800-845-6167 |
| Mismatch-repair IHC (MLH1, MSH2, MSH6, PMS2) with reflex MSI by PCR | Mayo Clinic Laboratories *(Mismatch repair (MMR) IHC and MSI)* | Pembrolizumab under the MSI-H/dMMR tumor-agnostic label; orthogonal confirmation of any NGS MSI signal. | [test info](https://www.mayocliniclabs.com/test-catalog) · 3050 Superior Drive NW, Rochester, MN 55901 · 800-533-1710 |
| **BRAF V600E confirmation by NGS (or VE1 IHC screen confirmed by NGS/PCR)** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Dabrafenib + trametinib (BRAF V600E tumor-agnostic / ROAR); distinguishes V600E from non-actionable class-2/3 BRAF.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 888-988-3639** |
| BRAF V600E confirmation by NGS (or VE1 IHC screen confirmed by NGS/PCR) | NeoGenomics Laboratories *(BRAF V600E (VE1) IHC)* | Dabrafenib + trametinib (BRAF V600E tumor-agnostic / ROAR); distinguishes V600E from non-actionable class-2/3 BRAF. | [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 |
| **IDH1 R132 hotspot detection by tumor DNA NGS (included in comprehensive panel)** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Ivosidenib (ClarIDHy) for IDH1 R132-mutant CCA; confirms DNA hotspot coverage in the ordered panel.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 888-988-3639** |
| IDH1 R132 hotspot detection by tumor DNA NGS (included in comprehensive panel) | Tempus *(Tempus xT)* | Ivosidenib (ClarIDHy) for IDH1 R132-mutant CCA; confirms DNA hotspot coverage in the ordered panel. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 · 800-739-4137 |
| **RNA-based fusion NGS for NTRK1/2/3 and RET (pan-TRK IHC as an optional screen)** | **Caris Life Sciences *(preferred)* (Caris MI Profile (whole-transcriptome))** | **Larotrectinib/entrectinib (NTRK) and selpercatinib (RET) tumor-agnostic labels; confirms RNA fusion coverage.** | **[test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 888-979-8669** |
| RNA-based fusion NGS for NTRK1/2/3 and RET (pan-TRK IHC as an optional screen) | Tempus *(Tempus xR (RNA fusion))* | Larotrectinib/entrectinib (NTRK) and selpercatinib (RET) tumor-agnostic labels; confirms RNA fusion coverage. | [test info](https://www.tempus.com/oncology/genomic-profiling/) · 600 West Chicago Avenue, Suite 510, Chicago, IL 60654 · 800-739-4137 |
| RNA-based fusion NGS for NTRK1/2/3 and RET (pan-TRK IHC as an optional screen) | ArcherDX / Invitae *(Archer FusionPlex)* | Larotrectinib/entrectinib (NTRK) and selpercatinib (RET) tumor-agnostic labels; confirms RNA fusion coverage. | [test info](https://www.invitae.com) · 1400 16th Street, San Francisco, CA 94103 · 800-436-3037 |
| **KRAS G12C detection by tumor DNA NGS (included in comprehensive panel)** | **Foundation Medicine *(preferred)* (FoundationOne CDx)** | **Adagrasib/sotorasib-class KRAS G12C inhibitors and G12C trial enrollment.** | **[test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 888-988-3639** |
| KRAS G12C detection by tumor DNA NGS (included in comprehensive panel) | Guardant Health *(Guardant360 CDx (ctDNA))* | Adagrasib/sotorasib-class KRAS G12C inhibitors and G12C trial enrollment. | [test info](https://www.guardanthealth.com/products/guardant360-cdx/) · 3100 Hanover Street, Palo Alto, CA 94304 · 855-698-8887 |
| **Baseline and serial ctDNA for FGFR2 kinase-domain mutations and co-altered PIK3CA / CDKN2A/B** | **Guardant Health *(preferred)* (Guardant360)** | **Switch between FGFR inhibitors (e.g. to next-generation agents) on acquired-resistance signal; does not gate enrollment.** | **[test info](https://www.guardanthealth.com/products/guardant360/) · 3100 Hanover Street, Palo Alto, CA 94304 · 855-698-8887** |
| Baseline and serial ctDNA for FGFR2 kinase-domain mutations and co-altered PIK3CA / CDKN2A/B | Foundation Medicine *(FoundationOne Liquid CDx)* | Switch between FGFR inhibitors (e.g. to next-generation agents) on acquired-resistance signal; does not gate enrollment. | [test info](https://www.foundationmedicine.com/test/foundationone-liquid-cdx) · 150 Second Street, Cambridge, MA 02141 · 888-988-3639 |
| **Germline multigene panel (Lynch genes MLH1/MSH2/MSH6/PMS2/EPCAM; BRCA1/2; reflex from somatic findings)** | **Invitae *(preferred)* (Invitae Multi-Cancer / Lynch Syndrome Panel)** | **Hereditary-syndrome diagnosis and cascade family screening; does not change current systemic therapy.** | **[test info](https://www.invitae.com/en/providers/test-catalog) · 1400 16th Street, San Francisco, CA 94103 · 800-436-3037** |
| Germline multigene panel (Lynch genes MLH1/MSH2/MSH6/PMS2/EPCAM; BRCA1/2; reflex from somatic findings) | GeneDx *(GeneDx hereditary cancer panel)* | Hereditary-syndrome diagnosis and cascade family screening; does not change current systemic therapy. | [test info](https://www.genedx.com) · 207 Perry Parkway, Gaithersburg, MD 20877 · 888-729-1206 |

### Biomarker plan

| Recommended assay | Rationale | Suggested assay provider | Tissue requirements |
|---|---|---|---|
| Comprehensive genomic profiling: paired DNA + RNA NGS with structural-variant/fusion calling, MSI, and TMB (covering FGFR2, IDH1, ERBB2 copy number, BRAF V600E, KRAS G12C, NTRK1/2/3, RET) | No molecular profiling was supplied, so every actionable axis in this case is unmeasured; a single comprehensive DNA+RNA panel resolves seven of the eight candidate features at once and is the gate for all targeted second-line options. NCCN advises CGP at diagnosis of unresectable/metastatic biliary tract cancer, and an RNA-based fusion read matters because DNA-only calling misses a subset of FGFR2 fusions with novel or intronic breakpoints. Skipping it leaves the patient on chemotherapy alone while a roughly 40% chance of an actionable alteration goes undetected. | Foundation Medicine *(FoundationOne CDx (tissue) / FoundationOne Liquid CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 888-988-3639 | archival FFPE block or 10-20 unstained slides; or 2 x 10 mL Streck tubes whole blood for ctDNA |
| HER2 IHC (PATHWAY anti-HER2/neu clone 4B5) with reflex HER2 ISH | NGS copy-number alone does not establish HER2 protein expression, and the approved biliary-tract HER2 agents key off a protein/ISH readout, not an amplification call: trastuzumab deruxtecan is labeled for IHC 3+, and zanidatamab eligibility was defined by ISH amplification plus IHC 2+/3+ in HERIZON-BTC-01. The PATHWAY 4B5 antibody is the FDA companion diagnostic for zanidatamab in biliary tract cancer. Without IHC/ISH, an NGS HER2 signal cannot be converted into a drug choice or the correct agent. | NeoGenomics Laboratories *(HER2/neu (4B5) IHC with reflex ISH)* · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 | archival FFPE block or 4-5 unstained slides |
| Mismatch-repair IHC (MLH1, MSH2, MSH6, PMS2) with reflex MSI by PCR | MMR protein IHC is the fastest, cheapest orthogonal readout for dMMR and catches cases an NGS-derived MSI score can miss when tumor purity is low; concordance with MSI-PCR is high but discordances occur, so the two together harden the call before committing to checkpoint blockade. The VENTANA MMR RxDx panel is an FDA companion diagnostic in the dMMR tumor-agnostic setting. MSI-H/dMMR is uncommon in biliary tract cancer (roughly 1-3%), so a confirmed positive is decision-changing and a clean negative redirects attention to the targeted axes. | NeoGenomics Laboratories *(MMR IHC panel with reflex MSI)* · [test info](https://neogenomics.com/test-menu) · 9490 NeoGenomics Way, Fort Myers, FL 33912 · 866-776-5907 | archival FFPE block or 4 unstained slides |
| BRAF V600E confirmation by NGS (or VE1 IHC screen confirmed by NGS/PCR) | VE1 IHC is a sensitive screen but is not definitive on its own; the dabrafenib/trametinib tumor-agnostic label and the ROAR biliary cohort were built on molecularly confirmed BRAF V600E, so a positive IHC needs NGS or PCR confirmation before committing. The comprehensive panel already covers this codon, so this row mainly flags that a non-V600E BRAF class-2/3 alteration would not qualify for the same regimen. Treating on an unconfirmed IHC risks exposing the patient to a doublet they cannot benefit from. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 888-988-3639 | no additional tissue if CGP is run; 1-2 unstained slides if VE1 IHC is added |
| IDH1 R132 hotspot detection by tumor DNA NGS (included in comprehensive panel) | Ivosidenib eligibility (ClarIDHy) requires a confirmed IDH1 R132 mutation, and the codon is captured by any comprehensive DNA panel, so this is satisfied by the shared comprehensive panel rather than a standalone assay. The row exists to make the IDH1 gate explicit and to note that IDH2 and non-R132 IDH1 variants do not qualify for ivosidenib. If only a limited fusion-focused panel is run, the IDH1 hotspot can be missed, so confirm DNA coverage when ordering. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 888-988-3639 | no additional tissue if CGP is run |
| RNA-based fusion NGS for NTRK1/2/3 and RET (pan-TRK IHC as an optional screen) | NTRK and RET fusions are rare in biliary tract cancer (<1%) but tumor-agnostically actionable, and an RNA-based assay detects them more reliably than DNA-only calling, especially for partners with large intronic breakpoints. This is satisfied by the RNA arm of the shared paired panel; a standalone RNA fusion test or pan-TRK IHC screen is only needed if a DNA-only platform was used. A missed fusion forecloses a high-response oral targeted option. | Caris Life Sciences *(Caris MI Profile (whole-transcriptome))* · [test info](https://www.carislifesciences.com/products-and-services/molecular-profiling/) · 4610 South 44th Place, Phoenix, AZ 85040 · 888-979-8669 | no additional tissue if paired DNA/RNA CGP is run |
| KRAS G12C detection by tumor DNA NGS (included in comprehensive panel) | KRAS G12C is uncommon in biliary tract cancer but, when present, opens covalent G12C inhibitors and trial enrollment; the codon is covered by any comprehensive DNA panel, so the shared CGP resolves it. The row flags that broader KRAS hotspot results (e.g. G12D, G12V) also carry prognostic and emerging-trial relevance even though they do not gate a G12C inhibitor. No separate assay is needed if the ordered panel reports KRAS codon 12. | Foundation Medicine *(FoundationOne CDx)* · [test info](https://www.foundationmedicine.com/test/foundationone-cdx) · 150 Second Street, Cambridge, MA 02141 · 888-988-3639 | no additional tissue if CGP is run |
| Baseline and serial ctDNA for FGFR2 kinase-domain mutations and co-altered PIK3CA / CDKN2A/B | If FGFR2 fusion is confirmed and an FGFR inhibitor is started, acquired FGFR2 kinase-domain mutations (gatekeeper N549K, V564F and others) and co-alterations such as PIK3CA or CDKN2A/B drive resistance and can prompt a switch to a next-generation FGFR inhibitor. Serial ctDNA tracks these clones earlier than imaging or re-biopsy. This is sequencing intelligence rather than an enrollment gate, so it is not essential up front, but it should be in place before or shortly after starting therapy. | Guardant Health *(Guardant360)* · [test info](https://www.guardanthealth.com/products/guardant360/) · 3100 Hanover Street, Palo Alto, CA 94304 · 855-698-8887 | 2 x 10 mL Streck tubes whole blood |
| Germline multigene panel (Lynch genes MLH1/MSH2/MSH6/PMS2/EPCAM; BRCA1/2; reflex from somatic findings) | If MMR IHC shows MLH1 loss or the somatic panel returns a pathogenic Lynch-gene or BRCA1/2 variant, germline testing distinguishes a heritable syndrome from a sporadic somatic event and triggers cascade family screening. MLH1 loss usually warrants a BRAF V600E or MLH1-promoter methylation check first to gauge whether germline testing is indicated. This does not change the patient's immediate therapy, so it is research-adjacent for the targeting question, but it carries real family implications when a driver is germline. | Invitae *(Invitae Multi-Cancer / Lynch Syndrome Panel)* · [test info](https://www.invitae.com/en/providers/test-catalog) · 1400 16th Street, San Francisco, CA 94103 · 800-436-3037 | 5-10 mL whole blood or a saliva kit |

---

*Decision support, not medical advice. Confirm assay availability and current standards with the treating team and the local pathology service.*

<!-- libby:target-validation:end -->

## Scope summary

30 trials surfaced across the eight candidate axes, including 16 new on-axis studies added by the July 2026 screen. 26 clinical-evidence rows cover the panel's approved and basket agents, backed by 12 preclinical rows. Nine ranked rows follow: a rank-1 shared comprehensive-genomic-profiling gate, then eight biomarker-conditional therapeutic recommendations (ranks 2-9), two of them held at considered_with_caveats (lirafugratinib and trastuzumab deruxtecan) so the reader sees what the board weighed and where it pulled back. Agreement scores run from 1.0 at the CGP gate and ivosidenib down to -0.6 on T-DXd. All five personas converged on the workup and on ivosidenib for the IDH1 lane. Three points of friction remain visible: a within-lane order dissent on futibatinib, a three-persona dissent on lirafugratinib over abstract-only maturity and guideline order, and a three-persona dissent that holds T-DXd below zanidatamab on its ILD signal. No persona issued a formal veto. The ranking is scoped to drugs that act on the candidate panel; chemotherapy backbones and other standard biliary care that do not target a panel feature are out of scope and are not named here.

## Cross-cutting caveat (read first)

**Nothing here is actionable until the tumor is genotyped.** No molecular profiling was supplied, so every therapeutic axis is unmeasured, and the rank-1 action is comprehensive genomic profiling itself. Each therapeutic recommendation below is conditional on its own feature reading positive; a single paired DNA+RNA panel (plus HER2 IHC/ISH and MMR IHC) resolves seven of the eight candidate axes in one pass, with roughly a 40% prior probability of surfacing some targetable alteration.

- **The ranking is targetable-feature-scoped.** Only the workup gate and the recommendations that act on a candidate panel feature appear. Standard care that does not target a panel feature, including the gemcitabine/cisplatin/durvalumab-class first-line backbone and later chemotherapy, lies outside Libby's targetable-feature ranking and is not named here.
- **If the panel returns no actionable alteration, this case has no within-scope recommendations; standard-of-care for metastatic cholangiocarcinoma lies outside Libby's targetable-feature ranking and should be pursued through the treating team's normal care channel.** Each feature forecloses independently: a negative IDH1 read does not foreclose the FGFR2 or HER2 lanes, and so on across the panel.
- **The protein-level gates are not interchangeable with the DNA panel.** HER2 keys off IHC with reflex ISH on the 4B5 companion antibody, not an NGS copy-number call; BRAF requires a true V600E confirmed by NGS or PCR, since a VE1 IHC screen alone and class-2/3 BRAF alterations do not qualify; MSI-H/dMMR is fastest confirmed by MMR IHC with reflex MSI-PCR. An RNA-based fusion read matters because DNA-only calling misses a subset of FGFR2 fusions with intronic breakpoints.
- **Workup logistics:** tissue turnaround is roughly 2-3 weeks, ctDNA 7-10 days as a faster parallel option when tissue is limited. The default is archival FFPE (a block or 10-20 unstained slides); a fresh biopsy is not required if stored tissue is adequate. Foundation Medicine's FoundationOne CDx is the companion diagnostic for the pemigatinib FGFR2 call, with Tempus, Caris, and Guardant as alternates.

## Intervention grouping

- **FGFR2-directed (FGFR inhibitors):** futibatinib ([PMID 36652354](https://pubmed.ncbi.nlm.nih.gov/36652354), [NCT02052778](https://clinicaltrials.gov/study/NCT02052778)) and pemigatinib ([PMID 32203698](https://pubmed.ncbi.nlm.nih.gov/32203698), [NCT02924376](https://clinicaltrials.gov/study/NCT02924376)) approved; FGFR2-selective lirafugratinib via the ReFocus cohort ([doi:10.1200/JCO.2026.44.2_suppl.476](https://doi.org/10.1200/JCO.2026.44.2_suppl.476), [NCT04526106](https://clinicaltrials.gov/study/NCT04526106)); resistance-directed TYRA-200 ([NCT06160752](https://clinicaltrials.gov/study/NCT06160752)).
- **IDH1-directed:** ivosidenib ([PMID 32416072](https://pubmed.ncbi.nlm.nih.gov/32416072), [NCT02989857](https://clinicaltrials.gov/study/NCT02989857)), with a preclinical IFNγ-TET2 immunoevasion mechanism ([PMID 34848557](https://pubmed.ncbi.nlm.nih.gov/34848557)).
- **HER2-directed:** zanidatamab ([PMID 37276871](https://pubmed.ncbi.nlm.nih.gov/37276871), [NCT04466891](https://clinicaltrials.gov/study/NCT04466891)), trastuzumab deruxtecan ([PMID 37870536](https://pubmed.ncbi.nlm.nih.gov/37870536), [NCT04482309](https://clinicaltrials.gov/study/NCT04482309)); first-line successors [NCT06282575](https://clinicaltrials.gov/study/NCT06282575) and [NCT06467357](https://clinicaltrials.gov/study/NCT06467357).
- **BRAF V600E-directed:** dabrafenib + trametinib ([PMID 32818466](https://pubmed.ncbi.nlm.nih.gov/32818466), [NCT02034110](https://clinicaltrials.gov/study/NCT02034110)).
- **Tumor-agnostic immunotherapy (MSI-H/dMMR, TMB-high):** pembrolizumab ([PMID 31682550](https://pubmed.ncbi.nlm.nih.gov/31682550), [PMID 32919526](https://pubmed.ncbi.nlm.nih.gov/32919526), [NCT02628067](https://clinicaltrials.gov/study/NCT02628067)).
- **Tumor-agnostic fusion inhibitors:** larotrectinib ([PMID 32105622](https://pubmed.ncbi.nlm.nih.gov/32105622), [NCT02576431](https://clinicaltrials.gov/study/NCT02576431)) and entrectinib ([PMID 31838007](https://pubmed.ncbi.nlm.nih.gov/31838007)) for NTRK; selpercatinib ([PMID 36029780](https://pubmed.ncbi.nlm.nih.gov/36029780)) for RET.
- **KRAS G12C-directed:** adagrasib-class covalent inhibitors via basket enrollment ([PMID 37099736](https://pubmed.ncbi.nlm.nih.gov/37099736), [NCT05722327](https://clinicaltrials.gov/study/NCT05722327)).

## Top interventions

### Rank 1. Comprehensive genomic profiling — paired DNA + RNA NGS plus HER2 IHC/ISH and MMR IHC

*The gate. Resolves which, if any, of the candidate panel axes is open. Non-toxic; can run on archival tissue or, faster, on ctDNA.*

#### Evidence base

This case has no molecular data, so the confirmatory test is the first move rather than a refinement of an existing call. A single paired DNA+RNA panel resolves FGFR2 fusion, IDH1 R132, BRAF V600E, KRAS G12C, NTRK/RET fusion, MSI and TMB at once. NCCN advises CGP at diagnosis of unresectable or metastatic biliary tract cancer ([NCT04466891](https://clinicaltrials.gov/study/NCT04466891) and the FIGHT-202 companion-diagnostic pedigree, [PMID 32203698](https://pubmed.ncbi.nlm.nih.gov/32203698)). The RNA arm earns its place because DNA-only calling misses FGFR2 fusions with novel or intronic breakpoints. Two readouts sit outside the DNA panel and have to be ordered alongside it: HER2 by IHC with reflex ISH (an amplification call does not establish protein expression, and the approved HER2 agents key off the protein/ISH read), and MMR by IHC with reflex MSI-PCR (the fastest orthogonal dMMR read, which catches low-purity cases an NGS MSI score can miss).

#### Likelihood of desired effect

Roughly 40% of metastatic CCA carries an alteration somewhere on this panel. The test does not treat anything; it decides whether any of ranks 2-8 are reachable and which one. Skipping it leaves the patient on chemotherapy alone while a meaningful chance of an actionable target goes undetected.

#### Toxicity profile

- None. Archival FFPE (a block or 10-20 unstained slides), or 2 x 10 mL Streck tubes for the ctDNA parallel option.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. The workup is non-toxic and gates everything, so no persona dissented or vetoed.

#### Practical considerations

Tissue turnaround is 2-3 weeks; ctDNA returns in 7-10 days when tissue is limited or a biopsy is undesirable, at the cost of lower fusion sensitivity. Confirm the ordered panel reports DNA hotspots (IDH1 R132, KRAS codon 12, BRAF V600E) and includes an RNA fusion arm; a fusion-focused panel alone can miss the IDH1 hotspot, and a DNA-only panel can miss FGFR2 and NTRK/RET fusions. FoundationOne CDx is the default for the FGFR2 companion-diagnostic decision; Tempus xT+xR and Caris whole-transcriptome strengthen rare-fusion detection; Guardant360 CDx is the liquid fallback.

#### Why this rank

It precedes everything. The board treated it as a gate, not a therapy, which is why no persona listed it as a pick even though all five named it the rank-1 action.

#### Per-trial detail

| Test / trial | Efficacy context | Toxicity | Reference |
|---|---|---|---|
| Comprehensive genomic profiling (paired DNA+RNA + HER2 IHC/ISH + MMR IHC) | Gates all targeted second-line therapy; ~40% chance of a targetable hit | None — diagnostic test on tissue or blood | [NCT04466891](https://clinicaltrials.gov/study/NCT04466891), [PMID 32203698](https://pubmed.ncbi.nlm.nih.gov/32203698) |

---

### Rank 2. Ivosidenib (if IDH1 R132 confirmed on tumor NGS)

*Conditional on `idh1_r132:positive`. Foreclosed if the hotspot is wild-type.*

*The only randomized phase-3 evidence in the set, but the single-agent win is disease control, not shrinkage.*

#### Evidence base

ClarIDHy ([PMID 32416072](https://pubmed.ncbi.nlm.nih.gov/32416072), [NCT02989857](https://clinicaltrials.gov/study/NCT02989857)) is the lone randomized, double-blind, placebo-controlled phase 3 here. It met its registered PFS endpoint, HR 0.37 (95% CI 0.25-0.54, p<0.0001), median PFS 2.7 versus 1.4 months. ORR was 2%. The critic was precise about the survival claim: the registered ITT OS missed at HR 0.69 (p=0.060), and the widely quoted 0.46 is an RPSFT crossover adjustment after 70% of placebo patients crossed over, so it is a sensitivity analysis rather than a clean result. IDH1 R132 runs 15-20% in intrahepatic CCA, which makes it one of the likelier positives the panel returns. Preclinical work adds a mechanistic reason to test the combination question: mutant IDH1 blocks IFNγ-TET2 signaling to drive immunoevasion, which is the rationale behind an ivosidenib-plus-checkpoint trial ([PMID 34848557](https://pubmed.ncbi.nlm.nih.gov/34848557)).

#### Likelihood of desired effect

Assuming a positive hotspot, the probability of disease control is real and the evidence grade is the best in the dossier, but the absolute payoff is modest. The honest pitch is delayed progression, not tumor regression. A wild-type IDH1 read forecloses this rec entirely.

#### Toxicity profile

- QT prolongation (class effect, grade 3 ~1%); needs baseline and on-treatment ECGs
- Ascites grade 3+ ~7%, matching the placebo arm
- Fatigue grade 3 ~3%
- No treatment-related deaths; the grade 3+ profile tracked placebo

No toxicity vetoes are on file. The QT signal is the one item that needs monitoring, and no organ-function labs were supplied to confirm that is feasible.

#### Counter-productive mechanisms / dissent

The drug itself drew unanimous endorsement; the disagreement was over where it sits. The risktaker dissented on rank, arguing that an ORR-2% option should not lead over the higher-response fusion agents once a test reads positive, and the advocate flagged that a balanced 0.5 weight does not license a safety-first tiebreaker. Neither objection contests using ivosidenib in IDH1-mutant disease. The critic and conservative reinforced the same OS-claim caveat from opposite directions.

#### Practical considerations

Once-daily oral pill. The open registration trial (NCT02989857) is the trial route the prefers_trials preference asks for. NCCN BTC v2.2025 lists it category 2A for subsequent-line IDH1-mutant disease; ESMO 2023 recommends it. IDH2 and non-R132 IDH1 variants do not qualify, so confirm the panel covers the R132 codon.

#### Why this rank

It leads the therapeutic ranks on agreement (1.0, all five endorse) and evidence grade. The risktaker would reorder on depth-of-response if a fusion also reads positive, but on a balanced preference weight and with the only RCT in the set, ivosidenib holds rank 2.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Ivosidenib — ClarIDHy, IDH1 R132-mutant CCA, n=185 | mPFS 2.7 vs 1.4 mo, HR 0.37 (95% CI 0.25-0.54); ORR 2%; ITT OS HR 0.69 (p=0.060) | QT prolongation ~1% G3; ascites ~7% G3+; no TRAE deaths | [PMID 32416072](https://pubmed.ncbi.nlm.nih.gov/32416072), [NCT02989857](https://clinicaltrials.gov/study/NCT02989857) |

---

### Rank 3. Futibatinib (if FGFR2 fusion/rearrangement confirmed on RNA-based CGP)

*Conditional on `fgfr2_fusion:positive`. Foreclosed if no fusion is detected.*

*The highest-yield molecular axis in this disease, with cross-trial-concordant response data. The grade-3 hyperphosphatemia is the tradeoff against the gentler pemigatinib.*

#### Evidence base

FOENIX-CCA2 ([PMID 36652354](https://pubmed.ncbi.nlm.nih.gov/36652354), [NCT02052778](https://clinicaltrials.gov/study/NCT02052778)) reported ORR 42% (95% CI 32-52), median OS 21.7 months, and only 2% discontinuing for toxicity in centrally confirmed FGFR2 fusions. The critic trusts this row most among the single-arm options because FOENIX and FIGHT-202 are two independent trials converging on the same effect direction, the nearest thing to replication in the dossier. Futibatinib binds irreversibly and holds activity against some pemigatinib-resistant kinase-domain mutations, which matters for sequencing. The limit is real: single-arm phase 2, surrogate ORR endpoint, no comparator.

#### Likelihood of desired effect

High in the FGFR2-fusion subset, which is also the most likely positive among the molecular axes at 10-15% of intrahepatic CCA. A negative or DNA-only-missed fusion forecloses this rec, which is why an RNA-based read is the gate.

#### Toxicity profile

- Hyperphosphatemia, on-target FGFR class effect, grade 3 ~30%; needs active phosphate management
- Increased AST grade 3+ ~7%
- Stomatitis and fatigue grade 3+ ~6% each
- Treatment-related discontinuation ~2%

No toxicity vetoes are on file. The 30% grade-3 hyperphosphatemia is the offsetting load against the balanced weight and the basis of the conservative's within-lane dissent.

#### Counter-productive mechanisms / dissent

The conservative dissented within the FGFR2 lane, reversing the order against pemigatinib on toxicity: grade 3 hyperphosphatemia reached 30% on futibatinib against essentially none on pemigatinib, and at comparable ORR the conservative takes the lower-grade burden plus the longer post-approval record. The concensusite seated futibatinib first on the higher ESMO-MCBS v1.1 score (3 vs 2) and the documented post-pemigatinib resistance activity; the critic agreed the FGFR2 lane belongs near the top but noted the MCBS score is built from two separate single-arm trials and cannot truly adjudicate a within-lane order. The hyperphosphatemia is on-target and managed, so it is a patient-AE burden, not a mechanism that blunts the antitumor goal.

#### Practical considerations

Continuous oral dosing, 20 mg daily. The advocate would surface the FGFR2 trial menu alongside, including the resistance-directed TYRA-200 study (NCT06160752) for a patient who later progresses on a first FGFR inhibitor. NCCN BTC v2.2025 category 2A. Eligibility was built on intrahepatic CCA, so a non-intrahepatic subsite weakens the match.

#### Why this rank

Futibatinib scores 0.6 against pemigatinib's 0.8, so this is a deliberate tie-break inversion: the efficacy-weighted preference fit seats it above the higher-agreement agent. The board's center of gravity (critic, concensusite, advocate) put futibatinib first in the FGFR2 lane on cross-trial concordance, resistance coverage, and the slightly higher response rate; the conservative's dissent on the 30% grade-3 hyperphosphatemia is the one voice for the reverse order. On a balanced preference weight the higher ORR and post-pemigatinib resistance activity carry it ahead, with pemigatinib the better-tolerated within-lane fallback directly below.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Futibatinib — FOENIX-CCA2, FGFR2-fusion intrahepatic CCA, n=103 | ORR 42% (95% CI 32-52); mOS 21.7 mo; 2% discontinued for TRAE | Hyperphosphatemia G3 ~30%; AST increase ~7% G3+; stomatitis/fatigue ~6% | [PMID 36652354](https://pubmed.ncbi.nlm.nih.gov/36652354), [NCT02052778](https://clinicaltrials.gov/study/NCT02052778) |

---

### Rank 4. Pemigatinib (if FGFR2 fusion/rearrangement confirmed)

*Conditional on `fgfr2_fusion:positive`. Foreclosed if no fusion is detected.*

*Same FGFR2 gate as futibatinib, gentler grade-3 profile, longer track record. The within-lane choice once the fusion confirms.*

#### Evidence base

FIGHT-202 ([PMID 32203698](https://pubmed.ncbi.nlm.nih.gov/32203698), [NCT02924376](https://clinicaltrials.gov/study/NCT02924376)) reported ORR 35.5% (95% CI 26.5-45.4). It was the first FGFR inhibitor approved in CCA. The reported OS of 21.1 months is immature at 40 events, so it should not carry weight. This is the second independent single-arm read on the FGFR2 axis, and its concordance with FOENIX is what keeps the whole lane near the top rather than the individual numbers.

#### Likelihood of desired effect

High in the FGFR2-fusion subset, concordant with futibatinib. Same prevalence and same foreclosure on a negative read.

#### Toxicity profile

- Hyperphosphatemia 55% any-grade, on-target, with no grade 3-4 events
- Hypophosphatemia grade 3+ ~12% (the reflex of phosphate dysregulation)
- Serous retinal detachment ~4%; needs scheduled ophthalmologic checks
- Nail and skin toxicity, alopecia (~42-46% any-grade), dysgeusia ~38%

The grade-3 burden is lighter than futibatinib's, which is the conservative's whole argument for the reverse order.

#### Counter-productive mechanisms / dissent

Four personas endorsed it and none dissented. The only contested question is its position relative to futibatinib, covered above. The on-target phosphate effect is managed and does not work against the antitumor goal.

#### Practical considerations

Oral, 13.5 mg daily on a 2-weeks-on / 1-week-off cycle. NCCN BTC v2.2025 category 2A, ESMO recommended. Serous retinal detachment is the monitoring item the guideline presumes is feasible, unconfirmed here against absent baseline data.

#### Why this rank

Pemigatinib carries the higher agreement score (0.8 against futibatinib's 0.6), yet sits one rank below it: the ranking rule tie-breaks on efficacy-weighted preference fit, and the board majority read futibatinib's resistance coverage and marginally higher response as the deciding edge in the FGFR2 lane. Pemigatinib holds rank 4 rather than lower because two independent trials converging on the same axis, plus the cleaner grade-3 profile, make it the better-tolerated within-lane option whenever toxicity is the deciding factor — the conservative's default.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Pemigatinib — FIGHT-202 cohort A, FGFR2-fusion CCA, n=107 | ORR 35.5% (95% CI 26.5-45.4); OS 21.1 mo (immature, 40 events) | Hyperphosphatemia 55% any-grade (no G3-4); hypophosphatemia ~12% G3+; serous retinal detachment ~4% | [PMID 32203698](https://pubmed.ncbi.nlm.nih.gov/32203698), [NCT02924376](https://clinicaltrials.gov/study/NCT02924376) |

---

### Rank 5. Lirafugratinib (RLY-4008), FGFR2-selective, via the ReFocus cohort (if FGFR2 fusion/rearrangement confirmed)

*Conditional on `fgfr2_fusion:positive`. Foreclosed if no fusion is detected. Status: considered with caveats.*

*The highest-ORR FGFR2 option and the best hyperphosphatemia profile in the lane, but the data are abstract-only, the drug is pre-approval, and three personas dissented.*

#### Evidence base

The ReFocus FGFRi-naive cholangiocarcinoma cohort ([doi:10.1200/JCO.2026.44.2_suppl.476](https://doi.org/10.1200/JCO.2026.44.2_suppl.476), [NCT04526106](https://clinicaltrials.gov/study/NCT04526106)) reported ORR 46.5% (95% CI 37.1-56.1) in n=114, with a 96.5% disease-control rate, median DoR 11.8 months, and median PFS 11.3 months. The FGFR2-selective design largely spares the FGFR1-driven hyperphosphatemia that runs 30-55% on the pan-FGFR agents. The honest limit is maturity: this is an ASCO GI 2026 abstract with no PubMed record and no peer-reviewed full text, so response ascertainment and censoring cannot be audited, and the drug is not yet approved. One provenance point the board flagged and I carry forward: lirafugratinib's own basket study NCT07359820 **excludes** cholangiocarcinoma. The 46.5% comes from the separate ReFocus cohort (NCT04526106), and the two must not be conflated as one enrollment route.

#### Likelihood of desired effect

High-response but low-certainty. In the FGFR2-fusion subset the ORR beats or matches the approved agents, but a single-arm, abstract-only readout on an unapproved drug carries more uncertainty than the peer-reviewed pivotals directly above it. A negative or DNA-only-missed fusion forecloses this rec, same as the rest of the lane.

#### Toxicity profile

- Palmar-plantar erythrodysesthesia grade 3+ 32.8% — dose-limiting, function-limiting, felt daily
- Stomatitis grade 3+ 12.1%
- Largely spares FGFR1-driven hyperphosphatemia, the tolerability argument for the selective design

No toxicity vetoes are on file. The conservative's point is that trading pan-FGFR hyperphosphatemia for a one-in-three grade-3 hand-foot rate is a lateral move, not a clean tolerability win.

#### Counter-productive mechanisms / dissent

This is the case's preference-conflict rec, and the split is real. The advocate and risktaker rank it at the head of the FGFR lane on the 46.5% ORR and the cleaner hyperphosphatemia profile, arguing that with `prefers_trials` set to true, an enrollable next-gen agent belongs in front of the patient rather than fenced off. Three personas dissented, which sets the status to considered_with_caveats: the critic discounts abstract-only data below the peer-reviewed FGFR pivotals; the conservative names the 32.8% grade-3 hand-foot rate the tolerability argument skips; the concensusite holds that seating a pre-approval, non-NCCN-listed agent above approved futibatinib and pemigatinib inverts the guideline order. No persona vetoed it — the objections are about evidence maturity and rank order, not a mechanism that would blunt the antitumor goal.

#### Practical considerations

Oral. Access runs through the ReFocus slot or expanded access pending the 27 September 2026 PDUFA; there is no on-label prescription yet, so enrollment logistics should be lined up alongside the genomic panel. Not FDA-approved and not NCCN-listed, so its place is the trial-enrollment lane rather than a standard rec.

#### Why this rank

Agreement drops to -0.2 here (two endorse, three dissent), the only negative-adjacent score above the T-DXd row. It sits below the two approved FGFR agents because the guideline-consonant use of pre-approval data is enrollment, not displacement of on-label therapy, and above the rarer-feature lanes because, if FGFR2 confirms, this is a live and higher-response door for a trials-seeking patient. The advocate and risktaker would seat it at rank 3; the board majority would not put an unaudited abstract above the NEJM and Lancet Oncology pivotals.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Lirafugratinib (RLY-4008) — ReFocus FGFRi-naive CCA cohort, n=114 | ORR 46.5% (95% CI 37.1-56.1); DCR 96.5%; mDoR 11.8 mo; mPFS 11.3 mo | PPE G3+ 32.8%; stomatitis G3+ 12.1%; spares FGFR1 hyperphosphatemia | [doi:10.1200/JCO.2026.44.2_suppl.476](https://doi.org/10.1200/JCO.2026.44.2_suppl.476), [NCT04526106](https://clinicaltrials.gov/study/NCT04526106) |

---

### Rank 6. Zanidatamab (if HER2 IHC 3+ with reflex ISH confirmed)

*Conditional on `erbb2_amp:positive`. Foreclosed if HER2 IHC/ISH is negative.*

*The guideline-endorsed HER2 lead on dedicated biliary-trial data. The gate is the protein read, not the DNA panel.*

#### Evidence base

HERIZON-BTC-01 ([PMID 37276871](https://pubmed.ncbi.nlm.nih.gov/37276871), [NCT04466891](https://clinicaltrials.gov/study/NCT04466891)) returned a confirmed ORR 41.3% (95% CI 30.4-52.8) with median DoR 12.9 months in HER2-amplified, IHC 2+/3+ biliary tract cancer. Unlike the basket cohorts, this is a dedicated biliary trial, which is why it outranks the other HER2 options. The biparatopic antibody induces a distinctive HER2 clustering and internalization not seen with trastuzumab plus pertuzumab ([PMID 36914633](https://pubmed.ncbi.nlm.nih.gov/36914633)), so the mechanistic case runs ahead of a me-too antibody. The evidence is single-arm phase 2b behind an accelerated approval.

#### Likelihood of desired effect

High in the HER2-positive subset, conditional on the protein read confirming. HER2 skews toward extrahepatic and gallbladder disease, so the prior probability rides on a subsite intake never specified.

#### Toxicity profile

- Decreased ejection fraction (HER2-directed cardiac class effect; grade 3 ~3%); needs baseline and serial echo
- Diarrhea grade 3 ~5%
- Infusion-related reactions ~35% any-grade

The cardiac signal has an established monitoring algorithm, but no baseline cardiac function was supplied.

#### Counter-productive mechanisms / dissent

Endorsed by four personas with no dissent. Every persona who addressed the HER2 axis preferred it over T-DXd on a direct safety argument: a 3% grade-3 ejection-fraction signal with a standard echo algorithm against T-DXd's 10.5% adjudicated ILD with three treatment-related deaths. HER2 blockade is direct and on-target, with no counter-productive vector at this depth.

#### Practical considerations

IV every two weeks. No modality veto is on file, so the IV route is not penalized. The gate is HER2 IHC with reflex ISH on the 4B5 companion antibody, not an NGS copy-number call substituting for the protein read. NCCN BTC v2.2025 category 2A. If the patient turns out HER2-positive and treatment-naive, the first-line successor trials (NCT06282575 zanidatamab + chemo, NCT06467357 T-DXd + rilvegostomig) become relevant.

#### Why this rank

Agreement 0.8, the highest among the rarer-feature lanes, and seated above both the BRAF doublet and its own within-axis competitor T-DXd. It leads the HER2 lane because it rests on a dedicated biliary trial rather than a basket subgroup, and because four personas held T-DXd below it on the ILD signal — the safer HER2 antibody wins the lane when a comparably active option carries three treatment-related deaths and no pulmonary baseline on file.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Zanidatamab — HERIZON-BTC-01 cohort 1, HER2-amplified IHC 2+/3+ BTC, n=80 | Confirmed ORR 41.3% (95% CI 30.4-52.8); mDoR 12.9 mo | Decreased EF G3 ~3%; diarrhea G3 ~5%; IRR ~35% any-grade | [PMID 37276871](https://pubmed.ncbi.nlm.nih.gov/37276871), [NCT04466891](https://clinicaltrials.gov/study/NCT04466891) |

---

### Rank 7. Dabrafenib + trametinib (if BRAF V600E confirmed on NGS/PCR)

*Conditional on `braf_v600e:positive`. Foreclosed if no true V600E is confirmed.*

*Strong response on a rare alteration, with dual guideline-plus-agnostic-label backing. The serious-AE load is what keeps it below the gentler oral options at equal agreement.*

#### Evidence base

The ROAR biliary cohort ([PMID 32818466](https://pubmed.ncbi.nlm.nih.gov/32818466), [NCT02034110](https://clinicaltrials.gov/study/NCT02034110)) hit ORR 47% (95% CI 31-62) with median PFS 9.0 months, a strong number for an alteration that sits at 1-5% of biliary tract cancer. The cohort is small (n=43) and single-arm. A confirmed V600E gives two routes to treat, the CCA precedent and the tumor-agnostic label, so access is not the bottleneck.

#### Likelihood of desired effect

High in the BRAF V600E subset, on a small single-arm basket cohort at low prevalence. The gate is strict: a true V600E confirmed by NGS or PCR. A VE1 IHC screen alone is suggestive only, and class-2/3 BRAF alterations do not qualify.

#### Toxicity profile

- Pyrexia ~19% any-grade, the characteristic combination effect; drove most treatment-related serious AEs
- Treatment-related serious AEs ~21%; any serious AE ~40%
- Increased GGT grade 3+ ~12%
- No treatment-related deaths

No fever or hospitalization veto is on file, but the serious-AE load is heavier than the higher-ranked oral agents carry.

#### Counter-productive mechanisms / dissent

No persona vetoed or dissented against the drug. The risktaker and concensusite carried it in their ranked picks; the rest kept it off their top five on prevalence and crowding, not on any safety objection. MEK co-inhibition mitigates the paradoxical RAF activation that single-agent BRAF inhibition can cause, so the pyrexia and serious-AE burden is a patient-AE load, not a mechanism that works against the therapeutic goal.

#### Practical considerations

Oral, dabrafenib 150 mg BID plus trametinib 2 mg daily. NCCN BTC v2.2025 category 2A plus the tumor-agnostic FDA label. Pyrexia has a standard dose-interruption and antipyretic playbook the guideline assumes is in place.

#### Why this rank

Agreement 0.4 (two personas ranked it, none dissented). It sits below the HER2 lane because V600E turns up in only 1-5% of biliary cancer against HER2's 5-15% in extrahepatic disease, and the ROAR evidence is a small single-arm basket cohort of 43. A confirmed V600E makes it immediately actionable at a 47% response, so the rank reflects prevalence and cohort size, not any doubt about the drug.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Dabrafenib + trametinib — ROAR biliary cohort, BRAF V600E, n=43 | ORR 47% (95% CI 31-62); mPFS 9.0 mo | Pyrexia ~19%; TR serious AE ~21%; GGT increase ~12% G3+; no TRAE deaths | [PMID 32818466](https://pubmed.ncbi.nlm.nih.gov/32818466), [NCT02034110](https://clinicaltrials.gov/study/NCT02034110) |

---

### Rank 8. Trastuzumab deruxtecan (T-DXd) (if HER2 IHC 3+/expressing confirmed)

*Conditional on `erbb2_amp:positive`. Foreclosed if HER2 IHC/ISH is negative. Status: considered with caveats.*

*Competitive IHC 3+ activity, but held below zanidatamab on a 10.5% ILD signal with three treatment-related deaths and no pulmonary baseline on file.*

#### Evidence base

The DESTINY-PanTumor02 biliary cohort ([PMID 37870536](https://pubmed.ncbi.nlm.nih.gov/37870536), [NCT04482309](https://clinicaltrials.gov/study/NCT04482309)) reported an investigator-assessed ORR of 22% (95% CI 10.6-37.6) across the full biliary cohort, rising to 56.3-61.3% in the IHC 3+ subgroup. That subgroup figure is competitive with zanidatamab, but it is a post-hoc subgroup, not the registered biliary-cohort endpoint. The tumor-agnostic approval covers IHC 3+ only.

#### Likelihood of desired effect

High in the IHC 3+ subgroup and low-certainty across the whole biliary cohort, where the registered ORR is 22%. Frame the HER2-low predictive hedge plainly: a low-positive HER2 read is a weaker predictor of benefit than IHC 3+, and the label does not extend to HER2-low in this setting, so a HER2-low-driven use would be investigational rather than approved. A negative HER2 read forecloses this rec.

#### Toxicity profile

- **Adjudicated drug-related ILD/pneumonitis 10.5%, with three treatment-related deaths** — the load-bearing safety signal
- Grade 3+ drug-related AE 40.8% study-wide
- Nausea, a common GI class effect of the deruxtecan payload

No pulmonary baseline, DLCO, or organ-function labs were supplied to gate the ILD risk, which is precisely why the board held this rec below zanidatamab.

#### Counter-productive mechanisms / dissent

Three personas dissented, so the status is considered_with_caveats, and the rec is kept on the list as considered-and-held-below rather than dropped, so the reader sees the HER2 option the board deliberately downgraded. The conservative, critic, and advocate all held T-DXd below zanidatamab on the 10.5% adjudicated ILD rate and three treatment-related ILD deaths, with no pulmonary baseline to gate against. Because no persona ranked it above zanidatamab, the board recorded this as a shared downgrade rather than a formal veto. The ILD is a genuine mechanism-level risk: on-mechanism pulmonary injury from the payload can be fatal, which is what moves the counter-productive severity to Moderate. If re-entered, it should be gated on a confirmed IHC 3+ tumor plus a baseline pulmonary assessment and a written ILD-monitoring plan; on that basis the conservative would not block it.

#### Practical considerations

IV every three weeks. Tumor-agnostic HER2 (IHC 3+) accelerated approval via the basket route rather than a dedicated biliary listing. The first-line successor trial NCT06467357 pairs T-DXd with rilvegostomig for HER2-expressing disease, relevant only if the patient is HER2-positive and treatment-naive.

#### Why this rank

Agreement -0.6, the lowest in the set, from three dissents and no endorsements. It sits below zanidatamab in its own HER2 lane and below every approved single-agent option on the safety downgrade. It stays visible at rank 8 rather than being cut so the reader can see what the board weighed and why it pulled back — the requirement that considered-and-rejected options remain on the table.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Trastuzumab deruxtecan — DESTINY-PanTumor02 biliary cohort | ORR 22% (95% CI 10.6-37.6); IHC 3+ subgroup 56.3-61.3% | ILD/pneumonitis 10.5% with 3 TRAE deaths; grade 3+ AE 40.8% | [PMID 37870536](https://pubmed.ncbi.nlm.nih.gov/37870536), [NCT04482309](https://clinicaltrials.gov/study/NCT04482309) |

---

### Rank 9. Pembrolizumab (if MSI-H/dMMR or TMB-high confirmed)

*Conditional on `msi_tmb:positive`. Foreclosed if MSI/MMR and TMB are not high.*

*A durable immunotherapy tail if the biomarker confirms, but the biliary magnitude is inferred from a cross-tumor basket with no CCA-specific subgroup.*

#### Evidence base

KEYNOTE-158 reported ORR 34.3% (95% CI 28.3-40.8) in the MSI-H/dMMR cohort ([PMID 31682550](https://pubmed.ncbi.nlm.nih.gov/31682550)) and ORR 29% (95% CI 21-39) in the TMB-high (≥10 mut/Mb) subgroup ([PMID 32919526](https://pubmed.ncbi.nlm.nih.gov/32919526), [NCT02628067](https://clinicaltrials.gov/study/NCT02628067)). Both rows admit biliary tract cancer through the biomarker, not a dedicated cohort, and neither publishes a CCA-specific subgroup ORR, so the biliary magnitude is inferred from a 27-tumor pool.

#### Likelihood of desired effect

Moderate in the MSI-H/dMMR or TMB-high subset, with the long-tail durability checkpoint blockade can deliver. MSI-H/dMMR is uncommon in biliary tract cancer (roughly 1-3%) but decision-changing when present.

#### Toxicity profile

- Immune-mediated grade 3-5 TRAEs ~14.6%; one treatment-related death (pneumonia)
- Immune-mediated colitis, pneumonitis, and endocrinopathies, class effects with an established management algorithm

#### Counter-productive mechanisms / dissent

The advocate surfaced it and declined to penalize the IV route since no modality veto exists. The critic and concensusite noted it as a legitimate conditional option but kept it off their ranked five on prevalence and the missing CCA-specific subgroup ORR, not on any mechanism objection. A confirmed MSI-H or TMB-high read still admits the patient to the labeled indication. The dissent is preference and evidence-flavored, not mechanistic; T-cell exhaustion is a theoretical checkpoint risk but was not raised for this biomarker-selected setting.

#### Practical considerations

IV every three weeks. Open MSI-H/TMB-high basket (NCT02628067) covers prefers_trials. MMR IHC with reflex MSI-PCR is the fastest orthogonal gate, and the same CGP returns the TMB value. No organ-function baseline was supplied to confirm immune-AE monitoring is feasible.

#### Why this rank

Agreement 0.2, with one explicit endorsement. It sits last because MSI-H/dMMR runs only 1-3% in biliary cancer, the lowest-prevalence positive on the panel, and KEYNOTE-158 publishes no CCA-specific subgroup ORR, so the biliary magnitude is inferred from a 27-tumor pool. When it does confirm, the durability is real, which is the advocate's reason for keeping it ranked rather than dropping it.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Pembrolizumab — KEYNOTE-158 MSI-H/dMMR cohort, n=233 | ORR 34.3% (95% CI 28.3-40.8) | Immune-mediated G3-5 TRAEs ~14.6%; one TRAE death | [PMID 31682550](https://pubmed.ncbi.nlm.nih.gov/31682550) |
| Pembrolizumab — KEYNOTE-158 TMB-high (≥10 mut/Mb) subgroup, n=102 | ORR 29% (95% CI 21-39) | Per study-wide immune-mediated AE profile | [PMID 32919526](https://pubmed.ncbi.nlm.nih.gov/32919526) |

## Classes examined but not ranked

- **Larotrectinib and entrectinib (NTRK fusion):** both are tumor-agnostically active — larotrectinib ORR 79% in the pooled TRK basket ([PMID 32105622](https://pubmed.ncbi.nlm.nih.gov/32105622)), entrectinib ORR 57.4% ([PMID 31838007](https://pubmed.ncbi.nlm.nih.gov/31838007)) — but NTRK fusions run under 1% in CCA, the lowest-prevalence axis on the panel, and the evidence is cross-tumor pooled with no biliary cohort. The critic and concensusite kept them off the ranked set on that inversion of testing priority. Defensible if the RNA arm returns a fusion; the same panel resolves both.
- **Selpercatinib (RET fusion):** tumor-agnostic, ORR 43.9% in the LIBRETTO-001 basket ([PMID 36029780](https://pubmed.ncbi.nlm.nih.gov/36029780)), but a 7% grade-5 TEAE rate and rare RET fusions in CCA kept it off the ranked set per the conservative and critic. Defensible if RET confirms; resolved by the same RNA arm.
- **Adagrasib-class KRAS G12C inhibitors:** the biliary readout is a 12-patient cohort at ORR 41.7% with a ROBINS-I Serious rating ([PMID 37099736](https://pubmed.ncbi.nlm.nih.gov/37099736)), the single weakest evidence row in the set, and no society lists a BTC-specific KRAS G12C recommendation. Trial enrollment (NCT05722327) is the route here, not a ranked recommendation.
- **Next-generation FGFR2 agents below lirafugratinib (gunagratinib, tinengotinib, fanregratinib, TYRA-200, 3D185):** mechanistically coherent for the FGFR2 lane, but each rests on an underpowered or non-Western-registered readout — gunagratinib on n=17 (ORR 52.9%, [doi:10.1200/JCO.2023.41.4_suppl.572](https://doi.org/10.1200/JCO.2023.41.4_suppl.572)), tinengotinib on an 11-patient FGFR2 subset (ORR 27.3%, [PMID 38297981](https://pubmed.ncbi.nlm.nih.gov/38297981)) — so the board held them in the trial-enrollment lane rather than ranking them above the approved agents.

## Ranked prioritization

<div class="trial-table-wrap">
  <div class="trial-scroll">
    <table class="trial-table">
      <thead><tr><th>Rank</th><th>Intervention</th><th>Likelihood of effect</th><th>Toxicity burden</th><th>Counter-productive MoA</th><th>Overall</th></tr></thead>
      <tbody>
        <tr>
          <td>1</td>
          <td><strong>Comprehensive genomic profiling — paired DNA + RNA NGS + HER2 IHC/ISH + MMR IHC</strong><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Diagnostic certainty — resolves which of up to eight feature-conditional pathways is reachable; ~40% prior probability of a targetable hit across the panel.</td>
          <td>Low (none — diagnostic test on tissue or blood)</td>
          <td><strong>N/A</strong> <span class="cpm-desc">(diagnostic, not therapeutic)</span></td>
          <td><strong>The non-toxic gate that opens every feature-conditional rec below; one paired DNA+RNA panel plus HER2 IHC/ISH and MMR IHC resolves seven of eight axes in a single pass.</strong></td>
        </tr>
        <tr>
          <td>2</td>
          <td><strong>Ivosidenib</strong> <span class="scenario-conditional">(conditional on idh1_r132 positive)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Moderate for control, low for shrinkage: randomized PFS HR 0.37 (pmid:32416072) but ORR only 2% and ITT OS non-significant (HR 0.69, p=0.060).</td>
          <td>Low (ascites 7%, QT prolongation, fatigue — grade 3+ tracked placebo)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(no counter-productive vector; risktaker's dissent was magnitude-of-benefit, not mechanism)</span></td>
          <td><strong>The only randomized and only category-1 option, but the survival claim rests on a PFS win and crossover modeling — buys control, not response.</strong></td>
        </tr>
        <tr>
          <td>3</td>
          <td><strong>Futibatinib</strong> <span class="scenario-conditional">(conditional on fgfr2_fusion positive)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span></small></td>
          <td>Moderate-to-high in FGFR2-fusion disease: ORR 42%, mOS 21.7 mo (pmid:36652354), concordant in direction with FIGHT-202 and the selective agents.</td>
          <td>Moderate (hyperphosphatemia 30% G3+, AST rise, stomatitis, fatigue)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(on-target FGFR inhibition; acquired kinase-domain resistance blunts durability but covalent binding delays escape)</span></td>
          <td><strong>The published, on-label FGFR2 anchor with a resistance-coverage edge for sequencing; response is a surrogate endpoint with no randomized comparator.</strong></td>
        </tr>
        <tr>
          <td>4</td>
          <td><strong>Pemigatinib</strong> <span class="scenario-conditional">(conditional on fgfr2_fusion positive)</span><br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Moderate in FGFR2-fusion disease: ORR 35.5% (pmid:32203698), concordant with futibatinib in direction; single-arm surrogate endpoint.</td>
          <td>High (grade 3+ AE 64%; hyperphosphatemia 55%, retinal detachment, hypophosphatemia)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(on-target FGFR inhibition; FGFR1-driven hyperphosphatemia is on-mechanism; acquired resistance blunts durability)</span></td>
          <td><strong>The longest-tenured FGFR2 option with the deepest safety record; edged below futibatinib on resistance-coverage sequencing, not on efficacy.</strong></td>
        </tr>
        <tr>
          <td>5</td>
          <td><strong>Lirafugratinib (RLY-4008)</strong> <span class="scenario-conditional">(conditional on fgfr2_fusion positive)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span></small><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span></small></td>
          <td>Moderate-to-high in FGFR2-fusion disease but low-certainty: ORR 46.5% (doi:10.1200/JCO.2026.44.2_suppl.476) is single-arm, abstract-only, pre-approval.</td>
          <td>Moderate (palmar-plantar erythrodysesthesia 32.8% G3+, stomatitis 12.1%)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(critic and conservative dissented on evidence maturity and the 32.8% hand-foot burden, not a counter-productive mechanism per se)</span></td>
          <td><strong>The highest-ORR FGFR2 option and the best hyperphosphatemia profile, but abstract-only, pre-approval, and carrying a one-in-three grade-3 hand-foot rate.</strong></td>
        </tr>
        <tr>
          <td>6</td>
          <td><strong>Zanidatamab</strong> <span class="scenario-conditional">(conditional on erbb2_amp positive)</span><br><small><em>endorse:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>Moderate in HER2-positive disease: confirmed ORR 41.3%, mDoR 12.9 mo (pmid:37276871), single-arm pivotal cohort with no randomized comparator.</td>
          <td>Low (diarrhea 5% G3, decreased ejection fraction 3% G3, infusion reactions)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(on-target HER2 blockade; no mechanism-level dissent — the tension was T-DXd's ILD, resolved by ranking zanidatamab ahead)</span></td>
          <td><strong>The dedicated-trial HER2 lead, ranked above T-DXd on a 10.5% ILD signal with no pulmonary baseline on file; gated on IHC 3+ with reflex ISH.</strong></td>
        </tr>
        <tr>
          <td>7</td>
          <td><strong>Dabrafenib + trametinib</strong> <span class="scenario-conditional">(conditional on braf_v600e positive)</span><br><small><em>endorse:</em> <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-concensusite">concensusite</span></small></td>
          <td>Moderate-to-high in BRAF V600E disease: ORR 47%, mPFS 9.0 mo (pmid:32818466); small single-arm cohort, low prevalence caps expected yield.</td>
          <td>Moderate (pyrexia 19%, GGT rise 12% G3+, serious AE 40%)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(on-target MAPK inhibition; MEK co-inhibition mitigates paradoxical RAF activation; no mechanism-level dissent)</span></td>
          <td><strong>A high-response, dual-endorsed doublet if V600E confirms; ranked low on 1-5% prevalence and a small single-arm cohort, not on any objection.</strong></td>
        </tr>
        <tr>
          <td>8</td>
          <td><strong>Trastuzumab deruxtecan</strong> <span class="scenario-conditional">(conditional on erbb2_amp positive)</span><br><small><em>dissent:</em> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-advocate">advocate</span></small></td>
          <td>High in IHC 3+ subgroup (ORR 56-61%) but low-certainty overall: full biliary-cohort ORR 22%, investigator-assessed (pmid:37870536), gated by ILD risk.</td>
          <td>High (ILD/pneumonitis 10.5% with 3 treatment-related deaths; grade 3+ AE 40.8%)</td>
          <td><strong>Moderate</strong> <span class="cpm-desc">(on-mechanism ILD/pneumonitis from the deruxtecan payload can cause fatal pulmonary injury, blunting the goal in an unmonitored patient)</span></td>
          <td><strong>Competitive IHC 3+ activity held below zanidatamab on a 10.5% ILD signal with three deaths and no pulmonary baseline; re-entry needs an ILD-monitoring plan.</strong></td>
        </tr>
        <tr>
          <td>9</td>
          <td><strong>Pembrolizumab</strong> <span class="scenario-conditional">(conditional on msi_tmb positive)</span><br><small><em>endorse:</em> <span class="persona persona-advocate">advocate</span></small></td>
          <td>High and durable when MSI-H/dMMR positive (ORR 34.3%, mOS 23.5 mo, pmid:31682550) but low prevalence (1-3%); TMB-high a weaker predictor.</td>
          <td>Low (immune-mediated AEs; grade 3-5 14.6%, one treatment-related death)</td>
          <td><strong>Low</strong> <span class="cpm-desc">(T-cell exhaustion is a theoretical checkpoint risk but not raised by any persona for this biomarker-selected setting)</span></td>
          <td><strong>Durable benefit when MSI-H/dMMR confirms, resolved free by the rank-1 workup; ranked last on 1-3% prevalence and no published CCA subgroup ORR.</strong></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

!!! note "Reading the columns"
    **Toxicity burden** is patient-level G3+ AE severity (Low / Moderate / High) summarized from the trial publications. **Counter-productive MoA** is the mechanism-level risk that the intervention's own pathway could blunt the therapeutic goal, distinct from patient AEs. The board's endorse / dissent / veto state appears as pills under each intervention; full per-persona rationale lives on the [board page](board.md).

## Caveats

- **Evidence-base caveats.** Outside ClarIDHy (the one randomized phase 3), every ranked therapeutic rests on single-arm phase 2 data with a surrogate ORR endpoint and no comparator. The FGFR2 lane carries the nearest thing to replication, two approved-agent trials converging on the same axis, but neither is randomized, and the FGFR2-selective option (lirafugratinib) sits on an abstract-only readout with no peer-reviewed full text, no PubMed record, and a pending September 2026 PDUFA. The immunotherapy rows are pooled cross-tumor baskets with no CCA-specific subgroup ORR, so the biliary magnitude is inferred. The KRAS G12C biliary readout is a 12-patient cohort, the weakest row in the set, and stays a trial-enrollment route rather than a ranked recommendation.
- **Biomarker dependency.** Every rank below the workup is conditional on its own feature reading positive. The rankings assume confirmation arrives; without it, none of ranks 2-9 applies. The protein gates are not interchangeable with the DNA panel: HER2 needs IHC with reflex ISH, BRAF needs a true V600E by NGS/PCR, and dMMR is fastest confirmed by MMR IHC with reflex MSI-PCR. A low-positive HER2 read (below IHC 3+) is a weaker predictor than a 3+ result and would make T-DXd investigational rather than on-label in this setting.
- **What would change the ranking.**
    - A positive IDH1 R132 read holds ivosidenib at rank 2 on evidence grade; a positive FGFR2 fusion alongside it would prompt the risktaker's and advocate's reorder toward the higher-response FGFR lane, since depth of response, not the lowest grade-3 rate, is the tie-break they argue for in advanced disease.
    - Lirafugratinib's September 2026 PDUFA read plus a peer-reviewed ReFocus safety table would lift it from considered_with_caveats toward the approved FGFR agents; a negative full-paper audit of response ascertainment would push it further down.
    - A documented HER2 IHC 3+ read plus a baseline pulmonary assessment and a written ILD-monitoring plan would move T-DXd up within the HER2 lane; the conservative stated they would not block it on those conditions.
    - Organ-function labs, performance status, prior-therapy history, or an actual patient preference would re-rank the whole set; a stated toxicity veto on hyperphosphatemia, pyrexia, hand-foot syndrome, or ILD would reorder the relevant lanes immediately.
- **Re-scoping caveat.** This ranking is a placeholder over a scope-unknown intake. If real molecular results, prior lines, performance status, or patient values arrive, re-run intake; the ranking narrows sharply to whichever feature reads positive, and if none does, the case has no within-scope recommendations.

## Sources

**PubMed (PMID):**

- [31682550](https://pubmed.ncbi.nlm.nih.gov/31682550) — Marabelle et al., KEYNOTE-158 MSI-H/dMMR, *J Clin Oncol* 2020
- [31838007](https://pubmed.ncbi.nlm.nih.gov/31838007) — Doebele et al., entrectinib NTRK basket, *Lancet Oncol* 2020
- [32105622](https://pubmed.ncbi.nlm.nih.gov/32105622) — Hong et al., larotrectinib TRK-fusion pooled analysis, *Lancet Oncol* 2020
- [32203698](https://pubmed.ncbi.nlm.nih.gov/32203698) — Abou-Alfa et al., FIGHT-202 pemigatinib, *Lancet Oncol* 2020
- [32416072](https://pubmed.ncbi.nlm.nih.gov/32416072) — Abou-Alfa et al., ClarIDHy ivosidenib, *Lancet Oncol* 2020
- [32818466](https://pubmed.ncbi.nlm.nih.gov/32818466) — Subbiah et al., ROAR dabrafenib + trametinib, *Lancet Oncol* 2020
- [32919526](https://pubmed.ncbi.nlm.nih.gov/32919526) — Marabelle et al., KEYNOTE-158 TMB-high, *Lancet Oncol* 2020
- [34848557](https://pubmed.ncbi.nlm.nih.gov/34848557) — Wu et al., mutant IDH IFNγ-TET2 immunoevasion (preclinical), *Cancer Discov* 2022
- [36029780](https://pubmed.ncbi.nlm.nih.gov/36029780) — Subbiah et al., LIBRETTO-001 selpercatinib, *Lancet Oncol* 2022
- [36652354](https://pubmed.ncbi.nlm.nih.gov/36652354) — Goyal et al., FOENIX-CCA2 futibatinib, *NEJM* 2023
- [36914633](https://pubmed.ncbi.nlm.nih.gov/36914633) — zanidatamab biparatopic HER2 clustering (preclinical), *Nat Commun* 2023
- [37099736](https://pubmed.ncbi.nlm.nih.gov/37099736) — Bekaii-Saab et al., adagrasib KRAS G12C solid tumors, *J Clin Oncol* 2023
- [37276871](https://pubmed.ncbi.nlm.nih.gov/37276871) — Harding et al., HERIZON-BTC-01 zanidatamab, *Lancet Oncol* 2023
- [37870536](https://pubmed.ncbi.nlm.nih.gov/37870536) — Meric-Bernstam et al., DESTINY-PanTumor02 T-DXd, *J Clin Oncol* 2024
- [38297981](https://pubmed.ncbi.nlm.nih.gov/38297981) — tinengotinib FGFR2 phase 1 subset, 2024

**Conference abstract (DOI):**

- [10.1200/JCO.2026.44.2_suppl.476](https://doi.org/10.1200/JCO.2026.44.2_suppl.476) — lirafugratinib ReFocus FGFRi-naive CCA cohort, ASCO GI 2026 (abstract-only)
- [10.1200/JCO.2023.41.4_suppl.572](https://doi.org/10.1200/JCO.2023.41.4_suppl.572) — gunagratinib FGFR2 cohort, ASCO GI 2023 (abstract-only)

**ClinicalTrials.gov (NCT):**

- [NCT02034110](https://clinicaltrials.gov/study/NCT02034110) — ROAR basket (dabrafenib + trametinib)
- [NCT02052778](https://clinicaltrials.gov/study/NCT02052778) — FOENIX-CCA2 (futibatinib)
- [NCT02576431](https://clinicaltrials.gov/study/NCT02576431) — NAVIGATE basket (larotrectinib)
- [NCT02628067](https://clinicaltrials.gov/study/NCT02628067) — KEYNOTE-158 (pembrolizumab)
- [NCT02924376](https://clinicaltrials.gov/study/NCT02924376) — FIGHT-202 (pemigatinib)
- [NCT02989857](https://clinicaltrials.gov/study/NCT02989857) — ClarIDHy (ivosidenib)
- [NCT04466891](https://clinicaltrials.gov/study/NCT04466891) — HERIZON-BTC-01 (zanidatamab)
- [NCT04482309](https://clinicaltrials.gov/study/NCT04482309) — DESTINY-PanTumor02 (trastuzumab deruxtecan)
- [NCT04526106](https://clinicaltrials.gov/study/NCT04526106) — ReFocus (lirafugratinib; the CCA cohort, distinct from the CCA-excluding basket NCT07359820)

## Transparency artifacts

- [Trial table](trials.md) — 30 rows, all columns
- [Evidence list](evidence.md) — 26 clinical-evidence rows + 12 preclinical rows
- [Master manuscripts table](manuscripts.md) — every paper considered, with n, effect, variance, and toxicity columns
- [Tumor-board transcript](board.md) — 5 positions, 30 cross-critiques
- [Recommendations table](recommendations.md) — full ranked detail with the biomarker-conditional flag
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Re-run July 2026 after the board fully re-deliberated over a refreshed dossier: the trial screen added 16 new on-axis studies (30 trials total, 26 clinical-evidence rows, 12 preclinical). The intake remains scope-unknown — the only input was "metastatic cholangiocarcinoma, no other information" — so the profile enumerates the recognized actionable biliary panel as candidate features, every one flagged `ngs_pending`, with comprehensive genomic profiling as the rank-1 gate. Age band, ECOG, stage detail, geography, and the balanced 0.5 efficacy/toxicity weight are placeholders, not user-supplied values, and are flagged as assumptions throughout. The nine ranked rows synthesize five board positions and thirty cross-critiques; agreement scores follow the (endorse − dissent − 2·veto)/5 rule, with ranking-order disputes distinguished from dissent against an intervention's use. Two rows sit at considered_with_caveats — lirafugratinib (three-persona dissent on abstract-only maturity and guideline order) and T-DXd (three-persona shared downgrade on the ILD signal). No formal vetoes were issued this run; the prior run's T-DXd veto resolved to a shared downgrade below zanidatamab. Reference verification promoted corrected identifiers over three upstream drifts still present in the read-only dossier: zanidatamab HERIZON-BTC-01 (pmid 37423227 → 37276871), larotrectinib pooled analysis (pmid 32092306 → 32105622), and the ivosidenib IFNγ-TET2 preclinical anchor (pmid 34880079 → 34848557). Because those source files are upstream-owned, re-run the evidence/target-validator stages to correct them at source. The cross-cutting caveat carries the negative-result foreclosure mapping. If real molecular results, prior lines, performance status, or patient values arrive, re-run intake. Humanizer pass applied July 2026.

<!-- libby:downloads:begin -->

## Downloads

### HTML

- [Target validation paths](target_validation.md?v=0fb86497) — per-feature biomarker-workup table with providers and references, sortable in-browser
- [Recommendations table](cca-mets-scope-unknown-z3p9-recommendations.html?v=f0b69849) — ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline
- [Access guide](accessibility.md?v=0f1ac5cf) — how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table
- [Access guide (offline)](cca-mets-scope-unknown-z3p9-accessibility.html?v=719b462f) — same access-guide content packaged as a self-contained HTML that opens offline
- [Master manuscripts table](manuscripts.md?v=de7b9de7) — every paper considered — n, effect, variance, toxicities, in a sortable in-browser table
- [Master manuscripts table (offline)](cca-mets-scope-unknown-z3p9-manuscripts.html?v=7fe9c969) — same manuscripts inventory packaged as a self-contained HTML that opens offline

### PDF

- [Target validation paths](cca-mets-scope-unknown-z3p9-target-validation.pdf?v=e3fd75db) — diagnostic + biomarker workup that hardens the targetable-feature call
- [Recommendations table](cca-mets-scope-unknown-z3p9-recommendations.pdf?v=8bee84fc) — ranked options + pipeline context + evidence in detail, in a print-friendly PDF
- [Access guide](cca-mets-scope-unknown-z3p9-accessibility.pdf?v=dd92c88d) — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF
- [Master manuscripts table](cca-mets-scope-unknown-z3p9-manuscripts.pdf?v=c834ccef) — every paper considered — n, effect, variance, toxicities, in a print-friendly PDF
- [Patient/caregiver PDF](cca-mets-scope-unknown-z3p9-plain-language.pdf?v=11a205bb) — plain-language summary

<!-- libby:downloads:end -->

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
