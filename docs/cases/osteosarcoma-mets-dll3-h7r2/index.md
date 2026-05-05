<meta name="robots" content="noindex">

# `osteosarcoma-mets-dll3-h7r2`

!!! danger disclaimer "Decision support, not medical advice"
    Libby is experimental. The recommendations on this page have **not** been
    reviewed by a clinician treating this patient. Do not act on this page
    without consulting a qualified oncologist. The clinical inputs are
    sparse — many profile fields were inferred and are flagged as
    open questions.

## Profile snapshot (scrubbed)

- **Primary site / histology:** bone — osteosarcoma
- **Stage:** IV (metastatic)
- **Performance status (assumed):** ECOG 1
- **Age band (assumed):** 18-29 (typical osteosarcoma demographics; not user-supplied)
- **Sex:** unknown
- **Biomarkers:** DLL3 RNA expression (level not specified; **protein-level IHC status unknown**)
- **Prior therapy (assumed):** MAP frontline; response not provided

## Preferences

- **Efficacy/toxicity weight:** 0.85 (strong efficacy lean)
- **Toxicity vetoes:** none stated
- **Modality constraints:** none stated
- **Free text:** "accepts high-risk high-reward options"
- **Trials preferred:** yes

## The DLL3 RNA→protein gap (this drives the ranking)

Every DLL3-directed therapy in clinical use today — tarlatamab (DLL3×CD3 BiTE),
the discontinued rovalpituzumab tesirine (DLL3 ADC), and the emerging
DLL3-CAR-T constructs — gates eligibility on **IHC protein expression**, not
RNA. The user's input identifies DLL3 RNA expression as a targetable feature;
the dossier finds no published evidence that osteosarcoma DLL3 RNA reliably
indicates membrane-localized DLL3 protein. NCT06788938 (the open tarlatamab
basket trial accepting non-SCLC tumors) requires SP347 IHC at ≥25% (stage 1)
or ≥1% (stage 2). Until that IHC is run, the high-upside DLL3-targeted
pathway cannot be triaged.

## Recommendations summary

| Rank | Status | Intervention | Endorsed | Dissent | Veto |
| ---- | ------ | ------------ | -------- | ------- | ---- |
| 1 | recommended | DLL3 IHC (SP347) workup — gate for #3 | risktaker, conservative, critic, concensusite, advocate | — | — |
| 2 | recommended | regorafenib | all 5 (rank-1 of conservative, concensusite, critic) | advocate (on rank, not drug) | — |
| 3 | considered with caveats | tarlatamab via NCT06788938 — **contingent on DLL3 IHC ≥1%** | risktaker, advocate | critic | conservative (lifts on IHC) |
| 4 | recommended | cabozantinib | all 5 | — | — |

See [Recommendations](recommendations.md) for the full table with rationale and
open questions.

## Synthesis

The board converged on **DLL3 IHC** as a non-negotiable first step — five
personas, no dissent. RNA expression alone does not establish whether DLL3 is
on the cell surface at the density that BiTE / ADC therapies require, and the
trial that would accept this case (NCT06788938) enforces an IHC threshold
exactly because of this.

Conditional on the IHC result, two pathways open:

- **If DLL3 IHC ≥1% (preferably ≥25%):** tarlatamab via NCT06788938 becomes
  a defensible rank-1 contingent option. The conservative's toxicity veto
  was issued specifically against treatment-without-IHC and lifts on
  confirmation. Two personas (risktaker, advocate) actively championed this
  pathway; the user's stated preferences (high-risk-high-reward, prefers
  trials) point here. The critic's evidence-quality dissent remains relevant
  even with IHC: there are no published osteosarcoma data with tarlatamab,
  and translatability from SCLC is unestablished. The PI did **not** override
  the veto — the contingent framing is what survives both objections.

- **If DLL3 IHC negative or while waiting:** regorafenib is the
  evidence-anchored backbone. Two replicating phase-2 RCTs (SARC024 +
  REGOBONE) show a real PFS signal in metastatic osteosarcoma. Universal
  endorsement across personas. The advocate dissented on its placement as
  rank-1 by other personas, but the dissent is on rank, not on the drug —
  honored by surfacing tarlatamab as the contingent rank-3 option.

**Cabozantinib** is the consensus backup with single-arm phase-2 evidence
(CABONE, ORR 11.9%, 6-mo non-progression 33%). Universally endorsed but
nobody's rank-1 — appropriate for second-line-after-regorafenib or
contraindication-driven selection.

## What was NOT confirmed

The user-supplied "DLL3 RNA expression" was not converted into actionable
biomarker status. The board's strongest single signal — heard from all five
personas — is that this conversion (RNA → IHC protein) is the next step in
care planning. Without it, ranking the DLL3-directed pathway is hypothesis
generation, not therapeutic selection.

## Transparency artifacts

- [Trial table](trials.md) — 5 trials in the dossier
- [Evidence list](evidence.md) — 5 clinical-evidence rows + 4 preclinical rows
- [Tumor-board transcript](board.md) — 5 positions, 20 cross-critiques
- [Recommendations table](recommendations.md) — full ranked detail
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Authored May 2026. Inputs supplied: targetable feature ("DLL3 RNA expression"),
clinical descriptor ("metastatic osteosarcoma"), preference summary ("accepts
high-risk high-reward options"). Profile fields beyond those were inferred —
flagged in the **Open questions** column of each recommendation row.
