# Search spec — mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4

## Patient one-liner
37yo MSS metastatic colon adenocarcinoma. Liver mets resected, peritoneal carcinomatosis active. On FOLFIRI + bevacizumab (1L). Planned cytoreductive surgery + HIPEC. ECOG 1.

Targetable features (all NGS-pending pending confirmation):
- KRAS A59T (atypical switch-II, non-G12/G13/Q61)
- APC E1295 (likely truncating, MCR)
- TP53 R273 (hotspot, GoF; substitution to be specified)
- PIK3CA M1043I (kinase domain activating)
- SMAD4 R361H (MH2 domain LOF; peritoneal-spread biology)
- 20q11 amplification, BCL2L1 + TOP1 co-amplified
- MSS / TMB-low / PD-L1-negative (negative finding that gates ICI biology)
- Peritoneal carcinomatosis with planned CRS-HIPEC (sequencing axis)

## Auto-mode framing
- `efficacy_toxicity_weight 0.70`; no toxicity vetoes; no modality vetoes.
- "Surface all options" — include trials with weak/partial fit so the board sees the full landscape.
- Conditional-fit rows allowed: e.g. "becomes strong if HER2 returns amplified", "becomes strong if BRAF V600E", "BCL-xL trial gated on confirmed BCL2L1 amp".

## Axis-by-axis search plan

### A. Peritoneal CRC / HIPEC / CRS / PIPAC
ClinicalTrials.gov queries:
- `peritoneal metastases colorectal HIPEC`
- `cytoreductive surgery HIPEC colorectal`
- `pressurized intraperitoneal aerosol chemotherapy PIPAC colorectal`
- `PRODIGE 7 PRODIGE 86 BIG-RENAPE`
- `oxaliplatin HIPEC colorectal mitomycin`
- `prophylactic HIPEC colon PROPHYLOCHIP COLOPEC`
- `intraperitoneal chemotherapy colorectal trial`

### B. Atypical KRAS / KRAS A59 / pan-RAS
- `KRAS A59T colorectal`
- `KRAS atypical mutation basket`
- `RMC-6236 daraxonrasib pan-RAS`
- `RMC-9805 KRAS G12D`
- `divarasib GDC-6036`
- `pan-KRAS inhibitor BI-2865 BI-2493 BI-1701963`
- `SOS1 inhibitor BI-3406 MRTX0902`
- `SHP2 inhibitor TNO155 RMC-4630 JAB-3068 BBP-398`
- `MEK inhibitor trametinib binimetinib colorectal`
- `non-G12C KRAS colorectal trial`
- `KRYSTAL-10 KRYSTAL-12 CodeBreak 300`

### C. PIK3CA / PI3K-alpha / AKT / mTOR
- `inavolisib PIK3CA colorectal`
- `INAVO121 inavolisib`
- `alpelisib colorectal PIK3CA`
- `serabelisib sapanisertib`
- `capivasertib colorectal`
- `ipatasertib colorectal`
- `samuraciclib PI3K AKT`
- `RLY-2608 PIK3CA mutant-selective`
- `STX-478 PI3K-alpha mutant-selective`
- `LOXO-783 mutant-selective PI3K`

### D. HER2 (conditional pathway, NGS-pending)
- `MOUNTAINEER tucatinib trastuzumab colorectal`
- `MOUNTAINEER-03 frontline tucatinib`
- `DESTINY-CRC02 trastuzumab deruxtecan`
- `zanidatamab colorectal HER2`
- `zanidatamab zovodotin ZW49`
- `disitamab vedotin RC48 HER2 colorectal`

### E. TP53 R273 / mutant p53 reactivation
- `PYNNACLE rezatapopt PC14586`
- `eprenetapopt APR-246 solid tumor`
- `arsenic trioxide TP53 mutant reactivation`
- `HSP90 inhibitor TP53 mutant solid tumor`
- `PMV-004 TP53 reactivator`
- `ATR inhibitor TP53 colorectal` (synthetic lethality)
- `WEE1 inhibitor adavosertib colorectal TP53`

### F. 20q11 amplification — BCL2L1 / TOP1
- `navitoclax colorectal solid tumor`
- `BCL-xL inhibitor solid tumor`
- `DT2216 BCL-xL PROTAC`
- `AZD0466 BCL-xL nanomedicine`
- `pelcitoclax APG-1252`
- `irinotecan rechallenge TOP1 amplification colorectal`
- `topoisomerase 1 amplification colorectal`
- `camptothecin payload ADC TOP1`

### G. Anti-EGFR backbone in non-G12C atypical KRAS / FRESCO-2 / encorafenib
- `cetuximab atypical KRAS colorectal`
- `panitumumab non-canonical RAS colorectal`
- `FRESCO-2 fruquintinib colorectal`
- `BREAKWATER encorafenib cetuximab first line colorectal`
- `encorafenib binimetinib cetuximab BRAF`
- `KRYSTAL-10 adagrasib cetuximab` (G12C — informational)

### H. MSS-CRC immunotherapy combinations
- `nivolumab ipilimumab MSS colorectal`
- `pembrolizumab MEK inhibitor colorectal`
- `bintrafusp alfa TGF-beta colorectal`
- `botensilimab balstilimab MSS colorectal`
- `regorafenib nivolumab REGONIVO MSS colorectal`
- `lenvatinib pembrolizumab MSS colorectal LEAP-017`
- `GRT-C901 GRT-R902 neoantigen vaccine`
- `NEO-PV-01 personalized vaccine`
- `cibisatamab CEA TCB colorectal`
- `tagraxofusp CEA bispecific colorectal`
- `CAR-T GUCY2C CEA EpCAM colorectal`
- `radiation immunotherapy MSS colorectal abscopal`

### I. Anti-angiogenics beyond bev
- `aflibercept colorectal VELOUR`
- `ramucirumab colorectal RAISE`
- `fruquintinib FRESCO-2`
- `regorafenib CONCUR CORRECT`

### J. Standard 2L / 3L mCRC (sequence with HIPEC)
- `FOLFOX colorectal second line`
- `trifluridine tipiracil bevacizumab SUNLIGHT`
- `regorafenib metastatic colorectal`

### K. MRD / ctDNA-adaptive in mCRC peri-HIPEC
- `circulating tumor DNA HIPEC colorectal`
- `MRD colorectal trial adaptive`
- `CIRCULATE NRG-GI008 colorectal`
- `DYNAMIC-Periton ctDNA HIPEC`
- `BESPOKE Signatera colorectal`

## Scope rules (this case)
- Auto-mode → include trials with weak fit because the board explicitly asked for all options.
- Mark cross-tumor extrapolation rows clearly (`tumor_type_relationship: cross_tumor_extrapolation`).
- Conditional-fit annotations live in `inclusion_match_notes` ("would become strong if HER2 ISH positive", etc).
- HIPEC perioperative/SOC trials count — they're the patient's actual sequencing decision, even though Libby normally drops SOC. The user explicitly requested HIPEC/CRS coverage.

## Output
Append rows to `data/cases/mcrc-kras-a59t-pik3ca-peritoneal-pre-hipec-q8k4/trials.jsonl`. One JSON object per line. Validate each against `scripts/schema/trials.schema.json`.
