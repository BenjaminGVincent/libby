# Search spec — aml-mds-related-rr-tp53-aberrant-hla-pending-x7q2-rerun2

Written by `trial_screener`, 2026-08. Fresh re-run.

## Patient handles this screen is scoped to

From `profile.json::targetable_features[]` — nothing else enters `trials.jsonl`.

1. **CD123-positive blasts** (flow, qualitative; density pending)
2. **CD33-positive blasts** (flow, qualitative; density pending)
3. **TP53 aberration, Y220C-contingent** (2019 mutant / 2026 limited-panel negative; unresolved)
4. **HLA-restricted immunotherapy handles** — HA-1/HA-2 miHA TCR-T, WT1, PRAME.
   This is a *restriction / platform* feature (HLA-A\*02:01 and, secondarily,
   A\*24:02), so per the scope rule any agent gated on that same restriction is
   on-axis whether or not its specific peptide was nominated.
5. **Allograft / second-transplant platform (HCT2)** — also a platform feature:
   conditioning regimens, RIC/FLAMSA sequencing, targeted radioimmunotherapy
   conditioning, and donor lymphocyte infusion all ride it.

## Explicitly out of scope

Standard R/R AML care whose mechanism does not touch a listed feature. In
particular **menin inhibitors (revumenib, ziftomenib) are dropped**: they act on
KMT2A-*rearranged* / NPM1-mutant disease, and this patient is NPM1-untested-but-
unreported with KMT2A **amplification**, which is not the menin-dependent lesion.
Approved for AML is not the same as acting on a stated feature. If they belong
anywhere, they belong to `standard_of_care_screener` flagged "target absent".

## Axes

### A. Tumor type + line + biomarker
R/R AML-MR, post-allo-HCT relapse, ECOG 1, prior FLAG-IDA + venetoclax,
extramedullary myeloid sarcoma, blasts 58–82%.

### B. Biomarker / target alone — basket and pan-tumor
- `HLA-A*02:01` × {`A*02:01`, `A*0201`, `HLA A2`, `A2-restricted`, `HLA-A2`}
- HA-1 / HA-2 / minor histocompatibility antigen / miHA
- WT1; PRAME; multi-antigen TAA-T
- CD123 / IL3RA; CD33 / SIGLEC-3
- TP53 Y220C (pan-tumor and myeloid-restricted)

### C. Drug-name / mechanism, cross-tumor
Alias-expanded per drug, hyphen and space variants, run against the registry
independent of indication. Roster in `pipeline.md`.

### D. Eligibility-gate sweep (Step 1.75)
Registry queried by the *gate* rather than the drug:
`query.cond=AML|MDS|leukemia` × `query.term=HLA-A*02:01 | HLA-A2 | minor
histocompatibility | donor-derived | after allogeneic transplant | second
transplant | donor lymphocyte infusion`. Enumerated to exhaustion, not
relevance-ranked. This is what surfaces novel-antigen agents riding the
patient's restriction (e.g. CBX-250 / CG1).

### E. Legacy / discontinued pass
`<drug> discontinued | failed | withdrawn | terminated` for every roster agent,
so the board sees Rova-T-style precedent (flotetuzumab, vibecotamab, NTLA-5001,
BPX-701, MDG1011, MDG1021, eprenetapopt, SGN-CD123A, UCART123).

## Sources
ClinicalTrials.gov v2 API (via the `beta-ut` host — the production host is
unreachable from this sandbox; same API version 2.0.5, data timestamp
2026-08), NCBI E-utilities (PubMed/PMC), Europe PMC and ASH/ASCO/AACR abstracts,
web search for regulatory events.

## Fit rules applied for this case

Eligibility realities recorded as fit detail, never used to omit a trial:
- **HLA-A\*02:01 unknown** — every peptide-HLA-restricted product is hard-gated
  on it. Ceiling on `fit_to_case` is `partial` until typing is retrieved.
- **HA-1/HA-2 genotype unknown for both patient and sibling donor**, and the
  HA-directed products need a *directional mismatch* (recipient HA-1+ / donor
  HA-1−). HLA-identical siblings frequently match at HA-1 too, so this is a real
  coin-flip, not a formality.
- **Blast burden 58–82%** breaches blast caps in several post-transplant and MRD-
  directed protocols outright.
- **Extramedullary myeloid sarcoma** is an exclusion or an unaddressed gap in
  several marrow-endpoint protocols.
- **Prior allo-HCT** and **prior venetoclax** exclude several arms; conversely
  prior allo-HCT is a *requirement* for the miHA and DLI trials.
- **Planned/prospective HCT** is required by the TSCAN-001, BSB-1001 and
  apamistamab-conditioning designs — these are consolidation platforms, not
  salvage for active refractory disease.

`toxicity_flags` will be empty for every row: `preferences.json::toxicity_vetoes`
is `[]` and `modality_constraints` is `[]`.
