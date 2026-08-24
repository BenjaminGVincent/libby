# Pipeline roster — chondrosarcoma-mets-acetabular-fx-idh-unknown-y34r

Built 2026-08 from ClinicalTrials.gov v2 alias-expanded queries plus NCBI
E-utilities. WebSearch budget was exhausted, so no Google-Scholar sweep of
ASCO / ESMO / AACR abstract sites ran; agents with meeting-only data may be
under-represented. Modality cross-product and isotope sweep both ran (see
`search.md` axes 5, 6, 9).

## IDH1 / IDH2-directed
| INN / generic | Aliases | Modality | Sponsor | Latest phase | Status |
|---|---|---|---|---|---|
| ivosidenib | AG-120, TIBSOVO, S095032 | small molecule | Servier | 3 (chondrosarcoma) | approved (AML, MDS, cholangiocarcinoma) |
| enasidenib | AG-221, IDHIFA, CC-90007 | small molecule | NCI / BMS | 2 (sinonasal/skull-base) | approved (AML) |
| olutasidenib | FT-2102, REZLIDHIA | small molecule | Rigel | 2 | approved (AML); no solid-tumour trial found |
| vorasidenib | AG-881, VORANIGO | small molecule | Servier | 3 | approved (grade 2 glioma); glioma-only programme |
| safusidenib | AB-218, DS-1001 | small molecule | Anheart / Nuvation | 3 | glioma-only |
| LY3410738 | — | covalent mIDH1/2 | Eli Lilly | 1 | solid-tumour basket, accrual closed |
| HMPL-306 | — | dual IDH1/2 | HUTCHMED | 3 | AML and glioma only |
| TQB3454 | — | small molecule | Chia Tai Tianqing | 2 | haematology only |
| BAY1436032 | — | small molecule | Bayer | 1 | no active trial found |
| olaparib + ceralasertib | AZD2281 / AZD6738 | small molecule | NCI | 2 | IDH-mutant basket, synthetic-lethality route |
| IACS-6274 | IPN60090 | glutaminase-1 inhibitor | MD Anderson / Ipsen | 1 | named chondrosarcoma population |

## B7-H3 (CD276)-directed
| INN / generic | Aliases | Modality | Sponsor | Latest phase | Status |
|---|---|---|---|---|---|
| ifinatamab deruxtecan | I-DXd, DS-7300, DS-7300a, MK-2400 | ADC | Daiichi Sankyo / Merck | 3 | sarcoma among enrolling types |
| risvutatug rezetecan | HS-20093, GSK5764227, ris-rez | ADC | Hansoh / GSK | 3 | sarcoma-specific phase 2 (ARTEMIS-002) |
| MGC026 | — | ADC | MacroGenics | 1 | sarcoma named |
| vobramitamab duocarmazine | MGC018 | ADC | MacroGenics | 2 | SCLC only |
| YL201 | — | ADC (B7-H3) | MediLink | 3 | no sarcoma cohort found |
| enoblituzumab | MGA271 | mAb | MacroGenics | 2 | prostate neoadjuvant only |
| omburtamab | 8H9 | radioimmunotherapy (131I, 177Lu) | Y-mAbs | 2 | CNS / DSRCT only |
| B7-H3 CAR-T (multiple) | 4SCAR-276, TAA06, TX103, iC9-CAR.B7-H3, B7-H3CART, CMD03, MT027, hBRCA84D | CAR-T | Stanford, Seattle Children's, UNC, Shenzhen, Tcelltech, others | 1 | mostly paediatric or non-sarcoma |
| CC-3 | — | CD276xCD3 bispecific | Univ. Tübingen | 1 | colorectal only |

## HLA-A*02:01-restricted platform (Step 1.75 eligibility-gate sweep)
Registry sweep on `HLA-A*02:01`, `HLA-A*02`, `A*02:01`, `HLA A2`, `HLA-A2
restricted` crossed with sarcoma conditions.

| Agent | Aliases | Modality | Sponsor | Phase | Gate |
|---|---|---|---|---|---|
| tebentafusp | IMCgp100, KIMMTRAK | ImmTAC | Immunocore / SARC | 2 | HLA-A*02:01, clear cell sarcoma |
| afamitresgene autoleucel | ADP-A2M4, Tecelra | TCR-T | Adaptimmune | 2 | MAGE-A4 + HLA-A*02:01, synovial / MRCLS |
| letetresgene autoleucel | lete-cel, GSK3377794 | TCR-T | GSK / Adaptimmune | 2 | NY-ESO-1 + HLA-A*02:01 |
| brenetafusp | IMC-F106C | ImmTAC | Immunocore / NCI | 3 | PRAME + HLA-A*02:01 |
| IMA203 | ACTengine | TCR-T | Immatics | 3 | PRAME + HLA-A*02:01 |
| MDG1015 | — | 3rd-gen TCR-T | Medigene | 1 | NY-ESO-1 + HLA-A*02:01 |
| ZI-MA4-1 | — | TCR-NK | Zelluna | 1 | MAGE-A4 + HLA-A*02:01 |
| NY-ESO-1 TCR-T (Shenzhen) | — | TCR-T | Shenzhen Univ. Gen. Hosp. | n/a | NY-ESO-1, ECOG 0-2 |

Every one of these gates on the patient's untested HLA class I genotype. None
enrolls a bone sarcoma as written; the gate itself is why HLA typing stays a
high-yield blood draw.

## Isotope sweep (radiopharmaceutical rule)
`chondrosarcoma OR bone sarcoma` × {177Lu, lutetium-177, 225Ac, actinium-225,
131I, iodine-131, 90Y, 211At, 212Pb, 227Th, 161Tb, radioligand,
radioimmunotherapy}, all recruitment statuses.

Returned: LNTH-2403 (177Lu, LRRC15-targeted, relapsed/refractory osteosarcoma,
NCT07357519), 177Lu-DOTATATE + olaparib (paediatric, NCT06607692), CLR 131
(iopofosine, paediatric, NCT03478462), 131I- and 177Lu-omburtamab (CNS /
DSRCT), 225Ac-FPI-2059 (terminated), 131I-8H9 (terminated). Each was screened
individually on therapeutic intent, not filtered as a class: all administer
therapeutic isotope, so none was dropped as imaging-only, but none targets a
nominated feature in an enrolling indication — LNTH-2403 is LRRC15-directed
and osteosarcoma-restricted, omburtamab is B7-H3-directed but CNS/DSRCT-only
and paediatric. No therapeutic radioligand row entered `trials.jsonl`; the
class is empty for this patient rather than excluded. 68Ga-B7-H3 nanobody
immunoPET (NCT07774533) and B7-H3 NIR imaging (NCT06778603) were dropped as
imaging-only per the rule.
