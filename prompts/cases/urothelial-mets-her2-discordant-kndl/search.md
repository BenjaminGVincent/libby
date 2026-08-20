# Search spec — urothelial-mets-her2-discordant-kndl

Run date: 2026-08. Autonomous run; spec written before the search and not
user-confirmed (no-questions mode), so it is recorded here for audit.

## Case anchors (from profile.json)

Metastatic urothelial carcinoma, IVB, currently oligometastatic nodal after SBRT
2026-06. ECOG 1. 1L enfortumab vedotin + pembrolizumab for ~25 months (CR; EV
stopped 2025-12 for CIPN), pembrolizumab maintenance to 2026-07 with nodal
progression and rising ctDNA. **No platinum chemotherapy has ever been given** —
this is the single most consequential eligibility fact in the case. Now on
trastuzumab deruxtecan (2 doses, severe nausea) plus an ongoing personalized
neoantigen mRNA vaccine series. HLA-A\*02:01 positive. TP53 R175H in plasma
ctDNA. Prostate second primary treated 2020, in remission.

## Axes searched

1. **Tumor + line + biomarker** — urothelial / bladder crossed with HER2,
   Nectin-4, TROP2, post-EV, post-checkpoint.
2. **Biomarker alone (basket / pan-tumor)** — HER2-expressing, Nectin-4-positive,
   TROP2, mesothelin-expressing, MUC1, PRAME, FAP-positive, TMB-H, ARID1A,
   TP53 R175H.
3. **Drug / mechanism name across tumor types** — per-agent alias-expanded
   queries from the pipeline roster in `pipeline.md`.
4. **Eligibility-gate sweep (Step 1.75)** — HLA-A\*02:01 as a restriction, run as
   `HLA-A*02:01`, `HLA-A2 positive`, `HLA A 02:01`, `A2-restricted`, `TCR-T solid
   tumor HLA`. This is what surfaced CLSP-1025 (GUARDIAN-101) and NT-175, the two
   TP53 R175H / HLA-A\*02:01-gated agents that no antigen-named search returns.
5. **Radiopharmaceutical isotope sweep** — `177Lu`, `225Ac`, `131I`, `90Y`,
   `211At`, `212Pb`, `227Th`, `68Ga` crossed with Nectin-4, HER2, FAP. This
   returned `[225Ac]Ac-AKY-1189` (Nectin-4 alpha-emitter, NCT07020117) and
   `[177Lu]Lu-FAP-2286` (LuMIERE). Imaging-only protocols (68Ga-NOTA-Nectin-4
   PET, Nectin-4 LMW PET probe, TROP2 NIR-II probe, 89Zr-s-C1 PET) were dropped
   under the radiopharmaceutical rule; the therapeutic and theranostic ones were
   kept as therapy rows.
6. **Modality cross-product** — each feature × {ADC, bispecific / T-cell engager,
   CAR-T, CAR-NK, TCR-T, radioligand, small molecule, vaccine, monoclonal
   antibody}.

## Registry and sources

ClinicalTrials.gov v2 API for discovery and for live verification of every NCT
written (status, arms, eligibility text read per row). PubMed E-utilities for the
one publication citation (DESTINY-PanTumor02). Web search for agent-target
resolution where the registry record does not name the target (AVZO-103,
LY4052031 payload).

## Scope gate applied

A trial enters `trials.jsonl` only if its drug's mechanism acts on a
`targetable_features[]` entry, or rides the HLA-A\*02:01 restriction the patient
is gated through. Standard 2L+ urothelial care whose mechanism is unrelated to a
nominated feature stays out and belongs to the standard-of-care track.

## Deliberate exclusions

- **B7-H3 / CD276 agents** (ifinatamab deruxtecan NCT06330064 and class). B7-H3
  appears in `target_validation.jsonl` under its own feature key but is **not** a
  `profile.json::targetable_features[]` entry, so the mechanism-scope gate
  excludes it. If a B7-H3 IHC comes back positive and the profile is amended,
  this is the first re-search to run.
- **FGFR3 agents** are admitted only through the one row that also carries HER2
  (FORAGER-1 cohort B7), because FGFR3 status is unknown and appears in the
  profile only inside the ARID1A entry's rationale as a retrieval gap.
- **GB-4362** (NCT07484022), an anti-MMAE neutralizing antibody given with EV.
  Its target is the payload, not Nectin-4, so it fails the mechanism gate despite
  being the most neuropathy-relevant agent in the urothelial registry.
- **MAGE-A4 agents** (CDR404, afami-cel class) — HLA gate matches, but tumor
  MAGE-A4 expression tested negative in 2024-06. Foreclosed by assay.
- **MSK-TCR5** (NCT07638371) requires HLA-A\*11:01 and RAS G12D. Neither applies.
- **Imaging-only** protocols per the radiopharmaceutical rule, listed above.
