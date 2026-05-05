<meta name="robots" content="noindex">

# `osteosarcoma-mets-dll3-h7r2`

<!-- libby:downloads:begin -->

## Downloads

- [Clinician PDF report](osteosarcoma-mets-dll3-h7r2-libby-report.pdf) — ranked recommendations + evidence + sources
- [Patient/caregiver PDF](osteosarcoma-mets-dll3-h7r2-plain-language.pdf) — plain-language summary
- [Master manuscripts table (PDF)](osteosarcoma-mets-dll3-h7r2-manuscripts.pdf) — every paper considered — n, effect, variance, toxicities
- [Self-contained HTML](osteosarcoma-mets-dll3-h7r2-recommendations.html) — recommendations table that opens offline

<!-- libby:downloads:end -->

## Research question

In metastatic osteosarcoma after first-line MAP, what interventions could target DLL3 expression, gated on IHC confirmation?

## Patient profile (scrubbed)

- **Primary site / histology:** bone — osteosarcoma
- **Stage:** IV (metastatic)
- **Performance status (assumed):** ECOG 1
- **Age band (assumed):** 18-29 (typical osteosarcoma demographics; not user-supplied)
- **Sex:** unknown
- **Biomarkers:** **DLL3 — RNA only (`confirmation_status: rna_only`); IHC SP347 status unknown.** Decision-relevant resolution: ≥1% (preferably ≥25%) by IHC for DLL3-directed clinical trials.
- **Prior therapy (assumed):** MAP frontline; response not provided.

## Preferences

- **Efficacy/toxicity weight:** 0.85 (strong efficacy lean)
- **Toxicity vetoes:** none stated
- **Modality constraints:** none stated
- **Free text:** "accepts high-risk high-reward options"
- **Trials preferred:** yes

## Scope summary

7 trials, 5 clinical-evidence rows, 4 preclinical rows. Two ranked rows: a workup gate at rank 1 plus one biomarker-conditional therapeutic option at rank 2. Board agreement: full consensus (all five personas) on the workup; one persistent dissent (critic) on the conditional rank-2 trial. Standard 2L+ care for relapsed osteosarcoma (regorafenib, cabozantinib) lies outside this case's targetable-feature scope and is not enumerated here.

## Cross-cutting caveat (read first)

**The DLL3 RNA expression in user input does not establish membrane DLL3 protein. The DLL3 IHC SP347 test (rank 1) gates whether tarlatamab via NCT06788938 (rank 2) is on the table at all.** Every DLL3-directed therapy in current clinical use requires IHC protein-level confirmation; RNA expression is necessary but not sufficient.

- **Rank 2 (tarlatamab)** is conditional on DLL3 IHC ≥1% (preferably ≥25%). It is the only therapeutic option within scope of this case's targetable feature.
- **If IHC is negative:** rank 2 is foreclosed and this case has no within-scope recommendations. The targetable-feature pathway is closed; the patient and clinician should pursue standard 2L+ care for relapsed osteosarcoma through their normal care channel — that lies outside Libby's targetable-feature-driven scope here.
- **Workup logistics:** SP347 IHC is non-toxic, runs on archival tissue (no fresh biopsy required), takes 1–3 weeks, and costs almost nothing relative to a treatment cycle. Confirm assay availability at the treating institution.

## Intervention grouping

- **DLL3-directed BiTEs (biomarker-conditional):** tarlatamab via NCT06788938. Cross-tumor efficacy anchor: DeLLphi-301 ([PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218)) and DeLLphi-304 ([PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646)).

## Top interventions

### Rank 1. DLL3 IHC (SP347) on tumor — diagnostic gate

*Non-toxic. Resolves whether the DLL3-directed pathway is open. Required for trial NCT06788938.*

#### Evidence base

NCT06788938 enforces DLL3 IHC ≥25% (stage 1) or ≥1% (stage 2) for enrollment. The basket-trial design exists precisely because DLL3 RNA expression is not a sufficient enrollment biomarker. Mechanistic anchor: every DLL3-directed therapy in clinical development requires protein-level confirmation.

#### Likelihood of desired effect

The test resolves whether rank 2 is reachable. Non-toxic and cheap regardless of result.

#### Toxicity profile

- None. Lab test on tissue.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. No persona dissented or vetoed.

#### Practical considerations

Archival or fresh tumor; SP347 antibody assay availability at the treating institution should be confirmed. 1–3 week turnaround. The IHC is the precondition for every DLL3-directed action regardless of which therapy the patient ultimately pursues.

#### Why this rank

The IHC is the precondition for rank 2. The board treated it as the gate, not as a therapy.

#### Per-trial detail

| Test / trial | Efficacy context | Toxicity | Reference |
|---|---|---|---|
| DLL3 IHC SP347 (assay) | Gates enrollment in DLL3-directed therapy trials | None — diagnostic | [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) |

---

### Rank 2. Tarlatamab via NCT06788938

*Conditional on `dll3_ihc:positive`. Foreclosed if test is negative.*

*High-efficacy bispecific T-cell engager; preferences point exactly here when the trial is reachable; one persistent dissent on cross-tumor translation.*

#### Evidence base

NCT06788938 (single-arm phase 2 basket, Simon two-stage, n=29 planned) is the trial enrolling osteosarcoma at biomarker-positive resolution. The mechanistic case rests on cross-tumor evidence: DeLLphi-301 ([PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218); ORR 40%, n=220 SCLC) and the confirmatory DeLLphi-304 phase 3 ([PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646); OS HR 0.60, 95% CI 0.47–0.77, median OS 13.6 vs 8.3 mo). No published osteosarcoma data with tarlatamab exist.

#### Likelihood of desired effect

Assuming positive IHC, mechanism-fit is concordant. Whether SCLC's clinical effect transfers to osteosarcoma is the central scientific question this trial enrollment would answer. The user's preferences (efficacy lean 0.85, accepts high-risk-high-reward, prefers trials) point exactly here. **A negative IHC forecloses this rec entirely.**

#### Toxicity profile

- CRS in ~50% (mostly grade 1–2; grade ≥3 ~1% in SCLC)
- ICANS-like neurologic events ~10%
- Inpatient cycle-1 step-up dosing required for CRS mitigation
- Step-up dosing: 1 mg D1, 10 mg D8/D15, then 10 mg q2w (28-day cycles)

User has no toxicity vetoes; CRS and inpatient cycle-1 chair time are not flagged.

#### Counter-productive mechanisms / dissent

**The critic's dissent persists.** No published osteosarcoma data with tarlatamab; cross-tumor translation from SCLC is unproven; the trial's basket design exists to *test* this premise. The conservative's earlier toxicity veto (issued under the IHC-unconfirmed scenario) lifts on biomarker confirmation — its own rationale specified the veto was contingent on IHC. Concensusite's qualified-on-guideline-fit position upgrades to endorsement when the trial-enrollment principle is in play.

#### Practical considerations

- Trial open at NCT06788938 (recruiting). Slot availability at treating site should be confirmed.
- Trial enrollment is NCCN cat-1 for relapsed osteosarcoma irrespective of mechanism.
- Inpatient cycle-1 monitoring required.
- Off-guideline for osteosarcoma per indication; the trial provides the regulatory pathway.

#### Why this rank

The only DLL3-directed therapeutic option on the table, conditional on biomarker confirmation. Foreclosed entirely if IHC negative.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Tarlatamab — NCT06788938 DLL3-IHC-selected basket (osteosarcoma included), n=29 planned | ORR endpoint at 18 mo (primary); no osteosarcoma data yet | Per SCLC mechanism: CRS ~50%, ICANS ~10%, inpatient C1 | [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) |
| Tarlatamab — DeLLphi-301 SCLC (cross-tumor mechanism evidence), n=220 | ORR 40% (95% CI 29–52); mPFS 4.9 mo | CRS ~50% (G3+ ~1%); ICANS ~10%; G3+ TRAEs 30% | [PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218) |
| Tarlatamab — DeLLphi-304 SCLC (cross-tumor confirmatory), n=509 | OS HR 0.60 (95% CI 0.47–0.77), p<0.001; median OS 13.6 vs 8.3 mo | G3+ TRAEs 24% vs 53% chemo arm — favorable vs comparator | [PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646) |

## Classes examined but not ranked

- **Anti-PD-1 / PD-L1 monotherapy in osteosarcoma:** historically negative (SARC028 and successors); not DLL3-directed.
- **HER2-, GD2-, B7-H3-directed therapies:** not in the dossier for this case; no biomarker selection performed at intake.
- **MTP-PE (mifamurtide):** historical adjuvant data in newly diagnosed disease; not 2L+; not DLL3-directed.
- **Multi-kinase TKIs (regorafenib, cabozantinib):** standard 2L+ care for relapsed osteosarcoma per NCCN ([PMID 31013172](https://pubmed.ncbi.nlm.nih.gov/31013172), [PMID 30477937](https://pubmed.ncbi.nlm.nih.gov/30477937), [PMID 32078813](https://pubmed.ncbi.nlm.nih.gov/32078813)). They do not target DLL3 and lie outside this case's targetable-feature scope. Surfaced here for transparency only — they should be considered through the patient's normal care channel, not via Libby's targeted-feature ranking.

## Ranked prioritization

| Rank | Status | Intervention | Endorsed by | Dissent | Veto | Likelihood | Toxicity burden | Why this rank |
|---|---|---|---|---|---|---|---|---|
| 1 | recommended | DLL3 IHC (SP347) | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span> | — | — | Resolves rank 2 reachability | None | Gate; precondition for rank 2 |
| 2 | recommended | Tarlatamab via NCT06788938 (conditional on DLL3 IHC positive) | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span> | <span class="persona persona-critic">critic</span> | — | Mechanism unproven cross-tumor | CRS, ICANS, C1 inpatient | Only DLL3-directed option; preference fit |

## Caveats

- **Evidence base is small for the conditional trial.** NCT06788938 plans n=29 with no published efficacy data yet. The mechanistic basis is the cross-tumor SCLC evidence (DeLLphi-301 / 304), which is robust in SCLC but unproven in any other tumor type.
- **Biomarker dependency:** rank 2's eligibility assumes a binary IHC result. Indeterminate / weak-positive (1–24%) edge cases are not explicitly addressed; in practice, NCT06788938's stage-2 ≥1% threshold may permit enrollment.
- **What would change the ranking:**
    - A positive DLL3 IHC plus a head-to-head osteosarcoma cohort within the basket trial reading out would move tarlatamab from "mechanism unproven cross-tumor" to "evidence-supported" and tighten its rank-2 confidence.
    - A user toxicity veto on CRS / inpatient cycle-1 monitoring would foreclose tarlatamab even with positive IHC.
    - Slot unavailability at NCT06788938 sites would close the within-scope therapeutic pathway entirely; standard 2L+ care for the indication would be the patient's residual option (outside Libby's enumeration here).
- **Out-of-scope caveat:** standard 2L+ care for relapsed osteosarcoma (regorafenib's two-RCT base, cabozantinib's CABONE phase-2) was surfaced by the trial screener and reviewed by the board, but those drugs do not target the user's stated targetable feature (DLL3). They are not ranked on this page; pursue them through the treating team independent of Libby's targetable-feature ranking.

## Sources

**PubMed (PMID):**

- [37861218](https://pubmed.ncbi.nlm.nih.gov/37861218) — Ahn et al., DeLLphi-301, *NEJM* 2023
- [40454646](https://pubmed.ncbi.nlm.nih.gov/40454646) — Mountzios et al., DeLLphi-304, *NEJM* 2025
- [35983951](https://pubmed.ncbi.nlm.nih.gov/35983951) — DLL3 IHC reference (cited in workup row)

**ClinicalTrials.gov (NCT):**

- [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) — DLL3-IHC-selected basket including osteosarcoma (tarlatamab)
- [NCT05060016](https://clinicaltrials.gov/study/NCT05060016) — DeLLphi-301 (cross-tumor mechanism)
- [NCT05740566](https://clinicaltrials.gov/study/NCT05740566) — DeLLphi-304 (cross-tumor confirmatory)

## Transparency artifacts

- [Trial table](trials.md) — 7 rows, all 25 columns
- [Evidence list](evidence.md) — 5 clinical-evidence rows + 4 preclinical rows
- [Tumor-board transcript](board.md) — 5 positions, 20 cross-critiques
- [Recommendations table](recommendations.md) — full ranked detail with biomarker-conditional flag
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Authored May 2026. Inputs supplied: targetable feature ("DLL3 RNA expression"), clinical descriptor ("metastatic osteosarcoma"), preference summary ("accepts high-risk high-reward options"). Re-rendered when Libby's biomarker-confirmation contract narrowed: instead of emitting parallel positive/negative therapeutic rankings, the PI now flags the confirmatory test as the rank-1 workup and tags only biomarker-conditional recs with `:positive`. Negative-branch ranking is foreclosed via the cross-cutting caveat above. Standard 2L+ care for the indication is out of scope and not ranked here.

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
