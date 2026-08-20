# Search spec — q-aml-x7q2-cr-induction-svl7

Question-scoped run. The scope spine is `question.json::in_scope`, **not**
`profile.json::targetable_features[]`. Linked source case
`aml-mds-related-rr-tp53-aberrant-hla-pending-x7q2-rerun2` (published, COMPLETE)
is cited rather than re-researched; its 47 trial rows and 36 clinical-evidence
rows were reference-verified there. Registry status was re-verified live for
every NCT carried forward.

## Endpoint being screened for
ELN 2022 **CR**. CRi / CRh / MLFS / composite CR (CRc) / ORR are recorded only
when labelled as what they are, with the denominator. A composite rate is never
written into a row as a CR rate. Because of the right-thigh myeloid sarcoma,
"remission" for this question means marrow CR **plus** extramedullary response;
every marrow-only figure is flagged as such.

## Patient axes that gate eligibility
- ~85% marrow blasts; peripheral blasts 58→82% — blast caps and WBC caps bite.
- Prior matched-sibling allo-HCT ~2020 — excludes some protocols, required by others.
- Refractory to FLAG-IDA + venetoclax — narrows re-treatment and excludes
  venetoclax-refractory and prior-HiDAC arms; makes her *secondary refractory*.
- Complex adverse karyotype (del(5q), del(7q), MECOM gain, KMT2A amplification).
- TP53 aberrant, unresolved in both directions — one trial excludes on TP53 history.
- Extramedullary myeloid sarcoma — an exclusion in some protocols, an inclusion in one.
- ECOG 1; organ function undocumented (creatinine / bilirubin / LVEF / DLCO gates unverified).
- CD33+ / CD123+ by qualitative flow only; no antigen density.

## Axis A — remission-directed regimens deliverable as next line
Intensive salvage on equal footing with targeted options, because an endpoint
question is not bound to the feature list: CLAG-M, CLAG, MEC, HAM / high-dose
cytarabine backbones, FLAG-based re-treatment, CPX-351 combinations, HMA +
venetoclax variants, uproleselan + chemotherapy. Registry and PubMed, R/R AML,
CR-bearing.

## Axis B — CD33- and CD123-directed agents with reported CR rates
CD33: gemtuzumab ozogamicin (fractionated, MyloFrance schedule), CLAG-GO,
lintuzumab-Ac225 (± CLAG-M, ± venetoclax). CD123: tagraxofusp, pivekimab
sunirine, flotetuzumab (discontinued, kept for the TP53-abnormal CR signal).
Alias-expanded: `gemtuzumab ozogamicin` / `Mylotarg` / `CMA-676`;
`lintuzumab-Ac225` / `Actimab-A` / `225Ac-lintuzumab` / `HuM195`;
`tagraxofusp` / `SL-401` / `Elzonris`; `pivekimab sunirine` / `IMGN632`;
`flotetuzumab` / `MGD006` / `S80880`.

## Axis C — transplant-integrated remission platforms
Remission produced by the procedure: FLAMSA-type sequential conditioning
(FLAMSA-RIC, FLAMSA-treosulfan), the US analogue DEC-FLAG-Ida/RIC
(NCT06928662), CLAG-M or FLAG-Ida into RIC allo (NCT04375631), and targeted
radioimmunoconditioning (Iomab-B / 131I-apamistamab; SIERRA and NCT07157514).
Plus the randomised test of whether induction before transplant is needed at all
(ASAP, NCT02461537). Remission data in scope; survival data are not this
question's endpoint.

## Axis D — CR evidence graded by population match
Dedicated searches on her three hardest axes: post-allo-HCT relapse,
post-venetoclax failure, TP53-aberrant R/R AML. Also blast-burden effect on CR
probability, since ~85% marrow blasts is the axis most published cohorts show a
gradient on.

## Axis E — extramedullary response
Whether any source assessed extramedullary disease at response; myeloid sarcoma
response to systemic regimens; registry sweep for protocols that enrol or
stratify on extramedullary involvement. Local radiotherapy in scope only as an
adjunct, never as the answer.

## Registry eligibility-gate sweep (Step 1.75 analogue)
The shared gate here is not an HLA restriction but **post-allo-HCT relapse at
high blast burden**. ClinicalTrials.gov v2 API swept on
`query.cond=Acute Myeloid Leukemia` × `{relapse after allogeneic
hematopoietic cell transplantation salvage, myeloid sarcoma extramedullary}`
with `filter.overallStatus=RECRUITING|NOT_YET_RECRUITING`, plus per-regimen
term queries for CLAG-M, MEC, lintuzumab-Ac225. Tokenisation variants run with
and without hyphens (`CLAG-M` / `CLAG M`, `Ac-225` / `Ac225` / `225Ac`).

## Out of bounds
The source case's ranking (not re-opened, not amended). Durability, RFS, OS, and
everything after CR. Sequencing consequences. The gating workup. Supportive or
bridging measures with no remission intent (hydroxyurea, leukapheresis).
Menin inhibitors: KMT2A *amplification* is not a rearrangement and she is
NPM1-wild-type, so revumenib / ziftomenib have no CR evidence in a population
matched to her; the source case's standard-of-care screen already carries them
flagged target-absent, and they are not re-routed here.
