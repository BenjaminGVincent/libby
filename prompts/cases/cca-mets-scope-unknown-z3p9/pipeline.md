# Pipeline roster — cca-mets-scope-unknown-z3p9

Scope-unknown CCA. Drugs targeting the candidate features. Most axes are
served by FDA-approved agents (approved on- or off-label for biliary tract /
tumor-agnostic), so the "pipeline" here is mature, not early-phase. All rows
gated on a positive confirmatory test (target_validation.jsonl).

| INN / generic | Aliases (codes) | Target / feature | Modality | Sponsor | Latest phase | Dev status |
|---|---|---|---|---|---|---|
| pemigatinib | INCB054828, Pemazyre | FGFR2 fusion | small_molecule | Incyte | approved (FIGHT-202) | approved |
| futibatinib | TAS-120, Lytgobi | FGFR2 fusion/rearr | small_molecule | Taiho | approved (FOENIX-CCA2) | approved |
| infigratinib | BGJ398, Truseltiq | FGFR2 fusion | small_molecule | QED/Helsinn | approved (US withdrawn 2024 commercial) | approved |
| lirafugratinib | RLY-4008 | FGFR2-selective | small_molecule | Relay/Elevar | phase 2 | phase_2_active |
| TYRA-200 | TYRA-200 | FGFR2 (incl resist) | small_molecule | Tyra Biosciences | phase 1 | phase_1_active |
| HMPL-453 | tinengotinib? / HMPL-453 | FGFR | small_molecule | Hutchmed | phase 2/3 | phase_2_active |
| ivosidenib | AG-120, Tibsovo | IDH1 R132 mutant | small_molecule | Servier | approved (ClarIDHy) | approved |
| zanidatamab | ZW25, zanidatamab-hrii, Ziihera | HER2 biparatopic | bispecific_other | Jazz/BeiGene | approved (HERIZON-BTC-01) | approved |
| trastuzumab deruxtecan | T-DXd, DS-8201, fam-trastuzumab deruxtecan, Enhertu | HER2 ADC | ADC | AstraZeneca/Daiichi Sankyo | approved tumor-agnostic IHC3+ (DP-02) | approved |
| trastuzumab + pertuzumab | — | HER2 | monoclonal_antibody | Genentech/Roche | MyPathway phase 2a | phase_2_active |
| dabrafenib + trametinib | GSK2118436 + GSK1120212, Tafinlar+Mekinist | BRAF V600E + MEK | small_molecule | Novartis | approved tumor-agnostic (ROAR) | approved |
| pembrolizumab | MK-3475, Keytruda | MSI-H/dMMR, TMB-high | monoclonal_antibody | Merck | approved tumor-agnostic (KEYNOTE-158) | approved |
| larotrectinib | LOXO-101, Vitrakvi | NTRK fusion | small_molecule | Bayer/Loxo | approved tumor-agnostic | approved |
| entrectinib | RXDX-101, Rozlytrek | NTRK (+ROS1) fusion | small_molecule | Genentech/Roche | approved tumor-agnostic | approved |
| selpercatinib | LOXO-292, Retevmo | RET fusion | small_molecule | Eli Lilly/Loxo | approved tumor-agnostic (LIBRETTO-001) | approved |
| adagrasib | MRTX849, Krazati | KRAS G12C | small_molecule | Mirati/BMS | approved (NSCLC/CRC); CCA via KRYSTAL baskets | approved |
| sotorasib | AMG 510, Lumakras | KRAS G12C | small_molecule | Amgen | approved (NSCLC); CodeBreaK baskets | approved |

Coverage note: every candidate feature in profile.json has at least one
approved or registrational targeting agent. No coverage gap. The binding
constraint is diagnostic, not therapeutic: nothing can be acted on until CGP
confirms a feature.
