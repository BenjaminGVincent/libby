<meta name="robots" content="noindex">

# `demo-nsclc-egfr-l858r-post-osi-d3m0`

!!! danger disclaimer "Decision support, not medical advice"
    Libby is experimental. The recommendations on this page have **not** been
    reviewed by a clinician treating this patient. Do not act on this page
    without consulting a qualified oncologist. This is a synthetic
    demonstration case; the patient profile is fictional.

<!-- libby:downloads:begin -->

## Downloads

- [Clinician PDF report](demo-nsclc-egfr-l858r-post-osi-d3m0-libby-report.pdf) — ranked recommendations + evidence + sources
- [Patient/caregiver PDF](demo-nsclc-egfr-l858r-post-osi-d3m0-plain-language.pdf) — plain-language summary
- [Self-contained HTML](demo-nsclc-egfr-l858r-post-osi-d3m0-recommendations.html) — recommendations table that opens offline

<!-- libby:downloads:end -->
## Profile snapshot (scrubbed)

- **Primary site / histology:** lung adenocarcinoma
- **Stage:** IV
- **Performance status:** ECOG 1
- **Age band:** 60-69
- **Biomarkers:** EGFR L858R (present); EGFR T790M (absent); MET amplification (GCN 8.2); PD-L1 TPS 10%
- **Prior therapy:** 1L osimertinib, PR x 22 months
- **Targetable features:** EGFR L858R; MET amplification (likely on-target resistance)

## Preferences

- **Efficacy/toxicity weight:** 0.55 (slight efficacy lean)
- **Toxicity vetoes:** severe neuropathy, cardiotoxicity, alopecia
- **Modality:** oral preferred; no inpatient infusion; minimize IV chair time
- **Free text:** working artist — manual dexterity in hands matters more than typical
- **Trials preferred:** yes

## Recommendations summary

| Rank | Status | Intervention | Endorsed | Dissent | Veto |
| ---- | ------ | ------------ | -------- | ------- | ---- |
| 1 | recommended | savolitinib + osimertinib (preferably on SAFFRON / SACHI) | risktaker, conservative, critic, advocate | — | — |
| 2 | considered with caveats | amivantamab + lazertinib | risktaker, concensusite | critic, advocate | conservative |
| 3 | considered with caveats | patritumab deruxtecan (HER3-DXd) | risktaker | — | — |

See [Recommendations](recommendations.md) for the full table with rationale and
open questions.

## Synthesis

The board converged on **savolitinib + osimertinib** as the rank-1
recommendation: four of five personas endorsed; the lone qualifier (concensusite)
flagged a guideline-fit concern that resolves on trial enrollment, which is
itself preferred by the patient. The combination's evidence anchors are TATTON
expansion (PMID 32679432) and the SAFFRON / SACHI phase-3 program (NCT05261399).
All stated preference axes — oral, no IV burden, no severe neuropathy /
cardiotoxicity / alopecia — clear cleanly.

**Amivantamab + lazertinib** drew a toxicity veto from the conservative on
neuropathy and IV-burden grounds, with concurring dissent from the advocate on
preference grounds and the critic on evidence-quality grounds. Concensusite
endorsed on NCCN 2A alignment; risktaker endorsed on effect-size grounds. Per
PI rules a veto is never silently dropped — the option remains on the table
marked `considered_with_caveats` so the patient and clinician can see what was
considered. **Override of the conservative's veto is not recommended absent
failure of the rank-1 option.**

**Patritumab deruxtecan** was advanced only by the risktaker and triggers the
alopecia veto outright; surfaced for transparency only.

## Transparency artifacts

- [Trial table](trials.md) — 4 trials in the dossier
- [Evidence list](evidence.md) — clinical + pre-clinical
- [Tumor-board transcript](board.md) — 5 positions, 20 cross-critiques
- [Recommendations table](recommendations.md) — full ranked detail
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Demo case authored May 2026 with synthetic data for smoke-testing the
pipeline. No real patient information is represented.
