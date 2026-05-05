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

7 trials, 5 clinical-evidence rows, 4 preclinical rows. Four ranked rows: one workup gate at rank 1 plus three therapeutic options (one biomarker-conditional at rank 2, two biomarker-independent at ranks 3 and 4). Board agreement: full consensus (all five personas) on the workup, regorafenib, and cabozantinib; one persistent dissent (critic) on the conditional rank-2 trial.

## Cross-cutting caveat (read first)

**The DLL3 RNA expression in user input does not establish membrane DLL3 protein. The DLL3 IHC SP347 test (rank 1) gates whether tarlatamab via NCT06788938 (rank 2) is on the table at all.** Every DLL3-directed therapy in current clinical use requires IHC protein-level confirmation; RNA expression is necessary but not sufficient.

- **Rank 2 (tarlatamab)** is conditional on DLL3 IHC ≥1% (preferably ≥25%). **Ranks 3 and 4 (regorafenib, cabozantinib)** are biomarker-independent and apply regardless of the IHC result.
- **If IHC is negative:** rank 2 is foreclosed; ranks 3 and 4 remain valid as the 2L+ standard backbone for relapsed osteosarcoma. There is no separate "negative-branch" ranking — the unified ranks below absorb both outcomes.
- **Workup logistics:** SP347 IHC is non-toxic, runs on archival tissue (no fresh biopsy required), takes 1–3 weeks, and costs almost nothing relative to a treatment cycle. Confirm assay availability at the treating institution.

## Intervention grouping

- **DLL3-directed BiTEs (biomarker-conditional):** tarlatamab via NCT06788938. Cross-tumor efficacy anchor: DeLLphi-301 ([PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218)) and DeLLphi-304 ([PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646)).
- **Multi-kinase TKIs (biomarker-independent):** regorafenib ([PMID 31013172](https://pubmed.ncbi.nlm.nih.gov/31013172), [PMID 30477937](https://pubmed.ncbi.nlm.nih.gov/30477937)) and cabozantinib ([PMID 32078813](https://pubmed.ncbi.nlm.nih.gov/32078813)).

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

Strong preference fit + the only DLL3-directed option on the table when the IHC is positive. Ranks above regorafenib *because* the user explicitly prefers trials; without that preference, the agreement_score gap (+0.6 vs +1.0) would invert the order. Foreclosed entirely if IHC negative.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Tarlatamab — NCT06788938 DLL3-IHC-selected basket (osteosarcoma included), n=29 planned | ORR endpoint at 18 mo (primary); no osteosarcoma data yet | Per SCLC mechanism: CRS ~50%, ICANS ~10%, inpatient C1 | [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) |
| Tarlatamab — DeLLphi-301 SCLC (cross-tumor mechanism evidence), n=220 | ORR 40% (95% CI 29–52); mPFS 4.9 mo | CRS ~50% (G3+ ~1%); ICANS ~10%; G3+ TRAEs 30% | [PMID 37861218](https://pubmed.ncbi.nlm.nih.gov/37861218) |
| Tarlatamab — DeLLphi-304 SCLC (cross-tumor confirmatory), n=509 | OS HR 0.60 (95% CI 0.47–0.77), p<0.001; median OS 13.6 vs 8.3 mo | G3+ TRAEs 24% vs 53% chemo arm — favorable vs comparator | [PMID 40454646](https://pubmed.ncbi.nlm.nih.gov/40454646) |

---

### Rank 3. Regorafenib

*Universal-consensus 2L+ backbone. Biomarker-independent — applies whether or not DLL3 IHC confirms.*

#### Evidence base

Two-RCT convergence in 2L+ metastatic osteosarcoma: SARC024 ([PMID 31013172](https://pubmed.ncbi.nlm.nih.gov/31013172); n=42, mPFS 3.6 vs 1.7 mo, HR 0.42 95% CI 0.21–0.85, p=0.017) and the REGOBONE osteosarcoma cohort ([PMID 30477937](https://pubmed.ncbi.nlm.nih.gov/30477937); n=38, 65% non-progression at 8 weeks, mPFS 16.4 vs 4.1 wk). Both placebo-controlled with crossover.

#### Likelihood of desired effect

Strongest 2L+ osteosarcoma evidence base in the dossier. Effect is real but not durable — neither RCT showed an OS benefit (crossover diluted). PFS gains are weeks-to-months. No biomarker dependency.

#### Toxicity profile

- Hand-foot reaction (predominant)
- Hypertension
- Fatigue
- Mucositis, transaminitis
- G3+ AE rate ~70% across the two RCTs; manageable with dose reduction; no treatment-related deaths

User has no toxicity vetoes; oral all-PO regimen aligns with the no-modality-constraints preference.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. No persona dissented or vetoed.

#### Practical considerations

- 160 mg PO daily, 3 weeks on / 1 week off
- NCCN-recommended for relapsed/refractory osteosarcoma
- Off-trial; no enrollment friction
- Outpatient

#### Why this rank

Below tarlatamab in rank order because the user's preferences favor the trial when reachable, but if IHC is negative this becomes the de facto first-line therapeutic. Above cabozantinib because two-RCT evidence beats single-arm phase-2 evidence.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Regorafenib — SARC024 (RCT, n=42 osteosarcoma) | mPFS 3.6 vs 1.7 mo (HR 0.42, p=0.017) | G3+ ~70%: HFS, HTN, fatigue, mucositis | [PMID 31013172](https://pubmed.ncbi.nlm.nih.gov/31013172) |
| Regorafenib — REGOBONE osteosarcoma cohort (RCT, n=38) | 65% non-progression at 8 wk; mPFS 16.4 vs 4.1 wk | G3+ ~76%: HFS, fatigue, HTN, transaminitis | [PMID 30477937](https://pubmed.ncbi.nlm.nih.gov/30477937) |

---

### Rank 4. Cabozantinib

*NCCN alternative; CABONE phase-2 evidence; sequencing option after or instead of regorafenib. Biomarker-independent.*

#### Evidence base

CABONE ([PMID 32078813](https://pubmed.ncbi.nlm.nih.gov/32078813); single-arm phase 2, French Sarcoma Group; osteosarcoma cohort n=42): ORR 11.9% (95% CI 4.0–25.6); 6-mo non-progression 33.3%; mPFS 6.2 mo. Pre-specified osteosarcoma cohort within a multicentre trial.

#### Likelihood of desired effect

Single-arm phase-2; effect smaller than regorafenib's PFS signal but in the same direction. Reasonable backup if regorafenib is contraindicated, intolerable, or prior. No biomarker dependency.

#### Toxicity profile

- Hypertension
- Hand-foot reaction
- Hypophosphatemia
- Transaminitis
- Thromboembolism in 7% (notable)
- G3+ AEs 68%

VTE prophylaxis warranted in patients with metastatic disease.

#### Counter-productive mechanisms / dissent

Board endorsement was unanimous. No persona disputed cabozantinib as a sequencing option.

#### Practical considerations

- 60 mg PO daily
- NCCN-listed alternative for relapsed bone sarcoma
- Outpatient
- AOST2032 ([NCT05691478](https://clinicaltrials.gov/study/NCT05691478)) is testing cabozantinib + MAP in frontline — relevant context but not a 2L+ option for this case

#### Why this rank

Phase-2 single-arm vs regorafenib's two-RCT base — that's the rank gap. Both are universally endorsed and biomarker-independent; cabozantinib is the sequencing alternative.

#### Per-trial detail

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Cabozantinib — CABONE osteosarcoma cohort (single-arm phase 2, n=42) | ORR 11.9% (95% CI 4.0–25.6); 6-mo non-progression 33.3%; mPFS 6.2 mo | G3+ 68%: HTN, HFS, hypophosphatemia; VTE 7% | [PMID 32078813](https://pubmed.ncbi.nlm.nih.gov/32078813) |
| Cabozantinib + MAP — AOST2032 (frontline phase 2/3, recruiting; context only) | Outcome pending | Per cabozantinib + MAP combined toxicity profile | [NCT05691478](https://clinicaltrials.gov/study/NCT05691478) |

## Classes examined but not ranked

- **Anti-PD-1 / PD-L1 monotherapy in osteosarcoma:** historically negative (SARC028 and successors). No persona surfaced this as a candidate.
- **HER2-, GD2-, B7-H3-directed therapies:** not in the dossier for this case; no biomarker selection performed at intake.
- **MTP-PE (mifamurtide):** historical adjuvant data in newly diagnosed disease; not a 2L+ option.
- **Mechanism-agnostic non-DLL3 trial search:** previously surfaced as a Path-B-only option under the prior contract. With the negative-branch ranking dropped, this falls under "consult an academic sarcoma center for fresh trial search" — outside Libby's enumerated scope; not ranked.

## Ranked prioritization

| Rank | Status | Intervention | Endorsed by | Dissent | Veto | Likelihood | Toxicity burden | Why this rank |
|---|---|---|---|---|---|---|---|---|
| 1 | recommended | DLL3 IHC (SP347) | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span> | — | — | Resolves rank 2 reachability | None | Gate; precondition for rank 2 |
| 2 | recommended | Tarlatamab via NCT06788938 (conditional on DLL3 IHC positive) | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-advocate">advocate</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-concensusite">concensusite</span> | <span class="persona persona-critic">critic</span> | — | Mechanism unproven cross-tumor | CRS, ICANS, C1 inpatient | Only DLL3-directed option; preference fit |
| 3 | recommended | Regorafenib | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span> | — | — | Real PFS gain, no OS benefit | HFS, HTN, fatigue (G3+ ~70%) | Two-RCT backbone; biomarker-independent |
| 4 | recommended | Cabozantinib | <span class="persona persona-risktaker">risktaker</span> <span class="persona persona-conservative">conservative</span> <span class="persona persona-critic">critic</span> <span class="persona persona-concensusite">concensusite</span> <span class="persona persona-advocate">advocate</span> | — | — | Smaller phase-2 effect | HTN, HFS, VTE 7% (G3+ ~68%) | Sequencing alternative |

## Caveats

- **Evidence base is small for the conditional trial.** NCT06788938 plans n=29 with no published efficacy data yet. The mechanistic basis is the cross-tumor SCLC evidence (DeLLphi-301 / 304), which is robust in SCLC but unproven in any other tumor type.
- **Single-arm phase-2 is the upper bound for cabozantinib in osteosarcoma** (CABONE). No randomized controlled comparison with regorafenib exists.
- **No OS benefit demonstrated for either TKI** (regorafenib's two RCTs both used crossover designs; cabozantinib was single-arm). The effect lives in PFS, not survival.
- **Biomarker dependency:** rank 2's eligibility assumes a binary IHC result. Indeterminate / weak-positive (1–24%) edge cases are not explicitly addressed; in practice, NCT06788938's stage-2 ≥1% threshold may permit enrollment.
- **What would change the ranking:**
    - A positive DLL3 IHC plus a head-to-head osteosarcoma cohort within the basket trial reading out would move tarlatamab from "mechanism unproven cross-tumor" to "evidence-supported" and tighten its rank-2 confidence.
    - A user toxicity veto on CRS / inpatient cycle-1 monitoring would foreclose tarlatamab even with positive IHC.
    - Slot unavailability at NCT06788938 sites would push the user toward regorafenib as the de facto first-line therapeutic.
- **Re-scoping caveat:** if the user's preference shifts away from trials (toward proven options) or toward minimizing inpatient time, regorafenib effectively becomes rank 2.

## Sources

**PubMed (PMID):**

- [30477937](https://pubmed.ncbi.nlm.nih.gov/30477937) — Duffaud et al., REGOBONE osteosarcoma cohort, *Lancet Oncol* 2019
- [31013172](https://pubmed.ncbi.nlm.nih.gov/31013172) — Davis et al., SARC024, *JCO* 2019
- [32078813](https://pubmed.ncbi.nlm.nih.gov/32078813) — Italiano et al., CABONE, *Lancet Oncol* 2020
- [37861218](https://pubmed.ncbi.nlm.nih.gov/37861218) — Ahn et al., DeLLphi-301, *NEJM* 2023
- [40454646](https://pubmed.ncbi.nlm.nih.gov/40454646) — Mountzios et al., DeLLphi-304, *NEJM* 2025
- [35983951](https://pubmed.ncbi.nlm.nih.gov/35983951) — DLL3 IHC reference (cited in workup row)

**ClinicalTrials.gov (NCT):**

- [NCT06788938](https://clinicaltrials.gov/study/NCT06788938) — DLL3-IHC-selected basket including osteosarcoma (tarlatamab)
- [NCT05691478](https://clinicaltrials.gov/study/NCT05691478) — AOST2032 frontline osteosarcoma (cabozantinib + MAP); context only
- [NCT05060016](https://clinicaltrials.gov/study/NCT05060016) — DeLLphi-301 (cross-tumor mechanism)
- [NCT05740566](https://clinicaltrials.gov/study/NCT05740566) — DeLLphi-304 (cross-tumor confirmatory)
- [NCT02243605](https://clinicaltrials.gov/study/NCT02243605) — CABONE
- [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) — SARC024
- [NCT02389244](https://clinicaltrials.gov/study/NCT02389244) — REGOBONE

## Transparency artifacts

- [Trial table](trials.md) — 7 rows, all 25 columns
- [Evidence list](evidence.md) — 5 clinical-evidence rows + 4 preclinical rows
- [Tumor-board transcript](board.md) — 5 positions, 20 cross-critiques
- [Recommendations table](recommendations.md) — full ranked detail with biomarker-conditional flag
- [Plain-language summary](plain_language.md) — patient/caregiver track

## Run log

Authored May 2026. Inputs supplied: targetable feature ("DLL3 RNA expression"), clinical descriptor ("metastatic osteosarcoma"), preference summary ("accepts high-risk high-reward options"). Re-rendered when Libby's biomarker-confirmation contract narrowed: instead of emitting parallel positive/negative therapeutic rankings, the PI now flags the confirmatory test as the rank-1 workup and tags only biomarker-conditional recs with `:positive`. Negative-branch ranking is foreclosed via the cross-cutting caveat above, not enumerated as a separate Path B.

!!! danger disclaimer "Decision support, not medical advice"
    Libby is an experimental decision-support tool. The recommendations on
    this page have not been reviewed by a clinician treating this patient.
    Do not act on this page without consulting a qualified oncologist.
