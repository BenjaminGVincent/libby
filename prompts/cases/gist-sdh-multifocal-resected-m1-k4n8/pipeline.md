# Pipeline roster — gist-sdh-multifocal-resected-m1-k4n8

## Targetable feature 1: SDH-deficient GIST (biallelic SDHA, KIT/PDGFRA-WT)

| Drug / regimen | Aliases | Modality | Sponsor | Latest phase | Development status |
|---|---|---|---|---|---|
| Belzutifan | MK-6482, PT2977, WELIREG | small_molecule (HIF-2α inhibitor) | Merck | Phase 2 (NCT04924075, wt-GIST cohort) | phase_2_active; approved (VHL-associated tumors, advanced ccRCC) |
| Temozolomide | TMZ, TEMODAR | small_molecule (alkylator) | UCSD (Burgoyne); Asan Medical Center | Phase 2 (NCT03556384, NCT05661643) | phase_2_active; approved (GBM, anaplastic astrocytoma) |
| Pemigatinib | INCB054828, Pemazyre | small_molecule (FGFR1/2/3 inhibitor) | Dana-Farber / Incyte | Phase 2 (NCT07434843, PEMIGIST) | phase_2_active; approved (cholangiocarcinoma w/ FGFR2 fusion, MLN w/ FGFR1) |
| Guadecitabine | SGI-110 | small_molecule (DNA methyltransferase inhibitor / hypomethylating agent) | NCI | Phase 2 (NCT03165721) | discontinued (trial terminated low accrual; published Ligon 2023) |
| Linsitinib | OSI-906 | small_molecule (IGF-1R/insulin receptor inhibitor) | NCI / SARC | Phase 2 (NCT01560260) | legacy_research_only (completed; negative; von Mehren 2020) |
| DFF332 | DFF332 | small_molecule (HIF-2α inhibitor, next-gen) | Novartis | Phase 1 (NCT04895748) | discontinued (terminated Feb 2026, business decision; SDH-mutated paraganglioma expansion arm never opened) |
| NKT-2152 | NKT2152 | small_molecule (HIF-2α inhibitor) | Nikang | Phase 1/2 (NCT05119335, ccRCC only) | discontinued (terminated Nov 2025, portfolio reprioritization) |
| TMZ + olaparib (PARP) | — | small_molecule + PARP combo | case-report only (Singh 2023, Pediatr Blood Cancer) | n/a (case report) | legacy_research_only |

## Targetable feature 2: KIT/PDGFRA wild-type GIST (TKI backbone, SOC adjacent)

| Drug | Aliases | Modality | Sponsor | Status |
|---|---|---|---|---|
| Sunitinib | SU011248, Sutent | small_molecule (multi-TKI) | Pfizer | approved (2L GIST); some dSDH-GIST activity |
| Regorafenib | BAY 73-4506, Stivarga | small_molecule (multi-TKI) | Bayer | approved (3L GIST); modest dSDH-GIST activity |
| Ripretinib | DCC-2618, Qinlock | small_molecule (KIT/PDGFRA switch-control TKI) | Deciphera | approved (4L GIST); limited dSDH-GIST data |
| Imatinib (adjuvant) | STI-571, Gleevec | small_molecule (KIT/PDGFRA TKI) | Novartis | approved (adjuvant high-risk KIT-mutant GIST); LOW activity in dSDH-GIST |

## Targetable feature 3: MAP2K1 P124S (ctDNA, tissue-confirmation pending)

| Drug | Aliases | Modality | Trial | Status |
|---|---|---|---|---|
| Cobimetinib | GDC-0973, Cotellic | small_molecule (MEK1/2 inhibitor) | MEGALiT NCT04185831 (NF1/MAP2K1 cohort) | phase_2_active; approved (BRAF V600 melanoma) |
| Trametinib | GSK1120212, Mekinist | small_molecule (MEK1/2 inhibitor) | MyCustom-02 NCT06739395 (MAP2K1 alteration arm) | phase_2_active; approved (BRAF V600 melanoma, NSCLC, ATC) |
| Selumetinib | AZD6244, Koselugo | small_molecule (MEK1/2 inhibitor) | NCT03109301 (NF1-GIST; WITHDRAWN) | discontinued (NF1-GIST arm withdrawn) |

## Targetable feature 4: PIK3CA R93W (ctDNA, non-canonical, tissue-confirmation pending)

| Drug | Aliases | Modality | Trial | Status |
|---|---|---|---|---|
| Inavolisib | GDC-0077, RG6114, Itovebi | small_molecule (PI3Kα-selective) | CRAFT NCT04551521 (closed); TAPISTRY NCT04589845 cohort H (closed) | approved (HR+/HER2- breast w/ PIK3CA mut + endocrine + CDK4/6i) |
| Tersolisib | STX-478 | small_molecule (allosteric PI3Kα) | NCT05768139 (recruiting) | phase_1_2_active |
| Alpelisib | BYL719, Piqray | small_molecule (PI3Kα-selective) | NCT04526470 (gastric) | approved (HR+/HER2- breast PIK3CA mut) |

## Tumor-agnostic / natural-history registries

| Protocol | NCT | Sponsor | Notes |
|---|---|---|---|
| Rare-tumor natural-history & biospecimen registry | NCT03739827 | NCI | Includes SDH-deficient GIST on eligibility list; biospecimen + longitudinal follow-up |
| DART rare-tumor immunotherapy (S1609) | NCT02834013 | SWOG | GIST cohort closed 2018; not enrollable |

## Coverage gap notes

- The NCI "Pediatric and Wild-Type GIST Clinic" referenced in target_validation does not appear to have a single registry NCT — it operates as a referral clinic under the NCI Pediatric Oncology Branch and feeds patients into NCT03739827 and into the negative-result NCT01560260 linsitinib trial. Treat the clinic as a referral pathway rather than a trial row.
- No active adjuvant trial enrolls KIT-WT / SDH-deficient GIST specifically; the historical adjuvant imatinib trials (Z9001 / SSGXVIII / PERSIST-5) all required KIT-positive disease.
- HIF-2α next-gen (DFF332, NKT-2152) both terminated for non-safety reasons in 2025–2026 — belzutifan is the only active HIF-2α program with a wt-GIST cohort.
