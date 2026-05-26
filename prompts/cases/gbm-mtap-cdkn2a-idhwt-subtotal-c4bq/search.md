# Search spec: gbm-mtap-cdkn2a-idhwt-subtotal-c4bq

## Patient anchor
- 66F, IDH1-wildtype glioblastoma (CNS WHO 2021 grade 4), s/p subtotal resection (residual enhancing disease), intratumoral hemorrhage at presentation
- ECOG 1 (assumed)
- US, no modality vetoes, prefers trials, efficacy-leaning (0.7)
- User intent: "surface all possible options" — interpret as exhaustive

## Confirmed targetable features
1. MTAP homozygous loss (9p21 codeletion)
2. CDKN2A/p16 homozygous loss
3. IDH1 wild-type (negative finding driving SOC and trial framework)

## Unknown / pending (enumerate conditional rows)
- MGMT promoter methylation — branch on methylated vs unmethylated
- EGFR amplification / EGFRvIII — gates CAR-T / bispecific rows
- BRAF V600E, NTRK fusions, MMR/MSI/TMB — tumor-agnostic rows

## Safety annotation
- Intratumoral hemorrhage at presentation — flag any antiangiogenic (bevacizumab, regorafenib) and any T-cell engager with CRS / ICANS risk

## Search axes

### Axis A — MTAP-loss / PRMT5-MTA cooperative + MAT2A
- AMG 193 (BMS-986504) — MTAPESTRY 101 (NCT05094336), GBM cohort
- MRTX1719 — NCT05245500 (Mirati / Bristol Myers Squibb)
- TNG908 (CNS-permeable) and TNG462 (peripheral) — NCT05275920, NCT05732831
- IDE397 (MAT2A) — NCT04794699
- Combination programs: PRMT5i + KRAS / CDK / DNA-damage
- "<feature> × <modality>" grid: small molecule, ADC (rare), bispecific
- Brain-permeant flag: TNG908 is the explicit CNS-penetrant arm

### Axis B — CDKN2A loss / CDK4/6 inhibitors with CNS penetration
- Abemaciclib (NCT02981940 — Wen recurrent GBM phase 2 of CDK4/6i)
- Palbociclib (NCT02530320 and successors)
- Ribociclib + everolimus (NCT03834740 — Wen everolimus combo)
- Newer: PF-06873600 (CDK2/4/6); CDK4-selective PF-07220060
- BI 765845, ribociclib + dabrafenib + trametinib combos
- INSIGhT adaptive platform (NCT02977780) — abemaciclib arm

### Axis C — Front-line IDH-WT GBM stratified by MGMT
- Stupp (Stupp et al. 2005 NEJM) — anchor for SOC
- CeTeG/NOA-09 (Herrlinger 2019 Lancet) — CCNU/TMZ in MGMT-methylated newly diagnosed GBM
- TTFields / Optune (EF-14, NCT00916409)
- Hypofractionated RT in elderly (Perry 2017 — CCTG CE.6)
- Biomarker-stratified front-line: GBM AGILE (NCT03970447) — adaptive platform
- Newly diagnosed trials: NRG-BN007 (ipi/nivo+RT vs TMZ+RT), CodeBreaK 101 GBM arms

### Axis D — EGFRvIII / EGFR-amp targeting
- CAR-T: CART-EGFRvIII (NCT02209376), E-SYNC EGFRvIII×IL13Rα2 (NCT05802693, Bagley/Penn)
- Tandem CAR (NCT03726515 — Bagley/Penn dual EGFR/IL13Rα2)
- Oncolytic / bispecific: CAN-3110 (NCT03152318)
- ADCs: depatuxizumab-mafodotin (ABT-414, INTELLANCE — historical, withdrawn)
- TKIs in CNS: erlotinib historical fail; new: WSD-0922, neratinib

### Axis E — Tumor-agnostic conditional rows
- BRAF V600E: dabrafenib + trametinib (ROAR HGG cohort, Wen 2022 Lancet Oncol)
- NTRK fusions: larotrectinib (Drilon 2018 NEJM, CNS cohort Doz 2022)
- MMR-D / MSI-H / TMB-high: pembrolizumab tumor-agnostic
- KEYNOTE-158 / KEYNOTE-016

### Axis F — Immunotherapy / vaccines / oncolytic virus / non-EGFR CAR-T
- DCVax-L (Liau 2023 JAMA Oncol; NCT00045968 expanded access)
- SurVaxM (NCT05163080; Ahluwalia survivin vaccine)
- IL13Rα2 CAR-T (NCT04003649 — CityHope Brown)
- GD2 CAR-T (NCT04196413 — H3K27M-mutant but include for class)
- B7-H3 CAR-T (NCT04077866, NCT05241392)
- Oncolytic virus: CAN-3110 (NCT03152318), DNX-2401 (NCT00805376), G207 (NCT02457845 — peds), PVSRIPO (lerapolturev) (NCT02986178)
- Checkpoint combos in newly diagnosed: NRG-BN007 ipi/nivo vs TMZ; CheckMate-498/548 historical (negative)

### Axis G — Standard of care
- Stupp RT+TMZ → adjuvant TMZ (anchor)
- TTFields adjuvant (EF-14)
- Bevacizumab for recurrence — flag hemorrhage caveat
- Lomustine / regorafenib for recurrence — flag heme/hemorrhage

### Axis H — Compassionate use / expanded access
- DCVax-L compassionate use
- TTFields commercial availability (no protocol needed)
- Pembrolizumab off-label TMB / MSI access

## Sources
1. ClinicalTrials.gov v2 API — per-drug per-NCT confirmation
2. PubMed E-utilities — pivotal/recent trial publications
3. PMC for OA full text
4. ASCO / SNO 2024-2026 abstracts for early-phase agents

## Coverage rule
Result-cap LIFTED. Pipeline expected to be ≥ 25-35 trials given the breadth requested. Enumerate full PRMT5/MAT2A roster (Step 1.5 mandatory) and full CDK4/6-inhibitor-in-glioma roster.

## Mechanism-scope gate (Libby rule)
For GBM specifically, the user has explicitly invoked SOC + trials + expanded-access. Standard-of-care rows (Stupp, TTFields, bevacizumab) are admitted not on the usual mechanism-scope gate but because the user request explicitly names them. Tag those with `tumor_type_relationship: primary_indication_match` and flag in inclusion_match_notes that they are SOC anchors rather than targetable-feature rows.
