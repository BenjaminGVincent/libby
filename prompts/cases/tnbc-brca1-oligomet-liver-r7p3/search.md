# Search spec — tnbc-brca1-oligomet-liver-r7p3

## Patient one-liner
42-year-old woman, newly diagnosed de novo M1 TNBC (single 1.5 cm liver lesion + ipsilateral axillary nodes, cT2-3 cN1 cM1), basal-like, ECOG 1, no prior systemic therapy. Targetable features: BRCA1 mut, TP53 mut, PIK3CA mut (codon TBD), MYC amp, IRS2 amp, PTEN loss, basal-like subtype, TMB 14 mut/Mb (TMB-H), 3+ stromal TILs, MSS, ER-/PR-/HER2-. PD-L1 CPS not yet documented. Geography_band: null (no filter).

## Targetable features and drug-class anchors

| Feature                       | Drug classes / anchor agents                                                                                                       |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| BRCA1 mutation                | olaparib, talazoparib, niraparib, rucaparib (PARPi); platinum (carboplatin, cisplatin); PARPi + ICI (durvalumab, pembrolizumab)    |
| TP53 mutation                 | adavosertib (AZD1775), azenosertib (ZN-c3), debio-0123 (WEE1i); ATR inhibitors (ceralasertib AZD6738, elimusertib BAY-1895344)     |
| PIK3CA mutation               | alpelisib (BYL719), inavolisib (GDC-0077), capivasertib (AZD5363)                                                                  |
| MYC amplification             | BET inhibitors (BMS-986158, ZEN-3694, NUV-868, PLX2853); CDK7 (samuraciclib CT7001, SY-5609); CDK9 (enitociclib, KB-0742)          |
| IRS2 amplification            | IGF-1R / IRS axis — xentuzumab, BI-836845; tepotinib-class out of scope                                                            |
| PTEN loss                     | capivasertib; ipatasertib (GDC-0068); MK-2206                                                                                      |
| Basal-like (TROP2)            | sacituzumab govitecan (IMMU-132), datopotamab deruxtecan (Dato-DXd, DS-1062a); +/- ICI                                             |
| TMB-H (14 mut/Mb)             | pembrolizumab tumor-agnostic; nivolumab; ipilimumab + nivolumab                                                                    |
| 3+ TIL                        | pembrolizumab + chemo (KEYNOTE-355), atezolizumab + nab-paclitaxel (IMpassion), durvalumab combos                                  |

## Search axes

1. **Tumor type + line + biomarker**
   - "TNBC 1L metastatic"; "TNBC PIK3CA"; "TNBC BRCA1"; "TNBC TMB"; "TNBC PD-L1 CPS"; "basal-like TNBC trial"; "oligometastatic breast cancer".
2. **Biomarker / target alone (basket and pan-tumor)**
   - "BRCA1 BRCA2 PARP basket"; "BRCA HRD platinum any tumor"; "MYC amplification basket BET"; "TMB-H pembrolizumab KEYNOTE-158 basket"; "PIK3CA inavolisib basket"; "AKT inhibitor PTEN basket".
3. **Drug name / mechanism per anchor agent**
   - For each anchor agent: alias-expanded ClinicalTrials.gov + PubMed query (e.g. olaparib OR Lynparza OR AZD2281; talazoparib OR Talzenna OR BMN-673; samuraciclib OR CT7001; ceralasertib OR AZD6738; azenosertib OR ZN-c3 OR ZN-c3; capivasertib OR AZD5363 OR Truqap; inavolisib OR GDC-0077 OR Itovebi; sacituzumab govitecan OR IMMU-132 OR Trodelvy; datopotamab OR Dato-DXd OR DS-1062a OR Datroway).

## Pipeline reconnaissance — modality cross-product

For each targetable feature, pull one recent (2024-2026) target-specific review and enumerate the investigational pipeline by modality:

- **PARPi**: olaparib (FDA, OlympiAD), talazoparib (FDA, EMBRACA), niraparib (FDA OvCa), rucaparib (FDA OvCa), pamiparib (China). Combos: + ICI (DORA, MEDIOLA, KEYLYNK-009, JAVELIN PARP Medley), + ATR (CAPRI), + WEE1.
- **WEE1i**: adavosertib (AZD1775, discontinued by AZ 2021), azenosertib (ZN-c3, Zentalis, active), debio-0123 (Debiopharm).
- **ATRi**: ceralasertib (AZD6738, AZ), elimusertib (BAY-1895344, Bayer; discontinued 2023), camonsertib (RP-3500, Repare), berzosertib (M6620, Merck KGaA, paused), tuvusertib (M1774, Merck KGaA).
- **PI3Kα / inavolisib / capivasertib / alpelisib**: alpelisib (FDA), inavolisib (FDA 2024 in HR+, basket trials), capivasertib (FDA HR+, CAPItello-290 in TNBC), ipatasertib (Roche; deprioritized post-IPATunity130).
- **BET**: BMS-986158 (BMS), ZEN-3694 (Zenith), PLX2853 (Plexxikon), NUV-868 (Nuvation), CC-90010 (BMS), molibresib (GSK; discontinued).
- **CDK7**: samuraciclib (CT7001, Carrick), SY-5609 (Syros), XL102 (Exelixis); **CDK9**: enitociclib (VIP152, BMS), KB-0742 (Kronos), AZD4573 (AZ; discontinued).
- **TROP2 ADC**: sacituzumab govitecan (FDA TNBC ASCENT), datopotamab deruxtecan (Dato-DXd, FDA HR+ TROPION-Breast01, TNBC TROPION-Breast02), sacituzumab tirumotecan (sac-TMT, MK-2870 Merck), DB-1305 (DualityBio), BL-M02D1 (Biokin).
- **ICI**: pembrolizumab, atezolizumab (TNBC withdrawal 2021), durvalumab, nivolumab, cemiplimab.
- **IGF-1R**: xentuzumab (BI-836845; stalled), AVE1642, ganitumab (discontinued), IMC-A12 (cixutumumab; discontinued). Pipeline largely paused.

## Scope rule for this case

Every Keep row must trace to one or more of the targetable features. Standard-of-care chemotherapy backbones (gemcitabine/carboplatin, eribulin, capecitabine) without a feature-targeting mechanism are out of scope. ICI + chemo registrational regimens are in scope because ICI mechanism targets the TMB/TIL feature axis. Olympia adjuvant olaparib (germline BRCA, early breast) is **informational only** — M1 disease puts the patient outside that label, but it anchors the BRCA1 PARPi evidence.

## Target counts

- 15-25 trial rows, high-signal.
- Mix of 1L-eligible (highest priority, given de novo M1 status), 2L+ trials flagged as future options, and informational cross-tumor / discontinued rows for mechanism context.
