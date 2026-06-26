# Pipeline roster — hgsoc-tuboovarian-stage3c-r0-hrd-pending-idyq

Agents whose mechanism targets a listed targetable feature. Drives per-drug registry search.

## Feature 1 — HRD / homologous-recombination (PARP inhibitors)
| INN / generic | Aliases (codes) | Modality | Sponsor | Latest phase | Development status |
|---|---|---|---|---|---|
| olaparib | AZD2281, KU-0059436, Lynparza | small_molecule PARPi | AstraZeneca / Merck | approved | approved (1L maint, BRCAm; +bev HRD+) |
| niraparib | MK-4827, Zejula | small_molecule PARPi | GSK | approved | approved (1L maint all-comers) |
| rucaparib | AG-014699, CO-338, Rubraca | small_molecule PARPi | pharmaand (ex-Clovis) | approved | approved (relapse maint; ATHENA-MONO 1L) |
| veliparib | ABT-888 | small_molecule PARPi | AbbVie | phase_3 | discontinued (VELIA/GOG-3005 read out; not advanced) |

## Feature 2 — VEGF / angiogenesis (anti-angiogenics)
| INN / generic | Aliases (codes) | Modality | Sponsor | Latest phase | Development status |
|---|---|---|---|---|---|
| bevacizumab | Avastin, rhuMAb-VEGF | monoclonal_antibody anti-VEGF-A | Roche/Genentech | approved | approved (1L + maint ovarian) |
| cediranib | AZD2171, Recentin | small_molecule VEGFR-TKI | AstraZeneca | phase_3 | legacy_research_only (combined w/ olaparib, NRG-GY004/005) |
| olaparib + bevacizumab | PAOLA-1 regimen | combo | AstraZeneca/Roche | approved | approved (1L maint, HRD+) |

## Feature 3 — ER expression (endocrine therapy)
| INN / generic | Aliases (codes) | Modality | Sponsor | Latest phase | Development status |
|---|---|---|---|---|---|
| letrozole | Femara, CGS-20267 | small_molecule aromatase inhibitor | generic | approved | approved_off_label (ER+ HGSC maintenance, investigational use) |
| anastrozole | Arimidex, ZD-1033 | small_molecule aromatase inhibitor | generic | approved | approved_off_label (PARAGON; granulosa/ER+ gyn) |

## Feature 4 — IL-12 / tumor immune microenvironment
| INN / generic | Aliases (codes) | Modality | Sponsor | Latest phase | Development status |
|---|---|---|---|---|---|
| GEN-1 | IMNN-001, EGEN-001, IL-12 plasmid/PEG-PEI-cholesterol lipopolymer | other (IL-12 immunogene) | Imunon | phase_3 | phase_3_active (OVATION 2 done; Phase 3 NCT06915025 recruiting) |

## Feature 7 — HER2-low expression (IHC 1+) — HER2-directed ADCs [ADDED 2026-06 re-run]
HER2-low (IHC 1+) reclassified in-scope. Tumor-agnostic T-DXd approval is IHC 3+ ONLY; all
HER2 ADCs are investigational in this HER2-low ovarian tumor (cross-tumor extrapolation from
breast HER2-low). Capture HER2 cutoff per trial.
| INN / generic | Aliases (codes) | Modality | Sponsor | Latest phase | Development status |
|---|---|---|---|---|---|
| trastuzumab deruxtecan | T-DXd, DS-8201, DS-8201a, fam-trastuzumab deruxtecan-nxki, Enhertu | ADC (topo-I payload) | Daiichi Sankyo / AstraZeneca | approved | approved (agnostic IHC 3+; HER2-low breast) |
| disitamab vedotin | RC48, RC48-ADC, hertuzumab vedotin, Aidixi | ADC (MMAE payload) | RemeGen / Pfizer (ex-Seagen) | phase_2/3 | phase_2_active (China-approved gastric/urothelial; US investigational) |
| trastuzumab duocarmazine | SYD985, vic-trastuzumab duocarmazine | ADC (duocarmazine payload) | Byondis | phase_3 | discontinued (FDA CRL on HER2+ breast filing) |

Key HER2 trials mapped:
- DESTINY-PanTumor02 (Meric-Bernstam 2024, NCT04482309, PMID 37870536) — T-DXd HER2 IHC 2+/3+ pan-tumor basket incl ovarian cohort (ORR 45%). Patient IHC 1+ below cutoff.
- DESTINY-Breast04 (Modi 2022, NCT03734029, PMID 35665782) — T-DXd HER2-low (IHC 1+ or 2+/ISH-) breast. The IHC 1+ cross-tumor anchor.
- DESTINY-Breast06 (Bardia 2024, NCT04494425, PMID 39282896) — T-DXd HR+ HER2-low/ultralow breast; ER+ analog.
- DAISY (Mosele 2023, NCT04132960, PMID 37488289) — T-DXd across HER2 range incl IHC 0 cohort.
- Disitamab vedotin solid-tumor basket (NCT06003231) — HER2 IHC 1+/2+/3+ incl ovarian; accepts IHC 1+ -> actionable.
- Disitamab vedotin + anlotinib platinum-resistant ovarian (NCT06660511) — HER2 IHC 1+/2+/3+; tumor-type match, anlotinib VTE caution.
- SYD985 phase 1 (Banerji 2019, NCT02277717, PMID 31257177) — HER2-low/expressing breast/gastric/urothelial/endometrial; program shelved post-CRL.

## Out-of-scope (foreclosed on current specimen) — NOT entered as fits
- mirvetuximab soravtansine (FRalpha ADC) — FOLR1 below PS2+ threshold.

## Key trials / publications mapped
- SOLO1 (Moore 2018, NCT01844986) — olaparib 1L maint, BRCAm.
- PRIMA (Gonzalez-Martin 2019, NCT02655016) — niraparib 1L maint, all-comers + HRD subgroups.
- PAOLA-1 (Ray-Coquard 2019, NCT02477644) — olaparib + bevacizumab 1L maint, HRD+.
- ATHENA-MONO (Monk 2022, NCT03522246) — rucaparib 1L maint, HRD-stratified.
- GOG-218 (Burger 2011, NCT00262847) — bevacizumab 1L + maint.
- ICON7 (Perren 2011, NCT00483782) — bevacizumab 1L + maint, high-risk benefit.
- NRG-GY004 (Liu 2022, NCT02446600) — olaparib +/- cediranib, recurrent platinum-sensitive.
- Heinzelmann-Schwarz 2018 (PMID 29157627) — letrozole maintenance in HGSC.
- PARAGON anastrozole (Banerjee 2021, PMID 34412908) — ER+/PR+ gyn (granulosa) endocrine.
- GEN-1/IMNN-001: OVATION 2 (NCT03393884), patient's regimen-matched Phase II + bev (NCT05739981),
  Phase 3 (NCT06915025), Thaker/Anwer mechanism review (PMID 30325199), Yin 2023 external-control (PMID 36608308).
