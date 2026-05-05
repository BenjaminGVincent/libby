# PHI policy

Libby is an experimental decision-support tool. It receives sensitive patient
information at intake and publishes derived recommendations to a public site.
This page documents the boundary between the two.

## The rule

> Raw patient data lives only under `case/<slug>/`. That directory is
> **gitignored**. Nothing under it ever enters version control or the
> published site. The only path data takes into the committable tree is
> through `scripts/promote_profile.py`, which validates a scrubbed
> `profile.json` and `preferences.json` against the JSON schema and a
> regex-based PHI scanner before copying.

## Three defensive layers

### 1. `.gitignore`

`case/` is excluded outright, plus `*.dcm`, `*MRN*`, `*phi*`, `*PHI*`, `*.patient.*`
as belt-and-suspenders for misplaced files.

### 2. Pre-commit hook

`.githooks/pre-commit` runs `scripts/scan_for_phi.py --mode=staged`. It refuses
any commit that:

- Stages a path under `case/`, **or**
- Includes a staged text file (`*.md`, `*.json`, `*.jsonl`, `*.yaml`, `*.txt`,
  `*.csv`, `*.tsv`) that matches any pattern in the PHI blocklist.

To install the hook on a fresh checkout:

```bash
bash scripts/install_hooks.sh
```

### 3. CI scanner

`.github/workflows/phi-scan.yml` re-runs the scanner against the entire tracked
tree on every push and on every PR. It is required-to-pass before the
`pages.yml` deploy job runs.

## What the scanner catches

<!-- The example shapes in the table below intentionally describe PHI shapes
     for documentation purposes; each row carries a phi-scan: ignore marker
     so the scanner does not refuse this very policy page. -->

| Pattern | Example shape |
|---|---|
| `ssn` | `123-45-6789` <!-- phi-scan: ignore --> |
| `us_phone` | `(415) 555-0199`, `415-555-0199`, `+1 415 555 0199` <!-- phi-scan: ignore --> |
| `email` | `name@hospital.org` <!-- phi-scan: ignore --> |
| `mrn_label` | `MRN: 12345678`, `Medical Record Number 12345678` <!-- phi-scan: ignore --> |
| `iso_date_full` | `2024-03-15` (day precision) <!-- phi-scan: ignore --> |
| `us_date` | `3/15/2024` (day precision) <!-- phi-scan: ignore --> |
| `dob_label` | `DOB`, `D.O.B.`, `Date of Birth` <!-- phi-scan: ignore --> |
| `all_caps_name` | `SMITH, JOHN` <!-- phi-scan: ignore --> |
| `patient_label` | `Patient name:` <!-- phi-scan: ignore --> |

To override a single line that is a known false positive, append
`# phi-scan: ignore` to the line.

## What the scanner does **not** catch

The scanner is shape-based. It will miss:

- A clinician's surname embedded in a free-text rationale.
- A hospital or clinic name dropped into a quoted note.
- An identifying combination — e.g. age 72 + a rare-disease subtype + a small
  geography — that re-identifies a single individual.

The **scrub agent** (`/intake`) is the real defense. The scanner is a tripwire.

For the first cases you run, manually review the rendered MD pages
(`mkdocs serve` locally) before pushing. If you find a false negative, expand
the pattern set in `scripts/scan_for_phi.py`.

## Slug guidance

The case slug appears in URLs (`https://benjamingvincent.github.io/libby/cases/<slug>/`).
The slug must be a clinical-descriptor phrase — e.g.
`nsclc-egfr-l858r-post-osi-a4f2` — never patient initials, names, or dates. The
random suffix (`-a4f2`) disambiguates without leaking. The `intake` agent
proposes the slug and refuses anything matching initials- or birthdate-shaped patterns.

For ultra-rare-population cases, slug + clinical detail can still be
de-anonymizing. Set `private: true` in `profile.json` to suppress generation of
public `docs/cases/<slug>/` pages — the case stays local-only.

## `noindex` on case pages

Every rendered case page emits a `<meta name="robots" content="noindex">` tag
so search engines do not index case URLs. Pages remain accessible by direct
link (shareable with a patient and their care team) but should not surface in
search.

## Reporting a leak

If you discover PHI in a published page, treat as a P0:

1. Force-push a removal commit to `main`.
2. Re-run `mkdocs gh-deploy --force` to overwrite the published artifact.
3. Open a GitHub issue describing the pattern that slipped through, so the
   scanner blocklist can be extended.
