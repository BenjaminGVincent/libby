# Trial-screener search spec — pdac-recurrent-cldn18-2-kras-g12r-tp53-y220c-p25m

Run date: 2026-08. Task direction from the launching agent; leads seeded by
target_validator. Patient context: recurrent PDAC (new pancreatic body mass
July 2026, likely vascular invasion, unbiopsied and unsequenced), ECOG 0,
prior mFOLFIRINOX x6 neoadjuvant + FOLFIRINOX x4 adjuvant (10 total cycles,
neuropathy ungraded), recurrence ~4 months after adjuvant. Travel acceptable,
no geography band, no toxicity vetoes, prefers trials.

## Axes

### Axis A — tumor type + line + biomarker
- "pancreatic" + CLDN18.2 (recruiting / not-yet-recruiting, any phase)
- "pancreatic" + KRAS G12R / pan-RAS / RAS(ON)
- "pancreatic" + TP53 Y220C
- second-line PDAC trials of feature-targeting drugs (post-FOLFIRINOX
  eligibility language captured per protocol)

### Axis B — biomarker / target alone (baskets, pan-tumor)
- CLDN18.2-positive solid tumors (each protocol's own IHC cutoff recorded;
  patient is 2+/3+ in 60% on the archival primary — clears >=40% CAR-T-style
  cutoffs, fails the >=75% zolbetuximab CDx cutoff)
- TP53 Y220C solid-tumor baskets (PYNNACLE and any other Y220C reactivator)
- KRAS codon 12 baskets that include G12R (pan-RAS(ON), pan-KRAS,
  mutant-KRAS vaccines whose peptide pools include G12R). G12C- and
  G12D-selective agents are allele-mismatched and are excluded, explicitly.
- KMT2C / COMPASS-complex basket sweep (expected empty; a gap is a finding)
- MSS / TMB-low: checkpoint-monotherapy baskets recorded as
  excluded-on-biomarker, not omitted silently.

### Axis C — drug-name / mechanism (alias-expanded, per Step 1.5 roster)
Per-drug ClinicalTrials.gov queries for every roster agent, each alias with
and without hyphens/spaces. Roster in pipeline.md alongside this file.
Modality cross-product for CLDN18.2: mAb, CAR-T, CD3 bispecific, 4-1BB
bispecific, CD47 bispecific, ADC, radioligand, vaccine. For KRAS G12R:
small molecule (pan-RAS(ON)/pan-KRAS), vaccine, TCR-T/TIL. For TP53 Y220C:
small-molecule reactivators.

### Adjacent-antigen rows requested by the launching agent
Mesothelin- and TROP2-directed agents enrolling PDAC. Neither antigen is a
nominated targetable feature and neither has been stained in this patient, so
these enter only as expression-unmeasured, fit weak/partial rows tied to the
pending recurrence-biopsy IHC bundle (which already lists MSLN and TROP2).
Kept to the few programs actually enrolling PDAC; not a full-pipeline sweep.

## Eligibility realities to encode as fit detail (not omission)
- CLDN18.2 60% at 2+/3+: screen against each protocol's own cutoff; record it.
- KRAS allele check on every RAS row: G12R must be covered explicitly.
- MSS / TMB 0.83: checkpoint rows are excluded-on-biomarker.
- Recurrence unbiopsied: record which trials need fresh/contemporaneous tissue.
- 10 prior FOLFIRINOX cycles; neuropathy ungraded (grade >=2 is a common
  exclusion); prior-line definitions vary — record per protocol.
- Likely vascular invasion: bears on measurability and biopsy access.

## Sources
ClinicalTrials.gov v2 API (primary; live status verbatim), PubMed E-utilities,
sponsor releases / meeting abstracts via web search for development-status
calls (discontinuations, approvals), NIH Inxight for alias resolution.

## Result cap
Roster exceeds 10 agents, so the 30-row cap is lifted; per-drug search runs
to exhaustion within the mechanism scope above.
