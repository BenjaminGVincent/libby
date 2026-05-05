# Libby

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental multi-agent framework for identifying candidate
    therapeutics for an individual cancer patient. It does not replace clinical
    judgment, a tumor board, or a conversation with a qualified oncologist.
    Output should always be reviewed by a clinician before any care decision.

A multi-agent framework that takes three inputs:

1. **Cancer features** the user thinks may be targetable.
2. **Patient clinical data** — kept local, never published. See [PHI policy](phi_policy.md).
3. **User preferences** — efficacy/toxicity tradeoff, toxicities to avoid, modality constraints.

Three research agents (`trial_screener`, `clinician`, `researcher`) compile a
dossier. Five board personas (`risktaker`, `conservative`, `critic`,
`concensusite`, `advocate`) post structured positions, then critique each
other. The `PI` agent synthesizes a ranked recommendation. The `translator`
agent produces a plain-language version.

See [Methods](methods.md) for the pipeline and [Cases](cases/index.md) for
published case pages.

## Output tracks per case

- **Clinician-grade** (`cases/<slug>/index.md`): structured recommendation
  table, links to trial table, evidence list, and board transcript.
- **Plain-language** (`cases/<slug>/plain_language.md`): patient/caregiver
  framing — absolute-risk language, no jargon, "questions to ask your oncologist."

## Status

Experimental. Built on the same MkDocs Material + GitHub Pages pattern as
[io-shieldbreak](https://github.com/BenjaminGVincent/io-shieldbreak).
