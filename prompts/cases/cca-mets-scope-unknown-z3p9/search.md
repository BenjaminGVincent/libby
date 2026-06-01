# Search spec — cca-mets-scope-unknown-z3p9

Scope-unknown metastatic cholangiocarcinoma. No molecular profiling supplied.
profile.json enumerates the recognized actionable CCA panel as candidate
targetable features, all flagged `ngs_pending`. Rank-1 gating workup is
comprehensive genomic profiling itself (see target_validation.jsonl). Every
therapeutic row below is conditional on a positive confirmatory test; that
prerequisite is recorded in each row's `inclusion_match_notes` and drives a
`partial` (not `strong`) fit cap, because no biomarker has been confirmed.

## Candidate targetable features → drug-class anchors

| Feature (untested) | Gating test | Anchor drugs |
|---|---|---|
| FGFR2 fusion/rearrangement | RNA fusion / DNA SV panel | pemigatinib, futibatinib, infigratinib, derazantinib, RLY-4008 (lirafugratinib), erdafitinib |
| IDH1 R132 | DNA hotspot (CGP) | ivosidenib |
| HER2 (ERBB2) amp/overexpr | IHC + reflex ISH / NGS CN | zanidatamab, trastuzumab deruxtecan, trastuzumab+pertuzumab, tucatinib+trastuzumab |
| BRAF V600E | NGS (VE1 IHC screen) | dabrafenib+trametinib |
| MSI-H / dMMR | MMR IHC / MSI-PCR / NGS | pembrolizumab, dostarlimab |
| high TMB (>=10 mut/Mb) | NGS TMB | pembrolizumab |
| NTRK1/2/3 fusion | RNA fusion panel | larotrectinib, entrectinib |
| RET fusion | RNA fusion panel | selpercatinib |
| KRAS G12C | DNA hotspot (CGP) | adagrasib, sotorasib |

## Three search axes (per contract Step 1)

(a) **Tumor type + line + biomarker.** "cholangiocarcinoma" / "biliary tract
    cancer" × each biomarker × 2L+, e.g. FGFR2 fusion CCA pemigatinib;
    HER2 biliary zanidatamab; IDH1 cholangiocarcinoma ivosidenib.
(b) **Biomarker / target alone (basket + pan-tumor).** Tumor-agnostic labels
    and baskets: BRAF V600E basket (ROAR), NTRK basket (larotrectinib NAVIGATE
    / entrectinib STARTRK), RET basket (LIBRETTO-001), dMMR/MSI-H basket
    (KEYNOTE-158), TMB-high basket (KEYNOTE-158 TMB cohort), HER2 pan-tumor
    (DESTINY-PanTumor02, MyPathway).
(c) **Drug-name / mechanism searches.** Each anchor drug as its own query with
    alias expansion (INN, pharma code, hyphen/space variants) against
    ClinicalTrials.gov v2 + PubMed.

## Sources
ClinicalTrials.gov v2 API (primary), PubMed E-utilities (trial pubs), PMC /
Europe PMC (OA full text), ASCO/ESMO abstracts for early-phase.

## Keep / drop
Keep only rows whose drug mechanism targets one of the candidate features.
Standard-of-care chemoimmunotherapy (gem/cis +/- durvalumab TOPAZ-1,
pembrolizumab KEYNOTE-966) is OUT of scope — mechanism not tied to a
targetable feature — UNLESS the immunotherapy arm is the vehicle for the
MSI-H/dMMR or TMB-high agnostic label (pembrolizumab), in which case it is
kept as a biomarker-gated checkpoint row.

All Keep rows here are `primary_indication_match` (CCA-enrolling) or
`basket_or_biomarker_match` (pan-tumor, accepts CCA via biomarker). Fit is
capped at `partial` until a confirmatory test returns positive.
