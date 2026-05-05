<meta name="robots" content="noindex">

# `osteosarcoma-mets-dll3-h7r2`

!!! danger disclaimer "Decision support, not medical advice"
    Libby is experimental. The recommendations on this page have **not** been
    reviewed by a clinician treating this patient. Do not act on this page
    without consulting a qualified oncologist. Several profile fields were
    inferred (sparse user input) and are flagged as open questions.

<!-- libby:downloads:begin -->

## Downloads

- [Clinician PDF report](osteosarcoma-mets-dll3-h7r2-libby-report.pdf) — ranked recommendations + evidence + sources
- [Patient/caregiver PDF](osteosarcoma-mets-dll3-h7r2-plain-language.pdf) — plain-language summary
- [Self-contained HTML](osteosarcoma-mets-dll3-h7r2-recommendations.html) — recommendations table that opens offline

<!-- libby:downloads:end -->
## Profile snapshot (scrubbed)

- **Primary site / histology:** bone — osteosarcoma
- **Stage:** IV (metastatic)
- **Performance status (assumed):** ECOG 1
- **Age band (assumed):** 18-29 (typical osteosarcoma demographics; not user-supplied)
- **Sex:** unknown
- **Biomarkers:** **DLL3 — RNA only (`confirmation_status: rna_only`); IHC SP347 status unknown.** Decision-relevant resolution: ≥1% (preferably ≥25%) by IHC for DLL3-directed clinical trials.
- **Prior therapy (assumed):** MAP frontline; response not provided

## Preferences

- **Efficacy/toxicity weight:** 0.85 (strong efficacy lean)
- **Toxicity vetoes:** none stated
- **Modality constraints:** none stated
- **Free text:** "accepts high-risk high-reward options"
- **Trials preferred:** yes

## The scenario fork

Because DLL3 is `rna_only` and DLL3-directed therapies require IHC protein
confirmation, the PI emits **two parallel ranked tracks** below — the
recommendations the user can plan against under each branch of the IHC
result. The single shared first action is the IHC test itself.

## Shared first step (applies to every scenario)

| Rank | Status | Action | Endorsed |
| ---- | ------ | ------ | -------- |
| 1 | recommended | **DLL3 IHC (SP347) on tumor** — gates branch selection | all 5 personas |

The IHC is non-toxic, takes 1–3 weeks, and is required for trial NCT06788938
regardless of which branch the result places the patient in.

## Path A — if DLL3 IHC ≥1% (preferably ≥25%)

| Rank | Status | Intervention | Endorsed | Dissent | Veto |
| ---- | ------ | ------------ | -------- | ------- | ---- |
| 1 | recommended | **tarlatamab via NCT06788938** | risktaker, advocate, conservative, concensusite | critic | — |
| 2 | recommended | regorafenib (off-trial backbone) | all 5 | — | — |
| 3 | recommended | cabozantinib (alternative) | all 5 | — | — |

In the positive scenario, the **conservative's earlier toxicity veto on
tarlatamab lifts** — its own comment specified the veto was conditional on
IHC confirmation. Concensusite's qualified-on-guideline-fit critique upgrades
to endorsement once the trial-enrollment principle and biomarker-fit principle
align. Risktaker and advocate continue to endorse from round 1. The critic's
**evidence-quality dissent persists** — there are no published osteosarcoma
data with tarlatamab; cross-tumor translation from SCLC remains unproven and
is the load-bearing scientific question this trial enrollment would answer.

The user's stated preferences (high-risk-high-reward + prefers_trials) point
exactly here.

## Path B — if DLL3 IHC negative or below threshold

| Rank | Status | Intervention | Endorsed | Dissent | Veto |
| ---- | ------ | ------------ | -------- | ------- | ---- |
| 1 | recommended | **regorafenib** | all 5 | — | — |
| 2 | recommended | cabozantinib | all 5 | — | — |
| 3 | considered with caveats | non-DLL3 trial search (mechanism-agnostic) | risktaker, advocate | — | — |

In the negative scenario, the tarlatamab pathway is foreclosed. The advocate's
prior rank-disagreement on regorafenib (which was a rank-issue, not a
drug-issue) goes away because the alternative they were championing is no
longer available. Regorafenib's two-RCT evidence base ([Davis 2019 SARC024](https://pubmed.ncbi.nlm.nih.gov/31013172),
[Duffaud 2019 REGOBONE](https://pubmed.ncbi.nlm.nih.gov/30477937)) is the
highest-utility option remaining. The third row honors the user's
prefers_trials preference even with the DLL3 pathway closed — a referral to
an academic sarcoma center for a fresh trial search is the residual high-EV
move.

## What was NOT confirmed

The user-supplied "DLL3 RNA expression" was not converted into actionable
biomarker status. The board's strongest single signal — heard from all five
personas — is that this conversion (RNA → IHC protein) is the next step in
care planning. The two ranked tracks above let the user plan for both
results in parallel rather than serially.

## Transparency artifacts

- [Trial table](trials.md) — 5 trials in the dossier
- [Evidence list](evidence.md) — 5 clinical-evidence rows + 4 preclinical rows
- [Tumor-board transcript](board.md) — 5 positions, 20 cross-critiques
- [Recommendations table](recommendations.md) — full ranked detail with scenario branches
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Authored May 2026. Inputs supplied: targetable feature ("DLL3 RNA expression"),
clinical descriptor ("metastatic osteosarcoma"), preference summary ("accepts
high-risk high-reward options"). Re-run after Libby gained scenario-branching
support for non-confirmed biomarkers.
