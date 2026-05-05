# Libby

> **Decision support, not medical advice.** Libby is an experimental multi-agent
> framework. It does not replace clinical judgment, a tumor board, or a
> conversation with your oncologist. Output should always be reviewed by a
> qualified clinician before any care decision.

A multi-agent framework that helps identify candidate therapeutics for an
individual cancer patient. Inputs:

1. **Cancer features** the user thinks may be targetable (gene/variant/pathway/biomarker).
2. **Patient clinical data** — stays local, never committed (see [PHI policy](docs/phi_policy.md)).
3. **User preferences** — efficacy/toxicity tradeoff, toxicities to avoid, modality constraints.

Outputs (per case, published at `https://benjamingvincent.github.io/libby/cases/<slug>/`):

- A trial table of relevant clinical trials with case-fit and toxicity flags.
- Reference lists from the clinical and pre-clinical literature.
- A virtual tumor-board transcript (5 personas debate; cross-critique pass).
- A ranked recommendation table with risks and benefits, in two tracks:
  - `index.md` — clinician-grade.
  - `plain_language.md` — patient/caregiver track.

## Architecture

Mirrors `pirl-unc/io-shieldbreak`'s pattern (per-slug isolation, append-only
JSONL, MkDocs Material + GH Pages auto-deploy, manually-invoked agents that own
specific files), with two additions:

- **PHI gate.** Raw patient data lives only under `case/` (gitignored). Two-stage
  scrub (`intake` agent → `scripts/promote_profile.py`) is the only path data
  takes into committed territory. Pre-commit hook + CI workflow defend the
  boundary.
- **Virtual tumor board.** Five persona agents (`risktaker`, `conservative`,
  `critic`, `concensusite`, `advocate`) post structured positions, then critique
  each other's picks. The `PI` agent synthesizes a ranked recommendation
  preserving `veto` flags. A `translator` agent produces the plain-language track.

See [docs/methods.md](docs/methods.md) for the full pipeline.

## Quickstart

```bash
# Install hooks (one-time)
bash scripts/install_hooks.sh

# Set up a case (PHI stays local under case/)
mkdir -p case/<slug>/clinical
cp /path/to/patient/files case/<slug>/clinical/

# Run the agent pipeline (manual invocation)
/intake <slug>
python3 scripts/promote_profile.py <slug>
/trial_screener <slug>
/clinician <slug>
/researcher <slug>
/risktaker <slug> --round 1
/conservative <slug> --round 1
/critic <slug> --round 1
/concensusite <slug> --round 1
/advocate <slug> --round 1
/risktaker <slug> --round 2
/conservative <slug> --round 2
/critic <slug> --round 2
/concensusite <slug> --round 2
/advocate <slug> --round 2
/PI <slug>
/translator <slug>

# Render and publish
bash scripts/run_case.sh <slug>
git add data/cases/<slug>/ docs/cases/<slug>/   # NEVER `git add -A` — case/ would slip in
git commit -m "case <slug>: initial run"
git push
```

## License

TBD.
